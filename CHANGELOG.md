# Historique des éditions

Les éditions v1 à v8 sont les jalons d’une même journée de travail (21 septembre 2026) ; les détails sont dans
l’historique git.

## v9 — 21 septembre 2026 (édition actuelle)

Révision après deux séries de relectures indépendantes : qualité des cartes vue par l’apprenant, exactitude et
cohérence, couverture et structure, trajectoire du projet ; puis simulation de transfert à l’épreuve (131
questions de style ETG), vérification adverse des modifications et de l’ordre d’étude, test des procédures
documentées par un nouveau mainteneur. 1 051 notes / 1 128 cartes.

- **Erreurs corrigées** : les deux scénarios « agent, bras tendus » étaient inversés (dessin, solveur et
  réponses) ; feux de position seuls la nuit en ville (R416-6) ; freinage doublé sur route mouillée (réponse
  attendue à l’épreuve) ; B33 (110 = chaussées séparées) ; couloir bus (circuler ≠ stationner) ; sas vélo ;
  exceptions de R414-11 ; PLS après traumatisme ; 3PMSF avec M+S ; plusieurs sources mal citées.
- **Cartes non devinables** : les tournures qui prédisaient le verdict (« puisque » 8/8 faux…) sont réparties
  entre vrai et faux ; les questions oui/non à 84 % « non » deviennent des questions de décision ; rectos qui
  contenaient leur réponse, cartes contradictoires, réponses « voir la notice », résidus de relecture adressés
  au rédacteur, cadres télégraphiques des vitesses et inversions littéraires réécrits.
- **Retraits** (≈ 60 notes) : contraintes de l’interface d’examen, cartes d’épistémologie, exercices à données
  fixes et tableaux fictifs, doublons vrai/faux de faits déjà à trous, affirmations trivialement vraies ou
  invraisemblables, trivia administratifs, 15 signaux transparents ou variantes, 3 voyants.
- **Ajouts** : carré des dizaines, périmètre du permis B, PTAC / charge utile / PTRA, alcoolémie par verre,
  chiffres de campagne (téléphone × 3, SMS × 23, somnolence sur autoroute, alcool, jeunes conducteurs), permis AM
  à 14 ans, 125 cm³ avec le B, vitesses des poids lourds, prise de virage, champ visuel, ouïe, régulateur
  adaptatif, caméra de recul, ABS et DAE (exemples officiels Q5 et Q6), deux STOP face à face (Q2), dégagement
  d’urgence, piéton engagé, flèche jaune au rouge, klaxon en agglomération, ceinture en autocar, fumer avec un
  mineur, clignotant rapide. PLS et climatisation alignées sur la réponse attendue à l’épreuve.
- **Ordre** : bases d’abord (`debut: true`), sous-thèmes ordonnés explicitement (PAS avant les gestes, capital
  de points avant le reste de D), scénarios de dépassement et de croisement après leurs règles, une seule étape
  socle → consolidation (le champ `importance` disparaît). Les fichiers de questions « applications », « transfert »
  et « décisions » sont fondus dans les fichiers par thème.
- **Générateur** : le paquet Socle, la couche de compatibilité (ids de champs figés, `--previous`), le champ
  `Repere` copié sur chaque note, les étiquettes de provenance, les rapports ROLES/CONCEPTION et les registres
  `retirements`, `contrasts`, `interface_revision` sont supprimés ; les repères de thème vont sur l’écran des
  sous-decks ; les limites de longueur et de style deviennent des avertissements ; barrière K2 dessinée,
  rétrécissement dessiné dans les scénarios B15/C18.
- **Documentation** réduite à README, conception, maintenance, sources et cet historique.

## v8 — 21 septembre 2026

Relecture complète ; 41 signaux déductibles retirés (sorties de zone, fins rares, pictogrammes transparents) ;
six scénarios de priorité ajoutés ; freinage régénératif, détecteur de fatigue et ISA ajoutés. 1 100 notes.

## v6 et v7 — 21 septembre 2026

101 signaux de catalogue retirés, compléments des reconnaissances resserrés, maxima de peine retirés ; règles
récentes reconsultées (délit dès 50 km/h, ZFE, inter-files, loi du 18 août 2026). Réponses des questions
réécrites en « décision + raison décisive », clozes à plusieurs trous scindées, cadre des vitesses.

## v5 et v5.1 — 21 septembre 2026

75 notes corrigées (sur-généralisations) ; contrôle du rendu de toutes les faces dans Chromium ; gabarits
refaits pour le téléphone (un seul volet de références, plus de consignes de notation au verso).

## v4 — 21 septembre 2026

Repères par thème, rappels indépendants (`rappels`), réutilisation des images de signaux dans les questions,
registres de familles de cas et de retraits.

## v3 et v3.1 — 21 septembre 2026

Manifeste d’objectifs reliant chaque note à une compétence, socle et consolidation, vérification par import
réel, premiers tests ; plafond de cartes introduit puis retiré.

## v2 — 21 septembre 2026

Type « affirmation » (vrai/faux justifié), programme d’introduction entrelacé, préréglage d’options embarqué,
premières limites de longueur, versos de reconnaissance resserrés.

## v1 — 21 septembre 2026

Bibliothèque initiale (896 notes), inventaire des signaux, générateur, solveur de priorité, images générées.
