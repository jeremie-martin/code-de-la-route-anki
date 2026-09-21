# Code de la route 2026 — apprendre les règles, puis les appliquer

Un deck Anki en français pour préparer l’ETG du permis B. L’objectif est de **reconnaître un indice,
retrouver la règle et prendre une décision justifiée**, pas de réciter un catalogue de panneaux.

**Commencer par [le paquet Socle](out/Code-de-la-route-2026-Socle.apkg)** : **552 cartes / 483 notes**,
organisées autour de **41 objectifs**, couvrant les dix thèmes de l’examen et sa méthode de lecture.
Le [paquet complet](out/Code-de-la-route-2026.apkg) contient **1 378 cartes / 1 179 notes**, dont
exactement ce même socle, suivi de l’approfondissement. Inutile d’importer les deux à la fois.

Le socle est une sélection pédagogique, **pas la promesse que seules ces cartes tomberont à l’examen**.
Le détail de chaque choix est dans [la couverture](out/COUVERTURE.md), la progression dans
[le programme](out/PROGRAMME.md), et le bilan critique dans [l’audit v3](docs/06-audit-v3.md).

## Ce qui change dans la v3

- **Un premier parcours réellement finissable.** Les décisions de tous les thèmes arrivent avant les
  variantes de signalisation, détails de procédure, dates et statistiques secondaires. À 20 nouvelles
  cartes par jour, compter au moins 28 jours d’introduction du socle ; apprendre durablement demande
  aussi les révisions. L’enfouissement des cartes sœurs peut allonger ce délai.
- **Des cartes qui demandent la bonne chose.** Le sens d’un panneau suffit, son nom officiel n’est pas
  à réciter. Un vrai/faux demande une justification et la correction de l’énoncé faux. Les détails
  explicatifs du verso ne sont pas des éléments supplémentaires à restituer.
- **Des conditions qui changent la réponse.** Dix-neuf applications ciblées : autoroute à 110 sous la
  pluie ou en probatoire, brouillard en zone 30, distances calculées, angle masqué, remorque, aides à
  la conduite, contrôle technique. Plusieurs scénarios demandent maintenant de lire le marquage
  dessiné au lieu de le révéler dans le texte.
- **Des corrections de fond.** Insertion sans créneau, portée d’un feu vert, placement en giratoire,
  contrôle de l’angle mort du bon côté, pression constructeur, limites des voyants, premiers secours
  selon le référentiel PSC de juillet 2026. [Changements par note](docs/research/revision-v3.md).
- **Une réimportation testée.** Les identifiants des champs et gabarits sont désormais stables eux
  aussi : la v2 ne stabilisait que les decks, types de notes et GUID. Les tests importent réellement
  les paquets et vérifient les corrections, les médias et la conservation d’un historique de révision.

## Apprendre avec le deck

1. **Importer le Socle** dans une version récente d’Anki et cocher « Importer les préréglages de deck ».
   Le préréglage propose 20 nouvelles cartes/jour, collecte par position croissante, tri par ordre de
   collecte et enfouissement des cartes sœurs. Étudier le **deck parent** « Code de la route 2026 ».
   Activer FSRS dans les options si souhaité : ce réglage global n’est pas activé par le paquet.
2. **Commencer aussi les photos et vidéos dès la première semaine.** D’abord de petites séries
   thématiques corrigées, même avant de connaître tout le socle. Elles révèlent les erreurs de
   perception qu’une carte textuelle ne mesure pas. Puis faire des examens blancs complets.
3. **Répondre avant de retourner.** Dire le sens, la décision ou la valeur demandée. Pour une
   décision, donner l’indice décisif ou la règle. Réponse devinée, justification absente ou règle
   erronée : « À revoir ». Réponse correcte avec effort : « Difficile » ; correcte sans difficulté :
   « Bon ». Ne pas utiliser « Difficile » pour masquer un oubli.
4. **Adapter le débit à la charge réelle.** Faire les révisions dues ; diminuer les nouvelles cartes
   si les révisions s’accumulent ou si les erreurs augmentent. Vingt est un point de départ, pas une
   prescription. Le deck ne promet pas un temps quotidien fixe.
