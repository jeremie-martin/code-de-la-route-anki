"""Procedural SVG diagrams for scenario cards (top-down views).

All diagrams share one visual identity: dark asphalt, white markings, soft green
surroundings, flat-colour vehicles with a windscreen showing the heading, real
road-sign pictograms (Commons SVG rasterised and embedded as data URIs).

Coordinate system: 600x600 px canvas, intersection centre at (300, 300).
Approaches are named by compass point of the ARRIVING vehicle: a vehicle on
approach "S" is south of the centre and heads north.
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


SIGN_FILES = {
    "stop": "France road sign AB4.svg",
    "cedez": "France road sign AB3a.svg",
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
    def __init__(self, w=600, h=600):
        self.w, self.h = w, h
        self.parts: list[str] = []

    def add(self, s: str):
        self.parts.append(s)

    def __str__(self):
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'
            + "".join(self.parts)
            + "</svg>"
        )


def _rot_for(approach: str) -> float:
    """Rotation (deg) that maps a north-heading sprite to the approach heading."""
    return {"S": 0, "E": 270, "N": 180, "W": 90}[approach]


def vehicle_sprite(kind: str, colour: str, label: str | None = None) -> str:
    """Sprite drawn heading NORTH (up), centred on origin."""
    c = CAR_COLOURS.get(colour, colour)
    label = esc(str(label)) if label else None
    stroke = "#111"
    if kind == "car":
        return (
            f'<g><rect x="-22" y="-42" width="44" height="84" rx="10" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-17" y="-30" width="34" height="16" rx="4" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<rect x="-17" y="18" width="34" height="12" rx="4" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<rect x="-19" y="-44" width="8" height="5" fill="#fff6c2"/><rect x="11" y="-44" width="8" height="5" fill="#fff6c2"/>'
            + (f'<text x="0" y="8" font-family="{FONT}" font-size="18" font-weight="700" text-anchor="middle" fill="#111">{label}</text>' if label else "")
            + "</g>"
        )
    if kind == "truck":
        return (
            f'<g><rect x="-26" y="-60" width="52" height="120" rx="6" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-26" y="-60" width="52" height="30" rx="6" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-20" y="-52" width="40" height="12" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            f'<line x1="-26" y1="-28" x2="26" y2="-28" stroke="{stroke}" stroke-width="2"/>'
            + (f'<text x="0" y="14" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle" fill="#111">{label}</text>' if label else "")
            + "</g>"
        )
    if kind == "bus":
        return (
            f'<g><rect x="-24" y="-64" width="48" height="128" rx="8" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-19" y="-56" width="38" height="12" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            + "".join(f'<rect x="-21" y="{y}" width="8" height="12" fill="#cfe6f7"/><rect x="13" y="{y}" width="8" height="12" fill="#cfe6f7"/>' for y in range(-36, 50, 20))
            + (f'<text x="0" y="8" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle" fill="#111">{label}</text>' if label else "")
            + "</g>"
        )
    if kind == "tram":
        return (
            f'<g><rect x="-20" y="-80" width="40" height="160" rx="12" fill="{c}" stroke="{stroke}" stroke-width="2"/>'
            f'<rect x="-15" y="-72" width="30" height="10" rx="3" fill="#cfe6f7" stroke="{stroke}" stroke-width="1.5"/>'
            + "".join(f'<rect x="-17" y="{y}" width="34" height="10" fill="#cfe6f7"/>' for y in range(-56, 70, 18))
            + f'<text x="0" y="6" font-family="{FONT}" font-size="14" font-weight="700" text-anchor="middle" fill="#111">TRAM</text></g>'
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
            f'<text x="0" y="14" font-family="{FONT}" font-size="12" font-weight="700" text-anchor="middle" fill="#fff">SOS</text></g>'
        )
    raise ValueError(kind)


def intention_arrow(goes: str, colour="#111") -> str:
    """Arrow drawn in front of a north-heading sprite showing intention."""
    if goes == "straight":
        path = "M0,-55 L0,-95"
        head = "M0,-100 L-8,-88 L8,-88 Z"
    elif goes == "right":
        path = "M0,-55 L0,-80 Q0,-90 10,-90 L30,-90"
        head = "M36,-90 L24,-98 L24,-82 Z"
    elif goes == "left":
        path = "M0,-55 L0,-80 Q0,-90 -10,-90 L-30,-90"
        head = "M-36,-90 L-24,-98 L-24,-82 Z"
    else:
        return ""
    return (
        f'<path d="{path}" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="{path}" fill="none" stroke="{colour}" stroke-width="3.5" stroke-linecap="round"/>'
        f'<path d="{head}" fill="{colour}" stroke="#fff" stroke-width="1.5"/>'
    )


def draw_intersection(spec: dict) -> str:
    """Render an intersection scenario.

    spec keys:
      layout: "cross" | "T" (branch list given by `branches`, default all four)
      branches: subset of ["N","E","S","W"] present
      approaches: {A: {vehicle: {kind, colour, label, me}, goes, sign, light, private}}
      priority_road: e.g. ["N","S"]  (draws AB6 on those approaches unless sign overrides)
      caption: optional text under the diagram
      marking: {"S": "stop"|"cedez"} transversal lines
    """
    branches = spec.get("branches") or ["N", "E", "S", "W"]
    approaches = spec.get("approaches", {})
    S = SVG(600, 640 if spec.get("caption") else 600)
    cx, cy, half = 300, 300, 54  # half road width (2 lanes of 54 px)
    S.add(f'<rect x="0" y="0" width="{S.w}" height="{S.h}" fill="{GRASS}"/>')
    # roads
    if "N" in branches:
        S.add(f'<rect x="{cx-half}" y="0" width="{2*half}" height="{cy}" fill="{ASPHALT}"/>')
    if "S" in branches:
        S.add(f'<rect x="{cx-half}" y="{cy}" width="{2*half}" height="{600-cy}" fill="{ASPHALT}"/>')
    if "W" in branches:
        S.add(f'<rect x="0" y="{cy-half}" width="{cx}" height="{2*half}" fill="{ASPHALT}"/>')
    if "E" in branches:
        S.add(f'<rect x="{cx}" y="{cy-half}" width="{600-cx}" height="{2*half}" fill="{ASPHALT}"/>')
    # centre lines (dashed) up to the intersection square
    dash = 'stroke-dasharray="18 14"'
    if "N" in branches:
        S.add(f'<line x1="{cx}" y1="0" x2="{cx}" y2="{cy-half}" stroke="{MARK}" stroke-width="3" {dash}/>')
    if "S" in branches:
        S.add(f'<line x1="{cx}" y1="{cy+half}" x2="{cx}" y2="600" stroke="{MARK}" stroke-width="3" {dash}/>')
    if "W" in branches:
        S.add(f'<line x1="0" y1="{cy}" x2="{cx-half}" y2="{cy}" stroke="{MARK}" stroke-width="3" {dash}/>')
    if "E" in branches:
        S.add(f'<line x1="{cx+half}" y1="{cy}" x2="600" y2="{cy}" stroke="{MARK}" stroke-width="3" {dash}/>')
    # edge lines
    S.add(f'<g fill="none" stroke="{MARK}" stroke-width="2">')
    for b in branches:
        if b == "N":
            S.add(f'<line x1="{cx-half}" y1="0" x2="{cx-half}" y2="{cy-half}"/><line x1="{cx+half}" y1="0" x2="{cx+half}" y2="{cy-half}"/>')
        if b == "S":
            S.add(f'<line x1="{cx-half}" y1="{cy+half}" x2="{cx-half}" y2="600"/><line x1="{cx+half}" y1="{cy+half}" x2="{cx+half}" y2="600"/>')
        if b == "W":
            S.add(f'<line x1="0" y1="{cy-half}" x2="{cx-half}" y2="{cy-half}"/><line x1="0" y1="{cy+half}" x2="{cx-half}" y2="{cy+half}"/>')
        if b == "E":
            S.add(f'<line x1="{cx+half}" y1="{cy-half}" x2="600" y2="{cy-half}"/><line x1="{cx+half}" y1="{cy+half}" x2="600" y2="{cy+half}"/>')
    S.add("</g>")
    # corner closures for missing branches (T intersections): draw grass edge line
    # transversal markings + signs + vehicles per approach
    for a, ap in approaches.items():
        if a not in branches:
            raise ValueError(f"approach {a} not in branches {branches}")
        sign = ap.get("sign")
        priv = ap.get("private")
        if sign == "stop":
            _transversal(S, a, cx, cy, half, solid=True)
        elif sign == "cedez":
            _transversal(S, a, cx, cy, half, solid=False)
        elif sign and sign.startswith("feu_"):
            _transversal(S, a, cx, cy, half, solid=True, thin=True)
        if priv:
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
        _crosswalk(S, b, cx, cy, half, pedestrian=(b == spec.get("pedestrian")))
    if spec.get("agent"):
        _agent(S, cx, cy, spec["agent"])
    for a, ap in approaches.items():
        v = ap.get("vehicle")
        if v:
            _vehicle(S, a, v, ap.get("goes"), cx, cy, half, ap.get("distance", 0))
    if spec.get("caption"):
        S.add(f'<rect x="0" y="600" width="600" height="40" fill="#ffffff"/>')
        S.add(f'<text x="300" y="626" font-family="{FONT}" font-size="18" text-anchor="middle" fill="#222">{esc(str(spec["caption"]))}</text>')
    return str(S)


def _pos_on_approach(a: str, cx, cy, half, dist, edge=None):
    """Centre point of a vehicle waiting on its right-hand lane at `dist` px from the stop line.

    `half` is the road half-width (sets the lane); `edge` is the distance from the centre to the
    stop line (defaults to `half`; the ring radius for a roundabout).
    """
    lane = half / 2  # centre of right-hand lane
    off = (half if edge is None else edge) + 60 + dist
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
    x, y = _pos_on_approach(a, cx, cy, half, dist)
    rot = _rot_for(a)
    body = vehicle_sprite(v.get("kind", "car"), v.get("colour", "bleu"), v.get("label"))
    arrow = intention_arrow(goes) if goes else ""
    me = v.get("me")
    halo = '<rect x="-30" y="-50" width="60" height="100" rx="14" fill="none" stroke="#f2c200" stroke-width="5"/>' if me else ""
    S.add(f'<g transform="translate({x},{y}) rotate({rot})">{halo}{body}{arrow}</g>')
    if me:
        # "MOI" label placed beside the vehicle
        S.add(f'<g transform="translate({x},{y}) rotate({rot})"><text x="0" y="66" font-family="{FONT}" font-size="15" font-weight="700" text-anchor="middle" fill="#111" transform="rotate({-rot})">MOI</text></g>')


def _transversal(S: SVG, a, cx, cy, half, solid=True, thin=False):
    """Stop line (solid) or give-way line (dashed) across the right-hand lane."""
    w = 4 if thin else 8
    dash = "" if solid else 'stroke-dasharray="10 8"'
    if a == "S":
        S.add(f'<line x1="{cx+2}" y1="{cy+half+6}" x2="{cx+half}" y2="{cy+half+6}" stroke="{MARK}" stroke-width="{w}" {dash}/>')
    elif a == "N":
        S.add(f'<line x1="{cx-half}" y1="{cy-half-6}" x2="{cx-2}" y2="{cy-half-6}" stroke="{MARK}" stroke-width="{w}" {dash}/>')
    elif a == "E":
        S.add(f'<line x1="{cx+half+6}" y1="{cy-half}" x2="{cx+half+6}" y2="{cy-2}" stroke="{MARK}" stroke-width="{w}" {dash}/>')
    elif a == "W":
        S.add(f'<line x1="{cx-half-6}" y1="{cy+2}" x2="{cx-half-6}" y2="{cy+half}" stroke="{MARK}" stroke-width="{w}" {dash}/>')


def _crosswalk(S: SVG, b, cx, cy, half, pedestrian=False):
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
    if pedestrian:
        S.add(f'<g transform="translate({px},{py})"><circle cx="0" cy="-14" r="6" fill="#e65100"/>'
              f'<path d="M-6,-6 l12,0 l4,16 l-5,1 l-3,-8 l-3,14 l-6,0 l2,-14 l-3,7 l-5,-2 z" fill="#e65100"/></g>')


def _private_exit(S: SVG, a, cx, cy, half):
    """Mark an approach as a private exit (parking/chemin): lighter surface, no markings, label."""
    if a == "S":
        S.add(f'<rect x="{cx-half}" y="{cy+half}" width="{2*half}" height="{600-cy-half}" fill="#8a8a8a"/>')
        S.add(f'<text x="{cx}" y="590" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff">PARKING</text>')
    elif a == "E":
        S.add(f'<rect x="{cx+half}" y="{cy-half}" width="{600-cx-half}" height="{2*half}" fill="#8a8a8a"/>')
        S.add(f'<text x="560" y="{cy+5}" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff">PARKING</text>')
    elif a == "W":
        S.add(f'<rect x="0" y="{cy-half}" width="{cx-half}" height="{2*half}" fill="#8a8a8a"/>')
        S.add(f'<text x="40" y="{cy+5}" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff">PARKING</text>')
    elif a == "N":
        S.add(f'<rect x="{cx-half}" y="0" width="{2*half}" height="{cy-half}" fill="#8a8a8a"/>')
        S.add(f'<text x="{cx}" y="20" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff">PARKING</text>')


def _sign(S: SVG, a, sign, cx, cy, half, px=54):
    """Place a sign on the right-hand verge of approach `a`, just before the intersection."""
    uri = sign_data_uri(SIGN_FILES[sign], 120)
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
    off = {"vert": 2, "rouge": 0, "orange": 1}[colour]  # index of the lit lamp (red, amber, green)
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
    if blink:
        S.add(f'<text x="{x+w/2}" y="{y+h+13}" font-family="{FONT}" font-size="11" '
              'text-anchor="middle" fill="#111">clignotant</text>')
    for i, c in enumerate(["#d8362d", "#f08a24", "#2fa14b"]):
        fill = c if i == off else "#555"
        S.add(f'<circle cx="{x+w/2}" cy="{y+11+i*18}" r="7" fill="{fill}"/>')


def _agent(S: SVG, cx, cy, pose):
    """Traffic officer in the centre. pose: 'bras_leve' | 'bras_tendus_NS' | 'bras_tendus_EW'."""
    S.add(f'<circle cx="{cx}" cy="{cy}" r="24" fill="#1f3a93" stroke="#fff" stroke-width="3"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#f5d0b0"/>')
    if pose == "bras_leve":
        S.add(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-46}" stroke="#fff" stroke-width="7" stroke-linecap="round"/>')
        S.add(f'<circle cx="{cx}" cy="{cy-48}" r="6" fill="#f5d0b0"/>')
    elif pose == "bras_tendus_NS":  # arms along the N-S axis: N and S see the profile and pass, E and W stop
        S.add(f'<line x1="{cx}" y1="{cy-46}" x2="{cx}" y2="{cy+46}" stroke="#fff" stroke-width="7" stroke-linecap="round"/>')
        S.add(f'<circle cx="{cx}" cy="{cy-48}" r="6" fill="#f5d0b0"/><circle cx="{cx}" cy="{cy+48}" r="6" fill="#f5d0b0"/>')
    elif pose == "bras_tendus_EW":
        S.add(f'<line x1="{cx-46}" y1="{cy}" x2="{cx+46}" y2="{cy}" stroke="#fff" stroke-width="7" stroke-linecap="round"/>')
        S.add(f'<circle cx="{cx-48}" cy="{cy}" r="6" fill="#f5d0b0"/><circle cx="{cx+48}" cy="{cy}" r="6" fill="#f5d0b0"/>')


# ----------------------------------------------------------- roundabout ----
def draw_roundabout(spec: dict) -> str:
    """Roundabout with 4 branches. spec: giratoire (bool: AB25 signs), vehicles: list of
    {pos: 'inside'|'S'|'E'|'N'|'W', angle (for inside, degrees, 0 = east, counter-clockwise), colour, me, goes}"""
    S = SVG(600, 640 if spec.get("caption") else 600)
    cx, cy = 300, 300
    R_out, R_in = 130, 60
    half = 54
    S.add(f'<rect x="0" y="0" width="{S.w}" height="{S.h}" fill="{GRASS}"/>')
    for a in ["N", "E", "S", "W"]:
        if a == "N":
            S.add(f'<rect x="{cx-half}" y="0" width="{2*half}" height="{cy}" fill="{ASPHALT}"/>')
        if a == "S":
            S.add(f'<rect x="{cx-half}" y="{cy}" width="{2*half}" height="{600-cy}" fill="{ASPHALT}"/>')
        if a == "W":
            S.add(f'<rect x="0" y="{cy-half}" width="{cx}" height="{2*half}" fill="{ASPHALT}"/>')
        if a == "E":
            S.add(f'<rect x="{cx}" y="{cy-half}" width="{600-cx}" height="{2*half}" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{R_out}" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{R_in}" fill="{GRASS}" stroke="{MARK}" stroke-width="3"/>')
    # give-way dashed lines at each entry if giratoire
    dash = 'stroke-dasharray="10 8"'
    if spec.get("giratoire", True):
        S.add(f'<line x1="{cx+2}" y1="{cy+R_out+2}" x2="{cx+half}" y2="{cy+R_out+2}" stroke="{MARK}" stroke-width="7" {dash}/>')
        S.add(f'<line x1="{cx-half}" y1="{cy-R_out-2}" x2="{cx-2}" y2="{cy-R_out-2}" stroke="{MARK}" stroke-width="7" {dash}/>')
        S.add(f'<line x1="{cx+R_out+2}" y1="{cy-half}" x2="{cx+R_out+2}" y2="{cy-2}" stroke="{MARK}" stroke-width="7" {dash}/>')
        S.add(f'<line x1="{cx-R_out-2}" y1="{cy+2}" x2="{cx-R_out-2}" y2="{cy+half}" stroke="{MARK}" stroke-width="7" {dash}/>')
        uri = sign_data_uri(SIGN_FILES["giratoire"], 120)
        cede = sign_data_uri(SIGN_FILES["cedez"], 120)
        # AB3a at the give-way line, AB25 on the same verge further from the ring
        for (x, y), (dx, dy) in zip([(cx+half+8, cy+R_out+6), (cx-half-8-50, cy-R_out-6-50), (cx+R_out+6, cy-half-8-50), (cx-R_out-6-50, cy+half+8)],
                                    [(0, 54), (0, -54), (54, 0), (-54, 0)]):
            S.add(f'<image href="{cede}" x="{x}" y="{y}" width="50" height="50"/>')
            S.add(f'<image href="{uri}" x="{x+dx}" y="{y+dy}" width="50" height="50"/>')
    else:
        uri = sign_data_uri(SIGN_FILES["priorite_droite"], 120)
        for (x, y) in [(cx+half+8, cy+R_out+30), (cx-half-8-50, cy-R_out-30-50), (cx+R_out+30, cy-half-8-50), (cx-R_out-30-50, cy+half+8)]:
            S.add(f'<image href="{uri}" x="{x}" y="{y}" width="50" height="50"/>')
    # rotation arrows on the ring (anti-clockwise as seen from above = counter-clockwise? In France traffic
    # circulates counter-clockwise around the central island when viewed from above.)
    for ang in (45, 135, 225, 315):
        r = (R_out + R_in) / 2
        a0 = math.radians(ang)
        x0, y0 = cx + r * math.cos(a0), cy - r * math.sin(a0)
        a1 = math.radians(ang + 14)
        x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
        S.add(f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 0 0 {x1:.1f},{y1:.1f}" fill="none" stroke="{MARK}" stroke-width="3"/>')
        a2 = math.radians(ang + 20)
        x2, y2 = cx + r * math.cos(a2), cy - r * math.sin(a2)
        S.add(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="4" fill="{MARK}"/>')
    for v in spec.get("vehicles", []):
        pos = v["pos"]
        body = vehicle_sprite(v.get("kind", "car"), v.get("colour", "bleu"), v.get("label"))
        halo = '<rect x="-30" y="-50" width="60" height="100" rx="14" fill="none" stroke="#f2c200" stroke-width="5"/>' if v.get("me") else ""
        if pos == "inside":
            r = (R_out + R_in) / 2
            a = math.radians(v.get("angle", 270))
            x, y = cx + r * math.cos(a), cy - r * math.sin(a)
            # heading tangent, counter-clockwise: direction of increasing angle
            # counter-clockwise travel: heading = angle + 90 (math), SVG rotation = 90 - heading = -angle
            rot = -v.get("angle", 270)
            S.add(f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})">{halo}{body}</g>')
        else:
            x, y = _pos_on_approach(pos, cx, cy, half, v.get("distance", 30), edge=R_out)
            rot = _rot_for(pos)
            arrow = intention_arrow(v["goes"]) if v.get("goes") else ""
            S.add(f'<g transform="translate({x},{y}) rotate({rot})">{halo}{body}{arrow}</g>')
        if v.get("me"):
            S.add(f'<text x="{x:.1f}" y="{y+70:.1f}" font-family="{FONT}" font-size="15" font-weight="700" text-anchor="middle" fill="#111">MOI</text>')
    if spec.get("caption"):
        S.add(f'<rect x="0" y="600" width="600" height="40" fill="#ffffff"/>')
        S.add(f'<text x="300" y="626" font-family="{FONT}" font-size="18" text-anchor="middle" fill="#222">{esc(str(spec["caption"]))}</text>')
    return str(S)


# ----------------------------------------------------------- road strip ----
def draw_road(spec: dict) -> str:
    """Straight two-way road seen from above, for overtaking / positioning / marking scenarios.

    spec:
      lanes: 2 (default) | 3 | 4 ; up_lanes: how many of them go my way (rightmost lanes)
      axis: "continue" | "discontinue" | "mixte_g" (continuous on my side) | "mixte_d" | "dissuasion" | "none"
      vehicles: [{lane: 1..n (1 = the vehicle's OWN rightmost lane: screen-right for 'up', screen-left for 'down'),
                  y: 0..100 (% from bottom), colour, kind, me, dir: 'up'|'down'}]
      caption, extras: list of {"kind": "virage"|"sommet"|"passage_pieton"|"intersection_droite", y}
    """
    S = SVG(600, 640 if spec.get("caption") else 600)
    lanes = spec.get("lanes", 2)
    lane_w = 90
    road_w = lanes * lane_w
    x0 = 300 - road_w / 2
    S.add(f'<rect x="0" y="0" width="{S.w}" height="{S.h}" fill="{GRASS}"/>')
    S.add(f'<rect x="{x0}" y="0" width="{road_w}" height="600" fill="{ASPHALT}"/>')
    S.add(f'<line x1="{x0}" y1="0" x2="{x0}" y2="600" stroke="{MARK}" stroke-width="2"/>')
    S.add(f'<line x1="{x0+road_w}" y1="0" x2="{x0+road_w}" y2="600" stroke="{MARK}" stroke-width="2"/>')
    axis = spec.get("axis", "discontinue")
    # axis position: between the "down" lanes (left) and the "up" lanes (right, my direction).
    # Default: half the lanes for me, rounded up (2 -> 1, 3 -> 2, 4 -> 2).
    up_lanes = spec.get("up_lanes", lanes - lanes // 2)
    ax = x0 + (lanes - up_lanes) * lane_w
    def vline(x, style):
        if style == "continue":
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="600" stroke="{MARK}" stroke-width="4"/>')
        elif style == "discontinue":
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="600" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 40"/>')
        elif style == "dissuasion":
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="600" stroke="{MARK}" stroke-width="4" stroke-dasharray="30 10"/>')
        elif style == "annonce":
            S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="600" stroke="{MARK}" stroke-width="4" stroke-dasharray="30 10"/>')
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
    for ex in spec.get("extras", []):
        y = 600 - ex.get("y", 50) * 6
        k = ex["kind"]
        if k == "passage_pieton":
            for i in range(int(road_w // 24)):
                S.add(f'<rect x="{x0+6+i*24}" y="{y-20}" width="14" height="40" fill="{MARK}"/>')
        elif k == "intersection_droite":
            S.add(f'<rect x="{x0+road_w}" y="{y-40}" width="{600-x0-road_w}" height="80" fill="{ASPHALT}"/>')
        elif k == "intersection_gauche":
            S.add(f'<rect x="0" y="{y-40}" width="{x0}" height="80" fill="{ASPHALT}"/>')
        elif k == "sommet":
            S.add(f'<rect x="{x0}" y="{y-6}" width="{road_w}" height="12" fill="#6c6c6c"/>')
            S.add(f'<text x="{x0+road_w+8}" y="{y+5}" font-family="{FONT}" font-size="14" fill="#333">sommet de côte</text>')
        elif k == "virage":
            S.add(f'<text x="{x0+road_w+8}" y="{y+5}" font-family="{FONT}" font-size="14" fill="#333">virage sans visibilité</text>')
            S.add(f'<path d="M{x0+road_w},{y-30} q40,-30 80,0" fill="none" stroke="#333" stroke-width="3" stroke-dasharray="6 6"/>')
        elif k == "sign":  # roadside sign, drawn large enough to be read on a phone
            uri = sign_data_uri(ex["file"], 200)
            S.add(f'<image href="{uri}" x="{x0+road_w+10}" y="{y-48}" width="96" height="96"/>')
        elif k == "retrecissement":  # the road narrows to one central lane over a stretch
            top, bottom, w = y - 70, y + 70, (road_w - lane_w) / 2
            for x in (x0, x0 + road_w - w):
                S.add(f'<path d="M{x},{top-40} L{x+w if x == x0 else x},{top} L{x+w if x == x0 else x},{bottom} L{x},{bottom+40} Z" fill="{GRASS}"/>'
                      if x == x0 else
                      f'<path d="M{x+w},{top-40} L{x},{top} L{x},{bottom} L{x+w},{bottom+40} Z" fill="{GRASS}"/>')
            S.add(f'<path d="M{x0},{top-40} L{x0+w},{top} L{x0+w},{bottom} L{x0},{bottom+40}" fill="none" stroke="{MARK}" stroke-width="2"/>')
            S.add(f'<path d="M{x0+road_w},{top-40} L{x0+road_w-w},{top} L{x0+road_w-w},{bottom} L{x0+road_w},{bottom+40}" fill="none" stroke="{MARK}" stroke-width="2"/>')
        elif k == "label":
            S.add(f'<text x="{ex.get("x", 20)}" y="{y}" font-family="{FONT}" font-size="15" fill="#222">{esc(str(ex["text"]))}</text>')
        elif k == "bau":
            S.add(f'<rect x="{x0 + road_w}" y="0" width="70" height="600" fill="#5c5c5c"/>')
            S.add(f'<line x1="{x0 + road_w}" y1="0" x2="{x0 + road_w}" y2="600" stroke="{MARK}" stroke-width="4" stroke-dasharray="78 26"/>')
            S.add(f'<text x="{x0 + road_w + 35}" y="300" font-family="{FONT}" font-size="13" text-anchor="middle" fill="#fff" transform="rotate(-90 {x0 + road_w + 35} 300)">bande d\'arrêt d\'urgence</text>')
    for v in spec.get("vehicles", []):
        lane = v["lane"]
        d = v.get("dir", "up")
        if d == "up":
            x = x0 + road_w - (lane - 0.5) * lane_w  # lane 1 = rightmost for an upward vehicle
            rot = 0
        else:
            x = x0 + (lane - 0.5) * lane_w  # lane 1 = rightmost for a downward vehicle (its right = our left)
            rot = 180
        y = 600 - v["y"] * 6
        body = vehicle_sprite(v.get("kind", "car"), v.get("colour", "bleu"), v.get("label"))
        halo = '<rect x="-30" y="-50" width="60" height="100" rx="14" fill="none" stroke="#f2c200" stroke-width="5"/>' if v.get("me") else ""
        arrow = intention_arrow(v["goes"]) if v.get("goes") else ""
        S.add(f'<g transform="translate({x},{y}) rotate({rot})">{halo}{body}{arrow}</g>')
        if v.get("me"):
            S.add(f'<text x="{x}" y="{y+68}" font-family="{FONT}" font-size="15" font-weight="700" text-anchor="middle" fill="#111">MOI</text>')
    if spec.get("caption"):
        S.add(f'<rect x="0" y="600" width="600" height="40" fill="#ffffff"/>')
        S.add(f'<text x="300" y="626" font-family="{FONT}" font-size="18" text-anchor="middle" fill="#222">{esc(str(spec["caption"]))}</text>')
    return str(S)


def render_png(svg: str, out: Path, width=600):
    import cairosvg
    out.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out), output_width=width)
    return out
