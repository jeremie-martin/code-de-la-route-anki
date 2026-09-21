"""Download Commons files listed in assets/commons_index.json on demand and rasterize SVGs.

fetch(title) -> Path of cached original (assets/_cache/commons/)
raster(title, out_png, width) -> renders SVG to PNG with cairosvg (or copies bitmap)
"""
import json, time, sys, urllib.error, urllib.request, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "assets" / "_cache" / "commons"
INDEX = ROOT / "assets" / "commons_index.json"
UA = "code-de-la-route-anki/0.1 (educational Anki deck; contact: jeremie.martin@abilityneuro.com)"

_index = None
def index():
    global _index
    if _index is None:
        _index = json.loads(INDEX.read_text(encoding="utf-8"))
    return _index

def norm_title(t):
    t = t.strip()
    if not t.startswith("File:"):
        t = "File:" + t
    return t.replace("_", " ")

def find(title):
    """Return index entry, tolerant to case/underscores; queries the API for unknown titles."""
    t = norm_title(title)
    idx = index()
    if t in idx:
        return t, idx[t]
    low = {k.lower(): k for k in idx}
    if t.lower() in low:
        return low[t.lower()], idx[low[t.lower()]]
    entry = _lookup(t)
    if entry:
        idx[t] = entry
        INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
        return t, entry
    return None, None


def _lookup(title):
    """Fetch imageinfo for one title from the Commons API (adds it to the local index)."""
    import urllib.parse
    q = urllib.parse.urlencode({"action": "query", "prop": "imageinfo", "titles": title, "format": "json",
                                "iiprop": "url|mime|sha1|size|extmetadata",
                                "iiextmetadatafilter": "LicenseShortName|Artist"})
    req = urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + q, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    for p in d["query"]["pages"].values():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            return None
        em = ii.get("extmetadata", {})
        return {"url": ii["url"], "mime": ii.get("mime"), "sha1": ii.get("sha1"), "width": ii.get("width"),
                "height": ii.get("height"), "license": em.get("LicenseShortName", {}).get("value"),
                "author": em.get("Artist", {}).get("value")}
    return None

def fetch(title):
    key, entry = find(title)
    if not entry:
        raise KeyError(f"not in commons index: {title}")
    CACHE.mkdir(parents=True, exist_ok=True)
    fname = key[len("File:"):].replace("/", "_")
    p = CACHE / fname
    if p.exists() and hashlib.sha1(p.read_bytes()).hexdigest() == entry["sha1"]:
        return p
    for attempt in range(5):
        try:
            req = urllib.request.Request(entry["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            break
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500 and e.code != 429:  # permanent: retrying will not help
                raise RuntimeError(f"{key}: HTTP {e.code} ({entry['url']})") from e
            print("retry", attempt, key, e, file=sys.stderr)
            time.sleep(2 + 3 * attempt)
        except Exception as e:
            print("retry", attempt, key, e, file=sys.stderr)
            time.sleep(2 + 3 * attempt)
    else:
        raise RuntimeError(key)
    if entry.get("sha1") and hashlib.sha1(data).hexdigest() != entry["sha1"]:
        print(f"ATTENTION: {key}: le fichier Commons a changé depuis l'indexation (sha1 différent) ; "
              "vérifier l'image et régénérer l'index pour ce titre", file=sys.stderr)
    p.write_bytes(data)
    time.sleep(0.4)
    return p

def raster(src: Path, out_png: Path, width=360):
    import cairosvg
    from PIL import Image
    out_png.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix.lower() == ".svg":
        cairosvg.svg2png(url=str(src), write_to=str(out_png), output_width=width, unsafe=True)
    else:
        im = Image.open(src).convert("RGBA")
        r = width / im.width
        im = im.resize((width, max(1, round(im.height * r))), Image.LANCZOS)
        im.save(out_png)
    return out_png

if __name__ == "__main__":
    for t in sys.argv[1:]:
        p = fetch(t)
        print(p, p.stat().st_size)


def raster_tinted(src: Path, out_png: Path, colour: str, width=360, pad=0.18, bg="#1b1b1b"):
    """Render a black-on-transparent ISO symbol as a lit dashboard tell-tale.

    The symbol's darkness becomes the alpha of a solid `colour` layer, composited on a
    dark rounded 'dashboard' tile so red/orange/green/blue lights read like the real thing.
    """
    import cairosvg
    from PIL import Image, ImageDraw, ImageChops
    out_png.parent.mkdir(parents=True, exist_ok=True)
    inner = int(width * (1 - 2 * pad))
    import io, re
    svg = src.read_text(encoding="utf-8", errors="ignore")
    # ISO 7000 files carry four grey registration marks in the corners: drop them
    svg = re.sub(r'<path d="m(0|200) (16|184)v-?16h-?16"/>', "", svg)
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=inner, unsafe=True)
    sym = Image.open(io.BytesIO(png)).convert("RGBA")
    # darkness mask: black pixels -> opaque; white/transparent -> transparent.
    # Grey strokes (some files use #999/#333) are boosted so they light up fully.
    lum = sym.convert("L")
    alpha = sym.getchannel("A")
    dark = ImageChops.invert(lum).point(lambda v: min(255, int(255 * (v / 255) ** 0.45)))
    mask = ImageChops.multiply(dark, alpha)
    layer = Image.new("RGBA", sym.size, colour)
    layer.putalpha(mask)
    tile = Image.new("RGBA", (width, width), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    d.rounded_rectangle([0, 0, width - 1, width - 1], radius=int(width * 0.12), fill=bg)
    # soft glow: paste a blurred, lower-alpha copy first
    from PIL import ImageFilter
    glow = layer.filter(ImageFilter.GaussianBlur(radius=width * 0.02))
    x = (width - sym.width) // 2
    y = (width - sym.height) // 2
    tile.alpha_composite(glow, (x, y))
    tile.alpha_composite(layer, (x, y))
    tile.save(out_png)
    return out_png
