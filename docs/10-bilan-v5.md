# Bilan critique — v5, 21 septembre 2026

La structure existante méritait d’être conservée : contenu séparé des gabarits, objectifs explicites,
scénarios calculables, médias attribués, repères explicatifs et imports Anki vérifiables. Le problème
principal était **la précision de certaines tâches et de leurs conditions**, jusque dans des notes
marquées comme déjà révisées. Une couverture reliée à des objectifs ne suffit pas à rendre chaque
phrase exacte ou chaque répétition utile.

Bilan de la modification : **75 notes existantes révisées, 8 ajoutées, 4 retirées**.
Le complet passe de 1 393 cartes / 1 240 notes à **1 371 cartes / 1 244 notes**.
Ces nombres décrivent le travail ; ils ne mesurent pas son efficacité.

## Connaissances et couverture

La bibliothèque couvre les grandes familles de l’ETG : signalisation, circulation, conducteur,
route, usagers, réglementation, secours, installation, mécanique, passagers et environnement.
La revue a porté sur cette organisation, les faits chiffrés, les décisions par thème, les affirmations
à risque de généralisation et les applications ajoutées. Elle n’est pas une certification indépendante
de chacune des phrases des 1 244 notes.

| Problème constaté | Décision mise en œuvre |
|---|---|
| C107 expliqué comme une limite de 110 par défaut ; séparateur et nombre de voies confondus | Correction du rappel et de la représentation canonique ; deux applications visuelles avec le même signal mais une route différente |
| STOP sans ligne décrit au niveau du panneau dans la reconnaissance, en contradiction avec la carte de décision | Correction de l’inventaire et de la surcharge canonique : limite de la chaussée abordée, vérifiée dans R415-6 |
| Mnémotechnique « trois 50 » assimilée à une règle de distance dans le brouillard | Distinguer seuil de visibilité, plafond de vitesse, intervalle minimal et adaptation à la distance réellement visible |
| Interdiction générale de dépasser dans tout giratoire ; voie centrale présumée commune aux deux sens | Retrait des généralisations ; décision sur un camion empiétant sur les voies, lecture de l’affectation et des conditions de dépassement |
| Chemin de terre assimilé nécessairement à une voie privée fermée au public | Expliquer la catégorie explicitement visée par R415-9, sans déduire le régime de la seule propriété |
| Pause présentée comme suffisante après une durée fixe ; facteurs de réaction/freinage trop universels | Reprise seulement après récupération ; hypothèses explicites des modèles, distinction temps/distance et réaction/freinage |
| Compression de toute plaie, extinction d’incendie trop prescriptive, DAE présenté sans critère de victime | Conditions précisées ; objet planté, sécurité du sauveteur et indication du DAE ; retrait d’une consigne de brûlure étrangère à la question |
| Statistiques ou effets individuels trop précis dans des explications | Retrait de multiplicateurs non contextualisés ; garder mécanisme, anticipation et action |
| Crit’Air réduit à la date et généralisé à tous les véhicules | Catégorie, énergie, norme Euro ou date à défaut ; exemples explicitement limités aux voitures |
| Peines maximales prises pour sanctions automatiques ; insinuation sur une ancienne banque ETG | Rappels centrés sur délit, seuils et points ; maxima qualifiés ; aucune prédiction du contenu confidentiel |

