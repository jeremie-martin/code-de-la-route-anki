# Relecture contradictoire — thème U « Les autres usagers » (v2)

Périmètre : `data/questions/05_autres_usagers.yaml` (34 notes), `data/faits/05_autres_usagers.yaml`
(8 notes), `data/affirmations/05_autres_usagers.yaml` (32 notes à la relecture, 31 après suppression
d'un doublon). **74 notes relues**, une par une, chaque valeur juridique retrouvée dans
`docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026), les autres dans `legal-facts.md`,
`knowledge-facts.md` et `exam.md` §3.1.

**Bilan : 7 ERREUR · 8 STYLE · 6 DOUTE** (+ 1 contradiction hors périmètre, § final).
Les ERREUR et les STYLE sont **appliquées** ; les DOUTE sont seulement proposées.
Après corrections : `python -m build.build --check | grep 05_autres` ne renvoie rien, les trois
fichiers se chargent (34 / 8 / 31 notes), aucune réponse > 40 mots, aucun `pourquoi` > 45 mots,
équilibre des affirmations 13 vrai / 31 = **41,9 %**.
Les notes sans remarque ne sont pas listées.

---

## data/questions/05_autres_usagers.yaml

**1. `u-pieton-hors-agglo-cote`** — ERREUR (appliquée)
- Problème : l'explication disait « Un cortège **ou un groupe organisé** marche à droite (R412-42) ».
  R412-42 **I** met à droite les *cortèges, convois ou processions* ; le **II** vise les *groupements
  organisés*, auxquels les règles de la section ne s'appliquent pas et qui, **en colonne par un et hors
  agglomération, se tiennent au bord gauche** — exactement l'inverse.
- Correction : « Un cortège, un convoi ou une procession marche à droite, en laissant libre toute la
  moitié gauche (R412-42). »
- Source : cdr.txt, R. 412-42 I et II.

**2. `u-cycliste-bras-gauche`** — ERREUR (appliquée)
- Problème : « R414-6 : on dépasse par la droite un usager qui a signalé qu'il va à gauche, **si la place
  suffit** ». La condition d'intervalle suffisant appartient au **II 2°** (véhicule sur rails) ; le
  **II 1°** (usager se portant à gauche) impose le dépassement par la droite sans condition. Le
  rapport v2-U §3.2 annonçait cette correction, elle n'avait été appliquée qu'à moitié.
- Correction : « R414-6 II 1° : un usager qui a signalé qu'il se porte à gauche se dépasse par la droite,
  jamais par la gauche ; dans le doute, j'attends. »
- Source : cdr.txt, R. 414-6 II ; cohérent avec `faits/02_circulation` (« ou un tramway (par la droite si
  la place suffit) »), où la condition est correctement rattachée au tramway.

**3. `u-tram-depasser`** — ERREUR (appliquée)
- Problème : l'explication contredisait la réponse. Le recto pose des voyageurs qui descendent **de mon
  côté** (donc à droite), et l'explication enchaînait « S'il n'y a pas de quai et que la place suffit
  **de l'autre côté**, on le dépasse **par la droite** au pas (R414-6) » — incohérent, et « au pas »
  n'est dans aucun texte.
- Correction : « En marche, un tramway se dépasse par la droite si l'intervalle jusqu'au bord de la
  chaussée suffit (R414-6 II 2°). Le tram ne peut ni dévier ni freiner court. »
- Source : cdr.txt, R. 414-13 (interdiction côté montée/descente) et R. 414-6 II 2° ;
  knowledge-facts U6.

**4. `u-convoi-exceptionnel`** — ERREUR (appliquée)
- Problème : « Les véhicules d'accompagnement ont autorité pour régler la circulation du convoi
  (**R433-17**) ». R433-17 ne fait que *définir* les véhicules de protection et de guidage ; l'opposabilité
  de leurs indications (et la sanction) est à **R433-2 III** (« contrevenir aux indications des conducteurs
  de véhicules de guidage […] 4e classe »).
- Correction : explication → « Ne pas suivre les indications d'un véhicule de guidage : 135 €
  (R433-2 III). Un convoi engagé dans une intersection garde la priorité (R412-33). » ;
  `source` → « Code de la route, art. R433-17, R433-2 III et R412-33 ».
- Source : cdr.txt, R. 433-2 III et R. 433-17.

**5. `u-zone-rencontre-pietons`** — STYLE (appliquée)
- Problème : « Je roule **au pas** derrière lui […] (20 km/h maximum) » mettait sur le même plan l'allure
  du pas (qui est la règle de l'**aire piétonne**, rappelée deux lignes plus bas) et les 20 km/h de la zone
  de rencontre — confusion exactement inverse du but de la carte.
- Correction : « Je le suis à son allure, sans klaxonner : en zone de rencontre (20 km/h maximum), … ».
- Source : R110-2 ; knowledge-facts U1 (l'allure du pas n'est pas chiffrée par le code).

**6. `u-enfants-sortie-ecole`** — STYLE (appliquée)
- Problème : « je ne le dépasse qu'**au pas** » va au-delà de R413-17 III 3°, qui n'impose qu'une vitesse
  réduite (knowledge-facts U6 : « Pas d'interdiction légale de dépasser : règle pédagogique »).
- Correction : « je ne le dépasse qu'**à très faible vitesse**, avec une extrême prudence ».
- Source : cdr.txt, R. 413-17 III 3°.

**7. `u-cycliste-tourner-droite`** — STYLE (appliquée)
- Problème : `source` citait **R415-4**, qui régit le conducteur *quittant une route sur sa gauche* ; la
  carte porte sur un virage à **droite**. Rien ne sourçait le « Même conduite avec une bande cyclable » de
  l'explication.
- Correction : `source` → « Code de la route, art. R415-14 (piste cyclable) et R415-13 (voie réservée) »
  (R415-13 : aux intersections, les règles de priorité s'imposent à tous sur une chaussée comportant une
  voie ou bande réservée).
- Source : cdr.txt, R. 415-13 et R. 415-14.

**8. `u-interfiles`** — STYLE (appliquée)
- Problème : l'explication datait le texte « Décret 2025-33 (**11 janvier 2025**) » alors que le champ
  `source` de la même carte dit « décret n° 2025-33 du **9 janvier 2025** » : contradiction interne. Le
  9 janvier est la date du décret, le 11 janvier celle de la généralisation (legal-facts E10).
- Correction : « Décret 2025-33, **en vigueur le 11 janvier 2025** : … ».
- Source : cdr.txt (« Décret n°2025-33 du 9 janvier 2025 ») ; legal-facts E10.

**9. `u-pl-insertion-autoroute`** — STYLE (appliquée)
- Problème : `source` citait **R414-2**, qui impose au contraire au véhicule *encombrant* (> 2 m ou > 7 m)
  de s'effacer devant les véhicules plus petits lorsque le croisement est difficile : il ne fonde pas le
  geste de faciliter l'insertion d'un poids lourd.
- Correction : `source` → « Code de la route, art. R421-3 ; coursdecode — Les poids lourds ».
- Source : cdr.txt, R. 414-2 et R. 421-3.

## data/faits/05_autres_usagers.yaml

**10. `u-pl-angles-morts-chiffres`** — ERREUR (appliquée)
- Problème : « Les autocollants sont apposés **à l'avant**, à l'arrière et sur les côtés du véhicule. »
  R313-32-1 impose la signalisation « visible **sur les côtés ainsi qu'à l'arrière** du véhicule » —
  l'avant n'y figure pas.
- Correction : « Les autocollants sont apposés sur les côtés et à l'arrière du véhicule (R313-32-1). » ;
  `source` → « … Code de la route, art. R313-32-1 et R412-12 ».
- Source : cdr.txt, R. 313-32-1 (décret n° 2020-1396) ; L. 313-1.

## data/affirmations/05_autres_usagers.yaml

**11. `aff-u-tram-priorite-droite`** — ERREUR / doublon (**carte supprimée**)
- Problème : la même connaissance (« le tramway est prioritaire même venant de gauche, la priorité à droite
  ne lui est pas opposable ») est déjà testée **trois fois** dans le deck : `r-tram-priorite`
  (`questions/04_route`, énoncé quasi identique : « Un tramway arrive sur ma gauche à un croisement sans
  feu ni panneau. Qui passe ? »), `scn-tram-gauche` (`scenarios/priorites`, même situation avec image) et
  `scn-tram-droite-moi-prioritaire` (`scenarios/priorites2`). Aucun piège distinct — brief §2.8.
- Correction : carte supprimée. Aucune connaissance perdue ; le sous-thème `transports_commun` de U garde
  `u-tram-depasser`, `u-voie-bus` et `aff-u-bus-hors-agglo`. Équilibre vrai/faux après suppression :
  13/31 = 41,9 % (dans la fourchette 35-65 %).

**12. `aff-u-edpm-gilet-agglo`** — ERREUR (appliquée)
- Problème : le contexte est « de nuit, dans une **rue éclairée** », le verdict est VRAI, mais le `pourquoi`
  justifiait par « partout **dès que la visibilité est insuffisante** » — un lecteur en conclut que la rue
  éclairée dispense, ce qui contredit le verdict. R412-43-3 II impose l'équipement « lorsqu'il circule **la
  nuit**, ou le jour lorsque la visibilité est insuffisante » : la nuit, sans condition d'éclairage.
- Correction : « Le cycliste ne porte le gilet que hors agglomération ; l'utilisateur d'EDPM, lui, doit un
  gilet ou un équipement rétro-réfléchissant partout, **la nuit ou de jour par visibilité insuffisante**
  (35 €). » (au passage, la mention « hors agglomération **la nuit** » pour le cycliste amputait R431-1-1,
  qui vise aussi le jour par visibilité insuffisante).
- Source : cdr.txt, R. 412-43-3 II et R. 431-1-1 ; legal-facts E8.

**13. `aff-u-pieton-nuit-croisement`** — STYLE (appliquée)
- Problème : « à 90 km/h la seule **distance de freinage dépasse 50 m** ». Valeur en désaccord entre
  sources : les chiffres Sécurité routière (7 m/s²) donnent ≈ 45 m à 90 km/h, la formule « dizaines au
  carré » 81 m. legal-facts A6 conclut explicitement « **ne pas faire de carte sur la valeur exacte**,
  seulement sur […] l'ordre de grandeur ».
- Correction : « … n'éclairent qu'environ 30 m, bien moins que la distance d'arrêt à 90 km/h : de nuit, on
  ne s'arrête plus dans la zone éclairée. » (concept de « surconduite », knowledge-facts R1, non chiffré).
- Source : legal-facts A6 ; knowledge-facts R1.

**14. `aff-u-place-pmr`** — STYLE (appliquée)
- Problème : « qui y stationnent gratuitement **et sans limite de durée** ». La commune peut fixer une
  durée maximale, qui ne peut être inférieure à 12 h (SP F2891, knowledge-facts U8).
- Correction : « … qui y stationnent gratuitement (durée limitable par la commune, mais au moins 12 h) ».
- Source : knowledge-facts U8 ; service-public.fr F2891.

**15. `aff-u-velo-bande-obligatoire`** — STYLE (appliquée)
- Problème : « Une trottinette électrique, elle, doit la prendre **dès qu'elle existe** » : l'obligation de
  R412-43-1 **I** ne vaut qu'**en agglomération** ; hors agglomération, un EDPM n'a pas accès à une bande
  cyclable du tout (II : voies vertes et pistes cyclables seulement).
- Correction : « … doit prendre la bande ou la piste **en agglomération** dès qu'elle existe ».
- Source : cdr.txt, R. 412-43-1 I et II.

---

## DOUTE (proposés, non appliqués)

**D1. `u-matieres-dangereuses`** — la puce correspondante de `knowledge-facts.md` U5 est marquée
« À VÉRIFIER (exemple d'une seule source) », et le brief §2.7 interdit de porter sur une carte une valeur
ainsi marquée. Le contenu est exact (accord ADR : code danger en haut, n° ONU en bas) et n'apparaît que
dans l'**explication**, la réponse se limitant à « matières dangereuses → distance accrue, signaler la
plaque aux secours ». *Proposition* : soit ajouter une source officielle (arrêté TMD / ADR, partie 5.3),
soit retirer de l'explication le détail « code danger en haut, numéro de la matière en bas ». Carte laissée
telle quelle (`importance: utile`).

**D2. `aff-u-pl-distance-arret`** — « À vitesse égale, un poids lourd chargé a besoin d'une distance
d'arrêt nettement plus longue qu'une voiture » est vrai mais **évident pour un adulte non conducteur**
(brief §5). *Proposition* : la resserrer sur le geste testé à l'examen, p. ex. contexte « Je viens de
dépasser un poids lourd sur autoroute » + affirmation « Je peux me rabattre dès que je le vois entier dans
mon rétroviseur intérieur » (FAUX). Non appliqué : c'est une réécriture, pas une correction.

**D3. Quasi-doublons à arbitrer entre thèmes** (aucun n'est faux, aucun n'a été touché) :
- `u-cycliste-bras-gauche` (U) et `c-indice-cycliste-regard` (`questions/03_conducteur`) portent sur le même
  indice ; l'explication de U le dit elle-même (« Un regard par-dessus l'épaule gauche annonce la même
  chose »). *Proposition* : supprimer cette phrase de U, ou l'assumer explicitement.
- L'explication de `u-double-sens-cyclable` (« la règle par défaut dans les zones 30 […], **même sans
  panonceau** ») donne littéralement la réponse de `aff-u-velo-double-sens-zone30`. *Proposition* : raccourcir
  l'explication de la question à « il vaut aussi pour les trottinettes électriques ».
- `aff-u-velo-bande-obligatoire` recouvre `conf-b22a-c113` (confusions/signalisation) ; voisinage assumé par
  le rapport v2-U, la mise en situation « je suis à vélo » justifie la seconde forme.
- `aff-u-pieton-nuit-croisement` (U) et le verso de `aff-c-pieton-detectable-motard`
  (`affirmations/03_conducteur` : « De nuit, un piéton sombre n'est vu qu'à 30 m, 150 m avec un gilet »)
  disent la même chose ; la carte U est la forme testable, la mention de C est un verso. Acceptable.

**D4. `u-motos-mortalite`** — le « × 27 » est marqué « À VÉRIFIER » dans knowledge-facts U4 (« retenir
environ 20 à 30 fois ; chiffre officiel SR = 27 »). La carte l'écrit « **environ** 27 fois » et donne la
fourchette en explication : la nuance exigée par le brief §2.7 est présente. Seul écart : l'explication dit
« 20 à 30 fois » là où le dossier écrit « 20 à 32 fois ». *Proposition* : aligner sur « 20 à 32 fois ».

**D5. `u-voie-bus`** — « Non, **sauf pour la traverser au dernier moment** en cédant le passage aux bus ».
R412-7 II interdit la circulation sur la voie réservée sans prévoir cette exception, qui est une règle
pédagogique (et dépend du marquage : franchissement impossible sur ligne continue). *Proposition* :
ajouter « si le marquage est discontinu » dans la réponse, ou basculer la tolérance en explication.
Le reste de la carte est exact (135 €, R417-11 ; damier blanc = traversée de voie bus, legal-facts F7).

**D6. `u-pieton-canne-blanche`** — knowledge-facts U1 marque la règle « s'arrêter pour une canne blanche »
comme « À VÉRIFIER (pas d'article dédié) ». La carte la rattache correctement à R415-11 + R412-6, ce qui
est la lecture du dossier lui-même. Aucune correction proposée ; signalé pour mémoire.

## Doutes du rédacteur (`v2-U.md` §6) — tranchés

- **§6.1 Priorité du tramway sous R422-3** — l'exception du I (« à l'exception des véhicules de transport
  public […] **dont les conducteurs doivent respecter les signalisations comportant des prescriptions
  absolues** et les indications des agents ») ne retire pas la priorité au tram : elle l'assortit de
  l'obligation d'obéir aux prescriptions absolues. La formulation retenue par le deck (« prioritaire sauf
  signalisation contraire », `r-tram-priorite`, `scn-tram-gauche`) est la bonne lecture. **Rien à changer.**
- **§6.2 Plaque orange** — voir D1 : conservé, avec réserve de sourçage.
- **§6.3 Allure du pas** — aucune carte de U ne la chiffre, ce qui est correct ; la seule ambiguïté
  (`u-zone-rencontre-pietons`, qui semblait assimiler l'allure du pas aux 20 km/h) est levée par la
  correction n° 5. **Résolu.**
- **§6.4 Casque EDPM** — les cartes s'en tiennent à la règle nationale (recommandé ; obligatoire hors
  agglomération sur les routes ouvertes par dérogation, R412-43-1 IV 1° a), les arrêtés locaux « À VÉRIFIER »
  de legal-facts E8 ne sont pas repris. **Conforme, rien à changer.**
- **§6.5 Survie du piéton selon la vitesse** — aucune carte ne reprend ces chiffres. **Conforme.**
- **§6.6 `aff-u-velo-ecouteurs`** — R412-6-1 vise « tout conducteur d'un véhicule en circulation », 4e classe
  (135 €), 3 points ; le cycliste est bien un conducteur de véhicule, et l'absence de retrait tient à
  l'absence de permis. Le verso le dit exactement. **Conforme.**

## Contradiction hors périmètre (non corrigée — autre fichier)

**`l-depassement-interdit-lieux-2`** (`data/questions/02_circulation.yaml`) énumère parmi les lieux où le
dépassement est interdit « un tramway **ou un bus** arrêté côté voyageurs ». R414-13 ne vise que « un train
ou un véhicule de transport public assujetti à suivre, de façon permanente, une trajectoire déterminée par
un ou des rails matériels » : un autobus ou un autocar n'est **pas** concerné (knowledge-facts U6 : « Pas
d'interdiction légale de dépasser » un bus, « règle pédagogique »). Cette carte **contredit frontalement**
`aff-u-car-scolaire-depassement` (thème U, verdict FAUX, « L'interdiction vise le tramway ou le train à
l'arrêt côté voyageurs »). À corriger par le relecteur du thème L : retirer « ou un bus », ou écrire
« un tramway ou un train à l'arrêt côté voyageurs ». Source : cdr.txt, R. 414-13.
