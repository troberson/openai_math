# Index link integrity — 65,690 links checked against the shipped files, 0 broken

Built 2026-10-07 by `notes/scripts/check_index_links.py` (report-only: it writes nothing and
exits non-zero if any link is broken). Every count below is from a fresh run of that script, of
`notes/scripts/build_catalog.py` (the canonical counts), and of `notes/scripts/build_index.py`
(the render-time report); the rule that yields each count is stated beside it. No `lake`, `lean`,
`lake exe cache get`, or comparator run.

**Headline, with the rule that yields it:** all 1,034 rendered index pages read from disk →
65,690 markdown links extracted with a paren-balanced target scanner, each resolved against its
page's directory → **0 broken**. Of those links, **16,818 resolve to a directory and 48,872 to a
file**. Every shipped-file category reconciles with a fresh `build_catalog.py` parse: 722
manuscript PDFs, 722 manuscript dirs, 722 `build/` trees, 722 `README.md` stubs, 235 scope notes,
405 comparator configs (JSON and Lean side by side), 180 Lean files named by
`formalization.yaml` over 172 module dirs, 30 verification dirs, 10 reasoning-trace stems.
`CONTENTS.md`, checked with the same scanner in the same pass: 958 links, 723 of them `.pdf`,
**0 broken**.

## The regex trap, and why the baseline is 0 broken links

One manuscript directory name contains parentheses:
`preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/` (family 337). A link
scan written as `\]\(([^)]*)\)` truncates that href, and the truncated target does not exist, so
a naive checker reports a broken link that the release does not contain. The scanner here walks
forward from `](` tracking paren depth and honours backslash escapes, so the balanced pair inside
the path is consumed. Measured on the line the family 337 page ships:

| Scanner | Target extracted | Exists |
|---|---|---|
| `[^)]*` | `../../../preprints/Sharp-integral-fillings-in-CAT(0` | no |
| paren-balanced | `../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf` | yes |

The baseline for any checker written against this corpus is **0 broken links, not 1**.
`python3 notes/scripts/check_index_links.py --mutant` prints both rows, so the trap stays
demonstrated rather than documented.

## A link to a directory is not a link to a file

16,818 of the 65,690 links resolve to a directory. They are deliberate: the index links a
manuscript's LaTeX tree, a verification bundle, and a Lean module directory because those are
trees, not documents, and the index's job is to get a reader to the tree. The report separates
them per category and names them:

| Category | Links | Distinct targets | What it points at |
|---|---|---|---|
| `manuscript-dir` | 15,850 | 722 | `preprints/<dir>/` — the manuscript directory |
| `latex-build-tree` | 722 | 722 | `preprints/<dir>/build/` — the LaTeX source tree |
| `lean-dir` | 185 | 172 | the Lean module dir named by a `main_results` file path |
| `verification-dir` | 60 | 30 | `preprints/<dir>/verification/` — certificate bundles |
| `index-dir` | 1 | 1 | `notes/index/names/`, linked from the entry point |

The remaining 48,872 links resolve to files. `verification-dir` counts 60 links over 30 dirs
because each bundle is linked twice on family pages — once in the Manuscripts table, once in the
verification section — and the registry appends one of the two; `lean-dir` counts 185 links over
172 dirs because 11 dirs host more than one `main_results` file (max 3).

## Category table, reconciled with a fresh parse

From `python3 notes/scripts/check_index_links.py` (1,034 pages, 65,690 links, 0 broken, 1.1 s):

