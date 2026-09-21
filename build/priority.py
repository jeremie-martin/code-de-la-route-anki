"""Priority solver for intersection scenarios.

Given the same spec as build.diagrams.draw_intersection, compute the order in
which vehicles cross. The result is used to CROSS-CHECK hand-written answers in
data/scenarios.yaml: a scenario whose hand answer disagrees with the solver
fails the build, so a mistake in either is caught.

Model (Code de la route, art. R415-5 to R415-11 and R412-30, R414-..):
  0. The agent's explicit directions override the following rules.
  1. Véhicules d'intérêt général prioritaires explicitly signalled pass first.
  2. Tramways pass before other vehicles (unless lights/agent say otherwise).
  3. Lights: green passes before red. Fixed amber = stop (treated as red here).
     Flashing amber leaves the signs/default priority rules applicable.
  4. Signs: a vehicle facing STOP / cédez-le-passage, or leaving a private
     exit (parking, chemin), yields to every vehicle on the road it joins.
     A vehicle on a road marked AB6/AB2, or with no sign while others have
     STOP/cédez, has priority.
  5. Same level: a vehicle turning left yields to oncoming vehicles going
     straight or turning right (R415-4/R412-30). Otherwise priorité à droite
     (R415-5): I yield to the vehicle coming from my right.

Paths are modelled on a 2x2 grid of the intersection square; two vehicles
conflict when their paths share a cell or merge into the same exit lane.
Opposite left-turners are declared non-conflicting (they cross "par la
gauche" without a priority question).
"""
from __future__ import annotations

from itertools import combinations

from build.diagrams import right_of, opposite, turn_target

# quadrant sequence per (approach, goes); a vehicle enters by its right-hand quadrant and leaves by the
# right-hand quadrant of its exit branch
PATHS = {
    ("S", "straight"): ["SE", "NE"], ("S", "right"): ["SE"], ("S", "left"): ["SE", "NE", "NW"],
    ("N", "straight"): ["NW", "SW"], ("N", "right"): ["NW"], ("N", "left"): ["NW", "SW", "SE"],
    ("E", "straight"): ["NE", "NW"], ("E", "right"): ["NE"], ("E", "left"): ["NE", "NW", "SW"],
    ("W", "straight"): ["SW", "SE"], ("W", "right"): ["SW"], ("W", "left"): ["SW", "SE", "NE"],
}

YIELD_SIGNS = {"stop", "cedez"}
PRIORITY_SIGNS = {"prioritaire", "priorite_ponctuelle"}


def level(approach: str, ap: dict, spec: dict) -> int:
    """0 = must yield (stop/cédez/private), 1 = priorité à droite, 2 = priority road."""
    sign = ap.get("sign")
    if ap.get("private") or sign in YIELD_SIGNS:
        return 0
    if sign in PRIORITY_SIGNS or approach in spec.get("priority_road", []):
        return 2
    others_yield = any(
        (o != approach) and (oap.get("private") or oap.get("sign") in YIELD_SIGNS)
        for o, oap in spec["approaches"].items()
    )
    return 2 if others_yield else 1


def conflict(a: str, ga: str, b: str, gb: str) -> bool:
    if a == opposite(b) and ga == "left" and gb == "left":
        return False
    pa, pb = PATHS[(a, ga)], PATHS[(b, gb)]
    if set(pa) & set(pb):
        return True
    return turn_target(a, ga) == turn_target(b, gb)


def yields(a: str, b: str, spec: dict) -> bool | None:
    """True if a yields to b, False if b yields to a, None if no ordering."""
    apa, apb = spec["approaches"][a], spec["approaches"][b]
    va, vb = apa["vehicle"], apb["vehicle"]
    # agent: his orders void lights and signs (R411-28)
    agent = spec.get("agent")
    if agent == "bras_leve":
        return None
    agent_frees_both = False
    if agent in ("bras_tendus_NS", "bras_tendus_EW"):
        blocked = {"N", "S"} if agent == "bras_tendus_NS" else {"E", "W"}
        ba, bb = a in blocked, b in blocked
        if ba != bb:
            return ba
        if ba:  # both blocked: no order
            return None
        agent_frees_both = True  # both free: only the turning rules (5) apply
    # A vehicle's appearance alone does not announce an urgent intervention.
    # The scenario explicitly records active warning devices as `siren`.
    ea, eb = bool(va.get("siren")), bool(vb.get("siren"))
    if ea != eb:
        return not ea
    if not agent_frees_both:
        # 2. trams
        ta, tb = va.get("kind") == "tram", vb.get("kind") == "tram"
        lights = {k: v.get("sign") for k, v in spec["approaches"].items()
                  if v.get("sign") in {"feu_vert", "feu_rouge", "feu_orange"}}
        if ta != tb and not lights:
            return not ta
        # 3. lights
        if lights:
            ga_, gb_ = apa.get("sign") == "feu_vert", apb.get("sign") == "feu_vert"
            if ga_ != gb_:
                return not ga_
            if not ga_:
                return None
        # 4. signs / levels
        else:
            la, lb = level(a, apa, spec), level(b, apb, spec)
            if la != lb:
                return la < lb
    # 5. same level: left-turn rule, then priorité à droite
    goes_a, goes_b = apa.get("goes", "straight"), apb.get("goes", "straight")
    if a == opposite(b):
        if goes_a == "left" and goes_b in ("straight", "right"):
            return True
        if goes_b == "left" and goes_a in ("straight", "right"):
            return False
        return None
    if right_of(a) == b:
        return True
    if right_of(b) == a:
        return False
    return None


