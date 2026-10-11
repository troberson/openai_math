# Scripts and generated files

Measured 2026-10-11 by `python3 notes/scripts/verify_script_ownership.py` — report-only, it writes
nothing, and every count below is re-derived by that run. The page answers one question: for each of
the **1,138** files under `notes/` (the scripts excluded), which is whose bytes. A generated file is
changed by editing its generator and re-rendering; a hand-written file is edited directly. Ownership
is per file, and the checker exits 1 on a file no rule owns.

It is also the script inventory. Every script under `notes/scripts/` is listed once, in one of three
classes — writer, report-only, checker — with what it writes and the command the gate runs for it, and
the fourth class, the scratch a session writes outside the tree, is recorded by rule rather than by
file. The classes partition the **55** scripts: **10** writers, **22** report-only, **22** checkers,
and `verify_script_ownership.py` itself, which is the 23rd checker and is not listed in its own table.

## The split: 10 write, 44 write nothing

The writer set is derived from the scripts' own source, not from this page: a script is a writer when
a path constant rooted at `notes/` appears on the left of `.open(..., "w")` or `.write_text(...)`,
plus the tree case — a `notes/index` constant reached through the module's own `write()` helper — and
plus one hop: a receiver built from a module constant (`out = TPL_DIR / (name)`, then
`out.write_text(...)`) is owned by that constant's directory, which is how a writer that names a
directory rather than a file stays visible. The fourth rule is the package-write case: a
`write_atomic(CONST, text)`, `stage(CONST, text)` or `promote(CONST, key, text)` call whose first
argument is a `notes/` path constant, an alias of one, or a local built from one, is owned by that
constant — this is how a writer whose write moved into `catlib.atomic` or `catlib.promote` stays
visible, since the write call itself is no longer in the script. The fifth rule subtracts the
self-test: a module-level
`mutants` / `mutant_test` / `selftest` body is blanked before the write calls are read, because a
self-test writes the page it checks only to mutate it and restores the bytes it read in the `finally`
— `verify_script_ownership.py` does exactly that, in three branches (the page it checks, `notes/scripts/README.md`, and `notes/templates.md`), so its normal run writes nothing and it stays in the checker class. `check_index_links.py` and `measure_proof_density.py` were this rule's examples; `math-o3a.3` moved their sync pass into `verify_page_sync.py`, which mutates page text in memory, so neither script carries a write call any more. That rule
finds **10** writers over **54** scripts.

### Writers

| Script | Writes | Gate | Report feeds |
|---|---|---|---|
| `build_catalog.py` | `notes/catalog.tsv` | single run; cached bytes == promoted bytes under the key | `notes/README.md`, `notes/findings.md` |
| `build_sources.py` | `notes/sources.tsv` | single run; cached bytes == promoted bytes under the key | `notes/sources.md` |
| `build_index.py` | `notes/index/` | single run; cached bytes == promoted bytes for all 1,049 files | `notes/index-links.md` |
| `compare_abstracts.py` | `notes/abstracts.tsv` | `--tsv` only; single run; cached bytes == promoted bytes under the key | `notes/abstracts.md` |
| `extract_formalization_deps.py` | `notes/formalization-deps.tsv` | single run; cached bytes == promoted bytes under the key | `notes/dependency-drift.md` |
| `extract_links.py` | `notes/links.tsv` | single run; cached bytes == promoted bytes under the key | `notes/links.md` |
| `extract_subfindings.py` | `notes/subfindings.tsv` | single run; cached bytes == promoted bytes under the key | `notes/subfinding-pairs.md` |
| `render_reports.py` | `notes/README.md`, `notes/abstracts.md`, `notes/dependency-drift.md`, `notes/index-design.md`, `notes/index-links.md`, `notes/links.md`, `notes/named-results.md`, `notes/names.md`, `notes/proof-density.md`, `notes/sources.md`, `notes/verification-dirs.md`, `notes/scope-exclusions.md`, `notes/topics.md`, `notes/t0-chains.md`, `notes/subfinding-pairs.md`, `notes/counterexample-crosscheck.md`, `notes/formalization-faithfulness.md`, `notes/templates.md` | single run; cached bytes == promoted bytes for all 18 pages | the eighteen report-fed pages |
| `build_report_templates.py` | `notes/templates/report` | not in `gate.sh` — it reads each page with `git show HEAD:`, so a gate run would rewrite templates from committed bytes; run explicitly with 0 args (all eighteen pages) or 2 (one page) after a writer's slot dict changes | the eighteen page templates; the registry, slot dicts and needle derivation it reads are in `catlib/templates.py` |
| `measure_open_probe.py` | `notes/probe` | not in `gate.sh` — a record carries a wall time per target, so a run-1/run-2 byte diff of a record is a timing artifact, not a proof; run explicitly over the purity and amplification targets, appending stdout to build a multi-target record | the two probe records `verify_fleet_design.py` parses |

