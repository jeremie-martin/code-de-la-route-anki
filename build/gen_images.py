"""Generated illustrations: road markings, traffic lights, officer signals, pictograms.

Each generator returns an SVG string. `render(name, params)` dispatches by name.
Visual identity matches build/diagrams.py (same asphalt, grass, marking colours).
"""
from __future__ import annotations

import base64
import math
import textwrap

from build.diagrams import (ASPHALT, GRASS, MARK, LABEL, RAIL, CAR_COLOURS, CEDEZ_SVG, FONT, SVG, agent_figure, draw_road, draw_intersection, draw_roundabout,
                            vehicle_sprite, intention_arrow, siren_rays, sign_data_uri, esc, _body, pedestrian)

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
        # vertical road with 3 lanes at an intersection: left / straight / right; `me`: MOI's lane, behind the arrows
        me = params.get("me")
        H = 400 if me else 300
        S = SVG(480, H)
        S.add(f'<rect x="0" y="0" width="480" height="{H}" fill="{GRASS}"/>')
        S.add(f'<rect x="90" y="0" width="300" height="{H}" fill="{ASPHALT}"/>')
        S.add(f'<rect x="0" y="0" width="480" height="60" fill="{ASPHALT}"/>')
        for x in (190, 290):
            S.add(f'<line x1="{x}" y1="70" x2="{x}" y2="{H}" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
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
        if me:
            S.add(f'<g transform="translate({ {"left": 140, "straight": 240, "right": 340}[me]},330)">{ME}</g>')
    elif kind == "insertion":
        pass
    return str(S)


def transversale(params):
    """Stop line (continuous) or give-way line (dashed) with sign; plus 'effet des feux'. `arret`: MOI stopped at the
    STOP line (question drawing) instead of the plain reference car."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="120" y="0" width="240" height="300" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="0" width="480" height="80" fill="{ASPHALT}"/>')
    S.add(f'<line x1="240" y1="100" x2="240" y2="300" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
    kind = params.get("kind", "stop")
    if kind == "stop":
        S.add(f'<rect x="242" y="84" width="116" height="16" fill="{MARK}"/>')      # wide: 50 cm, well over twice a lane line
    elif kind == "cedez":
        for x in range(244, 358, 20):
            S.add(f'<rect x="{x}" y="84" width="12" height="16" fill="{MARK}"/>')
    elif kind == "effet_feux":
        S.add(f'<line x1="244" y1="92" x2="358" y2="92" stroke="{MARK}" stroke-width="4" stroke-dasharray="6 6"/>')
        S.add(f'<rect x="366" y="40" width="22" height="58" rx="5" fill="#222"/>')
        for i, c in enumerate(["#d8362d", "#f08a24", "#2fa14b"]):
            S.add(f'<circle cx="377" cy="{51 + i * 18}" r="7" fill="{c if i == 0 else "#555"}"/>')
    if params.get("arret"):      # a decision drawing: MOI stopped with its front at the line, the STOP sign beside it
        uri, h = _sign_png({"kind": "sign", "file": "France road sign AB4.svg"}, 60)
        S.add(f'<image href="{uri}" x="372" y="104" width="60" height="{h}"/>')
        S.add(f'<g transform="translate(300,152)">{ME}</g>')
    else:
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
        _flash_rays(S, cx, cy, r + 3, colour)


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
        _flash_rays(S, 210, 270, 38, colour)
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
            _flash_rays(S, cx, 74, 30, AMBER)
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


CRITAIR = {"E": "#43a047", "1": "#7e57c2", "2": "#fdd835", "3": "#fb8c00", "4": "#7b3f2a", "5": "#757575"}


def _critair_disc(S, cx, cy, r, cls):
    """One Crit'Air sticker: class E (electric, hydrogen) is green without a figure; 1 to 5 carry their figure."""
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CRITAIR[cls]}" stroke="#222" stroke-width="2"/>')
    ink = "#222" if cls == "2" else "#ffffff"
    S.add(f'<text x="{cx}" y="{cy - r * 0.32}" font-family="{FONT}" font-size="{r * 0.34:.0f}" font-weight="800" '
          f'text-anchor="middle" fill="{ink}">Crit\'Air</text>')
    if cls != "E":
        S.add(f'<text x="{cx}" y="{cy + r * 0.62}" font-family="{FONT}" font-size="{r * 1.05:.0f}" font-weight="800" '
              f'text-anchor="middle" fill="{ink}">{cls}</text>')


