# Vérification du rendu navigateur

Paquet complet SHA-256 : `3f736768008574d3d6a177e4e54be98a8e907899703a0bca4c3c030184a90b00`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 430 × 740 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2250 |
| 430 × 932 | sombre | 2250 |
| 430 × 740 | sombre | 2250 |
| 320 × 640 | sombre | 2250 |
| 960 × 900 | clair | 54 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu ou repère ouvert par défaut.

288 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

135 ouvertures et fermetures du volet testées sur l’échantillon.

542 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
