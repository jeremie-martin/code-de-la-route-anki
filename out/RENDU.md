# Vérification du rendu navigateur

Paquet complet SHA-256 : `2031046307645475a2180c37209ef532c91bda97b8ba924b3fc43bb7af61284e`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 430 × 740 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2234 |
| 430 × 932 | sombre | 2234 |
| 430 × 740 | sombre | 2234 |
| 320 × 640 | sombre | 2234 |
| 960 × 900 | clair | 118 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu ou repère ouvert par défaut.

375 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

295 ouvertures et fermetures du volet testées sur l’échantillon.

1181 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle est décrite dans docs/11-interface-quotidienne.md. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
