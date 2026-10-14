"""The self-tests for `notes/scripts/verify_summaries.py`.

Each test injects one corruption into a real summary page in memory and asserts the pass that owns it
prints its problem: the quote-fidelity pass (an inline quotation corrupted one token deeper than the
source, a quotation wrapped across lines, a block-quote attribution corrupted, a fabricated quotation
attached to a line that already carries a citation), the supersession pass (the page's declared
manuscript root retargeted to a directory that is on disk, tracked, and named by no family), and the
locator pass (a bare line citation moved to the line just above the family's own block). The last two
are the mutants that only those passes can see: Pass B stays green on a superseded retarget because
the path resolves and the files exist, and Pass C has nothing to compare on a moved locator because
the marker still resolves to a line that is in range, non-blank, and in the right file.

Every mutant is built from a real span, a real path, and a real marker of a real page, so a checker
that only re-reads its own regexes cannot pass. Each test asserts the injected text differs from the
page it started from. The clean test asserts every page on disk is silent on all four passes, as a
**resolution invariant with a non-vacuity floor**: the page set is the tree, required non-empty, and
each page must carry markers, so 0 problems means every marker in that page resolved — a page with no
markers reports 0 problems and proves nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_summaries.py -q
"""
import contextlib
import io
import re

import pytest
from catlib.anchors import range_facts
from catlib.paths import SUMMARIES_DIR, read_text
from catlib.summaries import (
    MARKER,
    PAPDIR,
    PRIOR,
    QUOTE,
    Page,
    candidates,
    superseded_dir,
    units,
)
from catlib.text import strip_markup

pytestmark = pytest.mark.mutant

FABRICATED = "the formalization is complete and machine-checked"


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_summaries")


@pytest.fixture(scope="module")
def pages():
    return [Page(p, read_text(p).splitlines()) for p in sorted(SUMMARIES_DIR.rglob("*.md"))]


def printed(page, fn):
    """The problems a pass prints for a candidate page. The passes print, they do not return text."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(page)
    return buf.getvalue()


def inject(text, start, end, span):
    """Splice the marker token into the middle of a quotation, at a word boundary."""
    cut = span.rfind(" ", 0, len(span) // 2) + 1
    if cut <= 0:
        cut = span.find(" ", len(span) // 2) + 1
    if cut <= 0:
        return None
    return text[:start] + span[:cut] + "XYZZY " + span[cut:] + text[end:]


def inline_targets(text):
    """Inline quotations the mutant can be built from, split by whether the span is wrapped across
    source lines. The checker takes the first of each form per page; the tests mirror that."""
    single: list = []
    wrapped: list = []
    for m in QUOTE.finditer(text):
        span = m.group(1) or m.group(2)
        if len(span) < 12 or PRIOR in span:
            continue
        (wrapped if "\n" in span else single).append(m)
    return single, wrapped


def blockquote_targets(page):
    """Block-quote units Pass C checks, i.e. those with a citation on a line above them. The
    attribution is the package's `candidates` rule, the same one pass C runs."""
    out = []
    for start_line, unit, is_blockquote in units(page.lines):
        if not is_blockquote or len(unit) < 12:
            continue
        if candidates(page, unit, start_line, True):
            out.append((start_line, unit))
    return out


def test_clean_pages(mod, pages):
    """Every pass is silent on every page, and the marker pass is pinned as a resolution invariant with
    a non-vacuity floor: each page must carry markers, so 0 problems means every marker in that page
    resolved. A page with no markers reports 0 problems and proves nothing, so the floor is the witness
    that the pass ran. The page count is a floor, not a recorded number: the tree is the population."""
    assert len(pages) > 0, "no summary pages on disk, so every pass is vacuous"
    for page in pages:
        positions, _sources, _links, problems = mod.pass_b(page)
        _spans, misses = mod.pass_c(page)
        # The tree's index page is link-only, so the checker skips pass D and pass E for it; the clean
        # test mirrors that selection.
        if page.path.name == "README.md":
            continue
        assert positions > 0, f"{page.path.name}: pass B resolved 0 markers, so it checked nothing"
        _dirs, stale = mod.pass_d(page)
        _cites, outside = mod.pass_e(page)
        assert problems == 0, f"{page.path.name}: pass B reports {problems} problems"
        assert misses == 0, f"{page.path.name}: pass C reports {misses} non-verbatim spans"
        assert stale == 0, f"{page.path.name}: pass D reports {stale} superseded or off-family"
        assert outside == 0, f"{page.path.name}: pass E reports {outside} outside the family block"


