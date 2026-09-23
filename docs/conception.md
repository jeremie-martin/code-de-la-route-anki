# Conception du deck

Le deck prépare aux connaissances et aux distinctions utiles à l’ETG du permis B : reconnaître un signal,
identifier les conditions d’une règle et choisir une action justifiée. Ses dix thèmes sont reliés à des
objectifs dans `data/_meta/objectives.yaml`. Ce classement sert à retrouver une difficulté ; il ne prouve
pas la couverture d’une banque d’examen confidentielle.

Anki stabilise le rappel et le raisonnement. Les exercices sur photos et vidéos nouvelles entraînent la
perception, et les examens blancs la décision sous contrainte de temps. Les schémas du deck isolent des
conflits et des trajectoires ; ils ne remplacent pas ces scènes réalistes. Aucune efficacité sur la rétention
ou la réussite à l’examen n’a été mesurée.

## Choisir la forme selon la connaissance

| Forme | Travail demandé |
|---|---|
| Reconnaissance | Sens du signal et conséquence pratique ; pas son code technique |
| Comparaison A/B | Différence visible qui change la règle ou la conduite |
| Fait à trous | Valeur, terme ou décision à apprendre, sans indice donné par la phrase ou une carte sœur |
| Question | Décision justifiée, mécanisme ou calcul avec sa méthode, à partir des conditions du recto |
| Vrai/faux | Verdict justifié et correction de l’idée reçue |
| Scénario dessiné | Lire les positions, signes et trajectoires avant de décider |

Un trou vaut par ce qu’il fait retrouver, que le reste de la phrase ne souffle pas (« l’[agent] qui règle la
circulation » se devine ; « un agent règle un carrefour à feux : je suis [ses gestes] » s’apprend). Quand la
connaissance est un classement, une comparaison ou une décision, une phrase de situation dont le trou est
l’action, ou une autre forme, vaut mieux qu’un mot manquant. L’explication prolonge ce trou (mécanisme,
limite, piège), pas un sujet voisin. Anki n’a pas de QCM natif, et un QCM entraîne la reconnaissance plutôt
que le rappel : le format de l’examen se travaille sur les examens blancs.

Conserver plusieurs cartes d’une règle si elles font travailler des compétences distinctes (règle énoncée,
puis scène à lire). Éviter les reformulations qui demandent exactement le même rappel. Les exemples chiffrés
servent à comprendre une relation ; leur résultat seul ne doit pas devenir la connaissance à apprendre.

## Rédiger et vérifier

- Donner au recto les conditions nécessaires : véhicule, statut du conducteur, route, météo, visibilité,
  point de vue. Une image hors échelle ne permet pas de mesurer une distance ou une vitesse.
- Rendre la réponse jugeable avec ses propres mots. Mettre en explication le mécanisme, la limite ou la
  confusion utile. La longueur dépend du sujet ; aucune limite universelle de mots ou de listes.
- Enseigner la règle actuelle **avec ses conditions** et citer une source primaire qui les couvre. Ne pas
  énoncer une règle plus largement (« toujours », « partout », obligation là où le texte dit « peut ») ni plus
  étroitement que le texte. Un raccourci pédagogique ou un repère chiffré se nomme comme tel. Un exemple
  officiel prouve son propre corrigé, pas toutes les réponses de la banque. Ne pas faire passer une supposée
  convention d’examen, ni une règle d’un autre pays, avant le texte français actuel.
- Montrer les distinctions qui changent l’action : permis probatoire, seuil atteint, accès privé, traumatisme,
  visibilité masquée… Éviter les verdicts devinables par la tournure ou une prudence générique.
- Définir un sigle ou un terme à sa première apparition dans l’ordre d’étude (AAC, PTAC, EDPM…), et introduire
  les prérequis avant leurs applications. Le build entrelace les thèmes, place le socle avant la consolidation,
  espace les cartes sœurs et vérifie les dépendances déclarées ; les dépendances conceptuelles se relisent dans
  `out/PROGRAMME.md` (méthode de calcul avant application chiffrée, contrôle d’un pneu avant décision…).
- Sélectionner les signaux pour leur sens utile ou une confusion réelle. Les variantes déductibles et les
  inscriptions transparentes peuvent rester hors du deck ; les exclusions indiquent la règle qui les couvre.

## Présentation

Recto : situation, image utile, question. Une connaissance visuelle (signal, marquage, placement, pièce du
véhicule, position du corps) a une image. Un dessin qui pose la situation va au recto s’il ne montre pas la
réponse ; s’il la montre (trajectoire, placement, zone), il reste au verso, ou le même dessin passe au recto
sans ce tracé et le verso l’ajoute en place. Un dessin au recto ne doit pas faire d’une carte de règle le
double d’un scénario, ni légender le réglage que la question fait retrouver. À l’inverse, l’énoncé ne nomme
pas ce que l’image doit faire lire (panneau, marquage, geste d’agent, position ou trajectoire d’un usager) :
repérer l’indice fait partie de la compétence. Une image de reconnaissance n’écrit jamais sa réponse.

Le verso prolonge le recto sans rien déplacer ; réponse puis explication s’ajoutent dessous, le cloze se révèle
en place. Les références, noms techniques et codes restent dans le volet « Sources » ; les exemples visuels du
verso portent une légende. Les repères de thème sont sur les sous-decks, sans alourdir chaque carte.

Vérifier les cartes réellement rendues, sur téléphone en clair et sombre : images lisibles, conditions
visibles, réponse sans ambiguïté. Le défilement vertical est acceptable ; réduire la police pour faire tenir
une longue réponse ne résout pas un problème de rédaction. Les mesures automatiques complètent cette lecture ;
la manière de mener une relecture est dans la [méthode](methode.md).
