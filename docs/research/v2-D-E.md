# v2 — Thèmes D (réglementation) et E (environnement)

Périmètre : `data/faits/06_reglementation.yaml`, `data/questions/06_reglementation.yaml` (nouveau),
`data/affirmations/06_reglementation.yaml` (nouveau), `data/questions/11_environnement.yaml`,
`data/faits/11_environnement.yaml`, `data/affirmations/11_environnement.yaml` (nouveau).
Règles appliquées : `docs/research/brief-v2-redaction.md`, `docs/05-audit-v2.md` §2.1-§2.2.
`python -m build.build --check` ne signale plus rien sur ces six fichiers.

---

## 1. Thème D — Les notions diverses / réglementation

### 1.1 Faits à trous : conservés, vérifiés, resserrés

Les 41 notes sont conservées, avec leurs ids. Les valeurs ont été recontrôlées dans
`docs/research/legal-facts.md` C1-C7, D1-D4, E1-E5, I et, pour les articles cités, dans
`docs/research/sources/cdr.txt` (`L. 223-1`, `L. 234-1`, `L. 413-1`, `R. 412-1`, `R. 412-2`,
`R. 412-6-1`, `R. 413-15`, `R. 318-2`, `R. 323-22`) : aucune erreur de valeur trouvée. Les corrections
de la relecture v1 (`review-facts-questions.md` n° 15 à 19) étaient déjà appliquées et ont été
préservées (notamment la mention L237-1 dans `d-alcool-delit` et l'attribution « FAQ conduite
accompagnée » dans `d-accompagnateur`).

**Explications resserrées** (elles dépassaient 45 mots ; règle n° 9 du brief) :
`d-probatoire-3-points`, `d-recuperation-points`, `d-permis-17-ans`, `d-formation-minimale`,
`d-alcool-delit`, `d-stupefiants-delit`, `d-homicide-routier`, `d-documents-bord`,
`d-controle-technique`, `d-assurance-garanties`, `d-critair-prix`, `d-equipements-obligatoires`,
`d-stats-tues`, `d-consulter-points`. Aucune valeur n'a été supprimée : ce qui sortait de
l'explication est soit repris par une affirmation, soit sans valeur de décision.

