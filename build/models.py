"""Anki note types (models) for the deck: fields, card templates and CSS.

Stable ids: the backend assigns fresh ids on creation, so build.py remaps them
to these constants in SQLite before export (see build.py:remap_ids). Keeping
ids stable lets a learner import a new version of the deck without losing
review history.
"""

MODEL_IDS = {
    "CDR Reconnaissance": 1758400000001,
    "CDR Confusion": 1758400000002,
    "CDR Fait": 1758400000003,
    "CDR Question": 1758400000004,
    "CDR Scenario": 1758400000005,
    "CDR Affirmation": 1758400000006,
}
DECK_CONFIG_ID = 1758400002000  # options preset shipped with the deck (curriculum order, 20 new/day)

DECK_ROOT = "Code de la route 2026"
DECK_IDS = {  # subdeck name -> stable id
    DECK_ROOT: 1758400001000,
    f"{DECK_ROOT}::00 Méthode d'examen": 1758400001001,
    f"{DECK_ROOT}::01 Signalisation": 1758400001002,
    f"{DECK_ROOT}::02 Circulation": 1758400001003,
    f"{DECK_ROOT}::03 Le conducteur": 1758400001004,
    f"{DECK_ROOT}::04 La route": 1758400001005,
    f"{DECK_ROOT}::05 Les autres usagers": 1758400001006,
    f"{DECK_ROOT}::06 Réglementation et notions diverses": 1758400001007,
    f"{DECK_ROOT}::07 Premiers secours": 1758400001008,
    f"{DECK_ROOT}::08 Prendre et quitter son véhicule": 1758400001009,
    f"{DECK_ROOT}::09 Mécanique et équipements": 1758400001010,
    f"{DECK_ROOT}::10 Sécurité du passager et du véhicule": 1758400001011,
    f"{DECK_ROOT}::11 Environnement": 1758400001012,
}

THEME_NAMES = {
    "X": "Méthode d'examen",
    "L": "La circulation routière",
    "C": "Le conducteur",
    "R": "La route",
    "U": "Les autres usagers",
    "D": "Les notions diverses",
    "A": "Les premiers secours",
    "P": "Prendre et quitter son véhicule",
    "M": "La mécanique et les équipements",
    "S": "La sécurité du passager et du véhicule",
    "E": "L'environnement",
}

# Sub-themes of L that belong to the "Signalisation" subdeck; every other L sub-theme goes to "Circulation".
SIGNALISATION_SUBTHEMES = {"panneaux", "panonceaux", "balises", "marquages", "feux", "agents", "signalisation"}


def deck_for(theme: str, sous_theme: str) -> str:
    if theme == "X":
        return f"{DECK_ROOT}::00 Méthode d'examen"
    if theme == "L":
        if sous_theme in SIGNALISATION_SUBTHEMES:
            return f"{DECK_ROOT}::01 Signalisation"
        return f"{DECK_ROOT}::02 Circulation"
    return {
        "C": f"{DECK_ROOT}::03 Le conducteur",
        "R": f"{DECK_ROOT}::04 La route",
        "U": f"{DECK_ROOT}::05 Les autres usagers",
        "D": f"{DECK_ROOT}::06 Réglementation et notions diverses",
        "A": f"{DECK_ROOT}::07 Premiers secours",
        "P": f"{DECK_ROOT}::08 Prendre et quitter son véhicule",
        "M": f"{DECK_ROOT}::09 Mécanique et équipements",
        "S": f"{DECK_ROOT}::10 Sécurité du passager et du véhicule",
        "E": f"{DECK_ROOT}::11 Environnement",
    }[theme]


