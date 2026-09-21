"""Quote unquoted YAML scalar values that contain ': ' or ' #' (common in French prose)."""
import re, sys, yaml
from pathlib import Path

LINE = re.compile(r'^(\s*(?:- )?)([a-z_]+): (.*)$')

def fix_text(text: str) -> str:
    out = []
    block_indent = None  # indentation of the key that opened a block scalar (| or >): its body is left untouched
    for ln in text.split("\n"):
        if block_indent is not None:
            if not ln.strip() or len(ln) - len(ln.lstrip(" ")) > block_indent:
                out.append(ln)
                continue
            block_indent = None
        m = LINE.match(ln)
        if m:
            ind, key, val = m.groups()
            v = val.strip()
            if v and v[0] in "|>":
                block_indent = len(ind)
            elif v and v[0] not in "\"'[{" and (": " in v or " #" in v or v.endswith(":")):
                v = '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
                ln = f"{ind}{key}: {v}"
        out.append(ln)
    return "\n".join(out)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        p = Path(p)
        t = p.read_text(encoding="utf-8")
        f = fix_text(t)
        if f != t:
            p.write_text(f, encoding="utf-8")
            print("fixed", p)
        yaml.safe_load(f)  # raises if still invalid
