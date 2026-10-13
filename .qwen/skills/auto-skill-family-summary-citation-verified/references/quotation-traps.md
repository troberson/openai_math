# Quotation and citation traps, measured on the shipped pages

Each bullet is a defect a real page produced and the checker caught, with the fix that closed it.
Moved from `notes/development/summaries-workflow.md` on 2026-10-12: the state carrier carries state, the method
lives here. The family number names the page the trap came from.

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
  - Both companion columns come from the CONTENTS.md blurb alone (`build_catalog.py:116,117`), so a
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

