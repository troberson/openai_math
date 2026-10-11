---
name: pure-digest-script-fleet
description: Redesign a fleet of generator/verifier scripts as pure functions of a content digest — the four-layer split, the purity rule stated precisely (not "never read the output dir"), a free and exact git-tree-digest cache key with its exactness proof, cache records not text, atomic staging plus promote-as-approval, and dissolving a twice-run idempotence test. Use when asked to make scripts pure / read-once / atomic / cached, when a generated-artifact tree is order-dependent, or when a "run it twice and diff" test is the repo's proof.
source: auto-skill
extracted_at: '2026-10-10T19:43:53.211Z'
---

# Restructuring a script fleet as a DAG over content digests

Worked out on `/home/tamara/Downloads/_Git/math` for `notes/scripts/` (49 scripts and 9 writers at
the time, a 67-invocation gate run twice = ~67 min) after the cost investigation in the
`gate-cost-attribution` skill. The design is **realized**: the fleet is 55 scripts with 10 writers,
the gate is `gate.py`'s 75-row dependency list run once, and every writer promotes through the
digest-keyed store. The user asked for five properties: **pure** (idempotent, non-interdependent),
**read something only once**, **ACID atomicity** (no partial file on crash), **cached** (unchanged
inputs and unchanged search definition ⇒ unchanged output), plus anything else that helps.

Three cheap measurements decided the whole design. Do them before proposing anything:

1. **The cache key is free.** `git rev-parse HEAD:preprints HEAD:lean HEAD:overview.tex
   HEAD:CONTENTS.md HEAD:reasoning_traces` → 5 tree digests in **0.002 s** (five repeats: 0.004 s).
2. **The key is exact.** `git status --porcelain --ignored=matching -- <those paths>` → **0 lines**,
   so nothing under the read surface is untracked or ignored. A tree digest therefore covers every
   byte the scripts read. Without this check a cache silently serves stale bytes for ignored files.
3. **Atomicity is 0 % implemented.** `grep -n 'os\.replace\|os\.rename\|shutil\.move\|NamedTemporaryFile\|\.tmp\b' notes/scripts/*.py`
   → **zero matches** across all 49 scripts, while one writer emits 1,049 files in place.

## 1. The four layers

Name the layers before naming any rule; every later rule is stated in terms of them.

