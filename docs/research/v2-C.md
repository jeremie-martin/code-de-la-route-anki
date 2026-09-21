# Thème C — Le conducteur : rapport de réécriture v2

Périmètre : `data/questions/03_conducteur.yaml`, `data/faits/03_conducteur.yaml`,
`data/affirmations/03_conducteur.yaml` (fichier nouveau). Règles appliquées :
`docs/research/brief-v2-redaction.md`, décisions `docs/05-audit-v2.md` §2.1, §2.2, §2.5.
Version de référence pour les suppressions : `git show HEAD:data/…` (commit e02cf59).

---

## 1. Cartes v1 supprimées → cartes v2 créées

### 1.1 Questions (v1 : 36 notes → v2 : 25 notes)

| Id v1 supprimé | Motif | Ids v2 qui portent la connaissance |
|---|---|---|
| `c-champ-visuel-vitesse` | question de cours, chiffres déjà en fait | F `c-champ-visuel-chiffres` ; AFF `aff-c-champ-visuel-vitesse-pieton` |
| `c-detectabilite-pieton-nuit` | contredisait la Q11 officielle (relecture v1 n° 34) | AFF `aff-c-pieton-detectable-motard` (Q11 verbatim + visibilité de nuit 30 m / 150 m) |
| `c-vision-acuite-permis` | chiffres déjà en fait ; sanction en doublon | F `c-vue-90-pourcent` ; AFF `aff-c-lunettes-points` |
| `c-enfant-perception` | forme « question de cours » d'une double OUI/NON officielle (Q3) | AFF `aff-c-enfant-percoit-adulte`, `aff-c-enfant-croit-vu` |
| `c-passagere-sans-ceinture` | idem (Q12 officielle) | AFF `aff-c-passager-arriere-conducteur` |
| `c-indices-anticipation` | carte-liste (9 indices) | Q `c-indice-ballon`, `c-indice-feux-recul`, `c-indice-cycliste-regard`, `c-indice-bus-arrete`, `c-indice-vehicule-stationne-portiere`, `c-enfant-masque` ; AFF `aff-c-indice-danger-certain` |
| `c-fatigue-signes` | carte-liste (8 signes) ; relecture v1 n° 40 | AFF `aff-c-fatigue-signes` (fatigue → pause / somnolence → dormir) ; Q `c-somnolence-que-faire` |
| `c-fatigue-pause` | chiffres déjà en fait | F `c-fatigue-pause-chiffres` ; AFF `aff-c-pause-sans-signe`, `aff-c-repas-copieux`, `aff-c-micro-sommeil` |
| `c-distracteurs` | carte-liste (6 distracteurs) | AFF `aff-c-oreillette`, `aff-c-gps-roulant`, `aff-c-ecran-video`, `aff-c-mains-libres-passager` ; Q `c-telephone-arret` |
| `c-alcool-doses` | carte-liste ; chiffres déjà en fait ; relecture v1 n° 38 | F `c-verre-standard` ; AFF `aff-c-doses-maison` (Q17 officielle), `aff-c-biere-whisky` |
| `c-alcool-effets` | carte-liste (effets) | AFF `aff-c-alcool-sous-seuil`, `aff-c-alcool-jugement`, `aff-c-alcool-eblouissement` |
| `c-alcool-pic` | chiffres déjà en fait | F `c-alcool-elimination` ; AFF `aff-c-dernier-verre-depart`, `aff-c-cafe-dessoule`, `aff-c-lendemain-matin` |
| `c-medicaments-pictogrammes` | carte-liste (3 niveaux) | F `c-medicaments-niveaux` (nouveau) ; AFF `aff-c-medicament-sans-ordonnance`, `aff-c-somnifere-soir`, `aff-c-medicament-alcool` |
| `c-jeunes-conducteurs-risque` | carte-liste (7 causes) | AFF `aff-c-jeune-reflexes`, `aff-c-aac-accidents` |
| `c-telephone-risque` *(supprimé à cette passe)* | doublon : les ×3 / ×23 sont les clozes de `c-telephone-5s`, et le jugement « kit mains-libres = sans risque » est `aff-c-mains-libres-passager` (la consigne « mode avion » y a été reportée) | F `c-telephone-5s` ; AFF `aff-c-mains-libres-passager`, `aff-c-oreillette` ; Q `c-telephone-arret` |
| `c-indice-roues-braquees` *(créé puis supprimé à cette passe)* | doublon de `c-indice-feux-recul` (même situation, même réponse) | Q `c-indice-feux-recul`, dont l'explication cite désormais roues braquées / conducteur au volant / clignotant + R412-10 |

