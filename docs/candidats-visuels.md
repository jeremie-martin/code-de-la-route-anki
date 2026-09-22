# Candidats à une illustration

État au 22 septembre 2026, après `d6520d6`. Carte de discussion éditoriale, pas liste d’images à produire.
Les bénéfices indiqués sont des hypothèses de conception, sans mesure d’efficacité. Un candidat peut être
abandonné si son prototype n’améliore pas la compréhension ou le rappel. Aucun quota d’illustrations.

## Périmètre et lecture

Repérage dans les 1 051 notes : questions, affirmations et rappels des faits ; inventaire des reconnaissances,
comparaisons et scénarios pour chercher les recouvrements. Relecture détaillée des candidats principaux,
de leurs réponses et des réserves du registre des sources. Inspection du recto de `scn-dep-passage-pieton`
et de `scn-giratoire-cedez` à 390 px. Ce n’est ni une nouvelle validation juridique ni une inspection de
chaque image du deck. Les idées ci-dessous demandent encore une vérification de leurs sources et un essai.

Le deck possède déjà 284 notes de reconnaissance illustrées, 48 comparaisons visuelles et 56 scénarios ;
22 questions et un fait ont aussi une image principale. L’absence d’image n’est donc pas un défaut en soi.
Les notes non retenues restent inchangées ; leur omission ne signifie pas qu’elles ont été définitivement
écartées. Les identifiants ci-dessous désignent des **notes**, parfois porteuses de plusieurs cartes cloze.

Sources à ouvrir avec l’identifiant (recherche Anki : `Id:identifiant`) :
[questions](../data/questions/), [affirmations](../data/affirmations/), [faits](../data/faits/),
[scénarios](../data/scenarios/), [reconnaissances](../data/reconnaissance/),
[objectifs et recouvrements](../data/_meta/objectives.yaml), [consultations antérieures](../data/_meta/source_checks.yaml).

**Recto** : l’image fournit les données nécessaires à la décision ; le texte conserve les conditions
invisibles. **Verso** : l’image explique la réponse après le rappel. Un dessin de bonne conduite au recto
peut supprimer précisément l’effort qu’on veut entraîner. Les flèches d’intention sont des données ; une
trajectoire correcte tracée d’avance est souvent une réponse. Les couleurs ne doivent pas donner le verdict.

## Candidats les plus solides à prototyper

L’ordre commence par les voisins du chantier, puis élargit aux distinctions spatiales et à la lecture technique.
Chaque ligne décrit une piste, pas une autorisation de modifier toutes les notes citées.