| Category | Links | Targets | file | dir | canonical |
|---|---|---|---|---|---|
| `index-page` | 28,858 | 521 | 28,858 | 0 | — |
| `manuscript-dir` | 15,850 | 722 | 0 | 15,850 | 722 = canonical |
| `manuscript-pdf` | 15,850 | 722 | 15,850 | 0 | 722 = canonical |
| `latex-build-tree` | 722 | 722 | 0 | 722 | 722 = canonical |
| `latex-source` | 722 | 722 | 722 | 0 | — |
| `manuscript-readme` | 722 | 722 | 722 | 0 | 722 = canonical |
| `config-json` | 676 | 405 | 676 | 0 | 405 = canonical |
| `notes-doc` | 569 | 17 | 569 | 0 | — |
| `index-table` | 554 | 1 | 554 | 0 | — |
| `config-lean` | 405 | 405 | 405 | 0 | 405 = canonical |
| `lean-file` | 271 | 180 | 271 | 0 | 180 = canonical |
| `scope-note` | 235 | 235 | 235 | 0 | 235 = canonical |
| `lean-dir` | 185 | 172 | 0 | 185 | 172 = canonical |
| `verification-dir` | 60 | 30 | 0 | 60 | 30 = canonical |
| `trace` | 10 | 10 | 10 | 0 | 10 = canonical |
| `index-dir` | 1 | 1 | 0 | 1 | — |

`= canonical` means the number of distinct targets the index links equals the number the release
ships, computed from a fresh parse — not from a previous run's output. Categories with no
canonical column are index-internal. `index-page` 521 targets = 372 family pages + 92 topic
pages + 17 discipline pages + 40 name pages, and the 40 name pages are linked only from the entry
point — family pages link no name page, the direction recorded in `notes/names.md`.
`latex-source` 722 = the `main_tex` of each of the 722 manuscripts, all 722 present in
`notes/sources.tsv`. `notes-doc` 17 targets = `notes/names.md` (linked by all 552 name pages),
the 12 `notes/summaries/` pages family pages link, and the 5 notes docs the entry point links
(`index-design.md`, `names.md`, `topics.md`, `topics.tsv`, `scripts/measure_names.py`).
`index-table` 1 target = `notes/index/names.tsv`.

Traces: 10 stems attributed, 10 on disk, 0 unattributed. `reasoning_traces/` ships **11 files
over 10 stems** — the Mézard–Parisi trace ships as both `mezard-parisi-formula.pdf` and
`.tex` — and the index links the 10 `.pdf` files, so the `.tex` companion is on disk and
unlinked. `CONTENTS.md`'s 723 `.pdf` links are the 722 manuscript PDFs plus `overview.pdf`.

## Coverage: the disk scan is a superset of the render-time check

`build_index.py` checks its own links as it renders and reports **47,354 links checked, 0
broken** (fresh run). The disk scan finds **65,690 links, 0 broken**. The 18,336-link difference
is not a discrepancy about existence — both report zero — it is the render-time registry
under-covering the pages it writes. The registry appends one href per registered relationship
(an edge, a canonical file); the rendered bodies emit the same target again in other tables, and
they carry navigation links the registry never appends. Attributed two ways, each summing to
18,336:

| Page group | Scanned | Registered | Gap |
|---|---|---|---|
| name pages | 57,553 | 40,311 | 17,242 |
| family pages | 6,637 | 5,700 | 937 |
| topic pages | 971 | 971 | 0 |
| discipline pages | 372 | 372 | 0 |
| entry point (`notes/index/README.md`) | 157 | 0 | 157 |

