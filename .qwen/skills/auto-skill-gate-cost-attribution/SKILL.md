---
name: gate-cost-attribution
description: "Find out why a long gate/test runner takes an hour — attribute wall time per row without instrumenting the runner, separate re-collection from computation, measure the fleet's read/write graph and the runner's row-order cycles, census idempotency risk, price each candidate fix by cost removed and byte-identity risk, and implement the dependency scheduler the options table prices: the pool cap sized by measured RSS, canonical printing, and the honest form of the byte-identity test. Use when a gate is \"too slow\", when a no-cache hypothesis is raised, before adding a cache to a verification tree, when asked whether a twice-run is really needed, when asked to parallelize a gate over the full machine, or when a gate's \"byte-identical report\" acceptance criterion has to be verified."
source: auto-skill
extracted_at: '2026-10-10T18:55:25.508Z'
---

# Attributing the cost of a long serial gate

Worked out on `/home/tamara/Downloads/_Git/math` for `notes/scripts/gate.sh` (67 invocations, run
twice by `gate_driver.sh`): one pass **2006 s**, a pair **≈ 67 min**. The user's hypothesis was
"we're re-collecting the same data over and over again without caching it". It was **confirmed** — and
it turned out to be three separable problems with three different fixes, only one of which is a cache.

That runner is gone. The list is now `notes/scripts/gate.py` (**75 rows**, `(spec, needs, writes)`
triples over artifact keys, run by `gate_driver.sh` **once**), and the pool the options table priced is
implemented. Every figure below is the **pre-scheduler** baseline; the post-scheduler numbers are in
section 10.

The deliverable of an investigation like this is **options priced with measurements**, not a fix. Do
not implement anything until the numbers are on the table.

## 0. Get per-row wall times without touching the runner

A gate writes one report file per row, in row order. The delta between consecutive report mtimes **is**
the row's wall time — no instrumentation, no re-run.

```python
# group rows into maximal runs of increasing mtimes; a reset means a new run of the gate
rows = sorted(reports, key=lambda r: r.mtime)
runs, cur = [], [rows[0]]
for prev, nxt in zip(rows, rows[1:]):
    (cur if nxt.mtime >= prev.mtime else runs.append(cur) or cur).append(nxt)
```

Two traps:
- **Timezone.** Default `ls -l` timestamps are LOCAL (here UTC−7). Print `TZ=UTC date -u +%H:%M:%S`
  next to every timestamp you quote, and never infer a phase ("the writer block is running now") from
  a stale report mtime — confirm with `pgrep -af` plus the log tail.
- **Tag matching.** To map a report file back to a row, reproduce the runner's tag rule *exactly*,
  including the newline. `tag="$(echo "$name $*" | tr -c 'A-Za-z0-9' '_')"` — `echo`'s trailing newline
  is folded to `_` by `tr` **before** command substitution strips it, so a no-arg row's tag ends in
  **two** underscores and an arg row in **one**. Python:
  `parts = spec.split(); re.sub(r"[^A-Za-z0-9]", "_", f"{parts[0]} {' '.join(parts[1:])}\n")`.
  A tag rule you write from memory matches nothing.

Result: cost is concentrated. **4 rows = 58 % of a pass; the top 10 = 96 %** of the 50-row
measurement/checker block; everything below rank ~12 is ≤ 3 s. Optimize the head, ignore the tail.

## 1. Cold vs warm: the cheapest decisive experiment

Run the **same rows, same code** twice and compare. Here the 16 generator rows cost **450 s cold /
161.3 s warm** — a 2.8× swing on identical code. That single number proves the cost is cache state,
not computation, and it costs one run.

## 2. The in-process test that separates re-collection from work

Call the same function three times in one process and time each call:

```python
for i in range(3):
    t = time.perf_counter(); check(page); print(f"{time.perf_counter()-t:.2f}")
```

Measured: **104.50 s → 67.24 s → 0.13 s**. Same code, same page, same output. The third call is ~800×
cheaper than the first. Quote this triple when someone argues the gate is compute-bound.

## 3. Count opens and bytes per row

