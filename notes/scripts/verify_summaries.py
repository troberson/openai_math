#!/usr/bin/env python3
"""Verify every citation in a family summary page against the files it names. Writes nothing.

The page body cites sources as [S4:29], [S4:29–56] or [S4]; the Sources table at the bottom maps
S# to a file. Two passes read the same table:

  Pass B (markers)  - resolve every marker, print the line it names, flag out-of-range, blank and
                      reversed-range positions, check the table's declared line counts against the
                      files on disk, resolve every markdown link from the page's own directory, and
                      require zero raw HTML anywhere in the page.
  Pass C (quotes)   - every quoted span of a cited unit must appear, verbatim, in the lines that
                      unit cites. Pass B proves a line exists; it proves nothing about the text we
                      attribute to it, so a paraphrase dressed as a quote passes Pass B.

Pass A (the needle check: does the page contain the specific strings the reading pass recorded) is
written per page against that page's own findings, so it is not promoted here.

Passes B and C both prove things about the text at a cited line; neither says the line belongs to
the family the page is about. An upstream update leaves the manuscripts it replaced on disk, tracked
in git, with their names unchanged, so a page can stay green through B and C while describing a
manuscript the release no longer names. Two more passes close that gap:

  Pass D (supersession) - every manuscript directory the page names must be one the catalog's
                      overview entry currently names, and it must be named by *this* family. A
                      directory that is on disk and named by no family is a superseded manuscript.
  Pass E (bare cites) - a citation in a unit that carries no quotation makes a location claim, and
                      in a file whose blocks are keyed by family number (CONTENTS.md, overview.tex,
                      README.md, notes/*.md) the only legal location is the family's own block.
                      Files with no family key — manuscripts, Lean sources, yaml, tsv — are skipped:
                      the pass makes no claim about them.

--mutant proves the checker discriminates: it corrupts a real quotation in every quotation form the
page actually uses (inline, inline wrapped across line breaks, block quote), invents one fabricated
quotation, retargets the page's manuscript to a superseded sibling directory, and moves a bare
locator citation to the line above the family's own block; it asserts the matching pass flags each
while the real page stays silent. A form the page does not use is not tested, so the report names
the form it corrupted.

Usage: python3 notes/scripts/verify_summaries.py                 # every page under notes/summaries
       python3 notes/scripts/verify_summaries.py <page.md> ...   # named pages only
       python3 notes/scripts/verify_summaries.py --mutant        # discrimination test as well
"""
import argparse
import os
import re
import sys
from pathlib import Path

import build_catalog as B

ROOT = Path(__file__).resolve().parents[2]
SUMMARIES = ROOT / "notes" / "summaries"

ROW = re.compile(r"^\|\s*(S\d+)\s*\|\s*(.+?)\s*\|\s*([\d,]+|—)\s*\|\s*(.*?)\s*\|\s*$")
CELL = re.compile(r"`([^`]+)`")
MARKER = re.compile(r"\[S(\d+)(?::(\d+)(?:[–-](\d+))?)?\]")
QUOTE = re.compile(r"“([^”]{6,})”|\"([^\"]{6,})\"")
LINK = re.compile(r"\]\(([^)\s]+)\)")
ENTITY = re.compile(r"&(#[0-9]+|[a-zA-Z][a-zA-Z0-9]*);")
TAG = re.compile(r"<[a-zA-Z/][^>]*>")
PAPDIR = re.compile(r"preprints/([^/`\s]+)/")

# Pass E applies only to files whose blocks are keyed by the family number, because that is the only
# case where "the family's own block" is a fact the file itself records. Manuscript and Lean files
# carry no family key, so the pass makes no claim about them.
BLOCK_RULES = {
    "CONTENTS.md": (re.compile(r"^\*\*(\d{1,3})\."), re.compile(r"^\*\*\d{1,3}\.")),
    "overview.tex": (re.compile(r"^\\resultentry\{(\d{1,3})\}"), re.compile(r"^\\resultentry\{")),
    "README.md": (re.compile(r"^\|\s*(\d{1,3})\s*\|"), None),
}
NOTE_ENTRY = re.compile(r"^- \*\*(\d{1,3})\*\*")
# The Sources preamble demonstrates the marker syntax ("[S2:31] for one line"). Those tokens are an
# example of the format, not a citation, so the unit that carries them makes no claim to check.
FORMAT_EXAMPLE = "cited in the body as"


