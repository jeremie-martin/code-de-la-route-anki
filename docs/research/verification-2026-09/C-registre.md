# Ledger — group C (conducteur + route), 157 notes, in C_ids.txt order

Abbreviations: CdR = Code de la route consolidé 10/09/2026 (docs/research/sources/cdr.txt). SR-alcool = https://www.securite-routiere.gouv.fr/sites/default/files/2024-03/depliant_alcool-conduite-070823.pdf (text extracted). SR-fatigue = https://www.securite-routiere.gouv.fr/sites/default/files/2023-05/sets_fatigue.pdf. ONISR-2024 = https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2025-09/Bilan%20SR%202024%20version%20site%20internet%2012%20septembre.pdf. ONISR-2025 = https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2026-06/Accidentalit%C3%A9_Routi%C3%A8re_2025_v7_0.pdf (données définitives 2025). CETU = https://www.cetu.developpement-durable.gouv.fr/conduire-en-tunnel-a1597.html. CETU-22 = https://www.cetu.developpement-durable.gouv.fr/IMG/pdf/CETU-Note_Info_22_2011.pdf. IISR-5 = https://www.sdnsd.developpement-durable.gouv.fr/IMG/pdf/iisr_5epartie_vc_20220613.pdf.

aff-c-champ-visuel-vitesse-pieton | OK | SR vitesse (via dordogne.gouv.fr relay: « plus la vitesse augmente, plus le champ visuel est réduit ») | Qualitative, no angle table claimed.
aff-c-vision-peripherique | OK | general physiology; SR « La vue » | Descriptive, no figure.
aff-c-nuit-distances | OK | SR Conduire la nuit (qualitative) | No figure.
aff-c-regard-obstacle | OK | REMC / teaching principle | Advice presented as advice.
aff-c-temps-reaction-vitesse | OK | Cerema V80 annexe 2 (logged revue-deck-distances); physics | Distance doubles at constant reaction time: correct.
aff-c-pieton-detectable-motard | OK | SR exemples 2023 Q11 (logged corpus) | Advice.
aff-c-enfant-percoit-adulte | OK | SR enfants piétons | Avoids age figure.
aff-c-enfant-croit-vu | OK | SR enfants piétons | Advice.
aff-c-indice-danger-certain | OK | anticipation principle; R413-17 III 4° (« route ne lui apparaît pas entièrement dégagée ») | —
aff-c-klaxon-ecole | OK | CdR R416-1 (« En agglomération… qu'en cas de danger immédiat ») | —
aff-c-retros-suffisent | OK | SR angles morts | —
aff-c-pause-sans-signe | OK | SR-fatigue (« faites une pause toutes les deux heures et arrêtez-vous dès les premiers signes ») | —
aff-c-repas-copieux | OK | SR fatigue / press kit (2 h–5 h et 13 h–15 h périodes à risque) | —
aff-c-nuit-trafic-fluide | FIX | ONISR-2024 (« En 2024, 42 % des tués le sont de nuit »); ONISR-2025 (no night share) | SOURCE: figure is from bilan 2024, not « bilan 2025 ».
aff-c-senior-reaction | OK | SR seniors (qualitative) | —
aff-c-lunettes-points | OK | CdR R221-1-1 I, III (4e classe), V (suspension), VI (3 points) | 135 € = amende forfaitaire 4e classe.
aff-c-doses-maison | OK | SR-alcool (« À la maison, les doses servies sont souvent plus importantes »; 10 g) | —
aff-c-biere-whisky | OK | SR-alcool (« autant d'alcool dans un verre de bière ou de vin que dans un verre de whisky-soda, soit l'équivalent de 10 g ») | —
aff-c-alcool-sous-seuil | OK | SR-alcool (« Les conséquences… peuvent être observées dès le premier verre »); CdR R234-1 | —
aff-c-alcool-jugement | OK | SR-alcool (« sous-évalue les risques et surestime ses capacités ») | —
aff-c-alcool-eblouissement | OK | SR-alcool (« la sensibilité à l'éblouissement est plus importante ») | —
aff-c-dernier-verre-depart | OK | SR-alcool (« maximum 30 minutes après une absorption à jeun et 1 heure… au cours d'un repas ») | Labelled as averages.
aff-c-cafe-dessoule | OK | SR-alcool (« Il n'existe aucune "recette" pour éliminer l'alcool plus rapidement ») | —
aff-c-lendemain-matin | OK | SR-alcool (0,10–0,15 g/L/h) ; arithmetic: 6 h ≈ 0,6–0,9 g/L eliminated, so a high peak can still exceed 0,5 | —
aff-c-probatoire-un-verre | OK | CdR R234-1 I 1°; SR-alcool (« cette limite peut être dépassée dès le premier verre ») | —
aff-c-cannabis-veille | FIX | F2886 (no detection duration); Drogues Info Service « durée de positivité d'un test salivaire » | SOURCE: claim true (« peut ») but F2886 does not state it.
aff-c-medicament-sans-ordonnance | INCERTAIN | ANSM dossier; arrêté 8 août 2008; Vidal (level 3 = hypnotics, anaesthesia, psychiatry injectables, mydriatics) | « voire 3 » for OTC not found in any source.
aff-c-somnifere-soir | OK | ANSM levels; Vidal (hypnotics level 3) | « 2 ou 3 » covers anxiolytics/hypnotics.
aff-c-medicament-alcool | OK | SR médicaments; ANSM | —
aff-c-mains-libres-passager | OK | SR téléphone; CdR R412-6-1 (integrated kit not prohibited) | Advice framed as advice.
aff-c-oreillette | OK | CdR R412-6-1 al. 2 (port à l'oreille, exception correcteurs de surdité), 4e classe, 3 points; décret 2015-743 (1/7/2015) | —
aff-c-gps-roulant | OK | arithmetic 50/3,6×5 = 69 m; R412-6-2 allows navigation screen | —
aff-c-ecran-video | OK | CdR R412-6-2 (5e classe, saisie/confiscation, 3 points) | —
aff-c-alcool-un-sur-trois | OK | SR-alcool (« près de 30 % des accidents mortels »); ONISR-2025 (« 2021-2025… 28 % des personnes tuées… au moins un conducteur… supérieur à 0,5 g/l »); SR page (risque ×18, via search) | —
aff-c-jeunes-risque-double | OK | ONISR-2025 (« 2 fois plus que la moyenne »; 528 tués/3 263 = 16 %; « 8 % de la population ») | —
aff-c-musique-forte | OK | CdR R412-6-1 | —
aff-c-senior-visite-70 | FIX | CdR R221-10 I, R226-1; service-public F2882 | SUREXTENSION: « Chacun doit… faire vérifier sa vue » states an obligation that does not exist.
aff-r-descente-150m | OK | IISR 1re/2e partie as recorded in inventory (hors agglo ≈150 m, agglo ≈50 m, M1 otherwise) | « environ » present.
aff-r-pn-150m | OK | IISR (A7/A8 ≈150 m; J10 on A7/A8 support then 2/3 and 1/3 → 150/100/50 m) | —
aff-r-pn-feux-rouges-possibles | OK | SR Q19 (A7 + M9z « signal automatique »); IISR G2/R24 | —
aff-r-pn-barriere-contourner | OK | CdR R422-3 II (« fermées, soit en cours de fermeture ou d'ouverture »); SNCF Réseau (« un train lancé à 100 km/h a besoin d'1 km ») | —
aff-r-insertion-prioritaire | OK | CdR R421-3 | —
aff-r-autoroute-voie-gauche-80 | OK | CdR R413-19, R413-17 | Logged revue-ordre-apprenant.
aff-r-autoroute-vitesse-pluie | OK | CdR R413-2 II 1°, R413-5 I 1° | Context states « normalement limitée à 130 ».
aff-r-autoroute-cyclo | OK | CdR R421-2 I 5° | —
aff-r-autoroute-aac | FIX | CdR R413-5 I 1°–2° | SUREXTENSION: « 110 km/h sur autoroute » — 100 on autoroutes normally below 130.
aff-r-autoroute-bouchon-detresse | OK | CdR R416-18 (dernier véhicule de la file) | —
aff-r-peage-reculer | OK | CdR R421-6 | —
aff-r-brouillard-arriere-pluie | OK | CdR R416-7 II, III (4e classe = 135 €) | —
aff-r-brouillard-avant-pluie | OK | CdR R416-7 I | —
aff-r-brouillard-avant-sinueuse | OK | CdR R416-7 I, II | —
aff-r-brouillard-feux-route | FIX | CdR R416-6 II 3°, R416-7 I | SUREXTENSION (minor): R416-6 excludes high beams, but fog lights « peuvent remplacer » dipped beams — « impose… les feux de croisement » too absolute.
aff-r-visibilite-50-autoroute | OK | CdR R413-4 | —
aff-r-aquaplaning-freiner | OK | SR pluie / advice | —
aff-r-montagne-ms | OK | décret 2020-1264; service-public F19459 (symbole alpin + M+S; M+S seul sans chaînes non admis) | —
aff-r-montagne-4-pneus | OK | décret 2020-1264; F19459 | —
aff-r-verglas-pont | OK | physics / advice | —
aff-r-verglas-temperature-positive | OK | physics / advice | —
aff-r-neige-depassement-pl | OK | CdR R414-17 I 1° | —
aff-r-nuit-feux-position-agglo | OK | CdR R416-6 II 2°, 3° | Logged v9-eclairage.
aff-r-nuit-feux-route-arret | FIX | CdR R416-5, R416-12 I | SOURCE: second sentence (feux de position à l'arrêt) is R416-12, not cited.
aff-r-nuit-pieton-sombre | OK | SR Conduire de nuit; R313-3 (30 m) | Qualitative; no figure.
aff-r-tunnel-demi-tour | OK | IISR C111 (demi-tour et arrêt interdits, feux de croisement); CETU (« Reversing, U-turns… forbidden ») | Engine-off/radio = advice.
aff-r-tram-station-pieton | OK | CdR R414-13 | —
aff-r-chantier-sans-ouvriers | OK | IISR 8e partie; CdR R411-25 | —
aff-r-vent-deux-roues | OK | SR vent (advice); R414-4 IV minimum | —
c-temps-reaction | OK | SR / prep sources (≈1 s pour conducteur attentif) | Labelled « repère pédagogique ».
c-distance-reaction-formule | OK | arithmetic 90/3,6×2 = 50 m | —
c-distance-mouillee | OK | SR exemples 2023 Q13 (logged) | Labelled as the exercise's hypothesis.
c-vitesse-double-freinage | OK | physics v² | Labelled « modèle simplifié ».
c-intervalle-2s | OK | CdR R412-12 I, V, VII; arithmetic 27,8 / 72,2 m; 30 / 78 m | Both cards.
c-intervalle-pl-tunnel | OK | CdR R412-12 II, IV | —
c-autoroute-deux-traits | OK | CETU-22 (« deux traits blancs longs de 39 mètres espacés… de 13 mètres représentent… 91 mètres… 130 km/h… environ 72 mètres ») | Labelled « repère visuel usuel ».
c-acuite-5-10 | OK | arrêté 28 mars 2022 (binoculaire ≥ 5/10; œil < 1/10 → autre ≥ 5/10; champ horizontal ≥ 120°); R221-1-1 | —
c-fatigue-pause-chiffres | OK | SR-fatigue; SR sieste 15–20 min | Labelled « repère ». Both cards.
c-verre-standard | OK | SR-alcool; arithmetic 25 cl×5 %×0,8 = 10 g; 10 cl×12 % = 9,6 g; 3 cl×40 % = 9,6 g | —
c-verre-alcoolemie | OK | SR-alcool (« en moyenne… 0,25 g ») | Range 0,20–0,25 labelled « repère moyen ».
c-alcool-elimination | OK | SR-alcool (0,10–0,15 g/L/h; pic 30 min / 1 h) | Both cards.
c-conversion-air-sang | OK | CdR R234-1 (0,20↔0,10; 0,50↔0,25), L234-1 (0,80↔0,40) | —
c-medicaments-niveaux | OK | ANSM (niveau 1 « Ne pas conduire sans avoir lu la notice », 2 « sans l'avis d'un professionnel de santé », 3 « ne pas conduire… demandez l'avis d'un médecin »; ≈ un tiers) | Three cards.
c-alcool-seuils-sang | OK | CdR R234-1 I 1°–2° | Both cards.
c-energie-choc | OK | physics: (13,9)²/19,62 = 9,8 m | —
r-train-distance-arret | OK | SNCF Réseau (1 km à 100 km/h) | Labelled « ordre de grandeur ».
r-loi-montagne-periode | OK | décret 2020-1264; F19459; IISR 67-1 | —
r-tunnel-niches | OK | CETU (issues « flèches vertes »; niches « not shelters ») | —
r-autoroute-sortie-annonces | FIX | IISR-5 art. 83-6 (D50 « à environ 60 secondes de parcours… échangeurs… espacés d'au moins 5 km »; note 3 « échangeurs très rapprochés… pas mise en place »), 83-4 (D41 ≈ 30 s), 83-2; CdR R421-4 II | SUREXTENSION: 2 000 m warning presented as universal. Both cards.
c-regarder-loin | FIX | no official source for a mirror interval | CONVENTION-NON-SIGNALÉE: « La règle : … toutes les 5 à 10 secondes ».
c-croisement-nuit-regard | OK | SR exemples Q20; R416-6 II 1° a | —
c-angle-mort-definition | FIX | no official source for duration | CONVENTION-NON-SIGNALÉE (minor): « moins d'une seconde » as a fact.
c-ordre-controles-changement-file | OK | R412-10; teaching sequence labelled as not recited | —
c-clignotant-avant-ralentir | OK | CdR R412-10 | —
c-zone-attention-pluie | OK | SR exemples Q9 | —
c-enfant-masque | OK | SR exemples Q3 | —
c-trottinette-vulnerable | OK | CdR R414-4 IV (« engin à deux ou à trois roues » 1 m / 1,5 m) | —
c-cycliste-devant-depassement | OK | CdR R414-4 I, II | —
c-retro-avant-freiner | OK | advice | —
c-indice-feux-recul | INCERTAIN | CdR R416-20, R412-10; search for a yielding rule when leaving on-street parking (none found) | « et céder le passage » not supported by the cited articles.
c-indice-bus-arrete | OK | CdR R412-11 | —
c-indice-ballon | OK | advice | —
c-indice-cycliste-regard | OK | advice | —
c-indice-vehicule-stationne-portiere | OK | advice (≈1 m) | —
c-routine-monotonie | OK | advice | —
c-somnolence-que-faire | OK | SR-fatigue | —
c-fatigue-remedes-faux | OK | SR-fatigue | —
c-vitesse-fatigue | OK | SR vitesse (relayed by dordogne.gouv.fr: « Rouler vite fatigue… champ visuel est réduit ») | —
c-telephone-arret | OK | CdR R412-6-1; L224-1 I 7°; R224-19-1 (feux R412-30, vitesse, R415-6/-7, R415-11) | « priorité » in list = STOP/cédez/piéton, not R415-5; acceptable.
c-cannabis-effets | FIX | F2886 (interdiction après usage; no duration); Drogues Info Service | SOURCE: effect/detection durations not in F2886.
c-emotions | OK | advice | —
c-passagers-pression | OK | SR novices | « réduit l'impatience » is an unsourced aside, not a rule.
c-suiveur-trop-pres | OK | CdR R412-12 | —
c-distance-arret-composantes | OK | Cerema V80 (logged) | —
c-telephone-5s | OK | arithmetic 69,4 m; 15×5 = 75 m | —
c-double-vitesse-arret | OK | physics 20 + 40 = 60 m | —
c-intervalle-repere | OK | CdR R412-12 I | —
c-alcool-unites-probatoire | OK | CdR R234-1 I 1° (« égale ou supérieure… 0,10 milligramme ») | —
c-occlusion-pieton | OK | CdR R414-5, R415-11 | —
c-distance-obstacle-exercice | OK | arithmetic 15 + 25 = 40 > 35 | —
c-virage-technique | OK | physics (centripetal force ∝ v²) | —
r-nuit-feux-croisement-route | OK | CdR R416-6 II 1°–3°, III | —
r-nuit-suivre-vehicule-feux | OK | CdR R416-6 II 1° b | —
r-nuit-gabarit-camion | OK | CdR R313-10 I (> 2,10 m); R416-6 | —
r-nuit-vitesse-visibilite | FIX | CdR R313-3 I (« distance minimale de 30 mètres »), R413-17 | SOURCE: 30 m claim sourced only to R413-17.
r-pluie-feux | OK | CdR R416-4, R416-6 II 3°, R416-7 | —
r-pluie-premieres-gouttes | OK | advice | —
r-aquaplaning | OK | advice | —
r-brouillard-feux | FIX | CdR R416-6, R416-7, R416-12 | SOURCE: « À l'arrêt… feux de position » is R416-12, not cited.
r-brouillard-intervalle | OK | CdR R413-4 | —
r-neige-conduite | OK | physics (μ neige ≈ 0,2 vs 0,8 → ×4; verglas 0,05–0,1 → ×8–16) | Labelled « Ordres de grandeur »; no official page found stating ×4 on snow.
r-verglas-descente | OK | advice | —
r-deneigement-depassement | OK | CdR R414-17 I 2°, II; R311-1 6.6 | —
r-vent-lateral | OK | advice; A24/J7 | —
r-soleil-bas | OK | advice | —
r-tunnel-feux-jour | OK | CETU (« Allumez vos feux de croisement »); IISR C111 (allumage obligatoire) | —
r-tunnel-distance-arret | FIX | CETU-22 (« distance… à l'arrêt de 5 mètres. Cette notion… n'a toutefois pas été transposée en droit français ») | SUREXTENSION/SOURCE: « sans distance propre à l'arrêt, je garde la même qu'en circulation » not supported.
r-tunnel-panne | OK | CETU (hazards, engine off, vest, niche, call post) | « voit le tunnel en vidéo » generalises; not a rule.
r-tunnel-incendie | OK | CETU (« Évacuer… suivant les flèches vertes ») | —
r-tunnel-mon-vehicule-feu | OK | CETU; logged rev12 | —
r-pn-feu-rouge-clignotant | OK | CdR R412-30 (« rouge, fixe ou clignotant », 4 points), R422-3 | —
r-pn-engagement | OK | CdR R422-3 II, R414-12 | —
r-pn-bloque | OK | CdR R422-3 V; SNCF Réseau | —
r-pn-sans-barriere | OK | CdR R422-3 II, R414-12; IISR G1/G1a | —
r-pn-barrieres-ouverture | OK | CdR R422-3 II | —
r-tram-priorite | OK | CdR R422-3 I, R414-13; IISR 3e partie 42-9 B 3° (logged tram-priorite-iisr) | « sur tous les usagers »: vis-à-vis des VIG prioritaires non tranché, left as is.
r-tram-traversee-degager | OK | CdR R422-3 I–II | R417-11 concerns arrêt/stationnement, weak but R422-3 II suffices.
r-chantier-fleche-lumineuse | OK | IISR 8e partie art. 133 F (logged) | —
r-autoroute-sortie | OK | CdR R413-17, R421-4 | —
r-autoroute-bau | OK | CdR R412-8 (4e classe, 3 points), R421-7 | —
r-autoroute-panne | OK | CdR R421-7, R416-19 | —
r-autoroute-panne-attendre | OK | SR panne autoroute; R421-7 | —
r-autoroute-usagers-interdits | OK | CdR R421-2 I | —
r-autoroute-peage | OK | ASFA; IISR-5 84-3 | Zipper merge = advice.
r-autoroute-fatigue-aires | OK | IISR-5 art. 84-2 (« à 2000 m… à 1000 m »); SR-fatigue | —
r-montagne-croisement-difficile | OK | CdR R414-3 I, R414-2 | —
r-montagne-marche-arriere | OK | CdR R414-3 II, III | —
r-descente-freinage | OK | SR exemples Q18; R413-17 III 7° | —
r-b26-pneus-equivalence | OK | IISR 67-1 (arrêté 23 juin 2021, logged b26-equivalence) | —
r-b26-chaines-complement | OK | idem | —