**Clozes retirés** (−4 cartes, pour tenir l'objectif de volume du thème sans amputer une connaissance) :

| Note | Avant | Après | Ce qui passe en explication |
|---|---|---|---|
| `d-consulter-points` | 2 clozes | 1 (15 ans) | le nom du téléservice « Mes Points Permis » (administratif, hors carte des connaissances) |
| `d-stats-tues` | 4 clozes | 2 (3 263 tués ; 60 % hors agglomération) | « ≈ 9 par jour » (dérivable), « 77 % d'hommes » |
| `d-stats-usagers` | 3 clozes | 2 (voitures 47 %, 2RM 21 %) | piétons 15 %, cyclistes 7 %, EDPM 2 % |

### 1.2 Questions (nouveau fichier) — 2 décisions

Ligne de `02-carte-des-connaissances.md` visée : « Documents à bord … ; délais (adresse 1 mois, vente) ».

- `d-controle-papiers-oublies` — « Un agent me contrôle : je n'ai pas la carte grise sur moi. » →
  11 € et 5 jours pour présenter, sinon 135 €. *Formulé sur l'oubli et non sur « quels documents »,
  parce que la liste des documents est déjà le fait à trous `d-documents-bord` (règle n° 8).*
- `d-vente-vehicule` — ce que l'on remet à l'acheteur et la déclaration de cession. *Les délais
  (15 jours / 1 mois / CT de moins de 6 mois) restent en explication : ils sont déjà clozés dans
  `d-carte-grise-delais` et `d-controle-technique`.*

Le « changement d'adresse » et le « constat » demandés au cahier des charges sont traités en
affirmations (`aff-d-carte-grise-delai`, `aff-d-constat-desaccord`) plutôt qu'en questions, pour ne pas
doubler `d-carte-grise-delais` et `d-constat-declaration`.

### 1.3 Affirmations (nouveau fichier) — 24, 11 vrai / 13 faux (45,8 %)

| id | verdict | ligne de `02-…` | source |
|---|---|---|---|
| `aff-d-ceinture-passager-adulte` | faux | barème des retraits | R412-1, R412-2 |
| `aff-d-probatoire-alcool` | faux | permis probatoire / invalidation | R234-1, L223-5 |
| `aff-d-probatoire-majoration` | vrai | probatoire 6 (+2/an, +3/an AAC) | L223-1, R223-1 |
| `aff-d-invalidation-code-seul` | vrai | invalidation, récupération | L223-5 ; SP F1704 |
| `aff-d-invalidation-capital` | faux | invalidation | L223-1, R223-1 |
| `aff-d-recuperation-delai` | faux | récupération (6 mois / 2 ans / 3 ans) | L223-6 ; SP F1685 |
| `aff-d-velo-points` | faux | permis à points | SP F20443 |
| `aff-d-aac-points-eleve` | faux | AAC | SR — FAQ conduite accompagnée |
| `aff-d-grand-exces-delit` | vrai | grand excès (loi 2025) | L413-1 ; `cdr.txt` |
| `aff-d-clignotant-points` | faux | barème des retraits | R412-10 |
| `aff-d-detecteur-radar` | faux | détecteurs de radars | R413-15 ; `cdr.txt` |
| `aff-d-telephone-retention` | vrai | téléphone 3 pts / rétention | R412-6-1, L224-1, L224-2 |
| `aff-d-alcool-contravention` | faux | délits | L234-1, R234-1 |
| `aff-d-delit-fuite` | vrai | délit de fuite | CP 434-10 ; L231-1 |
| `aff-d-sans-assurance-points` | vrai | délit sans assurance | L324-2 ; C. assur. L211-1 |
| `aff-d-vignette-assurance` | faux | assurance dématérialisée FVA (04/2024) | décret 2023-1152 ; SP F1362 |
| `aff-d-permis-numerique` | vrai | permis dématérialisé | R233-1 ; SP F17970 |
| `aff-d-ct-tous-les-ans` | faux | contrôle technique (4 ans puis 2 ans) | R323-22, R323-27 |
| `aff-d-ct-defaillance-majeure` | vrai | contre-visite | SP F2878 |
| `aff-d-carte-grise-delai` | vrai | délais (adresse, vente) | R322-4, R322-5, R322-7 |
| `aff-d-assurance-tiers` | faux | RC / tiers / tous risques | C. assur. L211-1 ; SP F2655 |
| `aff-d-bonus-malus` | vrai | bonus-malus | C. assur. A121-1 ; SP F2655 |
| `aff-d-constat-desaccord` | vrai | constat amiable | C. assur. L113-2 ; SP F2149 |
| `aff-d-gilet-coffre` | faux | équipements obligatoires | R416-19 ; SP F19459 |

Deux formulations demandées ont été déplacées d'un cran pour éviter un doublon interdit par la
règle n° 8 :
- « En permis probatoire, je peux boire un verre et rester sous le seuil » existe déjà côté C
  (`aff-c-probatoire-un-verre`, thème C = doses et seuils). La carte D porte donc la **conséquence**
  (0,3 g/L la première année = 6 points = invalidation), qui est bien du ressort de D (sanctions).
- « Quels documents présenter à un contrôle » est déjà le fait `d-documents-bord` : la question D
  porte sur l'oubli d'un document.

### 1.4 Comptage D

104 cartes de faits (41 notes) + 2 questions + 24 affirmations = **130 cartes** (objectif 115-130).

---

## 2. Thème E — L'environnement

### 2.1 Cartes-listes supprimées → cartes créées

| id supprimé | motif (build) | remplacé par |
|---|---|---|
| `e-ecoconduite-principes` | 9 éléments | `e-feu-rouge-anticipation` (décision), `e-moteur-arret` (réécrit en situation), `aff-e-vitesse-stable`, `aff-e-ecoconduite-securite`, `aff-e-equipements-electriques` |
| `e-polluants` | 5 éléments | `e-polluant-co2`, `e-particules-usure`, `aff-e-diesel-nox` |
| `e-motorisations` | 49 mots | `e-electrique-avantages`, `e-e85`, `aff-e-ve-silence`, `aff-e-electrique-zero` |
| `e-pneus-conso` | — (doublon) | rien : `m-pneus-sous-gonflage` (thème M) couvre déjà risques **et** surconsommation ; le chiffre reste dans le cloze `e-surconsommations` |
| `e-vitesse-conso` | — (doublon) | rien : les chiffres sont les clozes de `e-vitesse-chiffres` ; le jugement est `aff-e-vitesse-stable` |
| `e-trajets-courts` | — (doublon) | `aff-e-trajets-courts` (l'idée reçue de `knowledge-facts` A6) ; les chiffres restent dans `e-trajets-courts-chiffres` |

### 2.2 Questions réécrites (erreurs du build corrigées sans changer d'id)

`e-critair-classes` (46 → 31 mots), `e-zfe-definition` (5 → 4 éléments), `e-pic-pollution`
(43 → 24 mots), `e-bruit-sources` (5 → 4), `e-ecomobilite-choix` (6 → 4), `e-covoiturage-voie`
(5 → 2), `e-ve-recharge` (44 → 21 mots), `e-moteur-arret` (question de barème → décision située à un
passage à niveau), `e-climatisation-conso` (question de chiffres → décision « clim ou vitres » en
ville, le couple autoroute étant porté par `aff-e-clim-autoroute`), `e-frein-moteur` (resserrée ; le
point mort part en affirmation).

Total : **17 questions** (18 avant).

### 2.3 Affirmations (nouveau fichier) — 18, 8 vrai / 10 faux (44,4 %)

Couvrent les six idées reçues demandées et le reste de `knowledge-facts` A6 :
`aff-e-clim-autoroute` (faux), `aff-e-point-mort-descente` (faux), `aff-e-moteur-chauffer` (faux),
`aff-e-trajets-courts` (faux), `aff-e-coffre-toit-vide` (faux), `aff-e-electrique-zero` (faux),
`aff-e-diesel-critair1` (faux), `aff-e-critair-renouvellement` (faux), `aff-e-zfe-supprimees` (faux),
`aff-e-borne-recharge` (faux) ; `aff-e-vitesse-stable` (vrai), `aff-e-ecoconduite-securite` (vrai),
`aff-e-equipements-electriques` (vrai), `aff-e-zfe-vignette` (vrai), `aff-e-pic-vitesse` (vrai),
`aff-e-diesel-nox` (vrai), `aff-e-ve-silence` (vrai), `aff-e-covoiturage-electrique` (vrai).

« En pic de pollution la vitesse est abaissée de 20 km/h » est **vraie** : elle sert précisément à
casser le réflexe « toute affirmation qui ressemble à une idée reçue est fausse » (`aff-e-pic-vitesse`).

Décisions d'écoconduite situées demandées : le feu rouge à 100 m (`e-feu-rouge-anticipation`) et
l'arrêt de plus de 20-30 s (`e-moteur-arret`) sont des questions ; « rapport engagé ou point mort en
descente » est porté par `aff-e-point-mort-descente` seule, parce que la **technique** de freinage en
longue descente est déjà `r-descente-freinage` (thème R, question officielle Q18) : en faire une
question E aurait créé un troisième exemplaire de la même connaissance.

### 2.4 Comptage E

16 cartes de faits (6 notes, inchangées) + 17 questions + 18 affirmations = **51 cartes**
(objectif 45-55).

---

## 3. Doutes et points de vigilance

1. **`e-vitesse-chiffres` (fait conservé)** — « 130 → 110 ≈ −20 à −25 % » est marqué « À VÉRIFIER »
   dans `knowledge-facts` A1. La note ne clozé que « −1 L/100 km par −10 km/h » et « 4 minutes sur
   100 km », qui sont sourcés (Ornikar, EVS/Codeclic) ; la fourchette −20/−25 % a été retirée de la
   question supprimée `e-vitesse-conso` et n'apparaît sur aucune carte.
2. **Climatisation** — les pourcentages divergent (Codeclic +10 / +25, Ornikar +3 à +5, ADEME +10 en
   moyenne). Le cloze du fait `e-surconsommations` garde « +10 % sur route, jusqu'à +25 % en ville » ;
   la question ne reprend plus de chiffre, pour ne pas figer une valeur discutée.
3. **« La climatisation sert à désembuer »** — vrai en pratique, mais absent des deux dossiers de
   recherche : aucune carte ne l'affirme (une affirmation envisagée a été remplacée par
   `aff-e-equipements-electriques`, sourcée en A1).
4. **Moteur tournant à l'arrêt** — l'interdiction (arrêté du 12 novembre 1963) est reprise, mais le
   montant de l'amende est « À VÉRIFIER » dans `knowledge-facts` A2 : aucune carte ne le chiffre.
5. **Losange « covoiturage »** — base réglementaire pérenne non retrouvée (`legal-facts` F5, J2). Les
   cartes citent L411-8 et l'IISR 9e partie, conformément à la correction n° 68 de la relecture v1.
6. **`aff-d-aac-points-eleve`** — repose sur la FAQ conduite accompagnée de la Sécurité routière, pas
   sur un article du code (même doute que `d-accompagnateur`, relecture v1 n° 19). L'attribution est
   explicite dans le verso.
7. **ZFE** — `aff-e-zfe-supprimees` est datée (censure du Conseil constitutionnel du 21 mai 2026,
   décision n° 2026-903 DC). À revérifier si une loi spécifique est votée : c'est la seule carte du
   périmètre dont la réponse pourrait basculer.
8. **Statistiques ONISR (`d-stats-tues`, `d-stats-usagers`)** — la carte des connaissances ne liste
   aucune ligne « statistiques » sous D. Les notes sont conservées (elles restent `utile`) mais
   ramenées à 2 clozes chacune, le reste passant en explication.

## 4. Récapitulatif des comptages

| Fichier | Notes | Cartes |
|---|---|---|
| `faits/06_reglementation.yaml` | 41 | 104 |
| `questions/06_reglementation.yaml` | 2 | 2 |
| `affirmations/06_reglementation.yaml` | 24 | 24 |
| **Thème D** | **67** | **130** |
| `faits/11_environnement.yaml` | 6 | 16 |
| `questions/11_environnement.yaml` | 17 | 17 |
| `affirmations/11_environnement.yaml` | 18 | 18 |
| **Thème E** | **41** | **51** |

Équilibre des affirmations : D 11 vrai / 13 faux (45,8 %), E 8 vrai / 10 faux (44,4 %) — dans la
fourchette 35-65 % exigée par le build.
