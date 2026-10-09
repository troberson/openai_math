# Linting the ledger scripts

The venv, the three tool configs, the commands, and every exemption with the count it covers.
Created for `math-e8k`. The three commands below are the lint gate; the twice-run gate that proves a
lint fix changed no generated output runs from the scratch list at `.qwen/tmp/gate.sh` (promoted to
`notes/scripts/` by `math-8ou`), and the idempotence discipline it implements is recorded in
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

`python -m py_compile notes/scripts/*.py` passes for all 44 under the venv interpreter.

## Exemptions

Each row is a rule the config turns off, the count it produced on the baseline, and why the finding
is not a defect in this tree.

| Rule | Count | Reason |
|---|---|---|
| ruff `UP031` / pylint `consider-using-f-string` | 166 / 160 | Report strings are %-formatting templates reused across tiers; converting 166 of them re-wraps the report output the checkers compare against. |
| ruff `ISC004` | 80 | Implicit concatenation inside a list literal is how the mutant tables are written. |
| ruff `FURB167` | 60 | `re.M` is the local alias convention for regex flags. |
| ruff `FURB188` | 8 | Single-character prefix/slicing where `removeprefix` adds nothing. |
| ruff `I001` | 4 | The sibling-module import pattern: `sys.path.insert` above the import, marked `# noqa: E402`. |
| pylint `line-too-long` | 351 | Report lines embed manuscript paths and verbatim quotations. |
| pylint `missing-function-docstring` | 194 | A report function's contract is the report line it prints; the module docstring states what the script measures. |
| pylint `too-many-*` | 80+37+35+5+3+2 | A generator that reconciles a corpus is wide by design; the metrics describe the report. |
| pylint `wrong-import-position` | 40 | Same sys.path.insert pattern as ruff `I001`. |
| pylint `invalid-name` | 12 | Module path constants are UPPER_CASE; extractors use short loop variables. |
| pylint `duplicate-code` | 24 | The measured duplication that `math-lon.1` removes; re-enabled after the shared package lands. |
| pylint `global-statement` | 3 | Report accumulators are module-level by design. |
| pylint `unsubscriptable-object` | 6 | `prev` is `None`-guarded before the subscript in `verify_dependency_drift.py:169-170` and `extract_formalization_deps.py:162-163`; pylint does not track the narrowing. |

## mypy per-file status

Under `mypy.ini` the gate command checks **44 files with 0 errors**. `check_untyped_defs = False`,
so a function with no annotations is not analyzed — the gate proves the annotated surface, not the
whole tree. The 3 baseline errors were real and are fixed: `compare_abstracts.py:64`
(`_CACHE: dict = {}`), `build_index.py:160` (`WRITTEN: set = set()`), and a `None` guard in
`verify_named_results.py` that now narrows `rel`/`ln` before use.

The per-file figure is the **strict probe**, which is not a gate command:

```bash
.venv/bin/mypy --check-untyped-defs notes/scripts/   # 168 errors in 37 files (44 checked)
```

Its 168 findings are an annotation backlog, not defects: `var-annotated` 93 (an empty `dict`/`list`
accumulator mypy cannot infer), `assignment` 41, `union-attr` 25, `index` 3, `attr-defined` 2,
`operator` 2, `misc` 1, `func-returns-value` 1. **7 of 44 files are clean under the probe** —
`extract_verification_348.py`, `locate_summary_quotes.py`, `read_manuscript.py`, `triage_t0.py`,
`verify_conditional.py`, `verify_index_design.py`, `verify_named_results.py`.

| Errors | File |
|---|---|
| 33 | `verify_upstream_history.py` |
| 11 | `build_index.py` |
| 9 | `extract_links.py` |
| 8 | `verify_citations.py`, `measure_names.py` |
| 7 | `extract_citations.py` |
| 6 | `verify_findings.py`, `verify_scope_exclusions.py`, `verify_counterexample_crosscheck.py` |
| 5 | `compare_abstracts.py`, `verify_subfinding_pairs.py` |
| 4 | `measure_proof_density.py`, `verify_named_conjectures.py`, `verify_summaries.py`, `verify_t0_chains.py` |
| 3 | `build_catalog.py`, `build_sources.py`, `check_index_links.py`, `extract_formalization_deps.py`, `extract_named_results.py`, `measure_index_sizes.py`, `measure_topics.py`, `verify_sources.py`, `verify_subfindings.py`, `verify_verification_dirs.py` |
| 2 | `extract_subfinding_pairs.py`, `extract_subfindings.py`, `extract_verification_dirs.py`, `verify_abstracts.py`, `verify_conjecture_standing.py`, `verify_script_ownership.py` |
| 1 | `check_summary_manuscripts.py`, `extract_counterexample_crosscheck.py`, `extract_scope_notes.py`, `extract_t0_chains.py`, `refresh_summary_line_counts.py`, `verify_dependency_drift.py` |

