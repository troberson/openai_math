#!/usr/bin/env python3
"""Fix blank-line citations in summary data files.

The data file's body cites source lines as [S4:29] or [S4:29–56]. A citation
whose start or end lands on a blank line in the named source is a miscite:
the author cited a paragraph boundary and the line numbering shifted. This
script finds those miscites and rewrites the data file so every cited line
carries non-blank text.

Rule:
- Single-line cite [S#:25] where line 25 is blank → try 26, then 24.
- Range [S#:25–28]: start shrinks forward to the first non-blank line ≥ 25;
  end shrinks backward to the last non-blank line ≤ 28.
- A window whose entire span is blank is left alone and reported (the target
  is ambiguous; the author must fix it by hand).

The script writes the data file atomically. It is an authoring tool, not a
gate row: run it after writing a data file and before `build_summaries.py`,
so the render picks up the corrected citations.

Usage: python3 notes/scripts/fix_blank_cites.py                # all data files
       python3 notes/scripts/fix_blank_cites.py <data-file> ... # named files
       python3 notes/scripts/fix_blank_cites.py --check-only   # report, no writes
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from catlib.atomic import write_atomic
from catlib.paths import ROOT

DATA_DIR = ROOT / "notes" / "data" / "summaries"
MARKER = re.compile(r"\[S(\d+):(\d+)([–-](\d+))?\]")


def parse_sources(text: str) -> dict[str, str]:
    """Map S# to its repo-relative path from the data file's sources block."""
    sources: dict[str, str] = {}
    m = re.search(r"<!-- sources\n(.*?)-->", text, re.DOTALL)
    if m:
        for line in m.group(1).strip().split("\n"):
            p = line.split("\t")
            if len(p) >= 2 and p[0].strip():
                sources[p[0].strip()] = p[1].strip()
    return sources


def nearest_nonblank(lines: list[str], pos: int, direction: int) -> int | None:
    """Walk from pos in `direction` (+1 forward, -1 backward) to the first non-blank line.

    Returns the 1-based line number, or None when no non-blank line is reachable
    within the file's bounds.
    """
    n = len(lines)
    step = direction
    p = pos
    while 1 <= p <= n:
        if lines[p - 1].strip():
            return p
        p += step
    return None


def fix_window(
    lines: list[str], a: int, b: int
) -> tuple[int, int] | None:
    """Fix a [a, b] window so both endpoints land on non-blank lines.

    Returns (a', b') or None when the whole window is blank (unfixable).
    """
    n = len(lines)
    if not (1 <= a <= n and 1 <= b <= n):
        return None
    if a > b:
        return None

    # Start: shrink forward
    a_fixed: int = a
    if not lines[a - 1].strip():
        candidate = nearest_nonblank(lines, a, +1)
        if candidate is None:
            return None
        a_fixed = candidate

    # End: shrink backward
    b_fixed: int = b
    if b != a and not lines[b - 1].strip():
        candidate = nearest_nonblank(lines, b, -1)
        if candidate is None:
            return None
        b_fixed = candidate

    if a_fixed > b_fixed:
        return None
    return a_fixed, b_fixed


def fix_text(data_text: str, sources: dict[str, str]) -> tuple[str, int]:
    """Apply the fix rule to all markers in the data file text.

    Returns (fixed_text, count) where count is the number of markers changed.
    """
    # Cache source file lines per sid
    _line_cache: dict[str, list[str]] = {}

    def get_lines(sid: str) -> list[str] | None:
        if sid in _line_cache:
            return _line_cache[sid]
        path = sources.get(sid)
        if path is None:
            return None
        fp = ROOT / path
        if not fp.is_file():
            return None
        try:
            ls = fp.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            return None
        _line_cache[sid] = ls
        return ls

    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        sid = f"S{m.group(1)}"
        a = int(m.group(2))
        b = int(m.group(4)) if m.group(4) else a
        lines = get_lines(sid)
        if lines is None:
            return m.group(0)
        fixed = fix_window(lines, a, b)
        if fixed is None:
            return m.group(0)
        if fixed == (a, b):
            return m.group(0)
        changed += 1
        a2, b2 = fixed
        if a2 == b2:
            return f"[{sid}:{a2}]"
        return f"[{sid}:{a2}\u2013{b2}]"

    # The quotes block uses tab-separated `S1  0  0` fields that do not match
    # the MARKER regex, so it is safe to scan the entire file.
    return MARKER.sub(repl, data_text), changed


def main() -> None:
    ap = argparse.ArgumentParser(description="Fix blank-line citations in summary data files.")
    ap.add_argument("files", nargs="*", help="data files (default: all under notes/data/summaries)")
    ap.add_argument("--check-only", action="store_true",
                    help="report fixes without writing")
    args = ap.parse_args()

    if args.files:
        docs = [Path(p).resolve() for p in args.files]
    else:
        docs = sorted(DATA_DIR.glob("*.md"))
    if not docs:
        print(f"no data files under {DATA_DIR}")
        sys.exit(1)

    total_fixes = 0
    total_unfixable = 0
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        sources = parse_sources(text)
        fixed, count = fix_text(text, sources)
        if count:
            total_fixes += count
            rel = doc.relative_to(ROOT)
            print(f"{rel}: {count} citation(s) fixed")
            if not args.check_only:
                target = DATA_DIR / doc.name
                write_atomic(target, fixed)
        # Report unfixable windows (entire span blank)
        _cache: dict[str, list[str]] = {}
        for m in MARKER.finditer(text):
            sid = f"S{m.group(1)}"
            a = int(m.group(2))
            b = int(m.group(4)) if m.group(4) else a
            if sid not in _cache:
                path = sources.get(sid)
                if path:
                    fp = ROOT / path
                    if fp.is_file():
                        _cache[sid] = fp.read_text(
                            encoding="utf-8", errors="replace"
                        ).splitlines()
                    else:
                        _cache[sid] = []
                else:
                    _cache[sid] = []
            lines = _cache[sid]
            if lines and 1 <= a <= len(lines) and 1 <= b <= len(lines):
                if a <= b:
                    span = lines[a - 1 : b]
                    if all(not l.strip() for l in span):
                        total_unfixable += 1
                        rel = doc.relative_to(ROOT)
                        print(f"{rel}: UNFIXABLE [{sid}:{a}\u2013{b}] "
                              f"(entire window blank)")
    status = "would fix" if args.check_only else "fixed"
    print(f"===== {len(docs)} data file(s): {total_fixes} citation(s) {status}, "
          f"{total_unfixable} unfixable")
    sys.exit(0 if total_unfixable == 0 else 1)


if __name__ == "__main__":
    main()
