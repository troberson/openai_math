# The script fleet as a DAG over content digests

Draft for `notes/fleet-design.md`. Every number is from a named command. The probe figures are the
2026-10-11 run of `notes/scripts/measure_open_probe.py` over the nine targets the two tables need;
the rest is measured 2026-10-10 and re-checked by `verify_fleet_design.py`.

## The four layers

| layer | what it is | who writes it | keyed by |
|---|---|---|---|
| **L0** | the release tree: `preprints/**`, `lean/**`, `overview.tex`, `CONTENTS.md`, `reasoning_traces/**` | upstream, via the merge commits | the git **tree digest** of each path |
| **L1** | the hand-authored inputs: `notes/tables/topics.tsv`, `notes/tables/conjecture-standing.tsv`, the **10** hand-written `notes/*.md` pages (of the **29** top-level pages — the other **19** are report-fed, so they are L3) | a human, in a commit | the file's content hash |
| **L2** | the derived records: the **8** `notes/tables/*.tsv` present on disk, `notes/index/**` (1,049 files), `notes/summaries/**`, `notes/probe/**`, and the untracked keyed store `.qwen/cache/records/**` | the 11 writers | (L0 digests, script-source hash, L1 hashes, args) |
| **L3** | the tracked output pages: the 19 report-fed `notes/*.md` | `render_reports.py` alone — `math-o3a.3` moved the two checkers' page writes into `verify_page_sync.py`, which mutates page text in memory | the same key |

## The purity rule, stated precisely

A script may read a derived record **iff** that record is a pure function of L0 ∪ L1 keyed by its
digest, and the graph over digests is a **DAG**. A read of a record that the same pass writes is not
pure: the record's bytes depend on a script that has not run yet, so the key cannot name them.

The rule is not "never read the output dir". `render_reports.py` reads `notes/tables/sources.tsv` and
`notes/tables/links.tsv` and is legal, because those records are pure functions of L0 ∪ L1 — the renderer
does not write them. `extract_links.py` reading `notes/links.md` is not legal: that page is written by
the renderer, in the same pass, from a key that includes `notes/tables/links.tsv`, which `extract_links.py`
writes.

## The cache key

key = (the five L0 tree digests, hash of the script's own source, hash of each L1 file it reads, its
argv). The script-source hash is what "we have not changed the definition of what we are searching
for" means: a regex edit invalidates exactly that script's cache entries, not the fleet's.

The key hashes the read surface the writer **reads**, and for one writer that is not the working tree.
`build_report_templates.py` rebuilds each template from `git show HEAD:<page>`, so `key_for()` hashes
its 18-page L1 from HEAD. Its own output feeds one of those entries — `notes/templates.md` tabulates
the template bytes — so a render after the builder moves that page, and a key computed from the
working tree stops matching the key the builder used. Measured 2026-10-12 at 00:48 UTC: with the
working-tree read, `verify_cache_promotion.py` reported **18** problems, every template's cache entry
missing under the recomputed key; with the HEAD read, the same run prints **0**.

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

**The store is built.** `math-o3a.4` put the key into `notes/scripts/catlib/records.py`, which writes
`.qwen/cache/records/<key>/manuscripts.jsonl` — one row per directory under `preprints/`, **749**
rows, not the **719** listed manuscripts: `measure_names.py` scans the whole tree, so a store scoped
to the listed set cannot reproduce its counts. The key is the **builder's**, not the consumer's:
`store_key()` hashes the five tree digests, `records.py`'s own source, each L1 file, and the args,
truncated to 32 hex, so a consumer that changes how it reads records does not invalidate records it
reads unchanged. Records are megabytes, text is not: a row carries derived counts (the `.tex` list, the
byte sum, the `\documentclass` roots, the resolved main file, the declared-environment counts, the
statement titles, the abstract bodies) — **4,992,197** bytes over **749** rows, built in **1.93 s**,
cache hit **0.012 s** — and no row carries raw `.tex` text, which is why `measure_names.py`'s prose
scan still reads files. The store lives under `.qwen/`, untracked by the repo's `.qwen/*` rule, so a
cache write never touches the tracked tree: `git status` is identical before and after a build.

Two scripts are not keyed by a tree digest, because they read git **history**, not the tree:
`verify_upstream_history.py` (`git show <rev>:` of `lean/formalization.yaml` and `notes/tables/catalog.tsv`)
and `verify_script_ownership.py` (the four-scripts-named-nowhere gap from
`git show <manifest-commit>^:`). Their key needs the commit graph. Enumerate them; do not cache them
blind.

