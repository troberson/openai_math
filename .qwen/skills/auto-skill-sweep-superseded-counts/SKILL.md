---
name: sweep-superseded-counts
description: Sweep every doc, checker and generated artifact that quotes a count a later batch
  invalidated — triage a fleet of red checkers first, enumerate the stale values, fix generated
  literals in the generator, make the checker measure the figure instead of carrying it, print the
  needles from the checker, re-target the mutants, and prove the sweep with a twice-run gate list
  diffed against HEAD.
source: auto-skill
extracted_at: '2026-10-08T15:40:04.714Z'
---

# Sweeping superseded counts out of a verified doc tree

For a repo whose analysis docs are verified by regex checkers, so a number that moves in the corpus
makes a page **false and its checker red**. Worked out on the OpenAI Research Catalog
(`/home/tamara/Downloads/_Git/math`) on 2026-10-08, sweeping three figures at once after 9 new
summary pages and a new TSV landed: the summary pairing (12 families / 31 manuscripts → 21 / 60),
the index link counts (47354 → 47363 registered, 65690 → 65699 scanned, 48872 → 48881
file-resolving, `notes-doc` 569 links / 12 targets → 578 / 26), and the all-TSV byte total
(541463 → 630987).

Applied a second time the same day on a much larger scale: an upstream merge moved 15 ledger figures
at once (manuscripts 722 → 719, scope notes 235 → 242, challenges 405 → 416, `main_results` 185/178 →
200/189, tiers T3 127 → 136 / T0 137 → 130, `.bib` files 501 → 521, entries 12,928 → 13,802) and
turned **10 of 19** checkers red. That run is where §4a and §3a came from.

The trigger is usually a checker failing **at HEAD**: the page quotes a number a later batch
invalidated. Record that as an issue whose description names the failing needle, the page line, and
the gate (`<checker> plain and --mutant both exit 0`). The gate is the bead's contract; write it
before touching the page.

## 1. Enumerate every stale value before editing anything

Collect each moved number in **every form it appears in**: raw (`65690`), thousands-grouped
(`65,690`), and the derived forms (deltas, denominators, target counts, percentages). Grep the whole
repo over `*.md` **and** `*.py`, including the generated tree, as one alternation:

```
541463|541,463|65690|65,690|48872|48,872|47354|47,354|17 targets|12 of 372 families have
```

Two reasons it must be one pass over all forms:

- A sweep that greps one number leaves the derived numbers. The link sweep moved four values inside
  one sentence and left three **gaps identical** — the registry gap (18,336), the dir-resolving count
  (16,818), the 94% share. Knowing which derived numbers do **not** move is as load-bearing as
  knowing which do; a "fixed" page that updates a gap the new data does not change is worse than the
  stale one.
- Do the arithmetic before editing, not during. `notes-doc` targets = 1 (`names.md`, linked by all
  552 name pages) + N summary pages + 5 entry-point docs − 1 (`names.md` is in the 5) → 17 at N=12,
  **26** at N=21. Write that derivation down so the next sweep can check it.

Grep the `.py` files too. Checkers and generators carry literals in four places: report-line needles,
record lists, mutant `replace()` targets, and text emitted into generated pages.

## 2. Fix a generated literal in the generator, never in the generated page

`notes/index/README.md:228` carries the link figure, and the string lives in `build_index.py`
(lines 911-913). `notes/links.tsv:23` is emitted by `extract_links.py`. Editing the generated page
desyncs it from the generator, and the next render silently reverts your fix.

```python
# build_index.py — the page footer is generated text; fix it here
"rendered page — 65699 links, 0 broken, 16818 of them resolving to a directory — "
```

Then re-render twice and diff the tree (a whole-tree `md5sum | md5sum` digest is the cheap version of
"byte-identical"). Same rule for a TSV row: change the row builder, regenerate, and diff the new TSV
against the pre-edit copy to prove **only** the intended row moved.

## 3. Where the checker carries the figure, make the checker measure it

A number in three places is three places to drift. `verify_findings.py` carried the disk link scan as
literals in three spots (the page needle, the `REPORTS` report-line literal, and `RECORD["S27"] =
["1,034", "65,690"]`). After the page sweep its plain run failed 3 problems, all of them the checker
quoting the old number. The durable fix is to measure it:

