"""Anki note types (models) for the deck: fields, card templates and CSS.

Stable ids: the backend assigns fresh ids on creation, so build.py remaps them
to these constants in SQLite before export (see build.py:remap_ids), and note
GUIDs derive from the note id. Reimporting the same edition therefore updates
notes in place instead of duplicating them.
"""

from pathlib import Path

MODEL_IDS = {
    "CDR Reconnaissance": 1758400000001,
    "CDR Confusion": 1758400000002,
    "CDR Fait": 1758400000003,
    "CDR Question": 1758400000004,
    "CDR Scenario": 1758400000005,
    "CDR Affirmation": 1758400000006,
}
DECK_CONFIG_ID = 1758400002000  # options preset shipped with the deck (curriculum order, siblings buried)

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
# sub-deck (short name) -> theme whose repère is shown on its overview screen
THEME_OF_DECK = {"00 Méthode d'examen": "X", "01 Signalisation": "L", "02 Circulation": "L", "03 Le conducteur": "C",
                 "04 La route": "R", "05 Les autres usagers": "U", "06 Réglementation et notions diverses": "D",
                 "07 Premiers secours": "A", "08 Prendre et quitter son véhicule": "P",
                 "09 Mécanique et équipements": "M", "10 Sécurité du passager et du véhicule": "S", "11 Environnement": "E"}


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


CSS = Path(__file__).with_name("cards.css").read_text(encoding="utf-8")


def reference(extra=""):
    """One collapsed layer for references (official name, code, source); corrective feedback never lives here."""
    return ('<details class="cdr-reference"><summary>Sources</summary>' + extra +
            '<p>{{#Code}}<span class="cdr-code">{{Code}}</span> · {{/Code}}{{Source}}</p></details>')


SRC = reference()

# Native Anki cloze conditionals work on both faces, without JavaScript or extra fields.
# Legacy prose is unaffected; only explicitly authored independent prompts are filtered.
CLOZE_FOCUS = ('<style>.cdr-unit { display: none; } .cdr-unit[data-cloze="' +
               ''.join('{{#c' + str(i) + '}}' + str(i) + '{{/c' + str(i) + '}}' for i in range(1, 5)) +
               '"] { display: block; }</style>')


