"""The self-tests for `notes/scripts/verify_summaries.py`.

Each test injects one corruption into a real data file or page in memory and asserts the pass that
owns it prints its problem. The provenance pass is tested by corrupting a data file's quote spec
(an undeclared sid, a missing path, a blank endpoint, a window out of range, a reversed window) and
asserting the pass flags it. The render diff is tested by corrupting a data file's section body and
asserting the page bytes no longer match the writer's render. The supersession pass is tested by
retargeting the page's declared manuscript root to a directory that is on disk, tracked, and named
by no family. The locator pass is tested by moving a bare line citation to the line just above the
family's own block.

The clean test asserts every family page is silent on the render diff, the provenance pass, pass D
and pass E, with a non-vacuity floor: the page set is required non-empty and each page must carry
markers, so 0 problems means every pass ran. Pass B is not asserted clean here: five pages carry
rendered LaTeX `<` that pass B's HTML check reads as a tag, a pre-existing false positive tracked
separately.

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
    QUOTE,
    Page,
    superseded_dir,
)
from catlib.text import strip_markup

pytestmark = pytest.mark.mutant


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_summaries")


@pytest.fixture(scope="module")
def family_pages():
    """The 60 family pages, excluding the link-only README index page."""
    return [Page(p, read_text(p).splitlines())
            for p in sorted(SUMMARIES_DIR.rglob("*.md")) if p.name != "README.md"]


def data_text(page, mod):
    """The page's data file bytes from disk."""
    return read_text(mod.data_file(page))


