# Vérification du rendu navigateur

Paquet complet SHA-256 : `902531e968d2de95f2b7340bf01f97b9e3622ff5228b5a47a74d21fab70abea1`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 390 px en clair et 320 px en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 390 × 844 | clair | 2742 |
| 320 × 640 | sombre | 2742 |
| 960 × 900 | clair | 38 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu ou repère ouvert par défaut.

1287 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Les captures sont en pleine hauteur.

114 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle manuelle est décrite dans le bilan v5. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
