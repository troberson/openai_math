# The script fleet as a DAG over content digests

Draft for `notes/fleet-design.md`. Every number is from a named command, measured 2026-10-10.

## The four layers

| layer | what it is | who writes it | keyed by |
|---|---|---|---|
| **L0** | the release tree: `preprints/**`, `lean/**`, `overview.tex`, `CONTENTS.md`, `reasoning_traces/**` | upstream, via the merge commits | the git **tree digest** of each path |
| **L1** | the hand-authored inputs: `notes/topics.tsv`, `notes/conjecture-standing.tsv`, the **11** hand-written `notes/*.md` pages (of the **28** top-level pages — the other **17** are report-fed, so they are L3) | a human, in a commit | the file's content hash |
| **L2** | the derived records: the **8** `notes/*.tsv` present on disk, `notes/index/**` (1,049 files), `notes/summaries/**` | the 9 writers | (L0 digests, script-source hash, L1 hashes, args) |
| **L3** | the tracked output pages: the 17 report-fed `notes/*.md` | `render_reports.py`, plus the **2** checkers that also write a page (`check_index_links.py`, `measure_proof_density.py` — mutant branch only) | the same key |

## The purity rule, stated precisely

A script may read a derived record **iff** that record is a pure function of L0 ∪ L1 keyed by its
digest, and the graph over digests is a **DAG**. A read of a record that the same pass writes is not
pure: the record's bytes depend on a script that has not run yet, so the key cannot name them.

The rule is not "never read the output dir". `render_reports.py` reads `notes/sources.tsv` and
`notes/links.tsv` and is legal, because those records are pure functions of L0 ∪ L1 — the renderer
does not write them. `extract_links.py` reading `notes/links.md` is not legal: that page is written by
the renderer, in the same pass, from a key that includes `notes/links.tsv`, which `extract_links.py`
writes.

## The cache key

key = (the five L0 tree digests, hash of the script's own source, hash of each L1 file it reads, its
argv). The script-source hash is what "we have not changed the definition of what we are searching
for" means: a regex edit invalidates exactly that script's cache entries, not the fleet's.

The digests are free and exact. `git rev-parse HEAD:preprints HEAD:lean HEAD:overview.tex
HEAD:CONTENTS.md HEAD:reasoning_traces` prints **5** digests in **0.001 s** (measured 2026-10-10;
`real 0m0.001s`), and the key is exact because
`git status --porcelain --ignored=matching -- preprints lean overview.tex CONTENTS.md reasoning_traces`
returns **1 line** — `!! lean/.lake/`, the lake cache downloaded on 2026-10-10 into the path the
release's own `lean/.gitignore` ignores. Nothing else under those five paths is untracked or ignored.
**Run that check before trusting a tree digest as a key**: this is the case the warning describes, an
ignored generated directory inside a hashed path. `HEAD:lean` is a **commit** digest, so the cache does
not change it, and a cache read under `lean/` is not a tree read the digest covers — which is why the
key stays exact here and would not if a generated file landed inside `preprints/`.

Two scripts are not keyed by a tree digest, because they read git **history**, not the tree:
`verify_upstream_history.py` (`git show <rev>:` of `lean/formalization.yaml` and `notes/catalog.tsv`)
and `verify_script_ownership.py` (the four-scripts-named-nowhere gap from
`git show <manifest-commit>^:`). Their key needs the commit graph. Enumerate them; do not cache them
blind.

## The size argument

Rule: `du -sk` per surface, divided by 1024. `preprints/` is **631M**, `lean/OAI/` is **1740M**
(122,458 files), `notes/index/` is **14M**. `cat notes/*.tsv | wc -c` = **630,606** bytes over the
**8** `notes/*.tsv` present on disk (`named-results.tsv` is absent — the named-result page is
report-fed, not table-fed). `free -h` reported **7.2 GiB available of 60 GiB** on 2026-10-10, with the
model server resident — a dated observation, not a re-derivable count.

A full-corpus `.tex` scan is 128.8 MB over 8,007 files; a `lean/OAI` scan is 1.7 GB. With that little
page cache, a 1.7 GB scan evicts everything the next gate row wants — which is why the same 16
generator rows cost 450 s cold and 161 s warm.

So the cache that matters is the **L0 read surface**, not the 630 KB of L2: the generated layer is
cheap to re-read and must not be cached (it is what the twice-run proof compares), and the release
inputs are the expensive, immutable, cacheable part.

