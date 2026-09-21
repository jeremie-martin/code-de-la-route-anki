# v2 — Thèmes M (mécanique et équipements) et S (sécurité du passager et du véhicule)

Périmètre : `data/questions/09_mecanique.yaml`, `data/faits/09_mecanique.yaml`,
`data/affirmations/09_mecanique.yaml` (nouveau), `data/questions/10_securite_passager.yaml`,
`data/faits/10_securite_passager.yaml`, `data/affirmations/10_securite_passager.yaml` (nouveau).
`data/reconnaissance/voyants.yaml` n'a pas été touché ; aucune carte ne le redouble.

## 1. Répartition M / S des aides à la conduite (point B du brief)

Règle appliquée : **la fonction et les limites d'un système vont dans M (`sous_theme: adas`)** ;
**ce qui protège les occupants reste dans S** (ceinture, airbag, appuie-tête, sièges enfants,
chargement, remorque, sécurité active/passive). Conséquences :

| Système | v1 | v2 | Carte |
|---|---|---|---|
| ABS (fonction, freinage d'urgence) | M `m-freinage-urgence-abs` **et** S `s-abs-fonction` (doublon) | M seul | `m-freinage-urgence-abs` + 3 affirmations |
| ESP | S | **M** | `s-esp-fonction` (id conservé, `theme: M`, `sous_theme: adas`) |
| AFU | S | **M** | `s-afu-fonction` (id conservé) |
| Régulateur / limiteur | S | **M** | `s-regulateur-limiteur` (id conservé) + 3 affirmations |
| eCall | S | **M** | `s-ecall` (id conservé, réponse resserrée) |
| Alerte de franchissement, maintien de voie, angle mort | M `m-ldw-lka-angle-mort` (58 mots) | M | `m-ldw-lka`, `m-adas-responsabilite`, `aff-m-angle-mort-moto` |
| Limites générales des ADAS | S `s-adas-limites` (7 éléments) | **M** | `m-adas-responsabilite` |
| Aide au stationnement | S `s-adas-limites` + P `p-assistance-stationnement` | **décision en P, piège en M** | `aff-m-stationnement-arriere` (Q8) — la décision reste `p-assistance-stationnement`, non dupliquée |
| Allumage automatique | nulle part | **M** | `m-allumage-automatique` |
| Conduite partiellement automatisée | M | M | `m-conduite-automatisee` |
| Sécurité active vs passive, Euro NCAP | S | **S** | `s-securite-active-passive`, `aff-s-abs-passive`, `aff-s-euroncap-pietons` |

Les ids déplacés sont conservés (`guid_for(kind, id)` ne dépend pas du fichier : l'historique de
révision est préservé, seul le sous-deck change).

## 2. Cartes-listes découpées (point A) — id supprimé → ids créés

### 09_mecanique.yaml (21 erreurs de build)

| Supprimé | Motif | Remplacé par |
|---|---|---|
| `m-voyant-moteur-clignote` (45 mots) | doublon du verso de reconnaissance `voyant-moteur` | rien (le voyant le dit déjà) |
| `m-pneus-sous-gonflage` (5 éléments) | doublon partiel de `e-pneus-conso` (thème E) | `aff-m-surgonflage`, `aff-m-chargement-pression`, `aff-m-pression-chaud` |
| `m-pneus-marquage` (49 mots) | hors carte des connaissances (M2 liste « âge », pas le marquage) | `aff-m-pneu-age` ; le marquage reste en explication de `m-pneus-usure-1-6` |
| `m-pneus-hiver-chaines` (48 mots) | doublon de `r-loi-montagne` et `r-neige-conduite` (thème R) | `aff-m-4-saisons-3pmsf` |
| `m-roue-galette` | le chiffre 80 km/h vit déjà dans le fait `m-galette-chiffres` | explication de `m-changer-roue-securite` |
| `m-amortisseurs-plaquettes` (46 mots, 2 sujets) | deux connaissances en une | `m-plaquettes-usure` (amortisseurs en explication) |
| `m-panne-freins` | réécrite (41 mots → 25) | `m-panne-freins` (conservé, `utile`) + `aff-m-frein-main-4-roues` |
| `m-feux-liste` (52 mots, 13 feux) | liste d'équipement, jamais demandée telle quelle | `aff-m-brouillard-arriere-pluie`, `aff-m-feu-grille-nuit`, `m-feux-jour-limite` (réécrite), `m-feux-reglage-hauteur` (réécrite) + le fait `m-feux-portees` qui porte déjà les portées |
| `m-ldw-lka-angle-mort` (58 mots) | trois systèmes en une carte | `m-ldw-lka`, `m-adas-responsabilite`, `aff-m-angle-mort-moto` |
| `m-changer-roue` (11 étapes) | procédure | `m-changer-roue-securite`, `m-changer-roue-ecrous` |

Réécrites sans changement d'id (réponse ≤ 40 mots, ≤ 4 éléments) : `m-pneus-pression-quand`,
`m-niveau-huile`, `m-liquide-frein`, `m-batterie-cables`, `m-carburants-etiquettes`,
`m-boite-auto-positions`, `m-feux-jour-limite`, `m-feux-reglage-hauteur`, `m-appel-phares`,
`m-conduite-automatisee`, `m-panne-procedure-route`, `m-crevaison-eclatement`, `s-ecall`.

### 10_securite_passager.yaml (8 erreurs de build)

| Supprimé | Motif | Remplacé par |
|---|---|---|
| `s-abs-fonction` | doublon de `m-freinage-urgence-abs` | `aff-m-abs-distance`, `aff-m-abs-direction`, `aff-m-abs-pedale` |
| `s-adas-limites` (7 éléments) | liste de systèmes | `m-adas-responsabilite`, `aff-m-stationnement-arriere` |
| `s-securite-active-passive` (10 éléments) | liste | conservé, réécrit en une opposition (exemples en explication) + `aff-s-abs-passive` |
| `s-coffre-toit` (5 éléments) | liste | conservé, réécrit + `aff-s-coffre-toit-lourd` |

Réécrites sans changement d'id : `s-ceinture-obligation`, `s-groupes-sieges`,
`s-chargement-depassement`, `s-remorque-permis-b`.

## 3. Ajouts (point C) — avec la ligne visée de `02-carte-des-connaissances.md`

### M — questions
| Id | Ligne de la carte des connaissances |
|---|---|
| `m-plaquettes-usure` | M · « freins (plaquettes, ABS…, AFU) » |
| `m-erreur-carburant` | M · « carburants (E10, SP95/98, gazole, GPL ; **erreur de carburant**) » |
| `m-adas-responsabilite` | M · « ADAS : … aide au stationnement, détecteur d'angle mort, AEB, alerte de franchissement » |
| `m-ldw-lka` | M · « ADAS : … alerte de franchissement » |
| `m-allumage-automatique` | M · « ADAS : … **allumage automatique** » |
| `m-changer-roue-securite`, `m-changer-roue-ecrous` | M · « Dépannage : triangle 30 m, gilet…, crevaison » |
| `m-remorquage` | M · « Dépannage : … **remorquage** » |

### M — affirmations (26 ; 12 vrai / 14 faux = 46 %)
- Voyants (`tableau_de_bord`) : `aff-m-voyant-orange-arret`, `aff-m-autotest-voyants`,
  `aff-m-voyant-abs-blocage` (Q5 officielle, VRAI), `aff-m-voyant-abs-arret` (Q5, FAUX).
- Freinage : `aff-m-abs-distance` (FAUX), `aff-m-abs-pedale`, `aff-m-abs-direction`,
  `aff-m-frein-main-4-roues`.
- Pneus : `aff-m-pression-chaud`, `aff-m-chargement-pression` (Q1 officielle, distracteur A),
  `aff-m-surgonflage`, `aff-m-pneus-neufs-arriere`, `aff-m-pneu-age`, `aff-m-4-saisons-3pmsf`.
- Entretien : `aff-m-refroidissement-bouchon`, `aff-m-boite-auto-p-arret`.
- Feux : `aff-m-brouillard-arriere-pluie`, `aff-m-reglage-feux-charge` (Q1, proposition C, VRAI),
  `aff-m-feu-grille-nuit`.
- ADAS : `aff-m-stationnement-arriere` (Q8), `aff-m-regulateur-obstacle`,
  `aff-m-regulateur-conditions`, `aff-m-limiteur-descente`, `aff-m-angle-mort-moto`, `aff-m-ecall-15`.
- Dépannage : `aff-m-detresse-bouchon` (R416-18).

### S — questions
| Id | Ligne visée |
|---|---|
| `s-surnombre` | S · « Ceinture : tous… » + E9 du dossier (R412-1-1, une place = une personne) |
| `s-remorque-conduite` | S · « remorque 750 kg, PTAC » (conduite d'un attelage) |

### S — affirmations (20 ; 8 vrai / 12 faux = 40 %)
- Ceinture et occupants : `aff-s-passagere-arriere-danger` (Q12 officielle, VRAI),
  `aff-s-ceinture-majeur-amende`, `aff-s-airbag-remplace-ceinture`, `aff-s-ceinture-manteau`,
  `aff-s-appuie-tete-securite`, `aff-s-airbag-pieds`, `aff-s-animal-libre`.
- Enfants : `aff-s-enfant-10-ans-avant`, `aff-s-enfant-135-cm`, `aff-s-enfant-genoux`,
  `aff-s-siege-manteau`, `aff-s-isofix`.
- Chargement et remorque : `aff-s-chargement-distance-arret`, `aff-s-plage-arriere`,
  `aff-s-chargement-avant`, `aff-s-coffre-toit-lourd`, `aff-s-caravane-passager`,
  `aff-s-remorque-retroviseurs`.
- Équipements : `aff-s-abs-passive`, `aff-s-euroncap-pietons`.

Toutes les affirmations fausses reprennent un piège documenté (knowledge-facts E10 « Pièges /
idées reçues, thèmes M et E ») ou un distracteur d'une question officielle (Q1, Q5, Q8, Q12).

## 4. Doublons évités (rien ajouté sur ces points)

- **Voyants** : aucune carte ne reprend le sens d'un voyant ; seules les deux affirmations de la
  question officielle Q5 (ABS) et le code couleur (`m-voyants-couleurs`) restent côté question.
- **Thème R** : usage des feux par temps de pluie/brouillard/nuit (`r-pluie-feux`, `r-brouillard-feux`,
  `r-nuit-feux-croisement-route`), loi Montagne et chaînes (`r-loi-montagne`, `r-neige-conduite`),
  panne sur autoroute (`r-autoroute-panne`), freinage en descente (`r-descente-freinage`).
  M ne garde que l'angle **équipement** (portées, réglage, feux de jour, appel de phares).
- **Thème P** : installation (`p-appuie-tete`, `p-ceinture-position`, `p-siege-reglage`),
  chargement avant départ (`p-verif-chargement-important`), quitter un stationnement
  (`p-quitter-stationnement-surveiller`, Q14), assistance au stationnement (`p-assistance-stationnement`, Q8).
- **Thème D** : gilet/triangle/éthylotest/extincteur (`d-equipements-obligatoires`), vitres teintées
  (`d-vitres-teintees`), sanctions de la ceinture (`d-ceinture-sanction`).
- **Thème E** : consommation (coffre de toit, pneus sous-gonflés, motorisations, recharge VE).
- **Thème A** : protéger un accident, triangle à 30 m, gilet avant de sortir.

## 5. Corrections de la relecture v1 vérifiées comme appliquées

n° 21 `m-galette-chiffres` (période des pneus cloutés en explication), n° 22 `s-enfant-chiffres`
(i-Size), n° 23 `s-airbag-chiffres` (« au moins 25 cm environ »), n° 58 `m-appel-phares` (phrase sur
les contrôles de police supprimée), n° 59 `s-animaux` (35 €, 2e classe), n° 60 `s-remorque-permis-b`
(PTRA, 90/80/80), n° 61 `s-ceinture-50-kmh` (75 kg → 2,5 t), n° 62 `s-ecall` (31 mars 2018).

## 6. Valeurs vérifiées dans `docs/research/sources/cdr.txt`

- `R. 412-6-3` : l'aide au stationnement n'est activée que par un conducteur qui « assure le contrôle
  de la manœuvre » et « est à tout instant en capacité de mettre fin à cette manœuvre » (fonde
  `aff-m-stationnement-arriere` et confirme la réponse de la question officielle Q8).
- `R. 416-1` / `R. 416-2` : avertisseur sonore limité au danger immédiat en agglomération ; de nuit
  l'avertissement se donne par allumage intermittent des feux (`m-appel-phares`).
- `R. 416-7` II : feux arrière de brouillard « qu'en cas de brouillard ou de chute de neige »
  (`aff-m-brouillard-arriere-pluie`).
- `R. 416-18` : feux de détresse obligatoires en allure fortement réduite ; en file ininterrompue,
  seul le dernier véhicule (`aff-m-detresse-bouchon`).
- `R. 416-19` : triangle + feux de détresse quand le véhicule immobilisé est un danger
  (`m-panne-procedure-route`).
- `R. 312-21` (3 m à l'arrière, 4e classe) et `R. 312-22` (aucun dépassement à l'avant, 3e classe =
  68 €) : `s-chargement-depassement`, `aff-s-chargement-avant`.
- `R. 412-1-1` : une personne par siège, dans la limite de la carte grise ; 4e classe, 3 points
  (`s-surnombre`, `aff-s-enfant-genoux`, `aff-s-caravane-passager`).
- `R. 412-2` / `R. 412-3` : retenue homologuée < 10 ans, avant interdit < 10 ans sauf dos à la route
  avec airbag désactivé (`aff-s-enfant-10-ans-avant`, `aff-s-enfant-135-cm`).
- `R. 316-6` : systèmes de vision indirecte sans angle mort notable (`aff-s-remorque-retroviseurs`).
- `R. 314-1` + arrêté du 18 juillet 2019 : 1,6 mm et témoins d'usure ; `D. 314-8` : 3PMSF depuis le
  1er novembre 2024.

## 7. Doutes restants

1. **« 25 cm » au volant** (`s-airbag-distance`, `s-airbag-chiffres`, `p-siege-reglage`) : source
   unique (Ornikar), marquée « À VÉRIFIER » dans knowledge-facts E2. Conservé comme ordre de grandeur
   (« au moins 25 cm environ »), conformément à la relecture v1 n° 23.
2. **Facteur du poids apparent** : knowledge-facts E1 donne « ×25 » (enfant de 20 kg à 50 km/h) et la
   relecture v1 « ×33 » (75 kg → 2,5 t). Les cartes évitent désormais d'énoncer un facteur : elles
   gardent les valeurs sourcées (2,5 t, objet de 300 g = boule de bowling, chute de 3 étages).
3. **Charge de toit « 50-75 kg »** (`s-coffre-toit`) : knowledge-facts E6 donne « ~75-100 kg selon la
   notice ». La carte renvoie à la notice constructeur plutôt qu'à un chiffre ; l'ordre de grandeur
   cité reste indicatif. À harmoniser si une source officielle est trouvée.
4. **Vitesse avec chaînes (~50 km/h)** : préconisation des fabricants, pas un texte (legal-facts E5).
   Aucune carte de M ne l'affirme ; elle reste en explication du fait `m-galette-chiffres` et de
   `r-neige-conduite` (thème R).
5. **« Feu défaillant : 68 € »** : knowledge-facts M5 et service-public F19459 (3e classe) ;
   l'article n'est pas chiffré dans le code. Conservé (`aff-m-feu-grille-nuit`), avec l'immobilisation
   possible qui est, elle, la vraie conséquence testée.
6. **Aide au stationnement** : la décision reste dans le thème P (`p-assistance-stationnement`) bien
   que la règle B du brief rattache les ADAS à M, parce que le fichier 08 est hors périmètre et qu'une
   seconde carte de décision aurait été un doublon. M porte le piège sous forme d'affirmation.

## 8. Comptages finaux

| Thème | Reconnaissance | Confusions | Faits (notes / cartes) | Questions | Affirmations | **Cartes** |
|---|---|---|---|---|---|---|
| M — Mécanique et équipements | 26 | 3 | 5 / 16 | 29 | 26 (12 vrai / 14 faux, 46 %) | **100** |
| S — Sécurité du passager et du véhicule | 0 | 0 | 5 / 16 | 16 | 20 (8 vrai / 12 faux, 40 %) | **52** |

Cible du brief : M ≈ 85-100, S ≈ 45-55 — atteinte.
v1 : M = 71 cartes (dont ADAS : 1 note essentielle + 2 utiles), S = 36.
`python -m build.build --check` ne signale plus rien sur ces fichiers (validation globale OK).
