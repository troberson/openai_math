# Scripts and generated files

Measured 2026-10-09 by `python3 notes/scripts/verify_script_ownership.py` — report-only, it writes
nothing, and every count below is re-derived by that run. The page answers one question: for each of
the **1,124** files under `notes/` (the scripts excluded), which is whose bytes. A generated file is
changed by editing its generator and re-rendering; a hand-written file is edited directly. Ownership
is per file, and the checker exits 1 on a file no rule owns.

It is also the script inventory. Every script under `notes/scripts/` is listed once, in one of three
classes — writer, report-only, checker — with what it writes and the command the gate runs for it, and
the fourth class, the scratch a session writes outside the tree, is recorded by rule rather than by
file. The classes partition the **46** scripts: **9** writers, **18** report-only, **18** checkers,
and `verify_script_ownership.py` itself, which is the 19th checker and is not listed in its own table.

## The split: 9 write, 36 write nothing

The writer set is derived from the scripts' own source, not from this page: a script is a writer when
a path constant rooted at `notes/` appears on the left of `.open(..., "w")` or `.write_text(...)`,
plus the tree case — a `notes/index` constant reached through the module's own `write()` helper — and
plus one hop: a receiver built from a module constant (`out = TPL_DIR / (name)`, then
`out.write_text(...)`) is owned by that constant's directory, which is how a writer that names a
directory rather than a file stays visible. That rule
finds **9** writers over **45** scripts.

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
| `render_reports.py` | `notes/abstracts.md`, `notes/dependency-drift.md`, `notes/index-design.md`, `notes/index-links.md`, `notes/links.md`, `notes/named-results.md`, `notes/names.md`, `notes/proof-density.md`, `notes/sources.md`, `notes/verification-dirs.md`, `notes/scope-exclusions.md`, `notes/topics.md`, `notes/t0-chains.md`, `notes/subfinding-pairs.md` | run twice, byte-identical | the fourteen report-fed pages |
| `build_report_templates.py` | `notes/templates/report` | not in `gate.sh` — it reads each page with `git show HEAD:`, so a gate run would rewrite templates from committed bytes; run explicitly with 0 args (all fourteen pages) or 2 (one page) after a writer's slot dict changes | the fourteen page templates |

Six writers emit one TSV each. `build_index.py` is the one-to-many case: it renders **1,049** files —
**1,033** `.md` pages and **16** `.tsv` tables. `render_reports.py` renders the fourteen report-fed pages
from the templates `build_report_templates.py` builds from the committed page and the slot dict that
writer supplies. `compare_abstracts.py` is the conditional case: its
default run writes nothing and only `--tsv` touches `notes/abstracts.tsv`.

Writers import each other, so a generated file's bytes are not a function of one script.
`build_index.py` imports `build_catalog`, `measure_topics`, `measure_names`,
`check_index_links` and `jinja2` (the index page text lives in `notes/templates/*.j2`, the fourteen
report-fed page skeletons in `notes/templates/report/*.j2`);
`extract_links.py`, `extract_subfindings.py`, `compare_abstracts.py`,
`check_index_links.py`, `measure_names.py` and `measure_topics.py` all import `build_catalog`;
`measure_index_sizes.py` imports `check_index_links` inside its link-check function
(`measure_index_sizes.py:118`), not at module scope. Counted over `notes/scripts/*.py` as a script
that imports the module (`import X` or `from X`, the module itself excluded), `build_catalog.py` has
**18** importers, `build_sources.py` **1** (`verify_sources.py`; `read_manuscript.py` names it in a
docstring, not in an import) and `verify_summaries.py` **3** (`verify_scope_exclusions.py` for its
`norm()`, `locate_summary_quotes.py` and `refresh_summary_line_counts.py`). Editing a join in `build_catalog.py` can move
rows in six artifacts.

### Report-only

The other **36** scripts write nothing. **18** of them print the report a page's counts come from.
The Gate column is the invocation the gate list runs: `notes/scripts/gate.sh`, which runs **63**
invocations — the **8** gated writers, the 17 gated report-only rows (including `check_summary_manuscripts.py`
and `locate_summary_quotes.py`), and **38** checker invocations: each of the 18 checkers plain and
with `--mutant` (**36**), plus `verify_conjecture_standing.py` plain and with `--mutant` (**2**) — in
class order, not in the order the rows sit; it prints one line per invocation with its exit code and
writes nothing to the repo. `math-8ou` promoted it from `.qwen/tmp/` into `notes/scripts/`, closing
the one gap the list had. A writer's gate is the twice-run byte-identity diff on its target, recorded
in the writers table.

