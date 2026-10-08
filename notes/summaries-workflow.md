# Summary-page production loop

The resume protocol for the `math-ckd` batches. Read this after a compaction; it is the state
carrier, so it states what to do and what not to re-derive.

## Current state (rewritten at every batch boundary)

- **Batch:** `math-ckd.2` is **complete and closed** (2026-10-08, commit `5d87d8bda`) — the 9 headline
  T0 families (002, 004, 006, 010, 011, 014, 016, 018, 019), 29 manuscripts, all in
  `notes/summaries/number-theory/`. `math-ckd.1` (the 10 trace families) closed the same day.
- **Pages done (21):** 102 (`notes/summaries/theoretical-computer-science/`), 001, 002, 004, 006, 007,
  010, 011, 014, 016, 017, 018, 019 (`notes/summaries/number-theory/`), 032
  (`notes/summaries/algebraic-and-complex-geometry/`), 087 (`notes/summaries/convex-and-metric-geometry/`),
  159 (`notes/summaries/combinatorics/`), 197 (`notes/summaries/algebra/`),
  221 (`notes/summaries/probability-and-statistical-mechanics/`), 271
  (`notes/summaries/mathematical-physics/`), 287 (`notes/summaries/operator-algebras/`), 362
  (`notes/summaries/partial-differential-equations/`). The ledger's `summary` column is 1 for those
  twenty-one; the generator reports "summary pages 21 of 372 families, 60 manuscripts behind them".
- **Next batch:** `math-ckd.3` — tier B, the 83 remaining T0 families with `resolves_named = 1`
  (124 manuscripts). `bd update math-ckd.3 --claim`, then steps 2–9 below per page. Check `bd ready`
  first: summaries are P4 and any ready P1/P2 issue outranks this batch.
- **Last gate run (2026-10-08, closing `math-ckd.2`):** regeneration byte-identical on two runs; 372
  families, 722 manuscripts, 162 formalized, 405 challenges, 185 `main_results` over 178 configs, 235
  scope notes, both cross-checks 0, discipline table summing 372 / 235 / 722 / 162 — the only line that
  moved is "summary pages 21 of 372 families, 60 manuscripts behind them" (was 12 / 31).
  `verify_summaries.py --mutant` over the 9 batch pages → **1470 marker positions, 499 quoted spans,
  0 problems (0 undetected mutants)**, 27 mutant FLAGGED lines (A1 inline, A3 block-quote attribution,
  B fabricated — three per page), no `UNUSED SOURCES`, no `AMBIGUOUS`. Re-run over all 21 pages at the
  boundary: **3589 marker positions, 940 quoted spans, 0 problems (0 undetected mutants)** — 21 pass-B
  and 21 pass-C lines all reading 0, 64 mutant FLAGGED, 0 MISSED.
- **Push state:** `origin/notes` at `3bf866361` (pushed 2026-10-08, the `math-ckd.2` batch: pages +
  regenerated ledger + this state carrier). Nothing unpushed.
- **Queue check (2026-10-08, after closing `math-ckd.2`):** `bd ready` lists 9 issues and **no P1**.
  P2: `math-el4.9` (el4.5 reading-band work — not started, user directive), `math-el4` (its parent),
  `math-u41` (blocked by the deferred `math-u41.6`), `math-7ur` (needs a go-ahead). P4: `math-ckd.5`,
  `math-ckd.6`, `math-ckd.3`, `math-ckd.4`, `math-ckd`. With the P2 line blocked by directives, the
  loop's next bead is `math-ckd.3`.
