#!/usr/bin/env python3
r"""Seed the quote-spec table for one page, and prove the resolver reproduces every quote.

A spec is `(page, fam, seq, which, path, start, end, head, tail)`: the source file, the line window the
quote sits on, the first words of the quote widened until they are unique inside that window, and the
last three words. `catlib/quotes.py` resolves the spec back to the source bytes. This script seeds the
specs from a page that already carries its quotes, then resolves each one and requires the resolved span
to be exactly the page's quote -- so a seeded table is a round-trip, not a transcription.

The page grammar is `notes/subfinding-pairs.md`'s pair line:

    - main|clause: "<clause>" (`overview.tex:94`) -> "<title>" (`overview.tex:94`) [009:3]

The anchors inside it are read with `catlib.quotes.ANCH`, which is `catlib.anchors.anchor_pattern` with
the manuscript extension set and ranges allowed -- the same grammar the page's checker uses. `which` is
`clause`, `main`, or `title`; `seq` is the manuscript the pair names. The window is seeded from the
anchored line and widened downward to `MAXW` lines, because a manuscript sentence wraps: measured
2026-10-12 over the 21 summaries pages, 491 of 736 checked spans sit across 2 to 8 source lines.

The table lands at `notes/tables/quotes.tsv` through the promote registry, so the cached bytes and the
tracked bytes are the same bytes. `--check-only` runs the full measurement and writes nothing.

Usage: python3 notes/scripts/seed_quotes.py [--tsv] [--check-only]
"""
import re
import sys

from catlib.paths import ROOT
from catlib.promote import key_for, promote
from catlib.quotes import ANCH, resolve, seed
from catlib.tsv import rows_text

PAGE = ROOT / "notes" / "subfinding-pairs.md"
SRC = ROOT / "overview.tex"
OUT = ROOT / "notes" / "tables" / "quotes.tsv"

COLS = ("page", "fam", "seq", "which", "path", "start", "end", "head", "tail")

# The widest window the pair-line seeder widens a spec to. Measured 2026-10-12: every pair-line quote
# sits on the anchored line, and the summaries spans, seeded against the range their own marker names,
# reach 26 lines, so this bound is never reached by the page it applies to.
MAXW = 24

HEADER = re.compile(r"^## (?P<fam>\d{3}) · `overview\.tex:(?P<line>\d+)` · n=(?P<n>\d+) · (?P<tier>T\d)$")
PAIR = re.compile(r'^-\s+(?P<kind>main|clause):\s+"(?P<q>.*?)"\s+\((?P<a>`[^`]+`)\)\s+->\s+(?P<rest>.*)$')
TARGET = re.compile(r'^"(?P<t>.*?)"\s+\((?P<a>`[^`]+`)\)\s+\[(?P<fam>\d{3}):(?P<seq>\d+)\]$')


def anchor(text: str) -> tuple[str, int, int]:
    """The (path, start, end) a backticked anchor names, read with the shared page grammar."""
    m = ANCH.search(text)
    if not m:
        return ("", 0, 0)
    start = int(m.group(2))
    return (m.group(1), start, int(m.group(3)) if m.group(3) else start)


def rows(lines: list[str]) -> list[tuple[dict[str, str], str]]:
    """Every pair-line quote in the page, seeded to a spec, with the quote it must reproduce."""
    out: list[tuple[dict[str, str], str]] = []
    fam = ""
    for ln in PAGE.read_text(encoding="utf-8").splitlines():
        h = HEADER.match(ln)
        if h:
            fam = h.group("fam")
            continue
        m = PAIR.match(ln)
        if not m:
            continue
        t = TARGET.match(m.group("rest"))
        path, start, end = anchor(m.group("a"))
        items = [(m.group("kind"), m.group("q"), t.group("seq") if t else "")]
        if t:
            items.append(("title", t.group("t"), t.group("seq")))
        for which, q, seq in items:
            got = seed(lines, q, start, end + MAXW - 1)
            if got is None:
                out.append(({"page": str(PAGE.relative_to(ROOT)), "fam": fam, "seq": seq,
                             "which": which, "path": path, "start": "0", "end": "0",
                             "head": "", "tail": ""}, q))
                continue
            s, e, head, tail = got
            out.append(({"page": str(PAGE.relative_to(ROOT)), "fam": fam, "seq": seq, "which": which,
                         "path": path, "start": str(s), "end": str(e),
                         "head": head, "tail": tail or ""}, q))
    return out


def main() -> int:
    args = tuple(sys.argv[1:])
    lines = SRC.read_text(encoding="utf-8").splitlines()
    pairs = rows(lines)
    bad = []
    for spec, q in pairs:
        if spec["start"] == "0":
            bad.append(("seed", spec["fam"] + ":" + spec["which"], "quote not in the anchored window"))
            continue
        got = resolve(lines, int(spec["start"]), int(spec["end"]), spec["head"], spec["tail"] or None)
        if got != q:
            bad.append((f"{spec['fam']}:{spec['which']}", spec["head"][:30],
                        f"resolved {str(got)[:44]!r} vs quote {q[:44]!r}"))
    seeded = [s for s, _q in pairs if s["start"] != "0"]
    print(f"quotes in the page: {len(pairs)}")
    print(f"  specs seeded: {len(seeded)}")
    print(f"  single-line spec: {sum(1 for s in seeded if s['start'] == s['end'])}"
          f"   range spec: {sum(1 for s in seeded if s['start'] != s['end'])}")
    print(f"  head widened past 3 words: {sum(1 for s in seeded if len(s['head'].split()) > 3)}")
    print(f"  whole-quote spec (no boundary): {sum(1 for s in seeded if s['tail'] == '')}")
    print(f"  resolver reproduces the page quote byte-for-byte: {len(pairs) - len(bad)}")
    print(f"  round-trip failures: {len(bad)}")
    for where, head, why in bad:
        print(f"    [{where}] {head}  -- {why}")
    specs = [s for s, _q in pairs]
    if "--tsv" in args:
        print()
        print(rows_text(COLS, specs))
    if "--check-only" in args:
        print("[check-only] nothing written")
    else:
        promote(OUT, key_for("seed_quotes.py", args), rows_text(COLS, specs))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