## The atomicity finding

Rule: `grep -cE 'os\.replace|os\.rename|shutil\.move|NamedTemporaryFile'` over `notes/scripts/*.py`
and `notes/scripts/catlib/*.py`, **excluding `verify_fleet_design.py`** — that checker carries the
pattern as a needle, so counting it would read 1 and the rule would be about the checker, not the
fleet. Over **50** scripts and **15** catlib modules the count is **2 matches**, both in
`catlib/atomic.py`: the `os.replace` at `catlib/atomic.py:41`, which promotes the sibling temp onto
the target, and the one at `catlib/atomic.py:67`, which promotes a staged slot onto its tracked path.
Before `math-o3a.2.1` the count was **0 matches** over **49** scripts and **14** modules: every writer
opened its tracked target directly, so a crash mid-write left a half-written tracked file. Atomic
promotion is now **2** sites, both in the package, and every writer's write goes through them —
`catlib/tsv.py`'s four TSV writers, `build_index.py`'s page writer, `render_reports.py`'s 17 page
writes, `build_report_templates.py`, `refresh_summary_line_counts.py` and `compare_abstracts.py --tsv`
— so the count stays small by construction: two primitives, and no writer carries its own move.

## The sync-pass census

`grep -lE 'sync problems' notes/scripts/*.py` returns **11** scripts. **11** are `verify_*` checkers —
reading the page they verify is their job, so the pass is legal: `verify_abstracts.py`,
`verify_counterexample_crosscheck.py`, `verify_dependency_drift.py`, `verify_index_design.py`,
`verify_named_results.py`, `verify_page_sync.py`, `verify_scope_exclusions.py`,
`verify_script_ownership.py`, `verify_sources.py`, `verify_subfinding_pairs.py`,
`verify_verification_dirs.py`. **0** are not. `verify_fleet_design.py` carries the string as a needle
and is excluded from the count, so the rule is 12 files found, 11 counted.

Before `math-o3a.3` the count was **15**, split **10** checkers and **5** non-checkers
(`check_index_links.py`, `extract_links.py`, `measure_names.py`, `measure_proof_density.py`,
`measure_topics.py`) — report-only scripts and writers reading a page they do not verify. Those five
passes now live in `verify_page_sync.py`, which owns the render diff for all five pages.

## The two-writer artifact

The 2026-10-10 probe recorded **two** pages with two writers: `notes/index-links.md`, written by
`render_reports.py` (mode-verified in its 17-page `r,w` list) and by `check_index_links.py` (mode
`r,w`); and `notes/proof-density.md`, written by `render_reports.py` and by
`measure_proof_density.py --mutant` (mutant branch only). Both second writers were the sync-pass
mutant, which wrote the mutated page to disk to test the render diff. `verify_page_sync.py` mutates
the page text in memory and compares it with the render, so neither checker writes a page and each
of those pages has one writer. A page with two writers is the reason `gate_driver.sh`'s `snap()`
cannot cover `notes/*.md`: the second writer runs after the first, so a run-1/run-2 md5 diff of the
pages is a real signal, not a formality — that stays true of the pages `render_reports.py` writes.

## The purity violations (7 scripts, mode-verified)

Rule: the audit-hook probe (`sys.addaudithook` on `open`, mode string recorded per path, parent process
only) lists every `notes/` path each script opens. A path is a write only if a mode string contains
`w`, `a` or `x`. The AST census maps a name to a call context and does **not** track branches, so a
`write_text` that lives only in a `--mutant` path is reported as a write in every mode — the probe's
mode strings are the authority.

| script | write modes | generated read that breaks purity |
|---|---|---|
| `build_sources.py` | `notes/sources.tsv` (w) | `notes/subfindings.tsv` (r) — written by `extract_subfindings.py` at gate row 5, **after** row 2 |
| `extract_links.py` | `notes/links.tsv` (r,w) | `notes/links.tsv` (r) — its own output, opened read-write; `notes/templates/report/links.md.j2` (r) |
| `render_reports.py` | 17 pages (w) | `notes/links.tsv`, `notes/sources.tsv`, `notes/subfindings.tsv`, `notes/abstracts.tsv`, `notes/formalization-deps.tsv` (r) — all written earlier in the same pass |
| `build_index.py` | `notes/index/**` (w, 1,049 files) | `notes/sources.tsv` (r) — written at row 2 |
| `check_index_links.py` | `notes/index-links.md` (r,w) | second writer of a page `render_reports.py` writes |
| `measure_proof_density.py` | `notes/proof-density.md` (r,w, mutant branch only) | second writer of a page `render_reports.py` writes |
| `verify_script_ownership.py` | 0 in a plain run (AST census says `RW` on `notes/README.md` and `notes/templates.md`; the probe records mode `r` only) | reads 22 `notes/templates/report/*.j2` — generated by `build_report_templates.py` |