- **Batch findings (`math-ckd.2`), for reuse:**
  - **The dominant quotation failure is off-by-one at a range endpoint, because LaTeX source wraps
    sentences mid-line.** All 13 Pass-C failures on the 014 page were that shape: a quote whose last
    words sit on the line *below* the range end, or whose first words sit on the line *above* the range
    start. A range's haystack is the joined cited lines only, so both ends must be derived from the
    shipped file, never from a paragraph boundary you remember.
  - **A quotation needs a marker of its own.** Two quotes in one paragraph where only the second
    carries a marker leaves the first matched against the second's range, and it fails.
  - **`\cite[Theorem~1.1]{X}` is not stripped — copy it verbatim.** `norm()` deletes only
    `\cite{…}`; the bracket form survives, and the `Theorem~1.1` tilde blocks the
    "Theorem + number" strip rule, so writing `[Theorem] CT` can never match. Same for
    `\cite[Corollary~1.2]{X}`, `\cite[Sections~3--7]{X}`, `\cite[\S14.4.1]{X}`.
  - **Pass B checks only the two endpoints of a range for `BLANK`.** Sweep interiors yourself
    (`awk -v a=.. -v b=.. 'NR>=a && NR<=b && $0 ~ /^[[:space:]]*$/ {printf "%d ", NR}' file`); on this
    batch the interior hit was MS8 `introduction.tex:53` inside `[S39:36–69]`, which became
    `[S39:36–52]`.
  - **A manuscript that ships one self-contained driver with an inline `thebibliography` needs a
    driver row and a PDF row only** — no section rows, no separate bibliography row (family 014 MS 1,
    family 016 MS B). Record the convention rather than re-deriving it per page.
  - **Precomposed accents never match the LaTeX macro.** `Erdős` fails against source `Erd\H{o}s`;
    same for `Radziwi\l\l{}`, `Matom\"aki`, `Pa\v{s}k\=unas`, `F{\ae}rgeman`, `R\'emond`, `K\"uhne`.
    `CONTENTS.md` prose uses the precomposed form, the manuscript LaTeX uses the macro — quote each
    from its own source, verbatim.
  - **A `CONTENTS.md` blurb quoted as a block quote must be copied from the line, never
    reconstructed.** The 016 MS D blurb was written from memory as a paraphrase dressed as a quote;
    the symptom is `NO CITATION in unit`, and the only fix is to print the line and copy it.
  - PDF byte counts come from `find -printf '%s\t%p\n'`; `wc -l` on a PDF is meaningless. One figure
    in the 014 Sources table was stale by 2 bytes (MS5 `paper.pdf` is 574,527).
- **007 finding, for reuse:** the ledger's `paps_form`/`mainres` counts are 0 for a family that
  ships 854 Lean files with zero `sorry`, because `formalization.yaml` has no entry for the
  manuscript. Counts are YAML bibliography entries, not Lean source — never read them as "not
  formalized". 017 is the same shape: 0 and 0 beside 869 files and 94,948 lines. 087 is the same
  shape at partial scale: 2 of 3 and 3 of 4 beside 591 files and 81,233 lines. 159 is the same shape
  at scale: 0 and 0 beside 4,774 files and 1,122,983 lines.
- **017 findings, for reuse:**
  - A `[Sxx]` marker for a binary source (a trace PDF, a manuscript `paper.pdf`) inside a unit that
    carries a quotation makes Pass C read that file as text, and its non-text bytes decode to
    replacement characters, so the quotation reports `NOT VERBATIM` against a source whose text is not
    extractable. Pass C tries the cited sources in marker order and stops at the first hit, so a PDF
    row is safe only in a unit with no quotation, or listed after a text source that can match. Cite
    trace rows in the closing note. **A block quote inherits the markers of the line above it**, so a
    paragraph that cites a PDF and ends with the intro line for a block quote puts that PDF in the
    block quote's candidate list and reports `NOT VERBATIM`: keep the PDF citation in its own
    paragraph. Before `math-j0k.1` this same shape aborted the run with `UnicodeDecodeError`.
  - A quotation containing `<` is a hazard twice over: the raw-HTML scan matches `<...>`, and
    `norm()` deletes the same span, so the quote compares as mangled text. Put a space after `<`, or
    paraphrase. Check the source line for a `>` before quoting an inequality. Never write `<sub>`,
    `<sup>` or `<i>` in a page: render *r_k(N)* and (log *N*)^*ε_k* as plain markdown.
  - Quotes from `lean/docs/<NNN>.md` must keep that file's `$...$` delimiters. `norm()` leaves `$` and
    `\(`/`\)` intact, so rewriting one form as the other never matches.
  - A footnote quotation can end on the line that closes it (`}`), so the cited range must include
    that line.
  - A scope note's exclusion is about the comparator's *selected statement*, not the tree: 017's note
    excludes the Flint–Hills consequence, and `Main.lean` proves `flint_hills_summable` separately.
    Read the Lean tree before repeating an exclusion as a coverage gap — and check it the other way
    too; 017's generalized `a > max{1,b}` criterion really is absent.
