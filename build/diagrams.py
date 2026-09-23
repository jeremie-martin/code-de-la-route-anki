"""Procedural SVG diagrams for scenario cards (top-down views).

All diagrams share one visual identity: dark asphalt, white markings, soft green
surroundings, flat-colour vehicles with a windscreen showing the heading, real
road-sign pictograms (Commons SVG rasterised and embedded as data URIs).

Coordinate system: intersections and roundabouts are drawn on a 600x600 plane centred at (300, 300);
road strips on a 600x480 plane. The exported viewBox is cropped to the part of the plane that carries
information, so vehicles, arrows and signs stay legible on a phone. Approaches are named by compass point
of the ARRIVING vehicle: a vehicle on approach "S" is south of the centre and heads north. "Me" is the
blue car with a yellow halo, labelled MOI inside the body.
"""
from __future__ import annotations

import base64
import math
from pathlib import Path
from xml.sax.saxutils import escape as esc  # for text taken from the data files

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------- palette ---
ASPHALT = "#4a4a4a"
GRASS = "#d5e2c4"
MARK = "#ffffff"
YELLOW = "#f2c200"
RAIL = "#c4c4c4"
LABEL = "#263336"
PEDESTRIAN = "#e65100"
CAR_COLOURS = {
    "bleu": "#2d6fd8",
    "rouge": "#d8362d",
    "vert": "#2fa14b",
    "jaune": "#f2c200",
    "blanc": "#f4f4f4",
    "gris": "#9a9a9a",
    "noir": "#222222",
    "orange": "#f08a24",
    "violet": "#8e44ad",
}
FONT = "Inter, 'Noto Sans', 'DejaVu Sans', sans-serif"

# heading (dx, dy) for each approach (direction of travel)
HEADING = {"S": (0, -1), "N": (0, 1), "E": (-1, 0), "W": (1, 0)}


def right_of(approach: str) -> str:
    """Approach that lies to the RIGHT of a vehicle arriving from `approach`.

    A vehicle from S heads north: its right is east, i.e. the approach E.
    """
    return {"S": "E", "E": "N", "N": "W", "W": "S"}[approach]


def opposite(approach: str) -> str:
    return {"S": "N", "N": "S", "E": "W", "W": "E"}[approach]


def left_of(approach: str) -> str:
    return opposite(right_of(approach))


def turn_target(approach: str, goes: str) -> str:
    """Approach name of the branch the vehicle leaves by."""
    if goes == "straight":
        return opposite(approach)
    if goes == "right":
        return right_of(approach)
    if goes == "left":
        return left_of(approach)
    raise ValueError(goes)


# ------------------------------------------------------------ sign images ---
_sign_cache: dict[str, str] = {}


def sign_data_uri(commons_title: str, px: int = 120) -> str:
    """Rasterise a Commons SVG sign to PNG and return a data URI (cached)."""
    key = f"{commons_title}@{px}"
    if key in _sign_cache:
        return _sign_cache[key]
    from build.commons_fetch import fetch  # local import keeps module light
    import cairosvg

    src = fetch(commons_title)
    if src.suffix.lower() == ".svg":
        png = cairosvg.svg2png(url=str(src), output_width=px, unsafe=True)
    else:
        png = src.read_bytes()
    uri = "data:image/png;base64," + base64.b64encode(png).decode()
    _sign_cache[key] = uri
    return uri


# AB3a without its optional plate, drawn here so scenarios and question drawings share it
CEDEZ_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="300" height="270" viewBox="0 0 300 270">'
             '<path d="M20,22 L280,22 L150,248 Z" fill="#d52b1e" stroke="#9a9a9a" stroke-width="2" stroke-linejoin="round"/>'
             '<path d="M58,44 L242,44 L150,204 Z" fill="#ffffff"/></svg>')


def sign_uri(name: str, px: int = 120) -> str:
    """Data URI of a scenario sign: the drawn give-way triangle, or the Commons file of SIGN_FILES."""
    if name == "cedez":
        return "data:image/svg+xml;base64," + base64.b64encode(CEDEZ_SVG.encode()).decode()
    return sign_data_uri(SIGN_FILES[name], px)


SIGN_FILES = {
    "stop": "France road sign AB4.svg",
    "cedez": None,  # drawn (CEDEZ_SVG): the Commons AB3a carries an unreadable « CÉDEZ LE PASSAGE » plate
    "prioritaire": "France road sign AB6.svg",
    "fin_prioritaire": "France road sign AB7.svg",
    "priorite_droite": "France road sign AB1.svg",
    "priorite_ponctuelle": "France road sign AB2.svg",
    "giratoire": "France road sign AB25.svg",
    "sens_interdit": "France road sign B1.svg",
    "sens_unique": "France road sign C12.svg",
    "feu": None,  # drawn
    "agent": None,  # drawn
}


# --------------------------------------------------------------- drawing ---
class SVG:
    """Drawing plane of w x h units; `view` (x, y, w, h) is the exported window."""

    def __init__(self, w=600, h=600, view=None):
        self.w, self.h = w, h
        self.view = view or (0, 0, w, h)
        self.parts: list[str] = []

    def add(self, s: str):
        self.parts.append(s)

    def caption(self, text):
        """One sentence on a white band under the exported window."""
        x, y, w, h = self.view
        self.add(f'<rect x="{x}" y="{y + h}" width="{w}" height="40" fill="#ffffff"/>')
        self.add(f'<text x="{x + w / 2}" y="{y + h + 26}" font-family="{FONT}" font-size="18" '
                 f'text-anchor="middle" fill="#222">{esc(str(text))}</text>')
        self.view = (x, y, w, h + 40)

    def __str__(self):
        x, y, w, h = self.view
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="{x} {y} {w} {h}">'
            + "".join(self.parts)
            + "</svg>"
        )


def _rot_for(approach: str) -> float:
    """Rotation (deg) that maps a north-heading sprite to the approach heading."""
    return {"S": 0, "E": 270, "N": 180, "W": 90}[approach]


# Half-length of each sprite: vehicles wait with their FRONT at the same distance from the junction,
# and intention arrows start at the front, whatever the vehicle.
HALF_WIDTH = {"car": 22, "truck": 26, "bus": 24, "lorry": 27}
HALF_LENGTH = {"car": 42, "truck": 60, "lorry": 115, "bus": 64, "tram": 80, "moto": 38, "bike": 34, "pompiers": 50}


