# Index link integrity — 66,107 links checked against the shipped files, 0 broken

Built 2026-10-07 by `notes/scripts/check_index_links.py` (report-only: it writes nothing and
exits non-zero if any link is broken). Every count below is from a fresh run of that script, of
`notes/scripts/build_catalog.py` (the canonical counts), and of `notes/scripts/build_index.py`
(the render-time report); the rule that yields each count is stated beside it. No `lake`, `lean`,
`lake exe cache get`, or comparator run.

**Headline, with the rule that yields it:** all 1,033 rendered index pages read from disk →
66,107 markdown links extracted with a paren-balanced target scanner, each resolved against its
page's directory → **0 broken**. Of those links, **17,700 resolve to a directory and 48,407 to a
file**. Every shipped-file category reconciles with a fresh `build_catalog.py` parse: 719
manuscript PDFs, 719 `build/` trees, 719 `README.md` stubs, 242 scope notes, 416 comparator
configs (JSON and Lean side by side), 192 Lean files named by `formalization.yaml` over 183
module dirs, 30 verification dirs, 10 reasoning-trace stems. `CONTENTS.md`, checked with the same
scanner in the same pass: 962 links, 720 of them `.pdf`, **0 broken**.

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

17,700 of the 66,107 links resolve to a directory. They are deliberate: the index links a
manuscript's LaTeX tree, a verification bundle, and a Lean module directory because those are
trees, not documents, and the index's job is to get a reader to the tree. The report separates
them per category and names them:

| Category | Links | Distinct targets | What it points at |
|---|---|---|---|
| `manuscript-dir` | 16,720 | 746 | `preprints/<dir>/` — the manuscript directory |
| `latex-build-tree` | 719 | 719 | `preprints/<dir>/build/` — the LaTeX source tree |
| `lean-dir` | 200 | 183 | the Lean module dir named by a `main_results` file path |
| `verification-dir` | 60 | 30 | `preprints/<dir>/verification/` — certificate bundles |
| `index-dir` | 1 | 1 | `notes/index/names/`, linked from the entry point |

The remaining 48,407 links resolve to files. `verification-dir` counts 60 links over 30 dirs
because each bundle is linked twice on family pages — once in the Manuscripts table, once in the
verification section — and the registry appends one of the two; `lean-dir` counts 200 links over
183 dirs because 14 dirs host more than one `main_results` declaration (max 3), and 6 files host
more than one (max 3), which is why 192 files sit in 183 dirs.

**`manuscript-dir` is the one category whose target count exceeds the canonical count: 746
linked of 719 shipped.** The 27 extra targets are directories the upstream merge superseded —
every one exists on disk, none is listed as a manuscript in `notes/subfindings.tsv`, and all 27
are reached only from name pages, by 1,100 links. The name layer is keyed by on-disk directory
names, so it reaches manuscript directories the release's own manuscript list no longer names.
The checker prints the count with its rule:

```
manuscript dirs linked outside the release set  27  on disk 27  links 1100
```

## Category table, reconciled with a fresh parse

From `python3 notes/scripts/check_index_links.py` (1,033 pages, 66,107 links, 0 broken):

| Category | Links | Targets | file | dir | canonical |
|---|---|---|---|---|---|
| `index-page` | 28,557 | 521 | 28,557 | 0 | — |
| `manuscript-dir` | 16,720 | 746 | 0 | 16,720 | 719 linked 746 of 719 |
| `manuscript-pdf` | 15,620 | 719 | 15,620 | 0 | 719 = canonical |
| `latex-build-tree` | 719 | 719 | 0 | 719 | 719 = canonical |
| `latex-source` | 719 | 719 | 719 | 0 | — |
| `manuscript-readme` | 719 | 719 | 719 | 0 | 719 = canonical |
| `config-json` | 705 | 416 | 705 | 0 | 416 = canonical |
| `notes-doc` | 577 | 26 | 577 | 0 | — |
| `index-table` | 553 | 1 | 553 | 0 | — |
| `config-lean` | 416 | 416 | 416 | 0 | 416 = canonical |
| `lean-file` | 289 | 192 | 289 | 0 | 192 = canonical |
| `scope-note` | 242 | 242 | 242 | 0 | 242 = canonical |
| `lean-dir` | 200 | 183 | 0 | 200 | 183 = canonical |
| `verification-dir` | 60 | 30 | 0 | 60 | 30 = canonical |
| `trace` | 10 | 10 | 10 | 0 | 10 = canonical |
| `index-dir` | 1 | 1 | 0 | 1 | — |

`= canonical` means the number of distinct targets the index links equals the number the release
ships, computed from a fresh parse — not from a previous run's output. Categories with no
canonical column are index-internal. `index-page` 521 targets = 372 family pages + 92 topic
pages + 17 discipline pages + 40 name pages, and the 40 name pages are linked only from the entry
point — family pages link no name page, the direction recorded in `notes/names.md`.
`latex-source` 719 = the `main_tex` of each of the 719 manuscripts, all 719 present in
`notes/sources.tsv`. `notes-doc` 26 targets = `notes/names.md` (552 links: one from each of the
551 name pages and one from the entry point), the 21 `notes/summaries/` pages family pages link,
and the 5 notes docs the entry point links (`index-design.md`, `names.md`, `topics.md`,
`topics.tsv`, `scripts/measure_names.py`). `index-table` 1 target = `notes/index/names.tsv`.

