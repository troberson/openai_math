#!/usr/bin/env python3
"""Verify notes/scripts/README.md: the ownership manifest for every file under notes/.

Passes:
  A. Derive the writer set from the scripts' own source and match the page's writer table.
  B. Enumerate every file under notes/ (scripts excluded), classify each by the page's rules,
     and flag any file no rule owns.
  C. Re-measure the census and match every count in the page's tables.
  D. Require every script to be named in the page and in the notes/README.md command block,
     and re-derive the "named before this pass" gap from the commit that created this page.
  E. Recompute the shared-basename sets and match the page.
  F. Layout: no preamble, a "## Not checked" section, and no self-reference in the checker table.
  G. Sync. notes/README.md -- the one page this checker reads that the writer generates -- is compared
     with notes/scripts/render_reports.py's render of it. notes/scripts/README.md is hand-authored, so
     it has no render to compare with; the generated ledger readme does, and its prose is not covered
     by any count phrase here.
  H. notes/development/templates.md -- the census of the two template trees. Lines, bytes and slot
     counts are re-measured here from the template files, the page<->checker pairing is re-read from the
     ALL_PAGES literal in `catlib/templates.py`, and the index tree's render counts are re-counted
     from notes/index/. The pass re-measures rather than importing measure_templates.py: a checker
     that re-derives a count through the same code the page's writer calls proves only that the code
     agrees with itself.

The self-tests are not here: they live in `notes/scripts/tests/test_script_ownership.py`, which
mutates page text in memory and asserts each fault is caught by the check that owns it. Passes H
and G take the page text as an argument, so no page is written by the checker or by the tests.
Report-only: writes nothing.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys

from catlib import render as RD
from catlib.atomic import RECORDS_ROOT
from catlib.paths import GATE_ROWS_TSV, NOTES, ROOT, SCRIPTS, read_text
from catlib.promote import CHECKER_L1, key_for

PAGE = SCRIPTS / "README.md"
SELF = "verify_script_ownership.py"
README = NOTES / "README.md"
TEMPLATES_PAGE = NOTES / "development" / "templates.md"
TPL_DIR = NOTES / "templates"
REPORT_TPL_DIR = TPL_DIR / "report"
INDEX_DIR = NOTES / "index"
PROBE_DIR = NOTES / "development" / "probe"
DEV_DIR = NOTES / "development"
REPORTS_DIR = NOTES / "reports"
TABLES_DIR = NOTES / "tables"
SLOT_MARK = "{{ "
# The record-store target the writers table carries. A record's directory is the digest key, which the
# source does not name, so the rule keys on the literal record name — the only part of the path the
# script writes down. The `.qwen/*` rule in `.gitignore` keeps the tree untracked, so this target is
# outside the notes/ census and outside the promote-and-verify byte comparison.
RECORD_PREFIX = ".qwen/cache/records/<key>/"
# The index-tree templates whose pages sit in a directory named for them; family pages sit in the
# 17 discipline directories, and the entry point is a single file.
INDEX_PAGE_DIRS = {"discipline.md.j2": "disciplines", "name.md.j2": "names", "topic.md.j2": "topics"}
INDEX_NON_FAMILY = {"disciplines", "names", "topics", "edges"}

# The page's hand-authored tables, by rule rather than by generator.
HAND_AUTHORED_TSVS = {"notes/tables/topics.tsv", "notes/tables/conjecture-standing.tsv"}

# The self-test entry points, whose page writes are a mutate-and-restore rather than ownership.
SELFTEST_DEF = re.compile(r"^def (?:mutants?|mutant_test|selftest)\(", re.MULTILINE)


def script_names():
    return sorted(p.name for p in SCRIPTS.glob("*.py") if p.name != SELF)


def catlib_census():
    """The catlib import census the census page's read-surface sentence names.

    The rule the page quotes — `^[ \\t]*(from|import) catlib` over each script's own source, a
    deferred import inside a function counts — over the census population (every top-level script
    but this page's own checker). Returns (total, importers, non_importers, per_prefix): the
    importers and the sorted non-importers, and per_prefix the importer count per script name
    prefix (extract_/build_/measure_/check_/verify_), with `plus` for the importers that carry
    none of those prefixes.
    """
    rule = re.compile(r"^[ \t]*(from|import) catlib", re.MULTILINE)
    names = script_names()
    imp: list[str] = []
    non: list[str] = []
    for n in names:
        (imp if rule.search(read_text(SCRIPTS / n)) else non).append(n)
    per_prefix = {"extract_": 0, "build_": 0, "measure_": 0, "check_": 0, "verify_": 0, "plus": 0}
    for n in imp:
        pre = next((k for k in per_prefix if k != "plus" and n.startswith(k)), "plus")
        per_prefix[pre] += 1
    return len(names), imp, sorted(non), per_prefix


def importer_problems(text):
    """The census page's catlib read-surface sentence: N of M scripts import, per the rule the page
    names, with every non-importer named. The page carries the rule, the pass carries the numbers, so
    the sentence is witnessed — a literal the pass re-derives from the scripts' own sources, not a
    hand-swept count. The non-importer list is checked name-for-name (the anchors behind the count),
    not by the count alone."""
    p = []
    total, imp, non, per_prefix = catlib_census()
    if f"**{len(imp)}** of the **{total}** scripts call the package" not in text:
        p.append(
            f"importer sentence does not read '**{len(imp)}** of the **{total}** scripts call the package'"
        )
    for pre, n in per_prefix.items():
        if pre == "plus":
            continue
        if f"**{n}** `{pre}`" not in text:
            p.append(f"the {pre} importer count is not {n}")
    folded = re.sub(r"\s+", " ", text)
    m = re.search(r"scripts that do not are (.*?)(?= The )", folded)
    if not m:
        p.append("no non-importer sentence")
    else:
        # The list is one clause per ';' — `<head names>, which <reason>`. A non-importer's reason
        # can name an importer (`dump_template_slots.py` reaches the slot dict
        # through `render_reports.py`), so a findall over the whole span picks up the embedded name.
        # Each clause's head names precede its "which"; the reason follows it.
        named: set[str] = set()
        for piece in m.group(1).split("; "):
            named.update(re.findall(r"`([a-z_]+\.py)`", piece.split(" which")[0]))
        if sorted(named) != non:
            p.append(f"non-importer list: page names {sorted(named)}, measured {non}")
    return p


def path_constants():
    """The notes/-rooted path constants the shared package defines: name -> repo-relative path.

    The chain is two levels deep now: `TABLES = NOTES / "tables"` and then
    `SOURCES_TSV = TABLES / "sources.tsv"`, so a rule that reads only `NAME = NOTES / "x"` loses the
    eight TSV constants and reports a writer that aliases them as a writer of nothing. Resolve the
    base identifier recursively, keeping only paths that start at `notes/`.
    """
    src = read_text(SCRIPTS / "catlib" / "paths.py")
    decls = {n: (base, re.findall(r'"([^"]+)"', parts))
            for n, base, parts in re.findall(
                r'^(\w+)\s*=\s*(\w+)\s*/\s*((?:"[^"]+"\s*/\s*)*"[^"]+")', src, re.MULTILINE)}
    out: dict[str, str] = {}

    def resolve(name: str, seen: set[str]) -> str | None:
        if name in out:
            return out[name]
        if name in seen or name not in decls:
            return None
        base, quoted = decls[name]
        if base == "ROOT":
            if quoted[0] != "notes":
                return None
            path = "/".join(quoted)
        else:
            pre = resolve(base, seen | {name})
            if pre is None:
                return None
            path = pre + "/" + "/".join(quoted)
        out[name] = path
        return path

    for name in decls:
        resolve(name, set())
    return {n: p for n, p in out.items() if p.startswith("notes")}


def notes_const(src: str, name: str) -> str | None:
    """The repo-relative path a module-level `NAME = ROOT / "notes" / ...` constant carries.

    Every quoted part is joined: `TPL_DIR = ROOT / "notes" / "templates" / "report"` is
    `notes/templates/report` — capturing only the last quoted part reads `notes/report`.
    """
    m = re.search(rf'^{name}\s*=\s*\w+\s*/\s*((?:"[^"]+"\s*/\s*)+"[^"]+")', src, re.MULTILINE)
    if not m:
        return None
    parts = re.findall(r'"([^"]+)"', m.group(1))
    return "/".join(parts) if parts and parts[0] == "notes" else None


def strip_selftest(src: str) -> str:
    """Blank the body of a module-level self-test function.

    A self-test writes the page it checks in order to mutate it, then restores the bytes it read —
    `PAGE.write_text(mutated)` inside the test, `PAGE.write_text(page_text)` in the `finally`. That
    pair leaves the file byte-identical, so it is not ownership: keying the writer rule on the write
    call alone reads a checker's self-test as a generator, and a script whose normal run writes
    nothing lands in the writers table.
    """
    lines = src.splitlines(keepends=True)
    for i in reversed([n for n, l in enumerate(lines) if SELFTEST_DEF.match(l)]):
        j = i + 1
        while j < len(lines) and (lines[j][:1] in (" ", "\t") or not lines[j].strip()):
            j += 1
        lines[i:j] = ["\n"] * (j - i)
    return "".join(lines)


def writer_targets(src: str) -> list[str]:
    """The notes/-rooted targets a script writes, from its own source.

    Five shapes, because a script may open the file itself (`OUT.open("w")`), hand a package
    constant to a package writer (`tsv.write_csv(OUT, COLUMNS, rows)`), build the receiver from a
    module constant (`out = TPL_DIR / (name)`, then `out.write_text(...)`), hand the target to the
    package's atomic writer (`write_atomic(TARGET, text)`), staging writer (`stage(TARGET, text)`) or
    promotion writer (`promote(TARGET, key, text)`), or hand a record name to the keyed store
    (`cached(KEY, "names.json", builder)`). The three package writers are the shape the fleet moved
    to: the write call no longer names a path, so a rule keyed on `open`/`write_text` alone reads a
    writer that stages as a writer of nothing. In each of the three, the target name is resolved the
    same way — package constant, alias of a package constant, or a locally built constant. The store
    is the shape that cannot be resolved that way: its directory is the digest key, which the source
    does not name, so the rule takes the literal record name and prefixes the store root. The write
    calls are read from `strip_selftest(src)`,
    which is the sixth rule: a self-test's mutate-and-restore write is not ownership, so the scripts
    whose only page write sits inside their self-test stay writers of nothing.
    """
    consts = path_constants()
    scan = strip_selftest(src)
    targets = set()
    for var in re.findall(r'([A-Za-z_]\w*)\.(?:open\([^)]*"w"[^)]*\)|write_text\()', scan):
        direct = notes_const(src, var)
        if direct:
            targets.add(direct)
            continue
        hop = re.search(rf"^\s*{var}\s*=\s*([A-Za-z_]\w*)\s*/\s*\(", src, re.MULTILINE)
        if hop:
            base = notes_const(src, hop.group(1))
            if base:
                targets.add(base)
    for const in re.findall(r'\b\w+\.write_\w+\(\s*([A-Za-z_]\w*)\b', src):
        # The script may define the constant itself (`OUT = ROOT / "notes" / "tables" / "catalog.tsv"`), alias
        # the package constant (`OUT = SOURCES_TSV`), or name a package constant directly.
        direct = notes_const(src, const)
        if direct:
            targets.add(direct)
            continue
        alias = re.search(rf"^{const}\s*=\s*([A-Za-z_]\w*)\s*$", src, re.MULTILINE)
        key = alias.group(1) if alias else const
        if consts.get(key):
            targets.add(consts[key])
    for var in re.findall(r"\b(?:write_atomic|stage|promote)\(\s*([A-Za-z_]\w*)\b", scan):
        direct = notes_const(src, var)
        if direct:
            targets.add(direct)
            continue
        if consts.get(var):
            targets.add(consts[var])
            continue
        alias = re.search(rf"^{var}\s*=\s*([A-Za-z_]\w*)\s*$", src, re.MULTILINE)
        key = alias.group(1) if alias else var
        if consts.get(key):
            targets.add(consts[key])
            continue
        hop = re.search(rf"^\s*{var}\s*=\s*([A-Za-z_]\w*)\s*/\s*\(", src, re.MULTILINE)
        if hop:
            base = notes_const(src, hop.group(1))
            if base:
                targets.add(base)
    for rec in re.findall(r'\bcached\(\s*[A-Za-z_]\w*\s*,\s*"([^"]+)"', scan):
        targets.add(RECORD_PREFIX + rec)
    if re.search(r'^\w+\s*=\s*\w+\s*/\s*"notes"\s*/\s*"index"', src, re.MULTILINE) and re.search(
        r"^def write\(", src, re.MULTILINE
    ):
        targets.add("notes/index/")
    # The index tree is one target: the constant reads `notes/index` and the tree rule reads
    # `notes/index/`, and the page's writers table carries the directory form.
    return sorted({"notes/index/" if t == "notes/index" else t for t in targets})


def writers():
    """A script is a writer when a notes/-rooted path constant is written, plus the tree and store cases."""
    return {name: writer_targets(read_text(SCRIPTS / name)) for name in script_names()
            if writer_targets(read_text(SCRIPTS / name))}


def population():
    """Every file under notes/, the scripts and __pycache__ excluded."""
    return [
        f
        for f in NOTES.rglob("*")
        if f.is_file() and "__pycache__" not in f.parts and "scripts" not in f.parts
    ]


def sections(text):
    """Split the page at its headings; a level-2 heading closes the level-3 section above it."""
    parts: dict[str, list[str]] = {}
    current = "top"
    for line in text.splitlines():
        if line.startswith("### "):
            current = line[4:].strip().lower()
            parts.setdefault(current, [])
        elif line.startswith("## "):
            current = "top"
        elif current in parts:
            parts[current].append(line)
    return parts


def table_rows(lines):
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0].startswith("`") and not set(cells[0]) <= set("-: "):
            rows.append(cells)
    return rows


def cell_paths(cell):
    return re.findall(r"`([^`]+)`", cell)


def census_rows(text):
    out = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[0].startswith("`notes/") and re.match(r"^\*\*[\d,]+\*\*$", cells[1]):
            out[cell_paths(cells[0])[0]] = int(cells[1].strip("*").replace(",", ""))
    return out


def template_measure():
    """Re-measure both template trees: name -> tree, lines, bytes, slots.

    A slot is a `{{ ` occurrence counted over the whole file, the same rule
    notes/development/templates.md quotes,
    read here from the bytes rather than from measure_templates.py.
    """
    out = {}
    for tree, directory in (("report", REPORT_TPL_DIR), ("index", TPL_DIR)):
        for t in sorted(directory.glob("*.j2")):
            if t.parent != directory:
                continue
            text = read_text(t)
            out[t.name] = {"tree": tree, "lines": len(text.splitlines()),
                           "bytes": len(text.encode()), "slots": text.count(SLOT_MARK)}
    return out


def registry_pairs():
    """The template registry's page -> checker pairs, its page -> template-file map, and the line its
    ALL_PAGES literal opens on. Both literals are parsed from the registry's bytes, which is what keeps
    this comparison independent of the writer's code."""
    lines = read_text(SCRIPTS / "catlib" / "templates.py").splitlines()
    start = next((i for i, l in enumerate(lines, start=1) if l.startswith("ALL_PAGES")), 0)
    if not start:
        return {}, {}, 0
    block = "\n".join(lines[start - 1:])
    end = block.find("\n}")
    pairs = re.findall(r'"(notes/[^"]+\.md)"\s*:\s*"([A-Za-z0-9_]+\.py)"', block[:end] if end >= 0 else block)
    tstart = next((i for i, l in enumerate(lines, start=1) if l.startswith("TEMPLATE_NAME")), 0)
    names: dict[str, str] = {}
    if tstart:
        tblock = "\n".join(lines[tstart - 1:])
        tend = tblock.find("\n}")
        names = dict(re.findall(r'"(notes/[^"]+\.md)"\s*:\s*"([A-Za-z0-9_.-]+\.j2)"',
                                tblock[:tend] if tend >= 0 else tblock))
    return dict(pairs), names, start


def index_render_counts():
    """Pages on disk per index-tree template, counted from the tree build_index.py writes."""
    counts = {n: len(list((INDEX_DIR / sub).rglob("*.md"))) for n, sub in INDEX_PAGE_DIRS.items()}
    fam = [d for d in INDEX_DIR.iterdir() if d.is_dir() and d.name not in INDEX_NON_FAMILY]
    counts["family.md.j2"] = sum(len(list(d.rglob("*.md"))) for d in fam)
    counts["index-readme.md.j2"] = int((INDEX_DIR / "README.md").is_file())
    return counts



def template_table_rows(text):
    """(report rows, index rows): template name -> cells, read from the page's two tables."""
    report, index = {}, {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0].startswith("`") or not cells[0].endswith(".j2`"):
            continue
        name = cell_paths(cells[0])[0]
        if len(cells) == 7:
            report[name] = cells
        elif len(cells) == 5:
            index[name] = cells
    return report, index


def templates_problems(text):
    """Pass H: notes/development/templates.md against the template files, the registry, and notes/index/."""
    p = []
    cen = template_measure()
    reg, names, anchor = registry_pairs()
    renders = index_render_counts()
    rows, idx_rows = template_table_rows(text)

    want_report = {n for n, v in cen.items() if v["tree"] == "report"}
    if set(rows) != want_report:
        p.append(f"report table rows {sorted(set(rows))} != report templates on disk {sorted(want_report)}")
    for n, cells in sorted(rows.items()):
        v = cen.get(n)
        if not v:
            continue
        if cells[1:4] != [f"{v['lines']:,}", f"{v['bytes']:,}", str(v["slots"])]:
            p.append(f"template row {n}: page {cells[1:4]}, disk "
                     f"{[f'{v['lines']:,}', f'{v['bytes']:,}', str(v['slots'])]}")
        # The page a report template renders is the registry's key, not `notes/<stem>`: four pages
        # live under `notes/development/`, so the mechanical name would demand a cell naming a file
        # that is not there.
        page = {names.get(pg, pg.rsplit("/", 1)[-1] + ".j2"): pg for pg in reg}.get(
            n, f"notes/{n[: -len('.j2')]}")
        if cell_paths(cells[4]) != [page]:
            p.append(f"template row {n}: page cell {cells[4]!r}, registry names {page!r}")
        checker = cell_paths(cells[5])
        if checker and checker[0] != reg.get(page, "-"):
            p.append(f"template row {n}: page checker {checker[0]!r}, registry says {reg.get(page)!r}")

    for n, cells in sorted(idx_rows.items()):
        v = cen.get(n)
        if not v:
            p.append(f"index table row for a template that is not on disk: {n}")
            continue
        if cells[1:4] != [f"{v['lines']:,}", f"{v['bytes']:,}", str(v["slots"])]:
            p.append(f"index row {n}: page {cells[1:4]}, disk "
                     f"{[f'{v['lines']:,}', f'{v['bytes']:,}', str(v['slots'])]}")
        m = re.match(r"([\d,]+)", cells[4])
        if not m or int(m.group(1).replace(",", "")) != renders.get(n, -1):
            p.append(f"index row {n}: page renders {cells[4]!r}, disk says {renders.get(n)}")
    if set(idx_rows) != {n for n, v in cen.items() if v["tree"] == "index"}:
        p.append(f"index table rows {sorted(idx_rows)} != index templates on disk "
                 f"{sorted(n for n, v in cen.items() if v['tree'] == 'index')}")

    for label, tree in (("report tree", "report"), ("index tree", "index")):
        vals = [v for n, v in cen.items() if v["tree"] == tree]
        want = (f"| **{label}** | **{len(vals)}** | **{sum(v['lines'] for v in vals):,}** |"
                f" **{sum(v['bytes'] for v in vals):,}** | **{sum(v['slots'] for v in vals):,}** |")
        if want not in text:
            p.append(f"{label} total row does not read {want!r}")

    if f"registry: **{len(reg)}** entries at `catlib/templates.py:{anchor}`" not in text:
        p.append(f"registry sentence does not read 'registry: **{len(reg)}** entries at "
                 f"`catlib/templates.py:{anchor}`'")
    # The registry's name map is part of the gap: the scripts census renders scripts-README.md.j2, which
    # the basename rule cannot produce, so the page set is the map's values, not the basenames.
    pageset = {names.get(pg, pg.rsplit("/", 1)[-1] + ".j2") for pg in reg}
    missing = sorted(t for t in pageset if not (REPORT_TPL_DIR / t).is_file())
    extra = sorted(t.name for t in REPORT_TPL_DIR.glob("*.j2") if t.name not in pageset)
    want = f"template-without-page **{len(missing)}**, page-without-template **{len(extra)}**"
    if want not in text:
        p.append(f"registry gap sentence does not read {want!r} (disk: {missing + extra})")
    return p


def check(text):
    p = []
    parts = sections(text)
    names = script_names()
    wr = writers()
    # A script can write more than one target (`build_index.py` stages the index pages and the 16
    # generated tables), so the writers table takes the sorted first target and the TSV rule reads
    # the whole list.
    derived = {k: min(v) for k, v in wr.items()}

    # A. writers: derived set == page table
    page_writers = {}
    for cells in table_rows(parts.get("writers", [])):
        script, target = cell_paths(cells[0]), cell_paths(cells[1])
        if not script or not target:
            p.append(f"writer row without script/target cells: {cells[0]!r}")
            continue
        page_writers[script[0]] = target[0]
    if page_writers != derived:
        for k in sorted(set(page_writers) | set(derived)):
            if page_writers.get(k) != derived.get(k):
                p.append(
                    f"writer {k}: page says {page_writers.get(k)!r}, source says {derived.get(k)!r}"
                )
    if f"**{len(derived)}** writers over **{len(names)}** scripts" not in text:
        p.append(
            f"writer split sentence does not read '**{len(derived)}** writers over "
            f"**{len(names)}** scripts'"
        )

    # A2. report-only and checker tables partition the non-writers
    ro = [cell_paths(c[0])[0] for c in table_rows(parts.get("report-only", [])) if cell_paths(c[0])]
    ck = [cell_paths(c[0])[0] for c in table_rows(parts.get("checkers", [])) if cell_paths(c[0])]
    non_writers = sorted(set(names) - set(derived))
    listed = ro + ck
    if sorted(listed) != non_writers:
        missing = sorted(set(non_writers) - set(listed))
        extra = sorted(set(listed) - set(non_writers))
        p.append(f"report-only+checkers != the {len(non_writers)} non-writers (missing {missing}, extra {extra})")
    if len(ro) + len(ck) != len(non_writers):
        p.append(
            f"report-only rows {len(ro)} + checker rows {len(ck)} != {len(non_writers)} non-writers"
        )
    if f"**{len(non_writers)}** scripts write nothing" not in text:
        p.append(f"report-only sentence does not read '**{len(non_writers)}** scripts write nothing'")
    if f"**{len(ro)}** of them" not in text:
        p.append(f"report-only sentence does not read '**{len(ro)}** of them'")
    if f"**{len(ck)}** scripts verify a page" not in text:
        p.append(f"checker sentence does not read '**{len(ck)}** scripts verify a page'")
    if SELF not in text:
        p.append(f"page never names its own checker {SELF}")
    if any(SELF in c[0] for c in table_rows(parts.get("checkers", []))):
        p.append(f"{SELF} listed in the checker table")

    # B/C. census
    files = population()
    index = [f for f in files if "index" in f.parts]
    summaries = [f for f in files if "summaries" in f.parts]
    templates = [f for f in files if "templates" in f.parts]
    uphist = [f for f in files if "upstream_history" in f.parts]
    probe = [f for f in files if "probe" in f.parts]
    tables = [f for f in files if "tables" in f.parts]
    dev = [f for f in files if f.parent == DEV_DIR]
    reports = [f for f in files if f.parent == REPORTS_DIR]
    top = [f for f in files if f.parent == NOTES]
    owned = (set(index) | set(summaries) | set(templates) | set(uphist) | set(probe) | set(tables)
             | set(dev) | set(reports) | set(top))
    for f in files:
        if f not in owned:
            p.append(f"file under notes/ owned by no rule: {f.relative_to(ROOT)}")
    tables_tsv = sorted(f.name for f in tables if f.suffix == ".tsv")
    derived_paths = {t for v in wr.values() for t in v}
    # `build_index.py` stages the 16 generated tables as `TABLES / basename`, so the target the rule
    # resolves is the directory, not a file. A TSV under a derived directory is generated; the
    # hand-authored pair is the rule that names which tables the writer set does not write.
    gen = {n for n in tables_tsv if f"notes/tables/{n}" in derived_paths}
    if "notes/tables" in derived_paths:
        gen |= set(tables_tsv) - {n.split("/")[-1] for n in HAND_AUTHORED_TSVS}
    gen_tsv = sorted(gen)
    hand_tsv = sorted(set(tables_tsv) - gen)
    if hand_tsv != sorted(n.split("/")[-1] for n in HAND_AUTHORED_TSVS):
        p.append(
            f"hand-authored tables TSVs: {hand_tsv}, page lists "
            f"{sorted(n.split('/')[-1] for n in HAND_AUTHORED_TSVS)}"
        )
    if f"**{len(gen_tsv)}** generated, **{len(hand_tsv)}** hand-authored" not in text:
        p.append(f"tsv census cell does not read '**{len(gen_tsv)}** generated, **{len(hand_tsv)}** hand-authored'")

    checked = set()
    for cells in table_rows(parts.get("checkers", [])):
        checked.update(cell_paths(cells[1]))
    # Pass H checks notes/development/templates.md, and this checker is not a row in its own table, so
    # the table-derived credit cannot see it. A page checked by the checker measuring it is checked.
    checked.add("notes/development/templates.md")
    top_md = sorted(f.name for f in top if f.suffix == ".md")
    reports_md = sorted(f.name for f in reports if f.suffix == ".md")
    dev_md = sorted(f.name for f in dev if f.suffix == ".md")
    # The checked/free split is over the pages the census tabulates as prose pages: the entry point at
    # the top level and the 23 report pages. A page's checker names it by its repo-relative path, so
    # the split is keyed on that path, not on the basename — after `math-faz.4` the checked pages sit
    # one level deeper and a basename key would credit a top-level name against a reports page.
    md_pages = sorted(f.relative_to(NOTES).as_posix() for f in top + reports if f.suffix == ".md")
    md_checked = sorted(n for n in md_pages if f"notes/{n}" in checked)
    md_free = sorted(n for n in md_pages if f"notes/{n}" not in checked)
    census = census_rows(text)
    expect = {
        "notes/index/": len(index),
        "notes/summaries/": len(summaries),
        "notes/templates/": len(templates),
        "notes/development/*.md": len(dev_md),
        "notes/development/upstream_history/": len(uphist),
        "notes/development/probe/": len(probe),
        "notes/tables/*.tsv": len(tables_tsv),
        "notes/reports/*.md": len(reports_md),
        "notes/*.md": len(top_md),
        "notes/": len(files),
    }
    for key, expect_val in expect.items():
        got = census.get(key)
        if got != expect_val:
            p.append(f"census row {key}: page says {got}, disk says {expect_val}")
    md = sum(1 for f in index if f.suffix == ".md")
    tsv = sum(1 for f in index if f.suffix == ".tsv")
    stated = re.search(r"\*\*([\d,]+)\*\* `\.md` pages and \*\*([\d,]+)\*\* `\.tsv` tables", text)
    if stated and (int(stated.group(1).replace(",", "")), int(stated.group(2).replace(",", ""))) != (md, tsv):
        p.append(f"index tree: {md} .md + {tsv} .tsv, page says {stated.group(1)} + {stated.group(2)}")
    if f"**{md:,}** `.md` pages and **{tsv}** `.tsv` tables" not in text:
        p.append(
            f"index split sentence does not read '**{md:,}** .md pages and **{tsv}** .tsv tables'"
        )
    if f"**{len(md_checked)}** with a checker, **{len(md_free)}** without" not in text:
        p.append(
            f"md census cell does not read '**{len(md_checked)}** with a checker, "
            f"**{len(md_free)}** without'"
        )
    free_named = re.search(r"The (\d+) pages with no checker are (.*?)\. Their counts", text, re.DOTALL)
    if not free_named:
        p.append("no sentence naming the pages with no checker")
    else:
        listed_free = sorted(re.findall(r"`notes/([^`]+\.md)`", free_named.group(2)))
        if int(free_named.group(1)) != len(md_free) or listed_free != md_free:
            p.append(
                f"no-checker list: page names {len(listed_free)} {listed_free}, "
                f"measured {len(md_free)} {md_free}"
            )

    # D. naming coverage
    for n in names:
        if n not in text:
            p.append(f"script not named in the page: {n}")
    readme = read_text(README)
    for n in names:
        if n not in readme:
            p.append(f"script not named in notes/README.md: {n}")
    # "Before this pass" is pinned to the commit that created this page, not to HEAD: HEAD moves
    # every time the command block is edited, and a check keyed to it stops being a record.
    # --reverse lists oldest first, so the creating commit is base[0]; keying to base[-1] re-pins
    # the baseline to every later edit of this page, and the naming that pass added reads as absent.
    base = subprocess.run(
        ["git", "log", "--format=%H", "--reverse", "--", "notes/scripts/README.md"],
        cwd=ROOT, capture_output=True, text=True, check=False).stdout.split()
    ref = f"{base[0]}^" if base else "HEAD"
    head_readme = subprocess.run(
        ["git", "show", f"{ref}:notes/README.md"], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout
    head_agents = subprocess.run(
        ["git", "show", f"{ref}:AGENTS.md"], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout
    gaps = sorted(n for n in names if n not in head_readme and n not in head_agents)
    named_before = len(names) - len(gaps)
    if f"named **{named_before}** of the {len(names)} scripts" not in text:
        p.append(f"naming sentence does not read 'named **{named_before}** of the {len(names)} scripts'")
    gap_page = re.search(
        r"named\s+nowhere in the repo at the pinned baseline:\s*(.*?)\.\s*The first four", text, re.DOTALL)
    if not gap_page:
        p.append("no sentence naming the scripts named nowhere")
    else:
        listed_gaps = sorted(re.findall(r"`([a-z0-9_]+\.py)`", gap_page.group(1)))
        if listed_gaps != gaps:
            p.append(f"gap list: page names {listed_gaps}, git HEAD says {gaps}")

    # E. shared basenames
    top_names = {f.name for f in top}
    idx_names = {f.name for f in index}
    shared = sorted(top_names & idx_names)
    want = (f"**{len(shared)}** shared basename — `{shared[0]}`" if len(shared) == 1 else
            f"**{len(shared)}** shared basenames — {' and '.join(f'`{n}`' for n in shared)}")
    if shared != ["README.md"]:
        p.append(f"top-level ∩ index basenames: {shared}, page says README.md alone")
    if want not in text:
        p.append(f"collision sentence does not read '{want}'")
    slug = len(idx_names & {f.name for f in summaries})
    if f"share **{slug}** page slugs" not in text:
        p.append(f"slug sentence does not read 'share **{slug}** page slugs'")

    # F. layout
    first = next(line for line in text.splitlines() if line.strip())
    if not first.startswith("# "):
        p.append(f"page opens with {first!r}, not a heading")
    if "## Not checked" not in text:
        p.append("no '## Not checked' section")
    return p


def sync_problems(page, text) -> list[str]:
    """Pass G: a generated page against the writer's render of it."""
    return RD.sync_problems(page, text)


def gate_rows() -> list[dict[str, str]]:
    """The gate's measured rows, read from the TSV the gate run lands.

    A list, not a dict keyed by spec: `measure_check_calls.py` is a gate row on both sides of
    the render, so the TSV carries that spec twice and a dict drops one row from the count
    and the sum.
    """
    return list(csv.DictReader(read_text(GATE_ROWS_TSV).splitlines(), delimiter="\t"))


def check_calls() -> dict[str, int]:
    """The probe's measured check()-call counts, read from the keyed record the probe lands."""
    return json.loads((RECORDS_ROOT / key_for("measure_check_calls.py", ())
                       / "check_calls.json").read_text(encoding="utf-8"))


def cost_problems(text: str) -> list[str]:
    """Pass I: the Cost cells, the tail figures, the sums, and the check()-count sentences.

    Every figure is measured: a Cost cell is the gate row time for the spec that names the checker,
    and a count is the probe's record. The pass carries none of these numbers.

    The self-test row times are not in the page. A run-dependent figure cannot live in a template
    keyed to HEAD, so quoting one forced a hand-sweep every run: the gate lands a new TSV, the
    template's literal is the previous run's figure, and the pass reported the page stale. The
    prose carries the caching claim; the numbers stay in the Cost table and the TSV.

    Nothing is exempted. The page wraps lines, so every sentence is matched on the block with its
    whitespace folded — a line break inside a phrase is one space. The checker name is normalized
    from the record's bare key by adding the extension the page uses, and the test file is the
    checker name with `verify_` dropped. The floors are the populations the TSV and the record name,
    so a page that drops a figure is flagged rather than skipped.
    """
    p = []
    rows_list = gate_rows()
    rows = {r["spec"]: r["seconds"] for r in rows_list}
    cold = {r["spec"]: r.get("cold", "0.0") for r in rows_list}
    calls = check_calls()
    folded = re.sub(r"\s+", " ", text)
    cost = re.findall(r"^\| `([a-z0-9_]+\.py)` \|.*\| ([0-9]+|—) \| ([0-9.]+) \| ([0-9.]+) \|$",
                      text, re.MULTILINE)
    if not cost:
        return ["no Cost table rows read"]
    for name, read_cell, cold_cell, cell in cost:
        spec = next((s for s in rows if s.startswith(name)), None)
        if spec is None:
            p.append(f"no gate row names {name}")
            continue
        want = "0" if rows[spec] == "0.0" else rows[spec]
        want_cold = "0" if cold[spec] == "0.0" else cold[spec]
        if cell != want:
            p.append(f"Wall cell for {name}: page {cell}, gate row {spec} measured {want}")
        if cold_cell != want_cold:
            p.append(f"Cold cell for {name}: page {cold_cell}, gate row {spec} measured {want_cold}")
        # The read surface is the checker's CHECKER_L1 entry — the files it reads outside the five
        # hashed trees. A checker the key cannot name has no entry, so its cell is a dash.
        want_read = str(len(CHECKER_L1[name])) if name in CHECKER_L1 else "—"
        if read_cell != want_read:
            p.append(f"Read cell for {name}: page {read_cell}, CHECKER_L1 has {want_read}")
    # The count sentence must sit in the paragraph that begins with the checker's own name. The Cost
    # prose is one block, so a block-level test lets a count belonging to a neighbouring checker
    # satisfy this checker's requirement — the sources paragraph's count carried named_results.
    lines = text.split("\n")
    starts = [k for k, l in enumerate(lines) if l.startswith("`verify_")]
    paras: dict[str, list[str]] = {}
    for i, k in enumerate(starts):
        head = re.match(r"`([a-z0-9_]+\.py)`", lines[k])
        if head is None:
            continue
        end = starts[i + 1] if i + 1 < len(starts) else len(lines)
        paras.setdefault(head.group(1), []).append(
            re.sub(r"\s+", " ", "\n".join(lines[k:end])))
    counts = 0
    positive = 0
    for checker, n in calls.items():
        if n < 0:
            continue
        positive += 1
        name = checker if checker.endswith(".py") else f"{checker}.py"
        want = f"the {n} `check()` calls"
        if any(want in s for s in paras.get(name, [])):
            counts += 1
        else:
            p.append(f"{checker}: the check() count is not {n}")
    checker_rows = [r["spec"] for r in rows_list if r["spec"].startswith("verify_")]
    csum = sum(float(rows[s]) for s in checker_rows)
    if f"The {len(checker_rows)} checker invocations sum to **{csum:.1f} s**" not in folded:
        p.append(f"the checker sum is not {len(checker_rows)} invocations at {csum:.1f} s")
    rsum = sum(float(r["seconds"]) for r in rows_list)
    if f"its {len(rows_list)} row times sum to **{rsum:.1f} s**" not in folded:
        p.append(f"the row sum is not {len(rows_list)} rows at {rsum:.1f} s")
    heaviest = max(float(cell) for *_rest, cell in cost)
    if f"**{heaviest:.1f} s** is the heaviest row with a Wall cell" not in folded:
        p.append(f"the heaviest row with a Wall cell is not {heaviest:.1f} s")
    # No heaviest-checker needle: the census checker is not a gate row, so the gate row TSV has no
    # Cost cell for it. A needle that reads a cell the TSV no longer carries raises KeyError.
    # Every writer figure the page names is checked against the gate row that names that writer.
    # The tail is the page's own claim, so the pass reads it from the page, not from a list.
    tail = re.findall(r"`([a-z0-9_]+\.py)` ([0-9.]+) s", folded)
    for name, val in tail:
        if rows.get(name) != val:
            p.append(f"the tail names {name} at {val} s, the gate row measured {rows.get(name)}")
    # Every checker row must be accounted for: a Cost cell in the table, or the page's own
    # declaration that the checker is not a row above. The exemption is read from that sentence, so
    # a checker is not exempted by name — a page-wide "not a row above" excuses every row.
    exempt = set(re.findall(r"`([a-z0-9_]+\.py)`[^.]*not a row above", folded))
    named = {name: cell for name, _read, _cold, cell in cost}
    for spec in checker_rows:
        name = spec.split()[0]
        if name in named:
            continue
        if name in exempt:
            continue
        p.append(f"{name} is a checker row the Cost table does not carry and the page does not account for")
    # The floors keep the pass from reporting green on a page that carries nothing. The record
    # names every checker whose count the page must state, so the count floor is the record's
    # population. The claim and tail floors are the page's own claims, which the pass reads off
    # the page; a gate row the page never discusses is not a defect.
    if not tail:
        p.append(f"the pass read {len(tail)} tail figures")
    if counts < positive:
        p.append(f"the pass read {counts} counts, below {positive} positive counts")
    return p


def main():
    text = read_text(PAGE)
    print("=== notes/scripts/README.md ownership check ===")
    wr = writers()
    names = script_names()
    print(f"scripts (excluding {SELF}): {len(names)}")
    print(f"writers derived from source: {len(wr)}")
    for k, v in sorted(wr.items()):
        print(f"  writes {k}: {', '.join(v)}")
    files = population()
    index = [f for f in files if "index" in f.parts]
    summaries = [f for f in files if "summaries" in f.parts]
    top = [f for f in files if f.parent == NOTES]
    print(
        f"index tree: {len(index)} "
        f"({sum(1 for f in index if f.suffix == '.md')} md + "
        f"{sum(1 for f in index if f.suffix == '.tsv')} tsv)"
    )
    print(f"summaries: {len(summaries)}")
    print(f"templates: {len([f for f in files if 'templates' in f.parts])}")
    print(f"top-level: {sum(1 for f in top if f.suffix == '.tsv')} tsv + {sum(1 for f in top if f.suffix == '.md')} md")
    print(f"notes/ total (scripts excluded): {len(files)}")
    shared = sorted({f.name for f in top} & {f.name for f in index})
    print(f"top-level ∩ index basenames: {shared}")
    print(f"index ∩ summaries slugs: {len({f.name for f in index} & {f.name for f in summaries})}")
    tpl = templates_problems(read_text(TEMPLATES_PAGE))
    print(f"templates census (notes/development/templates.md): {len(template_measure())} templates "
          f"on disk, {len(tpl)} problems")
    p = check(text)
    cost = cost_problems(text)
    importers = importer_problems(text)
    sync = sync_problems(README, read_text(README))
    for x in p + tpl + cost + importers + sync:
        print(f"PROBLEM: {x}")
    print(f"Cost pass (Cost cells, self-test row figures, check() counts): {len(cost)} problems")
    print(f"importer pass (catlib read-surface sentence): {len(importers)} problems")
    print(f"sync problems (notes/README.md): {len(sync)}")
    print(f"reconciliation: writers == page {not any('writer' in x for x in p)}")
    print(f"reconciliation: census rows == disk {not any('census' in x for x in p)}")
    print(f"reconciliation: naming complete {not any('named' in x for x in p)}")
    print(f"reconciliation: templates page == disk {not tpl}")
    print(f"reconciliation: Cost figures measured {not cost}")
    print(f"reconciliation: importer sentence measured {not importers}")
    sys.exit(1 if p + tpl + cost + importers + sync else 0)


if __name__ == "__main__":
    main()
