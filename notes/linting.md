# Linting the ledger scripts

The venv, the three tool configs, the commands, and every exemption with the count it covers.
Created for `math-e8k`. The three commands below are the lint gate; the twice-run gate that proves a
lint fix changed no generated output runs from the gate list at `notes/scripts/gate.sh` (promoted
there from `.qwen/tmp/` by `math-8ou`), and the idempotence discipline it implements is recorded in
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
.venv/bin/ruff check notes/scripts/      # exit 0
.venv/bin/mypy notes/scripts/            # exit 0
.venv/bin/pylint notes/scripts/          # exit 0
```

Configs: `ruff.toml`, `mypy.ini`, `.pylintrc` at the repository root. Each carries its exemptions
as comments; the tables below are the same list with the measured counts.

## Baseline (2026-10-09, before any fix)

| Tool | Default run | With the repo config | After the fixes |
|---|---|---|---|
| ruff | 446 findings over 44 scripts | 287 | **0** (287 → 26 by autofix, 26 → 0 by hand) |
| mypy | 3 errors in 3 files (44 checked) | 3 | **0** (3 → 0) |
| pylint | 1,422 findings over 44 scripts | 142 | **0** (142 → 38 after the ruff autofixes, 38 → 21 by hand, 21 → 0 by the last three exemptions) |

`python -m py_compile notes/scripts/*.py` passes for all 44 under the venv interpreter. The tree is
**57 source files** today — **46** scripts plus `catlib/`'s **11** — and every current-state figure
below is measured over 57; the baseline row above is the 44-file tree it was measured on.

## Exemptions

Each row is a rule the config turns off, the count it produced on the baseline, and why the finding
is not a defect in this tree.

| Rule | Count | Reason |
|---|---|---|
| ruff `UP031` / pylint `consider-using-f-string` | 166 / 160 | Report strings are %-formatting templates reused across tiers; converting 166 of them re-wraps the report output the checkers compare against. |
| ruff `ISC004` | 80 | Implicit concatenation inside a list literal is how the mutant tables are written. |
| ruff `FURB167` | 60 | `re.M` is the local alias convention for regex flags. |
| ruff `FURB188` | 8 | Single-character prefix/slicing where `removeprefix` adds nothing. |
| ruff `I001` | 4 → **14** | Import blocks are not isort-ordered: stdlib, then the sibling extractors, then `catlib`, in the order the reader follows them. Measured **13** before and **14** after the `sys.path.insert` boilerplate was dropped — the insert was never what made the block unsorted, so the exemption stays. |
| pylint `line-too-long` | 351 | Report lines embed manuscript paths and verbatim quotations. |
| pylint `missing-function-docstring` | 194 | A report function's contract is the report line it prints; the module docstring states what the script measures. |
| pylint `too-many-*` | 80+37+35+5+3+2 | A generator that reconciles a corpus is wide by design; the metrics describe the report. |
| pylint `invalid-name` | 12 | Module path constants are UPPER_CASE; extractors use short loop variables. |
| pylint `duplicate-code` | 24 → 28 → 26 → 26 → 24 → 22 → **29** | Measured 2026-10-09 with `--enable=R0801` over 57 files, after **all 19** checkers moved onto the package: **all 29** findings are attributed to `catlib/anchors.py`, whose anchor/fence loops are the reference side of every cluster (pylint reports a cluster under its first module). The 29 clusters pair 58 module entries: `render_reports` 7, `verify_sources` 6, `verify_index_design` 6, `verify_citations` 6, `extract_citations` 5, `verify_verification_dirs` 4, `extract_subfindings` 4, `verify_subfindings` 3, `verify_named_results` 2, `verify_dependency_drift` 2, `verify_counterexample_crosscheck` 2, `verify_conditional` 2, `catlib.overview` 2, and 7 singletons (`catlib.bib`, `catlib.text`, `extract_formalization_deps`, `locate_summary_quotes`, `verify_abstracts`, `verify_scope_exclusions`, `verify_summaries`). The 22 → 29 rise is `math-a0r.4`: `render_reports.py` arrives with 7 clusters because it re-derives, on the writer side, the anchor and phrase loops its four pages' checkers measure on the checker side — the split is the point of the design, so those clusters are the by-design extract-to-verify pair, not a shared-helper opportunity. `verify_sources` 3 → 6 and `verify_index_design` 5 → 6 are the same pair seen from the checker's side of that split, and `verify_named_results` 0 → 2 plus the `verify_abstracts` singleton are its two remaining anchor loops. Two clusters left and none arrived earlier, so the net is 24 → 22: out go the pair window and the connected-component scan, which were `verify_citations.py:140-146` and `:147-153` against `extract_citations.py` and are now one `catlib.bib.pair_counts` / `catlib.bib.clusters` call in each file. The 6 that remain on that pair are the extractor↔checker measurement loop — the checker re-derives the population from the corpus rather than trusting the report — which stays by design. `math-lon.2` ported the last **2** checkers (`verify_upstream_history.py`, `verify_summaries.py`) and moved no cluster. |
| pylint `global-statement` | 3 | Report accumulators are module-level by design. |
| pylint `unsubscriptable-object` | 6 | `prev` is `None`-guarded before the subscript in `verify_dependency_drift.py:169-170` and `extract_formalization_deps.py:161-162`; pylint does not track the narrowing. |
| pylint `exec-used` (inline, not in `.pylintrc`) | 1 | `build_report_templates.py:89` — the template builder loads its page's checker by `exec` to read its needle list, which the builder reports as **coverage** (how many of the checker's needles the template slots) and never uses as the slot source. The slots come from the writer's own label dict in `render_reports.py`, so a template cannot reference a label the writer does not supply. The file is a builder, not a checker: the page's own checker still re-derives the counts independently. |

Removed in the same pass as the boilerplate: pylint `wrong-import-position` (`C0413`), exempted for
**40** baseline sites. `pylint --enable=C0413` measures **61** findings on the tree that still had
the inserts and **0** on the tree that does not, so the disable is deleted from `.pylintrc` and the
gate stays green.

## mypy per-file status

Under `mypy.ini` the gate command checks **57 files with 0 errors**. `check_untyped_defs = False`,
so a function with no annotations is not analyzed — the gate proves the annotated surface, not the
whole tree. The 3 baseline errors were real and are fixed: `compare_abstracts.py:63`
(`_CACHE: dict = {}`), `build_index.py:166` (`WRITTEN: set = set()`), and a `None` guard in
`verify_named_results.py` that now narrows `rel`/`ln` before use.

The per-file figure is the **strict probe**, which is not a gate command:

```bash
.venv/bin/mypy --check-untyped-defs notes/scripts/   # 200 errors in 36 files (57 checked)
```

Its 200 findings are an annotation backlog, not defects: `var-annotated` 86 (an empty `dict`/`list`
accumulator mypy cannot infer), `assignment` 45, `union-attr` 29, `misc` 10, `index` 10, `arg-type` 8,
`operator` 4, `attr-defined` 2, `str-format` 2, `call-overload` 2, `str-unpack` 1,
`func-returns-value` 1. **21 of 57 files are clean under the probe** —
`build_catalog.py`, `build_report_templates.py`, `extract_verification_348.py`,
`locate_summary_quotes.py`, `read_manuscript.py`, `render_reports.py`, `triage_t0.py`,
`verify_counterexample_crosscheck.py`, `verify_index_design.py`,
`verify_named_results.py`, and all 11 files under `catlib/`.

The count rises as checkers move onto the package, and the rise is not a regression: `catlib` is
fully annotated, so a ported file's previously opaque calls (`read_text`, `read_rows`, `bib.read`)
become typed call surfaces the probe can analyze. `extract_citations.py` 7 → 32 and
`verify_citations.py` 8 → 11 across `math-lon.2.4` are that effect; the added findings are the
accumulators and string paths the probe can now see through, and they are the annotation backlog.

| Errors | File |
|---|---|
| 35 | `verify_upstream_history.py` |
| 32 | `extract_citations.py` |
| 12 | `build_index.py` |
| 11 | `verify_citations.py` |
| 10 | `verify_scope_exclusions.py`, `measure_names.py` |
| 9 | `extract_links.py` |
| 6 | `verify_findings.py` |
| 5 | `build_sources.py`, `compare_abstracts.py`, `verify_sources.py`, `verify_subfinding_pairs.py` |
| 4 | `measure_proof_density.py`, `verify_named_conjectures.py`, `verify_summaries.py`, `verify_t0_chains.py` |
| 3 | `check_index_links.py`, `extract_formalization_deps.py`, `extract_named_results.py`, `measure_index_sizes.py`, `measure_topics.py`, `verify_subfindings.py` |
| 2 | `extract_subfinding_pairs.py`, `extract_subfindings.py`, `extract_verification_dirs.py`, `verify_abstracts.py`, `verify_conjecture_standing.py`, `verify_script_ownership.py`, `verify_verification_dirs.py` |
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
| `R0902` too-many-instance-attributes | 1 | `verify_summaries.py`'s `Page` class is a parsed-page data holder, not a behaviour class. |

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
  evidence that none of it changed any output is the gate — 63 invocations run twice with every
  generated artifact md5-snapshotted and diffed (`notes/scripts/README.md`).
- **No test suite.** The generator report is the test, so a lint fix is verified by report
  equality, not by unit tests.
- **The strict probe is not scheduled.** The 200-error `--check-untyped-defs` backlog above is a
  work estimate; nothing runs that command as a gate.
- **`duplicate-code` is off corpus-wide** — **29** findings measured with `--enable=R0801` over 57
  files after **all 19** checkers moved onto the package, and nothing automatic re-enables
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
  **4** report templates under `notes/templates/report/`, rendered by `render_reports.py`. Both
  render through `python3` under the gate (gate.sh runs plain `python3`, not the venv interpreter), so
  the gate depends on jinja2 being importable by the system interpreter too; both interpreters report
  **3.1.6** here.
- **The venv is untracked.** `.venv/` is in `.gitignore`, so the versions in the table above are
  recorded only on this page — nothing in git pins them.
- **Mutant lists.** The checkers' `--mutant` self-tests run in the gate; a lint fix that moved a
  quotation needle would surface there, not in a linter.
