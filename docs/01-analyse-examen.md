# Analyse de l'épreuve — ce que l'ETG teste vraiment (septembre 2026)

Synthèse de `docs/research/exam.md` (dossier sourcé, 180+ références) et conséquences pour la
conception du deck. Les chiffres sont ceux des textes en vigueur ; les divergences entre sources
sont listées dans le dossier, §6.

## 1. L'épreuve en bref

| | |
|---|---|
| Questions | 40, tirées au hasard dans une banque de 1 037 questions (renouvelée le 12 septembre 2023) |
| Seuil | 35 bonnes réponses (arrêté du 20 avril 2012, art. 2) ; 1 point par question, tout ou rien |
| Support | tablette (≥ 9 pouces) ou ordinateur, casque audio ; énoncé lu à voix haute |
| Temps | ≈ 20 s par question après la lecture orale (usage constaté, non fixé par les textes) ; ≈ 30 min au total ; 3 questions d'essai non notées avant |
| Médias | photos réelles depuis le poste de conduite, vues par drone, photos « autre usager » (trottoir, guidon de moto) ; ≈ 10 % de vidéos, vues une seule fois |
| Réponses | 2 à 4 propositions A/B/C/D ; le bandeau indique « Une réponse » ou « Plusieurs réponses » (2 ou 3 bonnes) |
| Thèmes | 10 familles : L circulation, C conducteur, R route, U autres usagers, D réglementation/divers, A porter secours, P prendre/quitter le véhicule, M mécanique/équipements, S sécurité passagers/véhicule, E environnement |
| Pondération (non officielle, concordante) | C ≈ 10, U 4-5, L 4, R 4, M 4, D 3-4, P 3, S 3, E 3, A 1 |
| Coût, validité | 30 € ; 5 ans, quel que soit le nombre de présentations à la pratique |
| Réussite | 49,3 % en 2025 (58,9 % en 1re présentation) ; en baisse continue depuis la banque 2023 |
| 2026 | arrêté du 16 avril 2026 : inscription au plus tard la veille, résultat ≥ 24 h après, identité vérifiée, appareils interdits, vidéosurveillance ; contenu inchangé |

## 2. Ce que montrent les 20 exemples officiels

La Sécurité routière a publié 20 questions réelles de la banque 2023 (transcrites dans le dossier, §3.1).
Elles révèlent la *mécanique* de l'épreuve mieux que n'importe quel cours :

1. **La forme dominante est le double OUI/NON** (11/20) : deux affirmations à juger sur une même photo,
   notées ensemble. L'examen ne demande pas « quelle est la règle ? » mais « cette affirmation sur
   cette situation est-elle vraie ? ». Exemples : « Un enfant perçoit les dangers de la même façon
   qu'un adulte : OUI/NON », « Cette passagère arrière met le conducteur en danger : OUI/NON »,
   « Si la victime n'est pas en arrêt cardiaque, l'utilisation du DAE peut être dangereuse : OUI/NON ».
2. **La moitié des questions portent sur la compréhension du risque, pas sur un article du Code** :
   vulnérabilité (trottinette : équilibre précaire, faible gabarit), détectabilité d'un piéton la nuit,
   zone où porter son attention, adhérence divisée par 2 sur sol mouillé et distance de freinage
   multipliée par 2, doses d'alcool plus généreuses à la maison qu'au bar, ceinture du passager arrière
   qui protège aussi le conducteur.
3. **Les chiffres tombent sous forme de jugement** : « La descente dangereuse commence à environ
   150 m : OUI/NON », « le passage à niveau se situe à environ : 50 m / 150 m ». Il faut connaître les
   distances d'implantation (150 m hors agglomération, 50 m en agglomération) et savoir lire où l'on est.
4. **Les panneaux sont interrogés par leur sens exact** (« Ce panneau annonce : une école / un endroit
   fréquenté par les enfants / un passage pour piétons » → réponse B) et par leur *portée* (« Cette
   limitation concerne les motards en inter-files : OUI ; les automobilistes : NON »).