## The size argument

Rule: `du -sk` per surface, divided by 1024. `preprints/` is **631M**, `lean/OAI/` is **1740M**
(122,458 files), `notes/index/` is **14M**. `cat notes/tables/*.tsv | wc -c` = **907,744** bytes over the
**9** `notes/tables/*.tsv` present on disk. `free -h` reported **7.2 GiB available of 60 GiB** on 2026-10-10, with the
model server resident — a dated observation, not a re-derivable count.

A full-corpus `.tex` scan is 128.8 MB over 8,007 files; a `lean/OAI` scan is 1.7 GB. With that little
page cache, a 1.7 GB scan evicts everything the next gate row wants — which is why the same 16
generator rows cost 450 s cold and 161 s warm.

So the cache that matters is the **L0 read surface**, not the 630 KB of L2: the generated layer is
cheap to re-read and must not be cached (it is what the md5 snapshot and the promote-and-verify
assertion compare), and the release
inputs are the expensive, immutable, cacheable part.

## The atomicity finding

Rule: `grep -cE 'os\.replace|os\.rename|shutil\.move|NamedTemporaryFile'` over `notes/scripts/*.py`
and `notes/scripts/catlib/*.py`, **excluding `verify_fleet_design.py` and `render_reports.py`** — the
checker carries the pattern in its count pass and the writer carries it as its `FLEET_ATOMIC` constant,
so counting either would read a needle as a site and the rule would be about the censuses, not the
fleet. Over **59** scripts and **18** catlib modules the count is **2 matches**, both in
`catlib/atomic.py`: the `os.replace` at `catlib/atomic.py:42`, which promotes the sibling temp onto
the target, and the one at `catlib/atomic.py:84`, which promotes a staged slot onto its tracked path.
Before `math-o3a.2.1` the count was **0 matches** over **49** scripts and **14** modules: every writer
opened its tracked target directly, so a crash mid-write left a half-written tracked file. Atomic
promotion is now **2** sites, both in the package, and every writer's write goes through them —
`catlib/tsv.py`'s four TSV writers, `catlib/promote.py`'s `promote()`, `build_index.py`'s page writer,
`render_reports.py`'s 19 page writes, `build_report_templates.py`, `refresh_summary_line_counts.py` and
`compare_abstracts.py --tsv` — so the count stays small by construction: two primitives, and no writer
carries its own move.

## The sync-pass census

`grep -lE 'sync problems' notes/scripts/*.py` returns **12** scripts. **12** are `verify_*` checkers —
reading the page they verify is their job, so the pass is legal: `verify_abstracts.py`,
`verify_counterexample_crosscheck.py`, `verify_dependency_drift.py`, `verify_faithfulness.py`,
`verify_index_design.py`,
`verify_named_results.py`, `verify_page_sync.py`, `verify_scope_exclusions.py`,
`verify_script_ownership.py`, `verify_sources.py`, `verify_subfinding_pairs.py`,
`verify_verification_dirs.py`. **0** are not. `verify_fleet_design.py` and `render_reports.py` carry the
string as a needle — the checker's sync pass prints `sync problems`, the writer's census line tests for
it — and both are excluded from the count, so the rule is 14 files found, 12 counted.

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

## The purity population (8 scripts, mode-verified)

Rule: the audit-hook probe (`sys.addaudithook` on `open`, mode string recorded per path, parent process
only) lists every `notes/` path each script opens. A path is a write only if a mode string contains
`w`, `a` or `x`. The AST census maps a name to a call context and does **not** track branches, so a
`write_text` that lives only in a `--mutant` path is reported as a write in every mode — the probe's
mode strings are the authority. The probe is `notes/scripts/measure_open_probe.py`, promoted from
`.qwen/tmp/a11_open_probe2.py` by `math-o3a.3.4`. The tracked records are **8**:
`notes/probe/2026-10-10_writers.txt`, `notes/probe/2026-10-10_checkers.txt`,
`notes/probe/2026-10-11_writers.txt`, `notes/probe/2026-10-11_checkers.txt`,
`notes/probe/2026-10-11_rr_after.txt` (the single-target `render_reports.py` record taken mid-pass,
after the store conversion), `notes/probe/2026-10-12_seed_quotes.txt` (the `seed_quotes.py` run, which
reads `notes/subfinding-pairs.md` and writes the TSV through the atomic sibling temp),
`notes/probe/2026-10-12_seed_quotes_summaries.txt` (the widened `seed_quotes.py` run, which reads the
21 summaries pages, the notes pages their Sources cells cite, and the manuscript files those cells
resolve to), and `notes/probe/2026-10-12_rr_fleet.txt` (the `render_reports.py` record
taken after the fleet census moved into the writer, which names the script tree the census scans).
`verify_fleet_design.py` parses the two 2026-10-11 records; `verify_cache_promotion.py` reads all
five of the 2026-10-10, 2026-10-11 and 2026-10-12 records for its L1 exactness pass; the
2026-10-10 pair is the **before** state the amplification table's deltas are measured against.

