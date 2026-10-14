#!/usr/bin/env python3
r"""The layout probe's two moves, shared by the self-test suite.

`shift` inserts two lines after a page's first `## ` heading — a layout change that moves every
line number below it and changes no measured count. `reorder` swaps two data rows, the analogue
for a table, where an insert would change a count. Both are inert unless `LAYOUT_SHIFT` is set in
the environment, so the suite runs the committed page by default and the shifted page when the
probe is invoked: `LAYOUT_SHIFT=1 python3 notes/scripts/run_tests.py notes/scripts/tests -q`.
"""
from __future__ import annotations

import os


def shift(text):
    """Two lines inserted after the page's first `## ` heading."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("## "):
            return "".join(lines[:i + 1]) + "<!-- band shift -->\n\n" + "".join(lines[i + 1:])
    return text


def reorder(rows):
    """Swap two data rows — the layout analogue for a table. The counts the passes report are
    order-independent, so a needle that keys on a row's content survives the swap and one that
    keys on its position does not."""
    if os.environ.get("LAYOUT_SHIFT") and len(rows) > 2:
        rows[1], rows[2] = rows[2], rows[1]
    return rows