class Page:
    """A summary page plus the Sources table that resolves its markers."""

    def __init__(self, path, lines):
        self.path = path
        self.lines = lines
        self.cache = {}
        self.table = {}
        self.rows = []
        self.ambiguous = []
        m = re.match(r"(\d{1,3})-", path.name)
        self.fam = m.group(1) if m else None
        # Relative paths in the table are relative to the manuscript root the Sources prose names
        # first; the repository root is the fallback. Globbing preprints/* is deliberately not a
        # rule: build/main.tex, references.tex and README.md exist in many manuscript trees.
        pre = None
        for line in lines:
            m = re.search(r"`(preprints/[^`]+)`", line)
            if m:
                pre = ROOT / m.group(1)
                break
        self.roots = ([pre] if pre and pre.is_dir() else []) + [ROOT]
        self._read_table()

    def _read_table(self):
        for n, line in enumerate(self.lines, 1):
            m = ROW.match(line)
            if not m:
                continue
            sid, cell, declared = m.group(1), m.group(2), m.group(3)
            path_cell = CELL.search(cell)
            if not path_cell:
                print(f"{sid} row at doc line {n} names no file")
                continue
            rel = path_cell.group(1)
            hits = [r / rel for r in self.roots if (r / rel).is_file()]
            if len(hits) > 1:
                # Not pinned to one file: pass B counts this as a problem, so a page whose cell
                # resolves under both the manuscript root and the repo root cannot report green.
                self.ambiguous.append((sid, rel, hits))
            self.table[sid] = (rel, hits[0] if hits else None)
            self.rows.append((sid, rel, declared, n))

    def lines_of(self, sid):
        rel, path = self.table[sid]
        if rel not in self.cache:
            # A page may declare a compiled PDF as a source. Reading it must not abort the run:
            # bytes that are not text decode to replacement characters, so a quotation cited to a
            # PDF fails the verbatim test, which is the honest result - its text is not extractable.
            self.cache[rel] = path.read_text(encoding="utf-8", errors="replace").splitlines()
        return self.cache[rel]


