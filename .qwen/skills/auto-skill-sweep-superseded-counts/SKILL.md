---
name: sweep-superseded-counts
description: Sweep every doc, checker and generated artifact that quotes a count a later batch
  invalidated — enumerate the stale values first, fix generated literals in the generator, make the
  checker measure the figure instead of carrying it, re-target the mutants, and prove the sweep with
  a twice-run gate list diffed against HEAD.
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

## 4. Re-target every mutant whose `replace()` target was the old value

```python
"all-TSV total altered": lambda t: t.replace("together totals **630987** B", "together totals **296283** B", 1),
"disk link count altered": lambda t: t.replace("covers **65,699** links", "covers **65,700** links", 1),
```

Written against the old bytes, the target string is absent after the sweep, the mutation is a no-op,
and the mutant gate reports NOT INJECTED — a checker whose mutant cannot be injected verifies nothing
while exiting 0. Re-target in the **same** pass as the page, and assert `mutated != page` (see
`notes-page-checker-traps` §1.1).

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
(`extract_formalization_deps.py`, minutes over 121,734 files) as a background shell while the rest
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