```python
# in measured() — the disk scan is the source of the page's figure, so measure it
ci = run("check_index_links.py")
disk_links = int(re.search(r"links extracted\s+(\d+)", ci).group(1))
disk_broken = int(re.search(r"broken links\s+(\d+)", ci).group(1))
```

and derive the needle:

```python
f"**{m['index_pages']:,}** pages carry **{m['disk_links']:,}** links with **{m['disk_broken']}** broken"
```

Keep the report-line literal (`("check_index_links.py", "links extracted        65699", …)`) — that
one is a **format contract** with the report script, and it is the copy that tells you when the report
format changed. Rule: a page figure derived from a report line should be measured by the checker, not
written into it; a literal is correct only when it pins a format, not a value.

### 3a. Print the needles; don't hand-compute them

Once the checker measures everything, it **is** the authoritative list of needles. Import it and print
every needle in the checker's exact format, then sweep the page in one substitution pass against that
printout. Hand-computing 40 needles from a raw report is where a sweep introduces its own off-by-one.

```python
# .qwen/tmp/cit_needles.py — scratch, imports the checker's own measure()
import extract_citations as ec, verify_citations as vc
M  = vc.measure(ec.norm_title)      # guarded normalization
M2 = vc.measure(vc.norm_noguard)    # a sensitivity column needs a SECOND measurement
listed = sum(int(r["paps"]) for r in ec.ledger_rows())
print("**%d** of %d" % (len(M["owners"]), listed))
```

Three traps in writing the printer: it must reproduce the checker's **formatting** (`format(n, ",")`
vs `%d`), its **scope** (`len(multi)` components, not `len(big)`; `M["disc"][sorted(big)[0]]`, not
`M["disc"][big]` — a set has no order), and it must **not** re-derive a figure the checker already
exposes. A printer that re-reads 521 `.bib` files to recompute one count turns a 40-second job into 10
minutes; add the field to the measure dict instead.

### 3b. The exception: a measurement script keeps literal gates

§3 applies to checkers. In a **measurement** script the population gates must stay literal, because
they are what makes a mutant detectable. `measure_proof_density.py` gates on
`tier counts == {'T3':136,'T2':106,'T1':0,'T0':130}`; derive that from the ledger and the "flip a tier
label" mutant becomes a no-op the gate happily accepts. Sweep the literals to fresh values with a
dated comment, and say in the comment why they are not derived.

### 3c. Scope the denominator to the ledger, not to the raw file set

A `.bib` can sit in a manuscript directory the ledger no longer lists (a superseded release dir). Keying
a family join on those owners raises `KeyError` at three separate sites, and inflates every
"of 722" denominator. Split owned/unowned once, near the top of the measurement, and use the ledger's
own manuscript count as the denominator:

```python
unowned = [m for m in men if m not in man2fam]      # reported, never joined
men     = [m for m in men if m in man2fam]
listed  = sum(int(r["paps"]) for r in rows)         # 719, not the 513 .bib owners
```

The same scoping applies to a coverage caveat: "manuscripts with no `.bib`" is a blind spot only for
manuscripts the graph claimed to see.

## 4. Re-target every mutant whose `replace()` target was the old value

```python
"all-TSV total altered": lambda t: t.replace("together totals **630987** B", "together totals **296283** B", 1),
"disk link count altered": lambda t: t.replace("covers **65,699** links", "covers **65,700** links", 1),
```

Written against the old bytes, the target string is absent after the sweep, the mutation is a no-op,
and the mutant gate reports NOT INJECTED — a checker whose mutant cannot be injected verifies nothing
while exiting 0. Re-target in the **same** pass as the page, and assert `mutated != page` (see
`notes-page-checker-traps` §1.1).

## 4a. Triage a fleet of red checkers before editing any of them

After a big merge, 10 of 19 checkers went red at once. Do not start on one; run the whole fleet plain,
capture each report to a file, and classify **before** editing:

```
for s in notes/scripts/verify_*.py; do n=$(basename "$s" .py); timeout 580 python3 "$s" \
    > ".qwen/tmp/chk_${n}.txt" 2>&1; echo "$? $n"; done
for n in <the red ones>; do printf "%-30s %s\n" "$n" \
    "$(grep -c -E 'PROBLEM|MISSING|COUNT|not verbatim|Traceback' .qwen/tmp/chk_${n}.txt)"; done
```

