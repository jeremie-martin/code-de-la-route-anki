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

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "out"
MEDIA = OUT / "media"
BUILD_DIR = OUT / "_build"

THEMES = set(M.THEME_NAMES)
IMPORTANCE = {"essentiel", "utile", "rare"}
KINDS = ["reconnaissance", "confusions", "faits", "questions", "scenarios"]
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
# Insertion order = order in which Anki introduces new cards. Recognition files are ordered
# pedagogically (danger -> priorité -> interdiction -> ... -> voyants); other kinds follow their
# numeric file prefixes. Within a file, essential notes come before useful and rare ones.
RECON_ORDER = ["panneaux_danger", "panneaux_priorite", "panneaux_interdiction", "panneaux_obligation", "panneaux_fin",
               "panneaux_zones", "panneaux_indication", "panneaux_localisation", "panneaux_direction", "panonceaux",
               "balises", "passage_a_niveau", "temporaire", "voies_reservees", "panneaux_services", "feux", "marquages",
               "autres", "voyants"]
IMPORTANCE_RANK = {"essentiel": 0, "utile": 1, "rare": 2}


def load_all() -> dict[str, list[dict]]:
    data = {k: [] for k in KINDS}
    for kind in KINDS:
        files = sorted((DATA / kind).glob("*.yaml"))
        if kind == "reconnaissance":
            files.sort(key=lambda f: (RECON_ORDER.index(f.stem) if f.stem in RECON_ORDER else 99, f.stem))
        for f in files:
            items = yaml.safe_load(f.read_text(encoding="utf-8")) or []
            if not isinstance(items, list):
                raise DataError(f"{f}: expected a list")
            for it in items:
                if not isinstance(it, dict):
                    raise DataError(f"{f}: entrée non structurée {it!r}")
                it["_file"] = f.name
            items.sort(key=lambda it: IMPORTANCE_RANK.get(it.get("importance", "essentiel"), 1))
            data[kind].extend(items)
    return data


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
        n = sorted({int(x) for x in CLOZE_RE.findall(it.get("texte", ""))})
        if not n:
            errors.append(f"{it['_file']}:{it.get('id')}: aucun cloze")
        elif n != list(range(1, len(n) + 1)):
            errors.append(f"{it['_file']}:{it.get('id')}: numérotation des clozes non contiguë {n}")
        elif len(n) > 4:
            errors.append(f"{it['_file']}:{it.get('id')}: plus de 4 clozes ({len(n)})")
    for it in data["questions"]:
        common(it, "questions")
        req(it, "question", "reponse")
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

    for kind, prefix, w_commons, w_gen in (("reconnaissance", "img", 360, 480), ("faits", "fai", 420, 520), ("questions", "que", 420, 520)):
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


# ------------------------------------------------------------ collection ---
def guid_for(kind: str, ident: str) -> str:
    h = hashlib.sha1(f"cdr:{kind}:{ident}".encode()).digest()
    return base64.b64encode(h)[:10].decode().replace("+", "a").replace("/", "b")


def img_tag(fname: str) -> str:
    return f'<img src="{fname}">'


def tags_for(it: dict, kind: str) -> list[str]:
    t = [f"theme::{it['theme']}", f"sous::{it['sous_theme']}", f"importance::{it.get('importance', 'essentiel')}", f"type::{kind}"]
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
    for nt in M.notetypes():
        m = mm.new(nt["name"])
        if nt.get("cloze"):
            from anki.consts import MODEL_CLOZE
            m["type"] = MODEL_CLOZE
        m["flds"], m["tmpls"] = [], []
        for f in nt["fields"]:
            mm.add_field(m, mm.new_field(f))
        for t in nt["templates"]:
            tm = mm.new_template(t["name"])
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
                    "Conseil : 20 nouvelles cartes/jour, FSRS activé, et des séries d'entraînement en parallèle.")
    col.decks.save(root)
    for sub, desc in M.DECK_DESCRIPTIONS.items():
        d = col.decks.by_name(f"{M.DECK_ROOT}::{sub}")
        if d:
            d["desc"] = desc
            col.decks.save(d)

    counts = Counter()

    def add(model_name, fields: dict, kind: str, it: dict):
        m = model_objs[model_name]
        n = col.new_note(m)
        for k, v in fields.items():
            n[k] = "" if v is None else str(v)
        n.guid = guid_for(kind, it["id"])
        n.tags = tags_for(it, kind)
        did = old_dids[M.deck_for(it["theme"], it["sous_theme"])]
        col.add_note(n, did)
        counts[model_name] += 1
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
            "Id": it["id"], "Texte": md(it["texte"]), "Explication": md(it.get("explication", "")),
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
    for it in data["scenarios"]:
        add("CDR Scenario", {
            "Id": it["id"], "Image": img_tag(names[it["id"]]), "Question": md(it["question"]),
            "Reponse": md(it["reponse"]), "Explication": md(it.get("explication", "")), "Code": esc(it.get("code", "")),
            "Theme": M.THEME_NAMES[it["theme"]], "SousTheme": it["sous_theme"], "Source": md(it["source"]),
        }, "scenarios", it)

    # "00 Méthode d'examen" (theme X) is introduced first when studying the root deck, whatever the file order
    method = col.find_cards('"tag:theme::X"')
    if method:
        col.sched.reposition_new_cards(method, starting_from=0, step_size=1, randomize=False, shift_existing=True)

    # media
    for fname in set(names.values()):
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
        options=ExportAnkiPackageOptions(with_scheduling=False, with_deck_configs=False, with_media=True, legacy=True),
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
def inline_md(s) -> str:
    """Tiny markdown: **bold**, *italic*, `code`, line breaks, '- ' lists. Escapes HTML otherwise."""
    if s is None:
        return ""
    s = str(s).strip()
    lines = s.split("\n")
    out, in_list = [], False
    for ln in lines:
        e = html.escape(ln)
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
    n_notes, n_cards, counts, per_deck = build_collection(data, names, out_apkg)
    stats = ["# Statistiques du build\n", f"- Notes : {n_notes}\n- Cartes : {n_cards}\n", "\n## Par type de note\n"]
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
