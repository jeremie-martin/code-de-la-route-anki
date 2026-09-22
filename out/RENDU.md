# Vérification du rendu navigateur

Paquet complet SHA-256 : `62780b7aa7184ce7d17f168e1b16b7cd57e85e3337e23e4398643c4755b4cc36`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 430 × 740 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2250 |
| 430 × 932 | sombre | 2250 |
| 430 × 740 | sombre | 2250 |
| 320 × 640 | sombre | 2250 |
| 960 × 900 | clair | 260 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu ou repère ouvert par défaut.

290 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

650 ouvertures et fermetures du volet testées sur l’échantillon.

2602 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