`sys.addaudithook` on the `open` event + `/proc/self/io` deltas, wrapped around a target script:

```python
import sys, pathlib
opens = []
def hook(event, args):
    if event == "open":
        opens.append(str(args[0]))
sys.addaudithook(hook)
def io():
    return {k: int(v) for k, v in
            (l.split(":", 1) for l in pathlib.Path("/proc/self/io").read_text().splitlines())}
b0, t0 = io(), time.perf_counter()
runpy.run_path(target, run_name="__main__")          # caveat: does NOT set sys.path[0] to target dir
print(len(opens), len(set(opens)), len(opens) - len(set(opens)))
print(io()["rchar"] - b0["rchar"], io()["read_bytes"] - b0["read_bytes"])
```

`rchar` = bytes requested (page cache included); **`read_bytes` = bytes that actually came from
storage**. The pair is the whole diagnosis:

| row | wall s | opens | distinct | repeats | rchar MB | disk MB |
|---|---|---|---|---|---|---|
| `build_sources.py` | 2.47 | 39,081 | 7,753 | **31,328** | 641.1 | 0.3 |
| `extract_links.py` | 44.29 | 157,607 | 131,070 | 26,537 | 4,249.5 | **3,754.4** |
| `build_index.py` | 53.00 | 17,813 | 9,558 | 8,255 | 261.3 | **0.0** |
| `dump_template_slots.py` | 60.16 | 59,692 | 10,469 | **49,223** | 968.1 | 20.5 |

Read the rows, don't just record them: `build_sources` re-opens **80 %** of what it reads and costs
2.47 s *only because the pages are cached* (0.3 MB from disk). `build_index` reads 261 MB with **0.0 MB
from disk** — its 53 s is not I/O at all, so no cache helps it.

Two caveats to state whenever you quote these:
- The probe counts **the parent process only**. A script that shells out (`render_reports.py` runs
  `extract_links.py` and `build_index.py` as children) is **under-counted** — its children do the work.
- The audit hook adds per-open overhead, so **probed wall times are not gate wall times**. Never quote
  a probed wall time as a gate row time.

Do **not** probe the most expensive row: the hook made `verify_findings.py --mutant` run > 15 min with
an empty report. Probe the hot rows, skip the multiplied ones.

### 3b. The `most-reopened paths` histogram is what locates the mechanism in code

Print, per row, the top-N paths by open count and the opens grouped by top-level bucket. That
histogram — not the totals — is what turns "80 % repeats" into a named loop. The biggest writer row
probed at **154,407 opens / 12,309 distinct / 142,098 repeats (92 %)**, rchar **5,113.8 MB**,
`read_bytes` **1,895.2 MB**, and its histogram said:

```
58  overview.tex
36  notes/catalog.tsv
22  preprints/<slug>/build/main.tex   ← for every one of the 719 manuscript dirs
```

22 × 719 main-file opens in one row. Following it into the code found **stacked full-corpus walks**,
not one loop: `render_reports.py:119 measure()` is called **2× per process** (`:243`, `:3230`), and
each call walks all 719 listed dirs reading their `.tex` **four times** — `preprints.roots_of(d)`
(reads every `.tex` to find `\documentclass`), then a `rglob("main.tex")` read, then a
`rglob("*.tex")` read, then `build_sources.py:88 env_variants()` which does
`preprints.texts(preprints.tex_files(d))` — a third full read.

Two lessons:
- **Count real call sites before naming a multiplicity.** `grep -c "measure()"` reads 15; the other 13
  are docstrings naming *other* modules' `measure()`. The real call sites are 2.
- A shared helper (`catlib/paths.read_text`, **188 call sites** across the 47 gate scripts) being
  uncached is the *enabling* condition; the stacked walks are the *cause*. Fix both, name them
  separately — a cache in the helper does not stop a function being called twice.

## 4. Check the machine, not just the code