| script | write modes | generated reads, and whether any points backwards |
|---|---|---|
| `build_sources.py` | `notes/tables/.sources.tsv.tmp` (w) — the atomic sibling temp, not the tracked target | `notes/tables/catalog.tsv` (r), written at row 1 — forward |
| `extract_links.py` | `notes/tables/.links.tsv.tmp` (w) — the atomic sibling temp | `notes/tables/catalog.tsv` (r), written at row 1 — forward |
| `render_reports.py` | 0 under `notes/`: 18 staged slots under `.qwen/cache/staging/render_reports/` (w), moved onto the pages by `os.replace`, which is not an `open` event | 1,078 generated reads (6 `notes/tables/*.tsv`, 18 `notes/templates/report/*.j2`, 5 `notes/templates/*.j2`, 1,049 `notes/index/**`) — all written earlier in the same pass |
| `build_index.py` | 0 under `notes/`: 1,049 staged slots (w), promoted by `os.replace` | 7 generated reads (2 `notes/tables/*.tsv`, 5 `notes/templates/*.j2`) — forward |
| `check_index_links.py` | 0 — `math-o3a.3` removed its page write | 1,033 `notes/index/**` pages and `notes/tables/catalog.tsv` (r), written at row 3 — forward |
| `measure_proof_density.py` | 0 — `math-o3a.3` removed its page write | `notes/tables/catalog.tsv`, `notes/tables/sources.tsv` (r) — forward |
| `measure_names.py` | 0 under `notes/`: its write is the record's atomic sibling temp `.qwen/cache/records/<key>/.names.json.tmp` (w), outside `notes/`, moved onto the record by `os.replace` | `notes/tables/catalog.tsv` (r), written at row 1 — forward |
| `verify_script_ownership.py` | 0 in a plain run (AST census says `RW` on `notes/README.md` and `notes/templates.md`; the probe records mode `r` only) | 25 generated reads (2 `notes/tables/*.tsv`, 23 `notes/templates/*.j2`) — forward |

**0** of the 8 scripts reads a generated file that a later gate row writes. The two backwards edges
the 2026-10-10 probe recorded are gone: `build_sources.py` consumed the **previous pass's**
`subfindings.tsv` as its manuscript list and `extract_links.py` read `notes/links.md` that
`render_reports.py` wrote in the previous pass, and no single-pass order satisfies both — which is
why the row order in the shell list was provably not topological. `math-o3a.3` removed both: the
manuscript list comes from `overview.tex`, and no writer reads a page. The remaining generated reads
are all forward, so a single pass satisfies them.

Two shapes the probe records that the AST census cannot see. A staging writer writes nothing under
`notes/` during its run — its bytes land untracked and `promote()` moves them with `os.replace`, which
is not an `open` event — so the probe's write column for `render_reports.py` and `build_index.py` is
0, and the two `os.replace` sites in `catlib/atomic.py` are what accounts for those moves. And the
single-file
writers write the dotted sibling temp, so the write column names `notes/.sources.tsv.tmp` and
`notes/.links.tsv.tmp`, not the tracked targets. The third shape is the keyed store: `measure_names.py`
writes the dotted sibling temp inside `.qwen/cache/records/<key>/`, so its write is a mode-`w` path the
probe records **outside** `notes/` and its `notes/` write column is 0. The store is L2, so the purity
rule has nothing to check on that side — a record cannot point backwards, because its key names the
tree it was built from.

## The read amplification (why the gate cost an hour before the store and the pool)

Rule: `sys.addaudithook` on `open` counts events, distinct paths, repeats, `rchar` (bytes through
`read()`) and `read_bytes` (bytes from storage), parent process only. The records are
`notes/probe/2026-10-11_writers.txt` and `notes/probe/2026-10-11_checkers.txt`; the checker parses them.

