# Code de la route 2026 — deck Anki

Projet : générer `out/Code-de-la-route-2026.apkg`, un deck Anki pour réussir l'ETG (code de la route,
permis B) tel qu'il existe en 2026. Lire `README.md` puis `docs/01-analyse-examen.md`,
`docs/02-carte-des-connaissances.md`, `docs/03-conception-des-cartes.md`, `docs/04-sources.md`,
`docs/05-audit-v2.md` (audit et décisions v2) et `docs/research/brief-v2-redaction.md` (règles de rédaction).

## Commandes

```bash
source .venv/bin/activate            # créé avec: uv venv .venv && uv pip install anki pyyaml cairosvg pillow requests lxml
python -m build.build --check        # valide data/ (schéma, ids uniques, clozes, solveur de priorité)
python -m build.build --media        # génère out/media/ (téléchargement Commons au premier build, ~1 req/s)
python -m build.build                # build complet -> out/Code-de-la-route-2026.apkg + out/STATS.md + out/PROGRAMME.md + out/ATTRIBUTIONS.md
python -m build.preview --ids id1,id2   # captures de cartes rendues (Chrome headless) -> out/preview/sheet.png
python build/qa_sheet.py             # planches de contrôle image+code+nom par fichier -> out/qa/
python build/import_signs.py         # régénère data/reconnaissance/* depuis data/signs_inventory.yaml (+ data/_meta/sign_overrides.yaml)
python build/yamlfix.py data/*/*.yaml   # quote les valeurs YAML contenant ': '
```

## Structure des données (`data/`)

- `reconnaissance/*.yaml` : image → sens (panneaux, panonceaux, balises, marquages, feux, gestes, voyants).
  Générés par `build/import_signs.py` ; **ne pas éditer à la main** : corriger `data/_meta/sign_overrides.yaml`
  (clé = id) ou `data/signs_inventory.yaml`, puis régénérer. `voyants.yaml` est écrit à la main.
- `confusions/*.yaml` : paires à discriminer (`a`, `b` = ids de reconnaissance).
- `faits/*.yaml` : clozes `{{c1::…}}` (≤ 4 par note).
- `questions/*.yaml` : question → réponse courte (≤ 40 mots, ≤ 4 éléments ; `long_ok: true` pour une exception justifiée).
- `affirmations/*.yaml` : `contexte` (facultatif), `affirmation`, `verdict: vrai|faux`, `pourquoi` ; fausses
  affirmations plausibles, 35-65 % de vrai par fichier, pas de mot-signal (toujours/jamais/obligatoirement/uniquement)
  dans une fausse sauf `signal_ok: true`.
- `scenarios/*.yaml` : schémas générés (`kind: intersection|roundabout|road`, `spec`) ; pour les
  intersections, `check: {order: [...]}` ou `check: {pair: [a, b, avant|apres|independant]}` est
  recalculé par `build/priority.py` — le build échoue en cas de désaccord.
- Champs communs : `id` (unique, minuscules), `theme` (L C R U D A P M S E X), `sous_theme`,
  `importance` (essentiel|utile|rare), `source`, `tags` optionnels. Lettres officielles : A = porter
  secours, P = prendre/quitter le véhicule, S = sécurité passagers/véhicule, E = environnement.
- Ordre d'introduction des nouvelles cartes = programme calculé par `curriculum()` dans `build/build.py`
  (méthode d'abord ; phases essentiel → utile → rare ; thèmes entrelacés au prorata ; scénarios après les
  panneaux dont ils dépendent : `SCENARIO_GATES` ; `RECON_ORDER` = ordre des fichiers de signalisation).
  Le paquet embarque un préréglage d'options (id `DECK_CONFIG_ID`) qui applique cet ordre.
- Versos de reconnaissance ≤ 90 mots ; les phrases de catégorie répétées sont retirées à l'import
  (`BOILERPLATE` dans `build/import_signs.py`) et vivent dans des cartes de règle.

## Règles de rédaction

- Une carte = une connaissance ; réponse courte et non ambiguë ; explication d'une ligne (le pourquoi,
  le piège). Pas de cartes inversées. Convention d'examen (auto-écoles) en réponse, valeur officielle en
  explication si elles diffèrent. Valeur en vigueur en 2026 en réponse, ancienne valeur en explication
  si la banque de questions (2023) peut l'attendre encore (tag `nouveau::AAAA`).
- Toute valeur juridique se vérifie dans le Code de la route consolidé
  (`docs/research/sources/code_de_la_route_consolide_2026-09-10.pdf`, texte : `pdftotext -layout`).
- Images : Commons `commons:` (nom de fichier exact), générateurs `gen:` (`build/gen_images.py`),
  teinte `tint:` pour les voyants ISO.
- Les ids de types de notes/decks sont stables (`build/models.py`) : ne pas les changer, sinon les
  utilisateurs perdent leur historique à la réimportation.
