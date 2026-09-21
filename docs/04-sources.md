# Sources et vérification

Toutes les cartes portent un champ `Source`. Les dossiers de recherche complets, avec les URL et la
date de consultation (20-21 septembre 2026), sont dans `docs/research/` :

| Dossier | Contenu | Taille |
|---|---|---|
| `research/exam.md` | L'épreuve elle-même : textes (arrêté du 20 avril 2012, arrêté du 16 avril 2026), banque 2023, 20 exemples officiels verbatim, formes de questions, statistiques de réussite, pièges, divergences entre sources | ≈ 11 000 mots, 180 URL |
| `research/legal-facts.md` | Toutes les valeurs juridiques (vitesses, alcool, points, amendes, délits, documents, CT, Crit'Air/ZFE, équipements, EDPM, vélos, motos, stationnement, feux, marquages, santé, statistiques ONISR 2025) vérifiées sur Légifrance / service-public / ONISR, avec la chronologie des changements 2018-2026 | ≈ 28 000 mots |
| `research/knowledge-facts.md` | Connaissances non juridiques par thème (conducteur, route, usagers, véhicule, sécurité, environnement, secours, circulation), avec les pièges rapportés par les formateurs et les divergences entre éditeurs | ≈ 35 000 mots, 610 URL |
| `research/signs-notes.md` + `data/signs_inventory.yaml` | Inventaire de 504 éléments de signalisation (IISR via Wikipédia FR), formes/couleurs, implantation, portée, panonceaux, hiérarchie, panneaux récents | — |
| `research/sources/` | PDF officiels archivés : exemples de questions 2023 (Sécurité routière), communiqué DSR du 11/09/2023, Code de la route consolidé (édition codes.droit.org du 10/09/2026, dernière modification 20/08/2026) | — |

## Textes de référence

- **Code de la route** (parties L et R), version consolidée au 10 septembre 2026 : c'est l'autorité
  pour toute valeur juridique. Les articles cités dans les cartes (R413-2, R415-5, R412-19…) ont été
  relus dans cette version. Les changements récents intégrés : loi n° 2025-622 du 9 juillet 2025
  (homicide routier ; alcool/stupéfiants 3 ans / 9 000 € ; grand excès de vitesse = délit dès le
  29 décembre 2025), loi n° 2026-798 du 18 août 2026 (refus de dépistage 3 ans / 9 000 €, ivresse
  manifeste, rodéos), décret n° 2026-652 (véhicules prioritaires), décision CC 2026-903 DC (ZFE
  maintenues), décret n° 2025-33 (inter-files), décret n° 2023-1214 (permis à 17 ans), décret
  n° 2023-1152 (fin de la vignette d'assurance).
- **Instruction interministérielle sur la signalisation routière (IISR)**, parties 1 à 8, pour les
  panneaux, panonceaux, balises, feux et marques sur chaussée (modulations T1/T'1/T2/T3/T4/T'2).
- **Arrêté du 20 avril 2012** modifié (conditions de l'examen : 35/40, validité 5 ans) et **arrêté du
  16 avril 2026** (organisation des épreuves théoriques : inscription J-1, résultats ≥ 24 h).
- **securite-routiere.gouv.fr** (fiches thématiques, dépliants « vitesse », « la vue », « ceinture »,
  exemples officiels de questions), **service-public.fr** (fiches datées « vérifié le »),
  **ONISR** (bilan définitif 2025, publié le 29 mai 2026), **ADEME** (écoconduite), **Croix-Rouge
  française** (gestes de premiers secours), **ANSM** (pictogrammes médicaments).

## Conventions d'examen vs valeurs officielles

Certaines valeurs enseignées par les auto-écoles sont des simplifications : distance d'arrêt
« dizaines au carré » (25 m à 50 km/h) alors que la Sécurité routière donne 28 m ; sol mouillé × 1,5
ou × 2 ; « 30 min » de pic d'alcoolémie alors que la Sécurité routière dit un quart d'heure à jeun. Les
cartes donnent la **convention d'examen** (celle que la banque de questions attend) et signalent la
valeur officielle dans l'explication, pour que le candidat reconnaisse les deux.

Inversement, quand la loi a changé après la rédaction de la banque de questions (septembre 2023),
la carte donne la **valeur en vigueur** et mentionne l'ancienne (ex. « 3 ans / 9 000 € depuis juillet
2025, auparavant 2 ans / 4 500 € — les QCM peuvent encore l'afficher »). Ces cartes portent le tag
`nouveau::2024`, `nouveau::2025` ou `nouveau::2026`.

## Images

- Panneaux, panonceaux, balises : fichiers vectoriels de Wikimedia Commons (`France road sign
  XXX.svg` et catégories associées), dessinés d'après l'IISR ; licence et auteur de chaque fichier
  dans `out/ATTRIBUTIONS.md` (majorité domaine public / CC0 ; quelques CC BY-SA).
- Voyants : symboles **ISO 7000** (domaine public sur Commons), teintés en rouge / orange / vert /
  bleu selon leur fonction réelle et posés sur un fond de tableau de bord.
- Marquages, feux, gestes de l'agent, scénarios : SVG générés par `build/gen_images.py` et
  `build/diagrams.py` (charte unique), à partir des cotes de l'IISR.

## Processus de vérification

1. Quatre dossiers de recherche indépendants (examen, droit, connaissances, signalisation), chacun
   sourcé ligne à ligne, avec listes de divergences.
2. Rédaction des cartes à partir des dossiers, en citant l'article ou la page.
3. Contrôle croisé automatique : le solveur `build/priority.py` recalcule la réponse de chaque
   scénario d'intersection ; le build échoue en cas de désaccord avec la réponse rédigée.
4. Contrôle visuel : planches de contrôle (`build/qa_sheet.py`) de toutes les images avec leur code
   et leur nom ; captures de cartes rendues (`build/preview.py`).
5. Relecture par un agent indépendant de chaque fichier de données contre les dossiers et le code
   consolidé (rapports dans `docs/research/review-*.md`), puis corrections.
6. **Version 2** (21 septembre 2026, `docs/05-audit-v2.md`) : réécriture thème par thème selon
   `docs/research/brief-v2-redaction.md` (rapports `docs/research/v2-*.md`, avec pour chaque carte
   supprimée la carte qui porte désormais la connaissance), puis seconde relecture contradictoire
   indépendante de chaque thème contre le Code consolidé (`docs/research/review-v2-*.md`, corrections
   appliquées, doutes listés), contrôle des doublons entre fichiers (`python -m build.dedup`) et
   règles de qualité vérifiées par le build (longueurs, équilibre vrai/faux, clozes qui se soufflent
   la réponse, réponses identiques).

## Ce qu'il faudra surveiller (obsolescence)

- Tolérance loi Montagne (aucune sanction codifiée au 20/09/2026).
- Seuil de puissance des véhicules interdits à la location en probatoire (loi 2026-798, décret à
  paraître).
- Fin de l'exception des places matérialisées dans les 5 m avant un passage piéton (1er janvier 2027).
- Directive (UE) 2025/2205 (nouveaux contenus d'épreuve, applicable en novembre 2029).
- Éventuelle nouvelle banque de questions ETG (aucune annoncée au 20/09/2026).