| gate row | wall s | opens | distinct | repeats | rchar MB | disk MB |
|---|---|---|---|---|---|---|
| `build_sources.py` | 0.15 | 71 | 64 | 7 (10 %) | 6.5 | 0.0 |
| `extract_links.py` | 24.24 | 157,539 | 130,998 | 26,541 | 2,123.5 | 0.0 |
| `measure_names.py` | 46.17 | 15,050 | 7,801 | 7,249 (48 %) | 251.6 | 0.0 |
| `build_index.py` | 60.02 | 18,875 | 10,607 | 8,268 | 261.7 | 0.0 |
| `dump_template_slots.py` | 61.06 | 80,221 | 18,413 | 61,808 | 1,229.5 | 0.0 |
| `render_reports.py` | 151.32 | 117,360 | 18,935 | **98,425 (84 %)** | 4,103.9 | 0.1 |

`disk MB` is `read_bytes`, bytes taken from storage rather than from the page cache. Every row reads
0.0 except `render_reports.py` at **0.1**, because the cache was warm when this run started; the
2026-10-10 run, which started cold, recorded **3,601.4** for `extract_links.py` and **1,854.8** for
`render_reports.py`. The cold/warm swing is a
dated observation, not a re-derivable count, and the wall column moves with it.

`render_reports.py` opens **117,360** times over **18,935** distinct paths — **98,425 repeats
(84 %)** — and pulls 4.1 GB through `read()`. The bucket split says where: `preprints/` **84,089**
opens, `lean/OAI/` 23,275, `notes/index/` 5,229, `lean/docs/` 2,476, `lean/ComparatorChallenges/`
1,823, `notes/` 94, `notes/templates/` 87, `notes/scripts/` 59 — the buckets sum to the row's 117,360,
and **95 %** of the opens are release inputs. The record-store key changed when the 8 TSVs moved, so
this run rebuilt the store, and the rebuild walks every `preprints/` directory: the `preprints/` bucket
is 18,960 opens and `lean/OAI/` 21,405 opens above the run the call-site probe measured. The call-site
attribution below is that earlier run's measurement, and its 65,129 total is that run's `preprints/`
bucket, not this row's. The mechanism is now **attributed**, not inferred: a call-site probe (the same
audit hook, walking the caller stack up to the first frame under `notes/scripts/`; the scratch it was
run from is no longer on disk, so these figures cannot be re-measured) puts those opens at
`catlib/paths.py:77` **16,410**,
`extract_named_results.py:121` **15,358**, `catlib/templates.py:174` **8,991**,
`compare_abstracts.py:82` **7,705**, `measure_names.py:250` and `measure_names.py:376` **7,240** each,
`measure_index_sizes.py:93` **1,563**, `measure_names.py:291` **521**,
`extract_verification_dirs.py:43` **30**, `catlib/preprints.py:201` **7** — 65,129 in total. Every
anchor in that list is that run's line number; the store conversion and the 2026-10-12 autofix pass
moved those files, so they name lines in the current source that are not the call sites the probe saw,
and
`verify_fleet_design.py` checks only that an anchor's line falls inside the file. The stacked
walk `measure()` used to run is gone: it is `@cache`d and reads the record store, so its second call in
the process is a cache hit, and `build_sources.py`'s row fell from 39,083 opens to **71** for the same
reason. What remains is the extractors the renderer imports, each walking the corpus once per process.
`catlib/paths.read_text` is the uncached reader behind those opens (**230** `read_text(` call sites over
the **59** scripts and **18** catlib modules, counted as occurrences over both globs on 2026-10-11; the
page read **217** over **55** scripts before the two `math-faz` probes landed); the caches in catlib are `render.rendered`, keyed by page
name, `records.manuscript_store`, keyed by the store digest, and `promote.cached_text`, keyed by the
builder's key.

The same probe puts `check_index_links.py` at **1.23** s in its own row (plain run, 1,732 opens over
1,728 distinct paths), and the timed import run measured its subprocess cost inside
`verify_findings.py` at **51.49** s per call — 7 calls in the mutant loop. Two measurement sources,
quoted separately: the row time from the probe, the per-call cost from the in-process timing. The
2026-10-10 probe recorded the row at 57.91 s; that run started cold, and the row's opens are the
1,033 index pages plus the 416 comparator files and 242 scope notes, which is what a warm cache
makes cheap.

