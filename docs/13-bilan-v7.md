# Bilan critique — v7, 21 septembre 2026

## Méthode

Relecture indépendante, sans hypothèse de continuité avec les bilans précédents : lecture intégrale des
faits, des questions, des affirmations, des scénarios et des comparaisons ; lecture des reconnaissances
d’interdiction et de marquage et de l’inventaire complet des signaux retenus ; mesure des longueurs de
réponse et de trou sur les données ; examen des cartes rendues (captures v6, puis captures v7) ; contrôle
du pipeline (validation, construction, import réel, ordre des nouvelles cartes, préréglage d’options) ;
contrôles en ligne des règles récentes. Chaque valeur juridique relue a été rapprochée du Code de la route
consolidé du 10 septembre 2026 (`docs/research/sources/cdr.txt`) lorsqu’un doute existait.

## Ce qui a été conservé, et pourquoi

- **L’architecture** (bibliothèque YAML → génération → paquet Anki avec identifiants stables, ordre calculé,
  préréglage d’options, vérifications d’import et de rendu) est saine et vérifiée ; elle n’a pas été
  réécrite. Le préréglage exporté est correct : `newGatherPriority = 1` correspond bien à « position la
  plus basse » et `newSortOrder = 1` à « ordre de collecte » dans la bibliothèque Anki 26.09.
- **Les six tâches de rappel** et leurs gabarits : rien de plus simple ne couvre reconnaître, discriminer,
  rappeler une valeur, décider, juger et lire une scène. Aucune carte inversée, aucune récitation.
- **La couverture** : les dix thèmes officiels, leurs distinctions utiles et les règles récentes
  (inter-files pérennisée par le décret n° 2025-33, délit dès 50 km/h d’excès depuis le 29 décembre 2025,
  ZFE maintenues, obligation locale casque + rétro-réfléchissant pour les EDPM à Paris et en petite
  couronne depuis le 7 août 2026) sont présentes et sourcées. Les sondages par mot-clé n’ont révélé aucune
  compétence de l’épreuve absente ; le format de l’ETG est inchangé en 2026 (40 questions, 35 justes).
- **La rédaction des affirmations** : contextes réalistes, fausses propositions plausibles, justification
  qui corrige ; lecture intégrale sans erreur de fond trouvée.

## Problèmes constatés et décisions

| Problème | Décision |
|---|---|
| **Réponses de décision trop longues pour un auto-jugement fiable.** Médiane de 25 mots par réponse de question, 153 réponses sur 322 au-delà de 25 mots, maximum 39 : la réponse mélangeait la décision, sa raison, une deuxième condition et une conséquence. À la révision, on reconnaît la réponse au lieu de la retrouver, et on ne sait plus ce qu’il fallait produire pour dire « Bon ». | Environ 190 réponses réécrites : **décision + raison décisive**, le reste transféré dans l’explication quand il n’y figurait pas déjà. Médiane 22 mots, maximum 30, 90 % sous 27 mots. La limite du build passe de 40 à 30 mots (`MAX_ANSWER_WORDS`), cible 10-22. Aucune condition nécessaire n’a été retirée : les nuances sont au verso, hors de la cible de rappel. |
| **Trous à conditions empilées** (« Voiture, hors probatoire, sous la pluie, visibilité d’au moins 50 m : autoroute normalement à 110 ou route à chaussées séparées, sans limite locale plus basse, plafond … »). Précis, mais illisible en révision quotidienne. | Les onze rappels de vitesse (routes, autoroute, pluie, probatoire) sont réécrits dans un cadre constant : `Conditions. Configuration → plafond {{valeur}}`. La réserve « sans limitation locale plus basse » vit dans l’explication. Huit autres trous de plus de 30 mots sont raccourcis (assurance, validité du permis, triangle, 5 m avant un passage, inter-files, deux traits, épisode de pollution, vitesse minimale). |
| **Nomenclature et maxima résiduels** : « Question officielle 2023 (Q18) » dans des justifications ; « jusqu’à 1 500 €, forfait 200 € » pour le détecteur de radars ; mention d’une « expérimentation 2020-2026 » pour le losange des voies réservées. | Reformulés (« un exemple public de question (2023) porte sur ce cas »), maxima retirés conformément à la règle de rédaction, mention d’expérimentation supprimée. |
| **Cinq signaux sans décision** encore présents : point d’information CE3a, restaurant CE16, hôtel CE17, voies de péage CE64a (péagiste) et CE64b (carte). | Retirés et documentés dans `sign_exclusions.yaml` (couverture : services avec décision, application `r-autoroute-peage`, télépéage C64d et flux libre C65a). 356 → 351 reconnaissances. |
| **Lacune mineure** : le signe distinctif « A » n’était mentionné que dans une explication, alors que sa durée est une question fréquente. | Une affirmation (`aff-d-disque-a-duree`), vérifiée sur R413-5 II et III. |
| **Test d’import fragile** : `build.verify` cherchait une chaîne littérale d’une carte, cassée par toute reformulation. | Le test vérifie désormais le trou lui-même (`{{c2::100 km/h}}`), stable tant que la valeur ne change pas. |

