# Vérification du rendu navigateur

Paquet complet SHA-256 : `67698fcc616bd3ef9ee3652d739385425ed2bd8eaa95c37393c5812c5a8ce956`.

Paquet importé dans une collection temporaire ; contenus et gabarits rendus par Anki, puis chargés dans Chromium local sans réseau externe. Toutes les cartes, recto et verso, à 430 × 932 en clair et sombre, à 390 × 844 et 320 × 640 en sombre ; échantillon à 960 px.

| Largeur × hauteur | Mode | Faces contrôlées |
|---|---|---|
| 430 × 932 | clair | 2132 |
| 430 × 932 | sombre | 2132 |
| 390 × 844 | sombre | 2132 |
| 320 × 640 | sombre | 2132 |
| 960 × 900 | clair | 56 |

**0 échec(s)** : débordement horizontal, média absent, rappel mal isolé, gabarit non résolu, recto déplacé/modifié au verso ou repère ouvert par défaut.

4292 comparaisons recto/verso : géométrie des images, textes et typographie des prompts (le texte cloze se révèle en place et peut naturellement changer de longueur).

765 faces/configurations nécessitent un défilement vertical ; ce défilement est admis. Captures en pleine hauteur et captures du seul écran (`_viewport`).

140 ouvertures et fermetures du volet testées sur l’échantillon.

562 captures dans `out/qa/render/`, avec le détail dans `measurements.json`.

Les mesures de mise en page ne vérifient ni la lisibilité du texte incorporé dans une image, ni sa signification. L’inspection visuelle des captures reste nécessaire. Chromium ne remplace pas un essai dans AnkiMobile ou AnkiDroid.