`extract_links.py`'s `rchar` fell from 4,249.2 MB to 2,123.5 MB and its wall from 56.60 s to 24.24 s
when `math-o3a.3` moved its sync pass into `verify_page_sync.py`. The pass called
`catlib.render.rendered()`, which runs the renderer's `measure()` — the full-corpus walk — inside
`extract_links.py`'s own process. The writer now walks the corpus once, and the render happens in the
checker that owns it. `extract_links.py` is the one writer `math-o3a.4` has **not** converted to the
record store: its six `preprints/**` walks are still its own.

Decisive: `check("notes/findings.md")` timed three times in one process — **104.50 s → 67.24 s →
0.13 s** on identical code, identical page, identical output. Memoising the 5 report subprocesses
removes 37.26 s per call; the page-check work is 0.9 s. The gate's cost is re-collection, not
computation. `math-o3a.4.3` realized that for the corpus measures: `@cache` on
`render_reports.measure()`, `compare_abstracts.measure()`, `measure_names.measure()` and
`check_index_links.measure()`, so the repeats inside a process are cache hits.

## The cache-safety rule (the load-bearing constraint)

A process-wide memoised read is safe only for files **no writer in the same process writes**.
`render_reports.py` is the case that decides the scope: it runs `extract_links.py` as a subprocess at
`:1358` (comment at `:1354`: "extract_links.py writes `notes/tables/links.tsv`, and the renderer must" see
fresh bytes) and reads `LINKS_TSV` at `:1372` — **after** the child; it runs `build_index.py` at
`:1131` and reads its report stdout. So the safe scope is the **immutable release inputs**
(`preprints/**`, `lean/**`, `overview.tex`, `CONTENTS.md`, `reasoning_traces/**`, `lean/docs/**`) and
**not** the generated layer (`notes/tables/*.tsv`, `notes/index/**`, `notes/summaries/**`).

The probe prints per-path counts only for `notes/`, and those counts are exactly the generated side of
the split: `notes/tables/catalog.tsv` **33** opens, every `notes/index/` page **4**, `notes/index-links.md`
**1**. All three are generated, so none is cacheable under this rule. The release-input side has no
per-path count in the record — `overview.tex` and the manuscript main files sit in the bucket totals —
so the bucket split is the evidence for that half, not a reopen count. The record store is safe under
this rule by construction, not by scope: it is keyed by the L0 tree digests, so a cache hit can only
name bytes read from a tree that is still the tree at `HEAD`, and it writes nothing under `notes/`.

## Why the assertion replaces the second run

The gate's proof was **twice-run byte-identity** of the **8** TSV names `gate_driver.sh` snapshots
(all **8** present on disk, all under `notes/tables/`; the snapshot used to name a ninth,
`notes/named-results.tsv`, which no writer produces, and the `2>/dev/null` that hid its absence is gone
with it) plus every file under `notes/index/` (md5 snapshots), plus identical `git status` snapshots. The proof
is now the promote-and-verify assertion the gate's own `verify_cache_promotion.py` row carries: for
every tracked artifact, the bytes the writer landed under its key equal the bytes on the tracked path,
and the key is computed from the current `git rev-parse HEAD:<path>` tree digests, so a key that no
longer matches HEAD makes its records missing and the row fails. The driver keeps the md5 and
`git status` snapshots raw and prints the assertion row. `notes/scripts/gate.py` carries
**78** invocations as `ROWS` entries, each a (spec, needs, writes) triple over the generated
artifacts: the **10** writers declare what they write, every checker needs `pages`,
`check_index_links.py` and `measure_index_sizes.py` need `index`, and the two summary readers need
`summaries`. A row starts as soon as every row that writes its `needs` has finished, so counting the
tuples in the `ROWS` block is the row count. Non-determinism sources in the **10** writers,
by class:

- **Time / random / env:** **2 hits** — `render_reports.py:1155` and `render_reports.py:1375` set
  `env={**os.environ, "RENDER_REPORTS_CHILD": "1"}` for the two children. Zero `datetime`,
  `time.time`, `uuid`, `getpid`, `platform` in any writer, so no timestamp reaches a generated byte.
- **Set iteration order:** **2 sites** — `build_catalog.py:128`, `build_index.py:583`, both
  `paps_all = [p for fam in fams for p in set(...) | set(...)]`, both consumed only as
  `len(set(paps_all))`: order-independent **by consumption**, not by construction.
