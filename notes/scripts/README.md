# Scripts and generated files

Measured 2026-10-11 by `python3 notes/scripts/verify_script_ownership.py` — report-only, it writes
nothing, and every count below is re-derived by that run. The page answers one question: for each of
the **1,253** files under `notes/` (the scripts excluded), which is whose bytes. A generated file is
changed by editing its generator and re-rendering; a hand-written file is edited directly. Ownership
is per file, and the checker exits 1 on a file no rule owns.

It is also the script inventory. Every script under `notes/scripts/` is listed once, in one of three
classes — writer, report-only, checker — with what it writes and the command the gate runs for it, and
the fourth class, the scratch a session writes outside the tree, is recorded by rule rather than by
file. The classes partition the **74** scripts: **21** writers, **30** report-only, **23** checkers,
and `verify_script_ownership.py` itself, which is the 23rd checker and is not listed in its own table.

## The split: 21 write, 53 write nothing

The writer set is derived from the scripts' own source, not from this page: a script is a writer when
a path constant rooted at `notes/` appears on the left of `.open(..., "w")` or `.write_text(...)`,
plus the tree case — a `notes/index` constant reached through the module's own `write()` helper — and
plus one hop: a receiver built from a module constant (`out = TPL_DIR / (name)`, then
`out.write_text(...)`) is owned by that constant's directory, which is how a writer that names a
directory rather than a file stays visible. The fourth rule is the package-write case: a
`write_atomic(CONST, text)`, `stage(CONST, text)` or `promote(CONST, key, text)` call whose first
argument is a `notes/` path constant, an alias of one, or a local built from one, is owned by that
constant — this is how a writer whose write moved into `catlib.atomic` or `catlib.promote` stays
visible, since the write call itself is no longer in the script. The fifth rule is the keyed store:
`cached(KEY, "names.json", builder)` names no path, because the record's directory is the digest key
the source does not write down, so the rule takes the literal record name and prefixes the store root
`.qwen/cache/records/<key>/`. That is the one target outside `notes/` the page carries, and the one
the promote-and-verify byte comparison cannot check, because the `.qwen/*` rule keeps it untracked.
The sixth rule subtracts the
self-test: a module-level
`mutants` / `mutant_test` / `selftest` body is blanked before the write calls are read, because a
self-test writes the page it checks only to mutate it and restores the bytes it read in the `finally`
— `verify_script_ownership.py` does exactly that, in three branches (the page it checks, `notes/scripts/README.md`, and `notes/development/templates.md`), so its normal run writes nothing and it stays in the checker class. `check_index_links.py` and `measure_proof_density.py` were this rule's examples; `math-o3a.3` moved their sync pass into `verify_page_sync.py`, which mutates page text in memory, so neither script carries a write call any more. That rule
finds **21** writers over **74** scripts.

### Writers

| Script | Writes | Gate | Report feeds |
|---|---|---|---|
| `build_catalog.py` | `notes/gen/tables/catalog.tsv` | single run; cached bytes == promoted bytes under the key | `notes/README.md`, `notes/gen/reports/findings.md` |
| `build_sources.py` | `notes/gen/tables/sources.tsv` | single run; cached bytes == promoted bytes under the key | `notes/gen/reports/sources.md` |
| `build_index.py` | `notes/gen/index` | single run; cached bytes == promoted bytes for all 1,049 files | `notes/development/index-links.md` |
| `build_summaries.py` | `notes/gen/summaries` | a gate row; single run, cached bytes == promoted bytes for the 61 pages it renders — before `seed_quotes.py` (which re-seeds the quote specs from the pages) so the render chain stays acyclic | `notes/gen/summaries/` — the per-family pages `verify_summaries.py` checks and `seed_quotes.py` re-seeds from |
| `compare_abstracts.py` | `notes/gen/tables/abstracts.tsv` | `--tsv` only; single run; cached bytes == promoted bytes under the key | `notes/gen/reports/abstracts.md` |
| `extract_formalization_deps.py` | `notes/gen/tables/formalization-deps.tsv` | single run; cached bytes == promoted bytes under the key | `notes/gen/reports/dependency-drift.md` |
| `extract_links.py` | `notes/gen/tables/links.tsv` | single run; cached bytes == promoted bytes under the key | `notes/gen/reports/links.md` |
| `extract_subfindings.py` | `notes/gen/tables/subfindings.tsv` | single run; cached bytes == promoted bytes under the key | `notes/gen/reports/subfinding-pairs.md` |
| `extract_summary_data.py` | `notes/data/summaries/` | not in `gate.py` — a one-time bootstrap: it reads the 60 family pages and writes the `notes/data/summaries/` data files the summary renderer renders from, which are tracked in git and edited as prose, so re-running it would re-derive them from the pages and clobber hand edits | the 60 `notes/data/summaries/` data files `build_summaries.py` reads |
| `fix_blank_cites.py` | `notes/data/summaries` | not in `gate.py` — an authoring tool: run by hand after writing a data file and before `build_summaries.py`, so the render picks up the corrected citations | the data files `build_summaries.py` renders |
| `render_reports.py` | `notes/README.md`, `notes/gen/reports/abstracts.md`, `notes/gen/reports/dependency-drift.md`, `notes/development/index-design.md`, `notes/development/index-links.md`, `notes/gen/reports/links.md`, `notes/gen/reports/named-results.md`, `notes/gen/reports/names.md`, `notes/gen/reports/proof-density.md`, `notes/gen/reports/sources.md`, `notes/gen/reports/verification-dirs.md`, `notes/gen/reports/scope-exclusions.md`, `notes/gen/reports/topics.md`, `notes/gen/reports/t0-chains.md`, `notes/gen/reports/subfinding-pairs.md`, `notes/gen/reports/counterexample-crosscheck.md`, `notes/gen/reports/formalization-faithfulness.md`, `notes/development/fleet-design.md`, `notes/development/templates.md` | single run; cached bytes == promoted bytes for all 19 pages | the nineteen report-fed pages |
| `build_report_templates.py` | `notes/gen/tables/splits.tsv`, `notes/templates/report` | not in `gate.py` — it reads each page with `git show HEAD:`, so a gate run would rewrite templates from committed bytes; run explicitly with 0 args (all nineteen pages) or 2 (one page) after a writer's slot dict changes | the nineteen page templates; the registry, slot dicts and needle derivation it reads are in `catlib/templates.py` |
| `measure_names.py` | `.qwen/cache/records/<key>/names.json` | plain; no tracked artifact, so the promote-and-verify assertion compares no bytes for it — `verify_cache_promotion.py` proves its L1 against the probe record and the cache check reads no tracked path | `notes/gen/reports/names.md`, and the 551 name pages `build_index.py` renders from `--json` |
| `extract_named_results.py` | `.qwen/cache/records/<key>/named_results.json` | plain; no tracked artifact, so the promote-and-verify assertion compares no bytes for it — `verify_cache_promotion.py` proves its L1 against the probe record and the cache check reads no tracked path | `notes/gen/reports/named-results.md` — the writer, `verify_named_results.py` and `notes/scripts/tests/test_named_results.py` read the same record, so the 7,240-file `.tex` walk is paid once per key, not once per process |
| `measure_templates.py` | `.qwen/cache/records/<key>/templates.json`
| `measure_checker_reads.py` | `notes/development/probe` | not in `gate.py` — it runs the whole fleet with an audit hook, so a gate run inside a gate run would contaminate its own record; run explicitly after a writer's L1 changes | the probe record the census's L1-exactness pass reads, and the per-row read graph `notes/development/probe/checker_reads.txt` carries |
| `measure_open_probe.py` | `notes/development/probe` | not in `gate.py` — a record carries a wall time per target, so a run-1/run-2 byte diff of a record is a timing artifact, not a proof; run explicitly over the purity and amplification targets, appending stdout to build a multi-target record | the two probe records `verify_fleet_design.py` parses |
| `seed_quotes.py` | `notes/gen/tables/quotes.tsv` | single run; cached bytes == promoted bytes under the key | `notes/gen/reports/subfinding-pairs.md` and `notes/gen/summaries/**` — the two surfaces whose quotes it seeds; `render_reports.py` reads the pair rows back for the pair page, and `notes/scripts/tests/test_quotes.py` reads the whole table back |
| `build_index_db.py` | `.qwen/cache/records/<key>/fts.json` and `.qwen/cache/records/<key>/index.db` | not in `gate.py` — the report carries a build wall and a per-term query wall, so a run-1/run-2 byte diff is a timing artifact; the record itself carries only counts, and the database is untracked by the `.qwen/*` rule | the SQLite FTS5 layer over the 8,007 `.tex` files and the 372 abstracts, the layer `notes/development/index-design.md`'s schema decision leaves out |
| `measure_gate_rows.py` | `notes/gen/tables/gate-rows.tsv` | not in `gate.py` — it reads the driver's report for the last completed run, which the driver truncates at run start, so a gate row would read the previous run's bytes; run explicitly after a gate pass | none yet — beads `math-rui.3` and `math-rui.4` give the writer a slot and the census checker a needle |
| `measure_check_calls.py` | `.qwen/cache/records/<key>/check_calls.json` | a gate row; the record is the population the `check()` sentences in this page quote, and there are no tracked bytes for the promote assertion to compare | the eleven `check()` sentences in this page |

Eight writers emit one TSV each. `build_index.py` is the one-to-many case: it renders **1,049** files —
**1,033** `.md` pages and **0** `.tsv` tables in `notes/gen/index/`, plus the **16** `.tsv` tables it stages
into `notes/gen/tables/`. `render_reports.py` renders the nineteen report-fed pages
from the templates `build_report_templates.py` builds from the committed page and the slot dict that
writer supplies. `compare_abstracts.py` is the conditional case: its
default run writes nothing and only `--tsv` touches `notes/gen/tables/abstracts.tsv`. The three record
producers (`measure_names.py`, `extract_named_results.py`, `measure_templates.py`) write to the keyed
store, not to a tracked path: `measure_names.py`'s consumers (`render_reports.py`, `build_index.py`,
`extract_named_results.py`, `verify_named_results.py`) read it through `measure()`,
`extract_named_results.py`'s consumers (`render_reports.py`, `verify_named_results.py` and
`notes/scripts/tests/test_named_results.py`) read it through `population()`, and
`measure_templates.py`'s (`render_reports.py` and `build_report_templates.py`'s floor page) read it
through `population()`, so each walk is paid once per key instead of once per process.

All **18** writers take `--check-only`: the run does its full measurement, prints its report, and writes
nothing. Measured 2026-10-11 by running each writer plain and then with the flag — the report is
identical in both runs (the write announcement is the only line that differs) and
`git status --porcelain` is unchanged by the flagged run. The three record producers are the case where
the flagged run's proof is the report identity alone: their write lands in the untracked store, so
`git status` is clean for them plain and flagged alike. `gate.py` runs the writers plain; the read-only
rows `math-o3a.5.2` pooled are the rows that run with the flag, which is why the flag comes first.