- **087 findings, for reuse:**
  - A marker-only citation satisfies declare-or-cite, so a source whose content is paraphrased needs
    no quotation. 087 shipped 43 sources and 11 quoted spans (six block quotes, five inline) and
    passed Pass C on the first run.
  - In a unit with several markers, Pass C tries them in order and stops at the first match, so a
    quotation placed after an unrelated marker still verifies against the marker that can match it.
  - A verification bundle can name a file its driver reads that the release does not ship
    (`SOURCE-MANIFEST.json`, read at `reproduce.py:72`). State that as a source-level fact about the
    published bundle and say the bundle was not run; do not execute it.
  - Where a manuscript ships a proof with zero `sorry` and the release's YAML records no entry for it,
    write it as the index being behind, not as a coverage gap, and give both counts.
- **159 findings, for reuse:**
  - **A block quote is compared with its own delimiters included** (`pass_c` sets `spans = [unit]` for
    a block quote, and `norm()` does not strip `"`), so a block quote must be the raw source text with
    **no quote marks around it**. Inline quotes are fine — the `QUOTE` capture excludes delimiters.
  - **A block quote's citation belongs on the line exactly two above it** (intro line, blank line,
    quote). Attribution scans `start_line-2 … start_line-4` and takes the first line with usable
    markers; a marker on the wrong line attributes the quote to the wrong range.
  - **Quote a displayed formula with the delimiters the source uses.** `norm()` turns `\begin{equation}`
    into `equation` and `\begin{displaymath}` into `displaymath`, so `\[ … \]` never matches a source
    line pair that carries an `\begin{…}` — quote the environment, and cite the range that covers it.
  - Manuscript trees here put sections at `build/sections/…` and appendices at `build/foundations/…`;
    `README.md` exists at both the manuscript root and the repo root, so declare it with its full
    `preprints/…/README.md` path or the checker prints `AMBIGUOUS`.
  - The formalized quantitative statement can be **weaker** than the published one and still derive
    the headline conclusion: `Model.lean` states a saving in log log *N* with exponent 1 + *η*, where
    the manuscript's Theorem `ap:main` states a saving in (log *N*)^*ε_k*. Read the formalized `Prop`
    before repeating the manuscript's exponent as the formalized one.
  - Both companion columns come from the CONTENTS.md blurb alone (`build_catalog.py:274,295`), so a
    manuscript that names its companion in its introduction and bibliography can still have
    `companions` empty in the ledger. Say which layer the fact lives in.
- **197 findings, for reuse:**
  - **A marker written at the end of a block-quote line is invisible.** Attribution scans only
    `start_line-2 … start_line-4`, so the marker belongs on the intro line above the blank line;
    inside the quote it yields `NO CITATION in unit at doc line N`. Three of this page's three block
    quotes were written that way and all three needed the same fix — check marker placement before
    the first checker run, not after.
  - **Declare every path in a Sources row as a full repo-relative path, PDFs included.** A bare
    `paper.pdf` cell resolves only under the declared manuscript root, so trees 2–4 printed
    `FILE NOT ON DISK S22 -> paper.pdf`. The same trap covers `README.md` (`AMBIGUOUS`) and
    `build/main.tex` (collides across trees).
  - **Check the last line of every cited range is non-blank.** `[S4:73–81]` failed as
    `BLANK S4:81` because the paragraph ends at line 80 and line 81 is the blank separator.
  - A trace row is safe only in a unit with no quotation. Paraphrase the trace prompt (do not quote
    it) and put `[S36]` in that quote-free paragraph; the same paragraph can carry the file name as
    prose.
  - **The strongest coverage claim is a grep, not a scope-note restatement.** 197's scope note
    excludes the nonsofic conclusion; grepping `lean/OAI/RingTheory/DirectFiniteness/` for `sofic`,
    `surjunct` and `cellular` returns nothing, which turns the exclusion into a measured absence.
    Do the grep both ways: the odd-characteristic tree does prove its cellular-automaton claim, so
    of the family's two Gottschalk counterexamples exactly one is formalized.
  - When `mainres` < `chal`, find the mechanical cause before describing it: `KaplanskyDirectFiniteness`
    appears nowhere in `formalization.yaml`, which is why 4 challenges yield 3 `main_results` entries.
    Grep the YAML for the challenge config name.
  - Cost: 4 manuscripts → 36 sources, 181 markers, 57 quoted spans, green on the second checker run.
    A four-tree family with three Lean trees costs about the same as a one-manuscript family with a
    huge tree (159: 25 sources, 99 markers, 47 spans).
