# Approche d’un chantier : prototype SVG

[Ouvrir la carte](preview.html) pour alterner recto/verso et clair/sombre.
[Source SVG éditable](scene.svg), [PNG utilisé dans la carte](scene.png),
[recto](front.png), [verso](back.png), [champs proposés](note.json).
Comparer avec [l’essai par génération d’image](../roadworks/preview.html).
Prototype historique, désormais intégré à `r-chantier-approche`. La version de production est générée
par `chantier_approche` dans [gen_images.py](../../../build/gen_images.py), avec la palette, la voiture
et le cône partagés du deck. Les fichiers de ce dossier conservent l’essai approuvé.

## Choix du dessin

Vue schématique en plan, voiture bleue orientée vers le haut. Le panneau précède le début du balisage.
Une seule rangée de cônes forme le biseau, puis longe les travaux. Le passage restant est entièrement
à droite de l’axe médian. Les aplats et les symboles restent lisibles à petite taille.
Le panneau est représenté de face pour être reconnu dans cette vue en plan ; tailles et distances ne
sont pas à l’échelle. Ce n’est pas un plan réglementaire d’implantation de chantier.
La question teste l’anticipation, pas le calcul d’une distance ni la perception d’une scène photographique.

Dessin réalisé directement en SVG le 22 septembre 2026, sans génération d’image. Le PNG est une
rastérisation du SVG par CairoSVG à 1 280 px. Pour le reconstruire depuis la racine du dépôt :

```bash
.venv/bin/python -m cairosvg docs/prototypes/roadworks-svg/scene.svg -o docs/prototypes/roadworks-svg/scene.png -s 2
```

Le panneau AK5 reprend les tracés de [France road sign AK5.svg](https://commons.wikimedia.org/wiki/File:France_road_sign_AK5.svg),
par Roulex 45, sous [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
Il a été intégré au SVG et redimensionné. Composition du schéma : CC BY-SA 4.0.
La source du conseil de conduite figure dans le verso et dans le prototype précédent.

## Vérification

Le recto et le verso ont été ouverts dans Chromium à 320 et 390 px, en clair et sombre : huit
combinaisons sans débordement horizontal ni image manquante. Inspection visuelle du verso à 390 px.
Le schéma occupe environ 241 px de haut dans cette carte à 390 px de large. Aucun essai natif mobile
ni mesure d’efficacité pédagogique. La géométrie du biseau est contrôlée directement dans le SVG ;
son implantation n’a pas fait l’objet d’une validation de signalisation de chantier.

## Candidats voisins

| Carte | Décision |
|---|---|
| `r-chantier-fleche-lumineuse` | Prochain candidat : lire une flèche et choisir le côté du rabattement. Vérifier la représentation exacte du dispositif avant de dessiner ; pas encore modifié. |
| `kd10` | Déjà illustrée : la fermeture de voie est lisible sur le panneau. Pas de scène supplémentaire pour le même rappel. |
| `aff-r-chantier-sans-ouvriers` | Garder le texte : l’absence d’ouvriers ne rend pas caduque la limitation temporaire. Une image n’ajoute pas de distinction utile. |
