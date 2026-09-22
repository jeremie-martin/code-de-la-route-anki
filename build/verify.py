"""Verify the distributable package in a disposable Anki collection.

python -m build.verify
Tests a fresh import (content, media, study order, options preset) and a reimport of the same
edition (no duplicate, review history kept), without touching a user's collection.
Use --previous old.apkg to also verify an upgrade from an earlier package.
"""
from __future__ import annotations

import argparse
import hashlib
from importlib.metadata import version
from pathlib import Path
import re
import tempfile

from anki.collection import Collection
from anki.import_export_pb2 import ImportAnkiPackageRequest, ImportAnkiPackageOptions
from anki.scheduler.v3 import CardAnswer

from build.build import OUT, load_all, curriculum, inline_md, tags_for, fait_html, feedback_html, media_name
from build.learning import card_count, card_plan
from build.models import MODEL_IDS, DECK_ROOT, notetypes, CSS, SCHEMA_IDS


def import_package(col, path, *, with_deck_configs=True):
    result = col.import_anki_package(ImportAnkiPackageRequest(
        package_path=str(path.resolve()),
        options=ImportAnkiPackageOptions(with_deck_configs=with_deck_configs),
    ))
    # The backend import can replace note types already cached by the Python API.
    col.models._clear_cache()
    assert not result.log.conflicting, f'{len(result.log.conflicting)} notes en conflit : {path}'


def verify_content(col, data, removed=frozenset()):
    """The collection holds exactly the notes of `data`, rendered from it; `removed` names notes of an earlier
    edition that an update leaves in place (they are left out of the checks)."""
    expected = {n['id']: n for notes in data.values() for n in notes}
    notes = {nid: col.get_note(nid) for nid in col.find_notes('')}
    notes = {nid: n for nid, n in notes.items() if n['Id'] not in removed}
    assert len(notes) == len(expected), (len(notes), len(expected))
    assert sum(len(n.cards()) for n in notes.values()) == sum(card_count(n) for n in expected.values())
    assert {m['id'] for m in col.models.all() if m['name'] in MODEL_IDS} == set(MODEL_IDS.values())
    assert {n['Id'] for n in notes.values()} == set(expected)
    names = {n['id']: media_name('img', n['id']) for n in data['reconnaissance']}
    names.update({n['id'] + ':illustration': media_name('exp', n['id'])
                  for kind in ('faits', 'questions', 'affirmations') for n in data[kind] if n.get('illustration')})
    feedback_fields = {'reconnaissance': 'Piege', 'confusions': 'Difference',
                       'faits': 'Explication', 'questions': 'Explication',
                       'affirmations': 'Pourquoi', 'scenarios': 'Explication'}
    text_fields = {'Source': 'source', 'Texte': 'texte', 'Question': 'question',
                   'Reponse': 'reponse', 'Explication': 'explication', 'Contexte': 'contexte',
                   'Affirmation': 'affirmation', 'Pourquoi': 'pourquoi', 'Nom': 'nom',
                   'Signification': 'signification', 'ConduiteATenir': 'conduite',
                   'Complement': 'complement', 'Piege': 'piege', 'Difference': 'difference'}
    for note in notes.values():
        original = expected[note['Id']]
        for field, key in text_fields.items():
            is_feedback = field == feedback_fields[original['_kind']]
            if field in note and (key in original or is_feedback):
                if is_feedback:
                    value = feedback_html(original, key, names)
                else:
                    value = fait_html(original) if field == 'Texte' else inline_md(original[key])
                assert note[field] == value, f"{note['Id']} : {field} périmé"
        if 'Verdict' in note:
            assert note['Verdict'] == original['verdict']
        assert set(tags_for(original, original['_kind'])).issubset(note.tags)
    for expected_model in notetypes():
        model = col.models.by_name(expected_model['name'])
        assert model['css'] == CSS
        assert {f['name']: f['id'] for f in model['flds']} == SCHEMA_IDS[model['name']]['fields']
        assert {t['name']: t['id'] for t in model['tmpls']} == SCHEMA_IDS[model['name']]['templates']
        for actual, template in zip(model['tmpls'], expected_model['templates'], strict=True):
            assert actual['qfmt'] == template['qfmt'] and actual['afmt'] == template['afmt']
    missing = []
    for cid in col.find_cards(''):
        card = col.get_card(cid)
        if card.nid not in notes:
            continue
        for rendered in (card.question(), card.answer()):
            assert 'Invalid HTML' not in rendered and 'No cloze' not in rendered, notes[card.nid]['Id']
            for media in re.findall(r'<img src="([^"]+)"', rendered):
                if not (Path(col.media.dir()) / media).is_file():
                    missing.append(media)
        if expected[notes[card.nid]['Id']].get('comparaisons'):
            assert 'class="cdr-comparisons"' not in card.question()
            assert 'class="cdr-comparisons"' in card.answer()
        if expected[notes[card.nid]['Id']].get('illustration'):
            assert 'class="cdr-illustration' not in card.question()
            assert 'class="cdr-illustration' in card.answer()
    assert not missing, missing