def notetypes() -> list[dict]:
    """Return the note type definitions as plain dicts consumed by build.py."""
    types = [
        {
            "name": "CDR Reconnaissance",
            "fields": ["Id", "Type", "Image", "Question", "Nom", "Signification", "ConduiteATenir", "Complement", "Piege", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Reconnaissance",
                "qfmt": f'<div class="cdr-wrap"><div class="cdr-img sign">{{{{Image}}}}</div><div class="cdr-q">{{{{Question}}}}</div></div>',
                "afmt": (
                    '<div class="cdr-wrap cdr-back">' + '<div class="cdr-img sign">{{Image}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-a">{{Signification}}</div>'
                    '{{#ConduiteATenir}}<div class="cdr-box conduite"><b>En pratique.</b> {{ConduiteATenir}}</div>{{/ConduiteATenir}}'
                    '{{#Complement}}<div class="cdr-box info">{{Complement}}</div>{{/Complement}}'
                    '{{#Piege}}<div class="cdr-box piege"><b>Piège.</b> {{Piege}}</div>{{/Piege}}'
                    + reference('<p>{{Nom}}</p>') + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Confusion",
            "fields": ["Id", "ImageA", "ImageB", "NomA", "NomB", "Difference", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Confusion",
                "qfmt": (
                    '<div class="cdr-wrap">' +
                    '<div class="cdr-pair"><div><span class="cdr-side">A</span>{{ImageA}}</div><div><span class="cdr-side">B</span>{{ImageB}}</div></div>'
                    '<div class="cdr-q">Quelle est la différence ?</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap cdr-back">' +
                    '<div class="cdr-pair"><div><span class="cdr-side">A</span>{{ImageA}}</div><div><span class="cdr-side">B</span>{{ImageB}}</div></div>'
                    '<hr id=answer>'
                    '<div class="cdr-box cdr-difference">{{Difference}}</div>'
                    + reference('<p>A : {{NomA}}<br>B : {{NomB}}</p>') + '</div>'
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
                    '<div class="cdr-wrap">' +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    + CLOZE_FOCUS + '<div class="cdr-fait">{{cloze:Texte}}</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap cdr-back">' +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    + CLOZE_FOCUS + '<div class="cdr-fait">{{cloze:Texte}}</div>'
                    '{{#Explication}}<div class="cdr-box">{{Explication}}</div>{{/Explication}}'
                    + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Question",
            "fields": ["Id", "Question", "Reponse", "Explication", "Image", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Question",
                "qfmt": (
                    '<div class="cdr-wrap">' +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '<div class="cdr-q">{{Question}}</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap cdr-back">' +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '<div class="cdr-q">{{Question}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-a">{{Reponse}}</div>'
                    '{{#Explication}}<div class="cdr-box">{{Explication}}</div>{{/Explication}}'
                    + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Scenario",
            "fields": ["Id", "Image", "Question", "Reponse", "Explication", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Scenario",
                "qfmt": (
                    '<div class="cdr-wrap">' +
                    '<div class="cdr-img">{{Image}}</div>'
                    '<div class="cdr-q">{{Question}}</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap cdr-back">' +
                    '<div class="cdr-img">{{Image}}</div>'
                    '<div class="cdr-q">{{Question}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-a">{{Reponse}}</div>'
                    '{{#Explication}}<div class="cdr-box">{{Explication}}</div>{{/Explication}}'
                    + SRC + '</div>'
                ),
            }],
        },
        {
            "name": "CDR Affirmation",
            "fields": ["Id", "Contexte", "Affirmation", "Verdict", "Pourquoi", "Image", "Code", "Theme", "SousTheme", "Source"],
            "templates": [{
                "name": "Affirmation",
                "qfmt": (
                    '<div class="cdr-wrap">' +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '{{#Contexte}}<div class="cdr-ctx">{{Contexte}}</div>{{/Contexte}}'
                    '<div class="cdr-aff">{{Affirmation}}</div>'
                    '<div class="cdr-hint">Vrai ou faux ? Pourquoi ?</div></div>'
                ),
                "afmt": (
                    '<div class="cdr-wrap cdr-back">' +
                    '{{#Image}}<div class="cdr-img">{{Image}}</div>{{/Image}}'
                    '{{#Contexte}}<div class="cdr-ctx">{{Contexte}}</div>{{/Contexte}}'
                    '<div class="cdr-aff">{{Affirmation}}</div>'
                    '<hr id=answer>'
                    '<div class="cdr-verdict {{Verdict}}">{{Verdict}}</div>'
                    '<div class="cdr-box">{{Pourquoi}}</div>'
                    + SRC + '</div>'
                ),
            }],
        },
    ]
    return types


DECK_DESCRIPTIONS = {
    "00 Méthode d'examen": "Lire une question de l'ETG sans tomber dans les pièges : pictogramme de point de vue, halo jaune, « je peux / je dois », double affirmation, négations, questions vidéo. 40 questions, 35 bonnes réponses exigées, une vingtaine de secondes par question.",
    "01 Signalisation": "Panneaux, panonceaux, balises, marquages, feux, gestes de l'agent : image → sens exact, conduite à tenir, piège. Les cartes « Quelle est la différence ? » ciblent les paires confondues.",
    "02 Circulation": "Priorités (avec scénarios dessinés), vitesses, positionnement, dépassement, croisement, arrêt et stationnement, feux. Relier les règles aux indices de chaque situation.",
    "03 Le conducteur": "Distances (réaction, freinage, arrêt, sécurité), perception, vigilance et anticipation, alcool, stupéfiants, médicaments, fatigue, téléphone. Relier les règles aux indices ; justifier les réponses aux affirmations.",
    "04 La route": "Nuit, pluie, brouillard, neige, tunnels, passages à niveau, tramways, chantiers, autoroute, montagne.",
    "05 Les autres usagers": "Piétons, cyclistes, trottinettes, motos (inter-files 2025), poids lourds, bus et tramways, véhicules prioritaires et facilités de passage.",
    "06 Réglementation et notions diverses": "Permis à points et probatoire, classes d'amendes et barème des retraits, délits et conséquences, documents, assurance, contrôle technique, Crit'Air/ZFE, équipements.",
    "07 Premiers secours": "Protéger, alerter, secourir : choisir l’action selon la situation. Numéros d'urgence, PLS, RCP, DAE, obligations après un accident.",
    "08 Prendre et quitter son véhicule": "Vérifications, installation au poste de conduite (siège, appuie-tête, rétroviseurs, ceinture), quitter le véhicule (portière, pente, enfants).",
    "09 Mécanique et équipements": "Voyants du tableau de bord (symboles ISO en couleur réelle), pneus, niveaux, freinage, feux, aides à la conduite, dépannage.",
    "10 Sécurité du passager et du véhicule": "Ceinture, airbags, enfants (sièges, place avant), chargement et remorque, sécurité active/passive, ADAS.",
    "11 Environnement": "Écoconduite (gestes et chiffres), pollution et Crit'Air, pics de pollution, bruit, écomobilité, énergies.",
}
