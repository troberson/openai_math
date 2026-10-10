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
disciplines, entry point), which is what the coverage gap in notes/index-links.md
quotes: the render-time registry total minus the scanned total, attributed per group.

Run: python3 notes/scripts/check_index_links.py [--contents]
--contents adds the CONTENTS.md link check (it is on by default in the report).
--mutant runs the self-test instead of the scan: injected broken hrefs, one per
category, must all be caught, real hrefs must all resolve, and the paren-balanced
scanner must keep the CAT(0) path whole where `[^)]*` truncates it.
"""
from __future__ import annotations

import collections
import pathlib
import posixpath
import re
import sys
from typing import Any

import build_catalog as B

from catlib import yaml as Y

ROOT = pathlib.Path(__file__).resolve().parents[2]

IDX = ROOT / "notes" / "index"
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
        m = re.match(r'^(.*?)\s+"[^"]*"$', raw, re.S)
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
    if p[0] == "notes":
        return "notes-doc"
    return "release-surface"


DIR_CATEGORIES = {"manuscript-dir", "latex-build-tree", "verification-dir", "lean-dir",
                  "index-dir"}

# Fixed print order for the per-page-group link counts, so the report is stable.
GROUP_ORDER = ["name pages", "family pages", "topic pages", "discipline pages",
               "entry point"]

# The path that breaks a `[^)]*` link scan, used by the --mutant self-test.
CAT_DIR = "preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026"
CAT_PAGE = "differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md"


def resolve(page_rel, href):
    """Resolve an href found on an index page to a repo-relative path."""
    base = (IDX / page_rel).parent
    return posixpath.normpath(posixpath.join(base.relative_to(ROOT).as_posix(), href))


# Injected hrefs that must all be reported broken, one per category the checker
# classifies, so a checker that only walks manuscript paths fails the self-test.
MUTANTS = [
    ("README.md", "disciplines/no-such.md", "index-page"),
    ("README.md", "no-such-table.tsv", "index-table"),
    ("README.md", "no-such-dir/", "index-dir"),
    ("README.md", "../no-such-note.md", "notes-doc"),
    ("names/cauchy.md", "../number-theory/999-no-such-family.md", "index-page"),
    ("names/cauchy.md", "../topics/no-such-topic.md", "index-page"),
    ("names/cauchy.md", f"../../../{CAT_DIR}/no-such-file.tex", "latex-source"),
    ("names/cauchy.md", "../../../preprints/No-Such-Manuscript/paper.pdf",
     "manuscript-pdf"),
    ("names/cauchy.md", "../../../preprints/No-Such-Manuscript/", "manuscript-dir"),
    ("names/cauchy.md", "../../../lean/ComparatorChallenges/no_such_config.json",
     "config-json"),
    ("names/cauchy.md", "../../../lean/ComparatorChallenges/NoSuch.lean", "config-lean"),
    ("names/cauchy.md", "../../../lean/OAI/No/Such/Module.lean", "lean-file"),
    ("names/cauchy.md", "../../../lean/OAI/No/Such/", "lean-dir"),
    ("names/cauchy.md", "../../../lean/docs/999.md", "scope-note"),
    ("names/cauchy.md", "../../../reasoning_traces/no-such-trace.pdf", "trace"),
    ("names/cauchy.md", "../../../nope/thing.lean", "release-surface"),
    (CAT_PAGE, "../../../preprints/No-Such-Manuscript/build/", "latex-build-tree"),
    (CAT_PAGE, "../../../preprints/No-Such-Manuscript/verification/", "verification-dir"),
    (CAT_PAGE, "../../../preprints/No-Such-Manuscript/README.md", "manuscript-readme"),
    (CAT_PAGE, "../../../preprints/No-Such-Manuscript/nothing.bib", "latex-bib"),
]

# Real hrefs taken from the rendered pages: a checker that flags everything is useless,
# so these must resolve.
CONTROLS = [
    ("README.md", "../index-design.md"),
    ("README.md", "../topics.tsv"),
    ("README.md", "names/"),
    ("names/cauchy.md", "../names.tsv"),
    ("names/cauchy.md", "../../../lean/docs/003.md"),
    (CAT_PAGE, f"../../../{CAT_DIR}/paper.pdf"),
    (CAT_PAGE, f"../../../{CAT_DIR}/build/"),
]


def mutant_test():
    """Run the checker's own existence and classification tests over injected hrefs."""
    missed = []
    caught = 0
    for page, href, cat in MUTANTS:
        rel = resolve(page, href)
        if (ROOT / rel).exists():
            missed.append(f"{page} -> {href}: injected target resolves, the test is inert")
        elif category(rel) != cat:
            missed.append(f"{page} -> {href}: broken but classified {category(rel)}, "
                          f"expected {cat}")
        else:
            caught += 1

    clean = 0
    wrong = []
    for page, href in CONTROLS:
        rel = resolve(page, href)
        if (ROOT / rel).exists():
            clean += 1
        else:
            wrong.append(f"{page} -> {href}: resolves to {rel}, which is absent")

    # The regex trap, demonstrated on the line itself: `[^)]*` truncates at `(0)` and
    # the truncated target does not exist, so a naive checker reports a broken link.
    line = f"[paper](../../../{CAT_DIR}/paper.pdf)"
    naive = re.findall(r"\]\(([^)]*)\)", line)[0]
    balanced = md_links(line)[0]
    trap = []
    for label, target in (("naive [^)]*", naive), ("paren-balanced", balanced)):
        trap.append((label, target, (ROOT / resolve(CAT_PAGE, target)).exists()))

    # Directory-vs-file: what the classifier tags must match what is on disk.
    classed = []
    for rel, _ in ((f"{CAT_DIR}/build/", "dir"), (f"{CAT_DIR}/paper.pdf", "file"),
                   ("lean/docs/003.md", "file"), ("lean/OAI/Combinatorics", "dir"),
                   ("notes/index/names/", "dir"), ("notes/names.md", "file")):
        on_disk = "dir" if (ROOT / rel).is_dir() else "file"
        tagged = category(rel) in DIR_CATEGORIES
        classed.append((rel, on_disk, "dir" if tagged else "file", category(rel)))
        if on_disk == "dir" and not tagged:
            missed.append(f"{rel}: a directory the classifier does not tag as one")
    return caught, len(MUTANTS), missed, clean, len(CONTROLS), wrong, trap, classed


