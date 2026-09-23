Verdicts (190 notes) : OK 181 · FIX 9 · INCERTAIN 0 — par type : SOUS-EXTENSION 5 · SUREXTENSION 2 · SOURCE 2 · FAUX 0 · CONVENTION-NON-SIGNALÉE 0 · ÉTRANGER 0 · SANCTION 0 · CONTRADICTION 0

# Groupe B : rapport de fact-check (règles de circulation et scénarios)

Périmètre : les 190 notes de `B_ids.txt`, recto, réponse, explication et légendes lus un par un ; chaque article cité lu
dans `docs/research/sources/cdr.txt` (Code consolidé au 10/09/2026) ; lu aussi dans l'IISR, parties 1, 2, 3, 4, 6, 7 et 8
(PDF à jour de msr25.doubs.developpement-durable.gouv.fr) ; les 53 dessins de scénarios et les 53 images d'affirmations
et de questions ont été ouverts et comparés à la réponse. Aucune erreur de fond (règle fausse, sanction fausse, règle
étrangère) : tous les montants, classes et points vérifiés concordent (R412-19, R412-8, R414-4 à R414-16, R415-5 à
R415-12, R417-9 à R417-12, R421-6, R412-10, R413-17…). Les constats ci-dessous sont des conditions manquantes ou des
sources inexactes, en général de faible gravité.

## SOUS-EXTENSION (5)

### aff-l-depassement-intersection-prioritaire (`pourquoi`)
- Texte : « R414-11 interdit le dépassement aux intersections, sauf pour celui qui y est prioritaire (route prioritaire, ou STOP et cédez-le-passage pour les autres), aux carrefours à feux ou réglés par un agent. »
- Problème : la liste des exceptions se présente comme complète mais omet la première : dépasser un deux-roues est permis à toute intersection. Un apprenant en déduit qu'il ne peut pas dépasser un vélo ou un cyclomoteur à un carrefour à priorité à droite.
- Preuve : R414-11 al. 2 : « Tout dépassement **autre que celui des véhicules à deux roues** est interdit aux intersections de routes, sauf pour les conducteurs abordant une intersection où les conducteurs circulant sur les autres routes doivent leur laisser le passage en application des articles R. 415-6, R. 415-7 et R. 415-8, ou lorsqu'ils abordent une intersection dont le franchissement est réglé par des feux de signalisation ou par un agent ». (La note l-depassement-interdit-lieux-2 donne correctement l'exception.)
- Correction : `pourquoi: 'R414-11 interdit aux intersections le dépassement d’autre chose qu’un deux-roues, sauf pour celui qui y est prioritaire (route prioritaire, ou STOP et cédez-le-passage pour les autres), aux carrefours à feux ou réglés par un agent.'`

### aff-l-klaxon-nuit (`affirmation`)
- Texte : « S’il faut avertir de mon dépassement, je le fais de préférence par un appel de phares plutôt qu’au klaxon. »
- Problème : « de préférence » réduit à un conseil ce que le texte impose. Le verdict (vrai) et le `pourquoi` sont justes.
- Preuve : R416-2 : « De nuit, les avertissements **doivent** être donnés par l'allumage intermittent soit des feux de croisement, soit des feux de route, les signaux sonores ne devant être utilisés qu'en cas d'absolue nécessité. »
- Correction : `affirmation: S’il faut avertir de mon dépassement, je le fais par des appels de phares, pas au klaxon.`

