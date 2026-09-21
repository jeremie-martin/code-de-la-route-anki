# Bilan critique et refonte pédagogique — v4

Révision du 21 septembre 2026, conçue pour un import neuf : le deck n’avait pas encore été utilisé.
La question est la préparation à des situations nouvelles, pas le nombre de cartes produites.

## Verdict

La base était solide : contenu séparé du rendu, six formes de rappel, images identifiées, scénarios,
51 objectifs, parcours progressif, sources et imports testables. La remplacer par un catalogue neuf
ou par des QCM générés en masse aurait perdu ces acquis sans résoudre le problème pédagogique.

En revanche, l’affectation de chaque note à un objectif ne garantissait pas que sa question soit
utile. Certaines cartes faisaient mémoriser un calcul déductible, un chiffre de risque variable ou
une préconisation véhicule transformée en règle générale. Certaines tables donnaient à voir les
réponses sœurs. Des règles étaient décrites sans exercice qui oblige à choisir la bonne condition.
Des explications supposaient enfin que l’apprenant comprenait déjà le mécanisme.

**Décision : conserver l’architecture, refondre ces tâches, compléter les compétences manquantes et
ajouter un niveau d’explication.** Ne pas conserver des cartes ou ordinaux pour protéger un historique
inexistant. Le résultat est un meilleur outil de préparation à essayer réellement, pas une preuve
expérimentale du « meilleur deck possible » ni de l’exhaustivité d’une banque d’examen non publique.

## Ce que l’apprenant doit pouvoir faire

| Travail | Support retenu | Critère de réponse |
|---|---|---|
| Comprendre une relation | Repère de thème + exemple expliqué | Pouvoir expliquer pourquoi la règle intervient |
| Retrouver une règle nécessaire | Rappel court, avec conditions et unité | Retrouver sans déduire depuis une réponse sœur |
| Reconnaître un indice | Signal ou marquage visible | Donner son sens utile, sans réciter son code |
| Distinguer des cas voisins | Comparaison et applications contrastées | Identifier la condition qui change la décision |
| Combiner des informations | Scénario, tableau, question de décision | Lire les données puis appliquer la règle |
| Éviter une mauvaise généralisation | Affirmation justifiée | Verdict et correction de la règle si elle est fausse |
| Percevoir et décider dans une scène nouvelle | Séries externes de photos/vidéos | Réussite sans aide, avec justification après correction |

Il n’y a pas de raison de multiplier tous les formats pour chaque règle. Une reconnaissance et une
application peuvent être complémentaires ; deux reformulations du même oui/non ne le sont pas.
L’affirmation reste utilisable si elle exige une raison : la transformer systématiquement en QCM
faciliterait parfois la reconnaissance d’une réponse sans améliorer sa récupération.

## Changements livrés

### Comprendre avant de rappeler

Onze introductions de thème présentent principe, exemple et transfert. Elles sont réunies dans
[COMPRENDRE](../out/COMPRENDRE.md) et accessibles hors ligne au verso de chaque carte, dans un volet
fermé par défaut. L’apprenant peut remonter de la réponse à son mécanisme sans se voir imposer la
récitation d’un paragraphe. Ces introductions sont volontairement courtes ; elles ne remplacent pas
un cours ni les explications précises des cartes.

### Ne plus apprendre une table par ses indices

Les `rappels` indépendants conservent dans une note les seuils apparentés mais ne montrent, sur une
carte donnée, que sa question. Les conditions natives d’Anki fonctionnent sans JavaScript. Les tests
rendent chaque carte de ces notes avec le moteur Anki et contrôlent l’ordinal effectivement sélectionné.

Des cibles ont été réduites lorsque la multiplication n’ajoutait aucune connaissance : compter cinq
erreurs à partir de 40/35, réciter plusieurs résultats de la même formule, apprendre une date de réforme
au lieu de la règle applicable. Les seuils utiles restent, les applications doivent les mobiliser.

### Appliquer une règle dans des conditions différentes

Douze familles sont explicitées dans [CONCEPTION](../out/CONCEPTION.md). Exemples :

- Même « 50 m », avec ou sans flèches : distance jusqu’au danger ou longueur de la section.
- Même besoin de déposer quelqu’un : stationnement interdit ou arrêt également interdit.
- Même voyant batterie : contact avant démarrage ou apparition en roulant.
- Même tableau de pression : charge habituelle ou pleine charge, essieu avant ou arrière.
- Même somme de PTAC : la branche de la règle change selon que la remorque dépasse 750 kg.
- Même feu rouge avec M12 : EDPM autorisé sous conditions, voiture non autorisée.
- Même ligne continue : l’exception de chevauchement n’est pas étendue à n’importe quel usager lent.

Les images de signalisation sont réutilisées par référence et la reconnaissance précède l’application.
Les tableaux sont clairement fictifs : ils exercent la lecture, sans inventer une pression universelle.
Les cas sont entrelacés dans le parcours ; le manifeste les rassemble pour permettre leur critique.

### Remplacer la fausse précision par la bonne compétence