Six writers emit one TSV each. `build_index.py` is the one-to-many case: it renders **1,049** files —
**1,033** `.md` pages and **16** `.tsv` tables. `render_reports.py` renders the eighteen report-fed pages
from the templates `build_report_templates.py` builds from the committed page and the slot dict that
writer supplies. `compare_abstracts.py` is the conditional case: its
default run writes nothing and only `--tsv` touches `notes/abstracts.tsv`.

All **10** writers take `--check-only`: the run does its full measurement, prints its report, and writes
nothing. Measured 2026-10-11 by running each writer plain and then with the flag — the report is
identical in both runs (the write announcement is the only line that differs) and
`git status --porcelain` is unchanged by the flagged run. `gate.sh` runs the writers plain; the read-only
pool `math-o3a.5.2` adds is the block that runs with the flag, which is why the flag comes first.

All ten writers write through `catlib/atomic.py`, so a crash never leaves a half-written tracked
file. The single-file writers use `write_atomic()`, which lands bytes on a sibling temp name in the
same directory, fsyncs, and moves the temp onto the target. The three multi-file writers
(`build_index.py`, `render_reports.py`, `build_report_templates.py`) use `Staging(name)`: `stage()`
lands bytes under `.qwen/cache/staging/<name>/`, which the `.qwen/*` rule in `.gitignore` keeps
untracked, and records the tracked path; `promote()` moves every staged slot onto its tracked path.
A writer calls `promote()` only after its own reconciliation lines have printed, so killing a writer
mid-run leaves the tracked tree exactly as it was — the proof is `build_index.py` killed mid-run in
the 1,049-file case with `git status --porcelain` clean.

Writers import each other, so a generated file's bytes are not a function of one script.
`build_index.py` imports `build_catalog`, `measure_topics`, `measure_names`,
`check_index_links` and `jinja2` (the index page text lives in `notes/templates/*.j2`, the seventeen
report-fed page skeletons in `notes/templates/report/*.j2`);
`extract_links.py`, `extract_subfindings.py`, `check_index_links.py`, `measure_names.py` and
`measure_topics.py` all import `build_catalog`;
`measure_index_sizes.py` imports `check_index_links` inside its link-check function
(`measure_index_sizes.py:118`), not at module scope. Counted over `notes/scripts/*.py` as a script
that imports the module (`import X` or `from X`, the module itself excluded), `build_catalog.py` has
**12** importers, `build_sources.py` **2** (`verify_sources.py` and `render_reports.py:52`, which
imports it at module scope; `read_manuscript.py` names it in a docstring, not in an import) and
`verify_summaries.py` **0** — `math-6s7.1` moved the page parse to `catlib/summaries.py`, so
`locate_summary_quotes.py`, `refresh_summary_line_counts.py` and `verify_scope_exclusions.py` import
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

The other **44** scripts write nothing. **22** of them print the report a page's counts come from.
The Gate column is the invocation the gate list runs: `notes/scripts/gate.sh`, which runs **76**
invocations — the **8** gated writers (the two writers it does not run are `build_report_templates.py`
and `measure_open_probe.py`, each for the reason in its own row), the 22 gated report-only rows (including `check_summary_manuscripts.py`
and `locate_summary_quotes.py`, and `check_index_links.py` twice — plain and with `--mutant`, since
`math-a0r.6.2` gave its self-test a prose mutant that only the gate can run), and **46** checker
invocations: each of the 22 checkers plain and
with `--mutant` (**44**), plus `verify_conjecture_standing.py` plain and with `--mutant` (**2**) — in
class order, not in the order the rows sit; it prints one line per invocation with its exit code, its
wall time, and the first 200 bytes of its report, and writes nothing to the repo outside
`.qwen/tmp/reports/`. `math-8ou` promoted it from `.qwen/tmp/` into `notes/scripts/`, closing
the one gap the list had. A writer's gate is the single run plus the promote-and-verify assertion
recorded in the writers table: the bytes it lands under its key must equal the bytes on the tracked
path. The list is two arrays: `serial_rows` (the writers in dependency order, plus
`refresh_summary_line_counts.py`) run in order, `pool_rows` (the **59** read-only invocations) run
through `xargs -P 8` and print in the canonical order of the list, so the pooled report is the same
bytes a serial run prints — measured 2026-10-11: serial 928 s, pooled 431 s, pooled report diffed
against the serial report with wall-time tokens normalized 0 bytes. `GATE_POOL=1` runs everything
serially. A pooled row must spawn no writer, so the render children (`build_index.py`,
`extract_links.py`) run with `--check-only`. `gate_driver.sh` runs the list once, snapshots the md5 of
every generated artifact and `git status` raw, and prints the `verify_cache_promotion.py` row, whose
key is computed from the current `git rev-parse HEAD:<path>` tree digests. The wall-time normalization
the twice-run needed (`0.53s` → `Ts`, because every row prints its wall time) left with the second run.