The table is the 2026-10-10 probe, and the checker parses these records, so the rows are the state
the probe measured. `math-o3a.3` removes **three** of the seven violations: `build_sources.py` no
longer reads `notes/subfindings.tsv` (its manuscript list is parsed from `overview.tex`),
`extract_links.py` no longer reads `notes/links.tsv` or `notes/links.md` (its sync pass moved), and
`check_index_links.py` and `measure_proof_density.py` no longer write a page. The next probe run
measures the new set; until then the table is the dated record and the count stays **7**.

The two backwards edges are the ones the twice-run absorbs: `build_sources.py` consumes the
**previous pass's** `subfindings.tsv` as its manuscript list, and `extract_links.py` reads
`notes/links.md` that `render_reports.py` wrote in the previous pass. No single-pass order satisfies
both, so the row order in `gate.sh` is provably not topological. `math-o3a.3` removes both: the
manuscript list comes from `overview.tex`, and no writer reads a page. The remaining generated reads
are all forward — `render_reports.py` and `build_index.py` read TSVs written earlier in the same
pass — so a single pass satisfies them.

## The read amplification (why the gate costs an hour)

Rule: `sys.addaudithook` on `open` counts events, distinct paths, repeats, `rchar` (bytes through
`read()`) and `read_bytes` (bytes from storage), parent process only. The records are
`notes/probe/2026-10-10_writers.txt` and `notes/probe/2026-10-10_checkers.txt`; the checker parses them.

| gate row | wall s | opens | distinct | repeats | rchar MB | disk MB |
|---|---|---|---|---|---|---|
| `build_sources.py` | 2.51 | 39,080 | 7,752 | 31,328 (80 %) | 641.1 | 0.3 |
| `extract_links.py` | 56.60 | 157,599 | 131,062 | 26,537 | 4,249.2 | **3,601.4** |
| `build_index.py` | 51.94 | 17,809 | 9,554 | 8,255 | 261.2 | 3.5 |
| `dump_template_slots.py` | 76.92 | 59,681 | 10,459 | 49,222 | 967.8 | 44.7 |
| `render_reports.py` | 332.23 | 154,399 | 12,301 | **142,098 (92 %)** | 5,113.5 | 1,854.8 |

`render_reports.py` opens **154,399** times over **12,301** distinct paths — **142,098 repeats
(92 %)** — and pulls 1.9 GB from storage. The bucket split says where: `preprints/` **142,403** opens,
`notes/index/` 5,213, `lean/ComparatorChallenges/` 2,239, `lean/docs/` 2,234, `lean/OAI/` 1,870,
`notes/` 140, `notes/templates/` 63 — the buckets sum to the row's 154,399, and **95 %** of the opens
are release inputs. The mechanism is stacked full-corpus walks, not one loop: `render_reports.py:119
def measure()` is called twice per process, and each call walks all 719 listed dirs reading their `.tex`
four times (`roots_of`, `main_no_dc`, `substring_multi`, `build_sources.env_variants`). The probe
records buckets, not per-path counts under `preprints/`, so the **198** opens per listed dir the bucket
implies are not attributed to a call site: the split is measured, the per-call attribution is not.
`catlib/paths.read_text` is the uncached reader behind these opens
(**220** `read_text(` call sites over the **43** scripts the gate runs — 26 named explicitly, 17 in the
checker loop); the only cache in catlib is `render.rendered`, keyed by page name.

The same probe puts `check_index_links.py` at **57.91** s in its own row, and the timed import run
measured its subprocess cost inside `verify_findings.py` at **51.49** s per call — 7 calls in the
mutant loop. Two measurement sources, quoted separately: the row time from the probe, the per-call
cost from the in-process timing.

