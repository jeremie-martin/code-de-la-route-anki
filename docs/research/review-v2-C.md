# Relecture contradictoire — thème C « Le conducteur » (v2)

Périmètre : `data/questions/03_conducteur.yaml` (25 notes), `data/faits/03_conducteur.yaml` (21 notes),
`data/affirmations/03_conducteur.yaml` (42 notes). **88 notes relues, ligne à ligne.**

Référentiels interrogés : `docs/research/sources/cdr.txt` (code consolidé au 10/09/2026 — articles
R. 412-6-1, R. 412-6-2, R. 412-10, R. 412-11, R. 412-12, R. 413-17, R. 414-4, R. 416-1, R. 416-20,
R. 221-1-1, R. 234-1, L. 224-1 relus dans le texte), `docs/research/exam.md` §3.1 (les 20 questions
officielles verbatim) et §4.3, `docs/research/legal-facts.md` A6, B1-B7, G1-G3, H2-H4, J2-J3,
`docs/research/knowledge-facts.md` C1-C14 et U1, `docs/research/review-facts-questions.md` (n° 7-14,
34-40), `docs/research/brief-v2-redaction.md`, `docs/05-audit-v2.md`, `docs/research/v2-C.md`.

| Sévérité | Nombre | Dont appliqués |
|---|---|---|
| **ERREUR** | 3 | 3 |
| **DOUTE** | 8 | 0 (proposés ci-dessous) |
| **STYLE** | 12 | 12 |
| **Total** | **23** | **15 notes modifiées** |

Aucune carte supprimée. Aucun id modifié. `python -m build.build --check` ne signale rien sur les
trois fichiers ; les trois YAML se chargent (25 / 21 / 42 notes) ; équilibre des affirmations
inchangé : 20 vrai / 22 faux (47,6 %).

Contrôles menés sans remarque : conformité aux questions officielles **Q3, Q4, Q7, Q9, Q11, Q12, Q13,
Q17, Q20** (après corrections n° 4 et 9 ci-dessous) ; maintien des corrections de la relecture v1
n° 7, 8, 9, 10, 11, 12, 13 (faits) et 34, 35, 36, 37, 38, 39 (questions) — **toutes toujours
appliquées** ; sanctions et classes d'amende (R412-6-1 : 4e classe, 3 points ; R412-6-2 : 5e classe,
3 points, confiscation ; R234-1 : 0,20 g/L = 0,10 mg/L, 4e classe, **6 points** ; R221-1-1 VI :
3 points ; R412-12 V/VII : 4e classe, 3 points ; R414-4 IV : 1 m / 1,50 m) ; absence de doublon de
chiffre avec `data/faits/02_circulation.yaml` (`l-depassement-laterale`) et
`data/faits/06_reglementation.yaml` (téléphone, AAC, probatoire).

---

## 1. `data/questions/03_conducteur.yaml`

**1. `c-indice-feux-recul` — ERREUR (appliquée)**
- Problème : l'explication écrivait « Celui qui quitte un stationnement doit certes **céder le passage
  (R412-10)** ». L'article R. 412-10 n'impose pas de céder le passage : il impose d'**avertir** les
  autres usagers avant un changement de direction, un ralentissement ou « lorsque, après un arrêt ou
  stationnement, il veut reprendre sa place dans le courant de la circulation ». Aucun article du code
  ne fonde un « cédez-le-passage » pour la sortie d'un stationnement en bord de chaussée (R415-9 vise
  les chemins de terre et propriétés riveraines).
- Correction appliquée : « … doit **avertir de son intention (R412-10) et céder le passage**, mais
  l'ETG attend que j'anticipe. »
- Source : `cdr.txt` l. 20609-20620 (R. 412-10) ; `questions/08_prendre_quitter.yaml` (Q14 officielle,
  même formulation sans article cité).

**2. `c-indice-vehicule-stationne-portiere` — ERREUR (appliquée)**
- Problème : l'explication affirmait « à 30 km/h, la distance d'arrêt est environ **deux fois** plus
  courte qu'à 50 ». Contradiction interne avec `c-distance-arret-formule`, qui pose la convention
  d'auto-école (dizaines)² : 30 km/h → 9 m, 50 km/h → 25 m, soit **≈ 2,8 fois**. Le rapport « 2 » n'est
  vrai que sous la convention Sécurité routière (13 m / 28 m), non retenue en réponse dans le deck.
