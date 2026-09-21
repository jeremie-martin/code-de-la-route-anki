"""Index French road-sign files on Wikimedia Commons (title, url, license, sha1).

Output: assets/commons_index.json  {title: {url, mime, sha1, license, author, size}}
Polite: sequential requests, custom UA, small delay.
"""
import json, time, sys, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "commons_index.json"
UA = "code-de-la-route-anki/0.1 (educational Anki deck; contact: jeremie.martin@abilityneuro.com)"
API = "https://commons.wikimedia.org/w/api.php"

CATEGORIES = [
    "SVG warning road signs of France",
    "SVG prohibitory road signs of France",
    "SVG mandatory road signs of France",
    "SVG priority road signs of France",
    "SVG information road signs of France",
    "SVG additional road signs of France",
    "SVG regulatory road signs of France",
    "SVG service road signs of France",
    "SVG diagrams of route signs of France",
    "SVG road signs in France",
    "Diagrams of road markings of France",
    "Diagrams of temporary road signs of France",
    "Diagrams of level crossing road signs of France",
    "Diagrams of road sign beacon of France",
    "Diagrams of additional road signs of France",
    "Diagrams of direction road signs of France",
    "Diagrams of informatory road signs of France",
    "Diagrams of motorway exit signs of France",
    "Diagrams of route signs of France",
    "Symbols of road signs of France",
]

def get(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa
            print("retry", attempt, e, file=sys.stderr)
            time.sleep(2 + 3 * attempt)
    raise RuntimeError(url)

def list_category(cat, seen_cats):
    """Recursively list files of a category (depth-limited)."""
    if cat in seen_cats:
        return []
    seen_cats.add(cat)
    files, cont = [], {}
    while True:
        d = get({"action": "query", "list": "categorymembers", "cmtitle": "Category:" + cat,
                 "cmlimit": "500", "cmtype": "file|subcat", **cont})
        for m in d["query"]["categorymembers"]:
            t = m["title"]
            if t.startswith("File:"):
                files.append(t)
            elif t.startswith("Category:") and "historic" not in t.lower() and "obsolete" not in t.lower():
                sub = t[len("Category:"):]
                if len(seen_cats) < 80:
                    time.sleep(0.5)
                    files += list_category(sub, seen_cats)
        if "continue" in d:
            cont = d["continue"]
            time.sleep(0.5)
        else:
            break
    return files

def file_info(titles):
    out = {}
    for i in range(0, len(titles), 40):
        chunk = titles[i:i + 40]
        d = get({"action": "query", "prop": "imageinfo", "titles": "|".join(chunk),
                 "iiprop": "url|mime|sha1|size|extmetadata",
                 "iiextmetadatafilter": "LicenseShortName|Artist|Attribution|License"})
        for p in d["query"]["pages"].values():
            ii = (p.get("imageinfo") or [{}])[0]
            em = ii.get("extmetadata", {})
            out[p["title"]] = {
                "url": ii.get("url"), "mime": ii.get("mime"), "sha1": ii.get("sha1"),
                "width": ii.get("width"), "height": ii.get("height"),
                "license": em.get("LicenseShortName", {}).get("value"),
                "author": em.get("Artist", {}).get("value"),
            }
        time.sleep(0.6)
    return out

if __name__ == "__main__":
    seen = set()
    all_files = []
    for c in CATEGORIES:
        fs = list_category(c, seen)
        print(f"{c}: {len(fs)} files", file=sys.stderr)
        all_files += fs
        time.sleep(0.5)
    all_files = sorted(set(all_files))
    print("total unique files:", len(all_files), file=sys.stderr)
    info = file_info(all_files)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(info, ensure_ascii=False, indent=1))
    print("wrote", OUT, len(info), file=sys.stderr)