Decisive: `check("notes/findings.md")` timed three times in one process — **104.50 s → 67.24 s →
0.13 s** on identical code, identical page, identical output. Memoising the 5 report subprocesses
removes 37.26 s per call; the page-check work is 0.9 s. The gate's cost is re-collection, not
computation.

## The cache-safety rule (the load-bearing constraint)

A process-wide memoised read is safe only for files **no writer in the same process writes**.
`render_reports.py` is the case that decides the scope: it runs `extract_links.py` as a subprocess at
`:1365` (comment at `:1362`: "extract_links.py writes `notes/links.tsv`, and the renderer must" see
fresh bytes) and reads `LINKS_TSV` at `:1378` — **after** the child; it runs `build_index.py` at
`:1133` and reads its report stdout. So the safe scope is the **immutable release inputs**
(`preprints/**`, `lean/**`, `overview.tex`, `CONTENTS.md`, `reasoning_traces/**`, `lean/docs/**`) and
**not** the generated layer (`notes/*.tsv`, `notes/index/**`, `notes/summaries/**`).

The probe prints per-path counts only for `notes/`, and those counts are exactly the generated side of
the split: `notes/catalog.tsv` **36** opens, `notes/index-links.md` **8**, every `notes/index/` page
**5**. All three are generated, so none is cacheable under this rule. The release-input side has no
per-path count in the record — `overview.tex` and the manuscript main files sit in the bucket totals —
so the bucket split is the evidence for that half, not a reopen count.

## Why the second run earns its 33.4 minutes

The gate's proof is **twice-run byte-identity** of the **9** TSV names `gate_driver.sh` snapshots
(**8** present on disk — `notes/named-results.tsv` is absent, so `md5sum` skips it under `2>/dev/null`)
plus every file under `notes/index/` (md5 snapshots), plus identical `git status` snapshots. `notes/scripts/gate.sh` carries
**71** invocations: **33** `run` statements, of which **2** are the checker-loop body, so
**31** fixed rows + **20** checkers × 2 (plain and `--mutant`) = 71. Counting lines that start with
`run` at column 0 reads 31, because the loop body is indented. Non-determinism sources in the 9 writers,
by class:

- **Time / random / env:** **2 hits** — `render_reports.py:1132` and `:1357` set
  `env={**os.environ, "RENDER_REPORTS_CHILD": "1"}` for the two children. Zero `datetime`,
  `time.time`, `uuid`, `getpid`, `platform` in any writer, so no timestamp reaches a generated byte.
- **Set iteration order:** **2 sites** — `build_catalog.py:121`, `build_index.py:565`, both
  `paps_all = [p for fam in fams for p in set(...) | set(...)]`, both consumed only as
  `len(set(paps_all))`: order-independent **by consumption**, not by construction.
- **Unsorted filesystem walks: 9 sites in the writers + 3 in catlib** not wrapped in `sorted(`
  (`build_sources.py:63,142,144`, `build_index.py:325,326,712,772`, `render_reports.py:147,152`,
  `catlib/preprints.py:66` — the `d.rglob("*.tex")` inside `roots_of`, which sorts before returning —
  `catlib/yaml.py:126,171`). All consumed as `len(...)` or as dict keys by name. Two lines the earlier
  list carried, `render_reports.py:2033` and `:2034`, are **not** unsorted: they call
  `preprints.bundle_files`, which is `sorted(bundle.iterdir())` (`catlib/preprints.py:164`).
- `PYTHONHASHSEED` is set **nowhere**, so every process gets a random string-hash seed. Verified: three
  launches of the same one-liner over a 5-element string set gave three different orders. The twice-run
  therefore genuinely re-randomises set iteration order — it is a live probe for order dependence, and
  pinning `PYTHONHASHSEED=0` in `gate.sh` would **hide** the bug class rather than fix it.

Recorded catch: `.qwen/tmp/reports/a61_*` (2026-10-09 23:21→23:25) — `a61_run_diff.txt` **0 bytes**
(all 67 reports identical), the 9 TSV snapshots identical, and `a61_md5_diff.txt` **116 bytes**:
`notes/linting.md` md5 differed between the run-1 and run-2 snapshots. `notes/linting.md` is
hand-written (no `linting` slot in `render_reports.py`), so a page moved while the gate was running. A
single run cannot see that at all.

## Options, priced by measured cost removed