CSS = """
.card {
  font-family: -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-size: 20px; line-height: 1.4; text-align: center;
  color: #1c1c1c; background: #f7f7f5; padding: 14px 12px 24px;
}
.card.nightMode, .nightMode .card, .night_mode .card { color: #ececec; background: #1f1f1f; }
.cdr-wrap { max-width: 680px; margin: 0 auto; }
.cdr-kicker { font-size: 12px; letter-spacing: .12em; text-transform: uppercase; color: #8a8a8a; margin-bottom: 10px; }
.cdr-img { margin: 6px auto 10px; }
.cdr-img img { max-width: 100%; max-height: 46vh; width: auto; height: auto; border-radius: 10px; }
.cdr-img.sign img { max-height: 40vh; max-width: min(100%, 320px); }
.cdr-pair { display: flex; gap: 18px; justify-content: center; align-items: flex-start; flex-wrap: wrap; }
.cdr-pair > div { flex: 1 1 200px; max-width: 280px; }
.cdr-pair img { max-width: 100%; max-height: 32vh; border-radius: 10px; }
.cdr-pair .lbl { font-size: 17px; font-weight: 700; margin-top: 8px; color: #1a6b3a; }
.nightMode .cdr-pair .lbl, .night_mode .cdr-pair .lbl { color: #7ed49a; }
.cdr-q { font-size: 22px; font-weight: 600; margin: 10px 0 6px; }
.cdr-hint { font-size: 15px; color: #8a8a8a; margin-top: 4px; }
.cdr-a { font-size: 23px; font-weight: 700; color: #1a6b3a; margin: 12px 0 6px; }
.nightMode .cdr-a, .night_mode .cdr-a { color: #7ed49a; }
.cdr-sig { font-size: 19px; margin: 4px auto 10px; max-width: 620px; }
.cdr-box { font-size: 17px; text-align: left; margin: 10px auto; max-width: 620px;
  background: #ffffff; border-left: 4px solid #2d6fd8; padding: 8px 12px; border-radius: 6px; }
.nightMode .cdr-box, .night_mode .cdr-box { background: #2a2a2a; }
.cdr-box.conduite { border-left-color: #1a6b3a; }
.cdr-box.piege { border-left-color: #d8362d; background: #fff5f4; }
.nightMode .cdr-box.piege, .night_mode .cdr-box.piege { background: #332424; }
.cdr-box.info { border-left-color: #8a8a8a; color: #444; font-size: 16px; }
.nightMode .cdr-box.info, .night_mode .cdr-box.info { color: #cfcfcf; }
.cdr-box b { font-weight: 700; }
.cdr-src { font-size: 12px; color: #a0a0a0; margin-top: 18px; overflow-wrap: anywhere; }
.cdr-code { font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13px; color: #a0a0a0; }
.cloze { color: #1a6b3a; font-weight: 700; }
.nightMode .cloze, .night_mode .cloze { color: #7ed49a; }
.cdr-fait { font-size: 22px; max-width: 640px; margin: 8px auto; text-align: left; }
.cdr-fait.center { text-align: center; }
hr#answer { border: 0; border-top: 1px solid #d0d0d0; margin: 14px 0; }
ul.cdr-list { text-align: left; display: inline-block; margin: 6px auto; padding-left: 22px; }
.cdr-ctx { font-size: 17px; color: #555; margin: 6px auto 4px; max-width: 620px; }
.nightMode .cdr-ctx, .night_mode .cdr-ctx { color: #bdbdbd; }
.cdr-aff { font-size: 22px; font-weight: 600; margin: 8px auto 4px; max-width: 640px; }
.cdr-aff::before { content: "«\\00a0"; color: #8a8a8a; } .cdr-aff::after { content: "\\00a0»"; color: #8a8a8a; }
.cdr-verdict { display: inline-block; font-size: 20px; font-weight: 800; letter-spacing: .08em; padding: 4px 18px; text-transform: uppercase;
  border-radius: 999px; margin: 10px 0 8px; color: #fff; background: #1a6b3a; }
.cdr-verdict.faux { background: #d8362d; }
"""

KICKER = '<div class="cdr-kicker">{{Theme}}{{#SousTheme}} · {{SousTheme}}{{/SousTheme}}</div>'
FRONT_KICKER = '<div class="cdr-kicker">Code de la route · Rappel actif</div>'
GRADE = ('<div class="cdr-hint">À revoir si la décision ou la raison essentielle manquait. '
         'Les détails de l’explication ne sont pas à réciter.</div>')