def verify_new_order(col, data):
    assert col.db.scalar('select count(*) from revlog') == 0, 'historique exporté'
    for cid in col.find_cards(''):
        card = col.get_card(cid)
        assert (card.type, card.queue, card.reps, card.lapses, card.ivl) == (0, 0, 0, 0, 0)
        assert card.memory_state is None, 'état mémoire FSRS exporté'
    expected = card_plan(data, curriculum(data))
    actual = []
    for cid in col.db.list('select id from cards order by due, id'):
        card = col.get_card(cid)
        note = card.note()
        kind = next(t.removeprefix('type::') for t in note.tags
                    if t.removeprefix('type::') in data)
        actual.append((kind, note['Id'], card.ord))
    assert actual == expected, 'ordre du paquet importé différent du programme'
    config = col.decks.config_dict_for_deck_id(col.decks.id(DECK_ROOT))
    assert config['newGatherPriority'] == 1 and config['newSortOrder'] == 1
    assert config['new']['bury'] and config['rev']['bury']
    assert config['buryInterdayLearning']
    assert config['rev']['perDay'] >= col.card_count()


def verify_fsrs(col, path):
    """Exercise the native scheduler and an update with learner-owned settings."""
    did = col.decks.id(DECK_ROOT)
    config = col.decks.config_dict_for_deck_id(did)
    config['desiredRetention'] = 0.91
    config['new']['perDay'] = 7
    col.decks.update_config(config)
    config = col.decks.config_dict_for_deck_id(did)
    col.set_config('fsrs', True)
    col.decks.select(did)
    queued = col.sched.get_queued_cards(fetch_limit=7)
    expected = col.db.list('select id from cards order by due, id limit 7')
    assert [q.card.id for q in queued.cards] == expected, 'collecte réelle hors programme'
    reviewed = []
    for rating in (CardAnswer.EASY, CardAnswer.AGAIN):
        q = col.sched.get_queued_cards().cards[0]
        card = col.get_card(q.card.id)
        card.start_timer()
        col.sched.answer_card(col.sched.build_answer(card=card, states=q.states, rating=rating))
        card.load()
        assert card.memory_state is not None and card.memory_state.stability > 0
        assert card.type == (2 if rating == CardAnswer.EASY else 1)
        reviewed.append((card.id, card.due, card.ivl, card.memory_state))
    history = col.db.all('select * from revlog order by id')
    import_package(col, path, with_deck_configs=False)
    actual = col.decks.config_dict_for_deck_id(did)
    assert actual == config, 'préréglage personnel modifié malgré import désactivé'
    assert col.get_config('fsrs') is True
    assert col.db.all('select * from revlog order by id') == history
    for cid, due, ivl, memory in reviewed:
        card = col.get_card(cid)
        assert (card.due, card.ivl, card.memory_state) == (due, ivl, memory)


