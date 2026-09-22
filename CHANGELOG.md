# Historique des éditions

## v14 (22 septembre 2026)

Relecture des images générées (code et rendus), puis deux relectures indépendantes : exactitude juridique au
Code consolidé du 10 septembre 2026, et transfert à l’examen avec comparaison au livre. 1 059 notes, 1 131 cartes.

- **Images, justesse** : le tramway et les véhicules longs attendaient en partie dans le carrefour, flèche dessinée
  sur la carrosserie ; ils ont désormais leur avant à la même distance que les voitures (`HALF_LENGTH`). Le bras
  levé de l’agent, invisible de dessus, se lisait comme un bras tendu : il est montré de face dans un médaillon.
  Ligne d’effet des feux fine et discontinue partout (elle était continue dans les scénarios) ; sas vélo limité à
  la voie de mon sens ; damier blanc avec la voiture du bon côté de la chaussée ; flèche directionnelle « tout droit »
  sans tige ; aire de livraison sans croix ni texte barré ; voyant de direction assistée avec son « ! » ;
  sens de rotation du giratoire en vraies flèches ; voiture qui me dépasse placée à ma hauteur.
- **Images, système** : « MOI » (voiture bleue cerclée) aussi dans les scènes de décision des questions ;
  inscriptions TRAM et SOS lisibles quelle que soit l’orientation ; gyrophare allumé qui rayonne ; légende de la
  zone masquée hors des hachures ; voies du giratoire à environ 1,5 largeur de voiture ; panneau jaune sans le
  mot « DÉVIATION », qui donnait la réponse.
- **Exactitude** : triangle au sol avant un cédez-le-passage (l’IISR le prévoit) ; feux de position admis pour une
  voiture en agglomération bien éclairée (verdict inversé) ; engin de service hivernal = facilités de passage ;
  seul le stationnement dangereux… et l’arrêt de nuit non éclairé retirent des points ; conduite accompagnée sans
  transfert automatique de points ; suspension préfectorale ; stationnement à gauche (R417-1) ; distances
  d’implantation « environ » ; source du retrait de 9 points ; références R412-10, R412-43-3 ; règle « 1,3 fois »
  pour les remorques retirée ; distance à l’arrêt en tunnel sans chiffres non sourcés, plots bleus.
- **Cartes** : réponses de scénarios qui répondent enfin à la question posée (STOP, feu vert) ; dix questions
  « oui/non » dont la vraie compétence est l’action deviennent « que faire ? » ; cinq faux verdicts formulés sans
  absolu révélateur ; virage à gauche/droite, verglas, incendie (extincteur), tourne-à-gauche précisés. Quatre
  doublons retirés (pluie et probatoire à 110, PLS, panneau d’agglomération). Neuf ajouts : placement pour tourner
  à gauche, arrêt le long d’une ligne continue, arrêt sur un pont, neige et plafonds, énergie d’un choc à 50 km/h,
  cycliste avant de tourner à droite, secours déjà sur place, ne pas transporter un blessé, désembuage.
- **Ordre** : champ `prerequis` ; un prérequis pas encore vu est avancé juste avant la note qui en dépend
  (arrêt/stationnement avant les panneaux B6, PTAC/PTRA avant les règles de remorque, évaluation avant la
  réanimation). Protéger les lieux et les définitions de masses passent au socle. 13 corrections orphelines
  retirées de `sign_overrides.yaml`.
- **Vérification** : `--check` sans erreur ni avertissement ; 25 tests ; import neuf et réimport Anki (`build.verify`) ;
  contrôle de rendu de toutes les faces (`out/RENDU.md`) ; inspection des 84 scènes et 63 images générées, et de
  cartes rendues à 390 px. Non mesuré : rétention ou réussite à l’ETG.

## v13 (22 septembre 2026)

Révision ciblée du deck et de ses objectifs, sans refonte des gabarits ni des images.

- **Distances** : apprendre la conversion vitesse × durée, puis l’appliquer avec une méthode explicite.
  Le rappel du carré des dizaines devient une question sur réaction + freinage ; un vrai/faux redondant
  est retiré. Le temps de réaction n’est plus présenté comme indépendant de la situation.
- **Règles et décisions** : rectos des vitesses de camions bornés à des cas précis, avec les exceptions
  pertinentes au verso ; profondeur des pneus distinguée des autres défauts interdits. Une nouvelle
  décision sur une hernie teste cette distinction ; vieillissement et recommandation du fabricant séparés
  d’une obligation légale. Consultations primaires et portée dans `data/_meta/source_checks.yaml`.
- **Parcours et documentation** : méthode de calcul et contrôle des pneus dans le socle, avant leurs
  applications ; conseils Anki condensés, règle de ponctuation arbitraire retirée, effectifs renvoyés aux
  rapports générés. Les signaux, comparaisons et scènes existantes sont conservés.
