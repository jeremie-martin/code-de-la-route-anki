# Conception des cartes — v3

## Ce que l’on optimise

La décision correcte face à une **nouvelle situation**, avec une charge de révision soutenable.
Le nombre de cartes et leur ressemblance textuelle à un QCM ne sont pas des mesures de réussite.
Le socle sélectionne des prérequis et des discriminations utiles sur tous les thèmes ; le paquet
complet conserve les variantes et détails. Le plafond de 600 est un budget éditorial, pas un résultat
scientifique sur le nombre idéal de cartes. La sélection actuelle et ses raisons sont explicites dans
`data/_meta/objectives.yaml` et exportées dans `out/COUVERTURE.md`.

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
cloze, examiner **chaque recto rendu**, pas seulement la note YAML. Ne pas changer les numéros des
clozes publiées sans traiter la migration de leurs cartes.

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

Conserver la séparation YAML / rendu / paquet. Ajouter une compétence dans le manifeste du socle
avec sa justification ; arbitrer si son budget est dépassé. Vérifier données, ordre, rendus et
réimportation avec historique. Préserver aussi les identifiants internes des champs et gabarits dans
`data/_meta/anki_schema.json`, repris du paquet v2 publié. Ne pas confondre reproduction du contenu
avec identité binaire : les paquets contiennent notamment des dates de génération.

Voir `docs/06-audit-v3.md` pour les arbitrages, `docs/07-entrainement.md` pour le retour des séries
réelles. Le test final de la conception reste le transfert à des situations nouvelles, à mesurer en
usage : aucun essai comparatif de réussite des candidats n’a été réalisé pour ce deck.