def mark_reviewed(col):
    cid = col.find_cards('Id:l-vitesse-probatoire')[0]
    card = col.get_card(cid)
    card.type, card.queue, card.ivl, card.due = 2, 2, 31, 500
    card.reps, card.lapses = 7, 2
    col.update_card(card)
    # An actual revlog row, so this checks retained history as well as scheduling.
    col.db.execute('insert into revlog values (?,?,?,?,?,?,?,?,?)',
                   1750000000000, cid, -1, 3, 31, 15, 2500, 4000, 1)
    return cid, (card.nid, card.ord, card.ivl, card.due, card.reps, card.lapses)


def assert_history(col, cid, before):
    card = col.get_card(cid)
    assert (card.nid, card.ord, card.ivl, card.due, card.reps, card.lapses) == before
    assert col.db.scalar('select count(*) from revlog where cid=?', cid) == 1
    assert '{{c2::100 km/h}}' in card.note()['Texte'], 'contenu de la note absent après réimport'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, help='vérifier aussi la mise à jour de ce paquet antérieur')
    args = parser.parse_args(argv)
    data = load_all()
    full_path = OUT / 'Code-de-la-route-2026.apkg'
    checks = []
    with tempfile.TemporaryDirectory(prefix='cdr-verify-') as tmp:
        col = Collection(str(Path(tmp) / 'complet.anki2'))
        try:
            import_package(col, full_path)
            verify_content(col, data)
            verify_new_order(col, data)
            checks.append(f'import neuf : {col.note_count()} notes, {col.card_count()} cartes ; rendu, médias, ordre et options OK')
            verify_fsrs(col, full_path)
            checks.append('paquet vierge : toutes les cartes nouvelles, aucun historique ni état mémoire ; '
                          'FSRS natif : collecte des 7 premières cartes dans l’ordre, réponses Facile/À revoir ; '
                          'réimport sans préréglages : options personnelles, FSRS, états mémoire et historique conservés')
            cid, before = mark_reviewed(col)
            import_package(col, full_path)
            verify_content(col, data)
            assert_history(col, cid, before)
            checks.append('réimport de la même édition : aucun doublon ; historique et planification conservés')
        finally:
            col.close()
        if args.previous:
            col = Collection(str(Path(tmp) / 'mise-a-jour.anki2'))
            try:
                import_package(col, args.previous)
                note_ids = {n.guid: n.id for n in (col.get_note(nid) for nid in col.find_notes(''))}
                card_ids = {(col.get_note(c.nid).guid, c.ord): c.id
                            for c in (col.get_card(cid) for cid in col.find_cards(''))}
                cid, before = mark_reviewed(col)
                import_package(col, full_path)
                current = {n['id'] for notes in data.values() for n in notes}
                removed = {col.get_note(nid)['Id'] for nid in col.find_notes('')} - current
                verify_content(col, data, removed)
                assert_history(col, cid, before)
                for nid in col.find_notes(''):
                    n = col.get_note(nid)
                    if n.guid in note_ids:
                        assert n.id == note_ids[n.guid], 'identité de note modifiée'
                    for card in n.cards():
                        key = (n.guid, card.ord)
                        if key in card_ids:
                            assert card.id == card_ids[key], 'identité de carte modifiée'
                previous_hash = hashlib.sha256(args.previous.read_bytes()).hexdigest()
                checks.append(f'mise à jour depuis SHA-256 `{previous_hash}` : identités des notes/cartes '
                              'conservées, aucun doublon ; historique et planification du témoin conservés'
                              + (f' ; notes retirées depuis, restées dans la collection : {", ".join(sorted(removed))}'
                                 if removed else ''))
            finally:
                col.close()
    fingerprint = hashlib.sha256(full_path.read_bytes()).hexdigest()
    (OUT / 'VERIFICATION.md').write_text('# Vérification du paquet\n\n' +
        f'Import réel en collection temporaire avec la bibliothèque Anki {version("anki")}.\n\n' +
        '\n'.join('- ' + line for line in checks) + f'\n\nSHA-256 du paquet vérifié : `{fingerprint}`\n\n'
        'Ces contrôles ne valident ni la justesse de chaque phrase ni la réussite à l’examen. '
        'Voir aussi [le rendu navigateur](RENDU.md).\n')
    print('\n'.join(checks))


if __name__ == '__main__':
    main()
