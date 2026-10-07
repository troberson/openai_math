#!/usr/bin/env python3
"""Re-measure the Scope sections of the 235 scope notes. Writes nothing; prints the report.

Every count in notes/scope-exclusions.md comes from this run, so the page's numbers are checkable
against a command. The point of the two vocabulary lists is the floor: the narrow list reproduces
the 5-of-235 figure the earlier reading pass recorded, and the broad list shows how much a wider
rule finds. Both are keyword floors over prose, not censuses - the exclusions themselves are the
product of reading all 235 sections.

Definitions, stated so the counts are reproducible:
  scope section  - from the `## Scope` heading line through the line before the next `## ` heading.
  scope lines    - lines in that span, heading and trailing blank included.
  hit            - a phrase occurring case-insensitively in the section text.

Usage: python3 notes/scripts/extract_scope_notes.py
"""
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "lean" / "docs"

# The five phrases the earlier reading pass recorded, verbatim.
NARROW = ["not formalized", "excluded", "out of scope", "does not cover", "not covered"]

# A deliberately wide stem list, built to find exclusion vocabulary rather than to name a shape.
BROAD = [
    "not included", "not included in the scope", "not in scope", "out of scope",
    "not part of", "no explicit", "omitted", "not treated", "not addressed",
    "not proved", "not established", "not discussed", "not modelled", "not modeled",
    "not formalised", "not formalized", "excludes", "excluded", "exclusion", "exclude",
    "does not cover", "not covered", "not asserted", "not supplied",
]


def scope_section(lines):
    """(first, last) 1-based line numbers of the `## Scope` section, or None."""
    start = next((i for i, ln in enumerate(lines) if ln.strip() == "## Scope"), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))
    return start + 1, end


def main():
    docs = sorted(DOCS.glob("*.md"))
    sections = {}
    for path in docs:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        span = scope_section(lines)
        if span is None:
            print(f"{path.name}: no `## Scope` heading")
            continue
        first, last = span
        sections[path.stem] = (first, last, lines[first - 1:last])

    counts = [last - first + 1 for first, last, _ in sections.values()]
    print(f"scope notes: {len(sections)} of {len(docs)} docs")
    print(f"docs with a `## Comparator links` section: "
          f"{sum(1 for p in docs if '## Comparator links' in p.read_text(encoding='utf-8', errors='replace'))}")
    print(f"scope section lines total: {sum(counts)}")
    print(f"doc lines total: {sum(len(p.read_text(encoding='utf-8', errors='replace').splitlines()) for p in docs)}")
    print(f"scope lines per doc: min {min(counts)}, median {statistics.median(counts)}, "
          f"max {max(counts)}, mean {sum(counts) / len(counts):.2f}")

    for name, phrases in (("narrow", NARROW), ("broad", BROAD)):
        per_phrase = {}
        hits = []
        for stem, (_, _, sec) in sections.items():
            text = " ".join(sec).lower()
            found = [p for p in phrases if p in text]
            for p in found:
                per_phrase.setdefault(p, []).append(stem)
            if found:
                hits.append(stem)
        print(f"{name} list: {len(phrases)} phrases, {len(hits)} of {len(sections)} docs hit")
        print(f"{name} docs: {' '.join(hits)}")
        zero = [p for p in phrases if p not in per_phrase]
        print(f"{name} phrases with zero hits: {len(zero)}{' (' + ' '.join(zero) + ')' if zero else ''}")
        for p in phrases:
            print(f"  {p}: {len(per_phrase.get(p, []))}")

    print()
    print("Not checked: whether a section states an exclusion without using any of this vocabulary.")
    print("That is what the reading pass in notes/scope-exclusions.md is for; these counts are floors.")


if __name__ == "__main__":
    main()
