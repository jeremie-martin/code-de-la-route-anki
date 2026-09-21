# Code de la route 2026 — deck Anki pour *réussir* l'ETG

Un deck Anki conçu carte par carte pour passer l'épreuve théorique générale (permis B) telle qu'elle
existe en 2026 : 40 questions sur photos/vidéos, 35 bonnes réponses exigées, banque de questions de
septembre 2023, 10 thèmes officiels.

Le fichier à importer : **`out/Code-de-la-route-2026.apkg`** (généré par `build/`).

Contenu (build du 21 septembre 2026, détail dans `out/STATS.md`) : **896 notes / 1 095 cartes** —
425 reconnaissances (panneaux, panonceaux, balises, marquages, feux, gestes de l'agent, voyants),
49 paires de confusion, 127 faits à trous, 247 questions, 48 scénarios dessinés. Chaque note a été
relue deux fois (rédaction puis audit contradictoire contre le Code de la route consolidé au
10 septembre 2026 ; rapports dans `docs/research/review-*.md`).

## Ce qui rend ce deck différent

- **Conçu pour l'épreuve, pas pour réciter la loi.** Chaque carte répond à une question que l'examen
  pose réellement : reconnaître (panneau, marquage, feu, voyant), rappeler (le chiffre, la règle),
  décider (« dans cette situation, je… »). Voir `docs/01-analyse-examen.md`.
- **Une carte = une connaissance.** Pas de listes à réciter, pas de cartes inversées gratuites, pas de
  notes qui explosent en dix cartes. Voir `docs/03-conception-des-cartes.md`.
- **Des images correctes et nettes.** Panneaux vectoriels officiels (Wikimedia Commons, conformes à
  l'IISR), voyants ISO 7000, schémas d'intersections et de marquages générés avec une charte unique.
- **Des scénarios vérifiés par un solveur.** Chaque schéma de priorité a une réponse écrite à la main
  *et* recalculée par `build/priority.py` ; le build échoue en cas de désaccord.
- **À jour (septembre 2026)** : permis à 17 ans, mémo véhicule assuré, pneus hiver, EDPM, ZFE/Crit'Air,
  arrêté du 16 avril 2026 sur l'organisation de l'épreuve… chaque note cite sa source.
- **Mise à jour sans perte** : identifiants de notes et de types stables, on peut réimporter une
  nouvelle version sans perdre son historique de révision.

## Organisation

```
Code de la route 2026
├── 00 Méthode d'examen
├── 01 Signalisation            (panneaux, panonceaux, balises, marquages, feux, agents)
├── 02 Circulation              (priorités, vitesses, positionnement, dépassement, arrêt/stationnement)
├── 03 Le conducteur
├── 04 La route
├── 05 Les autres usagers
├── 06 Réglementation et notions diverses
├── 07 Premiers secours
├── 08 Prendre et quitter son véhicule
├── 09 Mécanique et équipements
├── 10 Sécurité du passager et du véhicule
└── 11 Environnement
```

Les sous-decks 03 à 11 correspondent aux thèmes officiels de l'épreuve, dans l'ordre où les sites
d'entraînement rendent leurs résultats : si vous échouez sur « Le conducteur », travaillez le sous-deck 03.

Tags : `theme::C`, `sous::vitesse`, `type::panneau`, `importance::essentiel|utile|rare`.
Pressé ? Suspendez `tag:importance::rare` (Parcourir → recherche → sélectionner tout → Suspendre).

## Comment l'utiliser

1. **Réglages** : 20 nouvelles cartes/jour, FSRS activé (Options du deck → Planification), « rétention
   souhaitée » 0,9. À ce rythme, le deck complet est vu en ~7 semaines ; les révisions ensuite prennent
   10-15 min/jour.
2. **Ordre** : commencez par `00 Méthode` et `01 Signalisation`, puis le reste dans l'ordre. Les
   scénarios de priorité (dans `02`) sont plus faciles une fois les panneaux connus.
3. **En parallèle, à partir de la 3e semaine** : des séries d'examens blancs (40 questions, photos
   réelles) sur un site d'entraînement. Le deck apporte les connaissances et les réflexes ; les séries
   apportent la lecture de photos et le rythme des 20 secondes. Notez vos thèmes faibles et augmentez le
   nombre de nouvelles cartes du sous-deck correspondant.
4. **Avant l'examen** : révisez `00 Méthode` et le tag `sous::priorites`.

## Reconstruire ou modifier le deck

```bash
uv venv .venv && source .venv/bin/activate
uv pip install anki pyyaml cairosvg pillow requests lxml
python -m build.build --check     # valide les données (YAML dans data/)
python -m build.build             # génère les images (téléchargement Commons au 1er build) et l'apkg
python -m build.preview --n 12    # capture d'écran de cartes au hasard (Chrome headless)
```

Les connaissances vivent dans `data/` (YAML, un fichier par thème et par type de note) ; le code de
génération dans `build/`. `docs/` explique l'analyse de l'épreuve, la carte des connaissances, la
conception des cartes et les sources.

## Licences

- Contenu (textes, schémas générés, code) : CC BY-SA 4.0.
- Panneaux : fichiers Wikimedia Commons (domaine public / CC0 / CC BY-SA selon le fichier,
  liste dans `out/ATTRIBUTIONS.md`), dessinés d'après l'Instruction interministérielle sur la
  signalisation routière.
- Voyants : symboles ISO 7000 (domaine public sur Commons).
