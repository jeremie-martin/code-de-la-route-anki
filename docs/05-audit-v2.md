# Audit de la version 1 et décisions pour la version 2 (21 septembre 2026)

Question posée : ce deck est-il, tel quel, le meilleur moyen de *réussir* l'ETG 2026 ? Réponse courte :
l'architecture est la bonne et ne change pas ; ce qui manque se situe au niveau des cartes elles-mêmes
et de l'ordre dans lequel on les apprend. Ce document liste ce qui a été constaté, ce qui est décidé,
et pourquoi.

## 1. Ce qui est juste et qu'on garde

- **Bibliothèque de connaissances en YAML → génération déterministe** (ids de notes, de types et de
  decks stables) : on peut corriger et régénérer sans perdre l'historique de révision. C'est la bonne
  façon de construire un deck qui doit rester à jour.
- **L'analyse de l'épreuve** (`01-analyse-examen.md`) part des 20 questions officielles de 2023, pas
  d'un manuel : les formes réelles (double OUI/NON, « je… », « environ 150 m », point de vue d'un
  autre usager) sont identifiées. C'est ce qui distingue « apprendre le code » de « passer le code ».
- **Cinq types de notes bien séparés** (reconnaissance, confusion, fait à trous, question, scénario),
  une carte par note sauf clozes, pas de cartes inversées.
- **Sources et vérification** : Code consolidé au 10/09/2026, dossiers de recherche, deux relectures
  contradictoires, solveur de priorité. Contrôle par sondage refait ici (L234-1 : 3 ans / 9 000 € ;
  R415-5 ; R412-19) : conforme.
- **Rendu** : panneaux vectoriels officiels, schémas générés lisibles, gabarit sobre, mode nuit ;
  import testé dans une collection vierge (896 notes, 1 095 cartes, 0 média manquant).

## 2. Ce qui empêche encore d'être « le meilleur deck possible »

### 2.1 Un tiers des cartes « Question » sont des fiches, pas des cartes
131 des 247 questions ont une réponse longue (> 45 mots) ou énumérative (4 à 13 éléments) :
« Dans quels cas la priorité à droite ne s'applique-t-elle pas ? » → 8 cas ; « Quels indices annoncent
un danger ? » → 9 indices ; « Quelles règles dans un tunnel ? » → 8 règles. Ces cartes :
- violent la règle n° 1 du projet (une carte = une connaissance) ;
- ne se notent pas honnêtement dans Anki (on se souvient de 5 éléments sur 8 : « bon » ou « à revoir » ?) ;
- ne ressemblent pas à l'épreuve, qui ne demande jamais une liste mais juge *une* situation :
  « Le véhicule A doit céder le passage : OUI/NON », « Je me replace à droite ».

**Décision** : chaque carte-liste est décomposée en cartes de décision (« Je sors d'un parking, un
vélo arrive de ma gauche : qui passe ? »), en affirmations à juger (voir 2.2) ou en faits à trous ;
les éléments sans valeur d'examen passent dans une explication. Plafond de validation : 40 mots de
réponse (le build refuse au-delà, sauf `long_ok: true` justifié).

