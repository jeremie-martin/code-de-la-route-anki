# Relecture contradictoire — thème L « Circulation » (v2)

Date : 21 septembre 2026. Fichiers relus intégralement, note par note :
`data/questions/02_circulation.yaml` (42 notes), `data/faits/02_circulation.yaml` (24 notes, 53 clozes),
`data/affirmations/02_circulation.yaml` (48 notes) — **114 notes relues**.

Référentiels : `docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026, articles relus directement :
R110-2, R411-25, R411-26, R411-28, R412-6, R412-9 à R412-12, R412-18 à R412-27, R412-30 à R412-33,
R412-37, R413-1 à R413-8, R413-17, R413-19, R414-1 à R414-17, R415-1 à R415-15, R416-1 à R416-7,
R416-12, R416-18 à R416-20, R417-1 à R417-13, R421-1 à R421-8, R422-1 à R422-4) ;
`docs/research/exam.md` §3.1 (Q2, Q18, Q19) ; `legal-facts.md` (A, F1-F9) ; `knowledge-facts.md` (L) ;
`review-facts-questions.md` (n° 4-6, 25-33) ; `brief-v2-redaction.md` ; `docs/05-audit-v2.md` ;
et, pour les contradictions inter-fichiers, `data/scenarios/*.yaml`, `data/reconnaissance/*.yaml`,
`data/confusions/signalisation.yaml`, `data/questions|affirmations/04_route.yaml` et `05_autres_usagers.yaml`.

**Bilan : 11 ERREUR, 8 DOUTE, 6 STYLE.** Les 11 ERREUR et les 6 STYLE sont **appliquées** ;
les 8 DOUTE sont **proposées** sans modification. Aucune carte supprimée, aucun id renommé.
`python -m build.build --check | grep 02_circulation` ne renvoie rien ; les trois YAML se chargent
(42 / 24 / 48 notes, ids uniques ; affirmations 19 vrai / 29 faux = 40 %).

Les corrections de la relecture v1 qui concernaient ces fichiers (n° 4, 5, 6, 25 à 33) ont été
re-vérifiées comme présentes ou rendues sans objet : giratoire = intersection sans dépassement
(R414-11) dans `l-giratoire-vs-rond-point` et `aff-l-giratoire-depassement` ; chevauchement de ligne
continue réservé aux cycles/EDPM/cyclomobiles légers dans `aff-l-continue-cyclomoteur` ; fin
d'interdiction rond blanc barré de noir / fin d'obligation rond bleu barré de rouge dans
`l-formes-couleurs-panneaux` ; E31 lieu-dit fond noir lettres blanches italiques dans
`l-agglomeration-panneau` et `aff-l-lieu-dit` (conforme à `docs/05-audit-v2.md` §2.7, qui tranche
contre la proposition « fond blanc » de la relecture v1) ; régimes gênant / très gênant / dangereux
séparés (R417-9 à R417-11). Sur le n° 5, le rédacteur a écrit **B6b2** pour la zone de stationnement
alterné là où la relecture v1 proposait B6b3 : **le rédacteur a raison** (B6b2 = zone à alternance
semi-mensuelle, B6b3 = zone bleue, cf. `data/reconnaissance/panneaux_zones.yaml`) ; la relecture v1
est donc corrigée sur ce point.

---

## 1. `data/questions/02_circulation.yaml`

### ERREUR (appliquées)

**1. `l-depassement-interdit-lieux-2` — « ou un bus arrêté côté voyageurs »**
- Problème : la réponse interdisait de dépasser « un tramway **ou un bus** arrêté côté voyageurs ».
  R414-13 ne vise que « un train ou un véhicule de transport public assujetti à suivre, de façon
  permanente, une trajectoire déterminée par un ou des rails » : un autobus ou un autocar à l'arrêt
  n'est couvert par aucune interdiction textuelle de dépassement. Contradiction directe avec
  `u-tram-depasser` (« un tramway (ou un train) ») et avec `aff-u-car-scolaire-depassement` (thème U).
- Correction (réponse) : « … et un tramway **ou un train** arrêté côté voyageurs. »
- Source : cdr.txt R414-13 ; legal-facts F2 (« un train ou tramway à l'arrêt côté montée/descente »).

**2. `l-tourner-gauche-regle` — article hors sujet**
- Problème : `source: … R415-4 et R412-30`. R412-30 règle l'arrêt au feu rouge ; la carte porte sur un
  tourne-à-gauche **sans feu** et sur le clignotant.
- Correction : `source: Code de la route, art. R415-4 et R412-10`.
- Source : cdr.txt R415-4 III (céder aux véhicules d'en face), R412-10 (avertir avant de se porter à gauche).

**3. `l-demi-tour-marche-arriere` — article hors sujet**
- Problème : `source: … R421-6 et R416-20`. R416-20 ne traite que des **feux** de marche arrière
  (« ne peuvent être allumés que pour l'exécution d'une marche arrière ») ; il ne fonde ni
  l'interdiction de demi-tour ni celle de franchir une ligne continue.
- Correction : `source: Code de la route, art. R421-6 et R412-19`.
- Source : cdr.txt R421-6 (demi-tour et marche arrière sur autoroute : 4e classe, 4 points — valeurs
  de la carte confirmées), R412-19 (ligne continue), R416-20.

**4. `l-stationnement-hors-agglo-nuit` — mauvais article (deux fois)**
- Problème : l'explication commence par « R417-1 » et la source cite R417-1, alors que la carte porte
  sur le stationnement **hors agglomération** : c'est R417-4 (« tout véhicule à l'arrêt ou en
  stationnement doit être placé autant que possible hors de la chaussée »). R417-1 ne vise que
  l'agglomération.
- Correction : explication « R417-4. … » ; `source: Code de la route, art. R417-4 et R416-12`.
- Source : cdr.txt R417-1 I / R417-4 I ; legal-facts F1 (« CR art. R417-1, R417-4 »).

**5. `l-panonceau-portee` — exemple de présignalisation faux**
- Problème : « panonceau « 150 m » sous un STOP = présignalisation ». Le signal avancé du STOP n'est
  pas l'octogone AB4 avec un panonceau de distance, mais le **panneau AB5** (triangulaire) complété du
  **panonceau M5** ; M1 (distance) ne se place pas sous un AB4.
- Correction (explication) : « panonceau M5 « STOP 150 m » sous un signal avancé AB5 = le STOP est
  150 m plus loin. »
- Source : `data/reconnaissance/panneaux_priorite.yaml` (ab5), `panonceaux.yaml` (M5) ;
  legal-facts F3 ; IISR 3e partie art. 42-2.

**6. `l-bus-quitte-arret` — citation entre guillemets non conforme au texte**
- Problème : l'explication mettait entre guillemets « faciliter la sortie », formule absente de
  R412-11, qui dit « ralentir si nécessaire et au besoin s'arrêter pour laisser les véhicules de
  transport en commun quitter les arrêts signalés comme tels ».
- Correction (explication) : citation remplacée par les mots du texte ; la restriction « en
  agglomération seulement » est conservée (cohérente avec `aff-u-bus-hors-agglo`).
- Source : cdr.txt R412-11.

### STYLE (appliquées)

**7. `l-stop-arret`** — « ou à l'aplomb du panneau s'il n'y a pas de ligne » remplacé par « ou, si elle
manque, **à la limite de la chaussée abordée** », formule exacte de R415-6 (l'aplomb du feu, lui, est
la règle de R412-30 ; et l'IISR impose une ligne STOP continue de 50 cm avec tout AB4, cf.
knowledge-facts L). Source : cdr.txt R415-6 ; knowledge-facts L (art. 117-4 A).

**8. `l-tourner-droite-serrer`** — « je ne m'y déporte pas » sur une **bande** cyclable relève de
R412-23 I 2° (on ne franchit la ligne d'une voie réservée que pour quitter ou aborder la chaussée) ;
R415-14 ne vise que la **piste**. Article ajouté dans l'explication et dans `source`.
Source : cdr.txt R412-23 I 2°, R415-14.

**9. `l-vocab-chaussee-voie`** — R110-2 définit « chaussée » et « voie de circulation » mais **pas**
« accotement » (il n'apparaît que dans la définition de la bande d'arrêt d'urgence).
`source` complétée : « … R110-2 ; IISR 7e partie ». Source : cdr.txt R110-2.

### DOUTE (proposés, non appliqués)

**10. `l-double-file` — « l'arrêt en double file est gênant (35 €) »**
- R417-10 **III** 2° ne qualifie de gênant que le *stationnement* en double file ; l'arrêt de 30 s
  décrit par la carte reste un « arrêt » au sens de R110-2. La qualification se rattache alors au I
  (« placé de manière à gêner le moins possible la circulation »), puni par le IV qui vise bien
  « tout arrêt ou stationnement gênant ». La carte est donc défendable et conforme aux dossiers
  (knowledge-facts L : « double file gênant », « pas de feux de détresse pour un arrêt en double
  file »). **Proposition** : ajouter en explication « le III vise le stationnement ; un arrêt qui
  bloque une voie tombe sous le I » — ou laisser tel quel, la convention d'examen étant celle de la carte.

**11. `l-entrecroisement` — « chacun facilite, celui qui change de voie cède »**
- Vérifié : knowledge-facts L reprend mot pour mot cette règle avec la même source (R421-3 ; IISR
  7e partie art. 117-3). Aucun article ne la formule directement. La carte est **conservée telle
  quelle** ; à surveiller si un référentiel officiel la contredit.

**12. `l-vocab-routes-lettres` et `l-vitesse-separateur-autoroute` — « route à accès réglementé : 110 »**
- R413-2 fixe 110 km/h pour les routes **à deux chaussées séparées par un terre-plein central**, pas
  pour la catégorie « route à accès réglementé » : une voie express bidirectionnelle serait à 80.
  legal-facts A1 et F6 retiennent toutefois « 110 par défaut » comme convention d'examen.
  **Proposition** : laisser la valeur, mais dire « 110 km/h quand elle est à chaussées séparées ».

**13. Deux tourne-à-gauche face à face** — le rapport `v2-L.md` §4 affirme que « ni legal-facts ni
knowledge-facts ne tranchent ». C'est inexact : `knowledge-facts.md` (section L, « Tourner à gauche »)
écrit « un véhicule en face qui tourne à sa gauche : on se croise **par la droite** (R414-1) sauf
aménagement », avec source. `docs/02-carte-des-connaissances.md` (L4) dit « par la gauche ».
**Proposition** : trancher pour « par la droite » (R414-1 : « les croisements s'effectuent à droite »)
et réintroduire la phrase dans `l-tourner-gauche-regle`, ou corriger la carte des connaissances.
Non appliqué : c'est un arbitrage de projet, pas une erreur de la carte actuelle.

---

## 2. `data/faits/02_circulation.yaml`

### ERREUR (appliquées)

**14. `l-feux-detresse-usage` — 35 € appliqué à deux infractions de classes différentes**
- Problème : « … et, avec le triangle, pour présignaler un véhicule immobilisé dangereux ; ne pas les
  utiliser **dans ces cas** : {{c2::35 €}} ». Le défaut de présignalisation d'un véhicule immobilisé
  dangereux est puni par R416-19 V de l'amende de **4e classe (135 €)**, pas de 2e classe.
  Seul R416-18 (allure fortement réduite) est à 35 €. legal-facts F8 range les deux sous « 2e classe » :
  c'est le dossier qui est imprécis, cdr.txt fait foi (brief §2.7).
- Correction (texte) : « … à allure fortement réduite ({{c1::dernier véhicule d'un bouchon}}) — ne pas
  les allumer : {{c2::35 €}} — et, avec le triangle, pour présignaler un véhicule immobilisé dangereux
  — défaut de présignalisation : {{c3::135 €}}. » ; explication : « Allure réduite : R416-18, 2e classe.
  Présignalisation d'un véhicule immobilisé dangereux : R416-19, 4e classe. … »
- Source : cdr.txt R416-18 (dernier alinéa) et R416-19 V.

**15. `l-vitesse-visibilite-50` — feux de brouillard arrière « autorisés » sous la pluie**
- Problème : l'explication (« brouillard, neige, **pluie violente** … feux de brouillard avant **et
  arrière** autorisés et recommandés ») laissait entendre que les feux arrière de brouillard sont
  admis sous la pluie. R416-7 II : « Le ou les feux arrière de brouillard ne peuvent être utilisés
  qu'en cas de brouillard ou de chute de neige. » Contradiction avec `aff-r-brouillard-arriere-pluie`
  (thème R). (Signalé par le relecteur du thème R.)
- Correction (explication) : « … Feux de croisement obligatoires ; feux de brouillard avant admis ;
  feux de brouillard arrière seulement par brouillard ou chute de neige, jamais sous la pluie (R416-7). »
- Source : cdr.txt R416-7 I et II ; legal-facts F8 (« jamais sous la pluie — piège classique »).

**16. `l-stationnement-cote` — article manquant**
- Problème : le fait énonce la règle hors agglomération (« autant que possible hors de la chaussée »)
  mais ne cite que R417-1 (agglomération) et R416-12.
- Correction : `source: Code de la route, art. R417-1, R417-4 et R416-12`.
- Source : cdr.txt R417-4 I ; legal-facts F1.

### Vérifications sans remarque (valeurs recoupées une à une dans cdr.txt)

- `l-vitesse-agglo` 50 (R413-3), 70 relevable, zone 30 / zone de rencontre 20 / aire piétonne allure du
  pas (R110-2) ✔ ; `l-vitesse-hors-agglo` 80 depuis le 01/07/2018, 90 par arrêté départemental
  (R413-2 I 3° ; CGCT L3221-4-1) ✔ ; `l-vitesse-separateur-autoroute` 110 / 130 (R413-2 I 1° et 2°) ✔ ;
  `l-vitesse-pluie` 110 / 100 / 80, « les routes à 80 restent à 80 » (R413-2 II, lecture exacte du 3°) ✔ ;
  `l-vitesse-probatoire` 110 / 100 / 80 + disque A (R413-5 I et II) ✔ ;
  `l-vitesse-minimale-autoroute` 80 sur la voie de gauche, 35 € (R413-19, 2e classe) et PL 90 / 80
  (R413-8 1° et 3°) ✔ ; `l-vitesse-engins` 25 / 45 (R311-1, legal-facts A5) ✔ ;
  `l-vitesse-peripherique` 50 depuis le 01/10/2024 alors que R413-3 affiche encore 70 — conforme à la
  règle « valeur en vigueur en réponse, valeur du code en explication » (brief §2.6) ✔.
- `l-stationnement-categories` 35 / 135 / 135 + 3 points / 7 jours + fourrière (R417-9 à R417-12) ✔ ;
  `l-stationnement-5m-passage` 5 m en amont hors emplacements matérialisés, tolérance jusqu'au
  31/12/2026 (R417-11 I 8° c ; CVR L118-5-1) ✔ ; `l-stationnement-alterne` impairs / pairs / 20 h 30-21 h
  (R417-2 II et III), B6a2-B6a3-B6b2 ✔ ; `l-zone-bleue` 35 €, 2e classe (R417-3 V) ✔.
- `l-depassement-laterale` 1 m / 1,50 m, 135 € et 3 points (R414-4 IV, V, VII) ✔ ;
  `l-ligne-continue-sanction` franchir 3 points / chevaucher 1 point (R412-19) ✔ ;
  `l-croisement-largeur` 2 m / 7 m, descendant, place d'évitement au **montant** (R414-2, R414-3 III) ✔ —
  la correction n° 45 de la relecture v1 est bien tenue ; `l-depasse-serrer-droite` 2 points (R414-16) ✔.
- `l-implantation-danger` 150 / 50 / 200 m (IISR ; Q18-Q19 officielles) ✔ ; `l-balises-j10` 3/2/1 bandes
  à 150/100/50 m ✔ ; `l-marquage-modulations` T1 3/10, T3 3/1,33, T4 39/13 — conformes à
  `data/reconnaissance/marquages.yaml` et à legal-facts F7 ✔ ; `l-passage-pieton-50m` 50 m, 6 points
  (R412-37, R415-11) ✔ ; `l-signalisation-hierarchie` agent > feux > panneaux > marquage > règle
  générale (R411-28, R411-25 dernier alinéa) ✔.

---

## 3. `data/affirmations/02_circulation.yaml`

### ERREUR (appliquées)

**17. `aff-l-vehicule-a-stop` — contredit la réponse officielle de la Q2**
- Problème : le `pourquoi` se terminait par « **B conserve la priorité** ». Or la question officielle
  Q2 (exam.md §3.1) attend les réponses **A et C**, c'est-à-dire « A doit céder le passage de chaque
  côté : OUI » **et** « A bénéficie de la priorité de passage par rapport au véhicule B : OUI ».
  La carte, qui se réclame de Q2, disait donc le contraire de la seconde moitié de la question.
- Correction (`pourquoi`) : « Question officielle 2023 (Q2) : le STOP oblige à s'arrêter puis à céder
  le passage à tous les usagers de la route abordée, à gauche comme à droite. Elle répond aussi OUI à
  « A est prioritaire sur B ». »
- Source : exam.md §3.1 Q2 (réponse AC) ; cdr.txt R415-6.

**18. `aff-l-croisement-depasseur-en-face` — article mal attribué**
- Problème : « R412-6 impose de rester maître de son véhicule ». R412-6 impose un « comportement
  prudent et respectueux » (et son III ne sanctionne que le II, position de conduite) ; l'obligation
  de rester maître de sa vitesse est à R413-17 II, et le fait de serrer à droite au croisement à R414-1.
- Correction (`pourquoi` et `source`) : « … R414-1 impose de serrer à droite, R413-17 de rester maître
  de sa vitesse. » ; `source: Code de la route, art. R414-1 et R413-17`.
- Source : cdr.txt R412-6, R413-17 II, R414-1.

**19. `aff-l-demi-tour-ligne-continue` — article hors sujet en source**
- Problème : `source: … R412-19 et R421-6` alors que le contexte est « route à double sens séparée par
  une ligne continue » : R421-6 ne concerne que l'autoroute.
- Correction : `source: Code de la route, art. R412-19 et R412-20` (la ligne mixte, évoquée par la
  solution « attendre une section à ligne discontinue »).
- Source : cdr.txt R412-19, R412-20, R421-6.

### DOUTE (proposés, non appliqués)

**20. `aff-l-3-voies-gauche` ≈ `scn-pos-trois-voies`** — même connaissance (R414-8), même réponse : le
scénario répond déjà « la voie centrale, uniquement si elle est libre dans les deux sens sur toute la
longueur ; jamais la voie la plus à gauche », ce qui couvre exactement le piège de l'affirmation
(« si elle est libre sur toute la longueur »). Doublon au sens du brief §2.8, sans piège distinct.
**Proposition** : supprimer `aff-l-3-voies-gauche` (et garder `aff-l-4-voies-double-sens`, qui porte
une autre configuration), ou déplacer son piège vers « je ne dépasse pas deux véhicules d'affilée ».

**21. `aff-l-c18-priorite` ≈ `scn-crois-c18-je-passe` + `conf-b15-c18`** — la même décision (C18 = je
passe, la flèche rouge désigne celui qui cède) est déjà portée par le scénario **avec l'image du
panneau**, par la carte de confusion et par la reconnaissance `c18`. L'affirmation redécrit le panneau
en mots, ce qui teste une reconnaissance déjà couverte. **Proposition** : supprimer, ou la recentrer
sur un piège non couvert (p. ex. « j'ai le C18, donc je peux m'engager même si un véhicule est déjà
engagé dans le rétrécissement » → FAUX).

**22. `aff-l-bau-appel` ≈ `r-autoroute-bau` (thème R)** — `r-autoroute-bau` répond déjà « s'y arrêter
pour téléphoner ou se reposer est interdit ». Le piège propre de l'affirmation est l'ajout « feux de
détresse allumés » (les warnings ne régularisent aucune immobilisation interdite), qui justifie de la
garder. **Proposition** : la conserver en faisant porter le `pourquoi` sur les feux de détresse plutôt
que sur la destination de la BAU, pour éviter la redite.

**23. `aff-l-surdepassement`** — aucun article n'interdit expressément le surdépassement ; la carte le
fonde sur R414-4 II 1° et 3°, ce qui est une lecture, non une interdiction textuelle. Réponse et
raisonnement restent ceux attendus à l'examen. **Proposition** : laisser, mais ne jamais annoncer de
sanction propre au surdépassement.

**24. `aff-l-klaxon-hors-agglo`** — `sous_theme: positionnement` alors que l'autre carte klaxon
(`aff-l-klaxon-nuit`) est en `depassement` ; les deux routent vers le même sous-deck, l'incohérence est
sans effet. **Proposition** : uniformiser (`depassement` ou un sous-thème `avertisseurs`) lors d'une
prochaine passe.

### Vérifications sans remarque

R415-5 / R415-6 / R415-7 / R415-9 / R415-10 / R415-11 (4 points, 6 points pour le piéton), R412-31
(jaune fixe : arrêt sauf impossibilité, 2e classe, **sans retrait de points**), R412-33, R412-19 al. 2
(cycle / EDPM / cyclomobile léger uniquement), R414-8, R414-11 al. 2 (exceptions R415-6, R415-7,
R415-8, feux, agent), R414-14 + IISR B3 (deux-roues sans side-car dépassables), R414-15, R412-23,
R412-24, R412-26, R412-27, R416-1 à R416-3 (klaxon, appels de phares), R417-1 (sens unique : droite ou
gauche), R417-9 à R417-12 (fourrière dans les quatre régimes), R413-2 I 3° (créneau à 90), R413-2 II +
R413-5 (110 pour tous sous la pluie sur autoroute), R413-3, R413-17, R110-2 (arrêt vs stationnement) —
toutes conformes. L'équilibre vrai/faux (19/29 = 40 %) respecte la fourchette 35-65 % du brief.

---

## 4. Connaissances v1 supprimées : où elles vivent maintenant

Vérification carte par carte des 19 suppressions annoncées dans `docs/research/v2-L.md` §1.
**Aucune connaissance perdue ; aucune carte n'a eu besoin d'être recréée.**

| Id v1 supprimé | Connaissance | Portée aujourd'hui par |
|---|---|---|
| `l-priorite-droite-exceptions` | exceptions à la priorité à droite | Q `l-sortie-parking-priorite` ; AFF `aff-l-chemin-terre`, `aff-l-zone-30-priorite-droite`, `aff-l-priorite-droite-rue-etroite` ; Q `l-insertion-autoroute-priorite` ; `scn-sortie-parking`, `scn-giratoire-cedez`, `scn-rond-point-priorite-droite` |
| `l-vehicules-prioritaires` | prioritaires vs facilités de passage | `u-vehicule-prioritaire-feu-rouge` (R415-12, 135 €/4 pts), `u-ambulance-privee-sans-sirene` (bleu + 2 tons → je cède ; éclats + 3 tons → je facilite), `u-gyrophare-orange`, `u-corridor-securite`, `scn-pompiers-gauche`, `scn-pompiers-face-tourne-gauche` — **règle de décision présente** |
| `l-pieton-priorite` | piéton engagé ou manifestant l'intention | AFF `aff-l-pieton-intention` + fait `l-passage-pieton-50m` (50 m, 6 points) + `scn-feu-vert-pieton` |
| `l-depassement-conditions` (liste) | 3 conditions de R414-4 | Q `l-depassement-conditions` (réécrite) + Q `l-depassement-rabattement` |
| `l-route-3-voies` | 3 voies à double sens | AFF `aff-l-3-voies-gauche`, `aff-l-4-voies-double-sens`, `scn-pos-trois-voies` (cf. DOUTE n° 20) |
| `l-stationnement-tres-genant` | liste des 135 € | fait `l-stationnement-categories` ; Q `l-stationnement-trottoir`, `l-stationnement-bande-cyclable` ; AFF `aff-l-5m-passage`, `aff-l-trottoir-moto` ; `aff-u-place-pmr` |
| `l-stationnement-genant` | liste des 35 € | fait `l-stationnement-categories` ; Q `l-double-file`, `l-entree-carrossable` ; AFF `aff-l-bau-appel`, `aff-l-zone-rencontre-stationnement`, `aff-l-genant-fourriere` |
| `l-feu-rouge-clignotant` | **arrêt absolu** devant un rouge clignotant | `feu-rouge-clignotant` (reconnaissance) : « Un ou deux feux rouges alternés : arrêt absolu — PN, pont mobile, sortie de pompiers, tram », conduite « s'arrêter avant le feu et attendre son extinction » — **règle de décision présente** |
| `l-feu-vert-conditions` | le vert ne prime pas sur tout | AFF `aff-l-feu-vert-priorite` + `feu-vert` (reconnaissance) + Q `l-intersection-encombree` |
| `l-cedez-vs-stop` | arrêt obligatoire ou non | AFF `aff-l-stop-rien-ne-vient`, `aff-l-cedez-arret` ; `conf-ab3a-ab4`, `conf-stop-cedez-lignes` |
| `l-depassement-cycliste-ligne-continue` | chevauchement pour un cycle | `scn-dep-cycliste-ligne-continue` + AFF `aff-l-continue-cyclomoteur` (l'exception ne vaut pas pour un cyclomoteur) + fait `l-depassement-laterale` |
| `l-depassement-vehicule-tourne-gauche` | dépasser par la droite | `scn-dep-vehicule-tourne-gauche` + Q `l-depassement-droite` + fait `l-depasse-serrer-droite` |
| `l-ligne-jaune-sens` | **lignes jaunes** | `marq-ligne-jaune-continue` (arrêt ET stationnement interdits, = B6d), `marq-ligne-jaune-discontinue` (stationnement interdit, arrêt autorisé, = B6a1), `marq-ligne-jaune-zigzag` (arrêt de bus) + AFF `aff-l-ligne-jaune-discontinue` — **règle de décision présente** |
| `l-feu-jaune-fixe` | **arrêt sauf impossibilité en sécurité** | `feu-jaune-fixe` (reconnaissance) : « arrêt obligatoire, sauf si l'on ne peut plus s'arrêter dans des conditions de sécurité suffisantes » + AFF `aff-l-jaune-accelerer` / `aff-l-jaune-trop-engage` — **présente** (la durée 3 s / 5 s, non sourcée, disparaît : conforme à la relecture v1 n° 28) |
| `l-feu-jaune-clignotant` | **prudence + panneaux, sinon priorité à droite** | `feu-jaune-clignotant` (reconnaissance) : « les feux ne règlent plus l'intersection, on applique les panneaux ou, à défaut, la priorité à droite » + `scn-feu-orange-clignotant` + Q `l-feu-hors-service-panneaux` — **présente** |
| `l-feu-fleche-jaune` | **flèche jaune clignotante = cédez-le-passage dans la direction** | `r16` : « les usagers allant dans cette direction peuvent passer, même au rouge, **sans aucune priorité** ; céder aux piétons et aux véhicules qui ont le vert », piège « flèche JAUNE = je cède / flèche VERTE (R14) = passage protégé » — **présente** |
| `l-feux-bus-tram` | **feux à barres des bus** | `r17` : « barre verticale = passage, disque = arrêt imminent, barre horizontale = arrêt », conduite « se méfier d'un bus dont la barre est verticale : il va passer » — **présente** |
| `l-signaux-affectation-voies` | **signaux d'affectation de voies** | `r21a` (croix rouge = voie interdite, la quitter), `r21b` (flèche verte = voie ouverte), `r21c` (flèche jaune oblique clignotante = se rabattre du côté indiqué) — **présente** ; la source est bien « IISR 6e partie » (correction v1 n° 29 sans objet) |
| `l-agent-bras-leve` | arrêt pour tous sauf déjà engagés | `agent-bras-leve` + `scn-agent-bras-leve` |
| `l-agent-bras-tendus` | face/dos = arrêt, profil = passage | `agent-bras-tendu-face`, `agent-profil`, `scn-agent-bras-tendus-face`, `scn-agent-bras-tendus-profil` |

Le geste « ralentir » (balancement du bras de haut en bas) n'est couvert par aucune carte de
reconnaissance : il est bien conservé en question (`l-agent-ralentir-avancer`, image `agent`
pose `ralentir`), et le geste d'appel l'est par `agent-geste-avancer`. Rien à recréer.

---

## 5. Points restant à arbitrer (récapitulatif)

1. Croisement de deux tourne-à-gauche : « par la droite » (knowledge-facts, R414-1) vs « par la
   gauche » (`docs/02-carte-des-connaissances.md` L4) — n° 13.
2. Doublons `aff-l-3-voies-gauche` / `scn-pos-trois-voies` et `aff-l-c18-priorite` /
   `scn-crois-c18-je-passe` — n° 20 et 21.
3. « Route à accès réglementé = 110 » : convention d'examen plutôt que règle de R413-2 — n° 12.
4. Qualification de l'**arrêt** (et non du stationnement) en double file — n° 10.
5. legal-facts F8 range R416-19 en « 2e classe » ; cdr.txt dit 4e classe (n° 14) : le dossier
   `legal-facts.md` mériterait d'être corrigé, hors de mon périmètre.
6. La relecture v1 n° 5 (B6b3 pour le stationnement alterné) est erronée : c'est B6b2.
