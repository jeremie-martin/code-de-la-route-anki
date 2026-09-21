"""Render sample cards to PNG (question + answer side) with headless Chrome for visual QA.

Usage: .venv/bin/python -m build.preview [--ids id1,id2] [--n 12] [--night]
Output: out/preview/<id>_q.png, <id>_a.png and out/preview/sheet.png
"""
from __future__ import annotations

import argparse
import random
import shutil
import subprocess
import sys
from pathlib import Path

from anki.collection import Collection

from build import models as M

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
PREVIEW = OUT / "preview"
MEDIA = OUT / "media"
CHROME = shutil.which("google-chrome") or shutil.which("google-chrome-stable") or shutil.which("chromium")

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{css}
body {{ margin: 0; }} .card {{ min-height: 100vh; box-sizing: border-box; }}</style></head>
<body class="{cls}"><div class="card {cls}">{body}</div>
<script>
// emulate Anki's cloze/hint behaviour minimally: nothing needed for static preview
</script></body></html>"""


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="")
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--night", action="store_true")
    ap.add_argument("--width", type=int, default=520)
    args = ap.parse_args(argv)
    if not CHROME:
        sys.exit("google-chrome / chromium introuvable dans le PATH (nécessaire pour les captures)")
    col = Collection(str(OUT / "_build" / "collection.anki2"))
    if args.ids:
        cids = []
        for i in args.ids.split(","):
            cids += col.find_cards(f'"Id:{i}"')
    else:
        cids = list(col.find_cards(f'"deck:{M.DECK_ROOT}"'))
        random.seed(7)
        cids = random.sample(cids, min(args.n, len(cids)))
    if PREVIEW.exists():
        shutil.rmtree(PREVIEW)
    PREVIEW.mkdir(parents=True)
    # media must be reachable relative to the html file
    (PREVIEW / "media").symlink_to(MEDIA)
    shots = []
    for cid in cids:
        card = col.get_card(cid)
        note = card.note()
        ident = note["Id"] if "Id" in note else str(cid)
        css = card.note_type()["css"]
        cls = "nightMode night_mode" if args.night else ""
        for side, html_ in (("q", card.question()), ("a", card.answer())):
            html_ = html_.replace('src="cdr_', 'src="media/cdr_')
            page = PAGE.format(css=css, body=html_, cls=cls)
            hp = PREVIEW / f"{ident}_c{card.ord}_{side}.html"
            hp.write_text(page, encoding="utf-8")
            png = PREVIEW / f"{ident}_c{card.ord}_{side}.png"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-sandbox",
                            f"--window-size={args.width},900", f"--screenshot={png}", str(hp)],
                           check=True, capture_output=True)
            shots.append(png)
    col.close()
    # contact sheet
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in shots]
    cols = 6
    cw, ch = args.width, 900
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (cw + 8), rows * (ch + 8)), (200, 200, 200))
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * (cw + 8), (i // cols) * (ch + 8)))
    sheet.save(PREVIEW / "sheet.png")
    print("preview:", PREVIEW / "sheet.png", len(shots), "shots")


if __name__ == "__main__":
    main()
