# Vérification du rendu navigateur

Paquet complet SHA-256 : `0b61659e187bd6fc3ecdb7a2bc40fdd756d9661a93009c5ef476c1d04770615c`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 430 × 740 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2256 |
| 430 × 932 | sombre | 2256 |
| 430 × 740 | sombre | 2256 |
| 320 × 640 | sombre | 2256 |
| 960 × 900 | clair | 130 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu ou repère ouvert par défaut.

287 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

325 ouvertures et fermetures du volet testées sur l’échantillon.

1301 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
