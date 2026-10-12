# Linting the ledger scripts

The venv, the three tool configs, the commands, and every exemption with the count it covers.
Created for `math-e8k`. The three commands below are the lint gate, run as one command by
`notes/scripts/lint_scripts.sh` (promoted from `.qwen/tmp/` by `math-3la`); the twice-run gate that proves a
lint fix changed no generated output runs from the gate list at `notes/scripts/gate.py` (promoted
there from `.qwen/tmp/` by `math-8ou` as `gate.sh`, and rewritten as the scheduler by `math-unv`), and
the idempotence discipline it implements is recorded in
`notes/scripts/README.md`.

## The environment

`uv 0.11.16` builds the venv; the interpreter is **CPython 3.12.13** (uv's default, not the system
3.14.7), and the tree is **`.venv/`**, ignored in `.gitignore` — nothing in it is tracked.

```bash
uv venv .venv
uv pip install --python .venv/bin/python jinja2 mypy ruff pylint
```

| Tool | Version | Installed for |
|---|---|---|
| jinja2 | 3.1.6 | `math-a0r` templating of generated pages |
| mypy | 2.4.0 | type checking of `notes/scripts/` |
| ruff | 0.16.10 | lint + import order + autofix |
| pylint | 4.1.2 | warning-class triage |

## The commands

```bash
notes/scripts/lint_scripts.sh          # the trio in one command; prints each tool's exit code

.venv/bin/ruff check notes/scripts/    # exit 0
.venv/bin/mypy notes/scripts/          # exit 0
PYTHONPATH=notes/scripts .venv/bin/pylint notes/scripts/   # exit 0
```

`notes/scripts/lint_scripts.sh` is the driver `math-3la` promoted from a scratch script; it sets
`PYTHONPATH=notes/scripts`, which `pylint` needs to import the sibling modules — without it pylint
reports `E0401: Unable to import 'render_reports'` and the run is not green for the right reason.

Configs: `ruff.toml`, `mypy.ini`, `.pylintrc` at the repository root. Each carries its exemptions
as comments; the tables below are the same list with the measured counts.

## Baseline (2026-10-09, before any fix)

| Tool | Default run | With the repo config | After the fixes |
|---|---|---|---|
| ruff | 446 findings over 44 scripts | 287 | **0** (287 → 26 by autofix, 26 → 0 by hand) |
| mypy | 3 errors in 3 files (44 checked) | 3 | **0** (3 → 0) |
| pylint | 1,422 findings over 44 scripts | 142 | **0** (142 → 38 after the ruff autofixes, 38 → 21 by hand, 21 → 0 by the last three exemptions) |

`python -m py_compile notes/scripts/*.py` passes for all 58 under the venv interpreter. The tree is
**75 source files** today — **58** scripts plus `catlib/`'s **17** — and every current-state figure
below is measured over 75 (re-measured 2026-10-12 at 00:37 UTC by `notes/scripts/lint_scripts.sh`,
the pass that made `measure_names.py` a record producer; mypy's own line reads
`Success: no issues found in 75 source files`); the baseline row above is the 44-file tree
it was measured on, and the `duplicate-code` row below carries its dated 2026-10-09 measurement over
57 files plus the 2026-10-10 re-measures over 62 and 63, the 2026-10-11 re-measures over 64, 65, 66
and 67, and the 2026-10-12 re-measure over 75.

## Exemptions

Each row is a rule the config turns off, the count it produced on the baseline, and why the finding
is not a defect in this tree.

