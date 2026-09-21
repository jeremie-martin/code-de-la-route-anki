# Décisions de conception v4

Les familles ci-dessous testent des conditions différentes. Elles sont mélangées dans le parcours ; leur regroupement ici sert à examiner le raisonnement et ne crée pas de cartes supplémentaires.

## distance-etendue

Même nombre ; les flèches changent la relation spatiale. Lire le panonceau avant de décider où anticiper.

- `l-visuel-distance` : Sous un panneau de chaussée rétrécie, je lis ce panonceau. Où le danger annoncé commence-t-il ?
- `l-visuel-etendue` : Sous un panneau de chaussée rétrécie placé au début du danger, je lis ce panonceau. Sur quelle longueur dois-je prévoir le rétrécissement ?

## arret-stationnement

Faire varier le signal puis le motif de l’immobilisation ; rester au volant ne suffit pas à qualifier un arrêt.

- `l-visuel-arret-b6a1` : De ce côté de la rue, après ce panneau, aucun autre motif d’interdiction ni danger. Puis-je déposer immédiatement mon passager en restant aux commandes ?
- `l-visuel-arret-b6d` : De ce côté de la rue, après ce panneau, aucun autre motif d’interdiction ni danger. Puis-je déposer immédiatement mon passager en restant aux commandes ?
- `l-visuel-attendre-b6a1` : Après ce panneau, je reste au volant en attendant un ami qui n’est pas encore arrivé. Est-ce autorisé de ce côté de la rue ?

## marquage-arret

Transférer la distinction arrêt/stationnement des panneaux au marquage, sans annoncer la réponse par le texte.

- `l-visuel-jaune-continu` : En bordure de cette chaussée, puis-je m’immobiliser pour charger immédiatement une valise, conducteur disponible, sans autre danger ?
- `l-visuel-jaune-discontinu` : En bordure de cette chaussée, puis-je m’immobiliser pour charger immédiatement une valise, conducteur disponible, sans autre interdiction ni danger ?

## plafond-adaptation

Lire une valeur puis distinguer son point d’application d’une permission de maintenir cette allure.

- `l-visuel-b14-position` : J’approche de ce panneau isolé, sans panonceau. Dois-je commencer à freiner au panneau ou avoir déjà atteint le plafond à son niveau ?
- `l-visuel-b14-adaptation` : Après ce panneau, des enfants jouent près du bord et pourraient surgir. La valeur affichée m’autorise-t-elle à conserver cette vitesse ?

## fin-et-regle-generale

Passer du nom d’un signal de fin à la règle qui s’applique ensuite.

- `l-visuel-fin-interdictions` : Voiture, permis hors probatoire, temps sec. Hors agglomération, une voie par sens sans séparateur, après une limitation à 50, je franchis ce panneau. Aucun autre panneau : quel plafond retrouve-je ?
- `l-vitesse-hors-agglo` : Temps sec, voiture, permis définitif. Route hors agglomération à double sens, sans séparateur central ni relèvement signalé → plafond {{c1::80 km/h}}.  Temps sec, voiture, permis définitif. Route hors agglomération à double sens sans séparateur central : le plafond peut être relevé et signalé à {{c2::90 km/h}}.

## voyant-et-contexte

Même symbole et même couleur ; moteur arrêté ou en fonctionnement changent la décision.

- `m-visuel-batterie-contact` : Ce témoin s’allume quand je mets le contact, avant de démarrer. À lui seul, prouve-t-il une panne de charge ?
- `m-visuel-batterie-roulant` : Ce témoin s’allume en roulant et reste allumé. Puis-je considérer que c’est seulement l’autotest du démarrage ?

## pression-document

Appliquer la notice exige de choisir la bonne ligne ET le bon essieu ; compléter le rappel verbal par une lecture de tableau.

- `m-visuel-pression-charge` : Cette étiquette correspond à ma voiture et à ses pneus. À pleine charge, pneus froids, quelles pressions appliquer à l’avant et à l’arrière ?
- `m-visuel-pression-usuelle` : Même étiquette, charge usuelle et pneus froids. Je lis 2,6 bar dans le tableau : est-ce la valeur à appliquer aux quatre pneus ?

## remorque-cas-limite