Les vérifications externes ciblées sont consignées dans les entrées `v5-*` du
[registre](../data/_meta/source_checks.yaml), avec notes et portée exactes. Elles s’appuient notamment
sur [les vitesses](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006159600),
[le dépassement](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074228/LEGISCTA000006177131/),
[les sanctions](https://www.service-public.gouv.fr/particuliers/vosdroits/F19460),
[Crit’Air](https://www.service-public.gouv.fr/particuliers/vosdroits/F33371) et
[le PSC de juillet 2026](https://www.securite-civile.interieur.gouv.fr/documentation/secourisme-et-associations/secourisme-references-techniques-nationales.html).
Les règles locales EDPM et les seuils alcool/stupéfiants ont également été reconsultés.

## Apprentissage

Conserver les six formes de cartes permet de choisir la tâche : reconnaître, distinguer, rappeler
ou appliquer. Les transformer toutes en QCM aurait surtout facilité la reconnaissance des réponses.
Les affirmations exigent une justification ; une décision correcte devinée ne suffit pas.

Les cycles courts cohérents PAS et RCP sont maintenant des unités de rappel, sans cartes qui demandent
séparément chaque morceau d’une séquence. Plusieurs cartes de sanctions perdent leurs listes de
montants et de peines de prison à réciter. Les conditions et unités importantes restent entraînées.
Quatre notes sont retirées avec motif et couverture : délai de fourrière, barème de paiement,
résultats arithmétiques fixes d’écoconduite et doublon de sortie d’autoroute manquée.

Huit applications sont ajoutées : C107 dans deux configurations, priorité face à un conducteur qui
ne ralentit pas, objet dans une plaie, inconscience traumatique, fatigue persistante après pause,
lecture d’un tableau de consommation et PTAC d’une remorque vide. Une proposition d’intervalle
avait déjà un équivalent exact : elle a été écartée au contrôle des doublons.
Les prérequis visuels restent placés avant les applications. Les objectifs couvrent les ajouts.

Le paquet conserve une bibliothèque large de signaux ; les bases viennent avant les variantes.
Il n’est pas nécessaire de connaître le code administratif d’un panneau. La révision n’ajoute pas de
photographies synthétiques susceptibles d’inventer une géométrie ou une signalisation. Les scènes
photo/vidéo nouvelles et examens blancs restent le support du travail perceptif et temporel.

## Rendu et réalisation

Les cartes réellement rendues ont révélé des comparaisons empilées trop haut sur téléphone.
Les deux images sont désormais côte à côte, repérées A/B. Les textes secondaires ont un contraste
renforcé en clair et en sombre ; les tableaux fictifs ont des caractères agrandis.
L’inspection a aussi détecté un libellé de tableau trop large après agrandissement ;
il est passé sur deux lignes, avec un contrôle de ses limites. Le build et le vérificateur
de paquets existants sont conservés.

Le nouveau `build.render_check` importe **le fichier APKG livré** dans une collection temporaire,
utilise les rectos/versos produits par Anki, puis les charge dans Chromium sans réseau externe.
Il mesure toutes les faces à 390 px en clair et 320 px en sombre, ainsi qu’un échantillon à 960 px.
Il contrôle débordement horizontal, images chargées, clozes, isolation des rappels, gabarits résolus et
repères fermés. Un test négatif vérifie qu’il détecte une image invalide et un débordement, sans
confondre cloze ordinaire et groupe de rappels indépendants.

## Vérification et limites

Les résultats exacts et empreintes du paquet figurent dans [VERIFICATION](../out/VERIFICATION.md)
et [RENDU](../out/RENDU.md) ; les effectifs dans [STATS](../out/STATS.md).
Les **15 tests automatisés passent**, sans test ignoré dans cet environnement.
Le détecteur de quasi-doublons à 0,95 ne relève qu’une paire de scénarios à trois véhicules :
les positions et l’ordre de passage diffèrent, donc les deux applications sont conservées.
Les tests couvrent aussi objectifs, prérequis, ordre du parcours, clozes natives et contraintes du
solveur de priorité. Les imports contrôlent Socle, complet, passage entre les deux et réimport
sans doublons. Ils ne promettent aucune migration depuis une v4 étudiée : cette édition est pour
un départ neuf, conformément à l’usage annoncé.

Les captures inspectées incluent signal, comparaison, cloze indépendant, affirmation, secours,
tableau et scénarios, sur téléphone en clair/sombre. Des versos nécessitent un défilement vertical :
il est permis, et les captures complètes ne masquent pas la fin. Les mesures de mise en page portent
sur toutes les cartes ; la lecture visuelle humaine reste un **échantillon**, pas 1 244 inspections.

Aucun essai sur appareils AnkiMobile/AnkiDroid réels ni mesure de rétention ou de réussite ETG n’a été
réalisé. Les sources héritées non reconsultées ne sont pas certifiées par les dates du registre.
Le contenu peut encore comporter des erreurs ; les corrections issues d’un enseignant ou de séries
nouvelles restent une source d’amélioration. Le [README](../README.md) donne le mode d’étude et la
procédure de maintenance, avec reconstruction puis revalidation après tout changement.

Exemples de rendus inspectés, conservés avec cette édition : [STOP](rendered-v5/ab4_c0_a_390.png),
[comparaison en mode sombre](rendered-v5/conf-ab3a-ab4_c0_q_320.png),
[tableau sur téléphone](rendered-v5/m-visuel-pression-charge_c0_q_320.png),
[lecture du marquage](rendered-v5/scn-dep-mixte-mon-cote_c0_q_390.png).