| layer | content | status |
|---|---|---|
| **L0** release tree | the upstream inputs (manuscripts, formalization source, the release's own tex/markdown) | read-only, **git-digest-keyed** |
| **L1** hand-authored | curated vocabulary / prior / templates the repo writes by hand | read-only, **content-hashed** |
| **L2** derived records | per-item records (per-manuscript / per-family / per-config) | generated, content-addressed, **NOT tracked** |
| **L3** tracked output | the ledgers, generated pages, rendered index | **promoted from L2 by an explicit move** |

L2 is the cache. L3 is never read by a generator.

## 2. State the purity rule precisely — the literal version is too strong

The obvious rule, "a script never reads the output directory", is **wrong**: it would force every
script to re-walk the corpus, which is exactly the cost being removed. The rule that works:

> A script may read a derived record **iff that record is a pure function of L0 ∪ L1 keyed by its
> digest**. The graph over digests must be a DAG, with no dependence on run order.

So a ledger generated from the release tex is a **legal** input to everything downstream, while a
script reading a *prose page* that a renderer writes 12 rows later is **not**. Judge each edge by
"does this edge close a cycle over digests", never by "does the path contain `notes/`".

Find the violations by open-mode census (see `gate-cost-attribution` §6b — an AST census is blind to
branches), then classify each edge: legal DAG edge, self-read (a writer reading its own output), or
backwards read of a page another script writes.

The structural cause of order-dependence in this fleet was **checkers embedded in writers**: 15
scripts carried a trailing `sync problems (page.md) N` pass comparing themselves with the renderer's
output. 10 are `verify_*` checkers (legal — reading a page is their job); **5 are writers**, and those
five are what makes the writer fleet order-dependent. Move them to checker rows.

Two scripts must be **excluded from tree-digest keying** because they read git *history*, not the
tree (`git show <rev>:` reads). Enumerate them explicitly; a digest-keyed cache over them is a bug.

## 3. The cache key

```
key = ( git tree digests of every L0 path,
        sha256 of the script's own source,
        sha256 of the L1 files it reads,
        its args )
```

The user's phrase "we haven't changed the definition of what we're searching for" **is** the
script-source hash. Include the args, or a `--mutant` run serves its corrupted bytes to a plain run.

## 4. Cache records, never text

Compare the sizes and the machine before choosing what to cache:

- all 8 tracked ledgers: **630,606 bytes**
- the release manuscript tree: **632 MB**; the formalization source: **1.8 GB**
- RAM: **1 GiB available of 60** (`free -g`; `nproc` = 32)

Records are megabytes, text is not, and RAM is the binding constraint. A canonical per-manuscript
record (root count, resolved main file, section/proof/statement counts, bib count, byte counts — the
shape one ledger already had) replaces the re-walks: the worst gate row measured **154,399 opens over
12,301 distinct paths, 142,098 repeats**, 142,403 of them under the manuscript tree, from `measure()`
called 2× per process each walking 719 dirs and reading their `.tex` four times = 22 × 719 = 15,818
main-file opens in one row. Under L2 that row reads 719 records.

Make the record store **canonical and complete**: add what each consumer re-derives today, and make
every consumer read records. A partial store leaves the walks in place.

## 5. Atomicity: write to staging, promote by move

```python
def write_atomic(path, text):        # sibling temp in the SAME dir, fsync, os.replace
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w") as fh:
        fh.write(text); fh.flush(); os.fsync(fh.fileno())
    os.replace(tmp, path)
```

Writers build into `.qwen/cache/<key>/`; a **separate promote step** moves staged bytes to the tracked
paths. Three things get fixed at once:

- crash-safety (a killed writer leaves the tracked tree untouched — prove it by killing a big writer
  mid-run and showing the tracked tree unchanged),
- **approval is the move**, and `git status` is the approval record,
- the byte-identity **snapshot-scope problem dissolves**: oscillation becomes a cache-key question
  instead of "does my md5 snapshot cover the markdown pages too".

Check your snapshot's scope before citing it as proof, and check that it has no silent existence
guard: here the snapshot list named 9 ledgers while **8** exist on disk, and `md5sum ... 2>/dev/null`
dropped the phantom silently. Quote such a pair with its rule: *8 files on disk, 9 names in the list,
1 phantom.*

## 6. The twice-run loses its purpose — and its replacement is stronger

A "run it twice and diff the bytes" test exists for two reasons: it absorbs write/read cycles in the
runner's row order, and it is the repo's proof of determinism. Purity removes the first; atomic
promotion removes the second, because determinism becomes structural — a pure function of a
digest-keyed input cannot produce two byte strings.

Replacement test: **run once; assert promoted bytes == cached bytes; assert the cache key equals the
current L0 tree digests.** That is content-addressed equality, stronger than the temporal coincidence
the twice-run checks.

Support it with an idempotency census (grep for `datetime` / `uuid` / `getpid` / `platform` / env
reads / unsorted `iterdir`/`rglob`). Here: 0 nondeterministic calls, 1 env read, 2 set-iteration sites
consumed as `len(set(...))`, 11+3 unsorted directory walks consumed as a length or dict keys — i.e.
**deterministic by consumption, not by construction**. Fix it by sorting at the collection boundary.
Do **not** pin `PYTHONHASHSEED` as the fix.

## 7. The extras that fall out

- **`--check-only` on every script** (compute, report, write nothing) is the *precondition* for
  parallelism, so it comes before any pool. Verify the mode claim with the open-mode probe, not with
  the AST census.
- **One process, many passes.** The biggest writer re-parsed the release tex 58× and re-read the
  ledger 36× because each checker shells out to it.
- **One writer per artifact.** One generated page had two writers (a renderer and a checker); pick the
  owner (recommendation: the renderer owns, the checker only checks).
- **Split measure from render** so a page's numbers are measured, and the page-vs-writer diff proves
  the bytes on disk are the bytes the writer renders.

## 8. Say what the design does *not* buy

State these in the design doc, or the design gets blamed for what it never promised:

- **Purity buys correctness, not time.** The dominant row's cost is the corpus walks, not the page
  reads; purity alone barely moves it. The collection layer buys the time.
- **Cache invalidation is the new risk surface.** A wrong key serves stale bytes *silently*, which is
  worse than a slow gate. That is why the exactness check (§2, item 2) is not optional.
- **The doc sweep happens twice.** Row counts and census figures in the runner's docs change when the
  sync passes move and when `--check-only` rows appear; sweep them in the same pass as the change.
- Composed savings must be **labelled as composition, not measurement** (2006 s → ~970 s → ~680 s
  here, never measured on a real gate run).

## 9. Encode the plan in the tracker so the order is enforced

Recommendation order ⇒ **linear dependency chain**: each sub-bead `--deps` its predecessor, so only
the first is claimable. Verify direction with `bd show` (bare ids = "this depends on those"; a
`blocks:` prefix makes the new issue the blocker and silently empties `bd ready`).

When a new architecture **subsumes** existing beads, close them with a pointer, don't delete them:
`bd close <id> --reason "Superseded by <new-id>.<n> — <what replaces it>; <what survives>"`. Keep the
doc-sweep bead open. Record where each moved so the store and the docs agree, and re-export the
tracked store before committing (`bd create`/`bd close` do not re-export).

## 10. Report shape

Deliver: the layer table, the purity rule as stated, the cache key with its cost and its exactness
proof, the size/RAM argument, the violation table with mode-verified evidence, the atomicity census
grep and its zero, the exceptions excluded from keying, the honest-costs list, and the composition
figures labelled as composition. End with what has **not** been checked: rows not probed, the record
size estimate (arithmetic, not measurement), and that no composed figure has been measured on a real
run.
