"""Verify distributable packages in disposable Anki collections.

python -m build.verify [--previous /path/to/previous.apkg]
Tests both fresh imports and upgrades, without accessing a user's collection.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import tempfile

from anki.collection import Collection
from anki.import_export_pb2 import ImportAnkiPackageRequest, ImportAnkiPackageOptions

from build.build import OUT, load_all, curriculum, inline_md, tags_for
from build.learning import card_count, card_plan
from build.models import MODEL_IDS, DECK_ROOT, notetypes, CSS


def import_package(col, path):
    result = col.import_anki_package(ImportAnkiPackageRequest(
        package_path=str(path.resolve()),
        options=ImportAnkiPackageOptions(with_deck_configs=True),
    ))
    assert not result.log.conflicting, f'{len(result.log.conflicting)} notes en conflit : {path}'


def verify_content(col, data):
    expected = {n['id']: n for notes in data.values() for n in notes}
    assert col.note_count() == len(expected), (col.note_count(), len(expected))
    assert col.card_count() == sum(card_count(n) for n in expected.values())
    assert {m['id'] for m in col.models.all() if m['name'] in MODEL_IDS} == set(MODEL_IDS.values())
    notes = {nid: col.get_note(nid) for nid in col.find_notes('')}
    assert {n['Id'] for n in notes.values()} == set(expected)
    text_fields = {'Source': 'source', 'Texte': 'texte', 'Question': 'question',
                   'Reponse': 'reponse', 'Explication': 'explication', 'Contexte': 'contexte',
                   'Affirmation': 'affirmation', 'Pourquoi': 'pourquoi', 'Nom': 'nom',
                   'Signification': 'signification', 'ConduiteATenir': 'conduite',
                   'Complement': 'complement', 'Piege': 'piege', 'Difference': 'difference'}
    for note in notes.values():
        original = expected[note['Id']]
        for field, key in text_fields.items():
            if field in note and key in original:
                assert note[field] == inline_md(original[key]), f"{note['Id']} : {field} périmé"
        if 'Verdict' in note:
            assert note['Verdict'] == original['verdict']
        assert set(tags_for(original, original['_kind'])).issubset(note.tags)
    for expected_model in notetypes():
        model = col.models.by_name(expected_model['name'])
        assert model['css'] == CSS
        for actual, template in zip(model['tmpls'], expected_model['templates'], strict=True):
            assert actual['qfmt'] == template['qfmt'] and actual['afmt'] == template['afmt']
    missing = []
    for cid in col.find_cards(''):
        card = col.get_card(cid)
        for rendered in (card.question(), card.answer()):
            assert 'Invalid HTML' not in rendered and 'No cloze' not in rendered, notes[card.nid]['Id']
            for media in re.findall(r'<img src="([^"]+)"', rendered):
                if not (Path(col.media.dir()) / media).is_file():
                    missing.append(media)
    assert not missing, missing


def verify_new_order(col, data):
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
    assert 'normalement à 110' in card.note()['Texte'], 'correction non importée'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path)
    args = parser.parse_args()
    data = load_all()
    core = {kind: [n for n in notes if n['_stage'] == 'socle'] for kind, notes in data.items()}
    full_path, core_path = OUT / 'Code-de-la-route-2026.apkg', OUT / 'Code-de-la-route-2026-Socle.apkg'
    checks = []
    with tempfile.TemporaryDirectory(prefix='cdr-verify-') as tmp:
        for name, subset, path in [('socle', core, core_path), ('complet', data, full_path)]:
            col = Collection(str(Path(tmp) / f'{name}.anki2'))
            try:
                import_package(col, path)
                verify_content(col, subset)
                verify_new_order(col, subset)
                checks.append(f'{name} : {col.note_count()} notes, {col.card_count()} cartes ; rendu, médias, ordre et options OK')
                if name == 'socle':
                    cid, before = mark_reviewed(col)
                    import_package(col, full_path)
                    verify_content(col, data)
                    assert_history(col, cid, before)
                    import_package(col, full_path)
                    verify_content(col, data)
                    assert_history(col, cid, before)
                    checks.append('socle → complet → réimport : aucun doublon ; historique et planification conservés')
            finally:
                col.close()
        if args.previous:
            col = Collection(str(Path(tmp) / 'upgrade.anki2'))
            try:
                import_package(col, args.previous)
                cid, before = mark_reviewed(col)
                import_package(col, full_path)
                verify_content(col, data)
                assert_history(col, cid, before)
                checks.append('ancien paquet → complet : correction appliquée ; historique et planification conservés')
            finally:
                col.close()
    (OUT / 'VERIFICATION.md').write_text('# Vérification des paquets\n\n' +
        '\n'.join('- ' + line for line in checks) + '\n\nCes contrôles ne valident pas la justesse juridique de chaque phrase ni la réussite à l’examen.\n')
    print('\n'.join(checks))


if __name__ == '__main__':
    main()