def _upright(text: str, y: float, rot: float, size: int, fill="#111", along=False) -> str:
    """Label centred on (0, y) of a sprite rotated by `rot`: it reads upright on screen, or, with `along`,
    bottom-to-top when the vehicle is vertical (a long label then follows the body)."""
    screen = -90 if along and rot % 180 == 0 else 0
    return (f'<text x="0" y="0" font-family="{FONT}" font-size="{size}" font-weight="700" text-anchor="middle" '
            f'dominant-baseline="central" fill="{fill}" transform="translate(0,{y}) rotate({screen - rot})">{text}</text>')


def vehicle_sprite(kind: str, colour: str, label: str | None = None, rot: float = 0) -> str:
    """Sprite drawn heading NORTH (up), centred on origin; `rot` is the rotation the caller applies,
    so that text stays readable."""
    c = CAR_COLOURS.get(colour, colour)
    label = esc(str(label)) if label else None
    stroke = "#111"
    if kind == "car":
        return (
            f'<g><rect x="-22" y="-42" width="44" height="84" rx="10" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-17" y="-30" width="34" height="16" rx="4" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<rect x="-17" y="18" width="34" height="12" rx="4" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<rect x="-19" y="-44" width="8" height="5" fill="#fff6c2"/><rect x="11" y="-44" width="8" height="5" fill="#fff6c2"/>'
            + (_upright(label, 2, rot, 15) if label else "")
            + "</g>"
        )
    if kind == "truck":
        return (
            f'<g><rect x="-26" y="-60" width="52" height="120" rx="6" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-26" y="-60" width="52" height="30" rx="6" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-20" y="-52" width="40" height="12" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<line x1="-26" y1="-28" x2="26" y2="-28" stroke="{stroke}" stroke-width="2"/>'
            + (_upright(label, 14, rot, 20) if label else "")
            + "</g>"
        )
    if kind == "lorry":  # rigid lorry, about 2.7 car lengths: cab, then the box
        return (
            f'<g><rect x="-27" y="-64" width="54" height="179" rx="4" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-27" y="-115" width="54" height="46" rx="7" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-21" y="-108" width="42" height="12" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            + (_upright(label, 20, rot, 20) if label else "")
            + "</g>"
        )
    if kind == "bus":
        return (
            f'<g><rect x="-24" y="-64" width="48" height="128" rx="8" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-19" y="-56" width="38" height="12" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            + "".join(f'<rect x="-21" y="{y}" width="8" height="12" fill="#cfe6f7"/><rect x="13" y="{y}" width="8" height="12" fill="#cfe6f7"/>' for y in range(-36, 50, 20))
            + (_upright(label, 0, rot, 20) if label else "")
            + "</g>"
        )
    if kind == "tram":  # windows leave the middle of the body free for the label
        return (
            f'<g><rect x="-20" y="-80" width="40" height="160" rx="12" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-15" y="-72" width="30" height="10" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            + "".join(f'<rect x="-17" y="{y}" width="34" height="10" fill="#cfe6f7"/>' for y in (-56, -38, 34, 52))
            + _upright("TRAM", 0, rot, 14, along=True) + "</g>"
        )
    if kind == "moto":
        return (
            f'<g><rect x="-11" y="-38" width="22" height="76" rx="10" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<line x1="-20" y1="-12" x2="20" y2="-12" stroke="#222" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="0" cy="0" r="12" fill="#222" stroke="#fff" stroke-width="2"/></g>'
        )
    if kind == "bike":
        return (
            f'<g><rect x="-8" y="-34" width="16" height="68" rx="8" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<line x1="-20" y1="-12" x2="20" y2="-12" stroke="#222" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="0" cy="0" r="11" fill="#222" stroke="#fff" stroke-width="2"/></g>'
        )
    if kind == "pompiers":
        return (
            f'<g><rect x="-24" y="-50" width="48" height="100" rx="8" fill="#d8362d" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-19" y="-40" width="38" height="14" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<circle cx="0" cy="-46" r="6" fill="#2d6fd8" stroke="#fff" stroke-width="1.5"/>'
            + _upright("SOS", 10, rot, 12, fill="#fff") + "</g>"
        )
    raise ValueError(kind)


def siren_rays(cx: float, cy: float, colour="#2d6fd8", r0=10, r1=18) -> str:
    """Radiating ticks around a lamp: the device is active (rotating beacon, flashing light)."""
    ticks = []
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        ticks.append(f'<line x1="{cx + r0 * math.cos(a):.1f}" y1="{cy + r0 * math.sin(a):.1f}" '
                     f'x2="{cx + r1 * math.cos(a):.1f}" y2="{cy + r1 * math.sin(a):.1f}" '
                     f'stroke="{colour}" stroke-width="3" stroke-linecap="round"/>')
    return "".join(ticks)


def intention_arrow(goes: str, colour="#111", front: float = 42) -> str:
    """Arrow drawn in front of a north-heading sprite (whose front is `front` px ahead of its centre)."""
    # Arrows stop short of the junction centre so that several intentions stay distinguishable.
    if goes == "straight":
        path = "M0,-54 L0,-78"
        head = "M0,-88 L-10,-72 L10,-72 Z"
    elif goes == "right":
        path = "M0,-54 L0,-68 Q0,-78 10,-78 L26,-78"
        head = "M36,-78 L22,-88 L22,-68 Z"
    elif goes == "left":
        path = "M0,-54 L0,-68 Q0,-78 -10,-78 L-26,-78"
        head = "M-36,-78 L-22,-88 L-22,-68 Z"
    else:
        return ""
    return (
        f'<g transform="translate(0,{42 - front})">'
        f'<path d="{path}" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="{path}" fill="none" stroke="{colour}" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="{head}" fill="{colour}" stroke="#fff" stroke-width="1.5"/></g>'
    )


def _halo(me: bool) -> str:
    return '<rect x="-30" y="-50" width="60" height="100" rx="14" fill="none" stroke="#f2c200" stroke-width="5"/>' if me else ""


def _body(v: dict, rot: float = 0) -> str:
    """Sprite with halo and label; the learner's vehicle carries MOI inside its body."""
    label = v.get("label") or ("MOI" if v.get("me") else None)
    body = vehicle_sprite(v.get("kind", "car"), v.get("colour", "bleu"), label, rot)
    if v.get("siren") and v.get("kind") == "pompiers":
        body += siren_rays(0, -46)
    return _halo(bool(v.get("me"))) + body