All sixteen writers reach `write_atomic()` in `catlib/atomic.py`, so a crash never leaves a
half-written tracked file. The single-file writers use `write_atomic()`, which lands bytes on a sibling
temp name in the same directory, fsyncs, and moves the temp onto the target. The three multi-file
writers (`build_index.py`, `render_reports.py`, `build_report_templates.py`) use `Staging(name)`:
`stage()` lands bytes under `.qwen/cache/staging/<name>/`, which the `.qwen/*` rule in `.gitignore`
keeps untracked, and records the tracked path; `promote()` moves every staged slot onto its tracked
path. The three record producers reach `write_atomic()` through `catlib/records.py`'s `cached()`,
which lands the record inside the keyed store; there is no tracked file there to half-write, so the
crash-safety
argument for it is the untracked-ness of the tree, not the temp-name move.
A writer calls `promote()` only after its own reconciliation lines have printed, so killing a writer
mid-run leaves the tracked tree exactly as it was — the proof is `build_index.py` killed mid-run in
the 1,049-file case with `git status --porcelain` clean.

Writers import each other, so a generated file's bytes are not a function of one script.
`build_index.py` imports `build_catalog`, `measure_topics`, `measure_names`,
`check_index_links` and `jinja2` (the index page text lives in `notes/templates/*.j2`, the seventeen
report-fed page skeletons in `notes/gen/templates/report/*.j2`);
`extract_links.py`, `extract_subfindings.py`, `check_index_links.py`, `measure_names.py` and
`measure_topics.py` all import `build_catalog`;
`measure_index_sizes.py` imports `check_index_links` inside its link-check function
(`measure_index_sizes.py:120`), not at module scope. Counted over `notes/scripts/*.py` as a script
that imports the module (`import X` or `from X`, the module itself excluded), `build_catalog.py` has
**12** importers, `build_sources.py` **2** (`verify_sources.py` and `render_reports.py:50`, which
imports it at module scope; `read_manuscript.py` names it in a docstring, not in an import) and
`verify_summaries.py` **0** — `math-6s7.1` moved the page parse to `catlib/summaries.py`, so
`locate_summary_quotes.py` and `verify_scope_exclusions.py` import
the package, not the checker, and `check_summary_manuscripts.py` stops importing `build_catalog`. The
**18** and **1** this paragraph carried were stale at HEAD, which measures **17** and **2**; the port
takes `build_catalog` to 16, and `math-6s7.2` takes it to 15 — `extract_verification_dirs.py`
now reads `catlib.overview.parse_overview`, `catlib.paths.owner` and `catlib.ledger.read_ledger`.
`math-6s7.4` takes it to **12**: `compare_abstracts.py`, `extract_subfinding_pairs.py` and
`extract_named_results.py` import `catlib.overview` / `catlib.ledger` / `catlib.paths` directly, and
the shim shrinks to the **10** names that still have an importer (`PAP`, `read_args`,
`parse_overview`, `parse_contents`, `parse_yaml`, `parse_challenges`, `parse_docs`, `parse_traces`,
`shapes_of`, `COUNTEREX_PHRASE`). `MONTHS`, `DATE_SUFFIX`, `SHAPES`, `conditional_hits`,
`resolves_named`, `counterex_broad`, `versions_of`, `TARGET_NOUN` and `RESOLVE_VERB` had none and are
dropped; `main()` reads the package through `ledger.` for the three it needs.
Editing a join in `build_catalog.py` can move rows in six artifacts.

### Report-only

The other **53** scripts write nothing. **30** of them print a report: **19** print the report a page's
counts come from, **1** prints the pytest report for the extracted checker self-tests
(`run_tests.py`), **2** print the notes-move surface `math-faz` prices before a pass and re-checks
after it, **7** print a wall, a candidate comparison, or a fleet census that no page's counts come from
(the render phase, pool and fresh-process probes, the links phase and scan-candidate probes, the Lean
import layout probe, and the needle census), and `gate.py` prints the gate report itself.
The Gate column is the invocation the gate list runs: `notes/scripts/gate.py`, which runs **79**
invocations — the **10** gated writers (the four writers it does not run as writer rows are
`build_report_templates.py` and `measure_open_probe.py`, each for the reason in its own row, and
`measure_names.py` and `extract_named_results.py`, which run as `--check-only` rows), the 43
gated report-only rows (including `check_summary_manuscripts.py`
and `locate_summary_quotes.py`, `check_index_links.py` plain and its extracted self-tests row, and
the twenty-five extracted self-tests rows, `run_tests.py notes/scripts/tests/test_scope_exclusions.py -q`,
`run_tests.py notes/scripts/tests/test_conjecture_standing.py -q`,
`run_tests.py notes/scripts/tests/test_abstracts.py -q`,
`run_tests.py notes/scripts/tests/test_named_conjectures.py -q`,
`run_tests.py notes/scripts/tests/test_subfindings.py -q`,
`run_tests.py notes/scripts/tests/test_summaries.py -q`,
`run_tests.py notes/scripts/tests/test_index_links.py -q` and
`run_tests.py notes/scripts/tests/test_script_ownership.py -q` and
`run_tests.py notes/scripts/tests/test_conditional.py -q` and
`run_tests.py notes/scripts/tests/test_upstream_history.py -q` and
`run_tests.py notes/scripts/tests/test_cache_promotion.py -q` and
`run_tests.py notes/scripts/tests/test_findings.py -q` and
`run_tests.py notes/scripts/tests/test_counterexample_crosscheck.py -q` and
`run_tests.py notes/scripts/tests/test_faithfulness.py -q` and
`run_tests.py notes/scripts/tests/test_proof_density.py -q` and
`run_tests.py notes/scripts/tests/test_sources.py -q` and
`run_tests.py notes/scripts/tests/test_index_design.py -q` and
`run_tests.py notes/scripts/tests/test_fleet_design.py -q` and
`run_tests.py notes/scripts/tests/test_verification_dirs.py -q` and
`run_tests.py notes/scripts/tests/test_named_results.py -q` and
`run_tests.py notes/scripts/tests/test_citations.py -q` and
`run_tests.py notes/scripts/tests/test_t0_chains.py -q` and
`run_tests.py notes/scripts/tests/test_dependency_drift.py -q` and
`run_tests.py notes/scripts/tests/test_subfinding_pairs.py -q` and
`run_tests.py notes/scripts/tests/test_quotes.py -q`), and **24** checker
invocations:
`verify_page_sync.py --both` (**1**) — both passes in one process, because `catlib.render.rendered`
is cached per process and two rows pay the corpus walk twice — plus `verify_script_ownership.py` plain
(**1**), `verify_scope_exclusions.py` plain (**1**), `verify_conjecture_standing.py` plain (**1**),
`verify_abstracts.py` plain (**1**),
`verify_named_conjectures.py` plain (**1**), `verify_subfindings.py` plain (**1**) and
`verify_summaries.py` plain (**1**) and
`verify_conditional.py` plain (**1**) and
`verify_upstream_history.py` plain (**1**) and
`verify_cache_promotion.py` plain (**1**) and
`verify_findings.py` plain (**1**) and
`verify_counterexample_crosscheck.py` plain (**1**) and
`verify_sources.py` plain (**1**) and
`verify_subfinding_pairs.py` plain (**1**) and
`verify_index_design.py` plain (**1**) and
`verify_fleet_design.py` plain (**1**) and
`verify_named_results.py` plain (**1**) and
`verify_faithfulness.py` plain (**1**) and
`verify_citations.py` plain (**1**) and
`verify_t0_chains.py` plain (**1**) and
`verify_dependency_drift.py` plain (**1**), which
no longer carry a `--mutant` branch — in
class order, not in the order the rows sit; it prints one line per invocation with its exit code, its
wall time, and the first 200 bytes of its report, and writes nothing to the repo outside
`.qwen/tmp/reports/`. `math-8ou` promoted the list from `.qwen/tmp/` into `notes/scripts/`, closing
the one gap the list had; `math-unv` replaced the shell list with the scheduler. A writer's gate is the single run plus the promote-and-verify assertion
recorded in the writers table: the bytes it lands under its key must equal the bytes on the tracked
path. The list is one array, `ROWS`, of (spec, needs, writes) triples over the generated artifacts; a
row starts as soon as every row that writes its `needs` has finished, so the 8 report-only extractors
and the corpus readers start at t=0 and the writer chain runs as a graph, not as a fixed order. Each
row writes its own `.line` file and the report prints the `.line` files in list order after the last
row, so the report is the same bytes a serial run prints. `GATE_POOL` is the concurrency cap, **12**
rows, sized by measured RSS (6.1 Gi available with the model server loaded, the two heaviest rows peak
at 415 MB), not by core count; `GATE_POOL=1` runs the rows one at a time in list order, the serial
baseline. A row must spawn no writer, so the render children (`build_index.py`,
`extract_links.py`) run with `--check-only`. `gate_driver.sh` runs the list once, snapshots the md5 of
every generated artifact and `git status` raw, and prints the `verify_cache_promotion.py` row, whose
key is computed from the current `git rev-parse HEAD:<path>` tree digests. Measured 2026-10-11:
**351.1** s of driver wall over **919.4** s of row time, against **461.4** s when the read-only rows
had to wait for the serial chain to finish.

