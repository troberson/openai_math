# Summary-page interpretation review

The mechanical layer proves citation fidelity, not interpretation fidelity:
`build_summaries.py` renders all 373 pages from `notes/data/summaries/<NNN>.md`
and `verify_summaries.py`'s five passes (marker / render-diff / provenance /
manuscript-dir / bare-citation) check that every quotation lands on the line it
cites, never what the surrounding prose asserts. This page records the reading
pass the mechanical layer cannot do — the one under **math-301** — and the
corrections it found.

## Method

Read the rendered pages in `notes/gen/summaries/` against the manuscript
statement environments and the `notes/gen/tables/catalog.tsv` ledger row,
tier by tier (T3 first, ~138, highest claim density; then T2, ~106; then T0,
~128). Four checks per family:

1. **Graduate theorems** match the manuscript's statement environments
   (quantifier order, hypotheses, scope).
2. **Prior paragraphs** — the `**Prior (my training data, not this repo).**`
   block, the highest-risk content because it is a claim about the literature,
   not derived from the repo — do not assert a consequence or overclaim what
   the literature supports.
3. **Formalization sections** match the ledger row (`tier`, `chal`, `mainres`,
   `paps_form`, `scope_note`).
4. **Cross-tier consistency** in how the same tier/stub pattern is described.

The pass is a cross-discipline sample, not a census of all 373: ~30 families
read in full across number theory, algebraic geometry, combinatorics, convex
and metric geometry, theoretical computer science, and analysis. The
fleet-wide mechanical sweep below is census-wide; the interpretive reading is
the sample.

## Corrections

### 160 — Superexponential van der Waerden numbers (Combinatorics, T3)

One defect, two sections, both fabricated author attributions. The rendered
page `notes/gen/summaries/160-superexponential-van-der-waerden-numbers.md`
(then carrying the pre-fix data file `notes/data/summaries/160.md`) credited
people the manuscript does not cite.

- **Undergraduate summary.** Claimed *"Classical results (bibercourt,
  Hales–Jewett, etc.) gave **tower-type** upper bounds."* Neither `bibercourt`
  nor `Hales–Jewett` appears anywhere in the manuscript
  (`preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/`).
  Fixed in the data file to *"Classical results (van der Waerden's original
  proof, and subsequent refinements) gave **tower-type** upper bounds"* — the
  bound the introduction attributes to van der Waerden's 1927 proof and its
  successors.
- **History of the conjecture.** Claimed *"The **upper** bounds are classical:
  B\H{a}b (1933), Hales–Jewett (1963), and subsequent improvements give
  tower-type bounds…"* — the same two fabricated names. Fixed to *"The
  **upper** bounds go back to van der Waerden's original proof and grow at a
  tower-like (indeed far worse, primitive-recursive) rate; the quantitative
  upper bounds include Shelah's primitive-recursive bound and those following
  from Gowers's proof of Szemerédi's theorem"* — all three credits are verbatim
  in `build/sections/01-introduction.tex` (the "Earlier bounds" survey and the
  explicit *"quantitative upper bounds include Shelah's primitive-recursive
  bound (1988) and the bounds following from Gowers's proof of Szemerédi's
  theorem (2001)"* line).

The fix is in the **data file** `notes/data/summaries/160.md`; the rendered
page was regenerated with `python3 notes/scripts/build_summaries.py` and
re-verified clean by `python3 notes/scripts/verify_summaries.py`
(**373 pages, 0 problems**, all five passes). The fabricated names do not
appear in the re-rendered page. The ledger row `fam=160` is unaffected
(`tier T3`, `paps 1`, `paps_form 1`, `chal 1`, `mainres 1`, `scope_note 1`,
`shapes resolution|uniform`, `resolves_named 0`) — the defect was in prose
attribution, not in any ledger-derived field.

No other page in the pass carried a fabricated name, a theorem that does not
match its statement environment, a Prior paragraph overclaiming, a
formalization section disagreeing with its ledger row, or a cross-tier
inconsistency.

## Fleet-wide mechanical sweep (census)

Beyond the ~30 families read in full, two corpus-wide sweeps were run to make
the negative claim defensible without a full reading of all 373:

- **Fabricated-name sweep.** A regex over every attribution parenthetical in
  all 373 `notes/data/summaries/*.md` data files confirmed no other garbled or
  invented surname; `grep` for the two 160 names over the whole `preprints/`
  tree reads **0** matches.
- **Prior-paragraph hedge sweep.** All 292 pages carrying a
  `**Prior (my training data, not this repo).**` block were checked. Each one
  separates the training-data prior from the repo-derived claim and carries a
  hedge — the standard forms include *"I have not seen this result and cannot
  confirm it independently"* (e.g. 001), *"the prior is a training-data
  recollection at an early-2025 cutoff, self-rated, and the repo supplies only
  the manuscript's citations"* (e.g. 334, 349), and *"I cannot independently
  verify this manuscript's argument"* (e.g. 091). A first-pass word-list
  flagged 48 pages for phrasing outside the list; spot-reading those (001,
  291, 334, 349, and the embedded 091/102/127) showed every one hedges in
  its own words — the flags are list-width false positives, not overclaims.

## Not checked

- The ~340 families not read in full have had only the two mechanical sweeps
  applied, not a reading of theorem text, Prior prose, or formalization
  sections. A fabricated name in an un-read family's prose, a theorem whose
  quantifier order the sample did not reach, or a cross-tier inconsistency
  outside the sampled disciplines would not have been caught.
- The Prior-paragraph sweep confirms the hedge is *present*, not that the
  training-data claim it hedges is *correct*; that is the corpus's
  surprise-ranking problem, not this accuracy pass's.
