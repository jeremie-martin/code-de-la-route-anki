"""Convert data/signs_inventory.yaml (research dataset) into deck notes in data/reconnaissance/.

Rules:
  * image = Commons file from the inventory if it resolves; else ALT_COMMONS[code]; else GEN_MAP[code]
    (a generator spec); explicit overrides take precedence. Missing images fail generation.
  * selection: explicit, reasoned exclusions in data/_meta/sign_exclusions.yaml; no rarity filter.
  * text fields are lightly normalised (generic implantation text compressed, 'fin' folded into complement,
    notes split between 'piege' and 'complement').
The generated files must not be edited by hand: re-running this script overwrites them, so
corrections go into data/_meta/sign_overrides.yaml (key = note id, a null value removes the field).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "data" / "signs_inventory.yaml"
OUT_DIR = ROOT / "data" / "reconnaissance"
sys.path.insert(0, str(ROOT))
from build.commons_fetch import find  # noqa: E402

CAT_FILE = {
    "danger": ("panneaux_danger", "panneaux"),
    "intersection_priorite": ("panneaux_priorite", "panneaux"),
    "interdiction": ("panneaux_interdiction", "panneaux"),
    "obligation": ("panneaux_obligation", "panneaux"),
    "fin_prescription": ("panneaux_fin", "panneaux"),
    "prescription_zonale": ("panneaux_zones", "panneaux"),
    "indication": ("panneaux_indication", "panneaux"),
    "indication_service": ("panneaux_services", "panneaux"),
    "direction": ("panneaux_direction", "panneaux"),
    "localisation": ("panneaux_localisation", "panneaux"),
    "panonceau": ("panonceaux", "panonceaux"),
    "balise": ("balises", "balises"),
    "temporaire": ("temporaire", "panneaux"),
    "passage_a_niveau": ("passage_a_niveau", "panneaux"),
    "voie_reservee": ("voies_reservees", "panneaux"),
    "marquage": ("marquages", "marquages"),
    "feux": ("feux", "feux"),
    "autre": ("autres", "panneaux"),
}
TYPE_BY_CAT = {"panonceau": "panonceau", "balise": "balise", "marquage": "marquage", "feux": "feu"}
# Alternative Commons files for entries whose inventory file name is blank or wrong.
ALT_COMMONS = {
    "A9b": "France road sign A9.svg", "M11d": "France road sign M11d.png", "KM1": "France Road Sign KM1.png", "KM2": "France Road Sign KM2.png",
    "C20b": "France road sign C20b.svg",
    "M12": "France road sign M12D.svg",
    "J4": "FR road beacon J4.svg", "J14a": "FR road beacon J14a.svg", "J14b": "FR road beacon J14b.svg",
    "J6": "FR road beacon J6.svg", "J7": "FR road beacon J7.svg", "J11": "FR road beacon J11.svg",
    "J12": "FR road beacon J12.svg", "J13": "FR road beacon J13.svg", "J1": "J1.svg", "J1bis": "FR road beacon J1 bis.svg",
    "J3": "J3A.svg", "J15": "FR road beacon J15a.svg", "J16": "FR road beacon J16.svg",
    "K2": "Barrage K2.webp", "K14": "Ruban K14.webp", "K16": "Séparateur K16.webp", "K1": "Fanion K1.webp",
    "K8": "K8e1.svg", "K15": "K15.svg",
    "KC1": "KC1 route barrée.svg", "KD8": "KD8e3.svg", "KD9": "KD9e3.svg", "KD10": "KD10e1.svg",
    "E42": "E42.svg", "E43": "E43.svg", "E44": "E44.svg", "E45": "E45.svg",
    "D20": "D21a.svg", "D30": "D31b.svg",
    "VR-LOSANGE-DEBUT": "Panneau de début de voie réservée aux véhicules à occupation multiple.svg",
    "VR-LOSANGE-FIN": "Panneau de fin de voie réservée aux véhicules à occupation multiple en France.svg",
    "G2": "France road sign A7.svg",
    "SR2": None,
}

# Generator specs for markings, lights, gestures and a few signs without vector files.
GEN_MAP = {
    "J1": ("balise_piquet", {"kind": "j1"}),
    "J3": ("balise_piquet", {"kind": "j3"}),
    "J6": ("balise_piquet", {"kind": "j6"}),
    "J1bis": ("balise_piquet", {"kind": "j1bis"}),
    "MARQ-ligne-continue": ("ligne_axiale", {"style": "continue"}),
    "MARQ-ligne-discontinue-T1": ("ligne_axiale", {"style": "discontinue", "dash": 3, "gap": 10}),
    "MARQ-ligne-T'1": ("ligne_axiale", {"style": "discontinue", "dash": 1.5, "gap": 5}),
    "MARQ-ligne-dissuasion": ("ligne_axiale", {"style": "dissuasion", "dash": 3, "gap": 1.33}),
    "MARQ-ligne-annonce": ("fleches", {"kind": "rabattement"}),
    "MARQ-ligne-mixte": ("ligne_axiale", {"style": "mixte_moi"}),
    "MARQ-fleches-rabattement": ("fleches", {"kind": "rabattement"}),
    "MARQ-fleches-directionnelles": ("fleches", {"kind": "directionnelles"}),
    "MARQ-ligne-stop": ("transversale", {"kind": "stop"}),
    "MARQ-ligne-cedez": ("transversale", {"kind": "cedez"}),
    "MARQ-ligne-effet-feux": ("transversale", {"kind": "effet_feux"}),
    "MARQ-passage-pietons": ("passage", {"kind": "pieton"}),
    "MARQ-passage-cyclistes": ("passage", {"kind": "cycliste"}),
    "MARQ-zebra": ("passage", {"kind": "zebra"}),
    "MARQ-ligne-rive": ("ligne_rive", {"style": "discontinue", "dash": 3, "gap": 3.5}),
    "MARQ-ligne-BAU-T4": ("ligne_rive", {"style": "bau"}),
    "MARQ-chevrons": ("chevrons", {}),
    "MARQ-voie-insertion": ("voie_insertion", {}),
    "MARQ-bande-cyclable": ("bande_cyclable", {"green": True}),
    "MARQ-couloir-bus": ("voie_texte", {"text": "BUS"}),
    "MARQ-damier-blanc": ("damier", {"colour": "blanc"}),
    "MARQ-ligne-jaune-continue": ("ligne_jaune", {"style": "continue"}),
    "MARQ-ligne-jaune-discontinue": ("ligne_jaune", {"style": "discontinue"}),
    "MARQ-ligne-jaune-zigzag": ("ligne_jaune", {"style": "zigzag"}),
    "MARQ-livraison": ("livraison", {}),
    "MARQ-marquage-temporaire-jaune": ("marquage_temporaire", {}),
    "MARQ-zone-bleue": ("zone_bleue", {}),
    "MARQ-damier-rouge-blanc": ("damier", {"colour": "rouge"}),
    "MARQ-ralentisseur-triangles": ("ralentisseur", {"kind": "dos_d_ane"}),
    "MARQ-plateau-sureleve": ("ralentisseur", {"kind": "plateau"}),
    "MARQ-sas-velo": ("passage", {"kind": "sas_velo"}),
    "MARQ-CVCB": ("cvcb", {}),
    "MARQ-losange-VR": ("losange_sol", {}),
    "FEU-rouge": ("feu_tricolore", {"state": "rouge"}),
    "FEU-jaune-fixe": ("feu_tricolore", {"state": "orange"}),
    "FEU-vert": ("feu_tricolore", {"state": "vert"}),
    "FEU-jaune-clignotant": ("feu_tricolore", {"state": "orange_clignotant"}),
    "FEU-rouge-clignotant": ("feu_rouge_clignotant", {"twin": True}),
    "R24": ("feu_rouge_clignotant", {"twin": False}),
    "R12": ("feu_pieton", {"state": "vert"}),
    "R13": ("feu_velo", {"state": "vert"}),
    "R14": ("feu_tricolore", {"state": "vert", "arrow": "left"}),
    "R16": ("feu_fleche_composite", {"colour": "orange", "direction": "right", "blink": True}),
    "R17": ("feu_bus", {"bar": "vertical"}),
    "R21a": ("signal_affectation", {"lanes": ["croix", "fleche", "fleche"], "me_lane": 0}),
    "R21b": ("signal_affectation", {"lanes": ["fleche", "fleche", "fleche"]}),
    "R21c": ("signal_affectation", {"lanes": ["rabattement_droite", "fleche", "fleche"], "me_lane": 0}),
    "R23": ("feu_bicolore", {"state": "vert"}),
    "KR11": ("feu_chantier", {"state": "rouge"}),
    "AGENT-bras-leve": ("agent", {"pose": "bras_leve"}),
    "AGENT-bras-tendu-face": ("agent", {"pose": "bras_tendus"}),
    "AGENT-profil": ("intersection", {"approaches": {"S": {"vehicle": {"colour": "bleu", "me": True}, "goes": "straight"}, "E": {"vehicle": {"colour": "rouge"}, "goes": "straight"}}, "agent": "bras_tendus_NS"}),  # MOI on the axis of the arms: sees the profile, passes
    "AGENT-geste-avancer": ("agent", {"pose": "avancer"}),
    "TRIANGLE-PRESIGNALISATION": ("triangle_seul", {}),
    "K5a": ("cone", {}),
    "D-COULEUR-BLEU": ("direction_panel", {"colour": "bleu", "text": "LYON", "dist": "45"}),
    "D-COULEUR-VERT": ("direction_panel", {"colour": "vert", "text": "PARIS", "dist": "12"}),
    "D-COULEUR-BLANC": ("direction_panel", {"colour": "blanc", "text": "Vernon", "dist": "3"}),
    "D-COULEUR-JAUNE": ("direction_panel", {"colour": "jaune", "text": "Évreux", "dist": ""}),
    "D-COULEUR-MARRON": ("direction_panel", {"colour": "marron", "text": "Château", "dist": "8"}),
    "E31": ("lieu_dit", {"text": "Le Bourg"}),
}

# Exclusions require an editorial reason; the report links each to its teaching coverage.
SELECTION_FILE = ROOT / "data/_meta/sign_exclusions.yaml"

GENERIC_IMPLANT = re.compile(r"^Hors agglomération\s*:\s*100 à 200 m", re.I)

# Category-level sentences that used to be repeated on every sign of a family; the rule lives in one card.
# They are dropped from the cards: the rule is carried once by a fact/question card
# (l-implantation-danger, l-portee-prescription, l-panonceau-portee, l-signalisation-temporaire).
BOILERPLATE = [
    r"^Sous le panneau qu'il complète, sur le même support\s*$",
    r"^il ne s'applique qu'à ce panneau\.?$",
    r"^Implanté à ~150 m du danger hors agglomération \(200 m sur autoroute\), ~50 m en agglomération\s*$",
    r"^un panonceau M1 précise une distance différente\.?$",
    r"^Placé à l'endroit où commence l'(interdiction|obligation)\s*$",
    r"^répété après chaque intersection( \(sauf voies privées et chemins de terre\))?\.?$",
    r"^En position devant le service, ou en présignalisation au dernier carrefour \(avec panonceau de direction M3b et/ou de distance M1\)\.?$",
    r"^Placé à l'endroit où cesse la prescription\.?$",
    r"^Comme les panneaux A : environ 150 m avant le danger hors agglomération \(100 à 200 m\), 50 m en agglomération, souvent complété par un panonceau KM1 \(distance\).*$",
    r"^Fond JAUNE = signalisation temporaire \(chantier, événement, danger passager\) : elle prévaut sur la signalisation permanente contradictoire\.?$",
    r"^À chaque entrée de la zone\s*$",
    r"^la prescription vaut dans toutes les rues de la zone jusqu'au panneau de sortie, sans être répétée après les intersections\.?$",
]
BOILERPLATE_RE = [re.compile(p, re.I) for p in BOILERPLATE]


def strip_boilerplate(text: str) -> str:
    """Remove category-level sentences; keep what is specific to this sign."""
    if not text:
        return ""
    parts = re.split(r"(?<=[.;])\s+", text)
    kept = []
    for p in parts:
        core = p.rstrip(" ;.")
        if any(r.match(core) or r.match(p) for r in BOILERPLATE_RE):
            continue
        kept.append(p)
    out = " ".join(kept).strip()
    out = re.sub(r"^[;\s]+", "", out)
    if out and out[-1] == ";":
        out = out[:-1].rstrip() + "."
    return out


def slug(code: str) -> str:
    s = code.lower().replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def strip_unverified(text: str) -> str:
    """Keep sentences carrying research flags ('À VÉRIFIER') out of cards."""
    if not text:
        return ""
    parts = re.split(r"(?<=[.;])\s+", text)
    kept = [p for p in parts if "VÉRIFIER" not in p and "À VERIFIER" not in p]
    out = " ".join(kept).strip()
    out = re.sub(r"\s*\([^()]*VÉRIFIER[^()]*\)", "", out)
    return out


def split_notes(notes: str) -> tuple[str, str]:
    """Return (piege, complement) from the free-text notes."""
    if not notes:
        return "", ""
    n = strip_unverified(notes.strip())
    if re.search(r"confondre|pi[èe]ge|≠|attention|ne pas prendre|à ne pas", n, re.I):
        piege = re.sub(r"^\s*Pi[èe]ge\s*:\s*", "", n)
        return piege[:1].upper() + piege[1:], ""
    return "", n


OVERRIDES_FILE = ROOT / "data" / "_meta" / "sign_overrides.yaml"
OVERRIDES: dict = {}


def convert():
    global OVERRIDES
    if OVERRIDES_FILE.exists():
        OVERRIDES = yaml.safe_load(OVERRIDES_FILE.read_text(encoding="utf-8")) or {}
    inv = yaml.safe_load(INV.read_text(encoding="utf-8"))
    by_file: dict[str, list] = defaultdict(list)
    decisions = yaml.safe_load(SELECTION_FILE.read_text(encoding="utf-8"))
    excluded = {}
    known = {e['code'] for e in inv}
    for decision in decisions:
        if not decision.get('raison'):
            raise ValueError('Exclusion sans justification')
        for code in decision['codes']:
            if code in excluded or code not in known:
                raise ValueError(f'Exclusion dupliquée ou inconnue : {code}')
            excluded[code] = decision
    skipped, missing_img = [], []
    for e in inv:
        code = e["code"]
        cat = e["categorie"]
        if code in excluded:
            skipped.append((code, excluded[code]["raison"]))
            continue
        # image
        image = OVERRIDES.get(slug(code), {}).get("image")
        wf = (e.get("wikimedia_file") or "").strip()
        if image is not None:
            pass
        elif code in GEN_MAP:
            g, p = GEN_MAP[code]
            image = {"gen": g, "params": p}
            if g == "intersection":  # cropped plan view: same export size as the scenario cards
                image["width"] = 800
        elif code in ALT_COMMONS and ALT_COMMONS[code]:
            image = {"commons": ALT_COMMONS[code]}
        elif wf:
            key, entry = find(wf)
            if entry:
                image = {"commons": key[len("File:"):]}
        if image is None:
            missing_img.append((code, e["nom"]))
            continue
        if "commons" in image:
            key, entry = find(image["commons"])
            if not entry:
                missing_img.append((code, e["nom"] + f" [fichier introuvable: {image['commons']}]"))
                continue
        fname, sous = CAT_FILE[cat]
        typ = TYPE_BY_CAT.get(cat, "panneau")
        if code.startswith("AGENT"):
            typ, sous = "geste", "agents"
        if code == "TRIANGLE-PRESIGNALISATION" or code in ("K5a",):
            typ = "equipement"
        implant = (e.get("implantation") or "").strip()
        if GENERIC_IMPLANT.match(implant):
            implant = "Implanté à ~150 m du danger hors agglomération (200 m sur autoroute), ~50 m en agglomération ; un panonceau M1 précise une distance différente."
        fin = (e.get("fin") or "").strip()
        piege, note_c = split_notes(e.get("notes") or "")
        comp_parts = [p for p in (implant, f"Fin : {fin}." if fin else "", note_c) if p]
        item = {
            "id": slug(code),
            "type": typ,
            "code": code if not code.startswith(("MARQ-", "FEU-", "AGENT-", "D-COULEUR", "VR-", "TRIANGLE")) else "",
            "image": image,
            "nom": e["nom"].strip(),
            "signification": strip_unverified((e.get("signification") or "").strip()),
            "conduite": strip_unverified((e.get("conduite_a_tenir") or "").strip()),
            "complement": strip_boilerplate(strip_unverified(" ".join(comp_parts).strip())),
            "piege": piege,
            "theme": "L",
            "sous_theme": sous,
            "source": "IISR (Instruction interministérielle sur la signalisation routière) ; Wikipédia FR, signalisation routière en France",
        }
        if e.get("variants"):
            item["complement"] = (item["complement"] + f" Variantes courantes : {', '.join(str(v) for v in e['variants'])}.").strip()
        item = {k: v for k, v in item.items() if v not in ("", None)}
        for k, v in OVERRIDES.get(item["id"], {}).items():
            if v is None:
                item.pop(k, None)
            else:
                item[k] = v
        if item.get("complement"):
            item["complement"] = strip_boilerplate(item["complement"])
            if not item["complement"]:
                item.pop("complement")
        by_file[fname].append(item)
    unused = set(OVERRIDES) - {it["id"] for items in by_file.values() for it in items}
    if unused:
        print(f"ATTENTION: {len(unused)} clé(s) de {OVERRIDES_FILE.name} sans note correspondante (id erroné ou obsolète) : {sorted(unused)}", file=sys.stderr)
    if missing_img:
        raise ValueError(f"Signaux sélectionnés sans média : {missing_img}")
    OUT_DIR.mkdir(exist_ok=True)
    total = 0
    for fname, items in by_file.items():
        p = OUT_DIR / f"{fname}.yaml"
        header = f"# Généré par build/import_signs.py depuis data/signs_inventory.yaml ({len(items)} entrées). Corrections manuelles : data/_meta/sign_overrides.yaml\n"
        p.write_text(header + yaml.safe_dump(items, allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
        total += len(items)
        print(f"{p.name}: {len(items)}")
    print("total", total)
    print("\nSANS IMAGE (ignorés):")
    for m in missing_img:
        print("  ", m)
    print("\nEXCLUS:", len(skipped))


if __name__ == "__main__":
    convert()
