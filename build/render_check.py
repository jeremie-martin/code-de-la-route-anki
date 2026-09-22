"""Check actual Anki-rendered cards in Chromium, offline, at phone widths.

Install requirements-qa.txt; use the system Chrome/Chromium (no browser download).
python -m build.render_check
Screenshots are samples; DOM/layout/media checks cover every card, both faces.
Vertical scrolling is reported, not treated as missing content.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile

from anki.collection import Collection
from playwright.sync_api import sync_playwright

from build.preview import CHROME, OUT
from build.verify import import_package

# Representative templates, visual feedback, long answers and this edition’s changed cards.
# Every card still gets all phone layout checks; this set only selects screenshots,
# source-disclosure checks and the additional desktop pass. Replace obsolete samples.
SAMPLES = {
    'a13a', 'b9b', 'ab4', 'voyant-temperature', 'conf-a2a-a2b', 'conf-ab3a-ab4',
    'l-vitesse-hors-agglo', 'triangle-distance', 's-chargement-chiffres',
    'r-aquaplaning', 'l-arret-vs-stationnement', 'r-b26-chaines-complement',
    'scn-stop-moi', 'scn-dep-cycliste-ligne-continue', 'aff-l-stop-rien-ne-vient',
    'aff-p-siege-verrouille', 'a-pls', 'a-message-alerte',
}

# Kept separate so the checker itself can be tested against deliberately bad pages.
MEASURE = """() => {
  const visible = e => e.getClientRects().length > 0;
  const images = [...document.images];
  return {
    front: [...document.querySelectorAll('.cdr-img, .cdr-img img, .cdr-pair, .cdr-pair img, .cdr-side, .cdr-q, .cdr-aff, .cdr-ctx, .cdr-hint')]
      .filter(visible).map(e => {
        const r = e.getBoundingClientRect(), s = getComputedStyle(e);
        return {text: e.innerText, src: e.getAttribute('src'),
          rect: [r.x, r.y, r.width, r.height],
          style: [s.fontFamily, s.fontSize, s.fontWeight, s.lineHeight, s.letterSpacing, s.color]};
      }),
    overflow: document.documentElement.scrollWidth > innerWidth + 1,
    broken: images.filter(e => !e.complete || !e.naturalWidth).map(e => e.src),
    units: [...document.querySelectorAll('.cdr-unit')].filter(visible).length,
    totalUnits: document.querySelectorAll('.cdr-unit').length,
    clozes: [...document.querySelectorAll('.cloze')].filter(visible).length,
    text: document.body.innerText.trim(),
    height: document.documentElement.scrollHeight,
    primaryBottom: Math.max(0, ...[...document.querySelectorAll('.cdr-a, .cdr-verdict, .cdr-fait, .cdr-difference')]
      .filter(visible).map(e => e.getBoundingClientRect().bottom)),
    reviewBottom: document.querySelector('.cdr-reference')?.getBoundingClientRect().top || 0,
    imageSizes: images.filter(visible).map(e => [Math.round(e.width), Math.round(e.height)]),
    expanded: [...document.querySelectorAll('details[open]')].length
  };
}"""


def page_html(body, css, night=False):
    cls = 'nightMode night_mode' if night else ''
    return ('<!doctype html><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<style>{css}\nbody {{margin:0}} .card {{box-sizing:border-box; min-height:100vh}}</style>'
            f'<body class="{cls}"><main class="card {cls}">{body}</main></body>')


def main():
    if not CHROME:
        raise SystemExit('Chrome/Chromium requis ; voir requirements-qa.txt')
    package = OUT / 'Code-de-la-route-2026.apkg'
    digest = hashlib.sha256(package.read_bytes()).hexdigest()
    target = OUT / 'qa' / 'render'
    target.mkdir(parents=True, exist_ok=True)
    # Never leave screenshots from a previous package beside the current run.
    for old in target.glob('*.png'):
        old.unlink()
    origin = target / 'index.html'
    origin.write_text('<!doctype html><title>Contrôle local</title>')
    temporary = tempfile.TemporaryDirectory(prefix='cdr-render-')
    col = Collection(str(Path(temporary.name) / 'render.anki2'))
    failures, scrolling, results = [], [], []
    shots = 0
    metrics = []
    disclosures = 0
    persistence_checks = 0
    try:
        import_package(col, OUT / 'Code-de-la-route-2026.apkg')
        present = {col.get_note(nid)['Id'] for nid in col.find_notes('')}
        missing = SAMPLES - present
        if missing:
            raise ValueError(f'Échantillon de rendu absent du paquet : {sorted(missing)}')
        media_uri = Path(col.media.dir()).as_uri()
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
            page = browser.new_page()
            # Cards must work without any online resource.
            page.route('http://**/*', lambda route: route.abort())
            page.route('https://**/*', lambda route: route.abort())
            page.goto(origin.as_uri())
            for width, height, night in ((430, 932, False), (430, 932, True), (390, 844, True), (320, 640, True), (960, 900, False)):
                page.set_viewport_size({'width': width, 'height': height})
                checked = 0
                config = f'{width}x{height}_{"dark" if night else "light"}'
                for cid in col.find_cards(''):
                    card = col.get_card(cid)
                    note = card.note()
                    ident = note['Id']
                    if width == 960 and ident not in SAMPLES:
                        continue
                    for side, html in (('q', card.question()), ('a', card.answer())):
                        html = html.replace('src="cdr_', f'src="{media_uri}/cdr_')
                        page.set_content(page_html(html, card.note_type()['css'], night), wait_until='load')
                        m = page.evaluate(MEASURE)
                        key = f'{ident}/c{card.ord}/{side}/{config}'
                        metrics.append(dict(id=ident, ord=card.ord, side=side, kind=card.note_type()['name'],
                                            config=config, words=len(m['text'].split()), height=m['height'],
                                            primaryBottom=m['primaryBottom'], reviewBottom=m['reviewBottom']))
                        errors = []
                        if side == 'q':
                            front = m['front']
                        else:
                            persistence_checks += 1
                            if m['front'] != front:
                                errors.append('image ou texte du recto déplacé/modifié au verso')
                        if m['overflow']:
                            errors.append('débordement horizontal')
                        if m['broken']:
                            errors.append('image non chargée')
                        if not m['text'] or 'Invalid HTML' in m['text'] or '{{' in m['text']:
                            errors.append('texte vide ou gabarit non résolu')
                        if m['totalUnits'] and m['units'] != 1:
                            errors.append(f"rappels visibles : {m['units']}")
                        if side == 'q' and 'CDR Fait' == card.note_type()['name'] and not m['clozes']:
                            errors.append('cloze absent')
                        if m['expanded']:
                            errors.append('repère ouvert par défaut')
                        if errors:
                            failures.append([key, errors])
                        if m['height'] > height:
                            scrolling.append([key, m['height']])
                        if ident in SAMPLES:
                            page.screenshot(path=str(target / f'{ident}_c{card.ord}_{side}_{config}.png'), full_page=True)
                            page.screenshot(path=str(target / f'{ident}_c{card.ord}_{side}_{config}_viewport.png'), full_page=False)
                            shots += 2
                            if side == 'a':
                                disclosure = page.locator('.cdr-reference')
                                disclosure.locator('summary').click()
                                opened = page.evaluate(MEASURE)
                                # Links and lesson must be reachable, without losing corrective feedback.
                                if opened['expanded'] != 1 or opened['overflow'] or len(opened['text']) <= len(m['text']):
                                    failures.append([key, ['volet de références inaccessible ou débordant']])
                                if note['Source'] and not disclosure.locator('p').first.is_visible():
                                    failures.append([key, ['source invisible après ouverture']])
                                if width == 430 and height == 932 and not night and ident in {'ab4', 'a-pls'}:
                                    page.screenshot(path=str(target / f'{ident}_references.png'), full_page=True)
                                    shots += 1
                                disclosure.locator('summary').click()
                                if page.evaluate(MEASURE)['expanded']:
                                    failures.append([key, ['volet impossible à refermer']])
                                disclosures += 1
                        checked += 1
                results.append({'width': width, 'height': height, 'night': night, 'faces': checked})
                print(f'{width}px: {checked} faces contrôlées', flush=True)
            browser.close()
    finally:
        col.close()
        temporary.cleanup()
    if hashlib.sha256(package.read_bytes()).hexdigest() != digest:
        raise SystemExit('Le paquet a changé pendant le contrôle ; relancer après le build.')
    report = dict(package_sha256=digest, configurations=results, failures=failures,
                  scrolling=scrolling, screenshots=shots, disclosure_checks=disclosures,
                  front_persistence_checks=persistence_checks)
    (target / "card-metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2))
    (target / 'measurements.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    lines = ['# Vérification du rendu navigateur\n',
             f'Paquet complet SHA-256 : `{digest}`.\n',
             'Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, '
             'puis chargés dans Chromium local sans réseau externe. '
             'Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 390 × 844 et 320 × 640 en sombre ; '
             'échantillon à 960 px.\n',
             '| Largeur × hauteur | Mode | Faces contrôlées |', '|---|---|---|']
    for row in results:
        lines.append(f"| {row['width']} × {row['height']} | {'sombre' if row['night'] else 'clair'} | {row['faces']} |")
    lines += [f'\n**{len(failures)} échec(s)** : débordement horizontal, média absent, rappel mal isolé, '
              'gabarit non résolu, recto déplacé/modifié au verso ou repère ouvert par défaut.\n',
              f'{persistence_checks} comparaisons recto/verso : géométrie des images, textes et typographie des prompts '
              '(le texte cloze se révèle en place et peut naturellement changer de longueur).\n',
              f'{len(scrolling)} faces/configurations nécessitent un défilement vertical ; '
              'ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).\n',
              f'{disclosures} ouvertures et fermetures du volet testées sur l’échantillon.\n',
              f'{shots} captures dans `out/qa/render/`, avec le détail dans `measurements.json`.\n',
              'Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, '
              'ni sa signification. L’inspection visuelle des captures reste nécessaire. '
              'Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.\n']
    if failures:
        lines.append('```json\n' + json.dumps(failures, ensure_ascii=False, indent=2) + '\n```')
    (OUT / 'RENDU.md').write_text('\n'.join(lines), encoding='utf-8')
    if failures:
        raise SystemExit(f'{len(failures)} échecs ; voir out/RENDU.md')


if __name__ == '__main__':
    main()
