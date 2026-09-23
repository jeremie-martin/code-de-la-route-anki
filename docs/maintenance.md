# Maintenance

## Structure du dépôt

```
data/                      bibliothèque de connaissances (YAML, une liste de notes par fichier)
  faits/NN_theme.yaml      clozes {{c1::…}} (texte, ou rappels = une phrase par trou)
  questions/NN_theme.yaml  question → réponse courte + explication
  affirmations/NN_theme.yaml  contexte (facultatif), affirmation, verdict vrai|faux, pourquoi
  scenarios/*.yaml         schémas générés (kind intersection|roundabout|road, spec) + question/réponse
  confusions/*.yaml        paires à discriminer (a, b = ids de reconnaissance)
  reconnaissance/*.yaml    image → sens : GÉNÉRÉS par build/import_signs.py (sauf voyants.yaml, écrit à la main)
  signs_inventory.yaml     inventaire des signaux (source des reconnaissances)
  _meta/objectives.yaml    objectifs : chaque note est dans `notes` (socle) ou `consolidation`
  _meta/lessons.yaml       un repère par thème (principe, exemple, transfert) → écran des sous-decks, REPERES.md
  _meta/sign_overrides.yaml corrections des reconnaissances générées (clé = id ; null retire un champ)
  _meta/sign_exclusions.yaml signaux de l’inventaire sans carte : codes, raison, couverts_par (ids)
  _meta/source_checks.yaml registre daté des consultations de sources (portée écrite, notes concernées)
build/                     build.py (chargement, validation, ordre, paquet) ; models.py (types de notes, gabarits) ;
                           cards.css ; learning.py (objectifs, rapports) ; diagrams.py (scènes) ; gen_images.py
                           (marquages, feux, gestes, dessins des questions) ; priority.py (solveur) ; import_signs.py ;
                           commons_fetch.py, commons_index.py (médias Wikimedia) ; verify.py, preview.py,
                           render_check.py, render_all.py, dedup.py, qa_sheet.py, yamlfix.py
assets/                    index Commons et icônes ISO des voyants ; cache des téléchargements (ignoré par git)
out/                       paquet, médias, rapports (STATS, PROGRAMME, COUVERTURE, REPERES, SELECTION-SIGNAUX,
                           VERIFICATION, RENDU, ATTRIBUTIONS)
docs/                      conception (ce que le deck optimise), méthode (comment le relire et le corriger),
                           maintenance (ce fichier), sources ; research/ : sources archivées et dossiers datés
tests/                     ordre, objectifs, gabarits, solveur, images, rendu des clozes, vérificateur de rendu
goal.md                    la demande initiale
```

Un fichier par thème et par forme (`02_circulation.yaml` … `11_environnement.yaml`, `00_methode.yaml` pour X).
À sous-thème égal, l’ordre du fichier est l’ordre d’introduction : placer une note près de celles de son
sous-thème. Les fichiers de reconnaissance sont organisés par famille de signaux (`RECON_ORDER`).

Installation : `uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt` (et
`requirements-qa.txt` pour les captures). Le premier `python -m build.build` télécharge ~300 fichiers Commons
(quelques minutes), puis tout est en cache. Le texte du Code consolidé, ignoré par git, se produit avec
`pdftotext -layout docs/research/sources/code_de_la_route_consolide_2026-09-10.pdf docs/research/sources/cdr.txt` ;
un article s’y lit avec `awk '/^R. 415-5 /,/^R. 415-6 /' docs/research/sources/cdr.txt`.

## Format des notes

Champs communs : `id` (unique, minuscules, chiffres, tirets), `theme` (X L C R U D A P M S E ; X = méthode de
lecture de l’épreuve), `sous_theme`, `source`. Facultatifs : `image`, `image_ref` (réutilise l’image d’une
reconnaissance, qui la précède alors), `illustration`, `comparaisons`, `prerequis: [ids]` (notes à connaître
avant), `debut: true` (base à introduire avant tout le reste), `multi_ok: true` (plusieurs trous voulus dans une
phrase : fait taire l’avertissement de `--check`), `dedup_ok: [id]` (paire proche assumée : retirée de la
sortie de `build.dedup`). Les valeurs contenant « : » se mettent entre guillemets
(`python build/yamlfix.py fichier`).