| Script | Report feeds | Gate |
|---|---|---|
| `check_index_links.py` | `notes/index-links.md` | plain + `--mutant` |
| `check_summary_manuscripts.py` | `notes/summaries/` — which manuscripts each page reads, and whether the release still names them | plain |
| `dump_template_slots.py` | `notes/templates.md` — the writer's slot labels with their values | plain |
| `extract_citations.py` | `notes/citations.md` | plain |
| `extract_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` | plain |
| `extract_named_results.py` | `notes/named-results.md` | plain |
| `extract_scope_notes.py` | `notes/scope-exclusions.md` | plain |
| `extract_subfinding_pairs.py` | `notes/subfinding-pairs.md` | plain |
| `extract_t0_chains.py` | `notes/t0-chains.md` | plain |
| `extract_verification_348.py` | `notes/verification-dirs.md` | plain |
| `extract_verification_dirs.py` | `notes/verification-dirs.md` | plain |
| `locate_summary_quotes.py` | `notes/summaries/` — the lines a page should cite when a quotation stops matching | plain, no page argument |
| `measure_checker_needles.py` | `notes/templates.md` — the per-checker needle inventory behind its Needles column | plain |
| `measure_faithfulness.py` | `notes/formalization-faithfulness.md` | plain |
| `measure_index_sizes.py` | `notes/index-design.md` | plain |
| `measure_names.py` | `notes/names.md` | plain |
| `measure_proof_density.py` | `notes/proof-density.md` | `--mutant` |
| `measure_templates.py` | `notes/templates.md` | plain |
| `measure_topics.py` | `notes/topics.md` | `--check` |
| `read_manuscript.py` | none — a reading aid; prints a manuscript's abstract, section skeleton and titled statement environments with `file:line` anchors | **not gated** |
| `refresh_summary_line_counts.py` | `notes/summaries/` — rewrites the `Lines` column of the Sources table in every page | plain, **first among the checkers** |
| `triage_t0.py` | `notes/t0-triage.md` | plain |

`read_manuscript.py` is the only script the gate does not run: it takes a `preprints/` directory
argument, so a gate run over it would read one manuscript chosen by the list rather than the corpus.
`refresh_summary_line_counts.py` runs before the checkers because `verify_summaries.py` flags a stale
`Lines` cell, so the checker must run after the refresh.

`check_index_links.py` is the link checker for `notes/index/` and `CONTENTS.md` — it reads the tree and
writes nothing, so it sits here rather than in the checker table, which lists scripts that verify a
page's text. Since `math-a0r.6.2` its run ends with a sync pass on `notes/index-links.md` (the page
compared with `render_reports.py`'s render of it, folded into the exit code), and its self-test's
21st mutant is a mutation of that page's prose.

### Checkers

The remaining **22** scripts verify a page or a table. Each exits non-zero when what it checks has
drifted; each takes `--mutant`, which injects faults and asserts they are caught. The gate runs each
one plain and then with `--mutant` — **46** of the 76 invocations: **44** from the loop over the 22
rows below, **2** more for `verify_conjecture_standing.py`, which the list runs outside the loop.