Dix-sept notes héritées retirées et un doublon proposé puis écarté pendant la refonte sont documentés
avec leur motif et la couverture conservée. Les taux de
mortalité périssables, multiplicateurs de risque décontextualisés, chiffres universels d’airbag,
de batterie ou de changement de rapport n’étaient pas de bonnes cibles de mémorisation.
Les mécanismes, mesures de prévention et interprétation des statistiques restent couverts.

Des remplacements demandent de distinguer part des victimes et exposition au risque, de comparer
des bilans de même périmètre, de consulter l’équipement réellement présent ou une échéance constructeur.
Il ne s’agit pas d’un plafond de cartes : des lacunes concrètes ont aussi été comblées, notamment le
rappel des seuils sanguins d’alcool et le retrait de points pour un dépassement de 40 à 49 km/h.

### Corriger les conditions, pas seulement les nombres

Les corrections portent notamment sur la distance de sécurité et les arrondis, le triangle lorsque
sa pose met en danger, le franchissement/chevauchement, le freinage en sortie d’autoroute, les limites
des feux de croisement, la pression et le refroidissement moteur, les angles morts, l’ABS,
l’inter-files et les conditions de certaines sanctions. Les informations conservées sont formulées
selon leur statut : droit, estimation pédagogique, donnée d’exercice ou préconisation du véhicule.

Le [registre de sources](../data/_meta/source_checks.yaml) donne les vérifications externes ciblées,
leur date et les phrases couvertes. Il évite de transformer une citation générique en certification.
Les dispositions applicables et les consignes propres au véhicule priment sur les raccourcis.

## Comparaison des paquets

| Mesure | Avant cette refonte | v4 |
|---|---:|---:|
| Notes du complet | 1 228 | 1 240 |
| Cartes du complet | 1 427 | 1 393 |
| Notes du socle | 555 | 581 |
| Cartes du socle | 632 | 651 |
| Objectifs | 51 | 51 |
| Repères avec exemple, dans le guide et les cartes | 0 | 11 |

Ces nombres décrivent le changement ; ils n’en prouvent pas la qualité. Le socle reçoit davantage
d’applications, tandis que le complet perd des rappels arithmétiques ou peu défendables. Les listes
exhaustives sont générées dans [COUVERTURE](../out/COUVERTURE.md) et [ROLES](../out/ROLES.md).

## Pourquoi ne pas tout refaire autrement ?

Un seul immense modèle compliquerait la rédaction sans rendre les tâches identiques. Six modèles
suffisent ici ; le nouveau champ explicatif est commun. Des photographies synthétiques ajouteraient
une ambiguïté sur la géométrie, les signaux et les distances ; les schémas explicites conviennent aux
relations contrôlées. Des QCM aléatoires ne rendraient pas le contenu plus représentatif de l’ETG.
Enfin, retirer toute la signalisation moins fréquente sur la seule base d’un classement de rareté
confondrait progression et exclusion. Le parcours complet est conservé et les exclusions restent motivées.

## Comment juger le résultat pendant l’apprentissage

Le deck n’ayant pas été utilisé, nous n’avons pas encore de mesures de difficulté, de rétention ou de
transfert. La prochaine source d’amélioration est l’erreur réelle, avec ce diagnostic :

| Observation | Action |
|---|---|
| Règle oubliée sur Anki et sur série nouvelle | Relire l’exemple, revoir la carte ; scinder si elle demande plusieurs réponses indépendantes |
| Carte réussie mais règle mal appliquée ailleurs | Ajouter ou revoir un cas où la condition change, plutôt qu’un doublon du rappel |
| Indice non vu dans la photo/vidéo | Travailler la recherche visuelle sur d’autres scènes ; une nouvelle carte textuelle ne suffit pas |
| Question ambiguë ou réponse valable seulement sous une condition absente | Corriger le recto ou qualifier la réponse et vérifier sa source |
| Révisions qui s’accumulent | Réduire les nouvelles cartes et traiter les cartes difficiles ; ne pas confondre débit et compétence |

Après plusieurs séries nouvelles, reprendre les erreurs récurrentes par objectif avec le
[carnet d’erreurs](07-entrainement.md). Les résultats sur de nouvelles séries, la nature des erreurs
et la capacité à expliquer les corrections sont plus utiles que le seul pourcentage de réussite Anki.
Terminer le deck n’est ni une condition officielle ni une preuve de préparation ; progresser dans
Anki et dans les exercices externes doit se faire en parallèle.

## Vérification et limites du contrôle

Le build vérifie schéma, références, couverture, médias et contraintes des scénarios calculables.
Les tests vérifient notamment les rappels indépendants, l’absence de champs de réponse au recto et
l’ordre des prérequis. Les imports réels contrôlent les deux paquets, les contenus exportés et le
passage Socle v4 → complet v4 → réimport avec historique conservé. Des rendus à 390 px sont inspectés
pour les nouveaux tableaux, applications et clozes. Voir [VERIFICATION](../out/VERIFICATION.md).

Ces contrôles ne démontrent pas l’exactitude juridique de chaque phrase héritée ni la réussite à
l’examen. Une revue ciblée de sources et une revue éditoriale large ne sont pas une revalidation
externe exhaustive. La v4 ne promet aucune migration d’historique depuis v2/v3 : des cartes ont
volontairement été supprimées et des ordinaux réaffectés pour ce départ neuf.
