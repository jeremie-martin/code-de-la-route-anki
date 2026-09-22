# Maintenance

## Structure du dépôt

```
data/                      bibliothèque de connaissances (YAML, une liste de notes par fichier)
  reconnaissance/*.yaml    image → sens : GÉNÉRÉS par build/import_signs.py (sauf voyants.yaml, écrit à la main)
  confusions/*.yaml        paires à discriminer (a, b = ids de reconnaissance)
  faits/NN_theme.yaml      clozes {{c1::…}} (texte, ou rappels = une phrase par trou)
  questions/NN_theme.yaml  question → réponse courte + explication
  affirmations/NN_theme.yaml  contexte (facultatif), affirmation, verdict vrai|faux, pourquoi
  scenarios/*.yaml         schémas générés (kind intersection|roundabout|road, spec) + question/réponse
  signs_inventory.yaml     inventaire des signaux (source des reconnaissances)
  _meta/objectives.yaml    objectifs d’apprentissage : chaque note est dans `notes` (socle) ou `consolidation`
  _meta/lessons.yaml       un repère par thème (principe, exemple, transfert) → écran des sous-decks, REPERES.md
  _meta/sign_overrides.yaml corrections des reconnaissances générées (clé = id ; null retire un champ)
  _meta/sign_exclusions.yaml signaux de l’inventaire sans carte : codes (inventaire), raison, couverts_par (ids)
  _meta/source_checks.yaml registre daté des consultations de sources (portée écrite, notes concernées)
build/                     build.py (chargement, validation, lint, ordre, paquet) ; models.py (types de notes,
                           gabarits) ; cards.css (style commun) ; learning.py (objectifs, étapes, rapports) ; diagrams.py + gen_images.py
                           (images générées) ; priority.py (solveur) ; import_signs.py ; commons_fetch.py +
                           commons_index.py (médias Wikimedia) ; verify.py, preview.py, render_check.py, dedup.py,
                           qa_sheet.py, yamlfix.py
assets/                    index Commons et icônes ISO des voyants ; cache des téléchargements (ignoré par git)
out/                       paquet, médias, rapports (STATS, PROGRAMME, COUVERTURE, REPERES, SELECTION-SIGNAUX,
                           VERIFICATION, RENDU, ATTRIBUTIONS)
docs/research/             dossiers de recherche (examen, faits juridiques, connaissances, signaux) et sources
                           archivées : Code consolidé (PDF), exemples officiels 2023, communiqué DSR
goal.md                    la demande initiale
tests/                     ordre, objectifs, gabarits, solveur, rendu des clozes, vérificateur de rendu
```

Un fichier par thème et par forme (`02_circulation.yaml` … `11_environnement.yaml`, `00_methode.yaml` pour X).
Dans un fichier, placer une note à côté de celles de son sous-thème : à sous-thème égal, l’ordre du fichier est
l’ordre d’introduction. Les fichiers de reconnaissance sont organisés par famille de signaux (`RECON_ORDER`).

Bootstrap : `uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt` ; le premier
`python -m build.build` télécharge ~300 fichiers Commons à une requête par seconde (quelques minutes, réseau
nécessaire), puis tout est en cache. Le texte du Code consolidé, ignoré par git, se produit avec
`pdftotext -layout docs/research/sources/code_de_la_route_consolide_2026-09-10.pdf docs/research/sources/cdr.txt`
(poppler) ; un article s’y cherche par `grep -n "R. 415-5" docs/research/sources/cdr.txt`.

## Format des notes

Champs communs : `id` (unique, minuscules, chiffres, tirets), `theme` (X L C R U D A P M S E ; X = méthode de
lecture de l’épreuve), `sous_theme` (voir la liste ci-dessous), `source`. Facultatifs : `image` (`{commons: nom
de fichier exact}`, `{gen: générateur, params: {…}}`, `tint: "#hex"` pour un voyant ISO), `image_ref` (une
question réutilise l’image d’une reconnaissance, qui la précède alors dans l’ordre), `debut: true` (base à
introduire avant tout le reste), `multi_ok`, `dedup_ok: [autre-id]` (exceptions assumées qui font
taire un avertissement). Les valeurs contenant « : » se mettent entre guillemets (`python build/yamlfix.py fichier`).

