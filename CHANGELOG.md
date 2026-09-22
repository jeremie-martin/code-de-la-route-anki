# Planification et utilisation avec FSRS — 22 septembre 2026

- Instructions de premier import, d’activation de FSRS et de mise à jour sans écraser les réglages personnels.
  Distinction entre positions d’introduction, identités stables et échéances calculées ; aucune renumérotation
  nécessaire. Les paramètres FSRS restent ceux de l’utilisateur, sans historique livré avec le deck.
- Plafond de révisions porté de 400 à 9 999 pour laisser visibles les cartes dues ; enfouissement étendu aux
  cartes sœurs en apprentissage ayant franchi le changement de jour. Contenu et ordre d’introduction inchangés.
- Vérification du paquet vierge, de la collecte réelle et de réponses avec FSRS natif ; réimport sans
  préréglages conservant les options personnelles, les états mémoire et l’historique. Import neuf, réimport et
  mise à jour depuis le paquet Signal vérifiés ; 24 tests réussis. Aucun essai natif mobile ni mesure d’efficacité.

# Thème Signal — 22 septembre 2026

- Application du Signal approuvé dans `docs/signal-theme-handoff/` : CSS consolidé et comparé au rendu de
  référence, réponses de 21 px, texte de 19 px, séparateur jaune court, feedback sans panneaux remplis,
  sources compactes et fermées. Alias sombres indépendants et contraste des labels A/B corrigés.
- Le verso conserve les images et prompts du recto ; les trois prompts manquants sont restaurés dans les
  gabarits natifs. Clozes, contenu, médias, objectifs et ordre d’apprentissage conservés.
- Correction d’un défaut de reconstruction découvert lors de l’essai de mise à jour : les identifiants des
  champs et modèles de cartes étaient aléatoires. Ceux du paquet publié `67618d8` sont désormais fixes ;
  `build.verify --previous` vérifie aussi la mise à jour, sans toucher à une collection utilisateur.
- Les captures utilisent un viewport Chromium exact, sans artefact de taille de fenêtre. Le contrôle complet
  compare désormais images, prompts et typographie entre les faces ; largeurs de téléphone 320, 390 et 430 px.
- 24 tests réussis ; 9 042 faces/configurations et 4 521 comparaisons recto/verso sans échec. Import neuf,
  réimport et mise à jour du paquet précédent réussis, sans doublon ni perte de l’historique témoin.
  Inspection visuelle des six types en clair/sombre, avec exemples étroits et images de comparaison.
  Rapports liés au paquet livré (1 051 notes, 1 125 cartes) par SHA-256 ; AnkiMobile/AnkiDroid non testés.

# Installation et stationnement : décisions et conditions — 22 septembre 2026

- Douze notes améliorées : réglage des rétroviseurs après déplacement du siège, verrouillage du siège,
  miroirs jour/nuit, immobilisation en pente, contact coupé, enfant sans surveillance et prévention du vol.
  L’affirmation non étayée sur les bras croisés cède la place au contrôle du siège ; effectifs inchangés.
- Trois illustrations retirées : deux révélaient le réglage demandé, une représentait mal la pente.
  Suppression des deux générateurs désormais inutilisés ; autres médias et modèles conservés.
  Échantillon de captures recentré ; les mesures sur téléphone portent toujours sur toutes les cartes.
- Ch. 10 et 26 du livre relus, illustrations du ch. 10 inspectées ; consultations primaires délimitées dans
  le registre. Conception, maintenance et notes de recherche harmonisées.
- Paquet reconstruit : 1 051 notes, 1 125 cartes, 362 médias. 22 tests réussis, import et réimport Anki réussis ;
  absence des trois anciens médias vérifiée dans le paquet. Un avertissement de balance oui/non conservé
  après lecture : les réponses restent décidées par le fond, sans quota.
