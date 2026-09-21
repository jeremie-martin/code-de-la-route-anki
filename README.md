# Code de la route 2026 — deck Anki pour *réussir* l'ETG

Un deck Anki conçu carte par carte pour passer l'épreuve théorique générale (permis B) telle qu'elle
existe en 2026 : 40 questions sur photos/vidéos, 35 bonnes réponses exigées, banque de questions de
septembre 2023, 10 thèmes officiels.

Le fichier à importer : **`out/Code-de-la-route-2026.apkg`** (généré par `build/`).

Contenu (version 2, build du 21 septembre 2026, détail dans `out/STATS.md`) : **1 160 notes /
1 359 cartes** — 425 reconnaissances (panneaux, panonceaux, balises, marquages, feux, gestes
de l'agent, voyants), 50 paires de confusion, 127 faits à trous (326 cartes),
250 questions de décision, 258 affirmations « vrai ou faux ? », 50 scénarios dessinés.
Chaque note a été rédigée à partir de dossiers sourcés, puis relue par un relecteur indépendant
contre le Code de la route consolidé au 10 septembre 2026 (rapports dans `docs/research/`).

## Ce qui rend ce deck différent

- **Conçu pour l'épreuve, pas pour réciter la loi.** Chaque carte répond à une question que l'examen
  pose réellement : reconnaître (panneau, marquage, feu, voyant), rappeler (le chiffre, la règle),
  décider (« dans cette situation, je… »), juger (« cette affirmation est-elle vraie ? » — la forme la
  plus fréquente de la banque 2023). Voir `docs/01-analyse-examen.md`.
- **Une carte = une connaissance décidable.** Pas de fiches à réciter : le build refuse toute réponse
  de plus de 40 mots ou de plus de 4 éléments, toute affirmation sans justification, tout verso de
  panneau de plus de 90 mots. Voir `docs/03-conception-des-cartes.md` et `docs/05-audit-v2.md`.
- **Un programme d'apprentissage, pas un tas de cartes.** L'ordre des nouvelles cartes est calculé :
  méthode d'examen d'abord, puis les connaissances essentielles de tous les thèmes entrelacées jour
  après jour (chaque journée est une tranche de l'épreuve entière), les scénarios de priorité une fois
  les panneaux connus, les signaux rares en dernier. Voir `out/PROGRAMME.md`.
- **Des images correctes et nettes.** Panneaux vectoriels officiels (Wikimedia Commons, conformes à
  l'IISR), voyants ISO 7000, schémas d'intersections et de marquages générés avec une charte unique.
- **Des scénarios vérifiés par un solveur.** Chaque schéma de priorité a une réponse écrite à la main
  *et* recalculée par `build/priority.py` ; le build échoue en cas de désaccord.
- **À jour (septembre 2026)** : permis à 17 ans, mémo véhicule assuré, pneus hiver 3PMSF, EDPM,
  inter-files 2025, ZFE/Crit'Air, délits 2025-2026 (alcool 3 ans / 9 000 €, grand excès de vitesse),
  arrêté du 16 avril 2026 sur l'organisation de l'épreuve. Chaque note cite sa source.
- **Mise à jour sans perte** : identifiants de notes, de types de notes et de decks stables, on peut
  réimporter une nouvelle version sans perdre son historique de révision.

## Organisation

```
Code de la route 2026
├── 00 Méthode d'examen         (lire une question sans tomber dans les pièges)
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

Six types de cartes : **Reconnaissance** (image → sens, conduite à tenir, piège), **Confusion**
(deux signaux côte à côte : quelle différence ?), **Fait** (phrase à trous pour les chiffres),
**Question** (situation → décision et sa raison), **Affirmation** (contexte + affirmation → VRAI/FAUX et
pourquoi), **Scénario** (schéma vu de dessus → qui passe, puis-je dépasser).

Tags : `theme::C`, `sous::vitesse`, `type::panneau`, `importance::essentiel|utile|rare`,
`nouveau::2025` (règle récente que la banque de 2023 peut encore présenter avec l'ancienne valeur).

## Comment l'utiliser

1. **Importer** : Fichier → Importer → `Code-de-la-route-2026.apkg`, et **cocher « Importer les
   préréglages de deck »** (Import any deck presets). Le deck arrive alors avec ses options : 20
   nouvelles cartes par jour, ordre des nouvelles cartes = programme calculé, cartes sœurs enterrées,
   rétention souhaitée 0,9. Si vous avez oublié la case : Options du deck → Nouvelles cartes → « Ordre
   de collecte : position croissante » et « Ordre de tri : ordre de collecte ». Activez FSRS
   (Options du deck → Planification) : c'est un réglage global d'Anki, il n'est pas dans le paquet.
2. **Étudier le deck parent** (« Code de la route 2026 »), pas les sous-decks un par un : c'est ce qui
   applique le programme. À 20 cartes/jour, l'essentiel (1 032 cartes) est vu en environ
   7 à 8 semaines, le reste (signaux utiles puis rares) dans les 2 semaines
   suivantes ; les révisions prennent ensuite 10 à 20 minutes par jour. Pressé ? Passez à 25-30
   nouvelles cartes par jour, ou suspendez `tag:importance::rare` (Parcourir → recherche →
   sélectionner tout → Suspendre).
3. **En parallèle, à partir de la 3e semaine** : des séries d'examens blancs (40 questions, photos
   réelles, 20 secondes) sur un site d'entraînement. Le deck apporte les connaissances et les réflexes ;
   les séries apportent la lecture de photos et le rythme. Notez vos thèmes faibles et augmentez le
   nombre de nouvelles cartes du sous-deck correspondant.
4. **S'inscrire** quand les séries donnent régulièrement 37-38/40 (le seuil est 35 ; la marge absorbe le
   stress). La Sécurité routière conseille elle-même de repousser de quelques jours si la préparation
   est à parfaire. **Avant l'examen** : revoir `00 Méthode` et le tag `sous::priorites`.

L'épreuve en pratique (ces informations ne sont volontairement pas des cartes) : 40 questions, 35
bonnes réponses, environ 20 secondes par question après la lecture orale, 3 questions d'essai non
notées, 30 €, résultat au plus tôt 24 h après, inscription au plus tard la veille (arrêté du 16 avril
2026), code valable 5 ans, dès 15 ans en conduite accompagnée et 16 ans sinon, dans un centre agréé
(La Poste, SGS, Dekra, Bureau Veritas, Pearson Vue).

## Reconstruire ou modifier le deck

```bash
uv venv .venv && source .venv/bin/activate
uv pip install anki pyyaml cairosvg pillow requests lxml
python -m build.build --check     # valide les données (YAML dans data/) : schéma, longueurs, doublons, solveur
python -m build.build             # génère les images (téléchargement Commons au 1er build) et l'apkg
python -m build.dedup             # liste les connaissances quasi identiques entre fichiers
python -m build.preview --n 12    # capture d'écran de cartes au hasard (Chrome headless)
```

Les connaissances vivent dans `data/` (YAML, un fichier par thème et par type de note) ; le code de
génération dans `build/`. `docs/` explique l'analyse de l'épreuve (01), la carte des connaissances (02),
la conception des cartes (03), les sources (04), l'audit de la première version et les décisions de la
seconde (05) ; `docs/research/brief-v2-redaction.md` est la règle du jeu pour écrire une carte.

## Licences

- Contenu (textes, schémas générés, code) : CC BY-SA 4.0.
- Panneaux : fichiers Wikimedia Commons (domaine public / CC0 / CC BY-SA selon le fichier,
  liste dans `out/ATTRIBUTIONS.md`), dessinés d'après l'Instruction interministérielle sur la
  signalisation routière.
- Voyants : symboles ISO 7000 (domaine public sur Commons).