Cache eviction is a machine fact. `free -h` here: 60 GiB total, **58 used, buff/cache 2.2 GiB,
available 1.9 GiB, swap 14 GiB used**; `vmstat 1 3` showing nonzero `si`/`so`; one process
(`strata`, the local model server) holding **≈ 41 GiB RSS**. Against 2.2 GiB of page cache, a row that
pulls **3,754 MB from storage** evicts what every later row wants. That is the mechanism behind the
cold/warm swing, and it is why "just add a cache" is not automatically the fix — the cache has to be
*in-process*, since the OS cache is being evicted between rows.

## 5. Find the loop that multiplies a subprocess

The biggest single waste was not a cache problem at all. `verify_findings.py --mutant` calls its own
`check()` **7×** (6 corruptions + 1 clean), and each `check()` re-runs 5 subprocesses:

```python
outs = {s: run(s) for s in {s for _, s, _ in REPORTS}}   # inside check() — 98 % one script
```

Fix: compute it once, pass it into `check()`. Zero cache semantics, zero byte risk.

**Price the saving from the in-process measurement, not from a sum of row times.** Summing the
individual report row times gave 52.5 s per `check()`; timing `check()` directly in one process gave
**37.26 s** of subprocess cost, and the page-check work is only **0.9 s** per call. So the waste is
6 × 37.26 = **223.6 s per pass (447.2 s per pair)** — the summed estimate overstates it by 40 %. The
full triple, quoted together:

```
check() cold (subprocesses included) 104.50 s   problems 0
check() with subprocess cache         67.24 s   problems 0
check() second cached call             0.13 s
7x mutant: subprocess cost 7x         260.8 s vs cached-once 37.3 s
7x mutant: page-check cost              0.9 s
```

Then aggregate each script **across every place it is invoked** — its own gate rows, plus once per
`check()` in each checker that shells out to it. `check_index_links.py` = **512.8 s = 25.6 % of a
pass**, of which 411 s is the same report produced 8 times. A script that "only" takes 51 s per row can
be a quarter of the gate.

Disprove the tempting hypothesis explicitly: `ledger()` measured 0.07 s and `tsv()` 0.00 s. The parse
helpers were not the cost; the subprocesses were. Measure before naming the culprit.

## 6. Cache-safety rule (the part that decides whether a cache is allowed)

A memoised read is safe **only for immutable release inputs**. Find every place a script generates a
file and then reads it back in the same run:

