"""Cross-file near-duplicate finder for the knowledge library.

Usage: .venv/bin/python -m build.dedup [--threshold 0.62]

Compares the *knowledge* carried by every note (question+answer, cloze text, affirmation+pourquoi,
scenario question+answer) across all files with a token-set similarity, and prints the pairs above the
threshold, most similar first. Editors decide; nothing is modified. Pairs inside the same file are
listed too (they matter as much), but pairs already known to be deliberate can be silenced by adding
`dedup_ok: [other-id]` to one of the two notes.
"""
from __future__ import annotations

import argparse
import re
import unicodedata
from itertools import combinations

from build.build import KINDS, load_all

STOP = set("""le la les l un une des du de d et ou à a au aux en pour par sur sous dans avec sans que qui quoi
dont où ne pas plus je j me ma mon mes il elle on nous vous ils elles ce cet cette ces se sa son ses est sont
être avoir fait faire dois doit peux peut puis si mais donc car ni y lui leur leurs tout tous toute toutes
même aussi très bien non oui km h m km/h € g/l s ans an jour jours vers entre chez comme afin lors dès
quand lorsque avant après sauf autre autres""".split())


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\{\{c\d+::(.*?)(?:::.*?)?\}\}", r"\1", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return s


def tokens(s: str) -> set[str]:
    toks = {t for t in norm(s).split() if len(t) > 2 and t not in STOP}
    return {t[:6] for t in toks}  # crude stemming: 6-char prefixes


def text_of(kind: str, it: dict) -> str:
    if kind == "faits":
        return it.get("texte", "")
    if kind == "affirmations":
        return f"{it.get('contexte', '')} {it['affirmation']} {it['pourquoi']}"
    if kind in ("questions", "scenarios"):
        return f"{it['question']} {it['reponse']}"
    if kind == "reconnaissance":
        return f"{it['nom']} {it['signification']} {it.get('conduite', '')}"
    if kind == "confusions":
        return it["difference"]
    return ""


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=0.62)
    ap.add_argument("--kinds", default="faits,questions,affirmations,scenarios")
    args = ap.parse_args(argv)
    kinds = args.kinds.split(",")
    data = load_all()
    notes = []
    for kind in kinds:
        for it in data[kind]:
            notes.append((kind, it, tokens(text_of(kind, it))))
    pairs = []
    for (ka, a, ta), (kb, b, tb) in combinations(notes, 2):
        if not ta or not tb:
            continue
        if b["id"] in (a.get("dedup_ok") or []) or a["id"] in (b.get("dedup_ok") or []):
            continue
        inter = len(ta & tb)
        sim = inter / min(len(ta), len(tb))  # overlap coefficient: catches a short card contained in a long one
        if sim >= args.threshold and inter >= 6:
            pairs.append((sim, ka, a, kb, b))
    pairs.sort(key=lambda p: -p[0])
    print(f"{len(pairs)} paires ≥ {args.threshold} (sur {len(notes)} notes)")
    for sim, ka, a, kb, b in pairs:
        print(f"\n[{sim:.2f}] {ka}/{a['_file']}:{a['id']}  ~  {kb}/{b['_file']}:{b['id']}")
        print("   A:", text_of(ka, a)[:170].replace("\n", " "))
        print("   B:", text_of(kb, b)[:170].replace("\n", " "))


if __name__ == "__main__":
    main()
