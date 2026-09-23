# Sources

Une citation est nécessaire mais ne suffit pas : elle doit couvrir **la phrase et ses conditions**. Une
référence générique (« Code de la route », « ISO 2575 ») ne valide pas une consigne de conduite. Chaque
consultation ciblée est inscrite dans [`data/_meta/source_checks.yaml`](../data/_meta/source_checks.yaml) :
date, lien, portée écrite, notes concernées. La vérification de chaque note du 23 septembre 2026 est archivée
dans [`research/verification-2026-09`](research/verification-2026-09/README.md).

## Références primaires

| Sujet | Référence | Ce qu’elle établit |
|---|---|---|
| Code de la route | [Légifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074228/) ; copie consolidée au 10 septembre 2026 dans `research/sources/` (`pdftotext -layout` → `cdr.txt` ; article cherchable par `^R. 415-5 `) | Toute règle, tout seuil et toute sanction |
| Signalisation | Arrêté du 24 novembre 1967 ; Instruction interministérielle sur la signalisation routière (IISR, parties 1 à 9, [Cerema](https://equipementsdelaroute.cerema.fr/)) | Sens, implantation et catégories des signaux et marquages |
| Gestes des agents | Convention de Vienne sur la circulation routière (1968), art. 6 ; Code, R411-28 | Bras levé, bras tendus ; primauté de l’agent |
| Examen | [Service Public, ETG](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694) ; [exemples officiels de questions, 2023](research/sources/securite-routiere_exemples_nouvelles_questions_code_2023-09.pdf) ; [communiqué DSR, 2023](research/sources/dsr_communique_banque-etg_2023-09-11.pdf) ; arrêté du 16 avril 2026 (organisation) | Format, seuil, formes des questions |
| Secours | [Références techniques nationales PSC, juillet 2026](https://www.securite-civile.interieur.gouv.fr/sites/securitecivile/files/medias/documents/2026-07/References-techniques-nationales-PSC_juillet-2026.pdf) ; securite-routiere.gouv.fr, « Accident de la route » | Conduites à tenir selon l’état de la victime |
| Conseils officiels | securite-routiere.gouv.fr (pages lisibles avec `?_format=json`) ; service-public.gouv.fr (fiches datées « vérifié le ») | Recommandations et démarches, présentées comme telles |
| Aides à la conduite | [CNSR, ADAS (2024)](https://www.securite-routiere.gouv.fr/sites/default/files/2024-06/les_aides_a_la_conduite_%28adas%29.pdf) | Fonctions et limites des systèmes |
| Véhicule | Notices constructeurs ; Michelin (pression) | Valeurs propres à un véhicule, à ne pas universaliser |
| Écoconduite, émissions | [ADEME](https://agirpourlatransition.ademe.fr/particuliers/economiser/carburant/ecoconduite-solution-consommer-moins-carburant-limiter-emissions-co2) | Gestes et mécanismes |
| Anki | [Options de deck](https://docs.ankiweb.net/deck-options), [paquets](https://docs.ankiweb.net/importing/packaged-decks.html) | Ordre de collecte, enfouissement, préréglages |

Les supports de préparation (Codes Rousseau, ENPC, Ornikar, En Voiture Simone…) servent à repérer les sujets et
les raccourcis pédagogiques ; ils ne certifient pas une règle. Une recherche web remonte souvent des règles
d’autres pays (Suisse, Belgique) : vérifier que le texte est français.

## Veille

À chaque édition, reconsulter en priorité : sanctions et permis (lois récentes), ZFE et voies réservées,
EDPM, équipements hivernaux, recommandations de secours, aides à la conduite obligatoires, et les points
ouverts du registre : liste des substances de L237-1 (non publiée en septembre 2026), fin de l’exception des
places dans les 5 m avant un passage piéton (`passages-pietons-2027`), calendrier GSR2 des aides obligatoires,
chiffres ADEME non revalidés.
Mettre à jour `source_checks.yaml` seulement après une consultation effective.
