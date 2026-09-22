# Vérification du rendu navigateur

Paquet complet SHA-256 : `d8f241b09b4d9af194d0703da0a3b2c11200b993c1bf478d9d8ba9fa22c0dc8b`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 390 × 844 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2250 |
| 430 × 932 | sombre | 2250 |
| 390 × 844 | sombre | 2250 |
| 320 × 640 | sombre | 2250 |
| 960 × 900 | clair | 42 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu, recto déplacé/modifié au verso ou repère ouvert par défaut.

4521 comparaisons recto/verso : géométrie des images, textes et typographie des prompts (le texte cloze se révèle en place et peut naturellement changer de longueur).

532 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

105 ouvertures et fermetures du volet testées sur l’échantillon.

422 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
