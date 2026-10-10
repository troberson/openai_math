#!/usr/bin/env python3
"""Locate the lines a summaries page *should* cite when a quotation stops matching.

`verify_summaries.py` pass C says a quoted span is not verbatim in the lines its marker names. That
is usually the file having moved, not the page having misquoted: a merge re-wraps CONTENTS.md, a
regenerated yaml shifts its declarations, a scope note gains a line. This script answers the one
question the checker does not — where does the span live now? — by searching the whole cited file,
line by line and across consecutive line windows, under the checker's own normalization.

Report-only; writes nothing. It uses the package's unit, marker and normalization functions
(`catlib/summaries.py`), the same ones pass C runs, so a span it reports is the span pass C reported.

Usage: python3 notes/scripts/locate_summary_quotes.py <page.md> [page.md ...]
"""
import sys
from pathlib import Path

from catlib.paths import ROOT
from catlib.summaries import QUOTE, Page, label, markers, units, usable
from catlib.text import strip_markup as norm

WINDOWS = range(1, 6)


def find_in(src, span):
    """Line ranges (1-based, inclusive) of src whose joined text contains the normalized span."""
    nspan = norm(span)
    out = []
    for start in range(1, len(src) + 1):
        for w in WINDOWS:
            end = start + w - 1
            if end > len(src):
                break
            if nspan in norm(" ".join(src[start - 1:end])):
                out.append((start, end))
                break
    # A span found at several starts is found in the *shortest* window: a 5-line join that contains
    # it because its last line does is not the citation the page should carry.
    if not out:
        return []
    best = min(e - s for s, e in out)
    return [(s, e) for s, e in out if e - s == best]


def scan(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    page = Page(path, lines)
    misses = 0
    for start_line, unit, is_blockquote in units(lines):
        if is_blockquote:
            resolved = []
            for back in range(start_line - 2, max(start_line - 5, -1), -1):
                resolved = usable(page, markers(page.lines[back]))
                if resolved:
                    break
            spans = [unit]
        else:
            if "Prior (my training data" in unit:
                continue
            resolved = usable(page, markers(unit))
            spans = [m.group(1) or m.group(2) for m in QUOTE.finditer(unit)
                     if len(m.group(1) or m.group(2)) >= 12]
        candidates = [(sid, a, b) for _, sid, a, b in resolved]
        for span in spans:
            if not candidates:
                continue
            # Pass C's own test first: any candidate whose cited range contains the span is a hit,
            # so a span that matches candidate #3 is not a miss even when candidate #1 is dead.
            if any(norm(span) in norm(" ".join(page.lines_of(sid)[a - 1:b]) if a
                 else " ".join(page.lines_of(sid))) for sid, a, b in candidates):
                continue
            located = None
            for sid, _a, _b in candidates:
                hits = find_in(page.lines_of(sid), span)
                if hits:
                    located = (sid, hits)
                    break
            if located is None:
                misses += 1
                print(f"[doc line {start_line}] cited {label(*candidates[0])} -> NOT FOUND IN "
                      f"ANY CITED FILE  {norm(span)[:90]}")
                continue
            sid, hits = located
            misses += 1
            ranges = ", ".join(f"{s}" if s == e else f"{s}-{e}" for s, e in hits[:6])
            print(f"[doc line {start_line}] cited {label(*candidates[0])} -> "
                  f"{sid}:{ranges}  {norm(span)[:90]}")
    return misses


def main():
    total = 0
    for arg in sys.argv[1:]:
        path = Path(arg).resolve()
        print(f"===== {path.relative_to(ROOT)}")
        total += scan(path)
    print(f"\nspans needing a marker change: {total}")
    raise SystemExit(0)


main()
