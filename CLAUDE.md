# Deck Anki du Code de la route 2026

Génère `out/Code-de-la-route-2026.apkg`, un deck Anki pour réussir l’ETG (permis B) telle qu’elle existe en
2026. Avant de modifier quoi que ce soit, lire `docs/conception.md` (ce qu’on optimise), `docs/methode.md`
(comment relire et corriger) et `docs/maintenance.md` (données, dessins, contrôles, procédure).

## Commandes

```bash
source .venv/bin/activate              # uv venv .venv && uv pip install -r requirements.txt (+ requirements-qa.txt)
python -m build.build --check          # erreurs de structure (bloquantes) + avertissements éditoriaux (à juger)
python -m build.build                  # médias, paquet, rapports out/
python -m build.verify [--previous ancien.apkg]   # import réel + réimport ; mise à jour d'un paquet déjà importé
python -m unittest discover -s tests
python -m build.preview --ids id1,id2 [--night] [--out dossier]   # captures de cartes
python -m build.render_all dossier     # toutes les cartes dans l'ordre d'étude + dump.md (relectures)
python -m build.render_check           # toutes les faces, tailles de téléphone (~10 min, en arrière-plan)
python build/import_signs.py           # régénère data/reconnaissance/* (sauf voyants.yaml)
```

## Ce qui n’est pas évident

- Un problème signalé est l’exemple d’une classe : la chercher dans tout le deck et corriger partout de la même
  façon, avec preuve, puis faire relire les modifications (`docs/methode.md`).
- L’utilisateur a importé le deck (paquet du commit 1e32131, voir la fin de `docs/maintenance.md`) : garder les
  `id` (GUID) et `build/schema_ids.json` ; reformuler plutôt que supprimer ; `build.verify --previous` sur ce
  paquet nomme les notes retirées, à lui signaler.
- `data/reconnaissance/*.yaml` sont **générés** : corriger `data/_meta/sign_overrides.yaml` (clé = id, `null`
  retire un champ) et garder `data/signs_inventory.yaml` cohérent, puis régénérer. `voyants.yaml` est écrit à la main.
- Chaque note figure dans `data/_meta/objectives.yaml` (`notes` = socle, `consolidation` = suite) ; les
  scénarios d’intersection déclarent `check` quand le solveur couvre la situation, et `build/priority.py`
  (modèle en tête du fichier) doit le confirmer.
- Toute règle se vérifie **avec ses conditions** dans une source primaire actuelle : `docs/research/sources/cdr.txt`
  (Code au 10/09/2026) pour trouver l’article, Légifrance pour la version en vigueur quand il a pu changer ; la
  consultation s’inscrit dans `data/_meta/source_checks.yaml`. Les recherches web ramènent
  des règles étrangères ; securite-routiere.gouv.fr se lit avec `?_format=json`.
- Les images générées sont invalidées automatiquement quand `diagrams.py` ou `gen_images.py` change ; un dessin
  réutilise la palette et les primitives partagées, et se regarde rendu sur téléphone (clair et sombre).
- Sous-agents : peu nombreux (un ou deux, davantage seulement à la demande), sur Opus, consigne autonome et
  « ne pas lancer de sous-agents » ; ils ne modifient rien, les corrections se font dans le fil principal.
