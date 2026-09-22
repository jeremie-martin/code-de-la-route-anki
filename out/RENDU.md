# Vérification du rendu navigateur

Paquet complet SHA-256 : `e221da753fad01373adadeb24f3faa0b56f8d3d407f46e109e1f82278fd29263`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 390 × 844 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2262 |
| 430 × 932 | sombre | 2262 |
| 390 × 844 | sombre | 2262 |
| 320 × 640 | sombre | 2262 |
| 960 × 900 | clair | 56 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu, recto déplacé/modifié au verso ou repère ouvert par défaut.

4552 comparaisons recto/verso : géométrie des images, textes et typographie des prompts (le texte cloze se révèle en place et peut naturellement changer de longueur).

593 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

140 ouvertures et fermetures du volet testées sur l’échantillon.

562 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
