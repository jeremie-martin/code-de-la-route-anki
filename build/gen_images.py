"""Generated illustrations: road markings, traffic lights, officer signals, pictograms.

Each generator returns an SVG string. `render(name, params)` dispatches by name.
Visual identity matches build/diagrams.py (same asphalt, grass, marking colours).
"""
from __future__ import annotations

import math
import textwrap

from build.diagrams import (ASPHALT, GRASS, MARK, FONT, SVG, agent_figure, draw_road, draw_intersection, draw_roundabout,
                            vehicle_sprite, intention_arrow, siren_rays, sign_data_uri, esc, _body)

ME = _body({"me": True})  # the learner's car in decision scenes: blue, yellow halo, MOI (as in the scenarios)

YELLOW = "#f2c200"
SCALE = 12  # px per metre for marking strips (so 3 m dash = 36 px)


# ---------------------------------------------------------------- strips ---
def _strip(width=480, height=300, with_grass=True) -> SVG:
    S = SVG(width, height)
    S.add(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{GRASS if with_grass else "#ffffff"}"/>')
    return S


def _road_h(S: SVG, y0, y1, edge=True):
    S.add(f'<rect x="0" y="{y0}" width="{S.w}" height="{y1 - y0}" fill="{ASPHALT}"/>')
    if edge:
        S.add(f'<line x1="0" y1="{y0 + 4}" x2="{S.w}" y2="{y0 + 4}" stroke="{MARK}" stroke-width="2"/>')
        S.add(f'<line x1="0" y1="{y1 - 4}" x2="{S.w}" y2="{y1 - 4}" stroke="{MARK}" stroke-width="2"/>')


def _dashes_h(S: SVG, y, dash_m, gap_m, colour=MARK, w=5, x0=0, x1=None):
    x1 = S.w if x1 is None else x1
    x = x0
    while x < x1:
        S.add(f'<rect x="{x}" y="{y - w / 2}" width="{min(dash_m * SCALE, x1 - x)}" height="{w}" fill="{colour}"/>')
        x += (dash_m + gap_m) * SCALE


def _me_car(S: SVG, x, y, colour="bleu"):
    S.add(f'<g transform="translate({x},{y}) rotate(90)">{vehicle_sprite("car", colour)}</g>')


def ligne_axiale(params):
    """Central line seen from above: params style = continue|discontinue|dissuasion|mixte_moi|mixte_autre|double_continue|annonce"""
    S = _strip()
    _road_h(S, 60, 240)
    y = 150
    style = params.get("style", "discontinue")
    dash = params.get("dash", 3)
    gap = params.get("gap", 10)
    if style == "continue":
        S.add(f'<rect x="0" y="{y - 2.5}" width="{S.w}" height="5" fill="{MARK}"/>')
    elif style == "double_continue":
        S.add(f'<rect x="0" y="{y - 7}" width="{S.w}" height="5" fill="{MARK}"/><rect x="0" y="{y + 2}" width="{S.w}" height="5" fill="{MARK}"/>')
    elif style in ("discontinue", "dissuasion", "annonce"):
        _dashes_h(S, y, dash, gap)
    elif style == "mixte_moi":  # I drive at the bottom (left to right): the line on MY side is the lower one
        S.add(f'<rect x="0" y="{y + 2}" width="{S.w}" height="5" fill="{MARK}"/>')
        _dashes_h(S, y - 4.5, dash, gap)
    elif style == "mixte_autre":
        S.add(f'<rect x="0" y="{y - 7}" width="{S.w}" height="5" fill="{MARK}"/>')
        _dashes_h(S, y + 4.5, dash, gap)
    elif style == "continue_puis_discontinue":
        S.add(f'<rect x="0" y="{y - 2.5}" width="{S.w * 0.5}" height="5" fill="{MARK}"/>')
        _dashes_h(S, y, 3, 10, x0=S.w * 0.5)
    if params.get("me", True):
        _me_car(S, 70, 197)
    if params.get("label"):
        S.add(f'<text x="{S.w / 2}" y="285" font-family="{FONT}" font-size="16" text-anchor="middle" fill="#333">{esc(str(params["label"]))}</text>')
    return str(S)


def ligne_rive(params):
    """Edge line: style continue|discontinue, colour white; BAU variant."""
    S = _strip()
    _road_h(S, 60, 240, edge=False)
    style = params.get("style", "discontinue")
    if style == "bau":
        # motorway: right-hand edge line T4 (39 m / 13 m, scaled) separating the hard shoulder
        S.add(f'<rect x="0" y="60" width="{S.w}" height="180" fill="{ASPHALT}"/>')
        S.add(f'<rect x="0" y="190" width="{S.w}" height="50" fill="#5c5c5c"/>')
        S.add(f'<rect x="0" y="62" width="{S.w}" height="4" fill="{MARK}"/>')
        _dashes_h(S, 130, 3, 10, w=4)
        x = 0
        while x < S.w:
            S.add(f'<rect x="{x}" y="187" width="{min(156, S.w - x)}" height="6" fill="{MARK}"/>')
            x += 156 + 52
        _me_car(S, 70, 160)
        S.add(f'<g transform="translate(330,160) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
        return str(S)
    for y in (66, 234):
        if style == "continue":
            S.add(f'<rect x="0" y="{y - 2}" width="{S.w}" height="4" fill="{MARK}"/>')
        else:
            _dashes_h(S, y, params.get("dash", 3), params.get("gap", 3.5), w=4)
    _me_car(S, 70, 197)
    return str(S)


def ligne_jaune(params):
    """Yellow kerb-side line: continue (arrêt + stationnement interdits) or discontinue (stationnement interdit) or zigzag (bus)."""
    S = _strip()
    S.add(f'<rect x="0" y="0" width="{S.w}" height="200" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="200" width="{S.w}" height="100" fill="#bdbdbd"/>')  # trottoir
    S.add(f'<line x1="0" y1="200" x2="{S.w}" y2="200" stroke="#8a8a8a" stroke-width="3"/>')
    style = params.get("style", "continue")
    y = 191
    if style == "continue":
        S.add(f'<rect x="0" y="{y - 3}" width="{S.w}" height="6" fill="{YELLOW}"/>')
    elif style == "discontinue":
        _dashes_h(S, y, 1, 1, colour=YELLOW, w=6)
    elif style == "zigzag":
        pts = []
        x = 0
        up = True
        while x <= S.w:
            pts.append(f"{x},{182 if up else 198}")
            x += 24
            up = not up
        S.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{YELLOW}" stroke-width="5"/>')
    _dashes_h(S, 100, 3, 10)
    _me_car(S, 80, 150)
    S.add(f'<text x="{S.w - 12}" y="260" font-family="{FONT}" font-size="15" text-anchor="end" fill="#333">trottoir</text>')
    return str(S)


def fleches(params):
    """Arrows on the road: rabattement (lean toward the right, announce a continuous line) or directionnelles."""
    S = _strip()
    kind = params.get("kind", "rabattement")
    if kind == "rabattement":
        _road_h(S, 60, 240)
        # ligne d'annonce (T3 : 3 m / 1,33 m) puis ligne continue sur la droite
        _dashes_h(S, 150, 3, 10, x1=90)
        _dashes_h(S, 150, 3, 1.33, x0=90, x1=330)
        S.add(f'<rect x="330" y="147.5" width="150" height="5" fill="{MARK}"/>')
        for x in (120, 210, 290):
            # arrow astride the announcement line, pointing forward and into my lane
            S.add(f'<path d="M{x},150 l40,0 l0,-10 l20,14 l-20,14 l0,-10 l-40,0 z" fill="{MARK}" transform="rotate(20 {x + 30} 150)"/>')
        _me_car(S, 50, 197)
    elif kind == "directionnelles":
        # vertical road with 3 lanes at an intersection: left / straight / right
        S = SVG(480, 300)
        S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
        S.add(f'<rect x="90" y="0" width="300" height="300" fill="{ASPHALT}"/>')
        S.add(f'<rect x="0" y="0" width="480" height="60" fill="{ASPHALT}"/>')
        for x in (190, 290):
            S.add(f'<line x1="{x}" y1="70" x2="{x}" y2="300" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
        S.add(f'<rect x="90" y="66" width="300" height="6" fill="{MARK}"/>')
        # arrows: shaft 14 wide; turning arrows bend towards their side and keep inside their lane
        def arrow(cx, kind_):
            if kind_ == "straight":
                return f'<path d="M{cx - 7},240 V150 H{cx - 18} L{cx},112 L{cx + 18},150 H{cx + 7} V240 Z" fill="{MARK}"/>'
            k = -1 if kind_ == "left" else 1  # mirror of the right-turn arrow
            pts = [(-7, 240), (-7, 150), (-7, 134), (9, 128), (14, 128), (14, 112), (40, 135), (14, 158), (14, 142),
                   (9, 142), (7, 146), (7, 240)]
            d = " ".join(f"{'M' if i == 0 else 'L'}{cx + k * x},{y}" for i, (x, y) in enumerate(pts))
            return f'<path d="{d} Z" fill="{MARK}"/>'
        S.add(arrow(146, "left")); S.add(arrow(240, "straight")); S.add(arrow(334, "right"))
        S.add(f'<rect x="90" y="0" width="300" height="60" fill="{ASPHALT}"/>')
    elif kind == "insertion":
        pass
    return str(S)


def transversale(params):
    """Stop line (continuous) or give-way line (dashed) with sign; plus 'effet des feux'."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="120" y="0" width="240" height="300" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="0" width="480" height="80" fill="{ASPHALT}"/>')
    S.add(f'<line x1="240" y1="100" x2="240" y2="300" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
    kind = params.get("kind", "stop")
    if kind == "stop":
        S.add(f'<rect x="242" y="88" width="116" height="10" fill="{MARK}"/>')
    elif kind == "cedez":
        for x in range(244, 358, 20):
            S.add(f'<rect x="{x}" y="88" width="12" height="10" fill="{MARK}"/>')
    elif kind == "effet_feux":
        S.add(f'<line x1="244" y1="92" x2="358" y2="92" stroke="{MARK}" stroke-width="4" stroke-dasharray="6 6"/>')
        S.add(f'<rect x="366" y="40" width="22" height="58" rx="5" fill="#222"/>')
        for i, c in enumerate(["#d8362d", "#f08a24", "#2fa14b"]):
            S.add(f'<circle cx="377" cy="{51 + i * 18}" r="7" fill="{c if i == 0 else "#555"}"/>')
    S.add(f'<g transform="translate(300,220)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def passage(params):
    """Pedestrian crossing (bandes), cyclist crossing (carrés), or 'zebra' hatched area."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    kind = params.get("kind", "pieton")
    if kind in ("pieton", "cycliste"):
        S.add(f'<rect x="0" y="60" width="480" height="180" fill="{ASPHALT}"/>')
        S.add(f'<rect x="0" y="240" width="480" height="60" fill="#bdbdbd"/><rect x="0" y="0" width="480" height="60" fill="#bdbdbd"/>')
        if kind == "pieton":  # bands parallel to the road axis, stacked across the carriageway
            for y in range(68, 226, 22):
                S.add(f'<rect x="{200}" y="{y}" width="100" height="14" fill="{MARK}"/>')
        else:
            for y in range(68, 236, 26):
                for x in (200, 262):
                    S.add(f'<rect x="{x}" y="{y}" width="18" height="18" fill="{MARK}"/>')
                S.add(f'<rect x="231" y="{y + 13}" width="18" height="0" fill="{MARK}"/>')
        _dashes_h(S, 150, 3, 10, x1=190)
        _dashes_h(S, 150, 3, 10, x0=300)
        _me_car(S, 70, 197)
    elif kind == "zebra":
        S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
        # a triangular island with hatching between two diverging lanes
        S.add(f'<path d="M180,150 L420,80 L420,220 Z" fill="none" stroke="{MARK}" stroke-width="5"/>')
        S.add('<clipPath id="z"><path d="M180,150 L420,80 L420,220 Z"/></clipPath>')
        for x in range(180, 440, 18):
            S.add(f'<line x1="{x}" y1="60" x2="{x - 40}" y2="240" stroke="{MARK}" stroke-width="5" clip-path="url(#z)"/>')
        _dashes_h(S, 150, 3, 10, x1=170)
        _me_car(S, 60, 197)
    elif kind == "sas_velo":
        S.add(f'<rect x="120" y="0" width="240" height="300" fill="{ASPHALT}"/>')
        S.add(f'<rect x="0" y="0" width="480" height="70" fill="{ASPHALT}"/>')
        # the box covers my approach only, between two "effet des feux" lines (thin, dashed)
        S.add(f'<rect x="243" y="80" width="114" height="54" fill="#3aa657" opacity="0.85"/>')
        for y in (78, 134):
            S.add(f'<line x1="243" y1="{y}" x2="357" y2="{y}" stroke="{MARK}" stroke-width="4" stroke-dasharray="6 6"/>')
        S.add(f'<g transform="translate(300,105)"><circle cx="-10" cy="6" r="8" fill="none" stroke="{MARK}" stroke-width="3"/><circle cx="12" cy="6" r="8" fill="none" stroke="{MARK}" stroke-width="3"/><path d="M-10,6 l8,-14 l12,0 l2,14 M-2,-8 l6,14" fill="none" stroke="{MARK}" stroke-width="3"/></g>')
        S.add(f'<line x1="240" y1="80" x2="240" y2="300" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
        S.add(f'<rect x="364" y="30" width="22" height="58" rx="5" fill="#222"/>')
        for i, c in enumerate(["#d8362d", "#f08a24", "#2fa14b"]):
            S.add(f'<circle cx="375" cy="{41 + i * 18}" r="7" fill="{c if i == 0 else "#555"}"/>')
        S.add(f'<g transform="translate(300,220)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def chevrons(params):
    """Motorway chevrons (safety distance) or 'voie d'insertion' marking."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="50" width="480" height="200" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="52" width="480" height="4" fill="{MARK}"/>')
    _dashes_h(S, 150, 3, 10)
    _dashes_h(S, 246, 3, 3.5, w=4)  # BAU edge (rive discontinue)
    for x in (110, 260, 410):
        S.add(f'<path d="M{x},175 l18,25 l-18,25" fill="none" stroke="{MARK}" stroke-width="7"/>')
        S.add(f'<path d="M{x},75 l18,25 l-18,25" fill="none" stroke="{MARK}" stroke-width="7"/>')
    _me_car(S, 60, 200)
    S.add(f'<g transform="translate(330,200) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    return str(S)


def voie_texte(params):
    """Lane with painted text: BUS, TAXI, VÉLO... or a 'zone 30' marking."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
    _dashes_h(S, 152, 3, 1.33, w=7)
    txt = esc(str(params.get("text", "BUS")))
    S.add(f'<text x="240" y="225" font-family="{FONT}" font-size="46" font-weight="800" text-anchor="middle" fill="{MARK}" transform="scale(1,1.6) translate(0,-85)">{txt}</text>')
    if params.get("bike"):
        pass
    _me_car(S, 60, 100)
    return str(S)


# ----------------------------------------------------------------- feux ---
def _lamp(S, cx, cy, r, colour, on=True, blink=False):
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour if on else "#3a3a3a"}"/>')
    if on:
        S.add(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="{colour}" stroke-opacity="0.45" stroke-width="4"/>')
    if blink and on:
        for ang in range(0, 360, 45):
            a = math.radians(ang)
            x1, y1 = cx + (r + 9) * math.cos(a), cy + (r + 9) * math.sin(a)
            x2, y2 = cx + (r + 16) * math.cos(a), cy + (r + 16) * math.sin(a)
            S.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{colour}" stroke-width="3" stroke-linecap="round"/>')


RED, AMBER, GREEN = "#e53935", "#fb8c00", "#43a047"


def feu_tricolore(params):
    """state: rouge|orange|vert|orange_clignotant|eteint ; arrow: none|left|right|straight (fléché)"""
    S = SVG(240, 360)
    S.add('<rect x="0" y="0" width="240" height="360" fill="#ffffff"/>')
    S.add('<rect x="70" y="20" width="100" height="300" rx="16" fill="#222" stroke="#000" stroke-width="2"/>')
    state = params.get("state", "rouge")
    arrow = params.get("arrow")
    cols = [(RED, "rouge"), (AMBER, "orange"), (GREEN, "vert")]
    for i, (c, name) in enumerate(cols):
        on = state.startswith(name)
        blink = "clignotant" in state and on
        cy = 70 + i * 100
        if arrow:
            S.add(f'<circle cx="120" cy="{cy}" r="36" fill="{"#111" if on else "#3a3a3a"}"/>')
            S.add(_arrow_glyph(120, cy, c if on else "#555", arrow))
        else:
            _lamp(S, 120, cy, 36, c, on=on, blink=blink)
    if params.get("caption"):
        S.add(f'<text x="120" y="348" font-family="{FONT}" font-size="15" text-anchor="middle" fill="#333">{esc(str(params["caption"]))}</text>')
    return str(S)


def _arrow_glyph(cx, cy, colour, direction):
    rot = {"straight": 0, "right": 90, "left": -90}[direction]
    return (f'<g transform="translate({cx},{cy}) rotate({rot})">'
            f'<path d="M0,-24 l16,18 l-9,0 l0,30 l-14,0 l0,-30 l-9,0 z" fill="{colour}"/></g>')


def feu_fleche_composite(params):
    """Red main light + flashing amber arrow (or green arrow) on the side."""
    S = SVG(300, 360)
    S.add('<rect x="0" y="0" width="300" height="360" fill="#ffffff"/>')
    S.add('<rect x="40" y="20" width="100" height="300" rx="16" fill="#222" stroke="#000" stroke-width="2"/>')
    _lamp(S, 90, 70, 36, RED, on=True)
    _lamp(S, 90, 170, 36, AMBER, on=False)
    _lamp(S, 90, 270, 36, GREEN, on=False)
    S.add('<rect x="160" y="220" width="100" height="100" rx="16" fill="#222" stroke="#000" stroke-width="2"/>')
    colour = AMBER if params.get("colour", "orange") == "orange" else GREEN
    S.add('<circle cx="210" cy="270" r="36" fill="#111"/>')
    S.add(_arrow_glyph(210, 270, colour, params.get("direction", "right")))
    if params.get("blink", True):
        for ang in range(0, 360, 45):
            a = math.radians(ang)
            S.add(f'<line x1="{210 + 44 * math.cos(a):.1f}" y1="{270 + 44 * math.sin(a):.1f}" x2="{210 + 50 * math.cos(a):.1f}" y2="{270 + 50 * math.sin(a):.1f}" stroke="{colour}" stroke-width="3" stroke-linecap="round"/>')
    return str(S)


def feu_rouge_clignotant(params):
    """R24: single (or twin) red flashing light, e.g. level crossing, pont mobile, sortie de pompiers."""
    S = SVG(300, 240)
    S.add('<rect x="0" y="0" width="300" height="240" fill="#ffffff"/>')
    S.add('<rect x="60" y="40" width="180" height="120" rx="14" fill="#222" stroke="#000" stroke-width="2"/>')
    if params.get("twin", True):
        _lamp(S, 110, 100, 32, RED, on=True, blink=True)
        _lamp(S, 190, 100, 32, RED, on=False)
    else:
        _lamp(S, 150, 100, 36, RED, on=True, blink=True)
    S.add(f'<text x="150" y="205" font-family="{FONT}" font-size="15" text-anchor="middle" fill="#333">{esc(str(params.get("caption", "clignote")))}</text>')
    return str(S)


def feu_pieton(params):
    S = SVG(200, 360)
    S.add('<rect x="0" y="0" width="200" height="360" fill="#ffffff"/>')
    S.add('<rect x="50" y="30" width="100" height="240" rx="14" fill="#222" stroke="#000" stroke-width="2"/>')
    state = params.get("state", "rouge")
    # standing figure (red) / walking figure (green)
    S.add(f'<rect x="60" y="40" width="80" height="105" rx="8" fill="{"#3b0f0f" if state != "rouge" else "#111"}"/>')
    S.add(f'<rect x="60" y="155" width="80" height="105" rx="8" fill="{"#0f3b16" if state != "vert" else "#111"}"/>')
    rc = RED if state == "rouge" else "#5a2a2a"
    S.add(f'<g fill="{rc}"><circle cx="100" cy="62" r="10"/><rect x="88" y="74" width="24" height="36" rx="6"/><rect x="90" y="110" width="8" height="28"/><rect x="102" y="110" width="8" height="28"/></g>')
    gc = GREEN if state == "vert" else "#2a5a30"
    S.add(f'<g fill="{gc}"><circle cx="100" cy="176" r="10"/><path d="M92,188 l16,0 l6,30 l-8,2 l-4,-14 l-6,26 l-8,0 l4,-30 l-6,10 l-6,-4 z"/></g>')
    if params.get("blink"):
        for ang in range(0, 360, 60):
            a = math.radians(ang)
            S.add(f'<line x1="{100 + 52 * math.cos(a):.1f}" y1="{92 + 60 * math.sin(a):.1f}" x2="{100 + 58 * math.cos(a):.1f}" y2="{92 + 67 * math.sin(a):.1f}" stroke="{RED}" stroke-width="3"/>')
    return str(S)


def feu_bus(params):
    """R17/R18 white-bar signals for buses/trams: vertical = go, horizontal = stop, diagonal = turn allowed."""
    S = SVG(240, 300)
    S.add('<rect x="0" y="0" width="240" height="300" fill="#ffffff"/>')
    S.add('<rect x="60" y="30" width="120" height="240" rx="14" fill="#222" stroke="#000" stroke-width="2"/>')
    S.add('<circle cx="120" cy="150" r="52" fill="#111"/>')
    bar = params.get("bar", "vertical")
    rot = {"vertical": 0, "horizontal": 90, "diag_droite": 45, "diag_gauche": -45}[bar]
    S.add(f'<rect x="112" y="108" width="16" height="84" rx="6" fill="#ffffff" transform="rotate({rot} 120 150)"/>')
    return str(S)


def feu_velo(params):
    S = SVG(200, 320)
    S.add('<rect x="0" y="0" width="200" height="320" fill="#ffffff"/>')
    S.add('<rect x="60" y="30" width="80" height="240" rx="12" fill="#222" stroke="#000" stroke-width="2"/>')
    state = params.get("state", "vert")
    for i, (c, name) in enumerate([(RED, "rouge"), (AMBER, "orange"), (GREEN, "vert")]):
        cy = 70 + i * 80
        on = state == name
        S.add(f'<circle cx="100" cy="{cy}" r="28" fill="{"#111" if on else "#3a3a3a"}"/>')
        S.add(f'<g transform="translate(100,{cy})" fill="none" stroke="{c if on else "#555"}" stroke-width="3"><circle cx="-10" cy="6" r="8"/><circle cx="10" cy="6" r="8"/><path d="M-10,6 l7,-13 l11,0 l2,13 M-3,-7 l5,13"/></g>')
    return str(S)


def signal_affectation(params):
    """Lane-control signals above lanes: red cross = lane closed, green arrow = open, amber diagonal = move over."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="60" y="0" width="360" height="300" fill="{ASPHALT}"/>')
    for x in (180, 300):
        S.add(f'<line x1="{x}" y1="0" x2="{x}" y2="300" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
    S.add('<rect x="40" y="30" width="400" height="14" fill="#555"/>')
    states = params.get("lanes", ["croix", "fleche", "fleche"])
    for i, st in enumerate(states):
        cx = 120 + i * 120
        S.add(f'<rect x="{cx - 30}" y="44" width="60" height="60" rx="8" fill="#111"/>')
        if st == "croix":
            S.add(f'<path d="M{cx - 18},56 l36,36 M{cx + 18},56 l-36,36" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>')
        elif st == "fleche":  # green arrow pointing down: this lane is open
            S.add(f'<path d="M{cx},92 l16,-18 l-9,0 l0,-20 l-14,0 l0,20 l-9,0 z" fill="{GREEN}"/>')
        elif st == "rabattement_droite":  # flashing amber arrow slanting down-right: move to the next lane
            for ang in range(0, 360, 45):
                a = math.radians(ang)
                S.add(f'<line x1="{cx + 36 * math.cos(a):.1f}" y1="{74 + 36 * math.sin(a):.1f}" x2="{cx + 43 * math.cos(a):.1f}" y2="{74 + 43 * math.sin(a):.1f}" stroke="{AMBER}" stroke-width="3" stroke-linecap="round"/>')
            S.add(f'<path d="M{cx - 14},60 l22,22" fill="none" stroke="{AMBER}" stroke-width="6" stroke-linecap="round"/>')
            S.add(f'<path d="M{cx + 14},88 l-16,-2 l14,-14 z" fill="{AMBER}" stroke="{AMBER}" stroke-width="3" stroke-linejoin="round"/>')
        elif st == "rabattement_gauche":
            S.add(f'<path d="M{cx + 14},60 l-22,22" fill="none" stroke="{AMBER}" stroke-width="6" stroke-linecap="round"/>')
            S.add(f'<path d="M{cx - 14},88 l16,-2 l-14,-14 z" fill="{AMBER}" stroke="{AMBER}" stroke-width="3" stroke-linejoin="round"/>')
    S.add(f'<g transform="translate({120 + 120 * params.get("me_lane", 1)},230)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def feu_chantier(params):
    """KR11: temporary yellow-backed traffic light (chantier) or K5 flashing beacons."""
    S = SVG(240, 360)
    S.add('<rect x="0" y="0" width="240" height="360" fill="#ffffff"/>')
    S.add('<rect x="60" y="20" width="120" height="300" rx="10" fill="#f5c400" stroke="#000" stroke-width="2"/>')
    S.add('<rect x="80" y="40" width="80" height="260" rx="10" fill="#222"/>')
    state = params.get("state", "rouge")
    for i, (c, name) in enumerate([(RED, "rouge"), (AMBER, "orange"), (GREEN, "vert")]):
        _lamp(S, 120, 85 + i * 85, 30, c, on=(state == name))
    return str(S)


# ---------------------------------------------------------------- agent ---
def agent(params):
    """Traffic officer seen from the front. pose: bras_leve | bras_tendus | ralentir | avancer.

    Side-view ('profil') situations are drawn top-down with draw_intersection(agent=...) instead,
    because a frontal drawing cannot show unambiguously where the viewer stands.
    """
    S = SVG(340, 360)
    S.add('<rect x="0" y="0" width="340" height="360" fill="#ffffff"/>')
    S.add(agent_figure(params.get("pose", "bras_leve")))
    if params.get("caption_text"):
        S.add(f'<text x="170" y="345" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">{esc(str(params["caption_text"]))}</text>')
    return str(S)


# ----------------------------------------------------------- pictograms ---
def pictogramme_medicament(params):
    """ANSM medicine pictograms: niveau 1 (jaune), 2 (orange), 3 (rouge)."""
    level = int(params.get("niveau", 1))
    colour = {1: "#f7d117", 2: "#f28c00", 3: "#d8232a"}[level]
    text = {1: "Soyez prudent", 2: "Soyez très prudent", 3: "Attention, danger : ne pas conduire"}[level]
    sub = {1: "Ne pas conduire sans avoir lu la notice", 2: "Ne pas conduire sans l'avis d'un professionnel de santé", 3: "Pour la reprise de la conduite, demandez l'avis d'un médecin"}[level]
    S = SVG(420, 300)
    S.add('<rect x="0" y="0" width="420" height="300" fill="#ffffff"/>')
    S.add(f'<path d="M210,20 L400,190 L20,190 Z" fill="{colour}" stroke="#000" stroke-width="4" stroke-linejoin="round"/>')
    S.add(f'<g transform="translate(210,120)"><rect x="-38" y="-14" width="76" height="30" rx="8" fill="#000"/><rect x="-24" y="-30" width="48" height="20" rx="6" fill="#000"/><circle cx="-22" cy="20" r="8" fill="#000"/><circle cx="22" cy="20" r="8" fill="#000"/></g>')
    S.add(f'<text x="210" y="178" font-family="{FONT}" font-size="18" font-weight="800" text-anchor="middle" fill="#000">NIVEAU {level}</text>')
    S.add(f'<text x="210" y="225" font-family="{FONT}" font-size="18" font-weight="700" text-anchor="middle" fill="#000">{text}</text>')
    S.add(f'<text x="210" y="252" font-family="{FONT}" font-size="13" text-anchor="middle" fill="#333">{sub}</text>')
    return str(S)


def critair(params):
    """Crit'Air vignette classes 0 (green, electric/hydrogen), 1 (violet), 2 (yellow), 3 (orange), 4 (bordeaux), 5 (grey)."""
    cls = str(params.get("classe", "1"))
    col = {"0": "#4caf50", "1": "#7e57c2", "2": "#fdd835", "3": "#fb8c00", "4": "#8d2b2b", "5": "#616161"}[cls]
    label = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5"}[cls]
    S = SVG(300, 300)
    S.add('<rect x="0" y="0" width="300" height="300" fill="#ffffff"/>')
    S.add(f'<circle cx="150" cy="150" r="130" fill="{col}" stroke="#222" stroke-width="3"/>')
    S.add(f'<text x="150" y="112" font-family="{FONT}" font-size="26" font-weight="800" text-anchor="middle" fill="#fff">Crit\'Air</text>')
    S.add(f'<text x="150" y="215" font-family="{FONT}" font-size="96" font-weight="800" text-anchor="middle" fill="#fff">{label}</text>')
    if cls == "0":
        S.add(f'<text x="150" y="255" font-family="{FONT}" font-size="15" text-anchor="middle" fill="#fff">électrique / hydrogène</text>')
    return str(S)


def triangle_distance(params):
    """Broken-down car and warning triangle upstream; the measured gap is broken (≈) because it is not to scale."""
    S = SVG(480, 220)
    S.add(f'<rect x="0" y="0" width="480" height="220" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="120" fill="{ASPHALT}"/>')
    _dashes_h(S, 100, 3, 10, w=4)
    S.add(f'<g transform="translate(400,130) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    S.add('<path d="M66,150 l14,-26 l14,26 z" fill="#e53935" stroke="#fff" stroke-width="2"/>')
    S.add('<path d="M80,192 H222 M258,192 H362 M80,184 v16 M362,184 v16 M216,202 l12,-20 M246,202 l12,-20" '
          'stroke="#222" stroke-width="3" fill="none"/>')
    S.add(f'<text x="221" y="182" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle" fill="#222">{esc(str(params.get("label", "≈ 30 m")))}</text>')
    return str(S)


def road_scene(params):
    return draw_road(params)


def intersection_scene(params):
    return draw_intersection(params)


def roundabout_scene(params):
    return draw_roundabout(params)


REGISTRY = {
    "ligne_axiale": ligne_axiale, "ligne_rive": ligne_rive, "ligne_jaune": ligne_jaune, "fleches": fleches,
    "transversale": transversale, "passage": passage, "chevrons": chevrons, "voie_texte": voie_texte,
    "feu_tricolore": feu_tricolore, "feu_fleche_composite": feu_fleche_composite, "feu_rouge_clignotant": feu_rouge_clignotant,
    "feu_pieton": feu_pieton, "feu_bus": feu_bus, "feu_velo": feu_velo, "signal_affectation": signal_affectation,
    "feu_chantier": feu_chantier, "agent": agent, "pictogramme_medicament": pictogramme_medicament, "critair": critair,
    "triangle_distance": triangle_distance,
    "road": road_scene, "intersection": intersection_scene, "roundabout": roundabout_scene,
}


def render(name: str, params: dict | None = None) -> str:
    if name not in REGISTRY:
        raise KeyError(f"generator inconnu: {name}")
    return REGISTRY[name](params or {})


def tableau_lecture(params):
    """Clearly fictional documents: practise selecting a row, unit and column."""
    rows = params['rows']
    columns = params['columns']
    width, cell, top = 540, 540 / len(columns), 96
    height = top + 62 * (len(rows) + 1) + 2
    S = SVG(width, height)
    S.add(f'<rect width="{width}" height="{height}" fill="#fff"/>')
    S.add(f'<text x="270" y="32" font-family="{FONT}" font-size="20" text-anchor="middle" fill="#555">Exercice avec données fictives</text>')
    S.add(f'<text x="270" y="72" font-family="{FONT}" font-size="30" font-weight="700" text-anchor="middle" fill="#222">{esc(params["title"])}</text>')
    for row_index, row in enumerate([columns] + rows):
        if len(row) != len(columns):
            raise ValueError('tableau : nombre de colonnes incohérent')
        y = top + row_index * 62
        for col_index, value in enumerate(row):
            x = col_index * cell
            S.add(f'<rect x="{x}" y="{y}" width="{cell}" height="62" fill="{"#e7edf5" if row_index == 0 else "#fff"}" stroke="#aab4c0"/>')
            lines = textwrap.wrap(str(value), width=11, break_long_words=False, break_on_hyphens=False)
            if len(lines) > 2:
                raise ValueError('tableau : raccourcir le libellé de cellule')
            baseline = y + (39 if len(lines) == 1 else 24)
            spans = ''.join(f'<tspan x="{x + cell / 2}" y="{baseline + i * 28}">{esc(line)}</tspan>'
                            for i, line in enumerate(lines))
            S.add(f'<text font-family="{FONT}" font-size="28" text-anchor="middle" fill="#111">{spans}</text>')
    return str(S)


REGISTRY['tableau_lecture'] = tableau_lecture


# ------------------------------------------------------- extra markings ---
def voie_insertion(params):
    """Motorway with an acceleration lane on the right delimited by a T2-type short dashed line."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="150" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="42" width="480" height="4" fill="{MARK}"/>')
    _dashes_h(S, 115, 3, 10)
    # acceleration lane below the carriageway: full width where the ramp has joined, closed by a taper ahead
    S.add(f'<path d="M0,190 L480,190 L260,260 L0,260 Z" fill="{ASPHALT}"/>')
    _dashes_h(S, 190, 3, 3.5, w=5, x1=260)
    S.add(f'<path d="M260,260 L480,190 L480,192 L262,262 Z" fill="{MARK}"/>')
    S.add(f'<g transform="translate(130,226) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    S.add(f'<g transform="translate(330,150) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    return str(S)


def bande_cyclable(params):
    """Cycle lane on the right of the carriageway: T3 line + bike pictogram (optionally green surface)."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="42" width="480" height="4" fill="{MARK}"/>')
    _dashes_h(S, 140, 3, 10)
    if params.get("green"):
        S.add(f'<rect x="0" y="205" width="480" height="52" fill="#3aa657" opacity="0.7"/>')
    _dashes_h(S, 205, 3, 1.33, w=5)
    for x in (100, 300):
        S.add(f'<g transform="translate({x},232)" fill="none" stroke="{MARK}" stroke-width="3"><circle cx="-12" cy="8" r="9"/><circle cx="12" cy="8" r="9"/><path d="M-12,8 l8,-16 l14,0 l2,16 M-2,-8 l6,16"/></g>')
    S.add(f'<g transform="translate(80,170) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def damier(params):
    """Checkerboard marking: white (bus lane through junction) or red/white (escape lane start)."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
    colour = params.get("colour", "blanc")
    if colour == "blanc":  # bus lane crossing a junction: the checkerboard marks its continuity
        # opposite lane (top), my general lane, my bus lane along the kerb; a side street crosses
        S.add(f'<rect x="200" y="0" width="120" height="300" fill="{ASPHALT}"/>')
        for x0_, x1_ in ((0, 200), (320, 480)):
            _dashes_h(S, 110, 3, 10, w=4, x0=x0_, x1=x1_)
            _dashes_h(S, 186, 3, 1.33, w=6, x0=x0_, x1=x1_)
            S.add(f'<text x="{(x0_ + x1_) / 2}" y="240" font-family="{FONT}" font-size="30" font-weight="800" text-anchor="middle" fill="{MARK}">BUS</text>')
        x0, y0, size = 200, 190, 20
        for i in range(6):
            for j in range(3):
                if (i + j) % 2 == 0:
                    S.add(f'<rect x="{x0 + i * size}" y="{y0 + j * size}" width="{size}" height="{size}" fill="{MARK}"/>')
        _me_car(S, 70, 148)
        return str(S)
    x0, y0, size = 150, 80, 30
    for i in range(6):
        for j in range(6):
            fill = MARK if (i + j) % 2 == 0 else "#d8362d"
            S.add(f'<rect x="{x0 + i * size}" y="{y0 + j * size}" width="{size}" height="{size}" fill="{fill}"/>')
    S.add(f'<rect x="330" y="40" width="150" height="220" fill="#b9a27a"/>')
    return str(S)


def direction_voies(params):
    """Simplified gantry: each downward arrow identifies its corresponding lane."""
    S = SVG(560, 340)
    S.add(f'<rect width="560" height="340" fill="{GRASS}"/>')
    S.add(f'<rect x="30" y="210" width="500" height="130" fill="{ASPHALT}"/>')
    for x in (197, 363):
        S.add(f'<path d="M{x},220 V340" stroke="white" stroke-width="3" stroke-dasharray="15 20"/>')
    for x, width, label, arrows in ((35, 321, 'PARIS', (113, 280)), (366, 159, 'LYON', (446,))):
        S.add(f'<rect x="{x}" y="25" width="{width}" height="175" rx="8" fill="#0759a4" stroke="white" stroke-width="4"/>')
        S.add(f'<text x="{x + width / 2}" y="75" font-family="{FONT}" font-size="30" fill="white" text-anchor="middle">{label}</text>')
        for arrow in arrows:
            S.add(f'<path d="M{arrow},98 V167 m-17,-18 l17,18 17,-18" stroke="white" stroke-width="7" fill="none"/>')
    return str(S)


def ralentisseur(params):
    """Speed hump seen from above with white triangles (dos d'âne) or trapezoidal plateau with crossing."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="42" width="480" height="4" fill="{MARK}"/><rect x="0" y="254" width="480" height="4" fill="{MARK}"/>')
    _dashes_h(S, 150, 3, 10, x1=200)
    _dashes_h(S, 150, 3, 10, x0=300)
    kind = params.get("kind", "dos_d_ane")
    if kind == "dos_d_ane":
        S.add(f'<rect x="215" y="46" width="70" height="208" fill="#5a5a5a"/>')
        # IISR 7e partie, art. 118-9: three contiguous triangles on the rising ramp, apex in the direction of travel
        for y in (160, 186, 212):  # my lane (bottom), heading right: left ramp
            S.add(f'<path d="M216,{y} l26,12 l-26,12 z" fill="{MARK}"/>')
        for y in (52, 78, 104):  # opposite lane (top), heading left: right ramp
            S.add(f'<path d="M284,{y} l-26,12 l26,12 z" fill="{MARK}"/>')
    else:  # trapezoidal: ramp, flat plateau (here carrying a pedestrian crossing), ramp
        S.add(f'<rect x="170" y="46" width="30" height="208" fill="#5a5a5a"/><rect x="300" y="46" width="30" height="208" fill="#5a5a5a"/>')
        S.add(f'<rect x="200" y="46" width="100" height="208" fill="#6a6a6a"/>')
        for y in (160, 186, 212):
            S.add(f'<path d="M172,{y} l26,12 l-26,12 z" fill="{MARK}"/>')
        for y in (52, 78, 104):
            S.add(f'<path d="M328,{y} l-26,12 l26,12 z" fill="{MARK}"/>')
        for y in range(60, 236, 22):  # crossing bands parallel to the axis
            S.add(f'<rect x="206" y="{y}" width="88" height="12" fill="{MARK}"/>')
    S.add(f'<g transform="translate(90,190) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def marquage_temporaire(params):
    """Yellow temporary axis line overriding a white one near a worksite."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
    _dashes_h(S, 150, 3, 10, x1=180)
    # yellow line deviates to the right around a worksite
    S.add(f'<path d="M180,150 L260,150 L330,200 L480,200" fill="none" stroke="{YELLOW}" stroke-width="5" stroke-dasharray="36 20"/>')
    S.add(f'<rect x="300" y="46" width="180" height="120" fill="#7a6a5a"/>')
    for x in range(310, 480, 34):
        S.add(f'<path d="M{x},150 l8,-24 l8,24 z" fill="#e8501e" stroke="#fff" stroke-width="2"/>')
    S.add(f'<g transform="translate(80,205) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def zone_bleue(params):
    """Blue dashed line delimiting parking bays (zone bleue) along the kerb."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="200" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="200" width="480" height="100" fill="#bdbdbd"/>')
    _dashes_h(S, 100, 3, 10)
    S.add(f'<rect x="0" y="140" width="480" height="4" fill="#2d6fd8"/>')
    for x in range(60, 480, 110):
        S.add(f'<rect x="{x}" y="140" width="4" height="56" fill="#2d6fd8"/>')
    S.add(f'<g transform="translate(115,170) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<text x="420" y="265" font-family="{FONT}" font-size="15" text-anchor="end" fill="#333">trottoir</text>')
    return str(S)


def losange_sol(params):
    """White diamond painted in a reserved lane."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="220" fill="{ASPHALT}"/>')
    S.add(f'<line x1="0" y1="150" x2="480" y2="150" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
    for x in (120, 300):
        S.add(f'<path d="M{x},60 l22,35 l-22,35 l-22,-35 z" fill="none" stroke="{MARK}" stroke-width="6"/>')
    S.add(f'<g transform="translate(240,205) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    return str(S)


def cvcb(params):
    """Chaussée à voie centrale banalisée: central two-way lane and two side lanes for bikes."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="60" width="480" height="180" fill="{ASPHALT}"/>')
    _dashes_h(S, 100, 3, 1.33, w=4)
    _dashes_h(S, 200, 3, 1.33, w=4)
    for x in (60, 400):
        S.add(f'<g transform="translate({x},80)" fill="none" stroke="{MARK}" stroke-width="2.5"><circle cx="-9" cy="6" r="7"/><circle cx="9" cy="6" r="7"/><path d="M-9,6 l6,-12 l10,0 l2,12 M-1,-6 l4,12"/></g>')
        S.add(f'<g transform="translate({x},220)" fill="none" stroke="{MARK}" stroke-width="2.5"><circle cx="-9" cy="6" r="7"/><circle cx="9" cy="6" r="7"/><path d="M-9,6 l6,-12 l10,0 l2,12 M-1,-6 l4,12"/></g>')
    S.add(f'<g transform="translate(160,150) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    S.add(f'<g transform="translate(340,150) rotate(-90)">{vehicle_sprite("car", "rouge")}</g>')
    return str(S)


def livraison(params):
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="200" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="200" width="480" height="100" fill="#bdbdbd"/>')
    _dashes_h(S, 90, 3, 10)
    S.add(f'<path d="M150,198 V130 H430 V198" fill="none" stroke="{YELLOW}" stroke-width="5" stroke-dasharray="12 12"/>')
    S.add(f'<text x="290" y="174" font-family="{FONT}" font-size="24" font-weight="700" text-anchor="middle" fill="{YELLOW}">LIVRAISON</text>')
    _me_car(S, 60, 150)
    return str(S)


def direction_panel(params):
    """Direction sign mock-up in the official colour family."""
    colour = params.get("colour", "vert")
    bg, fg = {
        "bleu": ("#0053a0", "#ffffff"), "vert": ("#1f8a46", "#ffffff"), "blanc": ("#ffffff", "#111111"),
        "jaune": ("#f2c200", "#111111"), "marron": ("#7a4a2a", "#ffffff"), "velo": ("#ffffff", "#1f8a46"),
    }[colour]
    text = esc(str(params.get("text", "PARIS")))
    dist = esc(str(params.get("dist", "12")))
    S = SVG(420, 160)
    S.add('<rect x="0" y="0" width="420" height="160" fill="#ffffff"/>')
    S.add(f'<rect x="20" y="30" width="380" height="100" rx="6" fill="{bg}" stroke="#333" stroke-width="3"/>')
    S.add(f'<path d="M40,80 l30,-22 l0,12 l50,0 l0,20 l-50,0 l0,12 z" fill="{fg}"/>')
    S.add(f'<text x="140" y="92" font-family="{FONT}" font-size="34" font-weight="700" fill="{fg}">{text}</text>')
    S.add(f'<text x="385" y="92" font-family="{FONT}" font-size="30" font-weight="700" text-anchor="end" fill="{fg}">{dist}</text>')
    return str(S)


def lieu_dit(params):
    """E31 locality sign: black background, white ITALIC letters, thin white border (no red)."""
    S = SVG(420, 160)
    S.add('<rect x="0" y="0" width="420" height="160" fill="#ffffff"/>')
    S.add('<rect x="30" y="35" width="360" height="90" rx="4" fill="#111" stroke="#111" stroke-width="5"/>')
    S.add('<rect x="38" y="43" width="344" height="74" rx="2" fill="none" stroke="#ffffff" stroke-width="2"/>')
    S.add(f'<text x="210" y="94" font-family="{FONT}" font-size="36" font-weight="700" font-style="italic" text-anchor="middle" fill="#ffffff">{esc(str(params.get("text", "Le Bourg")))}</text>')
    return str(S)


def rappel_limites(params):
    """C25a: reminder of the general speed limits at the border, four rows with their road pictograms."""
    S = SVG(360, 560)
    S.add('<rect x="0" y="0" width="360" height="560" rx="14" fill="#0e4aa5" stroke="#fff" stroke-width="4"/>')
    S.add(f'<text x="180" y="66" font-family="{FONT}" font-size="44" font-weight="800" text-anchor="middle" fill="#fff">FRANCE</text>')
    rows = [("50", "ville"), ("80", "hors_ville"), ("110", "separee"), ("130", "autoroute")]
    for i, (speed, picto) in enumerate(rows):
        y = 96 + i * 112
        S.add(f'<rect x="24" y="{y}" width="312" height="100" rx="6" fill="#fff"/>')
        S.add(f'<circle cx="94" cy="{y + 50}" r="40" fill="#fff" stroke="#d8362d" stroke-width="10"/>')
        S.add(f'<text x="94" y="{y + 63}" font-family="{FONT}" font-size="{34 if len(speed) == 3 else 38}" font-weight="800" text-anchor="middle" fill="#111">{speed}</text>')
        gx, gy = 250, y + 50
        if picto in ("ville", "hors_ville"):
            S.add(f'<path d="M{gx-46},{gy+22} v-22 h12 v-16 h10 v16 h8 v-30 h12 v30 h10 v-12 h10 v12 h12 v-24 h12 v24 h12 v22 z" fill="#111"/>')
            if picto == "hors_ville":
                S.add(f'<line x1="{gx-46}" y1="{gy+24}" x2="{gx+42}" y2="{gy-22}" stroke="#d8362d" stroke-width="8"/>')
        elif picto == "separee":  # two carriageways with a central reservation
            S.add(f'<rect x="{gx-40}" y="{gy-28}" width="30" height="56" fill="#111"/><rect x="{gx+10}" y="{gy-28}" width="30" height="56" fill="#111"/>')
            S.add(f'<rect x="{gx-12}" y="{gy-28}" width="24" height="56" fill="#2fa14b"/>')
        else:  # motorway pictogram
            S.add(f'<rect x="{gx-44}" y="{gy-34}" width="88" height="68" rx="6" fill="#0e4aa5"/>')
            S.add(f'<path d="M{gx-30},{gy+30} L{gx-12},{gy-26} M{gx+30},{gy+30} L{gx+12},{gy-26} M{gx},{gy+30} V{gy-26}" stroke="#fff" stroke-width="5"/>')
            S.add(f'<rect x="{gx-44}" y="{gy-10}" width="88" height="9" fill="#fff"/>')
    return str(S)


def feu_bicolore(params):
    """R23 two-colour light (red / green), one vehicle per green (contrôle individuel)."""
    S = SVG(240, 300)
    S.add('<rect x="0" y="0" width="240" height="300" fill="#ffffff"/>')
    S.add('<rect x="70" y="30" width="100" height="220" rx="16" fill="#222" stroke="#000" stroke-width="2"/>')
    state = params.get("state", "rouge")
    _lamp(S, 120, 80, 36, RED, on=(state == "rouge"))
    _lamp(S, 120, 190, 36, GREEN, on=(state == "vert"))
    return str(S)


def _draw_cone(S):
    """Shared K5a symbol, in its original 240 × 300 coordinate space."""
    S.add('<rect x="50" y="240" width="140" height="18" rx="4" fill="#e8501e" stroke="#333" stroke-width="2"/>')
    S.add('<path d="M100,40 L140,40 L180,240 L60,240 Z" fill="#e8501e" stroke="#333" stroke-width="2"/>')
    S.add('<path d="M92,80 L148,80 L156,120 L84,120 Z" fill="#ffffff"/>')
    S.add('<path d="M78,150 L162,150 L170,190 L70,190 Z" fill="#ffffff"/>')


def cone(params):
    S = SVG(240, 300)
    S.add('<rect x="0" y="0" width="240" height="300" fill="#ffffff"/>')
    _draw_cone(S)
    return str(S)


# These scenes share one carriageway: traffic upwards, median left, shoulder right.
def _motorway_scene():
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add('<path d="M60 0H85V440H60Z" fill="#aeb7a8"/>')
    S.add(f'<path d="M85 0H440V440H85Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M92 0V440 M433 0V440" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<path d="M225 0V440" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 18"/>')
    S.add(f'<path d="M365 0V440" stroke="{MARK}" stroke-width="5" stroke-dasharray="78 26"/>')
    return S


def _flr_panel(sign_uri):
    """Face-on FLR, left arrow active. IISR 8, annexes VI/VII (VC20250904)."""
    S = SVG(110, 180)
    # Red/white chevrons on the frame; inactive bulbs stay dark.
    S.add('<rect width="110" height="180" fill="#fff"/>')
    for y in range(-60, 200, 36):
        S.add(f'<path d="M0 {y}L55 {y-55}L110 {y}V{y+18}L55 {y-37}L0 {y+18}Z" fill="#d8362d"/>')
    S.add('<rect x="25" y="27" width="60" height="66" fill="#303638"/>')
    left = [(10, 82), (10, 68), (10, 54), (10, 40),
            (23, 82), (36, 82), (49, 82)]
    left += [(28 + 9*i, 64 - 10*i) for i in range(6)]
    right = {(110-x, y) for x, y in left}
    # The diagonals share their crossing lamp; the bottom row has eight distinct lamps.
    for x, y in sorted(right - set(left)):
        S.add(f'<circle cx="{x}" cy="{y}" r="5" fill="#45494a" stroke="#222"/>')
    for x, y in left:
        S.add(f'<circle cx="{x}" cy="{y}" r="5" fill="#ffe34a" stroke="#987f12" stroke-width=".6"/>')
    for x in (10, 100):
        S.add(f'<circle cx="{x}" cy="12" r="7" fill="#ffe34a" stroke="#987f12"/>')
    S.add(f'<image x="23" y="108" width="64" height="64" xlink:href="{sign_uri}"/>')
    return str(S)


def chantier_rabattement(params):
    """Two offset FLRs; enlarged face shows the signal, never a driving trajectory."""
    S = _motorway_scene()
    uri = sign_data_uri(params["sign"]["file"], 160)
    panel = _flr_panel(uri)
    # Longitudinal work boundary beyond the position unit. Distances are not to scale.
    S.add('<path d="M237 0H358V36H237Z" fill="#c9b99b"/>')
    for y in (18, 48):
        S.add(f'<g transform="translate(234,{y}) scale(.14) translate(-120,-249)">')
        _draw_cone(S)
        S.add('</g>')
    # Each trailer's panel is shown face-on within this plan view, like roadside signs.
    for x, y in ((295, 100), (365, 248)):
        S.add(f'<g transform="translate({x-27.5},{y-45}) scale(.5)">{panel}</g>')
        S.add(f'<path d="M{x-20} {y+49}h40" stroke="#222" stroke-width="6"/>')
    S.add(f'<g transform="translate(295,370) scale(1.5)">{ME}</g>')
    S.add('<path d="M397 244L469 220" stroke="#687475" stroke-width="2"/>')
    S.add(f'<g transform="translate(480,125)">{panel}</g>')
    S.add(f'<text x="535" y="106" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#263336">Signal agrandi</text>')
    return str(S)


def corridor_securite(params):
    """An adjacent car prevents an immediate lane change past a shoulder recovery."""
    S = _motorway_scene()
    S.add(f'<g transform="translate(155,335) scale(1.5)">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<g transform="translate(295,350) scale(1.5)">{ME}</g>')
    # Recovery vehicle: existing truck cab, flat bed, secured car and amber beacon.
    S.add(f'<g transform="translate(399,129) scale(1.35)">{vehicle_sprite("truck", "orange")}')
    S.add('<rect x="-23" y="-25" width="46" height="81" fill="#71787a"/>')
    S.add(f'<g transform="translate(0,15) scale(.75)">{vehicle_sprite("car", "gris")}</g>')
    S.add('<rect x="-16" y="-31" width="32" height="7" rx="2" fill="#ffc438" stroke="#805b14"/>')
    S.add(siren_rays(0, -28, "#f08a24", r0=14, r1=22))
    S.add('</g>')
    S.add(f'<text x="399" y="240" text-anchor="middle" font-family="{FONT}" font-size="26" fill="{MARK}">BAU</text>')
    return str(S)


def cycliste_tourne_droite(params):
    """Cycle track continues across a side street; both users have yet to reach it."""
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add('<path d="M97 0H472V440H97Z M370 98H640V252H370Z" fill="#ced6c8"/>')
    S.add(f'<path d="M110 0H370V440H110Z M370 110H640V240H370Z" fill="{ASPHALT}"/>')
    # Physically separate one-way cycle track, crossing the mouth of the side street.
    S.add(f'<path d="M398 0H456V440H398Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M240 0V440" stroke="{MARK}" stroke-width="3" stroke-dasharray="22 18"/>')
    S.add(f'<path d="M117 0V440 M363 0V110H398 M456 110H640 M363 440V240H398 M456 240H640" fill="none" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<path d="M402 0V110 M452 0V110 M402 240V440 M452 240V440" stroke="{MARK}" stroke-width="2"/>')
    S.add(f'<g transform="translate(312,318) scale(1.5)">{ME}{intention_arrow("right")}</g>')
    S.add(f'<g transform="translate(427,345) scale(.85)">{vehicle_sprite("bike", "rouge")}</g>')
    S.add(f'<path d="M427 300v-35m-7 8l7-9 7 9" fill="none" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<text x="477" y="342" font-family="{FONT}" font-size="26" fill="#263336">Piste</text>')
    S.add(f'<text x="477" y="374" font-family="{FONT}" font-size="26" fill="#263336">cyclable</text>')
    return str(S)


def giratoire_sortie(params):
    """Two lanes, one intended exit; no suggested crossing of the cyclist's lane."""
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add(f'<path d="M190 0H290V440H190Z M0 165H640V275H0Z" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="240" cy="220" r="195" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="240" cy="220" r="60" fill="{GRASS}" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<circle cx="240" cy="220" r="128" fill="none" stroke="{MARK}" stroke-width="3" stroke-dasharray="18 15"/>')
    S.add(f'<path d="M437 220H640 M240 0V23 M240 417V440 M0 220H43" stroke="{MARK}" stroke-width="3"/>')
    for x1,y1,x2,y2 in ((440,168,440,216),(193,22,236,22),(244,418,287,418),(40,224,40,272)):
        S.add(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{MARK}" stroke-width="6" stroke-dasharray="8 6"/>')
    # Shared symbols retain readable silhouettes, with the bicycle smaller than the car.
    for radius, angle, kind, colour, scale in ((94, -32, "car", "bleu", 1.0), (162, -30, "bike", "rouge", .9)):
        a = math.radians(angle)
        x, y = 240 + radius*math.cos(a), 220 - radius*math.sin(a)
        sprite = _body({"me": True}, -angle) if colour == "bleu" else vehicle_sprite(kind, colour)
        S.add(f'<g transform="translate({x},{y}) rotate({-angle}) scale({scale})">{sprite}</g>')
    S.add(f'<path d="M485 248h98m-12-8 12 8-12 8" fill="none" stroke="{MARK}" stroke-width="4"/>')
    S.add(f'<text x="537" y="314" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#263336">Sortie visée</text>')
    return str(S)


def entrecroisement(params):
    """Separate ramps join one shared weaving lane beside the motorway."""
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add('<path d="M45 0H70V440H45Z" fill="#aeb7a8"/>')
    S.add(f'<path d="M70 0H310V440H70Z M460 0H560L410 135V305L560 440H460L310 305V135Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M77 0V440 M303 0V128 M303 312V440" fill="none" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<path d="M190 0V440" stroke="{MARK}" stroke-width="3" stroke-dasharray="22 18"/>')
    S.add(f'<path d="M310 135V305" stroke="{MARK}" stroke-width="5" stroke-dasharray="12 14"/>')
    S.add(f'<path d="M460 0L310 135 M560 0L410 135V305L560 440 M310 305L460 440" '
          f'fill="none" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<g transform="translate(360,260) scale(1.4)">{ME}{intention_arrow("left")}</g>')
    S.add(f'<g transform="translate(250,220) scale(1.4)">{vehicle_sprite("car","rouge")}{intention_arrow("right")}</g>')
    for y, label in ((397, "Entrée"), (66, "Sortie")):
        S.add(f'<text x="574" y="{y}" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#263336">{label}</text>')
    S.add(f'<path d="M250 96V40m-8 12 8-12 8 12" fill="none" stroke="{MARK}" stroke-width="3"/>')
    return str(S)


def route_c107(params):
    """Matched framing: road layout changes, C107 and all non-geometric conditions do not."""
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add(f'<path d="M115 0H405V440H115Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M122 0V440 M398 0V440" stroke="{MARK}" stroke-width="3"/>')
    if params.get("separee"):
        S.add(f'<path d="M246 0H274V440H246Z" fill="{GRASS}" stroke="#b7c2ad" stroke-width="6"/>')
        S.add(f'<path d="M236 0V440 M284 0V440" stroke="{MARK}" stroke-width="3"/>')
    else:
        S.add(f'<path d="M260 0V440" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 18"/>')
    S.add(f'<g transform="translate(185,120) rotate(180) scale(1.5)">{vehicle_sprite("car","gris")}</g>')
    S.add(f'<g transform="translate(335,345) scale(1.5)">{ME}</g>')
    for x, y, direction in ((185, 300, 180), (335, 155, 0)):
        S.add(f'<g transform="translate({x},{y}) rotate({direction})"><path d="M0 20V-20m-8 10 8-10 8 10" '
              f'fill="none" stroke="{MARK}" stroke-width="4"/></g>')
    uri = sign_data_uri(params["sign"]["file"], 200)
    S.add('<path d="M510 298V372" stroke="#687475" stroke-width="5"/>')
    S.add(f'<image x="460" y="242" width="100" height="100" xlink:href="{uri}"/>')
    return str(S)


def camion_virage(params):
    """Initial lateral position only; flashing right indicator is also stated in the prompt."""
    S = SVG(640, 600)
    S.add(f'<rect width="640" height="600" fill="{GRASS}"/>')
    S.add('<path d="M77 0H443V600H77Z M430 98H640V262H430Z" fill="#ced6c8"/>')
    S.add(f'<path d="M90 0H430V600H90Z M430 110H640V250H430Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M97 0V600 M423 0V110H640 M423 600V250H640" fill="none" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<path d="M250 0V600 M430 180H640" stroke="{MARK}" stroke-width="3" stroke-dasharray="22 18"/>')
    S.add(f'<g transform="translate(294,360) scale(1.4)">{vehicle_sprite("truck","gris")}')
    # Keep the whole truck upstream: the cab has room to approach before the turn.
    # Lamps on the truck's right, with small rays indicating the lit phase.
    S.add('<path d="M23-60v9 M23 50v9" stroke="#ffc438" stroke-width="7"/>')
    S.add('<path d="M32-57h7 M32 55h7" stroke="#ffc438" stroke-width="3"/></g>')
    S.add(f'<g transform="translate(345,530) scale(1.4)">{ME}</g>')
    return str(S)


def camion_roues(params):
    """Bicycle-model axle-centre paths in a steady right turn, not a swept-body envelope."""
    S = SVG(640, 360)
    S.add(f'<rect width="640" height="360" fill="{GRASS}"/>')
    S.add(f'<path d="M110 330V240A200 200 0 0 1 310 40H590V245H340A30 30 0 0 0 310 275V330Z" fill="{ASPHALT}"/>')
    # Rear axle radius 110, wheelbase 90: front radius follows Pythagoras.
    rear, wheelbase = 110, 90
    front = math.hypot(rear, wheelbase)
    # One rigid vehicle pose: rear axle tangent to its own circle, front axle ahead.
    a = math.radians(220)
    rx, ry = 330 + rear*math.cos(a), 270 + rear*math.sin(a)
    fx, fy = rx - wheelbase*math.sin(a), ry + wheelbase*math.cos(a)
    cx, cy = (rx+fx)/2, (ry+fy)/2
    rot = math.degrees(math.atan2(fy-ry, fx-rx)) + 90
    S.add(f'<g transform="translate({cx},{cy}) rotate({rot})"><g transform="scale(1.1)" opacity=".55">{vehicle_sprite("truck","gris")}</g>')
    for y in (-45, 45):
        S.add(f'<path d="M-27 {y}h54" stroke="#222" stroke-width="3"/>')
        for x in (-26, 26):
            steer = math.degrees(math.atan2(wheelbase, rear-x)) if y < 0 else 0
            S.add(f'<rect x="{x-3}" y="{y-9}" width="6" height="18" rx="2" fill="#111" '
                  f'transform="rotate({steer},{x},{y})"/>')
    S.add('</g>')
    # A translucent body lets the two centre paths remain visible and meet their axles.
    for radius, colour, dash in ((front,"#ffffff",""),(rear,"#ffd166",'stroke-dasharray="9 6"')):
        S.add(f'<path d="M{330-radius} 270A{radius} {radius} 0 0 1 330 {270-radius}" '
              f'fill="none" stroke="{colour}" stroke-width="5" {dash}/>')
    for y, label, colour, dash in ((130, "Avant", "#ffffff", ""), (178, "Arrière", "#ffd166", 'stroke-dasharray="9 6"')):
        S.add(f'<path d="M394 {y}h38" stroke="{colour}" stroke-width="5" {dash}/>')
        S.add(f'<text x="447" y="{y+7}" font-family="{FONT}" font-size="28" fill="{colour}">{label}</text>')
    return str(S)


def barriere_k2(params):
    """K2 barrier: red and white striped rail on two legs, seen from the front, on a road."""
    S = SVG(360, 260)
    S.add(f'<rect x="0" y="0" width="360" height="260" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="150" width="360" height="110" fill="{ASPHALT}"/>')
    S.add('<ellipse cx="180" cy="232" rx="150" ry="10" fill="#000" opacity="0.2"/>')
    for x in (60, 288):
        S.add(f'<rect x="{x}" y="120" width="12" height="110" fill="#e8e8e8" stroke="#555" stroke-width="2"/>')
    S.add('<rect x="30" y="80" width="300" height="52" rx="6" fill="#ffffff" stroke="#333" stroke-width="3"/>')
    for i in range(0, 6, 2):
        S.add(f'<rect x="{34 + i * 49}" y="84" width="49" height="44" fill="#d8362d"/>')
    return str(S)


def triangle_seul(params):
    S = SVG(300, 280)
    S.add('<rect x="0" y="0" width="300" height="280" fill="#ffffff"/>')
    S.add('<path d="M150,30 L280,250 L20,250 Z" fill="#e53935" stroke="#333" stroke-width="3" stroke-linejoin="round"/>')
    S.add('<path d="M150,80 L240,230 L60,230 Z" fill="#ffffff"/>')
    S.add('<rect x="120" y="250" width="60" height="10" fill="#333"/>')
    return str(S)


def cedez_le_passage(params):
    """AB3a without its optional plate (the Commons file prints « CÉDEZ LE PASSAGE », i.e. the answer)."""
    S = SVG(300, 270)
    S.add('<path d="M20,22 L280,22 L150,248 Z" fill="#d52b1e" stroke="#9a9a9a" stroke-width="2" stroke-linejoin="round"/>')
    S.add('<path d="M58,44 L242,44 L150,204 Z" fill="#ffffff"/>')
    return str(S)


def balise_piquet(params):
    """Post beacons J1 (white band), J3 (red band), J1bis (red top): white trapezoid post, 1 m high."""
    kind = params.get("kind", "j1")
    S = SVG(240, 300)
    S.add(f'<rect x="0" y="0" width="240" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="230" width="240" height="70" fill="{ASPHALT}"/>')
    # post (slightly tapered), ground shadow
    S.add('<ellipse cx="120" cy="262" rx="34" ry="8" fill="#000" opacity="0.25"/>')
    S.add('<path d="M96,40 L144,40 L150,262 L90,262 Z" fill="#eeeeee" stroke="#8a8a8a" stroke-width="2"/>')
    if kind == "j1bis":
        S.add('<path d="M96,40 L144,40 L146,86 L94,86 Z" fill="#d8362d"/>')
    band = "#d8362d" if kind == "j3" else "#ffffff"
    S.add(f'<path d="M94,88 L146,88 L147,118 L93,118 Z" fill="{band}" stroke="#6a6a6a" stroke-width="2"/>')
    # retro-reflective sheen on the band
    S.add('<path d="M97,92 L142,92 L143,100 L96,100 Z" fill="#ffffff" opacity="0.45"/>')
    return str(S)


def voyant_direction(params):
    """Steering-assist tell-tale: steering wheel seen from the front with '!' on a dark dashboard tile."""
    c = params.get("colour", "#e53935")
    S = SVG(360, 360)
    S.add('<defs><filter id="g" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter></defs>')
    S.add('<rect x="0" y="0" width="360" height="360" rx="43" fill="#1b1b1b"/>')
    wheel = (f'<g transform="translate(150,180) scale(.82) translate(-180,-180)">'
             f'<circle cx="180" cy="180" r="112" fill="none" stroke="{c}" stroke-width="26"/>'
             f'<circle cx="180" cy="180" r="34" fill="{c}"/>'
             f'<path d="M180,214 L180,292 M70,166 L146,180 M290,166 L214,180" stroke="{c}" stroke-width="22" stroke-linecap="round"/></g>'
             f'<rect x="284" y="110" width="26" height="92" rx="8" fill="{c}"/><circle cx="297" cy="236" r="15" fill="{c}"/>')
    S.add(f'<g filter="url(#g)" opacity="0.6">{wheel}</g>')
    S.add(wheel)
    return str(S)


REGISTRY.update({
    "balise_piquet": balise_piquet, "voyant_direction": voyant_direction,
    "voie_insertion": voie_insertion, "bande_cyclable": bande_cyclable, "damier": damier, "ralentisseur": ralentisseur,
    "direction_voies": direction_voies,
    "marquage_temporaire": marquage_temporaire, "zone_bleue": zone_bleue, "losange_sol": losange_sol, "cvcb": cvcb,
    "livraison": livraison, "direction_panel": direction_panel, "lieu_dit": lieu_dit, "feu_bicolore": feu_bicolore,
    "giratoire_sortie": giratoire_sortie, "rappel_limites": rappel_limites, "entrecroisement": entrecroisement, "route_c107": route_c107,
    "camion_virage": camion_virage, "camion_roues": camion_roues, "chantier_rabattement": chantier_rabattement, "corridor_securite": corridor_securite,
    "cycliste_tourne_droite": cycliste_tourne_droite, "cone": cone, "cedez_le_passage": cedez_le_passage, "triangle_seul": triangle_seul, "barriere_k2": barriere_k2,
})