Traces: 10 stems attributed, 10 on disk, 0 unattributed. `reasoning_traces/` ships **11 files
over 10 stems** — the Mézard–Parisi trace ships as both `mezard-parisi-formula.pdf` and
`.tex` — and the index links the 10 `.pdf` files, so the `.tex` companion is on disk and
unlinked. `CONTENTS.md`'s 720 `.pdf` links are the 719 manuscript PDFs plus `overview.pdf`.

## Coverage: the disk scan is a superset of the render-time check

`build_index.py` checks its own links as it renders and reports **48,012 links checked, 0
broken** (fresh run). The disk scan finds **66,107 links, 0 broken**. The 18,095-link difference
is not a discrepancy about existence — both report zero — it is the render-time registry
under-covering the pages it writes. The registry appends one href per registered relationship
(an edge, a canonical file); the rendered bodies emit the same target again in other tables, and
they carry navigation links the registry never appends. Both sides are printed by the tools: the
checker counts scanned links per page group, and `build_index.py` prints registered links per
group and per category, classified by importing the checker's own `category`/`resolve` rule.
Attributed two ways, each summing to 18,095:

| Page group | Pages | Scanned | Registered | Gap |
|---|---|---|---|---|
| name pages | 551 | 57,888 | 40,899 | 16,989 |
| family pages | 372 | 6,712 | 5,763 | 949 |
| topic pages | 92 | 978 | 978 | 0 |
| discipline pages | 17 | 372 | 372 | 0 |
| entry point (`notes/index/README.md`) | 1 | 157 | 0 | 157 |

| Category | Scanned | Registered | Gap | Why |
|---|---|---|---|---|
| `index-page` | 28,557 | 12,521 | 16,036 | name pages link a family page in four tables (Families 9,819, the Manuscripts table's Family column 14,901, declaration and environment-title rows 986); the registry appends only the Families-table links, which are the 9,819 `family-name` edges. Family pages' 1,352 discipline/topic/companion links are all registered; the entry point's 149 are not registered at all. |
| `manuscript-dir` | 16,720 | 16,001 | 719 | the Manuscripts table on each family page links the manuscript directory; the registry registers the PDF, `build/`, `README.md`, and `main_tex` for that manuscript, not the directory row. |
| `notes-doc` | 577 | 21 | 556 | each of the 551 name pages links `notes/names.md`; the entry point links 5 notes docs. |
| `index-table` | 553 | 0 | 553 | each of the 551 name pages links `notes/index/names.tsv`; the entry point links 2 tables. |
| `config-json` | 705 | 505 | 200 | family pages link a config in the Configs table (416) and again in the `main_results` table (200 declarations); the registry appends the 416. Name pages' 89 are registered. |
| `verification-dir` | 60 | 30 | 30 | each bundle is linked twice in the bodies, registered once. |
| `index-dir` | 1 | 0 | 1 | the entry point's link to `names/`. |

Every other category has gap 0: scanned links equal registered links. So the render-time check is
a subset that passes; the disk check is the full set and also passes. The 18,095 surplus links are
all verified by the disk scan, and 16,989 of them (94%) sit on name pages, which is where the
tables repeat targets.

## Self-test

`python3 notes/scripts/check_index_links.py --mutant` injects 21 broken hrefs — one per
category the checker classifies, so a checker that only walks manuscript paths fails — and
requires 7 real hrefs to resolve. Fresh run: **21 injected, 21 caught, 0 missed; 7 controls, 7
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
  saying why. The reverse direction is safe and is used: `build_index.py` imports
  `check_index_links.py` (which has no module-scope work) so the registered-link counts it prints
  are classified by the same rule the disk scan uses, making the coverage gap measurable from two
  reports instead of from prose.
- **Counts are post-merge.** The upstream merge of 2026-10-08 changed the manuscript set (722 →
  719), the scope-note set (235 → 242), the config set (405 → 416), the `main_results` triples
  (185 → 200 over 189 configs), and the name layer (552 → 551 name pages); every figure above is
  from a run after it.

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
- **`overview.pdf` is inside the 720 `.pdf` links in `CONTENTS.md`** (719 manuscripts + 1). The
  checker reports the total, not the split; the split is stated here from the same run.
- **Only markdown link syntax is parsed.** A bare URL in angle brackets without `](`, an HTML
  `<a href>`, or a reference-style link `[text][ref]` would be invisible to the scanner; none are
  used by the generated pages, and no sweep confirmed their absence in `CONTENTS.md`.
- **The 27 superseded manuscript directories are not adjudicated.** The checker reports that the
  index links them and that they exist; nothing here decides whether the name layer should link
  directories the release's manuscript list no longer names.