- **Unsorted filesystem walks: 9 sites in the writers + 9 in catlib** not wrapped in `sorted(`
  (`build_catalog.py:68`, `build_index.py:304,305,306,338,339,730,796`, `extract_links.py:593`,
  `catlib/preprints.py:77`, `catlib/yaml.py:126,171`, `catlib/bib.py:56,148`,
  `catlib/records.py:110`, `catlib/measure.py:35,36,37`). All consumed as `len(...)` or as dict keys
  by name. The three `build_sources.py` walks the earlier list carried are gone: the corpus read moved
  into `catlib/records.py`, whose one unsorted walk is the `d.glob("*.pdf")` at `:110`, and
  `render_reports.py` has none. Two lines the earlier
  list carried, `render_reports.py:2043` and `:2044`, are **not** unsorted: they call
  `preprints.bundle_files`, which is `sorted(bundle.iterdir())` (`catlib/preprints.py:192`).
- `PYTHONHASHSEED` is set **nowhere**, so every process gets a random string-hash seed. Verified: three
  launches of the same one-liner over a 5-element string set gave three different orders. The twice-run
  therefore genuinely re-randomised set iteration order — it was a live probe for order dependence. The
  single run is not: a writer's bytes are written once, so cache == disk holds trivially over an order
  that changed them. The probe is gone with the second run; what covers the class is the two sites
  being order-independent **by consumption** and the nine walks consumed as `len(...)` or dict keys.
  Pinning `PYTHONHASHSEED=0` in `gate.py` would still **hide** the bug class rather than fix it.

Recorded catch: `.qwen/tmp/reports/a61_*` (2026-10-09 23:21→23:25) — `a61_run_diff.txt` **0 bytes**
(all 67 reports identical), the 9 TSV snapshots identical, and `a61_md5_diff.txt` **116 bytes**:
`notes/linting.md`'s md5 differed between the run-1 and run-2 snapshots. That page was hand-written
(no `linting` slot in `render_reports.py`), so it moved while the gate was running. A
single run cannot see that at all, and the assertion cannot: the page is not a writer output, so no
key names it. The catch is the honest cost of the single run. `notes/linting.md` is deleted
(2026-10-12), so the catch has no live target on this tree — the rule it recorded still applies to
every hand-written page.

## Options, priced by measured cost removed

| # | change | measured cost removed | byte-identity risk |
|---|---|---|---|
| A | Compute `outs`/`ledger()`/`tsv()` **once** in `verify_findings.py` and pass them into `check()`, so the 7-pass mutant loop re-runs only page work | 6 × 37.26 s = **223.6 s/pass** (447.2 s/pair); row 832.7 s → ~609 s | none — no cache, same subprocesses, same bytes |
| B | **Realized by `math-o3a.5.2`**: run the 56-row read-only block in a bounded pool (`xargs -P 8`), the writer block serial, printing in the canonical order of the list | pass 928 s → 431 s (497 s saved, 2.15x); the pooled report diffed against the serial report with wall-time tokens normalized is 0 bytes | none for checkers (they write nothing); writers stay in the dependency chain. The catch: the block is not read-only until the render children run with `--check-only` — two `build_index.py` children sharing the staging root collided in the first pooled run |
| C | **Realized by `math-o3a.4`**: memoise the corpus read as a digest-keyed record store (`catlib/records.py`) rather than as a memoised `read_text` | `build_sources.py` 39,083 → 65 opens, rchar 641.3 → 6.5 MB, wall 3.21 → 0.11 s; `render_reports.py` 152,680 → 75,394 opens, repeats 140,364 → 63,075, wall 231.58 → 138.99 s | none — the store writes nothing tracked and the generated layer is untouched |
| D | Collapse `extract_links.py`'s six `preprints/**` walks into one, or convert it to the store | 5 of 6 walks over 8,007 `.tex` + 521 `.bib`; rchar 4,249.2 MB → ~700 MB, disk 3,601.4 MB → ~630 MB (row 56.60 s) | none — same file set, one enumeration |
| E | **Realized by `math-unv`**: replace the shell list's two blocks with a dependency scheduler — `ROWS` carries (spec, needs, writes) over the generated artifacts and a row starts when every row that writes its needs has finished | pass 461.4 s → 351.1 s (110.3 s saved); the 8 report-only extractors and the corpus readers start at t=0 instead of after `render_reports.py` | none for checkers (they write nothing); the print order is the list order, so the report is the same bytes a serial run prints. The catch: row time is flat (921.8 → 919.4 s) — 12 rows share the machine, so each row runs slower than it does alone — and the cap must be sized by measured RSS, not core count |

