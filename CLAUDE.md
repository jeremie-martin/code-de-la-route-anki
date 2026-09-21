# Code de la route 2026 — deck Anki

Projet : générer `out/Code-de-la-route-2026.apkg`, un deck Anki pour réussir l'ETG (code de la route,
permis B) tel qu'il existe en 2026. Lire `README.md` puis `docs/01-analyse-examen.md`,
`docs/02-carte-des-connaissances.md`, `docs/03-conception-des-cartes.md`, `docs/04-sources.md`,
`docs/14-bilan-v8.md` (révision actuelle), `docs/13-bilan-v7.md`, `docs/12-bilan-v6.md`, `docs/10-bilan-v5.md` et `docs/11-interface-quotidienne.md`.
Les dossiers v1/v2 sont historiques ; ne pas réintroduire leurs formulations corrigées.

## Commandes

```bash
source .venv/bin/activate            # créé avec: uv venv .venv && uv pip install anki pyyaml cairosvg pillow requests lxml
python -m build.build --check        # valide data/ (schéma, ids uniques, clozes, solveur de priorité)
python -m build.build --media        # génère out/media/ (téléchargement Commons au premier build, ~1 req/s)
python -m build.build                # paquets Socle + complet, couverture, programme, statistiques
python -m unittest discover -s tests -v
python -m build.verify               # imports réels et conservation d’historique
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
- `faits/*.yaml` : clozes `{{c1::…}}` (≤ 4 par note). Les rappels de vitesse suivent le cadre « Conditions.
  Configuration → plafond {{valeur}} ». Plusieurs cibles → `rappels: [texte c1, texte c2]`,
  chaque entrée ciblant un seul ordinal distinct ; `texte` n'admet qu'un trou (sauf `multi_ok: true` pour
  une relation unique) et un trou fait au plus 8 mots (sauf `long_ok: true`). Ne pas cumuler `texte` et `rappels`.
  Une phrase à réciter ou un élément de liste à deviner devient une question ou une affirmation.
- `questions/*.yaml` : question → réponse courte : la décision ou la valeur et sa raison décisive (≤ 30 mots, viser 10-22,
  ≤ 4 éléments ; `long_ok: true` pour une exception justifiée) ; les nuances vont dans `explication`.
- `affirmations/*.yaml` : `contexte` (facultatif), `affirmation`, `verdict: vrai|faux`, `pourquoi` ; fausses
  affirmations plausibles, 35-65 % de vrai par fichier, pas de mot-signal (toujours/jamais/obligatoirement/uniquement)
  dans une fausse sauf `signal_ok: true`.
- `scenarios/*.yaml` : schémas générés (`kind: intersection|roundabout|road`, `spec`) ; pour les
  intersections, `check: {order: [...]}` ou `check: {pair: [a, b, avant|apres|independant]}` est
  recalculé par `build/priority.py` — le build échoue en cas de désaccord.
- Champs communs : `id` (unique, minuscules), `theme` (L C R U D A P M S E X), `sous_theme`,
  `importance` (essentiel|utile|rare), `source`, `tags` optionnels. Lettres officielles : A = porter
  secours, P = prendre/quitter le véhicule, S = sécurité passagers/véhicule, E = environnement.
- Parcours : `data/_meta/objectives.yaml` relie explicitement chaque note à ses objectifs :
  `notes` pour l’introduction, `consolidation` pour la suite. Aucun plafond de notes ou de cartes.
  `build/learning.py` annote `parcours::*` / `objectif::*`, place toutes les cartes du socle avant
  l’approfondissement et produit le programme depuis le même plan que les positions exportées.
- `data/_meta/sign_exclusions.yaml` justifie les signaux sans carte visuelle distincte et référence
  leurs couvertures. Pas de filtre automatique par rareté, mais un critère éditorial (v6, appliqué
  intégralement en v8) : un signal entre s'il porte une décision de conduite ou une discrimination que
  l'épreuve peut demander ; les variantes d'une famille apprise, les sorties de zone et fins déductibles du
  signal de début, les services et catégories au pictogramme transparent sont exclus (archétypes conservés :
  B51, B31/B33/B34/B40, CE2a/CE15a/CE15i, M4a/M4d1/M4d2/M4f). Tout signal sélectionné doit avoir un média.
- Ordre interne d’introduction des nouvelles cartes = programme calculé par `curriculum()` dans `build/build.py`
  (méthode d'abord ; phases essentiel → utile → rare ; thèmes entrelacés au prorata ; scénarios après les
  panneaux dont ils dépendent : `SCENARIO_GATES` ; `RECON_ORDER` = ordre des fichiers de signalisation).
  Le paquet embarque un préréglage d'options (id `DECK_CONFIG_ID`) qui applique cet ordre.
- Versos de reconnaissance ≤ 90 mots ; les phrases de catégorie répétées sont retirées à l'import
  (`BOILERPLATE` dans `build/import_signs.py`) et vivent dans des cartes de règle. Le `complement`
  ne cite ni codes de fin, ni panonceaux possibles, ni distances d'implantation : seulement une nuance
  qui change la décision (corrections dans `sign_overrides.yaml`).

## Règles de rédaction

- Une carte = une connaissance ; réponse courte et non ambiguë ; explication centrée sur le pourquoi,
  la limite ou la distinction utile (sa longueur doit se justifier). Pas de cartes inversées. Règle actuelle en réponse ; toute approximation explicitement nommée.
  Ne pas prétendre connaître une ancienne réponse attendue par la banque confidentielle. Pas de mention
  « question officielle » au recto. Pas de maxima de peine (prison, amende) dans les cartes : seuils,
  qualification de délit et points seulement.
- Toute valeur juridique se vérifie dans le Code de la route consolidé
  (`docs/research/sources/code_de_la_route_consolide_2026-09-10.pdf`, texte : `pdftotext -layout`).
- Images : Commons `commons:` (nom de fichier exact), générateurs `gen:` (`build/gen_images.py`),
  teinte `tint:` pour les voyants ISO.
- La v5 est une refonte pour import neuf (retraits et ordinaux modifiés, sans migration v2/v3/v4).
  Pour les modifications ultérieures, préserver les GUID, ids de types/decks (`build/models.py`), numéros de cloze ET ids internes
  des champs/gabarits (`data/_meta/anki_schema.json`, repris du paquet v2 publié).
  `build.verify` doit refuser tout conflit de réimport, même si le nombre total de notes est correct.
- Les contrôles externes ciblés sont documentés dans `data/_meta/source_checks.yaml` ; une date
  ne certifie que la portée écrite. Les références génériques héritées ne prouvent pas une vérification récente.

## Repères et applications (v4, poursuivis en v5)

`lessons.yaml` contient un repère avec exemple par thème, exporté dans `out/COMPRENDRE.md` et
le champ `Repere` de tous les modèles (volet au verso). Ce complément n’est pas une cible de rappel.
`questions.image_ref` réutilise un signal existant ; le parcours place sa reconnaissance avant
l’application. `contrasts.yaml` justifie les familles de cas ; `retirements.yaml` documente les
suppressions avec leur couverture conservée. Les deux alimentent `out/CONCEPTION.md`.

## Vérification du rendu v5.1

Installer `requirements-qa.txt` et Chrome/Chromium, puis `python -m build.render_check`.
Le vérificateur importe le paquet dans une collection temporaire et contrôle toutes les faces
à 430 × 932 clair/sombre, 430 × 740 sombre et 320 × 640 sombre ; captures dans `out/qa/render/`. Les mesures ne valident pas
le sens des images ni les petits textes incorporés : les inspecter. `out/RENDU.md` et
`out/VERIFICATION.md` portent le SHA-256 du paquet réellement contrôlé.

Interface : appliquer les niveaux de visibilité de `docs/03-conception-des-cartes.md`. Les corrections
restent visibles ; « Sources et repères » regroupe uniquement les références. Pas de consigne de notation
répétée au verso. Inspecter les captures `_viewport` et pleine hauteur, pas seulement les mesures.
