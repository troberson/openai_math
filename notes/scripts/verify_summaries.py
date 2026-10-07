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

--mutant proves the checker discriminates: it corrupts one real quotation and invents one fabricated
quotation, both carrying a citation, and asserts Pass C flags each while the real page stays silent.

Usage: python3 notes/scripts/verify_summaries.py                 # every page under notes/summaries
       python3 notes/scripts/verify_summaries.py <page.md> ...   # named pages only
       python3 notes/scripts/verify_summaries.py --mutant        # discrimination test as well
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUMMARIES = ROOT / "notes" / "summaries"

ROW = re.compile(r"^\|\s*(S\d+)\s*\|\s*(.+?)\s*\|\s*([\d,]+|—)\s*\|\s*(.*?)\s*\|\s*$")
CELL = re.compile(r"`([^`]+)`")
MARKER = re.compile(r"\[S(\d+)(?::(\d+)(?:[–-](\d+))?)?\]")
QUOTE = re.compile(r"“([^”]{6,})”|\"([^\"]{6,})\"")
LINK = re.compile(r"\]\(([^)\s]+)\)")
ENTITY = re.compile(r"&(#[0-9]+|[a-zA-Z][a-zA-Z0-9]*);")
TAG = re.compile(r"<[a-zA-Z/][^>]*>")


class Page:
    """A summary page plus the Sources table that resolves its markers."""

    def __init__(self, path, lines):
        self.path = path
        self.lines = lines
        self.cache = {}
        self.table = {}
        self.rows = []
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
                print(f"AMBIGUOUS {sid} ({rel}) resolves under {len(hits)} roots: "
                      f"{', '.join(str(h) for h in hits)}")
            self.table[sid] = (rel, hits[0] if hits else None)
            self.rows.append((sid, rel, declared, n))

    def lines_of(self, sid):
        rel, path = self.table[sid]
        if rel not in self.cache:
            self.cache[rel] = path.read_text(encoding="utf-8").splitlines()
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
    """Markers, links, declared line counts, raw HTML. Returns (positions, sources, links, problems)."""
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
        got = len(path.read_text(encoding="utf-8").splitlines())
        if got != want:
            problems += 1
            print(f"LINE COUNT {sid} ({rel}) says {declared}, file has {got} [doc line {n}]")

    unused = sorted({s for s in page.table} - used, key=lambda s: int(s[1:]))
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


def mutants(page):
    """Corrupt one real quotation and invent one, both cited; assert Pass C flags each."""
    text = "\n".join(page.lines)
    results = []

    # Mutant A: a real quotation, one token deeper than the source.
    target = None
    for m in QUOTE.finditer(text):
        span = m.group(1) or m.group(2)
        if len(span) >= 12 and "\n" not in span and "Prior (my training data" not in span:
            target = m
            break
    if target is None:
        results.append(("A corrupts a real quotation", False, "no quotable span on one line"))
    else:
        span = target.group(1) or target.group(2)
        cut = len(span) // 2
        cut = span.rfind(" ", 0, cut) + 1
        bad = text[:target.start(1) if target.group(1) else target.start(2)] + \
            span[:cut] + "XYZZY " + span[cut:] + text[target.end(1) if target.group(1) else target.end(2):]
        _, misses = pass_c(Page(page.path, bad.splitlines()))
        results.append(("A corrupts a real quotation", misses > 0, f"{misses} flagged"))

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
        sink = open("/dev/null", "w") if args.quiet else io
        with contextlib.redirect_stdout(sink):
            positions, sources, links, problems = pass_b(page)
            spans, misses = pass_c(page)
            print(f"--- pass B: {positions} marker positions against {sources} declared sources, "
                  f"{links} markdown links resolved from the page directory, {problems} problems")
            print(f"--- pass C: {spans} quoted spans checked against their cited lines, "
                  f"{misses} not verbatim")
            unflagged = 0
            if args.mutant:
                if misses:
                    print("--- mutants skipped: the real page is not silent")
                    unflagged = 2
                else:
                    for name, flagged, detail in mutants(page):
                        print(f"--- mutant {name}: {'FLAGGED' if flagged else 'MISSED'} ({detail})")
                        unflagged += 0 if flagged else 1
        if args.quiet:
            sink.close()
        total_b += positions
        total_c += spans
        total_problems += problems + misses + unflagged
        total_mutants += unflagged
    print(f"===== TOTAL {len(docs)} page(s): {total_b} marker positions, {total_c} quoted spans, "
          f"{total_problems} problems" + (f" ({total_mutants} undetected mutants)" if args.mutant else ""))
    sys.exit(1 if total_problems else 0)


if __name__ == "__main__":
    main()
