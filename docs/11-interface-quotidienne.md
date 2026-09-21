# Révision de l’interface de révision — septembre 2026

## Diagnostic et décisions, avant modification

Le point de départ est le commit `ec069bd`. Les deux captures signalées révèlent un problème commun
aux six gabarits : consignes de notation répétées, titres de thème, référence longue visible et
plusieurs niveaux d’encadrés concurrents. La correction est présente, mais sa hiérarchie est faible.
Les conseils de rédaction existants ne définissaient pas assez précisément ce qui doit apparaître
pendant une révision quotidienne.

Un relevé des 2 742 faces à 430 × 932 donne, par type, 84 à 110 mots médians au verso
(texte visible dans le DOM, hors texte des images). Ce chiffre diagnostique une charge ; ce n’est
pas une limite à imposer. Un échantillon de 34 notes combine les cas déjà suivis et les versos
courts, médians et longs de chacun des six types. Les captures initiales et mesures locales sont
conservées dans `out/qa/before-interface/`.

Décisions :

- Garder les six tâches de rappel et le parcours. Une modification de présentation ne justifie
  pas de refaire la structure des connaissances.
- Recto : situation, image utile et question. Pas de marque, sous-thème ou cours introductif.
- Verso : conserver le contexte pour comprendre la correction, mais lui donner moins de poids que
  la réponse. La réponse et le raisonnement correctif restent visibles sans ouverture de volet.
- Supprimer les consignes permanentes d’autoévaluation : elles sont déjà dans le guide de démarrage.
  Garder une consigne courte sur les affirmations, car « justifier » définit la tâche demandée.
- Regrouper source, désignation officielle, code et repère de thème dans un seul volet explicite.
  Les noms officiels souvent redondants ne constituent pas une deuxième réponse à apprendre.
- Ne pas déplacer globalement `Complement` dans ce volet : ce champ contient aussi des conditions
  de sécurité, par exemple la ligne du STOP ou la portée du M12. Réviser son contenu au cas par cas.
- Aligner la prose à gauche, limiter les traitements décoratifs, conserver des images lisibles.
  Aucune réduction automatique du texte, aucun rognage, aucune hauteur fixe de carte.
- Revoir les justifications sur l’auteur, les références aux anciennes questions et les précautions
  répétées. Conserver les réserves qui empêchent une mauvaise généralisation, comme le minimum
  de visibilité, les équipements hiver ou l’absence de garantie d’une durée de pause.
- Le tableau carburant reste un exercice de lecture et de calcul : sa colonne durée fournit une
  donnée à écarter, contrairement à une carte de rappel pur. Une seule mention de données fictives
  suffit ; le calcul constitue le retour utile.

## Appuis et limites

[SuperMemo, vingt règles de formulation](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge)
recommande compréhension préalable, questions précises et rappels simples. Ce sont des conseils
pratiques de formulation, pas la validation expérimentale de nos six gabarits ou d’un quota de mots.

