# Conception du deck

## Ce que l’on optimise

La bonne décision face à une **situation nouvelle** le jour de l’épreuve, avec une charge de révision qu’une
personne seule peut tenir. Ni le nombre de cartes, ni la ressemblance avec un QCM, ni la couverture d’une
banque de questions confidentielle ne sont des mesures de réussite.

L’ETG : 40 questions, 35 bonnes réponses exigées, une vingtaine de secondes par question, dix thèmes
officiels (L circulation, C conducteur, R route, U autres usagers, D notions diverses, A premiers secours,
P prendre et quitter le véhicule, M mécanique et équipements, S sécurité des passagers et du véhicule,
E environnement). Une question type montre une photo ou une vidéo, impose un point de vue et demande une
décision ou un jugement sur une ou plusieurs propositions.

Réussir demande cinq choses : **savoir** (sens d’un signal, seuil, droit de passage), **discriminer**
(la condition qui change la réponse : agglomération, météo, statut probatoire, catégorie d’usager),
**observer** (trouver ces conditions dans une scène, remarquer ce qui peut être masqué), **décider** (choisir
une action possible et sûre sans inventer un fait absent) et **lire** l’énoncé jusqu’au bout. Anki sert
surtout aux deux premières et stabilise le raisonnement de la quatrième ; les scènes nouvelles (séries photo
et vidéo, examens blancs) entraînent les autres. Le deck est conçu pour être complété par elles, pas pour les
remplacer.

## Les formes de cartes et le travail demandé

| Forme | Ce qu’on rappelle | Ce qui ne suffit pas |
|---|---|---|
| Reconnaissance (image → sens) | Le sens du signal et ce qu’il change pour moi | Son code, une vague catégorie |
| Comparaison A/B | La différence qui change la règle ou la conduite | Deux noms récités |
| Fait à trous | La valeur avec son unité, ou le terme | Deviner grâce au reste de la phrase ou à une carte sœur |
| Question | La décision et l’indice ou la règle qui la décide | Une réponse prudente générique |
| Affirmation vrai/faux | Le verdict et la raison ; la correction si c’est faux | Deviner au style |
| Scénario dessiné | Lire les signes et les trajectoires, puis décider | Lire la solution déjà écrite dans la question |

Une règle mérite plusieurs cartes quand elles entraînent des compétences différentes (reconnaître un marquage,
puis décider avec du trafic ; rappeler un seuil, puis l’appliquer à un cas limite). Elle n’en mérite pas deux
pour reformuler le même oui/non. Un scénario généré vaut une carte quand il matérialise un piège que le texte
ne rend pas (qui est à ma droite, qui est déjà dans l’anneau, qui est en train de me dépasser).

## Principes de rédaction

Ce sont des principes de jugement, pas des règles à faire respecter par un compteur. Le build ne refuse que
les défauts de structure ; les longueurs et les tics de style font l’objet d’avertissements à relire
(`python -m build.build --check`), qui appellent une décision éditoriale, pas un contournement.

1. **Une carte, une décision ou une valeur, et le recto contient tout ce dont la réponse dépend** : type de
   route, météo, véhicule, point de vue, statut du conducteur, visibilité. Si une condition manque, la carte
   est fausse, pas « courte ». Un schéma qui n’est pas à l’échelle ne mesure ni une vitesse ni une distance :
   on les écrit.
2. **La cible de rappel est ce que l’épreuve notera.** Quand le droit et la convention des supports de
   préparation divergent (freinage doublé sur route mouillée, carré des dizaines, PLS), la réponse est celle
   attendue à l’épreuve et l’explication porte la nuance, nommée comme telle. Quand la règle a changé après
   2023, la réponse est la règle actuelle et l’explication le dit. Aucune carte ne prétend connaître la réponse
   d’une banque confidentielle.
3. **Rien de devinable sans savoir.** Ni depuis le recto (un contexte qui énonce la condition du verdict), ni
   depuis une carte sœur (deux trous complémentaires, un exercice à données fixes qui devient du rappel de
   nombre), ni depuis le style : les affirmations vraies et fausses partagent les mêmes tournures
   (« puisque », « tant que », « je peux », « toujours »…), et l’ensemble des oui/non n’est pas majoritairement
   « non ». Une affirmation fausse est plausible pour un adulte.
4. **La réponse est courte et jugeable ; l’explication explique.** Réponse = la décision ou la valeur et la
   raison décisive. L’explication donne le mécanisme, la limite ou la distinction utile ; elle n’ajoute pas
   une seconde liste à réciter, ne commente pas la fabrication du deck et ne s’adresse pas à un rédacteur.
   Une réserve n’y figure que si elle change ce que l’élève peut conclure (« valeur constructeur »,
   « selon visibilité ») ; une réponse qui se limite à « voir la notice » n’est pas une réponse.
5. **Le français est celui d’un bon moniteur** : première personne, phrases naturelles, un seul registre,
   pas de cadres télégraphiques ni d’inversions littéraires, pas de jargon administratif quand un mot courant
   existe.
6. **Prérequis avant application.** Les bases (formes et couleurs des panneaux, vocabulaire, priorité à
   droite, code couleur des voyants) précèdent tout le reste ; un signal est reconnu avant qu’une question
   ne l’utilise ; les scénarios de priorité s’ouvrent après les panneaux de priorité. L’ordre est calculé par
   le build et vérifié à l’import.
7. **Un signal a sa carte s’il porte une décision de conduite ou une discrimination que l’épreuve peut
   demander.** Les variantes d’une famille apprise, les fins et sorties de zone déductibles d’un archétype,
   les pictogrammes et inscriptions transparents restent hors du deck, chacun documenté avec les cartes qui
   couvrent la règle (`data/_meta/sign_exclusions.yaml`). Tout signal retenu a un média.
8. **Ce qui ne décide rien au volant n’est pas une cible de rappel** : maxima de peine, statistiques annuelles,
   délais administratifs qu’on consulte, prix. Les seuils, la qualification (contravention, délit), les points
   et les délais que l’épreuve demande restent.
9. **Toute valeur juridique est vérifiée dans le Code de la route consolidé et datée** ; toute règle récente
   nomme son texte. Une référence générique n’est pas une vérification.
10. **Rien dans le paquet qui ne serve qu’au mainteneur** : les étiquettes de provenance, les journaux de
    révision et les commentaires de conception restent dans le dépôt.

## L’interface d’une carte

Recto : la situation, l’image utile, la question. Pas de sous-thème ni d’indice involontaire.
Verso : la réponse en évidence, puis l’explication ; pour une reconnaissance, le sens, « En pratique »,
un complément s’il change une décision, et un « Piège » s’il y a une confusion classique. Le volet fermé
« Sources » porte la référence et le nom officiel. Les repères de thème sont sur l’écran des sous-decks,
pas sur chaque carte. Tout se lit sur un téléphone en mode clair et sombre ; les longs versos se relisent,
ils ne se compriment pas en réduisant la police.

## Ce que le deck ne fait pas

Il n’entraîne ni la perception sur photo ni la décision sous chronomètre. Il ne couvre pas une banque
confidentielle : la sélection est éditoriale. Il ne remplace pas une formation pratique aux gestes de secours.
Aucune mesure de rétention ni de réussite à l’examen n’a été réalisée avec lui.
