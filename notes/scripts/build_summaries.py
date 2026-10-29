#!/usr/bin/env python3
"""Render notes/gen/summaries/ from the skeleton template and per-family data files.

Reads:
- notes/templates/summaries/summary.md.j2 (the skeleton)
- notes/data/summaries/<NNN>.md (per-family prose with {{seq}} tokens and a quotes block)
- preprints/<dir>/build/<main>.tex preamble (for macro expansion)
- overview.tex (family discipline, title)

Writes: notes/gen/summaries/<NNN>-<slug>.md (flat, no discipline subdirectory)

The renderer is pure over its digest key: it reads the working-tree templates and data
files, resolves each quote through the normalizer, and stages the rendered pages. A second
run with the same inputs produces identical bytes.

Usage: python3 notes/scripts/build_summaries.py [--check-only]
"""
from __future__ import annotations

import pathlib
import re
import sys

import build_catalog as B
import fix_blank_cites as FBC
from catlib import bib as BIB
from catlib import normalizer
from catlib import summaries as CSUM
from catlib import text as CTEXT
from catlib.atomic import Staging, outdir_of, write_atomic
from catlib.paths import ROOT as REPO
from catlib.promote import key_for
from catlib.records import manuscript_store
from jinja2 import Environment, FileSystemLoader

ROOT = pathlib.Path(__file__).resolve().parents[2]
TPL_DIR = ROOT / "notes" / "templates" / "summaries"
DATA_DIR = ROOT / "notes" / "data" / "summaries"
SUMM_DIR = ROOT / "notes" / "gen" / "summaries"

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


