# Brief de rédaction v2 — cartes de décision et affirmations

Ce brief s'applique à toute rédaction ou réécriture de cartes dans `data/questions/`, `data/faits/`
et `data/affirmations/`. Il découle de `docs/05-audit-v2.md` (lire d'abord), de `docs/01-analyse-examen.md`
(les formes réelles de l'épreuve) et de `docs/03-conception-des-cartes.md` (principes). La carte des
connaissances `docs/02-carte-des-connaissances.md` reste la liste de contrôle : **on n'ajoute rien qui
ne s'y rattache pas**.

## 1. Ce qu'est une bonne carte pour *réussir* l'ETG

L'épreuve montre une situation (photo/vidéo) et demande de la juger : « Le véhicule A doit céder le
passage : OUI/NON », « Je me replace à droite », « Ce panneau annonce : … », « la descente commence à
environ 150 m : OUI/NON ». Elle ne demande jamais une liste. Une bonne carte reproduit donc ce geste :

- **une situation + une décision** (« Je sors d'un parking, un vélo arrive de ma gauche : qui passe ? »
  → « Le vélo : en sortant d'un lieu non ouvert à la circulation, je cède à tous, piétons compris ») ;
- **une affirmation plausible + VRAI/FAUX + la raison** (« Avec un kit mains-libres intégré, téléphoner
  en conduisant ne présente pas de risque » → FAUX : la conversation détourne l'attention, risque ×3) ;
- **un chiffre à trou** dans une phrase vraie et complète (`{{c1::150 m}}`).

Une carte est bonne si, en la voyant à l'examen sous une autre photo, on répond juste *et vite*.

## 2. Règles (le build les vérifie en partie ; `python -m build.build --check`)

1. **Une carte = une connaissance décidable.** Réponse d'une question ≤ 40 mots et ≤ 4 éléments
   énumérés ; `pourquoi` d'une affirmation ≤ 45 mots ; affirmation ≤ 32 mots. Pas de « citez tous… ».
2. **Le recto porte le contexte nécessaire et suffisant** : agglomération ou non, type de route,
   conditions (nuit, pluie), qui je suis (conducteur, piéton, motard). Jamais plus.
3. **La réponse est spécifique** : jamais un simple « Oui/Non » ; toujours la décision *et* la règle ou
   le mécanisme qui la fonde, en une phrase.
4. **Les affirmations fausses sont plausibles** : ce sont les distracteurs réels de l'épreuve
   (« j'accélère », « je klaxonne », « je maintiens ma vitesse », « je peux » à la place de « je dois »,
   « le motard me voit aussi bien », « le triangle suffit »). Pas de mots-signaux qui trahissent la
   réponse (« toujours », « jamais », « obligatoirement », « uniquement ») dans une affirmation fausse,
   sauf si c'est exactement le mot de l'épreuve (`signal_ok: true`). Équilibre 35-65 % de vrai par fichier.
5. **Vocabulaire de la banque 2023** : adhérence, distance de freinage / d'arrêt, gabarit, angle mort,
   frein moteur, feux de route/croisement, inter-files, chaussettes à neige, assistance au stationnement,
   DAE, usager vulnérable, « je me replace à droite », « je ralentis », « je facilite le passage ».
6. **Convention d'examen en réponse, valeur officielle en explication** quand elles diffèrent ; valeur
   en vigueur en 2026 en réponse, ancienne valeur en explication si la banque (2023) peut l'attendre.
7. **Toute valeur juridique se vérifie** dans `docs/research/sources/cdr.txt` (Code consolidé au
   10/09/2026 ; les articles y sont notés `R. 415-5`, `L. 234-1`) ; toute autre valeur dans
   `docs/research/legal-facts.md` ou `knowledge-facts.md`. On cite la source dans `source`.
   Une valeur marquée « À VÉRIFIER » dans un dossier ne va pas sur une carte.
8. **Pas de doublon** : avant d'écrire, chercher (`grep -ri`) si la connaissance existe déjà en fait à
   trous, question, affirmation ou scénario. Un chiffre vit dans *un* fait à trous ; une décision dans
   *une* question ; on ne répète pas la même connaissance sous deux formes, sauf si la seconde forme
   entraîne un piège distinct (ex. le chiffre « 1 m / 1,50 m » en fait, et l'affirmation « je peux
   chevaucher la ligne continue pour dépasser un cycliste » en affirmation).
9. **Explication = une ligne utile** (le pourquoi, le piège de l'épreuve), pas un paragraphe.
10. **Importance** : `essentiel` (tombe à l'examen, ou fonde une décision fréquente), `utile`
    (peut tomber), `rare` (variante, cas limite). Par défaut `essentiel` ; ne pas gonfler.
11. **Ids stables** : ne pas renommer un id existant qu'on garde. Nouveaux ids : `<lettre>-<slug>` pour
    les questions/faits (`c-`, `l-`, `r-`, `u-`, `d-`, `a-`, `p-`, `m-`, `s-`, `e-`), `aff-<lettre>-<slug>`
    pour les affirmations. Minuscules, chiffres, tirets.
12. **Champs communs** : `theme` (lettre), `sous_theme` (réutiliser ceux du fichier), `importance`
    (facultatif), `source`, `tags` (facultatif : `nouveau::2025` pour une règle récente).

## 3. Réécrire une carte-liste : procédure

Pour chaque carte signalée par le build (« réponse énumérative » / « réponse trop longue ») :

1. Lister les éléments de la réponse. Pour chacun, se demander : *l'épreuve peut-elle me le demander
   sous une photo ?* Si oui → une carte de décision ou une affirmation (une par élément, ou par paire
   d'éléments qui se testent ensemble). Si non → il va dans l'explication d'une carte voisine, ou disparaît.
2. Choisir la forme : décision (« Dans cette situation, je… ») quand il y a une action ; affirmation quand
   l'épreuve juge un énoncé (vulnérabilité, mécanique, risque) ; fait à trous quand c'est un chiffre.
3. Écrire le recto avec la situation concrète, pas le nom de la règle.
4. Supprimer la carte-liste (ou la réduire à ≤ 4 éléments si les éléments forment vraiment *un* tout,
   ex. P·A·S). Ne jamais laisser deux cartes qui demandent la même chose.
5. Noter dans le rapport : id supprimé → ids créés.

**Exemple.** `l-priorite-droite-exceptions` (8 cas) devient :
- Q `l-sortie-parking-priorite` : « Je sors d'un parking (ou d'une voie privée, d'un chemin de terre) sur
  une rue. Un vélo arrive de ma gauche : qui passe ? » → « Le vélo : je quitte un lieu non ouvert à la
  circulation publique, je cède le passage à tous, piétons du trottoir compris (R415-9). »
- AFF `aff-l-chemin-terre` : « Un véhicule qui débouche d'un chemin de terre sur ma droite bénéficie de
  la priorité à droite. » → FAUX — il sort d'un lieu non ouvert à la circulation publique : il cède à tous.
- Q `l-giratoire-entree-priorite` : « J'aborde un carrefour à sens giratoire (AB25 + cédez-le-passage).
  Une voiture circule déjà dans l'anneau, à ma gauche : qui passe ? » → « Elle : dans un giratoire, ceux
  qui sont dans l'anneau sont prioritaires ; la priorité à droite ne s'applique pas à l'entrée. »
- (l'insertion sur autoroute existe déjà : `l-insertion-autoroute-priorite` → ne pas dupliquer)
- (« agent, feu, panneau en disposent autrement » = hiérarchie déjà couverte par `l-signalisation-hierarchie` → rien)

## 4. Schémas YAML

```yaml
# data/questions/NN_theme.yaml
- id: c-indice-ballon
  question: Un ballon roule sur la chaussée depuis le trottoir. Que fais-je ?
  reponse: 'Je freine fort et immédiatement (après un coup d''œil au rétroviseur) : un enfant va probablement le suivre.'
  explication: 'Indice classique de l''épreuve. La bonne réponse est de ralentir / se tenir prêt à s''arrêter, jamais de klaxonner.'
  image: {gen: roue_position, params: {pente: descente}}   # facultatif, générateurs existants seulement
  theme: C
  sous_theme: vigilance
  importance: essentiel
  source: REMC — Anticiper ; securite-routiere.gouv.fr — Enfants

# data/affirmations/NN_theme.yaml
- id: aff-c-mains-libres
  contexte: Je conduis sur route, téléphone connecté au kit mains-libres intégré du véhicule.   # facultatif, ≤ 30 mots
  affirmation: Téléphoner ainsi ne présente pas de risque particulier.
  verdict: faux            # vrai | faux
  pourquoi: 'La conversation elle-même détourne l''attention : risque d''accident ×3, champ de vision rétréci, temps de réaction allongé. Seul le téléphone en main est interdit, mais tout appel distrait.'
  theme: C
  sous_theme: deficiences
  source: securite-routiere.gouv.fr — Téléphone au volant

# data/faits/NN_theme.yaml (inchangé) : texte avec {{c1::…}} (≤ 4 clozes ; même numéro pour une même réponse répétée)
```

Générateurs d'images utilisables (`image: {gen: NOM, params: {...}}`), en copiant les `params` d'une
carte existante qui l'utilise (`grep -rn "gen: NOM" data/`) : `agent`, `feu_tricolore`,
`feu_fleche_composite`, `feu_rouge_clignotant`, `feu_pieton`, `feu_bus`, `signal_affectation`,
`ligne_axiale`, `ligne_rive`, `ligne_jaune`, `fleches`, `transversale`, `passage`, `chevrons`,
`voie_texte`, `voie_insertion`, `bande_cyclable`, `pictogramme_medicament`, `critair`, `roue_position`,
`triangle_distance`, `retroviseur`, `direction_panel`, `road`, `intersection`, `roundabout`. Une image
n'est ajoutée que si elle rend la situation plus claire que le texte ; jamais pour décorer.

## 5. Ce qu'on ne fait pas

- Pas de carte sur l'organisation de l'épreuve, le prix, les délais, l'histoire, les statistiques
  sans valeur de décision (une statistique n'est gardée que si l'épreuve la demande : « 1 accident
  mortel sur 3 sur autoroute est dû à la somnolence »).
- Pas de carte dont la réponse est évidente pour un adulte non conducteur (« Faut-il regarder avant de
  traverser ? »). Chaque carte doit apprendre quelque chose ou fixer un réflexe contre-intuitif.
- Pas de multiplication : si une règle se teste par une seule décision, une seule carte.
- Pas de modification des fichiers d'un autre thème, ni des types de notes, ni du build.

## 6. Livrable d'un agent de rédaction

1. Les fichiers YAML de son thème, valides (`python -m build.build --check` ne signale plus rien pour
   ces fichiers ; les erreurs des autres fichiers ne le concernent pas).
2. Un rapport `docs/research/v2-<theme>.md` : cartes supprimées → cartes créées ; cartes ajoutées pour
   combler un manque de la carte des connaissances (avec la ligne de `02-…` visée) ; doutes restants,
   avec la source consultée.
