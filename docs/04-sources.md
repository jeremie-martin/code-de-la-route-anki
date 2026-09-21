# Sources et périmètre de vérification

Une citation est nécessaire mais ne suffit pas : il faut qu’elle couvre **la phrase et ses conditions**.
Une référence « Code de la route » ou « ISO 2575 » ne valide pas à elle seule une consigne de conduite.
Le registre [`data/_meta/source_checks.yaml`](../data/_meta/source_checks.yaml) associe les contrôles
externes ciblés des révisions v3 et v4 à leurs notes et à leur portée, avec date de consultation du 21 septembre 2026.
Ce registre ne signifie pas que toute la bibliothèque a été à nouveau vérifiée ligne par ligne.

## Références utilisées pour la révision

| Sujet | Référence primaire | Ce qu’elle établit |
|---|---|---|
| Examen | [Service Public, ETG](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694) | Format et seuil officiels |
| Vitesse | [R413-1 à R413-16](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074228/LEGISCTA000006177128/) | Plafonds selon route, conditions et conducteur |
| Signalisation | [R411-25](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006842087), [R411-28](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006842090) | Portée des feux et des ordres des agents |
| Dépassement | [R414-4 à R414-17](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074228/LEGISCTA000006177131/) | Conditions et exceptions |
| Stationnement | [R417-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045025551) | Arrêt et stationnement à distinguer |
| Secours | [PSC juillet 2026](https://www.securite-civile.interieur.gouv.fr/sites/securitecivile/files/medias/documents/2026-07/References-techniques-nationales-PSC_juillet-2026.pdf) | Conduites adaptées à l’état de la victime |
| Pneumatiques | [Michelin, pression](https://www.michelin.fr/auto/conseils/pression-pneus/gonfler-pneus) | Préconisations du véhicule |
| Voyants | [Notice Renault](https://www.user-manual.renault.com/fr/content/xfk/getting-know-your-vehicle/temoins-lumineux) | Exemple documenté ; ne pas l’universaliser à tous les véhicules |
| Aides | [Comité des experts du CNSR](https://www.securite-routiere.gouv.fr/sites/default/files/2024-06/les_aides_a_la_conduite_%28adas%29.pdf) | Fonctions et limites des systèmes |
| Invalidation | [Service Public F1704](https://www.service-public.gouv.fr/particuliers/vosdroits/F1704) | Conditions de retour au permis |
| Contrôle technique | [Service Public F2878](https://www.service-public.gouv.fr/particuliers/vosdroits/F2878) | Validité selon le résultat |
| Remorque | [Catégories de permis](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074228/LEGISCTA000032465124/) | PTAC, B et B96 |
| Voie réservée | [Ville de Paris](https://www.paris.fr/pages/la-voie-reservee-sur-le-peripherique-entre-en-vigueur-le-3-mars-30106) | Exemple de conditions locales |
| EDPM | [Service Public, mesure locale août 2026](https://www.service-public.gouv.fr/particuliers/actualites/A19037) | Ne pas confondre portée locale et nationale |
| Anki | [Options](https://docs.ankiweb.net/deck-options), [paquets](https://docs.ankiweb.net/importing/packaged-decks.html) | Ordre, enfouissement et import ; vérification aussi dans la bibliothèque installée |

Le Code consolidé archivé dans `docs/research/sources/` reste utile pour rechercher les articles,
mais il s’agit d’une édition secondaire provenant de codes.droit.org. Légifrance est la référence
pour vérifier leur vigueur. Les contrôles textuels complémentaires de la v3 ont notamment porté sur
R234-1, R412-9, R414-3 et les règles de priorité ; ils ne remplacent pas une veille des modifications.

## Approximations et désaccords

Ne pas présenter une convention de manuel comme une consigne secrète connue de l’examen.
Distance d’arrêt « dizaines au carré », temps de réaction moyen, pourcentages de consommation et
statistiques de risque sont des repères contextuels. Leur résultat n’est pas garanti pour une scène.
La règle actuelle prévaut sur les anciennes valeurs d’un QCM. Pour la pression, l’entretien, les
aides et les alertes, suivre les spécifications du véhicule.

Les dossiers v1/v2 (`exam.md`, `legal-facts.md`, `knowledge-facts.md`, `signs-notes.md`, `review-*.md`)
sont conservés comme historique de recherche. Une formulation ancienne qui y subsiste ne doit pas
être réintroduite sans consulter la carte actuelle et le journal de révision. Les fichiers
`docs/01-…`, `02-…`, `03-…` et `06-…` décrivent les décisions actuelles.

## Images et contrôle

Images Commons : attributions et licences par fichier dans `out/ATTRIBUTIONS.md`. Les schémas et
marquages générés sont des supports simplifiés, pas des documents officiels ni des scènes d’examen.
Le solveur contrôle les relations déclarées pour les intersections qu’il sait modéliser ; ni toute
la réponse française ni tous les types de scène ne sont vérifiés par lui.

Les contrôles techniques couvrent données, ordre, présence des médias, rendu Anki et migration ;
les contrôles éditoriaux et les séries nouvelles restent indispensables pour détecter une ambiguïté.
Voir `out/VERIFICATION.md` et `docs/06-audit-v3.md`.

## Veille à poursuivre

Reconsulter les règles à chaque édition, en priorité : ZFE et voies réservées locales, EDPM,
équipements hivernaux, sanctions et permis, recommandations de secours. Les dispositions relatives
aux places avant passages piétons à l’échéance 2027 figurent dans la
[version future de R417-11](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041910488/2027-01-01),
consultée le 21 septembre 2026 : l’exception des emplacements matérialisés y est supprimée.
Recontrôler cette version lors du passage à l’édition 2027.
Mettre à jour `source_checks.yaml` seulement après une nouvelle consultation effective.

## Contrôles supplémentaires v4 — 21 septembre 2026

Les entrées `v4-*` du registre précisent les notes et la portée contrôlées : alcool, vitesses et sanctions,
inter-files, permis/remorque, triangle, ligne continue, adaptation de l’allure, pneumatiques, écoconduite,
accidentalité et signalisation. Les valeurs constructeur restent propres au véhicule ; les tableaux
créés pour exercer la lecture sont fictifs et explicitement signalés.

L’[arrêté de signalisation consolidé](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000829916/)
précise notamment les catégories M4d1/M12 et l’obligation des EDPM sous C113. Ne pas généraliser la
formulation « cyclistes » d’un signal à tous les pictogrammes vélo : le texte de R19 reste distinct.
La consultation de cette source corrige les notes concernées, sans certifier tous les autres signaux.
