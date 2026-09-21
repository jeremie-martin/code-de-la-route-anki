# Conception des cartes — v8

## Ce que l’on optimise

La décision correcte face à une **nouvelle situation**, avec une charge de révision soutenable.
Le nombre de cartes et leur ressemblance textuelle à un QCM ne sont pas des mesures de réussite.
Le paquet complet est le parcours de référence. L’introduction pose des prérequis ; la consolidation
ajoute distinctions, variantes, exceptions et entraînement. Aucun budget numérique ne décide de la
présence d’une note. Chaque note est nommément reliée à un objectif dans `data/_meta/objectives.yaml`.
Cette attribution explique sa place ; elle ne suffit pas à prouver sa qualité.

Examiner son apport : connaissance absente, discrimination utile, application d’une règle, ou variante
qui empêche une mauvaise généralisation. Garder plusieurs cartes quand leurs tâches diffèrent.
Réécrire ou fusionner si elles ne font que répéter une réponse ; ajouter autant que le besoin le demande.
Le même standard vaut dans toutes les étapes, sans réserve de cartes médiocres « facultatives ».
L’inventaire `out/ROLES.md` expose la cible de chaque carte, y compris chaque cloze, pour cette lecture.

## Choisir la forme selon le travail demandé

| Forme | À rappeler | Ce qui ne suffit pas |
|---|---|---|
| Reconnaissance | Sens du signal montré | Son code administratif ou une vague catégorie |
| Confusion | Différence qui change la règle ou le comportement | Deux noms récités sans distinction |
| Fait à trous | Valeur ou terme demandé, avec son unité | Deviner grâce au reste de la phrase |
| Question | Décision et indice/règle décisif | Réponse prudente générique sans lire la scène |
| Affirmation | Verdict + raison ; correction si faux | Deviner oui/non ou repérer un mot « suspect » |
| Scénario | Lire signes/trajectoires puis décider | Lire la solution déjà donnée dans la question |

Le recto doit porter les conditions nécessaires : type de route, météo, véhicule, point de vue,
signalisation et visibilité lorsqu’elles décident de la réponse. Une image ne suffit pas à mesurer
la vitesse ou une distance si le schéma n’est pas à l’échelle : les préciser dans le texte.
Ne pas inventer une priorité manquante pour obtenir une réponse tranchée.

La réponse principale est courte et évaluable. L’explication donne la limite, le mécanisme ou le
contre-exemple ; elle n’ajoute pas une liste obligatoire à réciter. Depuis la v7, une réponse de
question tient en 30 mots au plus (cible 10-22) : **la décision ou la valeur, puis la raison décisive**.
Une deuxième condition, une conséquence ou une sanction vont dans l’explication : elles restent lues au
verso sans devenir un critère pour se dire « Bon ». Le build refuse une réponse plus longue sans `long_ok`. Les rectos n’affichent plus le
sous-thème, qui pouvait servir d’indice involontaire.

## Clozes, variantes et doublons

Les clozes restent adaptées aux seuils utiles, mais une table visible peut permettre un calcul ou une
déduction au lieu du rappel voulu. Le socle évite les nombreuses tables de statistiques et de sanctions
secondaires ; il combine les seuils importants avec des applications nouvelles. Pour toute nouvelle
cloze, examiner **chaque recto rendu**, pas seulement la note YAML. La v5 est un départ neuf autorisé par l’absence d’import ; une diffusion ultérieure auprès
d’utilisateurs ayant étudié le deck doit traiter toute migration de cibles ou de numéros de cloze.

Règles de trous (v6, contrôlées par le build) : une phrase `texte` ne porte qu’un trou ; plusieurs cibles
vont dans `rappels` ; un trou fait au plus huit mots. Une formule à réciter devient une question ; une
énumération à trous (« quatre causes… ») devient une question qui demande la liste entière, car le
trou d’une liste se devine par élimination. `multi_ok` et `long_ok` documentent les rares exceptions.

