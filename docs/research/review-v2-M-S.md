# Relecture contradictoire v2 — thèmes M (mécanique et équipements) et S (sécurité du passager)

Périmètre : `data/questions/09_mecanique.yaml`, `data/faits/09_mecanique.yaml`,
`data/affirmations/09_mecanique.yaml`, `data/questions/10_securite_passager.yaml`,
`data/faits/10_securite_passager.yaml`, `data/affirmations/10_securite_passager.yaml`.
Aucun autre fichier de données, de code ou de documentation n'a été modifié.

**101 notes relues** (M : 29 questions + 5 faits + 26 affirmations ; S : 16 questions + 5 faits +
20 affirmations) — **10 ERREUR**, **5 STYLE** (toutes appliquées), **12 DOUTE** (proposées, non appliquées).

État après corrections : M = 29 questions / 5 faits / 22 affirmations (10 vrai – 12 faux, 45,5 %) ;
S = 16 questions / 5 faits / 20 affirmations (8 vrai – 12 faux, 40 %).
`python -m build.build --check` ne signale plus rien sur ces six fichiers (validation globale OK) et
`python -m build.dedup` ne laisse plus aucune paire interne M/S au-dessus du seuil par défaut (0,62).

Référentiels utilisés : `docs/research/sources/cdr.txt` (articles lus : R412-1, R412-1-1, R412-2,
R412-3, R412-6-3, R312-19 à R312-22, R313-*, R314-1, R314-3, R316-6, R413-7, R413-8, R416-1, R416-2,
R416-6, R416-7, R416-18, R416-19), `docs/research/exam.md` §3.1 (Q1, Q5, Q8, Q10, Q12, Q14),
`knowledge-facts.md` (M1-M7, E1-E10), `legal-facts.md` (A4, E5-E7, E11, G3),
`review-facts-questions.md`, `brief-v2-redaction.md`, `docs/05-audit-v2.md`.

---

## 1. Vérification « rien d'utile n'a disparu » (v1 → v2)

`git show HEAD:data/questions/09_mecanique.yaml` et `…10_securite_passager.yaml` relus intégralement.
Les connaissances d'examen listées dans `docs/02-carte-des-connaissances.md` sont toutes retrouvées :

| Connaissance v1 supprimée | Retrouvée dans |
|---|---|
| Feux obligatoires / facultatifs (`m-feux-liste`) | fait `m-feux-portees` (portées **et** explication « brouillard arrière obligatoire depuis 1990 ; brouillard avant, recul et feux de jour facultatifs ») |
| Feux de jour insuffisants sous la pluie | `m-feux-jour-limite` + `m-allumage-automatique` |
| Feu de brouillard arrière interdit sous la pluie | `aff-r-brouillard-arriere-pluie` (thème R) — voir ERREUR 2 |
| Réglage en hauteur des feux | `m-feux-reglage-hauteur` (cite Q1) |
| Changer une roue en sécurité | `m-changer-roue-securite` + `m-changer-roue-ecrous` |
| Galette 80 km/h | fait `m-galette-chiffres` + explication de `m-changer-roue-securite` |
| Câbles de démarrage (ordre) | `m-batterie-cables` (ordre conforme à knowledge-facts M3) + explication de `m-batterie-liquides-chiffres` |
| Boîte auto P/R/N/D | `m-boite-auto-positions` + `aff-m-boite-auto-p-arret` |
| Carburants (rond/carré/losange, E10, E85) | `m-carburants-etiquettes` + `m-erreur-carburant` |
| Ceinture / responsabilité | `s-ceinture-obligation`, `aff-s-ceinture-majeur-amende`, fait `d-ceinture-sanction` (thème D) |
| Sièges enfants | `s-enfant-moins-10-ans`, `s-siege-dos-route`, `s-groupes-sieges`, fait `s-enfant-chiffres`, 5 affirmations |
| Chargement | `s-chargement-placement`, `s-chargement-depassement`, fait `s-chargement-chiffres`, 4 affirmations |
| Remorque | `s-remorque-permis-b`, `s-remorque-conduite`, fait `s-remorque-chiffres` |
| Sécurité active / passive | `s-securite-active-passive` + `aff-s-abs-passive` |
| Roue de secours non obligatoire | `d-equipements-obligatoires` (thème D) |
| Pneus hiver / chaînes / loi Montagne | thème R (`r-loi-montagne-periode`, `aff-r-montagne-ms`, `aff-r-montagne-4-pneus`) + `aff-m-4-saisons-3pmsf` |

