"""The generated split table: which page breaks which slotted phrase, and where.

Written by `build_report_templates.py` from the page's own bytes at HEAD, read here. The split point
is irreducible information — a measured phrase is one string, and the page breaks it at a particular
place — so it has to be recorded somewhere. What changes is who records it: this table is generated
from the page, not transcribed by hand, and the writer's label dict carries one value per phrase
instead of one per part.

The table exists because the render cannot know where the page broke a phrase: it never reads HEAD.
The template names its parts (`p['label a']`, `p['label b']`), and the render fills those names by
splitting the measured value at the recorded boundaries.

`catlib/templates.py` cannot import this module — the registry imports the writer, and the writer
imports this package module, so a back-import would close the cycle the deferred-import rule exists to
keep open.

Columns: `page`, `label`, `part`. One row per part, in the page's own order, for a label the page
breaks. A label the page does not break has no row: it is one slot, and the boundary is not a fact
about it.
"""
from __future__ import annotations

from functools import cache

from catlib.paths import SPLIT_TSV
from catlib.text import apply_split
from catlib.tsv import read_rows

COLS = ("page", "label", "part")


@cache
def table() -> list[dict[str, str]]:
    """The recorded rows, in the order the writer wrote them: page order, then part order."""
    return read_rows(SPLIT_TSV)


def parts(page: str, label: str) -> list[str]:
    """The recorded parts for one label, in the page's own order. Empty when the page does not break it."""
    return [r["part"] for r in table() if r["page"] == page and r["label"] == label]


def expand(page: str, labels: dict[str, str]) -> dict[str, str]:
    """The slot dict the template gets: one entry per label, split where the page breaks it.

    A label the page does not break is one slot. A label the page breaks is split at the recorded
    boundaries, and each part is the measured span, not the recorded part — the recorded part carries
    HEAD's number, so a drifted count must still land in its own slot.
    """
    out: dict[str, str] = {}
    for lab, val in labels.items():
        pre = parts(page, lab)
        if pre:
            out.update(apply_split(lab, val, pre))
        else:
            out[lab] = val
    return out