5. **La mécanique est interrogée par ses conséquences** : « Ce voyant [ABS] reste allumé. Lors d'un
   freinage d'urgence, les roues risquent de se bloquer : OUI ; je dois m'arrêter immédiatement : NON ».
6. **Le point de vue change** (≈ 10 questions de la banque) : pictogramme jaune en haut à droite ;
   « je » est alors le piéton, l'enfant ou le motard.
7. **Les gestes de sécurité sont décrits avec précision** : « je regarde vers la droite le plus loin
   possible » (croisement de nuit), « je freine par intermittence et j'utilise le frein moteur »
   (descente), « je me replace à droite » (cycliste devant), « surveiller l'angle mort sur sa droite »
   (quitter un stationnement).

## 3. Conséquences pour le deck

**a. Apprendre les règles ne suffit pas ; il faut apprendre les *affirmations vraies et fausses*.**
Pour chaque connaissance, le deck formule la carte comme l'examen la posera : une affirmation à
juger ou une question à réponse précise, avec au verso le *pourquoi* en une ligne. Les cartes
« Question » du deck sont massivement de ce type (« Un enfant perçoit-il les dangers comme un
adulte ? → Non : champ visuel réduit, évaluation des vitesses impossible avant ~10 ans, impulsivité »).

**b. Le thème C (conducteur) est le premier poste de points (25 %) et le moins « scolaire ».**
Il combine des chiffres (distances, alcool, temps de réaction) et des raisonnements (vigilance,
perception, fatigue). Le deck lui consacre un sous-deck entier avec les tables de distances *et* les
raisonnements associés (pourquoi la distance de freinage est ×4 quand la vitesse est ×2).

**c. La signalisation et les priorités sont le deuxième poste, et le plus échoué.** Les formateurs
et les opérateurs (Codeclic, Dekra, Codes Rousseau) désignent priorités, signalisation temporaire et
distances de freinage comme les erreurs les plus fréquentes. Le deck : reconnaissance exhaustive des
panneaux (avec le *sens exact* et la *portée*), cartes de confusion sur les paires ambiguës, scénarios
d'intersection vérifiés par solveur.

**d. Les distances d'implantation et les « environ » doivent être sus par cœur** : 150 m / 50 m
(danger), présignalisation STOP et cédez-le-passage à 150 m, balises de passage à niveau 150/100/50 m,
triangle à 30 m, bornes d'appel tous les 2 km, chevrons, 2 secondes.

**e. Les mots-pièges sont une compétence à part** : « peux/dois », « obligatoirement », « uniquement »,
« le plus souvent », « sauf si », négations. Le sous-deck `00 Méthode` les entraîne, ainsi que les
conventions visuelles (bandeau, pictogramme, cadres jaunes) et la stratégie de réponse (sécurité
d'abord, rétroviseurs, klaxon, deux parties d'une question notées ensemble).

**f. Le vocabulaire de la banque 2023 est celui à employer** : « adhérence », « distance de freinage »,
« distance d'arrêt », « gabarit », « angle mort », « frein moteur », « feux de route », « inter-files »,
« chaussettes à neige », « assistance au stationnement », « DAE ». Le deck reprend ces termes tels quels.

**g. Ce que le deck ne peut pas faire** : lire une photo réelle en 20 secondes. C'est la compétence
que donnent les séries d'entraînement, à pratiquer en parallèle dès que les panneaux et les priorités
sont acquis (cf. README). Le deck rend chaque question *décidable* ; les séries rendent la décision *rapide*.

## 4. Risques d'obsolescence (à surveiller)

- Aucune nouvelle banque annoncée depuis septembre 2023 ; la DSR peut actualiser des diapositives
  silencieusement (ZFE, EDPM, ADAS).
- Directive (UE) 2025/2205 : transposition d'ici novembre 2028, application novembre 2029 ; elle
  ajoutera ADAS/conduite automatisée, recharge des VE, micromobilité, RCP, angles morts — déjà en
  grande partie couverts ici.
- Règles récentes déjà intégrées : permis à 17 ans (2024), mémo véhicule assuré (avril 2024), loi
  homicide routier et grand excès de vitesse = délit (2025), arrêté du 16 avril 2026.