## pylint triage

Trajectory: 1,422 on the default run → 142 with `.pylintrc` → **38** measured after the 113 ruff
autofixes (the autofix pass cleared 104 of the 142) → **21** after the manual fixes below → **0**
after the last three exemptions.

Fixed, with the site:

| Code | Count | Fix |
|---|---|---|
| `W0613` unused-argument | 5 | Parameters renamed to `_`-prefixed dummies — `check_files(_m, problems)` (`verify_t0_chains.py:359`), `lean_paths(_fams, docs)` (`measure_topics.py:92`), `seen_nt_order(rows, _M)` (`verify_citations.py:495`), `check_page(name, text, _p, problems)` and `check_needles(_p, problems)` (`verify_upstream_history.py:269,332`). Pylint's default `dummy-variables-rgx` exempts them; every call site passes the argument positionally, so no caller changed. |
| `W1514` unspecified-encoding | 4 | `encoding="utf-8"` at `check_index_links.py:337`, `extract_named_results.py:89`, `measure_names.py:68`, and the `os.devnull` sink in `verify_summaries.py`. |
| `W0106` expression-not-assigned | 2 | `verify_abstracts.py`: two `x.append(...) if cond else None` expressions became `if` statements. |
| `W0640` cell-var-from-loop | 1 | `compare_abstracts.py:147` binds the loop value as a default: `key=lambda x, ov=ov: ratio(ov, x[1])`. |
| `E0102` function-redefined | 1 | `verify_dependency_drift.py:298` rebound the name `want` (a tuple-unpack) over the function defined at `:333`; the local is now `want_q`. |
| `C0207` use-maxsplit-arg | 1 | `build_index.py:952` → `name.rsplit('/', 1)[-1][:-4]`. |
| `C0325` superfluous-parens | 2 | `verify_named_conjectures.py:184,275` → `if not 1 <= a <= b <= len(lines):`. |
| `C0411` wrong-import-order | 1 | `measure_names.py`: `import csv` moved into the stdlib block. |

Exempted in the same pass — the 21 findings that remained, as three codes:

| Code | Count | Reason |
|---|---|---|
| `C0206` consider-using-dict-items | 16 | Comprehensions that iterate a dict's keys and index it (`sum(1 for f in fams if ... fams[f]["abstract"] ...)`). The key is the family number the report line names, so `.items()` drops the name the measurement is about. |
| `C0200` consider-using-enumerate | 4 | The pair window `for i in range(len(ms)): for j in range(i + 1, len(ms)):`, which `enumerate` does not express. |
| `R0902` too-many-instance-attributes | 1 | `verify_summaries.py`'s `Page` class is a parsed-page data holder, not a behaviour class. |

## What has not been checked

- **Behaviour.** The linters prove style and typing facts only. The autofix pass ran with
  `--fix --unsafe-fixes` and took ruff from 287 findings to 26; the 26 were fixed by hand. The
  evidence that none of it changed any output is the gate — 61 invocations run twice with every
  generated artifact md5-snapshotted and diffed (`notes/scripts/README.md`).
- **No test suite.** The generator report is the test, so a lint fix is verified by report
  equality, not by unit tests.
- **The strict probe is not scheduled.** The 168-error `--check-untyped-defs` backlog above is a
  work estimate; nothing runs that command as a gate.
- **`duplicate-code` is off corpus-wide** (24 sites) and nothing automatic re-enables it;
  `math-lon.1` is where the shared package lands and the message is switched back on.
- **jinja2 is installed and unused** until `math-a0r`.
- **The venv is untracked.** `.venv/` is in `.gitignore`, so the versions in the table above are
  recorded only on this page — nothing in git pins them.
- **Mutant lists.** The checkers' `--mutant` self-tests run in the gate; a lint fix that moved a
  quotation needle would surface there, not in a linter.