```yaml
# questions/
- id: l-priorite-droite-defaut
  question: Intersection sans panneau ni feu ; deux voitures arrivent en même temps. À qui dois-je céder le passage ?
  reponse: 'À celle qui vient de ma droite : sans signalisation, la priorité à droite s’applique.'
  explication: Elle vaut aussi pour une petite rue qui débouche sur une grande ; seuls un panneau, un feu ou un agent la changent.
  theme: L
  sous_theme: priorites
  source: Code de la route, art. R415-5
  debut: true

# faits/ — un trou par phrase ; plusieurs cibles → rappels (un ordinal distinct par phrase, c1..c4)
- id: l-vitesse-agglo
  texte: En agglomération, la vitesse maximale par défaut est de {{c1::50 km/h}}.
  explication: Zone 30 : 30 ; zone de rencontre : 20 ; aire piétonne : allure du pas.
  theme: L
  sous_theme: vitesse
  source: Code de la route, art. R413-3

# affirmations/
- id: aff-l-stop-rien-ne-vient
  contexte: J'aborde un STOP ; la route transversale est parfaitement dégagée.
  affirmation: Un net ralentissement, sans immobiliser les roues, suffit.
  verdict: faux
  pourquoi: 'R415-6 impose l’arrêt à la ligne, roues immobiles, même sans trafic : 135 € et 4 points.'
  theme: L
  sous_theme: priorites
  source: Code de la route, art. R415-6

# confusions/ — a et b sont des ids de reconnaissance
- id: conf-b6a1-b6d
  a: b6a1
  b: b6d
  difference: 'A, une barre rouge : stationnement interdit. B, une croix rouge : arrêt et stationnement interdits.'
  theme: L
  sous_theme: panneaux
  source: IISR 4e partie

# scenarios/ — intersection : approaches N E S W (vehicle {colour, me, kind car|truck|bus|tram|moto|bike|pompiers,
# siren}, goes straight|left|right, sign stop|cedez|prioritaire|fin_prioritaire|priorite_droite|feu_vert|feu_rouge|
# feu_orange_clignotant…, private), branches [E, W, S] pour un T, agent bras_leve|bras_tendus_NS|bras_tendus_EW ;
# check {pair: [a, b, avant|apres|independant]} ou {order: [...]} est recalculé par build/priority.py.
# roundabout : vehicles [{pos: N|E|S|W|inside, angle, colour, me, goes}] ; road : lanes, axis, vehicles
# [{lane, y, colour, me, dir}], extras (sign, retrecissement, passage_pieton, bau, label…), caption. Voir diagrams.py.
- id: scn-pd-droite-tourne-gauche
  kind: intersection
  spec:
    approaches:
      S: {vehicle: {colour: bleu, me: true}, goes: straight}
      E: {vehicle: {colour: rouge}, goes: left}
  check: {pair: [S, E, apres]}
  question: "Intersection sans signalisation. La voiture rouge, à ma droite, tourne à sa gauche. Qui passe en premier ?"
  reponse: "La rouge : elle vient de ma droite."
  explication: "Priorité à droite (R415-5), quelle que soit la direction prise par le véhicule de droite."
  theme: L
  sous_theme: priorites
  source: "Code de la route, art. R415-5 et R415-4"

# reconnaissance/voyants.yaml (les autres fichiers sont générés) — type panneau|panonceau|balise|marquage|feu|geste|
# voyant|pictogramme|equipement ; champs nom, signification, conduite, complement, piege, code, question (facultatif)
- id: voyant-huile
  type: voyant
  code: ISO 7000-0248
  image: {commons: "ISO 7000 - Ref-No 0248.svg", tint: "#e53935"}
  nom: Pression d'huile moteur (rouge)
  signification: 'Pression d’huile insuffisante : le moteur risque la casse.'
  conduite: Je m’arrête dès que possible en sécurité et je coupe le moteur ; je ne repars pas si le voyant persiste.
  theme: M
  sous_theme: voyants
  source: ISO 2575 ; notice constructeur
```

