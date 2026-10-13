#!/usr/bin/env python3
"""Refresh the Lines column of the Sources table in every summaries page.

The Lines cell is a declared line count, and `verify_summaries.py` pass B compares it with the file
on disk. A merge moves that number for every cited file at once, so the cell is a derived value that
drifts; this script re-derives it.

Path resolution is the package's own (`catlib/summaries.py`'s `Page`), not a second implementation:
the number written is the number the checker compares against, which is the only way a refresh can be
trusted to land green. The count is `len(splitlines())`, matching the checker.

Formatting follows the pages' existing style: thousands separated by commas at 1,000 and above.

Usage: python3 notes/scripts/refresh_summary_line_counts.py            # rewrite every page
       python3 notes/scripts/refresh_summary_line_counts.py --check    # print drift, write nothing
       python3 notes/scripts/refresh_summary_line_counts.py <page.md>  # named pages only
"""
import argparse
import sys
from pathlib import Path

from catlib.atomic import cache_text
from catlib.paths import ROOT, SUMMARIES_DIR
from catlib.promote import artifact_of, key_for, promote
from catlib.summaries import ROW, Page

SUMMARIES = SUMMARIES_DIR

# The builder's key: the manuscript files it reads are inside the hashed trees; the summary pages it
# reads are its own output, so they are not L1.
KEY = key_for("refresh_summary_line_counts.py", tuple(sys.argv[1:]))


def fmt(n):
    return f"{n:,}" if n >= 1000 else str(n)


def refresh(path, write):
    """Return (rows checked, drift list) for one page; rewrite the table when write is true."""
    lines = path.read_text(encoding="utf-8").splitlines()
    page = Page(path, lines)
    out, drift = list(lines), []
    for sid, rel, declared, n in page.rows:
        # "—" is a page's deliberate "no line count" cell (the compiled PDFs, whose byte
        # newlines mean nothing), and pass B skips it. Writing a number there would invent a
        # problem, so the em dash is left exactly as the page states it.
        if declared == "—":
            continue
        target = page.table[sid][1]
        if target is None:
            drift.append(f"{sid} file not on disk: {rel}")
            continue
        want = fmt(len(target.read_text(encoding="utf-8", errors="replace").splitlines()))
        # Compare as numbers: "1015" and "1,015" are the same count, and the checker reads ints.
        if int(declared.replace(",", "")) == int(want.replace(",", "")):
            continue
        drift.append(f"{sid} ({rel}) says {declared}, file has {want}")
        if write:
            m = ROW.match(out[n - 1])
            if m is None:
                drift.append(f"{sid} row line {n} is not a table row")
                continue
            out[n - 1] = f"| {m.group(1)} | {m.group(2)} | {want} | {m.group(4)} |"
    body = "\n".join(out)
    if not body.endswith("\n"):
        body += "\n"
    if write and drift:
        promote(path, KEY, body)
    elif write:
        # A page with no drift is not promoted, so its bytes are cached without approval: the cache
        # entry and the tracked page stay the same bytes, which is what the cache verifier compares.
        cache_text(KEY, artifact_of(path), body)
    return len(page.rows), drift


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("pages", nargs="*", help="named pages (default: every page under notes/summaries)")
    ap.add_argument("--check", action="store_true", help="print drift and write nothing")
    ap.add_argument("--check-only", action="store_true", help="alias of --check")
    args = ap.parse_args()
    check = args.check or args.check_only
    pages = [Path(p).resolve() for p in args.pages] or sorted(SUMMARIES.glob("**/*.md"))

    total_rows = total_drift = 0
    for p in pages:
        rows, drift = refresh(p, write=not check)
        total_rows += rows
        total_drift += len(drift)
        if drift:
            print(f"{p.relative_to(ROOT)}: {len(drift)} stale cell(s)")
            for d in drift:
                print(f"    {d}")
    print(f"\npages {len(pages)}  table rows {total_rows}  "
          f"{'stale' if check else 'refreshed'} {total_drift}  "
          f"mode {'check' if check else 'write'}")
    raise SystemExit(1 if check and total_drift else 0)


main()
