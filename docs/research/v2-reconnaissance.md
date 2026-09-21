# v2 — Resserrage des versos de reconnaissance

Date : 21 septembre 2026. Objet : point 2.3 de `docs/05-audit-v2.md` (« les versos de reconnaissance sont
encombrés »). Périmètre : les 425 notes `data/reconnaissance/*.yaml`.

Méthode : toutes les corrections passent par `data/_meta/sign_overrides.yaml` (clé = id de la note), puis
`python build/import_signs.py` régénère les fichiers. Seul `voyants.yaml`, écrit à la main, est édité
directement. Les phrases de catégorie répétées (implantation des panneaux de danger, portée d'une
prescription, position d'un panonceau…) sont déjà retirées à l'import par la liste `BOILERPLATE` : elles
n'ont pas été réécrites.

Plafonds visés par champ : **signification ≤ 25 mots**, **conduite ≤ 20**, **complément ≤ 30** (uniquement
ce qui est propre au signal), **piège ≤ 25**. Plafond de build inchangé : verso ≤ 90 mots.

## 1. Résultat

État « avant » = état du dépôt au début du travail (boilerplate déjà retiré à l'import).

| Fichier | notes | resserrées | dont > 90 mots | méd. avant | max avant | méd. après | max après |
|---|--:|--:|--:|--:|--:|--:|--:|
| `autres.yaml` | 7 | 5 | 2 | 47 | 150 | 37 | 59 |
| `balises.yaml` | 13 | 9 | 1 | 52 | 128 | 44 | 65 |
| `feux.yaml` | 14 | 11 | 9 | 102 | 134 | 58 | 72 |
| `marquages.yaml` | 30 | 25 | 17 | 98 | 176 | 60 | 72 |
| `panneaux_danger.yaml` | 29 | 11 | 2 | 48 | 121 | 40 | 72 |
| `panneaux_direction.yaml` | 7 | 1 | 0 | 31 | 76 | 31 | 60 |
| `panneaux_fin.yaml` | 13 | 1 | 0 | 18 | 73 | 18 | 70 |
| `panneaux_indication.yaml` | 57 | 17 | 6 | 42 | 175 | 37 | 76 |
| `panneaux_interdiction.yaml` | 41 | 14 | 6 | 52 | 180 | 43 | 74 |
| `panneaux_localisation.yaml` | 6 | 2 | 1 | 52 | 128 | 52 | 73 |
| `panneaux_obligation.yaml` | 18 | 11 | 2 | 50 | 106 | 35 | 72 |
| `panneaux_priorite.yaml` | 9 | 7 | 6 | 118 | 188 | 69 | 73 |
| `panneaux_services.yaml` | 22 | 1 | 0 | 10 | 45 | 10 | 38 |
| `panneaux_zones.yaml` | 16 | 6 | 6 | 33 | 145 | 33 | 73 |
| `panonceaux.yaml` | 81 | 11 | 2 | 19 | 129 | 19 | 70 |
| `passage_a_niveau.yaml` | 3 | 2 | 1 | 89 | 141 | 68 | 76 |
| `temporaire.yaml` | 31 | 11 | 1 | 35 | 156 | 33 | 76 |
| `voies_reservees.yaml` | 2 | 1 | 1 | 156 | 263 | 64 | 79 |
| `voyants.yaml` | 26 | 7 | 0 | 44 | 90 | 42 | 68 |
| **Total** | **425** | **153** | **63** | **39** | **263** | **35** | **79** |

Global : moyenne 50,2 → **37,8 mots** ; médiane 39 → **35** (cible ≤ 35 atteinte) ; maximum 263 → **79**
(cible ≤ 90 atteinte) ; cartes au-dessus de 70 mots : 102 → **23** ; au-dessus de 90 : 63 → **0**.
Volume total des versos : 21 316 → 16 069 mots (−25 %). `python -m build.build --check` ne signale plus
aucun « verso trop long » ; `python build/import_signs.py` ne signale aucune clé d'override orpheline.

Les 23 cartes encore au-dessus de 70 mots sont des signaux à forte valeur d'examen qui portent quatre
champs pleins : `vr-losange-debut` (79), `triangle-presignalisation` (76), `g1` (76), `c25a` (76),
`c24a` (75), `b14` (74), `b1` (74), `eb10` (73), `b30` (73), `ab4` (73), `ab3a` (73), `ab25` (73),
`marq-ligne-effet-feux` (72), `feu-jaune-fixe` (72), `c207` (72), `c107` (72), `b26` (72), `a18` (72),
`marq-ligne-jaune-zigzag` (71), `c28` (71), `c12` (71), `b6a1` (71), `b15` (71).

## 2. Ce qui a été systématiquement supprimé

- Les **listes de variantes** : `sr3a` énumérait SR3b/SR3c1-c3/SR3d/SR3e (95 mots de complément),
  `b14` ses douze valeurs de vitesse, `m9v1` la généalogie de M9v2/M9v3/M9v4.
- Les **notes de fabrication** qui avaient fui dans les cartes : noms de fichiers Commons dans
  `b1` (« France road sign B1+M9.svg »), `b5c`, `a15a2`, `j10`, `a9b`.
- L'**historique et les dates de création** sans valeur d'examen : B21f supprimé en 1984 (`ab25`),
  C109/C110 remplacés en 2008 (`b54`), ZCR devenues ZFE-m (`b56`), anciennes acceptions IISR de
  C65a/C65b (`c65a`), arrêté du 31 décembre 2012 (`c9`), sas vélo « créé en 1998 » (`marq-sas-velo`).
- Les **répétitions de la signification dans le complément** (`c6`, `a16`, `a2b`, `feu-jaune-clignotant`).
- Les **généralités de famille** déjà portées par une carte de règle : implantation des signaux avancés,
  portée d'une prescription, « la signalisation temporaire prévaut sur la permanente ».
- Les **détails de comparaison internationale** (« contrairement aux États-Unis », « pas de rouge + jaune
  comme en Allemagne », déploiement des voies à losange à Lyon/Grenoble/Nantes).

## 3. Les dix cas où j'ai hésité

1. **`marq-ligne-continue` — les écarts de 1 m / 1,50 m.** Le complément portait l'exception R412-19 *et*
   l'écart latéral obligatoire lors du dépassement d'un cycliste. J'ai gardé l'exception (c'est la seule
   dérogation écrite au franchissement) et retiré les écarts : ils relèvent du dépassement des cyclistes,
   pas de la lecture du marquage, et ils ont leur propre carte de fait. Verso 176 → 69.

2. **`b14` — la règle du support commun avec EB10.** Elle figurait en double, dans `b14` et dans `eb10` ;
   la relecture v1 (point 6) l'avait déjà signalé. Je l'ai gardée **une seule fois**, dans `eb10`, parce
   que c'est là que le candidat la rencontre (lecture d'une entrée d'agglomération), et j'ai mis dans
   `b14` ce qui lui est propre : la fin de la limitation et la limitation posée sur un panneau de danger.

3. **`eb10` — le « 70 » de relèvement.** La relecture v1 avait ajouté « un 70 implanté après l'EB10 ne
   vaut que sur la route concernée ». Je l'ai supprimé pour tenir le plafond du complément, en gardant la
   liste des panneaux qui partagent le support et l'avertissement E31 (lettres italiques blanches sur fond
   noir ≠ agglomération), qui est une **ERREUR corrigée** en v1 et donc intouchable. À rétablir si l'on
   juge le relèvement de vitesse testé à l'examen — il tiendrait mieux dans une carte de fait.

4. **`ab25` — les deux clignotants du giratoire.** J'ai coupé « voie de droite pour les premières
   sorties » (couvert par les scénarios de giratoire) mais gardé « clignotant gauche si je dépasse la
   moitié », qui est la question réellement posée à l'épreuve. J'ai aussi gardé en entier l'opposition
   giratoire (priorité à l'anneau) / rond-point sans cédez-le-passage (priorité à droite) : c'est le
   piège n° 1 du thème.

5. **`ab4` — « peut surmonter un panneau G1 ».** Supprimé de `ab4`, conservé dans `g1` (« un AB4
   au-dessus impose l'arrêt »). Le candidat voit la croix de Saint-André, pas le STOP isolé ; la
   connaissance est donc utile du côté du passage à niveau.

6. **`feu-rouge` — le véhicule prioritaire en intervention.** Supprimé : c'est une règle de famille
   (elle vaut pour tous les feux et pour les panneaux), pas une propriété du feu rouge. J'ai gardé en
   revanche « les roues au-delà de la ligne, c'est déjà un feu grillé », qui est la question piège.

7. **`marq-ligne-cedez` — les « dents de requin ».** La relecture v1 avait établi que les triangles
   blancs au sol signalent en France un **ralentisseur**, pas un cédez-le-passage. J'ai réduit le piège à
   cette phrase et supprimé la mention Belgique/Pays-Bas. La correction est préservée, et elle reste
   cohérente avec `marq-ralentisseur-triangles` et `conf-stop-cedez-lignes`.

8. **`b58` / `b26` — le marquage 3PMSF.** La signification de `b58` est une **ERREUR corrigée** en v1
   (le seul M+S ne suffit plus depuis le 1er novembre 2024). Je l'ai ramenée de 51 à 25 mots en gardant
   les quatre éléments testables (zone de montagne, 1er novembre–31 mars, 3PMSF, chaînes pour deux roues
   motrices) et en déplaçant « M+S ne suffit plus depuis 2024 » dans le complément, où elle reste lisible.

9. **`c207` — la vitesse minimale.** Le verso mélangeait « véhicules ne pouvant dépasser 40 km/h » et
   « minimale 80 km/h sur la voie de gauche ». J'ai gardé le 80 (valeur d'examen, R413-19) et retiré le
   40, dont la relecture v1 avait déjà écarté l'équivalent sur `c107` faute de source. Voir § 4.

10. **`vr-losange-debut` — la signalisation expérimentale.** 263 mots, dont un paragraphe entier de
    références réglementaires (arrêtés 2020/2024/2025/2026, absence de code IISR) et la liste des villes.
    J'ai tout retiré sauf « sans panonceau, le losange vaut bus + taxis + covoiturage 2+ », qui est la
    seule information dont le candidat a besoin devant l'image. La carte reste la plus longue du deck (79).

## 4. Incohérences factuelles repérées, non corrigées ici

Elles dépassent le simple resserrage ; elles sont listées pour une passe de fond.

1. **`c207` — « véhicules ne pouvant dépasser 40 km/h »** (`data/signs_inventory.yaml`). L'accès de
   l'autoroute est interdit aux véhicules qui ne peuvent atteindre **80 km/h** en palier (R421-2) ; le
   seuil de 40 km/h ne correspond à rien. La relecture v1 avait déjà fait retirer la même phrase de
   `c107` (point 15). J'ai contourné la valeur dans le verso réécrit, mais la source n'est pas corrigée.

2. **`marq-ligne-bau-t4` — deux distances pour la même règle.** Le verso donnait « deux traits ≈ 90 m,
   soit un peu plus de 2 secondes » puis « la distance de sécurité de 2 s à 130 km/h ≈ 73 m ». Les deux
   sont exacts mais se lisent comme une contradiction. J'ai gardé la première formulation seule ; il
   faudrait décider laquelle le deck enseigne (la règle des deux traits est la convention d'auto-école).

3. **`a2b` — « exclusivement en agglomération ».** Le complément disait d'abord « uniquement en
   agglomération », puis « (ou sur voies limitées à 30 km/h) ». Le décret 94-447 autorise le dos-d'âne
   hors agglomération sur les sections limitées à 30 ; la formulation reste ambiguë et mériterait d'être
   tranchée dans l'inventaire.

4. **`c111` et `c9` — le faux code « C9 ».** Les deux notes portaient l'avertissement « C9 est utilisé à
   tort pour le tunnel ». Je l'ai gardé sur `c9` (station d'autopartage, là où la confusion se produit)
   et retiré de `c111`. À vérifier : la carte de confusion correspondante n'existe pas.

5. **`sr3a` / `sr3e` — doublon.** SR3e (radar tronçon) était décrit à la fois dans le complément de
   `sr3a` et dans sa propre note. Le doublon est supprimé, mais `sr3a` et `sr3e` restent deux cartes très
   proches visuellement, sans carte de confusion.

6. **`e42` — code couleur des cartouches.** Le complément (34 mots) *est* la connaissance de la carte,
   il dépasse donc le plafond. Il vaudrait mieux en faire une carte de fait (cloze) « rouge = A/N,
   jaune = D, blanc = C/VC, vert = E, bleu = M » et laisser à `e42` sa seule identification.

7. **`m8d`** porte encore, dans sa signification, la description de `m8e` et `m8f` (héritage de la
   correction v1, point 18). Je l'ai déplacée dans le complément, mais trois notes décrivent toujours
   partiellement les deux autres : un jeu de trois cartes autonomes serait plus propre.

8. **Plafonds par champ non atteints sur ~40 notes courtes** (verso total ≤ 70, mais un champ au-dessus
   de son plafond : `kc1`, `c117`, `marq-plateau-sureleve`, `a8`, `m7`… ont été traités ; il reste des
   dépassements de 1 à 5 mots, sans effet sur la lisibilité). Aucun n'est bloquant pour le build.
