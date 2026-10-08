# Scripts and generated files

Measured 2026-10-08 by `python3 notes/scripts/verify_script_ownership.py` — report-only, it writes
nothing, and every count below is re-derived by that run. The page answers one question: for each of
the **1,105** files under `notes/` (the scripts excluded), which is whose bytes. A generated file is
changed by editing its generator and re-rendering; a hand-written file is edited directly. Ownership
is per file, and the checker exits 1 on a file no rule owns.

## The split: 7 write, 31 write nothing

The writer set is derived from the scripts' own source, not from this page: a script is a writer when
a path constant rooted at `notes/` appears on the left of `.open(..., "w")` or `.write_text(...)`, plus
the tree case — a `notes/index` constant reached through the module's own `write()` helper. That rule
finds **7** writers over **38** scripts.

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

Six writers emit one TSV each. `build_index.py` is the one-to-many case: it renders **1,050** files —
**1,034** `.md` pages and **16** `.tsv` tables. `compare_abstracts.py` is the conditional case: its
default run writes nothing and only `--tsv` touches `notes/abstracts.tsv`.

Writers import each other, so a generated file's bytes are not a function of one script.
`build_index.py` imports `build_catalog`, `measure_topics` and `measure_names`;
`build_sources.py`, `extract_links.py`, `extract_subfindings.py`, `compare_abstracts.py`,
`check_index_links.py`, `measure_names.py` and `measure_topics.py` all import `build_catalog`;
`measure_index_sizes.py` imports `check_index_links`. Editing a join in `build_catalog.py` can move
rows in six artifacts.

### Report-only

The other **31** scripts write nothing. **14** of them print the report a page's counts come from:

| Script | Report feeds |
|---|---|
| `check_index_links.py` | `notes/index-links.md` |
| `extract_citations.py` | `notes/citations.md` |
| `extract_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` |
| `extract_named_results.py` | `notes/named-results.md` |
| `extract_scope_notes.py` | `notes/scope-exclusions.md` |
| `extract_subfinding_pairs.py` | `notes/subfinding-pairs.md` |
| `extract_t0_chains.py` | `notes/t0-chains.md` |
| `extract_verification_348.py` | `notes/verification-dirs.md` |
| `extract_verification_dirs.py` | `notes/verification-dirs.md` |
| `measure_index_sizes.py` | `notes/index-design.md` |
| `measure_names.py` | `notes/names.md` |
| `measure_proof_density.py` | `notes/proof-density.md` |
| `measure_topics.py` | `notes/topics.md` |
| `triage_t0.py` | `notes/t0-triage.md` |

`check_index_links.py` is the link checker for `notes/index/` and `CONTENTS.md` — it reads the tree and
writes nothing, so it sits here rather than in the checker table, which lists scripts that verify a
page's text.

### Checkers

The remaining **17** scripts verify a page or a table. Each exits non-zero when what it checks has
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
| `verify_verification_dirs.py` | `notes/verification-dirs.md` |

`verify_script_ownership.py` — this page's own checker — is not in the table: a checker cannot list
itself as its input. It is the 18th checker and the 39th script the run counts.

## The file census

| Population | Files | Owner |
|---|---|---|
| `notes/index/` | **1,050** | generated — `build_index.py` |
| `notes/summaries/` | **21** | hand-written — the reading record |
| `notes/*.tsv` | **8** | **6** generated, **2** hand-authored |
| `notes/*.md` | **26** | hand-written — **15** with a checker, **11** without |
| `notes/` total, scripts excluded | **1,105** | — |

The generated TSVs are the six writer targets. The two hand-authored tables are:

| Table | Why it is hand-authored |
|---|---|
| `notes/topics.tsv` | The curated topic vocabulary. `measure_topics.py --check` re-measures its 92 rows and exits 1 when a recorded count drifts; `build_index.py` reads it and renders `notes/index/topics.tsv`. A generated file inside `notes/index/` is overwritten by the next render, which is why the vocabulary lives above that tree. |
| `notes/conjecture-standing.tsv` | The training-data prior. Its `standing_prior_2025` column is the assistant's memory at an early-2025 cutoff, self-rated by `prior_confidence`; no script can derive a memory, and `verify_conjecture_standing.py` checks the rows against the ledger and `overview.tex` rather than regenerating them. |

The 11 pages with no checker are `notes/README.md`, `notes/conjecture-standing.md`,
`notes/counterexample-tag.md`, `notes/index-links.md`, `notes/links.md`, `notes/names.md`,
`notes/proof-density.md`, `notes/resolution-tag.md`, `notes/summaries-workflow.md`,
`notes/t0-triage.md` and `notes/topics.md`. Their counts are reproduced by the report-only scripts
above; nothing verifies them against the page.

## Two basenames are shared

Measured over the top level and the index tree: **2** shared basenames — `README.md` and `topics.tsv`.
`notes/README.md` is the ledger readme and `notes/index/README.md` is the index entry point, so that
pair is harmless. The TSV pair is the load-bearing one: `notes/topics.tsv` is the hand-authored
vocabulary and `notes/index/topics.tsv` is generated from it, and the schemas are adjacent —
`term pattern fams title abstract scope path status` in both, then `note` in the hand-authored file and
`page` in the rendered one — so a reference to `topics.tsv` without its directory is ambiguous, and a
`notes/**/topics.tsv` glob reads both. `measure_topics.py` reads the top-level file; `build_index.py`
reads the top-level file and writes the rendered one. Renaming the rendered file to
`topics-rendered.tsv` removes the ambiguity without touching the vocabulary, whose path
`measure_topics.py` and `AGENTS.md` both name.

The index tree and the summaries tree share **13** page slugs — the families that carry both a rendered
page and a reading summary, which is the pairing the index reports.

`notes/index/` is excluded from prettier for this reason and the byte-exactness contract:
`.prettierignore` names the tree with the instruction to edit `build_index.py` and re-render, and
excludes the checker-verified pages, allowing formatting only on the pages no checker parses.

## Naming coverage

`notes/README.md`'s command block named **34** of the 38 scripts before this pass. Four were named
nowhere in the repo — not in `notes/README.md` and not in `AGENTS.md`: `extract_citations.py`,
`verify_citations.py`, `verify_findings.py`, `verify_named_conjectures.py`. They are the tooling behind
`notes/citations.md`, `notes/findings.md` and `notes/named-conjectures.md`, so three pages carried
measurements whose generating command no document named. All 38 are named here and in the command
block.

## Not checked

- **The checker proves ownership, not byte-sync.** Nothing asserts that a file under `notes/index/`
  equals what `build_index.py` currently renders. That proof is the manual discipline — run the
  generator twice, diff, and diff against `HEAD`. A hand-edit to a rendered page survives until a
  checker's needle happens to break.
- `build_index.py` never deletes: it `mkdir`s and writes, with no `unlink`. A changed page slug leaves
  the old page on disk. Measured consistent now — **1,034** `.md` on disk against the **1,034** the
  render report claims — so this is latent, not realized.
- The writer rule reads path constants and write calls. A write built from a computed path (a variable
  assembled at runtime) would not be found by it.
- The report-only table records which page a report feeds as stated in that page and in `AGENTS.md`.
  It is not derived from the report text, so a page that stops quoting a report keeps its row here.
- Nothing in `lean/` is built, so no generated artifact here is a verification of a formalization.