```yaml
# questions/
- id: l-priorite-droite-defaut
  question: Intersection sans panneau ni feu, routes ordinaires ; nous arrivons en même temps. À qui dois-je céder le passage ?
  reponse: 'À la voiture rouge, qui vient de ma droite ; la verte, à ma gauche, me cède le passage.'
  explication: Sans panneau, feu ni agent, la priorité à droite s'applique, quelle que soit la largeur des rues.
  theme: L
  sous_theme: priorites
  source: Code de la route, art. R415-5
  debut: true
  image: {gen: intersection, params: {approaches: {S: {vehicle: {colour: bleu, me: true}, goes: straight}, E: {vehicle: {colour: rouge}, goes: straight}, W: {vehicle: {colour: vert}, goes: straight}}}}

# faits/ : un trou par phrase ; plusieurs cibles → rappels (un ordinal distinct par phrase, c1..c4)
- id: l-vitesse-agglo
  texte: Du panneau d'entrée d'agglomération au panneau de sortie, la vitesse maximale par défaut est de {{c1::50 km/h}}.
  explication: 'Zone 30 : 30 ; zone de rencontre : 20 ; aire piétonne : allure du pas.'
  theme: L
  sous_theme: vitesse
  source: Code de la route, art. R413-3

# affirmations/
- id: aff-l-stop-avancer
  contexte: Je suis arrêté à la ligne ; les voitures stationnées masquent la rue transversale.
  affirmation: Je peux ensuite avancer lentement au-delà de la ligne pour voir avant de m'engager.
  verdict: vrai
  pourquoi: 'L’arrêt à la ligne est obligatoire ; une fois marqué, on progresse au pas jusqu’à voir, puis on cède le passage.'
  theme: L
  sous_theme: priorites
  source: Code de la route, art. R415-6

# confusions/ : a et b sont des ids de reconnaissance
- id: conf-ab3a-ab4
  a: ab3a
  b: ab4
  difference: 'A : céder le passage, sans arrêt obligatoire si la voie est libre. B : arrêt complet obligatoire, puis céder le passage.'
  theme: L
  sous_theme: panneaux
  source: IISR 3e partie

# scenarios/ : intersection : approaches N E S W (vehicle {colour, me, kind car|truck|lorry|bus|tram|moto|bike|
# pompiers}, goes straight|left|right, sign stop|cedez|prioritaire|fin_prioritaire|priorite_droite|feu_vert|…,
# private), branches [E, W, S] pour un T, agent, parked, queue, rails, narrow ; check {pair: [a, b, avant|apres|
# independant|indetermine]} ou {order: [...]} est recalculé par build/priority.py. roundabout : vehicles [{pos, angle, colour,
# me, goes}]. road : lanes, up_lanes, axis, lane_lines, vehicles [{lane, y, colour, kind, me, dir, occludes}],
# extras (sign, retrecissement, passage_pieton, sommet, bau, ilot, label…), caption.
- id: scn-pd-droite-tourne-gauche
  kind: intersection
  spec:
    approaches:
      S: {vehicle: {colour: bleu, me: true}, goes: straight}
      E: {vehicle: {colour: rouge}, goes: left}
  check: {pair: [S, E, apres]}
  question: "Intersection sans signalisation. Les véhicules suivent les flèches. Qui passe en premier ?"
  reponse: "La rouge : elle vient de ma droite."
  explication: "Priorité à droite (R415-5), quelle que soit la direction prise par le véhicule de droite."
  theme: L
  sous_theme: priorites
  source: "Code de la route, art. R415-5 et R415-4"

# reconnaissance/voyants.yaml (les autres fichiers sont générés) : type panneau|panonceau|balise|marquage|feu|geste|
# voyant|pictogramme|equipement ; champs nom, signification, conduite, complement, piege, code, question, source
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

## Images

**Où la placer** (principe dans [conception](conception.md)) :
- `image` au **recto** (`{commons: fichier}` ou `{gen: générateur, params: {…}}`) quand elle pose la situation
  sans donner la réponse ; la question cesse alors de décrire ce que l’image montre.
- `illustration` au **verso** (`gen` ou `commons`, `params`, `width`, `legende` obligatoire, `signal: true`
  pour un signal à sa taille de signal) quand elle expliquerait ou révélerait la réponse.
- `verso: true` sur une `image` générée quand le même dessin se complète au verso : lettres ou numéros au
  recto, noms au verso ; ou un tracé de réponse que le générateur ne dessine qu’au verso (`answer_on_back`).
  Le build produit `<id>-verso` et la carte échange les deux sur place, sans déplacement.
- `comparaisons: [{ref: id de reconnaissance, legende}]` montre d’autres signaux au verso ; pour une
  reconnaissance, elles s’affichent dans l’encadré « Piège », qui doit exister. Pour tester la distinction,
  utiliser une note `confusions`.

Le `type` d’une reconnaissance fixe la taille : panneaux, panonceaux, balises, feux, voyants, pictogrammes et
équipements à la taille d’un signal (comme les feux et panneaux dessinés de `SIGNAL_GENERATORS`) ; marquages, gestes et
plans sur toute la largeur. Les panneaux Commons placés dans une scène se déclarent `{kind: sign, file}` : ils
sont attribués dans `out/ATTRIBUTIONS.md`. Un fichier Commons se vérifie avant usage (modèle français en
vigueur, image non générée par IA) ; sinon, le dessiner.

**Dessins générés.** `build/diagrams.py` dessine les scènes (carrefours, giratoires, routes) ; `build/gen_images.py`
les marquages, feux, gestes et dessins des questions. Tout changement de l’un ou l’autre invalide les images au
build suivant. Conventions :
- Une seule palette et les mêmes silhouettes partout : « moi » est la voiture bleue cerclée de jaune, étiquetée
  MOI (`ME`), toujours sur l’approche S dans les scénarios ; un piéton est la silhouette `pedestrian` ; un
  poids lourd est `lorry` (environ 2,7 longueurs de voiture) ; `truck`, plus court, sert au petit porteur,
  à la dépanneuse et à l’engin agricole.
- Échelle : sur les routes et dans les dessins des questions, une voie vaut environ deux largeurs de voiture,
  bande d’arrêt d’urgence comprise (`scale` des sprites) ; les carrefours et giratoires des scénarios resserrent la
  voie (54 pour une voiture de 44) pour que tout le carrefour tienne à l’écran ; distances hors
  échelle, jamais des plans d’implantation. Un véhicule qui attend garde son avant à la même distance du
  carrefour, en deçà de sa ligne d’arrêt, qui reste visible. Les panneaux se placent du côté droit du sens de
  circulation représenté.
- Les flèches montrent l’intention et partent de l’avant du véhicule ; elles ne tracent pas une réponse. Tout
  ce qui clignote rayonne (`_flash_rays`) ; un tramway a ses rails. Les inscriptions (MOI, TRAM, SOS) restent
  droites quelle que soit l’orientation (`_upright`) ; une légende (`caption`) s’ajoute sous la fenêtre. Ce qui ne se voit pas de dessus se montre
  de face dans un médaillon (bras levé de l’agent). Transversales : STOP continu large, cédez-le-passage
  discontinu large, ligne d’effet des feux discontinue fine.
- Les scènes sont dessinées sur un plan (600 × 600 carrefours, 600 × 480 routes) dont seule la fenêtre utile est
  exportée (`SVG.view`).
- Dessins pédagogiques : palette nommée (`INK` étiquettes, `ANSWER` réservé au texte révélé au verso, `WRONG`
  à ne pas faire, `HIDDEN` hachuré pour ce qui est masqué, `VISIBLE`/`YELLOW` pour ce qui est vu ou le trajet de
  MOI, `SKIN`/`CLOTH`/`SEAT`) et primitives partagées (`_text`, `_pill`, `_tag`/`_slot`, `_flash_rays`,
  `pedestrian`, `_car_side`, `_car_rear`, `_side_seat`, `_sign_png`). Réutiliser avant de créer ; une nouvelle
  couleur ou forme se nomme une fois.

`tests/test_images.py` rend chaque image générée d’une carte : texte hors cadre, étiquettes qui se chevauchent
(mesurées avec la vraie police) et verso de canevas différent du recto échouent. Il ne juge ni le sens ni la
lisibilité : suivre les coordonnées d’une scène jusque dans les symboles partagés, puis regarder la carte
rendue à taille réelle.

## Sous-thèmes, sous-decks, étiquettes

Sous-thèmes par thème, dans l’ordre de `SUBTHEME_ORDER` (`build/build.py` ; un sous-thème inconnu est signalé
et trié en dernier) :
L : signalisation, priorites, vitesse, feux, marquages, panonceaux, balises, agents, croisement, positionnement,
depassement, stationnement, applications · C : perception, distances, vigilance, deficiences, comprehension,
applications · R : nuit, intemperies, autoroute, tunnels, passages_a_niveau, tramways, montagne, chantiers ·
U : pietons, cyclistes, edpm, motos, poids_lourds, transports_commun, vehicules_prioritaires,
vehicules_lents_animaux · D : points, permis, sanctions, documents, controle_technique, comprehension · A : pas,
proteger, alerter, secourir, obligations, applications · P : verifications, installation, quitter · M :
tableau_de_bord, voyants, freinage, pneus, feux, entretien, adas, depannage, comprehension, applications · S :
passagers, enfants, chargement, equipements, applications · E : ecoconduite, pollution, ecomobilite, bruit,
applications. Hors de cette liste : `panneaux` pour les reconnaissances et comparaisons de L (ordre
`RECON_ORDER`), `lecture` pour X (en tête).

Les notes de L dont le sous-thème est panneaux, panonceaux, balises, marquages, feux, agents ou signalisation
(`SIGNALISATION_SUBTHEMES`, `build/models.py`) vont dans « 01 Signalisation », quelle que soit leur forme ; les
autres notes de L dans « 02 Circulation » ; chaque autre thème dans son sous-deck. Étiquettes : `type::`, `sous::`, `parcours::socle|consolidation`,
`objectif::`.

## Ordre d’introduction

Calculé par `curriculum()` (`build/build.py`) et exporté comme position des cartes nouvelles : méthode (X), puis
les notes `debut: true`, puis toutes les pistes entrelacées au prorata de leur taille. Dans une piste :
sous-thèmes dans l’ordre, faits avant questions avant affirmations, puis ordre du fichier. Les reconnaissances
suivent `RECON_ORDER`, une comparaison vient `CONFUSION_GAP` signaux après le second de ses
membres (le lendemain environ : la paire se rappelle au lieu de se relire), un scénario après les signaux dont il
dépend (`SCENARIO_GATES`) et, pour le dépassement et le croisement, après les faits et questions de ce sous-thème
(`SCENARIO_RULE_GATES`). Le socle passe avant la consolidation ; les prérequis (`image_ref`, `prerequis`) sont
avancés juste avant la note (un prérequis d’une note du socle doit être au socle) ; les cartes sœurs d’un fait
sont espacées de `SIBLING_GAP` positions. `out/PROGRAMME.md` liste l’ordre obtenu.

## Contrôles et commandes

`python -m build.build --check` s’arrête sur une **erreur** de structure : id absent ou dupliqué, champ
obligatoire manquant, thème inconnu, référence à une note inexistante, clozes mal numérotés, même réponse sous
deux numéros, affirmation en double, note absente des objectifs, scénario dont `check` contredit le solveur,
comparaisons sans piège, prérequis hors socle pour une note du socle, thème absent du socle, repère incomplet,
exclusion sans raison, entrée du registre sans date valide, sans portée ou sans lien `https://`.
`import_signs.py` s’arrête de son côté sur un signal retenu sans image, une exclusion sans raison, ou un code
dupliqué ou inconnu. Il imprime ensuite des
**avertissements à relire** (trou susceptible de révéler une carte sœur, réponses identiques, déséquilibre des
verdicts…) : ils invitent à relire, sans quota ni longueur imposée ; `multi_ok` documente une exception.