def _bib_pre_clean(t: str) -> str:
    """Bibliography-only LaTeX cruft, stripped before the normalizer runs.

    The normalizer is the quote path and must see quote windows untouched, so the
    bibliography's own formatting commands are peeled off here, before
    `normalize_window`. Two shapes need pre-normalization because
    `split_regions` would break them apart: a `\\href{url}{text}` whose title
    carries a `$` (the `$` splits the group, `_href` cannot match across the
    region break), and `\\(X\\)` inline math the region splitter does not read.
    Diacritic accents are NOT handled here — they run in `fold_accents`, the
    shared rule, so a name folds identically in a quote and in a bibliography.
    """
    # \href{url}{text} -> text (before the normalizer: a $ in the title would split the group)
    t = re.sub(r"\\href\s*\{[^}]*\}\s*\{([^}]*)\}", r"\1", t)
    # inline math \( ... \) -> $ ... $ so the region splitter sees it as a math span
    t = re.sub(r"\\\(", "$", t)
    t = re.sub(r"\\\)", "$", t)
    # \doi{10.x} -> doi:10.x
    t = re.sub(r"\\doi\s*\{([^}]*)\}", r"doi:\1", t)
    # \newblock (the entry separator) -> space
    t = re.sub(r"\\newblock\s*", " ", t)
    # \penalty<n> / \allowbreak / page-layout commands -> drop
    t = re.sub(r"\\penalty\s*-?\d*", " ", t)
    t = re.sub(r"\\allowbreak", " ", t)
    t = re.sub(r"\\(?:begingroup|endgroup|par|raggedright|newline|baselineskip|ldots)\b", " ", t)
    t = re.sub(r"\\enlargethispage\s*\{[^}]*\}", " ", t)
    # \texttt{X} / \mbox{X} -> X
    t = re.sub(r"\\(?:texttt|mbox)\s*\{([^}]*)\}", r"\1", t)
    # \em / \emph emphasis toggle -> strip (journal names render as plain prose)
    t = re.sub(r"\\em(?![a-zA-Z])", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _render_bibliography(sources: list[tuple[str, str, str]]) -> str:
    """Build the Bibliography section: one sorted list, full entries, normalized.

    All bibliography sources (deduped by path) are parsed, their entries combined
    into a single list sorted by first-author surname, each entry's bib-specific
    cruft stripped by `_bib_pre_clean`, and the result routed through the normalizer
    so LaTeX → markdown/UTF-8 (one code path with quotes). Returns "" if no
    bibliography source is declared.
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
                title = e["title"] or "(untitled)"
                year = f" ({e['year']})" if e["year"] else ""
                raw.append(f"{author}, {title}{year}")
        elif path.endswith(".tex"):
            for e in _parse_thebibliography(path):
                raw.append(e["text"])

    if not raw:
        return ""

    raw.sort(key=_bib_surname)
    return "\n".join(f"- {normalizer.normalize_window(_bib_pre_clean(t), '')}" for t in raw)


PREAMBLES: dict[str, str] = {}

_INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")


def _collect_preamble(base_path: pathlib.Path, text: str,
                      seen: set[pathlib.Path], depth: int = 0) -> str:
    """Collect the preamble text, following \\input/\\include directives.

    Resolves input files relative to `base_path`'s directory. Each input file
    contributes its text before `\\begin{document}` (or its full text if it has
    none). A `seen` set prevents circular includes; `depth` caps recursion at 8.
    """
    if depth > 8:
        return text
    m = re.search(r"\\begin\{document\}", text)
    pre = text[:m.start()] if m else text
    parts = [pre]
    for im in _INPUT_RE.finditer(pre):
        name = im.group(1)
        if not name.endswith(".tex"):
            name += ".tex"
        ipath = (base_path.parent / name).resolve()
        if ipath in seen or not ipath.is_file():
            continue
        seen.add(ipath)
        itext = ipath.read_text(encoding="utf-8", errors="replace")
        parts.append(_collect_preamble(ipath, itext, seen, depth + 1))
    return "\n".join(parts)


def get_preamble(rel_path: str) -> str:
    """The manuscript preamble (text before \\begin{document}) for macro expansion.

    Follows `\\input`/`\\include` directives so that macros defined in a separate
    preamble file (e.g. `latex/common.tex`) are visible to the macro table.

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
                seen = {main_path.resolve()}
                PREAMBLES[rel_path] = _collect_preamble(main_path, text, seen)
                return PREAMBLES[rel_path]
    text = p.read_text(encoding="utf-8", errors="replace")
    seen = {p.resolve()}
    PREAMBLES[rel_path] = _collect_preamble(p, text, seen)
    return PREAMBLES[rel_path]


_NUMBER_CACHE: dict[tuple[str, str, int], str] = {}


def _main_tex_for(quote_path: str) -> str:
    """The manuscript's main.tex path, derived from a quote's file path."""
    parts = quote_path.split("/")
    if len(parts) >= 4:
        candidate = f"{parts[0]}/{parts[1]}/build/main.tex"
        if (REPO / candidate).is_file():
            return candidate
    return ""


def compute_number(main_path: str, quote_path: str, quote_line: int) -> str:
    """The rendered LaTeX label (e.g. "Theorem 1.1") for a statement at quote_path:quote_line.

    Walks the manuscript in \\input order, counting \\section commands and theorem-like
    \\begin{X} environments up to the target line. Returns "" when the counter setup is
    unresolvable (no \\newtheorem in the preamble, the file is not in the \\input chain, etc.).
    """
    key = (main_path, quote_path, quote_line)
    if key in _NUMBER_CACHE:
        return _NUMBER_CACHE[key]
    result = _compute_number_uncached(main_path, quote_path, quote_line)
    _NUMBER_CACHE[key] = result
    return result


def _compute_number_uncached(main_path: str, quote_path: str, quote_line: int) -> str:
    mp = REPO / main_path
    if not mp.is_file():
        return ""
    text = mp.read_text(encoding="utf-8")
    m = re.search(r"\\begin\{document\}", text)
    if not m:
        return ""
    preamble = text[:m.start()]

    # Find the base theorem env: \newtheorem{X}{Label}[counter]
    base_env = base_label = base_counter = None
    pat = re.compile(
        r"\\newtheorem\s*(?:\[([^\]]*)\])?\{(\w+)\}"
        r"(\{([^}]*)\})?(?:\[([^\]]*)\])?"
    )
    for pm in pat.finditer(preamble):
        if pm.group(4) is not None and base_env is None:
            base_env, base_label, base_counter = pm.group(2), pm.group(4), pm.group(5)
    if not base_env:
        return ""

    # All env names sharing the base counter
    envs = {base_env}
    for pm in pat.finditer(preamble):
        if pm.group(4) is None and pm.group(5) == base_env:
            envs.add(pm.group(2))

    # Walk the \input chain
    body = text[m.start():]
    inputs = re.findall(r"\\(?:input|include|subfile)\{([^}]+)\}", body)
    build_dir = main_path.rsplit("/", 1)[0]
    quote_resolved = (REPO / quote_path).resolve()
    section_no = theorem_no = 0

    for inp in inputs:
        fp = f"{build_dir}/{inp}.tex"
        if not (REPO / fp).is_file():
            base = inp.rsplit("/", 1)[-1]
            cands = list((REPO / build_dir).rglob(f"*{base}*.tex"))
            if len(cands) != 1:
                continue
            fp = str(cands[0])
        is_target = (REPO / fp).resolve() == quote_resolved
        for ln, line in enumerate((REPO / fp).read_text(encoding="utf-8").splitlines(), 1):
            s = line.strip()
            if re.match(r"\\(?:section|chapter)\{", s):
                section_no += 1
                if base_counter == "section":
                    theorem_no = 0
            m2 = re.match(r"\\begin\{(\w+)\}", s)
            if m2 and m2.group(1) in envs:
                theorem_no += 1
                if is_target and ln == quote_line:
                    if base_counter == "section":
                        return f"{base_label} {section_no}.{theorem_no}"
                    return f"{base_label} {theorem_no}"
    return ""


_MARK = re.compile(r"\[S(\d+):(\d+)(?:\u2013(\d+))?\]")


def _label(sid: str, a: int, b: int) -> str:
    """The citation marker string: [S4:67–77] or [S4:67]."""
    return f"[{sid}:{a}\u2013{b}]" if a != b else f"[{sid}:{a}]"


def strip_own_markers(body: str, quotes: dict[int, dict]) -> str:
    """Remove hand-written markers that duplicate a token's own window.

    A marker is "own" when its string equals label(sid, start, end) for some quote row.
    It is stripped only from lines that carry a {{N}} token (inline) or a > {{N}} block
    intro, so broader references in other sentences are preserved.
    """
    own: set[str] = set()
    for row in quotes.values():
        if row["start"] == "0":
            continue
        a, b = int(row["start"]), int(row["end"])
        own.add(_label(row["sid"], a, b))

    lines = body.split("\n")
    targets: set[int] = set()
    for i, line in enumerate(lines):
        if re.search(r"\{\{\d+\}\}", line):
            targets.add(i)
        if re.match(r">\s*\{\{\d+\}\}", line.strip()):
            for j in range(i - 1, max(-1, i - 4), -1):
                if lines[j].strip():
                    targets.add(j)
                    break

    for i in sorted(targets):
        spans = []
        for m in _MARK.finditer(lines[i]):
            if m.group(0) not in own:
                continue
            e = m.end()
            if e < len(lines[i]) and lines[i][e] == ":":
                e += 1
            spans.append((m.start(), e))
        for s, e in reversed(spans):
            lines[i] = lines[i][:s] + lines[i][e:]
        lines[i] = re.sub(r"\s{2,}", " ", lines[i])
        lines[i] = re.sub(r"\s+:", ":", lines[i])
        lines[i] = re.sub(r"^:\s?", "", lines[i])
    return "\n".join(lines)


def resolve_token(token: str, quotes: dict[int, dict], main_tex_map: dict[str, str] | None = None) -> str:
    """Resolve a {{seq}} token to its normalized quote text plus the citation marker.

    The span comes from the data file's quotes block. The marker `label(sid, start, end)`
    is emitted from the same data row, by construction. The theorem number is computed from
    the manuscript's \\input chain when the quote opens a counter env.
    """
    row = quotes.get(int(token))
    if row is None:
        return token
    span = row["span"]
    if not span:
        return ""
    preamble = get_preamble(row["path"])
    number = ""
    if row["start"] != "0" and main_tex_map:
        mt = main_tex_map.get(row["path"], "")
        if mt:
            number = compute_number(mt, row["path"], int(row["start"]))
    fenced = row["path"].endswith(".lean")
    if fenced:
        # Lean source is code, not prose: the normalizer's space-collapse and
        # brace-strip corrupt it. Fence the raw span verbatim.
        text = "```lean\n" + span + "\n```"
    else:
        text = normalizer.normalize_window(span, preamble, number)
    if row["start"] != "0":
        a, b = int(row["start"]), int(row["end"])
        label = _label(row["sid"], a, b)
        text += ("\n" if fenced else " ") + label
    return text


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

    # The main.tex for each source path, so resolve_token can compute the
    # rendered statement number (Theorem 1.1) by walking the \input chain.
    main_tex_map: dict[str, str] = {}
    for _sid, path, _role in sources:
        mt = _main_tex_for(path)
        if mt:
            main_tex_map[path] = mt

    # Resolve quote tokens in each section body. The hand-written markers that
    # duplicate a token's own window are stripped first (while the {{N}} token is
    # still visible for line location), then the token is resolved to the span text
    # plus its own-window marker, emitted from the same data row, then bare [S#]
    # markers are expanded to [S#:start-end] when unambiguous.
    resolved: dict[str, str] = {}
    for key, body in sections.items():
        stripped = strip_own_markers(body, quotes)

        def _replace(m: re.Match[str]) -> str:
            prefix = m.group(1) or ""
            resolved = resolve_token(m.group(2), quotes, main_tex_map)
            # A code fence cannot sit inside a blockquote: the `> ` prefix the
            # author wrote lands on the fence opener only, leaving the body and
            # closing fence outside the quote and breaking the block. A fenced
            # quote is a code block, not a blockquote, so drop the prefix.
            if prefix and resolved.startswith("```"):
                return resolved
            return prefix + resolved
        text = re.sub(r"(?:(> ))?\{\{(\d+)\}\}", _replace, stripped)
        resolved[key] = expand_bare_markers(text, quotes)

    # Expand manuscript macros in the body's own math regions. The quote path
    # does this through normalize_window; the body path had no equivalent, so
    # a macro the manuscript defines (\eps, \F, ...) rendered raw in prose.
    # The union preamble is the concatenation of every manuscript source's
    # preamble, so a multi-manuscript family sees all its macros.
    body_preamble = "\n".join(
        get_preamble(path) for _sid, path, _role in sources
        if path.startswith("preprints/")
    )
    if body_preamble:
        resolved = {k: normalizer.normalize_body_math(v, body_preamble)
                    for k, v in resolved.items()}

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
        # is unchanged - `--` and the en-dash slugify to the same `-`.
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


def _ledger_sums() -> dict[str, int]:
    """Column sums over notes/gen/tables/catalog.tsv."""
    import csv
    p = REPO / "notes" / "gen" / "tables" / "catalog.tsv"
    sums = {"fams": 0, "paps": 0, "paps_form": 0, "scope_notes": 0,
            "chal": 0, "mainres": 0, "mainres_fams": 0}
    with open(p, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            sums["fams"] += 1
            sums["paps"] += int(row["paps"])
            sums["paps_form"] += int(row["paps_form"])
            if int(row["scope_note"]) > 0:
                sums["scope_notes"] += 1
            sums["chal"] += int(row["chal"])
            sums["mainres"] += int(row["mainres"])
            if int(row["mainres"]) > 0:
                sums["mainres_fams"] += 1
    return sums


def generate_readme(fams: dict[str, dict], page_slugs: dict[str, str]) -> str:
    """Render the summaries index README from the ledger and the page set.

    ``fams`` is the full family dict from ``parse_overview()`` (the denominator).
    ``page_slugs`` maps fam → slug for pages this build rendered (the numerator).
    Every figure is measured at build time; the page list is ordered by family number.
    """
    s = _ledger_sums()
    n_pages = len(page_slugs)
    n_fams = s["fams"]

    # Ordered page list.
    page_rows = []
    for fam in sorted(page_slugs, key=int):
        slug = page_slugs[fam]
        title = CTEXT.fold_dashes(fams[fam]["title"])
        fname = f"{fam}-{slug}.md"
        page_rows.append(f"- [{fam} — {title}]({fname})")
    page_list = "\n".join(page_rows)

    n_missing = n_fams - n_pages

    text = f"""# Family summary pages

{n_pages} extended summaries, one per family, each built from the manuscript's own LaTeX and
verified by script. The pages are rendered by `build_summaries.py` from a hand-edited data
file and the page skeleton; the checker measures the rendered bytes and writes nothing.

## Coverage, as four layers

The release's own formalization surface is four separate counts, and one percentage over them says
nothing. The numbers are the ledger's, quoted with the rule that yields each:

| Layer | Count | What the count is |
| --- | --- | --- |
| Formalized manuscripts | **{s['paps_form']}** of **{s['paps']}** listed manuscript directories | The per-manuscript formalized flag, counting only listed manuscripts. |
| Scope notes | **{s['scope_notes']}** of **{n_fams}** families | `lean/docs/NNN.md`, each with a `## Scope` section. |
| Comparator challenges | **{s['chal']}** distinct configs | `lean/ComparatorChallenges/*.lean` files, each a challenge **stub** with a `sorry` body. |
| `main_results` entries | **{s['mainres']}** entries over reaching **{s['mainres_fams']}** of {n_fams} families | `lean/formalization.yaml`'s `main_results:` list. |

The summaries are a fifth layer: **{n_pages}** of **{n_fams}** families have a page.

## The pages

{page_list}

## The checker

```
python3 notes/scripts/verify_summaries.py
```

It resolves every `[Sn:line]` marker against the shipped file, checks every quotation against the
lines it cites, counts a Sources-table `File` cell that resolves under both roots as a problem, and
writes nothing. Its self-tests are in `notes/scripts/tests/test_summaries.py`, run by
`python3 notes/scripts/run_tests.py notes/scripts/tests/test_summaries.py -q`.

Three more tools read the pages: `check_summary_manuscripts.py` reports which manuscripts each page
reads and whether the release still names them, `locate_summary_quotes.py` (takes a page path)
reports where a quotation's text actually sits when the checker flags a miss, and
`read_manuscript.py` takes a `preprints/` directory name and prints the abstract, the section
skeleton and the titled statement environments with anchors. All three write nothing.

This page is link-only: it names no manuscript directory and cites no family-keyed file, so the
checker's manuscript-directory pass and its family-citation pass skip it. Its links are checked.

## Not checked

- **{n_missing} families have no summary page.** The {n_pages} pages cover {n_pages} of {n_fams} families; the rest are recorded
  in the ledger and the index, not summarized.
- **The coverage counts are the release's own.** The yaml's `scope`, `automation` and `review` fields
  state partial progress, the agent method, and an unchecked review — those are the release's claims, not
  verified results. Zero `sorry` in a formalized file is not a comparator pass, and it does not mean the
  library elaborates.
- **No page was checked by running Lean.** Nothing in this repo builds, and a Lean run would prove the
  formalized statement, not the manuscript's theorem.
"""
    return text


def main() -> int:
    check_only = "--check-only" in sys.argv

    key = key_for("build_summaries.py", tuple(sys.argv[1:]))
    st = Staging("build_summaries", key, outdir_of(sys.argv[1:]))

    _order, fams = B.parse_overview()

    # Find all family pages that have a data file.
    data_files = sorted(DATA_DIR.glob("*.md"))
    print(f"data files: {len(data_files)}")

    problems = 0
    pages_written = 0
    written: set[pathlib.Path] = set()
    page_slugs: dict[str, str] = {}
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
        # Auto-fix blank-line citations so the render sees corrected markers.
        src_map = {sid: path for sid, path, _r in sources}
        fixed_text, nfix = FBC.fix_text(data_text, src_map)
        if nfix:
            data_text = fixed_text
            if not check_only:
                write_atomic(df, data_text)
            print(f"  {fam}: {nfix} blank citation(s) auto-fixed")
        page_text, slug = render_page(fam, info, data_text)
        out = SUMM_DIR / f"{fam}-{slug}.md"
        if not check_only:
            st.stage(out, page_text)
        written.add(out)
        page_slugs[fam] = slug
        pages_written += 1
        # Quick sanity: count unresolved tokens.
        unresolved = len(re.findall(r"\{\{\d+\}\}", page_text))
        if unresolved:
            print(f"  {fam}: {unresolved} UNRESOLVED TOKENS")
            problems += 1

    # The artifact tree is notes/gen/summaries/, which also carries the index README.
    # It is generated from the ledger and the rendered page set, ordered by family number.
    readme = SUMM_DIR / "README.md"
    readme_text = generate_readme(fams, page_slugs)
    if not check_only:
        st.stage(readme, readme_text)
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
