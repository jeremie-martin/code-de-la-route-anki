# Relecture des notes `data/reconnaissance/*.yaml`, `data/confusions/signalisation.yaml` et `data/scenarios/*.yaml`

Date : 21 septembre 2026. Périmètre : 423 notes de reconnaissance (19 fichiers), 49 paires de confusion, 48 scénarios. Chaque note a été lue intégralement.

Référentiels : texte consolidé du Code de la route (`cdr.txt`, édition du 10/09/2026) relu pour chaque article cité ci-dessous (R411-28, R412-8, R412-9, R412-11, R412-18 à R412-20, R412-29 à R412-33, R414-1 à R414-16, R415-4 à R415-12, R416-1, R416-2, R416-6, R416-7, R416-19, R417-2, R417-10, R417-11, R421-2, R421-6, R422-3, R432-3, D314-8) ; `docs/research/signs-notes.md`, `legal-facts.md`, `knowledge-facts.md` ; pages Wikipédia FR (listes des panonceaux, des signaux d'indication, des balises, de la signalisation temporaire, des feux, texte brut `action=raw`) ; API Wikimedia Commons (existence et description des fichiers). Les images ont été contrôlées visuellement sur les planches `out/qa/*.png` et, au besoin, sur les fichiers `out/media/`.

Sévérités : **ERREUR** = faux, image erronée ou contradiction interne ; **DOUTE** = incertain, à vérifier avant décision ; **STYLE** = rédaction, pertinence examen, source.

Résultat du contrôle image/code (point b) : les 366 images Commons (et 57 images générées) ont été comparées à leur `code` et à leur `nom` planche par planche ; les fichiers `France road sign <CODE>.svg` correspondent tous au code de leur note ; les noms atypiques (A9.svg pour A9b, B5c2, C64b new, C64d2, M3a1, M3b3, M6b debut mois, M6d1, M6f1, M12D, M11d.png, C117-B21b, D52a pour d50, D61b pour d60, FR road sign G1*, FR road beacon J*, K5B/K5D/K8e1/K10a/K10b, KC1/KD*/KM*, E42/E43/E44.svg, ISO 7000 - Ref-No *.svg, Kontrollleuchte *.svg) affichent bien le signal attendu (descriptions Commons relues par l'API). Les seuls problèmes d'image sont ceux listés ci-dessous (E31, voyant direction, ligne de cédez-le-passage, et quelques choix d'exemples).

---

## data/reconnaissance/panneaux_danger.yaml (29 notes)

**1. `a18`** — STYLE
- Problème : le piège dit « Ne pas confondre avec la fin de sens unique (pas de panneau spécifique) », alors que la note `c12` dit « La fin du sens unique peut être signalée par A18 ». Les deux sont vraies mais se contredisent en apparence : A18 est précisément le panneau utilisé quand une voie redevient bidirectionnelle.
- Correction (piege) : « C'est le seul panneau de danger implanté à l'endroit même du danger (pas à 150 m). Il n'existe pas de panneau « fin de sens unique » : c'est A18 qui signale qu'une voie à sens unique ou à chaussées séparées redevient bidirectionnelle. Ne pas confondre avec C24a (conditions particulières par voie). »

## data/reconnaissance/panneaux_priorite.yaml (9 notes)

**2. `ab3a`** — STYLE
- Problème : « Seul panneau de danger/priorité triangulaire pointe en bas » : AB3b et AB5 sont le même triangle (avec panonceau) et le panonceau M12 est aussi pointe en bas. Par ailleurs le fichier Commons `France road sign AB3a.svg` inclut le panonceau M9c « CÉDEZ LE PASSAGE » sous le triangle (visible sur la planche) : acceptable, mais à savoir pour la carte « nom du panneau ».
- Correction (complement, phrase concernée) : « Triangle pointe en bas (comme ses signaux avancés AB3b/AB5 et le panonceau M12) : reconnaissable par sa forme, même de dos ou couvert de neige. »

## data/reconnaissance/panneaux_interdiction.yaml (41 notes)

**3. `b2c`** — DOUTE
- Problème : « Le demi-tour est par ailleurs interdit sans panneau sur autoroute, dans les tunnels (C111), sur les ponts, en cas de visibilité insuffisante et sur les voies à sens unique. » Le Code n'interdit le demi-tour que sur autoroute (R421-6) et route express (R432-3 par renvoi) ; l'interdiction en tunnel vient de la légende IISR de C111 ; « sur les ponts » n'a aucune base (cdr.txt : `grep -n "demi-tour"` ne renvoie que R421-6 et R432-3).
- Correction (complement) : « Placé avant la section où s'applique l'interdiction. Sans panneau, le demi-tour est interdit sur autoroute et route express (R421-6, R432-3) et dans les tunnels (C111) ; il est de toute façon impossible sur une voie à sens unique et dangereux partout où la visibilité est insuffisante (virage, sommet de côte). »

**4. `b3`** — STYLE
- Problème : complement en double : « Fin : B34. Fin : B34, B31, ou à la prochaine intersection si non répété. »
- Correction : « … ou M9 « rappel ». Fin : B34, B31, ou à la prochaine intersection si le panneau n'est pas répété. Sur les panneaux d'interdiction de dépasser, la voiture ROUGE est à gauche (celle qui dépasserait). »

**5. `b6a1`** — STYLE
- Problème : « Fin : B50a (zone) » : B50a est la sortie de la *zone* B6b1, pas la fin d'un B6a1 ponctuel.
- Correction (complement, fin de phrase) : « Fin : prochaine intersection ou panonceau M8b (fin de section) ; en zone (B6b1) la fin est le panneau B50a. »

**6. `b14`** — STYLE
- Problème : « change aussi le régime de vitesse.. » (double point) ; complement très long qui répète deux fois la règle du support EB10 avec `eb10`.
- Correction : supprimer le point en trop ; garder une seule formulation : « Sur le même support qu'EB10 uniquement pour une vitesse < 50 km/h ; elle vaut alors dans toute l'agglomération. »

**7. `b16`** — STYLE
- Problème : « interdit de nuit (appels de phares à la place) » : R416-2 impose de nuit les avertissements lumineux, le klaxon restant possible « en cas d'absolue nécessité ».
- Correction (complement) : « … Hors panneau, le klaxon est interdit en agglomération sauf danger immédiat (R416-1) ; de nuit, on avertit par appels de phares, le klaxon n'étant admis qu'en cas d'absolue nécessité (R416-2). »

## data/reconnaissance/panneaux_zones.yaml (16 notes)

**8. `b58`** — ERREUR (valeur périmée)
- Problème : « pneus hiver (marquage 3PMSF ou M+S selon la période transitoire) » : la période transitoire est terminée depuis le 1er novembre 2024 ; seul le marquage 3PMSF (symbole alpin) vaut pneu hiver (D314-8 V ; legal-facts § 573 ; knowledge-facts 375).
- Correction (signification) : « Entrée d'une zone (communes de montagne désignées par le préfet) où, du 1er novembre au 31 mars, les véhicules doivent être équipés de pneus hiver marqués 3PMSF (le seul marquage M+S ne suffit plus depuis le 1er novembre 2024) ou détenir des chaînes/chaussettes à neige pour au moins deux roues motrices. »

## data/reconnaissance/panneaux_indication.yaml (57 notes)

**9. `c20a`** — STYLE (attribution)
- Problème : « Stationnement interdit 5 m en amont d'un passage piéton (loi LOM, très gênant 135 €) » : l'interdiction (R417-11 I 8° c) date du décret 2015-808 ; la loi LOM (2019) n'a fait qu'interdire l'aménagement de places dans ces 5 m (mise en conformité avant fin 2026).
- Correction (complement) : « … Arrêt et stationnement interdits 5 m en amont d'un passage piéton, hors emplacements matérialisés (R417-11, décret 2015-808 : très gênant, 135 €) ; la loi LOM impose la suppression de ces emplacements d'ici fin 2026. »

**10. `c6`** — STYLE
- Problème : « il a la priorité s'il a mis son clignotant » : R412-11 ne conditionne pas la règle au clignotant (« laisser les véhicules de transport en commun quitter les arrêts signalés comme tels ») ; le clignotant n'est que le signe de l'intention.
- Correction (conduite) : « Ne pas s'arrêter sur l'emplacement ; en agglomération, ralentir et au besoin s'arrêter pour laisser le bus quitter son arrêt (R412-11) — il annonce son départ par le clignotant. »

**11. `c12`** — STYLE
- Problème : « on peut utiliser toute la largeur de la chaussée » : R412-9 (rouler près du bord droit) s'applique aussi en sens unique ; on ne se place à gauche que pour tourner à gauche ou dépasser.
- Correction (signification) : « Indique que la chaussée est à sens unique : tous les véhicules circulent dans le sens de la flèche ; on peut se placer dans la voie de gauche pour tourner à gauche ou dépasser (les deux côtés sont dans le même sens) ; le demi-tour y est impossible. »

**12. `c25a`** — STYLE (image)
- Problème : le fichier Commons `France road sign C25a.svg` ne montre que trois lignes (50 / 80 / 130) ; la note énumère aussi 110 (chaussées séparées). Rien de faux, mais la carte image → sens peut surprendre.
- Correction (complement, ajouter) : « Le dessin ci-contre est simplifié (le panneau réel comporte aussi la ligne 110 km/h des routes à chaussées séparées). »

**13. `c50`** — STYLE (image)
- Problème : l'exemple Commons retenu porte « ARRÊT AUTORISÉ SUR TROTTOIR », mention rare et pédagogiquement trompeuse (l'arrêt sur trottoir est en principe très gênant).
- Correction : choisir un autre exemple de C50 (ou un `gen:` avec « NOUVEAU RÉGIME DE PRIORITÉ » / « ZONE DE COVOITURAGE »), ou ajouter en complement : « Exemple ci-contre : mention locale autorisant l'arrêt sur trottoir — cas exceptionnel, l'arrêt sur trottoir étant sinon très gênant (135 €). »

**14. `c65a`** — STYLE
- Problème : phrase commençant par une minuscule : « … depuis 2022-2024). dans les anciennes versions de l'IISR… ».
- Correction : « … depuis 2022-2024). Dans les anciennes versions de l'IISR, C65a/C65b désignaient la présignalisation des aires annexes (aujourd'hui assurée par les panneaux D46). »

