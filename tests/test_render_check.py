"""Optional browser regression checks; install requirements-qa.txt to run."""
import importlib.util
import unittest

from build.preview import CHROME


@unittest.skipUnless(CHROME and importlib.util.find_spec('playwright'), 'QA browser dependencies absent')
class RenderCheckerTests(unittest.TestCase):
    def test_screenshot_samples_reference_existing_notes(self):
        from build.build import load_all
        from build.render_check import SAMPLES
        ids = {n['id'] for notes in load_all().values() for n in notes}
        self.assertFalse(SAMPLES - ids, f'Stale screenshot samples: {SAMPLES - ids}')

    def test_distinguishes_plain_cloze_from_hidden_units_and_finds_bad_layout(self):
        from playwright.sync_api import sync_playwright
        from build.render_check import MEASURE, page_html
        from build.models import CSS

        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
            try:
                page = browser.new_page(viewport={'width': 320, 'height': 640})
                page.set_content(page_html('<div class="cloze">[...]</div>', CSS))
                m = page.evaluate(MEASURE)
                self.assertEqual((m['totalUnits'], m['units'], m['clozes']), (0, 0, 1))
                self.assertFalse(m['overflow'])
                page.set_content(page_html(
                    '<div class="cdr-unit">Question</div>'
                    '<div class="cdr-unit" style="display:none">Sibling answer</div>', CSS))
                m = page.evaluate(MEASURE)
                self.assertEqual((m['totalUnits'], m['units']), (2, 1))
                self.assertNotIn('Sibling answer', m['text'])
                page.set_content(page_html(
                    '<div style="width:2000px">Overflow</div><img src="data:image/png;base64,aW52YWxpZA==">', CSS))
                m = page.evaluate(MEASURE)
                self.assertTrue(m['overflow'])
                self.assertEqual(len(m['broken']), 1)
                from build.gen_images import tableau_lecture
                page.set_content(tableau_lecture({
                    'title': 'Pressions à froid (bar)', 'columns': ['Charge', 'Avant', 'Arrière'],
                    'rows': [['Pleine charge', '2,4', '2,6']],
                }))
                clipped = page.evaluate('''() => [...document.querySelectorAll('rect')]
                    .filter(r => r.getAttribute('width') === '180')
                    .filter(r => {
                        const t = r.nextElementSibling.getBBox(), box = r.getBBox();
                        return t.x < box.x + 3 || t.x + t.width > box.x + box.width - 3;
                    }).length''')
                self.assertEqual(clipped, 0, 'Libellé rogné dans une cellule du tableau')
            finally:
                browser.close()

    def test_reference_disclosure_keeps_feedback_visible_and_works_with_keyboard(self):
        import tempfile
        from anki.collection import Collection
        from anki.consts import MODEL_CLOZE
        from playwright.sync_api import sync_playwright
        from build.models import CSS, notetypes
        from build.render_check import MEASURE, page_html

        with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
            col = Collection(tmp + '/interface.anki2')
            browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
            try:
                page = browser.new_page(viewport={'width': 430, 'height': 740})
                for model in notetypes():
                    m = col.models.new(model['name'])
                    if model.get('cloze'):
                        m['type'] = MODEL_CLOZE
                    for field in model['fields']:
                        col.models.add_field(m, col.models.new_field(field))
                    t = col.models.new_template('Test')
                    t.update(model['templates'][0])
                    col.models.add_template(m, t)
                    col.models.add(m)
                    n = col.new_note(m)
                    for field in model['fields']:
                        n[field] = field + ' témoin'
                    for field in ('Image', 'ImageA', 'ImageB'):
                        if field in n:
                            n[field] = '<span>Image témoin</span>'
                    if 'Texte' in n:
                        n['Texte'] = 'Seuil : {{c1::réponse}}.'
                    if 'Verdict' in n:
                        n['Verdict'] = 'faux'
                    col.add_note(n, 1)
                    card = n.cards()[0]
                    page.set_content(page_html(card.question(), CSS))
                    self.assertNotIn('Source témoin', page.evaluate(MEASURE)['text'])
                    page.set_content(page_html(card.question(), CSS, night=True))
                    front = page.evaluate(MEASURE)['front']
                    page.set_content(page_html(card.answer(), CSS, night=True))
                    self.assertEqual(page.evaluate(MEASURE)['front'], front, model['name'])
                    text = page.evaluate(MEASURE)['text']
                    self.assertNotIn('Source témoin', text)
                    for field in ('Reponse', 'Explication', 'Pourquoi', 'Signification',
                                  'ConduiteATenir', 'Complement', 'Piege', 'Difference'):
                        if field in n:
                            self.assertIn(field + ' témoin', text, (model['name'], field))
                    summary = page.locator('summary')
                    self.assertGreaterEqual(summary.bounding_box()['height'], 44)
                    summary.focus()
                    page.keyboard.press('Enter')
                    self.assertIn('Source témoin', page.evaluate(MEASURE)['text'])
                    page.keyboard.press('Space')
                    self.assertNotIn('Source témoin', page.evaluate(MEASURE)['text'])
            finally:
                browser.close()
                col.close()
