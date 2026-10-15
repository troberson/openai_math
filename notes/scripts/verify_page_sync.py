#!/usr/bin/env python3
"""The render-diff checker for the five pages whose sync pass used to live in a writer.

`grep -lE 'sync problems' notes/scripts/*.py` used to return 15 scripts. 10 are `verify_*`
checkers, where reading the page is the job. 5 were not: `extract_links.py`, `measure_names.py`,
`measure_topics.py` (twice), `measure_proof_density.py`, `check_index_links.py` — report-only
scripts and writers reading a page they do not verify. Those five passes live here, so the writer
fleet reads only what it is allowed to read and the page check has one owner.

The pass is the render diff: the page's bytes on disk against the bytes `render_reports.py`
renders for it. It proves the page is what the writer produces; it proves nothing about whether
the writer's numbers are right, which is the count pass's job, and the two are deliberately
independent.

`--mutant` mutates each page's prose **in memory** and compares the mutated text with the
render. It never writes a page, so `notes/development/index-links.md` and `notes/reports/proof-density.md` —
the two pages that had a second writer in the mutant branch — have one writer each. A needle that is
absent from its page is reported as a problem: an inert mutant is not a pass.

`catlib.render.rendered` is cached per process, so the plain pass and the mutant loop pay for the
corpus once per page, not once per mutant. The cache is per process, so running the two passes as
two invocations pays the corpus walk twice: measured 123.4 s plain + 122.9 s mutant as two rows,
against **125.2 s** for both in one process. `--both` runs them in one process and prints both
reports, so the gate carries one row. The check stays independent — the render is the writer's code
run in this process, not bytes read from the writer's cache.
"""

import sys

from catlib import render as RD
from catlib.paths import ROOT

# (page, needle, replacement). Each needle is prose the page carries verbatim, not a count phrase:
# a count is re-derived by the page's own count pass, so mutating one proves that pass, not this.
PAGES = [
    (ROOT / "notes" / "reports" / "links.md",
     "A directory walk would count a superseded edition's bibliography a second time.",
     "A directory walk would count a superseded edition's bibliography twice over."),
    (ROOT / "notes" / "reports" / "names.md",
     "Names sit in four places in this release, and they do not",
     "Names sit in five places in this release, and they do not"),
    (ROOT / "notes" / "reports" / "topics.md",
     "the pattern column is the source of truth",
     "the pattern column is the authoritative source"),
    (ROOT / "notes" / "reports" / "proof-density.md",
     "a 40-line construction",
     "a 41-line construction"),
    (ROOT / "notes" / "development" / "index-links.md",
     "demonstrated rather than recorded.",
     "demonstrated rather than written down."),
    # The summary-page counts are writer slots, so the render diff is the pass that proves them: a page
    # that carries a hand-written family count is not the writer's measurement.
    (ROOT / "notes" / "reports" / "findings.md",
     "**39** of 372 families have a summary page",
     "**40** of 372 families have a summary page"),
    # The workflow page's live counts are writer slots, so the render diff is the pass that proves
    # them: a page whose Pages-done count is hand-written is not the writer's measurement.
    (ROOT / "notes" / "development" / "summaries-workflow.md",
     "**Pages done (39):**",
     "**Pages done (40):**"),
]


def check() -> list[str]:
    """Sync problems for each page: its bytes on disk against the writer's render."""
    out: list[str] = []
    for page, _, _ in PAGES:
        text = page.read_text(encoding="utf-8")
        for p in RD.sync_problems(page, text):
            out.append(f"{page.name}: {p}")
    return out


def mutant_problems() -> tuple[int, int, list[str]]:
    """(caught, total, problems). Each mutant is applied to the page text in memory."""
    caught = 0
    problems: list[str] = []
    for page, needle, repl in PAGES:
        text = page.read_text(encoding="utf-8")
        if needle not in text:
            problems.append(f"{page.name}: needle {needle!r} absent — the mutant is inert")
            continue
        mutated = text.replace(needle, repl, 1)
        probs = RD.diff_problems(mutated, RD.rendered(page))
        if probs:
            caught += 1
        else:
            problems.append(f"{page.name}: the mutated page matched the render — the pass is inert")
    return caught, len(PAGES), problems


def main() -> int:
    if "--both" in sys.argv:
        problems = check()
        print(f"sync problems {len(problems)}")
        for p in problems:
            print(f"  {p}")
        caught, total, mprobs = mutant_problems()
        print(f"sync mutants caught {caught} of {total}")
        for p in mprobs:
            print(f"  {p}")
        return 1 if problems or mprobs or caught != total else 0
    if "--mutant" in sys.argv:
        caught, total, problems = mutant_problems()
        print(f"sync mutants caught {caught} of {total}")
        for p in problems:
            print(f"  {p}")
        return 1 if problems or caught != total else 0
    problems = check()
    print(f"sync problems {len(problems)}")
    for p in problems:
        print(f"  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