Effectif : **1 139 notes / 1 224 cartes → 1 135 notes / 1 220 cartes** ; socle inchangé (582 notes / 636 cartes).
À 20 nouvelles cartes par jour, l’introduction complète prend au moins 61 jours.

## Ce qui a été examiné et volontairement laissé tel quel

- **Affirmations vrai/faux (260)**. Une carte vrai/faux revue plusieurs fois peut être « reconnue » plutôt
  que raisonnée. Elles ont été conservées parce que l’épreuve elle-même demande de juger des propositions
  plausibles, parce que le recto exige une justification et parce que chaque fausse proposition est
  corrigée au verso. Le risque est réel mais accepté ; le remède est de répondre à voix haute au
  « pourquoi », comme le demande le README.
- **Part de la signalisation (412 cartes sur 1 220)**. Élevée, mais chaque signal restant porte une
  décision ou une discrimination que l’épreuve peut demander ; les variantes de familles et les
  pictogrammes transparents ont été retirés en v6 et v7. Les cartes de type de panneau directionnel
  (position, présignalisation, confirmation) sont gardées parce que la lecture de l’itinéraire décide du
  placement sur la chaussée.
- **Ordre d’introduction**. Méthode d’abord, puis entrelacement au prorata, signaux de priorité avant les
  scénarios, reconnaissance avant application. Le premier jour mêle déjà vitesses, dangers, voyants et
  seuils : c’est voulu (chaque journée est une tranche de l’épreuve), au prix d’un démarrage moins
  « thématique » que dans un manuel.

## Ce que le deck ne fait pas

Il n’entraîne ni la perception sur photo ni la décision sous chronomètre : séries photo/vidéo et examens
blancs restent indispensables dès la première semaine. Il ne couvre pas la banque confidentielle : la
sélection est éditoriale. Il ne remplace pas une formation pratique aux gestes de secours.

## Vérification

- `python -m build.build --check` : 1 135 notes valides, nouvelle limite de 30 mots comprise.
- `python -m unittest` : 18 tests réussis.
- `python -m build.verify` : import du Socle, du complet, passage Socle → complet et réimport sans
  doublon, historique et planification conservés, ordre importé identique au programme, préréglage
  d’options présent ; empreintes dans [VERIFICATION](../out/VERIFICATION.md).
- `python -m build.render_check` : toutes les faces à 430 × 932 (clair et sombre), 430 × 740 et 320 × 640,
  échantillon à 960 px ; résultat et empreinte dans [RENDU](../out/RENDU.md). Captures relues après
  réécriture : STOP, voie de bus, panne en tunnel, freinage ABS, disque A, vitesses hors agglomération,
  formes et couleurs des panneaux, losange au sol.
- Contrôles en ligne du 21 septembre 2026 : décret n° 2025-33 (inter-files), actualité service-public
  A19037 (EDPM Paris et petite couronne), nouveautés 2026 de l’ETG (Codes Rousseau : format inchangé) ;
  Code consolidé : R413-5, R414-5, R417-10. Consignés dans `source_checks.yaml` (entrées `v7-*`).

## Incertitudes

- Les 190 réponses réécrites ont été relues une fois chacune sur la donnée et, pour un échantillon, sur le
  rendu ; une nuance perdue dans une reformulation reste possible. Le verso conserve toujours
  l’explication d’origine, ce qui limite le dommage à la cible de rappel.
- Les reconnaissances de danger, obligation, indication, panonceaux, balises et voyants n’ont été relues
  que par leur inventaire (nom, importance) et par sondage, pas phrase par phrase en v7 ; la v6 les avait
  revues.
- Aucune mesure de rétention ni de réussite à l’ETG n’a été réalisée ; aucun essai sur AnkiMobile ou
  AnkiDroid physiques. Les captures Chromium évaluent l’interface web d’Anki.
- Les amendes citées (35 €, 68 €, 135 €) sont des forfaits ; elles n’ont pas été revérifiées une par une
  en v7, seuls les points, seuils et qualifications l’ont été là où un doute existait.
