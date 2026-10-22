#!/usr/bin/env python3
"""Check every link the index emits against the files the release ships, report-only.

math-u41.5. The index checks its own links at render time; this is the independent
re-derivation: it parses the rendered markdown from disk, resolves each href against
the page's directory, and reports broken links as a count with the full list. It
writes nothing.

A link that resolves to a directory is reported as a directory, not as a file. The
index links directories on purpose (a manuscript's LaTeX tree at preprints/<dir>/build/,
a verification bundle at preprints/<dir>/verification/, a Lean module dir), so the
report separates "resolves to a file" from "resolves to a directory" per category and
names the directory categories.

Link extraction is paren-balanced, not `[^)]*`. One manuscript path contains
parentheses - preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/
paper.pdf (family 337) - and a `[^)]*` pattern truncates that href at `(0)`, which
invents a broken link. The scanner walks forward from `](` tracking paren depth and
honours backslash escapes, so the balanced pair inside the path is consumed. The
baseline is 0 broken links, not 1.

Coverage is reconciled against a fresh build_catalog.py parse: 719 manuscript PDFs,
719 build/ trees, 719 README.md stubs, 242 scope notes, 416 comparator configs,
10 reasoning traces in 11 files, 30 verification dirs, 192 Lean files named by the
yaml over 183 module dirs. CONTENTS.md is checked as the shipped-surface baseline in
the same pass. Links are also counted per page group (names, families, topics,
disciplines, entry point), which is what the coverage gap in notes/development/index-links.md
quotes: the render-time registry total minus the scanned total, attributed per group.

The basename pass is the invariant `math-faz.6` moved the 16 generated tables on: the index tree
and `notes/tables/` must share no file basename. A page links a table by relative path, so a bare
basename is ambiguous when both trees carry it, and a link that looks like it resolves can resolve
to the wrong tree. The pass takes the two basename sets as arguments so the self-tests can inject a
collision without writing a file.

Run: python3 notes/scripts/check_index_links.py [--contents]
--contents adds the CONTENTS.md link check (it is on by default in the report).

The self-tests are not here: they live in `notes/scripts/tests/test_index_links.py`, which injects
the broken hrefs, requires the real hrefs to resolve, and asserts the paren-balanced scanner keeps
the CAT(0) path whole where `[^)]*` truncates it. `trap()` stays in this file because
`render_reports.py` renders its two rows into the page's scanner table.

The page check is not here: `notes/development/index-links.md` is compared with `render_reports.py`'s
render of it by `verify_page_sync.py`, which owns that pass and mutates the page in memory. The scan
proves the counts are measured; it proves nothing about the sentences around them, and the page's
tables are prose in the template, not report output.
"""
from __future__ import annotations

import collections
import pathlib
import posixpath
import re
import sys
from functools import cache
from typing import Any

import build_catalog as B
from catlib import yaml as Y

ROOT = pathlib.Path(__file__).resolve().parents[2]

IDX = ROOT / "notes" / "index"
SUMM = ROOT / "notes" / "summaries"
TABLES = ROOT / "notes" / "tables"
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
# The main_results triples come from the package reader; build_index.py calls main() at module
# scope, so importing it would run the build.


def md_links(text):
    """Every (href) in markdown link syntax, with paren-balanced target scanning.

    `[text](target "title")` and `[text](target)`; a `)` inside the target is part of
    the target when its paren is balanced, which is what the CAT(0) path needs.
    """
    out = []
    i = 0
    while True:
        j = text.find("](", i)
        if j < 0:
            break
        k = j + 2
        depth = 1
        while k < len(text):
            c = text[k]
            if c == "\\":
                k += 2
                continue
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        if k >= len(text):
            break
        raw = text[j + 2:k]
        # A markdown title is a quoted tail: [t](path "Title")
        m = re.match(r'^(.*?)\s+"[^"]*"$', raw, re.DOTALL)
        if m:
            raw = m.group(1)
        raw = raw.strip()
        if raw.startswith("<") and raw.endswith(">"):
            raw = raw[1:-1]
        out.append(raw)
        i = k + 1
    return out


