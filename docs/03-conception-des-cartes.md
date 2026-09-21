# Conception des notes et des cartes

Ce document explique **pourquoi** chaque type de note existe, **quelle** connaissance il porte, et
**combien** de cartes il génère. Rien ici n'est laissé au hasard : une carte qui ne sert pas à
réussir l'épreuve n'a pas sa place dans le deck.

## 1. Le problème à résoudre

L'ETG n'est pas un examen de récitation : ce sont 40 photos/vidéos de situations réelles, 20 secondes
chacune, 35 bonnes réponses exigées. Une question mobilise presque toujours trois couches :

| Couche | Exemple | Apprenable avec Anki ? |
|---|---|---|
| **Reconnaître** un élément (panneau, marquage, feu, voyant, type d'usager) | « Ce panneau est un B6d » | Oui, parfaitement (image → sens) |
| **Rappeler** la règle ou le chiffre associé | « B6d = arrêt *et* stationnement interdits » ; « 80 km/h, 70 sous la pluie » | Oui, parfaitement (cloze / question) |
| **Décider** en appliquant la règle à la situation | « Donc je ne peux pas m'arrêter ici, même 1 minute » ; « Le véhicule à droite passe avant moi » | Partiellement : on entraîne le *raisonnement* (scénarios schématiques, cartes « si… alors ») ; la lecture de photos réelles reste à travailler sur des séries d'entraînement |

Le deck couvre **intégralement** les deux premières couches et **entraîne** la troisième avec des
scénarios générés et des cartes de décision. Il ne prétend pas remplacer les séries d'examens blancs :
le README indique comment articuler les deux (deck d'abord, séries en parallèle sur les dernières semaines).

## 2. Principes (dérivés des « 20 règles » de Wozniak et de la pratique des decks médicaux)

1. **Une carte = une connaissance atomique, une seule réponse attendue.** Pas de listes à réciter, pas de
   « citez les 5 cas… ». Les listes sont soit décomposées, soit posées comme *une* question à réponse
   courte (≤ 3 éléments) quand l'ordre lui-même est la connaissance (P·A·S).
2. **Le recto imite la forme de l'examen** quand c'est utile (« Dans cette situation, je… »), mais la
   réponse est toujours **spécifique** (pas de simple Oui/Non sans justification : le verso donne la
   décision *et* la règle qui la fonde).
3. **Sens unique par défaut.** Le sens de l'examen est *image/situation → signification/décision*. Les
   cartes inversées ne sont créées que là où elles servent la discrimination (voir « Confusion »).
4. **Pas de multiplication mécanique.** Une note Cloze ne porte plusieurs clozes que si elle décrit un
   *tableau naturel* (ex. vitesses par temps sec / pluie), chaque cloze étant un fait isolément testable ;
   maximum 4 clozes par note.
5. **Contexte minimal mais suffisant** : le recto contient ce qu'il faut pour que la réponse soit non
   ambiguë (type de route, agglomération ou non, conditions), jamais plus.
6. **Explication au verso** : une ligne de règle (« pourquoi »), et si utile le piège classique de
   l'examen. C'est ce qui transforme un fait mémorisé en décision transférable.
7. **Images de qualité et cohérentes** : panneaux vectoriels officiels (Wikimedia Commons, IISR),
   schémas générés avec une charte graphique unique, jamais de captures floues.
8. **Chaque note est traçable** : champ `Source` (article du Code de la route ou page officielle) et
   date de vérification, pour permettre les mises à jour futures.
9. **Étiquetage systématique** : thème officiel de l'ETG (L, C, R, U, D, A, P, M, S, E), sous-thème,
   type de connaissance, importance (`essentiel` / `utile` / `rare`). L'apprenant peut suspendre
   `importance::rare` s'il manque de temps.
10. **Un seul deck parent, des sous-decks par thème officiel** : les sites d'entraînement rendent des
    résultats par thème ; l'apprenant peut ainsi intensifier le sous-deck où il échoue.

## 3. Types de notes

### 3.1 `CDR Reconnaissance` (image → sens) — *1 carte par note*

Pour tout élément visuel à identifier : panneaux, panonceaux, balises, marquages, feux, gestes de
l'agent, voyants du tableau de bord, pictogrammes (médicaments, Crit'Air…).

Champs : `Id`, `Type` (panneau, panonceau, marquage, feu, balise, voyant, geste, pictogramme),
`Image`, `Nom`, `Signification`, `ConduiteATenir`, `Complement` (implantation, portée, fin), `Piege`,
`Source`.

Recto : l'image + « Que signifie ce {Type} ? ». Verso : nom, signification, conduite à tenir,
complément, piège. **Pas de carte inversée** : l'examen ne demande jamais de dessiner un panneau.

### 3.2 `CDR Confusion` (paire à discriminer) — *1 carte par note*

Pour les paires que les candidats confondent (B6a1/B6d, AB1/AB2, A13a/A13b, B15/C18, ligne
continue/dissuasion, feu orange fixe/clignotant…). Recto : les deux images côte à côte + « Quelle est la
différence ? ». Verso : chaque élément nommé, et la règle qui les distingue. Ces cartes ciblent
exactement l'erreur que ferait un candidat qui « reconnaît vaguement » — sans doubler toutes les cartes
de reconnaissance.

### 3.3 `CDR Fait` (cloze) — *1 carte par cloze, ≤ 4 clozes*

Pour les chiffres et règles à trous : vitesses, distances, taux d'alcool, points, amendes, délais, âges.
Champs : `Texte` (avec `{{c1::…}}`), `Explication`, `Image` (optionnelle), `Source`.
Règle d'écriture : la phrase entière doit rester vraie et compréhensible seule ; le trou porte sur
l'élément que l'examen demande (le chiffre, pas le libellé).

### 3.4 `CDR Question` (question → réponse courte) — *1 carte par note*

Pour les règles non numériques, procédures, définitions, décisions « si… alors » : « Feu orange fixe :
que dois-je faire ? » → « M'arrêter, sauf si je ne peux pas le faire en sécurité ».
Champs : `Question`, `Reponse`, `Explication`, `Image` (optionnelle), `Source`.

### 3.5 `CDR Scenario` (schéma → décision) — *1 carte par note*

Pour l'entraînement au raisonnement : intersections (ordre de passage), positionnement, dépassement,
stationnement, marquages. Le schéma est **généré** (SVG) à partir d'une spécification déclarative
(`data/scenarios.yaml`) : vue de dessus, véhicules colorés, panneaux, flèches d'intention. La réponse
attendue est **calculée par un solveur de priorité et vérifiée à la main** ; l'explication cite la règle.
Champs : `Image`, `Question`, `Reponse`, `Explication`, `Source`.

## 4. Ce qui est volontairement exclu

- Les cartes « nom → image » généralisées (inutiles pour l'épreuve, doublent le volume).
- Les questions d'histoire ou d'anecdote (date de création du permis…).
- Les panneaux de service ou de direction rarissimes qui n'apparaissent dans aucune banque
  d'entraînement (gardés seulement s'ils illustrent une règle : ex. couleurs des panneaux de direction).
- Les listes ouvertes (« citez tous les cas où… »).

## 5. Volumes visés

| Type | Notes | Cartes | Commentaire |
|---|---|---|---|
| Reconnaissance | ~300 | ~300 | ~220 panneaux/panonceaux/balises, ~35 marquages, ~15 feux/agents, ~25 voyants, ~10 pictogrammes |
| Confusion | ~40 | ~40 | paires ciblées |
| Fait (cloze) | ~200 | ~300 | 1 à 4 clozes par note |
| Question | ~300 | ~300 | |
| Scénario | ~70 | ~70 | intersections, dépassements, stationnement |
| **Total** | **~900** | **~1000** | ≈ 7 semaines à 20 nouvelles cartes/jour |

Ces chiffres sont des cibles de conception ; les volumes réels sont dans `out/STATS.md` (build du
21 septembre 2026 : 425 reconnaissances, 49 confusions, 127 faits / 326 cartes, 247 questions,
48 scénarios — 896 notes, 1 095 cartes). Écarts assumés : plus de reconnaissances que prévu (les
panonceaux et la signalisation temporaire sont couverts exhaustivement, les rares étant taggés
`importance::rare` pour pouvoir être suspendus), moins de notes à trous mais autant de cartes (2,6 clozes par note en moyenne ; beaucoup de
chiffres se retiennent mieux en question directe) et moins de scénarios (48 schémas couvrent toutes les
configurations de priorité et de dépassement décidables ; le reste relève des photos d'examens blancs).

## 6. Organisation du deck

```
Code de la route 2026
├── 00 Méthode d'examen            (fonctionnement de l'épreuve, pièges de lecture)
├── 01 Signalisation               (thème L : panneaux, panonceaux, marquages, feux, agents)
├── 02 Circulation                 (thème L : priorités, vitesses, positionnement, dépassement, arrêt/stationnement)
├── 03 Le conducteur               (thème C)
├── 04 La route                    (thème R)
├── 05 Les autres usagers          (thème U)
├── 06 Réglementation et notions diverses (thème D)
├── 07 Premiers secours            (thème A)
├── 08 Prendre et quitter son véhicule (thème P)
├── 09 Mécanique et équipements    (thème M)
├── 10 Sécurité du passager et du véhicule (thème S)
└── 11 Environnement               (thème E)
```

Tags : `theme::L` … `theme::A`, `sous::priorites`, `type::panneau`, `importance::essentiel|utile|rare`,
`nouveau::2023+` (règles ou panneaux récents, à ne pas confondre avec les anciennes versions).

## 7. Alternatives envisagées (et pourquoi elles ont été écartées ou limitées)

| Idée | Décision | Raison |
|---|---|---|
| Reprendre un deck existant et le « mettre à jour » | Écartée | Les decks publics mélangent des valeurs de 2010-2019 (90 km/h, 4 points piéton, vignette d'assurance, éthylotest obligatoire) sans source ; corriger coûte plus que reconstruire, et l'on hérite de leur structure (listes, cartes inversées). |
| Cartes « nom → image » pour tous les panneaux | Limitée aux cartes *Confusion* | L'examen ne demande jamais de produire un panneau ; la discrimination entre panneaux proches est mieux servie par une carte qui montre la paire. |
| Une note par thème avec 10-20 clozes | Écartée | Viole la règle « une carte = une connaissance » ; une note-tableau produit des cartes dont le contexte trahit la réponse ou, inversement, des trous impossibles à deviner. Maximum 4 clozes, seulement pour des tableaux naturels. |
| Occlusion d'image sur des photos réelles de situations | Écartée | Pas de banque de photos libres de droits calibrée sur l'examen ; les photos ambiguës créent des cartes contestables. Les scénarios sont donc des schémas générés, sans ambiguïté, vérifiés par un solveur. |
| Reproduire les 1 037 questions de la banque | Impossible et inutile | La banque n'est pas publique ; apprendre des réponses par cœur ne transfère pas à des photos différentes. Le deck vise les *connaissances* et les *raisonnements* qui rendent chaque question décidable. |
| Cartes Oui/Non calquées sur le format « double affirmation » | Transformées | Un simple Oui/Non se devine à 50 % et n'apprend rien ; chaque affirmation de l'examen devient une question dont la réponse contient la justification (« Non : champ visuel réduit, … »). |
| Tout inclure (504 signaux, tous les panonceaux de service) | Filtrée par importance | Les signaux rarissimes sont gardés seulement s'ils ont une image officielle et une signification propre, avec le tag `importance::rare` que l'apprenant peut suspendre ; les variantes sans valeur d'examen (sorties de zone de stationnement, cartouches obscurs) sont exclues. |
| Sous-decks par type de carte (panneaux / faits / questions) | Écartée | Les résultats d'entraînement sont donnés par thème ; les sous-decks suivent donc les 10 thèmes officiels, pour cibler ses faiblesses. |
| Générer les cartes directement avec un LLM sans base de données | Écartée | Pas de traçabilité ni de mise à jour possible ; ici chaque note vit dans un YAML sourcé, et le deck est régénéré de façon déterministe (ids stables). |