- `render_reports.py` runs `extract_links.py` as a child (comment: "extract_links.py writes
  notes/links.tsv, and the renderer must" see fresh bytes) and reads `LINKS_TSV` **after** it;
  same for `build_index.py`.
- So: cache `preprints/**`, `lean/**`, `overview.tex`, `CONTENTS.md`, `reasoning_traces/**`,
  `lean/docs/**`. **Exclude** `notes/*.tsv`, `notes/index/**`, `notes/summaries/**`.

Also check what the existing cache is keyed on before citing it as precedent. The only cache in the
package is `@functools.cache def rendered(page)` keyed by the **page NAME** (`render_reports.py`
dispatches `PAGE_RENDERERS[page]()`); passing page *text* raises `KeyError`. A cache keyed by name
explains why one mutant row is 1.05× its plain run while another is 7.8×.

## 6b. Census the fleet's read/write graph by **open mode**, not by AST

The cache-scope decision and any claim about row order both need one thing: which scripts write the
generated layer, and in which mode. Measure it with the same audit hook, capturing `(path, mode)`:

```python
if event == "open":
    path, mode = str(args[0]), (args[1] if len(args) > 1 else "r")
    opens.append((path, mode))
# strip the repo root first, then bucket by top-level dir
rel = pathlib.Path(path).resolve().relative_to(ROOT)
```

Print two tables: per-path counts **with their mode set** for every path under the generated dir, and
every write-mode open **outside** it. That is what answers "do the scripts read what they write?"

**Trap: an AST census is blind to branches.** Mapping a name to its enclosing call context tells you a
`write_text` exists in the file, not that it runs. Here it classified a checker as read-write on two
pages that a plain run opens in mode `r` only — the write lives solely in the `--mutant` branch. The
mode strings from a real run are the authority for "writes in this mode"; an AST census is a candidate
list. (Same class of bug as counting docstrings as call sites.)

**Trap: prefix comparison against absolute paths.** Bucketing by `path.startswith("notes/")` while the
paths are absolute reports **every** path as "other". Resolve and strip the root, then bucket.

**Trap: parsing your own probe output.** `awk '/,w, /'` matches only the write-mode section, not the
per-path table. Parse the table with block tracking:
`awk '/^=== /{blk=$2} /paths/{on=1;next} /write-mode/{on=0} on && NF>=3 && $2 ~ /[wax]/ {print blk": "$2"  "$3}'`.
And `sed -n '/^=== verify_foo/,/^=== /p'` matches **2 lines** — the target scripts print their own
`===` report headings, so block boundaries are unreliable. Get line numbers with `grep -n '^=== '`
first, then `sed -n 'a,bp'`.

What the census produced here: every writer reads the generated layer it writes
(`extract_subfindings` reads `catalog.tsv`; `build_sources` reads `catalog.tsv` **and**
`subfindings.tsv`; `extract_links` reads `links.tsv` in modes `r,w` and reads the page the renderer
writes), while the checker fleet writes almost nothing — two exceptions, one of them only in its
`--mutant` branch.

**Then read the row order off the graph.** Compare each writer's read set with the row that writes
that file. Two reads pointed **backwards** in the runner's order, so the generator block was **not
topological** and no single-pass ordering satisfied it — the twice-run absorbed the cycle. Two
consequences to state: a cross-row cache over the generated layer is unsafe (the file a row reads is
the file a later row rewrote), and a "just reorder the rows" fix must be proven, not argued.

**The cycle is removable, and removing it is cheaper than any cache.** Both backwards reads were the
same shape: a row read a file a later row wrote. Fixing them at the source (a writer stops reading its
own generated table, a checker stops reading a table another row writes later) makes the graph acyclic,
and the dependency scheduler then starts each row when its `needs` have finished. That is what the
scheduler in section 10 does, and it is why the twice-run is no longer needed.

**Check what your byte-identity snapshot covers before citing it as proof.** Re-read
`notes/scripts/gate_driver.sh`'s `snap()` 2026-10-11: it md5s **9 named TSVs** (only **8** exist on
disk — `notes/named-results.tsv` is a phantom that `2>/dev/null` drops silently) plus every file under
`notes/index/`. It does **not** cover `notes/*.md`, the summaries, the report templates, or
`notes/README.md`, so a hand-written page edit and a report-fed page edit are both invisible to the
snapshot diff. The promote-and-verify assertion, not the snapshot, is what proves the tracked
artifacts. Say which layers the snapshot actually proves.

## 7. Price the options, then recommend an order

Table every candidate with **measured cost removed** and **risk to the twice-run byte-identity proof**:

| # | change | measured cost removed | byte-identity risk |
|---|---|---|---|
| A | compute `outs`/`ledger()`/`tsv()` once, pass into `check()` | 315 s/pass; row 833 → ~518 s | **none** — no cache, same subprocesses, same bytes |
| B | run the read-only block in a bounded pool (32 CPUs; the gate was serial) | block 1555 s → max row (~114 s after A) | none for checkers (write nothing); writers stay in the dependency chain |
| C | memoise immutable release inputs in the shared read helper | 49,223 of 59,692 repeat opens; rchar 968 → ~200 MB | low, **only** if scoped to exclude generated files |
| D | collapse `extract_links.py`'s six `preprints/**` walks into one | rchar 4,249.5 → ~700 MB; disk 3,754 → ~630 MB | none — same file set, one enumeration |

Order: **A → D → C → B** — the changes with no cache semantics first, the cache (the real answer to the
hypothesis) third, the structural change last. Composition of measured parts must be **labelled as
composition, not measurement**: pass 2006 s → ~970 s after A+B → ~680 s with C warm, pair ≈ 23 min.

**B is the row to implement first once the graph is acyclic**, not last: with the two backwards reads
removed, the pool needs no second pass to be correct, and it is the only row whose saving does not
depend on cache state. Price it as `block time → the longest row on the critical path`, which is what
the measured scheduler delivered.