SRC = '<div class="cdr-src">{{#Code}}<span class="cdr-code">{{Code}}</span> · {{/Code}}{{Source}}</div>'


def notetypes() -> list[dict]:
    """Return the note type definitions as plain dicts consumed by build.py."""
    return [
        {
            "name": "CDR Reconnaissance",
            "fields": ["Id", "Type", "Image", "Question", "Nom", "Signification", "ConduiteATenir", "Complement", "Piege", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Reconnaissance",
                "qfmt": f'<div class="cdr-wrap">{FRONT_KICKER}<div class="cdr-img sign">{{{{Image}}}}</div><div class="cdr-q">{{{{Question}}}}</div><div class="cdr-hint">Donnez le sens ; le nom officiel n’est pas à réciter.</div></div>',
                "afmt": (
                    '<div class="cdr-wrap">' + KICKER + '<div class="cdr-img sign">{{Image}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-a">{{Signification}}</div>'
                    '<div class="cdr-hint">{{Nom}}</div>'
                    '{{#ConduiteATenir}}<div class="cdr-box conduite"><b>Conduite à tenir :</b> {{ConduiteATenir}}</div>{{/ConduiteATenir}}'
                    '{{#Complement}}<div class="cdr-box info">{{Complement}}</div>{{/Complement}}'
                    '{{#Piege}}<div class="cdr-box piege"><b>Piège :</b> {{Piege}}</div>{{/Piege}}'
                    + '<div class="cdr-hint">À revoir si le sens était faux ou incomplet. Les encadrés expliquent la conduite.</div>' + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Confusion",
            "fields": ["Id", "ImageA", "ImageB", "NomA", "NomB", "Difference", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Confusion",
                "qfmt": (
                    '<div class="cdr-wrap">' + FRONT_KICKER +
                    '<div class="cdr-pair"><div>{{ImageA}}</div><div>{{ImageB}}</div></div>'
                    '<div class="cdr-q">Quelle est la différence ?</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap">' + KICKER +
                    '<div class="cdr-pair"><div>{{ImageA}}<div class="lbl">{{NomA}}</div></div><div>{{ImageB}}<div class="lbl">{{NomB}}</div></div></div>'
                    '<hr id=answer>'
                    '<div class="cdr-box">{{Difference}}</div>'
                    + GRADE + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Fait",
            "cloze": True,
            "fields": ["Id", "Texte", "Explication", "Image", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Cloze",
                "qfmt": (
                    '<div class="cdr-wrap">' + FRONT_KICKER +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '<div class="cdr-fait">{{cloze:Texte}}</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap">' + KICKER +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '<div class="cdr-fait">{{cloze:Texte}}</div>'
                    '{{#Explication}}<div class="cdr-box">{{Explication}}</div>{{/Explication}}'
                    + '<div class="cdr-hint">À revoir si la valeur ou le terme demandé manquait. Vérifiez aussi l’unité.</div>' + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Question",
            "fields": ["Id", "Question", "Reponse", "Explication", "Image", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Question",
                "qfmt": (
                    '<div class="cdr-wrap">' + FRONT_KICKER +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '<div class="cdr-q">{{Question}}</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap">' + KICKER +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '<div class="cdr-q">{{Question}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-a">{{Reponse}}</div>'
                    '{{#Explication}}<div class="cdr-box">{{Explication}}</div>{{/Explication}}'
                    + GRADE + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Scenario",
            "fields": ["Id", "Image", "Question", "Reponse", "Explication", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Scenario",
                "qfmt": (
                    '<div class="cdr-wrap">' + FRONT_KICKER +
                    '<div class="cdr-img">{{Image}}</div>'
                    '<div class="cdr-q">{{Question}}</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap">' + KICKER +
                    '<div class="cdr-img">{{Image}}</div>'
                    '<div class="cdr-q">{{Question}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-a">{{Reponse}}</div>'
                    '{{#Explication}}<div class="cdr-box">{{Explication}}</div>{{/Explication}}'
                    + GRADE + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Affirmation",
            "fields": ["Id", "Contexte", "Affirmation", "Verdict", "Pourquoi", "Image", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Affirmation",
                "qfmt": (
                    '<div class="cdr-wrap">' + FRONT_KICKER +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '{{#Contexte}}<div class="cdr-ctx">{{Contexte}}</div>{{/Contexte}}'
                    '<div class="cdr-aff">{{Affirmation}}</div>'
                    '<div class="cdr-hint">Vrai ou faux ? Justifiez ; si faux, corrigez la proposition.</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap">' + KICKER +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '{{#Contexte}}<div class="cdr-ctx">{{Contexte}}</div>{{/Contexte}}'
                    '<div class="cdr-aff">{{Affirmation}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-verdict {{Verdict}}">{{Verdict}}</div>'
                    '<div class="cdr-box">{{Pourquoi}}</div>'
                    + GRADE + SRC + '</div>'
                ),
            }],
        },
    ]


DECK_DESCRIPTIONS = {
    "00 Méthode d'examen": "Lire une question de l'ETG sans tomber dans les pièges : bandeau « une/plusieurs réponses », pictogramme de point de vue, halo jaune, « je peux / je dois », adverbes, négations, questions vidéo. 40 questions, 35 bonnes réponses exigées, ~20 s par question. À voir en premier et à revoir la veille.",
    "01 Signalisation": "Panneaux, panonceaux, balises, marquages, feux, gestes de l'agent : image → sens exact, conduite à tenir, piège. Les signaux essentiels arrivent en premier ; « Parcourir → tag:importance::rare → Suspendre » si vous manquez de temps. Les cartes « Quelle est la différence ? » ciblent les paires confondues.",
    "02 Circulation": "Priorités (avec scénarios vérifiés), vitesses, positionnement, dépassement, croisement, arrêt et stationnement, feux. Relier les règles aux indices de chaque situation.",
    "03 Le conducteur": "Un quart des questions de l'examen : distances (réaction, freinage, arrêt, sécurité), perception, vigilance et anticipation, alcool, stupéfiants, médicaments, fatigue, téléphone. Beaucoup de cartes « Vrai ou faux ? » : l'épreuve juge des affirmations sur le risque, pas des articles de loi.",
    "04 La route": "Nuit, pluie, brouillard, neige, tunnels, passages à niveau, tramways, chantiers, autoroute, montagne.",
    "05 Les autres usagers": "Piétons, cyclistes, trottinettes, motos (inter-files 2025), poids lourds, bus et tramways, véhicules prioritaires et facilités de passage.",
    "06 Réglementation et notions diverses": "Permis à points et probatoire, classes d'amendes et barème des retraits, délits (valeurs 2025-2026, anciennes valeurs signalées), documents, assurance, contrôle technique, Crit'Air/ZFE, équipements.",
    "07 Premiers secours": "Protéger, alerter, secourir : une question à l'examen, toujours sur ce socle. Numéros d'urgence, PLS, RCP, DAE, obligations après un accident.",
    "08 Prendre et quitter son véhicule": "Vérifications, installation au poste de conduite (siège, appuie-tête, rétroviseurs, ceinture), quitter le véhicule (portière, pente, enfants).",
    "09 Mécanique et équipements": "Voyants du tableau de bord (symboles ISO en couleur réelle), pneus, niveaux, freinage, feux, aides à la conduite, dépannage.",
    "10 Sécurité du passager et du véhicule": "Ceinture, airbags, enfants (sièges, place avant), chargement et remorque, sécurité active/passive, ADAS.",
    "11 Environnement": "Écoconduite (gestes et chiffres), pollution et Crit'Air, pics de pollution, bruit, écomobilité, énergies.",
}