Pour montrer un autre signal dans le feedback, ajouter `comparaisons` à la note :

```yaml
comparaisons:
- ref: a13b
  legende: 'Un piéton sur des bandes : passage pour piétons annoncé.'
```

`ref` réutilise le média d’une reconnaissance ; `legende` explique le détail visible et son sens.
Le build valide la référence et incorpore l’image au verso, près de l’explication (dans « Piège » pour une
reconnaissance). Aucun nouveau téléchargement ni carte supplémentaire. L’image principale reste seule au
recto ; une comparaison au verso n’exige pas d’avoir étudié l’autre signal. Pour tester la distinction,
utiliser une note `confusions`. Éviter les exemples supplémentaires qui ne changent pas la compréhension.
Le style partagé est dans `build/cards.css`, adapté du fichier de référence `essential.css` ; reconstruire
le paquet après une modification du style.

Sous-thèmes par thème (l’ordre est aussi celui de `SUBTHEME_ORDER` dans `build/build.py` ; un sous-thème
inconnu est signalé par un avertissement et trié en dernier) :
L : signalisation, priorites, vitesse, feux, marquages, panonceaux, balises, agents, croisement, positionnement,
depassement, stationnement, applications, panneaux (reconnaissances) · C : perception, distances, vigilance,
deficiences, applications · R : nuit, intemperies, autoroute, tunnels, passages_a_niveau, tramways, montagne,
chantiers · U : pietons, cyclistes, edpm, motos, poids_lourds, transports_commun, vehicules_prioritaires,
vehicules_lents_animaux · D : permis, points, sanctions, documents, controle_technique · A : proteger, alerter,
secourir, obligations, pas, applications · P : verifications, installation, quitter · M : tableau_de_bord,
voyants, freinage, pneus, feux, entretien, adas, depannage, applications · S : passagers, enfants, chargement,
equipements, applications · E : ecoconduite, pollution, ecomobilite, bruit · X : lecture.

Sous-deck d’une note : les reconnaissances et comparaisons de L vont dans « 01 Signalisation », le reste de L
dans « 02 Circulation », chaque autre thème dans son sous-deck. Étiquettes exportées : `type::`, `sous::`,
`parcours::socle|consolidation`, `objectif::`.

## Ce que le build vérifie

`python -m build.build --check` charge tout et s’arrête sur une **erreur** de structure : id absent ou
dupliqué, champ obligatoire manquant, thème inconnu, référence à une note inexistante (confusions, `image_ref`,
`dedup_ok`, objectifs, exclusions, registre des sources), numérotation de clozes non contiguë ou `rappels` mal
formés, même réponse sous deux numéros de cloze, affirmation identique à une autre, note absente des objectifs,
scénario dont la réponse déclarée (`check`) contredit le solveur de priorité. `import_signs.py` refuse de son
côté un signal retenu sans média ou une exclusion sans `raison`.

Il imprime ensuite des **avertissements à relire** : trous susceptibles de révéler une carte sœur,
réponses identiques, indices de style ou déséquilibre des verdicts, sous-thème inconnu. Ces signaux invitent
à relire ; ils ne justifient ni un quota de vrai/faux ni une modification artificielle du texte. `multi_ok`
et `dedup_ok` documentent les exceptions utiles. La longueur des réponses se juge sur la carte rendue,
sans seuil automatique ; les anciens champs `long_ok` sont sans effet.

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

