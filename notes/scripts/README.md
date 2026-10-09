# Scripts and generated files

Measured 2026-10-09 by `python3 notes/scripts/verify_script_ownership.py` — report-only, it writes
nothing, and every count below is re-derived by that run. The page answers one question: for each of
the **1,105** files under `notes/` (the scripts excluded), which is whose bytes. A generated file is
changed by editing its generator and re-rendering; a hand-written file is edited directly. Ownership
is per file, and the checker exits 1 on a file no rule owns.

## The split: 7 write, 36 write nothing

The writer set is derived from the scripts' own source, not from this page: a script is a writer when
a path constant rooted at `notes/` appears on the left of `.open(..., "w")` or `.write_text(...)`, plus
the tree case — a `notes/index` constant reached through the module's own `write()` helper. That rule
finds **7** writers over **43** scripts.

### Writers

| Script | Writes | Gate | Report feeds |
|---|---|---|---|
| `build_catalog.py` | `notes/catalog.tsv` | run twice, byte-identical | `notes/README.md`, `notes/findings.md` |
| `build_sources.py` | `notes/sources.tsv` | run twice, byte-identical | `notes/sources.md` |
| `build_index.py` | `notes/index/` | run twice, tree byte-identical | `notes/index-links.md` |
| `compare_abstracts.py` | `notes/abstracts.tsv` | `--tsv` only; run twice, byte-identical | `notes/abstracts.md` |
| `extract_formalization_deps.py` | `notes/formalization-deps.tsv` | run twice, byte-identical | `notes/dependency-drift.md` |
| `extract_links.py` | `notes/links.tsv` | run twice, byte-identical | `notes/links.md` |
| `extract_subfindings.py` | `notes/subfindings.tsv` | run twice, byte-identical | `notes/subfinding-pairs.md` |

Six writers emit one TSV each. `build_index.py` is the one-to-many case: it renders **1,049** files —
**1,033** `.md` pages and **16** `.tsv` tables. `compare_abstracts.py` is the conditional case: its
default run writes nothing and only `--tsv` touches `notes/abstracts.tsv`.

Writers import each other, so a generated file's bytes are not a function of one script.
`build_index.py` imports `build_catalog`, `measure_topics` and `measure_names`;
`build_sources.py`, `extract_links.py`, `extract_subfindings.py`, `compare_abstracts.py`,
`check_index_links.py`, `measure_names.py` and `measure_topics.py` all import `build_catalog`;
`measure_index_sizes.py` imports `check_index_links` inside its link-check function
(`measure_index_sizes.py:116`), not at module scope. Counted over `notes/scripts/*.py`,
`build_catalog.py` has **22** importers, `build_sources.py` **2** (`verify_sources.py`,
`read_manuscript.py`) and `verify_summaries.py` **4** (`verify_findings.py` and
`verify_scope_exclusions.py` for its `norm()`, `locate_summary_quotes.py` and
`refresh_summary_line_counts.py`). Editing a join in `build_catalog.py` can move
rows in six artifacts.

### Report-only

The other **36** scripts write nothing. **18** of them print the report a page's counts come from:

| Script | Report feeds |
|---|---|
| `check_index_links.py` | `notes/index-links.md` |
| `check_summary_manuscripts.py` | `notes/summaries/` — which manuscripts each page reads, and whether the release still names them |
| `extract_citations.py` | `notes/citations.md` |
| `extract_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` |
| `extract_named_results.py` | `notes/named-results.md` |
| `extract_scope_notes.py` | `notes/scope-exclusions.md` |
| `extract_subfinding_pairs.py` | `notes/subfinding-pairs.md` |
| `extract_t0_chains.py` | `notes/t0-chains.md` |
| `extract_verification_348.py` | `notes/verification-dirs.md` |
| `extract_verification_dirs.py` | `notes/verification-dirs.md` |
| `locate_summary_quotes.py` | `notes/summaries/` — the lines a page should cite when a quotation stops matching |
| `measure_index_sizes.py` | `notes/index-design.md` |
| `measure_names.py` | `notes/names.md` |
| `measure_proof_density.py` | `notes/proof-density.md` |
| `measure_topics.py` | `notes/topics.md` |
| `read_manuscript.py` | none — a reading aid; prints a manuscript's abstract, section skeleton and titled statement environments with `file:line` anchors |
| `refresh_summary_line_counts.py` | `notes/summaries/` — rewrites the `Lines` column of the Sources table in every page |
| `triage_t0.py` | `notes/t0-triage.md` |

`check_index_links.py` is the link checker for `notes/index/` and `CONTENTS.md` — it reads the tree and
writes nothing, so it sits here rather than in the checker table, which lists scripts that verify a
page's text.

### Checkers

