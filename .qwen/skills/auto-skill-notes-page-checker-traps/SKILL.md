---
name: notes-page-checker-traps
description: "Author and maintain a script that verifies a notes/markdown page (numbered source markers, anchored quotations, quoted counts) — the traps that make a checker report green while checking nothing, and the needle-design rules that keep a mutant honest: derive needles from the mutated page and the checker's population, and never let a needle that fires for both the fixed and unfixed code be the proof. Use when writing a page verifier, adding a mutant to one, converting literal needles, widening a table row pattern, or trusting a checker you did not write."
source: auto-skill
extracted_at: '2026-10-14T07:05:46.252Z'
---

# Writing a checker for a notes page

Worked out on `/home/tamara/Downloads/_Git/math` while shipping `notes/reports/findings.md` with
`notes/scripts/verify_findings.py`. The page-writing half is covered by
`family-summary-citation-verified` (passes A/B/C). **This file is the checker-authoring half** — the
defects that made a checker report success while verifying nothing, and the ones that made it report
failure on a correct page. Problem count on the finished page went 71 → 5 → 1 → 0, and every step was a
checker defect, not a page defect.

## 0. The checker's contract, fixed before the first line

- **Write nothing.** If the generator's `main()` writes the ledger (here `build_catalog.main()` writes
  `notes/tables/catalog.tsv`), a checker that imports and calls it mutates the repo. **Copy the row builder**
  into the checker and rebuild rows from the shipped files.
- **The report line is the test.** Print the same figure the page quotes, with the rule attached
  (`main_results 200 entries over 189 configs`, not `189 over 189`). A report line that prints a
  different number from the page it is checking hides the disagreement.
- **Measure a figure the page takes from a report; do not write it into the checker.** A literal in a
  checker is a second copy of the number, and a corpus change makes it a third place the value has to
  be edited. `verify_findings.py` carried the disk link scan as literals in three spots (page needle,
  report-line needle, record list) and failed 3 problems the moment the page was swept; the fix was
  `disk_links = int(re.search(r"links extracted\s+(\d+)", run("check_index_links.py")).group(1))` and
  a derived needle. Keep a literal only where it pins a **format** contract with the report script —
  that copy is what tells you the report format changed. Full procedure:
  `sweep-superseded-counts` §3.
- **The exception: a population gate stays literal.** The rule above is for checkers. In a *measurement*
  script the gates that define the population must keep their literals, because they are what makes a
  mutant detectable: derive `tier counts == {'T3':136,'T2':106,'T1':0,'T0':130}` from the ledger and the
  "flip a tier label" mutant becomes a no-op the gate accepts. Sweep such literals to fresh values with a
  dated comment saying why they are not derived.
- **Once a checker measures everything, it is the needle list.** Import its `measure()` in a scratch
  script and print every needle in the checker's exact format; sweep the page against that printout
  instead of hand-computing counts from a raw report (`sweep-superseded-counts` §3a).
- **A checker writes nothing, so its own report is the test** — run it plain and with `--mutant` and
  exit non-zero on problems **and** on undetected mutants. The "run the writer twice and diff" test is
  gone: writers promote bytes under a digest key and `verify_cache_promotion.py` asserts the cached
  bytes equal the bytes on the tracked path, so one run proves the artifact.
- Fast extractors the page quotes are re-run as **subprocesses with `cwd=notes/scripts`** so sibling
  imports resolve (0.02–1 s each). Extractors that take 40–52 s are never imported into a checker.

## 1. Mutant design: the pass that never fires

Three separate failures, all found in one session:

1. **A stale mutant target is a silent no-op.** `p.replace("Reading all 235 sections, 115", …)` after
   the page had been rewritten to a verbatim quotation: the target string no longer existed, the
   mutation did nothing, the run reported `UNDETECTED (0 problems)` and **exited 0**. That pair is a
   dated incident, not a current figure — `notes/reports/scope-exclusions.md` now reads **242** scope notes
   with **121** stating an exclusion, so re-audit targets against the live page. Assert the
   mutation changed the page:

   ```python
   mutated = fn(page)
   assert mutated != page, f"mutant {name} targets text that is not in the page"
   ```

   After **any** page rewrite, re-audit every mutant's target against the live page.
