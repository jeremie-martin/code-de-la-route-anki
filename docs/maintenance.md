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
                           gabarits) ; cards.css ; learning.py (objectifs, étapes, rapports) ; diagrams.py (scènes
                           de scénarios) ; gen_images.py (marquages, feux, gestes, scènes de questions) ; priority.py
                           (solveur) ; import_signs.py ; commons_fetch.py + commons_index.py (médias Wikimedia) ;
                           verify.py, preview.py, render_check.py, dedup.py, qa_sheet.py, yamlfix.py
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
(poppler) ; un article s’y cherche par son en-tête, par exemple `grep -n "^R. 415-5 " docs/research/sources/cdr.txt`.

## Format des notes

Champs communs : `id` (unique, minuscules, chiffres, tirets), `theme` (X L C R U D A P M S E ; X = méthode de
lecture de l’épreuve), `sous_theme` (voir la liste ci-dessous), `source`. Facultatifs : `image` (`{commons: nom
de fichier exact}`, `{gen: générateur, params: {…}}`, `tint: "#hex"` pour un voyant ISO), `image_ref` (une
note réutilise l’image d’une reconnaissance, qui la précède alors dans l’ordre), `prerequis: [ids]` (notes
à connaître avant celle-ci : une définition, une évaluation avant le geste qui en dépend), `debut: true` (base à
introduire avant tout le reste), `multi_ok`, `dedup_ok: [autre-id]` (exceptions assumées qui font
taire un avertissement). Les valeurs contenant « : » se mettent entre guillemets (`python build/yamlfix.py fichier`).

```yaml
# questions/
- id: l-priorite-droite-defaut
  question: Intersection sans panneau ni feu ; deux voitures arrivent en même temps. À qui dois-je céder le passage ?
  reponse: 'À celle qui vient de ma droite : sans signalisation, la priorité à droite s’applique.'
  explication: La largeur des rues ne décide pas de la priorité. Une sortie de parking, de chemin de terre ou d’accès non ouvert au public change la règle.
  theme: L
  sous_theme: priorites
  source: Code de la route, art. R415-5
  debut: true

# faits/ : un trou par phrase ; plusieurs cibles → rappels (un ordinal distinct par phrase, c1..c4)
- id: l-vitesse-agglo
  texte: En agglomération, la vitesse maximale par défaut est de {{c1::50 km/h}}.
  explication: Zone 30 : 30 ; zone de rencontre : 20 ; aire piétonne : allure du pas.
  theme: L
  sous_theme: vitesse
  source: Code de la route, art. R413-3

# affirmations/
- id: aff-l-stop-avancer
  contexte: Je suis arrêté à la ligne du STOP, mais des véhicules en stationnement masquent la rue transversale.
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

# scenarios/ : intersection : approaches N E S W (vehicle {colour, me, kind car|truck|bus|tram|moto|bike|pompiers,
# siren}, goes straight|left|right, sign stop|cedez|prioritaire|fin_prioritaire|priorite_droite|feu_vert|feu_rouge|
# feu_orange_clignotant…, private), branches [E, W, S] pour un T, agent bras_leve|bras_tendus_NS|bras_tendus_EW ;
# check {pair: [a, b, avant|apres|independant]} ou {order: [...]} est recalculé par build/priority.py.
# roundabout : vehicles [{pos: N|E|S|W|inside, angle, colour, me, goes}] ; road : lanes, axis, vehicles
# [{lane, y, colour, me, dir, goes, occludes}], extras (sign, retrecissement, passage_pieton, bau, label…), caption.
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

# reconnaissance/voyants.yaml (les autres fichiers sont générés) : type panneau|panonceau|balise|marquage|feu|geste|
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

Le `type` d’une reconnaissance règle aussi la taille de l’image sur la carte : panneaux, panonceaux, balises,
feux, voyants et pictogrammes s’affichent à la taille d’un signal ; marquages, gestes et vues en plan prennent
toute la largeur.

Pour montrer un autre signal dans le feedback, ajouter `comparaisons` à la note :

```yaml
comparaisons:
- ref: a13b
  legende: 'Un piéton sur des bandes : passage pour piétons annoncé.'