Seule perte réelle, hors carte des connaissances : **parallélisme et équilibrage** (véhicule qui tire /
vibrations vers 90 km/h, `m-amortisseurs-plaquettes` v1) ont disparu du deck entier (`grep -rl`
« parallélisme » ne renvoie plus rien). Voir DOUTE 11. Le marquage de flanc `205/55 R16 91V` a aussi
disparu, mais il n'est pas dans la carte des connaissances : suppression validée.

---

## 2. `data/questions/09_mecanique.yaml`

### ERREUR 1 — `m-erreur-carburant` : mécanisme inversé (appliqué)
L'explication affirmait « **Le gazole dans un moteur essence** est le cas le plus destructeur », juste
après avoir rappelé qu'un pistolet essence entre dans un réservoir diesel — les deux phrases se
contredisent, et c'est l'inverse qui est enseigné : l'essence ne lubrifie pas la pompe à injection
haute pression d'un diesel et la détruit. L'affirmation « l'assurance ne couvre pas » était par
ailleurs trop absolue.
Correction appliquée : « …(un pistolet essence entre dans un réservoir diesel, l'inverse non).
**L'essence dans un moteur diesel** est le cas le plus grave : elle ne lubrifie pas la pompe à
injection et la détruit. L'assurance ne couvre **généralement** pas cette erreur. »
Source : knowledge-facts M3 (« erreur de carburant → ne pas démarrer ») ; TotalEnergies.

### ERREUR 6 — `m-appel-phares` : doublon avec le thème L (appliqué)
`python -m build.dedup` donnait **0,69** entre `m-appel-phares` et `aff-l-klaxon-nuit`
(« J'avertis de préférence par un appel de phares plutôt qu'au klaxon », VRAI, R416-2) ; la même règle
est en outre portée par le verso du panneau B34 (`panneaux_interdiction.yaml`). La seule connaissance
propre à la carte de M — *un appel de phares n'accorde aucune priorité* — n'était nulle part ailleurs
et dormait en explication.
Correction appliquée : l'id est conservé, la carte devient une décision —
« Un conducteur arrêté me fait un appel de phares pour me laisser passer. Puis-je m'engager ? » →
« Non : un appel de phares n'a aucune valeur réglementaire et ne donne aucune priorité. Je ne m'engage
qu'après avoir vérifié moi-même que la voie est libre. » ; R416-1/R416-2 passent en explication.
Similarité retombée sous 0,50.

### STYLE 5 — `s-ecall` : explication complétée (appliqué)
Ajout de « Il appelle le 112, jamais le 15, et transmet la position, l'identifiant du véhicule et le
nombre d'occupants », qui récupère le piège porté par l'affirmation supprimée (ERREUR 5).
Source : règlement (UE) 2015/758 ; knowledge-facts M6 et E10.

### Vérifications sans remarque
Ordre des câbles (knowledge-facts M3, consensus « rouge d'abord, masse en dernier ») ; ABS
(« écraser et maintenir », « ne raccourcit pas la distance », direction conservée — M4, dépliant
Sécurité routière) ; huile à froid sur sol plat (M3) ; liquide de refroidissement jamais à chaud (M3) ;
liquide de frein (plaquettes ou fuite, 2 ans — M3) ; 1,6 mm + témoins d'usure + 135 € et immobilisation
(R314-1, arrêté du 18 juillet 2019, legal-facts E5) ; pression à froid > 2 h ou < 3 km, +0,2/0,3 bar
chargé (M2, Q1) ; régulateur/limiteur (M6) ; ESP 2014, eCall 2018, GSR2 juillet 2024
(legal-facts E11) ; conduite automatisée niveau 2, décret 2021-873 (M6) ; triangle 30 m et gilet
avant de sortir (R416-19, arrêté du 30 septembre 2008) ; remorquage interdit sur autoroute (M7) ;
BVA code 78 + passerelle 7 h (M3).

---

## 3. `data/faits/09_mecanique.yaml`

Aucune erreur. `m-pneus-chiffres`, `m-feux-portees` (150 m visibles / 30 m / 100 m / plaque 20 m —
legal-facts E5, piège « visible à » vs « éclaire à » conservé), `m-batterie-liquides-chiffres` et
`m-adas-dates` sont conformes. Le fichier n'a pas été modifié par le rédacteur v2 : les corrections
n° 21 de la relecture v1 y sont bien présentes. Voir DOUTE 4 et 5 sur `m-galette-chiffres`.

---

## 4. `data/affirmations/09_mecanique.yaml`

### ERREUR 2 — `aff-m-brouillard-arriere-pluie` : doublon inter-thème (supprimée)
Similarité **0,75** avec `aff-r-brouillard-arriere-pluie` (thème R) : même situation (forte pluie, en
plein jour), même affirmation, même verdict, même article (R416-7 II). Le rapport du rédacteur
(`v2-M-S.md` §4) pose lui-même que « l'usage des feux par temps de pluie/brouillard » appartient à R et
que M ne garde que l'angle équipement. La carte de R est en outre plus complète (135 €, pendant
`aff-r-brouillard-avant-pluie`). **Carte supprimée de M.** Vérifié : R416-7 II — « le ou les feux
arrière de brouillard ne peuvent être utilisés qu'en cas de brouillard ou de chute de neige ».

### ERREUR 3 — `aff-m-detresse-bouchon` : doublon inter-thème (supprimée)
Similarité **0,61** avec `aff-r-autoroute-bouchon-detresse` (même contexte autoroute + file à l'arrêt,
même verdict, même R416-18) ; le fait `l-feux-detresse-usage` (thème L) couvre la règle à 0,53. Le
sous-thème `depannage` ne correspondait d'ailleurs pas à la situation. **Carte supprimée de M.**

### ERREUR 4 — `aff-m-reglage-feux-charge` : doublon interne (supprimée)
Similarité **0,80** avec la question `m-feux-reglage-hauteur` : même mécanisme (le véhicule s'affaisse,
le faisceau monte), même molette 0 → cran maximal, même renvoi à la question officielle Q1, même
verdict implicite. Aucun piège distinct au sens de la règle 8 du brief. **Carte supprimée** ; la
question conserve Q1 en explication et `aff-m-chargement-pression` rappelle « on règle aussi la
hauteur des feux ». La proposition C de Q1 reste donc couverte deux fois (M et `p-verif-chargement-important`).

### ERREUR 5 — `aff-m-ecall-15` : doublon interne (supprimée)
Similarité **0,78** avec `s-ecall`, dont la réponse énonce déjà « le véhicule appelle seul le 112 » et
« un bouton SOS » ; le fait `m-adas-dates` porte en outre « eCall appelle le 112, pas le 15 ». La carte
des connaissances attribue une **question** à l'e-call. **Affirmation supprimée**, piège rapatrié dans
l'explication de `s-ecall` (STYLE 5).

### Vérifications sans remarque
`aff-m-voyant-abs-blocage` (VRAI) et `aff-m-voyant-abs-arret` (FAUX) sont conformes au verbatim de la
Q5 officielle (réponses AD) ; `aff-m-chargement-pression` est conforme au distracteur A de Q1 ;
`aff-m-stationnement-arriere` est conforme à Q8 **et** au texte de R412-6-3 (le conducteur « assure le
contrôle de la manœuvre » et « est à tout instant en capacité de mettre fin à cette manœuvre ») ;
`aff-m-4-saisons-3pmsf` est conforme à D314-8 et au 1er novembre 2024 ; `aff-m-limiteur-descente`,
`aff-m-regulateur-obstacle` et `aff-m-regulateur-conditions` sont conformes à M6 ; aucune affirmation
fausse ne contient de mot-signal. Équilibre après suppressions : 10 vrai / 12 faux (45,5 %).

---

## 5. `data/questions/10_securite_passager.yaml`

### ERREUR 7 — `s-chargement-depassement` : doublon avec le fait `s-chargement-chiffres` (réécrite)
Similarité **0,86**, la troisième plus forte du deck entier : la réponse énumérait exactement les
quatre valeurs du fait à trous (0 à l'avant, 3 m à l'arrière, signalisation au-delà de 1 m,
largeur 2,55 m). La règle 8 du brief veut qu'un chiffre vive dans *un* fait et une décision dans *une*
question, et le brief §3 demande de transformer une carte-liste en décision.
Correction appliquée (id conservé) :
« Une planche dépasse de 2 m à l'arrière de mon break. Puis-je rouler ainsi ? » → « Oui, à condition de
la signaler : tout dépassement arrière de plus de 1 m exige un dispositif réfléchissant, remplacé la
nuit par un feu rouge visible de loin. » ; 3 m / aplomb avant / sanctions passent en explication, avec
`dedup_ok: [s-chargement-chiffres]` puisque le recouvrement de vocabulaire résiduel est inévitable.
Source : R312-21 (3 m, 4e classe), R312-22 (aucun dépassement à l'avant, 3e classe), arrêté du
16 juillet 1954 art. 40-41 via legal-facts E6.

### ERREUR 8 — `s-remorque-permis-b` : vitesse d'un ensemble > 3,5 t (appliqué)
L'explication disait « 90 km/h sur autoroute **et route à chaussées séparées**, 80 ailleurs », ce qui
contredisait le fait `s-remorque-chiffres` du même thème (« 90/80/80 ») et la relecture v1 n° 60.
R413-8 lu dans `cdr.txt` : 90 sur autoroute, **80 sur les routes à caractère prioritaire** (relevé à 90
pour les seuls véhicules ≤ 12 t sur routes à chaussées séparées par un terre-plein), 80 sur les autres
routes ; legal-facts A4 retient « 90/80/80 ».
Correction appliquée : « Si le PTRA dépasse 3,5 t : 90 km/h sur autoroute, 80 km/h partout ailleurs
(R413-8). »

### ERREUR 9 — `s-coffre-toit` : charge de toit hors dossier (appliqué)
« souvent limitée à 50-75 kg par la notice » ne s'appuie sur aucune source du projet ;
knowledge-facts E6 donne « charge de toit max selon notice (**~75-100 kg**) ». Le doute n° 3 du
rapport de rédaction est donc tranché par le dossier lui-même.
Correction appliquée : « La charge de toit admissible, fixée par la notice, dépasse rarement
75 à 100 kg ». Le « +10 à 15 % » de consommation est conforme à knowledge-facts M3.

### STYLE 1 — `s-ceinture-obligation` : dispenses (appliqué)
« dispense médicale sur certificat **seulement** » est faux : R412-1 II énumère six cas (morphologie
manifestement inadaptée, certificat médical, véhicules d'intérêt général et ambulances en
intervention, taxi en service, services publics à arrêts fréquents et livraisons de porte à porte en
agglomération).
Correction appliquée : « dispenses limitées (morphologie inadaptée, certificat médical, taxi en
service — R412-1 II) ».

### STYLE 2 — `s-enfant-moins-10-ans` : explication dupliquée (appliqué)
L'explication reprenait mot pour mot celle du fait `s-enfant-chiffres` (exceptions pour l'avant,
135 € sans points, « la limite légale est l'âge, pas la taille ») — similarité 0,60 entre les deux
notes. Les **dérogations au dispositif de retenue** (R412-2 III), elles, n'étaient nulle part.
Correction appliquée : « Dérogations au dispositif de retenue (R412-2 III) : morphologie de l'enfant
adaptée à la ceinture, certificat médical, taxi ou transport en commun. Sanction : 135 € pour le
conducteur, sans retrait de points. Les exceptions pour la place avant sont celles de l'article R412-3. »

### STYLE 3 — `s-ceinture-50-kmh` : cohérence de l'efficacité (appliqué)
« La ceinture réduit de moitié le risque de décès » contredisait le fait `s-ceinture-efficacite`
(« divise par 2 à 3 »). legal-facts G3 (vérifié 2026-09-21) : « la ceinture divise par 2 à 3 le risque
d'être tué ». Correction appliquée : « divise par deux à trois le risque d'être tué ».
La valeur « 2,5 t pour un adulte de 75 kg à 50 km/h » est confirmée par legal-facts G3 : le doute n° 2
du rapport de rédaction est levé.

### Vérifications sans remarque
`s-surnombre` (R412-1-1 lu : une personne par siège, 4e classe, 3 points au conducteur) ;
`s-siege-dos-route` (R412-3 I 1°, i-Size 15 mois) ; `s-animaux` (R412-6, 35 €, 2e classe) ;
`s-groupes-sieges` (R44 / R129, plus vendus depuis le 1er septembre 2024) ; `s-chargement-placement`
(arrimage 68 € et immobilisation = R312-19 IV, 3e classe) ; `s-remorque-conduite` (1,3 × le poids du
tracteur, legal-facts E6) ; `s-securite-active-passive` (knowledge-facts E7) ; `s-femme-enceinte`.

---

## 6. `data/faits/10_securite_passager.yaml`

### STYLE 4 — `s-ceinture-efficacite` : source (appliqué)
Le cloze « environ 1 occupant tué sur 5 ne la portait pas » vient du dépliant ceinture 2022 de la
Sécurité routière (21 % des tués en 2021, knowledge-facts E1), pas d'ONISR 2025 — legal-facts G3
donne pour l'ONISR « environ un quart », valeur marquée « À VÉRIFIER ». La valeur de la carte est la
bonne (règle 7 du brief) ; seule l'attribution était fausse.
Correction appliquée : `source: securite-routiere.gouv.fr — La ceinture de sécurité ; dépliant
ceinture 2022 (données 2021)`.

### Vérifications sans remarque
`s-enfant-chiffres` : les trois clozes sont dans le code — moins de 10 ans (R412-2 II), dos à la route
jusqu'à 15 mois (R129, legal-facts E7), **moins de 3 ans interdit sur un siège sans ceinture**
(R412-2 I, lu verbatim dans `cdr.txt`). `s-chargement-chiffres` (R312-20/21/22),
`s-remorque-chiffres` (R221-4, R317-8 II, R413-8), `s-airbag-chiffres` : conformes.

---

## 7. `data/affirmations/10_securite_passager.yaml`

### ERREUR 10 — `aff-s-enfant-135-cm` : dérogations incomplètes (appliqué)
« la **seule** dérogation est une morphologie manifestement adaptée à la ceinture, ou un certificat
médical » : R412-2 III en prévoit aussi deux autres (taxi, transport en commun).
Correction appliquée : « …la limite est l'âge de 10 ans (R412-2) ; on n'y échappe que par une
morphologie adaptée à la ceinture, un certificat médical, un taxi ou un transport en commun. »

### Vérifications sans remarque
`aff-s-passagere-arriere-danger` est conforme à Q12 (AC : « est en danger » OUI, « met le conducteur
en danger » OUI) ; `aff-s-enfant-10-ans-avant` VRAI est conforme à R412-2/R412-3 et au piège E10 ;
`aff-s-enfant-genoux` et `aff-s-caravane-passager` à R412-1-1 ; `aff-s-chargement-avant` à R312-21 et
R312-22 ; `aff-s-remorque-retroviseurs` à R316-6 (« sans angle mort notable susceptible de masquer un
véhicule s'apprêtant à dépasser ») ; `aff-s-abs-passive` et `aff-s-euroncap-pietons` à
knowledge-facts E7 ; `aff-s-isofix` (2011) à E4. Aucune affirmation fausse ne contient de mot-signal ;
équilibre 8 vrai / 12 faux (40 %).

---

## 8. DOUTE — proposés, non appliqués

1. **`aff-s-passagere-arriere-danger` ↔ `aff-c-passager-arriere-conducteur` (similarité 0,85).**
   Doublon inter-thème : deux affirmations sur la même question officielle Q12, même verdict, même
   raisonnement. La ceinture est la première ligne de la carte des connaissances du thème S ; le thème
   C est celui de la vigilance. *Proposition : supprimer `aff-c-passager-arriere-conducteur`
   (fichier hors périmètre).* Non appliqué pour ne pas risquer une double suppression.
2. **`aff-s-ceinture-manteau` ↔ `aff-p-ceinture-blouson`.** Doublon sémantique complet (doudoune sous
   la ceinture, VRAI) que `dedup.py` ne détecte pas (0,40, formulations différentes). Le positionnement
   de la ceinture appartient au thème P (`p-ceinture-position`, carte des connaissances P
   « ceinture plate »), et le rédacteur v2 l'écrit lui-même (§4). *Proposition : supprimer
   `aff-s-ceinture-manteau`* — non appliqué parce que S tomberait à 36,8 % de vrai, marge trop faible
   sur le seuil de 35 %, et que le relecteur de P a déjà retiré ses cartes `aff-p-appuie-tete-confort`
   et `aff-p-assistance-stationnement` au profit de S et M : l'arbitrage inverse ici doit être
   explicite. `aff-s-siege-manteau` (harnais d'un siège enfant) est, lui, bien distinct.
3. **`aff-m-voyant-abs-blocage` / `aff-m-voyant-abs-arret` ↔ `voyant-abs` (0,65).** Le champ `piege` de
   la carte de reconnaissance énonce déjà les deux réponses de Q5 verbatim, alors que sa
   `signification` et sa `conduite` les contiennent. *Proposition : retirer la ligne `piege` de
   `voyant-abs`* (`data/reconnaissance/voyants.yaml`, hors périmètre) et garder les deux affirmations,
   qui sont la forme réelle de l'épreuve.
4. **`m-galette-chiffres` — période des pneus cloutés.** Les deux dossiers se contredisent :
   knowledge-facts M2 « du samedi avant le 11 novembre au dernier dimanche de mars »,
   legal-facts E5 « du 1er novembre au 31 mars ». R413-7, lu dans `cdr.txt`, **ne fixe aucune période**
   (seulement les 90 km/h et le disque) ; elle est renvoyée à un arrêté. La carte est prudente
   (« pendant la période hivernale fixée par arrêté », la date classique restant en explication) :
   conservée telle quelle, mais la divergence mériterait d'être tranchée dans `legal-facts.md`.
5. **`m-galette-chiffres` — « chaînes ~50 km/h ».** legal-facts E5 précise que c'est « une
   préconisation des fabricants, pas un texte » et knowledge-facts M2 marque 50 vs 40 « À VÉRIFIER ».
   La valeur reste en explication avec la mention « (préconisation) » : acceptable, mais la règle 7 du
   brief pousserait à la retirer.
6. **« 25 cm » au volant — `s-airbag-distance`, `s-airbag-chiffres`, `s-femme-enceinte`.** Valeur à
   source unique, marquée « À VÉRIFIER » dans knowledge-facts E2, mais présente dans la carte des
   connaissances (« distance au volant ~25 cm ») et validée par la relecture v1 n° 23. Elle vit
   aujourd'hui sur trois cartes de S plus `p-siege-reglage`. *Proposition : garder le fait
   `s-airbag-chiffres` et fondre `s-airbag-distance` dans une décision (« le siège est trop près du
   volant : que corrige-t-on ? »)* — similarité actuelle 0,59, juste sous le seuil.
7. **`s-chargement-placement` — « une bouteille d'eau de 1,5 kg pèse ~50 kg à 50 km/h ».** C'est un
   facteur ×33, alors que knowledge-facts E1 retient le facteur officiel **×25** (enfant de 20 kg =
   projectile d'une demi-tonne, repris tel quel par `s-ceinture-efficacite`). Le deck porte donc deux
   facteurs. *Proposition : « près de 40 kg » (×25), ou basculer sur l'exemple sourcé de
   `aff-s-plage-arriere` (300 g = boule de bowling).*
8. **Q5, proposition B non couverte.** L'épreuve demande aussi, voyant ABS allumé, si « la distance
   d'arrêt sera fortement augmentée » : la bonne réponse est **non**, et aucune carte ne le dit
   (`aff-m-abs-distance` porte sur un ABS en état de marche). *Proposition : une affirmation
   `aff-m-voyant-abs-distance` — « Avec le voyant ABS allumé, ma distance d'arrêt sera fortement
   augmentée » → FAUX, le circuit de freinage classique est intact, c'est la **direction** que je
   risque de perdre.* Non appliquée : elle frôlerait `aff-m-abs-distance` au dedup et demande un
   arbitrage de volume.
9. **`s-esp-fonction` — « Son voyant clignote quand il travaille ».** knowledge-facts M1 marque ce
   point « À VÉRIFIER ». Il est en revanche cohérent avec `voyant-esp` (« Clignotant : l'ESP
   intervient »). Laissé tel quel, à confirmer par une source constructeur.
10. **`aff-m-pneu-age` — « doit être remplacé ».** Les dossiers disent « max 10 ans **recommandé** »
    (knowledge-facts M2) : il n'y a pas d'obligation légale. Le verdict VRAI reste celui des écoles de
    conduite ; *proposition de nuance : « est à remplacer »*.
11. **Parallélisme et équilibrage disparus du deck** (véhicule qui tire après un trottoir ; vibrations
    au volant vers 90 km/h — knowledge-facts M2/M3). Hors carte des connaissances, donc pas recréés ;
    *proposition : une ligne dans l'explication de `m-plaquettes-usure` si le volume de M le permet.*
12. **`s-remorque-chiffres` ↔ `s-remorque-permis-b` (0,50).** Le fait et la question portent les mêmes
    seuils (750 / 3 500 / 4 250 kg). Sous le seuil de `dedup.py`, mais la règle 8 voudrait que la
    question devienne une décision (« ma caravane pèse 900 kg, ma voiture 1 800 kg de PTAC : puis-je
    l'atteler avec mon permis B ? »). Non appliqué : ce serait une restructuration.

---

## 9. Recouvrements inter-thèmes restants (signalés, pas des erreurs)

- `p-verif-chargement-important` (P) ↔ `aff-m-chargement-pression` (M) : 0,55. La Q1 officielle est
  couverte par P (décision complète), M (piège sur la pression) et `m-feux-reglage-hauteur` (molette).
  Trois angles distincts, mais c'est le maximum tolérable pour une seule question officielle.
- `d-ceinture-sanction` (D, fait) ↔ `aff-s-ceinture-majeur-amende` (S) : 0,60. Piège distinct
  (« qui est verbalisé ? ») — légitime au titre de la règle 8. L'explication de `s-ceinture-obligation`
  redit cependant tout le barème de D : à resserrer si D est retouché.
- `r-autoroute-panne` (R) ↔ `m-panne-procedure-route` (M) : 0,55, contextes différents (autoroute vs
  route ordinaire). Noter que la sortie « côté droit / opposé à la circulation » (knowledge-facts M7)
  n'est plus dite que dans R : la réponse de M est déjà à 38 mots et ne peut pas l'accueillir.
- `aff-r-montagne-ms` (R) ↔ `aff-m-4-saisons-3pmsf` (M) : 0,59, verdicts opposés (M+S insuffisant /
  4 saisons 3PMSF accepté) : deux pièges distincts, conservés.
