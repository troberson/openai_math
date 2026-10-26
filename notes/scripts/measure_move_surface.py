#!/usr/bin/env python3
"""Classify every notes/ path mention in the notes pages by context, and split the surface the
reorg moves from the surface it does not.

Contexts: fenced block, blockquote, *"…"* prose quotation, inline code span, markdown link, plain
prose. A mention inside a fenced block, a blockquote, a quotation, or a checked code span is text a
checker compares verbatim against the file its anchor names, so moving the target means the quote and
the source must change together. The point is to price a directory move, and the reorg re-runs this
after each pass.

Two patterns, because one pattern cannot be comparable across the move. A single pattern that allows
`/` reads 350 mentions over the 29 pages after the move, 25 of them naming locations the reorg leaves
in place (`notes/scripts/README.md`, `notes/gen/tables/names.tsv`, `notes/development/upstream_history/…`).
A single pattern that forbids `/` reads 282 before the move and 305 after. So the probe prints three
counts:

- **moved, top level** — `notes/<page>.md|tsv`: 282 before the move, 0 after;
- **moved, in the new directories** — `notes/gen/reports/…`, `notes/development/…`, `notes/gen/tables/…`:
  0 before, 305 after. The two moved counts must agree; that is the comparability test;
- **stable** — mentions under `scripts/`, `index/`, `summaries/`, `development/probe/`,
  `development/upstream_history/`, plus `notes/README.md` and the six paths the sweep records as
  deleted or pre-move: 17 before `.3`, 25 after the move, 28 after `math-faz.5` rewrote the entry
  point. The constraint is that a *move* pass must not change it; a content pass that names a stable
  page in prose does change it, and the sweep records the new figure rather than the old one. The two
  `development/` buckets are directories the reorg moved *into*, so a mention naming them is
  stable, not moved: `MOVED_NEW` requires a filename directly after `development/`, and the probe
  records are `.txt`. `notes/README.md` is the entry point the reorg leaves at the top level, so a
  mention naming it is stable too, and `MOVED_TOP` excludes it — without the exclusion the
  comparability test reads the entry point's own 103 mentions as moved. The six historical names are
  excluded for the same reason: a mention of `notes/linting.md` is a record of a deletion, and a
  pass that moves pages cannot move it.

Scope is the 29 pages the reorg moved: the top-level `notes/*.md`, plus `notes/gen/reports/*.md` and
`notes/development/*.md` once those directories exist. Report-only: writes nothing.
"""

from __future__ import annotations

import re
from pathlib import Path

from catlib import anchors
from catlib.paths import ROOT

# Paths the sweep records as deleted or pre-move. A mention naming one is a dated observation, not
# part of the surface a pass moves, so it is stable: `notes/linting.md` is the deleted page,
# `notes/summaries-blocked.md` was never created, and the four TSV names are the pre-`math-ckd.2`
# paths the fleet pages record.
HISTORICAL = ("notes/catalog.tsv", "notes/.sources.tsv", "notes/.links.tsv",
              "notes/named-results.tsv", "notes/linting.md", "notes/summaries-blocked.md")
MOVED_TOP = re.compile(r"notes/(?!README\.md|" + "|".join(h[len("notes/"):].replace(".", r"\.")
                                                          for h in HISTORICAL) +
                       r")[A-Za-z0-9._+-]*\.(?:md|tsv)")
MOVED_NEW = re.compile(r"notes/(?:reports|development|tables)/[A-Za-z0-9._+-]*\.(?:md|tsv)")
STABLE = re.compile(r"notes/(?:scripts|index|summaries|development/probe|development/upstream_history)"
                    r"/[A-Za-z0-9._+/-]*\.(?:md|tsv)|notes/README\.md|"
                    + "|".join(re.escape(h) for h in HISTORICAL))
ANCHORED = re.compile(r"notes/(?:(?:reports|development|tables)/)?[A-Za-z0-9._+-]*\.(?:md|tsv):\d+")
QUOTE = re.compile(r'\*[^*]*["“][^"”]*["”][^*]*\*')
SPAN = re.compile(r"`[^`\n]+`")
LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")

CONTEXTS = ("fenced", "blockquote", "quote", "span", "link", "prose")
PATTERNS = ("moved_top", "moved_new", "stable")


def pages() -> list[Path]:
    notes = ROOT / "notes"
    dirs = [notes, notes / "reports", notes / "development"]
    return sorted(p for d in dirs for p in d.glob("*.md"))


def fence_ranges(lines: list[str]) -> list[tuple[int, int]]:
    """(start, end) line indices covered by each ``` block, body inclusive."""
    return [(i, i + len(body)) for i, body in anchors.fenced_blocks(lines)]


def classify(page: Path) -> tuple[dict[tuple[str, str], int], int, int]:
    lines = page.read_text(encoding="utf-8").splitlines()
    ranges = fence_ranges(lines)
    counts = {(pat, ctx): 0 for pat in PATTERNS for ctx in CONTEXTS}
    anchored = 0
    for n, line in enumerate(lines):
        for pat, rx in (("moved_top", MOVED_TOP), ("moved_new", MOVED_NEW), ("stable", STABLE)):
            for m in rx.finditer(line):
                if pat != "stable" and ANCHORED.match(line, m.start()) is not None:
                    anchored += 1
                if any(a <= n <= b for a, b in ranges):
                    ctx = "fenced"
                elif line.lstrip().startswith(">"):
                    ctx = "blockquote"
                elif QUOTE.search(line):
                    ctx = "quote"
                elif SPAN.search(line):
                    ctx = "span"
                elif LINK.search(line):
                    ctx = "link"
                else:
                    ctx = "prose"
                counts[(pat, ctx)] += 1
    return counts, anchored, len(lines)


def main() -> int:
    total = {(pat, ctx): 0 for pat in PATTERNS for ctx in CONTEXTS}
    rows = []
    for p in pages():
        c, a, n = classify(p)
        moved = sum(v for (pat, _), v in c.items() if pat != "stable")
        stable = sum(v for (pat, _), v in c.items() if pat == "stable")
        rows.append((p.relative_to(ROOT / "notes").as_posix(), n, moved, stable, a))
        for key, v in c.items():
            total[key] += v

    for pat in PATTERNS:
        per = {ctx: total[(pat, ctx)] for ctx in CONTEXTS}
        print(f"{pat:10} mentions {sum(per.values()):4}  anchored-eligible "
              f"{'yes' if pat != 'stable' else 'no'}")
        for ctx, v in sorted(per.items(), key=lambda kv: -kv[1]):
            if v:
                print(f"    {ctx:11} {v}")
    top = sum(v for (pat, _), v in total.items() if pat == "moved_top")
    new = sum(v for (pat, _), v in total.items() if pat == "moved_new")
    stable = sum(v for (pat, _), v in total.items() if pat == "stable")
    print(f"\nmoved surface: top-level {top} + new-dirs {new} = {top + new}")
    print(f"stable surface: {stable} (must not change across a pass)")
    print(f"pages {len(rows)}  anchored citations {sum(r[4] for r in rows)}")
    print("\nper page (moved, stable, anchored):")
    for name, n, moved, stable, a in rows:
        if moved or stable:
            print(f"  {name:38} lines {n:5}  moved {moved:4}  stable {stable:3}  anchored {a:3}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
