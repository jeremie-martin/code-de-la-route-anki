Counts — 329 notes : OK 306, FIX 17, INCERTAIN 6 · FIX by type : FAUX 5, SUREXTENSION 5, SOUS-EXTENSION 4, SOURCE 3 (+ CONTRADICTION 2, attached to FIX notes already counted: c207, voyant-brouillard-avant) · INCERTAIN 6 (1 of them also SOURCE)

# Fact-check report — group A (signs, markings, lights, gestures, dashboard lights, A/B confusions)

Sources read for this pass: the Code consolidated on 10 September 2026 (`cdr.txt`); the IISR, parts 1 to 9, downloaded from equipementsdelaroute.cerema.fr (1st part VC 2025-09-04, 2nd 2022, 3rd 2019, 4th 2022-06-13, 5th 2025-09-04, 6th 2025-09-04, 7th 2025-04-04, 8th 2025-09-04, 9th 2025-09-04); the arrêté du 24 novembre 1967 on Légifrance (version 2025-04-25, read by extracts: C107, C111, C112, C113, C115, C8, C29a, C51a, B25, B27a, M4a, M4d1, M9v1, M12, B9b); Convention de Vienne sur la circulation routière (1968), art. 6; arrêté du 30 septembre 2008, art. 2; decision of the Conseil constitutionnel of 21/05/2026 (ZFE). Recognition notes: fixes go into `data/_meta/sign_overrides.yaml` under the key given, then regenerate. `voyants.yaml` is written by hand.

## FAUX

### m10b (override `m10b`, and the inventory entry `M10b`: `signification`, `implantation`)
- Text: « Cartouche portant le numéro de la sortie/échangeur (sur autoroute), placé au-dessus des panneaux de sortie. » + « En pratique. Je compare ce numéro à celui de mon itinéraire avant de me rabattre vers la sortie. »
- Problem: M10b goes only above C107 and C207 (the start of a route à accès réglementé or an autoroute) and gives the number of the interchange where I **enter**. It is not a cartouche above exit signs.
- Evidence: IISR 1re partie art. 9-1 B 10: « Les panonceaux M10a et M10b ne peuvent être exclusivement employés qu'avec les panneaux C107 et C207 » ; annexe: « C207 + M10a + M10b — Entrée sur l'autoroute A75 à l'échangeur n°19 » ; IISR 5e partie art. 75-4: C207 « est complété par les panonceaux M10a si l'accès à l'autoroute se fait par un échangeur et M10b si les échangeurs sont numérotés ».
- Correction: signification « Cartouche placé au-dessus du panneau d'entrée d'autoroute (ou de route à accès réglementé) : numéro de l'échangeur par lequel j'entre. » ; conduite « Je repère ce numéro : il situe mon point d'entrée sur l'itinéraire. »

### d50 (override `d50`)
- Text: « Sur autoroute, panneau annonçant à 2 000 m, 1 000 m puis 500 m la proximité d'un échangeur ou d'une bifurcation ; une variante indique aussi l'affectation des voies. »
- Problem: a D50 is a single warning sign, placed about 60 s of driving before the advance signs. It is not repeated at 2 000, 1 000 and 500 m. The presignalisation sign (D40) is placed at about 30 s.
- Evidence: IISR 5e partie art. 83-6: « Le panneau de type D50 est implanté à environ 60 secondes de parcours en amont du point d'implantation de la signalisation avancée. Il est utilisé sur les autoroutes et les routes à chaussées séparées dont les échangeurs sont numérotés » ; art. 83-7 (Da50): « à environ 30 secondes de parcours ».
- Correction: « Sur autoroute ou voie rapide à échangeurs numérotés, panneau d'avertissement placé environ une minute avant la signalisation de la sortie ou de la bifurcation ; une variante indique l'affectation des voies. »

### a8 (override `a8`, `complement`)
- Text: « La croix de Saint-André marque le passage lui-même ; un STOP peut la surmonter. »
- Problem: at a level crossing with a STOP, the STOP sign is placed **under** the cross.
- Evidence: IISR 2e partie art. 35 C 2: « La signalisation de position est constituée par le panneau AB4 placé au-dessous du panneau G1, G1a, Gb ou G1c ». The same wording is in `signs_inventory.yaml` line 6009 (« si un AB4 (STOP) surmonte la croix »), which is not displayed on this card.
- Correction: « La croix de Saint-André marque le passage lui-même ; un STOP peut être placé sous la croix. »