5. **Utiliser les erreurs pour choisir la suite.** Noter si l’erreur vient d’une règle oubliée, d’un
   indice non vu, de la lecture de l’énoncé ou de la précipitation. Retrouver l’objectif dans
   [COUVERTURE](out/COUVERTURE.md). Réviser la règle existante avant de créer un doublon.
   Le [carnet d’erreurs](docs/07-entrainement.md) donne une méthode et un modèle.
6. **Ajouter l’approfondissement selon les besoins.** Importer le paquet complet conserve les notes
   du socle et ajoute les autres. On peut suspendre les nouvelles cartes portant
   `tag:parcours::approfondissement` puis réactiver les thèmes faibles ou les signaux rencontrés.
   Les tags historiques `importance::*` sont conservés ; **ils ne définissent plus le socle**.

L’ETG exige 35 réponses correctes sur 40. Comme repère personnel, viser des résultats réguliers de
37–38 sur des séries **nouvelles**, avec photos et vidéos, sans aide et au rythme de l’épreuve.
C’est une marge de préparation, ni un seuil officiel supplémentaire ni une garantie. Un bon taux de
réussite dans Anki ne mesure pas à lui seul l’aptitude à l’examen.
[Conditions officielles de l’ETG](https://www.service-public.gouv.fr/particuliers/vosdroits/F33694).

## Si une version précédente est déjà installée

Importer le **paquet complet** pour corriger aussi les anciennes notes d’approfondissement. Vérifier
le bilan d’import : aucun conflit de type de note ne doit laisser les anciennes formulations en place.
La migration est testée contre le paquet v2 présent dans le dépôt avant cette révision. Pour un autre
ancien build ou des types modifiés personnellement, inspecter les éventuels conflits dans Anki.

La conservation de l’historique ne signifie pas que les réponses corrigées sont déjà connues : chercher
`tag:revision::v3`, lire [le journal](docs/research/revision-v3.md), et revoir les cartes concernées.
Certaines formulations ou réponses ont changé. Une réimportation conserve aussi l’ordre et la
planification déjà présents : le programme publié décrit **un import neuf**, pas le réordonnancement
automatique de votre collection. Importer le Socle ne supprime pas les cartes déjà installées ;
suspendre `tag:parcours::approfondissement is:new` pour se concentrer sur lui.

## Contenu et entretien

Six types : reconnaissance visuelle, comparaison de signaux, fait à trous, question de décision,
affirmation justifiée et scénario dessiné. Les sous-decks suivent les thèmes ; les nouvelles cartes
sont entrelacées entre thèmes. Les [statistiques](out/STATS.md) sont générées à chaque build.
Les schémas sont simplifiés : aucune photo n’est inventée ni présentée comme une question officielle.

Chaque note porte une source. Les sources historiques sont parfois seulement des références de
manuel ou d’article ; **leur présence ne prouve pas une vérification récente de toute la phrase**.
L’audit v3 distingue les corrections vérifiées des éléments hérités, et retire les affirmations de
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
python -m build.verify --previous /chemin/ancienne-version.apkg
python -m build.preview --ids ab4,c-arret-somme,scn-dep-mixte-mon-cote --width 390
```

Le premier build nécessite un accès réseau pour les médias Commons ; les suivants utilisent le cache.
Les aperçus nécessitent Chrome/Chromium. Les sources YAML sont dans `data/`, les 41 objectifs dans
`data/_meta/objectives.yaml`. Le build refuse les références absentes et un socle dépassant 600 cartes :
un ajout exige un arbitrage. Les modèles, GUID, numéros de cloze, identifiants de champs et de gabarits
sont à préserver. [Conception](docs/03-conception-des-cartes.md), [vérification des paquets](out/VERIFICATION.md).

## Licences

Textes, code et schémas originaux : CC BY-SA 4.0. Images Commons : licence propre à chaque fichier,
avec auteurs et liens dans [ATTRIBUTIONS](out/ATTRIBUTIONS.md). Les représentations Commons de
signalisation ne sont pas une certification officielle du deck.