```bash
source .venv/bin/activate
python -m build.build --check            # erreurs (bloquantes) + avertissements (à juger)
python -m build.build [--media] [--force-media]   # médias puis paquet et rapports
python -m build.verify [--previous ancien.apkg]   # import, réimport ; mise à jour depuis un paquet déjà importé
python -m unittest discover -s tests
python build/import_signs.py             # régénère data/reconnaissance/* (sauf voyants.yaml)
python build/yamlfix.py data/*/*.yaml    # quote les valeurs contenant ': '
python -m build.preview --ids id1,id2 [--night] [--out dossier]   # captures de cartes (--out est vidé avant)
python -m build.render_all dossier [--ids …] [--night]           # toutes les cartes dans l’ordre d’étude + dump.md
python -m build.render_check             # toutes les faces à trois tailles de téléphone, échantillon à 960 px (~10 min) → out/RENDU.md
python -m build.dedup [--threshold 0.62] # paires de notes textuellement proches (rien n’est modifié)
python build/qa_sheet.py                 # planches image + code + nom par fichier de reconnaissance → out/qa/
```

## Modifier le deck

Pour une relecture ou une série de corrections, suivre la [méthode](methode.md). Pour chaque modification :

1. Définir la connaissance ou la décision visée ; vérifier la règle **et ses conditions** dans une source
   primaire actuelle ([sources](sources.md)) ; inscrire la consultation dans `source_checks.yaml` (`id`,
   `consulte_le`, `url`, `portee` en une phrase, `notes`).