**15. `c107`** — DOUTE
- Problème : « réservée aux véhicules à moteur circulant à plus de 40 km/h » : aucun seuil de 40 km/h n'existe dans le Code (R421-2 liste des catégories, pas une vitesse) ni dans la page IISR/Wikipédia du C107 ; legal-facts F6 ne le mentionne pas.
- Correction (signification) : « Début d'une route (voie express) réservée aux véhicules à moteur : interdite aux piétons, cycles, cyclomoteurs, tracteurs et véhicules lents, véhicules à traction animale. Interdiction d'arrêt, de stationnement, de demi-tour et de marche arrière. Vitesse maximale 110 km/h si 2×2 voies avec séparateur (100 par temps de pluie), 80 sur route bidirectionnelle. » (supprimer « circulant à plus de 40 km/h » sauf source IISR trouvée).

**16. `a13b` / `c20a` / `marq-passage-pietons`** — STYLE (doublon de `nom`)
- Problème : trois notes ont exactement le même `nom` « Passage pour piétons » ; pour une carte image → nom, la réponse ne distingue pas le triangle (annonce) du carré bleu (position) ni du marquage.
- Correction : `a13b` nom → « Passage pour piétons (annonce, danger) » ; `c20a` nom → « Passage pour piétons (position) » ; `marq-passage-pietons` nom → « Passage pour piétons (marquage au sol) ». Même remarque pour `ce2a` / `m9e` (« Poste d'appel d'urgence ») : `m9e` nom → « Panonceau : poste d'appel d'urgence (sous C8) ».

