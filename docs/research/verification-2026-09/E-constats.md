Verdicts (210 notes) : OK 205 · FIX 4 · INCERTAIN 1 — types : SOUS-EXTENSION 1 · SUREXTENSION 1 · SOURCE 2 (dont 1 avec chiffre inexact) · INCERTAIN 1 · FAUX 0 · CONVENTION-NON-SIGNALÉE 0 · ÉTRANGER 0 · SANCTION 0 · CONTRADICTION 0

# Rapport du groupe E (méthode d’examen, premiers secours, prendre et quitter le véhicule, mécanique et équipements, sécurité des passagers et du véhicule, environnement)

Sources principales relues : Code consolidé du 10/09/2026 (`docs/research/sources/cdr.txt`) ; références techniques nationales PSC de juillet 2026 (PDF téléchargé et lu en entier) ; exemples officiels de questions de la Sécurité routière (PDF local, rendu en images) et communiqué DSR du 11/09/2023 ; page « Accident de la route » de securite-routiere.gouv.fr (JSON) ; arrêté du 30/09/2008 art. 2 ; arrêté du 18/07/2019 art. 5 ; service-public F33513, F33371, F628, F19459, F33954 ; page 114 du ministère de l’Intérieur ; arrêté du 24/08/2020 (voies réservées). Le registre donne les sources note par note.

## SOUS-EXTENSION

### s-enfant-chiffres (3 cartes à trous ; `data/faits/10_securite_passager.yaml`, `explication`)
- **Texte** : « Exceptions pour l'avant : siège dos à la route avec airbag passager désactivé, absence de sièges arrière ou sièges arrière tous occupés par des enfants de moins de 10 ans. »
- **Problème** : la liste se présente comme complète, mais elle omet deux cas de R412-3 : sièges arrière **sans ceinture** et sièges arrière **momentanément inutilisables**. Elle omet aussi la condition du 3° : chaque enfant doit être retenu par un dispositif adapté.
- **Preuve** : R412-3 I, « 2° Lorsque le véhicule ne comporte pas de siège arrière ou si le siège arrière n'est pas équipé de ceinture de sécurité ; 3° Lorsque les sièges arrière du véhicule sont momentanément inutilisables ou occupés par des enfants de moins de dix ans, à condition que chacun des enfants transportés soit retenu par un système prévu au II de l'article R. 412-2. » La fiche service-public F628 donne la même liste (« rear seats lack belts, rear seats temporarily unusable »).
- **Correction** : « Exceptions pour l'avant : siège dos à la route avec airbag passager désactivé ; pas de sièges arrière ou sièges arrière sans ceinture ; sièges arrière momentanément inutilisables ou tous occupés par des enfants de moins de 10 ans, chaque enfant restant dans un dispositif adapté. Sanction : 135 € pour le conducteur, sans points. La limite légale est l'âge, pas la taille. »

## SUREXTENSION

### aff-m-feu-grille-nuit (`data/affirmations/09_mecanique.yaml`, `pourquoi`)
- **Texte** : « … contravention de 3e classe (68 €) avec immobilisation possible, surtout la nuit. »
- **Problème** : « surtout la nuit » laisse croire que l’immobilisation reste possible de jour par bonne visibilité. Le texte la limite à la nuit et au jour par visibilité insuffisante. Le recto et le verdict restent justes.
- **Preuve** : R313-3 VI, « La nuit, ou le jour lorsque la visibilité est insuffisante, en cas d'absence, de non-conformité ou de défectuosité des feux de croisement, l'immobilisation peut être prescrite » ; R313-3 V, « contraventions de la troisième classe ». La fiche service-public F19459 reprend la même formule.
- **Correction** : « Un feu défaillant est une contravention de 3e classe (68 €) ; la nuit, ou le jour par visibilité insuffisante, le véhicule peut être immobilisé. Un seul phare rend aussi le véhicule difficile à identifier par les autres usagers. »

## SOURCE