- **Vérification** : 24 tests réussis ; import neuf et réimport avec Anki 26.9.2 ; 9 064 faces/configurations
  contrôlées dans Chromium, sans échec ; inspection de neuf captures de cartes et scènes en clair/sombre,
  de 320 à 430 px. Les 371 médias sont identiques au paquet précédent. 1 054 notes, 1 126 cartes,
  dont 611 dans le socle. L’avertissement éditorial sur les questions oui/non (42 « non », 17 « oui »)
  est conservé : demander la justification reste nécessaire, sans fabriquer un quota de verdicts.

Le livre a servi de comparaison ponctuelle (sommaire, pneus et distances), sans fournir de contenu au
paquet. Cette passe ne constitue pas une nouvelle validation juridique de toutes les cartes ; elle ne
mesure ni rétention ni réussite à l’ETG. Résultats techniques de cette édition dans
`out/VERIFICATION.md` et `out/RENDU.md`.

## v12 (22 septembre 2026)

Révision d’ensemble à partir de deux relectures indépendantes (signaux ; règles et transfert à l’épreuve), puis
vérification adverse des modifications et comparaison des chapitres du livre non encore relus. 1 054 notes, 1 126 cartes.

- **Images** : les scènes de scénario sont exportées sur leur fenêtre utile (véhicules, flèches et panneaux
  environ une fois et demie plus grands sur téléphone) ; « MOI » est écrit dans la voiture ; un tramway a ses
  rails, une sirène et un feu jaune clignotant rayonnent ; les flèches d’intention s’arrêtent avant le centre du
  carrefour. Scènes de questions redessinées à l’échelle des scénarios. Corrections de sens : la scène « agent vu
  de profil » plaçait le conducteur sur l’axe barré ; voie d’insertion dessinée en sortie ; flèches vertes
  d’affectation de voie vers le haut ; triangles de ralentisseur à l’envers et trop nombreux ; plateau surélevé
  confondu avec un passage piéton ; bandes du passage piéton perpendiculaires à l’axe ; couloir bus à ligne
  continue ; panneau C25a sans la ligne 110. Les images de
  reconnaissance n’écrivent plus leur réponse (BAU, voie d’insertion, STOP, panneau AB3a, code R17) ; les
  marquages, gestes et vues en plan s’affichent en pleine largeur, les panneaux à taille de signal.
- **Contenu** : une phrase fausse corrigée (dépassement par la droite « interdit sur autoroute ») ; gilet imposé
  au seul conducteur ; emplacements matérialisés avant un passage piéton ; vitesses des autocars (R413-10) ;
  B8 (tonnage = PTAC), B9h (définition des motocyclettes), AB25 (clignotant), M12, B26, C107, triangle de
  présignalisation. Une trentaine d’explications réécrites pour énoncer le mécanisme ou la valeur attendue
  au lieu de mises en garde (galette, molette des feux, neige, frein moteur, climatisation, portée d’un panneau,
  panne de freins, remorquage, voyants…). Treize doublons retirés (sortie de parking, sortie de stationnement,
  camion en giratoire, pression à froid, voyant ABS, DAE, ligne jaune, insertion, quadrillage, B14…) ; quinze
  ajouts : moteur qui cale (direction et freins durcis), freinage d’urgence sans ABS, ne pas fumer sur les lieux
  d’un accident, contrôle des feux arrière, monoxyde de carbone en garage fermé, plaque illisible, sanction des
  distances de sécurité, fausse courtoisie envers un piéton, véhicule en feu dans un tunnel, limitation posée
  sur le support d’entrée d’agglomération, feux de gabarit d’un poids lourd la nuit, réattribution des points
  après dix ans, vidéo-verbalisation, feux de brouillard avant avec les feux de route, validité du titre de
  permis ; signaux B9i, M10b et C13b réintégrés ; paire A21/C20c retirée. Clozes dont l’énoncé
  donnait la réponse reformulées (téléphone 5 s, air/sang, balises J10, facteur de réaction).
- **Dépôt** : thème de cartes sans fixture ni test d’apparence figée ; prototypes archivés supprimés ; historique
  condensé ; médias obsolètes purgés au build ; carte des candidats visuels réduite aux décisions utiles.
- **Vérification** : `--check` sans avertissement, 24 tests, import et réimport Anki, contrôle du rendu de
  toutes les faces (`out/RENDU.md`), inspection à 390 px des scènes, marquages et cartes réécrites. Consultations
  consignées dans le registre. Non couvert : essai natif AnkiMobile/AnkiDroid, mesure d’efficacité, validation
  juridique exhaustive des notes non modifiées.