Two things this exposes that a single-checker view hides:

- **A zero problem-line count with exit 1 is a crash, not a clean page** (`verify_t0_chains` — a
  refactor changed a helper's signature; one call site needed the new argument).
- **The failure is on the page side or the checker side, and the fix is in the other file.** A report
  reading `page checks: 21 problems` with every line a `FAIL … page does not contain` means the checker
  is already measured and only the page needs sweeping — finish that one first; it is the shortest path
  to green and it needs no code change.

Classify each red checker as: stale page literal / shifted `file:line` anchor / checker-side hardcoded
needle or mutant / genuine code breakage / real reading work (a page whose content must be re-derived,
e.g. 144 problems across 21 summary pages). Report the fleet as a table with the remaining work per
checker, order it shortest-path-first, and state what was **not** checked: no `--mutant` run is
meaningful until the checker exits 0, and a grep census of stale numbers is sizing, not an enumeration.

Re-measure the git state too. A handoff note said 3 commits were queued for push; live it was 5.

## 5. Run the whole gate list, twice, diffed against HEAD as well as between runs

The bead's two gates are necessary, not sufficient: the sweep touched a generator, a checker, a
generated tree, and five docs. Run everything, twice, and add the third diff:

```
python3 X.py > /tmp/r1.txt && cp out.tsv /tmp/a.tsv
python3 X.py > /tmp/r2.txt && cp out.tsv /tmp/b.tsv
diff -q /tmp/a.tsv /tmp/b.tsv && diff -q /tmp/r1.txt /tmp/r2.txt && diff -q /tmp/head.tsv /tmp/b.tsv
```

"identical between runs" proves determinism. "Unchanged vs HEAD" proves the sweep did not silently
change a measurement — the sweep edited `extract_links.py`, and only the vs-HEAD diff shows the other
21 rows of `links.tsv` are untouched.

Batch the fast checkers in a loop that prints `plain=N mutant=N` per script (17 of them in one loop,
each run plain **and** `--mutant` — the two runs answer different questions). Run the slow one
(`extract_formalization_deps.py`, minutes over 122,458 files) as a background shell while the rest
run. Quote the reconciliation lines from the fresh runs, never from the handoff file.

## 6. Commit split: when files overlap across purposes, merge and say so

Checkers read the **working tree**, not the index, so a hunk-split commit is a commit no checker can
verify. Here four docs (`AGENTS.md`, `notes/README.md`, `notes/findings.md`,
`notes/index-design.md`) each carried figures from two or three of the three sweeps, so splitting by
purpose needed hunk-level staging and produced unverifiable intermediate commits. Ship one sweep
commit and record the reason in the body:

> The three sweeps ship as one commit: AGENTS.md, notes/README.md, notes/findings.md and
> notes/index-design.md each carry figures from more than one sweep, so splitting by purpose needs
> hunk-level staging and would leave intermediate commits that no checker can verify — the checkers
> read the working tree, not the index.

Merging is not bundling: name every figure, its old value, its new value, and its cause in the body.
An unexplained multi-figure commit is what a reviewer cannot audit.

Queue change travels in its own commit (`git commit -q -F - -- .beads/issues.jsonl`). A pathspec
commit excludes other staged paths, so a staged issue store survives into it cleanly. The beads
pre-commit hook's auto-export can fail with `.git/index.lock` (it races the commit process itself) —
harmless; export by hand (`bd export -o .beads/issues.jsonl`) and commit the store separately.

bd specifics that bite: `bd close <id> --reason "…"` (there is **no** `--note`). An epic refuses to
close while any child is open, **including a deferred child** — do not `--force` past that to hide a
deferred item; leave the epic open and state why.

## 7. Report

Quote each figure with the rule that yields it and the fresh report line it came from
(`links extracted 65699`, `all notes/*.tsv bytes 630987`), state which derived numbers did **not**
move and why, and close with what is not checked. In this repo the standing gap list includes: a doc
with no checker (`notes/links.md` — its counts are reproduced by `extract_links.py`'s report, not
verified against the page), citation checkers that verify quotations and not claims, and nothing in
`lean/` built, so no formalization is elaboration-verified.
