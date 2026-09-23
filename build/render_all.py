"""Render every card in study order for reviewers who read the deck as a learner would: full-page screenshots at
phone width (390 px), front and back, plus `dump.md`, the text of every card in the same order.

python -m build.render_all OUTDIR [--night] [--ids id1,id2]   (--ids limits the screenshots; dump.md stays complete)
Needs a previous build and requirements-qa.txt. Files: NNNN_<id>_cK_q.png / _a.png, NNNN = position in the programme.
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
import tempfile
from pathlib import Path

from anki.collection import Collection
from playwright.sync_api import sync_playwright

from build.preview import CHROME, MEDIA, OUT
from build.render_check import page_html


def card_text(h: str) -> str:
    h = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r' [IMG \1] ', h)
    h = re.sub(r'<(br|/div|/p|/li|hr)[^>]*>', '\n', h)
    h = re.sub(r'<style.*?</style>', '', h, flags=re.S)
    h = re.sub(r'<[^>]+>', '', h)
    return re.sub(r'\n\s*\n+', '\n', html.unescape(h)).strip()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--night", action="store_true")
    ap.add_argument("--ids", default="")
    args = ap.parse_args(argv)
    out = Path(args.out)
    ids = set(args.ids.split(",")) if args.ids else None
    out.mkdir(parents=True, exist_ok=True)
    if not (out / "media").exists():
        (out / "media").symlink_to(MEDIA)
    tmp = Path(tempfile.mkdtemp())
    shutil.copy(OUT / "_build" / "collection.anki2", tmp / "c.anki2")
    col = Collection(str(tmp / "c.anki2"))
    dump = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 390, "height": 700})
        for pos, cid in enumerate(col.db.list("select id from cards order by due, id"), 1):
            card = col.get_card(cid)
            ident = card.note()["Id"]
            q, a = card.question(), card.answer()
            dump.append(f"### {pos:04d} {ident} c{card.ord + 1} [{card.note_type()['name']}]\n"
                        f"--- RECTO\n{card_text(q)}\n--- VERSO\n{card_text(a)}\n")
            if ids is not None and ident not in ids:
                continue
            for side, body in (("q", q), ("a", a)):
                hp = out / f"{pos:04d}_{ident}_c{card.ord + 1}_{side}.html"
                hp.write_text(page_html(body.replace('src="cdr_', 'src="media/cdr_'), card.note_type()["css"], args.night),
                              encoding="utf-8")
                page.goto(hp.as_uri(), wait_until="load")
                page.screenshot(path=str(hp.with_suffix(".png")), full_page=True)
                hp.unlink()
        browser.close()
    (out / "dump.md").write_text("\n".join(dump), encoding="utf-8")
    col.close()
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