def run_pass(fn, *args):
    """Run a pass, capture its stdout, return (output, return_value)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = fn(*args)
    return buf.getvalue(), result


def first_real_spec(data_text):
    """The first quote spec row with start != 0 (a real window, not the unlocated sentinel)."""
    m = re.search(r"<!-- quotes\n(.*?)-->", data_text, re.DOTALL)
    if not m:
        return None
    for line in m.group(1).strip().split("\n"):
        p = line.split("\t")
        if len(p) >= 6 and p[3] != "0":
            return line
    return None


def test_clean_pages(mod, family_pages):
    """Every cgv.9 pass and pass D/E are silent on every family page, with a non-vacuity floor:
    the page set is required non-empty and each page must carry markers, so 0 problems means every
    pass ran. A page with no markers reports 0 problems and proves nothing, so the floor is the
    witness that the pass ran."""
    assert len(family_pages) > 0, "no family pages on disk, so every pass is vacuous"
    for page in family_pages:
        dt = data_text(page, mod)
        _pos, _src, _links, _b_problems = run_pass(mod.pass_b, page)[1]
        _out, rd = run_pass(mod.render_diff, page, dt)
        _out, (specs, prov) = run_pass(mod.provenance_pass, page, dt)
        _out, (_dirs, stale) = run_pass(mod.pass_d, page)
        _out, (_cites, outside) = run_pass(mod.pass_e, page)
        assert rd == 0, f"{page.path.name}: render diff reports {rd} problems"
        assert prov == 0, f"{page.path.name}: provenance reports {prov} problems"
        assert stale == 0, f"{page.path.name}: pass D reports {stale} superseded or off-family"
        assert outside == 0, f"{page.path.name}: pass E reports {outside} outside the family block"
        assert specs > 0, f"{page.path.name}: provenance checked 0 specs, so it ran on nothing"


def test_provenance_undeclared_sid(mod, family_pages):
    """A quote spec whose sid is not in the data file's sources block: the spec names a source the
    page never declared, so the provenance pass must flag it."""
    for page in family_pages:
        dt = data_text(page, mod)
        spec = first_real_spec(dt)
        if not spec:
            continue
        parts = spec.split("\t")
        parts[2] = "S999"
        bad_spec = "\t".join(parts)
        bad_dt = dt.replace(spec, bad_spec)
        assert bad_dt != dt, "the injection did not change the data file"
        _out, (_specs, problems) = run_pass(mod.provenance_pass, page, bad_dt)
        assert problems > 0, \
            f"{page.path.name}: an undeclared sid left the provenance pass silent"
        break
    else:
        pytest.fail("no data file carries a real quote spec")


def test_provenance_missing_path(mod, family_pages):
    """A quote spec whose source path is not on disk: the spec points at a file that does not
    exist, so the provenance pass must flag it."""
    for page in family_pages:
        dt = data_text(page, mod)
        spec = first_real_spec(dt)
        if not spec:
            continue
        # Retarget the source the spec's SID points to, to a path that does not exist.
        spec_parts = spec.split("\t")
        sid = spec_parts[2].strip()
        m = re.search(r"<!-- sources\n(.*?)-->", dt, re.DOTALL)
        assert m, "no sources block in the data file"
        src_lines = m.group(1).strip().split("\n")
        assert src_lines, "the sources block is empty"
        target = None
        for line in src_lines:
            p = line.split("\t")
            if p[0].strip() == sid:
                target = line
                break
        assert target is not None, f"SID {sid} not found in sources block"
        parts = target.split("\t")
        bad_path = parts[1] + "-nonexistent"
        parts[1] = bad_path
        bad_src = "\t".join(parts)
        bad_dt = dt.replace(target, bad_src)
        assert bad_dt != dt, "the injection did not change the data file"
        _out, (_specs, problems) = run_pass(mod.provenance_pass, page, bad_dt)
        assert problems > 0, \
            f"{page.path.name}: a missing source path left the provenance pass silent"
        break
    else:
        pytest.fail("no data file carries a real quote spec")


def test_provenance_blank_endpoint(mod, family_pages):
    """A quote spec whose endpoint lands on a blank line in the source file: the window names a
    line that carries no text, so the provenance pass must flag it."""
    for page in family_pages:
        dt = data_text(page, mod)
        spec = first_real_spec(dt)
        if not spec:
            continue
        parts = spec.split("\t")
        sid = parts[2].strip()
        m = re.search(r"<!-- sources\n(.*?)-->", dt, re.DOTALL)
        assert m, "no sources block in the data file"
        srcs = {}
        for line in m.group(1).strip().split("\n"):
            p = line.split("\t")
            if len(p) >= 2:
                srcs[p[0].strip()] = p[1].strip()
        if sid not in srcs:
            continue
        from catlib.paths import ROOT
        lines = (ROOT / srcs[sid]).read_text(encoding="utf-8", errors="replace").splitlines()
        # Find a blank line in the file to retarget the endpoint at.
        blank = None
        for i, ln in enumerate(lines, 1):
            if not ln.strip():
                blank = i
                break
        if blank is None:
            continue
        parts[4] = str(blank)
        bad_spec = "\t".join(parts)
        bad_dt = dt.replace(spec, bad_spec)
        assert bad_dt != dt, "the injection did not change the data file"
        _out, (_specs, problems) = run_pass(mod.provenance_pass, page, bad_dt)
        assert problems > 0, \
            f"{page.path.name}: a blank endpoint left the provenance pass silent"
        break
    else:
        pytest.fail("no data file carries a spec whose source has a blank line")


def test_provenance_oob_window(mod, family_pages):
    """A quote spec whose window is out of range: the start line exceeds the source file's line
    count, so the provenance pass must flag it."""
    for page in family_pages:
        dt = data_text(page, mod)
        spec = first_real_spec(dt)
        if not spec:
            continue
        parts = spec.split("\t")
        parts[3] = "999999"
        parts[4] = "999999"
        bad_spec = "\t".join(parts)
        bad_dt = dt.replace(spec, bad_spec)
        assert bad_dt != dt, "the injection did not change the data file"
        _out, (_specs, problems) = run_pass(mod.provenance_pass, page, bad_dt)
        assert problems > 0, \
            f"{page.path.name}: an out-of-range window left the provenance pass silent"
        break
    else:
        pytest.fail("no data file carries a real quote spec")


def test_provenance_reversed_window(mod, family_pages):
    """A quote spec with start after end: the window is reversed, so the provenance pass must
    flag it."""
    for page in family_pages:
        dt = data_text(page, mod)
        spec = first_real_spec(dt)
        if not spec:
            continue
        parts = spec.split("\t")
        if int(parts[3]) >= int(parts[4]):
            continue  # already reversed or single-line; need a multi-line window to swap
        parts[3], parts[4] = parts[4], parts[3]
        bad_spec = "\t".join(parts)
        bad_dt = dt.replace(spec, bad_spec)
        assert bad_dt != dt, "the injection did not change the data file"
        _out, (_specs, problems) = run_pass(mod.provenance_pass, page, bad_dt)
        assert problems > 0, \
            f"{page.path.name}: a reversed window left the provenance pass silent"
        break
    else:
        pytest.fail("no data file carries a multi-line quote spec")


def test_render_diff_data_file_corrupted(mod, family_pages):
    """A data file whose section body is corrupted: the writer's render of the corrupted file
    differs from the page on disk, so the render diff must flag it. This is the pass that replaces
    the old quote-fidelity check — a paraphrase dressed as a quote, a stale render, and a hand edit
    all leave a page whose citations resolve but whose bytes are not the writer's."""
    for page in family_pages:
        dt = data_text(page, mod)
        lines = dt.split("\n")
        injected = False
        for i, line in enumerate(lines):
            if line.startswith("## ") and i + 1 < len(lines):
                lines.insert(i + 1, "INJECTED CORRUPTION FOR RENDER DIFF TEST")
                injected = True
                break
        if not injected:
            continue
        bad_dt = "\n".join(lines)
        assert bad_dt != dt, "the injection did not change the data file"
        _out, problems = run_pass(mod.render_diff, page, bad_dt)
        assert problems > 0, \
            f"{page.path.name}: a corrupted data file left the render diff silent"
        break
    else:
        pytest.fail("no family page with a section to corrupt")