def critair(params):
    """Crit'Air stickers in a row (default: all six classes), each with its class written underneath."""
    classes = params.get("classes", list(CRITAIR))
    cols = min(3, len(classes))
    rows = (len(classes) + cols - 1) // cols
    step, r, row_h = 480 / cols, 56, 170
    S = SVG(480, rows * row_h)
    S.add(f'<rect x="0" y="0" width="480" height="{S.h}" fill="{PAPER}"/>')
    for i, cls in enumerate(classes):
        cx, top = step * (i % cols + 0.5), (i // cols) * row_h
        _critair_disc(S, cx, top + r + 8, r, cls)
        _text(S, cx, top + 2 * r + 38, "électrique" if cls == "E" else f"classe {cls}")
    return str(S)

def triangle_distance(params):
    """Broken-down car and warning triangle upstream; the measured gap is broken (≈) because it is not to scale."""
    S = SVG(480, 220)
    S.add(f'<rect x="0" y="0" width="480" height="220" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="120" fill="{ASPHALT}"/>')
    _dashes_h(S, 100, 3, 10, w=4)
    S.add(f'<g transform="translate(400,130) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    for dx, dy in ((-40, -18), (-40, 18), (40, -18), (40, 18)):          # hazard lights flashing
        _flash_rays(S, 400 + dx, 130 + dy, 3, AMBER)
    S.add('<path d="M66,150 l14,-26 l14,26 z" fill="#e53935" stroke="#fff" stroke-width="2"/>')
    S.add(f'<path d="M80,192 H222 M258,192 H362 M80,184 v16 M362,184 v16 M216,202 l12,-20 M246,202 l12,-20" '
          f'stroke="{LABEL}" stroke-width="3" fill="none"/>')
    S.add(f'<text x="221" y="174" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle" fill="{LABEL}">{esc(str(params.get("label", "≈ 30 m")))}</text>')
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
    if params.get("picto") == "velo":
        S.add(_bike(300, 80, fg, 1.3))
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
    """One carriageway going up: left lane (centre x 162), right lane (302), hard shoulder (BAU, 372–468) wide
    enough to hold a car clear of its line; roadside from x 475."""
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add('<path d="M60 0H85V440H60Z" fill="#aeb7a8"/>')
    S.add(f'<path d="M85 0H475V440H85Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M92 0V440 M468 0V440" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<path d="M232 0V440" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 18"/>')
    S.add(f'<path d="M372 0V440" stroke="{MARK}" stroke-width="5" stroke-dasharray="78 26"/>')
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
    S.add('<path d="M244 0H365V36H244Z" fill="#c9b99b"/>')
    for y in (18, 48):
        S.add(f'<g transform="translate(241,{y}) scale(.14) translate(-120,-249)">')
        _draw_cone(S)
        S.add('</g>')
    # Each trailer's panel is shown face-on within this plan view, like roadside signs.
    for x, y in ((302, 100), (420, 248)):
        S.add(f'<g transform="translate({x-27.5},{y-45}) scale(.5)">{panel}</g>')
        S.add(f'<path d="M{x-20} {y+49}h40" stroke="#222" stroke-width="6"/>')
    S.add(f'<g transform="translate(302,370) scale(1.5)">{ME}</g>')
    S.add('<path d="M450 236L480 226" stroke="#687475" stroke-width="2"/>')
    S.add(f'<g transform="translate(480,125)">{panel}</g>')
    S.add(f'<text x="535" y="106" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#263336">Signal agrandi</text>')
    return str(S)


def corridor_securite(params):
    """An adjacent car prevents an immediate lane change past a shoulder recovery."""
    S = _motorway_scene()
    S.add(f'<g transform="translate(162,335) scale(1.5)">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<g transform="translate(302,350) scale(1.5)">{ME}</g>')
    # Recovery vehicle: existing truck cab, flat bed, secured car and amber beacon.
    S.add(f'<g transform="translate(424,129) scale(1.35)">{vehicle_sprite("truck", "orange")}')
    S.add('<rect x="-23" y="-25" width="46" height="81" fill="#71787a"/>')
    S.add(f'<g transform="translate(0,15) scale(.75)">{vehicle_sprite("car", "gris")}</g>')
    S.add('<rect x="-16" y="-31" width="32" height="7" rx="2" fill="#ffc438" stroke="#805b14"/>')
    S.add(siren_rays(0, -28, "#f08a24", r0=14, r1=22))
    S.add('</g>')
    S.add(f'<text x="424" y="240" text-anchor="middle" font-family="{FONT}" font-size="26" fill="{MARK}">BAU</text>')
    return str(S)


def autoroute_attente(params):
    """Breakdown on the hard shoulder: the car with its hazard lights, the occupants behind the safety barrier,
    back from the car on the side traffic comes from (traffic goes up)."""
    S = _motorway_scene()
    for x in (162, 302):
        S.add(f'<g transform="translate({x},230)"><path d="M0 30V-30m-10 12 10-12 10 12" fill="none" stroke="{MARK}" stroke-width="4"/></g>')
    S.add(f'<g transform="translate(429,150) scale(1.5)">{vehicle_sprite("car", "gris")}</g>')
    for dx in (-27, 27):                     # hazard lights at the four corners, on the lamps
        for dy in (-59, 59):
            _flash_rays(S, 429 + dx, 150 + dy, 4, AMBER)
    S.add('<path d="M500 0V440" stroke="#8d969a" stroke-width="6"/>')                       # safety barrier
    for y in range(20, 440, 40):
        S.add(f'<rect x="496" y="{y}" width="8" height="8" fill="#6c7478"/>')
    for x, y in ((548, 306), (594, 326), (556, 356)):
        S.add(pedestrian(x, y, YELLOW, 1.6))
    _pill(S, 570, 40, "glissière", anchor="middle")
    _pill(S, 570, 420, "occupants", anchor="middle")
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
    """Two-lane roundabout seen from above (entries S, W, N, E; anticlockwise). params:
    vehicles: [{kind, colour, me, lane: "int" | "ext" | "both" (straddling), angle (deg, 0 = east, anticlockwise)}]
              or {entry: S|W|N|E} for a vehicle waiting at that entry; exit: the branch marked « Sortie visée »;
    marker: {angle, text, label: [x, y]} a spot of the outer lane, with its label placed at (x, y). Default: MOI inside, cyclist outside, exit E.
    answer_on_back: the marker is the answer, drawn only on the back of a « verso » image;
    cedez: a give-way sign on the right-hand verge of each entry (the entries' regime is then visible)."""
    vehicles = params.get("vehicles", [{"me": True, "lane": "int", "angle": -32}, {"kind": "bike", "colour": "rouge", "lane": "ext", "angle": -30}])
    exit_ = params.get("exit", "E")
    S = SVG(640, 440)
    S.add(f'<rect width="640" height="440" fill="{GRASS}"/>')
    S.add(f'<path d="M190 0H290V440H190Z M0 165H640V275H0Z" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="240" cy="220" r="195" fill="{ASPHALT}"/>')
    S.add(f'<circle cx="240" cy="220" r="60" fill="{GRASS}" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<circle cx="240" cy="220" r="128" fill="none" stroke="{MARK}" stroke-width="3" stroke-dasharray="18 15"/>')
    S.add(f'<path d="M437 220H640 M240 0V23 M240 417V440 M0 220H43" stroke="{MARK}" stroke-width="3"/>')
    for x1, y1, x2, y2 in ((440, 168, 440, 216), (193, 22, 236, 22), (244, 418, 287, 418), (40, 224, 40, 272)):
        S.add(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{MARK}" stroke-width="6" stroke-dasharray="8 6"/>')
    if params.get("cedez"):
        cede = "data:image/svg+xml;base64," + base64.b64encode(CEDEZ_SVG.encode()).decode()
        for x, y in ((298, 398), (148, 0), (446, 122), (0, 280)):  # S, N, E, W: verge on the entrant's right
            S.add(f'<image href="{cede}" x="{x}" y="{y}" width="40" height="40"/>')
    radius = {"int": 94, "ext": 162, "both": 128}
    entry = {"S": (265, 390, 0), "N": (215, 50, 180), "E": (560, 195, 270), "W": (-80, 245, 90)}
    for v in vehicles:
        kind, colour = v.get("kind", "car"), v.get("colour", "gris")
        sprite = _body({"me": True}, 0) if v.get("me") else vehicle_sprite(kind, colour)
        scale = .9 if kind == "bike" else 1.0
        if "entry" in v:
            x, y, rot = entry[v["entry"]]
            if v["entry"] == "W":
                x = 110
            S.add(f'<g transform="translate({x},{y}) rotate({rot}) scale({scale})">{sprite}</g>')
            continue
        a = math.radians(v["angle"])
        x, y = 240 + radius[v["lane"]] * math.cos(a), 220 - radius[v["lane"]] * math.sin(a)
        if v.get("me"):
            sprite = _body({"me": True}, -v["angle"])
        S.add(f'<g transform="translate({x},{y}) rotate({-v["angle"]}) scale({scale})">{sprite}</g>')
    if exit_ == "E":
        S.add(f'<path d="M485 248h98m-12-8 12 8-12 8" fill="none" stroke="{MARK}" stroke-width="4"/>')
        _pill(S, 537, 318, "Sortie visée", 24, anchor="middle")
    elif exit_ == "W":
        S.add(f'<path d="M40 192h-28m12-8 -12 8 12 8" fill="none" stroke="{MARK}" stroke-width="4"/>')
        _pill(S, 14, 318, "Sortie visée", 24)
    if params.get("marker") and (params.get("verso") or not params.get("answer_on_back")):
        m = params["marker"]
        a = math.radians(m["angle"])
        x, y = 240 + 185 * math.cos(a), 220 - 185 * math.sin(a)
        S.add(f'<circle cx="{x}" cy="{y}" r="9" fill="{YELLOW}" stroke="{LABEL}" stroke-width="2"/>')
        tx, ty = m["label"]
        S.add(f'<path d="M{x},{y} L{tx},{ty}" stroke="{LABEL}" stroke-width="2"/>')
        if params.get("answer_on_back"):         # revealed on the back: answer colour, as large as « Sortie visée »
            _pill(S, tx, ty + 12, m["text"], 24, ANSWER)
        else:
            _pill(S, tx, ty + 6, m["text"])
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
    """Initial lateral position only; flashing right indicator is also stated in the prompt. The lorry keeps its
    whole length before the junction; MOI follows it."""
    S = SVG(640, 640)
    S.add(f'<rect width="640" height="640" fill="{GRASS}"/>')
    S.add('<path d="M77 0H443V640H77Z M430 98H640V262H430Z" fill="#ced6c8"/>')
    S.add(f'<path d="M90 0H430V640H90Z M430 110H640V250H430Z" fill="{ASPHALT}"/>')
    S.add(f'<path d="M97 0V640 M423 0V110H640 M423 640V250H640" fill="none" stroke="{MARK}" stroke-width="3"/>')
    S.add(f'<path d="M250 0V640 M430 180H640" stroke="{MARK}" stroke-width="3" stroke-dasharray="22 18"/>')
    S.add(f'<g transform="translate(294,392) scale(1.1)">{vehicle_sprite("lorry","gris")}')
    # right indicators, front and rear, with the rays of every flashing light
    S.add('<path d="M23-115v9 M23 106v9" stroke="#ffc438" stroke-width="7"/>')
    S.add('<path d="M32-112h7 M32 111h7" stroke="#ffc438" stroke-width="3"/></g>')
    S.add(f'<g transform="translate(345,590) scale(1.1)">{ME}</g>')
    return str(S)


def camion_roues(params):
    """Bicycle-model axle-centre paths in a steady right turn, not a swept-body envelope."""
    S = SVG(640, 360)
    S.add(f'<rect width="640" height="360" fill="{GRASS}"/>')
    S.add(f'<path d="M110 330V240A200 200 0 0 1 310 40H590V245H340A30 30 0 0 0 310 275V330Z" fill="{ASPHALT}"/>')
    # Rear axle radius 110, wheelbase 160 (a rigid lorry): front radius follows Pythagoras.
    rear, wheelbase = 110, 160
    front = math.hypot(rear, wheelbase)
    # One rigid vehicle pose: rear axle tangent to its own circle, front axle ahead.
    a = math.radians(220)
    rx, ry = 330 + rear*math.cos(a), 270 + rear*math.sin(a)
    fx, fy = rx - wheelbase*math.sin(a), ry + wheelbase*math.cos(a)
    cx, cy = (rx+fx)/2, (ry+fy)/2
    rot = math.degrees(math.atan2(fy-ry, fx-rx)) + 90
    S.add(f'<g transform="translate({cx},{cy}) rotate({rot})"><g transform="translate(0,12)" opacity=".55">{vehicle_sprite("lorry","gris")}</g>')
    for y in (-wheelbase / 2, wheelbase / 2):
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


# ====================================================== teaching drawings ===
# Drawings added to rule cards share one visual language:
#   INK for text and outlines; ANSWER for what the back of an « verso » image adds in place (the cards' answer
#   colour); WRONG for what not to do; SIGN_RED / SIGN_BLUE for drawn signs; the scenarios' HIDDEN hatch for what
#   cannot be seen and VISIBLE for what a mirror shows. Drawings keep a white background in both card themes.
#   Front and back of a « verso » image are drawn by the same code with the same canvas: only the answer (text, or a
#   mark such as a path or a spot, with `answer_on_back`) is added.
INK = LABEL
ANSWER = "#17566e"            # cards.css --answer (light theme)
WRONG = "#a33c30"             # cards.css --false
SIGN_RED, SIGN_BLUE = "#d52b1e", "#1f5fae"
PAPER = "#ffffff"
HIDDEN = "#bac2c5"            # same hatch as the masked zone of the scenarios
VISIBLE = "#fff9c4"
SKIN, CLOTH, CLOTH_DARK = "#f2c8a0", "#5c7a99", "#3e556b"    # people
SEAT, SEAT_DARK = "#d7dde0", "#c5ccd0"                       # seats, head restraints, dashboard
LABEL_SIZE, NUMBER_SIZE = 18, 20


_font_cache: dict = {}


def text_width(s: str, size: float, weight: int = 700) -> float:
    """Width of a label in the font the PNGs are rendered with (Inter, via fontconfig), used for layout and by the
    image tests. Falls back to a conservative estimate if the font cannot be found."""
    key = (int(size), weight >= 600)
    if key not in _font_cache:
        try:
            import subprocess
            from PIL import ImageFont
            path = subprocess.run(["fc-match", "-f", "%{file}", "Inter:bold" if key[1] else "Inter"],
                                  capture_output=True, text=True, check=True).stdout
            _font_cache[key] = ImageFont.truetype(path, key[0])
        except Exception:  # noqa: BLE001 — measurement is a best effort; the estimate errs on the wide side
            _font_cache[key] = None
    font = _font_cache[key]
    return font.getlength(s) if font else len(s) * size * 0.6


def _text(S, x, y, s, size=LABEL_SIZE, colour=INK, anchor="middle", weight=700):
    S.add(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
          f'text-anchor="{anchor}" fill="{colour}">{esc(str(s))}</text>')


def _tag(S, x, y, front, back, verso, size=NUMBER_SIZE, anchor="middle"):
    """A label that reads `front` (a letter or number) and, on the back, `back` at the same place, in ANSWER colour."""
    _text(S, x, y, back if verso else front, size, ANSWER if verso else INK, anchor)


def _slot(S, cx, y, number, name, verso):
    """Numbered slot under an item: the number on both sides, the name added below it on the back."""
    if number is not None:
        _text(S, cx, y, number, NUMBER_SIZE)
    if verso:
        _text(S, cx, y + 24, name, LABEL_SIZE, ANSWER)


def _pill(S, x, y, s, size=LABEL_SIZE, colour=INK, anchor="start"):
    """Label on a white pill, for text drawn over asphalt or other busy areas."""
    w = text_width(s, size) + 16
    left = x - 8 if anchor == "start" else x - w / 2 if anchor == "middle" else x - w + 8
    S.add(f'<rect x="{left}" y="{y - size - 4}" width="{w}" height="{size + 12}" rx="6" fill="{PAPER}" opacity="0.92"/>')
    _text(S, x, y, s, size, colour, anchor)


def _hidden_pattern(S, pid="hidden"):
    S.add(f'<defs><pattern id="{pid}" width="12" height="12" patternUnits="userSpaceOnUse">'
          f'<path d="M-3 3L3-3 M0 12L12 0 M9 15L15 9" stroke="{HIDDEN}" stroke-width="2"/></pattern></defs>')


def _flash_rays(S, cx, cy, r, colour):
    """Short rays around a flashing light, as on every blinking light of the deck."""
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        S.add(f'<line x1="{cx + (r + 6) * math.cos(a):.1f}" y1="{cy + (r + 6) * math.sin(a):.1f}" '
              f'x2="{cx + (r + 13) * math.cos(a):.1f}" y2="{cy + (r + 13) * math.sin(a):.1f}" '
              f'stroke="{colour}" stroke-width="3" stroke-linecap="round"/>')


def _bike(x, y, colour, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{colour}" stroke-width="3">'
            f'<circle cx="-10" cy="6" r="8"/><circle cx="10" cy="6" r="8"/><path d="M-10,6 l7,-13 l11,0 l2,13 M-3,-7 l5,13"/></g>')


# ------------------------------------------------------------ road words ---

def vocab_route(params):
    """Road seen from above with a label margin: A = chaussée (brace), B = one lane (brace), C = accotement."""
    verso = params.get("verso", False)
    S = SVG(480, 280)
    S.add(f'<rect x="0" y="0" width="480" height="280" fill="{PAPER}"/>')
    L = 130  # label margin on the left
    S.add(f'<rect x="{L}" y="20" width="{480 - L}" height="50" fill="{GRASS}"/>')
    S.add(f'<rect x="{L}" y="190" width="{480 - L}" height="50" fill="{GRASS}"/>')
    S.add(f'<rect x="{L}" y="70" width="{480 - L}" height="120" fill="{ASPHALT}"/>')
    for y in (72, 188):
        S.add(f'<rect x="{L}" y="{y - 2}" width="{480 - L}" height="3" fill="{MARK}"/>')
    x = L
    while x < 480:
        S.add(f'<rect x="{x}" y="128" width="36" height="4" fill="{MARK}"/>')
        x += 96
    S.add(f'<g transform="translate(400,160) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<path d="M{L - 14},70 v120 M{L - 20},70 h12 M{L - 20},190 h12" stroke="{INK}" stroke-width="3" fill="none"/>')
    S.add(f'<path d="M{L + 24},130 v60 M{L + 18},130 h12 M{L + 18},190 h12" stroke="{YELLOW}" stroke-width="4" fill="none"/>')
    _tag(S, L - 26, 137, "A", "chaussée", verso, anchor="end")
    _pill(S, L + 36, 166, "voie" if verso else "B", NUMBER_SIZE, ANSWER if verso else INK)
    S.add(f'<path d="M{L - 18},215 H{L + 30} M{L + 20},207 l10,8 l-10,8" stroke="{INK}" stroke-width="3" fill="none"/>')
    _tag(S, L - 24, 221, "C", "accotement", verso, size=16 if verso else NUMBER_SIZE, anchor="end")
    return str(S)


def types_routes(params):
    """Three road types side by side (plan): 1 one carriageway; 2 two carriageways separated by a central
    reserve; 3 motorway (reserve, two lanes each way, hard shoulders). The back adds the limit under each number."""
    verso = params.get("verso", False)
    limits = params.get("limits", ["80 km/h", "110 km/h", "130 km/h"])
    H = 300
    S = SVG(480, H + 80)
    S.add(f'<rect x="0" y="0" width="480" height="{H}" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="{H}" width="480" height="80" fill="{PAPER}"/>')

    def carriage(x, w, lanes=1, shoulder=None):
        S.add(f'<rect x="{x}" y="0" width="{w}" height="{H}" fill="{ASPHALT}"/>')
        S.add(f'<path d="M{x + 2},0 V{H} M{x + w - 2},0 V{H}" stroke="{MARK}" stroke-width="3"/>')
        for i in range(1, lanes):
            S.add(f'<path d="M{x + w * i / lanes},0 V{H}" stroke="{MARK}" stroke-width="3" stroke-dasharray="18 16"/>')
        if shoulder:  # hard shoulder beyond the edge line
            S.add(f'<rect x="{x + w if shoulder == "right" else x - 16}" y="0" width="16" height="{H}" fill="#6e6e6e"/>')

    reserve = "#9cb07e"
    carriage(40, 90, lanes=2)                                                                   # 1
    carriage(180, 46); S.add(f'<rect x="226" y="0" width="24" height="{H}" fill="{reserve}"/>'); carriage(250, 46)  # 2
    carriage(356, 50, lanes=2, shoulder="left"); S.add(f'<rect x="406" y="0" width="14" height="{H}" fill="{reserve}"/>')
    carriage(420, 50, lanes=2, shoulder="right")                                                # 3
    uri = sign_data_uri("France road sign C207.svg", 160)
    S.add(f'<rect x="386" y="18" width="64" height="64" rx="6" fill="{PAPER}"/>')
    S.add(f'<image href="{uri}" x="390" y="22" width="56" height="56"/>')
    for i, cx in enumerate((85, 238, 413)):
        _slot(S, cx, H + 30, str(i + 1), limits[i], verso)
    return str(S)


# ---------------------------------------------------------------- signs ---

def _sign_shape(S, cx, cy, kind):
    r = 46
    if kind == "danger":
        S.add(f'<path d="M{cx},{cy - 50} L{cx + 55},{cy + 42} L{cx - 55},{cy + 42} Z" fill="{PAPER}" stroke="{SIGN_RED}" stroke-width="10" stroke-linejoin="round"/>')
    elif kind == "interdiction":
        S.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAPER}" stroke="{SIGN_RED}" stroke-width="10"/>')
    elif kind == "obligation":
        S.add(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="{SIGN_BLUE}"/>')
    elif kind == "indication":
        S.add(f'<rect x="{cx - 46}" y="{cy - 46}" width="92" height="92" rx="6" fill="{SIGN_BLUE}"/>')
    elif kind == "fin_interdiction":
        S.add(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="{PAPER}" stroke="#888888" stroke-width="2"/>')
        S.add(f'<path d="M{cx - 33},{cy + 33} L{cx + 33},{cy - 33}" stroke="#111111" stroke-width="10"/>')
    elif kind == "fin_obligation":
        S.add(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="{SIGN_BLUE}"/>')
        S.add(f'<path d="M{cx - 33},{cy + 33} L{cx + 33},{cy - 33}" stroke="{SIGN_RED}" stroke-width="10"/>')


def formes_panneaux(params):
    """Shape and colour families of French signs, without pictograms: numbered, then named on the back."""
    verso = params.get("verso", False)
    kinds = params.get("kinds", ["danger", "interdiction", "obligation", "indication", "fin_interdiction", "fin_obligation"])
    names = {"danger": "danger", "interdiction": "interdiction", "obligation": "obligation", "indication": "indication",
             "fin_interdiction": "fin d’interdiction", "fin_obligation": "fin d’obligation"}
    cols = 3
    S = SVG(480, 180 * ((len(kinds) + cols - 1) // cols))
    S.add(f'<rect x="0" y="0" width="{S.w}" height="{S.h}" fill="{PAPER}"/>')
    for i, k in enumerate(kinds):
        cx, cy = 80 + (i % cols) * 160, 66 + (i // cols) * 180
        _sign_shape(S, cx, cy, k)
        _slot(S, cx, cy + 86, str(i + 1), names[k], verso)
    return str(S)


def cedez_le_passage(params):
    """AB3a without its optional plate (the Commons file prints « CÉDEZ LE PASSAGE », i.e. the answer)."""
    return CEDEZ_SVG


def _sign_png(item, width):
    """Data URI and height of one sign item rendered at `width` px (keeps the file's proportions).
    item: {kind: sign, file: <Commons file>} (attributed automatically) or {gen: <generator>, params} for a drawn one."""
    import base64
    import re
    import struct
    if "gen" in item:
        svg = render(item["gen"], item.get("params") or {})
        w, h = (float(v) for v in re.search(r'width="([\d.]+)" height="([\d.]+)"', svg).groups())
        return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode(), round(width * h / w)
    uri = sign_data_uri(item["file"], width * 2)
    png = base64.b64decode(uri.split(",", 1)[1])
    w, h = struct.unpack(">II", png[16:24])
    return uri, round(width * h / w)


def support_panneaux(params):
    """Several signs (and plates, or a drawn light) on one post, top to bottom, as seen when approaching."""
    items = params["signs"]
    parts, y = [], 16
    for item in items:
        w = item.get("w", params.get("width", 150))
        uri, h = _sign_png(item, w)
        parts.append((uri, w, h, y))
        y += h + 6
    H = y + 70
    S = SVG(300, H)
    S.add(f'<rect x="0" y="0" width="300" height="{H}" fill="{PAPER}"/>')
    S.add(f'<rect x="144" y="20" width="12" height="{H - 20}" fill="#9a9a9a"/>')
    for uri, w, h, top in parts:
        S.add(f'<image href="{uri}" x="{150 - w / 2}" y="{top}" width="{w}" height="{h}"/>')
    return str(S)


def planche_signaux(params):
    """Numbered sheet of signs; on the back each name appears under its number (nothing else moves)."""
    verso = params.get("verso", False)
    items = params["signs"]
    cols = params.get("cols", len(items) if len(items) <= 3 else 2 if len(items) == 4 else 3)
    cell_w = 480 // cols
    sign_w = min(150, cell_w - 40)
    cells = [(*_sign_png(item, item.get("w", sign_w)), item.get("w", sign_w), item["name"]) for item in items]
    row_h = max(h for _, h, _, _ in cells) + 64
    rows = (len(items) + cols - 1) // cols
    S = SVG(480, rows * row_h)
    S.add(f'<rect x="0" y="0" width="480" height="{rows * row_h}" fill="{PAPER}"/>')
    for i, (uri, h, w, name) in enumerate(cells):
        cx = cell_w * (i % cols) + cell_w / 2
        top = (i // cols) * row_h + 8
        S.add(f'<image href="{uri}" x="{cx - w / 2}" y="{top + (row_h - 64 - h) / 2}" width="{w}" height="{h}"/>')
        _slot(S, cx, top + row_h - 38, str(i + 1), name, verso)
    return str(S)


# --------------------------------------------------------- lights, panels ---

def feu_modal(params):
    """Red main light with a small flashing amber head beside it: BUS (R15) or cycle + arrow (R19)."""
    kind = params.get("kind", "bus")
    S = SVG(320, 360)
    S.add(f'<rect x="0" y="0" width="320" height="360" fill="{PAPER}"/>')
    S.add('<rect x="50" y="20" width="100" height="300" rx="16" fill="#222" stroke="#000" stroke-width="2"/>')
    _lamp(S, 100, 70, 36, RED, on=True)
    _lamp(S, 100, 170, 36, AMBER, on=False)
    _lamp(S, 100, 270, 36, GREEN, on=False)
    S.add('<rect x="180" y="210" width="100" height="100" rx="14" fill="#222" stroke="#000" stroke-width="2"/>')
    S.add('<circle cx="230" cy="260" r="38" fill="#111"/>')
    if kind == "bus":
        _text(S, 230, 270, "BUS", 26, AMBER, weight=800)
    else:
        S.add(_bike(222, 256, AMBER))
        S.add(f'<path d="M244,244 h14 v-6 l10,10 l-10,10 v-6 h-14 z" fill="{AMBER}"/>')
    _flash_rays(S, 230, 260, 44, AMBER)
    return str(S)


def feu_sur_panneau(params):
    """Flashing amber light fixed above a warning sign (R1): it reinforces the sign's warning."""
    S = SVG(260, 330)
    S.add(f'<rect x="0" y="0" width="260" height="330" fill="{PAPER}"/>')
    S.add('<rect x="124" y="120" width="12" height="210" fill="#9a9a9a"/>')
    S.add('<rect x="95" y="14" width="70" height="70" rx="12" fill="#222"/>')
    _lamp(S, 130, 49, 24, AMBER, on=True)
    _flash_rays(S, 130, 49, 26, AMBER)
    uri = sign_data_uri(params["sign"]["file"], 300)
    S.add(f'<image href="{uri}" x="55" y="92" width="150" height="150"/>')
    return str(S)


def pmv(params):
    """Variable-message panel over a motorway lane showing a speed limit (red ring, lit figures)."""
    S = SVG(420, 260)
    S.add(f'<rect x="0" y="0" width="420" height="260" fill="{PAPER}"/>')
    S.add('<rect x="10" y="20" width="400" height="16" fill="#8a8a8a"/>')
    S.add('<rect x="110" y="36" width="200" height="200" rx="14" fill="#141414" stroke="#555" stroke-width="3"/>')
    S.add(f'<circle cx="210" cy="136" r="78" fill="none" stroke="{RED}" stroke-width="16"/>')
    _text(S, 210, 160, params.get("value", "90"), 68, "#f6f6f6", weight=800)
    return str(S)


def plaque_orange(params):
    """Rear of a lorry carrying dangerous goods: orange plate (hazard number over UN number) and a hazard diamond."""
    S = SVG(420, 300)
    S.add(f'<rect x="0" y="0" width="420" height="300" fill="{PAPER}"/>')
    S.add('<rect x="40" y="20" width="340" height="240" rx="8" fill="#c9ced1" stroke="#555" stroke-width="3"/>')
    S.add('<rect x="40" y="250" width="340" height="30" fill="#333"/>')
    for x in (70, 350):
        S.add(f'<rect x="{x - 20}" y="232" width="40" height="18" rx="3" fill="{SIGN_RED}"/>')
    S.add('<rect x="140" y="130" width="140" height="94" rx="4" fill="#f28c00" stroke="#111" stroke-width="5"/>')
    S.add('<path d="M140,177 H280" stroke="#111" stroke-width="4"/>')
    _text(S, 210, 167, params.get("danger", "33"), 34, "#111", weight=800)
    _text(S, 210, 214, params.get("matiere", "1203"), 34, "#111", weight=800)
    S.add(f'<path d="M320,40 l42,42 l-42,42 l-42,-42 z" fill="{SIGN_RED}" stroke="{PAPER}" stroke-width="3"/>')  # flammable
    S.add(f'<path d="M320,58 c10,14 14,22 8,34 c-3,6 -13,8 -18,2 c-6,-8 -1,-18 4,-22 c0,6 2,10 6,10 c2,-8 -2,-16 0,-24 z" fill="{PAPER}"/>')
    return str(S)


def disque_stationnement(params):
    """European parking disc, French model (arrêté du 6 décembre 2007): light text on a dark blue face, « P », one
    window « heure d'arrivée » where the pointer marks the time set (by half hours)."""
    blue = "#1f4fa8"
    S = SVG(300, 300)
    S.add(f'<rect x="0" y="0" width="300" height="300" fill="{PAPER}"/>')
    S.add(f'<rect x="20" y="10" width="260" height="280" rx="10" fill="{blue}"/>')
    S.add(f'<rect x="124" y="28" width="52" height="52" rx="4" fill="none" stroke="#fff" stroke-width="5"/>')
    _text(S, 150, 70, "P", 40, "#fff", weight=800)
    _text(S, 150, 112, "HEURE D’ARRIVÉE", 20, "#fff", weight=800)
    S.add('<path d="M130,128 H170 L150,236 Z" fill="#fff"/><circle cx="150" cy="170" r="4" fill="#9aa4b0"/>')
    S.add('<path d="M72,246 Q150,212 228,246 L218,278 Q150,250 82,278 Z" fill="#fff"/>')        # time window
    for i, x in enumerate(range(92, 212, 12)):
        S.add(f'<line x1="{x}" y1="{252 - 8 * math.sin(math.pi * (x - 72) / 156):.1f}" x2="{x}" '
              f'y2="{258 - 8 * math.sin(math.pi * (x - 72) / 156):.1f}" stroke="{blue}" stroke-width="2"/>')
    _text(S, 118, 270, "10", 17, blue, weight=800)
    _text(S, 150, 263, "30", 12, blue, weight=700)
    _text(S, 182, 270, "11", 17, blue, weight=800)
    return str(S)


def car_enfants(params):
    """Rear of a coach carrying children, stopped: the square signal (yellow, frame and two children in dark blue,
    arrêté du 2 juillet 1982, annexe 7) and both rear hazard lights flashing."""
    navy = "#1b2a5c"
    S = SVG(420, 300)
    S.add(f'<rect x="0" y="0" width="420" height="300" fill="{PAPER}"/>')
    S.add('<rect x="60" y="14" width="300" height="252" rx="18" fill="#e3e6e8" stroke="#555" stroke-width="3"/>')
    S.add('<rect x="82" y="30" width="256" height="92" rx="8" fill="#cfe6f7" stroke="#555" stroke-width="2"/>')   # rear window
    S.add('<rect x="60" y="252" width="300" height="28" rx="6" fill="#333"/>')                                   # bumper
    for x in (86, 334):                                                                     # hazard lights flashing
        S.add(f'<rect x="{x - 12}" y="212" width="24" height="28" rx="4" fill="{AMBER}"/>')
        _flash_rays(S, x, 226, 12, AMBER)
    S.add(f'<rect x="160" y="142" width="100" height="100" fill="#f7d117" stroke="{navy}" stroke-width="7"/>')
    for cx, h in ((194, 1.0), (226, 0.82)):                                                 # two children walking
        S.add(f'<g transform="translate({cx},226) scale({h})" fill="{navy}"><circle cx="0" cy="-58" r="9"/>'
              f'<path d="M-9,-46 h18 l4,26 h-6 l-2,-14 l-2,32 h-6 l-1,-22 l-1,22 h-6 l-2,-32 l-2,14 h-6 z"/></g>')
    S.add(f'<path d="M203,190 L213,194" stroke="{navy}" stroke-width="4" stroke-linecap="round"/>')          # holding hands
    return str(S)


# ------------------------------------------------------ vehicle & safety ---

def medicaments_niveaux(params):
    """The three medicine pictograms (arrêté of 8 August 2008) side by side, with their headline."""
    S = SVG(480, 220)
    S.add(f'<rect x="0" y="0" width="480" height="220" fill="{PAPER}"/>')
    for i, (colour, text) in enumerate((("#f7d117", "Soyez prudent"), ("#f28c00", "Soyez très prudent"), ("#d8232a", "Ne pas conduire"))):
        cx, level = 80 + i * 160, i + 1
        S.add(f'<path d="M{cx},18 L{cx + 70},142 L{cx - 70},142 Z" fill="{colour}" stroke="#000" stroke-width="3" stroke-linejoin="round"/>')
        S.add(f'<g transform="translate({cx},96) scale(.7)"><rect x="-38" y="-14" width="76" height="30" rx="8" fill="#000"/>'
              f'<rect x="-24" y="-30" width="48" height="20" rx="6" fill="#000"/><circle cx="-22" cy="20" r="8" fill="#000"/>'
              f'<circle cx="22" cy="20" r="8" fill="#000"/></g>')
        _text(S, cx, 134, f"NIVEAU {level}", 13, "#000", weight=800)
        _text(S, cx, 176, f"Niveau {level}", 17)
        _text(S, cx, 202, text, 15, weight=400)
    return str(S)


def etiquettes_carburant(params):
    """EN 16942 fuel labels: empty circle, square, diamond on the front; E10, B7, LPG and the fuel on the back."""
    verso = params.get("verso", False)
    S = SVG(480, 230)
    S.add(f'<rect x="0" y="0" width="480" height="230" fill="{PAPER}"/>')
    for cx, shape, code, name in ((80, "circle", "E10", "essence"), (240, "square", "B7", "gazole"), (400, "diamond", "LPG", "gaz (GPL)")):
        if shape == "circle":
            S.add(f'<circle cx="{cx}" cy="90" r="58" fill="{PAPER}" stroke="#111" stroke-width="8"/>')
        elif shape == "square":
            S.add(f'<rect x="{cx - 56}" y="34" width="112" height="112" fill="{PAPER}" stroke="#111" stroke-width="8"/>')
        else:
            S.add(f'<path d="M{cx},24 L{cx + 66},90 L{cx},156 L{cx - 66},90 Z" fill="{PAPER}" stroke="#111" stroke-width="8" stroke-linejoin="round"/>')
        if verso:
            _text(S, cx, 104, code, 36, "#111", weight=800)
        _slot(S, cx, 181, None, name, verso)
    return str(S)


def _alpine_symbol(cx, cy, s=1.0, colour=INK):
    """Three-peak mountain with a snowflake (3PMSF), outline style as moulded on a sidewall."""
    flake = "".join(f'<path d="M0,0 L0,-11" transform="rotate({a})"/>' for a in range(0, 360, 60))
    return (f'<g transform="translate({cx},{cy}) scale({s})" fill="none" stroke="{colour}" stroke-width="3" stroke-linejoin="round">'
            f'<path d="M-34,22 L-18,-6 L-8,8 L4,-22 L20,6 L26,-2 L36,22 Z"/>'
            f'<g transform="translate(2,6)" stroke-width="2.5">{flake}</g></g>')


def pneu_flanc(params):
    """Strip of tyre sidewall with moulded markings. mode '3pmsf' (M+S and alpine symbol) or 'comparaison'
    (1: M+S alone; 2: M+S and alpine symbol). On the back of '3pmsf', each marking is named in place."""
    verso = params.get("verso", False)
    mode = params.get("mode", "3pmsf")
    rows = [(False, "M+S seul : ne suffit plus"), (True, "M+S et symbole alpin : pneu hiver")] if mode == "comparaison" \
        else [(True, None)]
    moulded = "#d0d0d0"
    S = SVG(480, 170 * len(rows) + 10)
    S.add(f'<rect x="0" y="0" width="480" height="{S.h}" fill="{PAPER}"/>')
    for i, (alpine, caption) in enumerate(rows):
        y = 10 + i * 170
        S.add(f'<rect x="20" y="{y}" width="440" height="120" rx="60" fill="#2b2b2b"/>')
        S.add(f'<path d="M60,{y + 18} H420 M60,{y + 102} H420" stroke="#3d3d3d" stroke-width="3"/>')
        _text(S, 150 if alpine else 240, y + 74, "M+S", 36, moulded, weight=800)
        if alpine:
            S.add(_alpine_symbol(320, y + 58, 1.3, moulded))
        if caption:
            _text(S, 44, y + 72, str(i + 1), NUMBER_SIZE, MARK, weight=800)
            _text(S, 240, y + 152, caption, LABEL_SIZE)       # an explanatory comparison: captions on both sides
        elif verso:
            _text(S, 150, y + 152, "M+S", LABEL_SIZE, ANSWER)
            _text(S, 320, y + 152, "symbole alpin (3PMSF)", LABEL_SIZE, ANSWER)
    return str(S)


def pneu_usure(params):
    """Tread seen from above with wear bars at the bottom of the main grooves, and a groove in section."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{PAPER}"/>')
    S.add('<rect x="30" y="20" width="200" height="260" rx="14" fill="#2f2f2f"/>')
    for x in (78, 130, 182):
        S.add(f'<rect x="{x - 9}" y="20" width="18" height="260" fill="#151515"/>')
        for y in (70, 190):
            S.add(f'<rect x="{x - 9}" y="{y}" width="18" height="10" fill="#8a8a8a"/>')
    S.add(f'<path d="M130,75 C180,70 230,60 258,60" stroke="{INK}" stroke-width="2.5" fill="none"/>')
    _text(S, 262, 56, "témoin d’usure", 17, anchor="start")
    _text(S, 262, 76, "au fond d’une rainure", 15, anchor="start", weight=400)
    S.add('<path d="M270,150 H330 V240 H350 V214 H370 V240 H390 V150 H450 V270 H270 Z" fill="#2f2f2f"/>')
    S.add(f'<path d="M345,150 H375 M345,214 H375 M360,150 V214" stroke="{INK}" stroke-width="2.5"/>')
    _text(S, 360, 140, "rainure", 15)
    _text(S, 360, 292, "limite légale : 1,6 mm de rainure", 15, weight=400)
    return str(S)


def angles_morts(params):
    """Plan view: my car, what the mirrors show (VISIBLE cones) and the two blind spots (HIDDEN hatch), a motorbike in one.
    The zones are indicative: they vary with the vehicle and the mirror setting.
    answer_on_back: the blind spots and the motorbike are the answer, drawn only on the back of a « verso » image."""
    S = SVG(480, 420)
    S.add(f'<rect x="0" y="0" width="480" height="420" fill="{ASPHALT}"/>')
    for x in (160, 320):
        S.add(f'<path d="M{x},0 V420" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 20"/>')
    cx, cy = 240, 150
    for pts in (f"{cx - 14},{cy + 40} {cx - 50},420 {cx + 50},420 {cx + 14},{cy + 40}",
                f"{cx - 30},{cy - 10} {cx - 150},420 {cx - 70},420", f"{cx + 30},{cy - 10} {cx + 150},420 {cx + 70},420"):
        S.add(f'<polygon points="{pts}" fill="{VISIBLE}" opacity="0.3"/>')
    answer = params.get("verso") or not params.get("answer_on_back")
    if answer:
        _hidden_pattern(S)
        for side in (-1, 1):
            x_in, x_out = cx + side * 40, cx + side * 200    # across the whole neighbouring lane
            S.add(f'<path d="M{x_in},{cy - 20} L{x_out},{cy + 10} L{x_out},{cy + 150} L{x_in},{cy + 70} Z" fill="url(#hidden)" stroke="{HIDDEN}" stroke-width="2"/>')
    S.add(f'<g transform="translate({cx},{cy}) scale(1.4)">{ME}</g>')
    if answer:
        S.add(f'<g transform="translate(80,{cy + 60}) scale(1.3)">{vehicle_sprite("moto", "rouge")}</g>')  # mid-lane
        _pill(S, 16, 30, "angles morts")
    _pill(S, 464, 404, "vu dans les rétroviseurs", anchor="end")
    return str(S)


def ceinture(params):
    """Occupant seen from the front: lap belt low on the pelvis bones, diagonal over the middle of the shoulder and the
    sternum. Variants: 'enceinte' (lap belt under the belly, diagonal beside it), 'sous_bras' (what not to do, crossed)."""
    variant = params.get("variante", "correcte")
    S = SVG(360, 420)
    S.add(f'<rect x="0" y="0" width="360" height="420" fill="{PAPER}"/>')
    S.add(f'<rect x="70" y="60" width="220" height="340" rx="30" fill="{SEAT}"/>')                  # seat back
    S.add(f'<rect x="130" y="20" width="100" height="60" rx="16" fill="{SEAT_DARK}"/>')                  # head rest
    S.add(f'<circle cx="180" cy="82" r="36" fill="{SKIN}"/>')                                      # head
    S.add(f'<path d="M110,140 Q180,112 250,140 L262,300 L98,300 Z" fill="{CLOTH}"/>')               # torso
    S.add(f'<path d="M110,140 L78,280 M250,140 L282,280" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>')
    S.add(f'<path d="M98,300 H262 L256,352 H104 Z" fill="{CLOTH_DARK}"/>')                               # hips
    if variant == "enceinte":
        S.add('<ellipse cx="180" cy="262" rx="62" ry="46" fill="#6d8aa8"/>')
    belt = WRONG if variant == "sous_bras" else INK
    if variant == "sous_bras":
        S.add(f'<path d="M262,210 L112,318" stroke="{belt}" stroke-width="14" stroke-linecap="round"/>')
    else:
        mid, low = ("150,190", "116,246") if variant == "enceinte" else ("170,215", "140,262")
        S.add(f'<path d="M222,132 C205,175 {mid} {low} L112,318" fill="none" stroke="{belt}" stroke-width="14" stroke-linecap="round"/>')
    lap_y = 322 if variant == "enceinte" else 314
    S.add(f'<path d="M100,{lap_y} Q180,{lap_y + 10} 260,{lap_y}" fill="none" stroke="{belt}" stroke-width="14" stroke-linecap="round"/>')
    S.add('<rect x="102" y="306" width="22" height="18" rx="3" fill="#9e9e9e"/>')                  # buckle
    if variant == "sous_bras":
        S.add(f'<path d="M60,40 L300,380 M300,40 L60,380" stroke="{WRONG}" stroke-width="8" opacity="0.8"/>')
    return str(S)


# ------------------------------------------------ motorway ramps, level crossings ---

def bretelle(params):
    """Motorway (traffic left to right) with an auxiliary lane on the right: 'insertion' (acceleration lane closing
    ahead) or 'sortie' (deceleration lane opening ahead). vehicles: [{lane: gauche|droite|bretelle, x, me, colour}].
    A label names the auxiliary lane when `label` is given."""
    mode = params.get("mode", "insertion")
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="150" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="42" width="480" height="4" fill="{MARK}"/>')
    _dashes_h(S, 115, 3, 10)
    if mode == "insertion":
        S.add(f'<path d="M0,190 L260,190 L480,190 L260,260 L0,260 Z" fill="{ASPHALT}"/>')
        _dashes_h(S, 190, 3, 3.5, w=5, x1=260)
        S.add(f'<path d="M260,260 L480,190 L480,192 L262,262 Z" fill="{MARK}"/>')
    else:
        S.add(f'<path d="M0,190 L220,260 L480,260 L480,190 Z" fill="{ASPHALT}"/>')
        _dashes_h(S, 190, 3, 3.5, w=5, x0=220)
        S.add(f'<path d="M0,190 L220,260 L218,262 L0,192 Z" fill="{MARK}"/>')
    ys = {"gauche": 78, "droite": 152, "bretelle": 226}
    for v in params.get("vehicles", []):
        sprite = _body({"me": True}, 90) if v.get("me") else vehicle_sprite("car", v.get("colour", "gris"))
        S.add(f'<g transform="translate({v["x"]},{ys[v["lane"]]}) rotate(90)">{sprite}</g>')
    if params.get("label"):
        _pill(S, 470, 288, params["label"], anchor="end")
    return str(S)


def pn_face(params):
    """Level crossing with automatic half barriers (G2) seen from the approach: on each side of the road a single
    flashing red light R24 (no St Andrew's cross: it marks crossings without barriers), lit when `feux`, and the half
    barrier 'haute', 'mi' (moving) or 'basse'."""
    S = SVG(420, 320)
    S.add(f'<rect x="0" y="0" width="420" height="320" fill="{PAPER}"/>')
    S.add('<rect x="0" y="282" width="420" height="38" fill="#7a7a7a"/>')
    S.add('<rect x="96" y="100" width="10" height="186" fill="#9a9a9a"/>')
    S.add('<circle cx="101" cy="80" r="38" fill="#222" stroke="#000" stroke-width="2"/>')
    lit = params.get("feux", True)
    _lamp(S, 101, 80, 24, RED, on=lit, blink=lit)
    angle = {"haute": -84, "mi": -38, "basse": 0}[params.get("barriere", "haute")]
    S.add('<rect x="176" y="246" width="34" height="40" rx="4" fill="#d9d9d9" stroke="#777"/>')
    S.add(f'<g transform="translate(200,258) rotate({angle})">'
          f'<rect x="0" y="-7" width="210" height="14" fill="{PAPER}" stroke="#777" stroke-width="1.5"/>'
          + "".join(f'<rect x="{10 + 40 * i}" y="-7" width="20" height="14" fill="{SIGN_RED}"/>' for i in range(5)) + '</g>')
    return str(S)


def pn_plan(params):
    """Level crossing from above (traffic of my lane goes up): two tracks across the road, half barriers on the
    right-hand side of each approach ('basses' or 'hautes'), red lights flashing when `feux` (drawn only lit), optional stopped
    queue just after the tracks in my lane."""
    S = SVG(480, 440)
    S.add(f'<rect x="0" y="0" width="480" height="440" fill="{GRASS}"/>')
    x0, w = 150, 180                                         # road: two lanes of 90
    S.add(f'<rect x="{x0}" y="0" width="{w}" height="440" fill="{ASPHALT}"/>')
    S.add(f'<path d="M{x0 + w / 2},0 V440" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 18"/>')
    for ty in (170, 210):                                   # two tracks: sleepers and rails
        for x in range(0, 480, 16):
            S.add(f'<rect x="{x}" y="{ty - 12}" width="8" height="24" fill="#8d7b68"/>')
        for dy in (-7, 7):
            S.add(f'<path d="M0,{ty + dy} H480" stroke="{RAIL}" stroke-width="3"/>')
    low = params.get("barrieres", "basses") == "basses"
    # each approach has its half barrier and its light on its right: mine (going up) east, the other one west
    for post_x, post_y, arm, light_x in ((x0 + w + 12, 252, -1, x0 + w + 44), (x0 - 12, 128, 1, x0 - 44)):
        S.add(f'<rect x="{post_x - 8}" y="{post_y - 8}" width="16" height="16" fill="#d9d9d9" stroke="#777"/>')
        end = post_x + arm * ((w / 2 + 10) if low else 24)
        S.add(f'<path d="M{post_x},{post_y} H{end}" stroke="{PAPER}" stroke-width="9"/>'
              f'<path d="M{post_x},{post_y} H{end}" stroke="{SIGN_RED}" stroke-width="9" stroke-dasharray="12 12"/>')
        if params.get("feux", low):
            _lamp(S, light_x, post_y, 9, RED, blink=True)
    if params.get("file"):
        for i in range(3):
            y = 104 - i * 94
            S.add(f'<g transform="translate({x0 + w * 0.75},{y})">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<g transform="translate({x0 + w * 0.75},{380})">{ME}</g>')
    return str(S)


# ------------------------------------------------------------ parked street ---

def _dim_v(S, x, y0, y1, label):
    """Vertical dimension: a bar with end ticks and its measure on the right, in INK."""
    S.add(f'<path d="M{x},{y0} V{y1} M{x - 8},{y0} h16 M{x - 8},{y1} h16" stroke="{INK}" stroke-width="3" fill="none"/>')
    _text(S, x + 14, (y0 + y1) / 2 + 7, label, LABEL_SIZE, INK, "start")


ME_PATH = YELLOW                     # the yellow of MOI's halo: where MOI is going


def rue_stationnement(params):
    """Two-way street seen from above, my lane going up, a parking lane on the right along the pavement.
    parked: y centres of the parked cars; door: index of the car whose driver's door is open;
    door_label: its reach, written on the pavement; me: y of MOI (with a door open, the line its right side follows);
    crossing: y of a zebra crossing, with `no_parking` the 5 m before it (upstream) marked and measured;
    child: y of a child standing in a gap between the parked cars, about to step out (with answer_on_back, the child
    and the side-view inset are drawn only on the back of a « verso » image)."""
    S = SVG(420, 400, view=(80, 0, 340, 400))                                 # half of the oncoming lane is enough
    S.add(f'<rect x="0" y="0" width="420" height="400" fill="#cfd3d4"/>')     # pavements
    road0, axis, park0, park1 = 30, 120, 210, 272
    S.add(f'<rect x="{road0}" y="0" width="{park1 - road0}" height="400" fill="{ASPHALT}"/>')
    S.add(f'<path d="M{axis},0 V400" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 30"/>')
    for x in (road0, park1):
        S.add(f'<rect x="{x - 3}" y="0" width="6" height="400" fill="#9aa0a2"/>')    # kerbs
    px = (park0 + park1) / 2
    cross = params.get("crossing")
    if cross is not None:
        for x in range(road0 + 6, park1 - 10, 24):
            S.add(f'<rect x="{x}" y="{cross - 30}" width="14" height="60" fill="{MARK}"/>')
        if params.get("no_parking"):
            y0, y1 = cross + 34, cross + 34 + 100                               # 5 m at 20 px/m, upstream
            S.add(f'<rect x="{park0 + 4}" y="{y0}" width="{park1 - park0 - 10}" height="{y1 - y0}" fill="none" '
                  f'stroke="{WRONG}" stroke-width="3" stroke-dasharray="8 6"/>')
            S.add(f'<path d="M{park0 + 8},{y0 + 4} L{park1 - 10},{y1 - 4} M{park1 - 10},{y0 + 4} L{park0 + 8},{y1 - 4}" '
                  f'stroke="{WRONG}" stroke-width="3"/>')
            _dim_v(S, park1 + 22, y0, y1, "5 m")
    for i, y in enumerate(params.get("parked", [])):
        S.add(f'<g transform="translate({px},{y})">{vehicle_sprite("car", "gris")}</g>')
        if i == params.get("door"):
            # driver's door (left side, towards traffic) hinged at its front edge, swung open about 60°:
            # it reaches about 1 m (22 px) into the lane
            S.add(f'<path d="M{px - 22},{y + 10} A26,26 0 0 1 {px - 44.5},{y - 3}" fill="none" stroke="{MARK}" '
                  f'stroke-width="2" stroke-dasharray="4 3"/>')
            S.add(f'<rect x="-4.5" y="0" width="9" height="26" rx="2" fill="{CAR_COLOURS["gris"]}" stroke="#111" '
                  f'stroke-width="1.5" transform="translate({px - 22},{y - 16}) rotate(60)"/>')
            if params.get("door_label"):
                S.add(f'<path d="M{px + 26},{y - 6} H{park1 + 12}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="4 4"/>')
                _text(S, park1 + 16, y, params["door_label"], LABEL_SIZE, INK, "start")
    if params.get("child") is not None and (params.get("verso") or not params.get("answer_on_back")):
        y = params["child"]
        S.add(pedestrian(px - 4, y + 4))
        S.add(f'<path d="M{px - 20},{y} H{px - 50} m8,-7 l-8,7 l8,7" fill="none" stroke="{MARK}" stroke-width="3"/>')
        # side view on the pavement: the child, shorter than the car, is hidden behind it (hatched, dashed outline)
        mx, my = park1 + 14, 60
        S.add(f'<rect x="{mx}" y="{my}" width="130" height="92" rx="10" fill="{PAPER}" stroke="#9aa0a2" stroke-width="2"/>')
        S.add(f'<g transform="translate({mx + 8},{my + 84}) scale(0.48)">' + _car_side(0, 0, "gris") + '</g>')
        _hidden_pattern(S, "cache")
        S.add(f'<g transform="translate({mx + 74},{my + 80})"><circle cx="0" cy="-30" r="6" fill="url(#cache)" '
              f'stroke="{INK}" stroke-width="1.5" stroke-dasharray="3 2"/><rect x="-5" y="-23" width="10" height="20" rx="4" '
              f'fill="url(#cache)" stroke="{INK}" stroke-width="1.5" stroke-dasharray="3 2"/></g>')
    if params.get("me") is not None:
        me_x = px - 22 - 22 - 22            # a door's reach (≈ 1 m, 22 px) between MOI and the parked cars
        if params.get("door") is not None:
            S.add(f'<path d="M{me_x + 22},{params["me"] - 54} V0" stroke="{ME_PATH}" stroke-width="2.5" stroke-dasharray="8 6"/>')
        S.add(f'<g transform="translate({me_x},{params["me"]})">{ME}</g>')
    return str(S)


# ------------------------------------------------------ distances, lines ---
REACTION, BRAKING = VISIBLE, "#f6d0cb"     # pale yellow: I have not braked yet; pale sign red: I brake


def distance_arret(params):
    """Stopping distance as bars to scale: reaction then braking, one row per case.
    rows: [{label?, reaction, freinage}] in metres; `named` writes the words in the bars instead of the metres
    (and no legend), `total` writes each row's stopping distance at its end."""
    rows, named = params["rows"], params.get("named", False)
    L = 64 if any(r.get("label") for r in rows) else 16
    right = 84 if params.get("total") else 16
    top = 20 if named else 56
    H = top + 64 * len(rows) + (52 if named else 8)
    S = SVG(480, H)
    S.add(f'<rect x="0" y="0" width="480" height="{H}" fill="{PAPER}"/>')
    scale = (480 - L - right) / max(r["reaction"] + r["freinage"] for r in rows)
    if not named:
        for i, (name, fill, stroke) in enumerate((("réaction", REACTION, YELLOW), ("freinage", BRAKING, SIGN_RED))):
            x = L + i * 150
            S.add(f'<rect x="{x}" y="14" width="22" height="22" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            _text(S, x + 30, 32, name, LABEL_SIZE, INK, "start", 400)
    for i, r in enumerate(rows):
        y = top + 64 * i
        if r.get("label"):
            _text(S, L - 12, y + 32, r["label"], NUMBER_SIZE, INK, "end")
        x = L
        for key, fill, stroke in (("reaction", REACTION, YELLOW), ("freinage", BRAKING, SIGN_RED)):
            w = r[key] * scale
            S.add(f'<rect x="{x}" y="{y + 8}" width="{w}" height="40" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            _text(S, x + w / 2, y + 34, ("réaction" if key == "reaction" else "freinage") if named else f"{r[key]:g} m",
                  LABEL_SIZE, INK, "middle", 700)
            x += w
        if params.get("total"):
            _text(S, x + 10, y + 34, f"= {r['reaction'] + r['freinage']:g} m", LABEL_SIZE, INK, "start")
        if named:                                                   # the sum, spanned under the bar
            S.add(f'<path d="M{L},{y + 58} v8 H{x} v-8" fill="none" stroke="{INK}" stroke-width="2.5"/>')
            _text(S, (L + x) / 2, y + 90, "distance d’arrêt", LABEL_SIZE, INK)
    return str(S)


def ligne_continue_gestes(params):
    """The two gestures on a continuous line, side by side: straddle it (chevaucher), cross it entirely (franchir)."""
    S = SVG(480, 330)
    S.add(f'<rect x="0" y="0" width="480" height="330" fill="{PAPER}"/>')
    for cx, name in ((120, "chevaucher"), (360, "franchir")):
        S.add(f'<rect x="{cx - 90}" y="0" width="180" height="290" fill="{ASPHALT}"/>')
        S.add(f'<path d="M{cx},0 V290" stroke="{MARK}" stroke-width="5"/>')
        _text(S, cx, 318, name, LABEL_SIZE, INK)
    S.add(f'<g transform="translate(120,150) rotate(-12)">{ME}</g>')                  # wheels on both sides
    S.add(f'<path d="M405,280 C405,200 315,190 315,110" fill="none" stroke="{ME_PATH}" stroke-width="3" stroke-dasharray="8 6"/>')
    S.add(f'<g transform="translate(315,100)">{ME}</g>')                               # entirely on the other side
    return str(S)


# ------------------------------------------------------ at the wheel ---

def _limb(a, b, width, colour):
    return (f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{colour}" stroke-width="{width}" '
            f'stroke-linecap="round"/>')


def _knee(hip, ankle, thigh, shin, up=True):
    """Middle joint of a two-segment limb (knee, elbow): bends towards the top of the drawing, or down with up=False."""
    dx, dy = ankle[0] - hip[0], ankle[1] - hip[1]
    d = math.hypot(dx, dy)
    if d > thigh + shin:
        raise ValueError("the leg cannot reach the pedal")
    along = (thigh ** 2 - shin ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(max(thigh ** 2 - along ** 2, 0))
    ux, uy = dx / d, dy / d
    s = 1 if up else -1
    return hip[0] + ux * along + s * uy * h, hip[1] + uy * along - s * ux * h


SEAT_HIP, SEAT_LEAN = (160, 250), math.radians(15)     # side views: occupant's hip on the cushion, backrest lean


def _side_seat(S, head_top):
    """Front seat seen from the side (car front to the right), backrest leaning back; the head restraint's top front
    corner at `head_top` (distance along the backrest from hip level), right behind the head of an adult occupant."""
    up, fwd = (-math.sin(SEAT_LEAN), -math.cos(SEAT_LEAN)), (math.cos(SEAT_LEAN), -math.sin(SEAT_LEAN))
    ox, oy = SEAT_HIP[0] - fwd[0] * 25, SEAT_HIP[1] - fwd[1] * 25          # backrest front face, at hip level
    S.add(f'<g transform="translate({ox:.1f},{oy:.1f}) rotate(-15)">'
          f'<rect x="-22" y="-172" width="6" height="30" fill="#9aa0a2"/>'
          f'<rect x="-34" y="{-head_top / math.cos(SEAT_LEAN) - 4:.1f}" width="34" height="62" rx="12" fill="{SEAT_DARK}"/>'
          f'<rect x="-36" y="-158" width="36" height="190" rx="14" fill="{SEAT}"/></g>')
    S.add(f'<path d="M116,262 L264,248 Q274,248 274,258 L274,272 Q274,282 264,282 L124,298 Z" fill="{SEAT}"/>')
    S.add(f'<rect x="196" y="292" width="44" height="50" fill="{SEAT_DARK}"/>')
    S.add(f'<path d="M352,150 L480,140 L480,240 L346,232 Q336,190 352,150 Z" fill="{SEAT_DARK}"/>')   # dashboard


def poste_conduite(params):
    """Driver seen from the side (car front to the right), in the settings check: pedal pressed fully with the leg
    still slightly bent, shoulders against the backrest, arms straight with the wrists on top of the wheel, top of
    the head restraint level with the top of the head, close behind it. `focus`: jambe | bras | tete adds the
    matching callout."""
    S = SVG(480, 360)
    S.add(f'<rect x="0" y="0" width="480" height="360" fill="{PAPER}"/>')
    S.add('<rect x="0" y="342" width="480" height="18" fill="#9aa0a2"/>')                         # floor
    up, fwd = (-math.sin(SEAT_LEAN), -math.cos(SEAT_LEAN)), (math.cos(SEAT_LEAN), -math.sin(SEAT_LEAN))
    hip, torso, neck, half, head_r = SEAT_HIP, 150, 40, 25, 26
    at = lambda d_up, d_fwd=0: (hip[0] + up[0] * d_up + fwd[0] * d_fwd, hip[1] + up[1] * d_up + fwd[1] * d_fwd)  # noqa: E731
    shoulder, head = at(torso), at(torso + neck)
    _side_seat(S, torso + neck + head_r)
    # steering column and pedal hanging from under the dashboard
    tilt, wheel_r = math.radians(20), 45
    wrist = (shoulder[0] + 165 * math.cos(math.radians(10)), shoulder[1] + 165 * math.sin(math.radians(10)))
    # the rim's top leans forward: centre and bottom lie back and down from the wrist resting on the top
    centre = (wrist[0] - wheel_r * math.sin(tilt), wrist[1] + 7 + wheel_r * math.cos(tilt))
    rim_top = (centre[0] + wheel_r * math.sin(tilt), centre[1] - wheel_r * math.cos(tilt))
    bottom = (centre[0] - wheel_r * math.sin(tilt), centre[1] + wheel_r * math.cos(tilt))
    S.add(_limb(centre, (centre[0] + 104 * math.cos(tilt), centre[1] + 104 * math.sin(tilt)), 12, "#555"))
    pad = (402, 300)
    S.add(_limb((414, 236), pad, 7, "#555") + _limb((pad[0] - 3, pad[1] - 14), (pad[0] + 5, pad[1] + 12), 10, "#333"))
    # leg: thigh along the cushion, knee slightly bent, foot pressing the pedal fully
    ankle = (378, 314)
    knee = _knee(hip, ankle, 122, 122)
    S.add(_limb(hip, knee, 38, CLOTH_DARK) + _limb(knee, ankle, 30, CLOTH_DARK))
    S.add(_limb(ankle, (pad[0] - 2, pad[1] - 4), 16, "#333"))                              # shoe on the pedal
    # torso, head, steering wheel seen edge-on, then the near arm: straight, wrist on the top of the rim
    S.add(_limb(hip, shoulder, 2 * half, CLOTH))
    S.add(f'<circle cx="{head[0]:.1f}" cy="{head[1]:.1f}" r="{head_r}" fill="{SKIN}"/>')
    S.add(_limb(rim_top, bottom, 12, "#333"))
    focus = params.get("focus")
    if focus == "bras":          # the backrest test: arms straight, wrists resting on the top of the rim
        S.add(_limb(shoulder, wrist, 20, CLOTH) + _limb(wrist, (wrist[0] + 16, wrist[1] + 8), 14, SKIN))
    else:                        # driving: hands on the rim at 9 h 15 (the centre, seen from the side), elbows bent
        d = math.hypot(centre[0] - shoulder[0], centre[1] - shoulder[1])
        grip_wrist = (centre[0] - 16 * (centre[0] - shoulder[0]) / d, centre[1] - 16 * (centre[1] - shoulder[1]) / d)
        elbow = _knee(shoulder, grip_wrist, 84, 84, up=False)
        S.add(_limb(shoulder, elbow, 20, CLOTH) + _limb(elbow, grip_wrist, 18, CLOTH) + _limb(grip_wrist, centre, 14, SKIN))
    if focus == "tete":
        y = head[1] - head_r
        S.add(f'<path d="M30,{y:.1f} H200" stroke="{INK}" stroke-width="2" stroke-dasharray="6 5"/>')
        _pill(S, 214, y + 7, "même hauteur")
    elif focus == "jambe":
        _pill(S, 214, 334, "jambe encore fléchie")
    elif focus == "bras":
        _pill(S, 200, 44, "poignets sur le haut du volant")
    return str(S)


def siege_dos_route(params):
    """Front passenger seat from the side with a rear-facing infant carrier: the baby's head is at the high end of the
    shell, towards the dashboard, where an active frontal airbag would strike."""
    S = SVG(480, 360)
    S.add(f'<rect x="0" y="0" width="480" height="360" fill="{PAPER}"/>')
    S.add('<rect x="0" y="342" width="480" height="18" fill="#9aa0a2"/>')                         # floor
    _side_seat(S, 216)
    # carrier shell on the cushion, reclined, its back facing forward; the baby lies in it facing the rear
    S.add('<path d="M168,246 Q176,282 214,280 L262,262 Q300,244 306,176 L290,172 Q284,232 250,246 L206,262 Q186,262 182,242 Z" '
          'fill="#6d8aa8" stroke="#3e556b" stroke-width="2"/>')
    S.add(_limb((206, 252), (262, 222), 22, "#f7e3a1"))                                   # body in a light suit
    S.add(f'<circle cx="276" cy="200" r="15" fill="{SKIN}"/>')
    S.add('<path d="M188,236 Q240,150 300,170" fill="none" stroke="#3e556b" stroke-width="6"/>')        # handle
    # the airbag, deployed from the dashboard, reaching the shell at the head
    S.add(f'<ellipse cx="338" cy="188" rx="48" ry="42" fill="{PAPER}" stroke="{WRONG}" stroke-width="3" stroke-dasharray="8 5"/>')
    _pill(S, 470, 124, "airbag", colour=WRONG, anchor="end")
    return str(S)


def volant_mains(params):
    """Steering wheel from the driver's seat, hands at 9 h 15: each hand grips the rim just above the side spoke,
    thumb resting along the rim instead of hooked round the spoke."""
    S = SVG(420, 340)
    S.add(f'<rect x="0" y="0" width="420" height="340" fill="{PAPER}"/>')
    cx, cy, r = 210, 170, 120
    S.add(f'<path d="M{cx - r + 6},{cy + 8} H{cx + r - 6} M{cx},{cy} V{cy + r - 6}" stroke="#555" stroke-width="18"/>')
    S.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#333" stroke-width="22"/>')
    S.add(f'<circle cx="{cx}" cy="{cy + 4}" r="40" fill="#555"/>')
    for side in (-1, 1):
        x = cx + side * r
        S.add(f'<rect x="{x - 19}" y="{cy - 30}" width="38" height="46" rx="16" fill="{SKIN}" stroke="#c99a70" stroke-width="2"/>')
        # thumb along the inside of the rim, pointing up (mirrored for the right hand)
        rho = r - 12
        thumb = [(cx - side * rho * math.cos(math.radians(a)), cy - rho * math.sin(math.radians(a))) for a in (172, 160)]
        S.add(_limb(thumb[0], thumb[1], 14, SKIN))
    return str(S)


def retroviseur(params):
    """What a well set mirror shows. vue: 'interieur' (the whole rear window, framed by the cabin) or 'exterieur'
    (left door mirror: the road behind and beside, a thin strip of my own car on the inner edge, horizon mid-height)."""
    if params.get("vue", "interieur") == "interieur":
        S = SVG(480, 200)
        S.add(f'<rect x="0" y="0" width="480" height="200" fill="{PAPER}"/>')
        S.add('<rect x="20" y="24" width="440" height="152" rx="44" fill="#222"/>')
        S.add('<clipPath id="glace"><rect x="32" y="36" width="416" height="128" rx="34"/></clipPath>')
        S.add(f'<g clip-path="url(#glace)"><rect x="0" y="0" width="480" height="200" fill="{SEAT}"/>'   # cabin lining
              + "".join(f'<rect x="{x - 26}" y="148" width="52" height="30" rx="10" fill="{SEAT_DARK}"/>' for x in (130, 350))
              + '</g>')                                                  # rear head restraints, below the window
        S.add('<clipPath id="lunette"><path d="M96,52 H384 L412,140 H68 Z"/></clipPath>')
        S.add('<g clip-path="url(#lunette)">'
              '<rect x="0" y="0" width="480" height="200" fill="#dbe9f5"/>'
              f'<rect x="0" y="98" width="480" height="102" fill="{GRASS}"/>'
              f'<path d="M190,98 H290 L400,160 H80 Z" fill="{ASPHALT}"/>'
              f'<rect x="220" y="108" width="40" height="22" rx="6" fill="{CAR_COLOURS["gris"]}" stroke="#111" stroke-width="1.5"/>'
              '<rect x="226" y="112" width="28" height="7" rx="2" fill="#cfe6f7"/></g>')
        S.add('<path d="M96,52 H384 L412,140 H68 Z" fill="none" stroke="#9aa0a2" stroke-width="4"/>')
        return str(S)
    S = SVG(360, 260)
    S.add(f'<rect x="0" y="0" width="360" height="260" fill="{PAPER}"/>')
    S.add('<path d="M40,40 H300 Q330,40 330,70 V200 Q330,230 300,230 H70 Q30,230 26,190 L20,80 Q18,40 40,40 Z" fill="#222"/>')
    S.add('<clipPath id="miroir"><path d="M48,54 H296 Q316,54 316,74 V196 Q316,216 296,216 H74 Q44,216 40,186 L34,84 Q32,54 48,54 Z"/></clipPath>')
    S.add('<g clip-path="url(#miroir)">'
          '<rect x="0" y="0" width="360" height="135" fill="#dbe9f5"/>'
          f'<rect x="0" y="135" width="360" height="125" fill="{GRASS}"/>'
          f'<path d="M150,135 H190 L300,260 H-40 Z" fill="{ASPHALT}"/>'
          f'<path d="M170,138 L150,260" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 14"/>'
          f'<rect x="120" y="150" width="34" height="20" rx="5" fill="{CAR_COLOURS["gris"]}" stroke="#111" stroke-width="1.5"/>'
          '<rect x="125" y="153" width="24" height="6" rx="2" fill="#cfe6f7"/>'
          f'<path d="M286,0 H360 V260 H276 Q270,130 286,0 Z" fill="{CAR_COLOURS["bleu"]}"/></g>')         # my car's side
    return str(S)


def champ_visuel(params):
    """Plan view: from my seat, the narrow central vision (reads, identifies) inside the wide peripheral field
    (detects movement), and a pedestrian stepping off the pavement on the edge of the field."""
    S = SVG(480, 400)
    S.add(f'<rect x="0" y="0" width="480" height="400" fill="#cfd3d4"/>')
    S.add(f'<rect x="100" y="0" width="260" height="400" fill="{ASPHALT}"/>')
    S.add(f'<path d="M230,0 V400" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 30"/>')
    eye = (290, 300)
    R = 250
    wide = [(eye[0] + R * math.sin(math.radians(a)), eye[1] - R * math.cos(math.radians(a))) for a in range(-90, 91, 10)]
    S.add(f'<path d="M{eye[0]},{eye[1]} ' + " ".join(f"L{x:.0f},{y:.0f}" for x, y in wide) + f' Z" fill="{VISIBLE}" opacity="0.35"/>')
    narrow = [(eye[0] + R * math.sin(math.radians(a)), eye[1] - R * math.cos(math.radians(a))) for a in (-6, 6)]
    S.add(f'<path d="M{eye[0]},{eye[1]} L{narrow[0][0]:.0f},{narrow[0][1]:.0f} L{narrow[1][0]:.0f},{narrow[1][1]:.0f} Z" '
          f'fill="{YELLOW}" opacity="0.55"/>')
    S.add(f'<g transform="translate(290,330)">{ME}</g>')
    S.add(pedestrian(396, 206, scale=1.5) +
          f'<path d="M372,200 H346 m8,-7 l-8,7 l8,7" fill="none" stroke="{INK}" stroke-width="3"/>')
    _pill(S, 274, 40, "vision centrale : précise", anchor="end")
    _pill(S, 16, 250, "vision périphérique :")
    _pill(S, 16, 282, "détecte les mouvements")
    return str(S)


# ------------------------------------------------ vehicles from the side and behind, parts ---
GLASS, LOAD, LOAD_DARK = "#cfe6f7", "#c9a26b", "#8a6a3e"


def _car_side(x, y, colour="gris", tilt=0, flip=False):
    """Estate car from the side, 240 long, facing right (left with `flip`); (x, y) = rear bumper at ground level.
    `tilt` (degrees, negative = nose up) pivots the body about the rear wheel, as a load in the boot does."""
    c = CAR_COLOURS.get(colour, colour)
    body = (f'<g transform="rotate({tilt} 48 0)">'
            f'<path d="M0,-34 V-74 Q2,-82 12,-84 L20,-120 Q22,-126 30,-126 H140 Q150,-126 156,-120 L192,-86 L232,-80 '
            f'Q240,-78 240,-68 V-34 Q240,-28 234,-28 H6 Q0,-28 0,-34 Z" fill="{c}" stroke="#111" stroke-width="2"/>'
            f'<path d="M28,-118 H92 V-90 H24 Z M98,-118 H146 L176,-90 H98 Z" fill="{GLASS}" stroke="#111" stroke-width="1.5"/>'
            f'<rect x="0" y="-72" width="6" height="14" fill="#d8362d"/><rect x="232" y="-72" width="8" height="10" fill="#fff6c2"/></g>')
    wheels = "".join(f'<circle cx="{wx}" cy="-24" r="22" fill="#222"/><circle cx="{wx}" cy="-24" r="9" fill="#999"/>'
                     for wx in (48, 192))
    mirror = " translate(240,0) scale(-1,1)" if flip else ""
    return f'<g transform="translate({x},{y}){mirror}">{body}{wheels}</g>'


def feux_chargement(params):
    """Loaded car at night, two panels: headlamp levelling left at 0 (the nose rises, the beam dazzles the oncoming
    driver) and set for the load (the beam comes back onto the road)."""
    S = SVG(480, 380)
    S.add(f'<rect x="0" y="0" width="480" height="380" fill="{PAPER}"/>')
    for i, (setting, wrong) in enumerate((("molette sur 0", True), ("molette réglée", False))):
        top, ground = 190 * i, 190 * i + 170
        S.add(f'<rect x="0" y="{ground}" width="480" height="8" fill="#9aa0a2"/>')
        tilt = -4
        hx, hy = 30 + 236, ground - 66 - 236 * math.sin(math.radians(-tilt)) + 2   # headlamp once the nose has risen
        end = (480, hy - 40) if wrong else (480, ground)
        S.add(f'<path d="M{hx:.0f},{hy - 4:.0f} L{end[0]},{end[1] - 30} L{end[0]},{end[1] + 12} L{hx:.0f},{hy + 4:.0f} Z" '
              f'fill="{YELLOW}" opacity="0.45"/>')
        S.add(_car_side(30, ground, "gris", tilt))
        for bx, by, w, h in ((30, -106, 30, 16), (62, -100, 24, 10)):                  # load, seen through the window
            S.add(f'<rect x="{30 + bx}" y="{ground + by}" width="{w}" height="{h}" fill="{LOAD}" stroke="{LOAD_DARK}" '
                  f'stroke-width="1.5" transform="rotate({tilt} 78 {ground})"/>')
        _pill(S, 16, top + 30, setting, colour=WRONG if wrong else INK)
    return str(S)


def chargement_arriere(params):
    """Load sticking out behind an estate car, to scale (a car ≈ 4.5 m). `depasse` in metres; `limites` draws the
    3 m maximum and the 1 m beyond which the end must be signalled; the end carries a red reflector (and a red
    lamp at night)."""
    limits = params.get("limites", False)
    H = 290 if limits else 220
    S = SVG(480, H)
    S.add(f'<rect x="0" y="0" width="480" height="{H}" fill="{PAPER}"/>')
    ground, rear, px_m = 200, 210, 53
    S.add(f'<rect x="0" y="{ground}" width="480" height="8" fill="#9aa0a2"/>')
    end = rear - params.get("depasse", 2) * px_m
    S.add(f'<rect x="{end}" y="{ground - 96}" width="{rear + 120 - end}" height="10" fill="{LOAD}" stroke="{LOAD_DARK}" stroke-width="2"/>')
    S.add(_car_side(rear, ground, "gris"))
    S.add(f'<rect x="{end - 4}" y="{ground - 104}" width="12" height="26" fill="{SIGN_RED}" stroke="{PAPER}" stroke-width="2"/>')
    if limits:
        for y, metres, label in ((ground + 30, 1, "1 m : signalisation"), (ground + 68, 3, "3 m : maximum")):
            x = rear - metres * px_m
            S.add(f'<path d="M{rear},{y} H{x} M{rear},{y - 7} v14 M{x},{y - 7} v14" stroke="{INK}" stroke-width="2.5" fill="none"/>')
            _text(S, rear + 12, y + 6, label, LABEL_SIZE, INK, "start")
    return str(S)


def chargement_coffre(params):
    """Estate car cut away at the boot: heavy load on the floor against the rear seat back, lighter on top, nothing
    above the top of the seat back (dashed)."""
    S = SVG(480, 230)
    S.add(f'<rect x="0" y="0" width="480" height="230" fill="{PAPER}"/>')
    ground, x0, s = 220, 50, 1.6
    S.add(f'<rect x="0" y="{ground}" width="480" height="10" fill="#9aa0a2"/>')
    S.add(f'<g transform="translate({x0},{ground}) scale({s}) translate({-x0},{-ground})">' + _car_side(x0, ground, "gris")
          # cut-away of the boot (car coordinates): opening, rear seat back, then the load
          + f'<path d="M{x0 + 6},{ground - 36} V{ground - 116} H{x0 + 94} V{ground - 36} Z" fill="{PAPER}" stroke="#111" stroke-width="1.2"/>'
          f'<rect x="{x0 + 80}" y="{ground - 104}" width="14" height="68" rx="5" fill="{SEAT_DARK}"/>'
          f'<rect x="{x0 + 44}" y="{ground - 70}" width="36" height="34" fill="{LOAD_DARK}"/>'
          f'<rect x="{x0 + 12}" y="{ground - 62}" width="30" height="26" fill="{LOAD}" stroke="{LOAD_DARK}" stroke-width="1.2"/>'
          f'<rect x="{x0 + 46}" y="{ground - 92}" width="32" height="22" fill="{LOAD}" stroke="{LOAD_DARK}" stroke-width="1.2"/>'
          f'<path d="M{x0 + 6},{ground - 104} H{x0 + 94}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4"/></g>')
    return str(S)


def _car_rear(cx, ground, colour="gris", reversing=False):
    """Car seen from behind, 200 wide; reversing lamps (white) lit or not."""
    c = CAR_COLOURS.get(colour, colour)
    x0 = cx - 100
    out = (f'<rect x="{x0 + 14}" y="{ground - 30}" width="34" height="30" rx="6" fill="#222"/>'
           f'<rect x="{x0 + 152}" y="{ground - 30}" width="34" height="30" rx="6" fill="#222"/>'
           f'<path d="M{x0 + 30},{ground - 150} H{x0 + 170} L{x0 + 188},{ground - 96} H{x0 + 12} Z" fill="{c}" stroke="#111" stroke-width="2"/>'
           f'<path d="M{x0 + 40},{ground - 142} H{x0 + 160} L{x0 + 174},{ground - 104} H{x0 + 26} Z" fill="{GLASS}" stroke="#111" stroke-width="1.5"/>'
           f'<rect x="{x0}" y="{ground - 100}" width="200" height="76" rx="14" fill="{c}" stroke="#111" stroke-width="2"/>'
           f'<rect x="{x0 + 70}" y="{ground - 56}" width="60" height="18" rx="3" fill="{PAPER}" stroke="#111" stroke-width="1.5"/>')
    for lx in (x0 + 6, x0 + 156):
        out += f'<rect x="{lx}" y="{ground - 92}" width="38" height="24" rx="5" fill="#d8362d" stroke="#111" stroke-width="1.5"/>'
        rx = lx + 29 if lx < cx else lx + 9
        out += f'<circle cx="{rx}" cy="{ground - 80}" r="7" fill="{PAPER if reversing else "#e9e9e9"}" stroke="#111" stroke-width="1"/>'
        if reversing:                                                   # lit: a white glow around the lamp
            out += (f'<circle cx="{rx}" cy="{ground - 80}" r="17" fill="{PAPER}" opacity="0.35"/>'
                    f'<circle cx="{rx}" cy="{ground - 80}" r="11" fill="{PAPER}" opacity="0.6"/>')
    return out


def feux_recul(params):
    """A parked car seen from behind, its white reversing lamps lit."""
    S = SVG(400, 240)
    S.add(f'<rect x="0" y="0" width="400" height="240" fill="{ASPHALT}"/>')
    S.add('<rect x="0" y="0" width="400" height="70" fill="#cfd3d4"/>')
    S.add(_car_rear(200, 214, "rouge", reversing=True))
    return str(S)


def gabarit_nuit(params):
    """Night, unlit road rising to a crest: above the crest, the marker lamps high on a lorry's cab appear while
    its headlamps are still hidden (only their glow shows)."""
    S = SVG(480, 280)
    S.add('<rect x="0" y="0" width="480" height="280" fill="#101a2a"/>')
    S.add('<ellipse cx="240" cy="150" rx="70" ry="14" fill="#fff6c2" opacity="0.18"/>')      # glow of hidden headlamps
    S.add('<path d="M206,160 V114 Q206,106 214,106 H266 Q274,106 274,114 V160 Z" fill="#232a33"/>')    # top of the cab
    for x in (212, 268):                                                                       # end-outline marker lamps
        S.add(f'<circle cx="{x}" cy="112" r="4" fill="#fff6c2"/><circle cx="{x}" cy="112" r="10" fill="#fff6c2" opacity="0.25"/>')
    S.add('<path d="M0,190 Q240,120 480,190 V280 H0 Z" fill="#1c2127"/>')
    S.add('<path d="M170,280 L228,156 H252 L310,280 Z" fill="#2b3036"/>')
    S.add('<path d="M240,164 L240,280" stroke="#8a8f94" stroke-width="3" stroke-dasharray="14 16"/>')
    S.add('<path d="M0,190 Q240,120 480,190" fill="none" stroke="#2b3036" stroke-width="2"/>')
    return str(S)


def jauge_huile(params):
    """Oil dipstick after the wipe-and-dip: the oil film ends between the min and max marks."""
    S = SVG(480, 150, view=(146, 20, 334, 110))                              # the graduated end, large
    S.add(f'<rect x="0" y="0" width="480" height="150" fill="{PAPER}"/>')
    S.add(f'<circle cx="178" cy="60" r="18" fill="none" stroke="{YELLOW}" stroke-width="9"/>')
    S.add('<rect x="194" y="54" width="266" height="12" rx="6" fill="#b8bec1"/>')
    S.add('<rect x="392" y="54" width="68" height="12" rx="6" fill="#b07a1e" opacity="0.85"/>')          # oil film
    for x, name in ((432, "min"), (370, "max")):
        S.add(f'<path d="M{x},46 V74" stroke="{INK}" stroke-width="3"/>')
        _text(S, x, 104, name, LABEL_SIZE, INK)
    return str(S)


def ecrous_croix(params):
    """Wheel from the side: the five nuts tightened in a star (1 to 5), each followed by the one across."""
    S = SVG(360, 340)
    S.add(f'<rect x="0" y="0" width="360" height="340" fill="{PAPER}"/>')
    cx, cy = 180, 170
    S.add(f'<circle cx="{cx}" cy="{cy}" r="150" fill="#222"/><circle cx="{cx}" cy="{cy}" r="100" fill="#b8bec1"/>'
          f'<circle cx="{cx}" cy="{cy}" r="24" fill="#8d9396"/>')
    pts = [(cx + 60 * math.sin(math.radians(72 * k)), cy - 60 * math.cos(math.radians(72 * k))) for k in range(5)]
    order = [0, 2, 4, 1, 3]
    S.add('<path d="M' + " L".join(f"{pts[k][0]:.1f},{pts[k][1]:.1f}" for k in order + [0]) + f'" fill="none" '
          f'stroke="{INK}" stroke-width="2" stroke-dasharray="6 5"/>')
    for n, k in enumerate(order, 1):
        x, y = pts[k]
        S.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="#555" stroke="#111" stroke-width="1.5"/>')
        lx, ly = cx + 86 * math.sin(math.radians(72 * k)), cy - 86 * math.cos(math.radians(72 * k))
        _text(S, lx, ly + 7, n, NUMBER_SIZE, INK)
    return str(S)


def pneu_hernie(params):
    """Tyre from the side with a bulge on the sidewall."""
    S = SVG(360, 320)
    S.add(f'<rect x="0" y="0" width="360" height="320" fill="{PAPER}"/>')
    cx, cy = 180, 160
    S.add(f'<circle cx="{cx}" cy="{cy}" r="140" fill="#2a2a2a"/><circle cx="{cx}" cy="{cy}" r="136" fill="none" '
          f'stroke="#444" stroke-width="3" stroke-dasharray="4 6"/><circle cx="{cx}" cy="{cy}" r="82" fill="#b8bec1"/>'
          f'<circle cx="{cx}" cy="{cy}" r="22" fill="#8d9396"/>')
    S.add('<defs><radialGradient id="bosse" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#9a9a9a"/>'
          '<stop offset="0.55" stop-color="#555"/><stop offset="1" stop-color="#2a2a2a"/></radialGradient></defs>')
    S.add('<ellipse cx="264" cy="90" rx="34" ry="24" transform="rotate(40 264 90)" fill="url(#bosse)"/>'
          '<path d="M236,110 Q258,124 290,104" fill="none" stroke="#111" stroke-width="3" opacity="0.6"/>')
    return str(S)


def pneu_gonflage(params):
    """Tyre cross-sections on the road: correct pressure (whole tread on the road), over-inflated (crown bulges,
    only the centre touches), under-inflated (the crown sags, the shoulders carry the load). Contact in yellow."""
    S = SVG(480, 230)
    S.add(f'<rect x="0" y="0" width="480" height="230" fill="{PAPER}"/>')
    for i, (name, crown, contact) in enumerate((("correct", 0, (-40, 40)), ("surgonflé", 14, (-16, 16)),
                                                ("sous-gonflé", -8, None))):
        cx, ground = 80 + 160 * i, 170
        # section: two sidewalls and the tread; crown > 0 bulges down in the middle, < 0 lifts it
        side = 58 + (6 if crown < 0 else -4 if crown > 0 else 0)
        S.add(f'<path d="M{cx - side},{ground - 110} Q{cx - side - 8},{ground - 50} {cx - 46},{ground - 6} '
              f'Q{cx},{ground - 6 + crown} {cx + 46},{ground - 6} Q{cx + side + 8},{ground - 50} {cx + side},{ground - 110}" '
              f'fill="none" stroke="#2a2a2a" stroke-width="14" stroke-linejoin="round"/>')
        S.add(f'<rect x="{cx - 70}" y="{ground}" width="140" height="6" fill="#9aa0a2"/>')
        spans = [contact] if contact else [(-46, -26), (26, 46)]
        for a, b in spans:
            S.add(f'<rect x="{cx + a}" y="{ground - 3}" width="{b - a}" height="6" fill="{YELLOW}"/>')
        _text(S, cx, ground + 44, name, LABEL_SIZE, INK)
    return str(S)


def pente_roues(params):
    """Parked against the kerb (on the right) on a steep slope, from above: going down, front wheels turned towards
    the kerb; going up, towards the road — if the car rolls, a tyre stops against the kerb."""
    S = SVG(480, 330)
    S.add(f'<rect x="0" y="0" width="480" height="330" fill="#cfd3d4"/>')
    for i, (name, turn) in enumerate((("en descente", 32), ("en montée", -32))):
        x0 = 240 * i
        S.add(f'<rect x="{x0}" y="0" width="170" height="290" fill="{ASPHALT}"/>')
        S.add(f'<rect x="{x0 + 168}" y="0" width="6" height="290" fill="#9aa0a2"/>')              # kerb
        cx, cy = x0 + 126, 150
        # the car, larger than in the road scenes, with its front wheels drawn over the body so the steering shows
        S.add(f'<g transform="translate({cx},{cy}) scale(1.35)">{vehicle_sprite("car", "bleu")}'
              + "".join(f'<rect x="-6" y="-16" width="12" height="32" rx="3" fill="#111" stroke="{PAPER}" stroke-width="1.5" '
                        f'transform="translate({sx * 22},-26) rotate({turn})"/>' for sx in (-1, 1)) + '</g>')
        # slope: the arrow points downhill
        down = -1 if turn > 0 else 1
        S.add(f'<path d="M{x0 + 40},{150 - down * 60} V{150 + down * 60} m-10,{-down * 14} l10,{down * 14} l10,{-down * 14}" '
              f'fill="none" stroke="{MARK}" stroke-width="4"/>')
        _text(S, x0 + 56, 150 + down * 50, "bas", LABEL_SIZE, MARK, "start")
        _text(S, x0 + 85, 318, name, LABEL_SIZE, INK)
    return str(S)


# ------------------------------------------------ drinks, lorry, placements, bends, protection, reach ---
GLASS_EDGE, GLASS_FILL = "#8aa0aa", "#eef5f8"


def verres_standard(params):
    """Three standard drinks as served in a bar, each ≈ 10 g of pure alcohol."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{PAPER}"/>')
    base = 196
    # beer: tall tumbler, 25 cl
    S.add(f'<path d="M58,{base - 124} H122 L114,{base} H66 Z" fill="{GLASS_FILL}" stroke="{GLASS_EDGE}" stroke-width="3"/>'
          f'<path d="M60,{base - 104} H120 L114,{base - 2} H66 Z" fill="#e0a526"/>'
          f'<path d="M59,{base - 116} H121 L120,{base - 104} H60 Z" fill="{PAPER}" stroke="#e6d7b0" stroke-width="1"/>')
    # wine: stemmed glass, 10 cl
    S.add(f'<path d="M206,{base - 130} Q204,{base - 70} 240,{base - 62} Q276,{base - 70} 274,{base - 130} Z" fill="{GLASS_FILL}" '
          f'stroke="{GLASS_EDGE}" stroke-width="3"/>'
          f'<path d="M207,{base - 100} Q210,{base - 68} 240,{base - 64} Q270,{base - 68} 273,{base - 100} Z" fill="#8e1b3a"/>'
          f'<path d="M240,{base - 62} V{base - 6}" stroke="{GLASS_EDGE}" stroke-width="4"/>'
          f'<path d="M212,{base} Q240,{base - 10} 268,{base} Z" fill="{GLASS_FILL}" stroke="{GLASS_EDGE}" stroke-width="3"/>')
    # whisky: short tumbler, 3 cl
    S.add(f'<path d="M354,{base - 64} H426 L420,{base} H360 Z" fill="{GLASS_FILL}" stroke="{GLASS_EDGE}" stroke-width="3"/>'
          f'<path d="M359,{base - 16} H421 L420,{base - 2} H360 Z" fill="#b8741a"/>')
    for x, dose in ((90, "25 cl à 5°"), (240, "10 cl à 12°"), (390, "3 cl à 40°")):
        _text(S, x, base + 32, dose, LABEL_SIZE, INK, "middle", 400)
    S.add(f'<path d="M40,{base + 52} v8 H440 v-8" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    _text(S, 240, base + 88, "≈ 10 g d’alcool pur chacun", LABEL_SIZE, INK)
    return str(S)


def pl_angles_morts(params):
    """Rigid lorry from above, at the deck's lorry proportions: its blind spots (hatched) in front, along both
    sides — widest on the right — and behind; a cyclist waiting beside the cab, inside the right-hand one."""
    S = SVG(480, 560)
    S.add(f'<rect x="0" y="0" width="480" height="560" fill="{ASPHALT}"/>')
    _hidden_pattern(S)
    zones = ("M204,44 H276 V118 H204 Z",                                     # in front of the cab
             "M280,122 L470,96 L470,430 L280,404 Z",                         # right side, the largest
             "M200,190 L100,206 L100,366 L200,384 Z",                        # left side
             "M204,442 H276 V552 H204 Z")                                    # behind
    for d in zones:
        S.add(f'<path d="{d}" fill="url(#hidden)" stroke="{HIDDEN}" stroke-width="2"/>')
    S.add(f'<g transform="translate(240,280) scale(1.35)">{vehicle_sprite("lorry", "blanc")}</g>')
    S.add(f'<g transform="translate(318,170) scale(1.3)">{vehicle_sprite("bike", "rouge")}</g>')
    _pill(S, 16, 30, "angles morts")
    return str(S)


def tourner_gauche_placement(params):
    """Where I wait to turn left, three roads: two-way with two lanes (next to the centre line, without crossing it),
    two-way with three lanes (the middle lane), one-way (along the left edge)."""
    S = SVG(480, 330)
    S.add(f'<rect x="0" y="0" width="480" height="330" fill="{GRASS}"/>')
    panels = ((0, 128, 2, [(64, "discontinue")], 64 + 22, "2 voies"),
              (150, 180, 3, [(60, "discontinue"), (120, "discontinue")], 90, "3 voies"),
              (352, 128, 2, [], 26, "sens unique"))
    for x0, w, lanes, lines, me_x, name in panels:
        S.add(f'<rect x="{x0}" y="0" width="{w}" height="290" fill="{ASPHALT}"/>')
        for at, style in lines:
            S.add(f'<path d="M{x0 + at},0 V290" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 26"/>')
        if not lines:                                                   # one-way: arrows on the road
            for y in (40, 110):
                S.add(f'<path d="M{x0 + 88},{y + 40} V{y + 12} h-9 l13,-18 l13,18 h-9 V{y + 40} Z" fill="{MARK}" '
                      f'transform="translate(-4,0)"/>')
        S.add(f'<g transform="translate({x0 + me_x},200) scale(0.8)">{ME}{intention_arrow("left", front=42)}</g>')
        S.add(f'<rect x="{x0}" y="290" width="{w}" height="40" fill="{PAPER}"/>')
        _text(S, x0 + w / 2, 318, name, LABEL_SIZE, INK)
    return str(S)


def virage_gauche(params):
    """Blind left-hand bend on a two-way road: the inside of the bend (trees) hides the oncoming car; my path stays
    in my lane, near the right edge. answer_on_back: the path and the oncoming car are the answer, drawn only on the
    back of a « verso » image."""
    S = SVG(480, 380)
    S.add(f'<rect x="0" y="0" width="480" height="380" fill="{GRASS}"/>')
    road = "M330,380 V230 A150,150 0 0 0 180,80 H0"
    S.add(f'<path d="{road}" fill="none" stroke="{MARK}" stroke-width="166"/>'
          f'<path d="{road}" fill="none" stroke="{ASPHALT}" stroke-width="160"/>'
          f'<path d="{road}" fill="none" stroke="{MARK}" stroke-width="4" stroke-dasharray="22 26"/>')
    for cx, cy, r in ((186, 236, 44), (150, 270, 34), (214, 280, 30), (120, 230, 28), (160, 200, 26), (100, 300, 30),
                      (70, 250, 26), (200, 330, 26)):
        S.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#5d7f4a" stroke="#48673a" stroke-width="2"/>')
    if params.get("verso") or not params.get("answer_on_back"):  # the hidden oncoming car is part of the answer too
        S.add(f'<path d="M372,268 V230 A192,192 0 0 0 180,38 H60" fill="none" stroke="{YELLOW}" stroke-width="3" stroke-dasharray="8 6"/>')
        S.add(f'<g transform="translate(70,120) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<g transform="translate(372,318)">{ME}</g>')
    return str(S)


def protection_accident(params):
    """First on the scene of an accident, on a two-way road: I stop after it, on the verge, hazard lights on; the
    warning triangle goes about 30 m before it (not to scale)."""
    S = SVG(480, 290)
    S.add(f'<rect x="0" y="0" width="480" height="290" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="150" fill="{ASPHALT}"/>')
    _dashes_h(S, 115, 3, 10, w=4)
    S.add(f'<g transform="translate(250,152) rotate(118)">{vehicle_sprite("car", "rouge")}</g>')
    S.add(f'<g transform="translate(300,160) rotate(70)">{vehicle_sprite("car", "gris")}</g>')
    me = (420, 214)
    S.add(f'<g transform="translate({me[0]},{me[1]}) rotate(90)">{_body({"me": True}, 90)}</g>')
    for dx, dy in ((-40, -18), (-40, 18), (40, -18), (40, 18)):          # hazard lights flashing
        _flash_rays(S, me[0] + dx, me[1] + dy, 3, AMBER)
    S.add('<path d="M66,176 l14,-26 l14,26 z" fill="#e53935" stroke="#fff" stroke-width="2"/>')
    S.add(f'<path d="M80,236 H142 M178,236 H226 M80,228 v16 M226,228 v16 M136,246 l12,-20 M166,246 l12,-20" '
          f'stroke="{INK}" stroke-width="3" fill="none"/>')
    _text(S, 160, 272, "≈ 30 m", LABEL_SIZE, INK)
    return str(S)


def pieton_carrefour(params):
    """A pedestrian crossing a junction with no zebra nearby: each road crossed at right angles, in line with the
    pavements; never on the diagonal."""
    S = SVG(400, 400)
    S.add(f'<rect x="0" y="0" width="400" height="400" fill="#cfd3d4"/>')
    S.add(f'<rect x="130" y="0" width="140" height="400" fill="{ASPHALT}"/><rect x="0" y="130" width="400" height="140" fill="{ASPHALT}"/>')
    for d in ("M200,0 V120 M200,280 V400", "M0,200 H120 M280,200 H400"):
        S.add(f'<path d="{d}" stroke="{MARK}" stroke-width="4" stroke-dasharray="20 20"/>')
    S.add(f'<path d="M140,260 L260,140" stroke="{WRONG}" stroke-width="3" stroke-dasharray="8 6"/>'
          f'<path d="M188,188 l24,24 M212,188 l-24,24" stroke="{WRONG}" stroke-width="4"/>')
    S.add(f'<path d="M110,300 V110 H300" fill="none" stroke="{YELLOW}" stroke-width="4" stroke-dasharray="10 7"/>'
          f'<path d="M290,100 l12,10 l-12,10" fill="none" stroke="{YELLOW}" stroke-width="4"/>')
    S.add(pedestrian(110, 322))
    return str(S)


def portee_prescription(params):
    """How far a speed limit reaches: an isolated sign stops at the next junction; a zone lasts until its end sign,
    across junctions. Traffic goes right, signs stand on its right-hand side; the part where 30 applies is
    highlighted."""
    S = SVG(480, 400)
    S.add(f'<rect x="0" y="0" width="480" height="400" fill="{GRASS}"/>')
    rows = ((0, "panneau isolé", "France road sign B14 (30).svg", None, 180),
            (200, "zone 30", "France road sign B30 (30).svg", "France road sign B51 (30).svg", 450))
    for top, name, first, last, end in rows:
        road_y = top + 58
        for x in (180, 330):
            S.add(f'<rect x="{x - 22}" y="{top}" width="44" height="200" fill="{ASPHALT}"/>')
        S.add(f'<rect x="0" y="{road_y}" width="480" height="44" fill="{ASPHALT}"/>')
        S.add(f'<path d="M6,{road_y + 22} h22 m-8,-7 l8,7 l-8,7" fill="none" stroke="{MARK}" stroke-width="3"/>')
        S.add(f'<rect x="40" y="{road_y + 14}" width="{end - 40}" height="16" rx="8" fill="{YELLOW}"/>')
        for x, file in ((40, first), (end, last)):
            if file:
                uri, h = _sign_png({"kind": "sign", "file": file}, 48)
                S.add(f'<image href="{uri}" x="{x - 24}" y="{road_y + 54}" width="48" height="{h}"/>')
        _pill(S, 255, top + 30, name, anchor="middle")
    return str(S)


def deux_traits(params):
    """Motorway right lane and hard shoulder, traffic to the right: the long dashes of the edge line (39 m, gaps of
    13 m, to scale for the line only) and two full dashes between the car ahead and MOI."""
    S = SVG(480, 240)
    S.add(f'<rect x="0" y="0" width="480" height="240" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="140" fill="{ASPHALT}"/>')
    _dashes_h(S, 44, 3, 10, w=4)
    px_m, front_me = 3.6, 76                                              # 39 m dash ≈ 140 px
    rear_other = front_me + (39 + 13 + 39) * px_m                         # two full dashes and the gap between
    x = front_me - (39 + 13) * px_m
    while x < 480:
        x0, x1 = max(x, 0), min(x + 39 * px_m, 480)
        if x1 > x0:
            S.add(f'<rect x="{x0:.1f}" y="124" width="{x1 - x0:.1f}" height="6" fill="{MARK}"/>')
        x += (39 + 13) * px_m
    S.add(f'<g transform="translate({rear_other + 30:.1f},88) rotate(90) scale(0.7)">{vehicle_sprite("car", "gris")}</g>')
    S.add(f'<g transform="translate({front_me - 30},88) rotate(90) scale(0.7)">{_body({"me": True}, 90)}</g>')
    _pill(S, 470, 162, "bande d’arrêt d’urgence", size=15, anchor="end")
    S.add(f'<path d="M{front_me},196 v10 H{rear_other:.1f} v-10" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    _text(S, (front_me + rear_other) / 2, 230, "2 traits ≈ 90 m", LABEL_SIZE, INK)
    return str(S)


REGISTRY.update({
    "deux_traits": deux_traits,
    "verres_standard": verres_standard, "pl_angles_morts": pl_angles_morts,
    "tourner_gauche_placement": tourner_gauche_placement, "virage_gauche": virage_gauche,
    "protection_accident": protection_accident, "pieton_carrefour": pieton_carrefour, "portee_prescription": portee_prescription,
    "feux_chargement": feux_chargement, "chargement_arriere": chargement_arriere, "chargement_coffre": chargement_coffre,
    "feux_recul": feux_recul, "gabarit_nuit": gabarit_nuit, "jauge_huile": jauge_huile, "ecrous_croix": ecrous_croix,
    "pneu_hernie": pneu_hernie, "pneu_gonflage": pneu_gonflage, "pente_roues": pente_roues,
    "poste_conduite": poste_conduite, "siege_dos_route": siege_dos_route, "volant_mains": volant_mains, "retroviseur": retroviseur, "champ_visuel": champ_visuel,
    "distance_arret": distance_arret, "ligne_continue_gestes": ligne_continue_gestes,
    "rue_stationnement": rue_stationnement,
    "bretelle": bretelle, "pn_face": pn_face, "pn_plan": pn_plan,
    "autoroute_attente": autoroute_attente,
    "medicaments_niveaux": medicaments_niveaux, "etiquettes_carburant": etiquettes_carburant, "pneu_flanc": pneu_flanc,
    "pneu_usure": pneu_usure, "angles_morts": angles_morts, "ceinture": ceinture,
    "feu_modal": feu_modal, "feu_sur_panneau": feu_sur_panneau, "pmv": pmv, "plaque_orange": plaque_orange, "car_enfants": car_enfants, "disque_stationnement": disque_stationnement, "types_routes": types_routes,
    "support_panneaux": support_panneaux, "planche_signaux": planche_signaux,
    "vocab_route": vocab_route, "formes_panneaux": formes_panneaux,
    "balise_piquet": balise_piquet, "voyant_direction": voyant_direction,
    "voie_insertion": voie_insertion, "bande_cyclable": bande_cyclable, "damier": damier, "ralentisseur": ralentisseur,
    "direction_voies": direction_voies,
    "marquage_temporaire": marquage_temporaire, "zone_bleue": zone_bleue, "losange_sol": losange_sol, "cvcb": cvcb,
    "livraison": livraison, "direction_panel": direction_panel, "lieu_dit": lieu_dit, "feu_bicolore": feu_bicolore,
    "giratoire_sortie": giratoire_sortie, "rappel_limites": rappel_limites, "entrecroisement": entrecroisement, "route_c107": route_c107,
    "camion_virage": camion_virage, "camion_roues": camion_roues, "chantier_rabattement": chantier_rabattement, "corridor_securite": corridor_securite,
    "cycliste_tourne_droite": cycliste_tourne_droite, "cone": cone, "cedez_le_passage": cedez_le_passage, "triangle_seul": triangle_seul, "barriere_k2": barriere_k2,
})