- **221 findings, for reuse:**
  - **A block-quote intro line carries exactly one marker.** `pass_c` loops over *every* candidate
    marker on the attributed line for *each* span, with no consuming pointer, so extra markers on the
    intro line are tried first and produce a false `NOT VERBATIM`. Split the paragraph so the intro
    line cites only the quoted range.
  - **`norm()` does not strip `$`.** A quotation from LaTeX source must carry the source's `$…$`
    delimiters verbatim; "the $b(S)$ branching depths" only matches with the dollars present.
  - Two of this page's six defects were **invented text** — the abstract and the trial-functional
    display. Print the shipped lines (`grep -n "" file | sed -n 'A,Bp'`) before writing a quotation; a
    paraphrase held in memory is not a quotation. Two more were off-by-one range starts, because these
    sources wrap sentences mid-line: derive every range from the shipped file.
  - **A File cell that resolves under both roots is a counted problem** (`AMBIGUOUS S2 (README.md)
    resolves under 2 roots`), and the manuscript copy is the one used (`self.table[sid] = hits[0]`,
    roots ordered `[manuscript, repo]`). No path form disambiguates a repo-root file that also exists
    in the manuscript root — `Path("./README.md")` normalizes to `README.md` — so 221's release
    `README.md` row stays deleted and its trace files carry the citation. Before `math-j0k.1` the
    line printed without being counted, so a page could report green with it.
  - The scope note for 221 states **no exclusions** (15 lines, contrast 197), so its coverage claims
    come from the tree. Grep the tree for the manuscript's corollary vocabulary: `Viana`, `Bray`,
    `SAT`, `soft`, `temperature`, `ground` return 0 files in `lean/OAI/Probability/DilutedSpin/`, so
    the formula is formalized and its three named corollaries are not.
  - Dependency direction is measurable and runs **from 221 to its companion 235**: 23 files of
    `lean/OAI/Probability/SATComputability/` import 17 distinct `DilutedSpin` modules, and
    `mezard_parisi` is imported nowhere in `OAI/`. That mirrors the manuscript's closing remark, which
    cites the companion's Theorem 8.4 for random 3-SAT.
  - 221's trace is the release's **only trace shipped as LaTeX**, so its reasoning is quotable text
    (211 lines; prompts 86–155, five sections). Its working bibliography — Barbier–Panchenko, Mourrat,
    Mourrat–Panchenko — appears nowhere in the manuscript's `references.bib`: a source-level fact about
    the trace, not about the published manuscript.
  - Cost: 1 manuscript (11 sections under `build/sections/`), 1 trace in two formats, 3 Lean trees →
    30 sources, 133 markers, 36 quoted spans, green on the third checker run.
