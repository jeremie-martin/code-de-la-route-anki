# Code de la route 2026 — apprendre les règles, puis les appliquer

Un deck Anki en français pour préparer l’ETG du permis B. L’objectif est de **reconnaître un indice,
retrouver la règle et prendre une décision justifiée**, pas de réciter un catalogue de panneaux.

**Utiliser [le paquet complet](out/Code-de-la-route-2026.apkg)** : **1 393 cartes / 1 240 notes**,
reliées à **51 objectifs pédagogiques**. Le parcours introduit les bases, puis les cas, variantes et
approfondissements. **Aucun plafond de cartes ou de notes** : leur nombre découle des connaissances
et des exercices nécessaires, jamais d’un objectif de brièveté.

Le [paquet Socle](out/Code-de-la-route-2026-Socle.apkg), **651 cartes / 581 notes**, est une extraction
facultative de la première étape. Il n’est ni le deck recommandé à lui seul, ni un seuil de préparation
suffisant. Il partage ses identifiants avec le complet ; inutile d’importer les deux simultanément.
Le mot historique « approfondissement » signifie la suite du parcours, pas du contenu dispensable
ou moins soigneusement conçu. Aucune carte n’est suspendue automatiquement pour sa rareté.

Chaque note figure dans [la couverture de tout le deck](out/COUVERTURE.md) et chaque carte, y compris
chaque cloze sœur, dans [l’inventaire des cibles de rappel](out/ROLES.md). Les choix de représentation
des signaux sont [explicites et motivés](out/SELECTION-SIGNAUX.md). Voir aussi
[le programme](out/PROGRAMME.md), [les repères pour comprendre](out/COMPRENDRE.md) et
[le bilan critique et la refonte v4](docs/09-refonte-pedagogique.md).

## Principes de la version actuelle

- **Une introduction ordonnée, suivie de consolidation.** Les décisions de tous les thèmes arrivent avant les
  variantes de signalisation, détails de procédure, dates et statistiques secondaires. À 20 nouvelles
  cartes par jour, compter au moins 33 jours d’introduction du socle ; apprendre durablement demande
  aussi les révisions. L’enfouissement des cartes sœurs peut allonger ce délai.
- **Des cartes qui demandent la bonne chose.** Le sens d’un panneau suffit, son nom officiel n’est pas
  à réciter. Un vrai/faux demande une justification et la correction de l’énoncé faux. Les détails
  explicatifs du verso ne sont pas des éléments supplémentaires à restituer.
- **Des conditions qui changent la réponse.** Applications ciblées : autoroute à 110 sous la
  pluie ou en probatoire, brouillard en zone 30, distances calculées, angle masqué, remorque, aides à
  la conduite, contrôle technique. Plusieurs scénarios demandent maintenant de lire le marquage
  dessiné au lieu de le révéler dans le texte.
- **Des corrections de fond.** Insertion sans créneau, portée d’un feu vert, placement en giratoire,
  contrôle de l’angle mort du bon côté, pression constructeur, limites des voyants, premiers secours
  selon le référentiel PSC de juillet 2026. [Corrections initiales](docs/research/revision-v3.md) et [compléments](docs/research/revision-v3_1.md).
- **Comprendre avant de mémoriser.** Onze repères de thème, avec exemples expliqués, sont lisibles
  dans le guide et au verso des cartes, dans un volet fermé par défaut. Ils ne sont pas à réciter.
- **Des rappels indépendants.** Les notes à plusieurs seuils peuvent produire des rectos séparés :
  la réponse d’une carte sœur n’apparaît plus à côté du trou. Les calculs élémentaires déductibles,
  statistiques périssables et valeurs constructeur présentées à tort comme universelles ont été repris.
- **Des applications visuelles contrastées.** Lire un tableau de pression, distinguer un voyant au
  contact et en roulant, changer de véhicule sous le même signal. Les douze familles et les décisions de
  retrait motivées sont détaillées dans [CONCEPTION](out/CONCEPTION.md).
- **Un départ neuf.** Cette refonte ne conserve pas artificiellement les anciens numéros de cloze.
  Importer la v4 dans une collection neuve ; les réimports et le passage Socle → complet de cette
  version sont testés avec Anki.

## Apprendre avec le deck

1. **Importer le paquet complet** dans une version récente d’Anki et cocher « Importer les préréglages de deck ».
   Le préréglage propose 20 nouvelles cartes/jour, collecte par position croissante, tri par ordre de
   collecte et enfouissement des cartes sœurs. Étudier le **deck parent** « Code de la route 2026 ».
   Activer FSRS dans les options si souhaité : ce réglage global n’est pas activé par le paquet.
2. **Lire [le repère du thème](out/COMPRENDRE.md) avant ses premières cartes.** Revenir à l’exemple
   si une règle reste abstraite ; le volet « Comprendre ce thème » est aussi disponible hors ligne au verso.