Recommended order **A → D**: A and D are local with zero cache semantics; C is done, and the store is
the shape C took; B is done, and the measured pass was **431 s** — the pair the twice-run cost was
**862 s**, and the second run is gone, so the gate is one 431 s pass. The
composition the table predicted (2,006 s → ~970 s after A+B) landed at 431 s with B alone, because C
had already removed the re-collection B was priced to overlap. **E is done** and the pass is
**351.1 s**: E is what the serial block's read-only rows were waiting for, which is the one
re-collection the pool could not remove.

The pass re-measured 2026-10-11, after the scheduler replaced the two blocks, is **351.1** s of driver
wall, over **919.4** s of row time. The rule: the driver's own timestamps (first row's `.line` file at
19:32:08, driver output at 19:37:59) and the report's per-row `in X.Xs` tokens. The writer critical
path is `build_catalog.py` 0.1 → `extract_links.py` 21.5 → `build_index.py` 54.8 →
`render_reports.py` 147.1 = **223.5** s, and the longest row that needs the rendered pages
(`verify_page_sync.py --both`, 122.5 s) starts at 19:35:56 and finishes at 19:37:59, so the wall is
that path, plus that row, plus the 4 s it waited for a free slot in the 12-row pool. The 461.4 s pass
measured 23 minutes earlier over the same 75 rows ran the 8 report-only extractors inside the serial
chain, so nothing read-only could start until `render_reports.py` finished; the scheduler starts them
at 19:32:08 and the wall fell **110.3** s. Row time is flat — 921.8 s against **919.4** s: 12 rows
share the machine, so each row runs slower than it does alone, and the sum is the same. The serial
baseline (`GATE_POOL=1`) ran the same 75 rows at **876.0** s wall over **872.6** s row time — with
nothing overlapping the wall is the row sum, so the pooled pass is **2.49**× faster. The two reports
are identical in row order and row content once every wall-time token is normalized, including the
tokens a report carries inside its own first 200 bytes (`measure_checker_needles.py` prints a per-target
time), which is the honest form of the byte-identity the scheduler was asked to prove. The 431 s
figure is the same shape measured earlier on 2026-10-11 over 71 rows, and the 478.7 s
pass over 76 rows carried `verify_page_sync.py` as two rows (128.0 s plain, 124.8 s `--mutant`) with a
two-row tail; collapsing them into `--both` removed **130.9** s of row time and **17.3** s of wall.

Intended, not to be "fixed": a checker importing its own extractor, and `render_reports.py` running
writers in-process/subprocess (`:1131` build_index, `:1358` extract_links). A checker that re-derives
through the writer's code proves nothing (`catlib/measure.py` docstring).

## The checker

`notes/scripts/verify_fleet_design.py` (report-only, writes nothing) with seven passes:

1. **Anchors** — every backticked `path:line` anchor resolves, **prefixed** (a `notes/scripts/…` or
   `catlib/…` path) **or bare** (`measure_index_sizes.py:93`, `extract_links.py:593`); a bare name resolves
   under `notes/scripts/`. The line exists in the named file and a `path:a-b` span fits inside it. The
   page carries the anchors the checker counts, the four named here
   (`build_catalog.py:128`, `build_index.py:583`, `render_reports.py:1155`, `render_reports.py:2043`),
   the eight call-site anchors in the amplification section, the unsorted-walk list, the three measured
   site anchors the four do not carry (`catlib/atomic.py:42`, `catlib/atomic.py:84`,
   `render_reports.py:1375`), and
   `catlib/preprints.py:77`, `catlib/preprints.py:192`,
   `catlib/yaml.py:126`; an anchor written with trailing text
   (`` `render_reports.py:128 def measure()` ``) is not a form the checker parses, which is why the
   anchor mutant targets one of the four.
2. **Fenced blocks** — each block is attributed to the **nearest preceding** anchor and matched against
   the source lines it cites. The page ships **no** fenced block today, so this pass is vacuous on it
   and exists for the blocks the page will carry.
3. **Counts** — every count phrase is re-derived: the atomicity grep, the sync-pass grep, the
   tree-digest `git rev-parse`, the `--ignored=matching` check, the byte sum over the present
   `notes/tables/*.tsv`, the three `du -sk` sizes, the gate row count from `gate.py`'s `ROWS` block, the
   three site counts (atomicity, env, set iteration), and the probe table's figures (parsed from
   `notes/probe/2026-10-11_writers.txt` and `notes/probe/2026-10-11_checkers.txt`, the records
   `notes/scripts/measure_open_probe.py` writes, tracked in git). The `free -h` available line, the
   wall times, and the cold/warm swing are **not** re-derived: they are dated observations in the page,
   and a checker that re-measures them fails the day the machine changes.