def test_superseded_retarget(mod, family_pages):
    """The page's declared manuscript root moved to a superseded sibling. Pass B stays green — the
    path resolves and the files exist — so only Pass D sees that the release has moved on."""
    target = superseded_dir()
    assert target, "no superseded directory on disk to retarget at"
    hits = 0
    for page in family_pages:
        lines = list(page.lines)
        for i, line in enumerate(lines):
            m = PAPDIR.search(line)
            if m:
                lines[i] = line[:m.start(1)] + target + line[m.end(1):]
                assert lines != page.lines, "the retarget did not change the page"
                _out, (_dirs, stale) = run_pass(mod.pass_d, Page(page.path, lines))
                assert stale > 0, \
                    f"{page.path.name}: a superseded manuscript was not flagged"
                hits += 1
                break
    assert hits > 0, "no page declares a preprints/ path"


def test_bare_locator_moved_out_of_the_family_block(mod, family_pages):
    """A bare line citation moved to the line just above the family's own block: the marker still
    resolves, the line is in range and non-blank, and the file is the right file, so only Pass E sees
    the mislocation."""
    hits = 0
    for page in family_pages:
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
                    _out, (_cites, outside) = run_pass(mod.pass_e, Page(page.path, lines))
                    assert outside > 0, \
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
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = ln
        out.append(padded)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod, family_pages):
    bad = []
    for page in family_pages:
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
    r"""The normalizer folds a source line with `catlib.text.strip_markup`, whose citation rule
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


def test_accent_escape_is_not_a_quotation_opener():
    r"""A LaTeX accent escape (`K\"ahler`) puts a literal `"` in a prose line, and the quote pass's
    ASCII branch treats any `"` pair of 6+ chars as a span, so the text between the accent's `"` and the
    next real quote becomes a quotation the page never wrote. The lookbehind makes `\"` not an opener, so
    only the real span is read. The string is synthetic — no manuscript is read."""
    line = r'K\"ahler metrics appear in `build/sections/introduction.tex:11` and "scalar curvature" is real.'
    spans = [m.group(1) or m.group(2) for m in QUOTE.finditer(line)]
    assert spans == ["scalar curvature"], f"the shipped rule read {spans}"
    loose = re.compile(r"“([^”]{6,})”|\"([^\"]{6,})\"")
    bogus = [m.group(1) or m.group(2) for m in loose.finditer(line)]
    assert bogus != spans, f"the rule without the lookbehind read {bogus}, which is not the real span"
    assert bogus[0].startswith("ahler"), f"the widened rule read {bogus}"
