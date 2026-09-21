# v2 — Thème R « La route » : rapport de réécriture

Périmètre : `data/questions/04_route.yaml`, `data/faits/04_route.yaml` (créé),
`data/affirmations/04_route.yaml` (créé). Aucun autre fichier de données modifié.
Règles appliquées : `docs/research/brief-v2-redaction.md` ; cible de volume fixée par
`docs/05-audit-v2.md` §2.5 (R ≈ 70 cartes).

## 1. Comptage

| | v1 | v2 |
|---|---|---|
| Questions (décisions) | 33 | **39** |
| Faits à trous | 0 | **5** |
| Affirmations | 0 | **32** (14 vrai / 18 faux = 44 %) |
| **Total R** | **33** | **76** |

`python -m build.build --check` ne signale plus aucune erreur sur `04_route.yaml`
(19 erreurs en v1). Aucun `long_ok` n'a été nécessaire.

## 2. Cartes-listes supprimées ou réécrites → cartes créées

| id v1 | motif | devient |
|---|---|---|
| `r-nuit-feux-croisement-route` | 5 éléments | Q `r-nuit-feux-croisement-route` (décision : phares en face) + Q `r-nuit-suivre-vehicule-feux` + AFF `aff-r-nuit-feux-position-agglo` |
| `r-nuit-vitesse-visibilite` | 46 mots | réécrite (30 mots), valeur « 70 km/h » harmonisée avec `c-feux-portee` |
| `r-nuit-stationnement-feux` | **doublon** de `l-stationnement-hors-agglo-nuit` (02) | **supprimée** → AFF `aff-r-nuit-feux-route-arret` (angle distinct : R416-5, feux de route interdits à l'arrêt) |
| `r-pluie-feux` | énoncé ambigu + recouvrement `m-feux-jour-limite` | réécrite sur l'obligation d'éclairage (R416-4) ; le couple brouillard avant/arrière passe en AFF `aff-r-brouillard-avant-pluie` et `aff-r-brouillard-arriere-pluie` |
| `r-pluie-distances` | 49 mots, **doublon** des faits `c-distance-mouillee` et `l-vitesse-pluie` | **supprimée** → AFF `aff-r-autoroute-vitesse-pluie` + AFF `aff-r-visibilite-50-autoroute` |
| `r-aquaplaning` | définition + réaction | Q `r-aquaplaning` recentrée sur les **signes** + AFF `aff-r-aquaplaning-freiner` (« je freine » = piège R15) |
| `r-neige-conduite` | 46 mots, 7 éléments, « démarrer en 2e » non sourcé | Q `r-neige-conduite` (souplesse) + Q `r-verglas-descente` + Q `r-deneigement-depassement` + FAIT `r-neige-adherence` + AFF `aff-r-verglas-pont` + AFF `aff-r-neige-depassement-pl` |
| `r-loi-montagne` | 57 mots | **supprimée** → FAIT `r-loi-montagne-periode` + AFF `aff-r-montagne-4-pneus` (forme Q10) + AFF `aff-r-montagne-ms` |
| `r-vent-lateral` | 43 mots | Q `r-vent-lateral` (dépassement d'un PL sur viaduc) + AFF `aff-r-vent-manche` + AFF `aff-r-vent-deux-roues` |
| `r-soleil-bas` | 5 éléments | resserrée à 3 gestes |
| `r-tunnel-regles` | 54 mots, 8 règles | **supprimée** → Q `r-tunnel-feux-jour` + Q `r-tunnel-distance-arret` + AFF `aff-r-tunnel-demi-tour` + FAIT `r-tunnel-niches` |
| `r-tunnel-panne` | 46 mots | resserrée (« où me placer, que faire des clés ? ») |
| `r-tunnel-incendie` | 50 mots | resserrée |
| `r-pn-engagement` | énoncé abstrait | réécrite en situation (« la file est arrêtée juste après ») + AFF `aff-r-pn-barriere-contourner` |
| `r-pn-bloque` | 45 mots | resserrée |
| `r-pn-feu-rouge-clignotant` | — | conservée ; le « 1 km d'arrêt du train » sort de l'explication et devient le FAIT `r-train-distance-arret` |
| `r-tram-priorite` | 3 connaissances | resserrée (priorité) + Q `r-tram-traversee-degager` + AFF `aff-r-tram-station-pieton` |
| `r-chantier-regles` | 41 mots, **doublon partiel** de `l-signalisation-temporaire` | **supprimée** → Q `r-chantier-approche` + AFF `aff-r-chantier-sans-ouvriers` |
| `r-autoroute-insertion` | 46 mots, **doublon** de `l-insertion-autoroute-priorite` | **supprimée** → Q `r-autoroute-insertion-fin-voie` (fin de voie d'accélération) + AFF `aff-r-insertion-prioritaire` (point de vue de celui qui est **déjà** sur l'autoroute) |
| `r-autoroute-sortie` | 46 mots | resserrée (où ralentir) + Q `r-autoroute-sortie-ratee` + FAIT `r-autoroute-sortie-annonces` |
| `r-autoroute-panne` | 57 mots | scindée : Q `r-autoroute-panne` (ordre des gestes) + Q `r-autoroute-panne-attendre` (où attendre) + AFF `aff-r-autoroute-triangle` |
| `r-autoroute-interdictions` | 7 éléments | **supprimée** → AFF `aff-r-autoroute-trouee-terre-plein` + AFF `aff-r-peage-reculer` (la marche arrière/demi-tour est portée par `r-autoroute-sortie-ratee`, la BAU par `r-autoroute-bau`) |
| `r-autoroute-usagers-interdits` | 6 éléments | resserrée à 4 familles + AFF `aff-r-autoroute-cyclo` + AFF `aff-r-autoroute-aac` |
| `r-autoroute-peage` | 44 mots | resserrée |
| `r-autoroute-chevrons` | **doublon** de la reconnaissance `marq-chevrons` et du fait `c-autoroute-deux-traits` | **supprimée**, sans remplacement |
| `r-autoroute-bau` | style | resserrée (référence « voie auxiliaire » corrigée dès la v1) |
| `r-montagne-priorite` | 70 mots | **supprimée** → Q `r-montagne-croisement-difficile` (qui s'arrête) + Q `r-montagne-marche-arriere` (qui recule, exception « place d'évitement » du côté du montant) |
| `r-descente-freinage` | — | conservée, explication resserrée (Q18) |

## 3. Ajouts et ligne visée dans `docs/02-carte-des-connaissances.md` (section « R — La route »)

| Ligne de `02-…` | Cartes ajoutées |
|---|---|
| Nuit : feux de croisement/route, éblouissement, hors agglo | `r-nuit-suivre-vehicule-feux`, `aff-r-nuit-feux-position-agglo`, `aff-r-nuit-feux-route-arret`, `aff-r-nuit-pieton-sombre` |
| Pluie : adhérence, aquaplaning, feux, distances, vitesse | `r-pluie-premieres-gouttes`, `aff-r-aquaplaning-freiner`, `aff-r-autoroute-vitesse-pluie`, `aff-r-brouillard-arriere-pluie`, `aff-r-brouillard-avant-pluie` |
| Brouillard : feux avant/arrière, < 50 m → 50 km/h | `r-brouillard-intervalle` (règle des trois 50), `aff-r-brouillard-feux-route`, `aff-r-visibilite-50-autoroute`, `aff-r-brouillard-depasser` |
| Neige/verglas : chaînes, pneus hiver, conduite douce, frein moteur ; vent latéral | `r-verglas-descente`, `r-deneigement-depassement`, `r-neige-adherence` (F), `r-loi-montagne-periode` (F), `aff-r-montagne-ms`, `aff-r-montagne-4-pneus`, `aff-r-verglas-pont`, `aff-r-neige-depassement-pl`, `aff-r-vent-manche`, `aff-r-vent-deux-roues` |
| Tunnels : feux, 150 m, ne pas s'arrêter, incendie, panne | `r-tunnel-feux-jour`, `r-tunnel-distance-arret`, `r-tunnel-niches` (F), `aff-r-tunnel-demi-tour` |
| Passages à niveau : engagement, feu rouge clignotant, barrière, véhicule immobilisé, arrêt du train ~1 km | `r-pn-barrieres-ouverture`, `r-train-distance-arret` (F), `aff-r-pn-150m`, `aff-r-pn-feux-rouges-possibles`, `aff-r-pn-barriere-contourner` |
| Tramways, chantiers, montagne, routes étroites | `r-tram-traversee-degager`, `r-chantier-approche`, `r-montagne-croisement-difficile`, `r-montagne-marche-arriere`, `aff-r-tram-station-pieton`, `aff-r-chantier-sans-ouvriers`, `aff-r-descente-150m`, `aff-r-descente-freiner-permanence` |
| Autoroute : insertion, sortie, BAU, panne, interdictions, péage, aires, vitesse min | `r-autoroute-insertion-fin-voie`, `r-autoroute-sortie-ratee`, `r-autoroute-panne-attendre`, `r-autoroute-sortie-annonces` (F), `aff-r-insertion-prioritaire`, `aff-r-autoroute-voie-gauche-80`, `aff-r-autoroute-trouee-terre-plein`, `aff-r-autoroute-cyclo`, `aff-r-autoroute-aac`, `aff-r-autoroute-bouchon-detresse`, `aff-r-autoroute-triangle`, `aff-r-peage-reculer` |

Formes officielles reprises telles quelles : **Q10** (équipement hivernal → `aff-r-montagne-4-pneus`),
**Q18** (descente à 150 m, freinage par intermittence → `aff-r-descente-150m`, `aff-r-descente-freiner-permanence`,
`r-descente-freinage`), **Q19** (PN à 150 m, feux rouges clignotants → `aff-r-pn-150m`,
`aff-r-pn-feux-rouges-possibles`), **Q20** (croisement de nuit → traité côté C par
`c-croisement-nuit-regard`, complété ici par `r-nuit-feux-croisement-route`).
**Q13** (autoroute mouillée, ×2) reste dans le fait `c-distance-mouillee` : non dupliqué.

## 4. Corrections de fond

- **`R. 422-4` n'est pas l'article des routes à accès réglementé** : dans le Code consolidé au
  10/09/2026 (`docs/research/sources/cdr.txt`), R. 422-4 traite du **passage des ponts**.
  La source de `r-autoroute-usagers-interdits` a été ramenée à **R. 421-2** seul.
  `docs/research/legal-facts.md` §F6 cite R422-4 à tort pour ce point (à corriger côté dossier).
- « Démarrer en 2e » sur neige (marqué **[AV]** dans `knowledge-facts` R4) : retiré.
- Loi Montagne : **aucune amende n'est codifiée** (art. D314-8) ; le point reste en explication du
  fait, jamais en réponse (conforme à la relecture v1, n° 43).
- Montagne : l'exception « place d'évitement » vise bien le véhicule **montant** (R414-3 III).
- Tunnel : panneau **C111/C112** (pas « C9 ») ; l'intervalle affiché (souvent 150 m) n'est pas
  assimilé aux 2 secondes.
- Le triangle sur autoroute : présenté comme **non exigé** quand sa pose met en danger
  (arrêté du 30 septembre 2008, art. 2 ; `legal-facts` E5), et non comme une obligation générale.

## 5. Doutes restants et recouvrements assumés

1. **Niches de sécurité tous les ~200 m** (`r-tunnel-niches`) : source unique (CETU). Carte marquée
   `utile`. L'interdistance des **issues de secours** (~400 m, directive 2004/54/CE) reste
   « À VÉRIFIER » dans `knowledge-facts` R7 : elle n'est **pas** mise en carte (seul le balisage vert l'est).
2. **Aires : 15-20 km / 40-50 km** (`r-autoroute-fatigue-aires`) : divergence Ornikar / EVS / APRR ;
   fourchette conservée, carte `utile`.
3. **30 km/h au télépéage** : signalisation des concessionnaires, non codifiée → explication seulement.
4. **Gilet « visible à 150 m »** : non sourcé dans les dossiers → `aff-r-nuit-pieton-sombre` ne chiffre
   que la portée des feux de croisement (30 m, `m-feux-portees`).
5. **Recouvrement `b58` (reconnaissance) ↔ `r-loi-montagne-periode` + `aff-r-montagne-ms`** : le verso
   de `b58` porte déjà toute la règle (3PMSF, M+S, dates). Conservé parce que la carte des
   connaissances demande explicitement « Q + F » sur ce point et que Q10 est une question officielle ;
   à démoter si le volume de R devient excessif.
6. **Recouvrement `l-feux-detresse-usage` (fait L) ↔ `aff-r-autoroute-bouchon-detresse`** : le fait
   porte la règle générale (R416-18), l'affirmation la situation d'autoroute. Jugé acceptable.
7. **`r-pluie-feux` ↔ `m-feux-jour-limite`** : la carte M répond « les feux de jour suffisent-ils ? »,
   la carte R « l'éclairage est-il obligatoire de jour sous la pluie ? ». Formulations séparées
   volontairement ; à surveiller.
8. **Klaxon en montagne** (R416-1, avertissement hors agglomération) : écarté, `m-appel-phares` et
   `l-agglomeration-panneau` couvrent déjà la règle.
9. **B15 / C18, K10, chevrons, A16, A24, C111** : traités comme cartes de **reconnaissance** ; aucune
   carte R ne redit leur signification, seulement la conduite en situation.
