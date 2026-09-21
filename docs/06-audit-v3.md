# Audit et réalisation v3 — 21 septembre 2026

## Verdict

L’architecture bibliothèque YAML → médias → paquet Anki mérite d’être conservée. En revanche,
la v2 n’était pas le meilleur parcours que ce dépôt pouvait offrir : elle confondait trop souvent
couverture documentaire, fiabilité d’une explication et utilité d’une révision. **Refonte ciblée du
parcours et des cartes, pas réécriture intégrale ni génération massive.**

Cette version est une amélioration construite et vérifiée, pas la preuve expérimentale d’un optimum.
Elle ne remplace ni les séries sur scènes nouvelles ni une formation aux gestes de secours.

## Constats qui changent le diagnostic

| Constat v2 | Conséquence | Réponse v3 |
|---|---|---|
| 1 032 cartes classées essentielles avant le reste | Long délai avant d’avoir parcouru l’ensemble des bases | Socle explicite de 552 cartes, couvrant 41 objectifs ; bibliothèque complète conservée |
| Une carte courte peut rester fausse, ambiguë ou trop générale | La validation de longueur ne valide pas une connaissance | Corrections contextualisées, exemples et sources de contrôle |
| Table de distances et chiffres variables appris comme des certitudes | Confusion réaction / freinage / arrêt ; mauvais transfert | Applications à données fournies ; approximations nommées et reléguées hors socle |
| Le texte de certains schémas décrit déjà la ligne déterminante | Le dessin peut être ignoré | Rectos réécrits pour exiger sa lecture |
| Vrai/faux parfois résolu par une recette (« toujours ralentir ») | Réussite sur les cartes sans compréhension | Décision + raison ; correction de la proposition fausse ; retrait de recettes |
| Tous les champs et gabarits reçoivent de nouveaux identifiants à chaque build | Anki refuse les mises à jour malgré GUID et modèles stables | Identifiants internes repris du paquet v2 publié ; imports testés avec historique |
| Programme calculé en blocs de notes ; positions réelles avec décalage des clozes | Comptage hebdomadaire différent de l’ordre livré ; collisions de positions | Plan unique au niveau de la carte, positions distinctes, rapport issu de ce même plan |
| Le solveur assimile des pompiers non signalés à un véhicule prioritaire | La forme du véhicule devient abusivement une priorité | Intervention explicitement signalée ; ordres de l’agent évalués avant elle |
| Jaune fixe utilisé dans le schéma d’un jaune clignotant | Modèle et dessin ne portent pas la même situation | État clignotant explicite, dessin annoté et relation vérifiée |

## Ce qui a été construit

Deux paquets complémentaires à identités communes : **483 notes / 552 cartes de socle** ;
**1 179 notes / 1 378 cartes au total**. Dix-neuf nouvelles notes d’application seulement ; les
corrections portent surtout sur l’existant. Le détail des notes modifiées est généré dans
[`research/revision-v3.md`](research/revision-v3.md).

Le socle privilégie : sens et portée des signaux fréquents, priorités, vitesse selon les conditions,
observation et distances, vulnérabilité, risques routiers, installation, entretien utile, retenue des
occupants, règles administratives structurantes, protection et secours, écoconduite. Les exemples
contrastés entraînent les limites d’une règle. La sélection ne prétend pas connaître les probabilités
de la banque confidentielle ; les vingt exemples publics ne suffisent pas à les estimer.

Les variantes moins fréquentes, sanctions détaillées, dates d’équipement, statistiques et repères
chiffrés secondaires sont accessibles en approfondissement. Ils ne conditionnent plus le premier tour
de tous les thèmes. Le plafond de 600 cartes oblige à arbitrer tout nouvel ajout. Le socle n’est pas
une certification de complétude : les lacunes identifiées en séries nouvelles doivent faire évoluer
la sélection.

Les sous-decks et types existants restent stables. `objectif::*` relie les notes à leur intention ;
`parcours::socle` et `parcours::approfondissement` pilotent le parcours. Une comparaison incluse dans
le socle entraîne aussi l’inclusion de ses deux images de référence.

## Corrections représentatives et leur justification

- **Vitesses** : 100 sur une autoroute normalement à 110 pour le probatoire ou sous la pluie ; une
  visibilité inférieure à 50 m ne relève pas une zone 30. Vérification R413-1 à R413-5.
- **Signaux et trajectoires** : un feu ne prime que sur les panneaux réglant la priorité ; voie
  intérieure du giratoire facultative ; changement de voie à céder ; un contrôle d’angle mort dépend
  du côté de la manœuvre. Suppression d’énoncés sous-déterminés.
- **Insertion** : sans créneau sûr, céder peut imposer l’arrêt. La recherche de fluidité ne permet ni
  de forcer ni de continuer sur la bande d’arrêt d’urgence.
- **Équipement** : valeurs de pression constructeur, signification précise des alertes, distinction
  défaut airbag / airbag passager désactivé, limites des aides et automatismes selon la notice.
- **Secours** : distinction malaise non traumatique / traumatisme, respiration normale / gasps,
  adaptation de la protection thermique et alerte sans détour dangereux. Référentiel PSC juillet
  2026 consulté ; aucune « ancienne réponse attendue à l’examen » ne justifie une instruction périmée.
- **Règles locales** : voie réservée et EDPM ne se résument pas à un droit national uniforme.
- **Administration** : conditions de dispense de conduite après invalidation, circulation après
  défaillance critique, absence de transfert automatique des points de l’élève à l’accompagnateur.

Références et périmètre des contrôles : [`04-sources.md`](04-sources.md). Les documents v1/v2
conservent la trace historique ; leurs conclusions de qualité ne sont pas des garanties à reprendre.

## Validation et limites de ce qui est établi

`build.build --check` contrôle toutes les données, références et le budget du socle. Les tests
contrôlent notamment l’ordre des étapes et les prérequis des paires, les rectos, des décisions du
solveur et les liens. `build.verify` importe les vrais paquets dans des collections jetables : nombre
de notes/cartes, médias, rendus, options, ordre, absence de conflit, conservation de la planification
et d’une ligne d’historique. La migration depuis le paquet v2 du dépôt est également testée.
Les résultats du dernier passage sont dans [`out/VERIFICATION.md`](../out/VERIFICATION.md).

L’audit a porté sur la structure complète, les objectifs, les formulations de faits/questions et les
risques de généralisation ; les vérifications externes ont ciblé les points juridiques, techniques et
sanitaires modifiés. **Il ne constitue pas une nouvelle certification ligne par ligne des 1 179 notes**,
ni une inspection manuelle renouvelée des 425 images. Des références héritées restent génériques.
Le solveur contrôle une relation déclarée dans son modèle ; il ne démontre pas que toute la réponse
française est correcte. Les scènes synthétiques ne mesurent pas la lecture d’une photo réelle.

Le prochain critère utile est le retour de l’apprenant : erreurs sur séries inédites classées par
cause, charge de révision et confusions persistantes. Ce retour guide l’enrichissement ; il ne faut
pas ajouter des centaines de notes avant de savoir ce qu’elles corrigeraient.