```

`ref` réutilise le média d’une reconnaissance ; `legende` explique le détail visible et son sens. Le build
valide la référence et incorpore l’image au verso, près de l’explication. Pour tester la distinction, utiliser une
note `confusions`. Pour un dessin au **verso** d’un fait, d’une question ou d’une affirmation, utiliser
`illustration` (`gen` ou `commons`, `params`, `width`, `legende` obligatoire, `signal: true` pour un signal à sa
taille de signal) : le média est ajouté à l’explication, sans nouveau champ ni nouvelle carte.

Où placer l’image : au **recto** quand elle pose la situation sans donner la réponse (la question cesse alors de
décrire ce que l’image montre) ; en `illustration` quand elle l’expliquerait ou la révélerait ; en `verso: true`
sur une image générée quand le même dessin doit se compléter au verso (lettres ou numéros au recto, noms au
verso, à la même place) : le build produit `<id>-verso` et la carte échange les deux sur place, sans
déplacement. Une image de reconnaissance n’écrit jamais sa réponse.

## Images générées

`build/diagrams.py` dessine les scénarios (intersections, giratoires, bandes de route) ; `build/gen_images.py`
dessine les marquages, feux, gestes de l’agent et les scènes ponctuelles des questions (`image.gen`). Tout
changement de l’un ou l’autre invalide les images au build suivant. Conventions communes :

- Même palette, mêmes silhouettes de véhicules ; « moi » est la voiture bleue cerclée de jaune, étiquetée MOI,
  dans les scénarios comme dans les scènes de décision des questions (`ME` dans `gen_images.py`) ; en scénario,
  toujours l’approche S (en bas, cap au nord). Les voitures des bandes de marquage ne sont que des repères.
  Les flèches montrent l’intention, partent de l’avant du véhicule et ne dessinent jamais une trajectoire de
  réponse. Tout véhicule qui attend a son avant à la même distance du carrefour (`HALF_LENGTH`), quelle que
  soit sa longueur ; les inscriptions (MOI, TRAM, SOS) restent lisibles quelle que soit l’orientation.
  Un tramway a ses rails, une sirène ou un gyrophare en service rayonne, un feu jaune clignotant aussi.
- Ce qui ne se voit pas de dessus ne se dessine pas de dessus : un bras levé est montré de face dans un
  médaillon relié à l’agent. Marquages transversaux : STOP continu large, cédez-le-passage discontinu large,
  ligne d’effet des feux discontinue fine (aussi pour le sas vélo).
- Les scènes sont dessinées sur un plan (600 × 600 pour les carrefours, 600 × 480 pour les routes) dont seule la
  fenêtre utile est exportée (`SVG.view`) : les véhicules, panneaux et flèches restent lisibles sur un
  téléphone. Une légende (`caption`) s’ajoute sous la fenêtre.
- Échelle : une voie vaut environ deux largeurs de voiture ; les scènes ponctuelles des questions reprennent
  cette proportion (`scale` des sprites). Les distances ne sont pas à l’échelle et les schémas ne sont pas des
  plans d’implantation.
- Déclarer les panneaux Commons d’une scène dans `params` avec `kind: sign` et `file` : ils sont attribués
  automatiquement dans `out/ATTRIBUTIONS.md`.
- Dessins pédagogiques (section « teaching » de `gen_images.py`) : une palette nommée (`INK` pour les étiquettes,
  `ANSWER` réservé au texte révélé par un verso, `WRONG` pour ce qu’il ne faut pas faire, `HIDDEN` hachuré pour ce
  qui est masqué, `VISIBLE` et `YELLOW` pour ce qui est vu ou le trajet de MOI, `SKIN`/`CLOTH`/`SEAT` pour les
  personnes et sièges) et des primitives partagées (`_text`, `_pill` sur fond chargé, `_tag`/`_slot` pour les
  étiquettes recto/verso, `_flash_rays` pour tout ce qui clignote, `pedestrian` (silhouette de piéton posée sur les plans, la même que dans les scénarios), `_car_side`, `_car_rear`,
  `_side_seat`, `_sign_png`). Réutiliser avant de créer ; une nouvelle couleur ou forme se nomme une fois.
- `build.build` affiche à la taille d’un signal les feux, panneaux et panonceaux dessinés (`SIGNAL_GENERATORS`)
  comme ceux des reconnaissances ; les autres dessins prennent la largeur de la carte.
- `tests/test_images.py` rend chaque image générée d’une carte : texte hors cadre, étiquettes qui se chevauchent
  (mesurées avec la vraie police) et verso de canevas différent du recto font échouer les tests. Il ne juge ni le
  sens ni la lisibilité : regarder la carte.

Pour relire une scène, suivre les coordonnées jusque dans les symboles partagés : gabarit des usagers, place
dans la voie, sens de circulation, branches et espace disponible avant une manœuvre ; distinguer les panneaux
montrés de face du plan routier. Puis regarder la carte rendue à taille réelle (`build.preview`) : l’absence de
débordement ne prouve ni la lisibilité ni la justesse de la situation.

## Sous-thèmes, sous-decks, étiquettes

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
scénario dont la réponse déclarée (`check`) contredit le solveur de priorité, reconnaissance dont les
`comparaisons` n’ont pas de `piege` (elles s’affichent dans son encadré). `import_signs.py` refuse de son
côté un signal retenu sans média ou une exclusion sans `raison`.

Il imprime ensuite des **avertissements à relire** : trous susceptibles de révéler une carte sœur,
réponses identiques, indices de style ou déséquilibre des verdicts, sous-thème inconnu. Ces signaux invitent
à relire ; ils ne justifient ni un quota de vrai/faux ni une modification artificielle du texte. `multi_ok`
et `dedup_ok` documentent les exceptions utiles. La longueur des réponses se juge sur la carte rendue.

`python -m unittest discover -s tests` couvre l’ordre, les objectifs, les gabarits, le solveur, le rendu des
clozes indépendantes et le vérificateur de rendu. `python -m build.verify` importe le paquet dans une
collection temporaire (contenu, médias, ordre, préréglage, identifiants de schéma) puis le réimporte ; avec
`--previous ancien.apkg`, il contrôle aussi la mise à jour d’un paquet déjà étudié.

## Ordre d’introduction

Calculé par `curriculum()` dans `build/build.py` et exporté comme position des nouvelles cartes :
cartes de méthode (X), puis les notes `debut: true`, puis toutes les pistes entrelacées au prorata de leur
taille (signalisation, circulation, chaque thème, scénarios). Dans une piste : sous-thèmes dans l’ordre de
`SUBTHEME_ORDER`, faits avant questions avant affirmations, puis ordre du fichier. Les reconnaissances
suivent `RECON_ORDER` (fichiers), chaque comparaison arrive après ses deux membres, les scénarios s’ouvrent
quand les signaux dont ils dépendent sont vus (`SCENARIO_GATES`). Toutes les notes du socle (`notes` dans
`objectives.yaml`) passent avant la consolidation ; les prérequis d’une note (`image_ref`, `prerequis`) pas encore
vus sont avancés juste avant elle (un prérequis d’une note du socle doit être au socle) ; les cartes sœurs d’un fait sont espacées de
`SIBLING_GAP` positions. `out/PROGRAMME.md` liste l’ordre obtenu.

## Commandes

```bash
source .venv/bin/activate
python -m build.build --check            # erreurs (bloquantes) + avertissements (à juger)
python -m build.build [--media] [--force-media]   # médias puis paquet et rapports ; --media s'arrête après les médias
python -m build.verify [--previous ancien.apkg] # import, réimport ; mise à jour depuis un paquet conservé
python -m unittest discover -s tests
python build/import_signs.py             # régénère data/reconnaissance/* (sauf voyants.yaml)
python build/yamlfix.py data/*/*.yaml    # quote les valeurs contenant ': '
python -m build.preview --ids id1,id2 [--night] [--width 390] [--height 700] [--out dossier]   # captures (Chrome ;
                                         # requirements-qa.txt ; nécessite un build préalable ; --out est VIDÉ avant)
python -m build.render_check             # toutes les faces, quatre tailles d'écran (~10 min, requirements-qa.txt)
python -m build.dedup [--threshold 0.62] # paires de notes textuellement proches (décision éditoriale, rien n'est modifié)
python build/qa_sheet.py                 # planches image + code + nom par fichier de reconnaissance -> out/qa/
```

## Modifier le deck

1. Définir la connaissance ou la décision visée et vérifier la règle **et ses conditions** dans une source
   primaire actuelle (voir [sources](sources.md)). Inscrire la consultation dans `data/_meta/source_checks.yaml` :
   `id`, `consulte_le` (date ISO), `url`, `portee` (ce qui a été vérifié, en une phrase) et `notes` concernées.
2. Écrire ou corriger la note dans `data/`. Rechercher aussi la règle dans les autres cartes et leurs
   explications : une bonne réponse au recto ne compense pas une généralisation fausse au verso. Une procédure
   qui dépend du véhicule (voyant, aide à la conduite, remorquage) précise son contexte ; une notice constructeur
   documente un véhicule, pas une règle universelle. Pour une reconnaissance : corriger `signs_inventory.yaml`
   ou `_meta/sign_overrides.yaml`, puis `python build/import_signs.py` ; retirer un signal = l’ajouter à
   `_meta/sign_exclusions.yaml` (`codes`, `raison`, `couverts_par`), puis régénérer. `voyants.yaml` s’édite directement.
3. Relier la note à son objectif dans `_meta/objectives.yaml` (`notes` = socle, `consolidation` = suite).
   Retirer une note = la supprimer du fichier et de tous les registres (`objectives`, `source_checks`,
   `couverts_par`, `dedup_ok`) ; le build nomme ce qui a été oublié.
4. Pour un scénario d’intersection, déclarer `check` : le solveur (`build/priority.py`) doit être d’accord.
   `private: true` modélise une sortie de parking ou un accès relevant de R415-9. Giratoires et scénarios de
   route sont relus à la main.
5. `python -m build.build --check`, lire les avertissements, puis `python -m build.build`, `python -m build.verify`
   et les tests. Regarder les cartes modifiées avec `build.preview` (une carte cloze donne `_c0`, `_c1`…), en
   clair et en sombre. Pour une révision large, `python -m build.render_check` contrôle toutes les faces et
   écrit `out/RENDU.md` avec l’empreinte du paquet : le lancer en dernier, après le build définitif. `SAMPLES`
   (dans `render_check.py`) choisit les captures ; un identifiant absent du paquet fait échouer le contrôle.
   Les mesures ne lisent pas le sens des images : les inspecter.
6. Committer avec un message qui résume les changements de contenu (git tient l’historique des éditions).

## Relecture complète avant publication

Relire **toutes** les notes, pas un échantillon, par chapitres (signaux ; circulation ; scénarios et route ;
conducteur et usagers ; réglementation, secours, prendre et quitter ; mécanique, passagers, environnement),
avec une même grille : exactitude au Code consolidé ou à une source officielle, contradiction avec une autre
carte (chercher le même sujet dans `data/`), conception de la carte ([conception](conception.md)), place au
socle et prérequis, images rendues à 390 px en clair et sombre. Classer chaque constat : **bloquant** (règle
fausse ou dépassée, contradiction, image contraire au texte, réponse ambiguë ou donnée au recto), **important**
(condition omise, doublon, carte sans valeur au socle, prérequis après son application), **mineur** (style).
Corriger les deux premiers, puis faire relire toutes les modifications ; publier quand cette dernière relecture
ne trouve plus rien de bloquant ni d’important. Les chiffres se comparent d’un coup en extrayant de `data/`
toutes les phrases qui contiennent des points, euros, km/h, mètres, durées ou seuils d’alcool.

## Identifiants et réimport

Les identifiants des types de notes et des decks sont fixes (`build/models.py`), ceux des champs et modèles
de cartes sont conservés dans `build/schema_ids.json`. Ne pas les régénérer : Anki les utilise pour reconnaître
une mise à jour de schéma. Les GUID dérivent de l’`id` de la note : réimporter une nouvelle version de la même
édition met les notes à jour sans doublon et conserve l’historique de révision. Renommer un `id`, renuméroter un
cloze ou changer la structure des champs crée de nouvelles cartes à l’import.

Le paquet est exporté sans progression : cartes nouvelles, aucun historique ni état mémoire FSRS. Le `due`
d’une carte nouvelle est sa position dans le programme, pas son identité. Le préréglage embarqué (collecte par
position croissante, cartes sœurs enfouies, rétention 90 %) s’importe au premier import puis se laisse décoché
aux mises à jour pour conserver les réglages personnels ; `build.verify` exerce ce parcours. Une note retirée du
dépôt reste chez les utilisateurs précédents : `build.verify --previous` la nomme, pour la signaler à la publication.