4. **Site anchors** — the three paragraphs that state measured sites with line numbers (the atomicity
   paragraph, the env bullet, the set-iteration bullet) must each name **exactly** their measured
   `name:line` set, and the checker-section anchor list must carry every measured site. The count pass
   proves only the count and the anchor pass only that the line exists, so a site anchor shifted to a
   neighbouring line passes both: this pass is what makes the page's site anchors mean the measured
   lines. This is the fix for the count-only comparison the checker carried before 2026-10-12, which
   printed the measured sites with their line numbers and reported `problems 0` against a page that
   named a stale line. The comparison also requires each site to be **carried once** in the
   checker-section paragraph: a site enumerated twice there makes a shift of one copy invisible, which
   is why the bare example above names non-site anchors and the paragraph lists the six sites as four
   plus the three the four do not carry.
5. **Tables** — the 8-row purity table equals the probe parse, scanned **inside the purity section**
   (the amplification table names four of the same scripts, so a page-wide row scan lets a deleted
   purity row pass), and each of the 5 amplification rows is present. The options table is prose the
   checker does not re-derive.
6. **Sync** — the page's bytes on disk against the bytes `render_reports.py` renders for it. The page
   is report-fed: its measured phrases are slots the writer supplies from its own scan of the fleet's
   sources, so a hand edit to a slotted phrase, a stale render, or a template that no longer matches the
   page all show up here. The count pass proves the numbers are measured; this pass proves the page is
   the writer's text. The two measurements stay independent: the writer's scan is its own, not this
   checker's, so a checker that compared the page with the writer's numbers would prove nothing.
7. **Mutants** — 16 injected corruptions, each asserted against the pass it targets: the atomicity
   count shifted, the sync split altered, a purity row deleted, the purity population count in the
   section heading, the digest count widened, a probe figure altered, an anchor shifted outside its
   file, a notes-page anchor injected past its file's end, a prose count in the size argument,
   **six** site anchors shifted to a neighbouring line — one per list the site pass reads, the
   atomicity paragraph, the env bullet, the set-iteration bullet, and the checker-section anchor list
   for each of the three classes — and a dated observation in the page, which the writer deliberately
   leaves literal, so only the render diff can catch it.
   The purity heading count and the closing sentence of the purity section are both in the count
   phrase list, so the population is measured, not carried: adding a probe target moves the table,
   the heading and the sentence together. Measured
   2026-10-12 against the re-measured probe: plain **0 problems**, `--mutant` **16 of 16**
   flagged, and both reports byte-identical across two runs. The six site mutants were confirmed
   against the checker as it stood before this pass, which compared set sites only: run against
   `HEAD`'s version, they print **11 of 15** with the four atomicity and env mutants named
   `UNDETECTED`; run against the fixed checker, **16 of 16**. Two of them were first inert for the
   same reason the atomicity count mutant was inert twice earlier in this pass: a page that enumerates
   the six measured sites in the checker-section paragraph carries each site twice, so shifting one
   copy leaves the site present in the other and the presence check passes. The paragraph now lists the
   four plus the three the four do not carry, and the bare example in the anchor pass names
   non-site anchors. The probe-figure mutant targets the
   `render_reports.py` opens figure in the amplification table, so it re-targets whenever that row is
   re-measured. The atomicity mutant was inert twice
   during this pass, both times for the same reason: a paragraph that restates the atomicity count
   leaves the phrase a second time, so the single occurrence the mutant replaces is not the only one
   and the count check still finds it. Both restatements are now prose without the bold form, and the
   phrase occurs once. The sixteenth mutant alters a dated observation the writer does not slot, so the
   count pass cannot see it and the render diff is the only pass that can: it is the mutant that proves
   the sync pass is live on this page. The row pair is in `gate.py`'s `ROWS` list, where each checker is two explicit
   entries. The shell list ran each checker through a loop over 20 → **21** checkers (73 → **76**
   invocations) until `math-o3a.5.2`'s B pass collapsed `verify_page_sync.py` into a single `--both`
   row (75), and `math-unv` removed the loop when the list became a graph. The page + checker are rows in
   `notes/scripts/README.md`.