def norm(s):
    """Compare a page quotation with the source line it cites, markup aside."""
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("**", "").replace("`", "").replace("*", "")
    s = s.replace("&emsp;", " ").replace("&thinsp;", " ").replace("&mdash;", "-")
    # Markup, not words: the release writes <i>p</i> in its blurbs and the page renders *p*. Strip
    # tags to nothing, not to a space - `prime-to-<i>p</i>` must normalize to `prime-to-p`, and a
    # space here would break the substring test against the page.
    s = re.sub(r"</?[a-zA-Z][^>]*>", "", s)
    # The page links its sources relatively (../../../ from notes/summaries/<discipline>/), while
    # the release text spells the same target as a repo-relative path.
    s = re.sub(r"(?:\.\./)+", "", s)
    # LaTeX-aware: a rendered cross-reference is not a misquote. `\ref{thm:main}` in the source is
    # "Theorem 1" in the page, so strip the command *and* the number the page substituted for it.
    s = re.sub(r"\\(?:ref|eqref|label|autoref|Cref|cref|cite[tp]*|citeauthor|citeyear)\{[^}]*\}",
               "", s)
    s = re.sub(r"\\[a-zA-Z@]+", " ", s).replace("~", " ").replace("{}", " ")
    s = re.sub(r"\b(Theorem|Lemma|Corollary|Proposition|Definition|Remark|Item|Axiom|Step)"
               r"\s+\d+(?:\.\d+)*\b", r"\1", s)
    s = re.sub(r"[{}]", " ", s)
    s = re.sub(r"\s+([.,;:!?])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def markers(text):
    """Citations in source order: (offset, S#, first line or None for the whole file, last line)."""
    out = []
    for m in MARKER.finditer(text):
        a = int(m.group(2)) if m.group(2) else None
        b = int(m.group(3)) if m.group(3) else a
        out.append((m.start(), f"S{m.group(1)}", a, b))
    out.sort()
    return out


def units(doc_lines):
    """Join wrapped prose/bullet lines into logical units; keep block quotes as their own unit."""
    out, i = [], 0
    while i < len(doc_lines):
        line = doc_lines[i]
        if line.startswith("> "):
            j = i
            while j < len(doc_lines) and doc_lines[j].startswith(">"):
                j += 1
            out.append((i + 1, " ".join(l.lstrip("> ").strip() for l in doc_lines[i:j]), True))
            i = j
            continue
        if not line.strip() or line.startswith(("#", "|", "---")):
            i += 1
            continue
        j = i + 1
        while j < len(doc_lines):
            nxt = doc_lines[j]
            if not nxt.strip() or nxt.startswith(("#", "|", "---", "> ")):
                break
            if nxt.startswith(("- ", "* ")) and not doc_lines[i].startswith(("- ", "* ")):
                break
            j += 1
        out.append((i + 1, " ".join(l.strip() for l in doc_lines[i:j]), False))
        i = j
    return out


def usable(page, cites):
    return [c for c in cites if c[1] in page.table and page.table[c[1]][1] is not None]


def label(sid, a, b):
    return f"{sid}:{a}" + (f"-{b}" if b != a and a is not None else "") if a else f"{sid} (file)"


def pass_b(page):
    """Markers, links, declared line counts, ambiguous File cells, raw HTML.

    Returns (positions, sources, links, problems).
    """
    problems = 0
    checked = 0
    used = set()
    links = 0
    for n, line in enumerate(page.lines, 1):
        for m in LINK.finditer(line):
            href = m.group(1)
            links += 1
            if href.startswith(("http://", "https://", "mailto:")):
                problems += 1
                print(f"UPSTREAM LINK [doc line {n}]: {href} — this page links relatively, not upstream")
                continue
            if href.startswith("#"):
                problems += 1
                print(f"ANCHOR-ONLY LINK [doc line {n}]: {href}")
                continue
            target = (page.path.parent / href).resolve()
            if not target.is_file():
                problems += 1
                print(f"DEAD LINK [doc line {n}]: {href} -> {target}")
            elif not target.is_relative_to(ROOT):
                problems += 1
                print(f"LINK LEAVES THE REPO [doc line {n}]: {href} -> {target}")

    for sid, rel, hits in page.ambiguous:
        problems += 1
        print(f"AMBIGUOUS {sid} ({rel}) resolves under {len(hits)} roots: "
              f"{', '.join(str(h) for h in hits)} — the File cell is not the repository-relative path")

    for n, line in enumerate(page.lines, 1):
        for m in MARKER.finditer(line):
            sid = f"S{m.group(1)}"
            used.add(sid)
            if sid not in page.table:
                problems += 1
                print(f"UNKNOWN SOURCE {sid} [doc line {n}]")
                continue
            rel, path = page.table[sid]
            if path is None:
                problems += 1
                print(f"FILE NOT ON DISK {sid} -> {rel} [doc line {n}]")
                continue
            if m.group(2) is None:
                checked += 1
                print(f"{sid} = {rel}")
                continue
            a = int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            text = page.lines_of(sid)
            for pos in ({a} if a == b else {a, b}):
                checked += 1
                if not 0 < pos <= len(text):
                    problems += 1
                    print(f"OUT OF RANGE {sid}:{pos} -> {rel} (file has {len(text)} lines) "
                          f"[doc line {n}]")
                elif not text[pos - 1].strip():
                    problems += 1
                    print(f"BLANK {sid}:{pos} -> {rel} [doc line {n}]")
            if a > b:
                problems += 1
                print(f"REVERSED RANGE {sid}:{a}–{b} [doc line {n}]")
            span = " ".join(text[a - 1:max(a, b)]).strip()
            print(f"{sid}:{a}" + (f"–{b}" if b != a else "") + f" -> {rel} | {span[:58]}")

    for sid, rel, declared, n in page.rows:
        if declared == "—":
            continue
        want = int(declared.replace(",", ""))
        path = page.table[sid][1]
        if path is None:
            continue
        got = len(page.lines_of(sid))
        if got != want:
            problems += 1
            print(f"LINE COUNT {sid} ({rel}) says {declared}, file has {got} [doc line {n}]")

    unused = sorted(set(page.table) - used, key=lambda s: int(s[1:]))
    if unused:
        print(f"UNUSED SOURCES (declared, never cited): {', '.join(unused)}")

    # Zero HTML anywhere, including inside block quotes. The release writes HTML in its blurbs
    # (&emsp;, <i>p</i>); the page renders that markup as markdown and drops the indentation
    # entity, so a tag or entity surviving in the finished page is a paste artifact.
    for n, line in enumerate(page.lines, 1):
        hits = ENTITY.findall(line) + TAG.findall(line)
        if hits:
            problems += 1
            print(f"STRAY HTML [doc line {n}]: {', '.join(hits)}")

    return checked, len(page.table), links, problems


def pass_c(page):
    """Quote fidelity. Returns (spans, misses)."""
    checked = misses = 0
    for start_line, unit, is_blockquote in units(page.lines):
        if is_blockquote:
            # A block quote is attributed by the citation on the line above it.
            resolved = []
            for back in range(start_line - 2, max(start_line - 5, -1), -1):
                resolved = usable(page, markers(page.lines[back]))
                if resolved:
                    break
            spans = [unit]
        else:
            if "Prior (my training data" in unit:
                # A prior paragraph is explicitly not repo text; nothing in it is a quotation.
                continue
            resolved = usable(page, markers(unit))
            # Spans under 12 characters are terms under discussion ("proves"), not quotations.
            spans = [m.group(1) or m.group(2) for m in QUOTE.finditer(unit)
                     if len(m.group(1) or m.group(2)) >= 12]

        candidates = [(sid, a, b) for _, sid, a, b in resolved]
        for span in spans:
            if not candidates:
                print(f"NO CITATION in unit at doc line {start_line}: {span[:50]!r}")
                misses += 1
                continue
            hit = None
            for sid, a, b in candidates:
                src = page.lines_of(sid)
                haystack = norm(" ".join(src[a - 1:max(a, b)]) if a else " ".join(src))
                if norm(span) in haystack:
                    hit = (sid, a, b)
                    break
            checked += 1
            if hit is None:
                misses += 1
                near = ", ".join(label(s, a, b) for s, a, b in candidates[:4])
                print(f"NOT VERBATIM [doc line {start_line}] cited {near}")
                print(f"   page says : {norm(span)[:130]}")
                sid, a, b = candidates[0]
                src = page.lines_of(sid)
                print(f"   line says : {norm(' '.join(src[a - 1:b] if a else src))[:130]}")
    return checked, misses


FABRICATED = "the formalization is complete and machine-checked"


def _inject(text, start, end, span):
    """Splice the marker token into the middle of a quotation, at a word boundary."""
    cut = span.rfind(" ", 0, len(span) // 2) + 1
    if cut <= 0:
        cut = span.find(" ", len(span) // 2) + 1
    if cut <= 0:
        return None
    return text[:start] + span[:cut] + "XYZZY " + span[cut:] + text[end:]


def inline_targets(text):
    """Inline quotations Pass C can see, split by whether the span is wrapped across lines."""
    single, wrapped = [], []
    for m in QUOTE.finditer(text):
        span = m.group(1) or m.group(2)
        if len(span) < 12 or "Prior (my training data" in span:
            continue
        (wrapped if "\n" in span else single).append(m)
    return single, wrapped


def blockquote_targets(page):
    """Block-quote units Pass C checks, i.e. those with a citation on a line above them."""
    out = []
    for start_line, unit, is_blockquote in units(page.lines):
        if not is_blockquote or len(unit) < 12:
            continue
        resolved = []
        for back in range(start_line - 2, max(start_line - 5, -1), -1):
            resolved = usable(page, markers(page.lines[back]))
            if resolved:
                break
        if resolved:
            out.append((start_line, unit))
    return out


_NAMED_CACHE = None


def named_dirs():
    """{manuscript dir name: families whose overview entry names it} — the release's own claim."""
    global _NAMED_CACHE
    if _NAMED_CACHE is None:
        _, fams = B.parse_overview()
        _NAMED_CACHE = {}
        for fam, d in fams.items():
            for p in d["tex_paps"]:
                _NAMED_CACHE.setdefault(p.split("/")[1], set()).add(fam)
    return _NAMED_CACHE


def superseded_dir():
    """A manuscript directory that is on disk and named by no family — the shape an update leaves behind."""
    named = named_dirs()
    for p in sorted((ROOT / "preprints").iterdir()):
        if p.is_dir() and p.name not in named:
            return p.name
    return None


def pass_d(page):
    """Supersession. Every manuscript the page names must be one the catalog currently names for this family."""
    named = named_dirs()
    fam = page.fam
    seen = {}
    for n, line in enumerate(page.lines, 1):
        for d in PAPDIR.findall(line):
            seen.setdefault(d, n)
    if fam is None:
        print(f"NO FAMILY NUMBER in file name {page.path.name} — pass D cannot map the page to the catalog")
        return len(seen), 1
    problems = 0
    for d, n in sorted(seen.items(), key=lambda kv: kv[1]):
        owners = named.get(d)
        if owners is None:
            problems += 1
            print(f"SUPERSEDED MANUSCRIPT [doc line {n}]: preprints/{d}/ is on disk and tracked, but no "
                  f"family's overview entry names it — the release has moved on from this manuscript")
        elif fam not in owners:
            problems += 1
            print(f"OFF-FAMILY MANUSCRIPT [doc line {n}]: preprints/{d}/ is named by "
                  f"{', '.join(sorted(owners))}, not by family {fam}")
    return len(seen), problems


def family_blocks(rel, lines, fam):
    """Line spans of family `fam`'s own block(s) in a file whose blocks are keyed by family number.

    Returns None when the file carries no family key at all — a statement about the file, not about
    the citation. A block runs from its start token to the line before the next family's start token.
    """
    rule = BLOCK_RULES.get(rel)
    if rule is None:
        if rel.startswith("notes/") and rel.endswith(".md"):
            rule = (NOTE_ENTRY, NOTE_ENTRY)
        else:
            return None
    start, nxt = rule
    out, cur = [], None
    for i, line in enumerate(lines, 1):
        m = start.match(line)
        if m and int(m.group(1)) == fam:
            if nxt is None:
                out.append((i, i))
                continue
            cur = i
        elif nxt is not None and nxt.match(line):
            if cur:
                out.append((cur, i - 1))
                cur = None
    if cur:
        out.append((cur, len(lines)))
    return out


def bare_locator_cites(page):
    """Markers with line numbers, in units carrying no quoted span, into family-keyed files.

    A unit with a quotation is judged by Pass C against the text it quotes. A unit with none makes a
    location claim, and the only location a summary page may cite in a family-keyed file is that
    family's own block — a page citing a neighbour's block is citing the wrong family's record.
    """
    if page.fam is None:
        return []
    fam = int(page.fam)
    out = []
    for start_line, unit, is_blockquote in units(page.lines):
        if is_blockquote or FORMAT_EXAMPLE in unit or "Prior (my training data" in unit:
            continue
        if any(len(m.group(1) or m.group(2)) >= 12 for m in QUOTE.finditer(unit)):
            continue
        for _, sid, a, b in usable(page, markers(unit)):
            if a is None:
                continue
            rel = page.table[sid][0]
            bl = family_blocks(rel, page.lines_of(sid), fam)
            if bl is None:
                continue
            out.append((start_line, sid, a, b, rel, bl))
    return out


def pass_e(page):
    """Bare line citations into family-keyed files must land inside the family's own block."""
    cites = problems = 0
    for start_line, sid, a, b, rel, bl in bare_locator_cites(page):
        cites += 1
        if not any(s <= b and a <= e for s, e in bl):
            problems += 1
            near = ", ".join(f"{s}-{e}" for s, e in bl[:3]) if bl else "no block for this family"
            print(f"CITE OUTSIDE FAMILY BLOCK [doc line {start_line}] {label(sid, a, b)} -> {rel}: "
                  f"family {page.fam}'s block is {near}")
    return cites, problems


def mutants(page):
    """Corrupt a real quotation in every form the page uses, invent one, assert Pass C flags each."""
    text = "\n".join(page.lines)
    results = []

    # Mutant A: a real quotation, one token deeper than the source. Pages quote in three forms and
    # a page can carry only one of them, so each present form is tested and named.
    single, wrapped = inline_targets(text)
    for name, group in (("A1 corrupts an inline quotation", single),
                        ("A2 corrupts a wrapped inline quotation", wrapped)):
        if not group:
            continue
        m = group[0]
        g = 1 if m.group(1) else 2
        bad = _inject(text, m.start(g), m.end(g), m.group(g))
        if bad is None:
            continue
        _, misses = pass_c(Page(page.path, bad.splitlines()))
        results.append((name, misses > 0, f"{misses} flagged"))

    for start_line, _unit in blockquote_targets(page)[:1]:
        line = page.lines[start_line - 1]
        bad_line = _inject(line, 0, len(line), line)
        if bad_line is None:
            continue
        lines = list(page.lines)
        lines[start_line - 1] = bad_line
        _, misses = pass_c(Page(page.path, lines))
        results.append(("A3 corrupts a block-quote attribution", misses > 0,
                        f"{misses} flagged (block quote at doc line {start_line})"))

    # Mutant D: retarget the page's declared manuscript root to a superseded sibling — a directory
    # that is on disk, tracked in git, and named by no family. Pass B stays green on it (the path
    # resolves, the files exist); only Pass D sees that the release has moved on from it.
    target = superseded_dir()
    lines = list(page.lines)
    for i, line in enumerate(lines):
        m = PAPDIR.search(line)
        if m and target:
            lines[i] = line[:m.start(1)] + target + line[m.end(1):]
            _, stale = pass_d(Page(page.path, lines))
            results.append(("D retargets the manuscript to a superseded directory", stale > 0,
                            f"{stale} flagged (preprints/{target}/ at doc line {i + 1})"))
            break
    else:
        results.append(("D retargets the manuscript to a superseded directory", False,
                        "no preprints/ path in the page"))

    # Mutant E: move a bare locator citation to the line just above the family's own block. The
    # marker still resolves, the line is in range and non-blank, and the file is the right file —
    # Pass B is green and Pass C has nothing to compare, so only Pass E can see the mislocation.
    locs = bare_locator_cites(page)
    moved = False
    for start_line, sid, a, b, rel, bl in locs:
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
                _, outside = pass_e(Page(page.path, lines))
                results.append(("E moves a bare locator cite out of the family block", outside > 0,
                                f"{outside} flagged ({label(sid, a, b)} -> {rel} at doc line {start_line}, "
                                f"block starts {bl[0][0]})"))
                moved = True
                break
        if moved:
            break
    if not moved:
        results.append(("E moves a bare locator cite out of the family block", False,
                        "no bare locator cite into a family-keyed file"))

    # Mutant B: a fabricated quotation attached to a line that already carries a citation.
    lines = list(page.lines)
    for i, line in enumerate(lines):
        m = MARKER.search(line)
        if m and not line.startswith(("#", "|", ">")):
            lines[i] = line + f" “{FABRICATED}” [{m.group(0)}]"
            break
    else:
        results.append(("B invents a cited quotation", False, "no citable prose line"))
        return results
    _, misses = pass_c(Page(page.path, lines))
    results.append(("B invents a cited quotation", misses > 0, f"{misses} flagged"))
    return results


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("pages", nargs="*", help="summary pages (default: every page under notes/summaries)")
    ap.add_argument("--mutant", action="store_true", help="run the Pass C discrimination test")
    ap.add_argument("--quiet", action="store_true", help="print only the summary lines")
    args = ap.parse_args()

    if args.pages:
        docs = [Path(p).resolve() for p in args.pages]
    else:
        docs = sorted(SUMMARIES.rglob("*.md"))
    if not docs:
        print(f"no summary pages under {SUMMARIES}")
        sys.exit(1)

    import contextlib
    io = sys.stdout
    total_b = total_c = total_problems = total_mutants = 0
    for doc in docs:
        lines = doc.read_text(encoding="utf-8").splitlines()
        page = Page(doc, lines)
        print(f"===== {doc.relative_to(ROOT)}")
        with contextlib.ExitStack() as stack:
            sink = stack.enter_context(open(os.devnull, "w", encoding="utf-8")) if args.quiet else io
            stack.enter_context(contextlib.redirect_stdout(sink))
            positions, sources, links, problems = pass_b(page)
            spans, misses = pass_c(page)
            dirs, stale = pass_d(page)
            cites, outside = pass_e(page)
            print(f"--- pass B: {positions} marker positions against {sources} declared sources, "
                  f"{links} markdown links resolved from the page directory, {problems} problems")
            print(f"--- pass C: {spans} quoted spans checked against their cited lines, "
                  f"{misses} not verbatim")
            print(f"--- pass D: {dirs} manuscript directories named by the page, {stale} superseded "
                  f"or off-family")
            print(f"--- pass E: {cites} bare line citations into family-keyed files, {outside} "
                  f"outside the family's own block")
            unflagged = 0
            if args.mutant:
                if misses or problems or stale or outside:
                    print("--- mutants skipped: the real page is not silent")
                    unflagged = 2
                else:
                    for name, flagged, detail in mutants(page):
                        print(f"--- mutant {name}: {'FLAGGED' if flagged else 'MISSED'} ({detail})")
                        unflagged += 0 if flagged else 1
        total_b += positions
        total_c += spans
        total_problems += problems + misses + stale + outside + unflagged
        total_mutants += unflagged
    print(f"===== TOTAL {len(docs)} page(s): {total_b} marker positions, {total_c} quoted spans, "
          f"{total_problems} problems" + (f" ({total_mutants} undetected mutants)" if args.mutant else ""))
    sys.exit(1 if total_problems else 0)


if __name__ == "__main__":
    main()
