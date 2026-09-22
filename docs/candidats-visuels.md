# Candidats à une illustration

Carte de discussion des dessins envisagés pour les notes qui n’en ont pas, avec la raison des décisions,
pour ne pas les réexaminer à chaque édition. Aucun quota : une image existe si elle apporte une donnée que le
texte ne peut pas établir (recto) ou explique une relation après le rappel (verso). Une trajectoire correcte
tracée d’avance, une légende qui nomme la réponse ou une couleur qui donne le verdict disqualifient un recto.

Déjà illustrés : 284 reconnaissances, 48 comparaisons, 56 scénarios, une trentaine de questions
(`image`, `image_ref`) et un schéma explicatif de verso (`illustration`). Le support technique est décrit
dans [maintenance](maintenance.md).

## Pistes ouvertes

| Note | Dessin envisagé | Condition pour l’intégrer |
|---|---|---|
| `aff-l-stop-avancer`, `l-stop-arret` | Recto : ligne d’arrêt, voiture déjà arrêtée, obstacle latéral masquant la rue transversale. | Le texte doit dire que l’arrêt a eu lieu ; ne pas placer la voiture au-delà de la ligne dès le premier arrêt. |
| `l-vocab-chaussee-voie` | Verso : un plan avec accolades chaussée / voie / accotement. | Contrôler les définitions (accotement, trottoir, BAU) avant le dessin. |
| `m-pneus-usure-1-6` | Verso : coupe d’une rainure avec témoin d’usure. | Documentation technique primaire ; une photo peut valoir mieux qu’un SVG. |
| `c-angle-mort-definition`, `u-pl-angles-morts` | Verso : zones masquées d’une voiture, puis d’un camion avec le vélo situé. | Aucune zone universelle ni promesse « hors zone colorée = vu ». |
| `l-portee-prescription`, `aff-l-zone-30-portee` | Verso : deux parcours comparables avec intersection et panneaux. | Vérifier l’IISR ; ne pas généraliser la règle d’un panneau isolé. |
| `r-pn-engagement` | Recto : rails et file arrêtée juste après, espace de dégagement insuffisant. | Une seule scène de blocage suffit ; relire `r-tram-traversee-degager` et `l-intersection-encombree`. |

## Écartés, et pourquoi

- Gestes de secours (`a-pls`, `a-rcp-dae`, `a-hemorragie`) : un dessin du geste au recto donne l’action ;
  une procédure graphique demanderait des références techniques dédiées.
- Indices à percevoir (`c-indice-ballon`, `c-indice-cycliste-regard`, `r-nuit-vitesse-visibilite`) : un
  SVG rend le rappel trivial ; ce sont des photos et vidéos nouvelles qui entraînent la perception.
- Rétroviseurs et pente (`p-retro-*`, `p-pente-roues`) : les anciens dessins donnaient la réponse au recto
  ou représentaient mal la pente ; le texte suffit.
- Pictogrammes de médicaments au recto (`c-medicaments-niveaux`) : ils portent la consigne demandée.
- Doublons de reconnaissance (`e-covoiturage-voie`, `kd10`, `ak5`, `k5a`) : le signal a déjà sa carte ; une
  scène supplémentaire doit entraîner une décision distincte.
- Sanctions, seuils, formalités, écoconduite générale : aucune scène nécessaire.

Pour un candidat : écrire la décision que l’apprenant doit prendre, comparer la version textuelle à un
prototype de carte complète, vérifier que le cas fonctionne si l’on déplace un usager (règle transférable, pas
souvenir d’une composition), puis suivre la procédure de [maintenance](maintenance.md) (source, registre,
rendu clair et sombre sur téléphone).
