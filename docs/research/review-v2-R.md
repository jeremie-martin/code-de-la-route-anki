# Relecture contradictoire — thème R « La route » (v2)

Périmètre : `data/questions/04_route.yaml` (39 notes), `data/faits/04_route.yaml` (5 notes),
`data/affirmations/04_route.yaml` (32 notes) — **76 notes relues ligne à ligne**.
Référentiels interrogés : `docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026),
`docs/research/exam.md` §3.1, `legal-facts.md` (A2, A3, E5, F6, F8), `knowledge-facts.md` (R1-R15),
`review-facts-questions.md` (n° 41-51), `brief-v2-redaction.md`, `docs/05-audit-v2.md`,
`docs/research/v2-R.md`. Aucun autre fichier de données n'a été modifié ; pas de commit.

**Bilan : 3 ERREUR (+ 1 hors périmètre), 10 DOUTE, 12 STYLE.**
Appliqué : 3 ERREUR + 6 STYLE. Proposé sans application : 10 DOUTE + 6 STYLE.
`python -m build.build --check` : `validation OK`, aucune ligne `04_route`.
Les 32 affirmations restent à 14 vrai / 18 faux = 44 % (bande 35-65 % respectée).

## Vérifications passées sans remarque (rappel de ce qui a été contrôlé)

Toutes les valeurs juridiques du thème ont été retrouvées dans le Code consolidé et sont exactes :
R416-4 (éclairage de jour par visibilité insuffisante), R416-5 (feux de route interdits à l'arrêt,
4e classe = 135 €), R416-6 II 1° b et 2° et 3° (croisement/suivi/route éclairée/visibilité réduite),
R416-7 I et II (**avant** admis par brouillard, neige *ou forte pluie* ; **arrière** brouillard ou
neige seulement), R416-18 (détresse, dernier de la file), R416-19 I et II (triangle + gilet),
R413-2 II (110 sous la pluie), R413-4 (« sur l'ensemble des réseaux routier et autoroutier »),
R413-5 (probatoire), R413-19 (80 mini voie de gauche, sous conditions), R414-2 (2 m / 7 m),
R414-3 I et III (descendant s'arrête / recule, sauf montant près d'une place d'évitement),
R414-12, R414-13, R414-17 (engin de service hivernal + PL > 3,5 t / ensembles > 7 m),
R421-2 (liste des usagers interdits), R421-3, R421-4, R421-5, R421-6 (135 €, 4 points),
R421-7, R412-8 (BAU : 135 €, 3 points), R412-12 IV (distance imposée en tunnel),
R412-30, R422-3 I / II / V / VI / IX, R313-3 (croisement = 30 m minimum),
D314-8 II 1°, IV et V (deux roues de chaque essieu = 4 pneus ; 1er nov-31 mars ; symbole alpin).
**`R. 422-4` = passage des ponts** : confirmé ; aucune carte R ne le cite (correction du rédacteur
maintenue). `docs/research/legal-facts.md` §F6 le cite toujours à tort pour les routes à accès
réglementé — à corriger côté dossier, hors périmètre.

Conformité aux questions officielles 2023 (`exam.md` §3.1) vérifiée sur le sens : **Q10**
(`aff-r-montagne-4-pneus`), **Q18** (`aff-r-descente-150m`, `aff-r-descente-freiner-permanence`,
`r-descente-freinage` — « je freine par intermittence et j'utilise le frein moteur » verbatim),
**Q19** (`aff-r-pn-150m`, `aff-r-pn-feux-rouges-possibles`), **Q20** (`r-nuit-feux-croisement-route`).
**Q13** n'est pas dupliquée ici (elle vit dans `c-distance-mouillee`) : correct.

Les corrections de la relecture v1 (n° 41 à 50) sont toutes maintenues : « 70 km/h et plus »,
question `r-pluie-feux` conditionnée à la baisse de visibilité, loi Montagne sans amende,
150 m / 2 repères bleus en tunnel sans assimilation aux 2 s, exception « place d'évitement » côté
**montant**, source R421-3, « voie auxiliaire », aires 15-20/40-50 (voir ERREUR 3), KR42,
source R422-3 + R414-13.

---

## `data/questions/04_route.yaml`

### ERREUR 1 — `r-tunnel-panne` : on ne gare pas un véhicule dans une niche de sécurité **[appliqué]**
- Problème : la réponse dit « je gagne le **garage ou la niche** la plus proche ». Une niche de
  sécurité est un renfoncement de paroi contenant un extincteur et un poste d'appel — ce que dit le
  fait `r-tunnel-niches` du même fichier : contradiction interne. Le véhicule se range dans un
  **garage** (emplacement d'arrêt d'urgence).
- Correction appliquée (réponse) : « … je gagne le **garage (emplacement d'arrêt d'urgence)** le plus
  proche … ». L'explication, qui fait appeler « depuis le poste d'une niche de sécurité », est juste
  et reste inchangée.
- Source : `legal-facts` §F6 (« interdiction de s'arrêter **hors garages** ») ; `knowledge-facts` R7
  (« se garer sur l'emplacement d'arrêt d'urgence… appeler par la borne de la niche »).

### ERREUR 2 — `r-pn-engagement` : interdictions de dépasser et de s'arrêter généralisées **[appliqué]**
- Problème : l'explication affirmait « le dépassement et l'arrêt y sont **également interdits** » sans
  condition. R414-12 n'interdit le dépassement qu'« aux traversées de voies ferrées **non munies de
  barrières ou de demi-barrières** » ; R417-9 ne rend l'arrêt dangereux près d'un passage à niveau que
  « lorsque la visibilité est insuffisante ». Contradiction interne avec `r-pn-sans-barriere` (qui
  restreint correctement) et avec le verso de la reconnaissance `g1`.
- Correction appliquée (explication) : « … ; le dépassement est en outre interdit aux passages à
  niveau **sans barrière ni demi-barrière** (R414-12). »
- Source : cdr.txt R414-12, R417-9, R422-3 II.

### ERREUR 3 — `r-autoroute-fatigue-aires` : valeurs marquées « À VÉRIFIER » en réponse **[appliqué]**
- Problème : « une aire de repos tous les 15 à 20 km, une aire de service tous les 40 à 50 km » est
  explicitement **[AV]** dans `knowledge-facts` R11 (divergence Ornikar 15/45, EVS 20/50, APRR
  15-20/40-50) ; `legal-facts` F6 ne donne aucun espacement. Le brief (règle n° 7) interdit de mettre
  sur une carte une valeur marquée « À VÉRIFIER ». De surcroît le reste de la carte était un doublon :
  « pause toutes les 2 h » = `c-fatigue-pause-chiffres` + `aff-c-pause-sans-signe` ; « un accident
  mortel sur trois » = `c-somnolence-stats` ; « annoncées à 2 000 m puis 1 000 m » = explication du
  fait `r-autoroute-sortie-annonces`.
- Correction appliquée : carte **conservée sous le même id** mais recentrée sur ce qui n'est ni [AV]
  ni dupliqué — question « Sur autoroute, où puis-je m'arrêter pour faire une pause ? », réponse
  « Sur une aire seulement : l'aire de repos (stationnement et détente) revient le plus souvent ;
  l'aire de service y ajoute carburant et restauration. La bande d'arrêt d'urgence n'est jamais un
  lieu de pause. » (les chiffres d'espacement disparaissent, la distinction repos/service reste,
  elle, sourcée et non [AV]).
- Source : `knowledge-facts` R11 [AV] ; `legal-facts` F6 ; brief §2 règle 7.

### STYLE 1 — `r-nuit-feux-croisement-route` : l'explication soufflait une affirmation du fichier **[appliqué]**
- Problème : l'explication se terminait par « Les feux de route sont interdits à l'arrêt », qui est
  mot pour mot la réponse de l'affirmation `aff-r-nuit-feux-route-arret` du même thème.
- Correction appliquée : remplacé par le point utile et non redondant de R416-6 III (« le passage doit
  se faire *suffisamment à l'avance* »), qui fonde justement la réponse de la carte.
- Source : cdr.txt R416-6 III.

### STYLE 2 — `r-montagne-marche-arriere` : citation d'article imprécise **[appliqué]**
- Problème : l'explication annonçait « Art. R414-3 III » puis énumérait les cas de **R414-3 II**.
- Correction appliquée : « Art. R414-3 III. Entre catégories différentes (**R414-3 II**), recule … ».

### STYLE 3 — `r-tram-traversee-degager` : source incomplète **[appliqué]**
- Problème : l'interdiction de s'arrêter sur la plateforme du tramway ne découle pas de R422-3 (qui
  traite de la priorité et des passages à niveau) mais de R417-11 I 1° (arrêt **très gênant** sur une
  voie réservée à certaines catégories de véhicules).
- Correction appliquée (source) : « Code de la route, art. R422-3 **et R417-11** ; coursdecode.com ».

### STYLE 4 — `r-autoroute-panne-attendre` : superlatif non sourcé **[appliqué]**
- Problème : « Rester dans la voiture ou debout derrière elle est **la première cause de décès** lors
  d'une panne » : aucun dossier ne donne ce classement, et `c-somnolence-stats` attribue déjà « la
  première cause d'accident mortel sur autoroute » à la somnolence — deux superlatifs concurrents.
- Correction appliquée : « Rester dans la voiture, ou debout derrière elle, est ce qui tue lors d'une
  panne sur autoroute. Seul un dépanneur agréé peut y intervenir. »

### DOUTE 1 — `r-brouillard-intervalle` : doublon du fait `l-vitesse-visibilite`
- Le fait `data/faits/02_circulation.yaml:l-vitesse-visibilite` porte déjà les deux valeurs (« 50 m →
  50 km/h sur tous les réseaux, autoroute comprise ») **et** la règle des trois 50 dans son
  explication ; l'affirmation `aff-r-visibilite-50-autoroute` porte le piège R15. La question R
  restitue une troisième fois la même connaissance ; seuls le guidage sur la ligne de rive et l'effet
  « aspirateur » lui sont propres.
- Proposition (non appliquée, dépend du thème L) : soit passer la carte en `utile`, soit la recentrer
  sur le seul repère visuel (« Dans le brouillard, sur quoi je me guide, et pourquoi pas sur les feux
  du véhicule qui précède ? »), en laissant les chiffres au fait L.

### DOUTE 2 — `r-autoroute-panne` : « roues braquées vers l'extérieur » non sourcé
- Le geste ne figure ni dans `legal-facts` F6 ni dans `knowledge-facts` R11 (qui s'arrêtent à « se
  garer à droite au maximum, gilet, sortir par la droite, derrière la glissière »).
- Proposition : retirer la mention, ou la sourcer (ASFA) avant de la conserver.

### DOUTE 3 — `r-autoroute-panne-attendre` : « en amont du véhicule » non sourcé
- Même remarque : la position relative (amont / aval) n'est donnée par aucun des deux dossiers. Elle
  est conforme à la consigne enseignée, mais elle est en **réponse**, pas en explication.
- Proposition : soit sourcer, soit réduire à « derrière la glissière de sécurité, à l'écart du
  véhicule ».

### DOUTE 4 — `r-autoroute-bau` ↔ `aff-l-bau-appel` (`data/affirmations/02_circulation.yaml`)
- La réponse R dit « y rouler ou s'y arrêter **pour téléphoner** ou se reposer est interdit » ;
  l'affirmation L pose exactement la situation du coup de téléphone sur la BAU. Recouvrement assumable
  (règle 8 : piège distinct), mais à surveiller si le thème L est réécrit.

### DOUTE 5 — `r-pluie-premieres-gouttes` : mécanisme partiellement [AV]
- `knowledge-facts` R2 note **[AV]** que le mécanisme « gasoil + poussière » n'est pas cité mot pour
  mot par les sources. Le fait lui-même (« adhérence restreinte dès les premières gouttes ») n'est pas
  [AV] et la carte est juste ; seule la formule détaillée (« poussière, gomme et hydrocarbures ») est
  une reconstruction.
- Proposition : conserver, la réponse restant vraie ; ne pas durcir la formulation.

### STYLE 5 — `r-chantier-fleche-lumineuse` : dernière clause hors décision (proposé)
- « les véhicules déjà sur la voie facilitent l'insertion » décrit le comportement d'autrui et laisse
  croire à une obligation. Comparer `l-insertion-autoroute-priorite` : « rien ne les y oblige ».
- Proposition : « … ni forcer le passage ; la file se reconstitue en fermeture éclair. »

### STYLE 6 — `r-chantier-approche` : « sur une route à 90 » (proposé, très mineur)
- Une route hors agglomération à 90 suppose au moins deux voies dans le même sens (R413-2 I 3°) ;
  le décor est possible mais peut distraire. « sur une route hors agglomération » suffirait.

---

## `data/faits/04_route.yaml`

### DOUTE 6 — `r-tunnel-niches` : « environ 200 m » en position de cloze
- `knowledge-facts` R7 donne « niches tous les 200 m environ » sans marque [AV], mais `legal-facts` F6
  marque explicitement **« 200 m : À VÉRIFIER »** (pour l'interdistance en tunnel) : les deux dossiers
  ne se recoupent pas, et la valeur est le cœur du cloze c1.
- Proposition (non appliquée) : soit descendre la note en `rare`, soit remplacer c1 par un élément non
  contesté (par ex. le contenu de la niche : `{{c1::un extincteur et un poste d'appel}}`) et laisser
  l'espacement en explication avec « environ ». Le second cloze (issues **vertes**) est sûr.

Les quatre autres faits (`r-train-distance-arret`, `r-neige-adherence`, `r-loi-montagne-periode`,
`r-autoroute-sortie-annonces`) sont exacts et correctement sourcés ; les annonces 2 000 m / 1 000 m /
début de bretelle correspondent mot pour mot à `legal-facts` F6 (D50, D41, D30 — IISR 5e partie
art. 83-84) et à R421-4 II.

---

## `data/affirmations/04_route.yaml`

### STYLE 7 — `aff-r-montagne-ms` : le 3PMSF ne dispense pas du M+S **[appliqué]**
- Problème : « seul le marquage alpin 3PMSF (le flocon) vaut pneu hiver » ; D314-8 V exige « la
  présence **conjointe** du symbole alpin **et** de l'un des marquages M+S / M.S / M&S ».
- Correction appliquée : « … un pneu hiver doit porter le symbole alpin 3PMSF (le flocon) **en plus
  du marquage M+S** ; le M+S seul ne convient plus, sauf à détenir des chaînes ou des chaussettes à
  bord. » Le verdict (FAUX) et le sens de la carte sont inchangés.
- Source : cdr.txt D314-8 V ; `legal-facts` E5.

### STYLE 8 — `aff-r-tunnel-demi-tour` : ce que fonde vraiment R417-10 **[appliqué]**
- Problème : aucun article du Code n'interdit le demi-tour en tunnel (R421-6 ne vise que l'autoroute) ;
  R417-10 II 6° ne fonde que l'interdiction d'arrêt et de stationnement. La règle vient de
  l'exploitation (CETU) et de la signalisation.
- Correction appliquée (source) : « CETU — Conduire en tunnel ; Code de la route, art. R417-10
  **(arrêt et stationnement interdits en tunnel)** ». Le verdict reste juste.

### DOUTE 7 — `aff-r-nuit-pieton-sombre` ↔ `aff-u-pieton-nuit-croisement`
- `data/affirmations/05_autres_usagers.yaml:aff-u-pieton-nuit-croisement` porte déjà, du point de vue
  du piéton, « un conducteur en feux de croisement ne me découvre qu'à une trentaine de mètres »
  (VRAI). L'affirmation R reprend la même trentaine de mètres du point de vue du conducteur ; seul
  l'apport du gilet rétroréfléchissant lui est propre.
- Proposition : passer `aff-r-nuit-pieton-sombre` en `utile`, ou la recentrer sur le gain apporté par
  le gilet sans redire la portée des feux (déjà en fait `m-feux-portees`).

### DOUTE 8 — trois affirmations recouvrant `l-demi-tour-interdit` (`data/questions/02_circulation.yaml`)
- Cette question L répond déjà : « Sur l'autoroute et les routes à accès réglementé (**y compris par
  une trouée du terre-plein central**) ; **dans les tunnels** ; … » et son explication ajoute « **au
  péage non plus, on ne recule pas** ». Les trois affirmations `aff-r-autoroute-trouee-terre-plein`,
  `aff-r-tunnel-demi-tour` et `aff-r-peage-reculer` en sont la déclinaison quasi littérale.