### 2.2 La forme dominante de l'épreuve n'a pas de type de carte
11 des 20 questions officielles sont des affirmations à juger (« Un enfant perçoit les dangers comme un
adulte : OUI/NON », « Je dois m'arrêter immédiatement : OUI/NON »). La v1 les transformait en questions
ouvertes, ce qui est défendable mais ne fait pas travailler le réflexe attendu : lire une affirmation
plausible et la juger *avec sa raison*.

**Décision** : nouveau type `CDR Affirmation` (contexte facultatif + affirmation → **VRAI/FAUX** +
pourquoi en une ligne). Règles : une affirmation par carte ; les fausses sont *plausibles* (les
distracteurs réels de l'épreuve : « j'accélère », « je klaxonne », « je maintiens ma vitesse », « je
peux » pour « je dois ») ; équilibre vrai/faux par fichier ; pas de mots-signaux (« toujours », « jamais »)
qui trahissent la réponse. Un simple OUI/NON se devine à 50 %, mais la carte n'est « bonne » que si
l'on a su dire *pourquoi* — c'est ce que le verso impose.

### 2.3 Les versos de reconnaissance sont encombrés
Verso médian de 46 mots, 96 cartes au-delà de 80 mots. Cause principale : des phrases de catégorie
répétées sur chaque signal (« Sous le panneau qu'il complète, sur le même support ; il ne s'applique
qu'à ce panneau » × 76 ; « Implanté à ~150 m… » × 27 ; « Placé à l'endroit où commence l'interdiction ;
répété après chaque intersection » × 26 ; « En position devant le service… » × 22). L'information
utile (le sens exact, le piège) se noie.

**Décision** : ces phrases de catégorie sont retirées à l'import (`build/import_signs.py`) et portées
une seule fois par des cartes de règle (implantation des dangers, portée d'une prescription, portée
d'un panonceau — déjà existantes). Les versos restants sont resserrés (signification ≤ 25 mots,
conduite ≤ 20, complément ≤ 30 réservé à ce qui est propre au signal).

### 2.4 L'ordre d'apprentissage n'est pas un programme
Ordre des nouvelles cartes en v1 : 28 cartes de méthode (dont le prix de l'examen), puis 477 cartes
de signalisation, puis le reste. À 20 cartes/jour, « Le conducteur » (un quart des points) commence
vers le 30e jour ; les balises rares passent avant les panneaux de priorité essentiels.

**Décision** : le build calcule un **programme** : phase 1 = toutes les cartes `essentiel`,
entrelacées entre thèmes au prorata de leur volume (chaque jour est une tranche de l'épreuve entière),
prérequis respectés (panneaux de priorité avant les scénarios de priorité, marquages avant les
scénarios de dépassement) ; phase 2 = `utile` ; phase 3 = `rare`. Le paquet embarque un **préréglage
d'options** (20 nouvelles/jour, rétention souhaitée 0,9, ordre de présentation = position) pour que ce
programme s'applique sans réglage manuel.

### 2.5 Volume par thème décalé par rapport à l'épreuve
La route (R) : 33 cartes pour ~4 questions ; autres usagers (U) : 47 pour ~4-5 ; aides à la conduite
(ADAS) : 3 notes alors que trois des vingt questions officielles en relèvent (ABS, assistance au
stationnement, quitter un stationnement). Le conducteur (C) est bien couvert en chiffres, moins en
raisonnements sur le risque (la moitié des questions officielles).

**Décision** : compléter R, U, M-ADAS, C-risque, S, P à partir des dossiers de recherche, sous la forme
de l'épreuve (décision, affirmation), en restant rattaché à la carte des connaissances (`02-…`).
Objectif indicatif : R ≈ 70, U ≈ 80, M ≈ 90, C ≈ 130 cartes. Pas d'ajout hors carte des connaissances.

### 2.6 Le sous-deck « Méthode » contient des faits inutiles pour réussir
Prix (30 €), validité (5 ans), inscription J-1, nombre de questions de la banque (1 037), opérateurs,
âge minimum : ces cartes coûtent des révisions sans rapporter un point. Les cartes de *lecture*
(bandeau, pictogramme, halo jaune, « je peux / je dois », adverbes, vidéo, réflexe sécurité) sont, elles,
précieuses.

**Décision** : suppression des cartes administratives (l'information reste dans la description du deck
et le README) ; le sous-deck passe de 28 à ~12 cartes.

### 2.7 Divers
- Deux clozes d'une même note qui se soufflent la réponse (« 6 mois … 6 mois »), doublons entre faits
  et questions : contrôle automatique ajouté au build (mêmes valeurs répétées, réponses quasi identiques).
- Les corrections des relectures v1 ont été vérifiées comme appliquées (J1/J3 ajoutées, m8d/e/f, b58,
  m6i, giratoire/dépassement…). Le point « E31 lieu-dit » : la relecture proposait « fond blanc », le
  dossier signalisation et l'IISR disent fond noir, lettres blanches italiques — la carte est juste.

## 3. Ce qui a été envisagé et écarté (v2)

| Idée | Décision | Raison |
|---|---|---|
| Photos réelles de situations (occlusion, séries) | Non | Toujours pas de banque libre de droits ; l'ambiguïté d'une photo fait des cartes contestables. Les séries d'examens blancs restent le complément obligatoire (README). |
| Refondre les sous-decks par type de carte | Non | Les résultats des séries d'entraînement sont donnés par thème ; on garde les thèmes officiels. |
| Passer les reconnaissances en cartes inversées (nom → image) | Non | L'épreuve ne demande jamais de produire un panneau. |
| Réduire la signalisation aux seuls signaux « essentiels » | Non | Les signaux `utile`/`rare` restent, mais en fin de programme et suspendables par tag. |
| Un type de note « liste ordonnée » (P·A·S, ordre des contrôles) | Non | Trois cas seulement ; une question à réponse courte suffit. |

## 4. Mesure du résultat

Le build v2 échoue si : une réponse de question dépasse 40 mots sans `long_ok`, un verso de
reconnaissance dépasse 90 mots, une affirmation n'a pas de `pourquoi`, un fichier d'affirmations est
déséquilibré (moins de 35 % de vrai ou de faux), deux notes ont une réponse quasi identique. Les
statistiques (`out/STATS.md`) donnent la répartition par thème et par importance ; la cible est que la
phase « essentiel » tienne en ~6 semaines à 20 cartes/jour.
