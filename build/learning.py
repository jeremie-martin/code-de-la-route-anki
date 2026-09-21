"""Editorial objectives (data/_meta/objectives.yaml), the socle/consolidation split and the card-level programme."""
from __future__ import annotations

from collections import Counter
from datetime import date
from functools import cache
from pathlib import Path
import re

import yaml

OBJECTIVES = Path(__file__).resolve().parents[1] / "data/_meta/objectives.yaml"
CLOZES = re.compile(r"\{\{c(\d+)::")


def objectives():
    return yaml.safe_load(OBJECTIVES.read_text(encoding="utf-8"))


@cache
def lessons():
    return {lesson['theme']: lesson for lesson in yaml.safe_load(
        OBJECTIVES.with_name('lessons.yaml').read_text(encoding='utf-8'))}


def annotate(data):
    """Membership is explicit, except recognition prerequisites of confusion pairs."""
    by_id = {n["id"]: n for notes in data.values() for n in notes}
    for n in by_id.values():
        n["_objectives"] = []
        n["_stage"] = "approfondissement"
    for objective in objectives():
        for stage, field in (("socle", "notes"), ("approfondissement", "consolidation")):
            for ident in objective.get(field, []):
                if ident in by_id:
                    by_id[ident]["_objectives"].append(objective["id"])
                    if stage == "socle":
                        by_id[ident]["_stage"] = stage
    for n in data["confusions"]:
        if n["_objectives"]:
            for ident in (n["a"], n["b"]):
                if ident in by_id:
                    by_id[ident]["_objectives"].extend(n["_objectives"])
                    if n["_stage"] == "socle":
                        by_id[ident]["_stage"] = "socle"
    for n in by_id.values():
        n["_objectives"] = sorted(set(n["_objectives"]))


def card_count(note):
    return len(set(CLOZES.findall(note.get("texte", "")))) if note["_kind"] == "faits" else 1


def validate_objectives(data):
    by_id = {n["id"]: n for notes in data.values() for n in notes}
    errors, seen, assigned = [], set(), set()
    for obj in objectives():
        if obj["id"] in seen:
            errors.append(f"objectif dupliqué : {obj['id']}")
        seen.add(obj["id"])
        members = obj.get("notes", []) + obj.get("consolidation", [])
        assigned.update(members)
        if len(members) != len(set(members)):
            errors.append(f"objectif {obj['id']} : note répétée dans les étapes")
        for ident in members:
            if ident not in by_id:
                errors.append(f"objectif {obj['id']} : note inconnue {ident}")
        if not obj.get("raison") or not members:
            errors.append(f"objectif {obj['id']} : justification ou notes absentes")
    for n in by_id.values():
        if n['id'] not in assigned:
            errors.append(f"note sans objectif pédagogique : {n['id']}")
        if n.get('image_ref') in by_id and n['_stage'] == 'socle' and by_id[n['image_ref']]['_stage'] != 'socle':
            errors.append(f"{n['id']} : reconnaissance préalable hors socle")
    decisions = yaml.safe_load(OBJECTIVES.with_name('sign_exclusions.yaml').read_text(encoding='utf-8'))
    for decision in decisions:
        if not decision.get('raison'):
            errors.append('exclusion de signal sans justification')
        for ident in decision['couverts_par']:
            if ident not in by_id:
                errors.append(f"couverture d'un signal exclu : note inconnue {ident}")
    themes = {n["theme"] for n in by_id.values() if n["_stage"] == "socle"}
    if themes != set("XLCRUDAPMSE"):
        errors.append(f"socle : thèmes manquants {set('XLCRUDAPMSE') - themes}")
    checks = yaml.safe_load(OBJECTIVES.with_name('source_checks.yaml').read_text(encoding='utf-8'))
    if set(lessons()) != set('XLCRUDAPMSE'):
        errors.append('repères : chaque thème doit avoir une introduction')
    for lesson in lessons().values():
        if not all(lesson.get(f) for f in ('titre', 'principe', 'exemple', 'transfert')):
            errors.append(f"repère {lesson['theme']} incomplet")
    for check in checks:
        try:
            date.fromisoformat(check['consulte_le'])
        except (ValueError, TypeError):
            errors.append(f"source {check['id']} : date de consultation invalide")
        if not check.get('portee') or not check.get('url', '').startswith('https://'):
            errors.append(f"source {check['id']} : portée ou lien manquant")
        for ident in check['notes']:
            if ident not in by_id:
                errors.append(f"source {check['id']} : note inconnue {ident}")
    return errors


