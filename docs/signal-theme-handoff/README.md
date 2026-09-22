# Apply the approved Signal theme

The user chose **Signal** as their favourite after comparing real cards across multiple theme iterations. Adopt the precise Signal exported here, including front persistence and compact sources. This directory is a handoff, not an already-applied production change.

## Start here

1. Read the repository's README, CLAUDE.md, docs/conception.md and docs/maintenance.md.
2. Use **signal.css** as the visual reference for replacing `build/cards.css`. It is the complete composed lab stylesheet, including comparison-image rules, not the early Signal draft. Its successive overrides are intentional; do not cherry-pick only the first block. You may consolidate it if computed styles and rendering remain equivalent.
3. Review **templates.patch**, then use `git apply --check docs/signal-theme-handoff/templates.patch` from the repository root. It restores three omitted front prompts on the back in `build/models.py`. Apply it if still appropriate to the latest templates.
4. Keep the latest deck content. **samples.json** and **assets/** are reference fixtures from the lab, not input data to import back into production.
5. Validate real Anki output, rebuild the package and update relevant documentation/changelog using the repository workflow below.

The lab is at `/home/jmartin/code-de-la-route-style-lab`, accessible at http://10.77.77.3:8765/ while its server runs. The handoff also has an independent **preview.html**: serve this directory with `python3 -m http.server 8766 --bind 127.0.0.1` and open http://localhost:8766/preview.html. It shows front and back at 430 × 932 CSS pixels, in light or dark mode. It needs no lab files or external assets.

## What is approved

- **Signal, not Relay, Essential, or the corrected production preview.**
- Sans-serif type, light blue-grey paper and a dark navy appearance.
- Main answer: **21px, weight 650, line-height 1.4**; explanations: **19px, line-height 1.45**. Signal deliberately did NOT receive the later 22px answer enlargement used in other themes.
- Light main answer **#17566e**; dark main answer **#f4c63d**. False verdicts retain their distinct warning colour.
- Bold questions and claims; underlined, heavy cloze targets. Do not turn every sentence into equally heavy text.
- The short **yellow** question–answer divider remains: 42px wide, 4px high, 16px vertical margins. Do not substitute the later neutral full-width divider used in other themes.
- Main signs remain large and centred. Do not adopt Atlas's former small side-by-side sign layout.
- Explanations and practical advice are unboxed; no filled rounded panels, outer notebook frame, decorative rail, or added “À retenir / Réponse / Détail” labels. The slim trap border is part of approved Signal.
- Sources remain collapsed by default, with **no extra top rule**, a **4px top margin**, and a **44px minimum disclosure target**. Keep citations and technical codes accessible.
- Captioned supporting images stay on the answer only; preserve their 110px height cap and responsive wrapping.

The CSS is authoritative where prose omits details. Do not redesign the chosen theme while integrating it.

## Front persistence is mandatory

Revealing an answer extends the existing front instead of replacing its layout. The original sign/diagram keeps the same x/y coordinates and size. Context, question, claim and hints retain their position, width, family, weight, size, line-height and colour.

The patch restores:

- Recognition: `<div class="cdr-q">{{Question}}</div>` after the main image and before the answer divider. Use the actual field, not a hard-coded “Que signifie ce panneau ?”: it varies by signal type.
- Confusion: the same “Quelle est la différence ?” prompt as on the front, before the divider.
- Affirmation: “Vrai ou faux ? Pourquoi ?” before the divider.

Question and Scenario already repeat the front. Fait already reveals the cloze in place; preserve both native `{{cloze:Texte}}` rendering and `CLOZE_FOCUS`. Cloze replacement may naturally change line wrapping. Never expose hidden sibling prompts, copy front placeholders into the back, or add a second copy of the cloze.

The lab used DOM manipulation only to preview the three missing prompts. **Do not ship that JavaScript**: make the equivalent native template edits. Do not copy the lab's iframe wrappers or control UI into Anki.

## Integration details and scope

- Preserve all model IDs, deck IDs, note IDs/GUIDs, field order and cloze ordinals. This is a styling/template update, not new note types.
- The repository head and lab snapshot revision are recorded separately in **manifest.json**. They differ: the repository has newer content. Adapt the small patch if templates have moved; never replace whole data files with lab samples.
- The CSS is an exact export, not a production-normalized rewrite. Signal uses `.nightMode`. Production should support both `.nightMode` and `.night_mode`, on the card or an ancestor, as existing production does. Add equivalent aliases and verify the rendered result for each class separately; the lab used both classes together.
- Check the A/B comparison labels in dark mode: the exact export inherits a dark `.cdr-side` colour from the original theme. Give these small labels a legible dark-mode colour during integration. This is a contrast correction, not a change to the approved main-answer palette.
- Check `box-sizing`, page margins, viewport behaviour and platform text sizing in real Anki. The preview harness sets body margin 0 and a border-box card with min-height 100vh. It is not a simulated native Anki review screen.
- Preserve production-only structural helpers where needed: `.cdr-code`, `ul.cdr-list`, reference headings/paragraph spacing, and any newer selectors not exercised by the snapshot. Compare against the latest `build/cards.css`; merge these intentionally without restoring old answer colours or back-only question demotion.
- Do not overwrite the user's collections or reset scheduling. Rebuild/export through the normal build path and verify reimport with the existing temporary-collection checks.

## Validation

The lab passed 1,536 card/theme/face/appearance checks across 16 themes and 24 samples, including 768 front/back comparisons. That includes Signal but is NOT validation of the latest full deck or native AnkiMobile. **validation.json** records the Signal subset and export/template-patch checks performed for this handoff.

Run after integration, using the repository virtual environment:

```sh
.venv/bin/python -m build.build --check
.venv/bin/python -m unittest discover -s tests
.venv/bin/python -m build.build
.venv/bin/python -m build.verify
.venv/bin/python -m build.preview --ids a13a,conf-a2a-a2b,l-vitesse-hors-agglo,triangle-distance,r-aquaplaning,scn-stop-moi,aff-l-stop-rien-ne-vient,b9b,l-arret-vs-stationnement --width 430 --out out/qa/signal-light
.venv/bin/python -m build.preview --ids a13a,conf-a2a-a2b,l-vitesse-hors-agglo,triangle-distance,r-aquaplaning,aff-l-stop-rien-ne-vient --width 430 --night --out out/qa/signal-dark
.venv/bin/python -m build.render_check
```

Preview output directories are cleared by that command: use the dedicated paths above. Confirm those sample IDs still exist before running.

Add/retain meaningful regression checks: front/back image geometry and prompt typography; bold true/false claims; cloze sibling isolation; visible divider; answer/body size ratio; no boxed feedback/sources; comparison captions and image bounds; source expansion; no horizontal overflow at 320/390/430px. Long answers may scroll vertically—do not shrink them to force a fit.

Inspect light/dark recognition, paired signs, illustrated cloze, text-only question, long scenario, true/false and answer-only comparisons. Try the final package in AnkiMobile on the target iPhone before claiming native rendering parity. Update the maintenance note that currently describes the stylesheet as Essential.

## Files

- `signal.css`: exact approved composed CSS, no local browser edits.
- `templates.patch`: three native back-template additions, unapplied.
- `manifest.json`: provenance and file hashes.
- `samples.json`, `assets/`, `preview.html`: standalone rendered reference, preserving French content and source disclosures.
- `screenshots/`: reference images from the chosen theme.
- `validation.json`: bounded handoff checks, distinct from future production acceptance.

Sample text and media retain their original licences. Refer to the deck's `out/ATTRIBUTIONS.md` and README; this handoff does not change attribution or licensing.
