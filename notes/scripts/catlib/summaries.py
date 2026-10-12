"""The summary-page read shape: family number, Sources table, `[Sn:line]` markers, manuscript roots.

A page is `notes/summaries/<discipline>/<NNN>-<slug>.md`; the family number is the first token of the
file name. The body cites sources as `[S4:29]`, `[S4:29–56]` or `[S4]`; a Sources table at the bottom
maps `S#` to a backticked file, a declared line count, and a description. A relative path in the table
resolves against the manuscript root the page declares, with the repository root as fallback.

Measured 2026-10-10 over the **21** pages: **566** table rows, **0** rows with no backticked File cell,
**0** File cells resolving under both roots, exactly **1** table block per page, and all 21 pages use
all three marker forms (bare, single line, range). The row grammar is uniform, so one parser covers the
fleet. Two surfaces are not uniform, and neither is a parse: the header separator ships in **2** byte
forms (`|---|---|---|---|` 13 pages, `| --- | --- | --- | --- |` 8), and the root-declaring prose ships
in **13** forms — `Manuscript root: ` (6 pages), `Manuscript root — ` (2), "The three / eight / four
manuscript roots" (4), "Both manuscript roots" (1), and **5** pages whose first backticked
`preprints/` path is a table row, not prose. **5** pages declare more than one root. The root rule that
covers all 21 is the first backticked `preprints/...` path anywhere in the page; a rule keyed on the
`Manuscript root — ` phrase fires on **2** pages and reports "no declared root" on **19**, which is why
this module does not use that phrase.

The lenient read of a declared source lives here deliberately: a page may declare a compiled PDF as a
source and the run must not abort. Bytes that are not text decode to replacement characters, so a
quotation cited to a PDF fails the verbatim test, which is the honest result — its text is not
extractable. This is not `catlib.paths.read_text`.

Globbing `preprints/*` is deliberately not a rule: `build/main.tex`, `references.tex` and `README.md`
exist in many manuscript trees, so a File cell that resolves under both roots is counted as ambiguous
by the checker, not guessed.
"""

from __future__ import annotations

import re
from pathlib import Path

from catlib.overview import parse_overview
from catlib.paths import PREPRINTS, ROOT

# The page grammar: table row, File cell, citation marker, quotation, link, stray HTML, manuscript dir.
ROW = re.compile(r"^\|\s*(S\d+)\s*\|\s*(.+?)\s*\|\s*([\d,]+|—)\s*\|\s*(.*?)\s*\|\s*$")
CELL = re.compile(r"`([^`]+)`")
MARKER = re.compile(r"\[S(\d+)(?::(\d+)(?:[–-](\d+))?)?\]")
QUOTE = re.compile(r"“([^”]{6,})”|\"([^\"]{6,})\"")
LINK = re.compile(r"\]\(([^)\s]+)\)")
ENTITY = re.compile(r"&(#[0-9]+|[a-zA-Z][a-zA-Z0-9]*);")
TAG = re.compile(r"<[a-zA-Z/][^>]*>")
PAPDIR = re.compile(r"preprints/([^/`\s]+)/")

FAM = re.compile(r"(\d{1,3})-")
ROOTPATH = re.compile(r"`(preprints/[^`]+)`")

# The Sources preamble demonstrates the marker syntax ("[S2:31] for one line"). Those tokens are an
# example of the format, not a citation, so the unit that carries them makes no claim to check.
FORMAT_EXAMPLE = "cited in the body as"
# A prior paragraph is explicitly labelled as the assistant's training-data memory, not repo text, so
# nothing inside it is a quotation of a source.
PRIOR = "Prior (my training data"


def page_fam(name: str) -> str | None:
    """The family number a page name carries, in the ledger's zero-padded form."""
    m = FAM.match(name)
    return m.group(1) if m else None


def declared_root(lines: list[str]) -> Path | None:
    """The manuscript root the page declares — the first backticked `preprints/` path anywhere.

    Not the `Manuscript root — ` phrase: that prose ships in 13 forms and 5 pages declare their root
    inside a table row, so the phrase rule sees 2 of the 21 pages.
    """
    for line in lines:
        m = ROOTPATH.search(line)
        if m:
            return ROOT / m.group(1)
    return None


def page_dirs(path: Path) -> tuple[list[str], str | None]:
    """Manuscript directory names a page spells, and the directory its declared root names."""
    lines = path.read_text(encoding="utf-8").splitlines()
    dirs = sorted(set(PAPDIR.findall("\n".join(lines))))
    root = declared_root(lines)
    return dirs, (root.name if root and root.is_dir() else None)