2. Écrire la note dans `data/`, puis chercher la même règle dans les autres cartes et leurs explications : une
   correction vaut pour tout le deck. Une procédure propre au véhicule précise son contexte. Pour une
   reconnaissance : corriger `sign_overrides.yaml` en gardant `signs_inventory.yaml` cohérent, puis
   `import_signs.py` ; retirer un signal = l’ajouter à `sign_exclusions.yaml`. `voyants.yaml` s’édite directement.
3. Relier la note à son objectif (`objectives.yaml`). Retirer une note = l’ôter du fichier et de tous les
   registres ; le build nomme ce qui a été oublié (retirer aussi l’id des `SAMPLES` de `render_check.py`,
   sinon ce contrôle et ses tests échouent). Reformuler une note plutôt que la supprimer : l’utilisateur
   garde son historique.
4. Un scénario d’intersection déclare `check` dès que le solveur modélise la situation (véhicules, panneaux,
   feux, agent ; pas les piétons ; modèle décrit en tête de `build/priority.py`) : le solveur doit être d’accord ;
   `private: true` pour une sortie de parking ou un accès (R415-9). Giratoires et routes se relisent à la main.
5. `--check`, build, `verify`, tests ; regarder les cartes modifiées (`build.preview`, clair et sombre). En fin
   de série, `render_check` sur le paquet définitif.
6. Committer avec un message qui résume les changements de contenu (git tient l’historique).

## Identifiants et mises à jour

Les identifiants des types de notes et des decks sont fixes (`build/models.py`) ; ceux des champs et modèles de
cartes sont conservés dans `build/schema_ids.json` : ne pas les régénérer. Les GUID dérivent de l’`id` de la
note : réimporter une nouvelle édition met les notes à jour sans doublon et garde l’historique. Renommer un
`id`, renuméroter un cloze ou changer la structure des champs crée de nouvelles cartes.

Le paquet est exporté sans progression. Son préréglage (collecte par position croissante, cartes sœurs
enfouies, rétention 90 %) s’importe au premier import, puis se laisse décoché pour garder les réglages
personnels. Avant de publier, `build.verify --previous` sur le paquet déjà importé contrôle la mise à jour et
nomme les notes retirées : elles restent chez l’utilisateur, à supprimer à la main (`Id:…` dans le navigateur).
L’utilisateur n’a pas encore étudié le deck ; il le supprimera et le réimportera une fois fini. Noter ici le commit
du paquet réimporté : c’est lui que `build.verify --previous` devra prendre ensuite
(`git show <commit>:out/Code-de-la-route-2026.apkg > /tmp/importe.apkg`).