| # | change | measured cost removed | byte-identity risk |
|---|---|---|---|
| A | Compute `outs`/`ledger()`/`tsv()` **once** in `verify_findings.py` and pass them into `check()`, so the 7-pass mutant loop re-runs only page work | 6 × 37.26 s = **223.6 s/pass** (447.2 s/pair); row 832.7 s → ~609 s | none — no cache, same subprocesses, same bytes |
| B | Run the 50-row measurement/checker block in a bounded pool (32 CPUs; the gate is serial) | block 1,555 s → max row (832.7 s now, ~114 s after A) | none for checkers (they write nothing); writers stay in the dependency chain |
| C | Memoise reads of the **immutable release inputs** in `catlib/paths.read_text` (scope rule above) | 49,222 of 59,681 repeat opens (`dump_template_slots`); 31,328 of 39,080 (`build_sources`); rchar 967.8 MB → ~200 MB on the probed row | low, and only if the scope excludes generated files |
| D | Collapse `extract_links.py`'s six `preprints/**` walks into one | 5 of 6 walks over 8,007 `.tex` + 521 `.bib`; rchar 4,249.2 MB → ~700 MB, disk 3,601.4 MB → ~630 MB (row 56.60 s) | none — same file set, one enumeration |

Recommended order **A → D → C → B**: A and D are local with zero cache semantics; C is the real fix for
the re-collection hypothesis and belongs in `catlib/paths`; B is the structural win. Composition: pass
2,006 s → ~970 s after A+B → ~680 s with C warm, so the pair ≈ 23 min.

Intended, not to be "fixed": a checker importing its own extractor, and `render_reports.py` running
writers in-process/subprocess (`:1133` build_index, `:1365` extract_links). A checker that re-derives
through the writer's code proves nothing (`catlib/measure.py` docstring).

## The checker

`notes/scripts/verify_fleet_design.py` (report-only, writes nothing) with five passes:

1. **Anchors** — every backticked `path:line` anchor resolves, **prefixed** (a `notes/scripts/…` or
   `catlib/…` path) **or bare** (`render_reports.py:1132`, `build_catalog.py:121`); a bare name resolves
   under `notes/scripts/`. The line exists in the named file and a `path:a-b` span fits inside it. The
   page carries **4** anchors of the recognized form (`build_catalog.py:121`, `build_index.py:565`,
   `render_reports.py:1132`, `render_reports.py:2033`); an anchor written with trailing text
   (`` `render_reports.py:119 def measure()` ``) is not a form the checker parses, which is why the
   anchor mutant targets one of the four.
2. **Fenced blocks** — each block is attributed to the **nearest preceding** anchor and matched against
   the source lines it cites. The page ships **no** fenced block today, so this pass is vacuous on it
   and exists for the blocks the page will carry.
3. **Counts** — every count phrase is re-derived: the atomicity grep, the sync-pass grep, the
   tree-digest `git rev-parse`, the `--ignored=matching` check, the byte sum over the present
   `notes/*.tsv`, the three `du -sk` sizes, the gate row count from `gate.sh`, the two set-site lines,
   the env-hit count, and the probe table's figures (parsed from
   `notes/probe/2026-10-10_writers.txt` and `notes/probe/2026-10-10_checkers.txt`, the measurement's
   own records, tracked in git). The `free -h` available line, the
   wall times, and the cold/warm swing are **not** re-derived: they are dated observations in the page,
   and a checker that re-measures them fails the day the machine changes.
4. **Tables** — the 7-row purity table equals the probe parse, scanned **inside the purity section**
   (the amplification table names four of the same scripts, so a page-wide row scan lets a deleted
   purity row pass), and each of the 5 amplification rows is present. The options table is prose the
   checker does not re-derive.
5. **Mutants** — 7 injected corruptions, each asserted against the pass it targets: the atomicity
   count shifted, the sync split altered, a purity row deleted, the digest count widened, a probe
   figure altered, an anchor shifted outside its file, and a prose count in the size argument. Measured
   2026-10-11 at 05:35 UTC: plain **0 problems**, `--mutant` **7 of 7** flagged, and both reports
   byte-identical across two runs. The row pair is in `gate.sh` (the checker loop runs 19 → **20**
   checkers, so the list is 69 → **71** invocations) and the page + checker are rows in
   `notes/scripts/README.md`.