def named_dirs() -> dict[str, set[str]]:
    """`{manuscript dir: families whose overview entry names it}` — the release's own claim.

    A directory on disk that this map does not carry is a superseded manuscript: an upstream update
    ships a new dated directory and leaves the old one tracked, so both are real and the filesystem
    cannot tell them apart.
    """
    _, fams = parse_overview()
    out: dict[str, set[str]] = {}
    for fam, d in fams.items():
        for p in d["tex_paps"]:
            out.setdefault(p.split("/")[1], set()).add(fam)
    return out


def superseded_dir() -> str | None:
    """A manuscript directory on disk that no family names — the shape an update leaves behind."""
    named = named_dirs()
    for p in sorted(PREPRINTS.iterdir()):
        if p.is_dir() and p.name not in named:
            return p.name
    return None


class Page:
    """A summary page plus the Sources table that resolves its markers."""

    def __init__(self, path: Path, lines: list[str]) -> None:
        self.path = path
        self.lines = lines
        self.cache: dict[str, list[str]] = {}
        self.table: dict[str, tuple[str, Path | None]] = {}
        self.rows: list[tuple[str, str, str, int]] = []
        self.ambiguous: list[tuple[str, str, list[Path]]] = []
        self.fam = page_fam(path.name)
        pre = declared_root(lines)
        self.roots = ([pre] if pre and pre.is_dir() else []) + [ROOT]
        self._read_table()

    def _read_table(self) -> None:
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

    def lines_of(self, sid: str) -> list[str]:
        rel, path = self.table[sid]
        if path is None:
            # Callers filter this: pass B flags a File cell that resolves to no file before it
            # reads, pass C works through usable(), and the refresh script drift-flags it.
            return []
        if rel not in self.cache:
            # A page may declare a compiled PDF as a source. Reading it must not abort the run:
            # bytes that are not text decode to replacement characters, so a quotation cited to a
            # PDF fails the verbatim test, which is the honest result - its text is not extractable.
            self.cache[rel] = path.read_text(encoding="utf-8", errors="replace").splitlines()
        return self.cache[rel]


def markers(text: str) -> list[tuple[int, str, int | None, int | None]]:
    """Citations in source order: (offset, S#, first line or None for the whole file, last line)."""
    out: list[tuple[int, str, int | None, int | None]] = []
    for m in MARKER.finditer(text):
        a = int(m.group(2)) if m.group(2) else None
        b = int(m.group(3)) if m.group(3) else a
        out.append((m.start(), f"S{m.group(1)}", a, b))
    out.sort()
    return out


def units(doc_lines: list[str]) -> list[tuple[int, str, bool]]:
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


def usable(page: Page, cites: list[tuple[int, str, int | None, int | None]]) -> list[tuple[int, str, int | None, int | None]]:
    """Citations whose source is in the table and resolves to a file on disk."""
    return [c for c in cites if c[1] in page.table and page.table[c[1]][1] is not None]


def candidates(page: Page, unit: str, start_line: int, is_bq: bool) -> list[tuple[str, int | None, int | None]]:
    """The citations a unit is attributed to, in source order: `(S#, first line or None, last line)`.

    A block quote is attributed by the citation on the line **above** it, walking back at most three
    lines and taking the first line that carries a usable citation; a prose unit is attributed by the
    markers inside it. A citation whose source is not in the table, or resolves to no file, is not a
    candidate. This is the rule `verify_summaries.py` pass C, `locate_summary_quotes.py` and
    `seed_quotes.py` all run, so a span one of them attributes is the span the others attribute.
    """
    if is_bq:
        for back in range(start_line - 2, max(start_line - 5, -1), -1):
            res = usable(page, markers(page.lines[back]))
            if res:
                return [(sid, a, b) for _, sid, a, b in res]
        return []
    return [(sid, a, b) for _, sid, a, b in usable(page, markers(unit))]


def spans_of(unit: str, is_bq: bool) -> list[str]:
    """The quoted spans a unit carries: the whole block quote, or the prose quotations of 12+ chars.

    A span under 12 characters is a term under discussion ("proves"), not a quotation, and a block
    quote is one span: its lines are already joined by `units`.
    """
    if is_bq:
        return [unit]
    return [m.group(1) or m.group(2) for m in QUOTE.finditer(unit)
            if len(m.group(1) or m.group(2)) >= 12]


def label(sid: str, a: int | None, b: int | None) -> str:
    return f"{sid}:{a}" + (f"-{b}" if b != a and a is not None else "") if a else f"{sid} (file)"