- **271 findings, for reuse:**
  - **A formalized bound can be the manuscript's bound in disguise.** `Main.lean` states `(ℓ:ℝ)/8`
    where the manuscript states *S*/4; `Model.lean:55` is `abbrev Level (ℓ : ℕ) := Fin (ℓ + 1)`, so
    the site carries ℓ = 2*S* slots and ℓ/8 **is** *S*/4. Read the type encoding before calling a
    formal statement weaker than the paper's.
  - **The root manuscript is measurable from the bibliographies.** D's `references.bib` has 36 entries
    and zero `OAI:` self-citations; A, B and C each cite D by its `OAI:` href. Grep the `OAI:` hrefs
    across the family's trees: the manuscript nobody in the family cites is the root, and the dated
    directory names confirm it.
  - **A line-range marker on a binary source is legal; a quotation on it is not.** `lines_of` reads
    with `errors="replace"`, so the PDF's bytes become replacement characters and any quotation cited
    there reports `NOT VERBATIM`; a PDF row is safe only with whole-file markers `[Sn]`, in units that
    carry no quotation. 271's trace ships as PDF alone (no `.tex`), so its reasoning is not quotable at
    all. Before `math-j0k.1` this shape crashed the run inside `lines_of`.
  - **Two adjacent block quotes leave the second with no citation.** `pass_c` attributes a block quote
    from the lines at `start_line-2 … start_line-4`; a blank line plus the first quote fills that
    window, so the second quote reports `NO CITATION`. Merge them into one contiguous block quote and
    put one marker covering the whole joined range on the intro line — blank source lines collapse
    under `norm()`, so a joined two-paragraph quote verifies against a joined range.
  - `resolves_named` is 0 for 271 while manuscript D explicitly resolves **Lieb's 1999 Problem A**
    and says which formulation it resolves and which it does not. The ledger column is a keyword
    floor; read the manuscript before repeating it as a fact about the result.
  - `formalization.yaml` contains no `heisenberg` string, which is the mechanical cause of 271's
    `paps_form 0` / `mainres 0` beside 128 Lean files, 25,400 lines, zero `sorry`, 323 theorems.
  - Section-directory layout is not uniform: D keeps its sections under `build/source/sections/`,
    A/B/C under `build/sections/`. Confirm with `find` before writing a Sources path.
  - 271's trace cites six works absent from D's bibliography (Aizenman–Nachtergaele,
    Benjamini–Pemantle–Peres, Caputo–Liggett–Richthammer, Elboim–Sly, McBryan–Spencer, Ueltschi 2013)
    — a source-level fact about the trace, not about the published manuscript.
  - Cost: 4 manuscripts, 1 trace (PDF only), 1 Lean tree → 63 sources, 205 markers, 53 quoted spans,
    green on the third checker run. Four trees is the most expensive shape so far; a family with one
    manuscript costs about half the source rows.
- **287 findings, for reuse:**
  - **The adjacent-block-quote rule bites twice in one page.** Every block quote needs its own intro
    line carrying a marker that covers its whole range, because `pass_c` reads markers only from
    `start_line-2 … start_line-4`. 271's note says to merge; when the two quotes cite different
    sources, do not merge — insert an intro line two lines above the second quote
    (`The rank-three-to-infinite identification, from the formalization's own main file [S19:56–58]:`)
    and keep the quotes separate. Two sites, two intro lines, one checker run.
  - **A formalization can prove a strictly stronger rank step than the paper it mirrors.** The
    manuscript's Theorem 1.1 is the rank step for *n* ≥ 3 [S3:64–71] and reaches rank two only by
    amplifying at *t* = √2 with Dykema's formula *N_s^t* ≅ *N*_{1+(*s*−1)*t*⁻²} [S8:28–36]. The
    formalization proves `rank_step_ge_two` for *n* ≥ 2 (`FiniteRank.lean:143–145`, via
    `generating_haar_tuple_ge_two` at 122), so `rankTwo : L(𝔽₂) ≅ L(𝔽₃)` (147–148) is a direct
    instance and the amplification route is not needed for the headline. Check which route each side
    takes before describing the formalization as a transcription.
  - A scope note's exclusion is again about the *selected statement*: 287's note calls the
    fundamental-group conclusion "a further consequence rather than a separate selected statement"
    (`lean/docs/287.md:9`) while `allInterpolatedFundamentalGroups` (`Interpolation.lean:114–115`)
    proves `fundamentalGroup r = Set.Ioi 0`. Third family with this shape after 017 and 221.
  - **Vocabulary absence is the way to see an unformalized corollary.** Across 77 files / 26,804
    lines: `cocycle` 187, `semicircular` 114, and zero hits for `microstate`, `freeentropy`,
    `fisher`, `voiculescu`, `Catalan`, `entropy`. The free-entropy corollary — the part of the paper
    with independent content — is not formalized. Report the counts, not a conclusion about intent.
  - `formalization.yaml` (1,668 lines) has no entry naming the manuscript: the mechanical cause of
    `paps_form 0` / `mainres 0` beside 77 Lean files, 26,804 lines, zero `sorry`, 1,196 top-level
    `theorem`/`lemma` (395 + 801, counted with an anchored regex — a loose `\b(theorem|lemma)\b`
    overcounts by pulling prose).
  - The comparator challenge carries its own model: `InterpolatedFactors.lean` defines `Model.Algebra`,
    `Model.trace`, `Model.topology`, `parameterModel` (186–210) and `InterpolatedFactor` (212–214)
    before the challenge `allInterpolatedIsomorphic` (216–219), whose `sorry` sits in the challenge
    file. Count the challenge `sorry` separately from the tree's zero.
  - **A page with no quotation marks is proven by the block-quote mutant.** 287 carries zero `“ ” " ‘ ’`
    — all 25 of its Pass C spans are block quotes — which is why it is the page that exposed the gap.
    Mutant A scanned inline quotations only, so it printed `MISSED (no quotable span on one line)` and
    the TOTAL line read `(1 undetected mutants)`; that looked like a property of the page. `math-j0k.1`
    added A3 (corrupt a block-quote attribution) and A2 (a span wrapped across lines), so 287 reports
    `A3 corrupts a block-quote attribution: FLAGGED` with 0 undetected mutants. The gate is every
    present form FLAGGED, not "inline-only mutants are fine".
  - Cost: 1 manuscript (12 files, 17-entry bibliography, zero `OAI:` self-citations), 1 trace (PDF
    only, 11 pages), 1 Lean tree → 42 sources, 160 markers, 25 quoted spans, green on the second
    checker run. One manuscript is the cheapest shape in the batch.
