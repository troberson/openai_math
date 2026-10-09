#!/usr/bin/env python3
"""Locate the lines a summaries page *should* cite when a quotation stops matching.

`verify_summaries.py` pass C says a quoted span is not verbatim in the lines its marker names. That
is usually the file having moved, not the page having misquoted: a merge re-wraps CONTENTS.md, a
regenerated yaml shifts its declarations, a scope note gains a line. This script answers the one
question the checker does not — where does the span live now? — by searching the whole cited file,
line by line and across consecutive line windows, under the checker's own normalization.

Report-only; writes nothing. It reuses the checker's unit/marker/normalization functions so a span
it reports is the same span pass C reports.

Usage: python3 notes/scripts/locate_summary_quotes.py <page.md> [page.md ...]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_summaries as V  # noqa: E402

WINDOWS = range(1, 6)


def find_in(src, span):
    """Line ranges (1-based, inclusive) of src whose joined text contains the normalized span."""
    nspan = V.norm(span)
    out = []
    for start in range(1, len(src) + 1):
        for w in WINDOWS:
            end = start + w - 1
            if end > len(src):
                break
            if nspan in V.norm(" ".join(src[start - 1:end])):
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
    page = V.Page(path, lines)
    misses = 0
    for start_line, unit, is_blockquote in V.units(lines):
        if is_blockquote:
            resolved = []
            for back in range(start_line - 2, max(start_line - 5, -1), -1):
                resolved = V.usable(page, V.markers(page.lines[back]))
                if resolved:
                    break
            spans = [unit]
        else:
            if "Prior (my training data" in unit:
                continue
            resolved = V.usable(page, V.markers(unit))
            spans = [m.group(1) or m.group(2) for m in V.QUOTE.finditer(unit)
                     if len(m.group(1) or m.group(2)) >= 12]
        candidates = [(sid, a, b) for _, sid, a, b in resolved]
        for span in spans:
            if not candidates:
                continue
            # Pass C's own test first: any candidate whose cited range contains the span is a hit,
            # so a span that matches candidate #3 is not a miss even when candidate #1 is dead.
            if any(V.norm(span) in V.norm(" ".join(page.lines_of(sid)[a - 1:b]) if a
                 else " ".join(page.lines_of(sid))) for sid, a, b in candidates):
                continue
            located = None
            for sid, a, b in candidates:
                hits = find_in(page.lines_of(sid), span)
                if hits:
                    located = (sid, hits)
                    break
            if located is None:
                misses += 1
                print(f"[doc line {start_line}] cited {V.label(*candidates[0])} -> NOT FOUND IN "
                      f"ANY CITED FILE  {V.norm(span)[:90]}")
                continue
            sid, hits = located
            misses += 1
            ranges = ", ".join(f"{s}" if s == e else f"{s}-{e}" for s, e in hits[:6])
            print(f"[doc line {start_line}] cited {V.label(*candidates[0])} -> "
                  f"{sid}:{ranges}  {V.norm(span)[:90]}")
    return misses


def main():
    total = 0
    for arg in sys.argv[1:]:
        path = Path(arg).resolve()
        print(f"===== {path.relative_to(V.ROOT)}")
        total += scan(path)
    print(f"\nspans needing a marker change: {total}")
    raise SystemExit(0)


main()
