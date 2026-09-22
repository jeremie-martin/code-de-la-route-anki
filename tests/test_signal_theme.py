"""The handoff is a visual fixture, never a source for production note content."""
import importlib.util
import json
from pathlib import Path
import unittest

from build.models import CSS
from build.preview import CHROME
from build.render_check import MEASURE, page_html

HANDOFF = Path(__file__).resolve().parents[1] / 'docs/signal-theme-handoff'
# Compare observable layout and typography, not the lab's redundant cascade.
SNAPSHOT = """() => [...document.querySelectorAll(
  '.card, .cdr-wrap, .cdr-img, .cdr-img img, .cdr-pair, .cdr-pair img, .cdr-side, '
  + '.cdr-q, .cdr-aff, .cdr-ctx, .cdr-hint, .cdr-fait, .cloze, .cdr-a, .cdr-verdict, '
  + '.cdr-box, .cdr-box b, hr, .cdr-reference, summary, .cdr-comparisons, figure, figcaption')]
  .filter(e => e.getClientRects().length > 0).map(e => {
    const r = e.getBoundingClientRect(), s = getComputedStyle(e);
    return {tag: e.tagName, cls: e.className,
      rect: [r.x, r.y, r.width, r.height],
      style: [s.fontFamily, s.fontSize, s.fontWeight, s.lineHeight, s.letterSpacing,
        s.color, s.backgroundColor, s.padding, s.margin, s.borderWidth,
        s.textDecorationLine, s.textDecorationThickness, s.textUnderlineOffset]};
  })"""


@unittest.skipUnless(CHROME and importlib.util.find_spec('playwright'), 'QA browser dependencies absent')
class SignalThemeTests(unittest.TestCase):
    def test_approved_rendering_and_independent_night_aliases(self):
        from playwright.sync_api import sync_playwright
        # The only intended differences from the export: structural helpers and readable A/B labels.
        reference = (HANDOFF / 'signal.css').read_text() + '''
.cdr-reference h3 { font-size:16px; margin:16px 0 8px; }
.cdr-code { font-family:ui-monospace, Menlo, Consolas, monospace; }
ul.cdr-list { padding-left:24px; }
.nightMode .cdr-side { color:#bdc8c2; }
'''
        samples = json.loads((HANDOFF / 'samples.json').read_text())
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
            try:
                page = browser.new_page()
                page.goto((HANDOFF / 'preview.html').as_uri())
                for width in (320, 390, 430):
                    page.set_viewport_size({'width': width, 'height': 932})
                    for sample in samples:
                        for face in ('front', 'back'):
                            body = sample[face].replace('src="assets/', f'src="{HANDOFF.as_uri()}/assets/')
                            for night in (False, True):
                                with self.subTest(width=width, id=sample['id'], face=face, night=night):
                                    page.set_content(page_html(body, reference, night))
                                    expected = page.evaluate(SNAPSHOT)
                                    page.set_content(page_html(body, CSS, night))
                                    self.assertEqual(page.evaluate(SNAPSHOT), expected)
                                    self.assertFalse(page.evaluate(MEASURE)['overflow'])
                                    if night and face == 'back' and width == 390:
                                        # Each spelling alone, on the card or on an ancestor.
                                        for cls in ('nightMode', 'night_mode'):
                                            for on_card in (False, True):
                                                html = page_html(body, CSS)
                                                html = html.replace('class="card "', f'class="card {cls}"') if on_card else html.replace('<body class="">', f'<body class="{cls}">')
                                                page.set_content(html)
                                                actual = page.evaluate(SNAPSHOT)
                                                # Wrapper class strings differ; their appearance must not.
                                                actual[0]['cls'] = expected[0]['cls']
                                                self.assertEqual(actual, expected, (cls, on_card))
            finally:
                browser.close()

    def test_signal_review_affordances(self):
        from playwright.sync_api import sync_playwright
        body = '''<div class="cdr-wrap cdr-back"><div class="cdr-aff">Une affirmation</div>
<hr id="answer"><div class="cdr-a">Réponse</div><div class="cdr-box">Explication</div>
<div class="cdr-fait"><span class="cloze">Cible</span></div>
<details class="cdr-reference"><summary>Sources</summary><p>Citation</p></details></div>'''
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
            try:
                page = browser.new_page(viewport={'width': 320, 'height': 640})
                for night in (False, True):
                    page.set_content(page_html(body, CSS, night))
                    def style(selector, prop):
                        return page.locator(selector).evaluate('(e, p) => getComputedStyle(e)[p]', prop)
                    self.assertEqual(style('.cdr-aff', 'fontWeight'), '700')
                    self.assertEqual(style('.cdr-a', 'fontSize'), '21px')
                    self.assertEqual(style('.cdr-a', 'fontWeight'), '650')
                    self.assertEqual(style('.cdr-a', 'color'), 'rgb(244, 198, 61)' if night else 'rgb(23, 86, 110)')
                    self.assertEqual(style('.cdr-box', 'fontSize'), '19px')
                    self.assertEqual(style('.cdr-box', 'backgroundColor'), 'rgba(0, 0, 0, 0)')
                    self.assertEqual(style('.cdr-box', 'borderWidth'), '0px')
                    self.assertEqual(style('.cloze', 'textDecorationLine'), 'underline')
                    self.assertEqual(style('.cloze', 'fontWeight'), '800')
                    self.assertEqual(style('hr', 'backgroundColor'), 'rgb(244, 198, 61)')
                    self.assertEqual(style('hr', 'width'), '42px')
                    self.assertEqual(style('hr', 'height'), '4px')
                    self.assertEqual(style('hr', 'margin'), '16px 0px')
                    self.assertEqual(style('details', 'borderWidth'), '0px')
                    self.assertEqual(style('details', 'marginTop'), '4px')
                    self.assertGreaterEqual(page.locator('summary').bounding_box()['height'], 44)
                    self.assertFalse(page.locator('details').evaluate('e => e.open'))
            finally:
                browser.close()
