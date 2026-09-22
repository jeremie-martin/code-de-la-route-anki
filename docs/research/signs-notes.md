# Notes de recherche sur la signalisation routière française (permis B / ETG)

Rédigé le 2026-09-21. Complète le dataset `data/signs_inventory.yaml` (≈ 500 entrées).
Les points marqués **À VÉRIFIER** n'ont pas été confirmés sur une source primaire.

## Sources utilisées

Wikipédia FR (les pages citent l'IISR (Instruction interministérielle sur la signalisation routière) et
l'arrêté du 24 novembre 1967 modifié ; le texte wiki brut a été récupéré via `action=raw`) :

- Danger (A) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_de_danger_en_France
- Priorité (AB) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_de_priorit%C3%A9_en_France
- Prescription (B : interdiction, obligation, fin, zonale) :
  https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_de_prescription_en_France et
  https://fr.wikipedia.org/wiki/Liste_des_signaux_routiers_de_prescription_en_France
- Indication (C) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_d%27indication_en_France et
  https://fr.wikipedia.org/wiki/Liste_des_signaux_routiers_d%27indication_en_France
- Services (CE) : https://fr.wikipedia.org/wiki/Liste_des_signaux_routiers_de_services_en_France
- Direction (D) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_de_direction_en_France
- Localisation (E, EB) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_de_localisation_en_France ,
  https://fr.wikipedia.org/wiki/Panneau_d%27entr%C3%A9e_ou_de_sortie_d%27agglom%C3%A9ration_en_France
- Panonceaux (M) : https://fr.wikipedia.org/wiki/Liste_des_panonceaux_de_signalisation_routi%C3%A8re_en_France ,
  https://fr.wikipedia.org/wiki/Panonceau_de_signalisation_routi%C3%A8re_en_France
- Balises (J) : https://fr.wikipedia.org/wiki/Balise_de_signalisation_routi%C3%A8re_en_France (+ pages J1, J3, J6, J10)
- Temporaire (AK, K, KC, KD) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_temporaire_en_France
- Passage à niveau (G) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_d%27un_passage_%C3%A0_niveau_en_France
- Feux (R) : https://fr.wikipedia.org/wiki/Feux_et_signaux_lumineux_routiers_en_France
- Signalisation dynamique (X, R21) : https://fr.wikipedia.org/wiki/Signal_sp%C3%A9cifique_%C3%A0_la_signalisation_dynamique_en_France
- Marquage : https://fr.wikipedia.org/wiki/Signalisation_routi%C3%A8re_horizontale_en_France ,
  https://fr.wikipedia.org/wiki/Ligne_d%27effet_de_feux_en_France , https://fr.wikipedia.org/wiki/Sas_v%C3%A9lo ,
  https://fr.wikipedia.org/wiki/Marquage_d%27un_ralentisseur_en_France , https://fr.wikipedia.org/wiki/Marquage_du_stationnement_en_France
- Généralités (formes, couleurs, familles) : https://fr.wikipedia.org/wiki/Panneau_de_signalisation_routi%C3%A8re_en_France
- Zones : pages « zone 30 », « zone de rencontre », « aire piétonne », « zone d'obligation d'équipements en période hivernale (B58/B59) »

Légifrance :

- Arrêté du 24 août 2020 (expérimentation voies réservées, losange) : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000042283775/
- Arrêté du 5 avril 2024 (modif. voies réservées) : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049424783
- Arrêté du 28 juillet 2026 (prolongation « six ans et trois mois ») : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054728626
- Arrêté du 23 septembre 2015 (mobilités actives : M12 généralisé, etc.) : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000031285676
- Arrêté du 12 décembre 2018 (A9a, C20b) : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000037964816
- Arrêté du 13 juin 2022 (décompteur piétons, R12m) : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046014040

Wikimedia Commons : liste des fichiers `France road sign *.svg` (737 fichiers) récupérée par l'API `allpages` ;
descriptions de fichiers consultées pour K10a/K10b, C65a/b/c, C109/C110, SR3x, M9k/M9l, M9v3/v4, B56/B57.

Documents officiels non accessibles pendant la recherche (URL CEREMA en 404) : « Liste complète des signaux routiers
en usage » (annexe de l'arrêté de 1967, PDF CEREMA juin 2021) et les parties 1 à 9 de l'IISR. Refaire cette vérification si un
doute persiste.

## 1. Formes et couleurs : la grammaire des panneaux

| Forme / couleur | Famille | Exemples |
|---|---|---|
| Triangle blanc bordé de rouge, pointe en haut | Danger (A), annonce de priorité (AB1, AB2, AB25) | A1a, A13a, AB1 |
| Triangle **jaune** bordé de rouge | Danger temporaire (AK) | AK5 travaux |
| Triangle pointe en bas | Cédez le passage (AB3a, AB3b), STOP à 150 m (AB5), panonceau M12 | AB3a |
| Octogone rouge | STOP (AB4), unique | AB4 |
| Losange (carré sur pointe) jaune bordé de blanc | Route à caractère prioritaire (AB6) ; barré = fin (AB7) | AB6 |
| Rond blanc bordé de rouge | Interdiction (B) | B14, B3, B12 |
| Rond rouge à barre blanche | Sens interdit (B1) | B1 |
| Rond bleu bordé de rouge à barre(s) rouge(s) | Interdiction de stationner (B6a1) / d'arrêt et stationnement (B6d) | B6a1, B6d |
| Rond bleu, symbole blanc | Obligation (B21, B22, B25, B26, B27) | B21b, B22a |
| Rond blanc bordé de noir, barre noire oblique | Fin d'interdiction (B31, B33, B34, B35, B39) | B33 |
| Rond bleu, symbole blanc barré de rouge | Fin d'obligation (B40 à B49) | B40, B43 |
| Rectangle blanc bordé de rouge, mention ZONE + rond ou pictogrammes | Entrée de zone (B30, B6b, B56, B58) | B30 |
| Rectangle blanc bordé de noir, symbole grisé barré | Sortie de zone (B51, B50, B57, B59) | B51 |
| Carré bleu à listel blanc, pictogrammes blancs | Zone de rencontre (B52) et aire piétonne (B54) ; barré de rouge = sortie (B53, B55) | B52, B54 |
| Carré / rectangle bleu, symbole blanc | Indication (C) : information, parfois avec règles associées | C12, C18, C27, C111, C207 |
| Carré blanc bordé de bleu, pictogramme noir | Services (CE) | CE15a carburant, CE2a SOS |
| Rectangle bleu (direction) | Autoroute / mentions desservies par autoroute | D21, D61 |
| Rectangle vert (direction) | Grande liaison (pôle vert) par route ordinaire | D21 |
| Rectangle blanc (direction) | Itinéraire local | D21 |
| Rectangle jaune (direction ou indication) | Temporaire : déviation, chantier (KD, KC) | KD22, KC1 |
| Rectangle marron | Touristique / culturel (H, D marron, E33) | H10 |
| Rectangle blanc bordé de rouge, lettres droites | Entrée d'agglomération (EB10) ; barré = sortie (EB20) | EB10 |
| Rectangle noir, lettres blanches italiques | Lieu-dit, cours d'eau (E31, E32) : pas d'agglomération | E31 |
| Petit rectangle blanc sous un panneau | Panonceau (M) : complète le panneau du dessus uniquement | M1, M2, M4, M9 |
| Cartouche rouge / jaune / blanc / vert | Numéro de route : A ou N (rouge), D (jaune), C/VC (blanc), E (vert) | E42, E43 |
| Croix de Saint-André blanche/rouge | Position d'un passage à niveau sans barrière (G1) | G1 |
| Balise blanche à bandes rouges obliques | J10 : 3, 2, 1 bandes = 150, 100, 50 m du passage à niveau | J10 |
| Balise bleue à chevrons blancs | J4 : virage dangereux | J4 |
| Balise bleu/blanc (bandes obliques) | J13 : obstacle permanent ; rouge/blanc = obstacle temporaire (K5c, K8) | J13 |

Règles simples à retenir :

- Rouge = interdiction ou danger ; bleu = obligation (rond) ou indication (carré) ; jaune = temporaire ; noir barré = fin.
- Un panneau rond est une prescription (obligation ou interdiction) ; un panneau carré est une indication.
  Exception piège : C111 (tunnel) est carré bleu mais impose feux de croisement, pas d'arrêt ni de demi-tour ;
  C107 (route à accès réglementé) et C207 (autoroute) sont carrés bleus mais emportent les interdictions d'accès
  et de manœuvre correspondantes.
- B27a (voie bus) est rond bleu mais n'oblige pas les bus à l'emprunter (exception documentée par l'IISR).
- Reconnaître de dos : l'octogone = STOP ; le triangle pointe en bas = cédez-le-passage ; le losange = route prioritaire.

## 2. Distances d'implantation (questions classiques)

| Signal | Hors agglomération | En agglomération | Sur autoroute |
|---|---|---|---|
| Panneaux de danger A (sauf A18) | 100 à 200 m, le plus souvent **150 m** | 0 à 50 m, le plus souvent **50 m** | 200 m |
| A18 (circulation dans les deux sens) | à l'endroit même du danger | idem | Sans indication |
| AB1, AB2 (annonces de priorité) | ≈ 150 m (jusqu'à 400 m si visibilité, répété à mi-distance si > 200 m) | 0 à 30 m | Sans indication |
| AB3b (cédez à X m), AB5 (STOP à X m) | ≈ 150 m, distance sur M1 / M5 | distance sur panonceau (arrondie aux 10 m si < 50 m) | Sans indication |
| AB3a, AB4 | **à hauteur** de l'intersection, à la ligne au sol | idem | Sans indication |
| A7 / A8 + balises J10 | A7/A8 à 150 m avec J10 3 bandes, puis J10 2 bandes (100 m) et 1 bande (50 m) | A7/A8 à 50 m, balises facultatives | Sans indication |
| Panneaux de prescription B | à l'endroit où commence la prescription ; **répétés après chaque intersection** | idem | Sans indication |
| B2a/b/c, B4, B5, B21b à B21e | **avant** l'endroit où s'applique la prescription | idem | Sans indication |
| B6 (stationnement) | du côté où l'interdiction s'applique | idem | Sans indication |
| Panneaux de danger : panonceau M1 | seulement si la distance diffère de la distance normale (max 400 m) | (max 150 m) | Sans indication |
| Sorties d'autoroute (D50) | Sans indication | Sans indication | 2 000 m, 1 000 m, 500 m |
| Triangle de présignalisation (panne) | ≥ 30 m en amont du véhicule | idem | seulement si sa pose est sans danger (sinon feux de détresse + gilet + glissière) |
| Bornes d'appel d'urgence | Sans indication | Sans indication | tous les 2 km |

Autres chiffres : marquage STOP = ligne continue de 50 cm ; cédez-le-passage = T'2 (50 cm trait / 50 cm vide,
largeur 50 cm) ; ligne d'effet des feux = T'2 largeur 15 cm ; passage piéton = bandes de 2,50 m × 0,50 m espacées
de 0,50 m ; T1 = 3 m / 10 m ; T'1 = 1,5 m / 5 m ; T2 = 3 m / 3,5 m ; T3 = 3 m / 1,33 m ; T'3 = 20 m / 6 m ;
T4 (BAU autoroute) = 39 m / 13 m.

## 3. Portée d'une prescription (jusqu'où s'applique un panneau ?)

- Un panneau de prescription (B) s'applique **à partir du panneau** (il faut donc avoir adapté sa vitesse avant
  de le franchir) et **jusqu'à la prochaine intersection** (sauf voies privées et chemins de terre), où il doit
  être répété s'il continue à s'appliquer ; ou jusqu'au panneau de fin correspondant (B33 pour B14, B34 pour B3,
  B35 pour B16, B31 pour toutes les interdictions aux véhicules en mouvement) ; ou jusqu'à un panneau contraire.
- Panonceau **M2 (étendue)** : la prescription vaut sur la longueur indiquée, y compris au-delà des intersections.
- Panonceau **M1 (distance)** : la prescription ou le danger ne commence qu'à la distance indiquée.
- Panonceau **M9z « RAPPEL »** : la prescription est toujours en vigueur (elle n'est pas nouvelle).
- Panonceau **M9z « Dans toute l'agglomération »** : étend la prescription à toute l'agglomération.
- **B31** met fin à toutes les interdictions imposées aux véhicules **en mouvement** : il ne met pas fin à une
  interdiction de stationner ou de s'arrêter.
- **Zones** (B30 zone 30, B52 zone de rencontre, B54 aire piétonne, B6b stationnement, B56 ZFE, B58 hiver) :
  la prescription vaut dans **toutes les rues** de la zone, sans répétition, jusqu'au panneau de sortie.
- **Agglomération** (EB10 → EB20) : 50 km/h par défaut, priorité à droite par défaut, klaxon interdit sauf danger.
  Seuls B14 (< 50 km/h), AB6, AB7, B30, B52, E31, E32 peuvent être sur le support de l'EB10 ; une limitation
  ainsi placée vaut pour toute l'agglomération.
- Une limitation associée à un panneau de danger (ex. A2b + B14 30) ne vaut que pour le danger annoncé.
- Un panneau de danger ne prescrit rien : il n'y a pas de « fin de danger » ; le danger dure jusqu'à la fin
  de la section (M2) ou disparaît de lui-même.
- Stationnement : B6a1/B6d valent du côté du panneau jusqu'à la prochaine intersection ; les panonceaux M8a
  (début), M8b (fin), M8c (rappel) précisent la section.

## 4. Panonceaux : conventions

- Un panonceau est placé **sous** le panneau qu'il complète, sur le même support, et ne s'applique **qu'à ce
  panneau**. Si deux panneaux sont sur un support, chacun a ses panonceaux (sauf danger + prescription qui
  partagent le panonceau placé sous le panneau de prescription).
- M1 distance (« 150 m ») ≠ M2 étendue (« 3 km ») ≠ M5 (« STOP 150 m », uniquement sous AB5).
- M3 : position ou direction (M3a flèche oblique = voie concernée ; M3b flèche + distance = direction d'un
  service ; M3d flèche vers le bas = panneau au-dessus de la voie).
- M4 : catégorie d'usagers concernée (M4a < 3,5 t, M4b bus, M4c motos, M4d1 vélos, M4d2 cyclomoteurs, M4e
  inscription (« 3+ »), M4f PTAC > X t, M4g marchandises, M4n handicapés, M4p piétons, M4x caravane…).
  Le panneau ne concerne que cette catégorie.
- M6 : précisions de stationnement (M6a « gênant » → fourrière ; M6b alternance semi-mensuelle ; M6c disque ;
  M6d/M6e payant ; M6f/M6g précisions ; M6h « sauf handicapés » ; M6i véhicules électriques en recharge ;
  M6j autopartage ; M6k covoiturage).
- M7 : schéma de l'intersection (trait épais = branches prioritaires).
- M8 : début / fin / rappel de section pour l'arrêt-stationnement (M8a, M8b, M8c ; M8d-f avec distances).
- M9 : indications diverses (M9a danger aérien, M9b voie ferrée électrifiée, M9c « cédez le passage », M9d
  passage piéton surélevé, M9e/f poste d'appel / extincteur, M9j véhicules lents, **M9v1 « interdit sauf vélo » / M9v2 « sauf vélo »**,
  M9z texte libre : RAPPEL, SAUF RIVERAINS, PAR TEMPS DE PLUIE…).
- M10 : cartouches d'identification (numéro de route M10a, de sortie M10b, rocade M10c, nom M10z), placés
  au-dessus.
- M11 : dérogations (M11a route à accès réglementé, M11b aire piétonne / période hivernale, M11c catégorie de
  tunnel, M11d ZFE).
- **M12** : seul panonceau triangulaire (pointe en bas, vélo + flèche jaunes) : « cédez-le-passage cycliste au
  feu » ; il n'autorise que les cyclistes à passer au rouge, en cédant le passage.
- Version temporaire : KM1, KM2, KM9 (fond jaune) sous les panneaux AK.

## 5. Hiérarchie des signaux et priorités

1. **Injonctions des agents** (police, gendarmerie, signaleurs de chantier avec piquet K10, signaleurs agréés)
   priment sur tout.
2. **Feux lumineux** priment sur les panneaux de priorité (R411-25 : un STOP ou un cédez-le-passage sous un feu
   ne s'applique que si le feu est éteint ou au jaune clignotant).
3. **Panneaux** priment sur le marquage au sol.
4. **Marquage au sol.**
5. En l'absence de tout : règles générales (priorité à droite, 50/80/110/130…).

La **signalisation temporaire (jaune)** prévaut sur la signalisation permanente contradictoire (panneaux et
marquage jaune) ; les panneaux permanents contraires doivent en principe être masqués.
Les **panneaux dynamiques** (PMV, X…) ont la même valeur que les panneaux fixes lorsqu'ils sont allumés.

Priorités particulières : tramway toujours prioritaire (sauf feux) ; véhicules prioritaires en intervention
(bleu + deux-tons) ; piéton engagé ou manifestant l'intention de traverser ; bus quittant son arrêt en
agglomération ; véhicules déjà engagés dans un giratoire (AB25).

Gestes de l'agent : bras levé = arrêt pour tous ; agent vu de face ou de dos = arrêt ; agent vu de profil
(bras tendus dans votre axe ou bras baissés) = passage ; geste de va-et-vient = avancer.

## 6. Les ≈ 60 signaux « incontournables » (les plus interrogés)

Danger : A1a/A1b (virages), A1c/A1d (succession), A2a (cassis) vs A2b (ralentisseur), A3/A3a/A3b (chaussée
rétrécie), A4 (glissante), A7 (PN barrières) vs A8 (PN sans barrières), A9b (tramway), A13a (enfants) vs A13b
(piétons), A14 (autres dangers + panonceau), A15a1 (vaches) vs A15b (animaux sauvages), A16 (descente), A17
(feux), A18 (double sens), A21 (cyclistes), A24 (vent).

Priorité : AB1 (priorité à droite) vs AB2 (priorité ponctuelle), AB3a (cédez), AB4 (STOP), AB5 (STOP à 150 m),
AB6/AB7 (route prioritaire / fin), AB25 (giratoire).

Interdiction : B0 vs B1, B1j, B2a/B2b/B2c, B3 vs B3a, B6a1 vs B6d, B6a2/B6a3, B7a vs B7b, B8, B9a/B9b/B9g/B9h,
B10a/B11/B12 (longueur / largeur / hauteur), B13, B14, B15 vs C18, B16, B17, B18c, B19.

Obligation : B21-1/-2, B21a1/a2, B21b/c1/c2/d1/d2/e, B22a vs C113, B25 vs B14 vs C4a, B26, B27a, B29.

Fin : B31 vs B0, B33, B34, B40, B43, B44.

Zones (catégorie `prescription_zonale` du dataset) : B30/B51, B52/B53 (rencontre 20 km/h), B54/B55 (aire
piétonne), B56/B57 (ZFE), B58/B59 (hiver), B6b3/B50c (zone bleue), B6b4/B50d (payant).

Indication : C1a, C4a, C6, C8, C12 vs B21b, C13a-d, C18, C20a, C24a/b/c, C25b, C26a, C27, C28, C29b/c, C50,
C64d (télépéage), C107/C108 vs C207/C208, C111/C112, C113/C114, C115/C116.

Services : CE2a (SOS), CE15a (carburant), CE15i (recharge), CE16/CE17/CE18, CE22 (107.7), CE52 (covoiturage).

Localisation : EB10/EB20, E31 (lieu-dit), cartouches E41-E44.

Panonceaux : M1, M2, M5, M4 (catégories), M6a, M7, M8a/b/c, M9v1 (sauf vélo), M9z (rappel), M12.

Balises et PN : J4, J5, J10, J13, J14a, G1, G2, croix double G1a.

Temporaire : AK5, AK14, AK17, AK22, AK30, AK31, KC1, KD10, KD22, K2, K5a, K8, K10a/K10b, KR11.

Feux : rouge / jaune fixe / vert / jaune clignotant / rouge clignotant (R24), R12 piétons, R14 flèches
(vert = protégé), R16 flèche jaune clignotante (cédez), R17 barres bus/tram, R21 a/b/c, R19.

Marquage : ligne continue, T1, T3 dissuasion, ligne d'annonce + flèches de rabattement, ligne mixte, flèches
directionnelles, ligne STOP (continue) vs cédez (discontinue) vs effet des feux, passage piéton, zébra, T4 BAU
(deux traits), chevrons, jaune continue vs discontinue vs zigzag, zone bleue, damier rouge/blanc, triangles de
ralentisseur, sas vélo.

## 7. Nouveautés et changements depuis ≈ 2015-2018 (à surveiller dans les anciens decks)

- **2008-2010 (décret 2008-754 du 30 juillet 2008)** : création de la **zone de rencontre** (B52/B53, 20 km/h) et
  double-sens cyclable par défaut dans les zones 30 et zones de rencontre (généralisé au 1er juillet 2010) ;
  B54/B55 (aire piétonne) remplacent C109/C110 ; nouveaux M9v « sauf vélo », B1j, C111/C112, C115/C116, SR2-SR4.
- **2015 (arrêté du 23 septembre 2015, décret 2015-808 « mobilités actives »)** : généralisation du panonceau
  **M12** et du signal **R19** (cédez-le-passage cycliste au feu, créés en 2012) ; double-sens cyclable étendu par
  défaut à toutes les voies limitées à 30 km/h ou moins (B1 + M9v2) ; chevauchement de la ligne continue autorisé
  pour dépasser un cycliste (R412-19) ; sas vélo réservés aux cycles (cyclomoteurs sur autorisation) ; stationnement 5 m en
  amont des passages piétons interdit (très gênant) ; **CE52** aire de covoiturage et **M6k1/M6k2** (8 janvier
  2016) ; **CE25** banque, **CE28** dépannage (13 mai 2015).
- **2016-2017 (arrêté de création, date exacte À VÉRIFIER)** : **B56/B57** « zone à circulation restreinte » (ZCR)
  + panonceau **M11d** (Crit'Air). Depuis la loi LOM (2019) on parle de **ZFE-m** (zone à faibles émissions mobilité) ;
  le panneau reste B56/B57. Vignette Crit'Air obligatoire dans les ZFE.
- **2018 (1er juillet)** : 80 km/h sur routes bidirectionnelles sans séparateur (retour possible à 90 par
  décision départementale depuis 2020) ; **arrêté du 12 décembre 2018** : **A9a** (traversée de voie bus) et
  **C20b** (position), l'ancien A9 devient A9b (tramway).
- **2019-2020** : engins de déplacement personnel motorisés (trottinettes) intégrés au code (décret 2019-1082) :
  pas de panneau dédié ; interdits sur trottoir, 25 km/h, pistes cyclables ; certaines villes utilisent B19 /
  B9-style avec inscription. **À VÉRIFIER** : pas de code IISR spécifique en 2026.
- **2020 (arrêté du 24 août 2020)** : signalisation expérimentale des **voies réservées** sur routes à chaussées
  séparées : panneau carré à **losange blanc** (début), losange barré (fin), panneau d'information **SR**
  (catégories : bus, taxis, covoiturage 2+/3+, véhicules à très faibles émissions), panonceaux M3a/M3d, M4e,
  M11b2, marquage losange au sol. Modifiée en 2024 (voies de droite admises) et 2025 (véhicules à très faibles
  émissions seuls autorisables), prolongée par l'arrêté du 28 juillet 2026 à « six ans et trois mois », soit
  jusque fin 2026. **Aucun code IISR définitif** (Wikipédia : « référence inconnue »). Déployé à Lyon,
  Grenoble, Paris (A1/A13), Nantes, Strasbourg… Les cours de code l'enseignent depuis 2021.
- **2021 (arrêté du 23 juin 2021, décret 2020-1264 « loi Montagne II »)** : **B58/B59** zone d'obligation
  d'équipements hivernaux (1er novembre – 31 mars, pneus hiver ou chaînes/chaussettes dans le coffre), en
  vigueur depuis le 1er novembre 2021.
- **2021** : expérimentation de la **circulation inter-files** des deux-roues motorisés (panneau d'information
  SR + panonceau M4c « en inter-files », 50 km/h) ; état 2026 **À VÉRIFIER**.
- **2021-2022** : panonceaux **M9k1/M9k2** (contrôle automatisé des voies réservées, avec SR3d) et **M9l**
  (radars « bruit ») ; panonceaux **M9v3/M9v4** (« sauf cyclomoteurs »). Les arrêtés de création restent **À VÉRIFIER**.
- **2022 (arrêté du 13 juin 2022)** : décompteur de temps pour piétons, signal **R12m** (piétons + cycles),
  mise à jour de la 2e partie de l'IISR (passages à niveau : G1, G1a, G1b, G1c et versions « bis »).
- **2022-2025** : **péage en flux libre** (A79, A13/A14, A4…) : panneaux **C65a/C65b/C65c** (moyens et délai
  de paiement, rappel en sortie). Les fichiers Commons datent de décembre 2025 ; arrêté de création **À VÉRIFIER**.
  Attention : d'anciennes sources donnent C65a/b = présignalisation des aires (assurée aujourd'hui par D46).
- Panneaux **supprimés** à connaître pour trier les vieux decks : C7 (arrêt de tramway) et B45b (fin de voie
  tram) supprimés en 2009 ; C109/C110 (aire piétonne) devenus B54/B55 en 2008 ; B21f (sens giratoire) supprimé
  en 1984 au profit d'AB25 ; A21b (ancien débouché de cyclistes) périmé ; C1b « 1 h 30 » et M6c ancien
  remplacés en 2008 ; B6b3-ancien / B50c-ancien idem.
- **Notions sans panneau dédié** (souvent demandées) : **vélorue** (rue où les cyclistes peuvent rouler au
  milieu, signalée par C50/marquage, expérimental), **chaussée à voie centrale banalisée** (marquage sans axe +
  bandes de rive, panneau C24a/C50 explicatif), **ZTL** (zone à trafic limité, notion italienne : en France on
  utilise B54 aire piétonne, B0 + M9z « sauf riverains », ou B56 ZFE), **zone 30 généralisée** (« ville 30 » :
  panneaux B30 aux entrées d'agglomération ou B14 30 sur EB10).

## 8. Pièges d'examen relevés pendant la recherche

- Code du feu piéton : **R12** (pas R25 : R25 est le « STOP » piéton des traversées de tramway).
- Tunnel : **C111** (et non « C9 » que l'on voit dans d'anciens supports ; C9 = station d'autopartage).
- **B10a = longueur, B11 = largeur, B12 = hauteur** ; B13 = poids total, B13a = poids par essieu.
- B15 (rond) = je cède au sens inverse ; C18 (carré bleu) = je suis prioritaire. La flèche rouge = celui qui cède.
- AB1 (croix) = je cède à droite ; AB2 (barre épaisse) = je suis prioritaire à cette intersection seulement ;
  AB6 (losange) = prioritaire sur tout l'itinéraire.
- A2a (deux bosses) = déformation ; A2b (une bosse) = ralentisseur ; C27 = position du ralentisseur.
- A13a (enfants) ≠ A13b (passage piéton, position C20a).
- B0 (cercle rouge vide) ≠ B31 (barre noire oblique) ≠ B1 (fond rouge, barre blanche).
- B6a1 (1 barre) = stationnement interdit, arrêt possible ; B6d (2 barres) = arrêt et stationnement interdits.
  Ligne jaune continue = arrêt interdit ; jaune discontinue = stationnement interdit ; zigzag = arrêt de bus.
- B7a (2 symboles) laisse passer les cyclomoteurs ; B7b (3 symboles) interdit tous les véhicules à moteur.
- Rond bleu vélo (B22a) = obligatoire ; carré bleu vélo (C113) = conseillée ; rond rouge (B9b) = interdit ;
  triangle (A21) = débouché de cyclistes.
- B52 (zone de rencontre) et B54 (aire piétonne) sont des carrés BLEUS ; B30 (zone 30), B56 (ZFE), B58 (hiver) sont
  blancs bordés de rouge.
- Rond rouge chiffre (B14) = maximum ; rond bleu chiffre (B25) = minimum ; carré bleu chiffre (C4a) = conseillé.
- C12 (rectangle bleu flèche) = sens unique ; B21b (rond bleu flèche) = tout droit obligatoire.
- C107 (voiture de face) = route pour automobiles (110) ; C207 (pont) = autoroute (130).
- Lettres italiques blanches sur noir (E31) = lieu-dit, pas de 50 km/h ; lettres droites noires sur blanc
  bordé de rouge (EB10) = agglomération.
- « Feu vert clignotant » : n'existe pas en France. Tourner à droite au rouge : interdit sauf R16/R19/M12
  (vélos pour M12/R19).
- Flèche verte (R14) = passage protégé ; flèche jaune clignotante (R16) = passer en cédant le passage.
- Piquet K10 : face verte **K10a** = passer ; face rouge **K10b** = arrêt (vérifié sur Commons).
- Balises J1 (virage) = bande blanche ; J3 (intersection) = bande rouge ; J6 (délinéateur) = bande noire
  oblique + catadioptre ; J10 = 1 à 3 bandes rouges (passage à niveau).
- Il n'existe plus de panneau rond bleu « sens giratoire obligatoire » en France : à l'entrée d'un giratoire
  on trouve AB25 (annonce), AB3a + ligne discontinue, et J5 / B21a1 sur l'îlot.
- Ligne de dissuasion (T3, large, sans flèches) ≠ ligne d'annonce (T3 avec flèches de rabattement).
- Passage cycliste (carrés) : ne donne pas la priorité par lui-même, contrairement au passage piéton.
- Dépassement aux passages à niveau : interdit seulement aux traversées **sans barrières ni demi-barrières**
  (R414-12) ; avec barrières, pas d'interdiction spécifique.
- Ligne mixte / discontinue : c'est **R412-20** qui autorise le franchissement de la ligne discontinue la plus
  proche ; **R412-19** interdit de franchir ou chevaucher la continue (3 points, 1 point pour chevauchement).
- A2b (ralentisseur dos-d'âne) n'existe qu'en agglomération : implanté à 0-50 m, jamais à 150 m.
- Codes qui n'existent pas (à ne pas inventer dans le deck) : « K3 » (seule la barrière dynamique XK3 existe),
  « C9 tunnel », « R25 piétons », « B21f giratoire », « SR50 covoiturage » (le losange n'a pas de code), « B58 ZTL »
  (B58 = équipements hivernaux).
- Les « dents de requin » (triangles) au sol signalent en France un ralentisseur, pas un cédez-le-passage
  (marquage cédez = ligne discontinue T'2). L'usage sur les aménagements cyclables reste **À VÉRIFIER**.

## 9. Suites à donner

- Vérifier par script les 363 noms `wikimedia_file` (Commons : `File:France road sign <CODE>.svg` ; exceptions notées
  dans le dataset : « FR road sign G1.svg », « France Road Sign A9a.png », « K5B.svg », « KC1 absence signalisation
  horizontale.svg », panneaux losange VOM…). 141 entrées n'ont pas de fichier (marquages, feux, gestes, direction, quelques E/J).
- Récupérer la « Liste complète des signaux routiers en usage » (annexe de l'arrêté du 24 novembre 1967, CEREMA)
  pour lever les 11 « À VÉRIFIER » (B56 date, C65 flux libre, M9v3/v4, M9k/M9l, T'1, damier blanc, CVCB,
  quadrillage jaune, SR3e, inter-files).
- Vérifications visuelles déjà faites sur Commons (rendu SVG) : B15/C18, B6a2, B17, B18b, B21-1, C13b, C14, C29a,
  C51a, M6a, M8a/b/c, M9v1/M9v2, M12a/b/c, A15a2, C9, C23, CE30a, C20b, B1j, B9e, M4e, M6f1, C26a, C8, B19, B52,
  B54, B56, B58, B6b3, C24a/b/c, C25b, C28, B45a, B5c, G1 bis, J4, J5, J14a, KC1, KD8/9/10, K5b, SR3a-e, SR-interfile,
  M9k1/k2, M3a/M3b, M6c/d/e/g/h, M9d, M10c, M11a, A15c, A20, A23, B9c/d/f/h, B13a, B18a/c, B26, B29, C3, C5, C29c,
  C30, C62, C64a/b/d, C107, C111, C113, C115, CE1, CE15a, CE22, CE52, E39, M4n, M6i, M6k1, M7, M9a/b/c/e, M11b1,
  M4c inter-files.
- Relecture indépendante (agent de vérification, Légifrance + Wikipédia) effectuée le 2026-09-21 : corrections
  appliquées (R412-20 pour la ligne mixte, dates du double-sens cyclable, dépassement aux PN selon R414-12,
  A2b en agglomération uniquement, AB3a facultatif en agglomération aux giratoires, catégorie
  `prescription_zonale`). Non couvert par cette relecture : entrées CE, D, noms de fichiers Commons, la plupart
  des dates d'arrêtés.
