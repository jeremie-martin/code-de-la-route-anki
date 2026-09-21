# Code de la route 2026 — deck Anki

Génère `out/Code-de-la-route-2026.apkg`, un deck Anki pour réussir l’ETG (code de la route, permis B) telle
qu’elle existe en 2026. Lire `README.md`, `docs/conception.md` (ce qu’on optimise, principes de rédaction) et
`docs/maintenance.md` (structure des données, procédure) avant de modifier quoi que ce soit.

## Commandes

```bash
source .venv/bin/activate              # uv venv .venv && uv pip install -r requirements.txt
python -m build.build --check          # erreurs de structure (bloquantes) + avertissements éditoriaux (à juger)
python -m build.build                  # médias (téléchargement Commons au premier build), paquet, rapports out/
python -m build.verify                 # import réel + réimport dans une collection temporaire
python -m unittest discover -s tests
python -m build.preview --ids id1,id2 [--night] [--out dossier]   # captures de cartes (Chrome headless)
python -m build.render_check           # toutes les faces, quatre tailles d'écran (~10 min, lancer en arrière-plan)
python build/import_signs.py           # régénère data/reconnaissance/* (sauf voyants.yaml) depuis l'inventaire + overrides
python build/yamlfix.py data/*/*.yaml  # quote les valeurs YAML contenant ': '
```

## Ce qui n’est pas évident dans le code

- `data/reconnaissance/*.yaml` sont **générés** : corriger `data/_meta/sign_overrides.yaml` (clé = id, `null`
  retire un champ) ou `data/signs_inventory.yaml`, puis régénérer. `voyants.yaml` est écrit à la main.
  Exclure un signal = l’ajouter à `data/_meta/sign_exclusions.yaml` (`codes` de l’inventaire, `raison`,
  `couverts_par`). Formats des notes et sous-thèmes : `docs/maintenance.md`.
- Chaque note doit figurer dans `data/_meta/objectives.yaml` (`notes` = socle, `consolidation` = suite) ;
  retirer une note = la retirer aussi de tous les registres (le build le signale).
- Les scénarios d’intersection déclarent `check` ; `build/priority.py` (modèle documenté en tête du fichier)
  doit être d’accord.
- Toute valeur juridique se vérifie dans `docs/research/sources/cdr.txt` (Code consolidé au 10 septembre 2026,
  `grep -n "R. 415-5"`), puis la consultation se note dans `data/_meta/source_checks.yaml`.
- Les limites de longueur, la balance vrai/faux et les tournures qui trahissent un verdict sont des
  **avertissements** : on juge la carte, on ne la tord pas pour faire taire le compteur. `long_ok` /
  `multi_ok` / `dedup_ok` marquent une exception assumée.
- Les images générées sont invalidées automatiquement quand `diagrams.py` ou `gen_images.py` change.
- Pas de migration entre éditions : les GUID dérivent des ids, ce qui suffit au réimport d’une même édition.
- Pas d’agents en cascade : au plus deux sous-agents à la fois, sur Opus, avec « ne pas lancer de sous-agents ».