- **362 findings, for reuse:**
  - **The comparator is the tree's own file with the proof deleted.**
    `lean/ComparatorChallenges/VlasovMaxwell.lean:10–101` is a verbatim copy of `Model.lean:13–104`,
    then the statement at 103–105 with `sorry` at 106. `Main.lean:44–48` proves that same statement in
    two lines, so 362's challenge gap is a copy, not a missing argument. Diff the comparator against
    the tree before describing a challenge as open.
  - **362 is the positive control for the evidence-column trap.** `formalization.yaml` *does* index
    it — bibliography entry at 392–395, `main_results` at 1642–1644 — which is why the ledger reads
    `paps_form 1` / `mainres 1`. Contrast 007, 017, 159, 271 and 287, all 0/0 beside large trees with
    zero `sorry`. A 1 in those columns means the YAML has a block, nothing more.
  - The analytic crux is a **sign**: the absolute force bound loses a factor √*w* (`dir:absolute`,
    `direct.tex:26–29`; the loss is named at `introduction.tex:174–177`), while a signed
    integration-by-parts identity (`can:weighted-formula`, `cancellation.tex:278–306`) plus direction
    control (`ang:direction`, `direction.tex:22–37`) recovers *w*^{-1/2} (`selection.tex:481`), so the
    weighted bound closes with no √*w* (`sel:bulk`, `selection.tex:449–452`).
  - The continuation argument is a **divergent sum of log-sized steps**: the signed increment
    |*V*(*t*₂) − *V*(*t*₁)| ≤ *MP*√Δ*t* + *A* Δ*t* *P*²*L*/*w* (`prop:increment`, `setup.tex:35–47`)
    makes the doubling gaps Δ*n* ≥ *c*/log(2 + 1024·2ⁿ) (`setup.tex:95–102`), whose sum diverges, so
    momentum cannot blow up at a finite time.
  - Concurrent work is explicitly disclaimed in the manuscript: Wang's July 2026 cylindrically
    symmetric pair is cited and then separated — "Thus the two data classes should not be
    identified." (`introduction.tex:134–136`). Quote it; do not merge the two results.
  - **A range marker must not end on a file's trailing blank line.** `[S2:1–18]` failed as
    `BLANK S2:18` because the manuscript `README.md` has 18 lines and line 18 is blank; the marker
    became `[S2:1–17]`. This is the same trap as 197's `[S4:73–81]`, one layer further out.
  - **A repo-level Sources row needs a full repo-relative File cell.** The trace row's short cell
    `relativistic-vlasov-maxwell.pdf` printed `FILE NOT ON DISK` — the checker resolves cells under
    the manuscript root and the repo root only. Applies to trace PDFs, `lean/…`, `notes/…` and
    `CONTENTS.md`; only files under the manuscript root may use a short cell. `README.md` is the same
    trap at the other root: bare `README.md` resolves under the manuscript root (18 lines) *and* the
    repo root (50), and `math-j0k.1` turned that collision into a counted problem, so the cell is now
    `preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/README.md`.
  - **A JSON string inside a block quote is an inline mutant target.** Mutant A1 scans the raw page
    text for a `"` span ≥ 12 characters, so 362's JSON block quote (`"challenge_module"`) gives it a
    target and this page has reported 0 undetected mutants all along — which is why the bead that found
    the gap named 362. Running 362 alone shows A1 FLAGGED; the missed mutant was never on this page.
  - Cost: 1 manuscript (16 files), 1 trace (PDF only, 6 pages, so not quotable), 1 Lean tree (207
    files / 89,993 lines) → 23 sources, 109 markers, 38 quoted spans, green on the second checker
    run. A one-manuscript family with a mid-size tree is the cheapest shape measured so far.

