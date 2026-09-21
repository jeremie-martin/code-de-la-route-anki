import copy
import re
import tempfile
import unittest
from unittest.mock import patch

from build.build import curriculum, load_all, validate, lint, inline_md, fait_html
from build.learning import card_plan, objectives, annotate, validate_objectives
from build.priority import passes_before
from build.models import notetypes


class LearningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_all()

    def test_library_and_objectives_are_valid(self):
        self.assertEqual(validate(self.data), [])

    def test_no_extension_card_interrupts_foundation(self):
        plan = card_plan(self.data, curriculum(self.data))
        notes = {n['id']: n for ns in self.data.values() for n in ns}
        stages = [notes[i]['_stage'] for _, i, _ in plan]
        first_extension = stages.index('approfondissement')
        self.assertGreater(first_extension, 0)
        self.assertNotIn('socle', stages[first_extension:])
        self.assertEqual(len(plan), len(set(plan)))
        self.assertEqual({notes[i]['theme'] for _, i, _ in plan[:first_extension]}, set('XLCRUDAPMSE'))

    def test_every_note_has_an_explicit_learning_objective(self):
        for notes in self.data.values():
            for n in notes:
                self.assertTrue(n['_objectives'], n['id'])
        data = copy.deepcopy(self.data)
        orphan = copy.deepcopy(data['questions'][0])
        orphan['id'] = 'test-unassigned-note'
        data['questions'].append(orphan)
        annotate(data)
        self.assertTrue(any('test-unassigned-note' in e for e in validate_objectives(data)))

    def test_foundation_has_no_numerical_ceiling(self):
        data = copy.deepcopy(self.data)
        manifest = copy.deepcopy(objectives())
        for index in range(700):
            note = copy.deepcopy(data['questions'][0])
            note['id'] = f'test-additional-purpose-{index}'
            data['questions'].append(note)
            manifest[0]['notes'].append(note['id'])
        with patch('build.learning.objectives', return_value=manifest):
            annotate(data)
            self.assertEqual(validate_objectives(data), [])

    def test_pairs_require_both_images_first(self):
        plan = card_plan(self.data, curriculum(self.data))
        positions = {ident: pos for pos, (_, ident, _) in enumerate(plan)}
        for n in self.data['confusions']:
            for member in ('a', 'b'):
                self.assertLess(positions[n[member]], positions[n['id']], n['id'])

    def test_typo_in_coverage_cannot_silently_drop_a_competence(self):
        data = copy.deepcopy(self.data)
        data['questions'] = [n for n in data['questions'] if n['id'] != 'l-priorite-droite-defaut']
        self.assertTrue(any('l-priorite-droite-defaut' in error for error in validate(data)))

    def test_fronts_do_not_supply_topic_or_answer_fields(self):
        for nt in notetypes():
            for template in nt['templates']:
                self.assertNotIn('{{SousTheme}}', template['qfmt'])
                for answer in ('Reponse', 'Verdict', 'Pourquoi', 'Signification', 'Nom'):
                    self.assertNotIn('{{' + answer + '}}', template['qfmt'])

    def test_visual_applications_follow_their_recognition(self):
        plan = card_plan(self.data, curriculum(self.data))
        positions = {ident: pos for pos, (_, ident, _) in enumerate(plan)}
        recon = {n['id']: n for n in self.data['reconnaissance']}
        for note in self.data['questions']:
            if note.get('image_ref'):
                self.assertEqual(note['image'], recon[note['image_ref']]['image'])
                self.assertLess(positions[note['image_ref']], positions[note['id']])

    def test_a_prompt_cannot_mix_or_repeat_sibling_targets(self):
        for invalid in (["A {{c1::x}} et B {{c2::y}}"],
                        ["A {{c1::x}}", "B {{c1::y}}"], ["Texte sans trou"]):
            data = copy.deepcopy(self.data)
            data['faits'][0]['rappels'] = invalid
            self.assertTrue(any('chaque rappel' in e for e in validate(data)))

    def test_editorial_limits_warn_but_never_fail_the_build(self):
        data = copy.deepcopy(self.data)
        sheet = copy.deepcopy(next(n for n in data['faits'] if 'rappels' not in n))
        sheet['id'], sheet['texte'] = 'test-sheet', 'A {{c1::1}} et B {{c2::2}}.'
        recitation = copy.deepcopy(sheet)
        recitation['id'], recitation['texte'] = 'test-recitation', 'Règle : {{c1::une phrase entière de neuf mots à réciter sans faute}}.'
        data['faits'] += [sheet, recitation]
        self.assertFalse([e for e in validate(data) if 'test-' in e and 'objectif' not in e])
        warnings = lint(data)
        self.assertTrue(any('test-sheet' in w and 'trous' in w for w in warnings), warnings)
        self.assertTrue(any('test-recitation' in w and 'réciter' in w for w in warnings), warnings)
        sheet['multi_ok'] = True
        recitation['long_ok'] = True
        self.assertFalse([w for w in lint(data) if 'test-' in w])

    def test_style_tells_are_reported(self):
        data = copy.deepcopy(self.data)
        for index in range(6):
            note = copy.deepcopy(data['affirmations'][0])
            note.update(id=f'test-tell-{index}', affirmation=f'Je m\'arrête, attendu que la règle {index} l\'impose.', verdict='faux')
            data['affirmations'].append(note)
        with patch('build.build.STYLE_MARKERS', ['attendu que']):
            self.assertTrue(any('attendu que' in w for w in lint(data)))

    def test_independent_prompts_render_with_native_anki_conditionals(self):
        from anki.collection import Collection
        from anki.consts import MODEL_CLOZE
        from lxml import html
        model = next(m for m in notetypes() if m['name'] == 'CDR Fait')
        with tempfile.TemporaryDirectory() as tmp:
            col = Collection(tmp + '/clozes.anki2')
            try:
                m = col.models.new('CDR Fait')
                m['type'] = MODEL_CLOZE
                for name in model['fields']:
                    col.models.add_field(m, col.models.new_field(name))
                template = col.models.new_template('Cloze')
                template.update(model['templates'][0])
                col.models.add_template(m, template)
                col.models.add(m)
                for original in self.data['faits']:
                    if 'rappels' not in original:
                        continue
                    note = col.new_note(m)
                    note['Texte'] = fait_html(original)
                    col.add_note(note, 1)
                    cards = note.cards()
                    self.assertEqual(len(cards), len(original['rappels']), original['id'])
                    for card in cards:
                        for face in (card.question(), card.answer()):
                            # The selected ordinal is produced by Anki, not JS or our parser.
                            target = re.search(r'\.cdr-unit\[data-cloze="(\d+)"\]', face)[1]
                            self.assertEqual(int(target), card.ord + 1)
                            tree = html.fromstring(face)
                            shown = tree.xpath(f'//div[@class="cdr-unit"][@data-cloze="{target}"]')
                            self.assertEqual(len(shown), 1, original['id'])
                            self.assertTrue(shown[0].xpath('.//span[@class="cloze"]'))
                            self.assertFalse(shown[0].xpath('.//span[@class="cloze-inactive"]'))
            finally:
                col.close()

    def test_opposite_turn_changes_priority(self):
        spec = {'approaches': {
            'S': {'vehicle': {'colour': 'bleu'}, 'goes': 'left'},
            'N': {'vehicle': {'colour': 'rouge'}, 'goes': 'straight'},
        }}
        self.assertEqual(passes_before(spec, 'S', 'N'), 'apres')
        spec['approaches']['S']['goes'] = 'straight'
        spec['approaches']['N']['goes'] = 'left'
        self.assertEqual(passes_before(spec, 'S', 'N'), 'avant')

    def test_emergency_appearance_does_not_override_agent(self):
        spec = {'approaches': {
            'S': {'vehicle': {'kind': 'pompiers'}, 'goes': 'straight'},
            'E': {'vehicle': {'colour': 'rouge'}, 'goes': 'straight'},
        }}
        self.assertEqual(passes_before(spec, 'S', 'E'), 'apres')
        spec['approaches']['S']['vehicle']['siren'] = True
        self.assertEqual(passes_before(spec, 'S', 'E'), 'avant')
        spec['agent'] = 'bras_tendus_EW'  # arms across the S vehicle's path: it faces the agent and stops
        self.assertEqual(passes_before(spec, 'S', 'E'), 'apres')
        spec['agent'] = 'bras_tendus_NS'  # arms along its path: it sees the profile and passes
        self.assertEqual(passes_before(spec, 'S', 'E'), 'avant')

    def test_flashing_amber_is_not_a_fixed_stop_light(self):
        spec = {'approaches': {
            'S': {'vehicle': {'colour': 'bleu'}, 'sign': 'feu_orange_clignotant'},
            'E': {'vehicle': {'colour': 'rouge'}, 'sign': 'feu_orange_clignotant'},
        }}
        self.assertEqual(passes_before(spec, 'S', 'E'), 'apres')
        for approach in spec['approaches'].values():
            approach['sign'] = 'feu_orange'
        self.assertEqual(passes_before(spec, 'S', 'E'), 'indetermine')

    def test_french_punctuation_stays_with_the_preceding_word(self):
        self.assertEqual(inline_md("Qui passe ? Non : je cède ; pourquoi !"),
                         "Qui passe\u202f? Non\u202f: je cède\u202f; pourquoi\u202f!")
        self.assertIn("{{c1::30 km/h}}", inline_md("Plafond : {{c1::30 km/h}}."))

    def test_sources_clickable_and_text_escaped(self):
        value = inline_md('Source https://example.org/article?a=1&b=2 <script>')
        self.assertIn('href="https://example.org/article?a=1&amp;b=2"', value)
        self.assertNotIn('<script>', value)


if __name__ == '__main__':
    unittest.main()