- Lecture des douze cartes modifiées à 430 px, quatre échantillons sombres à 320 px et exemples des six types.
  9 054 faces/configurations contrôlées sans échec ; `out/RENDU.md` et `out/VERIFICATION.md`
  identifient le même paquet par SHA-256.
  Pas de revalidation juridique exhaustive, d’essai natif mobile ni de mesure d’efficacité.

# Aides à la conduite : fonctions et limites — 22 septembre 2026

- Neuf notes précisées : régulateur simple/adaptatif, limiteur en descente, détection d’angle mort,
  maintien de voie, eCall et compatibilité avant un démarrage avec câbles. Le cas ACC teste une file
  arrêtée découverte quand le véhicule suivi change de voie ; les notices ne deviennent pas des règles universelles.
- Retrait d’un rappel AFU redondant ; comparaison AFU/AEB conservée et avancée dans son sous-thème.
  Aucun ajout de média ni changement des modèles. Paquet : 1 051 notes, 1 125 cartes ; effectif du socle inchangé.
- Ch. 15 du livre relu et ses quatorze illustrations inspectées ; sources primaires et portée consignées.
  Documentation de maintenance précisée et notes de recherche harmonisées sur les points modifiés.
- Vérification : 22 tests réussis ; import et réimport Anki réussis ; 9 260 faces/configurations
  contrôlées sans échec. Lecture des neuf notes corrigées et de la comparaison conservée à 430 px,
  échantillons sombres à 320 px et exemples des six types de cartes. Rapports liés au paquet par SHA-256.
  Pas de nouvelle validation juridique exhaustive, d’essai natif mobile ni de mesure d’efficacité.

# Voyants et traversées piétonnes — 22 septembre 2026

- Huit notes corrigées, sans ajouter de cartes : distinguer contact et roulage, pression et niveau d’huile,
  adapter la consigne de surchauffe au véhicule ; préciser les conditions de traversée des piétons.
  Le vrai/faux redondant sur les 50 m devient une application au carrefour.
- Les questions personnalisées de reconnaissance passent désormais par le même traitement de texte que
  les autres questions ; le contrôle d’import a révélé puis confirmé la correction de cette incohérence.
- Sources primaires consultées, comparaison ciblée du livre prolongée et maintenance précisée.
  Le livre commercial reste local, ignoré par Git ; aucun de ses médias n’est incorporé.
- Paquet reconstruit : 1 052 notes, 1 126 cartes. 22 tests réussis ; import et réimport Anki réussis.
  Inspection des huit notes modifiées à 430 px, avec échantillons sombres et à 320 px.
  Le rapport `out/RENDU.md` donne les résultats automatiques pour l’empreinte du paquet livré.
  Pas de revalidation juridique exhaustive, d’essai natif mobile ni de mesure de rétention.

# Comparaison avec le livre 2025–2026 — 22 septembre 2026

- Trois questions ajoutées : plafonds de vitesse avec remorque, distinction permis/PTRA dans un cas
  concret, vérification des freins après lavage. Choix du siège enfant recentré sur l’adaptation,
  la compatibilité et l’installation ; R129 n’impose pas toujours une fixation Isofix.
- Comparaison ciblée et décisions dans `docs/research/comparaison-livre-2025-2026.md` ; sources et limites
  de consultation consignées. Aucun texte ou média du livre intégré au paquet.
- Paquet reconstruit : 1 052 notes, 1 126 cartes. 22 tests réussis, import et réimport Anki réussis,
  9 234 faces/configurations contrôlées sans échec. Lecture visuelle des quatre notes modifiées,
  avec échantillons en sombre et à 320 px. Pas de validation native mobile ni de mesure de rétention.

# Circulation : conditions décisives — 22 septembre 2026

- Douze notes améliorées, sans ajouter de cartes : placement au giratoire selon l’axe d’entrée, signalement
  de la première sortie, sorties de parking et statut des voies, arrêt et stationnement, consignes de tunnel.
