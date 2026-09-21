"""Editorial objectives, foundation selection and an exact card-level programme."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import re

import yaml

OBJECTIVES = Path(__file__).resolve().parents[1] / "data/_meta/objectives.yaml"
CLOZES = re.compile(r"\{\{c(\d+)::")


def objectives():
    return yaml.safe_load(OBJECTIVES.read_text(encoding="utf-8"))


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


def write_reports(data, note_order, out, per_day=20):
    by_id = {n["id"]: n for notes in data.values() for n in notes}
    plan = card_plan(data, note_order)
    core = sum(1 for _, ident, _ in plan if by_id[ident]["_stage"] == "socle")
    lines = ["# Programme calculé depuis les positions des cartes\n",
             f"{len(plan)} cartes au total ; **{core} cartes de socle** avant l'approfondissement.\n",
             f"À {per_day} nouvelles cartes/jour : socle en au moins {-(-core // per_day)} jours "
             f"d'introduction ; totalité en au moins {-(-len(plan) // per_day)} jours.\n",
             "Ces durées ne prédisent ni la maîtrise ni la charge de révision. L'enfouissement des cartes "
             "sœurs, les limites quotidiennes et les jours sans étude peuvent les allonger.\n",
             "Les thèmes sont entrelacés. Une carte sœur reçoit une position distincte ; toutes les "
             "cartes du socle passent avant l'approfondissement. Le tableau utilise exactement le plan exporté.\n",
             "| Semaine | Positions | Socle / approfondissement | Cartes par thème |",
             "|---|---|---|---|"]
    for start in range(0, len(plan), per_day * 7):
        chunk = plan[start:start + per_day * 7]
        mix = Counter(by_id[i]["theme"] for _, i, _ in chunk)
        stages = Counter(by_id[i]["_stage"] for _, i, _ in chunk)
        lines.append(f"| {start // (per_day * 7) + 1} | {start + 1}–{start + len(chunk)} | "
                     f"{stages['socle']} / {stages['approfondissement']} | " +
                     ", ".join(f"{t} {c}" for t, c in sorted(mix.items())) + " |")
    (out / "PROGRAMME.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    coverage = ["# Couverture de tout le deck\n",
                "Sélection éditoriale, pas garantie de couvrir la banque confidentielle de l'ETG. "
                "Chaque note du paquet complet est reliée à au moins un objectif explicite. "
                "Socle et consolidation sont des étapes d'apprentissage, pas deux niveaux de qualité. "
                "Aucun plafond de notes ou de cartes.\n"]
    for obj in objectives():
        notes = [n for n in by_id.values() if obj["id"] in n["_objectives"]]
        coverage.extend([f"## {obj['id']} — {obj['titre']}\n", obj["raison"] + "\n",
                         f"{len(notes)} notes / {sum(card_count(n) for n in notes)} cartes.\n",
                         "Recherche Anki : `objectif::" + obj["id"] + "`\n",
                         "| Note | Étape | Exercice | Source |", "|---|---|---|---|"])
        for n in notes:
            source = str(n["source"]).replace("|", "/").replace("\n", " ")
            coverage.append(f"| `{n['id']}` | {n['_stage']} | {n['_kind']} | {source} |")
        coverage.append("")
    (out / "COUVERTURE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")
    write_card_inventory(data, plan, out)
    decisions = yaml.safe_load(OBJECTIVES.with_name('sign_exclusions.yaml').read_text(encoding='utf-8'))
    selection = ['# Choix de représentation des signaux\n',
                 'Pas de filtre par rareté ni de plafond. Ces entrées de l’inventaire ne produisent pas '
                 'une carte de reconnaissance distincte pour les raisons ci-dessous. Une couverture '
                 'textuelle entraîne la règle, pas la reconnaissance visuelle de toutes ses variantes.\n',
                 '| Entrées | Raison | Cartes correspondantes |', '|---|---|---|']
    for d in decisions:
        selection.append('| ' + ', '.join(d['codes']) + ' | ' + d['raison'] + ' | ' +
                         ', '.join('`' + i + '`' for i in d['couverts_par']) + ' |')
    (out / 'SELECTION-SIGNAUX.md').write_text('\n'.join(selection) + '\n', encoding='utf-8')


def write_card_inventory(data, plan, out):
    """Expose every retrieval target, including every sibling of a cloze note.

    This is an inspection aid, not a claim that a tag proves educational quality.
    """
    by_id = {n['id']: n for ns in data.values() for n in ns}
    rows = ['# Rôle et cible de chaque carte\n',
            'Inventaire généré depuis les notes livrées, dans leur ordre d’introduction. '
            'Le rôle dépend du type ; la cible est le contenu effectivement demandé. '
            'Les objectifs renvoient aux raisons éditoriales de COUVERTURE.md. '
            'Cet inventaire ne remplace pas la lecture critique des rectos et versos.\n',
            '| Position | Note / carte | Objectifs | Travail demandé | Cible de rappel |',
            '|---|---|---|---|---|']
    roles = {'reconnaissance': 'Reconnaître le signal', 'confusions': 'Discriminer deux signaux',
             'faits': 'Rappeler une valeur ou notion', 'questions': 'Répondre à la question',
             'affirmations': 'Juger et justifier ; corriger si faux', 'scenarios': 'Lire la scène et décider'}
    for pos, (kind, ident, ordinal) in enumerate(plan, 1):
        n = by_id[ident]
        if kind == 'faits':
            target = ' / '.join(re.findall(r'\{\{c' + str(ordinal + 1) + r'::(.*?)(?:::.*?)?\}\}', n['texte']))
        else:
            field = {'reconnaissance': 'signification', 'confusions': 'difference',
                     'questions': 'reponse', 'affirmations': 'pourquoi', 'scenarios': 'reponse'}[kind]
            target = n[field]
        target = str(target).replace('|', '/').replace('\n', ' ')
        rows.append(f"| {pos} | `{ident}` / {ordinal + 1} | {', '.join(n['_objectives'])} | {roles[kind]} | {target} |")
    (out / 'ROLES.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