def category(rel):
    """What kind of shipped object a repo-relative target is."""
    if rel.endswith("/"):
        body = rel[:-1]
    else:
        body = rel
    p = pathlib.PurePosixPath(body).parts
    if not p:
        return "self"
    if p[0] == "preprints":
        if len(p) == 2:
            return "manuscript-dir"
        tail = p[-1]
        if tail == "build" and len(p) == 3:
            return "latex-build-tree"
        if tail == "verification" and len(p) == 3:
            return "verification-dir"
        if tail == "README.md" and len(p) == 3:
            return "manuscript-readme"
        if tail.endswith(".pdf"):
            return "manuscript-pdf"
        if tail.endswith(".tex"):
            return "latex-source"
        if tail.endswith(".bib"):
            return "latex-bib"
        return "preprint-file"
    if p[0] == "lean":
        if len(p) >= 2 and p[1] == "docs":
            return "scope-note"
        if len(p) >= 2 and p[1] == "ComparatorChallenges":
            return "config-json" if p[-1].endswith(".json") else (
                "config-lean" if p[-1].endswith(".lean") else "config-other")
        if len(p) >= 2 and p[1] == "OAI":
            if p[-1].endswith(".lean"):
                return "lean-file"
            return "lean-dir"
        return "lean-other"
    if p[0] == "reasoning_traces":
        return "trace"
    if p[0] == "notes" and len(p) >= 2 and p[1] == "index":
        last = p[-1]
        if last.endswith(".md"):
            return "index-page"
        if last.endswith(".tsv"):
            return "index-table"
        return "index-dir"
    if p[0] == "notes" and len(p) >= 2 and p[1] == "tables":
        return "tables-tsv" if p[-1].endswith(".tsv") else "notes-doc"
    if p[0] == "notes":
        return "notes-doc"
    return "release-surface"


DIR_CATEGORIES = {"manuscript-dir", "latex-build-tree", "verification-dir", "lean-dir",
                  "index-dir"}

# Fixed print order for the per-page-group link counts, so the report is stable.
GROUP_ORDER = ["name pages", "family pages", "topic pages", "discipline pages",
               "entry point"]

# The path that breaks a `[^)]*` link scan, used by the scanner table and by the self-tests.
CAT_DIR = "preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026"
CAT_PAGE = "differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md"


def resolve_in(tree, page_rel, href):
    """Resolve an href found on a page under `tree` to a repo-relative path."""
    base = (tree / page_rel).parent
    return posixpath.normpath(posixpath.join(base.relative_to(ROOT).as_posix(), href))


def resolve(page_rel, href):
    """Resolve an href found on an index page to a repo-relative path."""
    return resolve_in(IDX, page_rel, href)


def trap():
    """The paren-balanced scanner demonstrated on the line that breaks `[^)]*`.

    `render_reports.py` renders these two rows into `notes/development/index-links.md`, so the trap
    stays demonstrated rather than recorded: the naive pattern truncates at `(0)`, the truncated target
    does not exist, and a checker built on `[^)]*` reports a broken link that is not there.
    """
    line = f"[paper](../../../{CAT_DIR}/paper.pdf)"
    naive = re.findall(r"\]\(([^)]*)\)", line)[0]
    balanced = md_links(line)[0]
    return [(label, target, (ROOT / resolve(CAT_PAGE, target)).exists())
            for label, target in (("naive [^)]*", naive), ("paren-balanced", balanced))]


def check_tree(tree, rel_root):
    """Every link in every rendered page under `tree`, resolved against the page's directory.

    `rel_root` is the tree's path relative to ROOT, so the relative page path resolves against
    the tree, not the repo. The index and the summaries tree are the two callers; both share the
    paren-balanced scanner and the same href skipping rules.
    """
    del rel_root  # kept for signature symmetry with resolve_in's base read
    links = []
    for page in sorted(tree.rglob("*.md")):
        rel_page = page.relative_to(tree).as_posix()
        for href in md_links(page.read_text(encoding="utf-8", errors="replace")):
            if not href or href.startswith("#") or SCHEME.match(href):
                continue
            target = href.split("#")[0]
            if not target:
                continue
            links.append((rel_page, target, resolve_in(tree, rel_page, target)))
    return links