## data/reconnaissance/panonceaux.yaml (81 notes)

**17. `m6i`** — ERREUR (barème)
- Problème : « Ne pas occuper l'emplacement avec un véhicule thermique (très gênant : 135 €) ». R417-10 III 3° classe le stationnement « devant les dispositifs destinés à la recharge en énergie des véhicules électriques » comme *gênant* : 2e classe, 35 € (fourrière possible, R417-10 V). knowledge-facts 524 fait la même erreur.
- Correction (conduite) : « Ne pas occuper l'emplacement avec un véhicule non électrique ou hors recharge : stationnement gênant (R417-10 III 3°), 35 € et mise en fourrière possible. »

**18. `m8d`, `m8e`, `m8f`** — ERREUR (texte ≠ image)
- Problème : les fichiers Commons montrent M8d = flèche horizontale vers la droite (→), M8e = vers la gauche (←), M8f = double flèche horizontale (↔) ; la note dit « M8e et M8f : variantes (deux sens, flèches obliques) » et pour m8f « flèches obliques pour un stationnement en épi ou perpendiculaire ». Wikipédia (liste des panonceaux, IISR art. 9) : « la section sur laquelle s'applique la prescription s'étend dans le ou les sens indiqués par la ou les flèches ; la distance indiquée précise la longueur de la section ». De plus m8e et m8f ont le même `nom` « Section d'application (variante) ».
- Correction :
  - `m8d` nom : « Section d'application vers la droite (flèche horizontale) » ; signification : « Flèche horizontale vers la droite : la section sur laquelle s'applique la prescription d'arrêt/stationnement s'étend à droite du panneau (panneau implanté face à la chaussée, ex. parking, place) ; la distance éventuelle précise sa longueur. M8e : vers la gauche ; M8f : des deux côtés. »
  - `m8e` nom : « Section d'application vers la gauche (flèche horizontale) » ; signification : « Flèche horizontale vers la gauche : la section concernée s'étend à gauche du panneau, sur la distance éventuellement indiquée. »
  - `m8f` nom : « Section d'application des deux côtés (double flèche horizontale) » ; signification : « Double flèche horizontale : la prescription s'applique de part et d'autre du panneau, sur les distances éventuellement indiquées. »