| Rule | Count | Reason |
|---|---|---|
| ruff `UP031` / pylint `consider-using-f-string` | 166 / 160 | Report strings are %-formatting templates reused across tiers; converting 166 of them re-wraps the report output the checkers compare against. Re-measured 2026-10-12 at 00:37 UTC with `ruff check --select UP031 notes/scripts/` over the 75-file tree: **164** findings. The 166 → 164 fall is not this pass — `git archive HEAD notes/scripts` (the 75-file tree before the pass) measures the **same 164**, so the page's 166 is the figure an earlier pass recorded and the two findings left before HEAD. |
| ruff `ISC004` | 80 | Implicit concatenation inside a list literal is how the mutant tables are written. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **118** findings. The 80 → 118 rise is not this pass — HEAD measures the **same 118** — so the page's 80 is the 67-file-era figure; the rise is the mutant tables the checkers added since. |
| ruff `FURB167` | 60 → 64 → **70** | `re.M` is the local alias convention for regex flags. Re-measured 2026-10-11 at 03:49 UTC with `ruff check --select FURB167 notes/scripts/`: **70** findings, all reported fixable, over the 65-file tree, spread over 28 files (`verify_script_ownership` 10, `extract_links` 8, `verify_citations` 6, `verify_fleet_design` 5, `measure_names` 5, `catlib/yaml` 4, then 3s and 1s). The 64 → 70 rise is the 5 findings `verify_fleet_design.py` brings plus 1 elsewhere; **no finding names `catlib/atomic.py` or `catlib/tsv.py`** — the atomic-write modules carry no regex. Re-measured 2026-10-11 at 05:12 UTC over the 66-file tree: **70** findings over the **same 28 files** with the **same** per-file distribution — `math-o3a.3` added `verify_page_sync.py` and removed five regex-free import lines, so no finding moved. Re-measured 2026-10-11 at 06:42 UTC over the 67-file tree: **70** findings over the **same 28 files** — `measure_open_probe.py` imports no `re` at all (it parses nothing; the audit hook records paths and mode strings), so the new file adds no finding and the set stays 28. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **75** findings over **31** files (`verify_script_ownership` 11, `extract_links` 8, `verify_citations` 6, `verify_fleet_design` 5, `measure_names` 5, `catlib/yaml` 4, four 3s, three 2s, 18 singletons). The 70 → 75 rise is **not this pass**: `git archive HEAD notes/scripts` measures the **same 75 over the same 31 files** with the **same** per-file distribution, so the 5 findings and the 2 new files arrived before HEAD, and `measure_names.py`'s record-store rewrite moved no finding — it keeps its five `re.M` sites. |
| ruff `FURB188` | 8 | Single-character prefix/slicing where `removeprefix` adds nothing. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **12** findings; HEAD measures the **same 12**, so the 8 → 12 rise is an earlier pass. |
| ruff `I001` | 4 → 14 → **26** → **24** | Import blocks are not isort-ordered: stdlib, then the sibling extractors, then `catlib`, in the order the reader follows them. Measured **13** before and **14** after the `sys.path.insert` boilerplate was dropped — the insert was never what made the block unsorted, so the exemption stays. Re-measured 2026-10-11 at 03:49 UTC: **26** findings, exactly **one per file** over 26 files. The 14 → 26 rise is the checkers that moved onto the package: each gained a `catlib` import line after the sibling extractors, which is the order the reader follows, so the exemption stays. Re-measured 2026-10-11 at 05:12 UTC over the 66-file tree: **24** findings, exactly **one per file** over 24 files. The 26 → 24 fall is `math-o3a.3`: `measure_topics.py` and `measure_proof_density.py` leave the set — for those two, `from catlib import render as RD` was the block's only non-stdlib line, so deleting the sync pass left a plain sorted stdlib block (`measure_proof_density.py`) and a sorted stdlib-then-`build_catalog` block (`measure_topics.py`). The other three scripts that lost the pass keep their finding, because their blocks still carry the sibling extractors ahead of `catlib`. Re-measured 2026-10-11 at 06:42 UTC over the 67-file tree: **24** findings, exactly **one per file** over the **same 24 files** — `measure_open_probe.py`'s block is `__future__`, then stdlib in alphabetical order, then `catlib`, which is isort-ordered, so the new file is not in the set. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **29** findings, exactly **one per file** over **29** files. The 24 → 29 rise is **not this pass** — HEAD measures the **same 29** — so the five files that joined the set arrived before HEAD; `measure_names.py` stays in the set, since its record-store rewrite added `import json` and `from catlib.promote import key_for` to a block that was already unsorted. |
| pylint `line-too-long` | 351 | Report lines embed manuscript paths and verbatim quotations. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **754** findings. `git archive HEAD notes/scripts` measures **734** over the same tree, so **20** of the rise is this pass — the record-store comments and the type annotations `measure_names.py` and `catlib/promote.py` gained; the remaining 383 is the earlier passes' growth the page had not swept. |
| pylint `missing-function-docstring` | 194 | A report function's contract is the report line it prints; the module docstring states what the script measures. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **250** findings; HEAD measures the **same 250**, so the 194 → 250 rise is the checkers and package modules added since the page's figure, not this pass. |
| pylint `too-many-*` | 80+37+35+5+3+2 | A generator that reconciles a corpus is wide by design; the metrics describe the report. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree with `--enable=R0912,R0913,R0914,R0915,R0916,R0917 --disable=all`: **43+7+114+44+7+0** (branches 43, arguments 7, locals 114, statements 44, positional 7, returns 0). HEAD measures the **identical** six counts, so this pass moved none of them — the page's cell is the figure an earlier pass recorded. |
| pylint `invalid-name` | 12 | Module path constants are UPPER_CASE; extractors use short loop variables. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **8** findings; HEAD measures the **same 8**, so the 12 → 8 fall is an earlier pass. |
| pylint `duplicate-code` | 24 → 28 → 26 → 26 → 24 → 22 → **29** | Measured 2026-10-09 with `--enable=R0801` over 57 files, after **all 19** checkers moved onto the package: **all 29** findings are attributed to `catlib/anchors.py`, whose anchor/fence loops are the reference side of every cluster (pylint reports a cluster under its first module). The 29 clusters pair 58 module entries: `render_reports` 7, `verify_sources` 6, `verify_index_design` 6, `verify_citations` 6, `extract_citations` 5, `verify_verification_dirs` 4, `extract_subfindings` 4, `verify_subfindings` 3, `verify_named_results` 2, `verify_dependency_drift` 2, `verify_counterexample_crosscheck` 2, `verify_conditional` 2, `catlib.overview` 2, and 7 singletons (`catlib.bib`, `catlib.text`, `extract_formalization_deps`, `locate_summary_quotes`, `verify_abstracts`, `verify_scope_exclusions`, `verify_summaries`). The 22 → 29 rise is `math-a0r.4`: `render_reports.py` arrives with 7 clusters because it re-derives, on the writer side, the anchor and phrase loops its four pages' checkers measure on the checker side — the split is the point of the design, so those clusters are the by-design extract-to-verify pair, not a shared-helper opportunity. `verify_sources` 3 → 6 and `verify_index_design` 5 → 6 are the same pair seen from the checker's side of that split, and `verify_named_results` 0 → 2 plus the `verify_abstracts` singleton are its two remaining anchor loops. Two clusters left and none arrived earlier, so the net is 24 → 22: out go the pair window and the connected-component scan, which were `verify_citations.py:140-146` and `:147-153` against `extract_citations.py` and are now one `catlib.bib.pair_counts` / `catlib.bib.clusters` call in each file. The 6 that remain on that pair are the extractor↔checker measurement loop — the checker re-derives the population from the corpus rather than trusting the report — which stays by design. `math-lon.2` ported the last **2** checkers (`verify_upstream_history.py`, `verify_summaries.py`) and moved no cluster. **Re-measured 2026-10-10 over the 61-file tree: 39 clusters**, still all attributed to `catlib/anchors.py`, pairing **78** module entries: `render_reports` 16, `verify_verification_dirs` 8, `verify_dependency_drift` 7, `verify_sources` 6, `verify_index_design` 6, `verify_citations` 6, `extract_citations` 5, `extract_subfindings` 4, `verify_subfindings` 3, `verify_named_results` 2, `verify_counterexample_crosscheck` 2, `verify_conditional` 2, `catlib.overview` 2, and **9** singletons — the 7 recorded on 2026-10-09 plus `measure_proof_density` and `check_index_links`. The 29 → 39 rise is +9 on `render_reports`, +4 on `verify_verification_dirs`, +5 on `verify_dependency_drift` and the 2 new singletons; **no cluster names `measure_checker_needles.py`**, so the promotion added none. **Re-measured 2026-10-10 at 22:08 UTC over the 62-file tree: 40 clusters**, still all attributed to `catlib/anchors.py`, pairing **80** module entries: `render_reports` 16, `verify_verification_dirs` 8, `verify_dependency_drift` 7, `verify_sources` 6, `verify_index_design` 6, `verify_citations` 6, `extract_citations` 5, `extract_subfindings` 4, `verify_subfindings` 3, `verify_summaries` 2, `verify_named_results` 2, `verify_counterexample_crosscheck` 2, `verify_conditional` 2, `locate_summary_quotes` 2, `catlib.overview` 2, and **7** singletons (`catlib.bib`, `catlib.text`, `check_index_links`, `extract_formalization_deps`, `measure_proof_density`, `verify_abstracts`, `verify_scope_exclusions`). The 39 → 40 rise is `math-6s7.1`: `verify_summaries` and `locate_summary_quotes` pair on the call shape they both run through `catlib/summaries.py`, so `locate_summary_quotes` leaves the singleton list and `verify_summaries` joins it. **No cluster names `catlib/summaries.py`** — the shared module is the callee, not the reference side, which is what a port is for. **Re-measured 2026-10-10 at 22:31 UTC over the 62-file tree: 39 clusters**, still all attributed to `catlib/anchors.py`, pairing **78** module entries: `render_reports` 15, `verify_verification_dirs` 7, `verify_dependency_drift` 7, `verify_sources` 6, `verify_index_design` 6, `verify_citations` 6, `extract_citations` 5, `extract_subfindings` 4, `verify_subfindings` 3, `verify_summaries` 2, `verify_named_results` 2, `verify_counterexample_crosscheck` 2, `verify_conditional` 2, `locate_summary_quotes` 2, `catlib.overview` 2, and the **same 7** singletons. The 40 → 39 fall is `math-6s7.2` and it is exactly the cluster the bead targeted: the baseline pair `render_reports:[2021:2029]` ↔ `verify_verification_dirs:[156:164]` — the `for p in bundles: bundle = p / "verification"; _, rule, _ = evd.entry_point(bundle)` block the renderer and the checker each carried — is gone from the entry list, `render_reports` loses one entry and `verify_verification_dirs` loses one, and the remaining `verify_verification_dirs` entries shift by one line (the added package import). **No cluster names `catlib/preprints.py`**, as with `catlib/summaries.py`. **Re-measured 2026-10-10 at 23:00 UTC over the 63-file tree: 39 clusters**, pairing **78** module entries with the **same** per-module distribution as the 22:31 UTC measurement (`render_reports` 15, `verify_verification_dirs` 7, `verify_dependency_drift` 7, the three 6s, `extract_citations` 5, 4, 3, four 2s, `catlib.overview` 2) and the **same 7** singletons — `math-6s7.5` added no cluster. **No cluster names `catlib/templates.py`**: the registry is the callee the builder, `measure_checker_needles.py` and `measure_templates.py` now share, which is the same shape as `catlib/preprints.py` and `catlib/summaries.py`. **Re-measured 2026-10-11 at 02:44 UTC over the 64-file tree: 39 clusters**, pairing **78** module entries with the **same** per-module distribution as the 23:00 UTC measurement (`render_reports` 15, `verify_verification_dirs` 7, `verify_dependency_drift` 7, the three 6s, `extract_citations` 5, 4, 3, five 2s, `catlib.overview` 2) and the **same 7** singletons — `math-o3a.1` added no cluster, and **no cluster names `verify_fleet_design.py`**: the checker parses the probe records and the fleet's own sources, so it shares no anchor or fence loop with the reference side. **Re-measured 2026-10-11 at 03:49 UTC over the 65-file tree: 39 clusters**, pairing **78** module entries with the **same** per-module distribution as the 02:44 UTC measurement and the **same 7** singletons — `math-o3a.2.1` added no cluster, and **no cluster names `catlib/atomic.py` or `catlib/tsv.py`**: the atomic-write primitive and the staging class are write mechanics, not an anchor or fence loop, and the TSV writers are call sites, so neither shares a run with the reference side. **Re-measured 2026-10-11 at 05:12 UTC over the 66-file tree: 38 clusters**, all attributed to `catlib/anchors.py`, pairing **76** module entries: `render_reports` 15, `verify_verification_dirs` 7, `verify_dependency_drift` 7, the three 6s (`verify_sources`, `verify_index_design`, `verify_citations`), `extract_citations` 5, `extract_subfindings` 4, `verify_subfindings` 3, six 2s (`verify_summaries`, `verify_named_results`, `verify_counterexample_crosscheck`, `verify_conditional`, `locate_summary_quotes`, `catlib.overview`) and **5** singletons (`catlib.bib`, `catlib.text`, `extract_formalization_deps`, `verify_abstracts`, `verify_scope_exclusions`). The 39 → 38 fall is `math-o3a.3`: `measure_proof_density` and `check_index_links` leave the singleton list — the render-diff loop they shared with the reference side is the sync pass, which now lives in the checker. **No cluster names `verify_page_sync.py`**: the new checker calls `catlib.render` and mutates page text in memory, so it shares no anchor or fence loop with the reference side. **Re-measured 2026-10-11 at 06:42 UTC over the 67-file tree: 38 clusters**, pairing **76** module entries with the **same** per-module distribution as the 05:12 UTC measurement and the **same 5** singletons — `measure_open_probe.py` adds no cluster. **No cluster names `measure_open_probe.py` or `catlib/atomic.py`**: the probe records audit events and the atomic writer moves bytes, so neither carries an anchor or fence loop for the reference side to pair against. **Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: 47 clusters**, all attributed to `catlib/anchors.py`, pairing **94** module entries: `render_reports` 15, `verify_faithfulness` 9, `verify_verification_dirs` 8, `verify_counterexample_crosscheck` 8, `verify_dependency_drift` 7, three 6s (`verify_sources`, `verify_index_design`, `verify_citations`), `extract_citations` 5, `extract_subfindings` 4, `verify_subfindings` 3, six 2s (`verify_summaries`, `verify_named_results`, `verify_conditional`, `locate_summary_quotes`, `extract_counterexample_crosscheck`, `catlib.overview`) and **5** singletons (`catlib.bib`, `catlib.text`, `extract_formalization_deps`, `verify_abstracts`, `verify_scope_exclusions`). The 38 → 47 rise is **not this pass**: `git archive HEAD notes/scripts` measures the **same 47 clusters** with the **same** per-module distribution, so the 9 clusters arrived before HEAD. **No cluster names `measure_names.py`** — the record producer builds a JSON document and parses it, so it carries no anchor or fence loop for the reference side to pair against. |
| pylint `global-statement` | 3 | Report accumulators are module-level by design. |
| pylint `unsubscriptable-object` | 6 | `prev` is `None`-guarded before the subscript in `verify_dependency_drift.py:169-170` and `extract_formalization_deps.py:161-162`; pylint does not track the narrowing. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **9** findings; HEAD measures the **same 9**, so the 6 → 9 rise is an earlier pass. |
| pylint `exec-used` (inline, not in `.pylintrc`) | 1 | `catlib/templates.py:167` — the template registry derives a page checker's needle list by `exec`ing the checker source, and the builder reports the result as **coverage** (how many of the checker's needles the template slots) and never uses it as the slot source. The slots come from the writer's own label dict in `render_reports.py`, so a template cannot reference a label the writer does not supply. The package module is a registry, not a checker: the page's own checker still re-derives the counts independently. `math-6s7.5` moved the derivation out of `build_report_templates.py:89`, where this exemption pointed. |
| pylint `cyclic-import` | 7 → 8 → **9** → **8** → **7** → **1** | Measured 2026-10-10 at 22:08 UTC with `pylint --enable=R0401 notes/scripts/` over 62 files: **8** cycles, every one reported against `catlib/anchors.py`, all of them the writer-import shape — `catlib.render → render_reports` and the chains through it: `→ measure_names`, `→ measure_topics`, `→ measure_proof_density`, `→ check_index_links`, `→ extract_t0_chains → extract_links`, and the two in-process pairs `→ extract_named_results → measure_names` and `→ measure_index_sizes → check_index_links`, plus `build_report_templates → render_reports → measure_templates`. The **9** recorded earlier counted the **bare pair** `catlib.render → render_reports` as its own finding. Baseline for the port: `git archive HEAD notes/scripts` (the tree before `math-6s7.1`) prints the **same 8-cycle set**, byte-identical, so the port added no cycle and the bare pair is not reported on this tree. The writer imports the scripts whose numbers it renders, and the shared render-diff module imports the writer only inside `rendered()`, because that deferred import is the recursion guard `sync_inert()` needs: a module-level import there would make the writer unimportable from inside a render. The builder chain is closed by the census module's deferred `import catlib.templates` inside `registry()` (`measure_templates.py:44`). The import *graph* is cyclic; the import *cycle* never closes at runtime, since each deferred import runs when every module in the chain is already loaded — which is what the twice-run render and the 20 wired checkers demonstrate. `math-6s7.2` re-measured 2026-10-10 at 22:31 UTC: **8** cycles, the same set, byte-neutral — the bundle walk moving into `catlib/preprints.py` added no import edge, since `catlib.preprints` imports only `catlib.paths`. `math-6s7.3` re-measured at 22:52 UTC: **7** cycles. The one that left is `catlib.render → render_reports → extract_t0_chains → extract_links` — `extract_t0_chains.py` stopped importing `extract_links.py` when the chain edges, the companion-word set and the bib-edge shape moved into `catlib.ledger` and `catlib.bib`, which is exactly the dependency shape the epic exists to remove. The remaining 7 are the writer-import chains through `render_reports` named above. `math-6s7.5` re-measured at 23:00 UTC over the **63**-file tree: **7** cycles, the same set with one name changed — `build_report_templates → render_reports → measure_templates` is now `catlib.templates → render_reports → measure_templates`, because the registry moved into the package and the builder now imports it. The count is unchanged: the builder's module-level `import render_reports` left with the registry, so the edge count is the same, and `catlib.templates` importing the writer at module level is safe only because `measure_templates.py` keeps its import deferred. `math-o3a.1` re-measured 2026-10-11 at 02:44 UTC over the **64**-file tree and the count is **not stable across runs**: five runs of the same command on the same tree read **7, 7, 7, 8, 8**. The run that reads 8 is the one that reports the **bare pair** `catlib.render → render_reports` as its own finding; the 7-cycle chain set is reported in every run, and the set is identical between the runs that read 7 and the runs that read 8. `git archive HEAD notes/scripts` (the 63-file tree, before `math-o3a.1`) gave the **same distribution** — 7, 7, 7, 8, 8 — so the new checker added no cycle, and the 7 → 8 → 9 → 8 → 7 sequence above is partly this run-order dependence, not a record of five tree changes. Report the count with the run, not as a tree property. `math-o3a.2.1` re-measured 2026-10-11 at 03:49 UTC over the **65**-file tree: five runs read **7, 7, 7, 7, 7**. After `catlib/atomic.py` gained its `catlib.paths` import for the staging root, eleven further runs read **8, 8, 8, 7, 8, 8, 7, 8, 7, 7, 7** — the same 7/8 run-order dependence the 64-file record describes, not a tree change: `catlib.paths` imports nothing inside the package, so the added edge closes no cycle, and the 8s are the runs that report the bare pair. `math-o3a.3` re-measured 2026-10-11 at 05:15 UTC over the **66**-file tree: **1** cycle, and the run-order dependence is **gone** — five runs of the same command read **1, 1, 1, 1, 1**. The cycle is `catlib.templates → render_reports → measure_templates`, the chain the census module's deferred `import catlib.templates` inside `registry()` closes. The 7-cycle chain set dissolved: `math-o3a.3` removed `from catlib import render as RD` from `measure_names.py`, `measure_topics.py`, `measure_proof_density.py` and `check_index_links.py`, and those four lines were the closing edge of every chain through `render_reports`. With no chain left, the bare pair `catlib.render → render_reports` is not reported, so the 7/8 swing has nothing to swing between. This is the dependency shape the epic exists to remove: the writer fleet no longer imports the render-diff module. Re-measured 2026-10-11 at 06:42 UTC over the 67-file tree: **1** cycle, the same `catlib.templates → render_reports → measure_templates` — `measure_open_probe.py` imports `catlib.paths` and `catlib.atomic` only, so it enters no chain. Re-measured 2026-10-12 at 00:37 UTC over the 75-file tree: **1** cycle, the same chain, and the run-order dependence stays gone — `measure_names.py`'s record-store rewrite added module-level `from catlib.promote import key_for` and `from catlib.records import cached`, and both package modules import only `catlib.paths` / `catlib.atomic`, so neither closes a chain through `render_reports`. |

