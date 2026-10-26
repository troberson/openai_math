r"""The quote locator: resolve a (path, start, end, head, tail) spec to the verbatim source span.

A spec names a span WITHOUT containing it: the source file, the line window, the first words of the
quote widened until they are unique inside that window, and the last three words. The resolver joins
the window's lines the way a LaTeX paragraph does -- a line break is a space, and a line's trailing
space is not a second one -- bounds the span between head and tail, and returns the bytes between
them. The page's quote is verbatim source text, so the resolver's output is the page's quote, byte for
byte.

**The page grammar is shared with `catlib.anchors`.** `ANCH` is `anchor_pattern(EXT_MAN, ranges=True)`,
the grammar `notes/gen/reports/named-results.md` and `notes/gen/reports/t0-chains.md` ship, so a seeder that reads a page's
anchors uses the same rule the page's checker uses: a page whose anchor grammar narrows fails the seeder
the way it fails the checker. `nearest_anchor` is the block-quote attribution for a page that cites by
an anchor; `catlib.summaries.candidates` is the same idea for a page that cites by a `[Sn:line]` marker.

**Page breaks inside a quote are the common case, not the edge.** Measured 2026-10-13 over the 23
summaries pages, with the checker's own span and attribution rules (`catlib.summaries.spans_of` and
`candidates`): of the **1038** quoted spans of 12 characters or more that `verify_summaries.py` pass C
checks, **335** sit in one source line and **688** sit across 2 to 26 lines. A spec that names a single
line cannot carry them, so the spec names a window and the resolver joins it.

**Locate on raw bytes, never on the folded line.** `catlib.text.strip_markup` is the verification
normalizer and it is lossy on math: `overview.tex:505` carries
`for $0<q\le4$ and to the Brownian continuum random tree for $q>4$`, and folding turns `\le` into a
space, which leaves a `<` and a `>` with text between them -- the HTML-tag rule then deletes that text,
so the folded line reads `for $04$, establishing` and the clause is gone. Measured 2026-10-12 over the
236 quotes of `notes/gen/reports/subfinding-pairs.md`: locating in the folded line reproduced 232 of 236 and failed
to find 2 heads; locating in the raw line reproduced 236 of 236 and found every head.

The word pattern tolerates markup **inside** a word and **between** words, because the source writes
what the page drops: `**Date:** September` reads `Date: September`; `$1/9$~\cite{X}.` reads `$1/9$.`;
`prime-to-<i>p</i>` reads `prime-to-p`. Between words the pattern requires at least one whitespace, so
words cannot glue. The tolerance is a locator, not a normalizer: the span it returns is raw bytes, and
the round-trip test is byte equality with the page's quote.
"""
from __future__ import annotations

import re

from catlib.anchors import EXT_MAN, anchor_pattern
from catlib.summaries import FORMAT_EXAMPLE, PRIOR, Page, candidates, spans_of, units
from catlib.text import collapse_ws, strip_markup

MIN_BOUND = 3

# The page's anchor grammar, shared with the page checkers through catlib.anchors.
ANCH = anchor_pattern(EXT_MAN, ranges=True)

# Markup the source can write where the page writes none: a tag, a LaTeX command, a command with an
# argument, a tie, braces, and the page's own emphasis markers.
MARK = r"(?:\\[a-zA-Z@]+\{[^}]*\}|\\[a-zA-Z@]+|~|[{}]|[*`]|<[a-zA-Z/][^>]*>)*"

# Between words: the same markup, and at least one whitespace so words cannot glue.
SEP = MARK + r"\s+" + MARK


def word_pat(w: str) -> str:
    """A word as the source may write it: its characters, with markup allowed between each pair."""
    w = w.replace("*", "").replace("`", "")
    return MARK.join(re.escape(c) for c in w)


def head_pat(words: list[str]) -> str:
    """A word sequence as a pattern: words separated by markup-and-whitespace."""
    return SEP.join(word_pat(w) for w in words)


def join_window(lines: list[str], start: int, end: int) -> str:
    r"""Lines `start..end` (1-based, inclusive) joined as one paragraph.

    A LaTeX line break is a space. A line's own trailing space is not a second one: strip before
    joining, so a line ending `\qquad ` and a line starting `p` join to `\qquad p`, not `\qquad  p`.
    """
    return collapse_ws(" ".join(x.strip() for x in lines[start - 1:end]))


def bounded(text: str, head: str, tail: str | None) -> str | None:
    """The shortest span in `text` bounded by head then tail, or None when they do not occur in order.

    `tail` None means the span is the head itself. A head that occurs more than once is resolved to the
    occurrence whose span is shortest, which is the reading that keeps head and tail adjacent.
    """
    starts = list(re.finditer(head_pat(head.split()), text))
    if not starts:
        return None
    if tail is None:
        m = starts[0]
        return text[m.start():m.end()]
    best: tuple[int, int] | None = None
    best_len = 0
    for m in starts:
        j = re.search(head_pat(tail.split()), text[m.end():])
        if not j:
            continue
        span = (m.start(), m.end() + j.end())
        # `best_len` carries the length so the comparison never subscripts an Optional, which is what
        # pylint reports as E1136 on `best[1] - best[0]` behind a `best is None` guard.
        if best is None or span[1] - span[0] < best_len:
            best, best_len = span, span[1] - span[0]
    return text[best[0]:best[1]] if best else None


