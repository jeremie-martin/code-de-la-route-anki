# v2 — thèmes A (Porter secours, sous-deck 07) et P (Prendre et quitter son véhicule, sous-deck 08)

Rapport de rédaction (brief `docs/research/brief-v2-redaction.md`, audit `docs/05-audit-v2.md` §2.1-2.2).
Périmètre : `data/{questions,faits,affirmations}/07_premiers_secours.yaml` et `…/08_prendre_quitter.yaml`.
Le premier passage (réécriture de 07) a été relu puis complété ; 08 a été réécrit et complété ici.

## 1. Comptages finaux

| Thème | Questions | Faits | Affirmations | Total | Cible |
|---|---|---|---|---|---|
| A — Porter secours | 14 | 8 | 14 (6 vrai / 8 faux = 43 %) | **36** | ~30-35 |
| P — Prendre et quitter | 21 | 2 | 15 (6 vrai / 9 faux = 40 %) | **38** | ~35-45 |

`python -m build.build --check` ne signale plus rien sur `07_premiers` ni sur `08_prendre`
(les erreurs restantes portent sur 09, 10 et 11, hors périmètre).

## 2. Thème A — cartes supprimées → cartes créées

v1 : 11 questions + 8 faits. Les faits sont inchangés (sauf la correction n° 20 de
`review-facts-questions.md`, déjà appliquée : le 112 « sans carte SIM » a été retiré de
`numeros-urgence`).

