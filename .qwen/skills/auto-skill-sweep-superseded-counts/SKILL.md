---
name: sweep-superseded-counts
description: "Sweep every doc, checker and generated artifact that quotes a count a later batch invalidated — triage a fleet of red checkers first, enumerate the stale values, fix generated literals in the generator, make the checker measure the figure instead of carrying it, print the needles from the checker, re-target the mutants, and prove the sweep with the single gate run and the promote-and-verify assertion. The same sweep shape applies to a moved directory (section 6a): link depth, quotation-exempt links, repo-relative anchors versus page-relative links, census rules, and HEAD-keyed template regeneration; and to the bead store (section 6c): open bodies are live instructions, titles carry counts, and `bd update` writes the DB so the tracked JSONL must be exported before you verify."
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
`notes-page-checker-traps` §1.1). The two needles above are the 2026-10-08 pair; the current pair is
`all notes/*.tsv bytes **630,606**` and `links extracted **66,107**` — re-target against the live
page, not against the sweep's own record.

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

**A refactor that shrinks a script makes a page's `Lines` cell stale, and the gate row is the only
detector.** Measured 2026-10-10: five `catlib` ports moved the shared joins out of
`build_catalog.py`, and `notes/findings.md:224` still declared 198 lines — the gate row
`verify_findings.py` exited 1 with `S2: declares 198 lines, notes/scripts/build_catalog.py has 181`.
The fix is the cell, set from `len(read_text().splitlines())` (the checker's own rule), and the sweep
must re-run that checker plain **and** `--mutant`. When a batch of ports lands, grep every Sources
table for the scripts it names and refresh each `Lines` cell in the same pass — a page that declares a
script's length is a claim about a file the refactor edits.

Re-measure the git state too. A handoff note said 3 commits were queued for push; live it was 5.

## 5. Run the whole gate list once, and read the promote-and-verify assertion

The bead's two gates are necessary, not sufficient: the sweep touched a generator, a checker, a
generated tree, and five docs. **Since 2026-10-11 the gate is one pass and the second run is gone.** Every
writer computes its bytes once, lands them under the digest-keyed record store, and writes the same bytes
onto the tracked path, so the test is the `verify_cache_promotion.py` row: for every tracked artifact, the
bytes cached under the builder's key must equal the bytes on the tracked path. The driver runs the list
once, snapshots md5 and `git status --porcelain`, and prints `rows N failures M` plus that assertion row.

What the single run does **not** prove, and what you check by hand: a hand-written page moving mid-run is
invisible to a single run and to the assertion, so `git status --porcelain` after the run must list no
`notes/` file, and `git diff --stat HEAD` is still the check that the sweep did not silently change a
measurement. Report-only extractors keep their "run twice and diff" test.

Batch the fast checkers in a loop that prints `plain=N mutant=N` per script (each run plain **and**
`--mutant` — the two runs answer different questions). Run the slow one (minutes over 122,458 files) as a
background shell while the rest run. Quote the reconciliation lines from the fresh runs, never from the
handoff file.

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

## 6a. The same sweep shape applies to a moved directory

Worked 2026-10-10 on `upstream_history/` → `notes/upstream_history/` (3 pages). A move is a count
sweep in disguise: the path string is the literal, and every reader of it — checker path constants,
docs, the ownership census, generated templates, mutant needles — goes red at once. The standing rule
is that a doc naming the old path is a **defect of the move**, not a follow-up, so it lands in the
same pass.

Order that worked:

1. `git mv` (history preserved, staged as `R`), committed with a pathspec covering **both** roots:
   `git commit -q -F .qwen/tmp/msgs/x.md -- upstream_history notes/upstream_history notes/scripts/verify_upstream_history.py`
2. Deepen the relative links by the depth you added, computed from each page's own directory:
   `](../history.md)` → `](../../history.md)`.
3. **Do not touch a link inside a `*"…"*` quotation.** The checker scans links on `QUOTE.sub("", body)`,
   so a quotation that quotes the release's own markdown is not a page link; "fixing" its depth
   falsifies a verified quotation.
4. Separate anchors from links in the checker. Anchors here are repo-relative
   (`rel = path[3:] if path.startswith("../") else path`, then `(ROOT / rel).is_file()`), so moving the
   pages changes nothing about them. Only the link pass is page-relative — resolve it against the
   page's own parent so a future move needs no checker edit at all:

   ```python
   for m in LINK.finditer(QUOTE.sub("", body)):
       target = m.group(1)
       if target.startswith(("http://", "https://", "#")):
           continue
       if not (ROOT / name).parent.joinpath(target).resolve().is_file():
           problems.append(f"{name}:{a + 1}: link target {target!r} does not exist")
   ```

5. Ownership census. A checker that partitions `notes/` by path rule flags every moved file as
   "owned by no rule" and its census total is short by the moved count
   (`census row notes/: page says 1128, disk says 1131`). Add the rule **and** the census key, and add
   the page's census row (3 files; total 1,128 → 1,131). Sweep the prose too: the manifest sentence
   that explained *why* those pages sat outside the census becomes false on the move.
6. Re-target the mutant whose needle was the pre-move bytes. The dead-link mutant searched
   `[`history.md`](../history.md)`, which the move deletes, so the mutation was a no-op and the run
   reported `MISSED — mutation changed nothing` (12 of 13 fired). Re-targeted to
   `../../history.md` → `../../historyx.md`: 13 of 13. Same §4 rule, and it is easy to miss because a
   move changes the bytes the needle was written against.
7. **Generated report templates are the residual, and they cannot be fixed in the same commit.**
   `build_report_templates.py` reads `git show HEAD:<page>`, so a template can only be re-slotted after
   its page commits are in HEAD. Sequence: commit the pages → commit the doc sweep →
   `build_report_templates.py` → `measure_templates.py` → `dump_template_slots.py` →
   `render_reports.py` → commit the templates plus the page that tabulates their bytes
   (`notes/templates.md`: 6,279 lines unchanged, 412,921 → **412,933** report tree, 427,740 →
   **427,752** over all 22 — the +12 is exactly the two `notes/` prefixes). Re-measured 2026-10-11
   from `notes/templates.md`: **18** report templates / **6,708** lines / **440,523** bytes, and
   **455,342** bytes over all **23** (the 5 hand-written index skeletons are in the total). The
   template count moves with the fleet, so quote the page's headline, not this pair. Never hand-edit
   `notes/templates/report/*.j2`; the builder regenerates them from HEAD.
8. Proof after a template rebuild: `render_reports.py` twice, and `git status --porcelain` after each
   run must list **no** `notes/` file (every report-fed page byte-identical to HEAD) with the two
   render reports identical. Budget for it: each render runs the child extractors and takes ~5 minutes,
   so run the pair as one background shell.
9. Grep the old path over docs, templates, skills, the generated tree **and** the bead store. Closed-bead
   prose in `.beads/issues.jsonl` naming the old bare path is history — report it, do not rewrite it.

A skill file that changed mid-session under you (an auto-skill update) is not yours: exclude it from
every pathspec commit, name it in the report, and ask before committing it.

## 6b. Adding a script to the fleet is a census sweep in disguise

Worked 2026-10-11 on `verify_fleet_design.py` (the 50th script, the 19th looped checker): one new file
moved ~20 count phrases in five docs plus the gate list. Re-measured 2026-10-11 from
`notes/scripts/README.md`: the fleet is **56** scripts — **10** writers, **23** report-only, **22**
checkers — so the "Nth" ordinal in the page moves with every addition; read it from the page, not from
this record. The checker that measures the census is the
enumerator — run it plain and it prints every phrase it demands, so sweep against its output, not
against a hand-built list.

The chain, in the order that worked:

1. **The gate list**: append the row to `notes/scripts/gate.py`'s `ROWS` array as a
   `(spec, needs, writes)` triple, and add the artifact key the row writes. Invocations = the number of
   `ROWS` entries, so a new checker is **two** rows (plain and `--mutant`) and the count is read
   straight from the array — there is no `run`-statement arithmetic left. A checker that reads a
   generated artifact needs that artifact in its `needs`; a row that spawns a writer must run the child
   with `--check-only`.
2. **The inventory page**: the class partition (scripts / checkers / "the Nth checker and the Nth
   script"), the write-nothing split, the checker table row (alphabetical — its second cell must name
   the page it checks, because the checker builds the checked-page set from that cell, so a missing row
   makes the page read as unchecked), the checker-invocation counts, the cost sum (add the new row's
   measured plain + mutant seconds: 1196.1 + 0.27 + 0.49 = **1196.9 s**), the importer census and the
   non-importer sentence (the census rule is `^[[:space:]]*(from|import) catlib`, so a deferred import
   counts), the naming sentence `named **X** of the **N** scripts` where X = N − gaps and the gaps are
   re-derived from the **pinned baseline commit**, not HEAD, the gap list itself, and the census table
   (new directory row, `notes/*.md` count, total).
3. **`notes/README.md`'s command block is a generated page.** Hand-editing it leaves the ownership
   checker's sync pass red (`page line 65: page has '…', writer does not`). Sequence: commit the page →
   `build_report_templates.py notes/README.md verify_script_ownership.py` (it reads
   `git show HEAD:<page>`) → `render_reports.py` → the sync pass is green. Same rule as §6a item 7.
4. **`AGENTS.md`**: the importer line, the inventory, the gate counts, and the new page's rule.
5. **`notes/linting.md`**: the source-file count (scripts + `catlib/` modules), the mypy gate line
   (`Success: no issues found in 73 source files`, measured 2026-10-11 with `.venv/bin/mypy
   notes/scripts/` — the count moves with every script, so quote it from a fresh run), the strict
   probe's `(N checked)` and the clean set
   (**N − files-with-errors**, not the previous clean count plus one — count the distinct files the
   probe names), and the `duplicate-code` / `cyclic-import` rows.
6. **A checker's own count-phrase template must be grammatical.** `f"returns **{n} lines**"` fails when
   the measured value is 1: the checker reports `count phrase not in the page: returns **1 lines**` and
   the page is the stale side. Write `f"**{n}** line{'s' if n != 1 else ''}"`.
7. **Check a probe's stability before sweeping its count.** `pylint --enable=R0401` read **7, 7, 7, 8,
   8** across five runs on the same tree, and `git archive HEAD notes/scripts` (the tree before the
   addition) gave the **identical distribution** — so the new checker added no cycle, and the count is a
   run property, not a tree property. Record the distribution and the diff between the two sets
   (`sed 's/.*Cyclic import //' | sort | diff`), not one number, and say in the doc that the count
   varies. A sequence of recorded counts (7 → 8 → 9 → 8 → 7) can be run-order noise, not five tree
   changes.
8. **Lint the new file before committing it.** A six-clause `and` chain in a membership test trips
   pylint `too-many-boolean-expressions` (R0916, limit 5) — build the set union once outside the loop.
   A `×` in a comment trips ruff `RUF003`.
9. **A checker that parses a record requires that record on disk.** The probe records the page quotes
   lived in `.qwen/tmp/` (gitignored), so the gate row would be vacuous in a fresh clone. Track them
   (`notes/probe/`), give the ownership checker a rule for the new directory, add the census row, and
   keep the absence guard that exits 1 when a record is missing.

Commit order: the code (page + checker + tracked evidence) as one commit, then the inventory sweep,
then the template rebuild, then the doc sweeps. New files need `git add` before a pathspec commit —
`git commit -- <new-file>` fails with "pathspec did not match any file(s) known to git".

## 6c. An open bead body is a live instruction — sweep it, and export before you verify

Worked 2026-10-11 on six bead bodies. A count in an **open** bead body is a live instruction — the bead's
acceptance bar compares against it — so it is swept. A count in a **closed** bead body is history: report
it, never rewrite it (§6a item 9).

**The trap that makes the sweep look finished when it is not: `bd update` writes the database, not the
tracked JSONL.** Verifying by reading `.beads/issues.jsonl` immediately after six `bd update` calls read all
six bodies as the pre-edit text (byte lengths unchanged, so the check reported every one stale). Sequence:
`bd update` → `bd export -o .beads/issues.jsonl` → verify, or verify with `bd show <id>`.

The chain that worked:

1. **Dump each body to a file** (parse the store with `json`) and edit only the stale numbers, keeping the
   procedure text, the acceptance bar, and the standing directives verbatim.
2. **Measure each count from the source that produces it**, never from the body: the generator report
   (`build_catalog.py --check-only`), a ledger join (`tier == "T0"` and `resolves_named == "1"`), a
   filesystem measure (`find preprints -name '*.tex' | wc -l` and the byte sum), the page's own table with
   its checker reporting 0 problems, and `bd ready` for a queue.
3. **Rewrite the body to record the old value and the rule that yields the new one.** The sweep is then
   self-documenting: a later pass can tell a live claim from a documented move.
4. **Titles carry counts too** — `bd update <id> --title "…"`. A title is the retrieval surface, the same
   rule as a memory filename slug: a title naming "the 83 remaining …" keeps asserting the stale count after
   the body is fixed. Fix the title in the same pass.
5. **A stale blocker sentence is prose, not an edge.** "This child is blocked by X" where X closed months
   ago: the `blocks` edge is satisfied, so the sentence is the stale side. Say the edge is satisfied and the
   bead is ready; do not delete the edge.
6. `bd update --body-file` needs an **absolute** path — it resolves relative to `<repo>/.qwen/`, not cwd.
7. Commit the store as its own pathspec commit: `git commit -q -F msg -- .beads/issues.jsonl`.

What moved in the pass worked: a first-pass comparison 206/64/111/95 → **203/62/109/94** (the page's Summary
table, checker 0 problems); a tier band 83/124 over a T0 of 137 → **78/118** inside a T0 of 130 families and
244 manuscripts; a five-discipline group 131/272 → **132/273**; a twelve-discipline group 137/266 →
**141/271**, its formalized split 123 of 268 (59/64) → **163 of 273** (79/84), its unformalized denominator
560 of 722 → **547 of 719 listed**; a coverage denominator 722 → **719 listed** (749 dirs); an FTS surface
7,729 files / 128 MB → **8,007 / 129 MB**. Two titles fixed. The three reading bands (73/146, 37/119, 8/46)
reproduced exactly from a fresh `parse_overview()`, so they were verified, not changed.

## 7. Report

Quote each figure with the rule that yields it and the fresh report line it came from (2026-10-11:
`links extracted 66107`, `all notes/*.tsv bytes 630606`), state which derived numbers did **not**
move and why, and close with what is not checked. The 2026-10-08 gap "a doc with no checker
(`notes/links.md`)" is **closed**: `verify_page_sync.py --both` is the render diff for
`notes/links.md`, `notes/names.md`, `notes/topics.md`, `notes/proof-density.md` and
`notes/index-links.md`, so those five pages are compared with the writer's render. What remains:
citation checkers that verify quotations and not claims, and nothing in
`lean/` built, so no formalization is elaboration-verified.