- Proposition : en conserver deux au plus côté R (la trouée du terre-plein et le péage sont les deux
  pièges d'examen réels ; le demi-tour en tunnel est le plus faible des trois), ou attendre la
  réécriture v2 du thème L et arbitrer à ce moment-là.

### DOUTE 9 — `aff-r-autoroute-vitesse-pluie` ↔ explication de `l-vitesse-pluie` (`data/faits/02_circulation.yaml`)
- Le fait L dit déjà : « Sous la pluie, la limite probatoire et la limite normale se rejoignent sur
  autoroute (110) », qui est exactement le `pourquoi` de l'affirmation.
- Proposition : conserver (l'affirmation est la forme d'examen), mais ne pas ajouter d'autre carte sur
  ce point.

### DOUTE 10 — `aff-r-descente-150m` ↔ `l-danger-implantation` (`data/faits/02_circulation.yaml`)
- L'explication du fait L cite déjà Q18 verbatim (« la descente dangereuse à 15 % commence à environ
  150 m (OUI, hors agglomération) »). Même remarque pour `aff-r-pn-150m` ↔ `l-balises-j10`.
- Proposition : conserver — l'audit §2.2 justifie explicitement de rejouer les formes officielles en
  affirmation ; simplement, ne pas en créer une troisième occurrence.