Removed in the same pass as the boilerplate: pylint `wrong-import-position` (`C0413`), exempted for
**40** baseline sites. `pylint --enable=C0413` measures **61** findings on the tree that still had
the inserts and **0** on the tree that does not, so the disable is deleted from `.pylintrc` and the
gate stays green.

## mypy per-file status

Under `mypy.ini` the gate command checks **75 files with 0 errors**. `check_untyped_defs = False`,
so a function with no annotations is not analyzed — the gate proves the annotated surface, not the
whole tree. The 3 baseline errors were real and are fixed: `compare_abstracts.py:63`
(`_CACHE: dict = {}`), `build_index.py:166` (`WRITTEN: set = set()`), and a `None` guard in
`verify_named_results.py` that now narrows `rel`/`ln` before use.

The per-file figure is the **strict probe**, which is not a gate command:

```bash
.venv/bin/mypy --check-untyped-defs notes/scripts/   # 191 errors in 35 files (75 checked)
```

Its 191 findings are an annotation backlog, not defects: `var-annotated` 75 (an empty `dict`/`list`
accumulator mypy cannot infer), `assignment` 46, `union-attr` 28, `misc` 10, `index` 10, `arg-type` 8,
`operator` 5, `attr-defined` 2, `str-format` 2, `call-overload` 2, `type-var` 1, `str-unpack` 1,
`func-returns-value` 1. **40 of 75 files are clean under the probe** —
`build_catalog.py`, `build_report_templates.py`, `check_index_links.py`, `dump_template_slots.py`, `extract_subfinding_pairs.py`,
`extract_verification_348.py`, `gate.py`, `locate_summary_quotes.py`, `measure_anchor_blocks.py`, `measure_checker_needles.py`, `measure_faithfulness.py`, `measure_move_surface.py`, `measure_open_probe.py`, `measure_templates.py`, `read_manuscript.py`,
`render_reports.py`, `triage_t0.py`, `verify_cache_promotion.py`, `verify_counterexample_crosscheck.py`, `verify_index_design.py`,
`verify_named_results.py`, `verify_fleet_design.py`, `verify_page_sync.py`, and all 17 files under `catlib/` — `catlib/summaries.py` included.
`math-6s7.2` re-measured 2026-10-10 at 22:31 UTC: **197 errors in 34 files, the same 28-file clean set**,
byte-neutral. It briefly read 199 in 35: annotating `bundle_files` as `dict[str, Path]` made `n` a `str`
in the 348 extractor's byte-identity pass, so the later `for n in ap` (a line-number loop) collided with
it — `[assignment]` + `[operator]`. Renaming the second loop to `ln` cleared both; the strict probe
surfaced it because the shared function is annotated and the extractor body is not.
`math-6s7.3` re-measured at 22:52 UTC: **197 errors in 34 files, the same 28-file clean set** — the
T0 port is byte-neutral, and `triage_t0.py` stays in the clean set after moving its bucket rule out.
`math-6s7.5` re-measured at 23:00 UTC: **197 errors in 34 files, the same 28-file clean set** over the
63-file tree — `catlib/templates.py` arrives clean under the probe (it is fully annotated), so the
34-file error set is unchanged and the clean set gains the new package module as a 29th member of the
`catlib/` group. `math-o3a.1` re-measured 2026-10-11 at 02:44 UTC: **197 errors in 34 files** over the
64-file tree, the clean set **28 → 30** — `verify_fleet_design.py` is fully annotated and arrives clean,
and the 34-file error set is unchanged, so the rise is the new file plus the `catlib/templates.py` the
23:00 UTC count had already absorbed. `math-o3a.2.1` re-measured 2026-10-11 at 03:49 UTC:
**197 errors in 34 files** over the 65-file tree, the clean set **30 → 31** — `catlib/atomic.py` is
fully annotated and arrives clean, and the 34-file error set, the per-file distribution, and the
13-code split are all unchanged, so the writers' move through `write_atomic` added no finding.
`math-o3a.3` re-measured 2026-10-11 at 05:16 UTC: **195 errors in 34 files** over the 66-file tree, the
clean set **31 → 32** — `verify_page_sync.py` is fully annotated and arrives clean. The 197 → 195 fall is
`assignment` 46 → 45 and `operator` 6 → 5, both in `extract_links.py`: the sync pass typed `sync` as a
`Path` (it was built from `PAGE = REPO / "notes" / "links.md"`), then assigned the report string to it
and added a `str` to a `Path` on the next line, so deleting the pass deleted both findings and the file
leaves the 34-file error set. `measure_proof_density.py` stays in the set — its sync pass was a
`RD.sync_problems` call with no string arithmetic, so removing it moved no finding.
`math-o3a.3.4` re-measured 2026-10-11 at 06:42 UTC: **195 errors in 34 files** over the 67-file tree,
the clean set **32 → 33** — `measure_open_probe.py` is fully annotated and arrives clean, and the
34-file error set, the per-file distribution, and the 13-code split are all unchanged, so the promoted
probe added no finding. It carried two on arrival and they were fixed before the count: the probe
reused `ms` for a joined mode string in one loop and a `set[str]` in the next, which mypy read as
`[assignment]` plus `[operator]`; the first is now `shown`.
`math-faz.1` re-measured 2026-10-11 at 21:21 UTC: **199 errors in 35 files** over the 75-file tree,
the clean set **33 → 40**. The tree gained 8 files since 06:42 UTC: `gate.py`, `measure_faithfulness.py`,
`verify_cache_promotion.py`, `catlib/promote.py`, `catlib/records.py` and the two `math-faz` move probes
arrive clean, and `verify_faithfulness.py` arrives in the error set with 5 findings, which is the
34 → 35 rise. The 195 → 199 is that 5 less one `union-attr` that left elsewhere; the split moves
`var-annotated` 79 → 83 and `assignment` 45 → 46 and every other code is unchanged. The probes carried
one finding on arrival and it was fixed before the count: `measure_anchor_blocks.py` reused `h` for a
5-tuple in the block loop and a 3-tuple in the quotation loop, which mypy read as `[assignment]`; the
loops now use `b` and `q`.