[Anki, champs et indices](https://docs.ankiweb.net/templates/fields.html) distingue les informations
révélées sur demande et avertit contre les indices qui rendent le rappel artificiellement facile.
Ici, le volet n’existe qu’au verso ; aucune condition nécessaire n’est cachée au recto.

[Nielsen Norman Group, progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
recommande de laisser le travail fréquent au premier niveau et de donner un accès explicite au
secondaire. Nous l’appliquons aux références, pas au raisonnement que l’on doit comprendre après
une erreur. Il s’agit d’une décision d’interface, non d’une preuve de meilleure mémorisation.

[Mayer, principes de conception multimédia](https://www.benjamins.com/catalog/dd.1.1.02may)
étudie notamment la cohérence et la proximité entre mots et images. L’application à des cartes
Anki quotidiennes est une extrapolation : ces travaux ne justifient ni la suppression des nuances
nécessaires ni un maximum universel de texte.

[Apple, dimensions d’affichage](https://developer.apple.com/design/human-interface-guidelines/layout)
donne 430 × 932 points pour l’iPhone 15 Pro Max. C’est notre cadre navigateur principal, en clair
et sombre. Un cadre de 430 × 740 réserve arbitrairement davantage de place aux contrôles ; il ne
reproduit pas exactement AnkiMobile. 320 px reste un test de contrainte, pas la cible visuelle.

## Résultat éditorial

Les six gabarits ont été révisés ; **77 notes** ont reçu une modification de contenu (89 champs),
dont **42 comparaisons**. Le [journal avant/après](../data/_meta/interface_revision.json) permet de
relire chaque modification. Aucun ajout, retrait, changement de cible de cloze ou de parcours :
1 244 notes, 1 371 cartes dans le complet ; 588 notes, 652 cartes dans le Socle.

Quelques choix représentatifs :

| Cas | Changement et raison |
|---|---|
| Fatigue | Garder l’arrêt dès les signes, le besoin de dormir et la vigilance avant reprise ; enlever l’encadrement pédagogique répétitif. |
| Carburant | Calcul visible ; une seule mention de données fictives dans le tableau ; durée conservée comme donnée non pertinente à sélectionner. |
| STOP | Localisation de l’arrêt directement dans la réponse ; priorité du feu conservée ; suppression de la sanction accessoire à cette reconnaissance. |
| Comparaisons | Répondre avec A/B ; raccourcir dix discriminations particulièrement bavardes, puis le couple cédez-le-passage/STOP après rendu. |
| Agglomération | Garder l’effet du panneau sur la vitesse ; retirer la digression sur le stationnement. |
| Dépassement du cycliste | Remplacer le commentaire sur l’interprétation d’une photo officielle par le raisonnement du cas effectivement posé. |
| Compléments de signaux | Retirer six renvois composés seulement d’un code de fin et quelques détails de catalogue ; garder les conditions qui changent l’application. |
| Rappel de vitesses C25a | Reconnaître la fonction du panneau sans réciter une table déjà étudiée ; la simplification du dessin reste explicite. |
| Scénarios | Quatre réponses recentrées sur la décision dans la scène ; la règle générale reste dans l’explication visible. |

Le mot « piège » ne précède plus chaque nuance : certaines décrivent simplement un indice visuel.
Les lignes de séparation marquent le passage question/réponse et l’accès aux références ; les
explications ne sont plus enfermées dans une succession de boîtes. L’espacement insécable avant
la ponctuation haute française évite notamment les points d’interrogation isolés en bout de carte.

## Vérification et portée

Les contrôles du paquet livré figurent dans [VERIFICATION](../out/VERIFICATION.md) et
[RENDU](../out/RENDU.md), avec leurs empreintes SHA-256. La suite compte **17 tests réussis**,
y compris l’ouverture au clavier, la fermeture et la présence des explications hors du volet
pour les six modèles. Les imports réels vérifient aussi le passage Socle → complet et le réimport.
Les gabarits n’utilisent pas de JavaScript personnalisé ni de nouvelle dépendance d’exécution.

Inspection visuelle : 34 versos représentatifs, rectos des six formats en mode sombre, les deux
cartes signalées individuellement, un volet ouvert, puis quatre cas supplémentaires de grande
hauteur détectés par mesure. Les captures finales couvrent **38 notes**, dont plusieurs ordinaux.
Les valeurs des tableaux, la distinction des panneaux et les flèches des scènes ont été regardées,
en complément des tests DOM. C’est un échantillon raisonné ; les 1 371 cartes n’ont pas toutes reçu
une nouvelle inspection visuelle individuelle.

Le contrôle automatique couvre les deux faces de toutes les cartes dans les quatre configurations
mobiles, puis l’échantillon sur bureau. Il vérifie les médias hors ligne, le débordement horizontal,
les gabarits résolus, l’isolation des clozes et les références fermées par défaut. Les ouvertures et
fermetures sont testées sur l’échantillon. La hauteur et la position de la réponse sont mesurées ;
le défilement n’est pas interdit. L’outil efface ses anciennes captures pour éviter de confondre
une ancienne édition avec le paquet courant, et refuse un paquet modifié pendant le contrôle.

Non vérifié : AnkiMobile sur un iPhone physique, son chrome natif et ses gestes, tous les réglages
d’agrandissement du texte, ni l’efficacité d’apprentissage longitudinale. Cette révision éditoriale
ne constitue pas une nouvelle vérification juridique exhaustive : voir la portée des contrôles de
sources de la v5. La qualité de l’interface n’est pas une preuve de préparation à l’ETG.

## Captures et mesures comparables

Captures à **430 × 932**, même largeur avant/après. Les versions pleine hauteur gardent le contenu au-delà du premier écran.

| Exemple | Avant | Après |
|---|---|---|
| Fatigue | [Capture](rendered-v5.1/fatigue-avant.png) | [Capture](rendered-v5.1/fatigue-apres.png) |
| Carburant | [Capture](rendered-v5.1/carburant-avant.png) | [Capture](rendered-v5.1/carburant-apres.png) |
| Stop | [Capture](rendered-v5.1/stop-avant.png) | [Capture](rendered-v5.1/stop-apres.png) |
| Comparaison | [Capture](rendered-v5.1/comparaison-avant.png) | [Capture](rendered-v5.1/comparaison-apres.png) |

Autres vues : [mode sombre](rendered-v5.1/fatigue-sombre.png), [cloze au recto](rendered-v5.1/cloze.png), [scénario](rendered-v5.1/scenario.png), [références ouvertes](rendered-v5.1/references.png).

Nombre médian de mots affichés au verso (DOM visible, hors texte dans les images ; référence fermée) :

| Type | Avant | Après |
|---|---:|---:|
| Affirmation | 94 | 58 |
| Confusion | 96 | 43 |
| Fait | 93 | 61 |
| Question | 108 | 72 |
| Reconnaissance | 84 | 38 |
| Scenario | 109.5 | 74.5 |

Ces réductions mesurent le texte présenté, pas un gain de rétention ou de réussite. Les réponses et explications essentielles restent au premier niveau.

Résultat final : **11 062 faces/configurations contrôlées**, aucun échec, 235 essais d’ouverture/fermeture et 942 captures.

À 430x932_light : aucun bloc de réponse principale (ou verdict) ne dépasse le premier écran ; le volet des références commence après le premier écran sur 1 verso.

À 430x740_dark : aucun bloc de réponse principale (ou verdict) ne dépasse le premier écran ; le volet des références commence après le premier écran sur 33 versos. L’explication qui précède peut donc demander un défilement.

Empreinte du paquet auquel correspondent ces captures : `60d7c0488eabe64327924932ce284d0667eb7f818d56eaebd6abaf34909d9e00`.
