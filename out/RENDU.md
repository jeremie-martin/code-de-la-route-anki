# Vérification du rendu navigateur

Paquet complet SHA-256 : `ac8f412f9a0c4cc2598cc7b64851f2b820b897c3a9857325d0d3cf714ab99332`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 430 × 740 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2246 |
| 430 × 932 | sombre | 2246 |
| 430 × 740 | sombre | 2246 |
| 320 × 640 | sombre | 2246 |
| 960 × 900 | clair | 218 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu ou repère ouvert par défaut.

287 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

545 ouvertures et fermetures du volet testées sur l’échantillon.

2182 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
