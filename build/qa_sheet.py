"""Contact sheets of recognition images labelled code + nom, per data file, for visual QA."""
import sys, yaml
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "out" / "media"
OUT = ROOT / "out" / "qa"; OUT.mkdir(parents=True, exist_ok=True)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
fontb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
files = sys.argv[1:] or sorted((ROOT/"data"/"reconnaissance").glob("*.yaml"))
for f in files:
    f = Path(f)
    items = yaml.safe_load(f.read_text(encoding="utf-8")) or []
    cw, ch, cols = 230, 250, 6
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cw, rows * ch), (245, 245, 245))
    d = ImageDraw.Draw(sheet)
    for i, it in enumerate(items):
        x, y = (i % cols) * cw, (i // cols) * ch
        p = MEDIA / f"cdr_img_{it['id']}.png"
        if p.exists():
            im = Image.open(p).convert("RGBA"); im.thumbnail((200, 170))
            bg = Image.new("RGBA", im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
            sheet.paste(bg.convert("RGB"), (x + (cw - im.width) // 2, y + 8))
        d.text((x + 6, y + 184), f"{it.get('code', it['id'])}", font=fontb, fill=(0, 0, 0))
        name = it['nom']
        lines, cur = [], ""
        for w in name.split():
            if d.textlength(cur + " " + w, font=font) > cw - 12: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            d.text((x + 6, y + 202 + j * 15), ln, font=font, fill=(40, 40, 40))
    outp = OUT / (f.stem + ".png"); sheet.save(outp); print(outp, len(items), sheet.size)