**19. `m9v3`** — ERREUR (texte ≠ image) + STYLE
- Problème : « (M9v3 : inscription « SAUF » + pictogramme ; M9v4 : pictogramme seul) ». Vérifié sur Commons : M9v3 = « INTERDIT SAUF » + cyclomoteur, M9v4 = « SAUF » + cyclomoteur (même logique que M9v1/M9v2). Le complement se termine par « présents sur Commons ; » (ponctuation orpheline).
- Correction (signification) : « Précise que la prescription du panneau associé ne s'applique pas aux cyclomoteurs (M9v3 : « INTERDIT SAUF » + pictogramme cyclomoteur ; M9v4 : « SAUF » + pictogramme), par exemple pour ouvrir un double-sens cyclable aux cyclomoteurs. » ; (complement) : « Sous le panneau qu'il complète, sur le même support ; il ne s'applique qu'à ce panneau. Panonceaux récents (postérieurs à 2015), rares à l'examen. »

**20. `m6e`** — DOUTE
- Problème : nom « Stationnement payant avec parcmètre individuel » ; l'image (`France road sign M6e.svg`) porte l'inscription « STATIONNEMENT PAYANT HORODATEUR » + flèche. Wikipédia donne pour M6d et M6e la même légende « stationnement payant avec parcmètre » (M6d = pictogramme, M6e = inscription + flèche vers l'appareil). La mention « individuel » ne repose sur rien.
- Correction : nom → « Stationnement payant (inscription et direction de l'horodateur) » ; signification → « Variante par inscription de M6d : « stationnement payant horodateur » avec une flèche indiquant où se trouve l'appareil de paiement. »

**21. `m7`** — STYLE
- Problème : « Sous AB2 (route prioritaire) » : AB2 est la priorité *ponctuelle* ; la route prioritaire est AB6.
- Correction (complement) : « Sous AB2 (intersection où je suis prioritaire) ou sous AB3b/AB5 (pour montrer la configuration du carrefour). »

**22. `m10a`, `m10b`, `m10c`, `m10z`** — STYLE
- Problème : le complement générique « Sous le panneau qu'il complète… » contredit la signification (« placé au-dessus du panneau ») : les cartouches M10 se placent au-dessus.
- Correction (complement des quatre notes) : « Cartouche placé AU-DESSUS du panneau qu'il complète (exception parmi les panonceaux) ; il ne s'applique qu'à ce panneau. »

## data/reconnaissance/balises.yaml (11 notes)

**23. `j1bis`** — STYLE (couverture)
- Problème : la balise J1bis (rare) est présente alors que J1 (balise de virage, bande blanche) et J3 (balise d'intersection, bande rouge) — la confusion classique de l'examen, citée dans signs-notes §8 — sont absentes faute de fichier Commons (`FR road beacon J1.svg` / `J3.svg` n'existent pas). Le piège « J1 blanche / J3 rouge / J6 noire oblique » n'est donc porté par aucune carte.
- Correction : ajouter J1 et J3 avec un générateur `gen:` (piquet blanc 1 m, bande blanche pour J1, rouge pour J3), et rétrograder ou supprimer `j1bis` ; ou, a minima, ajouter à `j6` un piège : « J1 (virage) = bande blanche ; J3 (intersection) = bande rouge ; J6 (délinéateur) = bande noire oblique + catadioptre. »

## data/reconnaissance/temporaire.yaml (31 notes)

**24. `triangle-presignalisation`** — ERREUR (barème)
- Problème : « Gilet + triangle obligatoires (amende 135 € si absents ou non utilisés) ». R416-19 V : non-utilisation (ne pas présignaler / ne pas revêtir le gilet) = 4e classe, 135 € ; gilet non à portée de main = 1re classe, 11 € ; absence du triangle à bord : sanctionnée comme non-présentation (11 €, R233-1). legal-facts § 323 signale explicitement ce piège.
- Correction (complement) : « Au moins 30 m en amont du véhicule (plus loin si visibilité réduite, virage, sommet de côte), sauf danger pour soi (autoroute). Gilet et triangle obligatoires à bord : absence = 11 € (1re classe) ; ne pas revêtir le gilet ou ne pas présignaler un véhicule dangereux = 135 € (4e classe). Sur autoroute, la pose du triangle est déconseillée si elle met en danger : priorité à l'évacuation derrière la glissière. »

**25. `k8`** — STYLE (texte ≠ image)
- Problème : « Balise jaune et/ou rouge et blanche portant une flèche oblique (comme B21a1 en version chantier) » ; le fichier `K8e1.svg` montre un chevron rouge sur fond blanc pointant vers la droite.
- Correction (signification) : « Balise rectangulaire blanche portant un chevron rouge (parfois une flèche) implantée en tête de chantier ou de déviation : elle indique de quel côté contourner l'obstacle ou le rétrécissement. »

**26. `k5d`** — STYLE (texte ≠ image)
- Problème : « Balise de guidage (chevron ou flèche) rouge et blanche » ; le fichier `K5D.svg` montre une balise cylindrique jaune à bandes blanches rétroréfléchissantes. Wikipédia : K5c = balise d'alignement (rouge/blanc), K5d = balise de guidage.
- Correction (signification) : « Balise de guidage K5d : cylindre (ou lame) jaune à bandes blanches rétroréfléchissantes, implantée en file pour guider les usagers le long d'une déviation de trajectoire ; la balise d'alignement rouge et blanche est la K5c. »

**27. `k2`** — STYLE (image)
- Problème : le fichier `Barrage K2.webp` montre une barrière K2 surmontée d'un panneau « FIN DE CHANTIER », ce qui brouille la carte « barrage / route barrée ».
- Correction : préférer une photo ou un `gen:` de barrière seule ; à défaut ajouter au complement : « Sur l'image, la barrière porte un KC1 « fin de chantier » ; la barrière seule signale une fermeture ou un obstacle. »

**28. `ak2`, `ak3`, `ak4`, `ak5`, `ak14`, `ak17`, `ak22`, `ak30`, `ak31`, `ak32`** — STYLE
- Problème : complement redondant : « La signalisation temporaire prévaut sur la permanente. Fond JAUNE = signalisation temporaire (…) : elle prévaut sur la signalisation permanente contradictoire. »
- Correction (fin de complement commune) : « Fond JAUNE = signalisation temporaire (chantier, événement, danger passager) : elle prévaut sur la signalisation permanente contradictoire. »

## data/reconnaissance/marquages.yaml (30 notes)

**29. `marq-ligne-cedez`** — ERREUR (image ≠ texte)
- Problème : le générateur `transversale` (`build/gen_images.py`, branche `kind == "cedez"`) dessine une rangée de triangles blancs (« dents de requin ») derrière la ligne discontinue, alors que le complement de la note affirme que ces triangles « ne sont pas un marquage réglementaire de l'IISR » et qu'« en France les triangles réglementaires signalent un ralentisseur » (signs-notes §8). La carte se contredit elle-même, et la paire `conf-stop-cedez-lignes` reprend l'erreur (« souvent précédée de triangles blancs »).
- Correction : retirer les triangles du générateur (ne garder que la ligne T'2 50 cm / 50 cm, éventuellement l'inscription au sol ou le panneau AB3a) ; voir aussi le point 44.

**30. `marq-ligne-jaune-zigzag`** — ERREUR (barème)
- Problème : « S'arrêter ou stationner sur un emplacement réservé aux bus = très gênant (135 €, R417-11) ». R417-10 II 2° : arrêt ou stationnement « sur les emplacements réservés à l'arrêt ou au stationnement des véhicules de transport public de voyageurs » = *gênant*, 2e classe, 35 € (fourrière possible). Le très gênant de R417-11 I 1° vise les voies/chaussées réservées (couloir bus), pas l'emplacement d'arrêt.
- Correction (complement) : « Aux arrêts de bus (panneau C6). S'arrêter ou stationner sur l'emplacement réservé au bus = stationnement gênant (R417-10 II 2°) : 35 € et mise en fourrière possible ; circuler ou stationner dans un couloir bus est en revanche très gênant (135 €). »

## data/reconnaissance/voyants.yaml (26 notes)

**31. `voyant-direction`** — ERREUR (image)
- Problème : le fichier `ISO 7000 - Ref-No 2305.svg` (« Steering system », vérifié par l'API Commons) représente un volant vu de profil avec sa colonne : à l'écran, un coin rouge abstrait impossible à reconnaître (cf. `out/media/cdr_img_voyant-direction.png`). Le témoin réellement affiché par les voitures est un volant vu de face avec un point d'exclamation.
- Correction : utiliser `commons: Kontrollleuchte Lenkhilfe.svg` (volant + « ! » ; le fichier contient deux variantes côte à côte, jaune et rouge, à recadrer ou à teinter) ou un `gen:` volant + « ! » ; garder `code: ISO 7000-2305` seulement si le symbole affiché est celui-là.

**32. `voyant-position`** — STYLE
- Problème : « Seuls, ils suffisent uniquement à l'arrêt ou en stationnement de nuit sans éclairage public ; pour rouler, je passe en feux de croisement. » R416-6 II 3° admet en agglomération, sur chaussée suffisamment éclairée, de circuler « avec au moins leurs feux de position », et R416-12 impose les feux de position à l'arrêt sur chaussée « pourvue ou non d'éclairage public ».
- Correction (conduite) : « À l'arrêt ou en stationnement sur la chaussée la nuit, ils sont obligatoires (R416-12). Pour rouler, ils ne suffisent qu'en agglomération sur une rue suffisamment éclairée (R416-6) ; partout ailleurs, feux de croisement. »

**33. `voyant-temperature`** (et `conf-voyant-croisement-route`) — STYLE (cohérence)
- Problème : le piège dit « En bleu au démarrage sur certains véhicules = moteur froid », mais la paire `conf-voyant-croisement-route` affirme « Le bleu est le seul voyant bleu du tableau de bord ».
- Correction (`conf-voyant-croisement-route`, dernière phrase) : « Le voyant de feux de route est pratiquement le seul voyant bleu du tableau de bord (avec, sur certains modèles, le thermomètre bleu « moteur froid »). »

## data/reconnaissance/panneaux_localisation.yaml (6 notes)

**34. `e31`** — ERREUR (image)
- Problème : le générateur `lieu_dit` (`build/gen_images.py`, ligne 748 : « white background, black text, black border ») dessine « LE BOURG » en lettres droites noires sur fond blanc bordé de noir. Le panneau E31 réel est un rectangle à fond NOIR portant le nom en lettres BLANCHES ITALIQUES (police L4) — c'est ce que dit le piège de la note elle-même, `signs-notes.md` §1 et §8, et la photo Commons `FR 17 Sainte-Gemme - Panneaux E31 et KD69b.jpg` (« Prouataire », blanc italique sur noir). Telle quelle, l'image ressemble à un EB10 sans liseré rouge et enseigne le contraire du piège. (`knowledge-facts.md` ligne 1069 « fond blanc sans liseré » est également fausse.)
- Correction : `lieu_dit` → fond `#111`, texte blanc `font-style="italic"`, listel blanc fin ; ou remplacer par la photo Commons citée. Le piège de la note est correct et peut rester.

**35. `eb10`** — STYLE
- Problème : complement répétitif : « Seuls B14 (< 50 km/h), AB6, AB7, B30, B52, E31, E32 peuvent être sur le même support. Fin : EB20. Seul un B14 inférieur à 50 (30, 40) peut être sur le même support que l'EB10 ; il vaut alors pour toute l'agglomération. »
- Correction : « À la limite de l'agglomération, surmonté d'un cartouche de route (E41-E44). Seuls B14 (< 50 km/h, valable alors pour toute l'agglomération), AB6, AB7, B30, B52, E31, E32 peuvent partager son support. Fin : EB20. Un 70 (relèvement) est implanté après l'EB10 et ne vaut que sur la route concernée, jusqu'à la prochaine intersection ou au B33. Un E31 (lieu-dit, lettres italiques blanches sur fond noir) ne limite PAS la vitesse à 50. »

## data/reconnaissance/voies_reservees.yaml (2 notes)

**36. `vr-losange-debut`** — STYLE
- Problème : « Fin : VR-LOSANGE-FIN » (identifiant interne visible sur la carte).
- Correction : « Fin : panneau à losange barré de rouge (voir carte suivante). »

---

## data/confusions/signalisation.yaml (49 paires)

**37. `conf-b15-c18`** — ERREUR
- Problème : « **B15** (rond bordé de rouge, flèche rouge à gauche) ». Sur le panneau B15 (vérifié sur `out/media/cdr_img_b15.png`), la flèche ROUGE est à DROITE et pointe vers le HAUT (c'est moi) ; la flèche noire, à gauche, pointe vers le bas (l'autre). La note `b15` est juste ; la paire dit l'inverse.
- Correction (difference) : « **B15** (rond bordé de rouge : flèche rouge à droite pointant vers le haut = moi, flèche noire à gauche = l'autre) : je dois **céder le passage** aux véhicules venant en sens inverse dans le rétrécissement. **C18** (carré bleu : flèche blanche à droite vers le haut = moi, flèche rouge à gauche vers le bas = l'autre) : j'ai la **priorité** sur les véhicules d'en face. Dans les deux cas, la flèche rouge désigne celui qui cède. Les deux panneaux sont toujours posés en vis-à-vis. »

**38. `conf-eb10-e31`** — ERREUR
- Problème : « **E31** (nom sur fond blanc, bordure noire, ou fond bleu) » : E31 = fond noir, lettres blanches italiques (cf. point 34) ; « fond bleu » ne correspond à rien (E32 cours d'eau est aussi noir/blanc).
- Correction (difference) : « **EB10** (nom en lettres droites noires sur fond blanc, **bordure rouge**) : entrée d'agglomération — 50 km/h, règles de l'agglomération jusqu'au panneau de sortie barré (EB20). **E31** (nom en lettres **italiques blanches sur fond noir**) : simple localisation d'un lieu-dit ou hameau — aucun changement de règle. »

**39. `conf-stop-cedez-lignes`** — ERREUR (cohérence)
- Problème : « ligne transversale discontinue, souvent précédée de triangles blancs » contredit `marq-ligne-cedez` (triangles non réglementaires en France pour le cédez-le-passage).
- Correction (difference) : « **Ligne d'arrêt (STOP)** : ligne transversale **continue**, large (50 cm) : arrêt complet obligatoire à son niveau. **Ligne de cédez-le-passage** : ligne transversale **discontinue** (traits de 50 cm) : céder le passage, sans obligation d'arrêt si la voie est libre. Les triangles blancs au sol signalent en France un ralentisseur, pas un cédez-le-passage. »

**40. `conf-c107-c207`** — STYLE (source)
- Problème : source « R413-2 et R422-4 » : R422-4 concerne les ponts. Les interdictions d'accès des routes express sont posées par l'IISR (art. 75) et le Code de la voirie routière, R421-2 ne visant que les autoroutes.
- Correction (source) : « Code de la route, art. R413-2 (vitesses) ; IISR 5e partie, art. 75 (C107/C108) ; Code de la route, art. R421-2 (autoroutes) ».

**41. `conf-r14-r16`** — STYLE (source)
- Problème : source « R412-30 et R412-33 » : R412-30 est le feu rouge ; la flèche jaune clignotante relève de R412-32.
- Correction (source) : « IISR 6e partie ; Code de la route, art. R412-32 (jaune clignotant) et R412-33 (vert) ».

**42. `conf-voyant-croisement-route`** — STYLE : voir point 33.

**43. `conf-a13b-c20a`** — STYLE : dépend du point 16 (les deux notes ont le même `nom`) ; la paire est correcte.

**44. `conf-continue-dissuasion`** — STYLE
- Problème : « sauf pour dépasser un cycliste en chevauchant » : l'exception R412-19 vise aussi les EDPM et cyclomobiles légers (la note `marq-ligne-continue` est complète).
- Correction : « — sauf pour dépasser, en la chevauchant, un cycliste, une trottinette (EDPM) ou un cyclomobile léger, avec visibilité. »

---

## data/scenarios/priorites.yaml (25 scénarios)

Les 20 `check` ont été relus contre les `reponse` : ordre et sens (avant/après/indépendant) concordent partout (y compris les scénarios à trois véhicules et les agents). Restent des erreurs de références juridiques et deux schémas.

**45. `scn-tram-gauche`** — ERREUR (article)
- Problème : « Le tramway est toujours prioritaire aux intersections (art. R415-11) » et source « R415-11 » : R415-11 est la priorité des piétons. La priorité du tramway vient de R422-3 I (« la priorité de passage appartient aux matériels circulant normalement sur cette voie ferrée »), correctement cité dans `scn-tram-droite-moi-prioritaire`.
- Correction (explication) : « Le tramway est prioritaire sur tous les usagers, même venant de gauche (art. R422-3 I) ; seuls des feux ou un agent peuvent l'arrêter. Il ne peut pas freiner court ni dévier : je m'arrête avant les rails. » ; (source) : « Code de la route, art. R422-3 ».

**46. `scn-sortie-parking`** — ERREUR (article)
- Problème : « Art. R415-9 et R415-10 : sortie de lieu non ouvert à la circulation publique = céder à tous les usagers, piétons compris » : R415-10 est le carrefour à sens giratoire. R415-9 II impose de céder « à tout autre véhicule » ; les piétons relèvent de R415-9 I (franchissement du trottoir) et R415-11.
- Correction (explication) : « Art. R415-9 : celui qui débouche d'un accès non ouvert à la circulation publique, d'un chemin de terre ou d'une aire de stationnement doit céder le passage à tout autre véhicule (et aux piétons du trottoir qu'il franchit, R415-11). Même chose pour un véhicule qui quitte un stationnement ou une voie non revêtue. » ; (source) : « Code de la route, art. R415-9 et R415-11 ».

**47. `scn-feu-orange-clignotant`** — STYLE (article)
- Problème : « à défaut, la priorité à droite (art. R412-30) » et source « R412-30 » : R412-30 = feu rouge ; le jaune clignotant est R412-32.
- Correction : remplacer par « (art. R412-32 et R415-5) » dans l'explication et la source.

**48. `scn-feu-vert-tourne-gauche`** — STYLE (source)
- Problème : source « R412-30 et R415-4 » : le feu vert est R412-33.
- Correction (source) : « Code de la route, art. R412-33 et R415-4 ».

**49. `scn-agent-bras-tendus-profil`, `scn-pd-les-deux-tournent-droite`** — STYLE (source)
- Problème : R412-29 (couleurs des feux) et R415-4 (tourne-à-gauche) n'ont pas de rapport avec ces cas.
- Correction : `scn-agent-bras-tendus-profil` source → « Code de la route, art. R411-28 » ; `scn-pd-les-deux-tournent-droite` source → « Code de la route, art. R415-5 (aucun conflit de trajectoires) ».

**50. `scn-giratoire-cedez` et `scn-rond-point-priorite-droite`** — STYLE (schéma)
- Problème : `{pos: inside, angle: 300}` place la voiture rouge au sud-est de l'anneau, c'est-à-dire *après* mon entrée dans le sens de rotation (0° = est, sens antihoraire, cf. `build/diagrams.py` ligne 423) : elle s'éloigne vers la sortie est. Or les deux questions disent « une voiture circule dans l'anneau, à ma gauche », et la réponse du rond-point (« celui qui entre est prioritaire ») suppose un véhicule qui *arrive* sur ma gauche.
- Correction : `angle: 225` (ou 210-240) dans les deux specs, pour que la voiture rouge approche de mon entrée par la gauche.

**51. `scn-rond-point-priorite-droite`** — STYLE (question ≠ schéma)
- Problème : la question dit « Rond-point SANS panneau AB25 ni cédez-le-passage » mais le schéma (`giratoire: false`) dessine un AB1 à chaque entrée.
- Correction (question) : « Rond-point sans panneau AB25 ni cédez-le-passage, seulement des AB1 (rare, ex. place de l'Étoile). Une voiture circule dans l'anneau à ma gauche. Puis-je m'engager ? »

## data/scenarios/priorites2.yaml (10 scénarios)

Aucune erreur : réponses conformes aux `check`, articles exacts (R415-4, R415-6, R415-7, R415-9, R415-11, R415-12, R422-3, R411-28).

## data/scenarios/depassement.yaml (14 scénarios)

Articles et barèmes vérifiés (R412-8 : 3 points ; R412-19 ; R412-20 ; R414-4 à R414-8 ; R414-11 ; R414-16 : 2 points ; R414-5) : exacts.

**52. `scn-pos-croisement-obstacle`** — STYLE (source)
- Problème : « Règle du croisement (R414-1 et suivants) : celui dont la voie est encombrée cède » : aucun article ne le dit ; R414-1 pose seulement le croisement à droite et R414-2 vise les gabarits. C'est une règle de conduite enseignée (et la solution des panneaux B15/C18 quand elle est signalée).
- Correction (explication) : « Règle de conduite : l'obstacle est de mon côté, c'est à moi de laisser passer le véhicule d'en face avant de contourner (R414-1 : le croisement se fait à droite, chacun serrant sur sa droite). Sur un pont ou un passage étroit, les panneaux B15 (je cède) et C18 (j'ai la priorité) fixent l'ordre. »

---

## Résumé

| Fichier | ERREUR | DOUTE | STYLE |
|---|---|---|---|
| reconnaissance/panneaux_danger | 0 | 0 | 1 |
| reconnaissance/panneaux_priorite | 0 | 0 | 1 |
| reconnaissance/panneaux_interdiction | 0 | 1 | 4 |
| reconnaissance/panneaux_zones | 1 | 0 | 0 |
| reconnaissance/panneaux_indication | 0 | 1 | 7 |
| reconnaissance/panonceaux | 3 | 1 | 2 |
| reconnaissance/balises | 0 | 0 | 1 |
| reconnaissance/temporaire | 1 | 0 | 4 |
| reconnaissance/marquages | 2 | 0 | 0 |
| reconnaissance/voyants | 1 | 0 | 2 |
| reconnaissance/panneaux_localisation | 1 | 0 | 1 |
| reconnaissance/voies_reservees | 0 | 0 | 1 |
| confusions/signalisation | 3 | 0 | 5 |
| scenarios/priorites | 2 | 0 | 5 |
| scenarios/priorites2 | 0 | 0 | 0 |
| scenarios/depassement | 0 | 0 | 1 |
| **Total (52 constats)** | **14** | **3** | **35** |

Les fichiers `panneaux_obligation`, `panneaux_fin`, `panneaux_services`, `passage_a_niveau`, `feux`, `autres`, `panneaux_direction` n'appellent aucune remarque. Aucun doublon d'`id` ni de `code` ; trois doublons de `nom` (point 16). Les ERREUR à traiter en priorité, parce qu'elles enseignent le faux à l'examen : E31 (34, 38), B15/C18 (37), barèmes 35 € vs 135 € (17, 30) et 11 € vs 135 € (24), M8d-f (18), M9v3/M9v4 (19), triangles du cédez-le-passage (29, 39), 3PMSF (8), articles R415-11/R415-10 des scénarios (45, 46), voyant de direction (31).
