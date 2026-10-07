# Summary-page production loop

The resume protocol for the `math-ckd` batches. Read this after a compaction; it is the state
carrier, so it states what to do and what not to re-derive.

## Current state (rewritten at every batch boundary)

- **Batch:** `math-ckd.1`, claimed — the 10 trace families (007, 017, 087, 102, 159, 197, 221, 271,
  287, 362), 22 manuscripts. Close it with `bd close math-ckd.1 --reason "<outcome>"` when the tenth
  page is committed.
- **Pages done:** 102 (`notes/summaries/theoretical-computer-science/`), 001, 007, 017
  (`notes/summaries/number-theory/`), 032 (`notes/summaries/algebraic-and-complex-geometry/`), 087
  (`notes/summaries/convex-and-metric-geometry/`), 159 (`notes/summaries/combinatorics/`), 197
  (`notes/summaries/algebra/`), 221 (`notes/summaries/probability-and-statistical-mechanics/`), 271
  (`notes/summaries/mathematical-physics/`). The ledger's `summary` column is 1 for those ten; the
  generator reports "summary pages 10 of 372 families, 29 manuscripts behind them".
- **Next page:** family **287**. Steps 2–9 above, in order.
- **Last gate run (2026-10-07):** regeneration byte-identical on two runs; 372 families, 722
  manuscripts, 162 formalized, 405 challenges, 185 `main_results` over 178 configs, 235 scope notes,
  both cross-checks 0, discipline table summing 372 / 235 / 722 / 162; `verify_summaries.py --mutant`
  over 10 pages → 1850 marker positions, 378 quoted spans, 0 problems, 0 undetected mutants.
- **Push state:** `origin/notes` at 29169d579 (pushed 2026-10-07 07:48); local `notes` HEAD is
  f3c5293d8. Push when an hour has passed since the last push, not per commit.
- **007 finding, for reuse:** the ledger's `paps_form`/`mainres` counts are 0 for a family that
  ships 854 Lean files with zero `sorry`, because `formalization.yaml` has no entry for the
  manuscript. Counts are YAML bibliography entries, not Lean source — never read them as "not
  formalized". 017 is the same shape: 0 and 0 beside 869 files and 94,948 lines. 087 is the same
  shape at partial scale: 2 of 3 and 3 of 4 beside 591 files and 81,233 lines. 159 is the same shape
  at scale: 0 and 0 beside 4,774 files and 1,122,983 lines.
- **017 findings, for reuse:**
  - A `[Sxx]` marker for a binary source (a trace PDF, a manuscript `paper.pdf`) inside a unit that
    carries a quotation makes Pass C read that file as text and crash on `UnicodeDecodeError`. Pass C
    tries the cited sources in marker order and stops at the first hit, so a PDF row is safe only in
    a unit with no quotation, or listed after a text source that can match. Cite trace rows in the
    closing note. **A block quote inherits the markers of the line above it**, so a paragraph that
    cites a PDF and ends with the intro line for a block quote puts that PDF in the block quote's
    candidate list and crashes: keep the PDF citation in its own paragraph.
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
  - **`AMBIGUOUS` is printed, not counted, and the manuscript copy wins** (`self.table[sid] =
    hits[0]`, roots ordered `[manuscript, repo]`). No path form disambiguates a repo-root file that
    also exists in the manuscript root — `Path("./README.md")` normalizes to `README.md`. The release
    `README.md` therefore cannot be a declared source row; delete it and cite the trace files.
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
  - **A line-range marker on a binary source crashes the checker** — `UnicodeDecodeError` in
    `lines_of`. A PDF row is legal only with whole-file markers `[Sn]`, and only in units that carry
    no quotation. 271's trace ships as PDF alone (no `.tex`), so its reasoning is not quotable at all.
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
6. `python3 notes/scripts/verify_summaries.py --mutant` — green, zero problems.
7. Declare every Sources row, or delete it.
8. Regenerate the ledger; the `summary` column must flip to 1 for this family.
9. Commit.
10. `bd close <id> --reason "<outcome>"` at the end of the batch.

## Gates (run at every batch boundary, quote numbers only from this run)

```
python3 notes/scripts/build_catalog.py > /tmp/r1.txt && cp notes/catalog.tsv /tmp/c1.tsv
python3 notes/scripts/build_catalog.py > /tmp/r2.txt && cp notes/catalog.tsv /tmp/c2.tsv
diff /tmp/c1.tsv /tmp/c2.tsv && diff /tmp/r1.txt /tmp/r2.txt     # must be byte-identical
python3 notes/scripts/verify_summaries.py --mutant                # zero problems
```

Reconciliation lines that must not move: 372 families, 722 manuscripts, 162 formalized,
405 challenges, 185 `main_results` entries over 178 configs, 235 scope notes, and both
`overview.tex` ↔ `CONTENTS.md` cross-checks reading 0. The discipline table must sum to
372 / 235 / 722 / 162.

## Commit and push boundaries

Commit when a batch's gates pass: explicit paths, one purpose per commit, never `--no-verify`, never
`git add -A`. The beads store travels in the commit whose work it records (the pre-commit hook
re-exports and stages it), so stage it with the code it describes.

**Push to `origin` (the fork) about once per hour**, not on every commit — authorized for this run on
2026-10-07. `upstream` is read-only; confirm the destination with `git push --dry-run` when a push
boundary lands on a batch you did not expect to publish.

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
| B | 80 | 120 | remaining T0 families with `resolves_named = 1` |
| C | 271 | 542 | everything else, split into 132 families / 273 manuscripts (five largest disciplines: algebraic and complex geometry, number theory, combinatorics, topology, differential geometry) and 139 families / 269 manuscripts (the remaining twelve) |

Trace families: 007, 017, 087, 102, 159, 197, 221, 271, 287, 362 (22 manuscripts).
Headline T0: 002, 004, 006, 010, 011, 014, 016, 018, 019 (29 manuscripts).
T0 is 137 families and 255 manuscripts, so tier C is 271 families: 137 − 11 + 127 + 108 − 10.

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