- Correction appliquée : « … la distance d'arrêt est **bien plus courte** qu'à 50 » (le chiffre reste
  dans le seul fait qui le porte).
- Source : `c-distance-arret-formule` ; knowledge-facts C4 ; legal-facts A6.

**3. `c-zone-attention-pluie` — STYLE (appliquée)**
- Problème : le recto décrivait « le rétroviseur » et « des piétons près d'**un passage** à droite ».
  La Q9 officielle encadre trois zones : A = **rétroviseur gauche**, B = voiture au loin, C = piétons
  **et voiture** à droite ; aucun passage piéton n'y figure. Le recto ne doit pas ajouter d'élément
  absent de la question officielle qu'il prétend reproduire.
- Correction appliquée : recto « entre le rétroviseur **gauche**, **une voiture** au loin devant et des
  piétons à droite… » ; réponse « Sur les piétons, à droite : … ».
- Source : exam.md §3.1 Q9.

**4. `c-enfant-masque` — STYLE (appliquée)**
- Problème : l'explication listait « ballon, cartables, sortie d'école » (déjà l'objet de
  `c-indice-ballon`) et « Jamais “je klaxonne” » (déjà l'objet de `aff-c-klaxon-ecole`) : double
  redondance interne au thème.
- Correction appliquée : indices propres à la situation (« sortie d'école, adultes qui attendent, car
  scolaire : autant d'indices qui imposent d'arriver déjà lent »), Q3 conservée mot pour mot.
- Source : brief §2 règle 8 ; exam.md §3.1 Q3.

**5. `c-cycliste-devant-depassement` — STYLE (appliquée)**
- Problème : explication de ~60 mots (brief §2 règle 9 : « une ligne utile »).
- Correction appliquée : resserrée, **sans perdre** le contenu imposé par la correction v1 n° 35
  (Q7 sans énoncé ; le « véhicule en face » est une interprétation de la photo).
- Source : exam.md §3.1 Q7 et §3.3 ; review-facts-questions n° 35.

**6. `c-indice-bus-arrete` — STYLE (appliquée)**
- Problèmes : (a) « on doit **faciliter la sortie** d'un bus » est la formule floue que legal-facts J2
  signale comme source de confusion avec une prétendue « priorité du bus » ; R412-11 dit « ralentir si
  nécessaire et au besoin s'arrêter pour laisser les véhicules de transport en commun quitter les
  arrêts signalés comme tels » ; (b) la phrase sur le car scolaire aux feux de détresse duplique
  `u-enfants-sortie-ecole` (`questions/05_autres_usagers.yaml`, R413-17 III 3°) ; (c) `source` citait
  R413-17 pour un contenu qui n'y reste plus.
- Correction appliquée : explication réécrite sur le texte de R412-11 (« ce n'est pas une priorité du
  bus, c'est une obligation pour moi ») ; renvoi au car scolaire supprimé ; `source` ramenée à R412-11.
- Source : `cdr.txt` l. 20622-20628 (R. 412-11) ; legal-facts J2 ; `questions/05_autres_usagers.yaml`.

**7. `c-routine-monotonie` — STYLE (appliquée)**
- Problème : l'explication répétait « Environ **75 %** des accidents mortels surviennent près du
  domicile », qui est le cloze `c2` de `c-nuit-risque` (en-tête du fichier de faits : « un chiffre vit
  ici et nulle part ailleurs dans le thème »).
- Correction appliquée : chiffre retiré, remplacé par « surtout sur le trajet fait tous les jours » ;
  la réponse garde la formulation qualitative « la plupart des accidents mortels ».
- Source : brief §2 règle 8 ; `c-nuit-risque` ; knowledge-facts C13.

**8. `c-telephone-arret` — STYLE (appliquée)**
- Problèmes : (a) la réponse posait deux conditions non sourcées, « **moteur coupé** » et « sauf panne
  ou urgence sur la **BAU** » (cette dernière se lisait comme une exception à l'exception) ; le critère
  des dossiers est « être **garé sur un emplacement où l'arrêt/stationnement est autorisé** » ;
  (b) l'explication s'appuyait sur un arrêt de la Cour de cassation absent de tous les dossiers et
  écrivait « suspension possible si l'infraction est combinée à une autre », alors que le mécanisme est
  la **rétention immédiate** du permis (L224-1 I 7° : téléphone tenu en main établi *simultanément*
  avec une infraction de vitesse, croisement, dépassement, intersection ou priorité), puis suspension —
  c'est aussi ce que dit `faits/06_reglementation.yaml`.
- Correction appliquée : réponse recentrée sur « garé sur un emplacement où l'arrêt est autorisé » ;
  explication réécrite sur R412-6-1 (135 €, 3 points) + L224-1 I 7° ; `source` mise à jour.
- Source : `cdr.txt` l. 20470-20484 (R. 412-6-1) et l. 2188-2225 (L. 224-1) ; knowledge-facts C1 ;
  legal-facts G1.

**9. `c-cannabis-effets` — STYLE (appliquée)**
- Problème : l'explication reprenait mot pour mot les multiplicateurs (×1,65-1,8, ×29, ×15) qui sont
  les clozes et l'explication de `c-stupefiants-stats` : doublon de chiffres à l'intérieur du thème.
- Correction appliquée : explication recentrée sur ce que la question n'a pas (« Aucun seuil : toute
  trace détectée constitue le délit — L235-1 : 3 ans, 9 000 €, 6 points »), valeurs post-loi 2025-622.
- Source : legal-facts B4 ; brief §2 règle 8.

## 2. `data/faits/03_conducteur.yaml`

**10. `c-stupefiants-stats` — ERREUR (appliquée)**
- Problème : le cloze `{{c2::2}}` était immédiatement suivi, en texte non masqué, de « (1,65 à 1,8) » :
  la carte donnait sa propre réponse. C'est précisément le défaut que `05-audit-v2.md` §2.7 fait
  contrôler par le build (« clozes qui se soufflent la réponse »).
- Correction appliquée : la fourchette passe dans l'explication (« Valeurs Sécurité routière : cannabis
  ×1,65 — ×1,8 dans certains QCM ; alcool + cannabis ×29 — ×15 dans les anciens films »), le cloze
  reste « près de 2 ».
- Source : 05-audit-v2 §2.7 ; legal-facts B4 et J2 ; knowledge-facts C7.

**11. `c-intervalle-pl-tunnel` — STYLE (appliquée)**
- Problème : « les véhicules de plus de 3,5 t (**ou ensembles** de plus de 7 m) » : R412-12 II applique
  les deux critères (PTAC > 3,5 t **ou** longueur > 7 m) aux « véhicules **ou** ensembles de
  véhicules » — le critère des 7 m n'est pas réservé aux ensembles.
- Correction appliquée : « les véhicules **ou ensembles** de plus de 3,5 t (ou de plus de 7 m de long) ».
- Source : `cdr.txt` l. 20706-20724 (R. 412-12 II).

**12. `c-telephone-5s` — STYLE (appliquée)**
- Problème : cloze `{{c4::23}}` rattaché au seul fait « **en écrivant** un message » ; les deux dossiers
  attribuent le ×23 à la **lecture ou à l'écriture** d'un SMS (legal-facts G1 : « lire un message
  × 23 »).
- Correction appliquée : « … par 23 **en lisant ou en écrivant** un message ».
- Source : legal-facts G1 ; knowledge-facts C1.

## 3. `data/affirmations/03_conducteur.yaml`

**13. `aff-c-intervalle-pluie-nuit` — STYLE (appliquée)**
- Problème : « Deux secondes sont le minimum légal **par temps sec** (R412-12) » — R412-12 I ne
  conditionne pas son minimum à la météo ; la rédaction laissait croire que le minimum légal change
  sous la pluie (c'est R413-17 III 4°/5° qui impose alors de réduire l'allure).
- Correction appliquée : « Deux secondes sont le minimum légal (R412-12) **et ce minimum suppose une
  chaussée sèche**. »
- Source : `cdr.txt` l. 20706-20712 (R. 412-12 I) ; l. 21696-21725 (R. 413-17 III).

**14. `aff-c-lendemain-matin` — STYLE (appliquée)**
- Problème : le `pourquoi` affirmait « **il reste** 0,5 g/L ou plus à 8 h ». L'arithmétique ne le
  garantit pas sur toute la fourchette annoncée : 1,00 g/L au pic vers 3 h, éliminé à 0,15 g/L/h,
  donne 0,25 g/L à 8 h. L'affirmation, elle, dit « je **peux** encore être au-dessus » (VRAI).
- Correction appliquée : « **il peut rester** 0,5 g/L ou plus à 8 h ».
- Source : legal-facts B5 (élimination 0,10-0,15 g/L/h ; verre standard +0,20 à 0,25 g/L).

**15. `aff-c-aac-accidents` — STYLE (appliquée)**
- Problème : le `pourquoi` reprenait « 76 % contre 60 % » et « assurance moins chère », qui sont le
  contenu de `faits/06_reglementation.yaml` (thème D, AAC) ; de plus le taux de réussite à l'examen est
  hors sujet pour une affirmation portant sur l'**accidentalité**.
- Correction appliquée : `pourquoi` recentré sur le surrisque du novice et sur les 3 000 km/1 an
  d'expérience accompagnée ; la période probatoire réduite à 2 ans est conservée comme conséquence.
- Source : knowledge-facts C10/C11 ; `faits/06_reglementation.yaml` ; brief §2 règle 8.

---

## 4. DOUTES — proposés, non appliqués

**D1. `c-ordre-controles-changement-file` (question) — ordre clignotant / angle mort.**
La réponse impose une des deux écoles (rétro intérieur → rétro gauche → clignotant → angle mort).
knowledge-facts C12 marque ce point « **À VÉRIFIER** (deux écoles) » : Codeclic/Ornikar donnent cet
ordre, Stych et de nombreux moniteurs donnent rétros → angle mort → clignotant. Or le brief §2 règle 7
dit qu'« une valeur marquée “À VÉRIFIER” dans un dossier ne va pas sur une carte ». Aucune des vingt
questions officielles ne teste cet ordre.
*Proposition* : ne garder en réponse que le noyau certain — « les rétroviseurs d'abord (intérieur puis
extérieur du côté visé), l'angle mort en **dernier** regard avant de tourner le volant, le clignotant
entre les deux ; déport progressif à vitesse constante » — et laisser la divergence en explication (où
elle est déjà). *Source* : knowledge-facts C12 ; exam.md §3.1.