Deux cartes sur la même règle sont justifiées si elles entraînent des compétences différentes :
reconnaissance d’un marquage puis décision avec trafic, rappel d’un seuil puis application à un cas
limite. Elles ne le sont pas pour reformuler le même oui/non. Les paires proches relevées par
`build.dedup` demandent donc une décision éditoriale, pas une suppression automatique.

Une famille d’affirmations doit éviter une réponse devinable par le style. Le contrôle de balance
35–65 % des fichiers complets est une alerte de rédaction ; on ne rajoute pas de questions inutiles
pour équilibrer un nombre. Ces cartes ne sont pas un simulateur de notation ETG.

## Signaux : ce qui mérite une carte

Un signal reçoit une carte de reconnaissance s’il porte une décision de conduite (céder, s’arrêter,
ne pas dépasser, choisir une voie) ou une discrimination que l’épreuve peut demander (B6a1/B6d,
B15/C18, J1/J3, B7a/B7b). Les variantes d’une famille déjà apprise (catégories exotiques de M4, campings,
« arrêt au poste », rétrécissements temporaires latéraux), les services et catégories au pictogramme
transparent (distributeur de billets, embarcadère, toilettes, bus, camion) et les cartouches sont exclus
et documentés avec leur couverture. Depuis la v8, le même critère s’applique aux **sorties de zone** et
aux **fins de prescription** qui se déduisent du signal de début par une convention apprise sur un
archétype : B51 pour « même panneau barré de gris », B31/B33/B34/B40 pour « rond barré ». Un signal
est déductible quand un candidat qui connaît le signal de début et la convention produit la bonne réponse
sans l’avoir jamais vu ; sinon il reste.

Un scénario généré vaut une carte quand il matérialise un piège que le texte seul ne rend pas
(qui est à ma droite, qui est déjà dans l’anneau, qui est en train de me dépasser). Les réponses des
intersections sont vérifiées par le solveur ; giratoires et scénarios de dépassement sont relus à la main. Le complément d’une reconnaissance
ne contient pas la nomenclature (codes de fin, panonceaux possibles, distances d’implantation) :
il donne la seule nuance qui change une décision, ou rien.

## Sources et précision

Une règle actuelle passe avant une prétendue « réponse attendue par une banque ancienne ». Une
approximation doit se présenter comme telle ; une notice constructeur ou une règle locale doit être
nommée quand elle décide. Pas de garantie du type « orange = continuer », « jamais s’arrêter pour
s’insérer », « tous les tunnels = 150 m ». Ne pas présenter un échantillon de vingt exemples publics
comme une mesure de fréquence de la banque confidentielle.

Les limites automatiques de longueur rendent les cartes lisibles, mais ne prouvent ni atomicité ni
exactitude. Le solveur de priorité vérifie des relations spécifiées dans son domaine restreint ; il
ne lit pas la réponse française et ne valide pas les piétons, tous les feux ou tous les giratoires.

## Maintenance et vérification

Conserver la séparation YAML / rendu / paquet. Ajouter une compétence dans le manifeste de tout le deck
avec sa justification, puis rattacher explicitement chaque note à sa place dans le parcours. Vérifier données, ordre, rendus et
réimportation dans la même édition. Exécuter aussi `python -m build.render_check` avec les dépendances
QA et Chrome : les contrôles portent sur un import du paquet, pas sur une ancienne collection de build. Préserver aussi les identifiants internes des champs et gabarits dans
`data/_meta/anki_schema.json`, repris du paquet v2 publié. Ne pas confondre reproduction du contenu
avec identité binaire : les paquets contiennent notamment des dates de génération.

Voir `docs/08-integration-complete.md` pour les arbitrages, `docs/07-entrainement.md` pour le retour des séries
réelles. Le test final de la conception reste le transfert à des situations nouvelles, à mesurer en
usage : aucun essai comparatif de réussite des candidats n’a été réalisé pour ce deck.

## Rappels indépendants et explications (v4)

Un `fait` accepte soit `texte`, soit `rappels`, liste de phrases autonomes. Exemple :

```yaml
rappels:
  - "Dans le cas A, le seuil est {{c1::valeur A}}."
  - "Dans le cas B, le seuil est {{c2::valeur B}}."
```

