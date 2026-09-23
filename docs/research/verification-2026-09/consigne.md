# Fact-check of every note — shared brief

Do not spawn sub-agents. Do not modify any repository file. Write only to the paths given in your task.

## Why
`/home/jmartin/code-de-la-route-anki` builds a French Anki deck (1 015 notes) to pass the ETG (permis B) in 2026. Its
owner needs it to be **trustworthy**: every statement a learner memorises must be true, with its conditions. Earlier
reviews focused on design; the owner then found a card that stated a rule more broadly than the law (a pedestrian with a
white cane: « je m'arrête et le laisse traverser » unconditionally, whereas the French Code has no specific rule —
R415-11 applies: yield to a pedestrian who engages or clearly shows the intention to cross; the « canne levée = arrêt
partout » rule is Swiss). This review hunts that class of error across the whole deck, one note at a time.

This is a **fact-check**, not a design or style review. Do not propose rewordings for taste, layout, images or card
design unless the wording makes a statement false or misleading.

## Sources
- Consolidated Code de la route of 2026-09-10: `docs/research/sources/cdr.txt` (articles labelled at line start, e.g.
  `grep -n "^R. 415-11 " docs/research/sources/cdr.txt`; L articles `^L. 223-6 `; read the whole article with
  `awk '/^R. 415-11 /,/^R. 415-12 /' docs/research/sources/cdr.txt`). This is the primary source for rules.
- Web for texts outside the Code: Légifrance (arrêtés, e.g. arrêté du 24 novembre 1967 on signs; IISR), service-public.fr,
  securite-routiere.gouv.fr, interieur.gouv.fr, ANSM, ADEME, INRS/secourisme (first aid: current French recommendations).
- Already logged checks: `data/_meta/source_checks.yaml` (you may rely on an entry only if its `portee` covers the exact
  claim; otherwise check again).
- Card texts as the learner sees them: `/tmp/claude-1000/-home-jmartin-code-de-la-route-anki/c64d96e5-556d-424e-a0d4-701548ce9111/scratchpad/factcheck/cards/dump.md`
  (`### NNNN id cK [type]`, RECTO / VERSO). The data is in `data/` (see `docs/maintenance.md`); recognition notes are
  generated from `data/signs_inventory.yaml` + `data/_meta/sign_overrides.yaml` (report fixes against the override key).
- Design principles for what may be stated: `docs/conception.md` (« Enseigner la règle actuelle… Un raccourci
  pédagogique doit être nommé comme tel… Ne pas faire passer une supposée convention d’examen avant une consigne
  officielle actuelle »).

## What to check, for EVERY note of your list (front, answer, explanation/pourquoi/piège/complément, captions)
Extract each factual claim and classify it:
1. **Law** (Code, arrêté, IISR): find the article and check the claim *and its conditions* (who, where, when, which
   vehicle, which road, thresholds, sanctions: amount, class, points, suspension).
2. **Official recommendation** (Sécurité routière, first-aid bodies, constructors): check it is presented as advice, not
   as an obligation, and matches the current source.
3. **Exam convention / teaching shortcut** (e.g. ×2 braking when wet, dizaines au carré): acceptable only if labelled
   as such on the card.
4. **Physics / arithmetic**: recompute.

Error types to hunt (name the type in your report):
- `FAUX` false or outdated (2026) statement.
- `SUREXTENSION` rule stated more broadly or more absolutely than the source (missing condition, « toujours », « en
  toutes circonstances », « jamais », « interdit » where it is only advised, obligation where the text says « peut »).
- `SOUS-EXTENSION` rule stated too narrowly (a learner would wrongly think it doesn't apply).
- `CONVENTION-NON-SIGNALÉE` exam convention or shortcut presented as law.
- `ÉTRANGER` rule from another country or an unofficial source presented as French law.
- `SANCTION` wrong amount, class, points or measure.
- `CONTRADICTION` two cards of the deck disagree (give both ids; grep `data/` for the same topic).
- `SOURCE` the card's `source` field doesn't support the claim (the claim itself may be right).

## Output — two files
1. A **ledger** covering every note of your list, one line per note, in list order:
   `id | verdict | sources checked (articles / URLs) | remark`
   verdict ∈ `OK` (every claim checked and supported), `FIX` (at least one error), `INCERTAIN` (you could not settle a
   claim: say which and why). No note may be skipped; « OK » means you actually checked, not that nothing looked odd.
2. A **report** of every `FIX` and `INCERTAIN`, grouped by error type: id, the exact text concerned, the problem, the
   evidence (article number + quoted words, or URL + quoted words), and a corrected text ready to paste that keeps the
   card's form and length. Be strict with yourself: a finding without a quoted source is not a finding. First line:
   counts per verdict and per error type.
End your reply with only the counts and the two paths.