**D2. `c-stupefiants-stats` c3 = 29 et `c-cannabis-effets` — « alcool + cannabis ×29 ».**
Les deux dossiers divergent : legal-facts B4 **et** H4 attribuent explicitement « cannabis + alcool :
× 29 » à la page SR « La drogue et la conduite » (vérifié 2026-09-21), alors que knowledge-facts C6
marque la valeur « À VÉRIFIER » et recommande « ×15 alcool+cannabis / ×29 drogues+alcool ».
*Traitement retenu* : ×29 conservé en cloze, les deux valeurs désormais nommées dans l'explication
(correction n° 10). *Proposition* : arbitrage projet — si l'on suit knowledge-facts, le cloze devient
« ×15 » et « ×29 » se rapporte au cocktail drogues+alcool ; si l'on suit legal-facts (plus récemment
vérifié), rien à changer. *Source* : legal-facts B4, H4, J2 ; knowledge-facts C6.

**D3. `c-intervalle-pl-tunnel` c3 = 150 m.**
legal-facts A6 : « aucune distance chiffrée dans le code ; le “150 m” est une prescription locale
signalée dans certains tunnels ; le 150 m attendu à l'examen est *celui indiqué par la signalisation* ».
knowledge-facts C4 donne « 70 à 150 m selon signalisation ».
*Proposition* : garder le cloze mais formuler « l'intervalle **indiqué par la signalisation**, le plus
souvent {{c3::150 m}} » (la carte dit déjà « l'intervalle signalé »). Risque faible ; non appliqué pour
ne pas retoucher un cloze sans arbitrage. *Source* : legal-facts A6 ; knowledge-facts C4.

**D4. `aff-c-enfant-percoit-adulte` — « avant 10-12 ans ».**
La fourchette d'âge n'apparaît dans aucun dossier (knowledge-facts U1 ne retient que « comportements
imprévisibles, petits donc masqués » ; C10 ne traite que jeunes conducteurs et seniors). Le reste du
`pourquoi` (champ visuel étroit, yeux plus bas, attention absorbée par le jeu) est conforme.
*Proposition* : « incapacité à évaluer vitesses et distances **avant une dizaine d'années** », ou
suppression de la mention d'âge. *Source* : knowledge-facts U1 ; exam.md §3.1 Q3.

**D5. Doublon inter-thèmes : `c-croisement-nuit-regard` (C) ↔ `aff-r-nuit-regard-feux`
(`data/affirmations/04_route.yaml`, écrit en parallèle).**
Même question officielle (Q20), même distracteur (« je regarde ses feux »), même raison (« fixer les
phares éblouit ; on regarde vers la droite le plus loin possible et on ralentit »). Le brief §2
règle 8 interdit la même connaissance sous deux formes sans piège distinct ; ici le piège est
identique. *Proposition* : une seule des deux cartes — garder la question de décision C (la ligne
« vue nocturne / éblouissement » relève de la perception du conducteur) et supprimer l'affirmation R,
ou l'inverse. **Non appliqué : le fichier R est hors de mon périmètre.** *Source* : exam.md §3.1 Q20 ;
brief §2 règle 8.

**D6. Redondance inter-thèmes : `aff-c-pieton-detectable-motard` ↔ `aff-r-nuit-pieton-sombre`
(`data/affirmations/04_route.yaml`, écrit en parallèle).**
La queue du `pourquoi` de la carte C (« De nuit, un piéton sombre n'est vu qu'à 30 m, 150 m avec un
gilet »), ajoutée pour satisfaire la correction v1 n° 34, n'est plus orpheline : la carte R la porte
désormais (sans le 150 m). Elle ajoute une seconde connaissance à une carte Q11 qui, elle, ne parle pas
de nuit. *Proposition* : retirer cette queue de la carte C une fois le thème R stabilisé, et vérifier
que le « 150 m avec un gilet » survit quelque part (thème R ou U). **Non appliqué** (dépend de R).
*Source* : review-facts-questions n° 34 ; `data/affirmations/04_route.yaml`.

**D7. Doublon de chiffre inter-thèmes : `c-somnolence-stats` c1 = « 1 sur 3 » ↔
`r-autoroute-fatigue-aires` (`data/questions/04_route.yaml`, explication).**
Le chiffre de campagne « un accident mortel sur trois sur autoroute » est à la fois le cloze du fait C
et une phrase d'explication en R. *Proposition* : le retirer de l'explication R. **Non appliqué**
(hors périmètre). *Source* : legal-facts H4 ; brief §2 règle 8.

**D8. `c-verre-standard` — « 10 cl de vin à 12° ».**
legal-facts B5 écrit « 12,5 cl de vin à 12° » (Santé publique France / SR), knowledge-facts C6 écrit
« 10 cl de vin 12° ». La relecture v1 n° 12 a tranché pour 10 cl et l'harmonisation est faite dans tout
le thème (`c-verre-standard`, `aff-c-biere-whisky`). *Proposition* : rien à changer ; mentionné ici
pour mémoire, la divergence étant entre les dossiers et non dans la carte. *Source* : legal-facts B5 ;
knowledge-facts C6 ; review-facts-questions n° 12.

---

## 5. Points vérifiés sans remarque (échantillon)

- **Questions officielles** : Q3 (`c-enfant-masque`, `aff-c-enfant-percoit-adulte`), Q4
  (`c-trottinette-vulnerable`), Q7 (`c-cycliste-devant-depassement`), Q9 (`c-zone-attention-pluie`),
  Q11 (`aff-c-pieton-detectable-motard` : la bonne réponse est bien « le conducteur de la voiture »),
  Q12 (`aff-c-passager-arriere-conducteur` : les deux sous-affirmations OUI), Q13 (`c-distance-mouillee` :
  adhérence ÷ 2 **et** freinage × 2), Q17 (`aff-c-doses-maison` : situation B « à la maison »),
  Q20 (`c-croisement-nuit-regard` : BC) — **conformes au sens, mot pour mot**.
- **Valeurs juridiques relues dans `cdr.txt`** : R412-6-1 (téléphone tenu en main + port à l'oreille de
  tout dispositif émettant du son, sauf appareils correcteurs de surdité ; 4e classe ; 3 points) ;
  R412-6-2 (écran en fonctionnement dans le champ de vision hors aide à la conduite/navigation ;
  5e classe ; appareil saisi ; confiscation de plein droit ; 3 points) ; R414-4 IV (1 m / 1,50 m pour
  « un engin à deux ou à trois roues » — couvre bien la trottinette de `c-trottinette-vulnerable`) ;
  R416-1 (klaxon en agglomération : danger immédiat seulement) ; R416-20 (feux de marche arrière) ;
  R221-1-1 III et VI (restriction d'usage : 4e classe, 3 points → `aff-c-lunettes-points` a raison
  contre les sites qui disent « pas de points ») ; R234-1 I 1° et IV (0,20 g/L = 0,10 mg/L, 4e classe,
  **6 points**, applicable aussi à l'accompagnateur → `aff-c-probatoire-un-verre`) ; R412-12 (2 s,
  50 m, 4e classe, 3 points) ; L235-1 (aucun seuil ; 3 ans / 9 000 €).
- **Chiffres non juridiques** : temps de réaction 1 s / 2 s ; dizaines × 3 ; (dizaines)² avec la double
  lecture en explication (correction v1 n° 7 intacte) ; dizaines × 6 ; 2 traits ≈ 90 m (IISR T4 :
  39 + 13 + 39) ; 180°/45°/30° en clozes et 100°/75° hors cloze (correction v1 n° 9 intacte) ; 90 % par
  la vue, 5/10 binoculaire, 120° de champ ; pause 15-20 min / 2 h, sieste 20 min ; « 1 sur 3 » avec la
  nuance ONISR 4 % (8 à 14 % sur autoroute) (correction v1 n° 11 intacte) ; nuit × 7 ; 75 % près du
  domicile ; verre standard 10 g / +0,20-0,25 g/L (correction v1 n° 12 intacte) ; élimination
  0,10-0,15 g/L/h, pic 15-30 min / 1 h ; ×2 / ×10 / ×35 et « près de 30 % » ; conversions air/sang ;
  pictogrammes médicaments niveaux 1/2/3 (texte de l'arrêté du 8 août 2008) ; contrôle du rétroviseur
  « 5 à 10 s » (correction v1 n° 10 intacte, cohérent avec `c-regarder-loin`) ; 5 s / 70 m / ×3 / ×23 ;
  18-24 ans × 2, novices × 4.
- **Forme des cartes** : aucune réponse > 40 mots ni > 4 éléments ; aucun `pourquoi` > 45 mots ; aucune
  affirmation fausse porteuse d'un mot-signal (toujours / jamais / obligatoirement / uniquement) ;
  aucune réponse de question non décidable (pas de « ça dépend ») ; aucune explication contredisant sa
  réponse ; aucun apostrophe non échappé (les trois fichiers se chargent avec `yaml.safe_load`).
- **Recouvrements assumés maintenus** : `c-angle-mort-definition` (définition + geste) vs
  `aff-c-retros-suffisent` (piège « mes rétros bien réglés me suffisent ») ; `c-vitesse-double-freinage`
  (fait chiffré) vs `aff-c-vitesse-double-freinage-double` (piège « ×2 → ×2 » listé en knowledge-facts
  C14) — conformes à l'exception de la règle 8 du brief.

## Arbitrage inter-thèmes (passe finale, `python -m build.dedup`)
Supprimés comme doublons stricts d'une carte d'un autre thème : `aff-c-passager-arriere-conducteur` (→ `aff-s-passagere-arriere-danger`, S), `aff-s-ceinture-manteau` (→ `aff-p-ceinture-blouson`, P), `aff-r-autoroute-triangle` (→ `aff-a-triangle-autoroute`, A), `aff-r-descente-freiner-permanence` (→ `r-descente-freinage`, R), `r-nuit-eblouissement-suiveur` (→ `aff-p-retro-interieur-nuit`, P), `aff-e-pic-vitesse` (→ `e-pic-pollution-chiffres`, E), `aff-l-c18-priorite` (→ `scn-crois-c18-je-passe`). Les paires « fait à trous ↔ affirmation-piège sur le même chiffre » sont conservées volontairement et marquées `dedup_ok`.