def solve(spec: dict) -> dict:
    """Return {"order": [approach,...] or None, "pairs": {(a,b): who_first}, "cycle": bool}."""
    aps = {k: v for k, v in spec["approaches"].items() if v.get("vehicle")}
    edges = {a: set() for a in aps}  # a -> set of b that must pass before a
    pairs = {}
    for a, b in combinations(aps, 2):
        ga, gb = aps[a].get("goes", "straight"), aps[b].get("goes", "straight")
        if not conflict(a, ga, b, gb):
            pairs[(a, b)] = "independant"
            continue
        y = yields(a, b, spec)
        if y is True:
            edges[a].add(b); pairs[(a, b)] = b
        elif y is False:
            edges[b].add(a); pairs[(a, b)] = a
        else:
            pairs[(a, b)] = "indetermine"
    # topological sort (Kahn) with deterministic tie-break by compass order
    order, remaining = [], dict(edges)
    while remaining:
        ready = [a for a, deps in remaining.items() if not (deps & set(remaining))]
        if not ready:
            return {"order": None, "pairs": pairs, "cycle": True}
        ready.sort(key=lambda a: ["N", "E", "S", "W"].index(a))
        # ties (several ready at once) are only acceptable if they don't conflict
        order.append(ready)
        for a in ready:
            remaining.pop(a)
    return {"order": order, "pairs": pairs, "cycle": False}


def passes_before(spec: dict, a: str, b: str) -> str:
    """'avant' if a passes before b, 'apres' if after, 'independant'/'indetermine' otherwise."""
    r = solve(spec)["pairs"]
    if (a, b) in r:
        v = r[(a, b)]
    elif (b, a) in r:
        v = r[(b, a)]
    else:
        raise KeyError(f"paire ({a}, {b}) absente du solveur : approche inconnue, sans véhicule, ou a == b")
    if v in ("independant", "indetermine"):
        return v
    return "avant" if v == a else "apres"


if __name__ == "__main__":
    # self-test on textbook cases
    def spec(**aps):
        return {"approaches": {k: {"vehicle": {"colour": "x"}, **v} for k, v in aps.items()}}

    # 1. priorité à droite, 3 vehicles all straight: N first (nobody on its right), then E, then S
    r = solve(spec(S={"goes": "straight"}, E={"goes": "straight"}, N={"goes": "straight"}))
    assert r["order"] == [["N"], ["E"], ["S"]], r
    # 2. I go straight, oncoming turns left: I pass first
    assert passes_before(spec(S={"goes": "straight"}, N={"goes": "left"}), "S", "N") == "avant"
    # 3. I turn left, oncoming straight: I pass after
    assert passes_before(spec(S={"goes": "left"}, N={"goes": "straight"}), "S", "N") == "apres"
    # 4. STOP for me, vehicle from left straight: I pass after
    assert passes_before(spec(S={"goes": "straight", "sign": "stop"}, W={"goes": "straight"}), "S", "W") == "apres"
    # 5. Vehicle from right has cédez, I have nothing: I pass first
    assert passes_before(spec(S={"goes": "straight"}, E={"goes": "straight", "sign": "cedez"}), "S", "E") == "avant"
    # 6. priorité à droite with vehicle from left: I pass first
    assert passes_before(spec(S={"goes": "straight"}, W={"goes": "straight"}), "S", "W") == "avant"
    # 7. tram from left: tram first
    s = spec(S={"goes": "straight"}, W={"goes": "straight"}); s["approaches"]["W"]["vehicle"]["kind"] = "tram"
    assert passes_before(s, "S", "W") == "apres"
    # 8. both turn right: independent
    assert passes_before(spec(S={"goes": "right"}, N={"goes": "right"}), "S", "N") == "independant"
    # 9. lights: me green, right red
    assert passes_before(spec(S={"goes": "straight", "sign": "feu_vert"}, E={"goes": "straight", "sign": "feu_rouge"}), "S", "E") == "avant"
    # 10. private exit on my right: I pass first
    assert passes_before(spec(S={"goes": "straight"}, E={"goes": "straight", "private": True}), "S", "E") == "avant"
    # 11. 4 vehicles priorité à droite all straight -> cycle
    assert solve(spec(S={"goes": "straight"}, E={"goes": "straight"}, N={"goes": "straight"}, W={"goes": "straight"}))["cycle"]
    # 12. agent frees the N-S axis: lights and signs are void, only the turning rules apply
    s = spec(S={"goes": "left", "sign": "feu_vert"}, N={"goes": "straight", "sign": "feu_rouge"}); s["agent"] = "bras_tendus_EW"
    assert passes_before(s, "S", "N") == "apres"
    # 13. a pair the solver never computed must not pass silently
    try:
        passes_before(spec(S={"goes": "straight"}, E={"goes": "straight"}), "S", "Q")
    except KeyError:
        pass
    else:
        raise AssertionError("paire inconnue acceptée")
    print("priority self-test OK")
