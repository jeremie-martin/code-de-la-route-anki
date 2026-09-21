"""Build the Anki package from the YAML knowledge library.

Usage:
    .venv/bin/python -m build.build            # full build -> out/Code-de-la-route-2026.apkg
    .venv/bin/python -m build.build --check    # validate data only
    .venv/bin/python -m build.build --media    # (re)generate media only

Pipeline: load YAML -> validate -> generate media -> build collection with the
official `anki` library -> remap notetype/deck ids to stable constants ->
export legacy-compatible .apkg -> write out/STATS.md.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import re
import shutil
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import yaml

from build import models as M
from build.commons_fetch import fetch, raster, raster_tinted
from build import gen_images
from build.diagrams import SIGN_FILES, draw_intersection, draw_roundabout, draw_road, render_png
from build.priority import solve, passes_before
from build import learning

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "out"
MEDIA = OUT / "media"
BUILD_DIR = OUT / "_build"

THEMES = set(M.THEME_NAMES)
IMPORTANCE = {"essentiel", "utile", "rare"}
KINDS = ["reconnaissance", "confusions", "faits", "questions", "affirmations", "scenarios"]
# Card-quality limits (see docs/05-audit-v2.md §2.1, §2.3): a card that needs more words than this is a
# sheet, not a card, and must be split. `long_ok: true` on a note documents a deliberate exception.
MAX_ANSWER_WORDS = 30        # questions.reponse (v7 : décision + raison décisive ; viser 10-22 mots)
MAX_ANSWER_ITEMS = 4         # enumerated elements in questions.reponse
MAX_AFFIRMATION_WORDS = 32   # affirmations.affirmation
MAX_POURQUOI_WORDS = 45      # affirmations.pourquoi
MAX_RECON_BACK_WORDS = 90    # signification + conduite + complement + piege
MAX_CLOZE_WORDS = 8          # hidden text of one cloze; longer = recitation, not recall
AFF_BALANCE = (0.35, 0.65)   # share of 'vrai' per affirmations file
TYPE_QUESTION = {
    "panneau": "Que signifie ce panneau ?",
    "panonceau": "Que signifie ce panonceau ?",
    "balise": "Que signifie cette balise ?",
    "marquage": "Que signifie ce marquage ?",
    "feu": "Que signifie ce feu ?",
    "geste": "Que signifie ce geste de l'agent ?",
    "voyant": "Que signale ce voyant ?",
    "pictogramme": "Que signifie ce pictogramme ?",
    "equipement": "Qu'est-ce que c'est ?",
}


class DataError(Exception):
    pass


# ------------------------------------------------------------------ load ---
# Pedagogical order of the recognition files inside the "signalisation" track of the curriculum
# (see curriculum()): priority signs early because the priority scenarios depend on them, lights and
# markings before the overtaking scenarios, agents (autres) with the lights.
RECON_ORDER = ["panneaux_danger", "panneaux_priorite", "panneaux_interdiction", "panneaux_obligation", "panneaux_fin",
               "panneaux_zones", "feux", "autres", "marquages", "panneaux_indication", "panneaux_localisation",
               "panonceaux", "passage_a_niveau", "temporaire", "balises", "panneaux_direction", "voies_reservees",
               "panneaux_services", "voyants"]
IMPORTANCE_RANK = {"essentiel": 0, "utile": 1, "rare": 2}


def load_all() -> dict[str, list[dict]]:
    """Load every YAML file; file order is preserved (the curriculum decides the study order)."""
    data = {k: [] for k in KINDS}
    for kind in KINDS:
        d = DATA / kind
        files = sorted(d.glob("*.yaml")) if d.exists() else []
        if kind == "reconnaissance":
            files.sort(key=lambda f: (RECON_ORDER.index(f.stem) if f.stem in RECON_ORDER else 99, f.stem))
        for f in files:
            items = yaml.safe_load(f.read_text(encoding="utf-8")) or []
            if not isinstance(items, list):
                raise DataError(f"{f}: expected a list")
            for i, it in enumerate(items):
                if not isinstance(it, dict):
                    raise DataError(f"{f}: entrée non structurée {it!r}")
                it["_file"] = f.name
                it["_pos"] = i
                it["_kind"] = kind
                if kind == "faits" and "rappels" in it:
                    if "texte" in it or not isinstance(it["rappels"], list) or not all(isinstance(s, str) for s in it["rappels"]):
                        raise DataError(f"{f}:{it.get('id')}: rappels doit être une liste de textes, sans texte concurrent")
                    it["texte"] = "\n\n".join(it["rappels"])
            data[kind].extend(items)
    recon = {n['id']: n for n in data['reconnaissance']}
    for kind, notes in data.items():
        for n in notes:
            if 'image_ref' in n:
                if kind != 'questions' or n['image_ref'] not in recon or 'image' in n:
                    raise DataError(f"{n['id']}: image_ref doit référencer une reconnaissance, sans image concurrente")
                n['image'] = recon[n['image_ref']]['image']
    learning.annotate(data)
    return data


def words(s) -> int:
    return len(str(s or "").split())


def items_in(s) -> int:
    """Rough count of enumerated elements in an answer (separated by ' ; ' or by commas)."""
    s = str(s or "")
    return max(s.count(" ; ") + 1, s.count(", ") + 1)


def norm_text(s) -> str:
    s = str(s or "").lower()
    s = re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", s)
    return re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]+", " ", s).strip()


# -------------------------------------------------------------- validate ---
CLOZE_RE = re.compile(r"\{\{c(\d+)::")
IMAGE_KEYS = {"commons", "gen", "file"}
PAIR_RESULTS = {"avant", "apres", "independant", "indetermine"}


def validate(data: dict[str, list[dict]]) -> list[str]:
    errors: list[str] = []
    ids = Counter()
    recon_by_id = {}

    def req(it, *fields):
        for f in fields:
            if not str(it.get(f, "")).strip():
                errors.append(f"{it.get('_file')}:{it.get('id')}: champ manquant '{f}'")

    def common(it, kind):
        ids[it.get("id")] += 1
        req(it, "id", "theme", "sous_theme", "source")
        if it.get("theme") not in THEMES:
            errors.append(f"{it.get('_file')}:{it.get('id')}: thème inconnu {it.get('theme')}")
        if it.get("importance", "essentiel") not in IMPORTANCE:
            errors.append(f"{it.get('_file')}:{it.get('id')}: importance inconnue {it.get('importance')}")
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-_.]*", str(it.get("id", ""))):
            errors.append(f"{it.get('_file')}:{it.get('id')}: id invalide (minuscules, chiffres, tirets)")
        img = it.get("image")
        if img is not None:
            if not isinstance(img, dict) or len(IMAGE_KEYS & set(img)) != 1:
                errors.append(f"{it.get('_file')}:{it.get('id')}: image doit être un dict avec une seule clé parmi {sorted(IMAGE_KEYS)}")
            elif "gen" in img and img["gen"] not in gen_images.REGISTRY:
                errors.append(f"{it.get('_file')}:{it.get('id')}: générateur inconnu {img['gen']}")

    for it in data["reconnaissance"]:
        common(it, "reconnaissance")
        req(it, "type", "image", "nom", "signification")
        if it.get("type") not in TYPE_QUESTION:
            errors.append(f"{it['_file']}:{it.get('id')}: type inconnu {it.get('type')}")
        back = sum(words(it.get(k)) for k in ("signification", "conduite", "complement", "piege"))
        if back > MAX_RECON_BACK_WORDS and not it.get("long_ok"):
            errors.append(f"{it['_file']}:{it.get('id')}: verso trop long ({back} mots > {MAX_RECON_BACK_WORDS}) — resserrer via data/_meta/sign_overrides.yaml")
        recon_by_id[it.get("id")] = it
    for it in data["confusions"]:
        common(it, "confusions")
        req(it, "a", "b", "difference")
        for k in ("a", "b"):
            if it.get(k) not in recon_by_id:
                errors.append(f"{it['_file']}:{it.get('id')}: référence inconnue {k}={it.get(k)}")
        if it.get("a") == it.get("b"):
            errors.append(f"{it['_file']}:{it.get('id')}: a et b identiques")
    for it in data["faits"]:
        common(it, "faits")
        req(it, "texte")
        if "rappels" in it:
            ordinals = [set(CLOZE_RE.findall(s)) for s in it["rappels"]]
            if any(len(nums) != 1 for nums in ordinals) or len(set.union(set(), *ordinals)) != len(ordinals):
                errors.append(f"{it['id']}: chaque rappel doit cibler un seul numéro de cloze distinct")
        n = sorted({int(x) for x in CLOZE_RE.findall(it.get("texte", ""))})
        if not n:
            errors.append(f"{it['_file']}:{it.get('id')}: aucun cloze")
        elif n != list(range(1, len(n) + 1)):
            errors.append(f"{it['_file']}:{it.get('id')}: numérotation des clozes non contiguë {n}")
        elif len(n) > 4:
            errors.append(f"{it['_file']}:{it.get('id')}: plus de 4 clozes ({len(n)})")
        elif len(n) > 1 and "rappels" not in it and not it.get("multi_ok"):
            # v6: several targets in one sentence make a sheet, not a card; each target gets its own prompt
            errors.append(f"{it['_file']}:{it.get('id')}: {len(n)} clozes dans une même phrase — utiliser rappels (ou multi_ok: true pour une relation unique)")
        for _, ans in re.findall(r"\{\{c(\d+)::(.*?)(?:::.*?)?\}\}", it.get("texte", "")):
            if words(ans) > MAX_CLOZE_WORDS and not it.get("long_ok"):
                errors.append(f"{it['_file']}:{it.get('id')}: trou de {words(ans)} mots (> {MAX_CLOZE_WORDS}) — une phrase à réciter n'est pas une cible de rappel ; préférer une question")
        # two clozes with the same answer under different numbers: one gives the other away
        answers = {}
        for num, ans in re.findall(r"\{\{c(\d+)::(.*?)(?:::.*?)?\}\}", it.get("texte", "")):
            key = norm_text(ans)
            if key in answers and answers[key] != num:
                errors.append(f"{it['_file']}:{it.get('id')}: la réponse « {ans} » apparaît sous c{answers[key]} et c{num} (utiliser le même numéro)")
            answers.setdefault(key, num)
    seen_answers: dict[str, str] = {}
    for it in data["questions"]:
        common(it, "questions")
        req(it, "question", "reponse")
        if not it.get("long_ok"):
            w, k = words(it.get("reponse")), items_in(it.get("reponse"))
            if w > MAX_ANSWER_WORDS:
                errors.append(f"{it['_file']}:{it.get('id')}: réponse trop longue ({w} mots > {MAX_ANSWER_WORDS}) — découper en cartes de décision / affirmations")
            elif k > MAX_ANSWER_ITEMS:
                errors.append(f"{it['_file']}:{it.get('id')}: réponse énumérative ({k} éléments > {MAX_ANSWER_ITEMS}) — une carte par élément utile à l'examen")
        key = norm_text(it.get("reponse"))
        if len(key) > 30 and key in seen_answers:
            errors.append(f"{it['_file']}:{it.get('id')}: réponse identique à {seen_answers[key]} (doublon)")
        seen_answers.setdefault(key, it.get("id"))
    per_file_verdicts: dict[str, Counter] = {}
    seen_aff: dict[str, str] = {}
    for it in data["affirmations"]:
        common(it, "affirmations")
        req(it, "affirmation", "verdict", "pourquoi")
        if it.get("verdict") not in ("vrai", "faux"):
            errors.append(f"{it['_file']}:{it.get('id')}: verdict doit être 'vrai' ou 'faux'")
        if words(it.get("affirmation")) > MAX_AFFIRMATION_WORDS:
            errors.append(f"{it['_file']}:{it.get('id')}: affirmation trop longue ({words(it.get('affirmation'))} mots > {MAX_AFFIRMATION_WORDS})")
        if words(it.get("pourquoi")) > MAX_POURQUOI_WORDS and not it.get("long_ok"):
            errors.append(f"{it['_file']}:{it.get('id')}: pourquoi trop long ({words(it.get('pourquoi'))} mots > {MAX_POURQUOI_WORDS})")
        if re.search(r"\b(toujours|jamais|obligatoirement|uniquement)\b", str(it.get("affirmation", "")), re.I) and it.get("verdict") == "faux" and not it.get("signal_ok"):
            errors.append(f"{it['_file']}:{it.get('id')}: affirmation fausse contenant un mot-signal (toujours/jamais/obligatoirement/uniquement) — reformuler ou marquer signal_ok: true si le mot est celui de l'épreuve")
        key = norm_text(it.get("affirmation"))
        if key in seen_aff:
            errors.append(f"{it['_file']}:{it.get('id')}: affirmation identique à {seen_aff[key]}")
        seen_aff.setdefault(key, it.get("id"))
        per_file_verdicts.setdefault(it["_file"], Counter())[it.get("verdict")] += 1
    for f, c in per_file_verdicts.items():
        tot = c["vrai"] + c["faux"]
        if tot >= 8 and not AFF_BALANCE[0] <= c["vrai"] / tot <= AFF_BALANCE[1]:
            errors.append(f"{f}: affirmations déséquilibrées ({c['vrai']} vrai / {c['faux']} faux) — viser 35-65 % de vrai")
    for it in data["scenarios"]:
        common(it, "scenarios")
        req(it, "question", "reponse", "explication")
        if it.get("kind") not in ("intersection", "roundabout", "road"):
            errors.append(f"{it['_file']}:{it.get('id')}: kind inconnu {it.get('kind')}")
        if not isinstance(it.get("spec"), dict):
            errors.append(f"{it['_file']}:{it.get('id')}: champ manquant 'spec'")
            continue
        chk = it.get("check")
        if chk and it.get("kind") != "intersection":
            errors.append(f"{it['_file']}:{it.get('id')}: check n'est vérifié que pour kind=intersection")
        elif chk:
            pair = chk.get("pair")
            if pair is not None and (len(pair) != 3 or pair[2] not in PAIR_RESULTS):
                errors.append(f"{it['_file']}:{it.get('id')}: check.pair doit être [a, b, {'|'.join(sorted(PAIR_RESULTS))}]")
            elif not pair and not isinstance(chk.get("order"), list):
                errors.append(f"{it['_file']}:{it.get('id')}: check doit contenir 'order' ou 'pair'")
            else:
                try:
                    _check_scenario(it)
                except AssertionError as e:
                    errors.append(f"{it['_file']}:{it.get('id')}: solveur en désaccord: {e}")
                except Exception as e:  # spec malformée (approche ou direction inconnue, ...)
                    errors.append(f"{it['_file']}:{it.get('id')}: spec invalide pour le solveur: {e!r}")
    for i, c in ids.items():
        if c > 1:
            errors.append(f"id dupliqué: {i} (x{c})")
    errors.extend(learning.validate_objectives(data))
    return errors


def _check_scenario(it: dict):
    spec = it["spec"]
    chk = it["check"]
    if "order" in chk:
        r = solve(spec)
        assert not r["cycle"], "cycle de priorité (aucun ordre total)"
        got = [g[0] if len(g) == 1 else g for g in r["order"]]
        assert got == chk["order"], f"ordre calculé {got} != attendu {chk['order']}"
    if "pair" in chk:
        a, b, exp = chk["pair"]
        got = passes_before(spec, a, b)
        assert got == exp, f"{a} vs {b}: calculé '{got}' != attendu '{exp}'"


# ----------------------------------------------------------------- media ---
def media_name(prefix: str, ident: str, ext="png") -> str:
    return f"cdr_{prefix}_{ident}.{ext}".replace(" ", "_")


def make_image(img: dict, dest: Path, w_commons: int, w_gen: int, ident: str) -> None:
    """Produce one PNG from an image spec ({commons[, tint]} | {gen[, params]} | {file})."""
    if "commons" in img:
        src = fetch(img["commons"])
        if img.get("tint"):
            raster_tinted(src, dest, img["tint"], width=img.get("width", 360))
        else:
            raster(src, dest, width=img.get("width", w_commons))
    elif "gen" in img:
        svg = gen_images.render(img["gen"], img.get("params") or {})
        render_png(svg, dest, width=img.get("width", w_gen))
    elif "file" in img:
        shutil.copy(ROOT / img["file"], dest)
    else:
        raise DataError(f"{ident}: image spec inconnue {img}")


def ensure_media(data: dict[str, list[dict]], force=False) -> dict[str, str]:
    """Generate every image; return {item id: media filename}. Idempotent (skips existing)."""
    MEDIA.mkdir(parents=True, exist_ok=True)
    names: dict[str, str] = {}
    manifest_path = MEDIA / "_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}

    # every image also depends on the code that produced it: stamp that code so edits invalidate the output
    def code_hash(*files):
        return hashlib.sha1(b"".join((ROOT / "build" / f).read_bytes() for f in files)).hexdigest()
    gen_code = code_hash("gen_images.py", "diagrams.py")      # generators and scenario diagrams
    raster_code = code_hash("commons_fetch.py")               # raster() / raster_tinted() of Commons files

    def stamp(spec) -> str:
        salt = gen_code if ("gen" in spec or "kind" in spec) else raster_code
        return hashlib.sha1((json.dumps(spec, sort_keys=True, ensure_ascii=False) + salt).encode()).hexdigest()

    def need(fname, spec):
        p = MEDIA / fname
        return force or not p.exists() or manifest.get(fname) != stamp(spec)

    for kind, prefix, w_commons, w_gen in (("reconnaissance", "img", 360, 480), ("faits", "fai", 420, 520),
                                           ("questions", "que", 420, 520), ("affirmations", "aff", 420, 520)):
        for it in data[kind]:
            img = it.get("image")
            if not img:
                continue
            fname = media_name(prefix, it["id"])
            names[it["id"]] = fname
            if not need(fname, img):
                continue
            make_image(img, MEDIA / fname, w_commons, w_gen, it["id"])
            manifest[fname] = stamp(img)
            print("  media", fname)
    for it in data["scenarios"]:
        fname = media_name("scn", it["id"])
        names[it["id"]] = fname
        spec = {"kind": it["kind"], "spec": it["spec"]}
        if not need(fname, spec):
            continue
        draw = {"intersection": draw_intersection, "roundabout": draw_roundabout, "road": draw_road}[it["kind"]]
        render_png(draw(it["spec"]), MEDIA / fname, width=560)
        manifest[fname] = stamp(spec)
        print("  media", fname)
    manifest_path.write_text(json.dumps(manifest, indent=0), encoding="utf-8")
    write_attributions(data)
    return names


def _walk_dicts(obj):
    """Yield every dict nested inside obj (lists and dicts, any depth)."""
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from _walk_dicts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk_dicts(v)


def write_attributions(data):
    """List every Commons file used, with licence and author, for redistribution compliance."""
    from build.commons_fetch import find
    titles = {t for t in SIGN_FILES.values() if t}  # signs rasterised into scenario diagrams
    for kind in KINDS:
        for it in data[kind]:
            img = it.get("image") or {}
            if isinstance(img, dict) and img.get("commons"):
                titles.add(img["commons"])
            for ex in _walk_dicts(it.get("spec") or (img.get("params") if isinstance(img, dict) else None)):
                if ex.get("kind") == "sign" and ex.get("file"):  # draw_road extras
                    titles.add(ex["file"])
    lines = ["# Attributions des images (Wikimedia Commons)\n",
             "Fichiers utilisés tels quels ou rastérisés/teintés. Licence et auteur tels que déclarés sur Commons.\n"]
    for t in sorted(titles):
        key, e = find(t)
        if not e:
            continue
        author = re.sub(r"<[^>]+>", "", e.get("author") or "").strip() or "—"
        lines.append(f"- [{key}](https://commons.wikimedia.org/wiki/{key.replace(' ', '_')}) — {e.get('license') or '?'} — {author}")
    (OUT / "ATTRIBUTIONS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ------------------------------------------------------------ curriculum ---
# The study order of new cards (their "position") is computed here, not left to file order.
# Design (docs/05-audit-v2.md §2.4): method cards first; then three phases (essentiel, utile, rare);
# inside a phase the themes are interleaved in proportion to their volume, so every day is a slice of
# the whole exam; the scenario track is gated behind the signs it depends on. Cloze siblings of one
# note are spread SIBLING_GAP positions apart so the second blank is met a couple of days later.
SIBLING_GAP = 30
KIND_RANK = {"faits": 0, "questions": 1, "affirmations": 2, "reconnaissance": 0, "confusions": 1, "scenarios": 3}
# scenario sub-theme -> recognition file that must be (mostly) known before the track opens
SCENARIO_GATES = {"priorites": "panneaux_priorite", "agents": "autres", "depassement": "marquages",
                  "positionnement": "marquages", "croisement": "marquages"}


def track_of(kind: str, it: dict) -> str:
    if it["theme"] == "X":
        return "X"
    if kind == "scenarios":
        return "SCEN"
    if it["theme"] == "L" and kind in ("reconnaissance", "confusions"):
        return "SIGN"
    if it["theme"] == "L":
        return "CIRC"
    return it["theme"]


def _library_curriculum(data: dict[str, list[dict]]) -> list[tuple[str, str]]:
    """Return every note as (kind, id) in study order."""
    imp = lambda it: IMPORTANCE_RANK.get(it.get("importance", "essentiel"), 0)
    recon = {it["id"]: it for it in data["reconnaissance"]}
    # --- sign track: recognition in RECON_ORDER, each confusion right after the later of its members
    sign_recon = [it for it in data["reconnaissance"] if it["theme"] == "L"]
    sign_recon.sort(key=lambda it: (imp(it), RECON_ORDER.index(it["_file"][:-5]) if it["_file"][:-5] in RECON_ORDER else 99, it["_pos"]))
    sign_pos = {it["id"]: i for i, it in enumerate(sign_recon)}
    sign_items: list[tuple[float, int, str, str]] = [(i, imp(it), "reconnaissance", it["id"]) for i, it in enumerate(sign_recon)]
    for it in data["confusions"]:
        if it["theme"] != "L":
            continue  # e.g. dashboard-light pairs: they follow their own theme's track
        a, b = recon[it["a"]], recon[it["b"]]
        pos = max(sign_pos.get(a["id"], 0), sign_pos.get(b["id"], 0)) + 0.5
        it["_phase"] = max(imp(it), imp(a), imp(b))  # a pair is studied once both members are known
        sign_items.append((pos, it["_phase"], "confusions", it["id"]))
    sign_items.sort()
    # position after which each recognition file is fully seen (gates for the scenario track), per phase
    gate_after: dict[tuple[int, str], int] = {}
    counter = Counter()
    for _, ph, kind, ident in sign_items:
        counter[ph] += 1
        if kind == "reconnaissance":
            gate_after[(ph, recon[ident]["_file"][:-5])] = counter[ph]
    # --- other tracks: file order, grouped by sub-theme, facts before questions before affirmations
    tracks: dict[str, dict[int, list]] = {}
    for kind in KINDS:
        for it in data[kind]:
            tr = track_of(kind, it)
            if tr == "SIGN":
                continue
            tracks.setdefault(tr, {}).setdefault(imp(it), []).append(it)
    for tr, phases in tracks.items():
        for ph, items in phases.items():
            if tr == "SCEN":  # scenarios in the order their gates open (priorities first, overtaking later)
                items.sort(key=lambda it: (gate_after.get((ph, SCENARIO_GATES.get(it["sous_theme"], "panneaux_priorite")), 0), it["_file"], it["_pos"]))
                continue
            sub_order: dict[str, int] = {}
            for it in items:
                sub_order.setdefault(it["sous_theme"], len(sub_order))
            items.sort(key=lambda it: (sub_order[it["sous_theme"]], KIND_RANK[it["_kind"]], it["_file"], it["_pos"]))
    sign_phases: dict[int, list] = {}
    for _, ph, kind, ident in sign_items:
        sign_phases.setdefault(ph, []).append({"_kind": kind, "id": ident})
    tracks["SIGN"] = sign_phases

    order: list[tuple[str, str]] = []
    x = tracks.pop("X", {})
    for it in x.get(0, []) + x.get(1, []) + x.get(2, []):
        order.append((it["_kind"], it["id"]))
    for ph in (0, 1, 2):
        queues = {tr: list(phases.get(ph, [])) for tr, phases in tracks.items() if phases.get(ph)}
        # proportional interleaving; scenarios weighted up because their gates delay their start
        weights = {tr: float(len(q)) * (2.0 if tr == "SCEN" else 1.0) for tr, q in queues.items()}
        credit = {tr: 0.0 for tr in queues}
        emitted = Counter()
        while any(queues.values()):
            eligible = []
            for tr, q in queues.items():
                if not q:
                    continue
                if tr == "SCEN":
                    need = gate_after.get((ph, SCENARIO_GATES.get(q[0].get("sous_theme", ""), "panneaux_priorite")), 0)
                    if emitted["SIGN"] < min(need, len(tracks["SIGN"].get(ph, []))):
                        continue
                eligible.append(tr)
            total = sum(weights[tr] for tr in eligible)
            for tr in eligible:
                credit[tr] += weights[tr]
            best = max(eligible, key=lambda tr: credit[tr])
            credit[best] -= total
            it = queues[best].pop(0)
            emitted[best] += 1
            order.append((it["_kind"], it["id"]))
    return order


def curriculum(data: dict[str, list[dict]]) -> list[tuple[str, str]]:
    """Foundation first; preserve interleaving and prerequisite order within stages."""
    order = _library_curriculum(data)
    by_key = {(kind, n['id']): n for kind, notes in data.items() for n in notes}
    order = sorted(order, key=lambda key: by_key[key]['_stage'] != 'socle')
    # A visual application follows recognition of its signal. Delay only the
    # application, preserving the existing interleaving of other notes.
    emitted, result, pending = set(), [], []
    for key in order:
        pending.append(key)
        while True:
            ready = next((k for k in pending if not by_key[k].get('image_ref') or
                          by_key[k]['image_ref'] in emitted), None)
            if ready is None:
                break
            pending.remove(ready)
            result.append(ready)
            emitted.add(ready[1])
    if pending:
        raise DataError(f"Prérequis visuels absents : {pending}")
    return result


# ------------------------------------------------------------ collection ---
def guid_for(kind: str, ident: str) -> str:
    h = hashlib.sha1(f"cdr:{kind}:{ident}".encode()).digest()
    return base64.b64encode(h)[:10].decode().replace("+", "a").replace("/", "b")


def img_tag(fname: str) -> str:
    return f'<img src="{fname}">'


def tags_for(it: dict, kind: str) -> list[str]:
    t = [f"theme::{it['theme']}", f"sous::{it['sous_theme']}", f"importance::{it.get('importance', 'essentiel')}", f"type::{kind}"]
    t.append(f"parcours::{it['_stage']}")
    t.extend(f"objectif::{o}" for o in it['_objectives'])
    if kind == "reconnaissance":
        t.append(f"type::{it['type']}")
    for extra in it.get("tags", []) or []:
        t.append(extra)
    return t


def build_collection(data, names, out_apkg: Path):
    from anki.collection import Collection, ExportAnkiPackageOptions, DeckIdLimit

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)
    col_path = BUILD_DIR / "collection.anki2"
    col = Collection(str(col_path))
    mm = col.models
    old_mids = {}
    model_objs = {}
    # Anki compares field/template identities as well as notetype IDs. Preserve
    # those from the released v2 package; freshly generated IDs cause conflicts.
    schema_ids = json.loads((DATA / '_meta/anki_schema.json').read_text(encoding='utf-8'))
    for nt in M.notetypes():
        m = mm.new(nt["name"])
        if nt.get("cloze"):
            from anki.consts import MODEL_CLOZE
            m["type"] = MODEL_CLOZE
        m["flds"], m["tmpls"] = [], []
        for f in nt["fields"]:
            field = mm.new_field(f)
            field['id'] = schema_ids[nt['name']]['flds'][f]
            mm.add_field(m, field)
        for t in nt["templates"]:
            tm = mm.new_template(t["name"])
            tm['id'] = schema_ids[nt['name']]['tmpls'][t['name']]
            tm["qfmt"], tm["afmt"] = t["qfmt"], t["afmt"]
            mm.add_template(m, tm)
        m["css"] = M.CSS
        mm.add(m)
        old_mids[nt["name"]] = m["id"]
        model_objs[nt["name"]] = m
    old_dids = {}
    for name in M.DECK_IDS:
        old_dids[name] = col.decks.id(name)
    # deck descriptions
    root = col.decks.by_name(M.DECK_ROOT)
    root["desc"] = ("Deck pour réussir l'épreuve théorique générale (code de la route, permis B), édition 2026. "
                    "Cartes conçues une par une : reconnaissance, faits, questions, scénarios. "
                    "Conseil : 20 nouvelles cartes/jour (préréglage fourni), FSRS activé dans les options, et des séries photo/vidéo en parallèle.")
    col.decks.save(root)
    for sub, desc in M.DECK_DESCRIPTIONS.items():
        d = col.decks.by_name(f"{M.DECK_ROOT}::{sub}")
        if d:
            d["desc"] = desc
            col.decks.save(d)

    # options preset shipped with the deck: curriculum order (positions), 20 new/day, siblings buried
    import copy
    conf = copy.deepcopy(col.decks.get_config(1))
    conf.update({"id": M.DECK_CONFIG_ID, "name": M.DECK_ROOT, "newGatherPriority": 1, "newSortOrder": 1,
                 "desiredRetention": 0.9, "sm2Retention": 0.9})
    conf["new"].update({"perDay": 20, "bury": True})
    conf["rev"].update({"perDay": 400, "bury": True})
    col.decks.update_config(conf)
    for name in M.DECK_IDS:
        d = col.decks.by_name(name)
        d["conf"] = M.DECK_CONFIG_ID
        col.decks.save(d)

    counts = Counter()
    nids: dict[tuple[str, str], int] = {}
    used_media: set[str] = set()

    def add(model_name, fields: dict, kind: str, it: dict):
        m = model_objs[model_name]
        n = col.new_note(m)
        fields['Repere'] = repere_html(it['theme'])
        for k, v in fields.items():
            n[k] = "" if v is None else str(v)
            used_media.update(re.findall(r'<img src="([^"]+)"', n[k]))
        n.guid = guid_for(kind, it["id"])
        n.tags = tags_for(it, kind)
        did = old_dids[M.deck_for(it["theme"], it["sous_theme"])]
        col.add_note(n, did)
        counts[model_name] += 1
        nids[(kind, it["id"])] = n.id
        return n

    esc = lambda s: html.escape(str(s)) if s is not None else ""
    md = lambda s: inline_md(s)

    recon = {it["id"]: it for it in data["reconnaissance"]}
    for it in data["reconnaissance"]:
        add("CDR Reconnaissance", {
            "Id": it["id"], "Type": it["type"], "Image": img_tag(names[it["id"]]),
            "Question": it.get("question") or TYPE_QUESTION[it["type"]],
            "Nom": md(it["nom"]), "Signification": md(it["signification"]),
            "ConduiteATenir": md(it.get("conduite", "")), "Complement": md(it.get("complement", "")),
            "Piege": md(it.get("piege", "")), "Code": esc(it.get("code", "")),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "reconnaissance", it)
    for it in data["confusions"]:
        a, b = recon[it["a"]], recon[it["b"]]
        add("CDR Confusion", {
            "Id": it["id"], "ImageA": img_tag(names[a["id"]]), "ImageB": img_tag(names[b["id"]]),
            "NomA": md(a["nom"]), "NomB": md(b["nom"]), "Difference": md(it["difference"]),
            "Code": esc(f"{a.get('code', a['id'])} / {b.get('code', b['id'])}"),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "confusions", it)
    for it in data["faits"]:
        add("CDR Fait", {
            "Id": it["id"], "Texte": fait_html(it), "Explication": md(it.get("explication", "")),
            "Image": img_tag(names[it["id"]]) if it.get("image") else "", "Code": esc(it.get("code", "")),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "faits", it)
    for it in data["questions"]:
        add("CDR Question", {
            "Id": it["id"], "Question": md(it["question"]), "Reponse": md(it["reponse"]),
            "Explication": md(it.get("explication", "")),
            "Image": img_tag(names[it["id"]]) if it.get("image") else "", "Code": esc(it.get("code", "")),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "questions", it)
    for it in data["affirmations"]:
        add("CDR Affirmation", {
            "Id": it["id"], "Contexte": md(it.get("contexte", "")), "Affirmation": md(it["affirmation"]),
            "Verdict": it["verdict"], "Pourquoi": md(it["pourquoi"]),
            "Image": img_tag(names[it["id"]]) if it.get("image") else "", "Code": esc(it.get("code", "")),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "affirmations", it)
    for it in data["scenarios"]:
        add("CDR Scenario", {
            "Id": it["id"], "Image": img_tag(names[it["id"]]), "Question": md(it["question"]),
            "Reponse": md(it["reponse"]), "Explication": md(it.get("explication", "")), "Code": esc(it.get("code", "")),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "scenarios", it)

    # study order = curriculum positions (new cards are gathered by lowest position, see preset above)
    order = curriculum(data)
    assert len(order) == len(nids), f"curriculum: {len(order)} notes ordonnées pour {len(nids)} notes"
    card_ids = {}
    for key, nid in nids.items():
        for cid in col.card_ids_of_note(nid):
            card_ids[(*key, col.get_card(cid).ord)] = cid
    plan = learning.card_plan(data, order, SIBLING_GAP)
    assert len(plan) == col.card_count() and set(plan) == set(card_ids)
    db = col.db
    for pos, key in enumerate(plan, start=1):
        db.execute("update cards set due = ? where id = ? and type = 0", pos, card_ids[key])
    learning.write_reports(data, order, OUT)

    # media
    for fname in used_media:
        col.media.add_file(str(MEDIA / fname))
    n_notes, n_cards = col.note_count(), col.card_count()
    col.close()

    remap_ids(col_path, old_mids, old_dids)

    col = Collection(str(col_path))
    col.fix_integrity()
    out_apkg.parent.mkdir(parents=True, exist_ok=True)
    if out_apkg.exists():
        out_apkg.unlink()
    col.export_anki_package(
        out_path=str(out_apkg),
        options=ExportAnkiPackageOptions(with_scheduling=False, with_deck_configs=True, with_media=True, legacy=True),
        limit=DeckIdLimit(M.DECK_IDS[M.DECK_ROOT]),
    )
    per_deck = {d.name: len(col.find_cards(f'"deck:{d.name}"')) for d in col.decks.all_names_and_ids() if d.name.startswith(M.DECK_ROOT)}
    col.close()
    return n_notes, n_cards, counts, per_deck


def remap_ids(col_path: Path, old_mids: dict, old_dids: dict):
    db = sqlite3.connect(col_path)
    db.create_collation("unicase", lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower()))
    for name, old in old_mids.items():
        new = M.MODEL_IDS[name]
        for table, colname in (("notetypes", "id"), ("fields", "ntid"), ("templates", "ntid"), ("notes", "mid")):
            db.execute(f"update {table} set {colname}=? where {colname}=?", (new, old))
    for name, old in old_dids.items():
        new = M.DECK_IDS[name]
        db.execute("update decks set id=? where id=?", (new, old))
        db.execute("update cards set did=?, odid=case when odid=? then ? else odid end where did=?", (new, old, new, old))
    db.commit()
    db.close()


# ------------------------------------------------------------- markdown ---
def repere_html(theme):
    lesson = learning.lessons()[theme]
    return ('<p><b>' + inline_md(lesson['titre']) + '</b></p><p>' + inline_md(lesson['principe']) +
            '</p><p><b>Exemple.</b> ' + inline_md(lesson['exemple']) +
            '</p><p><b>À essayer sur une autre scène.</b> ' + inline_md(lesson['transfert']) + '</p>')


def fait_html(note) -> str:
    """Independent sibling prompts in the existing field; no schema or GUID change."""
    if "rappels" not in note:
        return inline_md(note["texte"])
    return "".join(
        f'<div class="cdr-unit" data-cloze="{CLOZE_RE.search(prompt)[1]}">{inline_md(prompt)}</div>'
        for prompt in note["rappels"]
    )


def inline_md(s) -> str:
    """Tiny markdown: **bold**, *italic*, `code`, line breaks, '- ' lists. Escapes HTML otherwise."""
    if s is None:
        return ""
    s = str(s).strip()
    # Keep French high punctuation with its preceding word on narrow screens.
    # Apply before HTML/link generation; URLs contain no literal spaces.
    s = re.sub(r" +(?=[;:!?])", "\u202f", s)
    lines = s.split("\n")
    out, in_list = [], False
    for ln in lines:
        e = html.escape(ln)
        e = re.sub(r'https?://[^\s<>]+', lambda m: '<a href="' + m[0] + '">' + m[0] + '</a>', e)
        e = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e)
        e = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*(?!\*)", r"<i>\1</i>", e)
        e = re.sub(r"`(.+?)`", r"<code>\1</code>", e)
        if e.startswith("- "):
            if not in_list:
                out.append('<ul class="cdr-list">'); in_list = True
            out.append(f"<li>{e[2:]}</li>")
        else:
            if in_list:
                out.append("</ul>"); in_list = False
            out.append(e)
    if in_list:
        out.append("</ul>")
    # join: paragraphs separated by <br>, but no <br> around lists
    res = ""
    for i, part in enumerate(out):
        if i and not part.startswith("<ul") and not out[i - 1].endswith("</ul>") and not part.startswith("<li") and not out[i - 1].startswith("<ul") and not out[i-1].startswith("<li"):
            res += "<br>"
        res += part
    return res


# ------------------------------------------------------------------ main ---
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--media", action="store_true")
    ap.add_argument("--force-media", action="store_true")
    args = ap.parse_args(argv)
    data = load_all()
    errors = validate(data)
    total = sum(len(v) for v in data.values())
    print(f"{total} notes chargées: " + ", ".join(f"{k}={len(v)}" for k, v in data.items()))
    if errors:
        print("\n".join("ERREUR " + e for e in errors))
        sys.exit(1)
    print("validation OK")
    if args.check:
        return
    names = ensure_media(data, force=args.force_media)
    if args.media:
        return
    out_apkg = OUT / "Code-de-la-route-2026.apkg"
    core = {kind: [n for n in notes if n['_stage'] == 'socle'] for kind, notes in data.items()}
    core_apkg = OUT / "Code-de-la-route-2026-Socle.apkg"
    core_notes, core_cards, _, _ = build_collection(core, names, core_apkg)
    n_notes, n_cards, counts, per_deck = build_collection(data, names, out_apkg)
    stats = ["# Statistiques du build\n", f"- Notes : {n_notes}\n- Cartes : {n_cards}\n",
             f"- Socle : {core_notes} notes / {core_cards} cartes (paquet séparé, mêmes identifiants)\n",
             "\n## Par type de note\n"]
    stats += [f"- {k} : {v}\n" for k, v in sorted(counts.items())]
    stats += ["\n## Cartes par sous-deck\n"] + [f"- {k} : {v}\n" for k, v in sorted(per_deck.items())]
    by_theme = Counter()
    for kind in KINDS:
        for it in data[kind]:
            by_theme[(it["theme"], it["sous_theme"], it.get("importance", "essentiel"))] += 1
    stats += ["\n## Notes par thème / sous-thème (essentiel / utile / rare)\n"]
    themes = sorted({k[0] for k in by_theme}, key=lambda t: "XLCRUDAPMSE".index(t))
    for t in themes:
        subs = sorted({k[1] for k in by_theme if k[0] == t})
        stats.append(f"- **{t} — {M.THEME_NAMES[t]}** : " + ", ".join(
            f"{sub} {by_theme[(t, sub, 'essentiel')]}/{by_theme[(t, sub, 'utile')]}/{by_theme[(t, sub, 'rare')]}" for sub in subs) + "\n")
    (OUT / "STATS.md").write_text("".join(stats), encoding="utf-8")
    print(f"OK -> {out_apkg} ({n_notes} notes, {n_cards} cartes)")
    print("".join(stats))


if __name__ == "__main__":
    main()
