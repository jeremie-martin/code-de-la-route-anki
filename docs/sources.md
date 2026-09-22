# Sources

Une citation est nécessaire mais ne suffit pas : elle doit couvrir **la phrase et ses conditions**. Une
référence générique (« Code de la route », « ISO 2575 ») ne valide pas une consigne de conduite. Le registre
[`data/_meta/source_checks.yaml`](../data/_meta/source_checks.yaml) associe chaque consultation ciblée à sa
date, sa portée écrite et les notes concernées ; il ne prétend pas que toute la bibliothèque a été relue à
cette date.

## Références primaires

| Sujet | Référence | Ce qu’elle établit |
|---|---|---|
| Code de la route | [Légifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074228/) ; copie consolidée au 10 septembre 2026 dans `docs/research/sources/` (`pdftotext -layout` → `cdr.txt`, article `R. 415-5` cherchable) | Toute valeur juridique : vitesses (R413), priorités (R415), dépassement et croisement (R414), arrêt et stationnement (R417), éclairage (R416), autoroute (R421), alcool et stupéfiants (L234, L235, R234), permis et points (L223, R221), équipements (R311–R323, D314-8) |
| Examen | [Service Public, ETG](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694) ; [exemples officiels de questions, sept. 2023](research/sources/securite-routiere_exemples_nouvelles_questions_code_2023-09.pdf) ; [communiqué DSR sur la banque 2023](research/sources/dsr_communique_banque-etg_2023-09-11.pdf) ; arrêté du 16 avril 2026 (organisation au 1er juillet 2026, sans changement de contenu ni de seuil) | Format, seuil, formes des questions, réponses attendues sur vingt exemples |
| Signalisation | Instruction interministérielle sur la signalisation routière (IISR, parties 1 à 8) ; arrêté du 24 novembre 1967 consolidé | Sens, implantation, catégories des signaux |
| Secours | [Références techniques nationales PSC, juillet 2026](https://www.securite-civile.interieur.gouv.fr/sites/securitecivile/files/medias/documents/2026-07/References-techniques-nationales-PSC_juillet-2026.pdf) | Conduites à tenir selon l’état de la victime |
| Aides à la conduite | [CNSR, comité des experts — ADAS (2024)](https://www.securite-routiere.gouv.fr/sites/default/files/2024-06/les_aides_a_la_conduite_%28adas%29.pdf) | Fonctions et limites des systèmes |
| Fiches pratiques | service-public.gouv.fr (permis F2828, points F1685/F2390, invalidation F1704, contrôle technique F2878, équipements F19459, sanctions vitesse F19460, alcool F31551) | Règles administratives, avec leur date « vérifié le » |
| Pneumatiques, entretien | Préconisations constructeur (exemple : notice Renault pour les témoins), Michelin pour la pression | Valeurs propres au véhicule : à ne pas universaliser |
| Écoconduite, émissions | [ADEME](https://agirpourlatransition.ademe.fr/particuliers/economiser/carburant/ecoconduite-solution-consommer-moins-carburant-limiter-emissions-co2), notices constructeur ; [étude IFPEN 2020](https://www.ifpenergiesnouvelles.fr/article/emissions-des-voitures-essence-et-diesel-recentes-publication-letude-realisee-ifpen) | Gestes et mécanismes ; une mesure sur un échantillon ne classe pas tout le parc |
| Anki | [Options de deck](https://docs.ankiweb.net/deck-options), [paquets](https://docs.ankiweb.net/importing/packaged-decks.html) | Ordre de collecte, enfouissement, import des préréglages |

Les supports de préparation (Codes Rousseau, ENPC, Ornikar, En Voiture Simone, Stych…) servent à repérer
les sujets et les raccourcis pédagogiques (ordre de grandeur des distances, repères d’écoconduite). Ils ne
certifient pas les réponses de la banque. Les dossiers `research/*.md` sont des notes de recherche historiques,
avec des hypothèses parfois remplacées ; vérifier la source actuelle avant de réutiliser un passage.

## Règles récentes (entrées datées du registre)

Délit dès 50 km/h d’excès (L413-1, en vigueur depuis le 29 décembre 2025) ; 9 points pour le cumul alcool +
stupéfiants (L235-1 IV, loi 2026-798 du 18 août 2026) ; ZFE maintenues (décision du Conseil constitutionnel du
21 mai 2026) ; circulation inter-files des deux-roues (R412-11-3, décret 2025-33) ; casque et gilet pour les
EDPM à Paris et dans les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne depuis le 7 août 2026 (mesure
locale) ; permis B dès 17 ans (R221-5) ; 3PMSF + M+S pour les pneus hiver (D314-8) ; suppression des places dans
les 5 m avant les passages piétons au 31 décembre 2026 (L118-5-1 du Code de la voirie routière : à revérifier
pour une édition 2027). Chacune a une entrée dans `source_checks.yaml` ; le registre décrit la consultation, mais le texte officiel actuel fait foi.

## Ce qui reste non vérifié sur une source primaire

Les dates des obligations d’équipement des voitures neuves (ISA, AEB : règlement GSR2, juillet 2024, de mémoire),
le détail de certains signaux hérités de Wikipédia (dimensions des balises J10, pictogramme exact de B56), les
consignes locales des exploitants (distances propres à chaque tunnel, péages en flux libre), les chiffres ADEME cités dans les
explications, la date exacte des obligations d’équipement des sièges enfants. Ils n’apparaissent pas comme
cibles de rappel.

Euro NCAP : [le protocole 2026](https://www.euroncap.com/press-media/euro-ncap-announces-2026-protocol-changes-to-tackle-modern-driving-risks/)
a été consulté le 22 septembre 2026 ; la carte ne présente plus l’ancienne grille comme actuelle.
Les sondages juridiques et les corrections de cette édition sont détaillés dans le registre, sans
assimiler l’import réussi du paquet à une validation du fond.

## Veille

À chaque édition, reconsulter en priorité : ZFE et voies réservées locales, EDPM, équipements hivernaux,
sanctions et permis, recommandations de secours, aides à la conduite obligatoires. Mettre à jour
`source_checks.yaml` seulement après une consultation effective.

Consultation ciblée du 22 septembre 2026 : PSC juillet 2026, pages 26–38. Les cartes distinguent désormais
malaise sans traumatisme (PLS) et traumatisme ou cause inconnue (sur le dos, alerte, voies aériennes libres,
surveillance ; sur le côté en cas de vomissements ou selon les secours). Aucun corrigé ETG 2026 vérifié ne
permet d’affirmer une exception à cette conduite. Le corrigé d’un exemple de 2023 ne suffit pas à en créer une.