Questions v1 conservées telles quelles (id inchangé) : `c-regarder-loin`, `c-croisement-nuit-regard`,
`c-eblouissement-duree`, `c-angle-mort-definition`, `c-zone-attention-pluie`, `c-enfant-masque`,
`c-trottinette-vulnerable`, `c-cycliste-devant-depassement`, `c-retro-avant-freiner`,
`c-fatigue-remedes-faux`, `c-telephone-arret`, `c-cannabis-effets`, `c-emotions`,
`c-passagers-pression`, `c-indice-feux-recul`, `c-indice-bus-arrete`, `c-indice-ballon`,
`c-indice-cycliste-regard`, `c-indice-vehicule-stationne-portiere`, `c-routine-monotonie`,
`c-vitesse-fatigue`.

### 1.2 Faits (v1 : 22 notes → v2 : 21 notes)

| Id v1 supprimé | Motif | Où la connaissance vit maintenant |
|---|---|---|
| `c-feux-portee` | hors thème C (feux = M, conduite de nuit = R) et déjà présent ailleurs | F `m-feux-portees` (30 m / 100 m / 150 m) ; Q `r-nuit-feux-croisement-route` et `r-nuit-vitesse-visibilite` dans `04_route.yaml` (« s'arrêter dans la distance éclairée », 70 km/h) ; lisibilité 150 m / 50 m = thème signalisation |
| `c-choc-50-etages` | hors thème C (sécurité des passagers) et déjà présent ailleurs | Q `s-ceinture-50-kmh` (chute de 3 étages, 2,5 t) et F de `10_securite_passager.yaml` (enfant 20 kg = demi-tonne) |

Fait créé : `c-medicaments-niveaux` (remplace la carte-liste `c-medicaments-pictogrammes`).
Corrections de la relecture v1 vérifiées comme toujours appliquées : n° 7 (`c-distance-arret-formule`),
n° 8 (`c-distance-mouillee`, cloze unifié sur « 2 »), n° 9 (`c-champ-visuel-chiffres`), n° 10
(`c-retro-7s`, « 5 à 10 s »), n° 11 (`c-somnolence-stats`, ONISR 4 % / 8-14 %), n° 12 (`c-verre-standard`,
10 cl de vin), n° 13 (`c-distance-laterale` supprimé, cf. `l-depassement-laterale`).

### 1.3 Affirmations (fichier nouveau : 42 notes)

Deux affirmations écrites à la passe précédente ont été retirées ou refondues à cette passe :

| Id retiré | Motif | Remplacement |
|---|---|---|
| `aff-c-retros-avant-clignotant` | contenu entièrement inclus dans la réponse de `c-ordre-controles-changement-file` (« rétroviseurs… puis clignotant ») | — (la connaissance reste sur la question de séquence et sur `c-clignotant-avant-ralentir`) |
| `aff-c-baillements` | doublon de `c-somnolence-que-faire` (mêmes signes, même réponse) | `aff-c-fatigue-signes` : rétablit la distinction officielle fatigue → pause / somnolence → dormir, perdue avec la carte-liste v1 `c-fatigue-signes` |

---

## 2. Cartes ajoutées pour combler un manque de `docs/02-carte-des-connaissances.md`

| Carte | Ligne visée de la carte des connaissances |
|---|---|
| Q `c-ordre-controles-changement-file` | « Prises d'information : … contrôles rétroviseurs (intérieur, gauche, droit) et angle mort avant tout changement, **ordre des contrôles** » — aucune carte v1 ne donnait la séquence |
| Q `c-clignotant-avant-ralentir` | même ligne (« le clignotant est mis avant de ralentir », knowledge-facts C12 ; R412-10) |
| Q `c-somnolence-que-faire` | « Fatigue, somnolence : signes, … ne pas lutter ; sieste » — décision située, à la place de la liste de signes |
| Q `c-suiveur-trop-pres` *(ajoutée à cette passe)* | « Intervalle de sécurité : 2 secondes… » notée **F + Q** : les quatre faits existaient (`c-intervalle-2s`, `c-intervalle-pl-tunnel`, `c-autoroute-deux-traits`, `c-distance-mouillee`) mais **aucune décision**. Piège visé : « je freine pour faire reculer celui qui me colle » |
| F `c-medicaments-niveaux` | « Médicaments : pictogrammes niveau 1/2/3 » (R + F) |
| AFF `aff-c-fatigue-signes` *(refondue à cette passe)* | « Fatigue, somnolence : **signes**… » |
| AFF perception (`aff-c-vision-peripherique`, `aff-c-nuit-distances`, `aff-c-regard-obstacle`, `aff-c-champ-visuel-vitesse-pieton`) | « Champ visuel… vision et vitesse… vue nocturne » (F + Q) — la v1 n'avait que des chiffres |
| AFF distances (`aff-c-temps-reaction-vitesse`, `aff-c-reaction-vehicule-ralentit`, `aff-c-vitesse-double-freinage-double`, `aff-c-intervalle-pluie-nuit`) | lignes « Temps de réaction » et « Distance de freinage » — pièges C14 (« le temps de réaction augmente avec la vitesse », « ×2 → ×2 ») |
| AFF seniors (`aff-c-senior-visite`, `aff-c-senior-reaction`) et `aff-c-lunettes-points` | « Émotions… personnes âgées » et « Aptitude médicale, maladies, permis et vue (mention 01) » |

Questions officielles 2023 couvertes en forme d'épreuve : Q3 (`c-enfant-masque`,
`aff-c-enfant-percoit-adulte`), Q4 (`c-trottinette-vulnerable`), Q7 (`c-cycliste-devant-depassement`),
Q9 (`c-zone-attention-pluie`), Q11 (`aff-c-pieton-detectable-motard`), Q12
(`aff-c-passager-arriere-conducteur`), Q13 (F `c-distance-mouillee`), Q17 (`aff-c-doses-maison`),
Q20 (`c-croisement-nuit-regard`). Q8/Q14 (assistance au stationnement, quitter un stationnement) et
Q5 (ABS) relèvent des thèmes P et M, déjà traités dans `08_prendre_quitter.yaml`, `09_mecanique.yaml`
et `10_securite_passager.yaml` : rien n'a été dupliqué ici.