def check_index():
    """Every link in every rendered index page, resolved against the page's directory."""
    links = []
    for page in sorted(IDX.rglob("*.md")):
        rel_page = page.relative_to(IDX).as_posix()
        for href in md_links(page.read_text(encoding="utf-8", errors="replace")):
            if not href or href.startswith("#") or SCHEME.match(href):
                continue
            target = href.split("#")[0]
            if not target:
                continue
            links.append((rel_page, target, resolve(rel_page, target)))
    return links


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


def measure() -> dict[str, Any]:
    """Every number the report prints, as data.

    `notes/index-links.md` is rendered from this dict by `render_reports.py`, which imports this
    module; `main()` prints the same dict. The page and the report share one measurement, so the
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
    with open(ROOT / "notes" / "catalog.tsv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            ledger[r["fam"]] = r
    paps = sum(int(r["paps"]) for r in ledger.values())
    ver_dirs = {p.parent.name for p in (ROOT / "preprints").glob("*/verification")}
    pdf_paths = {p for f in order for p in fam_paps.get(f, ())}
    trace_stems = sorted({s for v in traces_by_fam.values() for s in v})

    pages = sorted(p.relative_to(IDX).as_posix() for p in IDX.rglob("*.md"))
    gp = collections.Counter(page_group(r) for r in pages)
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
        "dir_links": sum(v for (c, k), v in kind.items() if k == "dir"),
        "dir_cats": sorted({c for (c, k) in kind if k == "dir"}),
        "file_links": sum(v for (c, k), v in kind.items() if k == "file"),
        "contents": cl,
        "contents_broken": cbroken,
        "contents_pdf": cpdf,
    }


def main(argv):
    if "--mutant" in argv:
        caught, total, missed, clean, ctotal, wrong, trap, classed = mutant_test()
        print(f"mutants injected       {total}  caught {caught}  missed {len(missed)}")
        for m in missed:
            print(f"  MISSED {m}")
        print(f"controls checked       {ctotal}  resolve {clean}  absent {len(wrong)}")
        for w in wrong:
            print(f"  CONTROL-FAIL {w}")
        print()
        for label, target, ok in trap:
            print(f"{label:16} {target!r:80} resolves {ok}")
        print()
        for rel, on_disk, tagged, cat in classed:
            print(f"on disk {on_disk:4}  reported {tagged:4}  {cat:18} {rel}")
        return 1 if (missed or wrong) else 0

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
    return 1 if (broken or m["contents_broken"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