| Script | Report feeds | Gate |
|---|---|---|
| `check_gate_budget.py` | none — the budget assertion `wall < 300 s`, the row-time sum, and the three heaviest rows | **not gated** — the driver runs it post-gate, because the wall it reads is landed by the run itself |
| `check_index_links.py` | `notes/development/index-links.md` | plain; the self-tests are in `notes/scripts/tests/test_index_links.py`, run by the `run_tests.py` row |
| `check_summary_manuscripts.py` | `notes/gen/summaries/` — which manuscripts each page reads, and whether the release still names them | plain |
| `dump_template_slots.py` | `notes/development/templates.md` — the writer's slot labels with their values | plain |
| `extract_citations.py` | `notes/gen/reports/citations.md` | plain |
| `extract_counterexample_crosscheck.py` | `notes/gen/reports/counterexample-crosscheck.md` | plain |
| `extract_scope_notes.py` | `notes/gen/reports/scope-exclusions.md` | plain |
| `extract_subfinding_pairs.py` | `notes/gen/reports/subfinding-pairs.md` | plain |
| `extract_t0_chains.py` | `notes/gen/reports/t0-chains.md` | plain |
| `extract_verification_348.py` | `notes/gen/reports/verification-dirs.md` | plain |
| `extract_verification_dirs.py` | `notes/gen/reports/verification-dirs.md` | plain |
| `gate.py` | none — the gate list itself: 81 rows as a dependency graph, printing one line per row in list order | **the list** — run by `gate_driver.sh` |
| `locate_summary_quotes.py` | `notes/gen/summaries/` — the lines a page should cite when a quotation stops matching | **not gated** — a renderer debug tool, run by hand against a page whose quotation stops matching |
| `measure_anchor_blocks.py` | `math-faz` — the fenced blocks and quotations in the moved pages attributed to a notes-page anchor; the bead re-runs it after each pass | **not gated** |
| `measure_checker_needles.py`, `measure_checker_reads.py`` | `notes/development/templates.md` — the per-checker needle inventory behind its Needles column | plain |
| `measure_faithfulness.py` | `notes/gen/reports/formalization-faithfulness.md` | plain |
| `measure_index_sizes.py` | `notes/development/index-design.md` | plain |
| `measure_import_layout.py` | `extract_links.py`'s import header rule — the Lean files whose first command is a doc-comment opener (`/-`), a bare `module` line, or a `public import` line, which is the evidence the widened `HEADER_SKIP` rule was written from | **not gated** — walks 122,458 files; run by hand when the header rule changes |
| `measure_links_phases.py` | `extract_links.py`'s phases — the wall each read and scan takes, attributed by wrapping the script's own reads, because cProfile totals attribute cost to functions, not phases | **not gated** — a phase wall is a function of a run |
| `measure_move_surface.py` | `math-faz` — the moved/stable path-mention split over the 7 pages the reorg moved, by context; the bead re-runs it after each pass | **not gated** |
| `measure_needles.py` | `notes/scripts/tests/` — the needle fleet: faults per file, needles recorded as a string versus derived as a callable, recorded needles split numeric versus structural, needle digits, synthetic rule inputs, the numeric literals in each clean test's asserted tuples, and the recorded needles whose digits their own mutation never writes | plain |
| `measure_proof_density.py` | `notes/gen/reports/proof-density.md` | the self-tests are in `notes/scripts/tests/test_proof_density.py`, run by the `run_tests.py` row; the plain run is not gated, because `render_reports.py` imports the module and calls `build_families()` rather than running the script |
| `measure_render_phases.py` | `render_reports.py`'s phase wall with concurrent children — cumulative, in `main()` call order | **not gated** — a phase wall is a function of a run |
| `measure_render_pool.py` | whether pooling the 15 child-free populations lowers the render wall; measured 2026-10-12 and the answer was no (22.16 s pooled against 16.78 s unpooled, because pool results never reach the parent's cached `population_of`) | **not gated** — a wall is a function of a run |
| `measure_render_processes.py` | the cost of each population in a fresh process, which is the pool's per-process price; `links` 14.59 s and `topics` 16.40 s, each re-running the `extract_links` child | **not gated** — a per-process wall is a function of a run |
| `measure_scan_candidates.py` | the four candidate scans priced against the rule each must reproduce; the import header and the MSC substring gate were accepted, the single-pass `norm` and the 372-alternation regex were rejected | **not gated** — the accepted rules are already in `extract_links.py` |
| `measure_topics.py` | `notes/gen/reports/topics.md` | `--check` |
| `read_manuscript.py` | none — a reading aid; prints a manuscript's abstract, section skeleton and titled statement environments with `file:line` anchors | **not gated** |
| `run_tests.py` | none — the seam between the gate and the extracted checker self-tests, which live in `notes/scripts/tests/`: the gate runs every row as `python3 notes/scripts/<spec>` and pytest lives in the venv, so this row names the venv's python and passes pytest args through | plain |
| `triage_t0.py` | `notes/gen/reports/t0-triage.md` | plain |

`read_manuscript.py` is the only script the gate does not run: it takes a `preprints/` directory
argument, so a gate run over it would read one manuscript chosen by the list rather than the corpus.

`check_index_links.py` is the link checker for `notes/gen/index/` and `CONTENTS.md` — it reads the tree and
writes nothing, so it sits here rather than in the checker table, which lists scripts that verify a
page's text. `math-o3a.3` removed its sync pass on `notes/development/index-links.md` — the page is compared with
`render_reports.py`'s render of it by `verify_page_sync.py`, which mutates the page in memory — and
the pass that extracted its self-tests removed its `--mutant` branch: the 21 injected hrefs live in
`notes/scripts/tests/test_index_links.py`, and the prose mutant `math-a0r.6.2` added is
`verify_page_sync.py`'s. `trap()` stays in the checker because `render_reports.py` renders its two
rows into the page's scanner table.

### Checkers

The remaining **23** scripts verify a page or a table. Each exits non-zero when what it checks has
drifted; **0** take `--mutant` — after the twenty-fourth extraction no checker carries a mutant
branch any more — and **23** —
`verify_scope_exclusions.py`, `verify_conjecture_standing.py`, `verify_abstracts.py`,
`verify_named_conjectures.py`, `verify_subfindings.py`, `verify_summaries.py` and
`verify_script_ownership.py`, `verify_conditional.py`, `verify_upstream_history.py`,
`verify_cache_promotion.py`, `verify_findings.py`, `verify_counterexample_crosscheck.py`,
`verify_faithfulness.py`, `verify_sources.py`, `verify_subfinding_pairs.py`, `verify_index_design.py`,
`verify_fleet_design.py`, `verify_verification_dirs.py`,
`verify_named_results.py`,
`verify_citations.py`,
`verify_t0_chains.py`, `verify_dependency_drift.py` and
`verify_tsv_quoting.py` — have their
self-tests extracted to `notes/scripts/tests/`, so the checker measures and the test file injects.
The gate runs each one plain —
**24** of the 81 invocations: **1** for
`verify_page_sync.py --both`, which runs both passes in one process, **1** plain for
`verify_script_ownership.py` (the 23rd checker, not listed in its own table), **1** plain for
`verify_scope_exclusions.py`, **1** plain for `verify_conjecture_standing.py`, **1** plain for
`verify_abstracts.py`, **1** plain for `verify_named_conjectures.py`, **1** plain for
`verify_subfindings.py`, **1** plain for `verify_summaries.py` and
**1** plain for `verify_conditional.py` and
**1** plain for `verify_upstream_history.py` and
**1** plain for `verify_cache_promotion.py` and
**1** plain for `verify_findings.py` and
**1** plain for `verify_counterexample_crosscheck.py` and
**1** plain for `verify_sources.py` and
**1** plain for `verify_subfinding_pairs.py` and
**1** plain for `verify_index_design.py` and
**1** plain for `verify_fleet_design.py` and
**1** plain for `verify_verification_dirs.py` and
**1** plain for `verify_named_results.py` and
**1** plain for `verify_faithfulness.py` and
**1** plain for `verify_citations.py` and
**1** plain for `verify_t0_chains.py` and
**1** plain for `verify_dependency_drift.py` and
**1** plain for `verify_tsv_quoting.py`. The extracted
self-tests rows are report-only rows, not checker invocations:
`run_tests.py notes/scripts/tests/test_scope_exclusions.py -q`,
`run_tests.py notes/scripts/tests/test_conjecture_standing.py -q`,
`run_tests.py notes/scripts/tests/test_abstracts.py -q`,
`run_tests.py notes/scripts/tests/test_named_conjectures.py -q`,
`run_tests.py notes/scripts/tests/test_subfindings.py -q`,
`run_tests.py notes/scripts/tests/test_summaries.py -q` and
`run_tests.py notes/scripts/tests/test_script_ownership.py -q` and
`run_tests.py notes/scripts/tests/test_conditional.py -q` and
`run_tests.py notes/scripts/tests/test_upstream_history.py -q` and
`run_tests.py notes/scripts/tests/test_cache_promotion.py -q` and
`run_tests.py notes/scripts/tests/test_findings.py -q` and
`run_tests.py notes/scripts/tests/test_counterexample_crosscheck.py -q` and
`run_tests.py notes/scripts/tests/test_faithfulness.py -q` and
`run_tests.py notes/scripts/tests/test_sources.py -q` and
`run_tests.py notes/scripts/tests/test_index_design.py -q` and
`run_tests.py notes/scripts/tests/test_fleet_design.py -q` and
`run_tests.py notes/scripts/tests/test_verification_dirs.py -q` and
`run_tests.py notes/scripts/tests/test_named_results.py -q` and
`run_tests.py notes/scripts/tests/test_tsv_quoting.py -q`.

| Checker | Checks | Gate | Read (files) | Cold (s) | Wall (s) |
|---|---|---|---|---|---|
| `verify_abstracts.py` | `notes/gen/reports/abstracts.md` | plain; the self-tests are in `notes/scripts/tests/test_abstracts.py`, run by the `run_tests.py` row | 11 | 0.8 | 0 |
| `verify_cache_promotion.py` | `catlib/promote.py` — the registry shape against the writers table, the L1 lists against the audit-hook records, and the cached bytes against every tracked artifact under its key | plain; the self-tests are in `notes/scripts/tests/test_cache_promotion.py`, run by the `run_tests.py` row | — | 1.6 | 1.6 |
| `verify_citations.py` | `notes/gen/reports/citations.md` | plain; the self-tests are in `notes/scripts/tests/test_citations.py`, run by the `run_tests.py` row | 4 | 1.8 | 0 |
| `verify_conditional.py` | `notes/gen/reports/conditional.md` | plain; the self-tests are in `notes/scripts/tests/test_conditional.py`, run by the `run_tests.py` row | 2 | 0 | 0 |
| `verify_conjecture_standing.py` | `notes/data/conjecture-standing.tsv` | plain; the self-tests are in `notes/scripts/tests/test_conjecture_standing.py`, run by the `run_tests.py` row | 3 | 0 | 0 |
| `verify_counterexample_crosscheck.py` | `notes/gen/reports/counterexample-crosscheck.md` | plain; the self-tests are in `notes/scripts/tests/test_counterexample_crosscheck.py`, run by the `run_tests.py` row | 11 | 0.4 | 0 |
| `verify_dependency_drift.py` | `notes/gen/reports/dependency-drift.md`, `notes/gen/reports/formalization-deps.md` | plain; the self-tests are in `notes/scripts/tests/test_dependency_drift.py`, run by the `run_tests.py` row | 13 | 0.3 | 0 |
| `verify_faithfulness.py` | `notes/gen/reports/formalization-faithfulness.md` — anchors, the count phrases re-derived by its own `main_results`/declaration/carrier/closure walk (not the writer's), the disjoint and overlap pairing tables, the `a.e.` table, and the render diff | plain; the self-tests are in `notes/scripts/tests/test_faithfulness.py`, run by the `run_tests.py` row | 11 | 1.8 | 0 |
| `verify_findings.py` | `notes/gen/reports/findings.md` | plain; the self-tests are in `notes/scripts/tests/test_findings.py`, run by the `run_tests.py` row | 37 | 14.8 | 0 |
| `verify_fleet_design.py` | `notes/development/fleet-design.md` — anchors, the count phrases re-derived from `git`/`du`/the probe records, each of the three site paragraphs (atomicity, env, set iteration) and the checker-section anchor list compared with the measured `name:line` set, the purity and amplification tables, and the page against `render_reports.py`'s render of it | plain; the self-tests are in `notes/scripts/tests/test_fleet_design.py`, run by the `run_tests.py` row | — | 0.8 | 0.8 |
| `verify_index_design.py` | `notes/development/index-design.md` | plain; the self-tests are in `notes/scripts/tests/test_index_design.py`, run by the `run_tests.py` row | 1067 | 3.5 | 0 |
| `verify_named_conjectures.py` | `notes/gen/reports/named-conjectures.md` | plain; the self-tests are in `notes/scripts/tests/test_named_conjectures.py`, run by the `run_tests.py` row | 3 | 0 | 0 |
| `verify_named_results.py` | `notes/gen/reports/named-results.md` | plain; the self-tests are in `notes/scripts/tests/test_named_results.py`, run by the `run_tests.py` row | — | 3.3 | 3.3 |
| `verify_page_sync.py` | `notes/gen/reports/links.md`, `notes/gen/reports/names.md`, `notes/gen/reports/topics.md`, `notes/gen/reports/proof-density.md`, `notes/development/index-links.md` — the render diff for the five pages whose sync pass used to live in a writer; the mutants mutate page prose in memory, so no page is written | `--both` — plain and mutant in one process | — | 36.5 | 36.5 |
| `verify_scope_exclusions.py` | `notes/gen/reports/scope-exclusions.md` | plain; the self-tests are in `notes/scripts/tests/test_scope_exclusions.py`, run by the `run_tests.py` row | 11 | 0.1 | 0 |
| `verify_sources.py` | `notes/gen/reports/sources.md` | plain; the self-tests are in `notes/scripts/tests/test_sources.py`, run by the `run_tests.py` row | 13 | 3.9 | 0 |
| `verify_subfinding_pairs.py` | `notes/gen/reports/subfinding-pairs.md` | plain; the self-tests are in `notes/scripts/tests/test_subfinding_pairs.py`, run by the `run_tests.py` row | 13 | 1.2 | 0 |
| `verify_subfindings.py` | `notes/gen/tables/subfindings.tsv` | plain; the self-tests are in `notes/scripts/tests/test_subfindings.py`, run by the `run_tests.py` row | 6 | 0.1 | 0 |
| `verify_summaries.py` | `notes/gen/summaries/` | plain; the self-tests are in `notes/scripts/tests/test_summaries.py`, run by the `run_tests.py` row | 337 | 60.2 | 0 |
| `verify_t0_chains.py` | `notes/gen/reports/t0-chains.md` | plain; the self-tests are in `notes/scripts/tests/test_t0_chains.py`, run by the `run_tests.py` row | 13 | 1.7 | 0 |
| `verify_tsv_quoting.py` | `notes/gen/tables/*.tsv` — the RFC 4180 rule: a field that does not start with a quote carries no quote at all, and a field that opens a quoted field must close inside the field with every interior quote doubled | plain; the self-tests are in `notes/scripts/tests/test_tsv_quoting.py`, run by the `run_tests.py` row | 26 | 0 | 0 |
| `verify_upstream_history.py` | `notes/development/upstream_history/` — the three pages | plain; the self-tests are in `notes/scripts/tests/test_upstream_history.py`, run by the `run_tests.py` row | — | 0.6 | 0.6 |
| `verify_verification_dirs.py` | `notes/gen/reports/verification-dirs.md` | plain; the self-tests are in `notes/scripts/tests/test_verification_dirs.py`, run by the `run_tests.py` row | 11 | 0.2 | 0 |

Cold is the wall the row's subprocess last paid (from the gate record for keyable rows, this
run's wall for non-keyable rows that always run); Wall is this run's wall as printed by the gate.
A skipped keyable row's Wall is the key computation (~0 s) and its Cold is the last real run —
the two name different rules, not one number for both. Measured 2026-10-16 with the local model
server loaded; a floor from one measurement, not a benchmark.
`verify_findings.py` is the subprocess case: its Pass E runs the fast extractors as subprocesses inside
`check()` (`:459`, the subprocess call at `:140`), so a plain run pays five of them. The pass that
extracted its self-tests put `run()` under `functools.cache` (`:134`) — every script in `REPORTS` is
report-only, so a second call in the same process cannot see a different stdout — and that is why the
`run_tests.py` row measures **15.6 s** where the `--mutant` row took **34.7 s** before that row was
replaced: the 9 `check()` calls the row makes (the clean page, each of the six faults, and the padded-table test's two) pay the
five subprocesses once.
`verify_faithfulness.py` is the same case with a corpus walk instead of subprocesses: `population()`
is under `functools.cache` (`:187`) — the checker writes nothing and the tests mutate page text in
memory, so a second call in the same process cannot see a different corpus — and that is why its
`run_tests.py` row measures **1.7 s** where the `--mutant` row took **12.8 s** before that row was
replaced: the 33 `check()` calls the row makes pay the yaml/docs/OAI/preprints walk once.
`verify_sources.py` is the same case with a wider walk: `population()` is under `functools.cache`
(`:152`) — the checker writes nothing and the tests mutate page text in memory, so a second call in the
same process cannot see a different corpus — and that is why its `run_tests.py` row measures **1.2 s**
where the `--mutant` row took **12.9 s** before that row was replaced: the 15 `check()` calls the
row makes pay the preprints/overview walk once.
`verify_index_design.py` is the same case with the index tree: `population()` is under
`functools.cache` (`:66`) and delegates to `measure_index_sizes.population()`, so its `run_tests.py`
row measures **5.5 s** where the `--mutant` row took **20.3 s** before that row was replaced: the
17 `check()` calls the row makes pay the `notes/gen/index/` walk once.
`verify_fleet_design.py` is the same case with the `git`/`du`/script-tree walk: `population()` is under
`functools.cache` (`:151`), so its `run_tests.py` row measures **0.7 s** where the `--mutant` row took
**0.8 s** before that row was replaced: the 22 `check()` calls the row makes pay the five
`git rev-parse` calls, the `--ignored=matching` check, the three `du -sk` calls and the 68-script scan
once.
`verify_verification_dirs.py` is the same case with two walks: `population()` (`:138`) and
`entry_measure()` (`:149`) are both under `functools.cache`, so its `run_tests.py` row measures
**0.4 s** where the `--mutant` row took **1.8 s** before that row was replaced: the 21 `check()`
calls the row makes pay the 749-directory bundle scan and the ledger join once.
`verify_named_results.py` is the keyed-record case, not the in-process-cache case: its `population()`
reads `named_results.json` under the producer's key, so the plain row is **0.6 s** and the
`run_tests.py` row measures **7.2 s** — the 15 `check()` calls pay the 7,240-file walk once,
under the key the producer landed, not inside the checker. Before the record the plain row was 18.9 s
and the test row 23.8 s. The remaining cost is the per-`check()` read of 61 anchors and 61 quotations,
which a mutant does multiply.
`verify_citations.py` is the same case with the `.bib` walk: `measure()` is under `functools.cache`
(`:75`), so its `run_tests.py` row measures **4.7 s** where the `--mutant` row took **3.0 s** — the
12 `check()` calls the row makes pay the two normalizations once. The cache persists only because the
test loader memoizes: a loader that re-executed the module per test gave each test an empty cache, and
the row measured **16.9 s** before the loader was memoized.
`verify_t0_chains.py` is the same case with the ledger, `subfindings.tsv`, `notes/gen/reports/t0-triage.md` and the
`.bib` layer: `population()` is under `functools.cache` (`:118`), so its `run_tests.py` row measures
**2.9 s** where the `--mutant` row took **1.4 s** — the 17 `check()` calls the row makes pay the
walk once.
`verify_dependency_drift.py` is the same case with the TSV, `lean/lakefile.lean`, `lean/formalization.yaml`
and the 23 patch files: `measure()` is under `functools.cache` (`:185`), so its `run_tests.py` row
measures **2.4 s** where the `--mutant` row took **2.0 s** — the 12 `check()` calls the row makes pay
the walk once.
`verify_subfinding_pairs.py` is the same case with `overview.tex`, `notes/gen/tables/subfindings.tsv` and the
ledger: `load_inputs()` is under `functools.cache` (`:54`), so its `run_tests.py` row measures **1.9 s**
where the `--mutant` row took **0.1 s** — the 11 `check()` calls the row makes pay the walk once.
`verify_page_sync.py --both` at **36.5 s** is the heaviest row with a Wall cell. `verify_script_ownership.py`,
this page's own checker, is not a row above, so it has no Cost cell.
`verify_page_sync.py`'s Cost is one number, not a pair: `--both`
runs the plain pass and the mutant loop in one process, so `catlib.render.rendered` is walked once
(123.4 s plain + 122.9 s mutant as two rows, against 125.2 s in one, measured 2026-10-10; the same
single walk measured **25.1 s** in the 2026-10-12 run, because the render-diff reads the cached
records the writers promote rather than re-walking the corpus). The 23 checker invocations sum
to **42.8 s**, measured 2026-10-16 as the sum of the wall times the gate printed for its rows in one
pooled run, each Wall cell re-checked cell-by-cell against that run (0
mismatches over the 23 Cost-table rows; `verify_script_ownership.py` is not a row
above, so it has no cell to check); the full 84-row gate ran in **232.97 s** wall
(05:47:37–05:51:30 local) and its 82 row times sum to **576.0 s**, so the 12-row pool brings the wall
to 39.2% of the sum. The writers are the tail: `render_reports.py` 21.8 s, the plain render as
the gate row, `extract_links.py` 17.0 s,
`extract_formalization_deps.py` 7.3 s (the 122,458-file walk under
`lean/OAI/` is paid once per cache key, so a warm run reads records), `build_index.py` 7.7 s.

`verify_conjecture_standing.py` is the one checker the list kept outside its loop: it ran plain only,
so its six mutants were never run by the gate. Measured 2026-10-09 by hand — `mutants 6  uncaught
0 []`, exit 0 — `math-8ou` added the `--mutant` invocation, which is why the count read 63 and not
62; the pass that extracted its self-tests removed that invocation again. `math-a0r.6.2` added
`check_index_links.py --mutant` for the same reason — its 21st mutant is a mutation of
`notes/development/index-links.md`'s own prose, which only a self-test can catch — and `math-3la`
added `measure_checker_needles.py`, `measure_checker_reads.py``, so the count is **79** after `math-o3a.1` added
`verify_fleet_design.py` plain and with `--mutant`, `math-o3a.6.1` added
`verify_cache_promotion.py` plain and with `--mutant`, and the rows `math-unv`'s
scheduler and `math-o3a.5.2`'s `--both` collapse added took the list to what the `ROWS` array
carries. That `--mutant` row is now the `run_tests.py` row for `notes/scripts/tests/test_index_links.py`,
and the prose mutant is `verify_page_sync.py`'s, so the row count did not move. The count is read
from the array, not from the history: **10** writer rows, **43**
report-only rows, **24** checker invocations.

`verify_script_ownership.py` — this page's own checker — is not in the table: a checker cannot list
itself as its input. It is the 23rd checker and the 67th script; the run counts **65** scripts
because it excludes itself.

## The shared package: `catlib/`

`notes/scripts/catlib/` holds the joins the extractors share, so a join is written once. It is 17
modules, not scripts: `paths.py` (the repo-root constants, `rel()`, `owner()`, `read_text()`),
`tsv.py` (the four TSV writer shapes), `promote.py` (the promotion protocol — the `L1` and `ARTIFACTS`
registry, `key_for()` for the builder's digest key, `promote()` which caches the bytes under the key
and then writes the same bytes onto the tracked path, and `cached_text()`), `records.py` (the
digest-keyed record store — `key()` over the five `git rev-parse HEAD:<path>` tree digests, the
builder's source, its L1 texts and its args, truncated to 32 hex; `manuscript_store()` reads the
749-row per-manuscript record set under `.qwen/cache/records/<key>/`, and `cached(KEY, "name",
builder)` builds a record once, lands it atomically, and reads it back), `atomic.py` (the atomic write primitive —
`write_atomic()` writes through a sibling temp name, fsyncs, then moves the temp onto the target, so
a crash never leaves a half-written tracked file; every writer's write site goes through it, which is
why the fleet's atomicity grep reads 1 match, not 9), `overview.py` (the `\resultentry` parse),
`ledger.py`
(`notes/gen/tables/catalog.tsv` and the claim-shape rules), `preprints.py` (the 749 dirs versus the 719 listed
manuscripts), `text.py` (the six normalizers), `yaml.py` (`main_results_entries()`, the scope-note
spans, the Lean-tree file list), `anchors.py` (the `path:line` anchor grammar, the fenced-block scan
and the nearest-preceding-anchor read the page checkers share), `bib.py` (the `.bib` entry parse, the
title normalizer, the citation-key read, the pair window and the component scan), `measure.py` (the
writer-side measurement API — the ledger and release counts as ints, sets and lists, with no report
formatting; checkers deliberately do **not** import it, because a checker that re-derives a count
through the page's own code proves nothing), `render.py` (the page-vs-writer comparison —
`diff_problems()` reports where a committed page differs from the bytes `render_reports.py` renders
for it, and `selftest_problems()` names the four cases it must report: identical, changed digit,
inserted line, deleted line), `summaries.py` (the Sources-table row, the `[Sn:line]` marker, the
page's manuscript roots, the lenient `errors="replace"` read of a declared source that may be a
compiled PDF, and the overview's manuscript-ownership map) and `templates.py` (the report-template
registry — `ALL_PAGES`, the writer's per-page `POPULATIONS` and `LABELS` slot dicts,
`checker_needles`, `group_labels`, `SPLIT_LABEL`) and `__init__.py`. A
script run as `python3 notes/scripts/foo.py` has `notes/scripts` on `sys.path`, so it imports them as
`from catlib import ...` with no path boilerplate.

**66** of the **74** scripts call the package, measured by the rule `^[ \t]*(from|import) catlib` over
each script's own source: **12** `extract_` (all of them), **6** `build_` (all), **14** `measure_`
(all 20 but `measure_needles.py`, `measure_proof_density.py`, `measure_topics.py` and the three render
probes, which reach `render_reports` directly), **2** `check_` (`check_index_links.py` and
`check_summary_manuscripts.py`),
**23** `verify_` scripts (all of them), plus `render_reports.py`, `seed_quotes.py`, `triage_t0.py`,
`read_manuscript.py`, `compare_abstracts.py`, `locate_summary_quotes.py`, `run_tests.py` and `gate.py`.
The eight scripts that do not are `check_gate_budget.py`, which reads the gate wall log and the gate row TSV
directly; `dump_template_slots.py`, which reaches the slot dict through
`render_reports.py` and never touches the registry; `measure_needles.py`, which parses the test files
with `ast` and reads no corpus; `measure_proof_density.py` and `measure_topics.py`, which read the
Sources table and the vocabulary directly; and `measure_render_phases.py`, `measure_render_pool.py`
and `measure_render_processes.py`,
which import `render_reports` and get the joins through it. The two summary-page readers
`check_summary_manuscripts.py` and `locate_summary_quotes.py` were
moved off `verify_summaries.py` onto `catlib/summaries.py` by `math-6s7.1` — a checker serving as a
library is the shape that port broke, and `verify_summaries.py` now has **0** importers. `math-lon.2.5` ported the last two checkers,
`verify_upstream_history.py` and `verify_summaries.py`, and the **22** `duplicate-code` findings
did not move (measured 2026-10-09 with `--enable=R0801` over 55 files, every cluster reported against
`catlib/anchors.py`). What deliberately stays outside the package is a **read
shape**, not a parse: `verify_upstream_history.py` reads `lean/formalization.yaml` and
`notes/gen/tables/catalog.tsv` from a **revision** through `git show <rev>:`, so the package gained
`parse_yaml_text` / `parse_overview_text` / `read_rows_from_text` — text-level cores its disk-level
`parse_yaml` / `parse_overview` / `read_rows` delegate to — rather than a git reader; and
`build_index.py` keeps its own `TRIPLE` regex. The summary-page read is in the package:
`catlib/summaries.py` carries the Sources-table row, the `[Sn:line]` marker, the page's manuscript
roots, the lenient `errors="replace"` read of a declared source that may be a compiled PDF, and the
overview's manuscript-ownership map. `math-6s7.2` put the verification-bundle walk in
`catlib/preprints.py` (`bundle_of` / `bundle_files` / `main_command` / `entry_point`, with
`MANIFESTS` and `SCRIPT_PREFIX`), which took the two `extract_verification_*` scripts onto the
package and took `extract_verification_dirs.py` off `build_catalog`; the page checker and the
renderer were importing the extractor's private `PRE` / `entry_point` / `main_command` and now
import the package's, so the six-rule entry-point classification has one vocabulary. What stays in
the extractor is the report shape: the numbered heading/command/scope lines, the README-section
reconciliation, and `families_by_slug`. `math-6s7.3` put the T0 first-match chain
(`T0_BUCKETS` / `bucket_of`), the chain edges and the companion-word set in `catlib/ledger.py`, and
the release-labelled bib-edge shape in `catlib/bib.py`, so `extract_t0_chains.py` stops importing
`extract_links.py` and `extract_subfinding_pairs.py` — the dependency shape this epic exists to
remove, and the one cycle that leaves the cyclic-import count — while `triage_t0.py` and
`verify_named_conjectures.py` read the bucket rule from the package. The bucket **prose** stays in
`triage_t0.py`: the order and the tags are a join, the wording is the report's labels.
`math-6s7.5` put the report-template registry in `catlib/templates.py` — `ALL_PAGES` (page →
checker, 17 entries), the writer's per-page `POPULATIONS` and `LABELS` dicts, `checker_needles`,
`group_labels` and `SPLIT_LABEL` — so `build_report_templates.py`, `measure_checker_needles.py`, `measure_checker_reads.py`` and
`measure_templates.py` read one registry instead of three routes to the builder, and
`measure_templates.py`'s `all_pages_anchor()` points at the package. What stays in the builder is
the writer path: the whitespace-flexible locate, the split at the page's own line breaks, the
raw-block wrapping, and the `git show HEAD:<page>` read, which is a revision the package does not
own. `dump_template_slots.py` prints the writer's slot dict through `render_reports.py` and never
touched the registry, so it is unchanged. `catlib/templates.py` imports the writer at module level
because its dicts are built from the writer's functions at import time, so a module the writer
imports must import the package only inside a function — `measure_templates.py`'s `registry()`
already does.

The package is not in the census below: the script population is `notes/scripts/*.py`, and
`catlib/` is 17 modules under that directory, so the population the census counts is **76** files.
The lint gate checks **79**, because the extracted checker self-tests live inside the tree
(`notes/scripts/tests/`, 3 files) and the trio over `notes/scripts/` recurses into it; the census
excludes them with the script tree, so they are not scripts.
(`.venv/bin/mypy notes/scripts/` prints the count it checked).

## The file census

| Population | Files | Owner |
|---|---|---|
| `notes/gen/index/` | **1,033** | generated — `build_index.py`; the 16 tables it renders land in `notes/gen/tables/` |
| `notes/gen/summaries/` | **164** | hand-written — the reading record: 163 family pages and the link-only index page `README.md` |
| `notes/data/` | **165** | the summary renderer's input: one data file per family page — the sources, quote spans and sections `build_summaries.py` renders `notes/gen/summaries/` from |
| `notes/templates/` | **27** | **6** hand-written index skeletons + **21** report templates built by `build_report_templates.py` |
| `notes/development/*.md` | **6** | hand-written in part: `summaries-workflow.md` is the resume protocol; `fleet-design.md`, `index-design.md` and `index-links.md` are report-fed pages `render_reports.py` renders and `templates.md` is generated by `build_report_templates.py`. `math-faz.3` moved them here from the top level. |
| `notes/development/upstream_history/` | **3** | hand-written — the record of each upstream merge, checked by `verify_upstream_history.py` |
| `notes/development/probe/` | **91** | the audit-hook probe records: the 2026-10-10 pair that proves the fleet's write modes, the 2026-10-11 writers/checkers pair that measures the purity population, the 2026-10-11 `render_reports.py` after-record that proves the render writes nothing, the 2026-10-12 `render_reports.py` record that captures the fleet census, the 2026-10-12 `render_reports.py` record that proves the writer's L1 names `notes/gen/tables/` as a tree after `math-faz.6` moved the tables out, the 2026-10-12 `extract_named_results.py` record that proves its L1 names the ledger at its `tables/` path, the 2026-10-12 `measure_templates.py` record that proves the census L1 names the index tree at its pre-move 1,049-file size, the 2026-10-12 `measure_templates.py` record that proves the census L1 names the 1,033-page index tree after the move, and the 2026-10-13 `build_index_db.py` record that proves the FTS builder's L1 is empty, the 2026-10-12 `seed_quotes.py` records that name `notes/reports/counterexample-tag.md`, `notes/reports/subfinding-pairs.md`, `notes/reports/t0-triage.md`, `notes/summaries/algebra/197-nonsofic-groups-and-group-ring-counterexamples.md`, `notes/summaries/algebraic-and-complex-geometry/032-the-rational-hodge-conjecture-for-cm-abelian-varieties.md`, `notes/summaries/combinatorics/159-quasipolynomial-bounds-for-arithmetic-progressions.md`, `notes/summaries/convex-and-metric-geometry/087-the-mahler-conjectures-and-symplectic-width.md`, `notes/summaries/mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md`, `notes/summaries/number-theory/001-milnes-rationality-conjecture.md`, `notes/summaries/number-theory/002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md`, `notes/summaries/number-theory/004-hilberts-tenth-problem-over-q.md`, `notes/summaries/number-theory/006-goldfelds-conjecture.md`, `notes/summaries/number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md`, `notes/summaries/number-theory/010-fontaine-mazur-modularity-at-the-prime-2.md`, `notes/summaries/number-theory/011-the-ford-konyagin-luca-conjecture-on-prime-predecessors.md`, `notes/summaries/number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md`, `notes/summaries/number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md`, `notes/summaries/number-theory/017-the-irrationality-exponent-of-pi-is-2.md`, `notes/summaries/number-theory/018-margulis-platonov-conjecture-over-global-fields.md`, `notes/summaries/number-theory/019-p-adic-section-conjecture.md`, `notes/summaries/operator-algebras/287-all-nonabelian-free-group-factors-are-isomorphic.md`, `notes/summaries/partial-differential-equations/362-global-smoothness-for-relativistic-vlasov-maxwell.md`, `notes/summaries/probability-and-statistical-mechanics/221-mezard-parisi-formula-for-diluted-spin-glasses.md`, `notes/summaries/theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md`, `notes/tables/catalog.tsv`, the 2026-10-13 `seed_quotes.py` records that name `notes/summaries/README.md`, `notes/summaries/convex-and-metric-geometry/101-the-sharp-simplex-conjecture-for-isotropic-constants.md`, `notes/summaries/dynamical-systems-and-ergodic-theory/147-the-near-boundary-birkhoff-conjecture.md`, `notes/summaries/functional-analysis/332-metric-markov-cotype-two-for-l1.md`, `notes/summaries/group-theory/258-gerstens-conjecture-for-one-relator-groups.md`, `notes/summaries/group-theory/259-a-group-without-fixed-price.md`, `notes/summaries/probability-and-statistical-mechanics/226-the-curve-scaling-limit-of-half-plane-double-dimers.md`, `notes/summaries/theoretical-computer-science/109-integer-multiplication-below-n-n.md`, `notes/summaries/theoretical-computer-science/136-quasilinear-pcp-for-ppad-conjecture.md`, the 2026-10-14 `seed_quotes.py` records that name `notes/summaries/differential-geometry/334-a-smooth-surface-metric-with-no-local-immersion-in-r-3.md`, `notes/summaries/differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md`, `notes/summaries/differential-geometry/344-metric-blaschke-conjecture.md`, `notes/summaries/differential-geometry/345-infinitely-many-closed-geodesics-on-spheres-and-three-manifolds.md`, `notes/summaries/differential-geometry/346-sharp-singular-set-bounds-for-stationary-integral-varifolds.md`, `notes/summaries/differential-geometry/347-counterexamples-to-stable-morse-fixed-point-bounds.md`, `notes/summaries/differential-geometry/348-einstein-four-manifold-classification-and-l2-gap.md`, `notes/summaries/differential-geometry/349-the-solomon-yau-least-volume-conjecture.md`, `notes/summaries/differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md`, `notes/summaries/differential-geometry/352-finite-time-singularity-of-calabi-flow.md`, the 2026-10-15 `seed_quotes.py` records that name `notes/summaries/algebra/195-a-complete-local-domain-without-a-small-cohen-macaulay-module.md`, `notes/summaries/algebra/196-a-torsion-free-group-algebra-with-zero-divisors.md`, `notes/summaries/algebra/198-a-counterexample-to-the-little-finitistic-dimension-conjecture.md`, `notes/summaries/algebra/199-counterexamples-to-conjectures-of-auslander-reiten-and-tachikawa.md`, `notes/summaries/algebraic-and-complex-geometry/039-nagatas-conjecture-and-maximal-seshadri-constants.md`, `notes/summaries/algebraic-and-complex-geometry/042-oka-classification-for-k3-surfaces-and-other-compact-complex-surfaces.md`, `notes/summaries/algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md`, `notes/summaries/algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md`, `notes/summaries/algebraic-and-complex-geometry/050-counterexample-to-griffiths-positivity-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/052-integrability-of-split-tangent-bundles.md`, `notes/summaries/convex-and-metric-geometry/088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md`, `notes/summaries/convex-and-metric-geometry/089-planar-and-bounded-treewidth-metrics-embed-into-l1.md`, `notes/summaries/convex-and-metric-geometry/098-a-negative-answer-to-the-lang-plaut-problem.md`, `notes/summaries/functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md`, `notes/summaries/functional-analysis/325-complete-crouzeix-conjecture.md`, `notes/summaries/functional-analysis/331-asymptotic-midpoint-uniform-convexity-without-asymptotically-uniformly-convex-renorming.md`, `notes/summaries/group-theory/254-classifying-spaces-and-geometric-obstructions-for-artin-groups.md`, `notes/summaries/mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md`, `notes/summaries/mathematical-logic/244-partition-principle-does-not-imply-choice.md`, `notes/summaries/mathematical-physics/274-moores-parity-conjecture-for-qac0.md`, `notes/summaries/real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md`, the 2026-10-16 `seed_quotes.py` record that names `notes/summaries/algebra/193-serres-intersection-multiplicity-conjecture.md`, `notes/summaries/algebra/195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md`, `notes/summaries/algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md`, `notes/summaries/algebra/199-counterexamples-to-conjectures-of-auslander-reiten-tachikawa-and-nakayama.md`, `notes/summaries/algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md`, `notes/summaries/algebra/201-a-counterexample-to-kuroshs-division-ring-problem.md`, `notes/summaries/algebra/202-blockwise-alperin-weight-conjecture.md`, `notes/summaries/algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md`, `notes/summaries/algebra/204-tensor-saturation-for-even-spin-groups.md`, `notes/summaries/algebra/208-finite-benson-etingof-ostrik-conjecture.md`, `notes/summaries/algebra/209-integral-counterexamples-to-gerstens-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md`, `notes/summaries/algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md`, `notes/summaries/algebraic-and-complex-geometry/037-sharp-ordinary-double-point-volume-gap.md`, `notes/summaries/algebraic-and-complex-geometry/038-fujitas-freeness-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/040-blochs-conjecture-for-complex-surfaces.md`, `notes/summaries/algebraic-and-complex-geometry/041-hyperkahler-syz-and-projective-space-bases.md`, `notes/summaries/algebraic-and-complex-geometry/043-p-w-for-fixed-determinant-moduli-spaces.md`, `notes/summaries/algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md`, `notes/summaries/algebraic-and-complex-geometry/048-a-characteristic-zero-counterexample-to-lipman-zariski.md`, `notes/summaries/algebraic-and-complex-geometry/050-a-counterexample-to-griffiths-positivity-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/052-tangent-bundle-splittings-and-universal-covers.md`, `notes/summaries/algebraic-and-complex-geometry/053-a-counterexample-to-pixtons-original-completeness-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/054-counterexamples-to-kuznetsovs-rationality-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/055-todas-gepner-conjecture-and-large-volume-stability.md`, `notes/summaries/algebraic-and-complex-geometry/057-campanas-abelianity-conjecture-and-special-varieties.md`, `notes/summaries/algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/062-lebrun-salamon-conjecture-and-projective-contact-classification.md`, `notes/summaries/algebraic-and-complex-geometry/063-generalized-mukai-conjecture.md`, `notes/summaries/algebraic-and-complex-geometry/064-constant-problem-for-surface-singularities.md`, `notes/summaries/algebraic-and-complex-geometry/065-virasoro-constraints-for-complete-intersections-and-projective-bundles.md`, `notes/summaries/algebraic-and-complex-geometry/067-campana-peternell-conjecture-in-dimension-six.md`, `notes/summaries/combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemeredi-bounds.md`, `notes/summaries/combinatorics/164-hindmans-finite-sums-and-products-conjecture.md`, `notes/summaries/combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md`, `notes/summaries/combinatorics/171-hypercube-ramsey-conjecture.md`, `notes/summaries/convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md`, `notes/summaries/convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md`, `notes/summaries/convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md`, `notes/summaries/differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md`, `notes/summaries/differential-geometry/338-yaus-uniformization-conjecture.md`, `notes/summaries/differential-geometry/339-katoks-entropy-rigidity-conjecture.md`, `notes/summaries/differential-geometry/340-a-counterexample-to-the-nearby-lagrangian-conjecture.md`, `notes/summaries/differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md`, `notes/summaries/differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md`, `notes/summaries/differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md`, `notes/summaries/differential-geometry/349-solomon-yau-least-volume-conjecture.md`, `notes/summaries/dynamical-systems-and-ergodic-theory/147-near-boundary-birkhoff-conjecture.md`, `notes/summaries/functional-analysis/332-metric-markov-cotype-two-for-1.md`, `notes/summaries/mathematical-physics/268-spin-one-haldane-gap.md`, `notes/summaries/mathematical-physics/270-threshold-and-positive-energy-bound-states-of-the-bfss-model.md`, `notes/summaries/mathematical-physics/274-moores-parity-conjecture-for-qac-0.md`, `notes/summaries/mathematical-physics/284-optimal-randomized-quantum-query-exponent.md`, `notes/summaries/number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md`, `notes/summaries/number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md`, `notes/summaries/number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md`, `notes/summaries/number-theory/017-irrationality-exponent-of-is-2.md`, `notes/summaries/number-theory/022-weak-inhomogeneous-duffin-schaeffer-conjecture.md`, `notes/summaries/number-theory/029-artins-primitive-root-conjecture-infinitude-for-every-base.md`, `notes/summaries/number-theory/030-modularity-over-imaginary-quadratic-fields.md`, `notes/summaries/number-theory/031-uchidas-conjecture-for-open-galois-homomorphisms.md`, `notes/summaries/operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md`, `notes/summaries/operator-algebras/300-popa-vaes-quadratic-strong-operator-paving-conjecture.md`, `notes/summaries/partial-differential-equations/366-planar-mumford-shah-regularity-conjecture.md`, `notes/summaries/partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md`, `notes/summaries/partial-differential-equations/375-de-giorgis-conjecture-in-dimension-eight.md`, `notes/summaries/probability-and-statistical-mechanics/226-double-dimer-cle-4-conjecture-in-the-half-plane.md`, `notes/summaries/real-and-complex-analysis/074-kakeya-in-three-and-four-dimensions.md`, `notes/summaries/real-and-complex-analysis/077-fourier-restriction-for-positively-curved-surfaces.md`, `notes/summaries/real-and-complex-analysis/078-three-dimensional-bochner-riesz-conjecture.md`, `notes/summaries/real-and-complex-analysis/079-sogges-local-smoothing-conjecture-in-dimension-three.md`, `notes/summaries/real-and-complex-analysis/080-sobolev-endpoint-in-carlesons-schrodinger-convergence-problem.md`, `notes/summaries/real-and-complex-analysis/086-an-l-3-bound-for-the-trilinear-hilbert-transform.md`, `notes/summaries/topology/304-hilbert-smith-conjecture-in-every-dimension.md`, `notes/summaries/topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md`, `notes/summaries/topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md`, `notes/summaries/topology/309-kervaire-invariant-problem-at-the-prime-three.md`, `notes/summaries/topology/310-quillens-conjecture-in-rational-homology.md`, `notes/summaries/topology/311-chais-invariant-ideal-conjecture.md`, `notes/summaries/topology/313-finite-generation-for-the-k-n-local-sphere.md`, `notes/summaries/topology/315-four-dimensional-singer-conjecture.md`, `notes/summaries/topology/316-curtiss-conjecture.md`, `notes/summaries/topology/319-counterexamples-to-the-hahn-wilson-conjecture-at-height-two.md`, `notes/summaries/topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md`, `notes/summaries/topology/321-a-counterexample-to-walls-finite-d-2-conjecture.md`, and the 2026-10-24 `seed_quotes.py` record that names `notes/summaries/theoretical-computer-science/103-derandomization-of-logarithmic-space-l-rl-bpl.md`, `notes/summaries/theoretical-computer-science/104-quasipolynomial-algorithms-for-mean-payoff-stochastic-and-parity-games.md`, `notes/summaries/theoretical-computer-science/105-2-to-1-games-conjecture-with-perfect-completeness.md`, `notes/summaries/theoretical-computer-science/106-hardness-of-coloring-three-colorable-graphs.md`, `notes/summaries/theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md`, `notes/summaries/theoretical-computer-science/112-beyond-the-square-root-exponent-for-depth-three-circuits.md`, `notes/summaries/theoretical-computer-science/113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md`, the 2026-10-15 `render_reports.py` and `measure_templates.py` records that name the accent-folded index tree, the 2026-10-15 `render_reports.py` and `measure_templates.py` records that name the census template the scripts page added, and the 2026-10-15 `render_reports.py` and `measure_templates.py` records that name the findings template |
| `notes/gen/tables/*.tsv` | **25** | **25** generated, **0** hand-authored — 9 written by the ledger scripts and 16 rendered by `build_index.py` since `math-faz.6` |
| `notes/gen/reports/*.md` | **23** | **15** generated — the report-fed pages `render_reports.py` renders; **8** hand-written. **11** with a checker, **12** without. `math-faz.4` moved them here from the top level. |
| `notes/*.md` | **1** | `notes/README.md`, the entry point — hand-written, no checker |
| `notes/` total, scripts excluded | **1,538** | — |

The generated TSVs are the **25** the writer set writes: the 9 named writer targets and the 16 tables
`build_index.py` stages into `notes/gen/tables/`. The two hand-authored tables are:

| Table | Why it is hand-authored |
|---|---|
| `notes/data/topics.tsv` | The curated topic vocabulary. `measure_topics.py --check` re-measures its 92 rows and exits 1 when a recorded count drifts; `build_index.py` reads it and renders `notes/gen/tables/topics-rendered.tsv`. A generated file inside `notes/gen/index/` is overwritten by the next render, which is why the vocabulary lives outside that tree; `math-faz.6` put the render in `notes/gen/tables/`, where the vocabulary and the render sit side by side. |
| `notes/data/conjecture-standing.tsv` | The training-data prior. Its `standing_prior_2025` column is the assistant's memory at an early-2025 cutoff, self-rated by `prior_confidence`; no script can derive a memory, and `verify_conjecture_standing.py` checks the rows against the ledger and `overview.tex` rather than regenerating them. |

Across the **24** prose pages — the 23 report pages and the entry point — **19** with a checker, **5** without.
The 5 pages with no checker are `notes/README.md`,
`notes/gen/reports/conjecture-standing.md`,
`notes/gen/reports/counterexample-tag.md`, `notes/gen/reports/resolution-tag.md` and `notes/gen/reports/t0-triage.md`. Their counts
are reproduced by the report-only
scripts above; nothing verifies them against the page. `notes/development/summaries-workflow.md` is
the one page under `notes/development/` with no checker — it is the resume protocol, a procedure, not a
count, and the census row above counts it. `notes/linting.md` was the seventh until
2026-10-12: it was the one page in that set whose counts came from tools outside this tree — the three
linter commands, run from the untracked `.venv/` — and because every count it carried is re-derivable
by running a rule alone, and every exemption reason is already a comment in `ruff.toml`, `mypy.ini`
and `.pylintrc`, the page was a manual transcription of what the linters print. It is deleted; the
annotation backlog its strict probe measured is queue state, so it moves to bd.
The five pages `notes/development/index-links.md`, `notes/gen/reports/links.md`, `notes/gen/reports/names.md`,
`notes/gen/reports/proof-density.md` and `notes/gen/reports/topics.md` were in this set until `math-o3a.3`: their render diff
was carried by a report-only script that read a page it did not verify, and `verify_page_sync.py`
owns that check now.

## One basename is shared

Measured over the top level and the index tree: **1** shared basename — `README.md`.
`notes/README.md` is the ledger readme and `notes/gen/index/README.md` is the index entry point, so that
pair is harmless.

The tree used to carry a second, load-bearing collision. `notes/data/topics.tsv` is the hand-authored
vocabulary and `notes/gen/index/topics.tsv` was generated from it, with adjacent schemas —
`term pattern fams title abstract scope path status` in both, then `note` in the hand-authored file
and `page` in the rendered one — so a reference to `topics.tsv` without its directory was ambiguous,
and a `notes/**/topics.tsv` glob read both. The rendered table is now
`notes/gen/index/topics-rendered.tsv`, which says which layer it measures, and the vocabulary moved to
`notes/gen/tables/` on 2026-10-11, so the two names cannot collide again. `measure_topics.py` and
`AGENTS.md` both name the vocabulary; `build_index.py` reads it and writes the rendered table.

The index tree and the summaries tree share **164** page slugs — the families that carry both a rendered
page and a reading summary, which is the pairing the index reports, plus `README.md`, which each tree
carries as its own entry point.

## Naming coverage

`notes/README.md`'s command block named **34** of the 74 scripts before this pass. 40 are named
nowhere in the repo at the pinned baseline: `build_report_templates.py`, `build_index_db.py`,
`verify_tsv_quoting.py`,
`check_summary_manuscripts.py`, `check_gate_budget.py`,
`extract_citations.py`, `gate.py`, `locate_summary_quotes.py`, `measure_anchor_blocks.py`,
`measure_checker_needles.py`, `measure_checker_reads.py``, `measure_faithfulness.py`, `measure_import_layout.py`,
`measure_links_phases.py`, `measure_move_surface.py`, `measure_needles.py`, `measure_open_probe.py`,
`measure_render_phases.py`, `measure_render_pool.py`, `measure_render_processes.py`,
`measure_scan_candidates.py`, `measure_templates.py`,
`read_manuscript.py`,
`build_summaries.py`, `extract_summary_data.py`, `fix_blank_cites.py`, `render_reports.py`, `seed_quotes.py`, `verify_citations.py`, `verify_faithfulness.py`, `verify_findings.py`,
`verify_fleet_design.py`, `verify_named_conjectures.py`, `verify_page_sync.py`, `verify_upstream_history.py`,
`dump_template_slots.py`, `verify_cache_promotion.py`, `measure_gate_rows.py`, `measure_check_calls.py` and `run_tests.py`. The first four are the report-template
builder this pass promoted plus the `notes/gen/summaries/` reading tooling and the citation extractor, so
the summaries tree and `notes/gen/reports/citations.md` carried measurements whose generating command no document
named; `read_manuscript.py`, `build_summaries.py` and `extract_summary_data.py` are the rest of that reading tooling;
`verify_citations.py`, `verify_findings.py` and `verify_named_conjectures.py` are the checkers for
`notes/gen/reports/citations.md`, `notes/gen/reports/findings.md` and `notes/gen/reports/named-conjectures.md`, so three pages carried
measurements whose checker no document named; `verify_upstream_history.py` is the tooling behind
`notes/development/upstream_history/`, the pages that record each upstream merge, which moved under `notes/` on
2026-10-10 and are inside this page's census; `measure_templates.py` is the census behind `notes/development/templates.md`, added by
the pass that added that page; `measure_checker_needles.py`, `measure_checker_reads.py`` is the per-checker needle probe the
checker-coverage bead promoted; `dump_template_slots.py` is the slot dump that prints the same dict the census measures, promoted by `math-a0r.7`; `verify_fleet_design.py` is the checker for `notes/development/fleet-design.md`, promoted by `math-o3a.1` together with the two probe records it parses; `verify_page_sync.py` is the checker `math-o3a.3` created when the five sync passes left the writer fleet, so the pinned baseline predates it; `measure_open_probe.py` is the audit-hook probe `math-o3a.3.4` promoted from `.qwen/tmp/a11_open_probe2.py`, so the pinned baseline predates it too; `measure_faithfulness.py` is the faithfulness measurement promoted from `.qwen/tmp/faith_probe.py` by the pass that added `notes/gen/reports/formalization-faithfulness.md`, and `verify_faithfulness.py` is that page's checker, so the pinned baseline predates both; `render_reports.py` is the renderer for the nineteen report-fed pages; `verify_cache_promotion.py` is the checker `math-o3a.6.1` created for the promotion protocol, so the pinned baseline predates it; `measure_anchor_blocks.py` and `measure_move_surface.py` are the two notes-move probes `math-faz.1` promoted from `.qwen/tmp/notes_block_probe.py` and `.qwen/tmp/notes_move_probe.py`, which price a directory move before it happens and re-check the mention counts after it, so the pinned baseline predates both; and `gate.py` is the dependency scheduler `math-unv` wrote to replace `notes/scripts/gate.sh`, so the pinned baseline predates it; `seed_quotes.py` is the quote-spec seeder this pass promoted from `.qwen/tmp/seed_quotes4.py`, which seeds `notes/gen/tables/quotes.tsv` from `notes/gen/reports/subfinding-pairs.md`'s pair lines and resolves each spec back against `overview.tex`, so the pinned baseline predates it; `run_tests.py` is the seam that runs the extracted checker self-tests through the venv's pytest, promoted by the pass that extracted `verify_scope_exclusions.py`'s, so the pinned baseline predates it; `build_index_db.py` is the SQLite FTS5 builder `math-u41.6` wrote, which lands the keyed record and the untracked database, so the pinned baseline predates it.
All 73 are named here and in the command
block. "Before this pass" is
pinned to the commit that created this page, read at its parent, not to `HEAD`: `HEAD` moves every
time this page is edited, so a check keyed to it re-pins the baseline on each edit, and the naming
that pass added then reads as already present and the recorded gap vanishes.

## Scratch: the fourth class

The three tables above cover `notes/scripts/*.py`. The fourth class the inventory records is the
scratch: the probes, drafts, baselines and gate reports that a session writes and that never become
repo content. The rule is a location rule — **scratch lives under `.qwen/tmp/`, a permanent script
lives under `notes/scripts/`** — and `.gitignore` keeps `.qwen/` (other than `.qwen/skills/`) out of
git, so nothing in the scratch tree is tracked and no checker here reads it. A probe that answers one
question stays where it is and is deleted; a probe that a later bead re-runs is promoted, gets a row
in the tables above, and only then gets a gate command.

Measured 2026-10-09 over `.qwen/tmp/` **after** the `math-8ou` cleanup: **345** top-level files,
**7,121** files including subdirectories, **14** subdirectories. By top-level suffix: **222** `.txt`,
**43** `.md`, **19** `.tsv`, **1** `.py`, and **0** in every other suffix — the tree is now reports,
drafts, baselines and index snapshots, with one script left in it. The largest trees are gate and
render snapshots — `reports/` **341**, `idx_pre_sweep/`, `idx_run1/` and `idx_run2/` at **1,052** each,
`index-run1/` **1,049**, `index_run1/` and `index_run2/` at **1,050** each, `lon2/` **85**, `msgs/`
**65**, `lon1/` **63**.

Before the cleanup the same measurement read **367** top-level files, **7,116** total, and a top-level
suffix histogram of **220** `.txt`, **70** `.py`, **43** `.md`, **19** `.tsv`, **3** `.sh` and **12**
files in the remaining suffixes. `math-8ou` closed that gap: the gate list and its driver,
`gate.sh` and `gate_driver.sh`, are promoted to `notes/scripts/gate.sh` and
`notes/scripts/gate_driver.sh` — a test that lives in an untracked directory is not a test the next
session can run, and the driver header now carries the one-driver and group-kill rules the gate runs
need. `math-unv` replaced `notes/scripts/gate.sh` with `notes/scripts/gate.py`, the dependency
scheduler, so the promoted pair is now the driver plus the scheduler. The **70** one-off `.py` probes are deleted (the `hqd5_probe*.py` family at 16, the `e8k_*.py`
lint-fix family at 8, the family-`001` summary builders at 11, the `probe_*` set at 6, the
`0h2`/`extra` generators at 4, the marker/layout fixers at 4, the citation-needle printers at 2, the
conditional-anchor checker `check_conditional_anchors.py`, and the single-purpose probes `measure_links.py`, `measure_subfindings.py`, `title_variants.py`,
`upstream_probe.py`, `yaml_probe.py`, `topo.py`, `thms.py`, `show.py`, `core_all.py`,
`find_core_only.py`, `cand_closure.py`, `gen_axioms.py`, `lint_anchors.py`, `port_nc.py`,
`drop_syspath.py`, `build_scope_page.py`, `fix_topics.py`, `fix_topics_md.py`), together with
`elab.sh` and the **12** probe outputs it left behind (`axioms.lean`, `axioms.log`, `axioms.olean`,
`check.lean`, `check.olean`, `elab.log`, `hqd5_quotes.json`, `names.json`, `leanout.tmp.1683434`,
`0h2_skel.err`, `cit1.err`, `cx2a.err`). The four `/tmp` trees `stage5/`, `portcheck/`,
`portcheck2/`, `pprobe/` and the six `/tmp` one-offs `e402_probe.py`, `e402_probe2.py`,
`lint_anchors_scratch.py`, `lint_stage4.txt`, `lint_stage4b.txt`, `port_check2.sh` are deleted too —
`/tmp` is outside the rule's location and outside the repo, so a script written there is a script
whose outputs cannot be re-measured.

Measured 2026-10-10 over `.qwen/tmp/` **after** the `math-3la` cleanup: **403** top-level files,
**136,180** files including subdirectories, **5** subdirectories. By top-level suffix: **344** `.txt`,
**52** `.md`, **20** `.out`, **19** `.tsv`, **3** `.md5`, **2** `.log` and **1** each `.patch`,
`.pat`, `.diff` — **0** `.sh` and **0** `.py`, which is the rule's own endpoint: a driver a later pass
re-runs lives under `notes/scripts/`, and the scratch tree keeps outputs. The file total is one
hardlink tree, not a working set: `ledger_bump_copy/` carries **135,177** of the **136,180** — the
`cp -al` copy `simulate_ledger_bump.sh` builds to run the writer chain against a bumped
`overview.tex`, whose entries share inodes with the repo, so it costs inodes and not disk. Excluding
it the tree is **1,003** files. The working trees are `reports/` **438** (gate and render snapshots),
`msgs/` **159** (commit messages and close notes) and **52** top-level `.md` drafts. The
`math-a0r.7` cleanup deleted **49** one-shot entries and **20** trees (`proof_v6`–`proof_v10`,
`render_proof_cc`, `render_proof_readme`, `idx_pre_sweep`, `idx_run1`, `idx_run2`, `index-run1`,
`index_run1`, `index_run2`, `leanout`, `lon1`, `lon2`, `head`, `esp`, `close`, `a0r5`,
`__pycache__`) and the superseded probes the promotion replaced — `a63_two_renders.sh` and
`a63_dump_slots.py` by `two_render_proof.sh` and `dump_template_slots.py`, `a63_lint.sh` by
`notes/scripts/lint_scripts.sh`, `a64_demo.sh` and `a64_sed.txt` by `simulate_ledger_bump.sh`,
`a63_measure_templates*.py` by `notes/scripts/measure_templates.py`, and `a62_lines_probe.py`, which
the bead rejects — plus the `a64_copy/` demo tree. The `math-3la` cleanup deleted **10** more: the
seven `a7_*` one-shots (`a7_apply.sh`, `a7_bump_run.sh`, `a7_il2_waiter.sh`, `a7_il_fix2.sh`,
`a7_promoted_run.sh`, `a7_proof.sh`, `a7_tpl_rebuild.sh`), `a8_lint.sh` by
`notes/scripts/lint_scripts.sh`, `a8_probe.py` by `notes/scripts/measure_checker_needles.py`, `measure_checker_reads.py``, and
`a8_proof_chain.sh`, deleted only after its run printed `CHAIN_DONE`. The top-level count falls by
**10** while the file total falls by **8**, because two of the deleted files were hardlinks whose
twins live in `ledger_bump_copy/`.

The scratch tree is not a record. `.qwen/tmp/n5d3-draft.md` is a working draft whose tail is the
state a compacted session resumes from, and `.qwen/tmp/canonical_counts.md` is the count sheet the
gate reports are checked against; both are untracked, and the findings they carry are moved into
tracked files under `notes/` before the bead that produced them closes.

## Not checked

- **The checker proves ownership, not byte-sync.** Nothing asserts that a file under `notes/gen/index/`
  equals what `build_index.py` currently renders. The assertion covers the cache half: the bytes under
  the key equal the bytes on the tracked path, and `git status` compares the tracked path with `HEAD`.
  A hand-edit to a rendered page survives until a checker's needle happens to break.
- `build_index.py` sweeps its own tree: it tracks every path its `write()` helper emits and, at the end
  of `main()`, unlinks any `notes/gen/index/**.md` or `**.tsv` it did not write, then removes empty
  directories and prints `stale swept N files [...]`. The realized case is the 2026-10-07 merge: family
  034's title changed, so its old-slug page survived as an orphan whose manuscript table pointed at the
  three withdrawn directories — 6 broken links, found only by `check_index_links.py`. Two name pages
  (`cech`, `kunneth`) went the same way; the sweep removed 3 files. Renaming the rendered topic table is
  the older case — `notes/gen/index/topics.tsv` survived the rename and was deleted by hand. Page counts are
  measured consistent: **1,034** `.md` on disk against the **1,034** the render report claims.
- The sweep is probe-verified on both branches (2026-10-09, `math-a0r.1`): a planted
  `notes/gen/index/names/zzz-sweep-probe.md` prints `stale swept 1 files ['names/zzz-sweep-probe.md']` and
  is gone after the run; a planted page inside a new directory prints `empty dirs removed 1` and the
  directory is gone too; both runs leave `git status` clean under `notes/gen/index/`. So `stale swept 0`
  on a clean tree is a measured negative, not an untested branch — which is what makes the templating
  epic (`math-a0r`) safe to start: templates render a tree that sweeps, and a tree that cannot shed an
  old-slug page would freeze that page into the template set.
- The idempotence gate for `build_index.py` is run 2 against run 3, not run 1 against run 2: the first
  run after a corpus change prints the sweep line with the files it removed, the second prints
  `stale swept 0 files []`. Diffing run 1 against run 2 reports the sweep as drift.
- The writer rule reads path constants and write calls. A write built from a computed path (a variable
  assembled at runtime) is not found by it, so a script that writes only through a path it assembles
  from its input is filed under report-only even when it writes a tracked tree.
- The report-only table records which page a report feeds as stated in that page and in `AGENTS.md`.
  It is not derived from the report text, so a page that stops quoting a report keeps its row here.
- **A needle can match nothing and the run stays green.** `verify_upstream_history.py`'s `SLUG`
  pattern required a trailing `/` inside the backticks **and** a 3-letter month, while the corpus
  writes full month names only (`September` 576, `October` 172 over the **749** `preprints/` dirs), so
  it matched **0** tokens on the three pages it checks — `notes/development/upstream_history/2026-10-07_3414888.md`
  carries **14** backticked manuscript-slug tokens of that shape, written without the slash. The run
  exited 0 because nothing was asserted, and a slug renamed to one the release does not name was not
  caught. `math-lon.2.5` ported the file and left the pattern as it is, because its acceptance is
  byte-identical gate reports. `math-cg1` fixed both halves (slash optional, full month names: the
  needle now matches the **14** tokens and **0** on the other two pages), added the `slug rename`
  mutant (**13** → **14**, needle `": slug '"` — the table pass reports the same fact as
  `table: '…' is not a preprints/ directory`, so a shared needle cannot tell the two passes apart),
  and made the report print the slug count: a run that matches **0** is a problem, not a green result.
- Nothing in `lean/` is built, so no generated artifact here is a verification of a formalization.