def resolve(lines: list[str], start: int, end: int, head: str, tail: str | None) -> str | None:
    """The verbatim source span the spec names, or None when the spec does not resolve.

    `lines` is the source file split into lines; `start` and `end` are 1-based and inclusive.
    """
    if start < 1 or start > end or end > len(lines):
        return None
    return bounded(join_window(lines, start, end), head, tail)


def seed(lines: list[str], quote: str, start: int, end: int) -> tuple[int, int, str, str | None] | None:
    """The locator for `quote` in the window: (start, end, head, tail), or None if it is not there.

    The window is found in ONE pass: the cited range is joined and the quote's word pattern is searched
    once, then the match offsets are mapped back to the lines they cover. A width-by-width scan over a
    bare marker's whole file is O(lines x width) regexes per quote, and this pattern is heavy -- it
    measured 300 s over the 21 summaries pages. The head is widened word by word, and a head is accepted
    only when the span it bounds with the tail is exactly the quote -- a head that is unique in the line
    can still bound a span that runs to a later occurrence of the tail, which is how family 262's title
    resolved to the whole `\resultentry` field. The head never overlaps the tail, so the head width is
    capped at `len(words) - MIN_BOUND`. A quote of six words or fewer has no boundary: the whole quote
    is the head.
    """
    words = quote.split()
    lo, hi = max(start, 1), min(end, len(lines))
    parts = [x.strip() for x in lines[lo - 1:hi]]
    pos: list[int] = []
    acc = 0
    for p in parts:
        pos.append(acc)
        acc += len(p) + 1
    blob = " ".join(parts)
    m = re.search(head_pat(words), blob)
    if not m:
        return None
    i, j = lo, lo
    for k, off in enumerate(pos):
        if off <= m.start():
            i = lo + k
        if off <= m.end() - 1:
            j = lo + k
    window = join_window(lines, i, j)
    if len(words) <= 2 * MIN_BOUND:
        return i, j, " ".join(words), None
    tail = " ".join(words[-MIN_BOUND:])
    for n in range(MIN_BOUND, len(words) - MIN_BOUND + 1):
        head = " ".join(words[:n])
        if bounded(window, head, tail) == quote:
            return i, j, head, tail
    return i, j, " ".join(words), None


def folded(lines: list[str], start: int, end: int, head: str, tail: str | None) -> str | None:
    """The span the spec names, normalized by the checker's rule. The page's quote is verbatim, so
    `resolve` is the comparison; this is the form for a quote the page wrote with markup dropped."""
    span = resolve(lines, start, end, head, tail)
    return strip_markup(span) if span is not None else None


def seed_page(page: Page) -> list[tuple[str, str, str, int, int, str, str | None, str]]:
    """Every quoted span a summaries page carries, seeded to a spec, in page order.

    Yields `(sid, which, span, start, end, head, tail, mode)` per span. `sid` is the Sources-table row
    the span is attributed to by `catlib.summaries.candidates` — the block-quote rule walks back from the
    quote to the citation on the line above it, so a block quote is seeded against the file its marker
    names, not against the page. The window is the cited range the marker names: a summaries marker
    cites lines, so the spec names those lines and no widening is needed. `which` is `block` for a block
    quote and `inline` for a prose quotation. `mode` is the round-trip class: `raw` when the resolved
    span is the page's quote byte-for-byte, `folded` when it is equal only after the checker's
    normalizer (the page dropped markup the source carries), and `none` when the cited file does not
    carry the span.
    """
    out: list[tuple[str, str, str, int, int, str, str | None, str]] = []
    for start_line, unit, is_bq in units(page.lines):
        if not is_bq and (PRIOR in unit or FORMAT_EXAMPLE in unit):
            continue
        cands = candidates(page, unit, start_line, is_bq)
        which = "block" if is_bq else "inline"
        for span in spans_of(unit, is_bq):
            hit = None
            for sid, a, b in cands:
                src = page.lines_of(sid)
                got = seed(src, span, a or 1, b or len(src))
                if got:
                    hit = (sid, src, got)
                    break
            if hit is None:
                out.append((cands[0][0] if cands else "", which, span, 0, 0, "", None, "none"))
                continue
            sid, src, (s, e, head, tail) = hit
            r = resolve(src, s, e, head, tail)
            if r == span:
                mode = "raw"
            elif r is not None and strip_markup(r) == strip_markup(span):
                mode = "folded"
            else:
                mode = "none"
            out.append((sid, which, span, s, e, head, tail, mode))
    return out


def spec_lines(path: str, start: int, end: int, head: str, tail: str | None) -> str:
    """The spec as a page writes an anchor: `path:start-end` plus the boundary words."""
    span = f"{path}:{start}" if start == end else f"{path}:{start}-{end}"
    return f"`{span}` " + (f"{head} … {tail}" if tail else head)