def card_plan(data, note_order, sibling_gap=30):
    """Unique positions, separated siblings, and no leakage across learning stages.

    This same plan drives the exported positions and the programme report. The
    integer ord is Anki's template/cloze ordinal, not the order returned by SQL.
    """
    by_key = {(kind, n["id"]): n for kind, notes in data.items() for n in notes}
    plan = []
    for stage in ("socle", "approfondissement"):
        notes = [key for key in note_order if by_key[key]["_stage"] == stage]
        pending = []
        for index, key in enumerate(notes):
            n = by_key[key]
            ords = sorted({int(x) - 1 for x in CLOZES.findall(n["texte"])}) if key[0] == "faits" else [0]
            for ordinal in ords:
                pending.append((index + ordinal * sibling_gap, index, ordinal, *key))
        pending.sort()
        plan.extend((kind, ident, ordinal) for _, _, ordinal, kind, ident in pending)
    return plan


def write_reports(data, note_order, out):
    by_id = {n["id"]: n for notes in data.values() for n in notes}
    plan = card_plan(data, note_order)
    core = sum(1 for _, ident, _ in plan if by_id[ident]["_stage"] == "socle")
    lines = ["# Ordre d'introduction des cartes\n",
             f"{len(plan)} cartes ; les **{core} cartes du socle** (positions 1 à {core}) précèdent la consolidation. "
             "Cet ordre est celui du paquet : nouvelles cartes collectées par position la plus basse (préréglage fourni). "
             "Les thèmes sont entrelacés ; une carte sœur d'un même fait reçoit une position plus lointaine.\n",
             "| Position | Carte | Thème | Forme | Étape |", "|---|---|---|---|---|"]
    for pos, (kind, ident, ordinal) in enumerate(plan, 1):
        n = by_id[ident]
        card = f"`{ident}`" + (f" ({ordinal + 1})" if kind == "faits" else "")
        lines.append(f"| {pos} | {card} | {n['theme']} · {n['sous_theme']} | {kind} | {n['_stage']} |")
    (out / "PROGRAMME.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    coverage = ["# Couverture : objectifs et notes\n",
                "Chaque note est reliée à au moins un objectif. La recherche Anki `objectif::…` retrouve les cartes "
                "d'un objectif après une erreur en série. Sélection éditoriale : elle ne garantit pas de couvrir la "
                "banque confidentielle de l'ETG.\n"]
    for obj in objectives():
        notes = [n for n in by_id.values() if obj["id"] in n["_objectives"]]
        coverage.extend([f"## {obj['id']} — {obj['titre']}\n", obj["raison"] + "\n",
                         f"{len(notes)} notes / {sum(card_count(n) for n in notes)} cartes.\n",
                         "Recherche Anki : `objectif::" + obj["id"] + "`\n",
                         "| Note | Étape | Forme | Source |", "|---|---|---|---|"])
        for n in notes:
            source = str(n["source"]).replace("|", "/").replace("\n", " ")
            coverage.append(f"| `{n['id']}` | {n['_stage']} | {n['_kind']} | {source} |")
        coverage.append("")
    (out / "COUVERTURE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")
    guide = ['# Repères par thème\n',
             'Un repère par thème : le principe, un exemple expliqué et une piste de transfert. Ils sont aussi affichés '
             'sur l’écran de chaque sous-deck dans Anki. Ils donnent un cadre de raisonnement ; les cartes et leurs '
             'sources précisent les règles et leurs exceptions.\n']
    for lesson in lessons().values():
        guide.extend([f"## {lesson['theme']} — {lesson['titre']}\n", lesson['principe'] + '\n',
                      '**Exemple.** ' + lesson['exemple'] + '\n', '**Transfert.** ' + lesson['transfert'] + '\n'])
    (out / 'REPERES.md').write_text('\n'.join(guide) + '\n', encoding='utf-8')
    decisions = yaml.safe_load(OBJECTIVES.with_name('sign_exclusions.yaml').read_text(encoding='utf-8'))
    selection = ['# Signaux sans carte de reconnaissance\n',
                 'Un signal a sa carte s’il porte une décision de conduite ou une discrimination que l’épreuve peut '
                 'demander. Chaque entrée de l’inventaire sans carte distincte est listée ici avec sa raison et les '
                 'cartes qui couvrent la règle.\n',
                 '| Entrées | Raison | Cartes correspondantes |', '|---|---|---|']
    for d in decisions:
        selection.append('| ' + ', '.join(d['codes']) + ' | ' + d['raison'] + ' | ' +
                         ', '.join('`' + i + '`' for i in d['couverts_par']) + ' |')
    (out / 'SELECTION-SIGNAUX.md').write_text('\n'.join(selection) + '\n', encoding='utf-8')
