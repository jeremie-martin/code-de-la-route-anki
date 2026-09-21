import copy
import unittest
from unittest.mock import patch

from build.build import curriculum, load_all, validate, inline_md
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
        data['questions'] = [n for n in data['questions'] if n['id'] != 'c-arret-somme']
        self.assertTrue(any('c-arret-somme' in error for error in validate(data)))

    def test_fronts_do_not_supply_topic_or_answer_fields(self):
        for nt in notetypes():
            for template in nt['templates']:
                self.assertNotIn('{{SousTheme}}', template['qfmt'])
                for answer in ('Reponse', 'Verdict', 'Pourquoi', 'Signification', 'Nom'):
                    self.assertNotIn('{{' + answer + '}}', template['qfmt'])

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
        spec['agent'] = 'bras_tendus_NS'
        self.assertEqual(passes_before(spec, 'S', 'E'), 'apres')

    def test_flashing_amber_is_not_a_fixed_stop_light(self):
        spec = {'approaches': {
            'S': {'vehicle': {'colour': 'bleu'}, 'sign': 'feu_orange_clignotant'},
            'E': {'vehicle': {'colour': 'rouge'}, 'sign': 'feu_orange_clignotant'},
        }}
        self.assertEqual(passes_before(spec, 'S', 'E'), 'apres')
        for approach in spec['approaches'].values():
            approach['sign'] = 'feu_orange'
        self.assertEqual(passes_before(spec, 'S', 'E'), 'indetermine')

    def test_sources_clickable_and_text_escaped(self):
        value = inline_md('Source https://example.org/article?a=1&b=2 <script>')
        self.assertIn('href="https://example.org/article?a=1&amp;b=2"', value)
        self.assertNotIn('<script>', value)


if __name__ == '__main__':
    unittest.main()