Changer de 50 kg fait changer de branche de la règle : ni 750 ni 3 500 kg ne sont des seuils universels isolés.

- `s-remorque-seuil-750` : Voiture de PTAC 3 500 kg, remorque de PTAC 750 kg ; capacités techniques respectées. Le permis B seul suffit-il ?
- `s-remorque-seuil-800` : Voiture de PTAC 3 500 kg, remorque de PTAC 800 kg ; capacités techniques respectées. Le permis B seul suffit-il ?

## distances-composantes

Combiner les composantes pour comparer à l’espace disponible ; changer l’adhérence sans modifier arbitrairement la réaction.

- `c-arret-somme` : L’exercice donne 15 m parcourus pendant la réaction et 25 m de freinage. Quelle est la distance d’arrêt ?
- `c-distance-freinage-mouille-exercice` : Un exercice donne 15 m de réaction et 25 m de freinage sur sol sec. Sur sol mouillé, il suppose le freinage doublé et la réaction inchangée. Quelle distance d’arrêt ?
- `c-distance-obstacle-exercice` : L’obstacle est à 35 m. L’exercice donne 15 m de réaction puis 25 m de freinage jusqu’à l’arrêt. Puis-je m’immobiliser avant l’obstacle ?
- `c-double-vitesse-arret` : À vitesse donnée : 10 m de réaction et 10 m de freinage. Je double la vitesse, avec le même temps de réaction et la même adhérence. Distance d’arrêt théorique ?

## ecart-et-exception

L’écart nécessaire n’autorise pas n’importe quel franchissement ; changer la catégorie d’usager change l’exception.

- `scn-dep-cycliste-ligne-continue` : Hors agglomération, bonne visibilité, personne en face ni en train de me dépasser. Un simple chevauchement permettrait de laisser 1,50 m au cycliste puis de revenir sans gêner. Puis-je dépasser ?
- `l-cycliste-ligne-espace` : Hors agglomération, dépasser le cycliste en laissant 1,50 m exigerait de franchir entièrement la ligne continue. Que faire ?
- `l-cavalier-ligne-continue` : Hors agglomération, un cavalier avance devant moi. L’écart de 1,50 m demanderait de chevaucher une ligne continue. Bonne visibilité : puis-je invoquer l’exception prévue pour les vélos ?

## intervalle-marge

Relier la règle temporelle à une stratégie en circulation, y compris quand le danger vient de derrière.

- `c-intervalle-repere` : Le véhicule devant passe un panneau. Je l’atteins une seconde après lui sur route sèche. Mon intervalle est-il suffisant ?
- `c-suiveur-trop-pres` : Sur une route à double sens, le véhicule qui me suit roule à quelques mètres de mon pare-chocs. Que fais-je ?

## m12-destinataire

Même feu, même direction ; changer le véhicule change la permission, jamais la priorité.

- `l-visuel-m12-edpm` : Je conduis une trottinette électrique (EDPM). Le feu est rouge et porte ce panonceau. Puis-je franchir la ligne d’effet du feu dans la direction fléchée ?
- `l-visuel-m12-voiture` : Je conduis une voiture. Le feu est rouge et porte ce panonceau. Puis-je franchir la ligne d’effet du feu dans la direction fléchée ?

## v5-acces-vitesse

Même panneau C107 ; seule la séparation des chaussées change le plafond applicable.

- `l-c107-route-simple` : Ce panneau est à l’entrée d’une route hors agglomération : une voie par sens, sans terre-plein central, ni relèvement signalé. Voiture, temps sec, hors probatoire : quel plafond ?
- `l-c107-route-separee` : Ce même panneau est à l’entrée d’une route à deux chaussées séparées par terre-plein central, hors agglomération. Voiture, temps sec, hors probatoire, sans limite plus basse : quel plafond ?

## v5-secours-condition

La présence d’un objet dans la plaie ou l’origine traumatique change l’action ; ne pas étendre une procédure hors de ses conditions.

