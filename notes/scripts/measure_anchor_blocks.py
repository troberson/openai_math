#!/usr/bin/env python3
"""Find every fenced block and every quotation in a notes page attributed to a notes/ page anchor.

The checkers attribute a fenced block to the nearest preceding anchor within a window and compare the
block's lines against that file. If the anchor names a notes/ page, moving that page means the block
and its anchor must change together. The same is true of a `*"…"*` quotation pinned to a notes/ page
anchor. This probe finds both, so a directory move can be priced before it happens and re-checked
after it.

The anchor set is the **moved** surface only — `notes/<page>.md|tsv`, `notes/reports/…`,
`notes/development/…`, `notes/tables/…`. A pattern that allows `/` freely in the body matches anchors
naming directories the reorg leaves in place (`notes/index/README.md:12`), which would read as an
attributed block that no move touches. Recorded baseline: 0 attributed blocks, 4 quotation lines in
`t0-chains.md` and 1 in `summaries-workflow.md` = 5 anchored citations.

Scope is the 30 pages the reorg moves: the top-level `notes/*.md`, plus `notes/reports/*.md` and
`notes/development/*.md` once those directories exist. Report-only: writes nothing.
"""

from __future__ import annotations

import re
from pathlib import Path

from catlib import anchors
from catlib.paths import ROOT

PAT = anchors.anchor_pattern(("md", "tsv", "py", "tex", "json", "yaml", "lean", "txt", "bib"))
MOVED = re.compile(r"notes/(?:(?:reports|development|tables)/)?[A-Za-z0-9._+-]*\.(?:md|tsv)")
ANCHORED = re.compile(r"notes/(?:(?:reports|development|tables)/)?[A-Za-z0-9._+-]*\.(?:md|tsv):\d+")


def pages() -> list[Path]:
    notes = ROOT / "notes"
    dirs = [notes, notes / "reports", notes / "development"]
    return sorted(p for d in dirs for p in d.glob("*.md"))


def pfx(page: Path) -> str:
    return page.relative_to(ROOT / "notes").as_posix()


def main() -> int:
    blocks = []
    quotes = []
    for page in pages():
        lines = page.read_text(encoding="utf-8").splitlines()
        for i, body in anchors.fenced_blocks(lines):
            a = anchors.nearest_anchor(lines, i, PAT)
            if a and MOVED.match(a[0]):
                blocks.append((pfx(page), i + 1, a[0], a[1], len(body)))
        for n, line in enumerate(lines):
            for m in ANCHORED.finditer(line):
                if "*" in line:
                    quotes.append((pfx(page), n + 1, m.group(0)))

    print(f"fenced blocks attributed to a notes/ page anchor: {len(blocks)}")
    for b in blocks:
        print("  ", b)
    print(f"lines with a notes/ page anchor and a quotation: {len(quotes)}")
    for q in quotes:
        print("  ", q)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