`math-faz.2` re-measured 2026-10-12 at 00:37 UTC: **191 errors in 35 files** over the 75-file tree,
the clean set **40** unchanged. The 199 → 191 fall is `var-annotated` **83 → 75** and every other code
is unchanged (`assignment` 46, `union-attr` 28, `misc` 10, `index` 10, `arg-type` 8, `operator` 5,
`str-format` 2, `call-overload` 2, `attr-defined` 2, `type-var` 1, `str-unpack` 1,
`func-returns-value` 1). All 8 are in `measure_names.py`: making the measurement a record producer
means `build_records()` is annotated (it returns the record text), so mypy checks its body, and the
eight accumulators it needed (`ms_title`, `env_hits`, `surfaces`, `cap`, `mid`, `low`, `variants`,
`rejected`) are now declared. One of them surfaced a real narrowing problem the probe caught:
`env_hits` must be `dict[str, list[tuple[str | None, str]]]`, because `fam` comes from
`dir2fam.get(...)` and can be `None` — the annotation the probe forced is the annotation the code
needs. `measure_names.py` stays in the 35-file error set.

The count rises as checkers move onto the package, and the rise is not a regression: `catlib` is
fully annotated, so a ported file's previously opaque calls (`read_text`, `read_rows`, `bib.read`)
become typed call surfaces the probe can analyze. `extract_citations.py` 7 → 32 and
`verify_citations.py` 8 → 11 across `math-lon.2.4` are that effect; the added findings are the
accumulators and string paths the probe can now see through, and they are the annotation backlog.