Chaque entrée ne contient qu’un ordinal, distinct des autres, contigu de 1 à 4. Le build compile ces
phrases dans `Texte` ; les conditions cloze natives d’Anki ne montrent que la phrase de la carte active,
au recto comme au verso. L’enfouissement des cartes sœurs reste utile. Garder `texte` quand plusieurs
trous forment volontairement une même relation ; contrôler l’absence d’indice qui court-circuite le rappel.

Les onze repères de `lessons.yaml` fournissent principe, exemple expliqué et piste de transfert.
Le volet au verso est fermé par défaut : il ne surcharge pas le rappel et ne donne pas la réponse au
recto. Le guide `COMPRENDRE.md` permet de lire ces introductions avant de commencer un thème.
Ces repères accompagnent les cartes ; ce ne sont ni un cours intégral ni onze nouvelles listes à apprendre.

Une question avec `image_ref` réutilise la représentation canonique d’un signal et attend son
introduction dans le parcours. Une image doit être nécessaire à la décision : ne pas nommer le signal
ou transcrire sa valeur dans l’énoncé. Un tableau fictif porte explicitement sa nature et son périmètre.
Les familles de `contrasts.yaml` rendent vérifiable la condition qui change entre les cas, sans imposer
leur présentation consécutive. Les retraits sont motivés dans `retirements.yaml` et gardent une couverture.


## Interface quotidienne : chaque élément doit justifier sa place

Le [bilan d’interface](11-interface-quotidienne.md) documente le diagnostic, les appuis externes,
les arbitrages et les vérifications. Ces règles s’appliquent à tous les types, avec des tâches différentes :

| Niveau | Contenu | Critère |
|---|---|---|
| Recto | Question, contexte nécessaire, image utile | Peut-on répondre sans deviner une condition absente ? |
| Verso principal | Réponse attendue, correction et explication utile | Peut-on juger sa réponse et comprendre son erreur sans ouvrir de volet ? |
| Référence | Source, nom/code officiel, repère de thème | Sert-il surtout à vérifier, situer ou réapprendre ? |
| Guide de démarrage | Méthode, notation, rythme | Est-ce une instruction identique à chaque révision ? |

Ne pas transformer cette table en automatisme fondé sur le nom d’un champ. `Complement` peut
porter une condition essentielle ; `Explication` peut contenir une remarque d’auteur inutile.
Relire le sens avant de déplacer ou supprimer. Une réserve est utile si elle change ce que l’élève
peut conclure : « valeur constructeur », « selon visibilité », « maxima encourus » ne sont pas du bruit.
Une seconde mention « données fictives » après un tableau déjà étiqueté l’est généralement.

Le contexte répété au verso facilite la comparaison avec sa réponse ; sa typographie est plus discrète.
Une comparaison A/B se corrige avec les repères **A et B**, pas en obligeant à apprendre leurs codes.
Une raison décisive reste visible. Ne jamais masquer les exceptions qui rendent la réponse exacte
pour faire tenir la carte dans un écran. Le défilement est permis, mais les longs versos sont à examiner.
Les noms officiels des signaux restent consultables, sans constituer une deuxième cible de récitation.

Préférer une explication concrète (« seul le freinage double ici ») à un commentaire sur la fabrication
du deck ou sur ce qu’il ne prétend pas garantir. Retirer une phrase déjà démontrée par la réponse si
elle n’ajoute ni mécanisme, ni limite, ni distinction. Conserver une procédure cohérente lorsqu’une
séparation ferait perdre le sens de l’action. Ne pas raccourcir en réduisant la police ou en rognant.

Pour chaque changement, vérifier une question courte, une longue, une avec image, une sans image,
une correction fausse, une comparaison et chaque ordinal d’une cloze modifiée. Examiner clair et sombre
à 430 × 932, puis l’espace réduit de 430 × 740 et la contrainte à 320 px. Ouvrir le volet, vérifier ses
liens et le refermer. Les captures Chromium évaluent l’interface web ; elles ne prouvent pas le rendu
WebKit, les gestes AnkiMobile ou l’efficacité d’apprentissage sur plusieurs mois.