The remaining **18** scripts verify a page or a table. Each exits non-zero when what it checks has
drifted; each takes `--mutant`, which injects faults and asserts they are caught.

| Checker | Checks |
|---|---|
| `verify_abstracts.py` | `notes/abstracts.md` |
| `verify_citations.py` | `notes/citations.md` |
| `verify_conditional.py` | `notes/conditional.md` |
| `verify_conjecture_standing.py` | `notes/conjecture-standing.tsv` |
| `verify_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` |
| `verify_dependency_drift.py` | `notes/dependency-drift.md`, `notes/formalization-deps.md` |
| `verify_findings.py` | `notes/findings.md` |
| `verify_index_design.py` | `notes/index-design.md` |
| `verify_named_conjectures.py` | `notes/named-conjectures.md` |
| `verify_named_results.py` | `notes/named-results.md` |
| `verify_scope_exclusions.py` | `notes/scope-exclusions.md` |
| `verify_sources.py` | `notes/sources.md` |
| `verify_subfinding_pairs.py` | `notes/subfinding-pairs.md` |
| `verify_subfindings.py` | `notes/subfindings.tsv` |
| `verify_summaries.py` | `notes/summaries/` |
| `verify_t0_chains.py` | `notes/t0-chains.md` |
| `verify_upstream_history.py` | `upstream_history/` — the three pages, outside `notes/` |
| `verify_verification_dirs.py` | `notes/verification-dirs.md` |

`verify_script_ownership.py` — this page's own checker — is not in the table: a checker cannot list
itself as its input. It is the 19th checker and the 44th script the run counts.

## The shared package: `catlib/`

`notes/scripts/catlib/` holds the joins the extractors share, so a join is written once. It is 9
modules, not scripts: `paths.py` (the repo-root constants, `rel()`, `owner()`, `read_text()`),
`tsv.py` (the four TSV writer shapes), `overview.py` (the `\resultentry` parse), `ledger.py`
(`notes/catalog.tsv` and the claim-shape rules), `preprints.py` (the 749 dirs versus the 719 listed
manuscripts), `text.py` (the six normalizers), `yaml.py` (`main_results_entries()`, the scope-note
spans, the Lean-tree file list), `anchors.py` (the `path:line` anchor grammar, the fenced-block scan
and the nearest-preceding-anchor read the page checkers share) and `__init__.py`. A script run as
`python3 notes/scripts/foo.py` has `notes/scripts` on `sys.path`, so it imports them as
`from catlib import ...` with no path boilerplate.

**22** of the **44** scripts call the package: **5** `extract_`, **3** `build_`, **2** `measure_`,
`check_index_links.py`, `read_manuscript.py`, and **10** of the **19** checkers. The other **9**
checkers are ported by `math-lon.2`'s remaining sub-beads, which is also where the **26**
`duplicate-code` findings go — measured 2026-10-09 with `--enable=R0801` over 53 files, every
cluster now reported against `catlib/anchors.py` (see `notes/linting.md`). Two joins deliberately
stay outside the package: `verify_upstream_history.py` reads `lean/formalization.yaml` through
`git show <rev>:` (a history read), and `build_index.py` keeps its own `TRIPLE` regex.

The package is not in the census below: the script population is `notes/scripts/*.py`, and
`catlib/` is 9 modules under that directory, counted as **53** source files by the lint gate in
`notes/linting.md`.

## The file census

| Population | Files | Owner |
|---|---|---|
| `notes/index/` | **1,049** | generated — `build_index.py` |
| `notes/summaries/` | **21** | hand-written — the reading record |
| `notes/*.tsv` | **8** | **6** generated, **2** hand-authored |
| `notes/*.md` | **27** | hand-written — **15** with a checker, **12** without |
| `notes/` total, scripts excluded | **1,105** | — |

The generated TSVs are the six writer targets. The two hand-authored tables are:

| Table | Why it is hand-authored |
|---|---|
| `notes/topics.tsv` | The curated topic vocabulary. `measure_topics.py --check` re-measures its 92 rows and exits 1 when a recorded count drifts; `build_index.py` reads it and renders `notes/index/topics-rendered.tsv`. A generated file inside `notes/index/` is overwritten by the next render, which is why the vocabulary lives above that tree. |
| `notes/conjecture-standing.tsv` | The training-data prior. Its `standing_prior_2025` column is the assistant's memory at an early-2025 cutoff, self-rated by `prior_confidence`; no script can derive a memory, and `verify_conjecture_standing.py` checks the rows against the ledger and `overview.tex` rather than regenerating them. |

