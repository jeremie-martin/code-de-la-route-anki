# Thème U — Les autres usagers : rapport de réécriture v2

Périmètre : `data/questions/05_autres_usagers.yaml`, `data/faits/05_autres_usagers.yaml`,
`data/affirmations/05_autres_usagers.yaml` (créé). Cadre : `docs/research/brief-v2-redaction.md`,
`docs/05-audit-v2.md` §2.1, §2.2, §2.5 (U trop mince : 47 cartes pour 4-5 questions ; objectif ≈ 80).

## 1. Comptage

| | v1 (`git show HEAD:`) | v2 |
|---|---|---|
| Questions | 28 | 34 |
| Faits (notes / cartes cloze) | 6 / 17 | 8 / 24 |
| Affirmations | 0 | 32 (13 vrai / 19 faux = **40,6 % de vrai**) |
| **Cartes** | **≈ 45-47** | **90** |

Importance : 67 `essentiel`, 7 `utile`, 0 `rare`.
Répartition par sous-thème : piétons 15, cyclistes 14, motos 11, poids lourds 10, EDPM 7,
véhicules prioritaires 7, véhicules lents/animaux 6, transports en commun 4.
`python -m build.build --check | grep 05_autres` ne renvoie rien.

## 2. Cartes v1 supprimées → ce qui les remplace

Ces six questions-listes ont été décomposées (1er passage de réécriture) ; rien n'est perdu.

