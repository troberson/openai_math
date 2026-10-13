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

import re
import subprocess
import sys

from catlib import render as RD
from catlib.paths import NOTES, ROOT, SCRIPTS, read_text

PAGE = SCRIPTS / "README.md"
SELF = "verify_script_ownership.py"
README = NOTES / "README.md"
TEMPLATES_PAGE = NOTES / "development" / "templates.md"
TPL_DIR = NOTES / "templates"
REPORT_TPL_DIR = TPL_DIR / "report"
INDEX_DIR = NOTES / "index"
PROBE_DIR = NOTES / "development" / "probe"
DEV_DIR = NOTES / "development"
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
    """The template registry's page -> checker pairs, and the line its ALL_PAGES literal opens on."""
    lines = read_text(SCRIPTS / "catlib" / "templates.py").splitlines()
    start = next((i for i, l in enumerate(lines, start=1) if l.startswith("ALL_PAGES")), 0)
    if not start:
        return {}, 0
    block = "\n".join(lines[start - 1:])
    end = block.find("\n}")
    pairs = re.findall(r'"(notes/[^"]+\.md)"\s*:\s*"([A-Za-z0-9_]+\.py)"', block[:end] if end >= 0 else block)
    return dict(pairs), start


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
    reg, anchor = registry_pairs()
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
        page = {pg.rsplit("/", 1)[-1] + ".j2": pg for pg in reg}.get(n, f"notes/{n[: -len('.j2')]}")
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
    pages = {pg.rsplit("/", 1)[-1] for pg in reg}
    missing = sorted(f"{n}.j2" for n in pages if not (REPORT_TPL_DIR / f"{n}.j2").is_file())
    extra = sorted(t.name for t in REPORT_TPL_DIR.glob("*.j2") if t.name[: -len(".j2")] not in pages)
    want = f"template-without-page **{len(missing)}**, page-without-template **{len(extra)}**"
    if want not in text:
        p.append(f"registry gap sentence does not read {want!r} (disk: {missing + extra})")
    return p


def check(text):
    p = []
    parts = sections(text)
    names = script_names()
    wr = writers()
    derived = {k: v[0] for k, v in wr.items()}

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
    top = [f for f in files if f.parent == NOTES]
    owned = (set(index) | set(summaries) | set(templates) | set(uphist) | set(probe) | set(tables)
             | set(dev) | set(top))
    for f in files:
        if f not in owned:
            p.append(f"file under notes/ owned by no rule: {f.relative_to(ROOT)}")
    tables_tsv = sorted(f.name for f in tables if f.suffix == ".tsv")
    gen_tsv = sorted(n for n in tables_tsv if f"notes/tables/{n}" in set(derived.values()))
    hand_tsv = sorted(n for n in tables_tsv if f"notes/tables/{n}" not in set(derived.values()))
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
    dev_md = sorted(f.name for f in dev if f.suffix == ".md")
    md_checked = sorted(n for n in top_md if f"notes/{n}" in checked)
    md_free = sorted(n for n in top_md if f"notes/{n}" not in checked)
    census = census_rows(text)
    expect = {
        "notes/index/": len(index),
        "notes/summaries/": len(summaries),
        "notes/templates/": len(templates),
        "notes/development/*.md": len(dev_md),
        "notes/development/upstream_history/": len(uphist),
        "notes/development/probe/": len(probe),
        "notes/tables/*.tsv": len(tables_tsv),
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
    sync = sync_problems(README, read_text(README))
    for x in p + tpl + sync:
        print(f"PROBLEM: {x}")
    print(f"sync problems (notes/README.md): {len(sync)}")
    print(f"reconciliation: writers == page {not any('writer' in x for x in p)}")
    print(f"reconciliation: census rows == disk {not any('census' in x for x in p)}")
    print(f"reconciliation: naming complete {not any('named' in x for x in p)}")
    print(f"reconciliation: templates page == disk {not tpl}")
    sys.exit(1 if p + tpl + sync else 0)


if __name__ == "__main__":
    main()
