#!/usr/bin/env python3
"""Refresh the Lines column of the Sources table in every summaries page.

The Lines cell is a declared line count, and `verify_summaries.py` pass B compares it with the file
on disk. A merge moves that number for every cited file at once, so the cell is a derived value that
drifts; this script re-derives it.

Path resolution is the checker's own (`verify_summaries.Page`), not a second implementation: the
number written is the number the checker compares against, which is the only way a refresh can be
trusted to land green. The count is `len(splitlines())`, matching the checker.

Formatting follows the pages' existing style: thousands separated by commas at 1,000 and above.

Usage: python3 notes/scripts/refresh_summary_line_counts.py            # rewrite every page
       python3 notes/scripts/refresh_summary_line_counts.py --check    # print drift, write nothing
       python3 notes/scripts/refresh_summary_line_counts.py <page.md>  # named pages only
"""
import argparse
from pathlib import Path

import verify_summaries as V

ROOT = V.ROOT
SUMMARIES = V.SUMMARIES
ROW = V.ROW


def fmt(n):
    return f"{n:,}" if n >= 1000 else str(n)


def refresh(path, write):
    """Return (rows checked, drift list) for one page; rewrite the table when write is true."""
    lines = path.read_text(encoding="utf-8").splitlines()
    page = V.Page(path, lines)
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
            out[n - 1] = f"| {m.group(1)} | {m.group(2)} | {want} | {m.group(4)} |"
    if write and drift:
        body = "\n".join(out)
        if not body.endswith("\n"):
            body += "\n"
        path.write_text(body, encoding="utf-8")
    return len(page.rows), drift


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("pages", nargs="*", help="named pages (default: every page under notes/summaries)")
    ap.add_argument("--check", action="store_true", help="print drift and write nothing")
    args = ap.parse_args()
    pages = [Path(p).resolve() for p in args.pages] or sorted(SUMMARIES.glob("**/*.md"))

    total_rows = total_drift = 0
    for p in pages:
        rows, drift = refresh(p, write=not args.check)
        total_rows += rows
        total_drift += len(drift)
        if drift:
            print(f"{p.relative_to(ROOT)}: {len(drift)} stale cell(s)")
            for d in drift:
                print(f"    {d}")
    print(f"\npages {len(pages)}  table rows {total_rows}  "
          f"{'stale' if args.check else 'refreshed'} {total_drift}  "
          f"mode {'check' if args.check else 'write'}")
    raise SystemExit(1 if args.check and total_drift else 0)


main()