## Commandes

```bash
source .venv/bin/activate
python -m build.build --check            # erreurs (bloquantes) + avertissements (à juger)
python -m build.build [--media] [--force-media]   # médias puis paquet et rapports ; --media s'arrête après les médias
python -m build.verify                   # import réel + réimport dans une collection temporaire
python -m unittest discover -s tests
python build/import_signs.py             # régénère data/reconnaissance/* (sauf voyants.yaml)
python build/yamlfix.py data/*/*.yaml    # quote les valeurs contenant ': '
python -m build.preview --ids id1,id2 [--night] [--width 430] [--out dossier]   # captures (Chrome headless ;
                                         # nécessite un build préalable ; --out est VIDÉ avant les captures)
python -m build.render_check             # toutes les faces, quatre tailles d'écran (~10 min, requirements-qa.txt)
python -m build.dedup [--threshold 0.62] # paires de notes textuellement proches (décision éditoriale, rien n'est modifié)
python build/qa_sheet.py                 # planches image + code + nom par fichier de reconnaissance -> out/qa/
```

## Modifier le deck

1. Définir la connaissance ou la décision visée et vérifier la règle **et ses conditions** dans une source
   primaire actuelle (voir [sources](sources.md)). Inscrire la consultation dans `data/_meta/source_checks.yaml` :
   `id`, `consulte_le` (date ISO), `url` (l’article ou la section sur Légifrance ou la fiche officielle, même si
   le texte a été lu dans `cdr.txt`), `portee` (ce qui a été vérifié, en une phrase) et `notes` concernées.
2. Écrire ou corriger la note dans `data/` (formats ci-dessus). Pour une reconnaissance : corriger
   `signs_inventory.yaml` ou `_meta/sign_overrides.yaml`, puis `python build/import_signs.py` ; retirer un
   signal = l’ajouter à `_meta/sign_exclusions.yaml` (`codes` de l’inventaire, `raison`, `couverts_par` = ids des
   cartes qui couvrent la règle), puis régénérer. `voyants.yaml` s’édite directement.
3. Relier la note à son objectif dans `_meta/objectives.yaml` (`notes` = socle, `consolidation` = suite).
   Retirer une note = la supprimer du fichier et de tous les registres (`objectives`, `source_checks`,
   `couverts_par`, `dedup_ok`) ; le build nomme ce qui a été oublié.
4. Pour un scénario d’intersection, déclarer `check` : le solveur (`build/priority.py`) doit être d’accord
   (deux scénarios sans `check` sont acceptés mais non vérifiés). Giratoires et scénarios de route sont relus
   à la main. Une modification de `diagrams.py` ou `gen_images.py` invalide les images générées au build suivant.
5. `python -m build.build --check`, lire les avertissements, puis `python -m build.build`, `python -m build.verify`
   et les tests. Regarder les cartes modifiées avec `build.preview` (une carte cloze donne `_c0`, `_c1`…). Pour
   une révision large, `python -m build.render_check` contrôle toutes les faces et écrit `out/RENDU.md` avec
   l’empreinte du paquet contrôlé : le lancer en dernier, après le build définitif. Un identifiant de capture
   absent du paquet fait échouer le contrôle ; actualiser `SAMPLES` si une note disparaît. Les mesures ne lisent pas le
   sens des images ni les petits textes incorporés : les inspecter.
6. Ajouter une ligne à [CHANGELOG](../CHANGELOG.md) et mettre à jour les effectifs du README.

## Identifiants et réimport

Les identifiants des types de notes et des decks sont fixes (`build/models.py`) et les GUID dérivent de
l’`id` de la note : réimporter une nouvelle version de la même édition met les notes à jour sans doublon et
conserve l’historique de révision. Il n’y a pas de migration entre éditions : renommer un `id`, renuméroter un
cloze ou changer la structure des champs crée de nouvelles cartes à l’import, à faire en connaissance de cause.
