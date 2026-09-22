# Comparaison avec le livre 2025–2026

22 septembre 2026 — *Le Code de la route 2025–2026 pour les Nuls, poche*, Permisecole.com,
édition numérique fournie localement (métadonnées : 23 janvier 2025).

Le sommaire a été rapproché des objectifs du deck, puis les passages susceptibles d’apporter une
distinction absente ou contradictoire ont été lus. Il s’agit d’une comparaison ciblée, pas d’une
certification de chaque phrase, illustration ou corrigé du livre. Les consultations primaires et
leurs limites sont consignées dans `data/_meta/source_checks.yaml`.

## Changements retenus

| Passage | Décision et intérêt |
|---|---|
| Ch. 7, remorque | Deux questions : plafonds selon le PTRA et application à une petite remorque vide. Le deck enseignait déjà les permis et les masses, mais pas cette conséquence sur la vitesse. R413-8 vérifié sur Légifrance ; préciser le caractère prioritaire de la route à chaussées séparées. |
| Ch. 13, freins mouillés | Une question après lavage : vérifier le freinage sans gêner le trafic, comprendre le retard possible, ne pas banaliser une anomalie persistante. Notice Volvo consultée via son texte indexé. |
| Ch. 10, siège enfant | Recentrer `s-groupes-sieges` sur l’adaptation à l’enfant, la compatibilité et la notice. Retirer la liste des anciens groupes du feedback ; distinguer homologation R129 et fixation Isofix. |

## Divergences et éléments conservés

- **Contrôle technique, ch. 9 :** la ligne R du livre répète « majeure ». La fiche
  [Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F2878) distingue bien
  majeure/S (deux mois) et critique/R (jour du contrôle). Les cartes existantes sont conservées.
- **Sièges, ch. 10 :** l’absence d’Isofix n’est pas une condition générale autorisant l’usage d’un
  ancien siège R44. Des R129 se fixent par ceinture, comme le précise
  [l’AWSR](https://www.awsr.be/securite-routiere/sieges-auto/). La notice du modèle décide.
- **Secours, ch. 4 :** ne pas remplacer la distinction actuelle malaise/traumatisme par une PLS
  systématique. Le deck s’appuie déjà sur les références PSC de juillet 2026, dont la consultation
  est documentée dans le registre.
- **Déjà enseigné :** risques des angles morts, visibilité masquée, distance d’arrêt et limites des
  estimations, montagne, passagers et chargement, aides à la conduite, niches et issues de tunnel,
  écoconduite. Une nouvelle formulation de ces thèmes n’est pas en elle-même une lacune à combler.
- **Pas de rappel ajouté** pour les statistiques de risque sans contexte, les chiffres universels
  de climatisation ou les détails mécaniques sans conséquence sur une décision du conducteur.

## Images et limites

Les deux schémas examinés du ch. 21 montrent utilement des trajectoires de tourne-à-gauche différentes,
mais sont de petits bitmaps et le premier superpose plusieurs positions de voitures. Ils servent
à expliquer une manœuvre, moins à tester une décision sans fournir sa réponse. Aucun texte ou média
du livre n’est incorporé au paquet ; les ajouts sont rédigés pour le deck à partir des sources vérifiées.

La géométrie des croisements simultanés à gauche reste une limite des schémas actuels : le solveur
abstrait les conflits, il n’enseigne pas toutes les trajectoires possibles selon l’aménagement.
Aucun scénario du paquet ne met actuellement en scène deux véhicules opposés tournant tous deux à gauche.
Cette comparaison ne démontre ni la couverture exhaustive de l’ETG ni un gain mesuré de rétention.
Les scènes photo/vidéo nouvelles restent nécessaires pour entraîner la perception.

## Seconde lecture ciblée — 22 septembre 2026

Relecture des passages sur le placement, les changements de direction, les croisements, les distances,
le fonctionnement du véhicule et les piétons (ch. 14, 19–21, 24 et 37), avec inspection du schéma de
croisement à l’indonésienne. Pas de nouveau média nécessaire pour les corrections retenues :

- **Voyants :** le livre rappelle les alertes en roulage, mais la comparaison des cartes du deck entre elles
  révèle une consigne erronée d’extinction avant démarrage. Cinq notes sont harmonisées avec une notice Renault :
  contact et roulage distincts, autotest de l’airbag, pression d’huile distincte du niveau, procédure de
  surchauffe dépendant du véhicule.
- **Piétons :** trois notes sont précisées à partir de R412-37 à R412-39 et R415-11. Le rappel du seuil
  reste dans le fait à trous ; le vrai/faux teste maintenant son transfert au carrefour, sans carte supplémentaire.
- **Distances :** ne pas reprendre les coefficients du livre comme des constantes physiques universelles.
  Le deck distingue déjà estimation pédagogique, réaction et freinage ; aucune nouvelle carte justifiée ici.

Cette passe porte sur les points ci-dessus et leur cohérence dans le deck, pas sur une nouvelle vérification
juridique de ses 1 052 notes. Le livre reste un document local de comparaison, exclu de Git et du paquet.