| id v1 supprimé | remplacé par |
|---|---|
| `u-sas-velo` | `marq-sas-velo` (reconnaissance/marquages, déjà existant : arrêt à la 1re ligne) + `m12` (panonceaux) + **`aff-u-velo-m12`** (le M12 n'est pas une priorité) |
| `u-velo-piste-obligatoire` | `conf-b22a-c113` (confusion rond/carré, déjà existante) + **`aff-u-velo-bande-obligatoire`** (obligation seulement si B22a) |
| `u-velo-equipements` | fait `u-velo-equipement-chiffres` (2 freins, feux, catadioptres, avertisseur 50 m) |
| `u-cycliste-equipements` | fait `u-velo-chiffres` (casque < 12 ans, gilet, < 8 ans, 2 de front) + **`aff-u-velo-casque-enfant-adulte`**, **`aff-u-velo-ecouteurs`**, **`aff-u-velo-enfant-trottoir`** |
| `u-edpm-regles` | fait `u-edpm-chiffres` (14 ans, 25 km/h, seul, assurance) + **`aff-u-edpm-gilet-agglo`** + question **`u-edpm-hors-agglo`** |
| `u-moto-equipements` | fait `u-moto-equipements-chiffres` (casque 3 pts, gants CE, gilet à bord) + **`aff-u-moto-feux-jour`** (R416-17) |

Les 22 autres ids v1 sont **conservés** (ids stables) et réécrits en décision située
(« Un tramway est arrêté à sa station et des voyageurs descendent de mon côté : puis-je le dépasser ? »
au lieu de « Un tramway est arrêté… Puis-je le dépasser ? » réponse-fiche).

Connaissances v1 réinjectées ailleurs plutôt que perdues : R412-25 (voie de gauche interdite aux PL sur
3 voies) → `aff-u-pl-voie-gauche` ; clichés radar vérifiés par un OPJ → `aff-u-prioritaire-feu-rouge-radar` ;
R412-33 (convoi engagé garde la priorité au feu vert) → `aff-u-convoi-feu-vert` ; priorité du tram →
`aff-u-tram-priorite-droite` (la règle générale reste dans `r-tram-priorite`, thème R).

## 3. Corrections apportées au 1er passage (relecture critique)

1. **`u-cycliste-tourner-droite`** — la question parlait d'une *bande* cyclable en invoquant R415-14, qui ne
   vise que la *piste* cyclable (« considérée comme une voie de la chaussée principale qu'elle longe »,
   vérifié dans `sources/cdr.txt`). Recto passé à « piste cyclable » ; la bande est traitée dans l'explication.
2. **`u-cycliste-bras-gauche`** — l'explication disait « le dépasser par la droite n'est possible que si la
   place suffit ». R414-6 II 1° impose au contraire de dépasser **par la droite** un usager qui a signalé
   qu'il se porte à gauche. Explication corrigée.
3. **`u-pieton-hors-agglo-cote`** — « un piéton sombre n'est vu qu'à 30 m en feux de croisement » est un
   raccourci (les 30 m sont la portée des croisements, pas une distance de détection d'un piéton). Retiré
   de la carte ; la connaissance exacte est portée par `aff-u-pieton-nuit-croisement`.
4. **`u-personnes-agees`** — la source citait R412-30 (feux de signalisation), sans rapport. Remplacée par
   R415-11 + ONISR 2025.
5. **Fait `u-velo-equipement-chiffres`** — l'explication affirmait « depuis novembre 2024, un feu porté sur
   le cycliste est admis et des feux clignotants sont autorisés » : aucune trace dans `legal-facts.md`,
   `knowledge-facts.md` ni `cdr.txt`. Remplacée par le rôle des catadioptres (visibilité latérale).
6. **Faits `u-pl-angles-morts-chiffres`, `u-moto-equipements-chiffres`, `u-motos-mortalite`** — explications
   allégées des phrases désormais portées par une affirmation (règle du rétroviseur, feux de jour,
   « je ne l'ai pas vue »), pour ne pas répéter la même connaissance sous deux formes (brief §2.8).
7. Valeurs re-vérifiées une à une dans `docs/research/sources/cdr.txt` : R412-34 (< 8 ans, assimilés
   piétons), R412-35/36 (fauteuil roulant, bord gauche hors agglo), R412-37 (50 m), R412-9 (écart aux
   portières ≤ 50 km/h), R412-12 (50 m entre PL), R412-25, R412-28-1 (double-sens ≤ 30 km/h),
   R412-33, R412-43-1 (EDPM), R412-6-1 (écouteurs), R413-17 III, R414-4 IV (1 m / 1,50 m), R414-6,
   R415-5, R415-12, R415-14, R416-17, R417-11, R422-3, R431-7 (décret 2024-1074), R431-9,
   R412-11-3 (décret 2025-33 : ≥ 70 km/h, 2 files les plus à gauche, 50/30 km/h). Aucune divergence
   trouvée avec les cartes en place.

## 4. Ajouts v2 et ligne visée dans `docs/02-carte-des-connaissances.md`

La carte des connaissances ne comporte que deux lignes pour U :
**(L1)** piétons / cyclistes / EDPM ; **(L2)** motos-cyclomoteurs, PL, bus-cars, tram, véhicules d'intérêt
général, convois, engins agricoles, animaux, cavaliers, personnes handicapées (CMI), voiturettes.

### 4.1 Questions ajoutées (5) — décisions situées manquantes

| id | ligne | comble |
|---|---|---|
| `u-edpm-hors-agglo` | L1 « EDPM » | où un EDPM peut rouler *hors* agglomération (point de vue de l'usager) |
| `u-moto-ecart-chaussee` | L2 « Motos/cyclomoteurs » | l'écart du motard (plaques, gravillons, rails) et la réaction attendue |
| `u-pl-insertion-autoroute` | L2 « PL » | faciliter l'insertion d'un PL chargé (R421-3, R414-2) |
| `u-troupeau-animaux` | L2 « animaux » | troupeau sur la chaussée : ralentir, s'arrêter, ne pas klaxonner |
| `u-voiturette` (utile) | L2 « voiturettes » | quadricycle léger : 45 km/h par construction, permis AM à 14 ans |

### 4.2 Affirmations ajoutées (32) — forme dominante de l'épreuve (audit §2.2)

Treize se placent du **point de vue de l'autre usager** (pictogramme, `exam.md` §3.2 forme 9) :
piéton (`aff-u-pieton-passage-50m`, `aff-u-pieton-nuit-croisement`), cycliste
(`aff-u-velo-bande-obligatoire`, `aff-u-velo-front-nuit`, `aff-u-velo-casque-enfant-adulte`,
`aff-u-velo-ecouteurs`, `aff-u-velo-double-sens-zone30`), trottinette (`aff-u-edpm-trottoir`,
`aff-u-edpm-pousse-main`, `aff-u-edpm-gilet-agglo`), motard (`aff-u-interfiles-vitesse`,
`aff-u-interfiles-files-gauche`, `aff-u-moto-vitesse-approche`).

- **Piétons (7, L1)** : `aff-u-pieton-telephone` (V), `aff-u-pieton-imprudent` (F, R412-6),
  `aff-u-pieton-passage-50m` (V), `aff-u-place-pmr` (F, CMI — seule carte U sur les personnes
  handicapées), `aff-u-fauteuil-roulant-pieton` (V), `aff-u-car-scolaire-depassement` (F : aucun texte
  n'interdit le dépassement, R413-17 impose de réduire la vitesse), `aff-u-pieton-nuit-croisement` (V).
- **Cyclistes (8, L1)** : `aff-u-velo-bande-obligatoire` (F), `aff-u-velo-front-nuit` (F),
  `aff-u-velo-enfant-trottoir` (F : *moins de* 8 ans), `aff-u-velo-casque-enfant-adulte` (V),
  `aff-u-velo-ecouteurs` (F), `aff-u-velo-double-sens-zone30` (V), `aff-u-velo-m12` (F),
  `aff-u-velo-ecart-portieres` (V).
- **EDPM (3, L1)** : `aff-u-edpm-trottoir` (F), `aff-u-edpm-pousse-main` (V), `aff-u-edpm-gilet-agglo` (V).
- **Motos (5, L2)** : `aff-u-interfiles-vitesse` (F), `aff-u-interfiles-files-gauche` (V),
  `aff-u-interfiles-panneau-autos` (F — **question officielle 2023 Q16**), `aff-u-moto-vitesse-approche` (F),
  `aff-u-moto-feux-jour` (V).
- **PL, bus, tram (5, L2)** : `aff-u-pl-retroviseur` (V), `aff-u-pl-voie-gauche` (F, R412-25),
  `aff-u-pl-distance-arret` (V), `aff-u-bus-hors-agglo` (F), `aff-u-tram-priorite-droite` (F).
- **Véhicules d'intérêt général et convois (4, L2)** : `aff-u-prioritaire-sans-avertisseur` (F),
  `aff-u-prioritaire-feu-rouge-radar` (F), `aff-u-prioritaire-route-prioritaire` (F, R415-12
  « en toutes circonstances »), `aff-u-convoi-feu-vert` (F, R412-33).

## 5. Contrôle des doublons

Vérifié par similarité (difflib) de chaque nouvelle affirmation et de chaque nouvelle question contre
l'ensemble des questions, scénarios et affirmations du deck. Deux voisinages assumés, avec un piège distinct :

- `aff-u-bus-hors-agglo` (0,56) vs `l-bus-quitte-arret` (02) : la question donne la règle **en**
  agglomération, l'affirmation teste l'idée reçue « le bus a toujours la priorité » **hors** agglomération
  (R412-11 ne vise que l'agglomération). C'est le piège listé dans `knowledge-facts.md`.
- `aff-u-place-pmr` vs `l-stationnement-tres-genant` (02, qui énumère les places PMR) : l'affirmation teste
  le distracteur « je ne fais que m'arrêter », alors que R417-11 vise « l'arrêt **ou** le stationnement ».
- `aff-u-velo-front-nuit` vs `u-cyclistes-de-front` : la question est du point de vue de l'automobiliste
  (le véhicule annonce son dépassement), l'affirmation du point de vue du cycliste à la chute du jour.

Cartes **écartées** parce que déjà portées ailleurs, et qui n'apportaient pas de piège nouveau :
« je peux m'avancer dans le sas vélo s'il est vide » (déjà dans `marq-sas-velo`.conduite) ;
« aire piétonne ≠ zone de rencontre » (déjà dans `b54`.piege) ; « gyrophare orange = priorité »
(déjà la question `u-gyrophare-orange`) ; « corridor de sécurité » (déjà `u-corridor-securite`) ;
distance latérale 1 m / 1,50 m (fait `l-depassement-laterale`, thème L) ; dépassement d'un cycliste sur
ligne continue (`l-depassement-cycliste-ligne-continue`, thème L) ; Q3 enfant, Q4 trottinette, Q7 cycliste,
Q11 détectabilité (transcrites en thème C : `aff-c-enfant-percoit-adulte`, `c-trottinette-vulnerable`,
`c-cycliste-devant-depassement`, `aff-c-pieton-detectable-motard`).

## 6. Doutes restants

1. **Priorité du tramway (`aff-u-tram-priorite-droite`, `u-tram-depasser`)** — R422-3 I donne la priorité
   aux matériels circulant sur la voie ferrée « à l'exception des véhicules de transport public […]
   dont les conducteurs doivent respecter les signalisations comportant des prescriptions absolues ».
   Lue à la lettre, cette exception retire au tram le bénéfice de l'article. Tous les supports
   pédagogiques et les cartes de reconnaissance du deck (`a9`, `c20c`, `b27b`) enseignent « le tramway est
   prioritaire, sauf signalisation contraire » : c'est la formulation retenue, cohérente avec
   `r-tram-priorite`. À revoir si une source officielle tranche autrement.
2. **`u-matieres-dangereuses` (plaque orange)** — `knowledge-facts.md` U5 marque la puce « À VÉRIFIER
   (exemple d'une seule source) ». La carte a été conservée (importance `utile`) parce que le fait est
   corroboré par les panneaux B18a/b/c du deck (accès interdit aux véhicules transportant des marchandises
   dangereuses) et par l'accord ADR ; seules la plaque orange et la distance accrue sont affirmées, pas le
   détail des codes.
3. **Allure du pas** — non définie par le code ; « ≈ 6 km/h » selon les sources pédagogiques, « < 4 km/h »
   selon d'autres (`knowledge-facts.md` U1, À VÉRIFIER). Aucune carte U ne chiffre l'allure du pas.
4. **Casque EDPM** — obligatoire par arrêtés locaux dans plusieurs départements (SP F308, base non
   identifiée). Les cartes s'en tiennent à la règle nationale : recommandé en agglomération, obligatoire
   hors agglomération sur les routes autorisées par dérogation.
5. **Survie du piéton selon la vitesse du choc** — chiffres non concordants entre sources
   (`knowledge-facts.md` U1, À VÉRIFIER) : aucune carte ne les reprend.
6. **`aff-u-velo-ecouteurs`** — R412-6-1 vise « tout conducteur d'un véhicule en circulation » ; le
   cycliste en est un (amende de 135 € confirmée par securite-routiere.gouv.fr). L'absence de retrait de
   points tient à ce qu'aucun permis n'est requis, non à une exemption : c'est ce que dit le verso.
