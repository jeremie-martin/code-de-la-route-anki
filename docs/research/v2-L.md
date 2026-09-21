# Thème L — Circulation (sous-deck 02) : passage v2

Fichiers traités : `data/questions/02_circulation.yaml`, `data/faits/02_circulation.yaml`,
`data/affirmations/02_circulation.yaml` (créé). Aucun autre fichier modifié.
`python -m build.build --check | grep 02_circulation` ne renvoie plus rien (19 erreurs au départ).

## 1. Cartes supprimées → cartes créées

### 1.1 Cartes-listes découpées (erreurs du build)

| Id supprimé | Motif | Remplacé par |
|---|---|---|
| `l-priorite-droite-exceptions` | 53 mots, 8 cas | Q `l-sortie-parking-priorite` ; AFF `aff-l-chemin-terre`, `aff-l-zone-30-priorite-droite`, `aff-l-priorite-droite-rue-etroite` (l'insertion et le giratoire étaient déjà couverts par `l-insertion-autoroute-priorite`, `l-giratoire-vs-rond-point` et `scn-giratoire-cedez` — pas de `l-giratoire-entree-priorite`, contrairement à l'exemple du brief §3, pour ne pas tripler la connaissance) |
| `l-vehicules-prioritaires` | 49 mots | Rien : entièrement couvert par `u-vehicule-prioritaire-feu-rouge`, `u-ambulance-privee-sans-sirene`, `u-gyrophare-orange` (05) |
| `l-pieton-priorite` | 51 mots | AFF `aff-l-pieton-intention` (le chiffre et la règle restent dans le fait `l-passage-pieton-50m`) |
| `l-depassement-conditions` | 58 mots | Q `l-depassement-conditions` réécrite (les 3 conditions de R414-4) + Q `l-depassement-rabattement` |
| `l-depassement-interdit-lieux` | 5 éléments | même id, réponse réécrite sans virgules (visibilité / ligne continue / B3) |
| `l-route-3-voies` | 41 mots | AFF `aff-l-3-voies-gauche` et `aff-l-4-voies-double-sens` (la décision est déjà dans `scn-pos-trois-voies`) |
| `l-demi-tour-marche-arriere` | 47 mots | même id, resserré (autoroute / tunnel / ligne continue) ; la marche arrière « courte manœuvre » passe en explication |
| `l-stationnement-tres-genant` | 49 mots, 7 lieux | Q `l-stationnement-trottoir`, Q `l-stationnement-bande-cyclable` ; AFF `aff-l-5m-passage`, `aff-l-trottoir-moto` |
| `l-stationnement-genant` | 41 mots, 8 lieux | Q `l-double-file` (exemple du brief), Q `l-entree-carrossable` ; AFF `aff-l-bau-appel`, `aff-l-zone-rencontre-stationnement`, `aff-l-genant-fourriere` |
| `l-stationnement-dangereux` | 6 éléments | même id, transformé en décision située (sommet de côte) |
| `l-stationnement-hors-agglo-nuit` | 41 mots | même id, recentré sur le placement du véhicule (les feux restent dans `r-nuit-stationnement-feux`, 04) |
| `l-feu-rouge-clignotant` | 5 éléments | Rien : `feu-rouge-clignotant` (reconnaissance) porte la même signification et la même conduite |
| `l-feu-vert-conditions` | 42 mots | AFF `aff-l-feu-vert-priorite` |
| `l-formes-priorite-temporaire` | 48 mots | même id, resserré (4 formes) ; AB1/AB2 et les couleurs de direction passent en explication |
| `l-portee-prescription` | 45 mots | même id, resserré ; les zones passent en explication + AFF `aff-l-zone-30-portee` |
| `l-panonceau-portee` | 7 éléments | même id, resserré (4 précisions) |
| `l-agglomeration-panneau` | 44 mots | même id, resserré (4 règles) ; 50 m et bus en explication |
| `l-vocab-chaussee-voie` | 54 mots | même id, resserré (chaussée / voie / accotement) |
| `l-stop-arret` | 5 éléments après réécriture | même id, réponse sans virgules (où s'arrêter) ; le « même si rien ne vient » devient `aff-l-stop-rien-ne-vient` |
| fait `l-vitesse-engins` | « 25 km/h » sous c1 et c3 | même id, le VAE reprend `c1` (même réponse, même numéro) |

### 1.2 Doublons supprimés (la connaissance existe ailleurs à l'identique)

| Id supprimé | Déjà porté par |
|---|---|
| `l-cedez-vs-stop` | `conf-ab3a-ab4` et `conf-stop-cedez-lignes` (confusions) ; les deux pièges de décision deviennent `aff-l-stop-rien-ne-vient` et `aff-l-cedez-arret` |
| `l-depassement-cycliste-ligne-continue` | `scn-dep-cycliste-ligne-continue` (question et réponse identiques) ; l'exception « cycle/EDPM seulement » devient `aff-l-continue-cyclomoteur` |
| `l-depassement-vehicule-tourne-gauche` | `scn-dep-vehicule-tourne-gauche` (réponse mot pour mot identique) |
| `l-ligne-jaune-sens` | `marq-ligne-jaune-continue`, `marq-ligne-jaune-discontinue`, `marq-ligne-jaune-zigzag` ; la décision devient `aff-l-ligne-jaune-discontinue` |
| `l-feu-jaune-fixe` | `feu-jaune-fixe` (reconnaissance) ; remplacé par la paire `aff-l-jaune-accelerer` / `aff-l-jaune-trop-engage` |
| `l-feu-jaune-clignotant` | `feu-jaune-clignotant` (reconnaissance) + `scn-feu-orange-clignotant` |
| `l-feu-fleche-jaune` | `r16` (reconnaissance), qui porte aussi la différence flèche verte / flèche jaune |
| `l-feux-bus-tram` | `r17` (reconnaissance) |
| `l-signaux-affectation-voies` | `r21a`, `r21b`, `r21c` (reconnaissance) |
| `l-agent-bras-leve` | `agent-bras-leve` (même image générée, même réponse) |
| `l-agent-bras-tendus` | `agent-bras-tendu-face` + `agent-profil` |

`l-agent-ralentir-avancer` est **conservé** mais recentré sur le geste « ralentir », absent des cartes de
reconnaissance (qui ne couvrent que bras levé, bras tendus, profil et geste d'appel).

## 2. Ajouts, avec la ligne de `docs/02-carte-des-connaissances.md` visée

| Carte | Ligne visée |
|---|---|
| Q `l-sortie-parking-priorite` | L4 « à qui la priorité à droite ne s'applique pas (sortie de parking, chemin de terre…) » |
| Q `l-giratoire-placement` | L4 « carrefour à sens giratoire… position dans l'anneau ; clignotant » |
| Q `l-entrecroisement` | L4 « Voie d'insertion / d'accélération : pas de priorité ; entrecroisement » |
| Q `l-retrecissement-croisement` | L4 « Rétrécissement, obstacle de mon côté (je cède)… B15/C18 » et L6 « Croisement : obstacle de mon côté » |
| Q `l-sortie-stationnement` | L7 « Sortir d'un stationnement » / L9 (R412-10) |
| Q `l-depassement-rabattement` | L6 « retour sans gêner : je vois le véhicule dans mon rétroviseur intérieur » |
| Q `l-file-changement` | L6 « circulation en files (R412-24) » |
| Q `l-ligne-rive-franchir` | L2 « lignes de rive » + piège L12 « la ligne de rive continue ne peut jamais être franchie » |
| Q `l-clignotant-quand` | L6 « Clignotant : avant tout changement de direction/file, assez tôt » |
| Q `l-tourner-droite-serrer` | L6 « Je circule à droite » (piège du tourne-à-droite) |
| Q `l-vitesse-adaptee` | L5 « Vitesse "adaptée" : cas où il faut ralentir même sous la limite » |
| Q `l-stationnement-trottoir`, `l-stationnement-bande-cyclable`, `l-double-file`, `l-entree-carrossable` | L7 « Lieux interdits (liste décomposée) » |
| 48 affirmations `aff-l-…` | L4 (12), L3 feux (3), L6 dépassement (8) et positionnement (7), L6 croisement (2), L7 (8), L5 (6), L1 portée (2) |

Les affirmations reprennent les formes réelles de l'épreuve : double OUI/NON (`aff-l-vehicule-a-stop`
calquée sur la question officielle Q2), estimation de distance (`aff-l-implantation-agglo-50`, forme des
Q18/Q19), et les distracteurs « je maintiens ma vitesse » (`aff-l-croisement-depasseur-en-face`),
« puisque… » (`aff-l-zone-30-priorite-droite`, `aff-l-surdepassement`), « je peux » pour « je dois ».

### Décisions demandées mais volontairement non ajoutées (déjà couvertes)

- **Stationnement en pente** : `p-pente-roues` et `p-pente-vitesse` (08), comme le prévoit la carte des
  connaissances (« quitter le véhicule → thème S/P »).
- **Croisement de nuit** : `c-croisement-nuit-regard` (03, question officielle Q20) et
  `r-nuit-feux-croisement-route` (04).
- **B15/C18** : `conf-b15-c18` (confusions) et les deux cartes de reconnaissance ; seules la situation
  *sans panneau* (Q `l-retrecissement-croisement`) et le piège en situation (`aff-l-c18-priorite`) ont été ajoutées.
- **Feux de détresse** : fait `l-feux-detresse-usage` + `aff-r-…` (04) ; j'ajoute seulement
  `aff-l-detresse-pluie` (usage en roulant, non couvert).
- **« Je peux dépasser par la droite un véhicule qui tourne à gauche »** : déjà en question
  (`l-depassement-droite`) et en scénario ; une affirmation aurait fait une troisième carte.
- Trois affirmations rédigées puis retirées parce que les fichiers d'affirmations U et R écrits en
  parallèle portent la même connaissance : `aff-l-insertion-facilite` (→ `aff-r-insertion-prioritaire`),
  `aff-l-place-pmr` (→ `aff-u-place-pmr`), `aff-l-bus-hors-agglo` (→ `aff-u-bus-hors-agglo`).

## 3. Scénarios proposés (à ajouter par le solveur, `data/scenarios/`)

Aucun de ces cas n'est dessiné aujourd'hui :

1. **Entrecroisement** (`road`) — voie reliant une entrée d'échangeur à la sortie suivante ; je descends
   la bretelle, une voiture quitte l'autoroute sur la même voie. *Réponse* : celui qui change de voie
   cède ; on s'entrecroise en ajustant l'allure, la priorité à droite ne s'applique pas. *Article* : R421-3.
2. **Giratoire à deux voies, sortie lointaine** (`roundabout`) — je vise la 3e sortie. *Réponse* : entrée
   sur la voie de gauche au clignotant gauche, puis rabattement à droite en signalant avant la sortie.
   *Article* : R415-10 et R412-9.
3. **Rétrécissement avec B15 face à moi** (`road`) — passage à une voie, un véhicule en face.
   *Réponse* : je m'arrête avant le rétrécissement et je le laisse passer (flèche rouge = je cède).
   *Article* : R414-1 ; IISR (B15/C18).
4. **Tourne-à-droite avec deux-roues à ma droite** (`intersection`) — je tourne à droite, un motard
   remonte par la droite. *Réponse* : je me serre à droite assez tôt et je contrôle l'angle mort ; je ne
   tourne pas tant qu'il est à ma hauteur. *Article* : R412-9, R415-14 (si bande cyclable).
5. **Voie de présélection fléchée** (`intersection`) — je suis dans la voie « tout droit » et je veux
   tourner à gauche. *Réponse* : je suis la direction imposée par la flèche et je fais le tour ; je ne
   change de voie que tant que la ligne est discontinue. *Article* : R412-26.
6. **Feu vert + carrefour encombré** (`intersection`). *Réponse* : je reste en deçà de la ligne d'effet.
   *Article* : R412-33. (La question `l-intersection-encombree` existe, le schéma manque.)

## 4. Doutes et sources

- **Deux « tourne-à-gauche » face à face** : la v1 écrivait « ils se croisent par la droite », la carte
  des connaissances (L4) écrit « par la gauche ». Ni `legal-facts` ni `knowledge-facts` ne tranchent et
  aucun article ne le fixe. La phrase a été **retirée** de `l-tourner-gauche-regle` (brief §2.7 :
  une valeur non vérifiée ne va pas sur une carte). À trancher avant d'y revenir.
- **Sanction du non-respect d'une flèche directionnelle (R412-26)** : `knowledge-facts` L2 dit « 4e classe,
  4 points », `legal-facts` F7 dit « 2e classe ». `aff-l-voie-preselection` ne cite donc aucun montant.
- **Chaussée mouillée sans précipitation** : `legal-facts` A2 signale que le code n'abaisse la vitesse
  qu'« en cas de pluie ou d'autres précipitations », alors que les éditeurs enseignent « mouillé =
  vitesses pluie ». Aucune carte n'a été écrite sur ce cas ; seul `aff-l-probatoire-pluie-autoroute`
  (110 pour tous sous la pluie) a été retenu, sourcé R413-2 II + R413-5.
- **Durée du feu jaune (3 s / 5 s)** : non sourcée dans les dossiers (relecture v1, point 28) ; elle
  disparaît avec `l-feu-jaune-fixe`.
- **Gestes de l'agent la nuit (bâton lumineux, sifflet)** : `knowledge-facts` L8 les marque « À VÉRIFIER
  (convention des formateurs) » — aucune carte.
- **Losange « covoiturage »** : base réglementaire « À VÉRIFIER » — aucune carte (reste mentionné dans
  l'explication du fait `l-vitesse-peripherique`, inchangé).
- **Marche arrière en tunnel / rue à sens unique** : règle enseignée sans article dédié ; seules
  l'autoroute (R421-6) et la ligne continue sont affirmées dans `l-demi-tour-marche-arriere`.
- Les corrections de `review-facts-questions.md` sur ces fichiers (n° 4, 5, 6, 25 à 33) ont été
  conservées ou rendues sans objet par une suppression (n° 25 `l-cedez-vs-stop`, n° 27
  `l-depassement-cycliste-ligne-continue`, n° 28 `l-feu-jaune-fixe`, n° 29 `l-signaux-affectation-voies`).

## 5. Comptage final

| Fichier | v1 | v2 |
|---|---|---|
| `data/questions/02_circulation.yaml` | 46 notes | **42 notes** (19 supprimées, 15 créées) |
| `data/faits/02_circulation.yaml` | 24 notes / 53 cartes | **24 notes / 52 cartes** (1 cloze fusionné) |
| `data/affirmations/02_circulation.yaml` | — | **48 notes** (19 vrai / 29 faux = 40 % de vrai) |
| **Total thème L « circulation »** | 70 notes / 99 cartes | **114 notes / 142 cartes** |

Répartition par sous-deck (le build route les sous-thèmes `feux`, `agents`, `signalisation`,
`marquages` vers « 01 Signalisation ») :

- **02 Circulation** : 33 questions + 41 cartes de faits + 43 affirmations = **117 cartes**,
  auxquelles s'ajoutent les 48 scénarios (`priorites`, `priorites2`, `depassement`) → **165 cartes**.
- **01 Signalisation** : 9 questions + 11 cartes de faits + 5 affirmations = 25 cartes (portée des
  prescriptions, panonceaux, formes et couleurs, hiérarchie, implantation, feux hors service, geste « ralentir »).

L'objectif indicatif de 150-180 cartes hors scénarios n'est pas atteint dans le seul sous-deck 02
(117) : 19 cartes ont été supprimées comme doublons stricts de cartes de reconnaissance, de confusion
ou de scénarios déjà présents, et 25 cartes du thème partent vers le sous-deck 01. Ajouter des cartes
au-delà aurait obligé à redire une connaissance déjà portée ailleurs (brief §2.8).