The 12 pages with no checker are `notes/README.md`, `notes/conjecture-standing.md`,
`notes/counterexample-tag.md`, `notes/index-links.md`, `notes/links.md`, `notes/linting.md`,
`notes/names.md`, `notes/proof-density.md`, `notes/resolution-tag.md`, `notes/summaries-workflow.md`,
`notes/t0-triage.md` and `notes/topics.md`. Their counts are reproduced by the report-only scripts
above; nothing verifies them against the page. `notes/linting.md` is the one page in that set whose
counts come from tools outside this tree — the three linter commands it names, run from the untracked
`.venv/`.

## One basename is shared

Measured over the top level and the index tree: **1** shared basename — `README.md`.
`notes/README.md` is the ledger readme and `notes/index/README.md` is the index entry point, so that
pair is harmless.

The tree used to carry a second, load-bearing collision. `notes/topics.tsv` is the hand-authored
vocabulary and `notes/index/topics.tsv` was generated from it, with adjacent schemas —
`term pattern fams title abstract scope path status` in both, then `note` in the hand-authored file
and `page` in the rendered one — so a reference to `topics.tsv` without its directory was ambiguous,
and a `notes/**/topics.tsv` glob read both. The rendered table is now
`notes/index/topics-rendered.tsv`, which says which layer it measures; the vocabulary's path is
unchanged, and `measure_topics.py` and `AGENTS.md` both name it. `build_index.py` reads the top-level
file and writes the rendered one.

The index tree and the summaries tree share **13** page slugs — the families that carry both a rendered
page and a reading summary, which is the pairing the index reports.

`notes/index/` is excluded from prettier for this reason and the byte-exactness contract:
`.prettierignore` names the tree with the instruction to edit `build_index.py` and re-render, and
excludes the checker-verified pages, allowing formatting only on the pages no checker parses.

## Naming coverage

`notes/README.md`'s command block named **34** of the 43 scripts before this pass. Nine are named
nowhere in the repo at the pinned baseline: `check_summary_manuscripts.py`, `extract_citations.py`,
`locate_summary_quotes.py`, `read_manuscript.py`, `refresh_summary_line_counts.py`,
`verify_citations.py`, `verify_findings.py`, `verify_named_conjectures.py` and
`verify_upstream_history.py`. The first four are the `notes/summaries/` reading tooling and the
citation extractor, so the summaries tree and `notes/citations.md` carried measurements whose
generating command no document named; `verify_citations.py`, `verify_findings.py` and
`verify_named_conjectures.py` are the checkers for `notes/citations.md`, `notes/findings.md` and
`notes/named-conjectures.md`, so three pages carried measurements whose checker no document named;
the last is the tooling behind `upstream_history/`, the pages that record each upstream merge, which
sit outside `notes/` and so outside this page's census. All 43 are named here and in the command
block. "Before this pass" is
pinned to the commit that created this page, read at its parent, not to `HEAD`: `HEAD` moves every
time this page is edited, so a check keyed to it re-pins the baseline on each edit, and the naming
that pass added then reads as already present and the recorded gap vanishes.

## Not checked

- **The checker proves ownership, not byte-sync.** Nothing asserts that a file under `notes/index/`
  equals what `build_index.py` currently renders. That proof is the manual discipline — run the
  generator twice, diff, and diff against `HEAD`. A hand-edit to a rendered page survives until a
  checker's needle happens to break.
- `build_index.py` sweeps its own tree: it tracks every path its `write()` helper emits and, at the end
  of `main()`, unlinks any `notes/index/**.md` or `**.tsv` it did not write, then removes empty
  directories and prints `stale swept N files [...]`. The realized case is the 2026-10-07 merge: family
  032's title changed, so its old-slug page survived as an orphan whose manuscript table pointed at the
  three withdrawn directories — 6 broken links, found only by `check_index_links.py`. Two name pages
  (`cech`, `kunneth`) went the same way; the sweep removed 3 files. Renaming the rendered topic table is
  the older case — `notes/index/topics.tsv` survived the rename and was deleted by hand. Page counts are
  measured consistent: **1,033** `.md` on disk against the **1,033** the render report claims.
- The idempotence gate for `build_index.py` is run 2 against run 3, not run 1 against run 2: the first
  run after a corpus change prints the sweep line with the files it removed, the second prints
  `stale swept 0 files []`. Diffing run 1 against run 2 reports the sweep as drift.
- The writer rule reads path constants and write calls. A write built from a computed path (a variable
  assembled at runtime) is not found by it, and `refresh_summary_line_counts.py` is the realized case:
  it resolves each page path through `verify_summaries.Page` and rewrites the `Lines` column of every
  page under `notes/summaries/`, so the rule files it under report-only and the census row calls that
  tree hand-written. The tree is hand-written in what it says and script-touched in that one column.
- The report-only table records which page a report feeds as stated in that page and in `AGENTS.md`.
  It is not derived from the report text, so a page that stops quoting a report keeps its row here.
- Nothing in `lean/` is built, so no generated artifact here is a verification of a formalization.