| Note cible | Gain attendu et dessin proposé | Conditions de réussite, recouvrements |
|---|---|---|
| `r-chantier-fleche-lumineuse` | **Recto.** Lire le sens du rabattement dans une situation réelle de voies : véhicule porteur, voie neutralisée, flèche lumineuse et voiture en approche. Demander de quel côté se rabattre et comment préparer la manœuvre. | Premier essai proposé. Choisir un dispositif précis, vérifier sa forme et son implantation dans l’IISR 8e partie. Ne pas mélanger FLR, panneau KD10 et signal au-dessus d’une voie. Pas de trajectoire de réponse ; une voie voisine dessinée libre ne garantit pas un créneau sûr. `kd10` entraîne déjà la reconnaissance du panneau. |
| `u-corridor-securite` | **Recto.** Distinguer BAU, voie de circulation et espace de protection : dépanneuse sur la BAU, voiture en approche, autre véhicule dans la voie voisine. Demander comment adapter la conduite. | Réutiliser route et véhicules du chantier. Vérifier R412-11-1 et R413-17 pour le cas exact. Le dessin doit permettre de discuter la possibilité du déport, sans faire croire qu’un changement de voie est inconditionnel. Ne pas confondre avec un couloir central entre files. |
| `u-cycliste-tourner-droite` | **Recto.** Comprendre le croisement des trajectoires : voiture avant le virage, piste longeant sa droite, cycliste arrivant derrière, intention de tourner indiquée. | Lire R415-13/R415-14 et dessiner un aménagement sans signal contradictoire. Ne pas montrer la voiture déjà en travers de la piste. Les scénarios de priorité existants ne montrent pas ce conflit longitudinal précis. |
| `l-entrecroisement` | **Recto.** Rendre compréhensible cette géométrie peu évidente en mots : entrée prolongée jusqu’à une sortie, deux véhicules et leurs destinations. Demander qui change de voie dans le cas montré. | La question générale devrait devenir un cas déterminé, sans attribuer une priorité universelle à un véhicule coloré. Vérifier R421-3/R412-10. `marq-voie-insertion` montre un marquage et une insertion simple, pas deux intentions qui se croisent. |
| `l-giratoire-sortie-impossible` | **Recto.** Voir pourquoi la sortie coupe la voie du cycliste : anneau à deux voies, voiture à l’intérieur, vélo à l’extérieur et sortie visée. | Le giratoire existant de `scn-giratoire-cedez` teste l’entrée, pas le changement de voie. Vérifier géométrie, sens et absence de flèches imposant une voie. Conserver la portée de `l-giratoire-placement` : une illustration ne doit pas transformer une voie facultative en obligation. |
| `u-pl-tourne-droite` | **Recto**, puis éventuellement explication au **verso**. Montrer le déport initial à gauche avec clignotant droit ; expliquer ensuite le passage des roues arrière à l’intérieur du virage. | Le déplacement initial ne prouve pas une trajectoire future certaine. Le balayage dessiné doit correspondre au véhicule choisi, pas à une enveloppe universelle. Relire avec `u-pl-angles-morts`, qui teste la visibilité et non le gabarit. |
| `scn-dep-passage-pieton` ; relire `c-occlusion-pieton` | **Amélioration d’un visuel existant.** Montrer ce que le véhicule arrêté empêche de voir depuis le conducteur. Le plan actuel situe les véhicules, mais ne représente pas le masque de visibilité. | Travailler d’abord le scénario existant ; décider ensuite si la question textuelle apporte un rappel distinct. Ne pas dessiner un piéton visible au recto : cela remplace l’incertitude par un danger certain. Un plan omniscient demande une zone explicitement non visible, ou une vue depuis le conducteur. |
| `aff-l-stop-avancer` ; relire `l-stop-arret` | **Recto.** Séparer l’endroit de l’arrêt obligatoire de celui où la vue se dégage : ligne, voiture déjà arrêtée et obstacle latéral masquant la rue. | Le texte doit dire que l’arrêt a déjà eu lieu, fait impossible à déduire d’une image fixe. Ne pas placer la voiture au-delà de la ligne dès le premier arrêt ni promettre qu’on peut toujours avancer. Les scénarios STOP actuels testent surtout les priorités. |
| `l-c107-route-simple`, `l-c107-route-separee` | **Remplacer les images actuelles du panneau seul** par deux scènes comparables : même C107, chaussée unique ou deux chaussées avec terre-plein. | Faire lire la différence qui détermine la réponse. Garder dans le texte météo, permis et absence de limite plus basse. Même cadrage et même style, sans chiffre de vitesse visible ni couleur donnant la réponse. Relire les conditions légales de chaque configuration. |
| `l-vocab-chaussee-voie` | **Verso.** Un même plan avec accolades et légendes montre qu’une chaussée contient plusieurs voies, et situe l’accotement. | Réutilisable comme vocabulaire explicatif, sans ajouter une nouvelle carte. Au recto, des légendes donneraient la réponse. Ne pas confondre accotement, trottoir et BAU ; contrôler les définitions avant le dessin. |
| `m-pneus-usure-1-6` | **Verso.** Coupe simple d’une rainure, témoin d’usure et surface de roulement pour rendre « atteindre le témoin » concret. | Vérifier sur une documentation technique primaire ; ne pas faire du témoin un diagnostic de tous les défauts. La cote du minimum reste au verso. Une photo de détail peut être préférable au SVG si celui-ci rend le témoin méconnaissable. |
| `m-pression-etiquette` | **Recto.** Remplacer les deux valeurs récitées dans la question par une petite étiquette lisible, avec charge et pressions ; demander de sélectionner la ligne adaptée. | Se fonder sur une notice ou étiquette réelle, identifier l’exemple et conserver pneus froids, dimensions et essieux utiles. Ne pas présenter 2,2/2,6 bar comme norme générale ni inventer une étiquette constructeur. L’image doit faire lire une information, pas répéter la phrase. |

## Pistes conditionnelles à discuter

Ces idées peuvent être utiles, mais le coût, la redondance ou le risque de fuite de réponse est plus important.

