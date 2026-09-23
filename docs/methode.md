# Méthode de travail

Comment améliorer ou relire le deck sans tourner en rond. Les demandes ouvertes du type « relis et améliore »
ne convergeaient pas : chaque relecteur voyait une partie du deck, mêlait goûts et erreurs réelles, et chaque
correction locale créait une incohérence ailleurs. La méthode ci-dessous a fait converger le travail.

## Les principes

1. **Un problème signalé est l’exemple d’une classe.** Nommer la classe (règle énoncée trop largement, image
   qui donne la réponse, trou deviné par la phrase…), écrire ou ajuster le principe dans
   [conception](conception.md), puis chercher tous les cas dans le deck. Ne pas corriger la seule carte vue.
2. **Une consigne écrite avant de relire** : ce qu’on vérifie, les types d’erreur, la gravité, la preuve
   exigée. Tous les relecteurs appliquent la même ; leurs résultats s’additionnent.
3. **Tout couvrir, pas un échantillon** : chaque note reçoit un verdict et ses sources, le deck étant réparti
   en groupes. « OK » veut dire vérifié, pas « rien de bizarre ». C’est ce qui permet de finir.
4. **Un angle par passe** : exactitude juridique, apprenant qui étudie dans l’ordre sur les cartes rendues,
   apprenant qui répond au recto avant de lire le verso (question ambiguë, réponse décalée, carte devinée,
   prérequis pas encore vu), images en clair et en sombre, couverture du programme officiel de l’ETG,
   confrontation aux sources. Chaque angle trouve une classe de problèmes différente.
5. **Seul le fond bloque** : faux, trompeur, contradictoire. Le goût se note et ne se corrige pas.
6. **Preuve, puis vérification** : un constat cite sa source primaire ; chaque constat est revérifié avant
   d’être appliqué (les relecteurs se trompent aussi : règle étrangère, article mal lu, chiffre inventé).
7. **Corriger par type, dans tout le deck, au plus juste** : une seule formulation partout où l’erreur
   apparaît ; chercher l’ancienne formulation dans `data/` ; garder les `id` (reformuler plutôt que supprimer).
8. **Relecture finale des modifications** : une correction introduit souvent une nouvelle erreur ou laisse la
   même ailleurs. Après plusieurs passes, relire aussi l’écart net depuis la dernière base vérifiée, note par
   note (mieux, égal, moins bien, régression) : c’est là qu’apparaissent les faits justes perdus en route.
   Retirer une phrase exige de montrer, par une recherche dans les cartes rendues, que le fait vit ailleurs ; un
   doute « à vérifier » se tranche dans les registres de vérification avant de supprimer.
9. **Contrôles automatiques, puis les yeux** : `--check`, tests, `verify --previous`, `render_check`, puis la
   lecture des cartes rendues sur téléphone, en clair et en sombre. Réussir les contrôles ne prouve ni le sens
   ni la lisibilité.
10. **Garder la preuve et dire l’incertitude** : `data/_meta/source_checks.yaml`, les registres de
    `docs/research/verification-*`, et une liste franche de ce qui reste ouvert.

Une tâche est finie quand une passe complète et sa relecture finale ne laissent aucun constat bloquant, et que
les incertitudes restantes sont écrites. Quand les constats ne portent plus que sur des détails, une nouvelle passe
générale coûte presque autant qu’elle rapporte (une part des derniers défauts venait des corrections elles-mêmes) :
geler, étudier, et ne traiter que les retours d’usage.

## Mettre en œuvre

- **Consigne type** : [`research/verification-2026-09/consigne.md`](research/verification-2026-09/consigne.md)
  (types d’erreur : faux, surextension, sous-extension, convention non signalée, règle étrangère, sanction,
  contradiction, source). La reprendre et l’adapter à l’angle de la passe.
- **Matériel des relecteurs** : `python -m build.render_all dossier` (après un build) écrit le texte de toutes
  les cartes dans l’ordre d’étude (`dump.md`) et leurs captures pleine page à 390 px, recto et verso ; y joindre
  les sources (`docs/research/sources/cdr.txt`).
- **Contradictions chiffrées** : extraire de `data/` toutes les phrases contenant points, euros, km/h, mètres,
  durées ou g/L, et les comparer d’un coup.
- **Relecteurs** : peu nombreux, indépendants, avec une consigne autonome et l’interdiction de lancer d’autres
  agents ; ils ne modifient rien. Les corrections se font dans le fil principal.
- **Registre par note** : `id | verdict | sources | remarque`, puis un rapport des seuls constats, groupés par
  type, chacun avec citation et correction prête.
- **Publication** : le paquet rebâti passe `build.verify --previous` sur le paquet déjà importé ; les notes
  retirées y sont nommées pour que l’utilisateur les supprime.

## Gel, retours d’étude et publication

- **Gel** : après la passe finale, plus de relecture générale. Le deck ne change que pour un retour d’usage ou une
  règle modifiée.
- **Retours d’étude** : pendant l’étude, marquer d’un drapeau Anki la carte qui gêne (ambiguë, fausse, trop facile,
  mal placée, image peu claire) et noter un mot dans la carte ou à part avec son `Id`. Chaque retour se traite comme
  une classe (principe 1) : chercher les cartes semblables, corriger par type, relire les modifications.
- **Avant de publier** : revérifier sur Légifrance les règles datées (vitesses, sanctions, délits récents, décrets
  attendus) et dater l’état du droit dans le README ; regarder le deck sur AnkiDroid et AnkiMobile, en clair et en
  sombre ; relire `out/ATTRIBUTIONS.md` et la section Licences du README ; vérifier que le dépôt publié ne contient
  que des textes publics (le livre commercial et `cdr.txt` sont ignorés par git) ; noter dans maintenance.md le
  commit du paquet publié, référence des mises à jour suivantes.