Measured 2026-10-10 over the 62-file tree: **197** findings over **34** files, the **28** clean files
being the list above — `measure_checker_needles.py` and `catlib/summaries.py` both arrive clean under
the probe, so the 34-file error set is unchanged by the promotion and by `math-6s7.1`. The port moved
three findings inside the same total: `var-annotated` 81 → 79 (the accumulators the moved parse now
annotates), `operator` 5 → 6 (`check_summary_manuscripts.py:63`, where the shared root rule can return
`None`), and `type-var` 0 → 1 (`verify_summaries.py:205`) — the last two are newly visible because the
ported calls are typed, which is the effect the paragraph above describes. Against the 200-finding /
36-file snapshot this table replaces, three files moved: `extract_links.py` 9 → 11, while
`check_index_links.py` 3 → 0 and `extract_subfinding_pairs.py` 2 → 0 — both are clean under the probe
today.

| Errors | File |
|---|---|
| 35 | `verify_upstream_history.py` |
| 32 | `extract_citations.py` |
| 12 | `build_index.py` |
| 11 | `verify_citations.py`, `extract_links.py` |
| 10 | `verify_scope_exclusions.py`, `measure_names.py` |
| 6 | `verify_findings.py` |
| 5 | `build_sources.py`, `compare_abstracts.py`, `verify_sources.py`, `verify_subfinding_pairs.py` |
| 4 | `measure_proof_density.py`, `verify_named_conjectures.py`, `verify_summaries.py`, `verify_t0_chains.py` |
| 3 | `extract_formalization_deps.py`, `extract_named_results.py`, `measure_index_sizes.py`, `measure_topics.py`, `verify_subfindings.py` |
| 2 | `extract_subfindings.py`, `extract_verification_dirs.py`, `verify_abstracts.py`, `verify_conjecture_standing.py`, `verify_script_ownership.py`, `verify_verification_dirs.py` |
| 1 | `check_summary_manuscripts.py`, `extract_counterexample_crosscheck.py`, `extract_scope_notes.py`, `extract_t0_chains.py`, `refresh_summary_line_counts.py`, `verify_conditional.py`, `verify_dependency_drift.py` |

