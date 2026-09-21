# Révision du parcours complet — 21 septembre 2026

Document historique de la révision précédente. La version actuelle est décrite dans
[la refonte pédagogique v4](09-refonte-pedagogique.md).


## Décision

Le commit `316dffb` conserve la première révision. Cette suite corrige son erreur de conception :
un plafond de 600 cartes, même nommé « budget éditorial », ne permet pas de déduire ce qu’il faut
apprendre. Il est supprimé du code, des tests et des instructions de maintenance. Aucun plafond ne
s’applique aux notes, cartes, objectifs ou familles de panneaux.

Le **paquet complet est le parcours recommandé**. Le socle est une première étape de prérequis,
exportée séparément par commodité. L’approfondissement fait partie de l’apprentissage prévu ;
ce n’est ni un stock non relu ni une série réservée aux seules erreurs déjà commises en examen blanc.
Un rythme de nouvelles cartes est un réglage quotidien adaptable, pas une réduction du programme.

## Intégration de toutes les notes

Les 51 objectifs du manifeste nomment maintenant toutes les notes. Les listes `notes` et
`consolidation` précisent leur étape. Le build échoue si une note est sans objectif, si une référence
est inconnue ou si une exclusion renvoie à une couverture absente. Les comparaisons conservent
leurs prérequis visuels et les clozes leur espacement. Aucune carte n’est supprimée ou suspendue
parce qu’une quantité souhaitée serait dépassée.

`out/COUVERTURE.md` expose l’intention de chaque objectif et ses notes. `out/ROLES.md` expose
chaque carte dans l’ordre livré : identifiant, objectif, travail demandé et cible de rappel. Cela rend
notamment inspectables les différentes clozes d’une même note. Un lien d’objectif ne prouve pas
qu’une carte est bonne : il rend sa place explicite et permet de contester son apport.

Les prérequis manquants de l’introduction ont été ajoutés à celle-ci : vocabulaire routier, indications
de direction, affectation des voies, balises, distinctions de feux et de panneaux, message d’alerte.
L’introduction dépasse désormais l’ancien plafond sans être rejetée. Le nombre obtenu n’est pas une
nouvelle cible.

## Signalisation : une sélection motivée

Le générateur excluait automatiquement certaines catégories marquées « rare ». Ce filtre disparaît.
Trente-deux cartes visuelles complètent notamment les directions, sorties de zones et services.
Les versos des nouvelles sorties de zones donnent leur sens, sans demander de connaître un code B6b.

Les entrées sans carte visuelle distincte sont nommées dans `data/_meta/sign_exclusions.yaml` avec
raison et cartes correspondantes, et publiées dans `out/SELECTION-SIGNAUX.md`. Exemples :
une enseigne commerciale ne change pas le service ; une autre référence administrative d’un feu
rouge déjà représenté ne justifie pas une deuxième carte identique ; un signal absent de France
ne doit pas être inventé en image. Un média manquant pour un signal retenu fait échouer la génération.

Dix-sept questions ajoutent des décisions distinctes : destinataire d’un feu, accès régulé, décompteur
piéton, panneau lumineux prescriptif, guidage, voie pour véhicules lents, itinéraire et localisation,
ou encore les deux cas contrastés du B26. Les exemples textuels ne constituent pas une vérification
de reconnaissance visuelle de toutes ces variantes : celle-ci reste aussi à travailler sur des scènes.

## Qualité appliquée au-delà de l’introduction

La relecture a corrigé des contradictions entre reconnaissance et comparaison : C20c est un tramway,
B13 porte sur les masses autorisées, B31 concerne les véhicules en mouvement, C107 ne fixe pas
une vitesse unique, un vert directionnel ne dispense pas de toutes les autres priorités. Le B26 a
été repris à partir de la modification de 2021 de l’IISR : équivalence des pneus hiver pour une
voiture, sauf complément imposant les chaînes. Références et périmètres : `source_checks.yaml`.

Des recettes numériques trop générales deviennent des rappels utiles ou des applications à données
explicites : surconsommation, choix des rapports, durée d’entretien, adhérence sur neige, champ visuel,
alcoolémie par verre et force d’un choc. Les nombres utiles ne sont pas bannis : seuil légal, calcul
explicite et ordre de grandeur daté ont des fonctions différentes. La pression en charge, les câbles
de démarrage, les alertes de freinage et la pente verglacée sont aussi contextualisés.

La vérification visuelle des nouveaux médias a aussi remplacé deux images de direction qui ne
correspondaient pas à leur fiche, et retiré une légende de damier qui donnait la réponse au recto.
Le schéma d’affectation des voies est identifié comme un dessin pédagogique simplifié.

Le [journal par note](research/revision-v3_1.md) détaille les corrections et les ajouts. Aucun identifiant
existant n’est supprimé. Une cible corrigée peut toutefois demander un réapprentissage malgré la
conservation technique de son historique.

## Critère de qualité durable

Pour chaque ajout ou révision, examiner le recto et les cartes effectivement produites :

- Quel savoir ou quelle décision manque, et à quel objectif se rattache-t-il ?
- Les conditions données permettent-elles une réponse déterminée et sourcée ?
- Le travail demandé est-il adapté : reconnaître, distinguer, rappeler ou appliquer ?
- Une autre carte fait-elle déjà le même travail ? Si oui, quelle différence justifie les deux ?
- Quels prérequis, variantes et contre-exemples assurent son intégration ?
- Chaque cloze teste-t-elle une information utile, sans réponse offerte par une autre partie du recto ?

Ces questions s’appliquent aux deux étapes. Elles ne se remplacent ni par un quota, ni par une
limite de mots, ni par un tag « relu ». Les validations techniques et l’inventaire ne constituent
pas une nouvelle certification juridique phrase par phrase de tout le dépôt, ni une preuve
expérimentale d’optimalité. Le contrôle éditorial reste nécessaire à chaque changement ; les erreurs
sur scènes nouvelles servent à vérifier le transfert, sans attendre ces erreurs pour couvrir les bases.
