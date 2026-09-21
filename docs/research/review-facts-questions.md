# Relecture factuelle des notes `data/faits/*.yaml` et `data/questions/*.yaml`

Date : 21 septembre 2026. Référentiels utilisés : `docs/research/legal-facts.md` (état au 20/09/2026), `docs/research/knowledge-facts.md`, `docs/research/exam.md` (§3.1 : les 20 questions officielles), et le texte consolidé du Code de la route (édition codes.droit.org du 10/09/2026, `cdr.txt`) relu directement pour les articles cités (R412-6, R412-10, R412-11-3, R412-19, R412-43-3, R413-2, R413-4, R413-7, R413-8, R413-19, R414-3, R414-6, R414-11, R414-16, R415-4, R416-7, R416-19, R417-1, R417-3, R417-10, R417-11, R417-12, R318-3, R312-3, L234-1, L237-1, L413-1).

Sévérités : **ERREUR** = faux ou contradictoire, à corriger ; **DOUTE** = incertain ou non sourcé, décision à prendre ; **STYLE** = rédaction, cohérence interne, qualité de carte, référence de source.

Chaque note a été lue intégralement. Les notes non citées ci-dessous n'appellent aucune remarque.

---

## data/faits/00_methode.yaml (8 notes)

**1. `etg-banque-2023`** — DOUTE
- Problème : l'explication affirme « le mot « anneau » a disparu, par exemple ». Cette substitution n'a pas été vérifiée à la source (exam.md §2.6 : « Non vérifiée à la source ; à traiter comme plausible mais non confirmée »).
- Correction (explication) : « Formulations simplifiées, photos réelles, mise en évidence en jaune du véhicule concerné, pictogramme indiquant le point de vue (piéton, cycliste, motard, conducteur de poids lourd…). »
- Source : exam.md §2.6.

**2. `etg-themes`** — ERREUR
- Problème : l'explication attribue aux thèmes des lettres (« premiers secours (P), prendre et quitter (S), sécurité du passager (E), environnement (A) ») qui ne correspondent ni à la nomenclature officielle (A = Porter secours, P = Prendre et quitter, S = Sécurité passager/véhicule, E = Environnement) ni aux codes `theme:` réellement utilisés dans le deck (faits/07 = A, faits/08 = P, faits/10 = S, faits/11 = E).
- Correction (explication) : « Les 10 thèmes : la circulation routière (L), le conducteur (C), la route (R), les autres usagers (U), les notions diverses (D), les premiers secours (A), prendre et quitter son véhicule (P), la mécanique et les équipements (M), la sécurité du passager et du véhicule (S), l'environnement (E). Les sous-decks de ce deck reprennent ce découpage. »
- Source : exam.md §2.2 (tableau des lettres L/C/R/U/D/A/P/M/S/E).

**3. `etg-age-minimum`** — STYLE
- Problème : « pour les personnes nées après 1988 » exclut les personnes nées en 1988 ; la règle vise celles nées à partir du 1er janvier 1988.
- Correction (explication) : « … et, pour les personnes nées à partir du 1er janvier 1988, l'ASSR 2 ou l'ASR. »
- Source : legal-facts E10 (« obligatoire pour les personnes nées après le 31 décembre 1987 ») ; arrêté du 20 avril 2012.

## data/faits/02_circulation.yaml (24 notes)

**4. `l-vitesse-visibilite-50`** — ERREUR (explication)
- Problème : « Feux de croisement + brouillard obligatoires ». R416-7 dispose que les feux de brouillard avant « peuvent » remplacer ou compléter les feux de croisement et que les feux arrière de brouillard « ne peuvent être utilisés qu'en cas de brouillard ou de chute de neige » : ils sont autorisés, pas obligatoires. Seuls les feux de croisement le sont (R416-6).
- Correction (explication) : « Article R413-4. Règle des trois 50 : visibilité 50 m = 50 km/h = 50 m d'intervalle. Feux de croisement obligatoires ; feux de brouillard avant et arrière autorisés et recommandés (R416-7). »
- Source : cdr.txt R416-7 I et II.

**5. `l-stationnement-alterne`** — STYLE
- Problème : « panneaux B6a2 (1-15) et B6a3 (16-31) » est ambigu : B6a2 signifie « stationnement interdit du 1er au 15 du mois » (il est donc posé du côté pair), B6a3 « stationnement interdit du 16 à la fin du mois » (côté impair). Lu comme « autorisé du 1 au 15 », c'est l'inverse.
- Correction (explication) : « Signalé par les panneaux B6a2 (stationnement interdit du 1er au 15 : côté des numéros pairs) et B6a3 (interdit du 16 à la fin du mois : côté impair), ou par le panneau de zone B6b3. »
- Source : IISR 4e partie (B6a2, B6a3, B6b3).

**6. `l-zone-bleue`** — DOUTE
- Problème : le cloze c1 « souvent 1 h 30 » porte sur une valeur locale sans base nationale (legal-facts F1 : « durée locale : pas de valeur nationale ») : la réponse n'est pas défendable. Par ailleurs R417-3 V punit d'une contravention de 2e classe sans qualifier le stationnement de « gênant ».
- Correction (texte) : « En zone bleue, le disque de stationnement (modèle européen) est obligatoire, avec l'heure d'arrivée affichée ; la durée autorisée est fixée par arrêté municipal (souvent 1 h 30) ; défaut ou dépassement : {{c1::35 €}} (contravention de 2e classe). »
- Source : cdr.txt R417-3 V ; legal-facts F1.

## data/faits/03_conducteur.yaml (23 notes)