def test_inline_quotation_corrupted(mod, pages):
    """A real quotation, one token deeper than the source, in the form a page quotes inline. The
    checker takes the first inline target on each page, so the test mirrors that and asserts the pass
    flags the page. A span with no word boundary cannot be spliced, so that page is skipped, as the
    checker skips it."""
    hits = 0
    for page in pages:
        text = "\n".join(page.lines)
        targets = inline_targets(text)[0]
        if not targets:
            continue
        m = targets[0]
        g = 1 if m.group(1) else 2
        bad = inject(text, m.start(g), m.end(g), m.group(g))
        if bad is None:
            continue
        assert bad != text, "the injection did not change the page"
        out = printed(Page(page.path, bad.splitlines()), mod.pass_c)
        assert "NOT VERBATIM" in out or "NO CITATION" in out, \
            f"{page.path.name}: a corrupted inline quotation left the pass silent"
        hits += 1
    assert hits > 0, "no page carries an injectable inline quotation"


def test_wrapped_inline_quotation_corrupted(mod, pages):
    """The same corruption in a span the page wraps across source lines."""
    hits = 0
    for page in pages:
        text = "\n".join(page.lines)
        targets = inline_targets(text)[1]
        if not targets:
            continue
        m = targets[0]
        g = 1 if m.group(1) else 2
        bad = inject(text, m.start(g), m.end(g), m.group(g))
        if bad is None:
            continue
        assert bad != text, "the injection did not change the page"
        out = printed(Page(page.path, bad.splitlines()), mod.pass_c)
        assert "NOT VERBATIM" in out or "NO CITATION" in out, \
            f"{page.path.name}: a corrupted wrapped quotation left the pass silent"
        hits += 1
    assert hits > 0, "no page carries an injectable quotation wrapped across lines"


def test_block_quote_attribution_corrupted(mod, pages):
    """A block quote is attributed by the citation on the line above it, so the corruption is the
    attributed unit itself. The checker takes the first such unit per page; the test mirrors that."""
    hits = 0
    for page in pages:
        targets = blockquote_targets(page)[:1]
        if not targets:
            continue
        start_line, _unit = targets[0]
        line = page.lines[start_line - 1]
        bad_line = inject(line, 0, len(line), line)
        assert bad_line is not None and bad_line != line, "the block-quote line is not injectable"
        lines = list(page.lines)
        lines[start_line - 1] = bad_line
        out = printed(Page(page.path, lines), mod.pass_c)
        assert "NOT VERBATIM" in out or "NO CITATION" in out, \
            f"{page.path.name}: a corrupted block-quote attribution left the pass silent"
        hits += 1
    assert hits > 0, "no page carries a block quote with a citation above it"


def test_fabricated_quotation(mod, pages):
    """A quotation attached to a line that already carries a citation: the marker resolves, the text
    is not in the file it cites."""
    hits = 0
    for page in pages:
        lines = list(page.lines)
        for i, line in enumerate(lines):
            m = MARKER.search(line)
            if m and not line.startswith(("#", "|", ">")):
                lines[i] = line + f" “{FABRICATED}” [{m.group(0)}]"
                assert lines != page.lines, "the fabricated quotation did not change the page"
                assert "NOT VERBATIM" in printed(Page(page.path, lines), mod.pass_c), \
                    f"{page.path.name}: a fabricated quotation was not checked against its cited lines"
                hits += 1
                break
    assert hits > 0, "no page carries a citable prose line"


def test_superseded_retarget(mod, pages):
    """The page's declared manuscript root moved to a superseded sibling. Pass B stays green — the
    path resolves and the files exist — so only Pass D sees that the release has moved on."""
    target = superseded_dir()
    assert target, "no superseded directory on disk to retarget at"
    hits = 0
    for page in pages:
        lines = list(page.lines)
        for i, line in enumerate(lines):
            m = PAPDIR.search(line)
            if m:
                lines[i] = line[:m.start(1)] + target + line[m.end(1):]
                assert lines != page.lines, "the retarget did not change the page"
                out = printed(Page(page.path, lines), mod.pass_d)
                assert "SUPERSEDED MANUSCRIPT" in out, \
                    f"{page.path.name}: a superseded manuscript was not flagged"
                hits += 1
                break
    assert hits > 0, "no page declares a preprints/ path"