### marq-livraison (override `marq-livraison`, `complement`)
- Text: « Un arrêté local peut ouvrir l'aire au stationnement à certaines heures (la nuit, par exemple) ; en dehors de ces horaires signalés, elle reste réservée aux livraisons. »
- Problem: the card (and its image) shows a **discontinuous** yellow line. That marking means the space is reserved only at certain times, by default on working days from 7:00 to 20:00. Outside those hours, parking is allowed without any extra sign. Only a doubled continuous line reserves the space at all times. The card turns the default the other way round.
- Evidence: IISR 7e partie art. 118-2 C: « Pour les emplacements réservés de manière périodique, la délimitation est réalisée par une ligne discontinue de type T'2 … Ce marquage indique que l'emplacement est réservé … les jours ouvrables de 7 heures à 20 heures, période durant laquelle le stationnement des autres véhicules est interdit » ; « Pour les emplacements réservés de manière permanente … une seconde ligne continue … est accolée ». R417-10 III 4° (stationnement gênant; « l'autorité … peut toutefois définir par arrêté les horaires pendant lesquels le stationnement est autorisé »).
- Correction: « Ligne discontinue : réservée aux livraisons les jours ouvrables de 7 h à 20 h, sauf autres horaires affichés ; en dehors, on peut y stationner. Double ligne continue : réservée en permanence. »
- (Outside the fact-check: the IISR also requires a yellow diagonal cross, which the image does not show.)

### a2a (field `signification` of inventory entry `A2a`, or add `signification` to the `a2a` override)
- Text: « Annonce une déformation naturelle ou accidentelle de la chaussée (creux « cassis » ou bosse « dos-d'âne ») qui n'est pas un aménagement volontaire. »
- Problem: no text limits A2a to natural or accidental deformations. It announces any pronounced cassis or dos-d'âne that is not a speed bump, including built ones such as the profile of some level crossings. What sets it apart from A2b is that it is not a ralentisseur.
- Evidence: IISR 2e partie art. 28: « Seuls peuvent être signalés les cassis ou dos d'âne accentués qui présentent un danger … Aux cassis ou dos d'âne présentant des difficultés de franchissement …, en particulier certains passages à niveau, le panneau A2a est complété par … « VÉHICULES SURBAISSÉS ATTENTION » » ; art. 28-1: A2b is used for the « ralentisseur de type dos-d'âne, coussins, plateaux ».
- Correction: « Annonce un cassis (creux) ou un dos-d'âne (bosse) marqué, dangereux à franchir vite, qui n'est pas un ralentisseur. »

## SUREXTENSION

### c207 (override `c207`, `complement`) — also CONTRADICTION
- Text: « 130 km/h (110 sous la pluie, 110 en permis probatoire) ; 80 minimum sur la voie de gauche. »
- Problem: the 80 km/h minimum applies only when traffic is fluid and visibility and grip are sufficient. The deck's own note `aff-r-autoroute-voie-gauche-80` (data/affirmations/04_route.yaml) teaches exactly those conditions and marks the unconditional version as « faux ».
- Evidence: R413-19: « En particulier sur autoroute, lorsque la circulation est fluide et que les conditions atmosphériques permettent une visibilité et une adhérence suffisantes, les conducteurs utilisant la voie la plus à gauche ne peuvent circuler à une vitesse inférieure à 80 km/h. »
- Correction: « 130 km/h (110 sous la pluie, 110 en permis probatoire) ; voie de gauche : 80 minimum si la circulation est fluide et le temps clair. »

### voyant-croisement (`data/reconnaissance/voyants.yaml`, `conduite`)
- Text: « Obligatoires la nuit, par visibilité réduite (pluie, brouillard, neige), dans les tunnels, et recommandés de jour. »
- Problem: 1) At night, the default rule is main beam (R416-5). Dipped beam is required only when main beam would dazzle, on a lit road, or in reduced visibility. On an unlit, empty road, main beam is the norm. 2) In reduced visibility, in a sufficiently lit built-up area, position lights are enough, except for motorcycles. 3) The day-time recommendation (Sécurité routière, 2004) concerns driving outside built-up areas.
- Evidence: R416-5: « les véhicules à moteur doivent circuler avec le ou leurs feux de route allumés » ; R416-6 II 1°-3° (« Toutefois, en agglomération, même par temps de pluie, cette disposition ne s'applique pas aux véhicules … qui circulent avec au moins leurs feux de position allumés, lorsque la chaussée est suffisamment éclairée ») ; C111 (arrêté 1967): « l'allumage des feux de croisement est obligatoire » in tunnels.
- Correction: « La nuit dès que les feux de route éblouiraient ou que la route est éclairée ; par visibilité réduite (sauf en ville bien éclairée : position) ; dans les tunnels ; conseillés de jour hors agglomération. »

### voyant-position (`voyants.yaml`, `conduite`)
- Text: « Obligatoires à l'arrêt ou en stationnement la nuit sur la chaussée (R416-12). »
- Problem: in a built-up area, a stopped or parked vehicle does not need lights when street lighting makes it clearly visible. A parking light on the traffic side can also replace them for a small vehicle in a built-up area.
- Evidence: R416-16: « En agglomération, tout véhicule à l'arrêt ou en stationnement peut ne pas être signalé lorsque l'éclairage de la chaussée permet aux autres usagers de voir distinctement celui-ci à une distance suffisante » ; R416-13 (feu de stationnement).
- Correction: « Obligatoires à l'arrêt ou en stationnement la nuit sur la chaussée (R416-12), sauf en agglomération suffisamment éclairée (R416-16). » (the rest of the field unchanged)

### b2c (override `b2c`, `complement`)
- Text: « Même sans ce panneau, le demi-tour est interdit sur autoroute, route express et dans un tunnel. »
- Problem: no general article bans U-turns in every tunnel. The ban comes with the C111 « tunnel » sign, which is compulsory only for tunnels longer than 300 m. On an autoroute or route express the ban comes from R421-6, which C107 makes applicable.
- Evidence: arrêté 1967, C111: « Ce panneau indique l'entrée d'un tunnel où il est interdit de faire demi-tour … » ; IISR 5e partie art. 75-2: « La signalisation d'une entrée de tunnel de plus de 300 mètres est obligatoire » ; R421-6.
- Correction: « Même sans ce panneau, le demi-tour est interdit sur autoroute, sur route express et dans un tunnel signalé par le panneau tunnel. Il ferait aussi circuler à contresens dans une rue à sens unique. »

### feu-jaune-clignotant (override `feu-jaune-clignotant`, `complement`) — minor
- Text: « Sur un feu tricolore, c'est la lampe du milieu qui clignote ; … »
- Problem: some tricolour lights have a flashing yellow **bottom** lamp in place of the green: R11j exceptionally, and KR11j at roadworks, where it is common. A learner who sees the bottom lamp flashing yellow would not recognise it.
- Evidence: IISR 6e partie art. 109-3 A: « Exceptionnellement … le vert peut être remplacé par du jaune clignotant (R11j) » ; IISR 8e partie art. 127: KR11 « vert (ou jaune clignotant) sur le feu inférieur … Un fonctionnement au jaune clignotant sur le feu médian peut être admis provisoirement ».
- Correction: « Le plus souvent, c'est la lampe du milieu qui clignote (parfois celle du bas, notamment aux feux de chantier) ; certains carrefours fonctionnent ainsi la nuit : ce n'est pas forcément une panne. »

## SOUS-EXTENSION

### voyant-brouillard-avant (`voyants.yaml`, `signification` and `conduite`) — also CONTRADICTION
- Text: « Les feux de brouillard avant sont en fonction, en complément des feux de croisement. » / « Je les utilise par brouillard, neige ou forte pluie … »
- Problem: front fog lights may **replace** the dipped beam, not only complement it. Outside built-up areas, on narrow and winding roads, they may also complement the main beam. The deck's own notes `aff-r-brouillard-avant-pluie` (« peuvent remplacer … », vrai) and `aff-r-brouillard-avant-sinueuse` (with main beam, vrai) state both rules.
- Evidence: R416-7 I: « En cas de brouillard, de chute de neige ou de forte pluie, les feux avant de brouillard peuvent remplacer ou compléter les feux de croisement. Ils peuvent compléter les feux de route en dehors des agglomérations, sur les routes étroites et sinueuses ».
- Correction: signification « Les feux de brouillard avant sont en fonction. » ; conduite « Par brouillard, neige ou forte pluie, à la place ou en plus des feux de croisement ; hors agglomération sur route étroite et sinueuse, avec les feux de route. Je les éteins dès que la visibilité revient (ils éblouissent). »

### conf-b52-b54 (`data/confusions/signalisation.yaml`, id `conf-b52-b54`)
- Text: « B, adulte et enfant : aire piétonne ; seuls les véhicules de desserte et les cycles y circulent, à l'allure du pas. »
- Problem: EDPM and cyclomobiles légers may also ride in a pedestrian area at walking pace. Cycles are admitted unless the authority decides otherwise. « Seuls » wrongly excludes EDPM.
- Evidence: R110-2 (aire piétonne): « sous réserve des dispositions des articles R. 412-43-1 et R. 431-9, seuls les véhicules nécessaires à la desserte interne de la zone sont autorisés à circuler à l'allure du pas » ; R412-43-1 I 2° (EDPM, « sur les aires piétonnes ») and R412-43-4 (applies to cyclomobiles légers) ; R431-9: cycles « sauf dispositions différentes prises par l'autorité ».
- Correction: « B, adulte et enfant : aire piétonne ; seuls les véhicules de desserte, les cycles et les trottinettes électriques y circulent (sauf interdiction locale), à l'allure du pas. »

### c6 (override `c6`, `conduite`)
- Text: « … ralentir et au besoin s'arrêter pour laisser le bus quitter son arrêt lorsqu'il annonce son départ par le clignotant (R412-11). »
- Problem: R412-11 sets no condition about the indicator. The duty applies as soon as the bus leaves a stop signed as such in a built-up area.
- Evidence: R412-11: « En agglomération, tout conducteur doit ralentir si nécessaire et au besoin s'arrêter pour laisser les véhicules de transport en commun quitter les arrêts signalés comme tels. »
- Correction: « Ne pas s'arrêter sur l'emplacement. En agglomération, ralentir et au besoin s'arrêter pour laisser le bus quitter son arrêt (R412-11) ; son clignotant annonce ce départ. »

### b6b4 (override `b6b4`, add `conduite`) — minor
- Text: « Payer et afficher le ticket ; sinon forfait post-stationnement (FPS). »
- Problem: proof of payment can also be sent electronically (app, plate). The card itself mentions « paiement mobile », and « afficher le ticket » then contradicts it.
- Evidence: R417-3-1: « le justificatif du paiement est : 1° Soit placé à l'avant du véhicule, bien lisible de l'extérieur ; 2° Soit transmis par voie dématérialisée ».
- Correction: « Payer (ticket placé à l'avant, ou paiement dématérialisé) ; sinon forfait post-stationnement (FPS). »

## SOURCE

### agent-bras-leve, agent-bras-tendu-face, agent-profil (overrides of the same keys; field `source`/`references` of the inventory entries)
- Text: sources « IISR (Instruction interministérielle sur la signalisation routière) ; Wikipédia FR ».
- Problem: none of the 9 IISR parts describes the traffic officer's gestures (checked: no « bras » outside « charrettes à bras »). These gestures come from the Convention de Vienne sur la circulation routière of 8 November 1968, art. 6, which France has ratified. R411-28 gives them precedence. The content of the three cards matches art. 6, except that agent-bras-leve leaves out the exception for drivers who can no longer stop safely.
- Evidence: Convention de Vienne 1968, art. 6 (UNECE, Conv_road_traffic_FR.pdf): « le bras levé verticalement … signifie « attention, arrêt » pour tous les usagers, sauf pour les conducteurs qui ne pourraient plus s'arrêter dans des conditions de sécurité suffisantes … ; si ce signal est donné dans une intersection, il n'oblige pas à s'arrêter les usagers déjà engagés » ; « le ou les bras tendus horizontalement signifient « arrêt » pour tous les usagers venant de directions qui coupent celle indiquée par le ou les bras tendus … ; pour les usagers qui se trouvent devant ou derrière l'agent, ce geste signifie également « arrêt » ». R411-28: « Les indications données par les agents réglant la circulation prévalent sur toutes signalisations ».
- Correction: source « Convention de Vienne sur la circulation routière (1968), art. 6 ; Code de la route, R411-28 ». agent-bras-leve, signification: « Bras levé verticalement : « attention, arrêt » pour tous, sauf ceux déjà engagés dans l'intersection, qui la dégagent, et ceux qui ne peuvent plus s'arrêter sans danger. »

## INCERTAIN

- **agent-geste-avancer**: « Un va-et-vient du bras dans le sens de la circulation invite à avancer ou à accélérer ». Art. 6 of the Convention de Vienne lists only the raised arm, the outstretched arms and the swinging red light. Neither the Code nor the IISR defines this gesture. It is a usage convention, and the card should name it as one (e.g. « geste d'usage, non défini par les textes : il invite à avancer »). SOURCE: IISR does not contain it.
- **marq-zebra**: « Zone hachurée … interdite à la circulation, à l'arrêt et au stationnement » and « bordé d'une ligne discontinue = franchissable en cas de nécessité ». IISR 7e partie art. 117-2 describes the hatchings as covering « surfaces de chaussées normalement inutilisées » inside a « zone non circulable » bounded by continuous 3u lines. I found no text for the ban on stopping and parking (it is not among the cases of R417-10/R417-11), nor for a hatched area bordered by a discontinuous line. Owner's source to check: arrêté 1967, art. on marks (not accessible in full via Légifrance here). Suggestion if no source is found: « Zone hachurée : on n'y circule pas (îlot peint, biseau, musoir) » and drop the second sentence.
- **marq-passage-cyclistes**: « matérialisée par deux rangées de carrés blancs de 50 cm ». The IISR 7e partie in force (VC 2025-04-04, art. 118-1 C) describes cycle crossings with « bandes rectangulaires blanches parallèles à l'axe de la chaussée dont la largeur se déduit des bandes [piétons] par une homothétie de rapport ½ … interdistance … 0,40 m », and no longer mentions squares. The squares survive on the ground in older markings. Suggestion: « … matérialisée par des bandes blanches étroites (ou, sur d'anciens marquages, deux rangées de carrés) ». The priority rules on the card are correct (R415-3 III, R415-4).
- **b14**: « Posée sur un panneau de danger, elle ne vaut que pour ce danger. » I found no text for this. IISR 4e partie art. 63 d says only that a B14 with a danger sign « peut être complété d'un panonceau M2 », and art. 63 e says that outside built-up areas a limit is repeated after each intersection. Keep this as a teaching shortcut, labelled as such, or source it.
- **c107** and **conf-c107-c207**: the cards say C107 does not set 110 km/h by itself (80 on a single carriageway, R413-2). Their accesses and manoeuvres (R421-2, R421-4 to R421-7) are verified. But the arrêté du 24 novembre 1967 (Légifrance version 2025-04-25) still says for C107: « … et sur laquelle, sauf indication contraire, la vitesse maximale des véhicules est fixée à 110 km/h ». The decree (R413-2 I 3°, « 80 km/h sur les autres routes ») ranks above the arrêté and is later, so the card is probably right. The conflict is worth logging in `source_checks.yaml`; the current entry `scenes-c107-configurations` does not mention it. No text change proposed.

## Notes (verdict OK, for information)
- `b56`: the ZFE still exist in 2026. The Conseil constitutionnel censured their abolition on 21/05/2026, and R411-19-1 (3rd class, 68 € for M1) is in the Code of 10/09/2026.
- `marq-marquage-temporaire-jaune`: « prévalent » is inferred from the IISR (8e partie art. 120 B and 122 B: the permanent marking « doit être effacé ou masqué »). I found no text using the word « prévaut ».
- `voyant-direction`: the reference ISO 7000-2305 was not verified (metadata, not a claim the learner memorises).
