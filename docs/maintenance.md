# Maintenance

## Structure du dépôt

```
data/                      bibliothèque de connaissances (YAML, une liste de notes par fichier)
  reconnaissance/*.yaml    image → sens : générés par build/import_signs.py (sauf voyants.yaml, écrit à la main)
  confusions/*.yaml        paires à discriminer (a, b = ids de reconnaissance)
  faits/*.yaml             clozes {{c1::…}} (texte, ou rappels = une phrase par trou)
  questions/*.yaml         question → réponse courte + explication
  affirmations/*.yaml      contexte (facultatif), affirmation, verdict vrai|faux, pourquoi
  scenarios/*.yaml         schémas générés (kind intersection|roundabout|road, spec) + question/réponse
  signs_inventory.yaml     inventaire des signaux (source des reconnaissances)
  _meta/objectives.yaml    objectifs d’apprentissage : chaque note est dans `notes` (socle) ou `consolidation`
  _meta/lessons.yaml       un repère par thème (principe, exemple, transfert) → écran des sous-decks, REPERES.md
  _meta/sign_overrides.yaml corrections des reconnaissances générées (clé = id ; null retire un champ)
  _meta/sign_exclusions.yaml signaux de l’inventaire sans carte, avec raison et cartes de couverture
  _meta/source_checks.yaml registre daté des consultations de sources (portée écrite, notes concernées)
build/                     génération : build.py (chargement, validation, lint, ordre, paquet), models.py
                           (types de notes, gabarits, CSS), learning.py (objectifs, étapes, rapports),
                           diagrams.py + gen_images.py (images générées), priority.py (solveur),
                           import_signs.py, verify.py, preview.py, render_check.py, dedup.py, qa_sheet.py
out/                       paquet, médias, rapports (STATS, PROGRAMME, COUVERTURE, REPERES, SELECTION-SIGNAUX,
                           VERIFICATION, RENDU, ATTRIBUTIONS)
docs/research/             dossiers de recherche et sources archivées (Code consolidé, exemples officiels 2023)
```

Champs communs à toutes les notes : `id` (unique, minuscules), `theme` (X L C R U D A P M S E ; X = méthode de
lecture de l’épreuve), `sous_theme`, `source`. Facultatifs : `image` (`commons:` nom de fichier exact,
`gen:` + `params`, `tint:` pour les voyants ISO), `image_ref` (une question réutilise l’image d’une
reconnaissance, qui la précède alors dans l’ordre), `debut: true` (base à introduire avant tout le reste),
`long_ok`, `multi_ok`, `dedup_ok` (exceptions assumées qui font taire un avertissement).

## Ce que le build vérifie

`python -m build.build --check` charge tout et s’arrête sur une **erreur** de structure : id absent ou
dupliqué, champ obligatoire manquant, thème inconnu, référence à une note inexistante (confusions, `image_ref`,
objectifs, exclusions, registre des sources), numérotation de clozes non contiguë ou `rappels` mal formés,
même réponse sous deux numéros de cloze, affirmation identique à une autre, note absente des objectifs,
scénario dont la réponse déclarée (`check`) contredit le solveur de priorité, signal retenu sans média.

Il imprime ensuite des **avertissements à relire** : réponse ou justification longue, trou de plus de huit
mots, plusieurs trous dans une même phrase, réponse identique à une autre question, part de « vrai » hors
de 40–60 %, tournure qui prédit le verdict (« puisque », « je peux », « toujours »… à plus de 85 % d’un côté),
majorité écrasante de « non » aux questions oui/non. Ce sont des invitations à juger la carte ; les seuils
sont dans `build/build.py` (`LINT_*`, `STYLE_MARKERS`).

`python -m unittest discover -s tests` couvre l’ordre, les objectifs, les gabarits, le solveur et le
rendu des clozes indépendantes. `python -m build.verify` importe le paquet dans une collection temporaire
(contenu, médias, ordre des nouvelles cartes, préréglage) puis le réimporte (aucun doublon, historique conservé).

## Ordre d’introduction

Calculé par `curriculum()` dans `build/build.py` et exporté comme position des nouvelles cartes :
cartes de méthode (X), puis les notes `debut: true`, puis toutes les pistes entrelacées au prorata de leur
taille (signalisation, circulation, chaque thème, scénarios). Dans une piste : sous-thèmes dans l’ordre de
`SUBTHEME_ORDER`, faits avant questions avant affirmations, puis ordre du fichier. Les reconnaissances
suivent `RECON_ORDER` (fichiers), chaque comparaison arrive après ses deux membres, les scénarios s’ouvrent
quand les signaux dont ils dépendent sont vus (`SCENARIO_GATES`). Toutes les notes du socle (`notes` dans
`objectives.yaml`) passent avant la consolidation ; les cartes sœurs d’un fait sont espacées de
`SIBLING_GAP` positions. `out/PROGRAMME.md` liste l’ordre obtenu.

## Modifier le deck

1. Définir la connaissance ou la décision visée et vérifier la règle **et ses conditions** dans une source
   primaire actuelle (voir [sources](sources.md)). Inscrire la consultation, sa portée et les notes concernées
   dans `data/_meta/source_checks.yaml`.
2. Écrire ou corriger la note dans `data/`. Pour une reconnaissance : corriger `signs_inventory.yaml` ou
   `_meta/sign_overrides.yaml`, puis `python build/import_signs.py` ; retirer un signal = l’ajouter à
   `_meta/sign_exclusions.yaml` avec sa couverture, puis régénérer. `voyants.yaml` s’édite directement.
   Les valeurs YAML contenant « : » se mettent entre guillemets (`python build/yamlfix.py fichier`).
3. Relier la note à son objectif dans `_meta/objectives.yaml` (`notes` = socle, `consolidation` = suite).
   Retirer une note = la supprimer du fichier et de tous les registres (`objectives`, `source_checks`,
   `couverts_par`, `dedup_ok`) ; le build signale ce qui a été oublié.
4. Pour un scénario d’intersection, déclarer `check: {order: [...]}` ou `check: {pair: [a, b, avant|apres|independant]}`
   : le solveur (`build/priority.py`) doit être d’accord. Giratoires et scénarios de route sont relus à la main.
   Une modification de `diagrams.py` ou `gen_images.py` invalide les images générées au build suivant.
5. `python -m build.build --check`, lire les avertissements, puis `python -m build.build`, `python -m build.verify`
   et les tests. Regarder les cartes modifiées : `python -m build.preview --ids id1,id2 [--night] [--out dossier]`
   (une carte cloze donne `_c0`, `_c1`…). Pour une révision large, `python -m build.render_check` contrôle
   toutes les faces à 430 × 932 (clair et sombre), 430 × 740 et 320 × 640 et écrit `out/RENDU.md` ; les mesures
   ne lisent pas le sens des images ni les petits textes incorporés : les inspecter.
6. Ajouter une ligne à [CHANGELOG](../CHANGELOG.md) et mettre à jour les effectifs du README.

Outils d’aide : `python -m build.dedup [--threshold 0.62]` liste les paires de notes textuellement proches
(décision éditoriale, jamais automatique) ; `python build/qa_sheet.py` produit des planches image + code + nom
par fichier de reconnaissance dans `out/qa/`.

## Identifiants et réimport

Les identifiants des types de notes et des decks sont fixes (`build/models.py`) et les GUID dérivent de
l’`id` de la note : réimporter une nouvelle version de la même édition met les notes à jour sans doublon et
conserve l’historique de révision. Renommer un `id`, renuméroter un cloze ou changer la structure des champs
crée en revanche de nouvelles cartes à l’import : le faire en connaissance de cause.