### l-depassement-interdit-lieux (`explication`)
- Texte : « Sans ces trois indices, il reste à vérifier l’espace pour me rabattre et l’écart de vitesse (R414-4). »
- Problème : la phrase laisse penser qu'une fois ces trois indices écartés (visibilité, ligne continue, panneau), plus rien n'interdit le dépassement. D'autres lieux l'interdisent pourtant, y compris dans l'article que la carte cite en source.
- Preuve : R414-11 al. 2 (intersection, sauf si les autres routes me cèdent le passage, feux ou agent, ou dépassement d'un deux-roues) ; R414-5 : « A l'approche des passages prévus à l'intention des piétons, les conducteurs ne doivent effectuer de dépassement qu'après s'être assurés qu'aucun piéton n'est engagé sur le passage » ; R414-12 : « Tout dépassement est interdit aux traversées de voies ferrées non munies de barrières ou de demi-barrières. »
- Correction : `explication: D’autres lieux l’interdisent aussi : intersection où je ne suis pas prioritaire, passage piéton où un piéton peut être engagé, passage à niveau sans barrières. Restent à vérifier l’espace pour me rabattre et l’écart de vitesse (R414-4).` (ajouter R414-5 et R414-12 à `source`)

### l-panonceau-portee (`reponse`)
- Texte : « …le 70 ne vise que les véhicules dont le poids total autorisé en charge (PTAC, sur la carte grise) dépasse la valeur indiquée. »
- Problème : le panonceau de tonnage vise le PTAC **ou le PTRA**. Avec le seul PTAC, un apprenant exclurait les ensembles, par exemple une voiture qui tracte une remorque et dont le PTRA dépasse la valeur.
- Preuve : IISR 4e partie (VC 2019), panonceau M4f : « L'inscription d'un chiffre de tonnage sur un panonceau de catégorie M4f signifie que l'interdiction ne s'applique que si le poids total autorisé en charge ou le poids total roulant autorisé du véhicule ou de l'ensemble de véhicules couplés dépasse ce chiffre » (même formule pour B3a et B13).
- Correction : `reponse: 'Au panneau qu’il complète : ici, le 70 ne vise que les véhicules ou ensembles dont le poids total autorisé (PTAC, ou PTRA pour un ensemble, sur la carte grise) dépasse la valeur indiquée.'` (source : ajouter « IISR 4e partie (M4f) »)

### scn-pd-je-tourne-gauche-gauche-arrive (`explication`)
- Texte : « …le tourne-à-gauche ne m'oblige à céder qu'aux véhicules venant d'en face et aux piétons de la rue que j'aborde. »
- Problème : « ne… qu'aux » rend la liste exhaustive ; elle omet les usagers des pistes cyclables traversées. La note l-tourner-gauche-regle les mentionne bien.
- Preuve : R415-4 III : « Il doit céder le passage aux véhicules venant en sens inverse sur la chaussée qu'il s'apprête à quitter ainsi qu'aux engins de déplacement personnel motorisés, aux cycles et cyclomoteurs circulant dans les deux sens sur les pistes cyclables qui traversent la chaussée sur laquelle il va s'engager. »
- Correction : `explication: "La priorité à droite joue en ma faveur ; le tourne-à-gauche m'oblige à céder aux véhicules venant d'en face, aux usagers d'une piste cyclable que je traverse et aux piétons de la rue que j'aborde. Je m'assure que le rouge ralentit, puis je tourne."` (source : « R415-5 et R415-4 »)

## SUREXTENSION (2)

### aff-l-4-voies-double-sens (`pourquoi`)
- Texte : « Sur une chaussée à quatre voies à double sens, la ligne axiale est continue : la franchir est interdit (R412-19 : 135 €, 3 points). »
- Problème : la règle est générale dans la carte, alors que l'IISR ne l'impose qu'en rase campagne. En ville, une chaussée à 4 voies peut avoir un axe discontinu, et le franchir pour tourner est alors permis. Le dessin montre un axe continu, donc le verdict tient.
- Preuve : IISR 7e partie, art. 114-2 A (« Routes à quatre voies… en rase campagne ») : « En dehors des zones urbaines ou suburbaines… La ligne axiale est alors continue de largeur 5u » ; art. 114-5 (milieu urbain) : « il **peut** être nécessaire de tracer une ligne axiale continue de largeur 3 ou 5u sur les routes urbaines à 2 ou 4 voies ». Et R414-8 interdit de toute façon au dépassant « la voie située pour eux le plus à gauche ».
- Correction : `pourquoi: 'Chaque sens dispose de deux voies : celle de gauche sert au dépassement, puis je me replace à droite. Les voies d’en face sont interdites au dépassement (R414-8) ; ici, la ligne axiale est continue, comme toujours à quatre voies hors agglomération : la franchir est interdit (R412-19 : 135 €, 3 points).'`

### l-stationnement-alterne (`explication` et rappel c2)
- Texte : rappel « …le dernier jour de chaque période, changement de côté entre {{c2::20 h 30 et 21 h}} » ; explication « Le changement de côté se fait le soir, entre 20 h 30 et 21 h. »
- Problème : l'horaire est un horaire par défaut, que l'autorité locale peut changer. Faible gravité : la carte dit déjà de lire les panneaux pour les dates.
- Preuve : R417-2 III : « **Sauf dispositions différentes prises par l'autorité investie du pouvoir de police**, le changement de côté s'opère le dernier jour de chacune de ces deux périodes entre 20 h 30 et 21 heures. »
- Correction : `explication: 'Sauf arrêté local différent, le changement de côté se fait le soir, entre 20 h 30 et 21 h. Je lis les dates d’interdiction sur les panneaux : du 1er au 15, ou du 16 à la fin du mois. Une prescription de zone peut aussi imposer ce régime.'` (le rappel c2 peut rester tel quel, l'explication donnant la condition)

## SOURCE (2)

### l-implantation-danger (`source`)
- Texte : « IISR 2e partie, art. 28 ; … »
- Problème : les distances d'implantation (150 m, 200 m sur autoroute, 50 m en agglomération) figurent à l'article 25, pas à l'article 28. Le contenu de la carte est exact.
- Preuve : IISR 2e partie, **Article 25. Implantation des panneaux**, B : « Hors agglomération, la distance normale d'implantation est comprise entre 100 et 200 m. Elle est choisie aussi proche que possible de 150 m sur route et 200 m sur autoroute… En agglomération, la distance normale d'implantation est comprise entre 0 et 50 m. Elle est choisie aussi proche que possible de 50 m. »
- Correction : `source: "IISR 2e partie, art. 25 ; Sécurité routière, Exemples de nouvelles questions (Q18, Q19)"`. La même référence « art. 28 » peut figurer ailleurs (grep `art. 28` dans `data/` : seule cette note).

### l-tourner-droite-serrer (`source`)
- Texte : `source: Code de la route, art. R412-9, R412-23 et R415-14` pour « Je cède aux usagers de la piste cyclable que je dois traverser ».
- Problème : aucune des sources citées ne pose cette obligation : R415-14 traite la piste comme une voie de la chaussée qu'elle longe. L'article pertinent, R415-3, manque ; il pose aussi « serrer le bord droit ».
- Preuve : R415-3 I : « Tout conducteur s'apprêtant à quitter une route sur sa droite doit serrer le bord droit de la chaussée » ; III : « Il doit céder le passage aux engins de déplacement personnel motorisés, aux cycles et cyclomoteurs circulant dans les deux sens sur les pistes cyclables qui traversent la chaussée sur laquelle il va s'engager. »
- Correction : `source: Code de la route, art. R415-3, R412-9 et R415-14`

## Remarques sans verdict FIX (détails dans le ledger)
- aff-l-klaxon-hors-agglo et l-agglomeration-panneau citent en source un article sans rapport avec la carte (R416-3 dans la première, R416-1 dans la seconde) ; les autres sources suffisent.
- scn-tram-droite-moi-prioritaire : la règle suit la lecture de l'IISR (3e partie, art. 42-9 B 3°) déjà consignée dans `source_checks` (tram-priorite-iisr). Selon cette même lecture, la route perd son caractère prioritaire à la traversée et la perte est signalée en amont, alors que le dessin garde un losange AB6 juste avant la voie. Ce n'est pas faux pour la question posée.
- l-insertion-autoroute-priorite : R421-3 ne vise que les bretelles autoroutières ; pour une « voie rapide », c'est la signalisation d'entrée qui fonde la même conduite.
- l-entrecroisement et scn-pos-croisement-obstacle : aucun article ne vise expressément ces cas. Les deux réponses découlent de R421-3 et de R414-4 II 1°, et suivent l'enseignement courant.
- l-vitesse-hors-agglo : le département ne relève à 90 que les routes qui relèvent de lui (CGCT L3221-4-1) ; tolérable pour la « Route 1 » générique.
