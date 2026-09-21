"""Optional browser regression checks; install requirements-qa.txt to run."""
import importlib.util
import unittest

from build.preview import CHROME


@unittest.skipUnless(CHROME and importlib.util.find_spec('playwright'), 'QA browser dependencies absent')
class RenderCheckerTests(unittest.TestCase):
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
