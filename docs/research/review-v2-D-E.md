# Relecture contradictoire v2 — thèmes D (réglementation) et E (environnement)

Date : 21 septembre 2026. Périmètre : `data/faits/06_reglementation.yaml` (41 notes),
`data/questions/06_reglementation.yaml` (2), `data/affirmations/06_reglementation.yaml` (24),
`data/faits/11_environnement.yaml` (6), `data/questions/11_environnement.yaml` (17 relues, 18 après),
`data/affirmations/11_environnement.yaml` (18). **108 notes relues.**

Référentiels : `docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026, articles relus
directement : L. 223-1, L. 223-2, L. 223-5, L. 223-6, L. 233-1, L. 234-1, L. 235-1, L. 237-1,
L. 324-2, L. 325-7, L. 413-1, R. 233-1, R. 316-3-1, R. 318-2, R. 318-3, R. 323-22, R. 412-1,
R. 412-2, R. 412-10, R. 413-14, R. 413-15, R. 416-19, R. 417-10, R. 417-12) ;
`legal-facts.md` C, D, E, H, I, J ; `knowledge-facts.md` A1-A6 ; `exam.md` §3.1-3.2 et §4.3 ;
`review-facts-questions.md` n° 15-19 ; `brief-v2-redaction.md` ; `05-audit-v2.md` ;
`02-carte-des-connaissances.md` ; `v2-D-E.md`.

**Bilan : 7 ERREUR, 8 STYLE (toutes appliquées), 12 DOUTE (proposés, non appliqués).**
Une carte créée (`e-energies-alternatives`), aucune carte supprimée, aucun id renommé.
`python -m build.build --check` ne renvoie rien sur les six fichiers ; les six YAML se chargent.

**Aucune erreur de valeur juridique ou chiffrée n'a été trouvée** : montants, points, durées, seuils,
dates et articles de D ont tous été retrouvés dans `cdr.txt` ou `legal-facts.md` (y compris les valeurs
récentes : 3 ans / 9 000 € alcool-stupéfiants, 5 ans / 15 000 € en cumul et 9 points, grand excès délit
dès la 1re fois depuis le 29/12/2025, refus de dépistage et ivresse manifeste L237-1 depuis le
20/08/2026, rodéo 2 ans / 30 000 €, vignette d'assurance supprimée le 01/04/2024, ZFE maintenues
par la décision CC n° 2026-903 DC, Crit'Air 3,85 € en 2026, statistiques ONISR 2025). Les corrections
n° 15 à 19 de la relecture v1 sont bien présentes et ont été préservées. Les erreurs ci-dessous
portent donc sur la **qualité de carte** (clozes qui se soufflent la réponse, réponse non décisive,
liste fermée fausse, contradiction interne au deck) et sur une imprécision de L325-7.

---

## data/faits/06_reglementation.yaml

**1. `d-points-delit-cumul`** — ERREUR (cloze soufflé)
- Problème : `{{c1::6 points}}` était immédiatement suivi de « une contravention en retire au plus **6** » ;
  la réponse du blanc était visible en clair trois mots plus loin.
- Correction appliquée (texte) : la proposition sur la contravention passe en explication
  (« Une contravention aussi retire au plus 6 points. »), le recto ne garde que délit / cumul 8 / 9.
- Source : `cdr.txt` L. 223-2 I, II et III ; legal-facts C1.

**2. `d-probatoire-duree`** — ERREUR (quatre clozes soufflés)
- Problème : `{{c3::2 points}} par an (6 → 8 → 10 → 12)` et `{{c4::3 points}} par an après AAC (6 → 9 → 12)` :
  chaque progression donnait la réponse de son propre blanc, et les deux donnaient aussi c1 (3 ans) et
  c2 (2 ans). Les quatre cartes de la note étaient donc devinables sans rien savoir.
- Correction appliquée : les deux progressions passent en explication ; le recto devient
  « le capital de 6 points augmente de {{c3::2 points}} par an — {{c4::3 points}} par an après AAC ».
- Source : `cdr.txt` L. 223-1 ; legal-facts C1.

**3. `d-controle-technique`** — ERREUR (cloze soufflé)
- Problème : c2 = « 4e anniversaire », mais la fin de la même phrase disait « pour vendre une voiture
  de **plus de 4 ans** ». (La relecture v1 n° 16 avait traité le double « 6 mois » en les mettant sous
  c1 ; le second souffle subsistait.)
- Correction appliquée : « pour vendre une voiture **d'occasion**, le contrôle doit dater de moins de
  {{c1::6 mois}} » ; la condition « plus de 4 ans » passe en tête d'explication.
- Source : `cdr.txt` R. 323-22 ; legal-facts E3.

**4. `d-fourriere-abandon`** — ERREUR (valeur imprécise)
- Problème : « réputé abandonné **après 15 jours** » laissait entendre 15 jours après la mise en
  fourrière. L. 325-7 : « quinze jours **à compter de la mise en demeure faite au propriétaire** ».
- Correction appliquée (texte) : « Un véhicule en fourrière est réputé abandonné {{c1::15 jours}} après
  la mise en demeure adressée au propriétaire (10 jours s'il est de faible valeur marchande) ».
- Source : `cdr.txt` L. 325-7 (délai réduit à dix jours pour « valeur marchande insuffisante », puis
  destruction) ; R. 417-12 (abusif > 7 jours, 2e classe) vérifié et conforme.

## data/questions/06_reglementation.yaml

Aucune remarque. Les deux questions (`d-controle-papiers-oublies` 11 € / 5 jours / 135 € ;
`d-vente-vehicule` carte grise barrée, CSA, CT < 6 mois, cession sous 15 jours) sont conformes à
`cdr.txt` R. 233-1 et R. 322-4, et ne doublonnent pas `d-documents-bord` ni `d-carte-grise-delais`.

## data/affirmations/06_reglementation.yaml

**5. `aff-d-invalidation-capital`** — STYLE (affirmation non sourcée dans le verso)
- Problème : « le délai probatoire s'applique de nouveau (3 ans, ou **2 ans après conduite
  accompagnée**) ». La réduction à 2 ans est attachée à l'obtention du permis **par** l'AAC
  (L. 223-1) ; un permis repassé après invalidation n'est pas obtenu par AAC. Ni `legal-facts` C2 ni
  SP F1704 ne prévoient ce cas.
- Correction appliquée (pourquoi) : « Il repart à 6 points, comme un premier permis, et un nouveau
  délai probatoire s'applique. Le capital de 12 points ne se retrouve qu'au terme de ce probatoire,
  sans aucune infraction avec retrait de points. »
- Source : `cdr.txt` L. 223-1 al. 2 et L. 223-5 ; legal-facts C1, C2.

Les 23 autres affirmations sont conformes. Vérifications notables : `aff-d-ceinture-passager-adulte`
(R. 412-2 IV relu : 4e classe pour le conducteur, **aucun** retrait de points) ; `aff-d-clignotant-points`
(R. 412-10 : 35 € mais 3 points) ; `aff-d-detecteur-radar` (R. 413-15 : détention et transport
suffisent) ; `aff-d-grand-exces-delit` (L. 413-1 relu) ; `aff-d-alcool-contravention` (L. 234-1) ;
`aff-d-sans-assurance-points` (L. 324-2, 0 point) ; `aff-d-bonus-malus` (×1,25 / ×1,125 / plafond 3,50) ;
`aff-d-ct-defaillance-majeure` (majeure = 2 mois, véhicule utilisable ; critique = jour même).

---

## data/faits/11_environnement.yaml

**6. `e-critair-chiffres`** — ERREUR (cloze soufflé) + STYLE (explication doublon)
- Problème 1 : « Crit'Air : {{c1::6}} classes **(0 à 5)** plus les non classés » — la parenthèse donne
  le compte demandé par le blanc.
- Problème 2 : l'explication répétait les **trois** réponses des clozes de `d-critair-prix`
  (« ≈ 3,85 € », « valable toute la vie du véhicule », « 68 € »). Par ailleurs, la réécriture v2 de
  `d-critair-prix` avait fait disparaître l'échelle des couleurs (1 violet, 2 jaune, 3 orange,
  4 bordeaux), présente en v1 et utile à l'examen.
- Corrections appliquées : recto « {{c1::6}} classes numérotées à partir de 0, plus les non classés » ;
  explication remplacée par « Couleurs : 0 vert (électrique, hydrogène), 1 violet, 2 jaune, 3 orange,
  4 bordeaux, 5 gris. À date égale, un diesel est une classe en dessous d'une essence. »
- Source : legal-facts E4 ; knowledge-facts A2.

**7. `e-surconsommations`** — STYLE (valeur marquée « À VÉRIFIER »)
- Problème : le cloze c1 « +10 % » de climatisation est donné comme valeur ferme alors que
  `knowledge-facts` A1 la marque « À VÉRIFIER (pourcentages divergents) » (Codeclic +10/+25,
  Ornikar +3 à +5, ADEME +10 en moyenne) — brief règle n° 7.
- Correction appliquée : « climatisation **environ** +{{c1::10 %}} sur route et jusqu'à +25 % en ville ».
- Source : knowledge-facts A1.

Les quatre autres faits (`e-rapports-chiffres`, `e-vitesse-chiffres`, `e-pic-pollution-chiffres`,
`e-trajets-courts-chiffres`) sont conformes aux ordres de grandeur de `knowledge-facts` A1-A3
(2 000/2 500 tr/min, 20-30 s, −1 L/100 km par −10 km/h, 4 min sur 100 km, −20 km/h sans descendre
sous 70, 40 % des trajets urbains < 2 km) — voir toutefois les DOUTE 1 et 2.

## data/questions/11_environnement.yaml

**8. `e-zfe-definition`** — ERREUR (contradiction interne au deck, non sourcée)
- Problème : la v2 a remplacé l'explication v1 « panonceau indiquant les Crit'Air **interdits** » par
  « panonceau des Crit'Air **admises** », sans source. Les cartes de reconnaissance du deck disent
  l'inverse (`b56` : « accès interdit aux véhicules dont la vignette ne correspond pas au panonceau
  M11d » ; `m11d` : « précise les catégories de véhicules (vignettes Crit'Air) **interdites** »).
  Ni `legal-facts` E4 ni `knowledge-facts` A2 ne tranchent (A2 marque B56/B57 « À VÉRIFIER »).
- Correction appliquée (formulation neutre, qui ne contredit plus rien) : « L'entrée est signalée par
  le panneau de zone B56, avec un panonceau qui précise les vignettes Crit'Air concernées et les
  horaires. »
- Source : `data/reconnaissance/panneaux_zones.yaml` (b56), `data/reconnaissance/panonceaux.yaml`
  (m11d) ; knowledge-facts A2. **À trancher définitivement sur l'IISR** (voir DOUTE 9).

**9. `e-covoiturage-voie`** — ERREUR (liste fermée qui contredit une autre carte du même fichier)
- Problème : la réponse énumérait « réservée aux véhicules transportant au moins deux personnes, aux
  taxis et aux bus » — liste apparemment exhaustive qui conduit à répondre FAUX à
  `aff-e-covoiturage-electrique` (VRAI : les véhicules à très faibles émissions, Crit'Air 0, y sont
  admis seuls). Deux cartes voisines donnaient donc des réponses opposées.
- Correction appliquée (réponse) : « … elle est réservée au covoiturage (au moins deux personnes) et
  à quelques catégories admises, comme les taxis et les bus. » (explication : « y circuler sans y
  avoir droit coûte 135 € »).
- Source : knowledge-facts A3 (VR2+ : ≥ 2 occupants, taxis, bus, Crit'Air 0) ;
  `data/_meta/sign_overrides.yaml` (losange blanc).

**10. `e-climatisation-conso`** — STYLE (réponse non décisive)
- Problème : la question pose un choix binaire (« climatisation ou vitres ouvertes ? ») et la réponse
  répondait « j'aère **ou** je règle la climatisation… » — le candidat ne sait pas ce qu'il faut cocher
  (brief règle n° 3).
- Correction appliquée : « Les vitres : à faible allure, c'est la climatisation qui coûte le plus cher
  en carburant. Si je la garde, je la règle 4 à 5 °C sous la température extérieure. » — cohérent avec
  `aff-e-clim-autoroute` (à 130 km/h, c'est l'inverse).
- Source : knowledge-facts A1, A6.

**11. `e-ve-recharge`** — STYLE (réponse quasi identique à deux autres cartes)
- Problème : « Planifier les recharges, adapter sa conduite au silence du véhicule près des piétons et
  tenir compte de son poids au freinage » reprenait mot pour mot les deux tiers de
  `e-electrique-avantages` (autonomie/recharge, poids) et toute la connaissance de `aff-e-ve-silence`
  (silence). Le contenu propre (20-40 min, froid) était relégué en explication.
- Correction appliquée : la carte est recentrée sur la recharge — « Que faut-il prévoir pour partir
  loin en voiture électrique ? » → « Planifier les recharges : 20 à 40 minutes sur une borne rapide,
  plusieurs heures sur une prise domestique — et compter une autonomie nettement réduite par temps
  froid. » Id, thème, sous-thème et importance inchangés.
- Source : knowledge-facts A4.

**12. `e-critair-classes`** — STYLE (doublon d'un cloze + prix répété)
- Problème : la question demandait « combien y a-t-il de catégories ? » et répondait « 6 classes,
  de 0 à 5 » — c'est exactement le cloze c1 de `e-critair-chiffres` (brief règle n° 8 : un chiffre vit
  dans *un* fait à trous). Son explication répétait en outre « 3,85 € en 2026 », qui est la réponse du
  cloze c1 de `d-critair-prix`, et « en bas à droite du pare-brise », déjà sur deux autres cartes.
- Correction appliquée : la carte porte désormais la connaissance non couverte ailleurs —
  « Sur quoi repose la classe Crit'Air d'un véhicule ? » → « Sur son type de motorisation et sa date
  de première mise en circulation, qui déterminent sa norme Euro — pas sur sa puissance ni sur sa
  consommation réelle. » ; explication débarrassée du prix et du collage.
- Source : legal-facts E4 ; knowledge-facts A2.

**13. `e-ecomobilite-choix`** — STYLE (cloze répété + valeur non sourcée)
- Problème : l'explication répétait « 40 % des trajets urbains moins de 2 km », qui est le cloze c1 de
  `e-trajets-courts-chiffres`, et affirmait « la moitié des trajets en voiture font moins de 5 km »,
  introuvable dans les dossiers (`knowledge-facts` A3 donne « 65 % des déplacements en voiture » et
  « sous 6 km, vélo/marche souvent aussi rapides »).
- Correction appliquée : « Sur les courtes distances urbaines, le vélo est souvent aussi rapide que la
  voiture. Autopartage, parcs relais et forfait mobilités durables complètent l'offre. »
- Source : knowledge-facts A3.

**14. `e-energies-alternatives`** — carte **créée** (connaissance v1 disparue)
- Problème : la suppression de `e-motorisations` (rapport v2 §2.1) a fait disparaître du deck le GPL,
  le GNV, l'hydrogène et le malus écologique, alors que la ligne E de `02-carte-des-connaissances.md`
  les liste explicitement (« énergies (électrique, hybride, GPL, GNV, hydrogène, E85) … ; malus »).
  Seul l'électrique (`e-electrique-avantages`, `aff-e-electrique-zero`, `aff-e-ve-silence`) et l'E85
  (`e-e85`) avaient été repris.
- Carte créée (`utile`, sous-thème `ecomobilite`) : « Qu'apportent le GPL, le GNV et l'hydrogène par
  rapport à une essence ou à un diesel ? » → « Moins de particules, d'oxydes d'azote et de bruit, avec
  un classement Crit'Air plus favorable ; en contrepartie, un réseau de stations très limité et un
  surcoût à l'achat. » La réponse ne cite volontairement **pas** les numéros de classe, qui sont les
  clozes c2/c3 de `e-critair-chiffres`.
- Source : knowledge-facts A4 ; legal-facts E4. Thème E : 52 cartes (objectif 45-55).

Les autres questions sont conformes : `e-bruit-sources` (R. 318-3 relu : 4e classe = 135 € et
immobilisation, confirmé), `e-polluant-co2`, `e-particules-usure` (> 50 % des particules viennent des
freins, pneus et chaussée), `e-pic-pollution`, `e-feu-rouge-anticipation`, `e-moteur-arret`,
`e-frein-moteur`, `e-rapports-regime`, `e-entretien-dechets`, `e-e85`, `e-electrique-avantages`.

## data/affirmations/11_environnement.yaml

**15. `aff-e-critair-renouvellement`** — STYLE (cloze répété)
- Problème : le `pourquoi` donnait « 3,85 € en 2026 », qui est la réponse du cloze c1 de
  `d-critair-prix` ; le prix n'apporte rien au jugement demandé (renouvellement annuel ou non).
- Correction appliquée : « Elle vaut pour toute la vie du véhicule : une seule commande sur
  certificat-air.gouv.fr. Elle n'est refaite que si le véhicule change de plaque d'immatriculation. »
- Source : legal-facts E4.

Les 17 autres affirmations sont conformes à `knowledge-facts` A1-A6 et, pour les valeurs juridiques,
à `cdr.txt` : `aff-e-borne-recharge` (R. 417-10 III 3° relu : stationnement gênant, 2e classe = 35 €,
fourrière possible), `aff-e-zfe-vignette` (68 € / 135 € PL, R. 411-19-1), `aff-e-zfe-supprimees`
(décision CC n° 2026-903 DC du 21 mai 2026), `aff-e-diesel-critair1`, `aff-e-pic-vitesse`,
`aff-e-diesel-nox`, `aff-e-clim-autoroute`, `aff-e-point-mort-descente`, `aff-e-moteur-chauffer`,
`aff-e-trajets-courts`, `aff-e-coffre-toit-vide` (10-15 % même vide, barres seules 5-10 %),
`aff-e-vitesse-stable`, `aff-e-ecoconduite-securite` (La Poste : −5 % carburant / −10 % sinistres),
`aff-e-equipements-electriques`, `aff-e-electrique-zero`, `aff-e-ve-silence`,
`aff-e-covoiturage-electrique`.

---

## Doutes (proposés, non appliqués)

1. **Valeurs « À VÉRIFIER » encore portées par des cartes** (brief règle n° 7) : les surconsommations
   de climatisation (`e-surconsommations` c1, simplement nuancée par « environ ») ; l'abaissement de
   **−20 km/h** en pic de pollution (`e-pic-pollution-chiffres` c1 et `aff-e-pic-vitesse`), marqué
   « À VÉRIFIER » dans `knowledge-facts` A2 mais présent dans `02-carte-des-connaissances.md` ; les
   **≈ 30 %** d'émissions de GES dues aux transports (`e-trajets-courts-chiffres` c2 et explication de
   `e-polluant-co2`), marqué « À VÉRIFIER » dans A2. Proposition : les garder (ce sont des ordres de
   grandeur attendus à l'examen) mais faire lever le flag « À VÉRIFIER » par une vérification CITEPA /
   arrêté préfectoral-type, ou déclasser les deux clozes concernés en explication.
2. **`e-entretien-dechets`** — « Un litre d'huile pollue des **milliers de litres** d'eau » : chiffre
   absent des dossiers (`knowledge-facts` A5 dit seulement « une très grande surface d'eau », marqué
   « À VÉRIFIER »). Proposition : « Un litre d'huile suffit à polluer une très grande surface d'eau ».
3. **`d-critair-prix` c2 « toute la vie du véhicule » ≈ `aff-e-critair-renouvellement`** : la même
   connaissance existe en fait à trous (thème D) et en affirmation (thème E). Le piège est distinct
   (confusion avec la vignette d'assurance annuelle), donc la carte est conservée, mais si l'on veut
   appliquer strictement la règle n° 8, c'est l'affirmation E qui doit sauter.
4. **`d-recuperation-points`** — la réécriture v2 a retiré de l'explication la **règle des 10 ans**
   (L. 223-6 al. 5 : les points des contraventions des quatre premières classes reviennent au plus tard
   10 ans après, sauf invalidation). Elle n'apparaît plus nulle part dans le deck. Proposition : la
   remettre en fin d'explication, ou l'assumer comme hors programme (elle n'est pas dans la ligne
   « récupération (6 mois / 2 ans / 3 ans) » de la carte des connaissances).
5. **`aff-d-aac-points-eleve` et `d-accompagnateur`** — le retrait de points à l'accompagnateur repose
   sur la FAQ conduite accompagnée de la Sécurité routière, pas sur un article (doute n° 19 de la
   relecture v1, maintenu). Élément nouveau utile : `cdr.txt` **L. 237-1 in fine** (« Le présent article
   est applicable à l'accompagnateur d'un élève conducteur ») et R. 234-1 V confirment au moins que
   l'accompagnateur est bien le conducteur responsable au sens pénal. L'attribution explicite dans le
   verso reste la bonne solution.
6. **`e-bruit-sources`** — « Des radars sonores sont expérimentés depuis 2022 » : hors des deux
   dossiers de recherche. Proposition : supprimer la phrase ou la sourcer (décret n° 2022-28).
7. **`aff-e-ve-silence`** — « avertisseur sonore imposé **sous 20 km/h** » : `knowledge-facts` A4 dit
   seulement « à basse vitesse, sur les modèles neufs depuis 2019-2021 ». Le seuil de 20 km/h vient du
   règlement (UE) 540/2014 cité en source mais n'est pas dans les dossiers. Proposition : « à basse
   vitesse » si l'on veut rester strictement dans les dossiers.
8. **`d-formation-post-permis`** — la fenêtre « entre le 6e et le 12e mois » est désormais renvoyée à un
   arrêté par R. 223-4-1 (décret n° 2025-1437 du 31/12/2025) ; SP F2390 l'affiche toujours
   (`legal-facts` C1). La carte est conforme à ce que l'examen attend ; à resurveiller.
9. **Panonceau M11d (ZFE)** — les deux formulations (« Crit'Air admises » / « Crit'Air interdites »)
   circulent dans le projet ; l'IISR consolidée n'a pas été relue sur ce point. La carte E est désormais
   neutre (point 8 ci-dessus), mais `data/reconnaissance/panneaux_zones.yaml` (b56) et
   `data/reconnaissance/panonceaux.yaml` (m11d) — hors de mon périmètre — restent à trancher.
10. **`e-covoiturage-voie`** recoupe la carte de reconnaissance du losange blanc
    (`sign_overrides.yaml` : « Losange blanc au-dessus d'une voie : voie réservée… bus, taxis et
    covoiturage »). La question E reste utile (elle porte sur *qui* peut l'emprunter, pas sur la forme
    du signal), mais c'est la limite de la règle n° 8.
11. **`d-vitesse-bareme`** — l'explication écrit « 40 à 49 km/h : 4 points, 135 €, rétention immédiate
    du permis » ; `legal-facts` D2 précise « rétention **si interception** ». Nuance mineure, non
    appliquée pour ne pas alourdir l'explication.
12. **Inexactitude du rapport `v2-D-E.md` §2.1** (pas des cartes) : la suppression de `e-pneus-conso`
    est justifiée par « `m-pneus-sous-gonflage` (thème M) couvre déjà risques et surconsommation ». Cet
    id n'existe pas ; le thème M couvre les risques (`aff-m-surgonflage`, `aff-m-chargement-pression`,
    `m-pneus-pression-quand`) mais **pas** la surconsommation, qui ne survit que dans le cloze c4 de
    `e-surconsommations` (+8 %). Le résultat est bon, la justification est à corriger.

## Contrôles croisés sans remarque

- **Alcool et téléphone, D vs C** : `d-alcool-contravention` / `d-alcool-delit` / `aff-d-alcool-contravention`
  vs `faits/03` (`c-verre-standard`, `c-alcool-risque-multiplie`, `c-conversion-air-sang`) et
  `affirmations/03` (`aff-c-probatoire-un-verre`, `aff-c-oreillette`) : aucune valeur divergente.
  Le recouvrement `aff-c-probatoire-un-verre` (dose) / `aff-d-probatoire-alcool` (conséquence : 6 points
  = invalidation) est celui que le rapport v2 §1.3 annonce ; il est acceptable.
- **Sanctions de circulation, D vs L** : `d-feu-rouge-stop-sanction`, `d-autres-bareme-3-points` vs
  `questions/02` et `affirmations/02` : barèmes identiques (4 points feu rouge/STOP/priorités,
  6 points piéton, 3 points ligne continue franchie / 1 point chevauchée, 35 € feu jaune fixe).
- **Pneus et consommation, E vs M** : pas de valeur contradictoire (voir DOUTE 12).
- **Route, E vs R** : `e-frein-moteur` renvoie explicitement à la question officielle Q18 traitée par
  `r-descente-freinage` (`questions/04`) et `aff-r-descente-freiner-permanence` (`affirmations/04`) ;
  pas de troisième exemplaire, conformément au choix du rédacteur.
- **Stationnement, E vs L** : `aff-e-borne-recharge` (R. 417-10 III 3°) est cohérente avec les cartes
  R417-10 de `affirmations/02` et avec `panonceaux.yaml` (M6i).
- **Connaissances supprimées en E** : les six cartes-listes retirées ont été recontrôlées ligne à ligne
  contre `git show HEAD:data/questions/11_environnement.yaml`. Tout est repris ailleurs, à trois
  exceptions près : les énergies alternatives (corrigé, point 14), le monoxyde de carbone et les
  hydrocarbures imbrûlés de `e-polluants` (CO mortel en garage fermé — relève plutôt du thème M/P, non
  recréé ici), et « la climatisation sert aussi à désembuer » (absent des deux dossiers, doute n° 3 du
  rapport v2 : à laisser de côté tant qu'il n'est pas sourcé).