| Script | Report feeds | Gate |
|---|---|---|
| `check_index_links.py` | `notes/index-links.md` | plain |
| `check_summary_manuscripts.py` | `notes/summaries/` — which manuscripts each page reads, and whether the release still names them | plain |
| `extract_citations.py` | `notes/citations.md` | plain |
| `extract_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` | plain |
| `extract_named_results.py` | `notes/named-results.md` | plain |
| `extract_scope_notes.py` | `notes/scope-exclusions.md` | plain |
| `extract_subfinding_pairs.py` | `notes/subfinding-pairs.md` | plain |
| `extract_t0_chains.py` | `notes/t0-chains.md` | plain |
| `extract_verification_348.py` | `notes/verification-dirs.md` | plain |
| `extract_verification_dirs.py` | `notes/verification-dirs.md` | plain |
| `locate_summary_quotes.py` | `notes/summaries/` — the lines a page should cite when a quotation stops matching | plain, no page argument |
| `measure_index_sizes.py` | `notes/index-design.md` | plain, run twice and diff |
| `measure_names.py` | `notes/names.md` | plain |
| `measure_proof_density.py` | `notes/proof-density.md` | `--mutant` |
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
page's text.

### Checkers

The remaining **18** scripts verify a page or a table. Each exits non-zero when what it checks has
drifted; each takes `--mutant`, which injects faults and asserts they are caught. The gate runs each
one plain and then with `--mutant` — **38** of the 63 invocations: **36** from the loop over the 18
rows below, **2** more for `verify_conjecture_standing.py`, which the list runs outside the loop.

| Checker | Checks | Gate |
|---|---|---|
| `verify_abstracts.py` | `notes/abstracts.md` | plain + `--mutant` |
| `verify_citations.py` | `notes/citations.md` | plain + `--mutant` |
| `verify_conditional.py` | `notes/conditional.md` | plain + `--mutant` |
| `verify_conjecture_standing.py` | `notes/conjecture-standing.tsv` | plain + `--mutant` |
| `verify_counterexample_crosscheck.py` | `notes/counterexample-crosscheck.md` | plain + `--mutant` |
| `verify_dependency_drift.py` | `notes/dependency-drift.md`, `notes/formalization-deps.md` | plain + `--mutant` |
| `verify_findings.py` | `notes/findings.md` | plain + `--mutant` |
| `verify_index_design.py` | `notes/index-design.md` | plain + `--mutant` |
| `verify_named_conjectures.py` | `notes/named-conjectures.md` | plain + `--mutant` |
| `verify_named_results.py` | `notes/named-results.md` | plain + `--mutant` |
| `verify_scope_exclusions.py` | `notes/scope-exclusions.md` | plain + `--mutant` |
| `verify_sources.py` | `notes/sources.md` | plain + `--mutant` |
| `verify_subfinding_pairs.py` | `notes/subfinding-pairs.md` | plain + `--mutant` |
| `verify_subfindings.py` | `notes/subfindings.tsv` | plain + `--mutant` |
| `verify_summaries.py` | `notes/summaries/` | plain + `--mutant`, no page argument |
| `verify_t0_chains.py` | `notes/t0-chains.md` | plain + `--mutant` |
| `verify_upstream_history.py` | `upstream_history/` — the three pages, outside `notes/` | plain + `--mutant` |
| `verify_verification_dirs.py` | `notes/verification-dirs.md` | plain + `--mutant` |

`verify_conjecture_standing.py` is the one checker the list kept outside its loop: it ran plain only,
so its six mutants were never run by the gate. Measured 2026-10-09 by hand — `mutants 6  uncaught
0 []`, exit 0 — `math-8ou` added the `--mutant` invocation, which is why the count reads 63 and not
62.

`verify_script_ownership.py` — this page's own checker — is not in the table: a checker cannot list
itself as its input. It is the 19th checker and the 46th script the run counts.

## The shared package: `catlib/`

