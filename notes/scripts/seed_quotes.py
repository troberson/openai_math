#!/usr/bin/env python3
r"""Seed the quote-spec table for the pair-line page and the 21 summaries pages, and prove the resolver
reproduces every quote.

A spec is `(page, fam, seq, which, path, start, end, head, tail, mode)`: the source file, the line window
the quote sits on, the first words of the quote widened until they are unique inside that window, the last
three words, and the round-trip class. `catlib/quotes.py` resolves the spec back to the source bytes. This
script seeds the specs from pages that already carry their quotes, then resolves each one and requires the
resolved span to be the page's quote -- so a seeded table is a round-trip, not a transcription.

**The two page grammars are two seeders.** `notes/subfinding-pairs.md` cites by anchor:

    - main|clause: "<clause>" (`overview.tex:94`) -> "<title>" (`overview.tex:94`) [009:3]

The anchors inside it are read with `catlib.quotes.ANCH`, which is `catlib.anchors.anchor_pattern` with the
manuscript extension set and ranges allowed -- the same grammar the page's checker uses. `which` is
`clause`, `main`, or `title`; `seq` is the manuscript the pair names. The window is seeded from the anchored
line and widened downward to `MAXW` lines, because a manuscript sentence wraps.

A summaries page cites by a `[Sn:line]` marker, so the window is the range the marker names and no widening
is needed. The span set, the attribution and the classification are the shared rules
(`catlib.summaries.spans_of`, `catlib.summaries.candidates`, `catlib.quotes.seed_page`), so the specs seeded
here are exactly the spans `verify_summaries.py` pass C checks. `which` is `inline` or `block`; `seq` is the
span's index in the page. `mode` is `raw` when the resolved span is the page's quote byte-for-byte, `folded`
when it is equal only after `catlib.text.strip_markup` (the page dropped markup the source carries), and
`none` when the cited file does not carry the span.

Measured 2026-10-12: **1,161** specs over the two surfaces -- **236** pair-line specs, all raw, and **925**
summaries specs, **860** raw, **51** folded, **14** not located. The 14 are seeded with `start` 0 and kept as
measured negatives: the table records that the cited file does not carry the span, and they do not fail the
round-trip.

The table lands at `notes/tables/quotes.tsv` through the promote registry, so the cached bytes and the
tracked bytes are the same bytes. `--check-only` runs the full measurement and writes nothing.

Usage: python3 notes/scripts/seed_quotes.py [--tsv] [--check-only]
"""
import re
import sys
from collections import Counter

from catlib.paths import ROOT, SUMMARIES_DIR
from catlib.promote import key_for, promote
from catlib.quotes import ANCH, resolve, seed, seed_page
from catlib.summaries import Page
from catlib.text import strip_markup
from catlib.tsv import rows_text

PAGE = ROOT / "notes" / "subfinding-pairs.md"
SRC = ROOT / "overview.tex"
OUT = ROOT / "notes" / "tables" / "quotes.tsv"
PAGES = str(PAGE.relative_to(ROOT))

COLS = ("page", "fam", "seq", "which", "path", "start", "end", "head", "tail", "mode")

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
                out.append(({"page": PAGES, "fam": fam, "seq": seq, "which": which, "path": path,
                             "start": "0", "end": "0", "head": "", "tail": "", "mode": "none"}, q))
                continue
            s, e, head, tail = got
            out.append(({"page": PAGES, "fam": fam, "seq": seq, "which": which, "path": path,
                         "start": str(s), "end": str(e), "head": head, "tail": tail or "",
                         "mode": "raw"}, q))
    return out


def summary_rows() -> list[tuple[dict[str, str], str]]:
    """Every quoted span the 21 summaries pages carry, seeded to a spec, with the quote it must reproduce.

    `path` is the file the page's `[Sn]` row resolves to, repo-relative, so a row names a file the round-trip
    can read without knowing the manuscript root. A span with no usable citation, or one the cited file does
    not carry, is seeded to `start` 0 with `mode` `none`.
    """
    out: list[tuple[dict[str, str], str]] = []
    for p in sorted(SUMMARIES_DIR.rglob("*.md")):
        page = Page(p, p.read_text(encoding="utf-8").splitlines())
        for n, (sid, which, span, start, end, head, tail, mode) in enumerate(seed_page(page), 1):
            src = page.table.get(sid, ("", None))[1]
            out.append(({"page": str(p.relative_to(ROOT)), "fam": page.fam or "", "seq": str(n),
                         "which": which, "path": str(src.relative_to(ROOT)) if src else "",
                         "start": str(start), "end": str(end), "head": head, "tail": tail or "",
                         "mode": mode}, span))
    return out


def main() -> int:
    args = tuple(sys.argv[1:])
    lines = SRC.read_text(encoding="utf-8").splitlines()
    all_rows = rows(lines) + summary_rows()
    specs = [s for s, _q in all_rows]
    cache: dict[str, list[str]] = {"overview.tex": lines}
    bad: list[tuple[str, str, str]] = []
    for spec, q in all_rows:
        if spec["mode"] == "none":
            # A measured negative: the cited file does not carry the span, so there is no spec to resolve.
            continue
        key = spec["path"]
        if key not in cache:
            f = ROOT / key
            cache[key] = (f.read_text(encoding="utf-8", errors="replace").splitlines()
                          if f.is_file() else [])
        src = cache[key]
        got = resolve(src, int(spec["start"]), int(spec["end"]), spec["head"], spec["tail"] or None)
        ok = got == q if spec["mode"] == "raw" else got is not None and strip_markup(got) == strip_markup(q)
        if not ok:
            bad.append((f"{spec['page']} [{spec['fam']}:{spec['seq']} {spec['which']}]",
                        spec["head"][:30], f"resolved {str(got)[:44]!r} vs quote {q[:44]!r}"))
    seeded = [s for s in specs if s["start"] != "0"]
    pair = [s for s in specs if s["page"] == PAGES]
    summ = [s for s in specs if s["page"] != PAGES]
    modes = Counter(s["mode"] for s in specs)
    print(f"quotes in the pages: {len(specs)}")
    print(f"  pair-line specs ({PAGES}): {len(pair)}")
    print(f"  summaries specs ({len({s['page'] for s in summ})} pages): {len(summ)}")
    print(f"  specs seeded: {len(seeded)}   measured negatives (start 0): {len(specs) - len(seeded)}")
    print(f"  single-line spec: {sum(1 for s in seeded if s['start'] == s['end'])}"
          f"   range spec: {sum(1 for s in seeded if s['start'] != s['end'])}")
    print(f"  head widened past 3 words: {sum(1 for s in seeded if len(s['head'].split()) > 3)}")
    print(f"  whole-quote spec (no boundary): {sum(1 for s in seeded if s['tail'] == '')}")
    print(f"  mode: raw {modes['raw']}  folded {modes['folded']}  not located {modes['none']}")
    print(f"  resolver reproduces the page quote: {len(seeded) - len(bad)} of {len(seeded)}")
    print(f"  round-trip failures: {len(bad)}")
    for where, head, why in bad:
        print(f"    [{where}] {head}  -- {why}")
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