| Checker | Checks | Gate | Cost (s) |
|---|---|---|---|
| `verify_abstracts.py` | `notes/abstracts.md` | plain + `--mutant` | 1.0 / 1.0 |
| `verify_cache_promotion.py` | `catlib/promote.py` — the registry shape against the writers table, the L1 lists against the audit-hook records, and the cached bytes against every tracked artifact under its key | plain + `--mutant` | 1.0 / 7.0 |
| `verify_citations.py` | `notes/citations.md` | plain + `--mutant` | 1.4 / 2.8 |
| `verify_conditional.py` | `notes/conditional.md` | plain + `--mutant` | 0.0 / 0.0 |
| `verify_conjecture_standing.py` | `notes/conjecture-standing.tsv` | plain + `--mutant` | 0.0 / 0.0 |
| `verify_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` | plain + `--mutant` | 0.3 / 2.4 |
| `verify_dependency_drift.py` | `notes/dependency-drift.md`, `notes/formalization-deps.md` | plain + `--mutant` | 0.3 / 1.8 |
| `verify_faithfulness.py` | `notes/formalization-faithfulness.md` — anchors, the count phrases re-derived by its own `main_results`/declaration/carrier/closure walk (not the writer's), the disjoint and overlap pairing tables, the `a.e.` table, and the render diff | plain + `--mutant` | 0.0 / 0.0 |
| `verify_findings.py` | `notes/findings.md` | plain + `--mutant` | 103.4 / 825.3 |
| `verify_fleet_design.py` | `notes/fleet-design.md` — anchors, the count phrases re-derived from `git`/`du`/the probe records, the purity and amplification tables | plain + `--mutant` | 0.3 / 0.5 |
| `verify_index_design.py` | `notes/index-design.md` | plain + `--mutant` | 2.7 / 20.7 |
| `verify_named_conjectures.py` | `notes/named-conjectures.md` | plain + `--mutant` | 0.0 / 0.1 |
| `verify_named_results.py` | `notes/named-results.md` | plain + `--mutant` | 104.6 / 108.3 |
| `verify_page_sync.py` | `notes/links.md`, `notes/names.md`, `notes/topics.md`, `notes/proof-density.md`, `notes/index-links.md` — the render diff for the five pages whose sync pass used to live in a writer; the mutants mutate page prose in memory, so no page is written | plain + `--mutant` | 115.1 / 70.2 |
| `verify_scope_exclusions.py` | `notes/scope-exclusions.md` | plain + `--mutant` | 0.1 / 0.2 |
| `verify_sources.py` | `notes/sources.md` | plain + `--mutant` | 1.9 / 13.2 |
| `verify_subfinding_pairs.py` | `notes/subfinding-pairs.md` | plain + `--mutant` | 0.1 / 0.1 |
| `verify_subfindings.py` | `notes/subfindings.tsv` | plain + `--mutant` | 0.1 / 0.6 |
| `verify_summaries.py` | `notes/summaries/` | plain + `--mutant`, no page argument | 0.3 / 1.0 |
| `verify_t0_chains.py` | `notes/t0-chains.md` | plain + `--mutant` | 0.1 / 0.2 |
| `verify_upstream_history.py` | `notes/upstream_history/` — the three pages | plain + `--mutant` | 0.7 / 0.5 |
| `verify_verification_dirs.py` | `notes/verification-dirs.md` | plain + `--mutant` | 0.1 / 0.8 |

Cost is plain seconds / `--mutant` seconds, measured 2026-10-10 as one timed pass per checker with
the local model server loaded — a floor from one measurement, not a benchmark. The spread between
the two columns is structural, not noise: `--mutant` re-runs the whole check once per injected
fault, so a checker whose plain run is a full measurement pays it again per mutant.
`verify_findings.py` is the extreme: its Pass E runs the fast extractors as subprocesses inside
`check()` (`:357`, the subprocess call at `:116`), and `check()` runs 8 times under `--mutant` — the
clean page in `main()`, once per each of the 6 mutants (`:514`), and the clean page again as the
mutants' baseline (`:518`) — so 8 × 103 s = 825 s, and that one checker is most of the gate's
runtime. `verify_named_results.py` is expensive in both columns (104.6 / 108.3) because its cost is
the corpus read, which a mutant does not multiply. The 11 wired checkers pay the render-diff in their
mutant runs; `verify_script_ownership.py`, this page's own checker, is 0.2 plain / 1.1 with
`--mutant` and is not a row above. The 40 checker invocations sum to **1196.9 s** (20 min); the full
65-invocation gate took **35 min** and **38 min** on its two runs measured 2026-10-10
(10:48–11:23 and 11:23–12:01 UTC); the 64-invocation list took **62 min** the same morning
(05:49–06:51 UTC), so the two figures are a spread, not a regression — the difference being the
writers — `extract_formalization_deps.py` reads all 122,458 files under `lean/OAI/` and
`build_index.py` renders 1,049 pages.

`verify_conjecture_standing.py` is the one checker the list kept outside its loop: it ran plain only,
so its six mutants were never run by the gate. Measured 2026-10-09 by hand — `mutants 6  uncaught
0 []`, exit 0 — `math-8ou` added the `--mutant` invocation, which is why the count read 63 and not
62. `math-a0r.6.2` added `check_index_links.py --mutant` for the same reason — its 21st mutant is a
mutation of `notes/index-links.md`'s own prose, which only the self-test can catch — and `math-3la`
added `measure_checker_needles.py`, so the count is **73** after `math-o3a.1` added
`verify_fleet_design.py` plain and with `--mutant` (0.3 / 0.5 s) and `math-o3a.6.1` added
`verify_cache_promotion.py` plain and with `--mutant` (1.0 / 7.0 s).

`verify_script_ownership.py` — this page's own checker — is not in the table: a checker cannot list
itself as its input. It is the 22nd checker and the 52nd script the run counts.

## The shared package: `catlib/`

`notes/scripts/catlib/` holds the joins the extractors share, so a join is written once. It is 16
modules, not scripts: `paths.py` (the repo-root constants, `rel()`, `owner()`, `read_text()`),
`tsv.py` (the four TSV writer shapes), `promote.py` (the promotion protocol — the `L1` and `ARTIFACTS`
registry, `key_for()` for the builder's digest key, `promote()` which caches the bytes under the key
and then writes the same bytes onto the tracked path, and `cached_text()`), `atomic.py` (the atomic write primitive —
`write_atomic()` writes through a sibling temp name, fsyncs, then moves the temp onto the target, so
a crash never leaves a half-written tracked file; every writer's write site goes through it, which is
why the fleet's atomicity grep reads 1 match, not 9), `overview.py` (the `\resultentry` parse),
`ledger.py`
(`notes/catalog.tsv` and the claim-shape rules), `preprints.py` (the 749 dirs versus the 719 listed
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

**49** of the **53** scripts call the package, measured by the rule `^[ \t]*(from|import) catlib` over
each script's own source: **11** `extract_` (all of them), **4** `build_` (all), **5** `measure_`
(`measure_checker_needles.py`, `measure_index_sizes.py`, `measure_names.py`, `measure_open_probe.py`,
`measure_templates.py`), **2** `check_` (`check_index_links.py` and `check_summary_manuscripts.py`),
**all 21** checkers, plus `render_reports.py`, `triage_t0.py`, `read_manuscript.py`,
`compare_abstracts.py`, `locate_summary_quotes.py` and `refresh_summary_line_counts.py`. The four
scripts that do not are `dump_template_slots.py`, which reaches the slot dict through
`render_reports.py` and never touches the registry; `verify_fleet_design.py`, which measures the
fleet's own sources and the probe records, so it has no corpus join to import; and
`measure_proof_density.py` and `measure_topics.py`, which read the Sources table and the vocabulary
directly. The three summary-page readers
`check_summary_manuscripts.py`, `locate_summary_quotes.py` and `refresh_summary_line_counts.py` were
moved off `verify_summaries.py` onto `catlib/summaries.py` by `math-6s7.1` — a checker serving as a
library is the shape that port broke, and `verify_summaries.py` now has **0** importers. `math-lon.2.5` ported the last two checkers,
`verify_upstream_history.py` and `verify_summaries.py`, and the **22** `duplicate-code` findings
did not move (measured 2026-10-09 with `--enable=R0801` over 55 files, every cluster reported against
`catlib/anchors.py`; see `notes/linting.md`). What deliberately stays outside the package is a **read
shape**, not a parse: `verify_upstream_history.py` reads `lean/formalization.yaml` and
`notes/catalog.tsv` from a **revision** through `git show <rev>:`, so the package gained
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
`group_labels` and `SPLIT_LABEL` — so `build_report_templates.py`, `measure_checker_needles.py` and
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
`catlib/` is 15 modules under that directory, counted as **66** source files by the lint gate in
`notes/linting.md`.

## The file census

| Population | Files | Owner |
|---|---|---|
| `notes/index/` | **1,049** | generated — `build_index.py` |
| `notes/summaries/` | **21** | hand-written — the reading record |
| `notes/templates/` | **22** | **5** hand-written index skeletons + **17** report templates built by `build_report_templates.py` |
| `notes/upstream_history/` | **3** | hand-written — one page per upstream merge, moved from the repository root on 2026-10-10 |
| `notes/probe/` | **5** | the audit-hook probe records the fleet-design page quotes: the 2026-10-11 writers/checkers pair `measure_open_probe.py` writes and the checker parses, the 2026-10-11 `render_reports.py` after-record that proves the repeat count fell, and the 2026-10-10 pair the page's cold-cache figures come from |
| `notes/*.tsv` | **8** | **6** generated, **2** hand-authored |
| `notes/*.md` | **29** | hand-written — **22** with a checker, **7** without |
| `notes/` total, scripts excluded | **1,137** | — |

The generated TSVs are the six writer targets. The two hand-authored tables are:

| Table | Why it is hand-authored |
|---|---|
| `notes/topics.tsv` | The curated topic vocabulary. `measure_topics.py --check` re-measures its 92 rows and exits 1 when a recorded count drifts; `build_index.py` reads it and renders `notes/index/topics-rendered.tsv`. A generated file inside `notes/index/` is overwritten by the next render, which is why the vocabulary lives above that tree. |
| `notes/conjecture-standing.tsv` | The training-data prior. Its `standing_prior_2025` column is the assistant's memory at an early-2025 cutoff, self-rated by `prior_confidence`; no script can derive a memory, and `verify_conjecture_standing.py` checks the rows against the ledger and `overview.tex` rather than regenerating them. |

The 7 pages with no checker are `notes/README.md`, `notes/conjecture-standing.md`,
`notes/counterexample-tag.md`, `notes/linting.md`, `notes/resolution-tag.md`,
`notes/summaries-workflow.md` and `notes/t0-triage.md`. Their counts are reproduced by the report-only
scripts above; nothing verifies them against the page. `notes/linting.md` is the one page in that set
whose counts come from tools outside this tree — the three linter commands it names, run from the
untracked `.venv/`. The five pages `notes/index-links.md`, `notes/links.md`, `notes/names.md`,
`notes/proof-density.md` and `notes/topics.md` were in this set until `math-o3a.3`: their render diff
was carried by a report-only script that read a page it did not verify, and `verify_page_sync.py`
owns that check now.

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

`notes/README.md`'s command block named **34** of the 52 scripts before this pass. Eighteen are named
nowhere in the repo at the pinned baseline: `build_report_templates.py`, `check_summary_manuscripts.py`,
`extract_citations.py`, `locate_summary_quotes.py`, `measure_checker_needles.py`, `measure_open_probe.py`, `measure_templates.py`,
`read_manuscript.py`,
`refresh_summary_line_counts.py`, `render_reports.py`, `verify_citations.py`, `verify_findings.py`,
`verify_fleet_design.py`, `verify_named_conjectures.py`, `verify_page_sync.py`, `verify_upstream_history.py`,
`dump_template_slots.py` and `verify_cache_promotion.py`. The first four are the report-template
builder this pass promoted plus the `notes/summaries/` reading tooling and the citation extractor, so
the summaries tree and `notes/citations.md` carried measurements whose generating command no document
named; `read_manuscript.py` and `refresh_summary_line_counts.py` are the rest of that reading tooling;
`verify_citations.py`, `verify_findings.py` and `verify_named_conjectures.py` are the checkers for
`notes/citations.md`, `notes/findings.md` and `notes/named-conjectures.md`, so three pages carried
measurements whose checker no document named; `verify_upstream_history.py` is the tooling behind
`notes/upstream_history/`, the pages that record each upstream merge, which moved under `notes/` on
2026-10-10 and are inside this page's census; `measure_templates.py` is the census behind `notes/templates.md`, added by
the pass that added that page; `measure_checker_needles.py` is the per-checker needle probe the
checker-coverage bead promoted; `dump_template_slots.py` is the slot dump that prints the same dict the census measures, promoted by `math-a0r.7`; `verify_fleet_design.py` is the checker for `notes/fleet-design.md`, promoted by `math-o3a.1` together with the two probe records it parses; `verify_page_sync.py` is the checker `math-o3a.3` created when the five sync passes left the writer fleet, so the pinned baseline predates it; `measure_open_probe.py` is the audit-hook probe `math-o3a.3.4` promoted from `.qwen/tmp/a11_open_probe2.py`, so the pinned baseline predates it too; `render_reports.py` is the renderer for the seventeen report-fed pages; and `verify_cache_promotion.py` is the checker `math-o3a.6.1` created for the promotion protocol, so the pinned baseline predates it.
All 52 are named here and in the command
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

Measured 2026-10-09 over `.qwen/tmp/` **after** the `math-8ou` cleanup: **285** top-level files,
**7,121** files including subdirectories, **14** subdirectories. By top-level suffix: **222** `.txt`,
**43** `.md`, **19** `.tsv`, **1** `.py`, and **0** in every other suffix — the tree is now reports,
drafts, baselines and index snapshots, with one script left in it. The largest trees are gate and
render snapshots — `reports/` **271**, `idx_pre_sweep/`, `idx_run1/` and `idx_run2/` at **1,052** each,
`index-run1/` **1,049**, `index_run1/` and `index_run2/` at **1,050** each, `lon2/` **85**, `msgs/`
**65**, `lon1/` **63**, `leanout/` **38**.

Before the cleanup the same measurement read **367** top-level files, **7,116** total, and a top-level
suffix histogram of **220** `.txt`, **70** `.py`, **43** `.md`, **19** `.tsv`, **3** `.sh` and **12**
files in the remaining suffixes. `math-8ou` closed that gap: the gate list and its driver,
`gate.sh` and `gate_driver.sh`, are promoted to `notes/scripts/gate.sh` and
`notes/scripts/gate_driver.sh` — a test that lives in an untracked directory is not a test the next
session can run, and the driver header now carries the one-driver and group-kill rules the gate runs
need. The **70** one-off `.py` probes are deleted (the `hqd5_probe*.py` family at 16, the `e8k_*.py`
lint-fix family at 8, the family-`001` summary builders at 11, the `probe_*` set at 6, the
`0h2`/`extra` generators at 4, the marker/layout fixers at 4, the citation-needle printers at 2, the
conditional-anchor checker `check_conditional_anchors.py`, and the single-purpose probes `measure_links.py`, `measure_subfindings.py`, `title_variants.py`,
`upstream_probe.py`, `yaml_probe.py`, `topo.py`, `thms.py`, `show.py`, `core_all.py`,
`find_core_only.py`, `cand_closure.py`, `gen_axioms.py`, `lint_anchors.py`, `port_nc.py`,
`drop_syspath.py`, `build_scope_page.py`, `fix_topics.py`, `fix_topics_md.py`), together with
`elab.sh` and the **12** probe outputs it left behind (`axioms.lean`, `axioms.log`, `axioms.olean`,
`check.lean`, `check.olean`, `elab.log`, `hqd5_quotes.json`, `names.json`, `leanout.tmp.1682832`,
`0h2_skel.err`, `cit1.err`, `cx2a.err`). The four `/tmp` trees `stage5/`, `portcheck/`,
`portcheck2/`, `pprobe/` and the six `/tmp` one-offs `e402_probe.py`, `e402_probe2.py`,
`lint_anchors_scratch.py`, `lint_stage4.txt`, `lint_stage4b.txt`, `port_check2.sh` are deleted too —
`/tmp` is outside the rule's location and outside the repo, so a script written there is a script
whose outputs cannot be re-measured.

Measured 2026-10-10 over `.qwen/tmp/` **after** the `math-3la` cleanup: **403** top-level files,
**136,180** files including subdirectories, **5** subdirectories. By top-level suffix: **304** `.txt`,
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
`__pycache__`) and the **36** superseded probes the promotion replaced — `a63_two_renders.sh` and
`a63_dump_slots.py` by `two_render_proof.sh` and `dump_template_slots.py`, `a63_lint.sh` by
`notes/scripts/lint_scripts.sh`, `a64_demo.sh` and `a64_sed.txt` by `simulate_ledger_bump.sh`,
`a63_measure_templates*.py` by `notes/scripts/measure_templates.py`, and `a62_lines_probe.py`, which
the bead rejects — plus the `a64_copy/` demo tree. The `math-3la` cleanup deleted **10** more: the
seven `a7_*` one-shots (`a7_apply.sh`, `a7_bump_run.sh`, `a7_il2_waiter.sh`, `a7_il_fix2.sh`,
`a7_promoted_run.sh`, `a7_proof.sh`, `a7_tpl_rebuild.sh`), `a8_lint.sh` by
`notes/scripts/lint_scripts.sh`, `a8_probe.py` by `notes/scripts/measure_checker_needles.py`, and
`a8_proof_chain.sh`, deleted only after its run printed `CHAIN_DONE`. The top-level count falls by
**10** while the file total falls by **8**, because two of the deleted files were hardlinks whose
twins live in `ledger_bump_copy/`.

The scratch tree is not a record. `.qwen/tmp/n5d3-draft.md` is a working draft whose tail is the
state a compacted session resumes from, and `.qwen/tmp/canonical_counts.md` is the count sheet the
gate reports are checked against; both are untracked, and the findings they carry are moved into
tracked files under `notes/` before the bead that produced them closes.

## Not checked

- **The checker proves ownership, not byte-sync.** Nothing asserts that a file under `notes/index/`
  equals what `build_index.py` currently renders. The assertion covers the cache half: the bytes under
  the key equal the bytes on the tracked path, and `git status` compares the tracked path with `HEAD`.
  A hand-edit to a rendered page survives until a checker's needle happens to break.
- `build_index.py` sweeps its own tree: it tracks every path its `write()` helper emits and, at the end
  of `main()`, unlinks any `notes/index/**.md` or `**.tsv` it did not write, then removes empty
  directories and prints `stale swept N files [...]`. The realized case is the 2026-10-07 merge: family
  032's title changed, so its old-slug page survived as an orphan whose manuscript table pointed at the
  three withdrawn directories — 6 broken links, found only by `check_index_links.py`. Two name pages
  (`cech`, `kunneth`) went the same way; the sweep removed 3 files. Renaming the rendered topic table is
  the older case — `notes/index/topics.tsv` survived the rename and was deleted by hand. Page counts are
  measured consistent: **1,033** `.md` on disk against the **1,033** the render report claims.
- The sweep is probe-verified on both branches (2026-10-09, `math-a0r.1`): a planted
  `notes/index/names/zzz-sweep-probe.md` prints `stale swept 1 files ['names/zzz-sweep-probe.md']` and
  is gone after the run; a planted page inside a new directory prints `empty dirs removed 1` and the
  directory is gone too; both runs leave `git status` clean under `notes/index/`. So `stale swept 0`
  on a clean tree is a measured negative, not an untested branch — which is what makes the templating
  epic (`math-a0r`) safe to start: templates render a tree that sweeps, and a tree that cannot shed an
  old-slug page would freeze that page into the template set.
- The idempotence gate for `build_index.py` is run 2 against run 3, not run 1 against run 2: the first
  run after a corpus change prints the sweep line with the files it removed, the second prints
  `stale swept 0 files []`. Diffing run 1 against run 2 reports the sweep as drift.
- The writer rule reads path constants and write calls. A write built from a computed path (a variable
  assembled at runtime) is not found by it, and `refresh_summary_line_counts.py` is the realized case:
  it resolves each page path through `catlib/summaries.py`'s `Page` and rewrites the `Lines` column of every
  page under `notes/summaries/`, so the rule files it under report-only and the census row calls that
  tree hand-written. The tree is hand-written in what it says and script-touched in that one column.
- The report-only table records which page a report feeds as stated in that page and in `AGENTS.md`.
  It is not derived from the report text, so a page that stops quoting a report keeps its row here.
- **A needle can match nothing and the run stays green.** `verify_upstream_history.py`'s `SLUG`
  pattern required a trailing `/` inside the backticks **and** a 3-letter month, while the corpus
  writes full month names only (`September` 576, `October` 172 over the **749** `preprints/` dirs), so
  it matched **0** tokens on the three pages it checks — `notes/upstream_history/2026-10-07_3014888.md`
  carries **14** backticked manuscript-slug tokens of that shape, written without the slash. The run
  exited 0 because nothing was asserted, and a slug renamed to one the release does not name was not
  caught. `math-lon.2.5` ported the file and left the pattern as it is, because its acceptance is
  byte-identical gate reports. `math-cg1` fixed both halves (slash optional, full month names: the
  needle now matches the **14** tokens and **0** on the other two pages), added the `slug rename`
  mutant (**13** → **14**, needle `": slug '"` — the table pass reports the same fact as
  `table: '…' is not a preprints/ directory`, so a shared needle cannot tell the two passes apart),
  and made the report print the slug count: a run that matches **0** is a problem, not a green result.
- Nothing in `lean/` is built, so no generated artifact here is a verification of a formalization.