`notes/scripts/catlib/` holds the joins the extractors share, so a join is written once. It is 11
modules, not scripts: `paths.py` (the repo-root constants, `rel()`, `owner()`, `read_text()`),
`tsv.py` (the four TSV writer shapes), `overview.py` (the `\resultentry` parse), `ledger.py`
(`notes/catalog.tsv` and the claim-shape rules), `preprints.py` (the 749 dirs versus the 719 listed
manuscripts), `text.py` (the six normalizers), `yaml.py` (`main_results_entries()`, the scope-note
spans, the Lean-tree file list), `anchors.py` (the `path:line` anchor grammar, the fenced-block scan
and the nearest-preceding-anchor read the page checkers share), `bib.py` (the `.bib` entry parse, the
title normalizer, the citation-key read, the pair window and the component scan), `measure.py` (the
writer-side measurement API — the ledger and release counts as ints, sets and lists, with no report
formatting; checkers deliberately do **not** import it, because a checker that re-derives a count
through the page's own code proves nothing) and `__init__.py`. A
script run as `python3 notes/scripts/foo.py` has `notes/scripts` on `sys.path`, so it imports them as
`from catlib import ...` with no path boilerplate.

**33** of the **46** scripts call the package: **6** `extract_`, **3** `build_`, **2** `measure_`,
`check_index_links.py`, `read_manuscript.py`, `render_reports.py`, and **all 19** checkers — `math-lon.2.5` ported the last
two, `verify_upstream_history.py` and `verify_summaries.py`, and the **22** `duplicate-code` findings
did not move (measured 2026-10-09 with `--enable=R0801` over 55 files, every cluster reported against
`catlib/anchors.py`; see `notes/linting.md`). What deliberately stays outside the package is a **read
shape**, not a parse: `verify_upstream_history.py` reads `lean/formalization.yaml` and
`notes/catalog.tsv` from a **revision** through `git show <rev>:`, so the package gained
`parse_yaml_text` / `parse_overview_text` / `read_rows_from_text` — text-level cores its disk-level
`parse_yaml` / `parse_overview` / `read_rows` delegate to — rather than a git reader;
`verify_summaries.py` keeps its lenient `errors="replace"` read of a declared source, which may be a
compiled PDF; and `build_index.py` keeps its own `TRIPLE` regex.

The package is not in the census below: the script population is `notes/scripts/*.py`, and
`catlib/` is 11 modules under that directory, counted as **57** source files by the lint gate in
`notes/linting.md`.

## The file census

| Population | Files | Owner |
|---|---|---|
| `notes/index/` | **1,049** | generated — `build_index.py` |
| `notes/summaries/` | **21** | hand-written — the reading record |
| `notes/templates/` | **19** | **5** hand-written index skeletons + **14** report templates built by `build_report_templates.py` |
| `notes/*.tsv` | **8** | **6** generated, **2** hand-authored |
| `notes/*.md` | **27** | hand-written — **15** with a checker, **12** without |
| `notes/` total, scripts excluded | **1,124** | — |

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

`notes/README.md`'s command block named **34** of the 45 scripts before this pass. Eleven are named
nowhere in the repo at the pinned baseline: `build_report_templates.py`, `check_summary_manuscripts.py`,
`extract_citations.py`, `locate_summary_quotes.py`, `read_manuscript.py`,
`refresh_summary_line_counts.py`, `render_reports.py`, `verify_citations.py`, `verify_findings.py`,
`verify_named_conjectures.py` and `verify_upstream_history.py`. The first four are the report-template
builder this pass promoted plus the `notes/summaries/` reading tooling and the citation extractor, so
the summaries tree and `notes/citations.md` carried measurements whose generating command no document
named; `read_manuscript.py` and `refresh_summary_line_counts.py` are the rest of that reading tooling;
`verify_citations.py`, `verify_findings.py` and `verify_named_conjectures.py` are the checkers for
`notes/citations.md`, `notes/findings.md` and `notes/named-conjectures.md`, so three pages carried
measurements whose checker no document named; `verify_upstream_history.py` is the tooling behind
`upstream_history/`, the pages that record each upstream merge, which sit outside `notes/` and so
outside this page's census; and `render_reports.py` is the renderer for the fourteen report-fed pages.
All 45 are named here and in the command
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

One script stays in the scratch tree: `scratch_census.py`, the enumerator that produced the
classification above. It is a census of the scratch tree, not a measurement of the corpus, so it has
no row in the tables above and no gate command; the next cleanup re-runs it.

The scratch tree is not a record. `.qwen/tmp/n5d3-draft.md` is a working draft whose tail is the
state a compacted session resumes from, and `.qwen/tmp/canonical_counts.md` is the count sheet the
gate reports are checked against; both are untracked, and the findings they carry are moved into
tracked files under `notes/` before the bead that produced them closes.

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
  it resolves each page path through `verify_summaries.Page` and rewrites the `Lines` column of every
  page under `notes/summaries/`, so the rule files it under report-only and the census row calls that
  tree hand-written. The tree is hand-written in what it says and script-touched in that one column.
- The report-only table records which page a report feeds as stated in that page and in `AGENTS.md`.
  It is not derived from the report text, so a page that stops quoting a report keeps its row here.
- **A needle can match nothing and the run stays green.** `verify_upstream_history.py`'s `SLUG`
  pattern required a trailing `/` inside the backticks **and** a 3-letter month, while the corpus
  writes full month names only (`September` 576, `October` 172 over the **749** `preprints/` dirs), so
  it matched **0** tokens on the three pages it checks — `upstream_history/2026-10-07_3014888.md`
  carries **14** backticked manuscript-slug tokens of that shape, written without the slash. The run
  exited 0 because nothing was asserted, and a slug renamed to one the release does not name was not
  caught. `math-lon.2.5` ported the file and left the pattern as it is, because its acceptance is
  byte-identical gate reports. `math-cg1` fixed both halves (slash optional, full month names: the
  needle now matches the **14** tokens and **0** on the other two pages), added the `slug rename`
  mutant (**13** → **14**, needle `": slug '"` — the table pass reports the same fact as
  `table: '…' is not a preprints/ directory`, so a shared needle cannot tell the two passes apart),
  and made the report print the slug count: a run that matches **0** is a problem, not a green result.
- Nothing in `lean/` is built, so no generated artifact here is a verification of a formalization.
