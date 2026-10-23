#!/usr/bin/env python3
"""Render notes/summaries/ from the skeleton template and per-family data files.

Reads:
- notes/templates/summaries/summary.md.j2 (the skeleton)
- notes/data/summaries/<NNN>.md (per-family prose with {{seq}} tokens and a quotes block)
- preprints/<dir>/build/<main>.tex preamble (for macro expansion)
- overview.tex (family discipline, title)

Writes: notes/summaries/<discipline>/<NNN>-<slug>.md (60 pages)

The renderer is pure over its digest key: it reads the working-tree templates and data
files, resolves each quote through the normalizer, and stages the rendered pages. A second
run with the same inputs produces identical bytes.

Usage: python3 notes/scripts/build_summaries.py [--check-only]
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notes" / "scripts"))

import build_catalog as B  # noqa: E402
from catlib import bib as BIB  # noqa: E402
from catlib import normalizer  # noqa: E402
from catlib import summaries as CSUM  # noqa: E402
from catlib import text as CTEXT  # noqa: E402
from catlib.atomic import Staging  # noqa: E402
from catlib.paths import ROOT as REPO  # noqa: E402
from catlib.promote import key_for  # noqa: E402
from catlib.records import manuscript_store  # noqa: E402
from jinja2 import Environment, FileSystemLoader  # noqa: E402

TPL_DIR = ROOT / "notes" / "templates" / "summaries"
DATA_DIR = ROOT / "notes" / "data" / "summaries"
SUMM_DIR = ROOT / "notes" / "summaries"

ENV = Environment(loader=FileSystemLoader(str(TPL_DIR)),
                  keep_trailing_newline=True,
                  trim_blocks=True, lstrip_blocks=True, autoescape=False)


def slugify(title: str) -> str:
    """The index page's mechanical slug for a family title.

    The order matters: NFKD before brace expansion, so that an escaped
    character like `\\'e` is decomposed to `e` + combining accent, the
    combining mark is stripped, and only then does the brace rule see the
    clean letter. `build_index.slug` carries the same order; a summary
    page whose slug diverges from the index page's slug is a dead
    breadcrumb link.
    """
    import unicodedata
    t = unicodedata.normalize("NFKD", title)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"\\[A-Za-z]{1,2}\{([^{}]*)\}", r"\1", t)
    t = t.replace("$", "").replace("'", "").replace("\u2019", "")
    t = re.sub(r"\\[A-Za-z]+\*?", "", t)
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t.removeprefix("the-")


def disc_slug(discipline: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", discipline.lower()).strip("-")


def _parse_bibtex(path: str) -> list[dict[str, str]]:
    """Parse a .bib file into a list of {key, type, author, title, year} dicts."""
    p = REPO / path
    if not p.is_file():
        return []
    text = BIB.read(p)
    out = []
    for etype, key, body, _line in BIB.entries(text):
        out.append({
            "key": key,
            "type": etype,
            "author": BIB.field(body, "author") or "",
            "title": BIB.field(body, "title") or "",
            "year": BIB.field(body, "year") or "",
        })
    return out


def _parse_thebibliography(path: str) -> list[dict[str, str]]:
    """Parse a \\begin{thebibliography} block into a list of {key, text} dicts.

    The entries are \\bibitem{key} followed by free text until the next \\bibitem
    or \\end{thebibliography}. No BibTeX field structure exists in this form.
    """
    p = REPO / path
    if not p.is_file():
        return []
    text = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"\\begin\{thebibliography\}[^}]*\}", text)
    if not m:
        return []
    block_end = re.search(r"\\end\{thebibliography\}", text[m.end():])
    block = text[m.end(): m.end() + block_end.start()] if block_end else text[m.end():]
    # \bibitem comes in two forms: \bibitem{key} and \bibitem[optlabel]{key}.
    # The key is always in the final brace group, so the optional label is skipped.
    items = re.split(r"\\bibitem\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}", block)
    # items[0] is the preamble before the first \bibitem; then alternating key, text
    out = []
    for i in range(1, len(items) - 1, 2):
        key = items[i].strip()
        entry_text = re.sub(r"\s+", " ", items[i + 1].strip()).strip()
        out.append({"key": key, "text": entry_text})
    return out


def _bib_surname(raw: str) -> str:
    """First-author surname for sorting.

    The corpus uses two author naming conventions: BibTeX style (`Last, First`) and
    thebibliography prose style (`F. Last`). Both are handled: for the first form, the
    surname is the last word before the first comma; for the second, it is the last word
    (the given name precedes). The accent fold runs before the escape strip so that
    `Andr{\'e}` becomes `Andre` (not `Andr` + `e`).
    """
    comma = raw.find(",")
    head = raw[:comma] if comma > 0 else raw
    folded = CTEXT.fold_accents(head)
    words = re.sub(r"[~\\{}'\"\x27]", " ", folded).split()
    return words[-1].lower() if words else ""


def _render_bibliography(sources: list[tuple[str, str, str]]) -> str:
    """Build the Bibliography section: one sorted list, full entries, normalized.

    All bibliography sources (deduped by path) are parsed, their entries combined
    into a single list sorted by first-author surname, and each entry routed
    through the normalizer so LaTeX → markdown/UTF-8 (one code path with quotes).
    Returns "" if no bibliography source is declared.
    """
    seen: set[str] = set()
    raw: list[str] = []
    for _sid, path, _role in sources:
        if path in seen:
            continue
        seen.add(path)
        if path.endswith(".bib"):
            for e in _parse_bibtex(path):
                author = e["author"].replace(" and ", ", ") if e["author"] else ""
                title = e["title"] if e["title"] else "(untitled)"
                year = f" ({e['year']})" if e["year"] else ""
                raw.append(f"{author}, {title}{year}")
        elif path.endswith(".tex"):
            for e in _parse_thebibliography(path):
                raw.append(e["text"])

    if not raw:
        return ""

    raw.sort(key=_bib_surname)
    return "\n".join(f"- {normalizer.normalize_window(t, '')}" for t in raw)


PREAMBLES: dict[str, str] = {}


def get_preamble(rel_path: str) -> str:
    """The manuscript preamble (text before \\begin{document}) for macro expansion.

    For non-LaTeX sources (README, .md, .lean, .bib, overview.tex), the preamble is
    empty — no macros to expand.
    """
    if rel_path in PREAMBLES:
        return PREAMBLES[rel_path]
    p = REPO / rel_path
    if not p.is_file() or p.suffix != ".tex":
        PREAMBLES[rel_path] = ""
        return ""
    # Use the main .tex in the same manuscript dir for the macro table.
    if "preprints/" in rel_path:
        parts = rel_path.split("/")
        ms_dir = parts[1]
        store = manuscript_store()
        rec = store.get(ms_dir)
        if rec and rec["main"]:
            main_path = REPO / rec["main"]
            if main_path.is_file():
                text = main_path.read_text(encoding="utf-8", errors="replace")
                m = re.search(r"\\begin\{document\}", text)
                PREAMBLES[rel_path] = text[:m.start()] if m else ""
                return PREAMBLES[rel_path]
    text = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"\\begin\{document\}", text)
    PREAMBLES[rel_path] = text[:m.start()] if m else ""
    return PREAMBLES[rel_path]


def resolve_token(token: str, quotes: dict[int, dict]) -> str:
    """Resolve a {{seq}} token to its normalized quote text.

    The span comes from the data file's quotes block, not from quotes.tsv: the data file is the
    quote source, so the renderer reads no artifact any other writer produces. That is what breaks
    the seed->render cycle (the renderer is a root, depending only on hand-maintained data).
    """
    row = quotes.get(int(token))
    if row is None:
        return token  # Unresolvable: leave the token as-is
    span = row["span"]
    if not span:
        return ""
    preamble = get_preamble(row["path"])
    return normalizer.normalize_window(span, preamble)


def expand_bare_markers(body: str, quotes: dict[int, dict]) -> str:
    """Expand bare [S#] markers to [S#:start–end] when unambiguous.

    A bare marker carries no line number (e.g. ``[S5]`` not ``[S5:23–26]``).
    When exactly one quote exists for that source ID in the quotes block, the
    renderer expands it using that quote's start and end lines. Zero or
    multiple quotes leave the marker as-is (ambiguous).
    """
    sid_quotes: dict[str, list[tuple[str, str]]] = {}
    for row in quotes.values():
        if row["start"] == "0":
            continue  # Unlocated quote (measured negative) — no line window to expand to.
        sid_quotes.setdefault(row["sid"], []).append((row["start"], row["end"]))

    def _replace(m: re.Match[str]) -> str:
        if m.group(2) is not None:
            return m.group(0)  # Already has a line number.
        sid = f"S{m.group(1)}"
        entries = sid_quotes.get(sid, [])
        if len(entries) == 1:
            start, end = entries[0]
            if start == end:
                return f"[{sid}:{start}]"
            return f"[{sid}:{start}\u2013{end}]"
        return m.group(0)

    return CSUM.MARKER.sub(_replace, body)


def parse_data_file(text: str) -> tuple[list[tuple[str, str, str]], dict[str, str], str, dict[int, dict]]:
    """Parse a data file into (sources, sections, slug, quotes).

    Returns:
    - sources: list of (sid, path, role)
    - sections: dict of canonical_name -> body text
    - slug: the page's slug, carried from the committed page filename (the data
      file's ``<!-- slug ... -->`` line), not recomputed from the overview title.
    - quotes: dict of seq -> {which, path, start, end, span}, the data file's
      ``<!-- quotes`` block with each row's ``sid`` resolved to its source path.
    """
    sources: list[tuple[str, str, str]] = []
    sections: dict[str, str] = {}
    slug = ""
    quotes: dict[int, dict] = {}

    lines = text.split("\n")
    i = 0
    # Parse the sources block.
    if i < len(lines) and lines[i].strip() == "<!-- sources":
        i += 1
        while i < len(lines) and lines[i].strip() != "-->":
            parts = lines[i].split("\t")
            if len(parts) >= 3:
                sources.append((parts[0], parts[1], parts[2]))
            i += 1
        i += 1  # skip -->
    # Skip the blank line the extractor emits between blocks; a strict next-line check would
    # miss the quotes block and every token would render as its bare number.
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    # Parse the quotes block, which follows the sources block: one row per quote token,
    # `seq  which  sid  start  end  span`. The `sid` resolves to a source path below. A
    # quote's span may run across several physical lines (the source window is wrapped), and
    # the data file stores it that way; every line after a row's first line, up to the next
    # row, is a continuation of the most recent quote's span and is appended newline-joined.
    # A continuation line is one whose first tab-field is not a positive integer — including
    # an interior blank line in the window, so the check is on row-ness, not field count.
    if i < len(lines) and lines[i].strip() == "<!-- quotes":
        i += 1
        cur_seq: int | None = None
        while i < len(lines) and lines[i].strip() != "-->":
            line = lines[i]
            parts = line.split("\t")
            seq_field = parts[0].strip() if parts else ""
            if len(parts) >= 6 and re.fullmatch(r"\d+", seq_field) is not None:
                cur_seq = int(seq_field)
                quotes[cur_seq] = {"which": parts[1], "sid": parts[2],
                                   "start": parts[3], "end": parts[4],
                                   "span": "\t".join(parts[5:])}
            elif cur_seq is not None:
                quotes[cur_seq]["span"] += "\n" + line
            i += 1
        i += 1  # skip -->
    # Parse the slug line, which sits between the family line and the sections.
    for line in lines:
        m = re.match(r"^<!-- slug (.+?) -->$", line.strip())
        if m:
            slug = m.group(1)
            break

    # Resolve each quote's sid to its source path.
    sid2path = {sid: path for sid, path, _role in sources}
    for row in quotes.values():
        row["path"] = sid2path.get(row["sid"], "")

    # Parse sections.
    current_key = ""
    current_lines: list[str] = []
    for line in lines[i:]:
        m = re.match(r"^## (\S+)$", line)
        if m:
            if current_key:
                sections[current_key] = "\n".join(current_lines).strip()
            current_key = m.group(1)
            current_lines = []
        elif line.strip() == "<!-- family" or line.strip() == "":
            if current_key:
                current_lines.append(line)
        elif current_key:
            current_lines.append(line)
    if current_key:
        sections[current_key] = "\n".join(current_lines).strip()

    return sources, sections, slug, quotes


def lines_of(path: str) -> str:
    """The line count of a file as a string, or '—' if it doesn't exist."""
    p = REPO / path
    if not p.is_file():
        return "—"
    return str(len(p.read_text(encoding="utf-8", errors="replace").splitlines()))


def render_page(fam: str, info: dict, data_text: str) -> tuple[str, str]:
    """Render one family's summary page. Returns (page_text, slug).

    The quote spans come from the data file's quotes block (parsed inside
    ``parse_data_file``), so the renderer reads no artifact any other writer
    produces — it is a root, and the seed->render cycle it used to form is gone.
    """
    discipline = info["discipline"]
    title = info["title"]
    ds = disc_slug(discipline)

    sources, sections, _stored_slug, quotes = parse_data_file(data_text)
    # The slug is always derived from the ledger title, never from the data file's stored
    # line: the data file's slug is a transcription and drifts from the index page's slug
    # the moment the title changes. The index uses build_index.slug (NFKD-first); this
    # slugify carries the same order, so a summary page's filename is its index page's.
    slug = slugify(title)

    # Resolve quote tokens in each section body, then expand bare [S#] markers
    # to [S#:start–end] when the quotes block gives exactly one window for that
    # source ID.
    resolved: dict[str, str] = {}
    for key, body in sections.items():
        def _replace(m: re.Match[str]) -> str:
            return resolve_token(m.group(1), quotes)
        text = re.sub(r"\{\{(\d+)\}\}", _replace, body)
        resolved[key] = expand_bare_markers(text, quotes)

    # Build the Sources table rows. The File cell is a markdown link whose label is the
    # backticked repo-relative path: the checker reads the first backticked text in the cell
    # as the path (catlib.summaries.CELL), so the label keeps the backticks and the href is
    # the page-relative target. A paren-bearing path is angle-bracket-wrapped so the href is
    # not misread at its first ')'. This merges what was a separate Links section into the
    # Sources table, so the cell is both the path and its link.
    src_rows: list[str] = []
    for sid, path, role in sources:
        lc = lines_of(path)
        href = f"../../../{path}"
        if "(" in path or ")" in path:
            href = f"<{href}>"
        src_rows.append(f"| {sid} | [`{path}`]({href}) | {lc} | {role} |")

    # Build the Bibliography section from the sources that declare a .bib or a
    # thebibliography block. Empty when no bibliography source is declared.
    bibliography = _render_bibliography(sources)

    # Render through the skeleton.
    template = ENV.get_template("summary.md.j2")
    page_text = template.render(p={
        "discipline": discipline,
        "disc_slug": ds,
        "fam": fam,
        "slug": slug,
        # The overview title carries LaTeX dashes (`M\'ezard--Parisi`); the accent is already
        # folded by parse_overview, so the remaining `--` needs the same dash rule as prose.
        # The slug is derived from the raw title above (before this fold), so the filename
        # is unchanged — `--` and `–` slugify to the same `-`.
        "title": CTEXT.fold_dashes(title),
        "contents": resolved.get("contents", ""),
        "headline": resolved.get("headline", ""),
        "undergraduate": resolved.get("undergraduate", ""),
        "graduate": resolved.get("graduate", ""),
        "history": resolved.get("history", ""),
        "consequences": resolved.get("consequences", ""),
        "section_skeleton": resolved.get("section_skeleton", ""),
        "formalized": resolved.get("formalized", ""),
        "coverage": resolved.get("coverage", ""),
        "sources_rows": "\n".join(src_rows),
        "bibliography": bibliography,
    })
    return page_text, slug


def main() -> int:
    check_only = "--check-only" in sys.argv

    key = key_for("build_summaries.py", tuple(sys.argv[1:]))
    st = Staging("build_summaries", key)

    _order, fams = B.parse_overview()

    # Find all family pages that have a data file.
    data_files = sorted(DATA_DIR.glob("*.md"))
    print(f"data files: {len(data_files)}")

    problems = 0
    pages_written = 0
    written: set[pathlib.Path] = set()
    for df in data_files:
        fam = df.stem  # e.g. "195"
        if fam not in fams:
            print(f"  {fam}: NOT IN OVERVIEW")
            problems += 1
            continue
        info = fams[fam]
        data_text = df.read_text(encoding="utf-8")
        # Flag declared source paths that do not exist on disk.
        sources, _s, _sl, _q = parse_data_file(data_text)
        for sid, path, _role in sources:
            if not (REPO / path).is_file():
                print(f"  {fam}: {sid} MISSING SOURCE {path}")
                problems += 1
        page_text, slug = render_page(fam, info, data_text)
        out = SUMM_DIR / disc_slug(info["discipline"]) / f"{fam}-{slug}.md"
        if not check_only:
            st.stage(out, page_text)
        written.add(out)
        pages_written += 1
        # Quick sanity: count unresolved tokens.
        unresolved = len(re.findall(r"\{\{\d+\}\}", page_text))
        if unresolved:
            print(f"  {fam}: {unresolved} UNRESOLVED TOKENS")
            problems += 1

    # The artifact tree is notes/summaries/, which also carries the index README. It is not a
    # family page, so the renderer passes it through unchanged: a cache entry for it must exist
    # (verify_cache_promotion.py Pass C) and its bytes must equal the tracked bytes.
    readme = SUMM_DIR / "README.md"
    if readme.is_file():
        if not check_only:
            st.stage(readme, readme.read_text(encoding="utf-8"))
        written.add(readme)

    if not check_only:
        st.promote()
        # A page whose title changed is written under a new slug, so the old page survives on
        # disk and its breadcrumb link is dead. The tree is generated, so anything this build
        # did not write is stale and is removed (the same sweep build_index.py runs over its tree).
        stale = sorted(p for p in SUMM_DIR.rglob("*.md") if p not in written)
        for p in stale:
            p.unlink()
        for d in sorted((x for x in SUMM_DIR.rglob("*") if x.is_dir()),
                        key=lambda x: -len(x.parts)):
            if not any(d.iterdir()):
                d.rmdir()
        print(f"stale swept       {len(stale)} files")

    print(f"pages rendered: {pages_written}")
    print(f"problems: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