Check the scope of existing tracked work before recommending: the repo's catlib-refactor epic covers
*join* refactoring, not a read cache, so C needs its own sub-bead.

## 8. Operational traps hit while measuring

- `pkill -f <pattern>` **self-kills** when the pattern appears in your own command line (Signal 15,
  Exit Code 0) — and if the killed command was a compound one, the tail of it never ran. Kill detached
  drivers by explicit PID and process group (`kill -TERM -- -<PGID>`), and kill their child `sleep`
  separately.
- Writer/builder/gate stdout is block-buffered: run with `python3 -u`.
- Long probe runs: `is_background: true`, one poller per job, verify by pid/file — not by notification.
- Never edit `notes/**`, `overview.tex`, `CONTENTS.md`, `preprints/`, `lean/` while a writer, render,
  builder, gate or probe is live. `.qwen/tmp/` is safe.
- A call-site census from a bare-name regex counts docstrings: 109 "preprints reader" sites became
  **26 in 9 scripts** under the paren-anchored rule `\bNAME\s*\(`. Quote the paren-anchored number.

## 9. Report

State the baseline with its rule (75 rows, one pass; the pre-scheduler shell list was 67 rows × 2
passes = 2006 s/pass). Give the concentration, the cold/warm pair, the three-call triple, the per-row
opens table with both byte columns, and the options table with each row's byte-identity risk. Label
composed figures as composed. End with what has **not** been checked: the rows not yet probed, whether
a cache changes any generated byte (the promote-and-verify assertion is the test, not the probe), and
that no fix is implemented.

## 10. Implementing the scheduler the options table priced

The pool is not `xargs -P` over a list. It is a **dependency scheduler**, and the four parts that make
it correct are the parts a shell list cannot do.

**The list carries dependencies.** Each row is a `(spec, needs, writes)` triple over artifact keys, and
a row starts as soon as every row that writes its `needs` has finished. A row that reads a file a later
row writes is a cycle; remove it at the source (stop the reader reading) rather than absorbing it with
a second pass.

**The pool cap is sized by measured RSS, not by core count.** 32 cores is not the constraint here:
~6.1 GiB available with the model server loaded (2026-10-10), the two heaviest rows peaking at 415 MB.
Re-measured 2026-10-11: `free -h` reads **4.7 Gi available** of 60 with the engine at **34.3 GiB** RSS,
so the available figure moves with the loaded model — re-measure before sizing. A cap of 12
rows is what the measurement supports. `GATE_POOL=1` runs everything serially — that is the baseline
the pooled report is diffed against, and it must be run, because "pooled is faster than serial" is a
claim you can only make against a measured serial pass.

**Printing must be canonical.** A row's output is captured to a per-row file and the report prints the
files **in list order**, not in completion order. Without this the report is a race: the same rows, the
same bytes, in a different order every run. A row in the pool must spawn no writer — a render row that
runs a builder as a child must run it in `--check-only`.

**Byte-identical reports are impossible once every row prints its wall time**, and the honest test is
the normalized diff: strip the ` in X.Xs` suffix **and** every `\d+\.\d+s` token inside report heads,
collapse whitespace, then diff. A diff that only strips the suffix fails on rows whose report head
carries durations. The serial baseline's normalized report must match the pooled report in row order
and row content.

Measured result: shell list **461.4 s** wall / **921.8 s** row time → scheduler **351.1 s** wall /
**919.4 s** row time. Row time is flat; wall fell **110.3 s**. The serial pass is **876.0 s** wall over
**872.6 s** row time, so the pool is **2.49×** serial. The floor is the writer critical path
(`build_catalog` 0.1 → `extract_links` 21.5 → `build_index` 54.8 → `render_reports` 147.1 = **223.5 s**,
plus the longest row that needs the rendered pages, 122.5 s = **346.0 s**), and the measured wall was
351.1 s — 4 s of slot wait. **No pool makes the gate faster than its critical path.**

Two collapse wins are orthogonal to the pool and come from **per-process caching**: a cache keyed by
page name inside a module is paid once per process, so two gate rows that both render the same page
pay the corpus walk twice. Collapsing them into one row that prints both reports halves that cost.