| Note(s) | Proposition et raison | Réserve qui décide |
|---|---|---|
| `c-angle-mort-definition`, `u-pl-angles-morts` | **Verso**, vues schématiques des zones masquées ; pour le camion, situer le vélo par rapport à la cabine. | Aucune zone universelle ni promesse « hors zone colorée = vu ». Vérifier le véhicule et distinguer champ optique, regard du conducteur et détection. Deux schémas ne sont utiles que s’ils enseignent des limites différentes. |
| `l-ligne-continue-sanction` | **Verso**, vues comparables des roues et de la ligne pour expliquer chevauchement/franchissement. | Deux rappels cloze dans la même note : une planche nommée au recto révélerait les réponses. Relire aussi `scn-dep-cycliste-ligne-continue` et `l-cycliste-ligne-espace` ; ne pas dessiner des sanctions ou exceptions comme propriétés de la seule géométrie. |
| `p-pente-roues` | **Verso**, montée et descente, bordure à droite, roues et mouvement possible jusqu’à la bordure. | Un ancien dessin a été retiré pour pente ambiguë et roues déjà braquées au recto. Ne rouvrir la piste qu’avec ces défauts résolus et une notice constructeur. Une flèche de pente doit être distinguée du sens de circulation. |
| `p-ceinture-position`, `s-femme-enceinte`, `p-appuie-tete` | **Verso**, détail anatomique sobre montrant les contacts et alignements difficiles à exprimer seulement en mots. | Préférer une illustration technique vérifiable aux silhouettes approximatives. La carte sur la grossesse demande actuellement une obligation : un visuel doit aider son explication sans détourner ce rappel. Ne pas ajouter les trois par principe. |
| `s-siege-dos-route` | **Verso**, coupe de profil pour expliquer l’interaction entre airbag frontal et siège dos à la route. | Vérifier notice et orientation. Le recto ne doit pas montrer d’emblée un voyant OFF qui fournit la condition demandée. Ce n’est pas un guide de montage du siège. |
| `c-double-vitesse-arret` | **Verso**, deux barres à la même échelle, chacune séparant réaction et freinage. | Le résultat chiffré et les proportions restent cachés jusqu’au rappel. Garder les hypothèses du modèle ; pas une distance garantie sur route. Un tableau peut suffire, sans produire de média. |
| `c-intervalle-repere` | Deux instants autour d’un même repère fixe pour expliquer une mesure en secondes. | Au verso si la question reste inchangée. Au recto seulement si la lecture des instants remplace réellement la description. Deux voitures espacées sur une image fixe ne donnent pas leur intervalle temporel. |
| `r-vent-lateral` | **Verso**, passage d’une zone abritée par un camion à une zone exposée au vent. | Expliquer le changement d’exposition, sans inventer un vecteur de déport exact ni une trajectoire corrective. Dessin fixe limité pour un phénomène dynamique. |
| `r-pn-engagement` | **Recto**, rails et file arrêtée après la traversée, espace de dégagement manifestement insuffisant. | Bon exercice spatial possible, mais la phrase actuelle est déjà claire. Relire `r-tram-traversee-degager` et `l-intersection-encombree` ; retenir une application utile plutôt que trois scènes identiques de blocage. |
| `r-pn-barrieres-ouverture` | **Recto**, barrière en cours d’ouverture et feu encore actif pour lire deux indications ensemble. | Une image fixe ne prouve ni le mouvement ni le clignotement. Le texte doit conserver ces faits ; juger alors ce que l’image apporte encore. |
| `u-interfiles`, `aff-u-interfiles-files-gauche` | Plan à trois voies montrant les deux files les plus à gauche. | Utile surtout pour la localisation, pas les seuils de vitesse. Sur l’affirmation actuelle, dessiner la moto au bon endroit confirme déjà la réponse : préférer un verso ou repenser la question. Vérifier les conditions actuelles de l’inter-files. |
| `l-portee-prescription`, `aff-l-zone-30-portee` | **Verso**, deux parcours comparables avec intersection et panneaux pour expliquer la portée. | Légendes et zones colorées doivent attendre la réponse. Ne pas généraliser la règle d’un panneau isolé à toutes les prescriptions. Vérifier IISR et cas d’agglomération. |
| `l-panonceau-portee` | **Recto**, assemblage réglementaire concret de panneaux et panonceau pour demander à quoi il s’applique. | La note actuelle énonce un principe général. Choisir un cas autorisé par l’IISR, sans inventer un empilement ; comparer avec les 29 reconnaissances de panonceaux avant d’ajouter un rappel. |
| `m-carburants-etiquettes`, `m-galette-chiffres` | Formes des étiquettes carburant ; détail du marquage 3PMSF sur un pneu. | La première piste pourrait faire lire les formes au recto. La seconde doit isoler le rappel concerné : la note contient aussi un rappel sur les pneus cloutés. Ne pas coller une image commune sans rapport à toutes ses cartes. Vérifier les symboles officiels et leur licence. |
| `etg-pictogramme-point-de-vue`, `etg-halo-jaune` | Extrait officiel autorisé illustrant le repère d’interface dont parle la note. | Utile si le repère est difficile à imaginer ; vérifier version, provenance et droits. Une maquette inventée pourrait enseigner une fausse convention d’examen. Pas une priorité de dessin SVG. |
| `r-montagne-croisement-difficile`, `r-montagne-marche-arriere` | **Verso**, pente et emplacement de croisement pour distinguer l’arrêt initial d’une éventuelle marche arrière. | Une vue en plan représente mal la pente. Vérifier d’abord les conditions et exceptions des deux réponses ; ne pas déduire une règle unique du véhicule dessiné en haut. |

## Ajouts peu justifiés dans l’état actuel