## pylint triage

Trajectory: 1,422 on the default run → 142 with `.pylintrc` → **38** measured after the 113 ruff
autofixes (the autofix pass cleared 104 of the 142) → **21** after the manual fixes below → **0**
after the last three exemptions.

Fixed, with the site:

| Code | Count | Fix |
|---|---|---|
| `W0613` unused-argument | 5 | Parameters renamed to `_`-prefixed dummies — `check_files(_m, problems)` (`verify_t0_chains.py:343`), `lean_paths(_fams, docs)` (`measure_topics.py:91`), `seen_nt_order(rows, _M)` (`verify_citations.py:481`), `check_page(name, text, _p, problems)` and `check_needles(_p, problems)` (`verify_upstream_history.py:275,338`). Pylint's default `dummy-variables-rgx` exempts them; every call site passes the argument positionally, so no caller changed. |
| `W1514` unspecified-encoding | 4 | `encoding="utf-8"` at `check_index_links.py:337`, `extract_named_results.py:89`, `measure_names.py:70`, and the `os.devnull` sink in `verify_summaries.py`. |
| `W0106` expression-not-assigned | 2 | `verify_abstracts.py`: two `x.append(...) if cond else None` expressions became `if` statements. |
| `W0640` cell-var-from-loop | 1 | `compare_abstracts.py:146` binds the loop value as a default: `key=lambda x, ov=ov: ratio(ov, x[1])`. |
| `E0102` function-redefined | 1 | `verify_dependency_drift.py:298` rebound the name `want` (a tuple-unpack) over the function defined at `:333`; the local is now `want_q`. |
| `C0207` use-maxsplit-arg | 1 | `build_index.py:682` → `name.rsplit('/', 1)[-1][:-4]`. |
| `C0325` superfluous-parens | 2 | `verify_named_conjectures.py:188,278` → `if not 1 <= a <= b <= len(lines):`. |
| `C0411` wrong-import-order | 1 | `measure_names.py`: `import csv` moved into the stdlib block. |

