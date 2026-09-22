# Deck Anki du Code de la route 2026

Un deck Anki en français pour **réussir l’épreuve théorique générale** (ETG, permis B) telle qu’elle existe
en 2026, et comprendre les règles assez bien pour les appliquer à des situations nouvelles.
Il est généré à partir d’une bibliothèque de connaissances écrite à la main (`data/`) par le code de `build/`.

**[Télécharger le paquet](out/Code-de-la-route-2026.apkg)**. Effectifs exacts dans [STATS](out/STATS.md).
Le deck relie les signaux, les règles, les décisions et des scénarios dessinés à
49 objectifs d’apprentissage. Il ne contient pas de photographies d’examen.

## Commencer

1. Au premier import dans Anki (version récente), cocher **« Importer les préréglages de deck »** : c’est
   ce préréglage qui fait arriver les nouvelles cartes dans l’ordre calculé (position la plus basse) et qui
   enfouit les cartes sœurs. Sans lui, l’ordre dépend de vos options existantes.
   Vérification : Options du deck → Ordre d’affichage → collecte des nouvelles cartes par **position
   croissante**, tri dans **l’ordre de collecte**.
2. Étudier le deck parent **Code de la route 2026**. L’ordre d’introduction entrelace les thèmes ; les
   cartes du socle précèdent la consolidation (variantes, exceptions, applications). Le nombre
   de nouvelles cartes par jour est un réglage personnel.
3. L’écran de chaque sous-deck affiche le **repère** du thème (principe, exemple, transfert) ; les mêmes
   textes sont réunis dans [REPERES](out/REPERES.md), pour retrouver le principe derrière une carte.
4. Faire en parallèle, dès le début, des séries de questions sur **photos et vidéos** puis des examens
   blancs chronométrés : Anki entraîne le savoir, les distinctions et le raisonnement ; la perception d’une
   scène nouvelle et la décision sous contrainte de temps s’entraînent sur des scènes nouvelles.

L’ETG demande 35 bonnes réponses sur 40 ([conditions officielles](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694)).
Réussir les cartes ne prouve pas l’aptitude à l’examen ; des séries nouvelles réussies régulièrement en donnent
une meilleure idée.

## Options Anki

FSRS s’active dans les options d’Anki pour toute la collection, pas par l’import du paquet.
Le préréglage fourni fixe l’ordre d’introduction et enfouit les cartes sœurs ; les limites quotidiennes
et la rétention souhaitée restent des choix personnels. Voir le [guide Anki](https://docs.ankiweb.net/deck-options.html#fsrs).
Les positions des cartes nouvelles organisent leur introduction ; après les réponses, le planificateur
calcule leurs échéances.

Le dépôt permet de reconstruire une édition, mais ne garantit pas la migration d’une édition à l’autre
si des notes changent de type ou sont supprimées. Le paquet est destiné ici à un premier import.

## Répondre et s’évaluer

Répondre **avant** de retourner la carte, avec ses propres mots ou à voix haute. Pas de récitation mot à mot :

| Carte | Réponse attendue |
|---|---|
| Signal | Son sens utile et ce qu’il change pour moi ; son code n’est pas à réciter |
| Comparaison A/B | La différence qui change la règle ou la conduite |
| Trou | La valeur avec son unité, ou le terme demandé |
| Question / scénario | La réponse demandée : décision justifiée, distinction ou calcul avec sa méthode |
| Vrai/faux | Le verdict **et** la raison ; si c’est faux, la règle exacte |

**À revoir** si la réponse est fausse, devinée, ou si la raison manque ; **Difficile** si elle est correcte avec
effort ; **Bon** pour un rappel correct ordinaire ; **Facile** si le rappel est immédiat et sans hésitation.
Une réponse juste formulée autrement est juste. L’explication
sous la réponse donne le mécanisme, la limite ou la distinction : elle se lit, elle ne se récite pas.
Les comparaisons utiles montrent les autres signaux avec leur sens en légende. Le volet
« Sources » contient la référence, le code technique et le nom officiel du signal ; ces codes ne sont pas à apprendre.

Pour retrouver une difficulté par compétence, utiliser les étiquettes `objectif::…` et
[COUVERTURE](out/COUVERTURE.md). Une carte ambiguë se corrige dans `data/`.

## Reconstruire

```bash
uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt
source .venv/bin/activate
python -m build.build --check      # structure des données (erreurs) et relecture éditoriale (avertissements)
python -m build.build              # médias, paquet, rapports dans out/
python -m build.verify             # import réel et réimport dans une collection temporaire
```

Le premier build télécharge les médias Commons (quelques minutes), ensuite tout est en cache. Les autres
commandes (tests, captures de cartes, contrôle du rendu) sont dans la [maintenance](docs/maintenance.md).
Les rapports [d’import](out/VERIFICATION.md) et [de rendu](out/RENDU.md) identifient le paquet contrôlé
par son SHA-256. Ils ne constituent pas une validation juridique exhaustive ; la portée des consultations
est dans le [registre des sources](data/_meta/source_checks.yaml).

- [Conception](docs/conception.md) : ce que le deck optimise, les formes de cartes, les principes de rédaction.
- [Maintenance](docs/maintenance.md) : structure des données, procédure de modification, contrôles.
- [Sources](docs/sources.md) : références utilisées et registre des consultations.
- [Comparaison avec le livre](docs/research/comparaison-livre-2025-2026.md) : apports retenus, divergences et limites.

## Licences

Textes, code et schémas originaux : CC BY-SA 4.0. Médias Wikimedia Commons : licence propre à chaque fichier,
auteurs et liens dans [ATTRIBUTIONS](out/ATTRIBUTIONS.md). Ce deck n’est pas une publication officielle.