## Loop shape

One parent agent, sequential. **No subagents** — the box is a single GPU and switching context
per subagent turn costs more than the parallelism buys.

**No cron job.** This run is one-time, so continuation is human-driven: the next batch starts when
the user says so. The reason this file exists is context compaction, not unattended cadence — a
timer that fires mid-page is the failure mode, not the fix.

A batch is one bd issue. Per page, in this order:

1. `bd update <id> --claim` (once per batch).
2. `ls` the manuscript root before the page says what it ships.
3. Read the manuscript, the scope note, the YAML block, the challenge JSON, the trace if any.
4. Write the page in the format fixed by the `family-summary` skill.
5. Self-verify: every quotation against the lines it cites, every count against the file.
6. `python3 notes/scripts/verify_summaries.py --mutant` — zero problems, and every mutant form the
   page's quotation style can exercise printed FLAGGED.
7. Declare every Sources row, or delete it.
8. Regenerate the ledger; the `summary` column must flip to 1 for this family.
9. Commit.
10. `bd close <id> --reason "<outcome>"` at the end of the batch.

## Gates (run at every batch boundary, quote numbers only from this run)

```
python3 notes/scripts/build_catalog.py > /tmp/r1.txt && cp notes/catalog.tsv /tmp/c1.tsv
python3 notes/scripts/build_catalog.py > /tmp/r2.txt && cp notes/catalog.tsv /tmp/c2.tsv
diff /tmp/c1.tsv /tmp/c2.tsv && diff /tmp/r1.txt /tmp/r2.txt     # must be byte-identical
python3 notes/scripts/verify_summaries.py --mutant                # zero problems, zero undetected mutants
```

Reconciliation lines that must not move: 372 families, 722 manuscripts, 162 formalized,
405 challenges, 185 `main_results` entries over 178 configs, 235 scope notes, and both
`overview.tex` ↔ `CONTENTS.md` cross-checks reading 0. The discipline table must sum to
372 / 235 / 722 / 162.

## Commit and push boundaries

Commit when a batch's gates pass: explicit paths, one purpose per commit, never `--no-verify`, never
`git add -A`. The beads store travels in the commit whose work it records (the pre-commit hook
re-exports and stages it), so stage it with the code it describes.

**Push to `origin` (the fork) at a batch boundary, not on every commit** — authorized for this run on
2026-10-07. The cadence is a way of batching commits, not a timer: never idle or sleep to reach an
interval, and never push each commit as it lands. `upstream` is read-only; confirm the destination with
`git push --dry-run` when a push boundary lands on a batch you did not expect to publish.

## Stop and escalate

- **Stop the batch** when a gate fails twice on the same page. Two failures mean the checker or
  the format is wrong, not the page; fix that first, in its own commit.
- **Stop the run** when a P1/P2 issue becomes ready. Summaries are P4 and rank below them.
- **Never write an ungroundable page.** Record the family in `notes/summaries-blocked.md` with
  the specific reason (what the sources do not state) and leave its `summary` row 0.