def test_bare_locator_moved_out_of_the_family_block(mod, pages):
    """A bare line citation moved to the line just above the family's own block: the marker still
    resolves, the line is in range and non-blank, and the file is the right file, so only Pass E sees
    the mislocation."""
    hits = 0
    for page in pages:
        for start_line, sid, a, _b, _rel, bl in mod.bare_locator_cites(page):
            if not bl:
                continue
            line = page.lines[start_line - 1]
            new = bl[0][0] - 1
            for m in MARKER.finditer(line):
                if m.group(2) and int(m.group(2)) == a and f"S{m.group(1)}" == sid:
                    sep = (line[m.start(3) - 1] if m.group(3) else "")
                    tok = f"[S{m.group(1)}:{new}" + (f"{sep}{new}]" if m.group(3) else "]")
                    lines = list(page.lines)
                    lines[start_line - 1] = line[:m.start()] + tok + line[m.end():]
                    assert lines != page.lines, "the moved locator did not change the page"
                    out = printed(Page(page.path, lines), mod.pass_e)
                    assert "CITE OUTSIDE FAMILY BLOCK" in out, \
                        f"{page.path.name}: a locator moved out of the family block was not flagged"
                    hits += 1
                    break
            if hits:
                break
    assert hits > 0, "no page carries a bare locator cite into a family-keyed file"


def pad_cells(t):
    """Pad every table cell with two spaces. The row regex allows whitespace, so the marker pass must
    read the same rows; a regex that required exact spacing would drop rows and print UNKNOWN SOURCE
    for every marker whose row vanished, so the row count and the pass's problem count are the
    discriminators, not the render diff."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod, pages):
    bad = []
    for page in pages:
        cand = Page(page.path, pad_cells("\n".join(page.lines)).splitlines())
        if len(cand.rows) != len(page.rows):
            bad.append(f"{page.path.name}: {len(cand.rows)} rows against {len(page.rows)}")
            continue
        _pos, _src, _links, problems = mod.pass_b(cand)
        clean = mod.pass_b(page)[3]
        if problems != clean:
            bad.append(f"{page.path.name}: {problems} problems against {clean}")
    assert not bad, f"padded rows are not read: {bad[:3]}"


def test_citation_stripping_keeps_a_bracketed_note():
    r"""The quote pass folds a source line with `catlib.text.strip_markup`, whose citation rule
    `\cite[tp]*\{[^}]*\}` requires the brace to follow `\cite` directly, so a bracketed note
    (`\cite[Theorem~1.2]{X}`) is not swallowed: the note's word survives the fold and a page quoting it
    matches. A rule that allows the optional `[...]` argument strips the whole citation, so the note's
    word is gone and the same quote fails. The fold also strips a theorem number after the word (the
    deliberate rule that lets a page write "Theorem 1" for a source `\ref{thm:main}`), so the word, not
    the number, is what the comparison sees. Neither string is read from the corpus."""
    src = r"the bound in \cite[Theorem~1.2]{X} is sharp"
    quote = "Theorem"
    assert quote in strip_markup(src), f"the shipped fold read {strip_markup(src)!r}"
    narrow = re.compile(r"\\(?:ref|eqref|label|autoref|Cref|cref|cite[tp]*(?:\[[^\]]*\])?|"
                        r"citeauthor|citeyear)\{[^}]*\}")
    assert quote not in narrow.sub("", src), \
        f"the widened rule read {narrow.sub('', src)!r}, so it does not swallow the note"
    assert narrow.sub("", src).startswith("the bound in "), \
        "the widened rule removed text outside the citation"


def test_range_facts_flags_a_blank_line_at_the_end_of_a_range():
    """Pass B flags a blank line inside a cited range, so `[S4:2–3]` naming a file whose third line is
    empty is a problem. A rule that checks only that the positions are inside the file reports nothing.
    The line list is synthetic — no manuscript is read."""
    lines = ["first line", "second line", ""]
    out, blank, rev = range_facts(2, 3, len(lines), lines)
    assert not out and blank == [3], f"the shipped rule read out {out}, blank {blank}"
    assert not rev, "a forward range reported a reversed range"
    assert [p for p in (2, 3) if 0 < p <= len(lines)] == [2, 3], \
        "the inside-the-file rule must see no problem for the same range"


def test_range_facts_flags_a_reversed_range():
    """Pass B flags `[S4:29–12]` — a reversed range — and the flag comes from the shared rule. A rule
    that checks only that both positions sit inside the file accepts it. The line list is synthetic."""
    lines = [f"line {i}" for i in range(1, 31)]
    out, blank, rev = range_facts(29, 12, len(lines), lines)
    assert rev is True, "the shipped rule does not report the reversed range"
    assert not out and not blank, f"the shipped rule read out {out}, blank {blank}"
    assert all(0 < p <= len(lines) for p in (29, 12)), \
        "the inside-the-file rule rejects the reversed range, so it is not the rule that accepts it"
