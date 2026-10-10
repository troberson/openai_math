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

--mutant injects eleven faults, one per check form the page uses, and asserts each is caught.
Report-only: writes nothing.
"""
from __future__ import annotations

import re
import subprocess
import sys

from catlib.paths import NOTES, ROOT, SCRIPTS, read_text

PAGE = SCRIPTS / "README.md"
SELF = "verify_script_ownership.py"
README = NOTES / "README.md"

# The page's hand-authored tables, by rule rather than by generator.
HAND_AUTHORED_TSVS = {"notes/topics.tsv", "notes/conjecture-standing.tsv"}


def script_names():
    return sorted(p.name for p in SCRIPTS.glob("*.py") if p.name != SELF)


def path_constants():
    """The notes/-rooted path constants the shared package defines: name -> repo-relative path."""
    src = read_text(SCRIPTS / "catlib" / "paths.py")
    return {n: f"notes/{f}"
            for n, f in re.findall(r'^(\w+)\s*=\s*NOTES\s*/\s*"([^"]+)"', src, re.M)}


def notes_const(src: str, name: str) -> str | None:
    """The repo-relative path a module-level `NAME = ROOT / "notes" / ...` constant carries.

    Every quoted part is joined: `TPL_DIR = ROOT / "notes" / "templates" / "report"` is
    `notes/templates/report` — capturing only the last quoted part reads `notes/report`.
    """
    m = re.search(rf'^{name}\s*=\s*\w+\s*/\s*((?:"[^"]+"\s*/\s*)+"[^"]+")', src, re.M)
    if not m:
        return None
    parts = re.findall(r'"([^"]+)"', m.group(1))
    return "/".join(parts) if parts and parts[0] == "notes" else None


def writers():
    """A script is a writer when a notes/-rooted path constant is written, plus the tree case.

    Three shapes, because a script may open the file itself (`OUT.open("w")`), hand a package
    constant to a package writer (`tsv.write_csv(OUT, COLUMNS, rows)`), or build the receiver from
    a module constant (`out = TPL_DIR / (name)`, then `out.write_text(...)`). The second and third
    are invisible to a source-text pattern over `open`/`write_text` keyed to the receiver alone, so
    a write that moves into the shared package, or a writer that names a directory rather than a
    file, would silently drop its script out of the writer set.
    """
    consts = path_constants()
    out = {}
    for name in script_names():
        src = read_text(SCRIPTS / name)
        targets = set()
        for var in re.findall(r'([A-Za-z_]\w*)\.(?:open\([^)]*"w"[^)]*\)|write_text\()', src):
            direct = notes_const(src, var)
            if direct:
                targets.add(direct)
                continue
            hop = re.search(rf"^\s*{var}\s*=\s*([A-Za-z_]\w*)\s*/\s*\(", src, re.M)
            if hop:
                base = notes_const(src, hop.group(1))
                if base:
                    targets.add(base)
        for const in re.findall(r'\b\w+\.write_\w+\(\s*([A-Za-z_]\w*)\b', src):
            # A script may alias the package constant (`OUT = SOURCES_TSV`), so resolve one hop.
            alias = re.search(rf"^{const}\s*=\s*([A-Za-z_]\w*)\s*$", src, re.M)
            key = alias.group(1) if alias else const
            if consts.get(key):
                targets.add(consts[key])
        if re.search(r'^\w+\s*=\s*\w+\s*/\s*"notes"\s*/\s*"index"', src, re.M) and re.search(
            r"^def write\(", src, re.M
        ):
            targets.add("notes/index/")
        if targets:
            out[name] = sorted(targets)
    return out


def population():
    """Every file under notes/, the scripts and __pycache__ excluded."""
    return [
        f
        for f in NOTES.rglob("*")
        if f.is_file() and "__pycache__" not in f.parts and "scripts" not in f.parts
    ]


def sections(text):
    """Split the page at its headings; a level-2 heading closes the level-3 section above it."""
    parts = {}
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
    if len(names) != 45:
        p.append(f"scripts on disk (excluding {SELF}): {len(names)}, page says 45")
    if len(derived) != 9:
        p.append(f"derived writers: {len(derived)}, page says 9")

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
    top = [f for f in files if f.parent == NOTES]
    for f in files:
        if f not in index and f not in summaries and f not in templates and f not in top:
            p.append(f"file under notes/ owned by no rule: {f.relative_to(ROOT)}")
    top_tsv = sorted(f.name for f in top if f.suffix == ".tsv")
    gen_tsv = sorted(n for n in top_tsv if f"notes/{n}" in set(derived.values()))
    hand_tsv = sorted(n for n in top_tsv if f"notes/{n}" not in set(derived.values()))
    if sorted(f"notes/{n}" for n in hand_tsv) != sorted(HAND_AUTHORED_TSVS):
        p.append(
            f"hand-authored top-level TSVs: {hand_tsv}, page lists "
            f"{sorted(n.split('/')[-1] for n in HAND_AUTHORED_TSVS)}"
        )
    if len(gen_tsv) != 6:
        p.append(f"generated top-level TSVs: {len(gen_tsv)}, page says 6")
    if f"**{len(gen_tsv)}** generated, **{len(hand_tsv)}** hand-authored" not in text:
        p.append(f"tsv census cell does not read '**{len(gen_tsv)}** generated, **{len(hand_tsv)}** hand-authored'")

    checked = set()
    for cells in table_rows(parts.get("checkers", [])):
        checked.update(cell_paths(cells[1]))
    top_md = sorted(f.name for f in top if f.suffix == ".md")
    md_checked = sorted(n for n in top_md if f"notes/{n}" in checked)
    md_free = sorted(n for n in top_md if f"notes/{n}" not in checked)
    census = census_rows(text)
    expect = {
        "notes/index/": len(index),
        "notes/summaries/": len(summaries),
        "notes/templates/": len(templates),
        "notes/*.tsv": len(top_tsv),
        "notes/*.md": len(top_md),
        "notes/": len(files),
    }
    for key, want in expect.items():
        got = census.get(key)
        if got != want:
            p.append(f"census row {key}: page says {got}, disk says {want}")
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
    free_named = re.search(r"The (\d+) pages with no checker are (.*?)\. Their counts", text, re.S)
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
        r"named\s+nowhere in the repo at the pinned baseline:\s*(.*?)\.\s*The first four", text, re.S)
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


def mutants():
    """Eleven faults, one per check form. Each must be caught by the check it targets."""
    original = read_text(PAGE)
    cases = [
        ("writer target altered", original.replace("| `build_catalog.py` | `notes/catalog.tsv` |", "| `build_catalog.py` | `notes/catalog-x.tsv` |"), "page says 'notes/catalog-x.tsv'"),
        ("writer row deleted", original.replace("| `extract_links.py` | `notes/links.tsv` | run twice, byte-identical | `notes/links.md` |\n", ""), "writer extract_links.py: page says None"),
        ("hand-authored TSV claimed as generated", original.replace("**6** generated, **2** hand-authored", "**7** generated, **1** hand-authored"), "tsv census cell"),
        ("writer count altered", original.replace("**9** writers over **45** scripts", "**10** writers over **45** scripts"), "writer split sentence"),
        ("index file count altered", original.replace("| `notes/index/` | **1,049** |", "| `notes/index/` | **1,050** |"), "census row notes/index/"),
        ("collision name altered", original.replace("**1** shared basename — `README.md`", "**2** shared basenames — `README.md` and `topics.tsv`"), "collision sentence"),
        ("checker name altered", original.replace("| `verify_sources.py` |", "| `verify_sources2.py` |"), "non-writers"),
        ("unchecked page claimed as checked", original.replace("| `verify_abstracts.py` | `notes/abstracts.md` |", "| `verify_abstracts.py` | `notes/abstracts.md`, `notes/links.md` |"), "md census cell"),
        ("Not checked section deleted", original.replace("## Not checked", "## Checked"), "no '## Not checked' section"),
        ("summaries count altered", original.replace("| `notes/summaries/` | **21** |", "| `notes/summaries/` | **22** |"), "census row notes/summaries/"),
        ("templates count altered", original.replace("| `notes/templates/` | **21** |", "| `notes/templates/` | **3** |"), "census row notes/templates/"),
    ]
    fails = []
    for label, mutated, needle in cases:
        if mutated == original:
            fails.append(f"{label}: mutation changed nothing")
            continue
        PAGE.write_text(mutated, encoding="utf-8")
        try:
            found = check(mutated)
        finally:
            PAGE.write_text(original, encoding="utf-8")
        if not any(needle in x for x in found):
            fails.append(f"{label}: NOT caught by {needle!r} (problems: {found[:2]})")
        else:
            print(f"  caught {label}: {next(x for x in found if needle in x)[:110]}")
    return fails, len(cases)


def main():
    text = read_text(PAGE)
    if "--mutant" in sys.argv:
        print("=== notes/scripts/README.md mutant self-test ===")
        fails, total = mutants()
        for f in fails:
            print(f"MUTANT NOT CAUGHT: {f}")
        print(f"mutants flagged: {total - len(fails)} of {total}")
        sys.exit(1 if fails else 0)

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
    p = check(text)
    for x in p:
        print(f"PROBLEM: {x}")
    print(f"reconciliation: writers == page {not any('writer' in x for x in p)}")
    print(f"reconciliation: census rows == disk {not any('census' in x for x in p)}")
    print(f"reconciliation: naming complete {not any('named' in x for x in p)}")
    sys.exit(1 if p else 0)


if __name__ == "__main__":
    main()
