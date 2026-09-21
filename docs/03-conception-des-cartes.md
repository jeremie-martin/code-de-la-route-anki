# Conception des cartes — v5

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
contre-exemple ; elle n’ajoute pas une liste obligatoire à réciter. Les rectos n’affichent plus le
sous-thème, qui pouvait servir d’indice involontaire.

## Clozes, variantes et doublons

Les clozes restent adaptées aux seuils utiles, mais une table visible peut permettre un calcul ou une
déduction au lieu du rappel voulu. Le socle évite les nombreuses tables de statistiques et de sanctions
secondaires ; il combine les seuils importants avec des applications nouvelles. Pour toute nouvelle
cloze, examiner **chaque recto rendu**, pas seulement la note YAML. La v5 est un départ neuf autorisé par l’absence d’import ; une diffusion ultérieure auprès
d’utilisateurs ayant étudié le deck doit traiter toute migration de cibles ou de numéros de cloze.

Deux cartes sur la même règle sont justifiées si elles entraînent des compétences différentes :
reconnaissance d’un marquage puis décision avec trafic, rappel d’un seuil puis application à un cas
limite. Elles ne le sont pas pour reformuler le même oui/non. Les paires proches relevées par
`build.dedup` demandent donc une décision éditoriale, pas une suppression automatique.

Une famille d’affirmations doit éviter une réponse devinable par le style. Le contrôle de balance
35–65 % des fichiers complets est une alerte de rédaction ; on ne rajoute pas de questions inutiles
pour équilibrer un nombre. Ces cartes ne sont pas un simulateur de notation ETG.

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