- La liste disparate des lieux de dépassement devient une décision à une intersection à priorité à droite ;
  la carte du passage piéton masqué teste désormais explicitement la vérification avant de dépasser.
  Les règles des passages à niveau et des tramways restent dans leurs cartes dédiées.
- Références consultées et portée consignées ; exemple de maintenance et sens du champ `private` clarifiés.
  Modèles, ordre, médias et effectifs conservés (1 049 notes, 1 123 cartes).
- Vérification : 22 tests réussis ; import et réimport réussis ; 9 202 faces/configurations contrôlées
  sans échec. Inspection des douze notes modifiées et d’exemples des six types de cartes ; contrôles visuels
  complémentaires en sombre et à 320 px. Aucun essai natif AnkiMobile/AnkiDroid ni mesure d’efficacité.

# Conditions et décisions — 22 septembre 2026

- Huit notes corrigées sans ajout de cartes : limites sous la pluie, documents de vente, accès au 114,
  remorquage, trois décisions d’écoconduite et comparaison des particules essence/diesel.
- Les régimes moteur et seuils de climatisation arbitraires cèdent la place au choix adapté à la situation ;
  les conditions manquantes et les références sont précisées. Consultations délimitées dans le registre.
- Structure, ordre et médias conservés ; maintenance complétée sur la cohérence entre cartes et explications.
- Vérification : 22 tests réussis, import et réimport réussis, 9 178 faces/configurations contrôlées sans échec.
  Lecture visuelle des huit notes corrigées et de signaux/scénarios représentatifs ; vérification ponctuelle en
  sombre et à 320 px. Rapports liés au SHA-256 du paquet. Pas d’essai AnkiMobile/AnkiDroid ni de mesure d’efficacité.

# Audit ciblé — 22 septembre 2026

- Corrections de fond : tabac/vapotage avec mineur, grille Euro NCAP 2026, statut des ambulances,
  conditions de traversée des piétons et délai de réinscription après invalidation.
- Cohérence : insertion sans recette « jamais s’arrêter », voyant de pression sans règle « rouge = toujours
  arrêt », ABS testé sur la perte d’antiblocage plutôt que sur une distance imprévisible.
- Apprentissage : cinq rappels de chiffres de campagne/angles de vision retirés ; les cartes de perception,
  distraction et somnolence gardent les principes et décisions. Pluie : hypothèse du modèle explicite.
  Plusieurs explications cessent d’affirmer un corrigé universel de l’ETG.
- Documentation ajustée ; sources consultées et portée consignées. Échantillon visuel élargi aux cartes
  corrigées ; import réel, réimport, tests et contrôle de toutes les faces relancés sur le nouveau paquet.
- 1 049 notes, 1 123 cartes ; modèles, médias et architecture conservés.

# Révision ciblée — 22 septembre 2026

- Secours : distinction malaise/traumatisme conforme au PSC juillet 2026 ; vomissements et analyse du DAE sans choc traités explicitement. Retrait de la prétendue exception « réponse attendue à l’examen ».
- Rappel : observation vidéo élargie aux indices stables et aux zones masquées ; formule de distance d’arrêt présentée comme raccourci ; contrôles de changement de voie expliqués par leur fonction.
- Maintenance : suppression des seuils de longueur et de taille des listes dans le lint ; conception condensée et statut des dossiers de recherche clarifié.
- Rendu : sept identifiants de capture obsolètes remplacés ; le contrôle refuse désormais un échantillon absent du paquet.
- Aucun ajout de cartes ni changement de modèle ; effectifs inchangés. Rapports d’import et de rendu régénérés avec le paquet.

# Historique des éditions

Les éditions v1 à v8 sont les jalons d’une même journée de travail (21 septembre 2026) ; les détails sont dans
l’historique git.

## v10 — 22 septembre 2026

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

## v9 — 21 septembre 2026

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
