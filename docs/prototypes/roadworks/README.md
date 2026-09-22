# Prototype visuel : approche d’un chantier

Essai du 22 septembre 2026, réalisé avec l’outil intégré imagegen. Ouvrir [la carte](preview.html)
pour alterner recto/verso et clair/sombre. [Image retenue pour l’essai](scene.png), [recto](front.png),
[verso](back.png), [champs proposés](note.json). Aucun changement dans les données ou le paquet publié.

Le rappel testé est l’anticipation dès l’annonce des travaux. La reconnaissance du panneau existe déjà
sur la carte `ak5`. Le texte proposé s’appuie sur le [dépliant Sécurité routière](https://www.securite-routiere.gouv.fr/sites/default/files/2019-01/198x210-chantier_cle181d87.pdf),
qui demande de réduire sa vitesse pour anticiper et de ne pas attendre le dernier moment.
Ce document ancien étaye ce conseil, sans constituer une revalidation juridique pour 2026.

## Résultat

Le panneau reste identifiable dans la carte à 320 et 390 px. L’image occupe environ 233 px de haut
à 390 px de large. Les huit combinaisons largeur/face/thème ont été ouvertes dans Chromium : pas de
débordement horizontal ni d’image manquante. Inspection visuelle du verso à 390 px.

Le balisage ne dessine toujours pas un rétrécissement assez clair : les cônes forment des rangées ambiguës,
avec un chantier surtout sur l’accotement. Des dégradés subsistent malgré la demande d’aplats. Le pictogramme
est reconnaissable, mais ce dessin généré ne remplace pas un modèle réglementaire exact.
Le prototype convient pour discuter du style et de l’anticipation ; il n’est pas retenu pour le deck en l’état.
Pour poursuivre, corriger précisément la géométrie et le panneau avant intégration, puis comparer la carte
à sa version texte. Aucune efficacité pédagogique n’a été mesurée.

## Génération

Deux appels à l’outil intégré : une création, puis une retouche. La première version avait un ciel sombre,
un tableau de bord superflu et des cônes alignés sur le bord de route. Elle a été écartée.
Le prompt de création demandait une illustration plane, une route française à double sens, un panneau AK5
à droite avant un rétrécissement balisé, sans texte, flèches, valeurs de vitesse, véhicules ou décor superflu.

Prompt final de retouche, appliqué à cette première image :

> Revise this educational French roadworks illustration into a much cleaner flat vector-like diagram. Preserve the two-way road, right-hand driving view, the recognisable red/yellow roadworks sign on the right roadside BEFORE the cones, and the white centre dashes. Make these specific corrections: (1) Replace the entire black/green gradient sky with a uniform pale cream #f4f1e8 background. Remove all gradients, shadows, asphalt texture and grass tufts throughout: solid flat colour shapes only. (2) Remove the dashboard, steering wheel and all vehicle interior at the bottom; let the clear road continue to the bottom edge. (3) Make the cone arrangement an unmistakable progressive RIGHT-lane narrowing: the closest cone in the taper is at the right road edge, the subsequent cones farther away move progressively INWARD across the right portion of that lane, then a line of cones continues parallel to the road. Leave sufficient passable lane width entirely to the RIGHT of the dashed centre line. Put the work patch behind the cone boundary on the right, so that cones protect it. Do not put cones on or left of the centre line. The cones must visibly bend inward relative to the right road edge, not just follow it. Keep a clear gap of empty road between the advance warning sign and the beginning of the taper. (4) Use compact landscape framing with less empty sky. Keep the large legible sign and use crisp flat colours, muted sage verge, charcoal road, orange/white cones. No text, no arrows, no numeric signs, no people or vehicles. The illustration should remain clear at 340 pixels wide.
