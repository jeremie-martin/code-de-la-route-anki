"""Generated drawings: every one used by a card renders, keeps its text inside the frame without overlaps,
and a « verso » image has exactly the canvas of its front (the back only adds answer text in place)."""
import re
import unittest
import xml.etree.ElementTree as ET

from build.build import load_all
from build import gen_images
from build.gen_images import text_width

NS = "{http://www.w3.org/2000/svg}"


def used_generators():
    """(note id, generator, params, verso) for every generated front image and back illustration of the data."""
    data = load_all()
    out = []
    for kind in ("faits", "questions", "affirmations", "reconnaissance"):
        for note in data[kind]:
            for spec in (note.get("image"), note.get("illustration")):
                if isinstance(spec, dict) and "gen" in spec:
                    out.append((note["id"], spec["gen"], spec.get("params") or {}, bool(spec.get("verso"))))
    return out


def text_boxes(svg: str):
    """Approximate boxes of the labels that are not inside a rotated or scaled group: (x0, y0, x1, y1, text)."""
    root = ET.fromstring(svg)
    boxes = []

    def walk(node, dx, dy):
        transform = node.get("transform", "")
        if any(k in transform for k in ("rotate", "scale", "matrix")):
            return
        m = re.search(r"translate\(([-\d.]+)[ ,]+([-\d.]+)\)", transform)
        if m:
            dx, dy = dx + float(m.group(1)), dy + float(m.group(2))
        if node.tag == NS + "text" and (node.text or "").strip():
            size = float(node.get("font-size", 16))
            x, y = float(node.get("x", 0)) + dx, float(node.get("y", 0)) + dy
            w = text_width(node.text.strip(), size, int(node.get("font-weight", 400)))
            anchor = node.get("text-anchor", "start")
            x0 = x - w / 2 if anchor == "middle" else x - w if anchor == "end" else x
            boxes.append((x0, y - size * 0.72, x0 + w, y + size * 0.2, node.text.strip()))
        for child in node:
            walk(child, dx, dy)

    walk(root, 0, 0)
    return root, boxes


def canvas(root):
    vb = [float(v) for v in root.get("viewBox").split()]
    return vb[0], vb[1], vb[0] + vb[2], vb[1] + vb[3]


class GeneratedImagesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.used = used_generators()

    def test_the_checker_sees_overflow_and_overlap(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100" viewBox="0 0 200 100">'
               '<text x="190" y="40" font-size="18" font-weight="700">accotement</text>'
               '<text x="10" y="80" font-size="18">fin d’interdiction</text>'
               '<text x="60" y="82" font-size="18">6 : fin</text></svg>')
        root, boxes = text_boxes(svg)
        _, _, right, _ = canvas(root)
        self.assertGreater(boxes[0][2], right)                                   # runs off the frame
        a, b = boxes[1], boxes[2]
        self.assertTrue(a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3])  # the two labels collide

    def test_verso_images_keep_the_front_canvas(self):
        for ident, gen, params, verso in self.used:
            if not verso:
                continue
            with self.subTest(note=ident):
                front, _ = text_boxes(gen_images.render(gen, params))
                back, _ = text_boxes(gen_images.render(gen, {**params, "verso": True}))
                self.assertEqual(canvas(front), canvas(back))

    def test_labels_stay_inside_and_do_not_overlap(self):
        # scenario-style plans (road, intersection, roundabout) are checked by the scenario review, not here
        skip = {"road", "intersection", "roundabout"}
        for ident, gen, params, verso in self.used:
            if gen in skip:
                continue
            for side in ((False, True) if verso else (False,)):
                with self.subTest(note=ident, verso=side):
                    root, boxes = text_boxes(gen_images.render(gen, {**params, "verso": side} if side else params))
                    left, top, right, bottom = canvas(root)
                    for x0, y0, x1, y1, s in boxes:
                        self.assertTrue(left - 1 <= x0 and x1 <= right + 1 and top - 1 <= y0 and y1 <= bottom + 1,
                                        f"« {s} » dépasse du cadre")
                    for i, a in enumerate(boxes):
                        for b in boxes[i + 1:]:
                            overlap = a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
                            self.assertFalse(overlap, f"« {a[4]} » chevauche « {b[4]} »")


if __name__ == "__main__":
    unittest.main()
