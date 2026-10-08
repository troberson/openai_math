---
name: notes-page-checker-traps
description: Author and maintain a script that verifies a notes/markdown page (numbered source markers, anchored quotations, quoted counts) — the traps that make a checker report green while checking nothing. Use when writing a page verifier, adding a mutant to one, or trusting a checker you did not write.
source: auto-skill
extracted_at: '2026-10-08T06:34:04.344Z'
---

# Writing a checker for a notes page

Worked out on `/home/tamara/Downloads/_Git/math` while shipping `notes/findings.md` with
`notes/scripts/verify_findings.py`. The page-writing half is covered by
`family-summary-citation-verified` (passes A/B/C). **This file is the checker-authoring half** — the
defects that made a checker report success while verifying nothing, and the ones that made it report
failure on a correct page. Problem count on the finished page went 71 → 5 → 1 → 0, and every step was a
checker defect, not a page defect.

## 0. The checker's contract, fixed before the first line

- **Write nothing.** If the generator's `main()` writes the ledger (here `build_catalog.main()` writes
  `notes/catalog.tsv`), a checker that imports and calls it mutates the repo. **Copy the row builder**
  into the checker and rebuild rows from the shipped files.
- **The report line is the test.** Print the same figure the page quotes, with the rule attached
  (`main_results 185 entries over 178 configs`, not `178 over 178`). A report line that prints a
  different number from the page it is checking hides the disagreement.
- **Measure a figure the page takes from a report; do not write it into the checker.** A literal in a
  checker is a second copy of the number, and a corpus change makes it a third place the value has to
  be edited. `verify_findings.py` carried the disk link scan as literals in three spots (page needle,
  report-line needle, record list) and failed 3 problems the moment the page was swept; the fix was
  `disk_links = int(re.search(r"links extracted\s+(\d+)", run("check_index_links.py")).group(1))` and
  a derived needle. Keep a literal only where it pins a **format** contract with the report script —
  that copy is what tells you the report format changed. Full procedure:
  `sweep-superseded-counts` §3.
- **Run twice, diff, byte-identical.** Exit non-zero on problems **and** on undetected mutants.
- Fast extractors the page quotes are re-run as **subprocesses with `cwd=notes/scripts`** so sibling
  imports resolve (0.02–1 s each). Extractors that take 40–52 s are never imported into a checker.

## 1. Mutant design: the pass that never fires

Three separate failures, all found in one session:

1. **A stale mutant target is a silent no-op.** `p.replace("Reading all 235 sections, 115", …)` after
   the page had been rewritten to a verbatim quotation: the target string no longer existed, the
   mutation did nothing, the run reported `UNDETECTED (0 problems)` and **exited 0**. Assert the
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
  *before* a quotation and consumed the quotation's opening quote (`**509** `sorry` occurrences …
  "zero of the 121,734 files under `lean/OAI/` …"`), so the candidate list came out empty. Scan the
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
| checker 178 `main_results`, page 185 | both are right and they are different quantities: `sum(main_results.values())` = 185 entries, `len(main_results)` = 178 configs. Print both. |
| checker 36 T0 families with two manuscripts, page 28 | page imprecise: 36 = T0 ∩ `paps == 2`; 28 = a named reading population carrying 56 manuscripts. Page rewritten to say both. |
| checker 0 `INPUTS.md`, page 4 | use the generator's glob (`preprints/*/INPUTS.md`), not a narrower one. |
| checker "30 bundles over 0 families" | map bundle dirs → families **through the ledger rows**; a manuscript dir is not a family dir. |
| checker 12 summary manuscripts, report 31 | `sum(paps for families with a summary)`, not a count of families. |

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

## 7. Report

Quote the final run's report lines verbatim, the twice-run diff result, and the mutant block including
the `clean page: clean (0 problems)` line. State the anchored-quotation count. End with what the
checker does **not** verify: prose citations with no adjacent span, claims inherited from the records
the page cites, and anything that would need a build.