**7. `c-distance-arret-formule`** — DOUTE
- Problème : les deux dossiers se contredisent sur ce que représente « (dizaines)² » : knowledge-facts C4 = distance d'ARRÊT (Ornikar, EVS, Codeclic, Stych) ; legal-facts A6 = distance de FREINAGE chez EVS/Ornikar (arrêt = 15 + 25 = 40 m à 50 km/h) et distance d'arrêt chez digischool/Codes Rousseau, avec la recommandation « ne pas faire de carte sur la valeur exacte ». La carte impose une seule lecture.
- Correction (explication) : « Distance d'arrêt = distance de réaction + distance de freinage. Convention d'examen la plus répandue ; certaines écoles appliquent le carré à la distance de freinage (arrêt = 15 + 25 = 40 m à 50 km/h) et la Sécurité routière retient 28 m / 70 m / 129 m (décélération 7 m/s²). Ce qui est sûr : l'ordre de grandeur (25-28 m à 50 km/h) et la relation vitesse × 2 → freinage × 4. »
- Source : legal-facts A6 et J2 ; knowledge-facts C4.

**8. `c-distance-mouillee`** — ERREUR (qualité de carte)
- Problème : le cloze c1 attend « 1,5 » alors que la phrase rappelle elle-même que l'examen dit « 2 fois plus longue » (Q13 officielle) : deux réponses défendables pour un même blanc, et la valeur officielle est celle reléguée en parenthèse.
- Correction (texte) : « Sur chaussée mouillée, l'adhérence est environ {{c1::2}} fois moins bonne et la distance de freinage environ {{c1::2}} fois plus longue (question officielle 2023) ; sur neige ou verglas, la distance de freinage peut être multipliée par {{c2::10}}. »
- Correction (explication) : « Q13 officielle : autoroute mouillée → « l'adhérence est 2 fois moins bonne » OUI, « la distance de freinage est 2 fois plus longue » OUI. Certaines écoles enseignent plutôt « distance d'arrêt × 1,5 » : l'ordre de grandeur suffit. Conséquence pratique : on double l'intervalle et on réduit la vitesse. »
- Source : exam.md §3.1 Q13 ; legal-facts A6.

**9. `c-champ-visuel-chiffres`** — DOUTE
- Problème : l'explication attribue le barème complet (100° à 40, 75° à 70) à la Sécurité routière ; legal-facts A6/G2 n'a retrouvé sur source officielle que 180° à l'arrêt, 45° à 100 km/h et 30° à 130 km/h et classe le reste « À VÉRIFIER (non vérifié officiellement) » ; knowledge-facts C2 l'attribue au dépliant SR. Le cloze c2 porte justement sur la valeur la moins sûre (100° à 40 km/h).
- Correction (texte) : « Champ visuel du conducteur : environ {{c1::180°}} à l'arrêt, 100° à 40 km/h, 75° à 70 km/h, {{c2::45°}} à 100 km/h et seulement {{c3::30°}} à 130 km/h. » ; (explication) : « Barème enseigné par les auto-écoles ; la Sécurité routière ne cite explicitement que 180° à l'arrêt, 45° à 100 km/h et 30° à 130 km/h (Code en Poche enseigne un barème un peu différent). À grande vitesse… »
- Source : legal-facts G2, J2 ; knowledge-facts C2.

