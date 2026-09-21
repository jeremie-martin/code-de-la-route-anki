# Bilan critique — v8, 21 septembre 2026

## Méthode

Relecture indépendante de la bibliothèque complète, sans présumer que les bilans précédents avaient raison :
lecture intégrale des 102 faits, des 322 questions, des 260 affirmations, des 50 scénarios et des 351
reconnaissances (signification, conduite, complément, piège) ; examen de cartes rendues (captures v7 puis v8) ;
contrôle du pipeline (validation, solveur de priorité, construction, imports réels, préréglage d’options) ;
contrôle en ligne de l’actualité de l’épreuve ; rapprochement des valeurs juridiques douteuses avec le Code de la
route consolidé du 10 septembre 2026 (`docs/research/sources/cdr.txt`).

## Ce qui a été trouvé sain

- **Exactitude.** Aucune valeur juridique fausse n’a été trouvée dans les cibles de rappel. Les points de doute ont
  été vérifiés dans le texte consolidé : le retrait de **9 points** pour le cumul alcool + stupéfiants existe bien
  (L235-1 IV, trois quarts du capital, par dérogation au plafond de 8 points de L223-2) ; les durées de rétention et de
  suspension administrative (L224-2) ; les qualifications gênant / très gênant de R417-10 et R417-11 (moto sur
  trottoir, borne de recharge, double file, zone de rencontre). Une seule explication était fausse : la lettre d’une
  route à accès réglementé (C107) ne vaut pas 110 km/h ; seules les chaussées séparées par un terre-plein central le
  permettent (R413-2). Corrigée.
- **Actualité.** L’arrêté du 16 avril 2026, appliqué au 1er juillet 2026, ne change que l’organisation de l’ETG
  (inscription close la veille, contrôle d’identité, pas de nouvelle tentative le jour même) : format, banque de
  septembre 2023 et seuil de 35/40 sont inchangés. Les règles récentes déjà intégrées (délit dès 50 km/h d’excès,
  ZFE maintenues, inter-files, EDPM en petite couronne) restent exactes.
- **Conception.** Les six tâches de rappel, la séparation recto / verso principal / références, les rappels de
  vitesse à cadre constant et les réponses de décision courtes (v7) fonctionnent à l’écran : rien n’a été réécrit.
- **Architecture.** Bibliothèque YAML → génération → paquet avec identifiants stables, ordre calculé, préréglage
  d’options, imports vérifiés, rendu contrôlé. Le solveur de priorité a validé les quatre nouveaux scénarios
  d’intersection sans désaccord.

## Problèmes constatés et décisions

| Problème | Décision |
|---|---|
| **Le critère de sélection des signaux (v6) n’était pas appliqué jusqu’au bout.** 41 signaux restaient alors qu’ils se déduisent d’un signal appris : sorties de zone (le panneau d’entrée barré de gris), fins de prescription rares (le signal barré), services au pictogramme transparent (croix rouge, tente, toilettes, fauteuil), catégories évidentes (bus, moto, camion, charrette, tracteur), variantes miroir ou jaunes (AK3a/b, KM1/KM2, CE30b, KD21), objets de chantier après le cône. Ils occupaient la phase « utile » sans décision propre. | **41 reconnaissances retirées**, chacune rattachée à sa couverture dans `sign_exclusions.yaml` (cinq groupes v8). Les archétypes de chaque convention restent appris : B51 pour les sorties de zone, B31/B33/B34/B40 pour les fins, CE2a/CE15a/CE15i/CE29/CE30a pour les services qui portent une décision, M4a/M4d1/M4d2/M4f pour les catégories, B7a/B7b et B9g/B9h pour la discrimination cyclomoteur / moto. 351 → 310 reconnaissances. |
| **Le sous-deck Méthode contenait des conseils sans cible de rappel** (« comment vérifier une réponse choisie vite », « comment choisir entre ralentir et maintenir ») et une question de contenu déguisée (pneus hiver / chaînes, doublon des cartes B26). Une carte révisée pendant des mois doit demander une connaissance. | Trois notes retirées et consignées dans `retirements.yaml` ; les conseils vivent dans le README et le repère du thème X. Les onze cartes conservées portent des faits de l’épreuve (bandeau, pictogramme de point de vue, halo, 20 s, pas de retour, notation tout ou rien, négations). |
| **Les scénarios laissaient des pièges fréquents sans image** : véhicule de droite qui tourne à gauche (le candidat croit que « tourner à gauche = céder »), intersection en T vue depuis la branche, sortie de parking vue par celui qui sort, cycliste venant de droite, giratoire avec un véhicule à une autre entrée (pas encore dans l’anneau), tourne-à-gauche alors qu’un véhicule me dépasse. | **Six scénarios ajoutés** (`scn-pd-droite-tourne-gauche`, `scn-t-moi-branche`, `scn-moi-sortie-parking`, `scn-pd-cycliste-droite`, `scn-giratoire-autre-entree`, `scn-dep-tourne-gauche-depasse`), images générées et relues, réponses vérifiées par le solveur pour les quatre intersections. 50 → 56 scénarios. |
| **Trois compétences de la banque 2023 n’avaient pas de carte** : freinage régénératif des électriques et hybrides, détecteur de fatigue, adaptation intelligente de la vitesse (ISA, obligatoire sur les voitures neuves depuis juillet 2024). | Trois affirmations (`aff-e-freinage-regeneratif`, `aff-m-detecteur-fatigue`, `aff-m-isa-panneaux`), rattachées aux objectifs `e-ecoconduite` et `m-aides`. |
| **Deux explications refusaient tout repère chiffré** là où les supports de préparation en donnent un que l’épreuve peut reprendre (régime de passage des rapports, arrêt moteur au-delà d’une trentaine de secondes). | Repères ajoutés dans l’explication, explicitement qualifiés de repères de supports de préparation et non de règles ; la réponse (cible de rappel) reste « suivre l’indicateur et la notice ». |
| Explication d’un scénario d’autoroute confondant voie d’entrecroisement et bande d’arrêt d’urgence ouverte aux heures de pointe. | Reformulée (voie auxiliaire sur signalisation lumineuse explicite). |