Exempted in the same pass — the 21 findings that remained, as three codes:

| Code | Count | Reason |
|---|---|---|
| `C0206` consider-using-dict-items | 16 | Comprehensions that iterate a dict's keys and index it (`sum(1 for f in fams if ... fams[f]["abstract"] ...)`). The key is the family number the report line names, so `.items()` drops the name the measurement is about. |
| `C0200` consider-using-enumerate | 4 | The pair window `for i in range(len(ms)): for j in range(i + 1, len(ms)):`, which `enumerate` does not express. |
| `R0902` too-many-instance-attributes | 1 | `catlib/summaries.py`'s `Page` class is a parsed-page data holder, not a behaviour class — the site moved there with the parse on 2026-10-10 (`math-6s7.1`). |

## The import boilerplate pass (math-lon.1)

A script run as `python3 notes/scripts/foo.py` already has `notes/scripts` as `sys.path[0]`, so all
**31** `sys.path.insert` sites — every one naming that same directory — added nothing. Dropping them
and hoisting the sibling imports above the first module-level statement removed **31** insert lines,
the **13** `# noqa: E402` markers they needed, **7** `import sys` that became unused, and **3**
`import pathlib` that only built the inserted path: **31 files changed**, all 52 byte-compile clean,
**0** inserts and **0** markers left. `ruff check --select E402` reports nothing and
`pylint --enable=C0413` reports **0**, which is why the `C0413` disable is gone from `.pylintrc`.