## v11 (22 septembre 2026)

Quinze passes ciblées après la v10, sans changement d’effectif notable (1 051 notes, 1 125 cartes) :

- **Contenu** : conditions décisives des règles de circulation (giratoires, sorties de parking, arrêt et
  stationnement, tunnels) ; voyants distingués selon contact ou roulage ; aides à la conduite décrites par leur
  fonction et leurs limites ; installation au poste de conduite et départ du véhicule ; secours alignés sur les
  références PSC de juillet 2026 ; corrections de fond (tabac avec mineur, grille Euro NCAP 2026, statut des
  ambulances, traversée des piétons, réinscription après invalidation). Trois questions issues de la comparaison
  avec le livre 2025–2026 (vitesses avec remorque, freins après lavage) ; sièges enfants recentrés sur R129.
- **Images** : scènes de décision dessinées pour l’approche d’un chantier, la flèche lumineuse de rabattement,
  le corridor de sécurité, le cycliste à droite, l’entrecroisement, la sortie de giratoire, les deux routes sous
  C107, le camion qui tourne à droite (avec schéma explicatif au verso) et le passage piéton masqué. Trois
  illustrations qui donnaient la réponse au recto retirées.
- **Présentation** : thème de cartes consolidé dans `build/cards.css` ; verso qui prolonge le recto ; volet
  « Sources » compact ; identifiants de champs et de gabarits figés ; préréglage FSRS (rétention 90 %, étapes
  `1m 10m`, révisions non plafonnées, cartes sœurs enfouies) ; formulations sans tirets cadratins.
- **Vérification** : `build.verify` étendu à la mise à jour d’un paquet précédent ; `build.render_check`
  compare recto et verso sur trois largeurs de téléphone.

## v10 (22 septembre 2026)

Révision ciblée de 150 notes pour rendre l’apprentissage autonome : les codes de panneaux et de marquages
laissent place aux indices visibles et aux décisions de conduite. Les références techniques restent dans
« Sources ». Les comparaisons A/B existantes sont conservées ; 40 notes montrent désormais au verso des
exemples supplémentaires légendés, à partir des médias déjà présents. Les questions sur les chaînes montrent
le panneau ; quelques sigles de secours, renvois opaques et points de vue ambigus sont reformulés.

Style Essential repris et consolidé dans `build/cards.css` : réponses bleu discret, feedback sans encadré,
espacement compact et modes clair/sombre. Documentation du champ `comparaisons`, contrôle des références et
vérification des images dans le paquet importé. 1 051 notes / 1 128 cartes, sans cartes supplémentaires.

Validation des données, 21 tests et import/réimport Anki réussis ; résultats du contrôle navigateur dans
[out/RENDU](out/RENDU.md), liés à l’empreinte du paquet. Captures inspectées : enfants/piétons, familles vélo,
marquages, chaînes et cartes de secours. Consultations juridiques ciblées consignées dans le registre ; cette
édition ne constitue pas une nouvelle vérification juridique exhaustive ni un essai sur téléphone réel.

## v9 (21 septembre 2026)

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

## v8 (21 septembre 2026)

Relecture complète ; 41 signaux déductibles retirés (sorties de zone, fins rares, pictogrammes transparents) ;
six scénarios de priorité ajoutés ; freinage régénératif, détecteur de fatigue et ISA ajoutés. 1 100 notes.

## v6 et v7 (21 septembre 2026)

101 signaux de catalogue retirés, compléments des reconnaissances resserrés, maxima de peine retirés ; règles
récentes reconsultées (délit dès 50 km/h, ZFE, inter-files, loi du 18 août 2026). Réponses des questions
réécrites en « décision + raison décisive », clozes à plusieurs trous scindées, cadre des vitesses.

## v5 et v5.1 (21 septembre 2026)

75 notes corrigées (sur-généralisations) ; contrôle du rendu de toutes les faces dans Chromium ; gabarits
refaits pour le téléphone (un seul volet de références, plus de consignes de notation au verso).

## v4 (21 septembre 2026)

Repères par thème, rappels indépendants (`rappels`), réutilisation des images de signaux dans les questions,
registres de familles de cas et de retraits.

## v3 et v3.1 (21 septembre 2026)

Manifeste d’objectifs reliant chaque note à une compétence, socle et consolidation, vérification par import
réel, premiers tests ; plafond de cartes introduit puis retiré.

## v2 (21 septembre 2026)

Type « affirmation » (vrai/faux justifié), programme d’introduction entrelacé, préréglage d’options embarqué,
premières limites de longueur, versos de reconnaissance resserrés.

## v1 (21 septembre 2026)

Bibliothèque initiale (896 notes), inventaire des signaux, générateur, solveur de priorité, images générées.