**10. `c-retro-7s`** — DOUTE
- Problème : « toutes les 7 secondes » est la convention d'une seule école (Stych) ; questions/03 `c-regarder-loin` dit « toutes les 5 à 10 secondes » : incohérence interne et cloze sur une valeur non normative.
- Correction (texte) : « En circulation, on contrôle le rétroviseur intérieur {{c1::régulièrement (toutes les 5 à 10 secondes environ)}} et, obligatoirement, avant de {{c2::ralentir, freiner, s'arrêter ou tourner}}. »
- Source : knowledge-facts C12 ; questions/03 `c-regarder-loin`.

**11. `c-somnolence-stats`** — STYLE
- Problème : « l'ONISR … donne 8 % » ; legal-facts H3/H4 : 4 % des présumés responsables tous réseaux (14 % sur autoroute urbaine) ; knowledge-facts C5 : 8 % sur autoroute.
- Correction (explication) : « … l'ONISR (facteurs relevés par les forces de l'ordre) ne relève la somnolence que chez 4 % des présumés responsables (8 à 14 % sur autoroute) — l'examen retient « 1 sur 3 ». »
- Source : legal-facts H3, H4.

**12. `c-verre-standard`** — STYLE
- Problème : « 10 cl de vin » ici, « 12 cl de vin » dans questions/03 `c-alcool-doses`, « 12,5 cl » dans legal-facts B5. Harmoniser.
- Correction : « (25 cl de bière à 5°, 10 cl de vin à 12°, 3 cl d'alcool à 40°) » dans les deux notes.
- Source : knowledge-facts C6 (Santé publique France).

**13. `c-distance-laterale`** — STYLE
- Problème : doublon exact de `l-depassement-laterale` (faits/02) : même fait, mêmes clozes (1 m / 1,50 m).
- Correction : supprimer `c-distance-laterale` (ou n'en garder que l'explication sur le chevauchement, déjà présente dans l'autre note).

**14. `c-choc-50-etages`** — STYLE
- Problème : la Sécurité routière dit aussi « chute du 4e étage » (quiz 2021) ; un candidat peut rencontrer les deux.
- Correction (explication) : ajouter « Certains supports SR disent « 4e étage » ; physiquement v²/2g ≈ 10 m, soit 3 étages. »
- Source : legal-facts A6, J2.

## data/faits/05_autres_usagers.yaml (6 notes)

Aucune remarque.

## data/faits/06_reglementation.yaml (41 notes)

**15. `d-assurance-garanties`** — STYLE
- Problème : le cloze c1 « responsabilité civile » est suivi de « (« au tiers ») » visible : la réponse est donnée.
- Correction (texte) : « L'assurance obligatoire est la {{c1::responsabilité civile (« au tiers »)}} : elle couvre… »

**16. `d-controle-technique`** — STYLE
- Problème : c1 et c4 sont tous deux « 6 mois » : quand l'un est masqué, l'autre reste visible et souffle la réponse.
- Correction : mettre les deux occurrences sous le même numéro ({{c1::6 mois}} … {{c1::6 mois}}), ou ne clozer que la première.

**17. `d-invalidation-delai`** — STYLE
- Problème : « seulement le code si le permis avait plus de 3 ans » ; la condition est « au moins 3 ans » (legal-facts C2 : « ≥ 3 ans »).
- Correction : « … on repasse seulement le code si le permis avait au moins 3 ans, sinon code + conduite. »
- Source : legal-facts C2 ; SP F1704.

**18. `d-alcool-delit`** — STYLE
- Problème : « ou en état d'ivresse manifeste » : depuis le 20/08/2026, l'ivresse manifeste relève du nouvel article L237-1 (mêmes peines), le II de L234-1 étant abrogé. La source ne le cite pas.
- Correction (source) : « Code de la route, art. L234-1, L234-2, L234-8, L237-1 (lois n° 2025-622 et n° 2026-798) » ; (explication) ajouter « L'ivresse manifeste est depuis le 20 août 2026 un délit distinct (L237-1), aux mêmes peines. »
- Source : cdr.txt L234-1 (« II.-(Abrogé) »), L237-1.

**19. `d-accompagnateur`** — DOUTE
- Problème : « c'est l'accompagnateur qui perd les points » repose sur la FAQ conduite accompagnée de la Sécurité routière (knowledge-facts C11) ; aucun article du code ne le dit (L223-1 vise le titulaire du permis auteur de l'infraction). À garder mais à attribuer.
- Correction (explication) : « Selon la FAQ conduite accompagnée de la Sécurité routière, c'est l'accompagnateur, responsable de la conduite, qui est sanctionné et perd les points ; l'élève n'a pas de permis à points. Plusieurs accompagnateurs sont possibles, tous mentionnés au contrat d'assurance. »
- Source : knowledge-facts C11.

## data/faits/07_premiers_secours.yaml (8 notes)

**20. `numeros-urgence`** — DOUTE (forte présomption d'erreur)
- Problème : l'explication affirme « Depuis un téléphone … sans carte SIM, le 112 fonctionne aussi ». En France, les appels d'urgence sans carte SIM ne sont plus acheminés depuis 2008 (décision ARCEP, appels malveillants) ; le dossier ne mentionne que « même sans crédit/verrouillé » (knowledge-facts P3). Source « Code de la route, art. R412-6 (obligations) » sans rapport.
- Correction (explication) : « Le 112 est le bon réflexe si l'on hésite : il redirige vers le service compétent. Il fonctionne depuis un téléphone verrouillé ou sans crédit, via n'importe quel réseau disponible. » ; (source) : « service-public.fr — Numéros d'urgence ; Code pénal, art. 223-6 ».
- Source : knowledge-facts P3.

## data/faits/08_prendre_quitter.yaml (2 notes)

Aucune remarque.

## data/faits/09_mecanique.yaml (5 notes)

**21. `m-galette-chiffres`** — DOUTE
- Problème : période des pneus cloutés « du samedi précédant le 11 novembre au dernier dimanche de mars » (Stych, source unique, marquée [AV] dans knowledge-facts R4) alors que legal-facts E5 écrit « du 1er novembre au 31 mars » (période loi Montagne : confusion probable du dossier). R413-7 ne fixe aucune période (renvoi à arrêté). La carte est vraisemblablement juste (arrêté du 18 juillet 1985), mais la valeur n'est pas confirmée par les dossiers.
- Correction : garder le cloze c3 (90 km/h) ; déplacer la période en explication : « Période fixée par arrêté (classiquement du samedi précédant le 11 novembre au dernier dimanche de mars, prolongeable par le préfet). »
- Source : cdr.txt R413-7 ; knowledge-facts R4 ; legal-facts E5.

## data/faits/10_securite_passager.yaml (5 notes)

**22. `s-enfant-chiffres`** — STYLE
- Problème : « un siège dos à la route (i-Size) est obligatoire jusqu'à 15 mois » présente une exigence de la norme R129 (valable pour les sièges i-Size) comme une obligation générale ; les sièges R44 restent utilisables.
- Correction (texte) : « … avec un siège homologué i-Size (R129), l'enfant voyage dos à la route jusqu'à {{c2::15 mois}} au moins ; … »
- Source : legal-facts E7.

**23. `s-airbag-chiffres`** — DOUTE (faible)
- Problème : « 25 cm » repose sur une seule source (Ornikar, « À VÉRIFIER » dans knowledge-facts E2) ; la valeur est aussi reprise dans questions/10 `s-airbag-distance` et questions/08 `p-siege-reglage`.
- Correction : garder comme ordre de grandeur en écrivant « au moins 25 cm environ ».
- Source : knowledge-facts E2.

## data/faits/11_environnement.yaml (6 notes)

Aucune remarque.

---

## data/questions/00_methode.yaml (12 notes)

**24. `etg-adverbes`** — STYLE
- Problème : réponse = liste de 9 mots.
- Correction (réponse) : « Les restrictions (« obligatoirement », « uniquement », « exclusivement »), les nuances de fréquence (« principalement », « le plus souvent »), les conditions en fin d'énoncé (« sauf si », « dans ce cas ») et les négations (« il n'est pas interdit de… » = c'est autorisé). »

## data/questions/02_circulation.yaml (42 notes)

**25. `l-cedez-vs-stop`** — DOUTE
- Problème : « sa ligne au sol est discontinue (avec des triangles) » : la ligne de cédez-le-passage est une ligne discontinue T'2 (traits de 50 cm espacés de 50 cm) ; les triangles « dents de requin » ne sont pas un marquage réglementaire français (knowledge-facts L7 : « À VÉRIFIER »).
- Correction (explication) : « … sa ligne au sol est discontinue (traits de 50 cm espacés de 50 cm) ; celle du STOP est continue. Les deux sont présignalés à 150 m hors agglomération (AB3b / AB5). »
- Source : knowledge-facts L1, L7 ; IISR 7e partie art. 117-4.

**26. `l-giratoire-vs-rond-point`** — ERREUR (explication)
- Problème : « Il n'est pas interdit d'y dépasser ». R414-11 al. 2 interdit tout dépassement (sauf de deux-roues) aux intersections, avec pour seules exceptions les intersections où l'on est prioritaire au titre de R415-6, R415-7, R415-8, ou réglées par feux/agent ; le carrefour à sens giratoire (R415-10) n'y figure pas (legal-facts F2 : « le giratoire ne figure pas dans les exceptions de R414-11 »).
- Correction (explication, dernière phrase) : « Changer de voie à l'intérieur (pour sortir à gauche) est permis en signalant (R412-9), mais un giratoire reste une intersection : on n'y dépasse pas un autre véhicule (R414-11, sauf un deux-roues). »
- Source : cdr.txt R414-11.

**27. `l-depassement-cycliste-ligne-continue`** — ERREUR
- Problème : « Un motard a la même exception ». R412-19 al. 2 n'autorise le chevauchement que « pour le dépassement d'un engin de déplacement personnel motorisé, d'un cyclomobile léger ou d'un cycle » : une moto ou un cyclomoteur ne peuvent pas être dépassés en chevauchant la ligne continue.
- Correction (explication) : « Exception introduite en 2015 (R412-19), réservée aux cycles, EDPM et cyclomobiles légers : pour une moto ou un cyclomoteur, la ligne continue reste infranchissable. Sans visibilité ou avec un véhicule en face, j'attends derrière à distance. »
- Source : cdr.txt R412-19.

**28. `l-feu-jaune-fixe`** — DOUTE
- Problème : « Le jaune dure 3 s en ville, 5 s hors agglomération » n'est sourcé dans aucun dossier (l'IISR 6e partie fixe la durée du jaune selon la vitesse : 3 s si V ≤ 50 km/h, 5 s au-delà).
- Correction : supprimer, ou écrire « Le jaune fixe dure 3 s sur les voies limitées à 50 km/h, 5 s au-delà (IISR 6e partie). »
- Source : IISR 6e partie (à vérifier).

**29. `l-signaux-affectation-voies`** — STYLE
- Problème : source « signaux R21/R22 » : les signaux d'affectation de voies sont les R21 (R21a croix rouge, R21b flèche verte, R21c/d flèche jaune oblique) ; R22 est le feu de contrôle de flot.
- Correction (source) : « IISR 6e partie, art. 109-3 (signaux R21a à R21d) ».
- Source : knowledge-facts L6.

**30. `l-formes-couleurs-panneaux`** — ERREUR
- Problème : « Rond bleu ou rond rouge barré de noir : fin d'obligation ou d'interdiction ». Fin d'interdiction = rond BLANC barré de noir (B31, B33…) ; fin d'obligation = rond BLEU barré de ROUGE (B40…). En outre la réponse énumère 9 items.
- Correction (réponse) : « Triangle bordé de rouge : danger. Rond bordé de rouge : interdiction. Rond bleu : obligation. Carré bleu : indication. Rond blanc barré de noir : fin d'interdiction (B31, B33). Rond bleu barré de rouge : fin d'obligation (B40). » et déplacer STOP / cédez / losange jaune / jaune temporaire dans une seconde note « panneaux de priorité et signalisation temporaire ».
- Source : IISR 4e partie (B31, B33, B40).

**31. `l-agglomeration-panneau`** — ERREUR (explication)
- Problème : « Un panneau d'agglomération sur fond noir (ou blanc sans bordure rouge, EB10 « lieu-dit ») n'entraîne pas ces règles » : EB10 EST le panneau d'entrée d'agglomération (fond blanc, liseré rouge) ; le lieu-dit est le panneau E31 (fond blanc sans liseré, aucun effet réglementaire) ; il n'existe pas de panneau d'agglomération « sur fond noir ». La réponse énumère aussi 7 règles (STYLE).
- Correction (explication) : « Le panneau de sortie (même nom barré de rouge, EB20) rétablit les règles hors agglomération. Un panneau de lieu-dit (E31 : fond blanc sans bordure rouge) n'entraîne aucune de ces règles. »
- Source : knowledge-facts L10 ; IISR 5e partie art. 99-3.

**32. `l-stationnement-interdits`** — STYLE
- Problème : réponse de 14 lieux mêlant les trois régimes ; les emplacements de livraison et les bornes de recharge y apparaissent alors qu'ils relèvent du stationnement gênant (35 €, R417-10 III 3° et 4°), pas du très gênant.
- Correction : scinder en trois notes — « très gênant (135 €) » : voies réservées, trottoirs, passages piétons et 5 m en amont, bandes/pistes cyclables, voies vertes, places PMR, bouches d'incendie, bandes d'éveil, devant feux/panneaux masqués ; « gênant (35 €) » : double file, entrées carrossables, ponts/tunnels/passages souterrains, emplacements de livraison, bornes de recharge, BAU, zones de rencontre hors emplacements ; « dangereux (135 €, 3 points) » : visibilité insuffisante (virage, sommet de côte, intersection, passage à niveau).
- Source : cdr.txt R417-9, R417-10, R417-11.

**33. Listes longues** — STYLE
- `l-priorite-droite-exceptions` (6 cas), `l-depassement-conditions` (7 étapes), `l-depassement-interdit-lieux` (7 lieux), `l-demi-tour-marche-arriere` (6 lieux) : réponses > 4 items. Scinder, par exemple `l-depassement-interdit-lieux` en « visibilité/marquage » (virage, sommet de côte, brouillard, ligne continue, B3) et « lieux » (intersections non prioritaires, PN sans barrière, passage piéton avec véhicule arrêté, tram/bus à l'arrêt côté voyageurs).

## data/questions/03_conducteur.yaml (36 notes)

**34. `c-detectabilite-pieton-nuit`** — ERREUR
- Problème : la question invente un contexte (« vêtements sombres, de nuit ») absent de la Q11 officielle, et la réponse (« Par l'automobiliste, seulement à courte distance… encore moins par le motard ») contredit la réponse attendue : « Je suis facilement détectable par : le conducteur de la voiture » (C), et non par le motard.
- Correction (question) : « Piéton au bord d'un passage, une voiture et une moto arrivent (question officielle Q11, point de vue piéton) : par quel conducteur suis-je facilement détectable ? » ; (réponse) : « Par le conducteur de la voiture — pas par le motard, dont le champ de vision est réduit par le casque et l'attention absorbée par l'équilibre et la trajectoire ; je m'assure donc d'être vu des deux avant de traverser. » ; (explication) : garder « De nuit, un piéton sombre n'est vu qu'à ~30 m en feux de croisement, ~150 m avec un gilet réfléchissant. »
- Source : exam.md §3.1 Q11.

**35. `c-cycliste-devant-depassement`** — DOUTE
- Problème : la Q7 officielle n'a pas d'énoncé et sa transcription ne mentionne pas de véhicule en face ; « un véhicule arrive en face » est une interprétation présentée comme le contenu de la question officielle.
- Correction (explication) : « Question officielle 2023 (Q7, sans énoncé : cycliste devant à droite, dépassement en cours ; réponse « Je me replace à droite. ») — le contexte « véhicule en face » est l'interprétation la plus probable de la photo. »
- Source : exam.md §3.1 Q7 et §3.3.

**36. `c-vision-acuite-permis`** — STYLE
- Problème : « conduire sans correction est une infraction (135 €) » sans les 3 points ; faits `c-vue-90-pourcent` dit « 135 € et 3 points ».
- Correction (explication) : « … conduire sans correction : 135 € et 3 points (R221-1-1). »
- Source : legal-facts G2.

**37. `c-regarder-loin`** — STYLE
- Problème : « toutes les 5 à 10 secondes » vs faits `c-retro-7s` « 7 secondes » (voir n° 10). Harmoniser sur « 5 à 10 secondes environ ».

**38. `c-alcool-doses`** — STYLE
- Problème : « 12 cl de vin » vs faits `c-verre-standard` « 10 cl » (voir n° 12).
- Correction : « (25 cl de bière à 5°, 10 cl de vin à 12°, 3 cl d'alcool fort à 40°) ».

**39. `c-cannabis-effets`** — DOUTE (faible)
- Problème : « les effets durent plusieurs heures (2 à 7 h) » : durée non sourcée dans les dossiers.
- Correction : « les effets durent plusieurs heures » (sans chiffre), ou sourcer la page SR « La drogue et la conduite ».

**40. Listes longues** — STYLE
- `c-fatigue-signes` (8 signes), `c-indices-anticipation` (9 indices), `c-jeunes-conducteurs-risque` (7 causes), `c-distracteurs` (6). Pour `c-fatigue-signes`, structurer en deux familles utiles à l'examen : « Fatigue : picotements des yeux, nuque raide, douleurs dorsales, regard fixe → pause. Somnolence : bâillements, paupières lourdes, trajectoire flottante, micro-sommeils → s'arrêter et dormir. »

## data/questions/04_route.yaml (32 notes)

**41. `r-nuit-feux-croisement-route` et `r-nuit-vitesse-visibilite`** — DOUTE
- Problème : « ~50-60 km/h » comme vitesse compatible avec les 30 m des feux de croisement est un calcul du deck ; la Sécurité routière dit « dès 70 km/h de nuit en croisement, l'obstacle qui surgit dans la zone éclairée est inévitable » et faits `c-feux-portee` dit « au-delà de ~70 km/h » : incohérence interne.
- Correction : remplacer « ~50-60 km/h » par « à 70 km/h et plus, on ne peut plus s'arrêter dans la zone éclairée (Sécurité routière) » dans les deux notes.
- Source : legal-facts A6 ; knowledge-facts C2, C4.

**42. `r-pluie-feux`** — STYLE
- Problème : « Sous la pluie, en plein jour, quels feux sont obligatoires ? » : R416-4 n'impose l'éclairage de jour que « lorsque la visibilité est insuffisante » ; Codes Rousseau parle de « recommandé » (knowledge-facts R2). L'explication le nuance, la question non.
- Correction (question) : « Sous une pluie qui réduit la visibilité, en plein jour, quels feux faut-il allumer ? »
- Source : cdr.txt R416-4 ; knowledge-facts R2.

**43. `r-loi-montagne`** — ERREUR (explication)
- Problème : « Sanction prévue : 135 € et immobilisation possible (la verbalisation a été différée, mais l'obligation existe) » : aucune sanction n'est codifiée (D314-8 ne prévoit pas de peine) ; le « 135 € » annoncé n'a jamais été mis en œuvre (tolérance reconduite chaque hiver). En outre « pneus M+S admis jusqu'en 2024 puis tolérés » est imprécis : depuis le 1er novembre 2024 le seul marquage M+S ne vaut plus pneu hiver, sauf chaînes à bord.
- Correction (réponse) : « Soit 4 pneus hiver (marquage 3PMSF « flocon » ; depuis le 1er novembre 2024 le seul marquage M+S ne suffit plus, sauf à avoir des chaînes à bord), soit des chaînes ou chaussettes à neige à bord pour au moins deux roues motrices — dans les communes listées par le préfet, signalées par le panneau B58. » ; (explication) : « … Aucune amende n'est codifiée (D314-8) : le « 135 € » annoncé n'a jamais été appliqué ; l'obligation existe néanmoins et c'est la réponse attendue. »
- Source : legal-facts E5 et I (1er novembre 2021, 1er novembre 2024) ; SP F19459.

**44. `r-tunnel-regles`** — ERREUR
- Problème : « Le panneau C9 (tunnel) » : le panneau d'entrée de tunnel est C111 (sortie C112) ; C9 n'a rien à voir. De plus « intervalle d'au moins 150 m (ou 2 repères lumineux bleus / 2 secondes) » assimile 150 m et 2 s (72-78 m à 130 km/h). « Issues tous les 200 m environ » est marqué À VÉRIFIER (legal-facts F6 ; knowledge-facts R7 : ~400 m selon la directive).
- Correction (réponse) : « … intervalle de sécurité indiqué par la signalisation (souvent 150 m, ou 2 repères lumineux bleus), à respecter même à l'arrêt ; … » ; (explication) : « Le panneau C111 (entrée de tunnel) rappelle ces obligations. Avant d'entrer : retirer ses lunettes de soleil, repérer les issues de secours signalées en vert. »
- Source : knowledge-facts R7 ; legal-facts F6.

**45. `r-montagne-priorite`** — ERREUR
- Problème : « sauf si le descendant est le plus proche d'un refuge/garage » : inversé. R414-3 III : à catégorie égale, le descendant recule « sauf si cela est manifestement plus facile pour le conducteur du véhicule montant, notamment si celui-ci se trouve près d'une place d'évitement ».
- Correction (réponse) : « Le véhicule qui descend doit s'arrêter le premier (et reculer si nécessaire) pour laisser passer celui qui monte — sauf si le véhicule montant est plus près d'une place d'évitement (c'est alors lui qui recule). Entre véhicules de catégories différentes, celui qui recule est : le véhicule seul face à un attelage, le plus léger des deux, le camion de plus de 3,5 t face à un transport en commun. »
- Source : cdr.txt R414-3 II et III.

**46. `r-autoroute-insertion`** — STYLE
- Problème : source « Code de la route, art. R412-9 et R415-... » (référence incomplète).
- Correction (source) : « Code de la route, art. R421-3 ; securite-routiere.gouv.fr — Autoroute ».

**47. `r-autoroute-bau`** — STYLE
- Problème : « Certaines voies d'entrecroisement peuvent être ouvertes à la circulation aux heures de pointe » : confusion de terme ; il s'agit de la BAU transformée en voie auxiliaire.
- Correction (explication) : « Sur certains tronçons, la bande d'arrêt d'urgence est ouverte à la circulation aux heures de pointe comme voie auxiliaire (signalisation dynamique). »

**48. `r-autoroute-fatigue-aires`** — DOUTE
- Problème : « repos tous les 10 à 20 km, service tous les 30 à 40 km » ; les sources donnent 15-20 km et 40-50 km (Ornikar 15/45, EVS 20/50, APRR 15-20/40-50).
- Correction (réponse) : « Une aire de repos environ tous les 15 à 20 km et une aire de service (carburant, restauration) environ tous les 40 à 50 km ; … »
- Source : knowledge-facts R11 [AV].

**49. `r-chantier-fleche-lumineuse`** — DOUTE
- Problème : codes « KD10/KD9 » absents des dossiers ; les flèches lumineuses de rabattement et d'urgence sont KR42 (FLR) et KR43 (FLU).
- Correction (question) : « Une flèche lumineuse de rabattement (FLR, KR42) ou un panneau de rabattement précède un chantier sur voie rapide : que faire ? »
- Source : knowledge-facts R10.

**50. `r-tram-priorite`** — STYLE
- Problème : source « R415-11 et R414-9 » (piétons ; véhicules lents) sans rapport.
- Correction (source) : « Code de la route, art. R422-3 et R414-13 ».

**51. Listes longues** — STYLE
- `r-autoroute-interdictions` (9 items), `r-neige-conduite` (7), `r-vent-lateral` : scinder (ex. `r-autoroute-interdictions` en « manœuvres interdites » et « usagers interdits »).

## data/questions/05_autres_usagers.yaml (26 notes)

**52. `u-edpm-regles`** — STYLE
- Problème : réponse de 9 items, doublon partiel de faits `u-edpm-chiffres`.
- Correction : scinder en « conditions » (14 ans, seul, 25 km/h, assurance, gilet la nuit, casque recommandé) et « où circuler » (trottoir interdit sauf autorisation au pas ; en ville pistes/bandes obligatoires sinon chaussées ≤ 50 km/h ; hors agglomération pistes et voies vertes seulement).

**53. `u-velo-equipements`** — STYLE
- Problème : 7 items.
- Correction : scinder en « équipements du vélo » (2 freins, feux avant/arrière, catadioptres, sonnette) et « équipements du cycliste » (casque < 12 ans, gilet hors agglomération la nuit, écouteurs et téléphone interdits).

## data/questions/07_premiers_secours.yaml (11 notes)

Aucune erreur. `a-proteger-actions` est une liste de 5 étapes mais décrit une procédure ordonnée : acceptable.

## data/questions/08_prendre_quitter.yaml (17 notes)

**54. `p-pente-roues`** — ERREUR (explication)
- Problème : « la roue arrière-droite braquée vers la route vient s'appuyer contre le trottoir » : les roues arrière ne braquent pas ; en montée avec bordure, c'est l'arrière du pneu AVANT droit (roues braquées vers la chaussée) qui vient buter contre le trottoir.
- Correction (explication) : « … en montée, elle reculerait : roues avant braquées vers la route, l'arrière du pneu avant droit vient s'appuyer contre le trottoir. Sans trottoir : roues vers l'accotement dans les deux cas. Plus : première en montée, marche arrière en descente. »
- Source : knowledge-facts S4.

**55. `p-quitter-checklist`** — STYLE
- Problème : source « Code de la route, art. R417-... (immobilisation) » incomplète.
- Correction (source) : « Code de la route, art. R417-8 (précautions avant de s'éloigner du véhicule) ».

**56. `p-quitter-stationnement-surveiller`** — STYLE
- Problème : source « R415-10 » = carrefour à sens giratoire, sans rapport.
- Correction (source) : « Sécurité routière — Exemples de nouvelles questions (Q14) ; Code de la route, art. R412-10 (avertir avant de reprendre sa place dans la circulation) ».

**57. `p-enfants-seuls`** — STYLE
- Problème : « dépasse 50 °C en moins d'une demi-heure » vs faits `p-quitter-reperes` « 70 °C en 20 minutes » (knowledge-facts S4).
- Correction (explication) : « L'habitacle d'une voiture au soleil peut atteindre 70 °C en 20 minutes. »

## data/questions/09_mecanique.yaml (26 notes)

**58. `m-appel-phares`** — STYLE
- Problème : « Faire des appels de phares pour signaler un contrôle de police n'est pas une infraction en soi mais reste déconseillé » : affirmation juridiquement discutée et hors programme.
- Correction : supprimer cette phrase.

## data/questions/10_securite_passager.yaml (20 notes)

**59. `s-animaux`** — ERREUR
- Problème : « 135 € pour « gêne du conducteur » » : R412-6 III punit la gêne du conducteur (II) d'une contravention de 2e classe, soit 35 €.
- Correction (explication) : « Un animal libre distrait le conducteur (35 €, contravention de 2e classe, R412-6 : possibilités de mouvement et champ de vision réduits) et devient un projectile en cas de choc. Ne jamais laisser un animal dans une voiture au soleil. »
- Source : cdr.txt R412-6 III.

**60. `s-remorque-permis-b`** — ERREUR
- Problème : « vitesse limitée si le PTAC de l'ensemble dépasse 3,5 t (110/100/80… selon la route) » : R413-8 fixe 90 km/h sur autoroute, 80 km/h sur les routes prioritaires (90 sur routes à chaussées séparées pour ≤ 12 t) et 80 km/h sur les autres routes ; contradiction avec faits `s-remorque-chiffres` (90/80/80). Et c'est le PTRA (poids total roulant autorisé), pas le PTAC.
- Correction (explication) : « … Si le PTRA de l'ensemble dépasse 3,5 t, vitesses réduites : 90 km/h sur autoroute et sur route à chaussées séparées, 80 km/h sur les autres routes (R413-8). »
- Source : cdr.txt R413-8.

**61. `s-ceinture-50-kmh`** — STYLE
- Problème : « un passager de 70 kg est projeté avec une force de plus d'une tonne » vs faits `s-ceinture-efficacite` « 75 kg → environ 2,5 tonnes » (chiffre SR : poids apparent × 33).
- Correction (réponse) : « … un adulte de 75 kg est projeté avec une force d'environ 2,5 tonnes — impossible à retenir avec les bras. »
- Source : legal-facts A6, G3.

**62. `s-ecall`** — STYLE
- Problème : « obligatoire sur les voitures neuves depuis avril 2018 » : l'obligation vise les nouveaux types homologués depuis le 31 mars 2018.
- Correction (réponse) : « … obligatoire sur les modèles homologués depuis le 31 mars 2018 … »
- Source : knowledge-facts M6 ; règlement (UE) 2015/758.

## data/questions/11_environnement.yaml (18 notes)

**63. `e-rapports-regime`** — ERREUR
- Problème : « Vers 2 000 tr/min en essence et 1 500 tr/min en diesel (dès 2 000-2 500 au plus tard) » contredit faits `e-rapports-chiffres` (2 500 essence / 2 000 diesel) et les sources (knowledge-facts A1 : essence ≈ 2 500, diesel ≈ 2 000).
- Correction (réponse) : « Vers 2 500 tr/min en essence et 2 000 tr/min en diesel ; on roule sur le rapport le plus élevé possible sans faire peiner le moteur (ex. 4e à 50 km/h en ville). »
- Source : knowledge-facts A1.

**64. `e-ve-recharge`** — ERREUR
- Problème : « y stationner sans recharger est un stationnement très gênant (135 €) » : R417-10 III 3° classe le stationnement « devant les dispositifs destinés à la recharge » parmi les stationnements GÊNANTS (2e classe, 35 €).
- Correction (explication) : « Une place de recharge est réservée aux véhicules en charge : y stationner sans recharger est un stationnement gênant (35 €, R417-10), avec mise en fourrière possible. »
- Source : cdr.txt R417-10 III 3° et IV.

**65. `e-moteur-arret`** — STYLE
- Problème : source « Code de la route, art. R318-1 (moteur à l'arrêt) » : R318-1 concerne les émissions polluantes ; l'interdiction de laisser tourner le moteur à l'arrêt vient de l'arrêté du 12 novembre 1963 (montant À VÉRIFIER).
- Correction (source) : « ADEME — Écoconduite ; arrêté du 12 novembre 1963 (moteur tournant à l'arrêt) ».
- Source : knowledge-facts A2.

**66. `e-critair-classes`** — STYLE
- Problème : « ~3,80 € » vs faits `e-critair-chiffres` et `d-critair-prix` « 3,85 € » (SP F33371, 2026).
- Correction : « (3,85 € en 2026, frais d'envoi inclus) ».

**67. `e-zfe-definition`** — STYLE
- Problème : « a fait l'objet de débats parlementaires en 2025 » sans l'issue, alors que faits `d-critair-prix` précise que la suppression a été censurée (CC, 21 mai 2026) et que les ZFE sont maintenues.
- Correction (explication) : « … Le Parlement avait voté leur suppression en 2025, censurée par le Conseil constitutionnel le 21 mai 2026 : les ZFE restent en vigueur ; les cartes et règles locales sont à vérifier avant un trajet. »
- Source : legal-facts E4, I.

**68. `e-covoiturage-voie`** — DOUTE
- Problème : « Signal créé en 2020-2021 » et source « Arrêté du 5 mars 2021 modifiant l'IISR (signal SR3/C-losange) » : legal-facts F5 n'a retrouvé le losange que dans des arrêtés d'expérimentation et la signalisation dynamique (IISR 9e partie, arrêté du 15 mars 2024) et marque la base pérenne « À VÉRIFIER » ; « SR3 » n'apparaît dans aucun dossier.
- Correction (source) : « Code de la route, art. L411-8 ; IISR 9e partie (signalisation dynamique, arrêté du 15 mars 2024) ; paris.fr (voie réservée du périphérique, 2025) » ; (explication) : remplacer « Signal créé en 2020-2021 » par « Signal déployé depuis 2020 (Lyon, Grenoble, Paris périphérique, A48/A13…) ».
- Source : legal-facts F5, J2.

**69. `e-motorisations`** — DOUTE
- Problème : « malus au-delà d'un seuil, 108 g/km en 2026 » : valeur reprise de lePERMISLIBRE, non vérifiée (exam.md §5.2) et hors programme.
- Correction (explication) : « … étiquette énergie/CO₂ (malus au-delà d'un seuil de CO₂ fixé chaque année). »
- Source : exam.md §5.2.

---

## Synthèse

### Notes relues

| Fichier | Notes | Fichier | Notes |
|---|---|---|---|
| faits/00_methode | 8 | questions/00_methode | 12 |
| faits/02_circulation | 24 | questions/02_circulation | 42 |
| faits/03_conducteur | 23 | questions/03_conducteur | 36 |
| faits/05_autres_usagers | 6 | questions/04_route | 32 |
| faits/06_reglementation | 41 | questions/05_autres_usagers | 26 |
| faits/07_premiers_secours | 8 | questions/07_premiers_secours | 11 |
| faits/08_prendre_quitter | 2 | questions/08_prendre_quitter | 17 |
| faits/09_mecanique | 5 | questions/09_mecanique | 26 |
| faits/10_securite_passager | 5 | questions/10_securite_passager | 20 |
| faits/11_environnement | 6 | questions/11_environnement | 18 |
| **Total faits** | **128** | **Total questions** | **240** |

368 notes relues ; 69 constats.

### Constats par sévérité

- **ERREUR : 16** (n° 2, 4, 8, 26, 27, 30, 31, 34, 43, 44, 45, 54, 59, 60, 63, 64)
- **DOUTE : 18** (n° 1, 6, 7, 9, 10, 19, 20, 21, 23, 25, 28, 35, 39, 41, 48, 49, 68, 69)
- **STYLE : 35** (n° 3, 5, 11-18, 22, 24, 29, 32, 33, 36-38, 40, 42, 46, 47, 50-53, 55-58, 61, 62, 65-67)

Aucune valeur légale « 2025-2026 » n'est fausse : les montants post-loi 2025-622 (3 ans / 9 000 €, 5 ans / 15 000 €, 9 points, délit ≥ 50 km/h depuis le 29/12/2025), la loi 2026-798 (refus de dépistage, rodéos), le maintien des ZFE, le permis à 17 ans, la fin du point pour < 5 km/h, la carte verte, le CT deux-roues et l'inter-files sont corrects et cohérents entre faits et questions. Les erreurs relevées portent sur des points de droit secondaires (classe d'amende, article cité), des codes de panneaux, des inversions de règle et des contradictions internes au deck.

### Les 10 corrections les plus importantes

1. **n° 60 `s-remorque-permis-b`** : vitesses avec remorque > 3,5 t = 90/80/80 (R413-8), pas 110/100/80 ; et PTRA, pas PTAC.
2. **n° 45 `r-montagne-priorite`** : l'exception « place d'évitement » vise le véhicule MONTANT (R414-3 III), pas le descendant.
3. **n° 27 `l-depassement-cycliste-ligne-continue`** : le chevauchement de la ligne continue ne vaut que pour dépasser un cycle, un EDPM ou un cyclomobile léger — jamais une moto (R412-19).
4. **n° 34 `c-detectabilite-pieton-nuit`** : la réponse contredit la Q11 officielle (le piéton est facilement détectable par le conducteur de la voiture, pas par le motard) ; le contexte « de nuit, vêtements sombres » est inventé.
5. **n° 63 `e-rapports-regime`** : régimes de passage des rapports inversés (essence ≈ 2 500 tr/min, diesel ≈ 2 000) ; contradiction avec faits `e-rapports-chiffres`.
6. **n° 59 `s-animaux` et n° 64 `e-ve-recharge`** : classes d'amende fausses (gêne du conducteur R412-6 = 35 € ; stationnement devant une borne de recharge R417-10 = gênant, 35 €).
7. **n° 30 `l-formes-couleurs-panneaux`** : fin d'interdiction = rond blanc barré de noir ; fin d'obligation = rond bleu barré de rouge.
8. **n° 31 `l-agglomeration-panneau`** : EB10 est le panneau d'entrée d'agglomération ; le lieu-dit est E31 ; pas de panneau « fond noir ».
9. **n° 43 `r-loi-montagne`** : aucune sanction n'est codifiée pour le défaut d'équipement hivernal (D314-8) ; ne pas annoncer « 135 € prévu ».
10. **n° 8 `c-distance-mouillee` et n° 2 `etg-themes`** : cloze à deux réponses possibles (1,5 vs 2 ; la valeur officielle Q13 est × 2) ; lettres de thèmes contredisant à la fois la nomenclature officielle et les codes `theme:` du deck.

### Points à trancher (DOUTE) avant mise en cartes

- Convention « (dizaines)² » = distance d'arrêt ou de freinage (n° 7) : les deux dossiers de recherche se contredisent ; conserver l'ordre de grandeur et la relation × 4.
- Barème du champ visuel selon la vitesse (n° 9) : seuls 180°/45°/30° sont officiels.
- Période des pneus cloutés (n° 21) : la carte suit Stych (« samedi précédant le 11 novembre → dernier dimanche de mars »), legal-facts dit « 1er novembre → 31 mars » (probable confusion avec la loi Montagne) ; R413-7 ne tranche pas.
- Appel au 112 sans carte SIM (n° 20) : à supprimer, la France n'achemine plus ces appels depuis 2008.
- Base réglementaire du losange « covoiturage » (n° 68) et durée du feu jaune (n° 28) : non sourcées dans les dossiers.