### STYLE 9 — `aff-r-nuit-feux-route-arret` : citation du Code, donc devinable (proposé)
- « À l'arrêt ou en stationnement, l'usage des feux de route est interdit » est le texte même de
  R416-5 : la forme légale signale le VRAI.
- Proposition : situer l'énoncé et inverser le verdict, par ex. contexte « Je m'arrête sur le
  bas-côté d'une route non éclairée, la nuit », affirmation « Je laisse mes feux de route allumés pour
  être vu de loin » → **FAUX** (R416-5 ; on se signale par les feux de position). L'équilibre du
  fichier passerait à 13/19 = 41 %, toujours dans la bande.

### STYLE 10 — `aff-r-brouillard-depasser` : deux connaissances et réponse devinable (proposé)
- « je reste sur la voie de droite **et** je renonce à dépasser » : deux gestes dans un énoncé, et un
  énoncé prudent se devine VRAI.
- Proposition : ne garder que le dépassement, ou inverser en distracteur (« Le brouillard s'éclaircit
  par plaques : je profite d'une éclaircie pour dépasser » → FAUX).

### STYLE 11 — `aff-r-tram-station-pieton` : « peut masquer » se devine VRAI (proposé)
- Une affirmation de possibilité est presque toujours vraie. Proposition : passer au geste
  (« Je dépasse ce tramway à l'arrêt du côté où les voyageurs descendent » → FAUX, R414-13), ce qui
  fait travailler la même vigilance avec un vrai piège.

### STYLE 12 — `aff-r-autoroute-voie-gauche-80` : « en toutes circonstances » (signalé, non modifié)
- Ce n'est pas un des quatre mots-signaux contrôlés par le build, mais la locution joue le même rôle
  dans une affirmation **fausse**. Elle est toutefois exactement la formulation du piège
  `knowledge-facts` R15 — conservée à ce titre, signalée pour mémoire.

---

## Hors périmètre (à traiter par les rédacteurs concernés)

### ERREUR (fichier du thème L) — `l-vitesse-visibilite`, `data/faits/02_circulation.yaml`
- Son explication dit : « Quand la visibilité est inférieure à 50 m (brouillard, neige, **pluie
  violente**) … feux de brouillard avant **et arrière** autorisés et recommandés (R416-7). » Sous la
  pluie, même violente, les feux **arrière** de brouillard sont interdits (R416-7 II : « qu'en cas de
  brouillard ou de chute de neige »). L'explication contredit donc `aff-r-brouillard-arriere-pluie`,
  `knowledge-facts` R15 et `legal-facts` F8 (« jamais sous la pluie », « piège classique »).
- Correction proposée : « … feux de croisement obligatoires ; feux de brouillard avant autorisés, et
  arrière seulement si la visibilité est réduite par le brouillard ou la neige (R416-7). »

### `docs/research/legal-facts.md` §F6
- « Route à accès réglementé (B7b) … — CR art. **R422-4** » : R422-4 traite du passage des **ponts** ;
  le code de panneau est **C107** (fin C108), pas B7b. Les interdictions des routes à accès réglementé
  ne découlent pas de R421-2 mais de la signalisation (IISR 5e partie, art. 75), comme le dit déjà
  `conf-c107-c207`. Le thème R a été purgé de cette référence.

### Lacunes de la carte des connaissances (`docs/02-carte-des-connaissances.md`, ligne « Tramways… »)
- « routes étroites (B15/C18) » et « ponts » n'ont aucune carte R (les deux premiers vivent en
  reconnaissance, ce qui est défendable ; les ponts ne sont traités que par `aff-r-verglas-pont`).
  Le « corridor de sécurité » (R412-11-1), pertinent pour les chantiers, est couvert côté U
  (`u-corridor-securite`) : pas de doublon à créer.

---

## Vérification finale

```
$ python -m build.build --check | grep -E "04_route"      # (aucune sortie)
$ python -m build.build --check | tail -1
validation OK
```
Les trois fichiers se chargent (`yaml.safe_load` : 39 / 5 / 32 notes, ids uniques et inchangés).