### aff-s-isofix (`data/affirmations/10_securite_passager.yaml`, `pourquoi`) : chiffre inexact et sans source citée
- **Texte** : « … Isofix équipe les véhicules neufs depuis 2011 ; deux sièges sur trois sont mal installés. »
- **Problème** : 2011 est confirmé. En revanche, aucune des deux sources citées ne donne « deux sièges sur trois ». La statistique française actuelle (Prévention routière, étude OURSE, janvier 2026) porte sur les **enfants** mal attachés : « près de 2 enfants observés sur 3 (62 %) présentent au moins une erreur d'installation ». Il s’agit surtout du réglage du harnais ou de la ceinture, pas seulement de la fixation du siège.
- **Preuve** : service-public F628, « Isofix, qui est obligatoire dans les véhicules neufs depuis 2011 » ; https://www.preventionroutiere.asso.fr/securite-des-enfants-en-voiture-toujours-pres-de-2-enfants-sur-3-sont-mal-attaches/
- **Correction** : « Le siège s'ancre par deux crochets sur des points fixes de la caisse, avec sangle haute ou jambe de force, au lieu d'être sanglé par la ceinture. Isofix équipe les véhicules neufs depuis 2011 ; près de deux enfants sur trois restent mal attachés (harnais, ceinture). » Ajouter à `source` : « ; Prévention routière, étude OURSE (2026) ».

### m-pneus-chiffres (2 cartes à trous ; `data/faits/09_mecanique.yaml`, `source`)
- **Texte** : `source: "R314-1 ; Michelin, …"`
- **Problème** : R314-1 traite des sculptures, des toiles et des déchirures des flancs. Il ne dit rien de la pression, de la mesure à froid ni de la fréquence de contrôle. Les affirmations de la carte sont justes, mais elles relèvent de Michelin et des notices (repère d’entretien, présenté comme tel).
- **Preuve** : R314-1, « doivent présenter sur toute leur surface de roulement des sculptures apparentes. Aucune toile ne doit apparaître … aucune déchirure profonde » (aucune mention de la pression).
- **Correction** : `source: "Michelin, https://www.michelin.fr/auto/conseils/pression-pneus/gonfler-pneus ; notices constructeurs (étiquette de pression)"`

## INCERTAIN

### aff-p-neige-toit (`data/affirmations/08_prendre_quitter.yaml`)
- **Texte** : « Je dois aussi déneiger le toit avant de partir. » (vrai)
- **Point non tranché** : aucun texte du Code consolidé n’impose explicitement de déneiger le toit. R412-6 II exige seulement que le « champ de vision » ne soit pas réduit, et R312-19 vise le « chargement ». Le seul appui est donc un conseil (Sécurité routière, « Conduire en hiver »). Or la carte du deck **etg-je-peux-je-dois** enseigne : « "Je dois" demande si elle est obligatoire ». Sur ce modèle, un apprenant lira ici une obligation légale.
- **Proposition, si le propriétaire ne trouve pas de texte** : garder l’affirmation (le « je dois » de sécurité est courant à l’ETG), mais ajouter au `pourquoi` : « Aucun article ne vise le toit en propre ; c’est une précaution de sécurité, et une plaque qui glisse sur le pare-brise réduit le champ de vision (R412-6 II). » Autre solution : reformuler l’affirmation en « Je déneige aussi le toit avant de partir. »

## Remarques sans correction (détail dans le registre)
- **Distance du triangle** : le deck suit l’arrêté du 30/09/2008 (« 30 mètres environ, ou au-delà si nécessaire »). La page « Accident de la route » de securite-routiere.gouv.fr conseille « 200 mètres en amont du sinistre ». Le texte légal prime et les cartes (triangle-distance, a-proteger-arret, m-panne-procedure-route, aff-a-triangle-autoroute) disent déjà « davantage si nécessaire ». Aucune correction.
- **aff-a-donner-a-boire** : la carte cite seulement le PSC 2026, qui ne contient pas la consigne. La source exacte est la page Sécurité routière : « Ne donnez ni à boire, ni à manger à un blessé ». On peut l’ajouter à `source`.
- **p-vehicule-emprunte-equipements** : R416-19 V n’attache aucune amende à l’absence du triangle à bord. La carte ne chiffre que le gilet (11 €), ce qui est juste.
- **aff-m-stationnement-arriere** : R412-6-3 vise la fonction d’aide au stationnement (manœuvre automatisée). La citation convient au cas de l’énoncé.
- **Casque du motard** : l’affirmation « retrait obligatoire si inconscient », trouvée en ligne, vient de sources suisses. La consigne française (Sécurité routière) est « Ne retirez pas le casque d’un motard ». Le deck la suit (ÉTRANGER évité).
