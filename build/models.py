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
  font-family: -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 20px; line-height: 1.45; text-align: left;
  color: #202124; background: #fafaf8; padding: 18px 18px 28px;
  -webkit-text-size-adjust: 100%;
}
.card.nightMode, .nightMode .card, .night_mode .card { color: #ececec; background: #202124; }
.cdr-wrap { max-width: 640px; margin: 0 auto; overflow-wrap: anywhere; }
.cdr-img { text-align: center; margin: 0 auto 16px; }
.cdr-img img { display: inline-block; max-width: 100%; max-height: 46vh; width: auto; height: auto; border-radius: 6px; }
.cdr-img.sign img { max-height: 36vh; max-width: min(100%, 300px); }
.cdr-pair { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 16px; align-items: start; text-align: center; }
.cdr-pair > div { min-width: 0; }
.cdr-side { display: block; font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.cdr-pair img { max-width: 100%; max-height: 30vh; width: auto; height: auto; border-radius: 6px; }
.cdr-q, .cdr-aff { font-size: 22px; font-weight: 600; margin: 12px 0; }
.cdr-a { font-size: 22px; font-weight: 650; margin: 16px 0 12px; color: #176039; }
.nightMode .cdr-a, .night_mode .cdr-a { color: #91d7ad; }
.cdr-box { font-size: 18px; margin: 12px 0; }
.cdr-box.conduite { margin-top: 14px; }
.cdr-box.piege { border-left: 3px solid #b26614; padding-left: 12px; }
.nightMode .cdr-box.piege, .night_mode .cdr-box.piege { border-color: #eab777; }
.cdr-box b { font-weight: 650; }
.cdr-ctx, .cdr-hint { font-size: 18px; color: #555b61; margin: 8px 0; }
.cdr-hint { font-size: 16px; }
.nightMode .cdr-ctx, .night_mode .cdr-ctx,
.nightMode .cdr-hint, .night_mode .cdr-hint { color: #c0c3c7; }
.cdr-back .cdr-q, .cdr-back .cdr-aff { font-size: 18px; font-weight: 400; }
.cdr-aff::before { content: "«\\00a0"; }
.cdr-aff::after { content: "\\00a0»"; }
.cdr-fait { font-size: 22px; margin: 8px 0 16px; }
.cloze { color: #176039; font-weight: 700; }
.nightMode .cloze, .night_mode .cloze { color: #91d7ad; }
hr#answer { border: 0; border-top: 1px solid #d0d3d5; margin: 18px 0; }
.nightMode hr#answer, .night_mode hr#answer { border-color: #51555b; }
.cdr-verdict { font-size: 22px; font-weight: 700; margin: 14px 0 8px; text-transform: capitalize; color: #176039; }
.cdr-verdict.faux { color: #af2929; }
.nightMode .cdr-verdict, .night_mode .cdr-verdict { color: #91d7ad; }
.nightMode .cdr-verdict.faux, .night_mode .cdr-verdict.faux { color: #ffaaa5; }
.cdr-reference { margin-top: 20px; border-top: 1px solid #d0d3d5; font-size: 16px; color: #555b61; }
.cdr-reference summary { cursor: pointer; min-height: 44px; box-sizing: border-box; padding: 11px 0; }
.cdr-reference summary:focus-visible { outline: 2px solid #2867b2; outline-offset: 3px; }
.cdr-reference p { margin: 8px 0 14px; }
.cdr-reference a { color: #24559a; overflow-wrap: anywhere; }
.cdr-reference h3 { font-size: 17px; margin: 16px 0 8px; }
.cdr-code { font-family: ui-monospace, Menlo, Consolas, monospace; }
.nightMode .cdr-reference, .night_mode .cdr-reference { border-color: #51555b; color: #c0c3c7; }
.nightMode .cdr-reference a, .night_mode .cdr-reference a { color: #9bc3ff; }
ul.cdr-list { padding-left: 24px; }
@media (max-width: 350px) { .card { padding: 14px 12px 24px; } }
"""


def reference(extra=""):
    """One secondary layer; corrective feedback never lives here."""
    return ('<details class="cdr-reference"><summary>Sources et repères</summary>' + extra +
            '<p>{{#Code}}<span class="cdr-code">{{Code}}</span> · {{/Code}}{{Source}}</p>'
            '{{#Repere}}<h3>{{Theme}}</h3>{{Repere}}{{/Repere}}</details>')


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
                    '{{#Piege}}<div class="cdr-box piege">{{Piege}}</div>{{/Piege}}'
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
    for note_type in types:
        note_type['fields'].append('Repere')
    return types


DECK_DESCRIPTIONS = {
    "00 Méthode d'examen": "Lire une question de l'ETG sans tomber dans les pièges : bandeau « une/plusieurs réponses », pictogramme de point de vue, halo jaune, « je peux / je dois », adverbes, négations, questions vidéo. 40 questions, 35 bonnes réponses exigées, ~20 s par question. À voir en premier et à revoir la veille.",
    "01 Signalisation": "Panneaux, panonceaux, balises, marquages, feux, gestes de l'agent : image → sens exact, conduite à tenir, piège. Les bases précèdent les variantes ; adapter le débit des nouvelles cartes à la charge de révision. Les cartes « Quelle est la différence ? » ciblent les paires confondues.",
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