def check_index():
    """Every link in every rendered index page, resolved against the page's directory."""
    return check_tree(IDX, "notes/index")


def check_summaries():
    """Every link in every rendered summary page, resolved against the page's directory."""
    return check_tree(SUMM, "notes/summaries")


def page_group(rel_page: str) -> str:
    """Page group a scanned link sits in, keyed by the top-level path under notes/index/.

    The 17 discipline dirs hold family pages, so anything that is not names/, topics/,
    disciplines/ or the entry point is a family page.
    """
    top = rel_page.split("/")[0]
    if top == "README.md":
        return "entry point"
    return {"names": "name pages", "topics": "topic pages",
            "disciplines": "discipline pages"}.get(top, "family pages")


def contents_links():
    """CONTENTS.md links, checked with the same paren-balanced scanner."""
    text = (ROOT / "CONTENTS.md").read_text(encoding="utf-8", errors="replace")
    out = []
    for href in md_links(text):
        if not href or href.startswith("#") or SCHEME.match(href):
            continue
        target = href.split("#")[0]
        if target:
            out.append(target)
    return out


def basenames(d: pathlib.Path) -> set[str]:
    """Every file basename under a directory, as a set."""
    return {p.name for p in d.rglob("*") if p.is_file()}


def basename_dupes(d: pathlib.Path) -> list[str]:
    """Basenames that appear more than once under a directory, in sorted order.

    Inside the index tree, 6 discipline names are also topic terms, so `disciplines/X.md` and
    `topics/X.md` share a basename. That is benign — links are relative, so there is no ambiguity —
    and it is why the collision pass is scoped to the two trees rather than to the index alone.
    """
    c = collections.Counter(p.name for p in d.rglob("*") if p.is_file())
    return sorted(n for n, k in c.items() if k > 1)


def basename_overlap(idx: set[str], tab: set[str]) -> list[str]:
    """Basenames shared by the index tree and `notes/tables/`, in sorted order.

    `math-faz.6` moved the 16 generated tables out of `notes/index/` into `notes/tables/` so every
    TSV in the repo sits in one directory. The invariant that keeps that move safe is that the two
    trees share no basename: an index page links a table by relative path, so a page that names a
    bare basename is ambiguous when both trees carry it, and a link that appears to resolve can
    resolve into the wrong tree. The pass takes the two sets as arguments so the self-tests can
    inject a collision without writing a file.
    """
    return sorted(set(idx) & set(tab))


