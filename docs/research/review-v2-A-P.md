# Relecture contradictoire — thèmes A (Porter secours, 07) et P (Prendre et quitter son véhicule, 08)

Périmètre : `data/{questions,faits,affirmations}/07_premiers_secours.yaml` et `…/08_prendre_quitter.yaml`.
Référentiels : `docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026), `docs/research/exam.md` §3.1,
`knowledge-facts.md` (P1-P7, S1-S5, « Pièges U et S »), `legal-facts.md` (D3, E5, E7, G3),
`review-facts-questions.md`, `brief-v2-redaction.md`, `docs/05-audit-v2.md`, rapport de rédaction `v2-A-P.md`.

## Bilan

| | notes relues | ERREUR | DOUTE | STYLE |
|---|---|---|---|---|
| questions/07 | 14 | 1 | 2 | 1 |
| faits/07 | 8 | 0 | 0 | 1 |
| affirmations/07 | 14 | 2 | 3 | 0 |
| questions/08 | 21 | 1 | 3 | 1 |
| faits/08 | 2 | 0 | 0 | 0 |
| affirmations/08 | 15 | 3 | 1 | 1 |
| **total** | **74** | **7** | **9** | **4** |

Corrections **appliquées** : 7 ERREUR + 4 STYLE (dont 2 suppressions de doublons).
`python -m build.build --check` ne renvoie plus rien sur `07_premiers` ni `08_prendre`
(la seule erreur restante, `02_circulation.yaml:aff-l-vehicule-a-stop`, est hors périmètre).
Effectifs après relecture : A = 14 Q + 8 F + 14 AFF (6 vrai / 8 faux = 43 %) ;
P = 21 Q + 2 F + 13 AFF (5 vrai / 8 faux = 38 %).

Les valeurs suivantes ont été recontrôlées une à une et sont **exactes** : 15/17/18/112/114 ; bornes
autoroute tous les 2 km ; triangle « 30 m environ » (arrêté du 30 septembre 2008, art. 2 — le code ne
chiffre rien, E5) ; gilet « à portée de main », revêtu avant de sortir (R416-19 II) ; RCP 30/2, 5-6 cm,
100-120/min ; brûlure 10-20 min à l'eau tempérée ; DAE utilisable sans formation (décret 2007-705) ;
non-assistance 5 ans / 75 000 € (CP 223-6) ; délit de fuite 3 ans / 75 000 € / 6 points (CP 434-10,
repris à CR L231-1) ; R231-1 (1°/2°/3°) ; R417-7 (tout occupant, 1re classe) ; R417-8 (« précautions
utiles ») ; R412-10 (avertir pour reprendre sa place) ; déclaration assureur 5 jours ouvrés (C. assur.
L113-2) ; 70 °C en 20 min ; appuie-tête au sommet de la tête ; 5 s à 90 km/h = 125 m ; Q1, Q6, Q8, Q14
conformes à `exam.md` §3.1 ; correction n° 20 de `review-facts-questions.md` (112 sans carte SIM) bien
maintenue dans `numeros-urgence`.

---

## `data/questions/07_premiers_secours.yaml`

**`a-accident-corporel-obligations`** — ERREUR (appliquée)
- Problème : la réponse disait « ne rien modifier sur les lieux : les véhicules restent en place pour
  l'enquête ». R231-1 3° c) n'impose d'éviter la modification de l'état des lieux que « dans toute la
  mesure compatible avec la sécurité de la circulation » ; la formulation absolue peut conduire à
  laisser un véhicule dangereux en place.
- Correction : « Rester sur place, faire prévenir la police ou la gendarmerie et lui donner mon
  identité ; je ne modifie pas l'état des lieux (traces, position des véhicules) autant que la sécurité
  de la circulation le permet. » (35 mots, 3 éléments).
- Source : `cdr.txt`, R. 231-1 3° a) b) c).

**`a-pls`** — STYLE (appliquée)
- Problème : contradiction de récit avec `a-evaluer-victime`, dont le contexte pose « Zone protégée,
  secours alertés », alors que `a-pls` conclut « puis j'alerte ».
- Correction : « puis j'alerte **si ce n'est pas fait** et je surveille sa respiration » (38 mots).
- Source : knowledge-facts P4 (PLS puis alerte, dans l'ordre Croix-Rouge).

**`a-proteger-arret`** — DOUTE (non appliqué)
- Problème : l'explication écrit « gilet pour chaque occupant qui sort » avec `source: art. R416-19`.
  R416-19 II n'impose le gilet qu'**au conducteur** ; l'extension aux passagers est une recommandation
  (knowledge-facts P2), pas une obligation. Un candidat peut y lire une règle de droit.
- Proposition : « gilet pour le conducteur — et pour tout occupant qui sort, c'est la consigne de
  sécurité ». Source : `cdr.txt` R. 416-19 II ; knowledge-facts P2.

**`a-casque-motard`** — DOUTE (non appliqué)
- Problème : recouvrement franc avec `aff-a-pls-avec-casque` (même connaissance : on ne retire pas le
  casque). Le brief §2.8 ne tolère la double forme que si la seconde porte un piège distinct ; ici les
  deux pièges (« pour qu'il respire mieux » / « PLS avec le casque ») sont très proches.
- Proposition : garder la question et supprimer l'affirmation, **ou** réorienter l'affirmation vers un
  autre geste du motard accidenté (ne pas le relever, ouvrir la visière). Non appliqué : la suppression
  ferait tomber 07 à 5 vrai / 8 faux (38 %), acceptable, mais le choix relève du rédacteur.
- Source : knowledge-facts P4/P7 ; brief §2.8.

---

## `data/faits/07_premiers_secours.yaml`

**`triangle-distance`** — STYLE (appliquée)
- Problème : la carte ne donnait que « environ 30 m » alors que knowledge-facts P2 et le piège P7
  (« Sur autoroute je pose le triangle à 30 m comme ailleurs » → FAUX) retiennent « 100 m au moins sur
  route rapide/nationale ». Incomplet sur un piège explicitement recensé.
- Correction (explication) : ajout de « Sur route rapide, il se place plus loin (100 m et plus). » ;
  `source` : « securite-routiere.gouv.fr » remplacé par « Ornikar — Protéger la zone », qui est la
  source réelle du 100 m dans le dossier.
- Source : knowledge-facts P2 et P7 ; legal-facts E5 (arrêté du 30 septembre 2008 : « 30 mètres environ,
  ou au-delà si nécessaire »).

---

## `data/affirmations/07_premiers_secours.yaml`

**`aff-a-contact-vehicules-accidentes`** — ERREUR (appliquée)
- Problème : l'affirmation reposait sur une prémisse fausse — « Je laisse leur contact mis **pour que
  leurs feux de détresse continuent de clignoter** ». Les feux de détresse fonctionnent contact coupé
  (c'est une exigence d'homologation) ; la carte apprenait donc une fausse mécanique en même temps que
  la bonne consigne.
- Correction : affirmation remplacée par « Laisser leur contact mis ne présente pas de risque
  particulier. » (verdict `faux` inchangé, `pourquoi` inchangé) — forme de distracteur attestée par le
  brief §1.
- Source : knowledge-facts P2 (« couper le contact des véhicules accidentés (risque d'incendie) »).

**`aff-a-rester-sur-place`** — ERREUR (appliquée)
- Problème : contradiction interne avec le fait `non-assistance`, dont l'explication dit « Alerter les
  secours suffit à remplir l'obligation ». Le `pourquoi` affirmait au contraire que, **après avoir
  alerté**, « Partir, c'est s'exposer au délit de non-assistance à personne en danger ». Pour un simple
  témoin qui a alerté, l'obligation de l'art. 223-6 CP est remplie : l'affirmation juridique est fausse.
- Correction : « Celui qui alerte reste joignable, surveille la victime et fait signe aux secours :
  l'opérateur peut rappeler ou demander un geste. Conducteur impliqué, je n'ai de toute façon pas le
  droit de quitter les lieux (R231-1). » ; `source` → « Croix-Rouge française — Alerter ; Code de la
  route, art. R231-1 ».
- Source : knowledge-facts P1 (« porter assistance (au moins alerter) ») ; `cdr.txt` R. 231-1 1°.

**`aff-a-triangle-autoroute`** — ERREUR d'attribution (appliquée)
- Problème : le `pourquoi` imputait la dispense à « (R416-19) ». R416-19 I ne prévoit **aucune**
  dispense (knowledge-facts P2 : « le code n'exempte pas formellement ») ; la dispense (« mise en danger
  manifeste de la vie du conducteur ») est dans l'arrêté du 30 septembre 2008.
- Correction : « La mise en place du triangle n'est pas exigée quand elle met manifestement en danger la
  vie du conducteur (arrêté du 30 septembre 2008) : feux de détresse et mise à l'abri priment. Ailleurs,
  30 m au moins. »
- Source : `cdr.txt` R. 416-19 I à V ; legal-facts E5 (citation de l'arrêté).

**`aff-a-pls-avec-casque`** — DOUTE, nuance mineure appliquée
- Problème : knowledge-facts P4 marque « PLS avec le casque » **À VÉRIFIER** (le PSC1 enseigne le
  retrait à deux pour la RCP ; seul l'examen attend « ne pas retirer »). Le brief §2.7 interdit de poser
  une valeur « À VÉRIFIER » sans nuance, et la carte affirmait sans réserve.
- Correction appliquée : « On ne retire pas le casque **(réponse attendue à l'examen)** : … » — aligne la
  carte sur `a-casque-motard`, qui porte déjà la réserve.
- Source : knowledge-facts P4 et P7.

**`aff-a-triangle-autoroute`** (second point) — DOUTE (non appliqué)
- Problème : doublon inter-thèmes avec `aff-r-autoroute-triangle` (`data/affirmations/04_route.yaml`) :
  « En panne sur la BAU, je dois poser le triangle à 30 m derrière mon véhicule » → FAUX, même règle,
  même dispense, `pourquoi` quasi identique. Le rapport `v2-A-P.md` §6 ne l'avait pas repéré.
- Proposition : supprimer l'une des deux. La règle relève plutôt du thème R (autoroute) ou du thème D
  (équipements obligatoires, `faits/06_reglementation.yaml`) ; garder `aff-a-triangle-autoroute` seulement
  si le thème R renonce à la sienne. Non appliqué : `04_route.yaml` est hors périmètre et en cours de
  réécriture par un autre rédacteur — l'arbitrage doit être fait quand les deux fichiers sont stables.
- Source : brief §2.8.

**`a-constat-desaccord` / `aff-a-constat-signature`** — DOUTE (non appliqué)
- Problème : knowledge-facts P5 marque **À VÉRIFIER** tout le paragraphe « constat amiable » (« page
  service-public dédiée non retrouvée »), et les deux cartes citent « service-public.fr — Constat
  amiable ». Le `source` de `a-constat-desaccord` cite en outre « Code des assurances, art. L113-2 », qui
  fonde le délai de 5 jours (cité, lui, dans `a-accident-materiel-obligations`) et non
  l'immuabilité du constat signé.
- Proposition : remplacer le renvoi par « service-public.fr F2679 — Accident de la route » (la seule
  page service-public réellement consultée dans le dossier) et retirer L113-2 de cette carte. Contenu
  factuel conservé : les deux affirmations retenues (on ne signe pas un constat inexact ; le constat
  n'établit pas la responsabilité) ne sont contestées par aucune source.
- Source : knowledge-facts P5 ; brief §2.7.

---

## `data/questions/08_prendre_quitter.yaml`

**`p-siege-reglage`** — ERREUR de raisonnement (appliquée)
- Problème : « ma jambe **gauche** doit rester légèrement fléchie. Jambe tendue, **je ne pourrais pas
  freiner** de toutes mes forces » — la jambe gauche commande l'embrayage, pas le frein ; l'explication
  contredisait la réponse. Le critère de la jambe gauche fixe la distance du siège, laquelle conditionne
  ensuite l'appui du pied droit sur le frein.
- Correction : « Jambe tendue, **le siège est trop loin** et je ne pourrais pas écraser le frein en
  urgence. » (31 mots).
- Source : knowledge-facts S2 (« la jambe gauche doit rester légèrement fléchie lorsque la pédale
  d'embrayage est complètement enfoncée » ; « pied droit = frein + accélérateur, talon au sol »).

**`p-passagers-descendre`** — ERREUR juridique légère (appliquée)
- Problème : « R417-7 vise tout occupant, **mais c'est le conducteur qui répond de ce qui se passe à
  bord** ». R417-7 sanctionne l'occupant qui ouvre ; la responsabilité du conducteur pour ses passagers
  est limitée aux mineurs et au port de la ceinture (R412-1, R412-2), pas à l'ouverture des portières.
- Correction : « R417-7 vise tout occupant du véhicule ; avec des enfants à l'arrière, c'est au
  conducteur d'organiser la descente. »
- Source : `cdr.txt` R. 417-7 ; legal-facts E7/G3.

**`p-verif-pare-brise`** — DOUTE (non appliqué)
- Problème : la réponse fonde la règle sur « (R412-6) ». Le II de R412-6 ne vise littéralement que la
  réduction du champ de vision « par le nombre ou la position des passagers, par les objets transportés
  ou par l'apposition d'objets non transparents sur les vitres » — le givre n'y figure pas. Le rattachement
  est celui du dossier (knowledge-facts S1) et celui de la pratique, mais il est fragile si l'épreuve
  demande l'article.
- Proposition : retirer la parenthèse de la `reponse` et garder R412-6 dans `source` seulement, ou
  écrire « le conducteur doit garder un champ de vision dégagé (R412-6 II) ».
- Source : `cdr.txt` R. 412-6 II.

**`p-pente-roues`** — DOUTE (non appliqué, carte conservée)
- Problème : knowledge-facts S4 marque **À VÉRIFIER** la nuance « en montée avec bordure : roues vers la
  chaussée » (les sources consultées ne disent que « vers le trottoir »), alors que la carte l'affirme.
  Brief §2.7.
- Vérification faite ici : la règle est mécaniquement juste (en montée le véhicule recule ; roues avant
  braquées vers la chaussée, l'arrière du pneu avant droit vient buter contre la bordure) et c'est la
  règle enseignée partout. **Recommandation : conserver la carte** et lever la mention « À VÉRIFIER »
  dans knowledge-facts S4, plutôt que d'amputer la carte. Le fait `p-quitter-reperes` ne retient, lui,
  que la partie non contestée (descente) : pas de contradiction entre les deux.
- Source : knowledge-facts S4 ; « Pièges U et S » (« 1re en montée, marche arrière en descente »).

**`p-verif-chargement-important`** — DOUTE (non appliqué)
- Problème : la question officielle Q1 est désormais portée par **trois** cartes : celle-ci (pression +
  hauteur des feux) et, dans `data/affirmations/09_mecanique.yaml`, `aff-m-chargement-pression`
  (« je diminue la pression… » FAUX, contexte « question officielle 2023, Q1 ») et
  `aff-m-reglage-feux-charge` (« je descends le faisceau… » VRAI, « Question officielle 2023 »).
- Proposition : les deux moitiés de Q1 étant déjà traitées en thème M, la carte P pourrait se recentrer
  sur ce que le thème M ne dit pas (le freinage allongé, le tour du véhicule avant un départ chargé), ou
  disparaître. Non appliqué : `09_mecanique` est hors périmètre et en cours de réécriture.
- Source : `exam.md` §3.1 Q1 ; brief §2.8.

**`p-retro-interieur`** — STYLE (non appliqué)
- Problème : la réponse (« La totalité de la lunette arrière, sans bouger la tête ni les épaules. »,
  12 mots) donne le critère mais pas le mécanisme demandé par le brief §2.3 (« la décision *et* la règle
  ou le mécanisme qui la fonde »). Le mécanisme est relégué à l'explication.
- Proposition : « … : c'est le seul rétroviseur qui ne déforme pas les distances, il sert à juger un
  véhicule qui suit et à savoir quand se rabattre. »

---

## `data/affirmations/08_prendre_quitter.yaml`

**`aff-p-appuie-tete-confort`** — ERREUR (doublon) — **carte supprimée**
- Problème : doublon quasi mot pour mot de `aff-s-appuie-tete-securite`
  (`data/affirmations/10_securite_passager.yaml`) : même affirmation (« l'appuie-tête est d'abord/sert au
  confort »), même verdict `faux`, même `pourquoi` (« sécurité passive », « coup du lapin », « réglé trop
  bas, il fait pivot »). Le rôle de l'appuie-tête relève du thème S (sécurité du passager) ; le thème P
  garde son angle propre, le **réglage**, avec la question `p-appuie-tete`.
- Correction : suppression dans `08_prendre_quitter.yaml` (la connaissance reste couverte par
  `aff-s-appuie-tete-securite` et par `p-appuie-tete`).
- Source : brief §2.8 ; legal-facts G3.

**`aff-p-assistance-stationnement`** — ERREUR (doublon) — **carte supprimée**
- Problème : doublon de `aff-m-stationnement-arriere` (`data/affirmations/09_mecanique.yaml`), qui porte
  déjà la question officielle Q8 avec le même contexte verbatim (« Ce conducteur va se ranger en créneau
  … assistance au stationnement »), un `pourquoi` plus riche (R412-6-3, limites des capteurs) et le bon
  `sous_theme` (`adas`). Le rapport `v2-A-P.md` §3 justifiait cette carte par la suppression d'un
  `p-assistance-stationnement` doublon de « `s-adas-limites` » — id qui n'existe pas dans `data/` : la
  carte réellement visée est `aff-m-stationnement-arriere`, et le doublon a donc été recréé.
  Second défaut : `sous_theme: quitter` pour une manœuvre de **rangement** en créneau.
- Correction : suppression dans `08_prendre_quitter.yaml` ; Q8 reste couverte en thème M, conformément à
  l'en-tête de `10_securite_passager.yaml` (« les aides à la conduite … sont traitées dans le thème M,
  sous-thème "adas" »).
- Source : `exam.md` §3.1 Q8 ; brief §2.8.

**`aff-p-ceinture-blouson`** — ERREUR (doublon) — **proposée, non appliquée**
- Problème : doublon de `aff-s-ceinture-manteau` (`10_securite_passager.yaml`) : contexte identique
  (hiver, grosse doudoune), verdict `vrai` identique, même mécanisme (le vêtement se comprime et laisse
  du jeu). La ceinture « protection » relève du thème S ; le thème P garde son angle propre avec
  `p-ceinture-position` et `aff-p-ceinture-sous-le-bras` (positionnement des sangles), qui eux ne sont
  pas dupliqués.
- Pourquoi non appliqué : la supprimer en plus des deux précédentes ramènerait `08_prendre_quitter.yaml`
  à 4 vrai / 8 faux = 33 %, sous le plancher de 35 % contrôlé par `build.build` (AFF_BALANCE), et donc
  en erreur de build. L'arbitrage doit être fait avec le propriétaire de `10_securite_passager.yaml` :
  soit supprimer `aff-s-ceinture-manteau` (thème S), soit supprimer `aff-p-ceinture-blouson` **en même
  temps qu'une affirmation fausse** de 08 ou en ajoutant une affirmation « vrai » propre au thème P.
- Source : brief §2.8 ; build/build.py (AFF_BALANCE = 0.35-0.65).

**`aff-p-boite-auto-position-p`** — STYLE (appliquée)
- Problème : le `pourquoi` était circulaire (« La séquence attendue demande les deux ») : il justifiait
  la règle par l'attente de l'examen au lieu du mécanisme, contrairement au brief §1 et §2.3.
- Correction : « Le cliquet de la position P n'est qu'un doigt d'acier bloquant la transmission : en
  pente il encaisse tout le poids du véhicule. Frein de stationnement serré en plus, et roues braquées
  vers le trottoir en descente. » (36 mots).
- Source : knowledge-facts S4 (« en plus du frein à main, engager une vitesse … boîte auto : P »).

**`aff-p-quitter-documents`** — DOUTE (non appliqué)
- Problème : la même consigne figure déjà dans l'explication de `p-quitter-objets` (« Les papiers du
  véhicule et les objets de valeur partent avec moi »). Ce n'est pas un doublon de cartes au sens du
  brief §2.8 (une explication n'est pas une carte), mais la redondance est frontale.
- Proposition : retirer la phrase de l'explication de `p-quitter-objets` pour que l'affirmation garde
  son effet de surprise.

---

## Points vérifiés sans remarque

- Ordre P·A·S, contenu du message d'alerte, quand raccrocher, borne plutôt que portable, 114,
  évaluation de la victime (répond / respire 10 s / saigne), PLS (femme enceinte à gauche), RCP + DAE,
  analyse du DAE, hémorragie et garrot, ne pas déplacer un blessé, incendie et plaque orange,
  obligations après accident matériel : conformes à knowledge-facts P1-P5 et à `cdr.txt`.
- Thème P : tour du véhicule, GPS avant le départ, dossier, appuie-tête, rétroviseurs intérieur et
  extérieurs, position des sangles, mains à 9 h 15, ordre d'installation (divergence Code en Poche / EVS
  correctement neutralisée), démarrage au point mort, checklist de sortie (R417-8), objets de valeur,
  pente (rapport engagé), ouverture de portière (R417-7, « portière gauche, main droite »), enfants
  seuls (70 °C / 20 min), quitter un stationnement (Q14 + R412-10) : conformes à knowledge-facts S1-S5.
- Aucune affirmation fausse ne contient de mot-signal (`toujours` / `jamais` / `obligatoirement` /
  `uniquement`) ; aucune affirmation dont le verdict se devine par le seul contexte.
- YAML : les six fichiers se chargent (`yaml.safe_load`) ; aucun scalaire nu fragile (pas de « : » ni de
  « # » non protégé). Seule remarque cosmétique : `affirmations/07` et `affirmations/08` mélangent
  scalaires quotés et non quotés d'une ligne à l'autre (`source:`, `contexte:`) — sans risque, mais
  moins lisible que le style quoté systématique des fichiers `questions/`.
- `importance` : 70 des 72 notes restent `essentiel` alors que le thème A pèse ≈ 1 question sur 40.
  Candidats naturels à `utile` : `a-alerter-borne-ou-portable`, `a-dae-utilisation`, `a-constat-desaccord`,
  `aff-a-112-remplace-les-autres`. Non appliqué : cela déplace le curriculum, décision de l'auteur.