def _vehicle_group(x, y, rot, v, goes=None) -> str:
    front = HALF_LENGTH[v.get("kind", "car")]
    arrow = intention_arrow(goes, front=front) if goes else ""
    return f'<g transform="translate({x},{y}) rotate({rot})">{_body(v, rot)}{arrow}</g>'


def draw_intersection(spec: dict) -> str:
    """Render an intersection scenario.

    spec keys:
      layout: "cross" | "T" (branch list given by `branches`, default all four)
      branches: subset of ["N","E","S","W"] present
      approaches: {A: {vehicle: {kind, colour, label, me, siren}, goes, sign, private, distance}}
      priority_road: e.g. ["N","S"]  (draws AB6 on those approaches unless sign overrides)
      caption: optional text under the diagram
      crosswalks: branches with a zebra crossing; pedestrian: the branch whose crossing is in use
      agent: bras_leve | bras_tendus_NS | bras_tendus_EW
      narrow: branches drawn as a one-lane street without centre line (a lane is still two car widths)
      parked: [{branch, side}] two cars parked along one kerb of a branch, next to the corner (side: compass
              point of that kerb, e.g. "S" for the southern kerb of the E branch)
      queue: {branch, count} stopped cars on the exit lane of a branch, bumper to bumper from the junction
      rails: branches whose lane carries tram rails even with no tram in the scene
    """
    branches = spec.get("branches") or ["N", "E", "S", "W"]
    approaches = spec.get("approaches", {})
    S = SVG(600, 600, view=(100, 100, 400, 400))
    cx, cy, half = 300, 300, 54  # half road width (2 lanes of 54 px)
    S.add(f'<rect x="0" y="0" width="600" height="600" fill="{GRASS}"/>')
    narrow = set(spec.get("narrow", []))
    hw = {b: (30 if b in narrow else half) for b in "NESW"}  # half width of each branch
    # roads
    if "N" in branches:
        S.add(f'<rect x="{cx-hw["N"]}" y="0" width="{2*hw["N"]}" height="{cy}" fill="{ASPHALT}"/>')
    if "S" in branches:
        S.add(f'<rect x="{cx-hw["S"]}" y="{cy}" width="{2*hw["S"]}" height="{600-cy}" fill="{ASPHALT}"/>')
    if "W" in branches:
        S.add(f'<rect x="0" y="{cy-hw["W"]}" width="{cx}" height="{2*hw["W"]}" fill="{ASPHALT}"/>')
    if "E" in branches:
        S.add(f'<rect x="{cx}" y="{cy-hw["E"]}" width="{600-cx}" height="{2*hw["E"]}" fill="{ASPHALT}"/>')
    S.add(f'<rect x="{cx-half}" y="{cy-half}" width="{2*half}" height="{2*half}" fill="{ASPHALT}"/>')
    # centre lines (dashed) up to the intersection square; a narrow street has none
    dash = 'stroke-dasharray="18 14"'
    if "N" in branches and "N" not in narrow:
        S.add(f'<line x1="{cx}" y1="0" x2="{cx}" y2="{cy-half}" stroke="{MARK}" stroke-width="3" {dash}/>')
    if "S" in branches and "S" not in narrow:
        S.add(f'<line x1="{cx}" y1="{cy+half}" x2="{cx}" y2="600" stroke="{MARK}" stroke-width="3" {dash}/>')
    if "W" in branches and "W" not in narrow:
        S.add(f'<line x1="0" y1="{cy}" x2="{cx-half}" y2="{cy}" stroke="{MARK}" stroke-width="3" {dash}/>')
    if "E" in branches and "E" not in narrow:
        S.add(f'<line x1="{cx+half}" y1="{cy}" x2="600" y2="{cy}" stroke="{MARK}" stroke-width="3" {dash}/>')
    # edge lines
    S.add(f'<g fill="none" stroke="{MARK}" stroke-width="2">')
    for b in branches:
        h = hw[b]
        if b == "N":
            S.add(f'<line x1="{cx-h}" y1="0" x2="{cx-h}" y2="{cy-half}"/><line x1="{cx+h}" y1="0" x2="{cx+h}" y2="{cy-half}"/>')
        if b == "S":
            S.add(f'<line x1="{cx-h}" y1="{cy+half}" x2="{cx-h}" y2="600"/><line x1="{cx+h}" y1="{cy+half}" x2="{cx+h}" y2="600"/>')
        if b == "W":
            S.add(f'<line x1="0" y1="{cy-h}" x2="{cx-half}" y2="{cy-h}"/><line x1="0" y1="{cy+h}" x2="{cx-half}" y2="{cy+h}"/>')
        if b == "E":
            S.add(f'<line x1="{cx+half}" y1="{cy-h}" x2="600" y2="{cy-h}"/><line x1="{cx+half}" y1="{cy+h}" x2="600" y2="{cy+h}"/>')
    # the edge line runs straight on across the side of a T where there is no branch
    closed = {"N": (cx - half, cy - half, cx + half, cy - half), "S": (cx - half, cy + half, cx + half, cy + half),
              "W": (cx - half, cy - half, cx - half, cy + half), "E": (cx + half, cy - half, cx + half, cy + half)}
    for b, (x1, y1, x2, y2) in closed.items():
        if b not in branches:
            S.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    S.add("</g>")
    for b in spec.get("rails", []):
        _rails(S, b, cx, cy, half)
    # a tram runs on rails laid in its lane, through the whole junction
    for a, ap in approaches.items():
        if (ap.get("vehicle") or {}).get("kind") == "tram":
            _rails(S, a, cx, cy, half)
    # transversal markings + private exits per approach
    for a, ap in approaches.items():
        if a not in branches:
            raise ValueError(f"approach {a} not in branches {branches}")
        sign = ap.get("sign")
        if sign == "stop":
            _transversal(S, a, cx, cy, half, "stop")
        elif sign == "cedez":
            _transversal(S, a, cx, cy, half, "cedez")
        elif sign and sign.startswith("feu_"):
            _transversal(S, a, cx, cy, half, "feux")
        if ap.get("private"):
            _private_exit(S, a, cx, cy, half)
    for a in spec.get("priority_road", []):
        if a in branches and approaches.get(a, {}).get("sign") is None:
            _sign(S, a, "prioritaire", cx, cy, half)
    for a, ap in approaches.items():
        sign = ap.get("sign")
        if sign in ("stop", "cedez", "prioritaire", "priorite_droite", "priorite_ponctuelle", "fin_prioritaire", "giratoire"):
            _sign(S, a, sign, cx, cy, half)
        elif sign and sign.startswith("feu_"):
            _light(S, a, sign.split("_", 1)[1], cx, cy, half)
    for b in spec.get("crosswalks", []):
        _crosswalk(S, b, cx, cy, half, walker=(b == spec.get("pedestrian")))
    if spec.get("agent"):
        _agent(S, cx, cy, spec["agent"])
    for p in spec.get("parked", []):  # two cars along a kerb, just past the corner (they mask the view)
        b, side = p["branch"], p["side"]
        for i in range(2):
            along = half + 34 + i * 92
            if b in ("E", "W"):
                x = cx + along if b == "E" else cx - along
                y = cy - hw[b] + 14 if side == "N" else cy + hw[b] - 14
                S.add(f'<g transform="translate({x},{y}) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
            else:
                y = cy - along if b == "N" else cy + along
                x = cx - hw[b] + 14 if side == "W" else cx + hw[b] - 14
                S.add(f'<g transform="translate({x},{y})">{vehicle_sprite("car", "gris")}</g>')
    if spec.get("queue"):  # stopped cars on the exit lane of a branch, first one just past the junction
        b, n = spec["queue"]["branch"], spec["queue"].get("count", 3)
        for i in range(n):
            d = half + 8 + HALF_LENGTH["car"] + i * 2 * (HALF_LENGTH["car"] + 4)
            x, y = {"N": (cx + hw["N"] / 2, cy - d), "S": (cx - hw["S"] / 2, cy + d),
                    "E": (cx + d, cy + hw["E"] / 2), "W": (cx - d, cy - hw["W"] / 2)}[b]
            S.add(_vehicle_group(x, y, _rot_for(opposite(b)), {"colour": "gris"}))
    for a, ap in approaches.items():
        v = ap.get("vehicle")
        if v:
            if a in narrow:
                x, y = _pos_on_approach(a, cx, cy, hw[a], ap.get("distance", 0), edge=half,
                                        length=HALF_LENGTH[v.get("kind", "car")])
                S.add(_vehicle_group(x, y, _rot_for(a), v, ap.get("goes")))
            else:
                _vehicle(S, a, v, ap.get("goes"), cx, cy, half, ap.get("distance", 0))
    if spec.get("caption"):
        S.caption(spec["caption"])
    return str(S)


def _pos_on_approach(a: str, cx, cy, half, dist, edge=None, length=42):
    """Centre point of a vehicle of half-length `length` waiting on its right-hand lane, its front
    28 + `dist` px before the junction edge.

    `half` is the road half-width (sets the lane); `edge` is the distance from the centre to the
    junction edge (defaults to `half`; the ring radius for a roundabout).
    """
    lane = half / 2  # centre of right-hand lane
    off = (half if edge is None else edge) + 28 + length + dist
    if a == "S":
        return cx + lane, cy + off
    if a == "N":
        return cx - lane, cy - off
    if a == "E":  # heading west: right-hand lane is the NORTH half of the east road
        return cx + off, cy - lane
    if a == "W":  # heading east: right-hand lane is the SOUTH half of the west road
        return cx - off, cy + lane
    raise ValueError(a)


def _vehicle(S: SVG, a, v, goes, cx, cy, half, dist):
    x, y = _pos_on_approach(a, cx, cy, half, dist, length=HALF_LENGTH[v.get("kind", "car")])
    S.add(_vehicle_group(x, y, _rot_for(a), v, goes))


def _rails(S: SVG, a, cx, cy, half):
    """Tram track along the lane of approach `a`, across the whole plane: a slightly paler strip carrying two rails
    about a track gauge apart, so rails read as a track even without a tram."""
    lane = half / 2
    if a in ("N", "S"):
        x = cx - lane if a == "N" else cx + lane
        S.add(f'<rect x="{x - 22}" y="0" width="44" height="600" fill="#5a5a5a"/>')
        for off in (-13, 13):
            S.add(f'<line x1="{x + off}" y1="0" x2="{x + off}" y2="600" stroke="{RAIL}" stroke-width="3.5"/>')
    else:
        y = cy - lane if a == "E" else cy + lane
        S.add(f'<rect x="0" y="{y - 22}" width="600" height="44" fill="#5a5a5a"/>')
        for off in (-13, 13):
            S.add(f'<line x1="0" y1="{y + off}" x2="600" y2="{y + off}" stroke="{RAIL}" stroke-width="3.5"/>')


def _transversal(S: SVG, a, cx, cy, half, kind="stop"):
    """Transverse line across the right-hand lane: stop (solid, wide), give-way (dashed, wide) or the line
    where traffic lights take effect (dashed, thin: IISR T'2 of 15 cm)."""
    w, dash = {"stop": (8, ""), "cedez": (8, 'stroke-dasharray="10 8"'), "feux": (4, 'stroke-dasharray="6 6"')}[kind]
    if a == "S":
        S.add(f'<line x1="{cx+2}" y1="{cy+half+6}" x2="{cx+half}" y2="{cy+half+6}" stroke="{MARK}" stroke-width="{w}" {dash}/>')
    elif a == "N":
        S.add(f'<line x1="{cx-half}" y1="{cy-half-6}" x2="{cx-2}" y2="{cy-half-6}" stroke="{MARK}" stroke-width="{w}" {dash}/>')
    elif a == "E":
        S.add(f'<line x1="{cx+half+6}" y1="{cy-half}" x2="{cx+half+6}" y2="{cy-2}" stroke="{MARK}" stroke-width="{w}" {dash}/>')
    elif a == "W":
        S.add(f'<line x1="{cx-half-6}" y1="{cy+2}" x2="{cx-half-6}" y2="{cy+half}" stroke="{MARK}" stroke-width="{w}" {dash}/>')


def _crosswalk(S: SVG, b, cx, cy, half, walker=False):
    """Zebra crossing across branch b just outside the intersection square, optionally with a pedestrian."""
    off = half + 24
    if b in ("N", "S"):
        y0 = cy - off - 26 if b == "N" else cy + off
        for x in range(int(cx - half + 6), int(cx + half - 6), 16):
            S.add(f'<rect x="{x}" y="{y0}" width="9" height="26" fill="{MARK}"/>')
        px, py = cx + half - 14, y0 + 13
    else:
        x0 = cx + off if b == "E" else cx - off - 26
        for y in range(int(cy - half + 6), int(cy + half - 6), 16):
            S.add(f'<rect x="{x0}" y="{y}" width="26" height="9" fill="{MARK}"/>')
        px, py = x0 + 13, cy + half - 14
    if walker:
        S.add(pedestrian(px, py))


def pedestrian(x, y, fill=PEDESTRIAN, scale=1.25) -> str:
    """A person on a plan (every card draws people with this figure); YELLOW `fill` for a high-visibility vest."""
    return (f'<g transform="translate({x},{y}) scale({scale})"><circle cx="0" cy="-14" r="6" fill="{fill}" stroke="#5a3a00" stroke-width="1"/>'
            f'<path d="M-6,-6 l12,0 l4,16 l-5,1 l-3,-8 l-3,14 l-6,0 l2,-14 l-3,7 l-5,-2 z" fill="{fill}" stroke="#5a3a00" stroke-width="1"/></g>')


def _private_exit(S: SVG, a, cx, cy, half):
    """Mark an approach as a private exit (parking/chemin): lighter surface, no markings, label."""
    text = f'font-family="{FONT}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff"'
    if a == "S":
        S.add(f'<rect x="{cx-half}" y="{cy+half}" width="{2*half}" height="{600-cy-half}" fill="#8a8a8a"/>')
        S.add(f'<text x="{cx}" y="491" {text}>PARKING</text>')
    elif a == "N":
        S.add(f'<rect x="{cx-half}" y="0" width="{2*half}" height="{cy-half}" fill="#8a8a8a"/>')
        S.add(f'<text x="{cx}" y="118" {text}>PARKING</text>')
    elif a == "E":
        S.add(f'<rect x="{cx+half}" y="{cy-half}" width="{600-cx-half}" height="{2*half}" fill="#8a8a8a"/>')
        S.add(f'<text x="486" y="{cy}" {text} transform="rotate(90 486 {cy})">PARKING</text>')
    elif a == "W":
        S.add(f'<rect x="0" y="{cy-half}" width="{cx-half}" height="{2*half}" fill="#8a8a8a"/>')
        S.add(f'<text x="114" y="{cy}" {text} transform="rotate(-90 114 {cy})">PARKING</text>')


def _sign(S: SVG, a, sign, cx, cy, half, px=54):
    """Place a sign on the right-hand verge of approach `a`, just before the intersection."""
    uri = sign_uri(sign)
    gap = 8
    if a == "S":
        x, y = cx + half + gap, cy + half + 10
    elif a == "N":
        x, y = cx - half - gap - px, cy - half - 10 - px
    elif a == "E":  # right verge of a west-bound vehicle = north side
        x, y = cx + half + 10, cy - half - gap - px
    elif a == "W":  # right verge of an east-bound vehicle = south side
        x, y = cx - half - 10 - px, cy + half + gap
    S.add(f'<image href="{uri}" x="{x}" y="{y}" width="{px}" height="{px}"/>')


def _light(S: SVG, a, colour, cx, cy, half):
    blink = colour == "orange_clignotant"
    if blink:
        colour = "orange"
    lit = {"vert": 2, "rouge": 0, "orange": 1}[colour]  # index of the lit lamp (red, amber, green)
    gap = 8
    w, h = 22, 58
    if a == "S":
        x, y = cx + half + gap, cy + half + 10
    elif a == "N":
        x, y = cx - half - gap - w, cy - half - 10 - h
    elif a == "E":
        x, y = cx + half + 10, cy - half - gap - h
    elif a == "W":
        x, y = cx - half - 10 - w, cy + half + gap
    S.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#222" stroke="#000"/>')
    for i, c in enumerate(["#d8362d", "#f08a24", "#2fa14b"]):
        S.add(f'<circle cx="{x+w/2}" cy="{y+11+i*18}" r="7" fill="{c if i == lit else "#555"}"/>')
    if blink:  # rays around the amber lamp: it flashes
        S.add(siren_rays(x + w / 2, y + 11 + 18, "#f08a24", r0=10, r1=16))


def agent_figure(pose: str) -> str:
    """Traffic officer seen from the front, in a 340 x 360 box.
    pose: bras_leve | bras_tendus | ralentir | avancer."""
    cx = 170  # room on the left for the motion marks of the "ralentir" gesture
    body, hand = "#1f3a93", "#f5d0b0"
    out = [f'<rect x="{cx - 28}" y="200" width="22" height="110" rx="8" fill="{body}"/><rect x="{cx + 6}" y="200" width="22" height="110" rx="8" fill="{body}"/>',
           f'<rect x="{cx - 40}" y="110" width="80" height="100" rx="14" fill="{body}"/>',
           f'<rect x="{cx - 40}" y="150" width="80" height="14" fill="#fff" opacity="0.85"/>',
           f'<circle cx="{cx}" cy="80" r="26" fill="{hand}"/>',
           f'<path d="M{cx - 30},70 q30,-30 60,0 l0,-8 q-30,-26 -60,0 z" fill="#0d1f5c"/><rect x="{cx - 34}" y="66" width="68" height="8" rx="3" fill="#0d1f5c"/>']

    def arm(x0, y0, x1, y1):
        out.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{body}" stroke-width="18" stroke-linecap="round"/>')
        out.append(f'<circle cx="{x1}" cy="{y1}" r="10" fill="{hand}"/>')

    ls, rs = (cx - 34, 122), (cx + 34, 122)  # shoulders (viewer's left / right)
    if pose == "bras_leve":
        arm(*rs, cx + 44, 22)
        arm(*ls, cx - 52, 200)
    elif pose == "bras_tendus":
        arm(*ls, cx - 130, 128)
        arm(*rs, cx + 130, 128)
    elif pose == "ralentir":
        arm(*ls, cx - 120, 170)
        arm(*rs, cx + 52, 200)
        # motion marks, drawn like those of "avancer": the outstretched arm swings up and down
        out.append(f'<path d="M{cx - 140},128 q-18,42 0,84" fill="none" stroke="#333" stroke-width="4" stroke-dasharray="7 6"/>')
        out.append(f'<path d="M{cx - 140},116 l-9,16 l17,-2 z" fill="#333"/>')
        out.append(f'<path d="M{cx - 140},224 l-9,-16 l17,2 z" fill="#333"/>')
    elif pose == "avancer":
        arm(*ls, cx - 100, 140)          # upper arm out
        arm(cx - 100, 140, cx - 70, 96)  # forearm swept back towards the chest
        arm(*rs, cx + 52, 200)
        out.append(f'<path d="M{cx - 150},130 q 10,-70 60,-70" fill="none" stroke="#333" stroke-width="4" stroke-dasharray="7 6"/>')
        out.append(f'<path d="M{cx - 90},60 l14,-10 l-2,18 z" fill="#333"/>')
        out.append(f'<path d="M{cx - 150},130 l-4,-18 l16,8 z" fill="#333"/>')
    else:
        raise ValueError(pose)
    return "".join(out)


def _agent(S: SVG, cx, cy, pose):
    """Traffic officer in the centre, seen from above. pose: 'bras_leve' | 'bras_tendus_NS' | 'bras_tendus_EW'.
    Outstretched arms are hi-vis yellow with a dark outline so their axis stays readable over the markings.
    A raised arm cannot be seen from above (drawn as an arm along the road it would read as an outstretched
    one): the officer is then drawn without arms and an inset shows the gesture face-on."""
    def arm(x1, y1, x2, y2):
        S.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="15" stroke-linecap="round"/>')
        S.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ffb300" stroke-width="9" stroke-linecap="round"/>')
        S.add(f'<circle cx="{x2}" cy="{y2}" r="7" fill="#f5d0b0" stroke="#222" stroke-width="2"/>')
    if pose == "bras_tendus_NS":  # arms along the N-S axis: N and S see the profile and pass, E and W stop
        arm(cx, cy, cx, cy - 56)
        arm(cx, cy, cx, cy + 56)
    elif pose == "bras_tendus_EW":
        arm(cx, cy, cx - 56, cy)
        arm(cx, cy, cx + 56, cy)
    elif pose != "bras_leve":
        raise ValueError(pose)
    S.add(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#1f3a93" stroke="#ffb300" stroke-width="4"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="11" fill="#f5d0b0"/>')
    if pose == "bras_leve":  # inset in the north-west corner (grass), linked to the officer
        x, y = S.view[0] + 8, S.view[1] + 8
        S.add(f'<path d="M{x + 120},{y + 110} L{cx - 24},{cy - 24}" stroke="{LABEL}" stroke-width="2" stroke-dasharray="5 4"/>')
        S.add(f'<rect x="{x}" y="{y}" width="124" height="134" rx="8" fill="#fff" stroke="{LABEL}" stroke-width="2"/>')
        S.add(f'<g transform="translate({x + 11},{y + 4}) scale(.3)">{agent_figure("bras_leve")}</g>')
        S.add(f'<text x="{x + 62}" y="{y + 124}" font-family="{FONT}" font-size="14" text-anchor="middle" fill="{LABEL}">vu de face</text>')


# ----------------------------------------------------------- roundabout ----
def draw_roundabout(spec: dict) -> str:
    """Roundabout with 4 branches. spec: giratoire (bool: AB25 signs), vehicles: list of
    {pos: 'inside'|'S'|'E'|'N'|'W', angle (for inside, degrees, 0 = east, counter-clockwise), colour, me, goes}"""
    S = SVG(600, 600, view=(45, 45, 510, 510))
    cx, cy = 300, 300
    R_out, R_in = 130, 60
    half = 54
    S.add(f'<rect x="0" y="0" width="600" height="600" fill="{GRASS}"/>')
    S.add(f'<rect x="{cx-half}" y="0" width="{2*half}" height="600" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="{cy-half}" width="600" height="{2*half}" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{R_out}" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{R_in}" fill="{GRASS}" stroke="{MARK}" stroke-width="3"/>')
    # give-way dashed lines at each entry if giratoire
    dash = 'stroke-dasharray="10 8"'
    if spec.get("giratoire", True):
        S.add(f'<line x1="{cx+2}" y1="{cy+R_out+2}" x2="{cx+half}" y2="{cy+R_out+2}" stroke="{MARK}" stroke-width="7" {dash}/>')
        S.add(f'<line x1="{cx-half}" y1="{cy-R_out-2}" x2="{cx-2}" y2="{cy-R_out-2}" stroke="{MARK}" stroke-width="7" {dash}/>')
        S.add(f'<line x1="{cx+R_out+2}" y1="{cy-half}" x2="{cx+R_out+2}" y2="{cy-2}" stroke="{MARK}" stroke-width="7" {dash}/>')
        S.add(f'<line x1="{cx-R_out-2}" y1="{cy+2}" x2="{cx-R_out-2}" y2="{cy+half}" stroke="{MARK}" stroke-width="7" {dash}/>')
        uri = sign_uri("giratoire")
        cede = sign_uri("cedez")
        # AB3a at the give-way line, AB25 on the same verge further from the ring
        for (x, y), (dx, dy) in zip([(cx+half+8, cy+R_out+6), (cx-half-8-50, cy-R_out-6-50), (cx+R_out+6, cy-half-8-50), (cx-R_out-6-50, cy+half+8)],
                                    [(0, 54), (0, -54), (54, 0), (-54, 0)]):
            S.add(f'<image href="{cede}" x="{x}" y="{y}" width="50" height="50"/>')
            S.add(f'<image href="{uri}" x="{x+dx}" y="{y+dy}" width="50" height="50"/>')
    else:
        uri = sign_data_uri(SIGN_FILES["priorite_droite"], 120)
        for (x, y) in [(cx+half+8, cy+R_out+30), (cx-half-8-50, cy-R_out-30-50), (cx+R_out+30, cy-half-8-50), (cx-R_out-30-50, cy+half+8)]:
            S.add(f'<image href="{uri}" x="{x}" y="{y}" width="50" height="50"/>')
    # rotation arrows on the ring: in France, traffic circulates counter-clockwise around the central island
    r = (R_out + R_in) / 2
    pt = lambda ang, rad=r: (cx + rad * math.cos(math.radians(ang)), cy - rad * math.sin(math.radians(ang)))  # noqa: E731
    for ang in (45, 135, 225, 315):
        (x0, y0), (x1, y1) = pt(ang), pt(ang + 16)
        S.add(f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 0 0 {x1:.1f},{y1:.1f}" fill="none" stroke="{MARK}" stroke-width="3"/>')
        (tx, ty), (ax, ay), (bx, by) = pt(ang + 25), pt(ang + 16, r - 7), pt(ang + 16, r + 7)
        S.add(f'<path d="M{tx:.1f},{ty:.1f} L{ax:.1f},{ay:.1f} L{bx:.1f},{by:.1f} Z" fill="{MARK}"/>')
    for v in spec.get("vehicles", []):
        pos = v["pos"]
        if pos == "inside":
            r = (R_out + R_in) / 2
            a = math.radians(v.get("angle", 270))
            x, y = cx + r * math.cos(a), cy - r * math.sin(a)
            # counter-clockwise travel: heading = angle + 90 (math), SVG rotation = 90 - heading = -angle
            S.add(_vehicle_group(round(x, 1), round(y, 1), -v.get("angle", 270), v))
        else:
            x, y = _pos_on_approach(pos, cx, cy, half, v.get("distance", 20), edge=R_out - 10,
                                    length=HALF_LENGTH[v.get("kind", "car")])
            S.add(_vehicle_group(x, y, _rot_for(pos), v, v.get("goes")))
    if spec.get("caption"):
        S.caption(spec["caption"])
    return str(S)


# ----------------------------------------------------------- road strip ----
ROAD_H = 480  # height of the road plane; vehicle and extra positions are given in % of it


def draw_road(spec: dict) -> str:
    """Straight two-way road seen from above, for overtaking / positioning / marking scenarios.

    spec:
      lanes: 2 (default) | 3 | 4 ; up_lanes: how many of them go my way (rightmost lanes)
      axis: "continue" | "discontinue" | "mixte_moi" (continuous on my side) | "mixte_autre" | "dissuasion" | "none"
      vehicles: [{lane: 1..n (1 = the vehicle's OWN rightmost lane: screen-right for 'up', screen-left for 'down'),
                  y: 0..100 (% from bottom), colour, kind, me, dir: 'up'|'down', goes, label, occludes}]
      caption, extras: list of {"kind": "virage"|"sommet"|"passage_pieton"|"intersection_droite"|"intersection_gauche"
                  |"sign"|"retrecissement"|"label"|"bau"|"ilot" (length), y}
    """
    H = ROAD_H
    lanes = spec.get("lanes", 2)
    lane_w = 90
    road_w = lanes * lane_w
    x0 = 300 - road_w / 2
    left, right = max(0, x0 - 70), min(600, x0 + road_w + 180)
    S = SVG(600, H, view=(left, 0, right - left, H))
    ypx = lambda pct: H - pct * H / 100  # noqa: E731
    S.add(f'<rect x="0" y="0" width="600" height="{H}" fill="{GRASS}"/>')
    S.add(f'<rect x="{x0}" y="0" width="{road_w}" height="{H}" fill="{ASPHALT}"/>')
    S.add(f'<line x1="{x0}" y1="0" x2="{x0}" y2="{H}" stroke="{MARK}" stroke-width="2"/>')
    S.add(f'<line x1="{x0+road_w}" y1="0" x2="{x0+road_w}" y2="{H}" stroke="{MARK}" stroke-width="2"/>')
    axis = spec.get("axis", "discontinue")
    # axis position: between the "down" lanes (left) and the "up" lanes (right, my direction).
    # Default: half the lanes for me, rounded up (2 -> 1, 3 -> 2, 4 -> 2).
    up_lanes = spec.get("up_lanes", lanes - lanes // 2)
    ax = x0 + (lanes - up_lanes) * lane_w

    def vline(x, style):
        if style == "continue":
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{MARK}" stroke-width="4"/>')
        elif style == "discontinue":
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 40"/>')
        elif style in ("dissuasion", "annonce"):
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{MARK}" stroke-width="4" stroke-dasharray="30 10"/>')
    if axis == "mixte_moi":  # continuous line on MY side (the line nearest my lane), dashed on the other
        vline(ax + 4, "continue"); vline(ax - 4, "discontinue")
    elif axis == "mixte_autre":  # dashed on my side, continuous on the oncoming side
        vline(ax + 4, "discontinue"); vline(ax - 4, "continue")
    elif axis == "double_continue":
        vline(ax - 4, "continue"); vline(ax + 4, "continue")
    elif axis != "none":
        vline(ax, axis)
    for sep in spec.get("lane_lines", []):
        vline(x0 + sep["at"] * lane_w, sep.get("style", "discontinue"))
    side = x0 + road_w + 10  # left edge of roadside labels and signs
    text = f'font-family="{FONT}" font-size="16" fill="{LABEL}"'
    for ex in spec.get("extras", []):
        y = ypx(ex.get("y", 50))
        k = ex["kind"]
        if k == "passage_pieton":
            for i in range(int(road_w // 24)):
                S.add(f'<rect x="{x0+6+i*24}" y="{y-20}" width="14" height="40" fill="{MARK}"/>')
        elif k == "intersection_droite":
            S.add(f'<rect x="{x0+road_w}" y="{y-40}" width="{600-x0-road_w}" height="80" fill="{ASPHALT}"/>')
        elif k == "intersection_gauche":
            S.add(f'<rect x="0" y="{y-40}" width="{x0}" height="80" fill="{ASPHALT}"/>')
        elif k == "sommet":  # crest: the road beyond is hidden
            S.add(f'<rect x="{x0}" y="{y-7}" width="{road_w}" height="14" fill="#7a7a7a"/>')
            S.add(f'<rect x="{x0}" y="0" width="{road_w}" height="{y-7}" fill="#000" opacity="0.18"/>')
            S.add(f'<text x="{side}" y="{y+6}" {text}>sommet de côte</text>')
        elif k == "virage":
            S.add(f'<text x="{side}" y="{y-2}" {text}>virage</text><text x="{side}" y="{y+16}" {text}>sans visibilité</text>')
            S.add(f'<path d="M{x0+road_w},{y-30} q40,-30 80,0" fill="none" stroke="{LABEL}" stroke-width="3" stroke-dasharray="6 6"/>')
        elif k == "sign":  # roadside sign, drawn large enough to be read on a phone
            uri = sign_data_uri(ex["file"], 200)
            S.add(f'<image href="{uri}" x="{side}" y="{y-48}" width="96" height="96"/>')
        elif k == "retrecissement":  # the road narrows to one central lane over a stretch
            top, bottom, w = y - 70, y + 70, (road_w - lane_w) / 2
            S.add(f'<path d="M{x0},{top-40} L{x0+w},{top} L{x0+w},{bottom} L{x0},{bottom+40} Z" fill="{GRASS}"/>')
            S.add(f'<path d="M{x0+road_w},{top-40} L{x0+road_w-w},{top} L{x0+road_w-w},{bottom} L{x0+road_w},{bottom+40} Z" fill="{GRASS}"/>')
            S.add(f'<path d="M{x0},{top-40} L{x0+w},{top} L{x0+w},{bottom} L{x0},{bottom+40}" fill="none" stroke="{MARK}" stroke-width="2"/>')
            S.add(f'<path d="M{x0+road_w},{top-40} L{x0+road_w-w},{top} L{x0+road_w-w},{bottom} L{x0+road_w},{bottom+40}" fill="none" stroke="{MARK}" stroke-width="2"/>')
        elif k == "label":  # free text beside the road, at the height of what it names
            S.add(f'<text x="{ex.get("x", side)}" y="{y+6}" {text}>{esc(str(ex["text"]))}</text>')
        elif k == "ilot":  # raised traffic island in the axis, announced at both ends by hatched (zebra) markings
            half, w = ex.get("length", 140) / 2, 48
            top, bottom = y - half, y + half
            S.add(f'<defs><pattern id="zebra" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
                  f'<rect width="6" height="14" fill="{MARK}"/></pattern></defs>')
            for tip, base in ((top - 100, top + 4), (bottom + 100, bottom - 4)):
                S.add(f'<path d="M{ax},{tip} L{ax - w / 2},{base} L{ax + w / 2},{base} Z" fill="url(#zebra)" stroke="{MARK}" stroke-width="3"/>')
            S.add(f'<rect x="{ax - w / 2}" y="{top}" width="{w}" height="{bottom - top}" rx="{w / 2}" fill="{GRASS}" stroke="{MARK}" stroke-width="4"/>')
        elif k == "bau":
            S.add(f'<rect x="{x0 + road_w}" y="0" width="70" height="{H}" fill="#5c5c5c"/>')
            S.add(f'<line x1="{x0 + road_w}" y1="0" x2="{x0 + road_w}" y2="{H}" stroke="{MARK}" stroke-width="4" stroke-dasharray="78 26"/>')
            S.add(f'<text x="{x0 + road_w + 35}" y="{H/2}" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff" '
                  f'transform="rotate(-90 {x0 + road_w + 35} {H/2})">bande d\'arrêt d\'urgence</text>')
    # A stopped or tall vehicle masks an angular sector, not a confirmed pedestrian. The sector is bounded by the
    # sight lines from my eye (driver's seat) through the two extreme corners of the obstacle; both head up.
    for obstacle in spec.get("vehicles", []):
        if not obstacle.get("occludes"):
            continue
        observer = next((v for v in spec["vehicles"] if v.get("me")), None)
        if (observer is None or obstacle.get("kind", "car") not in HALF_WIDTH or
                any(v.get("dir", "up") != "up" for v in (observer, obstacle))):
            raise ValueError("occludes requires a northbound car, truck, lorry or bus ahead of the northbound learner")
        ox = x0 + road_w - (observer["lane"] - .5) * lane_w - 12
        oy = ypx(observer["y"]) - 20
        bx, cy = x0 + road_w - (obstacle["lane"] - .5) * lane_w, ypx(obstacle["y"])
        hw, hl = HALF_WIDTH[obstacle.get("kind", "car")], HALF_LENGTH[obstacle.get("kind", "car")]
        if cy + hl >= oy:
            raise ValueError("the occluding vehicle must be ahead of the observer")
        corners = sorted(((bx + sx * hw, cy + sy * hl) for sx in (-1, 1) for sy in (-1, 1)),
                         key=lambda c: math.atan2(c[0] - ox, oy - c[1]))
        (lx_, ly_), (rx_, ry_) = corners[0], corners[-1]
        far = lambda x, y: (ox + (x - ox) * 40, oy + (y - oy) * 40)  # noqa: E731  (clipped by the frame)
        (flx, fly), (frx, fry) = far(lx_, ly_), far(rx_, ry_)
        S.add('<defs><pattern id="hidden" width="12" height="12" patternUnits="userSpaceOnUse">'
              '<path d="M-3 3L3-3 M0 12L12 0 M9 15L15 9" stroke="#bac2c5" stroke-width="2"/></pattern></defs>')
        S.add(f'<path d="M{lx_:.1f} {ly_:.1f}L{flx:.1f} {fly:.1f}L{frx:.1f} {fry:.1f}L{rx_:.1f} {ry_:.1f}Z" '
              'fill="url(#hidden)" stroke="#bac2c5" stroke-width="2"/>')
        S.add(f'<path d="M{ox} {oy}L{lx_} {ly_} M{ox} {oy}L{rx_} {ry_}" '
              'stroke="#bac2c5" stroke-width="1.5" stroke-dasharray="5 5"/>')
        # label beside the road below the obstacle; its leader ends just inside the sector's right edge
        ux, uy = (rx_ - ox), (ry_ - oy)
        d = math.hypot(ux, uy)
        vx, vy = (lx_ - ox) / math.hypot(lx_ - ox, ly_ - oy), (ly_ - oy) / math.hypot(lx_ - ox, ly_ - oy)
        tx, ty = ox + (ux / d * .85 + vx * .15) * (d + 50), oy + (uy / d * .85 + vy * .15) * (d + 50)
        lx, ly = side + 6, cy + hl + 40
        S.add(f'<path d="M{lx + 20} {ly - 20}L{tx:.1f} {ty:.1f}" fill="none" stroke="{LABEL}" stroke-width="2"/>')
        for dy, t in ((0, "Zone masquée"), (24, "depuis ma place")):
            S.add(f'<text x="{lx}" y="{ly + dy}" font-family="{FONT}" font-size="19" fill="{LABEL}">{t}</text>')
    for v in spec.get("vehicles", []):
        lane = v["lane"]
        if v.get("dir", "up") == "up":
            x = x0 + road_w - (lane - 0.5) * lane_w  # lane 1 = rightmost for an upward vehicle
            rot = 0
        else:
            x = x0 + (lane - 0.5) * lane_w  # lane 1 = rightmost for a downward vehicle (its right = our left)
            rot = 180
        S.add(_vehicle_group(x, ypx(v["y"]), rot, v, v.get("goes")))
    if spec.get("caption"):
        S.caption(spec["caption"])
    return str(S)


def render_png(svg: str, out: Path, width=600):
    import cairosvg
    out.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out), output_width=width)
    return out