| Notes ou famille | Décision et raison |
|---|---|
| `r-chantier-approche` | Déjà intégré. Conserver le dessin source, la question ciblée et la limite hors échelle ; pas de nouvelle variante décorative. |
| `kd10`, `ak5`, `k5a` | Images de reconnaissance déjà présentes. Une scène supplémentaire doit entraîner une décision distincte, comme sur l’approche du chantier. |
| `aff-r-chantier-sans-ouvriers` | Garder le texte : la présence de la prescription, pas la capacité à repérer un ouvrier, fait l’objet du rappel. |
| `l-retrecissement-croisement`, `l-priorite-droite-defaut`, `r-tram-priorite` | Les applications visuelles existent : `scn-pos-croisement-obstacle`, `scn-pd-droite-tout-droit`, `scn-tram-gauche`. Préserver la complémentarité règle/application. |
| `p-retro-interieur`, `p-retro-exterieurs` | Ne pas rétablir les anciens cadrages au recto : ils donnaient la réponse. Un verso pourrait se discuter, mais un miroir dessiné générique peut aussi faire croire à un réglage universel. |
| `c-medicaments-niveaux` | Les pictogrammes complets portent les consignes demandées par les clozes. Pas au recto. Le générateur existant ne suffit pas à justifier leur ajout ; un verso reste possible si une difficulté de reconnaissance apparaît. |
| `e-covoiturage-voie` | Le losange existe dans `vr-losange-debut` et `marq-losange-vr`. Ne pas ajouter une troisième reconnaissance déguisée ; les conditions d’usage se travaillent séparément. |
| `c-indice-ballon`, `c-indice-cycliste-regard`, `r-nuit-vitesse-visibilite` | Pour détecter un indice ou apprécier la visibilité, préférer des photos/vidéos nouvelles. Un ballon très visible ou un regard grossi en SVG risque de rendre le rappel trivial. |
| `a-pls`, `a-rcp-dae`, `a-hemorragie` | Les cartes testent d’abord le choix de l’action selon l’état de la victime. Un dessin du geste au recto donne cette action ; une procédure graphique exigerait des références techniques et une vérification dédiée. Ne pas improviser une gestuelle médicale. |
| Réglementation administrative, sanctions, seuils, formalités ; écoconduite générale | Aucun besoin manifeste de scène dans ce repérage. Ne pas ajouter de permis, billets, balances ou voitures décoratives aux rappels numériques et conceptuels. Un tableau explicatif peut suffire si une confusion précise apparaît. |

## Comment reprendre ce travail

Commencer par `r-chantier-fleche-lumineuse`, puis comparer l’intérêt de `u-corridor-securite` et
`u-cycliste-tourner-droite`. Ce sont des essais proposés, sans obligation de réaliser un lot ni de suivre
ensuite tout le tableau. Les vues techniques au verso peuvent attendre une décision sur leur apport réel.

Pour un candidat, reprendre la note entière et ses voisines, écrire la décision que l’apprenant devra prendre,
puis confronter la version textuelle à un prototype de carte complète. L’image doit apporter une information
utile ou expliquer une relation ; supprimer du prompt la description devenue inutile, sans retirer les
conditions que le dessin ne peut pas établir. Vérifier aussi que le cas fonctionne si l’on change une
position ou un usager pertinent : on cherche une règle transférable, pas le souvenir de cette composition.

Réutiliser `SVG`, la palette, les véhicules et les symboles existants dans `build/diagrams.py` et
`build/gen_images.py`. Le support sert le sujet : SVG pour géométrie contrôlée, média technique sourcé pour
un détail matériel, photos/vidéos pour la perception. Pas de bibliothèque de scènes ni de génération en masse
à partir de cette liste. Un helper partagé se justifie par une réutilisation concrète.

**Limite technique actuelle :** `image` apparaît au recto et reste au verso. `comparaisons` ajoute au verso
des médias de reconnaissance déjà présents. Les nouveaux schémas explicatifs proposés ici n’ont pas encore
de champ dédié au verso : décider du plus petit ajout nécessaire avec le premier cas retenu, sans utiliser
une fausse reconnaissance ni modifier tous les types de notes par anticipation. Attention aux images communes
aux cartes d’une même note cloze.

Avant intégration, consulter la source primaire pour la règle **et** la configuration dessinée, consigner
la portée dans le registre, puis contrôler attribution, rendu clair/sombre sur téléphone et absence d’indices
involontaires. Suivre les vérifications de [maintenance](maintenance.md). Ce document ne remplace pas cette
validation. Après décision, mettre à jour la ligne avec le motif et le commit : intégrée, différée ou abandonnée.
La présence dans une table ne suffit jamais à considérer l’image comme validée ; le motif d’un refus reste utile
aux prochains contributeurs. Réexaminer une décision si une difficulté concrète ou un meilleur prototype le justifie.
