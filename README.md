# Code de la route 2026 — comprendre, rappeler, décider

Deck Anki en français pour l’ETG du permis B, **édition v5, révisée le 21 septembre 2026**.

**[Télécharger le deck complet](out/Code-de-la-route-2026.apkg)**. Les [statistiques générées](out/STATS.md)
donnent les effectifs exacts. Le deck relie les règles, la reconnaissance des signaux et leur application
à 51 objectifs. Il comprend des schémas simplifiés, pas des photographies d’examen.

La v5 corrige des généralisations encore présentes en v4, resserre les rappels de sanctions,
ajoute des cas où une condition change la réponse et améliore le rendu sur téléphone.
Voir le [bilan critique](docs/10-bilan-v5.md), les [imports vérifiés](out/VERIFICATION.md)
et les [contrôles de rendu](out/RENDU.md).

## Commencer

1. Importer le **paquet complet** dans une collection neuve avec une version récente d’Anki.
   Cocher « Importer les préréglages de deck ». Étudier le parent **Code de la route 2026**.
2. Lire les [repères expliqués](out/COMPRENDRE.md) avant les premières cartes d’un thème.
   Ils restent accessibles hors ligne au verso, dans « Comprendre ce thème ».
3. Faire les révisions dues avant les nouvelles cartes. Le préréglage propose **20 nouvelles/jour**,
   avec ordre progressif et enfouissement des cartes sœurs. Diminuer ce débit si les révisions
   s’accumulent ; ce n’est ni une prescription ni une promesse de durée quotidienne.
4. Commencer dès la première semaine de courtes séries corrigées sur **photos et vidéos**,
   puis des examens blancs nouveaux, chronométrés. Anki entraîne le rappel ; les scènes nouvelles
   entraînent aussi la perception, la recherche d’indices et la décision sous contrainte de temps.

Le [programme](out/PROGRAMME.md) donne l’ordre et les durées minimales d’introduction, pas un délai
pour être prêt. Les cartes du socle passent avant la consolidation ; les deux étapes couvrent des
compétences utiles. Le [paquet Socle](out/Code-de-la-route-2026-Socle.apkg) est une extraction de la
première étape, pas un autre programme ni une préparation suffisante à lui seul. Inutile d’importer
les deux en même temps. Le passage **Socle v5 → complet v5** est vérifié.

Cette édition est conçue pour votre **premier import**. Des notes et des numéros de cloze ont changé :
ne pas l’importer sur une v4 étudiée en espérant conserver le sens de toutes les anciennes cartes.
Une migration depuis v2/v3/v4 n’est pas fournie. Les réimports de la même v5 sont testés.

## Répondre et s’évaluer

Répondre **avant** de retourner, en une phrase ou à voix haute. Pas de récitation mot à mot :

| Carte | Réponse attendue |
|---|---|
| Signal | Son sens utile ; son code administratif n’est pas à réciter |
| Comparaison A/B | La différence qui change la règle ou la conduite |
| Trou | La valeur avec l’unité, ou le terme demandé |
| Décision / scénario | L’action et l’indice ou la règle décisive |
| Vrai/faux | Le verdict justifié ; corriger la proposition fausse |

**À revoir** si la réponse est fausse, devinée, ou si la raison essentielle manque.
**Difficile** pour une réponse correcte obtenue avec effort ; **Bon** si correcte sans difficulté.
Les explications et encadrés du verso ne sont pas des éléments supplémentaires à réciter.
Une réponse valide formulée autrement doit être acceptée. Les versos longs se lisent en défilant.

Après une erreur récurrente, relire le repère puis comparer les conditions d’un cas voisin.
Les [familles de cas](out/CONCEPTION.md) montrent ces différences. Si une carte reste ambiguë ou trop
chargée, corriger sa formulation ; ne pas apprendre une réponse douteuse par répétition.
Utiliser le [carnet d’erreurs](docs/07-entrainement.md) pour distinguer règle oubliée, indice manqué,
lecture de l’énoncé et précipitation. Chercher d’abord une carte existante dans la
[couverture](out/COUVERTURE.md) avant d’ajouter un doublon.

L’ETG demande **35 bonnes réponses sur 40**. Des résultats réguliers de 37–38 sur des séries
**nouvelles**, sans aide et au rythme de l’épreuve, constituent une marge personnelle de préparation,
pas une garantie ni un seuil officiel supplémentaire.
[Conditions officielles](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694).
Ni terminer le deck ni avoir un bon taux de réussite Anki ne prouve l’aptitude à l’examen.
Les gestes de secours bénéficient aussi d’une formation pratique.

## Reconstruire et maintenir

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements-qa.txt
.venv/bin/python -m build.build --check
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m build.build
.venv/bin/python -m build.verify
.venv/bin/python -m build.render_check
```

`requirements.txt` suffit au build et aux imports ; `requirements-qa.txt` ajoute Playwright pour
les contrôles visuels. Installer Chrome/Chromium système pour ces derniers. Les premiers médias
Commons sont téléchargés ; le cache permet ensuite les builds hors ligne. Le paquet contient les
médias et les repères nécessaires à l’étude hors ligne. Seule la consultation des sources demande Internet.

Pour une modification :

1. Définir la connaissance ou la décision à apprendre, vérifier la règle **et ses conditions** dans
   une source primaire actuelle. Inscrire la consultation et sa portée dans
   [`source_checks.yaml`](data/_meta/source_checks.yaml). Une ancienne référence ne vaut pas revalidation.
2. Modifier `data/`. La reconnaissance est générée : modifier `signs_inventory.yaml` ou
   `_meta/sign_overrides.yaml`, puis exécuter `python build/import_signs.py`.
   `reconnaissance/voyants.yaml` est rédigé directement.
3. Relier les notes aux objectifs dans `_meta/objectives.yaml` et aux familles de cas si utile.
   Consigner les retraits avec leur couverture restante. Les délais administratifs et statistiques
   n’ont pas à devenir des cibles de rappel lorsqu’une consultation est plus pertinente.
4. Pour plusieurs seuils dans une note, préférer `rappels` autonomes : chaque recto doit se suffire
   sans afficher les réponses sœurs. Garder ensemble une procédure courte cohérente, comme le cycle RCP.
   Voir la [conception des cartes](docs/03-conception-des-cartes.md).
5. Exécuter les commandes ci-dessus. Inspecter les captures dans `out/qa/render/`, notamment les
   nombres, flèches et petits textes **dans les images** : les mesures DOM ne les comprennent pas.
   Après toute nouvelle modification, reconstruire avant de revérifier le paquet.
6. Relire le diff et actualiser le bilan. Pour une diffusion ultérieure à des utilisateurs ayant
   étudié le deck, traiter explicitement les suppressions, changements de schéma ou de cibles de cloze.

Les rapports [ROLES](out/ROLES.md), [COUVERTURE](out/COUVERTURE.md) et
[SELECTION-SIGNAUX](out/SELECTION-SIGNAUX.md) rendent les choix inspectables. Ils ne prouvent pas
l’exhaustivité de la banque confidentielle. La [documentation des sources](docs/04-sources.md)
distingue les vérifications ciblées des références héritées. Reconsulter en priorité les règles locales,
les sanctions, les équipements et les recommandations de secours ; revoir l’échéance 2027 des places
en amont des passages piétons avant de publier une édition 2027.

## Licences

Textes, code et schémas originaux : CC BY-SA 4.0. Médias Commons : licence propre à chaque fichier,
auteurs et liens dans [ATTRIBUTIONS](out/ATTRIBUTIONS.md). Ce deck n’est pas une publication officielle.
