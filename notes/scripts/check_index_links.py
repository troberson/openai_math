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

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notes" / "scripts"))
import build_catalog as B  # noqa: E402

IDX = ROOT / "notes" / "index"
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
# The main_results triples, same pattern build_index.py uses. build_index.py calls main()
# at module scope, so importing it would run the build; the pattern is carried here.
TRIPLE = re.compile(r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json\s*\n"
                    r"\s*declaration:\s*(\S+)\s*\n\s*file:\s*(\S+)")


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

    links = check_index()
    broken, cats = [], collections.Counter()
    kind = collections.Counter()
    groups = collections.Counter()
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
    triples = sorted(TRIPLE.findall(
        (ROOT / "lean" / "formalization.yaml").read_text(encoding="utf-8", errors="replace")))
    import csv
    ledger = {}
    with open(ROOT / "notes" / "catalog.tsv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            ledger[r["fam"]] = r
    paps = sum(int(r["paps"]) for r in ledger.values())
    ver_dirs = {p.parent.name for p in (ROOT / "preprints").glob("*/verification")}
    pdf_paths = {p for f in order for p in fam_paps.get(f, ())}
    trace_stems = sorted({s for v in traces_by_fam.values() for s in v})

    print(f"index pages scanned    {len(list(IDX.rglob('*.md')))}")
    print(f"links extracted        {len(links)}")
    print(f"broken links           {len(broken)}")
    for b in broken:
        print(f"  BROKEN {b}")
    print()
    print(f"{'category':22} {'links':>7} {'targets':>8} {'file':>6} {'dir':>5}  canonical")
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
    gp = collections.Counter(page_group(p.relative_to(IDX).as_posix())
                             for p in IDX.rglob("*.md"))
    for g in GROUP_ORDER:
        print(f"{g:16} {gp[g]:>6} {groups[g]:>7}")
    print(f"{'total':16} {sum(gp.values()):>6} {sum(groups.values()):>7}")
    print()
    print(f"directory-resolving links  {sum(v for (c, k), v in kind.items() if k == 'dir')} "
          f"over {sorted({c for (c, k) in kind if k == 'dir'})}")
    print(f"file-resolving links       {sum(v for (c, k), v in kind.items() if k == 'file')}")
    # Manuscript dirs the index links that the release does not list as manuscripts: the name
    # layer is keyed by on-disk directory names, so it reaches dirs the merge superseded.
    canon_dirs = {f"preprints/{p.split('/')[1]}" for p in pdf_paths}
    extra_dirs = sorted(targets["manuscript-dir"] - canon_dirs)
    print(f"manuscript dirs linked outside the release set  {len(extra_dirs)}  on disk "
          f"{sum(1 for d in extra_dirs if (ROOT / d).is_dir())}  "
          f"links {sum(1 for _p, _h, rel in links if rel in set(extra_dirs))}")
    print(f"trace stems attributed     {len(trace_stems)}  on disk "
          f"{len({p.stem for p in (ROOT / 'reasoning_traces').iterdir() if p.is_file()})}  "
          f"unlisted {' '.join(trace_unlisted) if trace_unlisted else 'none'}")

    cl = contents_links()
    cbroken = [h for h in cl if not (ROOT / posixpath.normpath(h.split('#')[0])).exists()]
    cpdf = [h for h in cl if h.endswith(".pdf")]
    print()
    print(f"CONTENTS.md links        {len(cl)}  pdf links {len(cpdf)}  "
          f"broken {len(cbroken)}")
    for b in cbroken[:10]:
        print(f"  BROKEN {b}")
    return 1 if (broken or cbroken) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