Effectif : **1 135 notes / 1 220 cartes → 1 100 notes / 1 185 cartes** ; socle 577 notes / 631 cartes. À 20 nouvelles
cartes par jour, l’introduction complète prend au moins 60 jours (socle : 32).

## Ce qui a été examiné et volontairement laissé tel quel

- **Les 263 affirmations.** Une dizaine de fausses propositions sont invraisemblables pour un adulte (« le 15, le 17
  et le 18 ne sont plus valables »). Elles sont conservées parce que l’épreuve pose ce type de proposition et que la
  justification au verso porte la nuance utile ; leur coût de révision est faible. Le risque de reconnaissance
  plutôt que de raisonnement reste accepté, avec la même parade qu’en v7 : répondre « pourquoi » à voix haute.
- **Les statistiques d’accidentalité et les délais administratifs** restent hors des cibles de rappel : ils changent
  chaque année et ne décident d’aucun comportement au volant. Deux questions de lecture (`d-risque-*`) apprennent à
  les interpréter.
- **L’ordre d’introduction** (méthode d’abord, entrelacement au prorata, signaux de priorité avant les scénarios,
  reconnaissance avant application) et le préréglage (20 nouvelles/jour, cartes sœurs enfouies) n’ont pas changé.
- **Les 50 comparaisons A/B et les 102 faits** : relus intégralement, aucune modification nécessaire.

## Ce que le deck ne fait pas

Il n’entraîne ni la perception sur photo ni la décision sous chronomètre : séries photo/vidéo et examens blancs
restent indispensables dès la première semaine. Il ne couvre pas la banque confidentielle : la sélection est
éditoriale. Il ne remplace pas une formation pratique aux gestes de secours.

## Vérification

- `python -m build.build --check` : 1 100 notes valides ; solveur de priorité en accord avec les 34 scénarios
  d’intersection vérifiables (dont les 4 nouveaux).
- `python -m unittest` : 18 tests réussis.
- `python -m build.verify` : import du Socle, du complet, passage Socle → complet et réimport sans doublon,
  historique et planification conservés, ordre importé identique au programme, préréglage d’options présent ;
  empreintes dans [VERIFICATION](../out/VERIFICATION.md).
- `python -m build.render_check` : toutes les faces à 430 × 932 (clair et sombre), 430 × 740 et 320 × 640,
  échantillon à 960 px ; résultat et empreinte dans [RENDU](../out/RENDU.md). Captures relues à la main : les
  images des six nouveaux scénarios, les versos de `scn-t-moi-branche`, `scn-dep-tourne-gauche-depasse`,
  `aff-m-isa-panneaux` et de la question sur les lettres de route corrigée (clair), la comparaison B15/C18 (sombre) ;
  les cartes inchangées depuis la v7 (rappels de vitesse, scénarios à trois véhicules) l’avaient été en v7.
- Contrôles du 21 septembre 2026 consignés dans `source_checks.yaml` (entrées `v8-*`) : arrêté du 16 avril 2026
  (organisation de l’ETG au 1er juillet 2026), L235-1, L224-2, R417-10 / R417-11, R413-2.

## Incertitudes

- Le retrait des 41 signaux repose sur un jugement de « déductibilité » : un candidat qui n’aurait pas compris la
  convention du panneau barré peut manquer une question sur une fin de prescription rare. Les archétypes conservés
  et la question sur les formes et couleurs sont censés l’empêcher ; ce n’est pas mesuré.
- Les six scénarios ajoutés sont des schémas simplifiés ; le solveur vérifie l’ordre de passage des intersections,
  pas le giratoire ni le scénario de dépassement, relus à la main.
- Aucune mesure de rétention ni de réussite à l’ETG n’a été réalisée ; aucun essai sur AnkiMobile ou AnkiDroid
  physiques. Les captures Chromium évaluent l’interface web d’Anki.
- Les amendes forfaitaires citées dans les explications (35 €, 68 €, 135 €) n’ont pas été revérifiées une à une en
  v8 ; les qualifications (classe, points, délit) l’ont été là où un doute existait.
