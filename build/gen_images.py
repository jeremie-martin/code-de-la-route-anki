"""Generated illustrations: road markings, traffic lights, officer signals, pictograms.

Each generator returns an SVG string. `render(name, params)` dispatches by name.
Visual identity matches build/diagrams.py (same asphalt, grass, marking colours).
"""
from __future__ import annotations

import math

from build.diagrams import ASPHALT, GRASS, MARK, FONT, SVG, draw_road, draw_intersection, draw_roundabout, vehicle_sprite, esc

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
        S.add(f'<text x="{S.w - 10}" y="230" font-family="{FONT}" font-size="14" text-anchor="end" fill="#fff">bande d\'arrêt d\'urgence</text>')
        _me_car(S, 70, 160)
        S.add(f'<g transform="translate(330,160) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
        return str(S)
    for y in (66, 234):
        if style == "continue":
            S.add(f'<rect x="0" y="{y - 2}" width="{S.w}" height="4" fill="{MARK}"/>')
        else:
            _dashes_h(S, y, params.get("dash", 3), params.get("gap", 3.5), w=4)
    _dashes_h(S, 150, 3, 10)
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
        S.add(f'<text x="{S.w / 2}" y="150" font-family="{FONT}" font-size="26" font-weight="700" text-anchor="middle" fill="{MARK}">BUS</text>')
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
            # arrow in my lane (bottom half), pointing forward and slanting right (toward the kerb)
            S.add(f'<path d="M{x},197 l40,0 l0,-10 l20,14 l-20,14 l0,-10 l-40,0 z" fill="{MARK}" transform="rotate(20 {x + 30} 197)"/>')
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
        # arrows
        def arrow(cx, kind_):
            if kind_ == "straight":
                return f'<path d="M{cx},210 l0,-70 l-14,0 l14,-30 l14,30 l-14,0 l0,70 z" fill="{MARK}" transform="translate(0,0)"/>'
            if kind_ == "left":
                return (f'<path d="M{cx},210 l0,-60 q0,-16 -16,-16 l-10,0 l0,-12 l-26,20 l26,20 l0,-12 l10,0 q0,0 0,0 l0,60 z" fill="{MARK}"/>')
            if kind_ == "right":
                return (f'<path d="M{cx},210 l0,-60 q0,-16 16,-16 l10,0 l0,-12 l26,20 l-26,20 l0,-12 l-10,0 l0,60 z" fill="{MARK}"/>')
        S.add(arrow(140, "left")); S.add(arrow(240, "straight")); S.add(arrow(340, "right"))
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
        S.add(f'<text x="300" y="150" font-family="{FONT}" font-size="30" font-weight="800" text-anchor="middle" fill="{MARK}">STOP</text>')
    elif kind == "cedez":
        for x in range(244, 358, 20):
            S.add(f'<rect x="{x}" y="88" width="12" height="10" fill="{MARK}"/>')
        # AB3a on the verge, next to the line
        S.add('<rect x="404" y="98" width="6" height="60" fill="#666"/>')
        S.add('<path d="M378,96 L436,96 L407,146 Z" fill="#d8362d" stroke="#333" stroke-width="2" stroke-linejoin="round"/>')
        S.add('<path d="M390,103 L424,103 L407,132 Z" fill="#ffffff"/>')
    elif kind == "effet_feux":
        for x in range(244, 358, 12):
            S.add(f'<rect x="{x}" y="90" width="6" height="4" fill="{MARK}"/>')
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
        if kind == "pieton":
            for x in range(200, 300, 24):
                S.add(f'<rect x="{x}" y="66" width="14" height="168" fill="{MARK}"/>')
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
        S.add(f'<rect x="126" y="80" width="228" height="50" fill="#3aa657" opacity="0.85"/>')
        S.add(f'<rect x="126" y="78" width="228" height="6" fill="{MARK}"/><rect x="126" y="130" width="228" height="6" fill="{MARK}"/>')
        S.add(f'<g transform="translate(240,105)"><circle cx="-10" cy="6" r="8" fill="none" stroke="{MARK}" stroke-width="3"/><circle cx="12" cy="6" r="8" fill="none" stroke="{MARK}" stroke-width="3"/><path d="M-10,6 l8,-14 l12,0 l2,14 M-2,-8 l6,14" fill="none" stroke="{MARK}" stroke-width="3"/></g>')
        S.add(f'<line x1="240" y1="140" x2="240" y2="300" stroke="{MARK}" stroke-width="4" stroke-dasharray="14 10"/>')
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
    S.add(f'<rect x="0" y="150" width="480" height="5" fill="{MARK}"/>')
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
        if arrow and on:
            _lamp(S, 120, cy, 36, "#3a3a3a", on=False)
            S.add(f'<circle cx="120" cy="{cy}" r="36" fill="#111"/>')
            S.add(_arrow_glyph(120, cy, c, arrow))
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
    if bar == "vertical":
        S.add('<text x="120" y="290" font-family="%s" font-size="14" text-anchor="middle" fill="#333">R17 / R18</text>' % FONT)
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
        if on:
            S.add(f'<g transform="translate(100,{cy})" fill="none" stroke="{c}" stroke-width="3"><circle cx="-10" cy="6" r="8"/><circle cx="10" cy="6" r="8"/><path d="M-10,6 l7,-13 l11,0 l2,13 M-3,-7 l5,13"/></g>')
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
        elif st == "fleche":
            S.add(f'<path d="M{cx},58 l16,18 l-9,0 l0,20 l-14,0 l0,-20 l-9,0 z" fill="{GREEN}"/>')
        elif st == "rabattement_droite":
            S.add(f'<path d="M{cx - 14},60 l24,24 l-8,0 l0,8 l8,0 l0,-8" fill="none" stroke="{AMBER}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
        elif st == "rabattement_gauche":
            S.add(f'<path d="M{cx + 14},60 l-24,24 l8,0 l0,8 l-8,0 l0,-8" fill="none" stroke="{AMBER}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
    S.add(f'<g transform="translate(240,230)">{vehicle_sprite("car", "bleu")}</g>')
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
    S = SVG(300, 360)
    S.add('<rect x="0" y="0" width="300" height="360" fill="#ffffff"/>')
    pose = params.get("pose", "bras_leve")
    cx = 150
    body, hand = "#1f3a93", "#f5d0b0"
    S.add(f'<rect x="{cx - 28}" y="200" width="22" height="110" rx="8" fill="{body}"/><rect x="{cx + 6}" y="200" width="22" height="110" rx="8" fill="{body}"/>')
    S.add(f'<rect x="{cx - 40}" y="110" width="80" height="100" rx="14" fill="{body}"/>')
    S.add(f'<rect x="{cx - 40}" y="150" width="80" height="14" fill="#fff" opacity="0.85"/>')
    S.add(f'<circle cx="{cx}" cy="80" r="26" fill="{hand}"/>')
    S.add(f'<path d="M{cx - 30},70 q30,-30 60,0 l0,-8 q-30,-26 -60,0 z" fill="#0d1f5c"/><rect x="{cx - 34}" y="66" width="68" height="8" rx="3" fill="#0d1f5c"/>')

    def arm(x0, y0, x1, y1):
        S.add(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{body}" stroke-width="18" stroke-linecap="round"/>')
        S.add(f'<circle cx="{x1}" cy="{y1}" r="10" fill="{hand}"/>')

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
        # motion marks: the arm moves up and down
        S.add(f'<path d="M{cx - 128},120 l0,-14 M{cx - 136},128 l-14,0" fill="none" stroke="#333" stroke-width="3"/>')
        S.add(f'<path d="M{cx - 150},200 l0,14 M{cx - 158},192 l-14,0" fill="none" stroke="#333" stroke-width="3"/>')
        S.add(f'<path d="M{cx - 140},140 q-16,30 0,60" fill="none" stroke="#333" stroke-width="3" stroke-dasharray="5 5"/>')
    elif pose == "avancer":
        arm(*ls, cx - 130, 128)
        arm(*rs, cx + 52, 200)
        S.add(f'<path d="M{cx - 150},100 l-22,28 l22,28" fill="none" stroke="#333" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    if params.get("caption_text"):
        S.add(f'<text x="150" y="345" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">{esc(str(params["caption_text"]))}</text>')
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


def roue_position(params):
    """Wheel positions when parking on a slope, seen from above with the kerb at the right."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="0" width="360" height="300" fill="{ASPHALT}"/>')
    S.add('<rect x="360" y="0" width="120" height="300" fill="#bdbdbd"/>')
    S.add('<line x1="360" y1="0" x2="360" y2="300" stroke="#8a8a8a" stroke-width="3"/>')
    slope = params.get("pente", "descente")  # descente = the car faces downhill (down the image)
    S.add(f'<text x="20" y="30" font-family="{FONT}" font-size="16" fill="#fff">{"⬇ descente" if slope == "descente" else "⬆ montée"}</text>')
    # car heading up (north) parked along kerb
    S.add(f'<g transform="translate(300,150)">{vehicle_sprite("car", "bleu")}</g>')
    ang = params.get("angle", 25)
    for (x, y) in [(300 - 22, 150 - 28), (300 + 22, 150 - 28)]:
        S.add(f'<rect x="{x - 5}" y="{y - 12}" width="10" height="24" rx="3" fill="#111" transform="rotate({ang} {x} {y})"/>')
    for (x, y) in [(300 - 22, 150 + 28), (300 + 22, 150 + 28)]:
        S.add(f'<rect x="{x - 5}" y="{y - 12}" width="10" height="24" rx="3" fill="#111"/>')
    S.add(f'<text x="420" y="160" font-family="{FONT}" font-size="15" text-anchor="middle" fill="#333">trottoir</text>')
    return str(S)


def triangle_distance(params):
    """Broken-down car with warning triangle placed 30 m behind."""
    S = SVG(480, 200)
    S.add(f'<rect x="0" y="0" width="480" height="200" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="120" fill="{ASPHALT}"/>')
    _dashes_h(S, 100, 3, 10, w=4)
    S.add(f'<g transform="translate(400,130) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
    S.add('<path d="M120,150 l14,-26 l14,26 z" fill="#e53935" stroke="#fff" stroke-width="2"/>')
    S.add(f'<line x1="140" y1="175" x2="360" y2="175" stroke="#fff" stroke-width="2"/><text x="250" y="192" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff">{esc(str(params.get("label", "≈ 30 m")))}</text>')
    return str(S)


def retroviseur(params):
    """Correct mirror adjustment: interior mirror frames the whole rear window; side mirrors show a sliver of car + horizon."""
    S = SVG(480, 240)
    S.add('<rect x="0" y="0" width="480" height="240" fill="#ffffff"/>')
    kind = params.get("kind", "exterieur")
    if kind == "exterieur":
        S.add('<rect x="90" y="30" width="300" height="180" rx="16" fill="#9ec9f0" stroke="#222" stroke-width="4"/>')
        S.add('<rect x="90" y="120" width="300" height="90" fill="#7fa86a"/>')
        S.add('<rect x="90" y="30" width="300" height="90" fill="#bfe0ff"/>')
        S.add('<rect x="90" y="118" width="300" height="4" fill="#333"/>')
        S.add('<rect x="340" y="40" width="50" height="170" rx="6" fill="#2d6fd8" opacity="0.9"/>')
        S.add(f'<text x="365" y="130" font-family="{FONT}" font-size="12" text-anchor="middle" fill="#fff" transform="rotate(90 365 130)">carrosserie</text>')
        S.add(f'<text x="200" y="90" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">ciel</text><text x="200" y="170" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#fff">route</text>')
    else:
        S.add('<rect x="60" y="60" width="360" height="120" rx="12" fill="#bfe0ff" stroke="#222" stroke-width="4"/>')
        S.add('<rect x="80" y="76" width="320" height="88" rx="10" fill="none" stroke="#333" stroke-width="3" stroke-dasharray="8 6"/>')
        S.add(f'<text x="240" y="126" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">toute la lunette arrière</text>')
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
    "roue_position": roue_position, "triangle_distance": triangle_distance, "retroviseur": retroviseur,
    "road": road_scene, "intersection": intersection_scene, "roundabout": roundabout_scene,
}


def render(name: str, params: dict | None = None) -> str:
    if name not in REGISTRY:
        raise KeyError(f"generator inconnu: {name}")
    return REGISTRY[name](params or {})


# ------------------------------------------------------- extra markings ---
def voie_insertion(params):
    """Motorway with an acceleration lane on the right delimited by a T2-type short dashed line."""
    S = SVG(480, 300)
    S.add(f'<rect x="0" y="0" width="480" height="300" fill="{GRASS}"/>')
    S.add(f'<rect x="0" y="40" width="480" height="150" fill="{ASPHALT}"/>')
    S.add(f'<rect x="0" y="42" width="480" height="4" fill="{MARK}"/>')
    _dashes_h(S, 115, 3, 10)
    # insertion lane below, tapering
    S.add(f'<path d="M0,190 L480,190 L480,260 L200,260 Z" fill="{ASPHALT}"/>')
    _dashes_h(S, 190, 3, 3.5, w=5, x0=200)
    S.add(f'<path d="M0,190 L200,260 L200,262 L0,192 Z" fill="{MARK}"/>')
    S.add(f'<g transform="translate(330,226) rotate(90)">{vehicle_sprite("car", "bleu")}</g>')
    S.add(f'<text x="330" y="288" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">voie d\'insertion</text>')
    S.add(f'<g transform="translate(120,150) rotate(90)">{vehicle_sprite("car", "gris")}</g>')
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
    x0, y0, size = 150, 80, 30
    cols, rows = 6, 6
    for i in range(cols):
        for j in range(rows):
            if (i + j) % 2 == 0:
                S.add(f'<rect x="{x0 + i * size}" y="{y0 + j * size}" width="{size}" height="{size}" fill="{MARK}"/>')
            elif colour == "rouge":
                S.add(f'<rect x="{x0 + i * size}" y="{y0 + j * size}" width="{size}" height="{size}" fill="#d8362d"/>')
    if colour == "blanc":
        S.add(f'<text x="240" y="285" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">damier blanc : traversée d\'un couloir bus</text>')
    else:
        S.add(f'<rect x="330" y="40" width="150" height="220" fill="#b9a27a"/>')
        S.add(f'<text x="240" y="285" font-family="{FONT}" font-size="14" text-anchor="middle" fill="#333">damier rouge et blanc : voie de détresse</text>')
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
    S.add(f'<rect x="215" y="46" width="70" height="208" fill="#5a5a5a"/>')
    if kind == "dos_d_ane":
        for y in (60, 100, 140, 180, 220):
            S.add(f'<path d="M215,{y} l-26,12 l26,12 z" fill="{MARK}"/>')
            S.add(f'<path d="M285,{y} l26,12 l-26,12 z" fill="{MARK}"/>')
    else:
        for i in range(8):
            S.add(f'<rect x="{222 + i * 8}" y="60" width="4" height="180" fill="{MARK}"/>')
        for x in range(215, 285, 16):
            S.add(f'<rect x="{x}" y="46" width="8" height="14" fill="{MARK}"/><rect x="{x}" y="240" width="8" height="14" fill="{MARK}"/>')
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
    S.add(f'<rect x="120" y="130" width="240" height="4" fill="{YELLOW}"/>')
    S.add(f'<path d="M140,140 L340,196 M340,140 L140,196" stroke="{YELLOW}" stroke-width="4"/>')
    S.add(f'<text x="240" y="176" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle" fill="{YELLOW}">LIVRAISON</text>')
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


def feu_bicolore(params):
    """R23 two-colour light (red / green), one vehicle per green (contrôle individuel)."""
    S = SVG(240, 300)
    S.add('<rect x="0" y="0" width="240" height="300" fill="#ffffff"/>')
    S.add('<rect x="70" y="30" width="100" height="220" rx="16" fill="#222" stroke="#000" stroke-width="2"/>')
    state = params.get("state", "rouge")
    _lamp(S, 120, 80, 36, RED, on=(state == "rouge"))
    _lamp(S, 120, 190, 36, GREEN, on=(state == "vert"))
    return str(S)


def cone(params):
    S = SVG(240, 300)
    S.add('<rect x="0" y="0" width="240" height="300" fill="#ffffff"/>')
    S.add('<rect x="50" y="240" width="140" height="18" rx="4" fill="#e8501e" stroke="#333" stroke-width="2"/>')
    S.add('<path d="M100,40 L140,40 L180,240 L60,240 Z" fill="#e8501e" stroke="#333" stroke-width="2"/>')
    S.add('<path d="M92,80 L148,80 L156,120 L84,120 Z" fill="#ffffff"/>')
    S.add('<path d="M78,150 L162,150 L170,190 L70,190 Z" fill="#ffffff"/>')
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
    S.add('<path d="M96,40 L144,40 L150,262 L90,262 Z" fill="#ffffff" stroke="#8a8a8a" stroke-width="2"/>')
    if kind == "j1bis":
        S.add('<path d="M96,40 L144,40 L146,86 L94,86 Z" fill="#d8362d"/>')
    band = "#d8362d" if kind == "j3" else "#d9d9d9"
    S.add(f'<path d="M94,88 L146,88 L147,118 L93,118 Z" fill="{band}" stroke="#8a8a8a" stroke-width="1"/>')
    # retro-reflective sheen on the band
    S.add('<path d="M97,92 L142,92 L143,100 L96,100 Z" fill="#ffffff" opacity="0.45"/>')
    return str(S)


def voyant_direction(params):
    """Steering-assist tell-tale: steering wheel seen from the front with '!' on a dark dashboard tile."""
    c = params.get("colour", "#e53935")
    S = SVG(360, 360)
    S.add('<defs><filter id="g" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter></defs>')
    S.add('<rect x="0" y="0" width="360" height="360" rx="43" fill="#1b1b1b"/>')
    wheel = (f'<circle cx="180" cy="180" r="112" fill="none" stroke="{c}" stroke-width="26"/>'
             f'<circle cx="180" cy="180" r="34" fill="{c}"/>'
             f'<path d="M180,214 L180,292 M70,166 L146,180 M290,166 L214,180" stroke="{c}" stroke-width="22" stroke-linecap="round"/>'
             f'<rect x="168" y="112" width="24" height="60" rx="6" fill="#1b1b1b"/><circle cx="180" cy="188" r="12" fill="#1b1b1b"/>'
             f'<rect x="171" y="118" width="18" height="46" rx="5" fill="{c}"/><circle cx="180" cy="186" r="9" fill="{c}"/>')
    S.add(f'<g filter="url(#g)" opacity="0.6">{wheel}</g>')
    S.add(wheel)
    return str(S)


REGISTRY.update({
    "balise_piquet": balise_piquet, "voyant_direction": voyant_direction,
    "voie_insertion": voie_insertion, "bande_cyclable": bande_cyclable, "damier": damier, "ralentisseur": ralentisseur,
    "marquage_temporaire": marquage_temporaire, "zone_bleue": zone_bleue, "losange_sol": losange_sol, "cvcb": cvcb,
    "livraison": livraison, "direction_panel": direction_panel, "lieu_dit": lieu_dit, "feu_bicolore": feu_bicolore,
    "cone": cone, "triangle_seul": triangle_seul,
})