| Category | Scanned | Registered | Gap | Why |
|---|---|---|---|---|
| `index-page` | 28,858 | 12,571 | 16,287 | name pages link a family page in four tables (Families 9,883, the Manuscripts table's Family column 15,128, declaration and environment-title rows 1,010); the registry appends only the Families-table links, which are the 9,883 `family-name` edges. Family pages' 1,345 discipline/topic/companion links are all registered. |
| `manuscript-dir` | 15,850 | 15,128 | 722 | the Manuscripts table on each family page links the manuscript directory; the registry registers the PDF, `build/`, `README.md`, and `main_tex` for that manuscript, not the directory row. |
| `notes-doc` | 569 | 12 | 557 | each of the 552 name pages links `notes/names.md`; the entry point links 5 notes docs. |
| `index-table` | 554 | 0 | 554 | each of the 552 name pages links `notes/index/names.tsv`; the entry point links 2 tables. |
| `config-json` | 676 | 491 | 185 | family pages link a config in the Configs table (405) and again in the `main_results` table (185); the registry appends the 405. |
| `verification-dir` | 60 | 30 | 30 | each bundle is linked twice in the bodies, registered once. |
| `index-dir` | 1 | 0 | 1 | the entry point's link to `names/`. |

So the render-time check is a subset that passes; the disk check is the full set and also passes.
The 18,336 surplus links are all verified by the disk scan, and 17,242 of them (94%) sit on name
pages, which is where the tables repeat targets.

## Self-test

`python3 notes/scripts/check_index_links.py --mutant` injects 20 broken hrefs — one per
category the checker classifies, so a checker that only walks manuscript paths fails — and
requires 6 real hrefs to resolve. Fresh run: **20 injected, 20 caught, 0 missed; 7 controls, 7
resolve** (exit 0). The self-test earned its keep on the first run, catching two real defects:

- `notes/index/names/` is a directory, and the classifier tagged it `index-table` because it
  sits under `notes/index/` and has no `.md` suffix. It is now its own category, `index-dir`,
  and is in the directory set — which is exactly the bead's "a link that resolves to a directory
  is not a link to a file" requirement, found by the checker's own test rather than by reading.
- Three entry-point mutants were written with hrefs that leave `notes/index/` (`../x`), so they
  resolved to `notes/` and classified as `notes-doc`. The mutants, not the checker, were wrong;
  they now use hrefs that stay in the category they claim to test.

## Recorded decisions

- **The checker is an independent re-derivation, not a re-run of the render-time check.** It
  parses the rendered markdown from disk and re-resolves every href, so a bug in the render-time
  registry (a link emitted in a body but never registered) shows up as coverage, not as silence.
- **Directory links stay, and are reported as directories.** The index links trees on purpose;
  the report states which categories resolve to directories instead of flattening them into
  "links".
- **Canonical counts come from a fresh parse in the same run** (`parse_contents`, `parse_docs`,
  `parse_challenges`, `parse_traces`, the ledger's `paps` column, the `main_results` triples read
  from `formalization.yaml`), never from a previous report.
- **`CONTENTS.md` is checked in the same pass** as the shipped-surface baseline, with the same
  paren-balanced scanner, so the two surfaces are measured by one rule.
- **`build_index.py` is not imported.** It calls `main()` at module scope, so importing it runs
  the 45-second build; the `main_results` triple pattern is carried in the checker with a comment
  saying why.

## Not checked

- **Link text is not judged against its target.** A cell labelled "PDF" that points at a `.tex`,
  or a link whose label names a different family than the page it opens, is a valid link to this
  checker. It checks existence and type, not semantics.
- **Fragments and URLs are skipped.** `#anchor` targets and scheme-prefixed hrefs are dropped
  before resolution, so intra-document anchors are not verified, and no external URL was fetched.
- **The 16 TSV tables are not link-checked.** Only markdown pages (`notes/index/**/*.md`) and
  `CONTENTS.md` are scanned; a path cell inside `manuscripts.tsv` or `edges/*.tsv` is not
  resolved.
- **Navigation reachability is not measured.** Every link resolving does not mean every page is
  reachable from the entry point; no graph traversal over the link set was done.
- **`reasoning_traces/mezard-parisi-formula.tex` is unlinked** by the index (the `.pdf` twin is
  linked). The file's existence is confirmed; nothing checks that a trace's `.tex` companion
  should be linked.
- **`overview.pdf` is inside the 723 `.pdf` links in `CONTENTS.md`** (722 manuscripts + 1). The
  checker reports the total, not the split; the split is stated here from the same run.
- **Only markdown link syntax is parsed.** A bare URL in angle brackets without `](`, an HTML
  `<a href>`, or a reference-style link `[text][ref]` would be invisible to the scanner; none are
  used by the generated pages, and no sweep confirmed their absence in `CONTENTS.md`.