The transform was validated on a copy of the tree first, which is where its bugs were found:
hoisting above the shebang, above the module docstring (including the `r"""` form), splitting a
comment from the statement it documents, landing inside a parenthesised import list (the depth check
must be cumulative over the block, not per line), and re-inserting a blank line inside that list.

## What has not been checked

- **Behaviour.** The linters prove style and typing facts only. The autofix pass ran with
  `--fix --unsafe-fixes` and took ruff from 287 findings to 26; the 26 were fixed by hand. The
  evidence that none of it changed any output is the gate — **75** invocations run once, with every
  tracked artifact's cached bytes compared with the bytes on its tracked path (`notes/scripts/README.md`).
  The trio was not green at `HEAD` before `math-faz.1`: `gate.py:140` carried one `RUF005` finding, the
  `[a, b] + c` list concatenation in the row command, and it is fixed to `[a, b, *c]` — the same list,
  so the command each row spawns is unchanged.
- **No test suite.** The generator report is the test, so a lint fix is verified by report
  equality, not by unit tests.
- **The strict probe is not scheduled.** The 191-error `--check-untyped-defs` backlog above is a
  work estimate; nothing runs that command as a gate.
- **`duplicate-code` is off corpus-wide** — **29** findings measured with `--enable=R0801` over 57
  files after **all 19** checkers moved onto the package, re-measured 2026-10-10 at **40** over 62
  files, 2026-10-11 at 03:49 UTC at **39** over 65 files, 2026-10-11 at 05:12 UTC at **38** over
  66 files, and 2026-10-12 at 00:37 UTC at **47** over 75 files, and nothing automatic re-enables
  it. `math-lon.1` moved the joins into `catlib/`; `math-lon.2.1` moved the anchor grammar there,
  which is why every cluster is now reported against `catlib/anchors.py`; `math-lon.2.4` moved the
  `.bib` primitives into `catlib/bib.py`, which is where the pair window and component scan lived
  twice. What the port did not remove is the duplication that is the design: the `catlib/anchors.py`
  loops every checker's anchor pass is measured against, and the extract-to-verify measurement pairs
  where the checker re-derives the population from the corpus instead of trusting the extractor's
  report.
- **jinja2 is used by `build_index.py` and `render_reports.py`** — `math-a0r.3` moved the prose of
  every generated index page into `notes/templates/`: `family.md.j2`, `discipline.md.j2`,
  `topic.md.j2`, `name.md.j2`, and `index-readme.md.j2` (**5** skeletons); `math-a0r.4` added the
  report templates under `notes/templates/report/`, and `math-a0r.5` added `names.md.j2`,
  `proof-density.md.j2`, `index-links.md.j2`, `links.md.j2`, `dependency-drift.md.j2` and
  `verification-dirs.md.j2` and `scope-exclusions.md.j2` and `topics.md.j2` and `t0-chains.md.j2` and `subfinding-pairs.md.j2` — **17**
  templates under `notes/templates/report/` (counted on disk 2026-10-11 at 03:49 UTC), rendered by
  `render_reports.py`. Both
  render through `python3` under the gate (gate.py runs plain `python3`, not the venv interpreter), so
  the gate depends on jinja2 being importable by the system interpreter too; both interpreters report
  **3.1.6** here.
- **The venv is untracked.** `.venv/` is in `.gitignore`, so the versions in the table above are
  recorded only on this page — nothing in git pins them.
- **Mutant lists.** The checkers' `--mutant` self-tests run in the gate; a lint fix that moved a
  quotation needle would surface there, not in a linter.
