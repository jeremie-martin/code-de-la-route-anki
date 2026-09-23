# Deck Anki du Code de la route 2026

Un deck Anki en français pour **réussir l’épreuve théorique générale** (ETG, permis B) telle qu’elle existe
en 2026, et comprendre les règles assez bien pour les appliquer à des situations nouvelles. Il est généré à
partir d’une bibliothèque de connaissances écrite à la main (`data/`) par le code de `build/`.

**[Télécharger le paquet](out/Code-de-la-route-2026.apkg)** (effectifs dans [STATS](out/STATS.md)). Le deck
relie signaux, règles, décisions et scénarios dessinés à 49 objectifs d’apprentissage ; chaque note a été
vérifiée contre une source primaire (registre dans [`docs/research/verification-2026-09`](docs/research/verification-2026-09/README.md)).
Il ne contient pas de photographies d’examen. État du droit : Code de la route consolidé au 10 septembre 2026,
règles datées revérifiées sur Légifrance du 21 au 23 septembre 2026.

## Étudier

1. Au premier import dans Anki (version récente), cocher **« Importer les préréglages de deck »** : ce
   préréglage fait arriver les nouvelles cartes dans l’ordre calculé et enfouit les cartes sœurs. Vérifier
   dans Options du deck → Ordre d’affichage : collecte des nouvelles cartes par **position croissante**, tri
   dans **l’ordre de collecte**. Le préréglage propose 20 nouvelles cartes par jour et une rétention de 90 % ;
   FSRS (réglage global d’Anki), les limites et la rétention s’ajustent selon chacun
   ([guide Anki](https://docs.ankiweb.net/deck-options.html#fsrs)).
2. Étudier le deck parent **Code de la route 2026**. Les thèmes sont entrelacés ; le socle précède la
   consolidation (variantes, exceptions, applications). L’écran de chaque sous-deck affiche le **repère** du
   thème (principe, exemple, transfert), réunis aussi dans [REPERES](out/REPERES.md).
3. Faire en parallèle, dès le début, des séries sur **photos et vidéos** puis des examens blancs chronométrés :
   Anki entraîne le savoir, les distinctions et le raisonnement ; la perception d’une scène nouvelle et la
   décision sous contrainte de temps s’entraînent sur des scènes nouvelles. L’ETG demande 35 bonnes réponses
   sur 40 ([conditions officielles](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694)).

**Mettre à jour** : réimporter une nouvelle édition du paquet (préréglages décochés) met les cartes à jour et
garde la progression. Une note retirée d’une édition reste dans la collection sans être mise à jour ; les notes
à supprimer sont nommées dans [VERIFICATION](out/VERIFICATION.md) (chercher `Id:…` dans le navigateur d’Anki).

## Répondre et s’évaluer

Répondre **avant** de retourner la carte, avec ses propres mots ou à voix haute :

| Carte | Réponse attendue |
|---|---|
| Signal | Son sens utile et ce qu’il change pour moi ; son code n’est pas à réciter |
| Comparaison A/B | La différence qui change la règle ou la conduite |
| Trou | La valeur avec son unité, le terme ou la décision demandés |
| Question / scénario | Décision justifiée, distinction ou calcul avec sa méthode |
| Vrai/faux | Le verdict **et** la raison ; si c’est faux, la règle exacte |

**À revoir** si la réponse est fausse, devinée ou sans raison ; **Difficile** si elle est correcte avec effort ;
**Bon** pour un rappel correct ordinaire ; **Facile** si le rappel est immédiat. Une réponse juste formulée
autrement est juste. L’explication donne le mécanisme, la limite ou la distinction : elle se lit, elle ne se
récite pas. Le volet « Sources » contient la référence et le code officiel du signal, qui ne sont pas à
apprendre. Après plusieurs erreurs sur un même sujet, rechercher l’étiquette `objectif::…` dans Anki ; les
objectifs et leurs notes sont dans [COUVERTURE](out/COUVERTURE.md). Une carte ambiguë ou fausse se corrige dans
`data/`.

## Reconstruire et maintenir

```bash
uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt
source .venv/bin/activate
python -m build.build --check      # structure des données (erreurs) et relecture éditoriale (avertissements)
python -m build.build              # médias, paquet, rapports dans out/
python -m build.verify             # import réel et réimport dans une collection temporaire
```

- [Conception](docs/conception.md) : ce que le deck optimise, les formes de cartes, les principes de rédaction.
- [Méthode](docs/methode.md) : comment relire et corriger le deck sans tourner en rond.
- [Maintenance](docs/maintenance.md) : données, dessins, contrôles, procédure, mises à jour.
- [Sources](docs/sources.md) : références primaires et veille ; consultations datées dans
  [`data/_meta/source_checks.yaml`](data/_meta/source_checks.yaml).

Les rapports [d’import](out/VERIFICATION.md) et [de rendu](out/RENDU.md) identifient le paquet contrôlé par son
empreinte SHA-256.

## Licences

Textes, code et schémas originaux : CC BY-SA 4.0. Médias Wikimedia Commons : licence propre à chaque fichier,
auteurs et liens dans [ATTRIBUTIONS](out/ATTRIBUTIONS.md). Ce deck n’est pas une publication officielle.
