# Bilan critique — v6, 21 septembre 2026

## Méthode

Lecture complète des faits, questions, scénarios, comparaisons et d’un large échantillon d’affirmations ;
inventaire des signaux par importance ; analyse automatique des trous (nombre par phrase, longueur du
texte caché) ; relecture des compléments de reconnaissance ; contrôle en ligne des règles les plus
récentes ; rendus réels du paquet importé. Les décisions ci-dessous portent sur ce qui change la
valeur d’apprentissage ; ce qui était solide a été conservé sans réécriture.

## Ce qui a été conservé, et pourquoi

- **La structure** : six tâches de rappel (reconnaître, discriminer, rappeler, décider, juger,
  lire une scène), données YAML séparées des gabarits, objectifs explicites, parcours calculé,
  paquet Socle extrait du même plan, vérifications d’import et de rendu. Rien ne justifiait un
  changement d’approche.
- **La couverture** : les dix thèmes officiels sont traités avec leurs distinctions utiles
  (arrêt/stationnement, cédez/STOP, franchir/chevaucher, prioritaire/facilité de passage,
  pluie/probatoire, EDPM/vélo, AAC/probatoire…). Les vérifications v5 des changements 2024-2026
  sont confirmées par de nouvelles consultations : format inchangé de l’ETG en 2026, délit dès
  50 km/h d’excès (décret du 22 décembre 2025), ZFE maintenues après la censure du Conseil
  constitutionnel du 21 mai 2026, loi n° 2026-798 du 18 août 2026 sur l’emprise manifeste.
  Voir les entrées `v6-*` de [`source_checks.yaml`](../data/_meta/source_checks.yaml).
- **Le rendu** : hiérarchie recto/verso, comparaison A/B, volet de références fermé, modes clair et
  sombre ; aucune modification de gabarit n’était nécessaire.

## Problèmes constatés et décisions

| Problème | Décision |
|---|---|
| **Catalogue de signaux sans valeur d’examen** : 88 signaux « rares » (distributeur de billets, embarcadère, télésiège, charrettes à bras, cartouches, variantes de péage…) et quelques familles de doublons « utiles » (quatre « arrêt au poste », trois campings, trois « marchandises dangereuses ») occupaient les deux dernières semaines du programme. | 101 signaux retirés du deck, chacun avec sa raison et sa couverture dans [`sign_exclusions.yaml`](../data/_meta/sign_exclusions.yaml) ; l’inventaire les conserve. La fin du parcours mêle désormais applications, décisions et signaux utiles. 457 → 356 reconnaissances. |
| **Compléments de reconnaissance encombrés de nomenclature** (« Fin : B33, B31 », « panonceaux M8, M6a, M4 », distances d’implantation, « en position », « sur portique »). | 122 compléments réécrits ou supprimés via `sign_overrides.yaml` : ne restent que les nuances qui changent une décision (5 m avant un passage piéton, chevauchement autorisé pour un cycle, arrêt interdit sur une aire d’arrêt d’urgence…). Médiane du verso : 38 mots. |
| **Trous de phrase et trous de liste** : 38 faits cumulaient plusieurs cibles dans une phrase (72 h / 6 mois / 1 an ; 15 ans / 1 an / 3 000 km) ; quatre demandaient de réciter une formule ou de deviner l’élément caché d’une énumération. | 35 faits réécrits en rappels indépendants ou en cible unique (36 avec le rappel ajouté) ; 7 retirés dont 4 convertis en question ou affirmation (message d’alerte, non-assistance, causes de surconsommation, verglas par température positive). Le build refuse maintenant deux trous dans une phrase (sauf `multi_ok`) et un trou de plus de huit mots (sauf `long_ok`). |
| **Sur-investissement sur la remorque** : onze cartes pour une règle de permis rarement posée. | Trois applications redondantes retirées ; la paire 750/800 kg et le cas de la remorque vide gardent les discriminations utiles. |
| **Maxima pénaux dans les explications** (3 ans, 75 000 €…) alors que les lois de 2025 et 2026 les ont modifiés. | Retirés des explications ; seuls seuils, qualification de délit et points restent enseignés. |
| **Lacunes** : conduite supervisée absente ; ordre de grandeur de la distance d’arrêt retiré en v4 alors que l’épreuve le demande. | Une question sur la conduite supervisée ; deux rappels d’ordre de grandeur (25 m à 50 km/h, 80 m à 90 km/h) explicitement qualifiés « sol sec, conducteur attentif ». |
| Mentions « question officielle 2023 » sur des rectos ; analogies chiffrées non sourcées (« boule de bowling », « plusieurs tonnes »). | Retirées des rectos et des explications concernées. |

Effectif : **1 244 notes / 1 371 cartes → 1 139 notes / 1 224 cartes** ; socle 582 notes / 636 cartes.
À 20 nouvelles cartes par jour, l’introduction complète prend au moins 62 jours au lieu de 69.
Ces nombres décrivent le travail, pas son efficacité.

## Ce que le deck ne fait pas

Il n’entraîne ni la perception sur photo ni la décision sous chronomètre : les séries photo/vidéo et
les examens blancs restent indispensables, dès la première semaine. Il ne couvre pas la banque
confidentielle : la sélection est éditoriale. Il ne remplace pas une formation pratique aux gestes
de secours.

## Vérification

- `python -m build.build --check` : 1 139 notes valides, y compris les nouvelles règles de trous.
- `python -m unittest` : 18 tests réussis, dont un nouveau test des règles de trous.
- `python -m build.verify` : import du Socle, du complet, passage Socle → complet et réimport sans
  doublon ; empreintes dans [VERIFICATION](../out/VERIFICATION.md).
- `python -m build.render_check` : 2 448 faces (toutes les cartes, recto et verso) dans chacune des
  quatre configurations téléphone, 114 faces d’échantillon à 960 px, **0 échec**, 1 142 captures ;
  empreinte du paquet contrôlé dans [RENDU](../out/RENDU.md), identique à celle de
  [VERIFICATION](../out/VERIFICATION.md). Captures relues : STOP, passage piéton C20a, B14,
  comparaisons, rappels de ceinture et de distance d’arrêt, en clair et en sombre.
- Contrôles en ligne du 21 septembre 2026 : vitesse et délit (service-public F19460), ZFE
  (décision n° 2026-903 DC), loi n° 2026-798 (Légifrance, L234-2), format ETG 2026 (Codes Rousseau).

## Incertitudes

- Les sources héritées (`IISR`, `Wikipédia`) des reconnaissances n’ont pas été reconsultées une à
  une ; les corrections v3-v6 ont porté sur les signaux et compléments relus.
- Les peines maximales issues des lois de 2025 et 2026 ne sont plus enseignées ; si une future
  édition les réintroduit, les vérifier article par article sur Légifrance.
- Aucune mesure de rétention ni de réussite à l’ETG n’a été réalisée ; aucun essai sur AnkiMobile ou
  AnkiDroid physiques.
- Les affirmations du thème L ont été lues intégralement ; les autres en vue compacte (contexte,
  affirmation, verdict et début de la justification). Une erreur dans la fin d’une justification
  reste possible.
