#!/usr/bin/env python3
"""Verify every source citation in notes/conditional.md against the shipped files.

Report-only; writes nothing. Two passes:

1. Fenced code blocks. Each block is attributed to the nearest `path:line` anchor that
   precedes it, and every block line must match that file at consecutive line numbers.
2. Prose quotations in *"..."* form. Each is attributed to the nearest `path:line` anchor
   that precedes it and must occur on that file. Whitespace runs are collapsed on both
   sides before comparing: line-wrapping in the page is markup, not part of the quote.

A block with no preceding anchor, a block line that does not match, and a prose quotation
that is not found are problems (exit 1). Prose quotations with no anchor at all are
counted and reported separately as a known gap, not as a failure — the pre-existing
per-family sections quote catalog abstracts without line anchors.
"""
import re
import sys

from catlib import anchors
from catlib.paths import NOTES, ROOT
from catlib.text import collapse_ws

PAGE = NOTES / "conditional.md"

ANCHOR = anchors.anchor_pattern(anchors.EXT_LEAN)
QUOTE = re.compile(r'\*"([^"|]{12,})"\*')
# `quoted source text` at/(`) `path:line`  — the page's inline citation form
INLINE = re.compile(
    r"`([^`\n]{12,})`\s*(?:at|in)\s*`([\w./+-]+\.(?:lean|md|yaml)):(\d+)`"
    r"|`([^`\n]{12,})`\s*\(`([\w./+-]+\.(?:lean|md|yaml)):(\d+)`\)")

norm = collapse_ws


def check(text):
    """-> (problems, unanchored, measured)"""
    lines = text.split("\n")
    problems = []
    unanchored = 0
    n_blocks = n_lines = n_prose = n_inline = 0

    for start, body in anchors.fenced_blocks(lines):
        found = anchors.nearest_anchor(lines, start, ANCHOR)
        if found is None:
            problems.append(f"page:{start + 1}: fenced block has no preceding file:line anchor")
            continue
        rel, at = found[0], int(found[1])
        f = ROOT / rel
        if not f.exists():
            problems.append(f"page:{start + 1}: anchor file {rel} does not exist")
            continue
        src = f.read_text(encoding="utf-8", errors="replace").split("\n")
        n_blocks += 1
        for i, want in enumerate(body):
            got = src[at - 1 + i] if at - 1 + i < len(src) else "<past end of file>"
            n_lines += 1
            if got != want:
                problems.append(
                    f"page:{start + 2}: block line {i} != {rel}:{at + i}\n"
                    f"    want {want!r}\n    got  {got!r}")

    for m in QUOTE.finditer(text):
        quote = norm(m.group(1))
        upto = text[: m.start()].split("\n")
        found = anchors.nearest_anchor(upto, len(upto), ANCHOR)
        if found is None:
            unanchored += 1
            continue
        rel, at = found[0], int(found[1])
        f = ROOT / rel
        if not f.exists():
            problems.append(f"prose anchor file {rel} does not exist")
            continue
        src = norm(f.read_text(encoding="utf-8", errors="replace"))
        n_prose += 1
        if quote not in src:
            problems.append(f"prose quote not found in {rel}: {quote[:70]!r}")

    for m in INLINE.finditer(text):
        span, rel, at = (m.group(1), m.group(2), m.group(3)) if m.group(1) \
            else (m.group(4), m.group(5), m.group(6))
        f = ROOT / rel
        if not f.exists():
            problems.append(f"inline anchor file {rel} does not exist (citing {span[:50]!r})")
            continue
        src = norm(f.read_text(encoding="utf-8", errors="replace"))
        n_inline += 1
        if norm(span) not in src:
            problems.append(f"inline citation not found in {rel}:{at}: {span[:70]!r}")

    return problems, unanchored, (n_blocks, n_lines, n_prose, n_inline)


MUTANTS = {
    "block anchor shifted by one": lambda t: t.replace(
        "`lean/OAI/ModelTheory/Categoricity/Main.lean:233`",
        "`lean/OAI/ModelTheory/Categoricity/Main.lean:234`", 1),
    "anchor file renamed": lambda t: t.replace(
        "`lean/OAI/ModelTheory/Categoricity/Model.lean:101`",
        "`lean/OAI/ModelTheory/Categoricity/Mode.lean:101`", 1),
    "prose quote altered": lambda t: t.replace(
        "and failure of the Axiom of Choice.", "and failure of Choice.", 1),
    "block line altered": lambda t: t.replace(
        "theorem main (hCH : CH.{u}) :", "theorem main (hCH : CH) :", 1),
    "block anchor dropped": lambda t: t.replace(
        "exists only as a challenge stub, `lean/ComparatorChallenges/PartitionConsistency.lean:318`:",
        "exists only as a challenge stub:", 1),
}


def main():
    text = PAGE.read_text(encoding="utf-8", errors="replace")

    if "--mutant" in sys.argv:
        uncaught = []
        for name, fn in MUTANTS.items():
            mutated = fn(text)
            if mutated == text:
                print(f"mutant target absent: {name}")
                uncaught.append(name)
                continue
            problems, _, _ = check(mutated)
            print(f"mutant {name}: {'caught' if problems else 'NOT CAUGHT'}"
                  f" ({len(problems)} problems)")
            if not problems:
                uncaught.append(name)
        print(f"mutants not caught {len(uncaught)} of {len(MUTANTS)}")
        raise SystemExit(1 if uncaught else 0)

    problems, unanchored, (n_blocks, n_lines, n_prose, n_inline) = check(text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"\nblocks {n_blocks}  block lines {n_lines}  anchored prose quotes {n_prose}"
          f"  inline citations {n_inline}  unanchored prose quotes {unanchored}"
          f"  problems {len(problems)}")
    raise SystemExit(1 if problems else 0)


main()