- `a-hemorragie` : Zone protégée. Une victime saigne abondamment du bras, sans objet planté dans la plaie. Quel geste immédiat ?
- `a-objet-plaie` : Un morceau de métal est planté dans une plaie du bras qui saigne abondamment. Puis-je l’enlever puis appuyer dessus ?
- `a-pls` : Après un malaise sans chute ni traumatisme, une personne ne répond pas mais respire normalement. Quel geste après vérification de la respiration ?
- `a-traumatisme-respiration` : Après un choc routier, une victime ne répond pas mais respire normalement, allongée sur le dos, sans vomissement. La PLS est-elle automatique ?

## Retraits justifiés

Aucun plafond numérique : chaque retrait ci-dessous a un motif et une couverture conservée. La v4 est destinée à un import neuf ; réimporter ne supprime pas les anciennes cartes.

- `l-marquage-modulations` : Les longueurs de construction T1/T3 sont déjà documentées dans les signaux ; la compétence utile est la lecture et la décision, pas trois dimensions isolées. Couverture : `marq-ligne-discontinue-t1`, `marq-ligne-dissuasion`, `scn-dep-ligne-discontinue-libre`.
- `c-distance-arret-formule` : Trois résultats de carrés mémorisés ne permettent pas de calculer un arrêt réel ; remplacer par les composantes et les limites des hypothèses. La v6 réintroduit deux ordres de grandeur explicitement qualifiés (50 et 90 km/h sur sol sec), car l’épreuve les demande, sans en refaire une formule à réciter. Couverture : `c-arret-repere-limite`, `c-arret-somme`, `c-double-vitesse-arret`, `c-distance-arret-reperes`.
- `c-somnolence-stats` : Un taux sans périmètre et une équivalence expérimentale en alcoolémie ne décident pas de l’aptitude à poursuivre. Couverture : `c-somnolence-que-faire`, `aff-c-micro-sommeil`, `d-risque-comparer-bilans`.
- `c-alcool-risque-multiplie` : Écarter la récitation d’une table de multiplicateurs peu contextualisée ; conserver effets, seuils et distinction légalité/sécurité. Couverture : `aff-c-alcool-sous-seuil`, `aff-c-alcool-jugement`.
- `c-stupefiants-stats` : Remplacer les ratios de population par les effets et le risque de cumul réellement utiles à une décision. Couverture : `c-cannabis-effets`, `aff-c-medicament-alcool`, `d-stupefiants-delit`.
- `u-motos-mortalite` : Ni le pourcentage du trafic ni un risque relatif non contextualisé ne sont un seuil de conduite. Couverture : `u-moto-vulnerabilite`, `d-risque-part-exposition`.
- `u-pietons-mortalite` : Protéger les piétons selon la scène, sans apprendre deux fractions datées ni généraliser leurs capacités. Couverture : `u-personnes-agees`, `u-pieton-canne-blanche`, `d-risque-part-exposition`.
- `d-stats-tues` : Le total annuel exact devient une donnée de consultation ; apprendre à lire le périmètre et la date d’un bilan. Couverture : `d-risque-comparer-bilans`.
- `d-stats-usagers` : Une table de parts des victimes est une donnée à lire, pas un barème de risque individuel à réciter. Couverture : `d-risque-part-exposition`.
- `p-installation-reperes` : Doublons de questions ouvertes qui demandent déjà les mêmes réglages avec leur usage. Couverture : `p-appuie-tete`, `p-dossier-reglage`, `p-siege-reglage`, `p-volant-mains`.
- `p-quitter-reperes` : Même décision déjà interrogée sans indices par les questions de portière et de pente. Couverture : `p-ouvrir-portiere`, `p-pente-vitesse`.
- `m-adas-dates` : Les dates de généralisation étaient aussi ambiguës entre homologation et immatriculation ; vérifier l’équipement réel et sa fonction. Couverture : `m-adas-equipement-reel`, `s-ecall`, `s-esp-fonction`, `m-afu-aeb`.
- `m-batterie-liquides-chiffres` : Trois phrases à compléter par « notice » n’ajoutent pas de compétence aux applications, sauf l’échéance temporelle désormais explicitée. Couverture : `m-batterie-cables`, `m-liquide-frein`, `m-distribution-delai`.
- `s-airbag-chiffres` : Distance déjà interrogée ; réciter l’unité de vitesse de déploiement apporte moins que connaître la bonne position. Couverture : `s-airbag-distance`, `aff-s-airbag-pieds`.
- `s-ceinture-efficacite` : Les chiffres de risque et la pseudo-frontière de 20 km/h n’ajoutent rien à la décision de s’attacher à toute allure. Couverture : `s-ceinture-obligation`, `s-ceinture-50-kmh`, `aff-s-airbag-remplace-ceinture`.
- `e-rapports-chiffres` : Répétition à trous de trois règles déjà demandées par des questions ouvertes. Couverture : `e-rapports-regime`, `e-moteur-arret`.
- `e-trajets-courts-chiffres` : Fractions collectives non datées ; conserver l’effet des trajets à froid et le choix de mobilité. Couverture : `aff-e-trajets-courts`, `e-ecomobilite-choix`.
- `c-intervalle-urgence-arriere` : Ajout de cette révision identifié comme doublon d’une application déjà présente. Couverture : `c-suiveur-trop-pres`.
- `d-fourriere-abandon` : Le délai de récupération en fourrière relève de la consultation de la notification ; la prévention du stationnement abusif est conservée. Couverture : `l-stationnement-categories`.
- `d-amende-minoree-majoree` : Réciter les montants de paiement ne prépare pas une décision de conduite ; lire délais et montants sur l’avis reçu. Couverture : `d-classes-amendes`.
- `e-vitesse-chiffres` : Résultats arithmétiques fixes appris par cœur ; le nouveau tableau demande de lire et comparer des données sans universaliser une économie. Couverture : `e-budget-trajet-tableau`.
- `r-autoroute-sortie-ratee` : Même décision et mêmes conditions que la question existante ; aucun transfert supplémentaire. Couverture : `l-demi-tour-marche-arriere`.
- `s-remorque-cas-b` : Révision v6 : cinq applications pour une règle de permis que l’examen pose rarement ; la paire 750/800 kg et le cas de la remorque vide gardent les trois discriminations utiles. Couverture : `s-remorque-seuil-750`, `s-remorque-seuil-800`, `s-remorque-masse-reelle`.
- `s-remorque-cas-b96` : Révision v6 : même contraste que le cas 800 kg (somme des PTAC au-delà de 3 500 kg). Couverture : `s-remorque-seuil-800`, `s-remorque-chiffres`.
- `s-remorque-permis-b` : Révision v6 : la question récitait la règle déjà portée par les rappels de la note chiffrée et exercée par les applications. Couverture : `s-remorque-chiffres`, `s-remorque-seuil-750`.
- `c-champ-visuel-chiffres` : Révision v6 : trois trous de vocabulaire (« rétrécir », « latéraux », « adapter l’allure ») demandaient de réciter une phrase, pas de rappeler une connaissance ; l’affirmation et la question d’exploration visuelle portent la même idée. Couverture : `aff-c-champ-visuel-vitesse-pieton`, `c-regarder-loin`.
- `c-retro-7s` : Révision v6 : trous de phrase (« régulièrement », « ralentissement anticipé… ») sans valeur de rappel ; la question sur le contrôle avant ralentissement suffit. Couverture : `c-retro-avant-freiner`, `c-regarder-loin`.
- `c-nuit-risque` : Révision v6 : trous de mots devinables ; l’affirmation sur le trafic fluide de nuit et la question sur la vitesse de nuit entraînent la même décision. Couverture : `aff-c-nuit-trafic-fluide`, `r-nuit-vitesse-visibilite`.
- `r-neige-adherence` : Révision v6 : remplacée par une affirmation à juger (température positive n’exclut pas le verglas), plus proche du travail demandé à l’examen qu’un trou de phrase. Couverture : `aff-r-verglas-temperature-positive`, `aff-r-verglas-pont`.
- `message-alerte` : Révision v6 : une liste à trous fait deviner l’élément caché ; la question demande le message complet. Couverture : `a-message-alerte`.
- `non-assistance` : Révision v6 : le trou portait sur une formule de sept mots ; la question demande l’obligation et sa limite. Couverture : `a-non-assistance`.
- `e-surconsommations` : Révision v6 : liste de quatre trous devinables par élimination ; la question demande les quatre facteurs. Couverture : `e-surconsommations-causes`.