3. **Commencer aussi les photos et vidéos dès la première semaine.** D’abord de petites séries
   thématiques corrigées, même avant de connaître tout le socle. Elles révèlent les erreurs de
   perception qu’une carte textuelle ne mesure pas. Puis faire des examens blancs complets.
4. **Répondre avant de retourner.** Dire le sens, la décision ou la valeur demandée. Pour une
   décision, donner l’indice décisif ou la règle. Réponse devinée, justification absente ou règle
   erronée : « À revoir ». Réponse correcte avec effort : « Difficile » ; correcte sans difficulté :
   « Bon ». Ne pas utiliser « Difficile » pour masquer un oubli.
5. **Adapter le débit à la charge réelle.** Faire les révisions dues ; diminuer les nouvelles cartes
   si les révisions s’accumulent ou si les erreurs augmentent. Vingt est un point de départ, pas une
   prescription. Le deck ne promet pas un temps quotidien fixe.
6. **Utiliser les erreurs pour choisir la suite.** Noter si l’erreur vient d’une règle oubliée, d’un
   indice non vu, de la lecture de l’énoncé ou de la précipitation. Retrouver l’objectif dans
   [COUVERTURE](out/COUVERTURE.md). Réviser la règle existante avant de créer un doublon.
   Le [carnet d’erreurs](docs/07-entrainement.md) donne une méthode et un modèle.
7. **Poursuivre la consolidation.** Les variantes, les panneaux et les cas particuliers font partie
   du travail prévu. Les erreurs en séries servent à anticiper un thème ou à reprendre une règle,
   sans attendre d’échouer pour apprendre une connaissance déjà identifiée. Un rythme soutenable
   règle le débit quotidien, pas le périmètre du contenu. Les tags historiques `importance::*`
   ne déterminent ni les exclusions ni un plafond de contenu.

L’ETG exige 35 réponses correctes sur 40. Comme repère personnel, viser des résultats réguliers de
37–38 sur des séries **nouvelles**, avec photos et vidéos, sans aide et au rythme de l’épreuve.
C’est une marge de préparation, ni un seuil officiel supplémentaire ni une garantie. Un bon taux de
réussite dans Anki ne mesure pas à lui seul l’aptitude à l’examen.
[Conditions officielles de l’ETG](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694).

## Import neuf et versions précédentes

La **v4 est conçue pour un import neuf**, conformément au fait que le deck n’avait pas encore été étudié.
Des notes ont été retirées et certains rappels réorganisés : importer sur une ancienne version ne
supprime pas les anciennes cartes et peut réaffecter le sens d’un numéro de cloze. Utiliser un nouveau
profil Anki pour garder une éventuelle ancienne collection à part. Aucune migration v2/v3 → v4 avec
conservation de l’historique n’est promise. Le passage du Socle v4 au complet v4 et les réimports v4
conservent l’historique dans les tests. Le programme publié décrit l’ordre d’un import neuf.

## Contenu et entretien

Six types : reconnaissance visuelle, comparaison de signaux, fait à trous, question de décision,
affirmation justifiée et scénario dessiné. Les sous-decks suivent les thèmes ; les nouvelles cartes
sont entrelacées entre thèmes. Les [statistiques](out/STATS.md) sont générées à chaque build.
Les schémas sont simplifiés : aucune photo n’est inventée ni présentée comme une question officielle.

Chaque note porte une source. Les sources historiques sont parfois seulement des références de
manuel ou d’article ; **leur présence ne prouve pas une vérification récente de toute la phrase**.
Le registre de vérification distingue les corrections vérifiées des éléments hérités, et retire les affirmations de
certification exhaustive. Les textes applicables, les préconisations du véhicule et les consignes
locales priment sur les approximations pédagogiques. Voir [sources](docs/04-sources.md).

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
python -m build.build --check
python -m unittest discover -s tests -v
python -m build.build                 # produit Socle + complet et les rapports
python -m build.verify                # importe et vérifie les deux paquets
python -m build.preview --ids ab4,c-arret-somme,scn-dep-mixte-mon-cote --width 390
```

Le premier build nécessite un accès réseau pour les médias Commons ; les suivants utilisent le cache.
Les aperçus nécessitent Chrome/Chromium. Les sources YAML sont dans `data/`, les 51 objectifs dans
`data/_meta/objectives.yaml`. Le build refuse une note sans objectif, les références absentes et les médias manquants ;
il ne refuse jamais un ajout à cause du nombre de cartes. Le générateur de signalisation n’exclut
plus une catégorie parce qu’elle est marquée « rare ». À partir de cette v4, préserver les modèles, GUID, numéros de cloze et identifiants de champs/gabarits
ou traiter explicitement leur migration. [Conception](docs/03-conception-des-cartes.md), [vérification des paquets](out/VERIFICATION.md).

## Licences

Textes, code et schémas originaux : CC BY-SA 4.0. Images Commons : licence propre à chaque fichier,
avec auteurs et liens dans [ATTRIBUTIONS](out/ATTRIBUTIONS.md). Les représentations Commons de
signalisation ne sont pas une certification officielle du deck.