@cache
def measure() -> dict[str, Any]:
    """Every number the report prints, as data.

    `notes/development/index-links.md` is rendered from this dict by `render_reports.py`, which imports
    this module; `main()` prints the same dict. The page and the report share one measurement, so the
    report stays the page's source and the two cannot drift apart.
    """
    links = check_index()
    broken: list[str] = []
    cats: collections.Counter[str] = collections.Counter()
    kind: collections.Counter[tuple[str, str]] = collections.Counter()
    groups: collections.Counter[str] = collections.Counter()
    targets = collections.defaultdict(set)
    for page, href, rel in links:
        c = category(rel)
        cats[c] += 1
        groups[page_group(page)] += 1
        targets[c].add(rel)
        p = ROOT / rel
        if not p.exists():
            broken.append(f"{page} -> {href}")
        elif p.is_dir():
            kind[(c, "dir")] += 1
        else:
            kind[(c, "file")] += 1

    # Canonical counts, from a fresh parse of the release.
    order, _fams = B.parse_overview()
    fam_paps = B.parse_contents()
    docs = B.parse_docs()
    traces_by_fam, trace_unlisted = B.parse_traces()
    chal = B.parse_challenges()
    triples = sorted((e["config"], e["declaration"], e["file"])
                     for e in Y.main_results_entries())
    import csv
    ledger = {}
    with open(ROOT / "notes" / "tables" / "catalog.tsv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            ledger[r["fam"]] = r
    paps = sum(int(r["paps"]) for r in ledger.values())
    ver_dirs = {p.parent.name for p in (ROOT / "preprints").glob("*/verification")}
    pdf_paths = {p for f in order for p in fam_paps.get(f, ())}
    trace_stems = sorted({s for v in traces_by_fam.values() for s in v})

    pages = sorted(p.relative_to(IDX).as_posix() for p in IDX.rglob("*.md"))
    gp = collections.Counter(page_group(r) for r in pages)
    idx_names = basenames(IDX)
    tab_names = basenames(TABLES)
    collide = basename_overlap(idx_names, tab_names)
    idx_dupes = basename_dupes(IDX)
    canon = {
        "manuscript-pdf": len(pdf_paths),
        "manuscript-dir": paps,
        "latex-build-tree": paps,
        "manuscript-readme": paps,
        "verification-dir": len(ver_dirs),
        "scope-note": len(docs),
        "config-json": len(chal),
        "config-lean": len(chal),
        "trace": len(trace_stems),
        "lean-file": len({f for _, _, f in triples}),
        "lean-dir": len({posixpath.dirname(f) for _, _, f in triples}),
    }
    # Manuscript dirs the index links that the release does not list as manuscripts: the name
    # layer is keyed by on-disk directory names, so it reaches dirs the merge superseded.
    canon_dirs = {f"preprints/{p.split('/')[1]}" for p in pdf_paths}
    extra_dirs = sorted(targets["manuscript-dir"] - canon_dirs)
    cl = contents_links()
    cbroken = [h for h in cl if not (ROOT / posixpath.normpath(h.split('#')[0])).exists()]
    cpdf = [h for h in cl if h.endswith(".pdf")]
    return {
        "pages": pages,
        "links": links,
        "broken": broken,
        "cats": cats,
        "kind": kind,
        "groups": groups,
        "targets": targets,
        "gp": gp,
        "canon": canon,
        "paps": paps,
        "triples": triples,
        "trace_stems": trace_stems,
        "trace_unlisted": list(trace_unlisted),
        "trace_files": sum(1 for p in (ROOT / "reasoning_traces").iterdir() if p.is_file()),
        "trace_disk": sorted({p.stem for p in (ROOT / "reasoning_traces").iterdir() if p.is_file()}),
        "extra_dirs": extra_dirs,
        "extra_dirs_on_disk": sum(1 for d in extra_dirs if (ROOT / d).is_dir()),
        "extra_dir_links": sum(1 for _p, _h, rel in links if rel in set(extra_dirs)),
        "idx_basenames": len(idx_names),
        "tab_basenames": len(tab_names),
        "idx_dupes": len(idx_dupes),
        "collisions": collide,
        "trap": trap(),
        "dir_links": sum(v for (c, k), v in kind.items() if k == "dir"),
        "dir_cats": sorted({c for (c, k) in kind if k == "dir"}),
        "file_links": sum(v for (c, k), v in kind.items() if k == "file"),
        "contents": cl,
        "contents_broken": cbroken,
        "contents_pdf": cpdf,
    }


@cache
def measure_summaries() -> dict[str, Any]:
    """Every number the summaries-tree report prints, as data.

    The summaries tree (`notes/summaries/`) is where `build_summaries.py` renders the 60 family
    pages and keeps the link-only README. It is a second page tree with its own links — breadcrumb
    to the index, manuscript PDFs and LaTeX, `CONTENTS.md`, `overview.tex` — and those links have
    no checker of their own: `verify_summaries.py` resolves a page's markdown links only relative to
    the page's directory and does not reconcile them against the release, and it is being retired by
    the renderer pass. `measure()` stays index-scoped because the index page's canonical comparisons
    are index facts; this dict is the summaries tree's own scan, kept separate so the two trees
    report their counts under their own names. `main()` prints both and folds the summaries broken
    links into the exit code.
    """
    links = check_summaries()
    broken: list[str] = []
    cats: collections.Counter[str] = collections.Counter()
    kind: collections.Counter[tuple[str, str]] = collections.Counter()
    targets = collections.defaultdict(set)
    for page, href, rel in links:
        c = category(rel)
        cats[c] += 1
        targets[c].add(rel)
        p = ROOT / rel
        if not p.exists():
            broken.append(f"{page} -> {href}")
        elif p.is_dir():
            kind[(c, "dir")] += 1
        else:
            kind[(c, "file")] += 1
    pages = sorted(p.relative_to(SUMM).as_posix() for p in SUMM.rglob("*.md"))
    return {
        "pages": pages,
        "links": links,
        "broken": broken,
        "cats": cats,
        "kind": kind,
        "targets": targets,
        "dir_links": sum(v for (c, k), v in kind.items() if k == "dir"),
        "file_links": sum(v for (c, k), v in kind.items() if k == "file"),
    }


def main():
    m = measure()
    links, broken, cats, kind, groups, targets = (m["links"], m["broken"], m["cats"], m["kind"],
                                                  m["groups"], m["targets"])
    canon, gp = m["canon"], m["gp"]

    print(f"index pages scanned    {len(m['pages'])}")
    print(f"links extracted        {len(links)}")
    print(f"broken links           {len(broken)}")
    for b in broken:
        print(f"  BROKEN {b}")
    print()
    print(f"{'category':22} {'links':>7} {'targets':>8} {'file':>6} {'dir':>5}  canonical")
    for c in sorted(cats, key=lambda k: (-cats[k], k)):
        nf = kind[(c, "file")]
        nd = kind[(c, "dir")]
        cv = canon.get(c)
        note = "" if cv is None else ("= canonical" if len(targets[c]) == cv
                                     else f"linked {len(targets[c])} of {cv}")
        print(f"{c:22} {cats[c]:>7} {len(targets[c]):>8} {nf:>6} {nd:>5}  "
              f"{'' if cv is None else str(cv) + '  ' + note}")
    print()
    print(f"{'page group':16} {'pages':>6} {'links':>7}")
    for g in GROUP_ORDER:
        print(f"{g:16} {gp[g]:>6} {groups[g]:>7}")
    print(f"{'total':16} {sum(gp.values()):>6} {sum(groups.values()):>7}")
    print()
    print(f"directory-resolving links  {m['dir_links']} over {m['dir_cats']}")
    print(f"file-resolving links       {m['file_links']}")
    print(f"basename collisions (notes/index vs notes/tables)  {len(m['collisions'])}  "
          f"over {m['idx_basenames']} index basenames and {m['tab_basenames']} table basenames")
    for b in m["collisions"]:
        print(f"  COLLISION {b}")
    print(f"index basenames shared inside the index tree  {m['idx_dupes']}")
    print(f"manuscript dirs linked outside the release set  {len(m['extra_dirs'])}  on disk "
          f"{m['extra_dirs_on_disk']}  "
          f"links {m['extra_dir_links']}")
    print(f"trace stems attributed     {len(m['trace_stems'])}  on disk {len(m['trace_disk'])}  "
          f"unlisted {' '.join(m['trace_unlisted']) if m['trace_unlisted'] else 'none'}")

    print()
    print(f"CONTENTS.md links        {len(m['contents'])}  pdf links {len(m['contents_pdf'])}  "
          f"broken {len(m['contents_broken'])}")
    for b in m["contents_broken"][:10]:
        print(f"  BROKEN {b}")

    s = measure_summaries()
    print()
    print(f"summaries pages scanned  {len(s['pages'])}")
    print(f"summaries links          {len(s['links'])}")
    print(f"summaries broken links   {len(s['broken'])}")
    for b in s["broken"]:
        print(f"  BROKEN {b}")
    print(f"summaries dir links      {s['dir_links']}   file links {s['file_links']}")

    return 1 if (broken or s["broken"] or m["contents_broken"] or m["collisions"]) else 0


if __name__ == "__main__":
    sys.exit(main())