2. **Match the expected message, not "any problem".** `hit = [p for p in got if expect in p]` is right;
   `if got` is not. A mutant that corrupts a quotation can be caught by an unrelated guard (the
   anchored-quotation count guard fired instead of the verbatim check) and the pass it was meant to
   prove is still unproven.
3. **A mutation that inserts a delimiter breaks the scanner, not the claim.** Replacing a quote's
   opening `"115 of 235 sections state at` with `"115 of 235 scope notes state at"` added a **closing**
   quote, which closed the span early; the quote regex then matched nothing near the marker, the marker
   was skipped as a prose citation, and the mutant was caught only by the count guard. Mutate the words,
   keep the delimiters.

Undetected mutants must fail the run:

```python
summary = mutants(page) if mutant else None
if summary is not None:
    undetected = int(summary.rsplit("undetected mutants:", 1)[1])
    if undetected:
        problems.append(f"{undetected} injected mutants went undetected")
```

Include a **paraphrase dressed as a quotation** in the mutant set. It is the failure a line-existence
pass cannot see, and it is the defect that actually shipped in the page (a `[S5:25-26]` "quotation" that
was the page's own summary of those lines).

## 2. Adjacency windows: the test that can never be true

A quotation is verified against the source lines its marker cites; the page text near the marker
supplies the candidate. Comparing a **window-relative** `sp.end()` against an **absolute** `m.start()`
can never satisfy the gap test:

```python
window = flat[max(0, m.start() - 400):m.start()]   # window-relative offsets live here
for sp in QUOTE.finditer(window):
    if len(window) - sp.end() <= PRE_GAP:          # NOT m.start() - sp.end()
        cand.append(sp.group(1))
```

This ran green while verifying **0** anchored quotations. Print the count of anchored quotations
verified on every run, and gate it:

```python
if checked < 12:
    problems.append(f"only {checked} anchored quotations verified")
```

The guard exists to catch a pass that verifies nothing — which is exactly what it caught.

Accept a candidate only under a directional rule: a **quotation** counts when it ENDS just before the
marker; a **code span** counts when it STARTS just after it (the yaml form `[S4:915] carries
`scope: "Partial progress."``). A marker with no adjacent span is a **prose citation** and is skipped.
That rule is what keeps `[S25]`-style prose citations from producing false positives.

## 3. Regex hazards

- **A quote/code-span alternation swallows quotations.** `“…”|`...`` matched a code span that opened
  *before* a quotation and consumed the quotation's opening quote (`**539** `sorry` occurrences, 415
  of them at least one; "zero of the 122,458 files under `lean/OAI/` …"`), so the candidate list
  came out empty. Scan the
  two forms with **separate regexes in separate windows**:

  ```python
  QUOTE = re.compile(r"[“\"]([^”\"]{8,})[”\"]")   # preceding window
  CODE  = re.compile(r"`([^`]{8,})`")             # following window
  ```
- **Needles that span a line break never match raw text.** Flatten the record before searching:
  `text = re.sub(r"\s+", " ", path.read_text(...))`. Same for the page. Needles must not embed `\n`.
- **Measure a TSV's value vocabulary before writing a needle.** `subfindings.tsv` `kind` is
  `manuscript` / `comparator-link` (not `comparator`); `formalization-deps.tsv` `lakefile_declared` is
  `y` / `n` and `patch_file` is the literal `none` for 8 rows. A needle written from a guess reads 0.

## 4. When a count disagrees, decide who is wrong from the generator report

Never "fix" both sides. Worked cases, each resolved against a fresh `build_catalog.py` report:

| Disagreement | Resolution |
|---|---|
| checker 189 `main_results`, page 200 | both are right and they are different quantities: `sum(main_results.values())` = 200 entries, `len(main_results)` = 189 configs. Print both. |
| checker 35 T0 families with two manuscripts, page 28 | page imprecise: 35 = T0 ∩ `paps == 2`; 28 = a named reading population carrying 56 manuscripts. Page rewritten to say both. |
| checker 0 `INPUTS.md`, page 4 | use the generator's glob (`preprints/*/INPUTS.md`), not a narrower one. |
| checker "30 bundles over 0 families" | map bundle dirs → families **through the ledger rows**; a manuscript dir is not a family dir. |
| checker 21 summary families, report 57 | `sum(paps for families with a summary)`, not a count of families. |

## 5. Renumbering markers by script

Renumber to contiguous ids in **first-use order**, then re-parse and assert: ids 1..n contiguous, every
cited id declared, every declared id cited, every link resolves, declared line count == live count.

Slice arithmetic is the trap. In a marker match, `group(0)` is `"[" + "S" + id + rest + "]"`, so the id
starts at index 2:

```python
rest = m.group(0)[2 + len(m.group(1)):-1]     # [S4:29–56] -> ":29–56"
```

Both `len(tok)` (where `tok` includes the `S`) and `len(id) + 1` are off by one, and they **silently
duplicate a digit** (`[S44:29]` from `[S4:29]`). Verify by re-parsing the rewritten page, not by
eyeballing the diff.

Page shape when a page must both "put the links at the bottom" and "close with the gap": `## Sources`
immediately above the final `## Not checked`.

## 6. A checker finding is a page defect until judged

The `[S5:25-26]` "quotation" was a paraphrase; the fix was the page (quote the record verbatim), not the
checker. Judge every finding both ways before touching either side, and re-run the checker after the
last edit — the tally you report is from that final run.

**The numbering contract is `splitlines()`, and the `BLANK` guard is what exposes a violation.** The
checker resolves a marker against `read_text().splitlines()`, so a page whose anchors were read off a
shell display is off by one wherever the display dropped a leading blank line. Measured 2026-10-10: 10
anchors in one manuscript, reported as 4 `BLANK` problems and 4 `NOT VERBATIM` misses. The fix is the
page, and the fix is a probe that prints the index (`enumerate(splitlines())`), not a `sed` range —
`cat -n` prints the number, a bare `sed -n 'A,Bp'` does not, and the shell tool's display drops the
blank line the count depends on. Keep the `BLANK` guard: it is the only signal an anchor landed on a
blank line, and a page can report green on a shifted anchor whose span happens to contain the quote.

## 7. The anchor-set comparison, and the duplication that makes it inert

A page that quotes measured `name:line` sites (atomicity sites, env sites, set-iteration sites) needs a
pass that compares the page's anchors with the measured **set**. Two passes are not enough:

- the **count** pass proves only the count — a page naming a stale line still says `2 sites`;
- the **anchor** pass proves only that the line exists in the file — a site shifted to a neighbouring
  line resolves fine.

So the pass must require `sorted(page anchors in the paragraph) == sorted(measured sites)`, and the
report must print the measured sites with their line numbers so the page's numbers are checkable.
Measured 2026-10-12 on `notes/development/fleet-design.md`: the checker printed `set sites 2` with line numbers and
reported `problems 0` against a page naming two stale lines.

**The duplication trap.** A presence check ("every measured site appears in the checker-section
paragraph") is inert when the page carries the site **twice** in that paragraph — shifting one copy
leaves the site present in the other. Two mutants were undetected this way: the page enumerated all six
measured sites in the same paragraph that also carried the four-anchor list. Fixes, in order:

1. Require each site carried **once** in the paragraph, and de-duplicate the page: list the four, then
   "the three the four do not carry", never the six.
2. Move the paragraph's **illustrative** anchors off the measured sites. A bare-anchor example written
   with a measured site anchor (`render_reports.py:1150`) is a second copy of that site in the same
   paragraph. Pick a verified anchor that is not a measured site.
3. Path every anchor in a bullet the pass reads. A pathless anchor (`:1375`) is invisible to a regex
   that requires a path, so a bullet with one pathless anchor reads as one anchor and the set
   comparison silently compares one of two.

**Proving a new pass with new mutants.** Do not run `HEAD`'s checker with `--mutant` against the new
page: its needles are stale, so it prints `UNDETECTED: <name>: target not in the page` and the count is
meaningless. The honest proof is to load HEAD's checker as a module and evaluate the **new** lambdas
against the **current** page with HEAD's problem functions:

```python
import importlib.util, pathlib, subprocess
src = subprocess.run(["git", "show", "HEAD:notes/scripts/verify_X.py"], capture_output=True, text=True)
pathlib.Path(".qwen/tmp/head_X.py").write_text(src.stdout, encoding="utf-8")
spec = importlib.util.spec_from_file_location("headX", ".qwen/tmp/head_X.py")
head = importlib.util.module_from_spec(spec); spec.loader.exec_module(head)
page = pathlib.Path("notes/X.md").read_text(encoding="utf-8")
pop = head.population()
for name, a, b in new_mutants:          # (name, needle, replacement)
    m = page.replace(a, b, 1)
    print(name, len(head.count_problems(m, pop) + head.anchor_problems(m) + head.old_site_pass(m, pop)))
```

Expect `0 problems` for every new mutation under HEAD's checker and `N of N` under the fixed one. A
`LazyLoader` wrapper breaks this: the checker computes `ROOT = Path(__file__).resolve().parents[2]` and
`__file__` is undefined under a LazyLoader, so write the copy to a file and load it with
`spec_from_file_location`.

When the page's anchors move (a lint autofix shifts a line number), **re-target every mutant needle in
the same pass** — a needle matching pre-sweep bytes is an inert mutant. Full sweep procedure:
`sweep-superseded-counts`.

## 8. Needle design: a needle that fires for both states cannot prove the fix

Three rules, each from a measured case:

- **Derive the needle from the mutated page and the checker's measured population.** A needle that
  quotes a page line has to be re-measured by hand whenever the page's layout moves. Measured
  2026-10-13: one three-line paragraph edit moved five needles and a declared line count. Make the
  needle a function of the mutated text (find the line carrying the mutation's own byte) and of
  `population()` / `needles(measured())` for the corpus figures. Numeric literals in the needles go
  46 → 21 on `test_t0_chains.py` and 11 → 4 on `test_findings.py`; what remains is the mutation's own
  input (a family id, the value written, a decrement), not a measured figure.
- **Prove it with a layout shift.** Insert two lines into the page in memory and run every fault.
  Measured on `test_t0_chains.py`: literal needles break on **6** faults, derived needles break on
  **0**. A needle that survives a shift is a needle that carries no page line.
- **A needle that fires for the fixed and the unfixed code is not the proof.** The padding mutant's
  needle is the render-diff line, and the render diff fires against the pre-fix pattern too — the
  padded page differs from the writer's render either way. The discriminating assertion was the row
  count the pattern reads (**0** pre-fix, **27** post-fix), so the fault carried a second test. Confirm
  a new test fails against `git show HEAD:`'s checker before claiming coverage.

Two derivation traps. Key on the line the **pass reports**, not the line you mutated: the fenced-block
needle keys on the opening fence (the pass names 99; the mutated line is 103). And key on the
mutation's own byte when the page repeats prose — the first title-swap needle asserted on a substring
appearing on two lines.

Re-measure specificity after converting: no needle fires on another fault's page, and no needle fires on
the clean page.

## 9. Report

Quote the final run's report lines verbatim, the render-diff result (the page's bytes on disk against
the bytes its writer renders), and the mutant block including the `clean page: clean (0 problems)`
line. State the anchored-quotation count. End with what the checker does **not** verify: prose
citations with no adjacent span, claims inherited from the records the page cites, and anything that
would need a build.