---

## 3. Corrections apportées à cette passe (relecture du premier passage)

1. **`c-cycliste-devant-depassement`** — correction n° 35 de `review-facts-questions.md` rétablie :
   l'explication dit maintenant que la Q7 officielle **n'a pas d'énoncé** (photo + trois propositions)
   et que le « véhicule en face » du recto est **l'interprétation la plus probable de la photo**, pas
   un élément du texte officiel.
2. **`aff-c-pieton-detectable-motard`** — la fin de la correction n° 34 (« De nuit, un piéton sombre
   n'est vu qu'à 30 m en feux de croisement, 150 m avec un gilet ») avait disparu du thème et
   n'existe nulle part ailleurs dans le deck ; elle est rétablie dans le `pourquoi` (45 mots max).
3. **`c-telephone-risque`** et **`c-indice-roues-braquees`** supprimés (doublons, cf. § 1.1).
4. **`aff-c-retros-avant-clignotant`** supprimée, **`aff-c-baillements`** refondue en
   `aff-c-fatigue-signes` (cf. § 1.3).
5. **`aff-c-alcool-sous-seuil`** : « effets dès 0,2-0,3 g/L » → « dès 0,3 g/L », seule valeur sourcée
   (knowledge-facts C6).
6. **`aff-c-jeune-reflexes`** : source « ONISR — Bilan 2025 » → « ONISR — Bilan définitif 2024 »
   (l'édition réellement dépouillée dans les dossiers).
7. **`c-emotions`** et **`c-passagers-pression`** : `importance: utile`, pour s'aligner sur la ligne
   « Émotions, stress, colère ; jeunes conducteurs ; personnes âgées | Q | **U** » de la carte des
   connaissances (les affirmations du même groupe étaient déjà en `utile`).
8. **`c-indice-feux-recul`** : explication enrichie des indices absorbés
   (roues braquées, conducteur installé, clignotant) et de R412-10.

Valeurs juridiques revérifiées dans `docs/research/sources/cdr.txt` (code consolidé au 10/09/2026) :
R412-6-1 (téléphone tenu en main + port à l'oreille, 4e classe, 3 points — `aff-c-oreillette`,
`c-telephone-arret`), R412-6-2 (écran, 5e classe, 3 points, confiscation — `aff-c-ecran-video`),
R234-1 (0,20 g/L en probatoire = 0,10 mg/L, 4e classe, **6 points** — `aff-c-probatoire-un-verre`),
R416-1 (klaxon en agglomération : danger immédiat seulement — `aff-c-klaxon-ecole`),
R416-20 (feux de recul — `c-indice-feux-recul`), R412-11 (laisser un bus quitter son arrêt en
agglomération) et R413-17 III 3° (ralentir au croisement d'un véhicule de transport d'enfants —
`c-indice-bus-arrete`), R412-10, R412-12, R414-4, R221-1-1. Toutes conformes.

---

## 4. Doutes restants

| Point | Traitement retenu | Source |
|---|---|---|
| **Q7 officielle sans énoncé** | Le recto pose « un véhicule arrive en face » ; l'explication signale explicitement que c'est une interprétation de la photo. Seule la réponse « Je me replace à droite » est certaine. | exam.md §3.1 Q7, §3.3 ; relecture v1 n° 35 |
| **Distance d'arrêt = (dizaines)²** | Convention d'auto-école majoritaire gardée en cloze ; l'explication de `c-distance-arret-formule` rappelle la lecture « freinage » d'EVS/Ornikar et les 28/70/129 m de la Sécurité routière. | legal-facts A6 et J2 ; knowledge-facts C4 ; relecture v1 n° 7 |
| **Sol mouillé : ×1,5 ou ×2 ?** | La Q13 officielle dit « 2 fois » : c'est la valeur du cloze ; le ×1,5 reste en explication. | exam.md §3.1 Q13 |
| **Barème du champ visuel** | Clozes uniquement sur 180° / 45° / 30° (valeurs officielles) ; 100° et 75° restent en texte non masqué. | legal-facts G2, J2 ; relecture v1 n° 9 |
| **Ordre clignotant / angle mort** | Deux écoles (Codeclic-Ornikar vs Stych). Retenu : rétros → clignotant → angle mort, avec la divergence signalée dans l'explication de `c-ordre-controles-changement-file`. | knowledge-facts C12 (« À VÉRIFIER ») |
| **Alcool + cannabis : ×15 ou ×29 ?** | ×29 en cloze (`c-stupefiants-stats`, valeur securite-routiere.gouv.fr), ×15 mentionné en explication comme valeur des anciens supports. | knowledge-facts C6/C7 ; relecture v1 n° 39 |
| **Somnolence : « 1 accident mortel sur 3 » sur autoroute** | Gardé (c'est la valeur de campagne que l'examen reprend), avec la nuance ONISR (4 % tous réseaux, 8-14 % sur autoroute) en explication. | legal-facts H3/H4 ; relecture v1 n° 11 |
| **Pic d'alcoolémie : 15-30 min ou 30 min ?** | « 15 à 30 min à jeun, 1 h au cours d'un repas » : fourchette des auto-écoles, compatible avec les « ≈ 30 min » de la Sécurité routière. | knowledge-facts C6 |
| **Pictogramme médicament en carte de reconnaissance** | La carte des connaissances note « R + F » ; seul le fait existe. Le générateur `pictogramme_medicament` affiche le niveau **et** son texte : une carte image donnerait la réponse. Aucune carte image n'a donc été créée ; à trancher si l'on veut un rendu partiel du générateur (hors périmètre : `build/`). | brief §4 ; `build/gen_images.py` |
| **`c-angle-mort-definition` / `aff-c-retros-suffisent`** | Recouvrement assumé : la question porte la définition et le geste (vocabulaire « angle mort » utilisé par tous les autres thèmes), l'affirmation porte le piège « mes rétroviseurs bien réglés me suffisent ». Conservées toutes les deux. | brief § 2 règle 8 |
| **`aff-c-aac-accidents`** | Recouvre partiellement `d-aac` / `d-accompagnateur` (thème D, chiffres de la filière). Conservée car l'énoncé porte sur le **surrisque novice**, ligne C « jeunes conducteurs (surrisque) », et non sur les règles de l'AAC. | 02-carte-des-connaissances §C ; knowledge-facts C10/C11 |

### Sources consultées

`docs/research/brief-v2-redaction.md` ; `docs/05-audit-v2.md` §2.1, §2.2, §2.5 ;
`docs/01-analyse-examen.md` ; `docs/research/exam.md` §3.1 (20 questions verbatim), §3.2, §4.3 ;
`docs/02-carte-des-connaissances.md` (section C) ; `docs/research/knowledge-facts.md` C1 → C14 ;
`docs/research/legal-facts.md` A6, B, G, H ; `docs/research/review-facts-questions.md` (faits n° 7-14,
questions n° 34-40 et la synthèse) ; `docs/research/sources/cdr.txt` (articles listés au § 3).

---

## 5. Comptage final

| Fichier | Notes | Cartes Anki |
|---|---|---|
| `data/questions/03_conducteur.yaml` | 25 | 25 |
| `data/faits/03_conducteur.yaml` | 21 | 56 (clozes distincts) |
| `data/affirmations/03_conducteur.yaml` | 42 | 42 |
| **Total thème C** | **88 notes** | **123 cartes** |

- Affirmations : **20 vrai / 22 faux** (48 % de vrai ; cible du build : 35-65 %).
- Importance : 25 questions dont 2 `utile` ; 42 affirmations dont 7 `utile` ; 21 faits tous `essentiel`.
- Sous-thèmes utilisés : `perception`, `vigilance`, `distances`, `deficiences` (identiques à la v1 ;
  `distances` apparaît pour la première fois côté questions avec `c-suiveur-trop-pres`).
- `python -m build.build --check` ne signale **aucune** erreur sur les trois fichiers.
- Cible de `05-audit-v2.md` §2.5 (« C ≈ 130 cartes ») : 123, sans carte de remplissage.