| id v1 supprimé | remplacé par |
|---|---|
| `a-proteger-actions` (5 étapes) | `a-proteger-arret` (où s'arrêter, détresse, gilet) + `aff-a-contact-vehicules-accidentes` (couper le contact) + `aff-a-triangle-autoroute` (ne pas poser le triangle si ça expose) ; la mise à l'abri derrière la glissière est passée dans l'explication de `a-proteger-arret` (elle a déjà sa carte en thème R : `r-autoroute-panne-attendre`) |
| `a-alerter-message` (5 éléments + quand raccrocher) | fait `message-alerte` (contenu du message, conservé) + `a-alerter-raccrocher` (quand raccrocher) + `a-alerter-borne-ou-portable` (borne plutôt que portable) + `aff-a-rester-sur-place` |

Cartes v1 conservées et resserrées (recto situé, réponse = décision + raison) : `a-evaluer-victime`,
`a-pls`, `a-rcp-dae`, `a-hemorragie`, `a-blesse-deplacer`, `a-casque-motard`, `a-incendie-vehicule`,
`a-accident-materiel-obligations`, `a-accident-corporel-obligations`.

Correctifs apportés au premier passage sur 07 :
- `a-dae-choc-non-conseille` → **renommé `a-dae-utilisation`** et réorienté (que faire pendant
  l'analyse et le choc). Motif : sa réponse v2 (« il ne peut pas nuire à une victime qui n'en a pas
  besoin ») faisait doublon avec la question officielle Q6, désormais portée par deux affirmations.
- `a-pls` : restitution de « femme enceinte : sur le côté gauche » (perdu au premier passage).
- `a-hemorragie` : restitution de la brûlure (refroidir 10 à 20 min), perdue au premier passage.
- `a-incendie-vehicule` : restitution de la plaque orange (matières dangereuses), perdue au premier passage.
- `a-proteger-arret` : explication complétée (mise à l'abri hors chaussée).
- `a-proteger-temoins`, ajouté puis **retiré** : doublon avec `r-autoroute-panne-attendre` (thème R).

### Cartes ajoutées (thème A) et ligne de `02-carte-des-connaissances.md` visée

Toutes se rattachent aux deux lignes du bloc « A — Porter secours » :
*« PAS : Protéger …, Alerter …, Secourir … »* et *« Non-assistance …, obligation de s'arrêter, délit de fuite »*.

| id | forme | ligne visée / source de l'idée reçue |
|---|---|---|
| `a-constat-desaccord` | Q | ligne 2 (obligation de s'arrêter, suites de l'accident) ; knowledge-facts P5 |
| `aff-a-dae-formation` | AFF faux | ligne 1 « DAE » — **question officielle Q6** (exam.md §3.1) |
| `aff-a-dae-sans-arret-cardiaque` | AFF faux | ligne 1 « DAE » — **question officielle Q6** |
| `aff-a-pls-avec-casque` | AFF vrai | ligne 1 « PLS », « ne pas retirer le casque » ; knowledge-facts P4 |
| `aff-a-respire-mais-inconsciente` | AFF faux | ligne 1 « PLS / RCP » — discrimine les deux gestes |
| `aff-a-compressions-seules` | AFF vrai | ligne 1 « RCP 30/2 » ; knowledge-facts P4 |
| `aff-a-couvrir-victime` | AFF vrai | ligne 1 « couvrir, parler » ; P7 « la couverture ne sert que s'il fait froid » |
| `aff-a-donner-a-boire` | AFF faux | ligne 1 « Secourir » ; P7 « donner à boire au blessé » |
| `aff-a-contact-vehicules-accidentes` | AFF faux | ligne 1 « couper contact » |
| `aff-a-triangle-autoroute` | AFF vrai | ligne 1 « triangle 30 m » ; P7 « sur autoroute je pose le triangle à 30 m » ; R416-19 |
| `aff-a-18-secours-personne` | AFF vrai | ligne 1 « 15/17/18/112/114 » ; P7 « le 18, c'est seulement pour les incendies » |
| `aff-a-112-remplace-les-autres` | AFF faux | ligne 1 « numéros » ; P7 « le 112 remplace les autres numéros » |
| `aff-a-rester-sur-place` | AFF vrai | ligne 1 « ne pas raccrocher en premier » / ligne 2 |
| `aff-a-ne-rien-faire` | AFF faux | ligne 2 « non-assistance » ; P7 « mieux vaut ne rien faire » |
| `aff-a-constat-signature` | AFF faux | ligne 2 ; P7 « le constat amiable engage ma responsabilité » |

## 3. Thème P — cartes supprimées → cartes créées

v1 : 17 questions + 2 faits ; 3 questions étaient refusées par le build (réponses énumératives).

| id v1 | traitement |
|---|---|
| `p-verif-tour-vehicule` (5 éléments) | **conservé**, réduit à 4 éléments (pneu, fuite, feux/plaques, obstacle bas) ; le pare-brise a déjà `p-verif-pare-brise`, le chargement `p-verif-chargement-important` ; ajout de `aff-p-neige-toit` |
| `p-ceinture-position` (6 éléments) | **conservé**, réduit aux deux sangles ; les deux pièges sortent en affirmations : `aff-p-ceinture-sous-le-bras`, `aff-p-ceinture-blouson` |
| `p-quitter-checklist` (7 éléments) | **conservé**, réduit à moteur/clé + frein + rapport ; éclaté en `p-quitter-objets` (objets, vitres, verrouillage), `aff-p-quitter-documents`, et les roues/rapport en pente qui avaient déjà `p-pente-roues` et `p-pente-vitesse` |
| `p-assistance-stationnement` | **supprimé** : doublon de `s-adas-limites` (thème S, qui cite déjà la question officielle Q8). Remplacé par `aff-p-assistance-stationnement`, qui reprend la forme exacte de Q8 (double OUI/NON) |
| `p-siege-reglage` (siège + dossier) | scindé en `p-siege-reglage` (avancée) et `p-dossier-reglage` (inclinaison) |
| faits `p-installation-reperes`, `p-quitter-reperes` | inchangés (repères chiffrés : sommet de la tête, haut du volant, jambe fléchie, 9 h 15 ; angle mort, main opposée, 1re / marche arrière) |

Les 12 autres questions v1 sont conservées avec leur id ; leur recto a été **situé** (« Je stationne dans
une rue en forte pente, le long d'un trottoir : … » au lieu de « Stationné en pente, dans quel sens… »)
et la réponse ramenée à une décision + sa raison, pour s'aligner sur le style du thème A.
Corrections de la relecture v1 déjà présentes et vérifiées : `p-pente-roues` (pneu **avant** droit contre
le trottoir), `p-quitter-checklist` (source R417-8), `p-quitter-stationnement-surveiller` (source Q14 +
R412-10), `p-enfants-seuls` (70 °C en 20 minutes).

### Cartes ajoutées (thème P) et ligne de `02-carte-des-connaissances.md` visée

Lignes visées : *« Vérifications avant de partir (pneus, feux, niveaux, chargement, vitres) ; installation
(siège, dossier, appuie-tête …, rétroviseurs …, ceinture plate, volant 9 h 15 / 10 h 10) »* et
*« Quitter : moteur coupé, frein à main, rapport ou P, roues en pente, objets cachés, fenêtres fermées,
contrôle rétroviseur + angle mort avant d'ouvrir (« hollandaise »), enfants, jamais seul en voiture »*.

| id | forme | ligne visée / source |
|---|---|---|
| `p-verif-gps-passagers` | Q | ligne 1 (vérifications avant de partir) ; knowledge-facts S1 (GPS programmé avant, passagers attachés) |
| `p-dossier-reglage` | Q | ligne 1 « dossier » ; S2 (poignets sur le haut du volant) |
| `p-demarrage-point-mort` | Q | ligne 1 (installation) ; S1/S3 (levier au point mort, P en boîte auto) |
| `p-quitter-objets` | Q | ligne 2 « objets cachés, fenêtres fermées » ; S4 |
| `p-passagers-descendre` | Q | ligne 2 « enfants » ; S4 (descendre côté trottoir, sécurité enfant) |
| `aff-p-reglage-en-roulant` | AFF faux | ligne 1 (réglages à l'arrêt) ; S2 « ne jamais modifier ces réglages en roulant » |
| `aff-p-retro-interieur-nuit` | AFF vrai | ligne 1 « rétroviseur intérieur » ; S2 (position nuit anti-éblouissement) |
| `aff-p-appuie-tete-confort` | AFF faux | ligne 1 « appuie-tête » ; S2 (rôle : coup du lapin) |
| `aff-p-ceinture-sous-le-bras` | AFF faux | ligne 1 « ceinture plate » ; S2 |
| `aff-p-ceinture-blouson` | AFF vrai | ligne 1 « ceinture plate » ; S2 (vêtements épais) |
| `aff-p-volant-bras-croises` | AFF faux | ligne 1 « volant » ; S2 (ne pas croiser les bras) |
| `aff-p-pied-gauche-frein` | AFF faux | ligne 1 (installation, pédales) ; S2 |
| `aff-p-neige-toit` | AFF vrai | ligne 1 « vitres » ; S1 (pare-brise dégagé, neige comprise sur le toit) |
| `aff-p-vehicule-emprunte` | AFF vrai | ligne 1 (vérifications) ; S1 (gilet + triangle, commandes, carburant) |
| `aff-p-entrer-face-circulation` | AFF vrai | ligne 1 (prendre son véhicule) ; S1 |
| `aff-p-assistance-stationnement` | AFF vrai | ligne 2 (quitter / reprendre une place) — **question officielle Q8** |
| `aff-p-sortie-stationnement-priorite` | AFF faux | ligne 2 ; R412-10 + **question officielle Q14** |
| `aff-p-portiere-responsabilite` | AFF faux | ligne 2 « hollandaise » ; R417-7 |
| `aff-p-boite-auto-position-p` | AFF faux | ligne 2 « frein à main, rapport ou P » ; S4 |
| `aff-p-quitter-documents` | AFF faux | ligne 2 « objets cachés » ; S4 (documents avec soi) |

## 4. Valeurs vérifiées

Vérifiées dans `docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026) :
- **R. 416-19** : présignalisation par feux de détresse **et** triangle quand le véhicule immobilisé
  constitue un danger (intersections, virages, sommets de côte, PN, visibilité insuffisante) ; gilet
  revêtu **avant** de quitter le véhicule après un arrêt d'urgence ; le code ne chiffre pas les 30 m
  (arrêté du 30 septembre 2008) — c'est pourquoi la carte dit « environ 30 m ».
- **R. 412-6 II** : possibilités de mouvement et champ de vision non réduits par les passagers ou les
  objets → fonde `p-verif-pare-brise`.
- **R. 231-1** : s'arrêter aussitôt que possible ; dégâts matériels → identité et adresse ; blessés →
  avertir police/gendarmerie et ne pas modifier l'état des lieux.
- **L. 231-1** (renvoi à CP 434-10) : délit de fuite = **3 ans, 75 000 €** ; suspension ≤ 5 ans.
- **R. 417-7** : interdiction d'ouvrir une portière quand la manœuvre constitue un danger, 1re classe.
- **R. 417-8** : précautions utiles avant de s'éloigner du lieu de stationnement.
- **R. 412-10** : avertir avant de reprendre sa place dans le courant de la circulation, 3 points.
- Non-assistance : **5 ans, 75 000 €** (CP 223-6, legal-facts D3).

## 5. Doutes restants

1. **« Chaque minute sans RCP ≈ −10 % de survie »** : marqué À VÉRIFIER dans knowledge-facts P4
   (chiffre FFC non recoupé). **Non repris** sur une carte (il figurait dans l'explication de
   `a-rcp-dae` en v1) — règle 7 du brief.
2. **Ordre exact d'installation** : knowledge-facts S2 signale la divergence Code en Poche
   (siège → dossier → appuie-tête → volant → rétroviseurs → ceinture) / EVS (volant avant le dossier).
   `p-ordre-installation` retient le dénominateur commun (« siège d'abord, rétroviseurs et ceinture en
   dernier ») et la divergence est dite dans l'explication.
3. **Séquence de démarrage** (S3) : marquée « pratique enseignée, partiellement sourcée ».
   `p-demarrage-point-mort` ne retient que ce qui est sourcé en S1 (levier au point mort, P + pied sur
   le frein en boîte auto) ; l'extinction des voyants reste en explication.
4. **Roues en pente sans bordure** : S4 marque À VÉRIFIER la nuance « montée avec bordure ».
   `p-pente-roues` garde la règle enseignée et met « sans trottoir, roues vers l'accotement » en
   explication seulement.
5. **Constat amiable** : knowledge-facts P5 marque À VÉRIFIER l'ensemble du paragraphe (pas de page
   service-public dédiée retrouvée). Deux cartes en dépendent (`a-constat-desaccord`,
   `aff-a-constat-signature`) ; seules les affirmations non contestées ont été retenues (on ne signe pas
   un constat inexact ; le constat n'établit pas la responsabilité). Le délai de **5 jours ouvrés**
   (Code des assurances, art. L113-2) reste dans l'explication de `a-accident-materiel-obligations`,
   comme en v1.
6. **Moteur tournant à l'arrêt** et **chaussures inadaptées** : écartés faute de base textuelle sûre
   (S4 marque le montant À VÉRIFIER ; aucune interdiction spécifique des chaussures dans le code).
7. **Feux de stationnement de nuit** (R416-12/13/16) : écarté — ne figure sur aucune ligne du bloc P de
   `02-carte-des-connaissances.md` (brief §5, « pas d'ajout hors carte des connaissances »).

## 6. Doublons évités (recensés pendant la rédaction)

- `aff-p-retro-angle-mort` (rédigé puis supprimé) : doublon de `aff-c-retros-suffisent` (thème C).
- `a-proteger-temoins` (rédigé puis supprimé) : doublon de `r-autoroute-panne-attendre` (thème R).
- `p-assistance-stationnement` : doublon de `s-adas-limites` (thème S) → supprimé.
- Pression des pneus à froid, objets non arrimés/projectiles, sécurité enfant des portières, ceinture
  (obligation, femme enceinte), airbag : laissés aux thèmes M et S, non repris en P.
- Angle mort (définition, ordre des contrôles avant de déboîter) : laissé au thème C ; P ne garde que
  ses deux applications propres (avant d'ouvrir la portière, avant de quitter une place).
- Redondance assumée, conforme au brief §2.8 : le triangle à 30 m vit en fait dans `triangle-distance`
  (07, avec le schéma) et dans `faits/06` au titre des équipements obligatoires — deux angles distincts
  (placement en situation d'accident / obligation d'avoir l'équipement à bord).