- **Ambiguity:** record the decision point below with the provisional choice and what would force
  a revisit, then keep going. If it is critical, or fixing it later means rewriting pages,
  claim a different bead and come back.

## Tiers (measured from the ledger, 2026-10-07)

| Tier | Families | Manuscripts | Definition |
|---|---|---|---|
| A | 21 | 60 | 10 trace families, 9 headline T0 from `t0-triage.md`, plus 001 and 032 (done) |
| B | 83 | 124 | remaining T0 families with `resolves_named = 1` (80 / 120 under the abstract-only scope) |
| C | 268 | 538 | everything else, split into 131 families / 272 manuscripts (combinatorics, differential geometry, number theory, probability and statistical mechanics, theoretical computer science) and 137 families / 266 manuscripts (the remaining twelve) |

Trace families: 007, 017, 087, 102, 159, 197, 221, 271, 287, 362 (22 manuscripts).
Headline T0: 002, 004, 006, 010, 011, 014, 016, 018, 019 (29 manuscripts).
T0 is 137 families and 255 manuscripts, so tier C is 268 families: 137 − 11 (tier-A T0) − 83 (tier B)
+ 127 (T3) + 108 (T2) − 10 (trace families, all of them T2 or T3).

Tier B moved when `resolves_named` took the overview title into its input: the three T0 additions are
022 (number theory), 044 (algebraic and complex geometry) and 209 (algebra), which left tier C, so B is
83 / 124 and C is 268 / 538. The five-discipline split is named by the set that reproduces the
manuscript counts, not by size rank: the five largest C disciplines **by families** are theoretical
computer science 37, combinatorics 33, probability 27, mathematical physics 21, differential geometry
20, and that set is 138 families, not 131. The named five are the grouping the plan reads in, and the
list this page carried before (algebraic and complex geometry, number theory, combinatorics, topology,
differential geometry) reproduces neither the old 132 / 273 nor the new 131 / 272 — it is 89 / 156.

## What not to re-derive

- Page format, citation grammar, the repo-relative File cell, the block-quote rule, the
  PDF/quote rule: `.qwen/skills/auto-skill-family-summary-citation-verified/SKILL.md`.
- Cost model: 001 (1 manuscript → 15 sources, 173 markers, 9 quoted spans) and 032
  (8 manuscripts → 32 sources, 272 markers, 52 quoted spans). Sources ≈ 4 per manuscript.
  087 (3 manuscripts → 43 sources, 268 markers, 11 quoted spans): a three-tree family with a
  verification bundle and four challenges doubles the source count at the same manuscript count.
  159 (1 manuscript → 25 sources, 99 markers, 47 quoted spans): a single-manuscript family with a
  4,774-file Lean tree and a two-part trace costs as much as a multi-manuscript family, because the
  sources are the tree's entry points, not extra manuscripts. Block-quote-heavy pages raise the
  quoted-span count without raising the source count.
- `bd ready` is the only task tracker; nothing here is a task list.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.

## Decision points

Provisional choices, with what would force a revisit. Not tasks — a revisit that needs work gets
a bd issue.

- **History/Consequences depth.** Pages carry these only when grounded in the manuscript, the
  scope note, or the trace. A prior-based framing is labelled as a prior. Revisit if a page reads
  as empty; the fix is `math-el4.6`, not invention.
- **Tier C order within a batch.** Chosen by ascending manuscript count. Revisit if the small
  families turn out to be the expensive ones.
- **Companion families.** A page cites its companion by number and links the companion's page
  when one exists; it does not duplicate the companion's content. Revisit if cross-linking
  starts producing circular sources tables.
- **Dated re-issues** (`versions > 0`). One page per family; the Sources table lists the
  manuscript tree, not each dated copy. Revisit if a re-issued manuscript differs in content.
- **Cadence.** No cron job and no self-paced loop: the user drives continuation, because this is a
  one-time run and the stated concern is losing context to compaction, not stalling. Revisit if the
  run outgrows a sitting — then arm a prompt-only `/loop` whose prompt points here and stops when
  `bd ready` has no P4 issue.
