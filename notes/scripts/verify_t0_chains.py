#!/usr/bin/env python3
r"""Verify every citation, quotation, table row, and count in notes/t0-chains.md.

Report-only: writes nothing, runs nothing. Lean is never invoked, so nothing here proves a theorem.

Checks, in order:
  1. every backticked `path:line` anchor resolves to a file that exists, with the line in range;
  2. every fenced block is attributed to the nearest PRECEDING anchor (searching back up to 9
     lines) and its joined text must appear verbatim, modulo whitespace, in the same number of
     source lines starting at that anchor — a block re-wrapped from a one-line `overview.tex`
     abstract is checked against that single line, which is why the comparison is joined text
     rather than line by line;
  3. every *"…"* quotation is pinned to an anchor in its own row (an anchor earlier in the same
     line, else the last anchor in the contiguous lines above it) and must appear verbatim,
     modulo whitespace, on that anchored line;
  4. the count phrases are re-derived from notes/catalog.tsv, notes/subfindings.tsv,
     notes/t0-triage.md and the .bib layer by importing extract_t0_chains;
  5. the 27-row summary table and the 5-row chain table are re-derived field by field;
  6. the 27 per-family blocks match the population, each names exactly its own two manuscripts
     with titles that match notes/subfindings.tsv and sit verbatim on the family's anchor line,
     and each Citation layer line matches the recomputed .bib / edge / mutual counts;
  7. the named mutual, one-directional, no-edge and no-.bib lists match the recomputation;
  8. family 268's two verification directories exist.

--mutant corrupts twelve facts, one per check family, and the checker must flag every one.
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import extract_links
import extract_subfinding_pairs as ep
import extract_t0_chains as tc

ROOT = tc.ROOT
PAGE = ROOT / "notes" / "t0-chains.md"
ANCHOR = re.compile(r"`([\w./+-]+?\.(?:py|md|tex|json|txt|lean|yaml|bib)):(\d+)`")
QUOTE = re.compile(r'\*"([^"]{12,})"\*')
HEAD = re.compile(r"^### (\d{3}) — ")
BULLET = re.compile(r'^- \*\*(\d)\*\* \(`overview\.tex:(\d+)`\) — \*"(.+)"\*$')
TARGET = re.compile(r"^  → `([^`]+)`$")
CITE = re.compile(r"Citation layer: (\d+) `\.bib` file[s]?, (\d+) intra-family edges?, (\d+) mutual pair")
SUM_ROW = re.compile(r"^\| (\d{3}) \| (.+?) \| (.+?) \| (\d+) \| (\d+) \| (\d+) \| `overview\.tex:(\d+)` \|$")
CHAIN_ROW = re.compile(r"^\| (\d{3}) \| (T\d) \| " + r" \| ".join([r"(\d+)"] * 7)
                       + r" \| (.+?) \|$")
LIST_LINE = "The {} are {}."
WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
DISC = {
    "Algebraic and complex geometry": "A&CG",
    "Real and complex analysis": "real&complex",
    "Theoretical computer science": "TCS",
    "Dynamical systems and ergodic theory": "dyn sys",
    "Algebra": "algebra",
    "Probability and statistical mechanics": "prob",
    "Group theory": "group theory",
    "Mathematical physics": "mathphys",
    "Operator algebras": "opalg",
    "Topology": "topology",
    "Differential geometry": "diffgeom",
    "Partial differential equations": "PDE",
    "Number theory": "number theory",
}
CHAIN_FAMS = ("001", "032", "002", "006", "311")
VER268 = (
    "preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/verification/",
    "preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/verification/",
)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def measured():
    """Everything the page asserts, recomputed from the shipped files."""
    v = tc.population()
    rows, pop = v["rows"], v["pop"]
    mss = tc.manuscripts()
    edges = tc.release_bib_edges()
    lines = ep.resultentry_lines()
    dirs = {f: sorted({extract_links.owner(pathlib.Path(m["path"])) for m in mss[f]}) for f in pop}
    fam_edges = {f: tc.intra_edges(dirs[f], edges) for f in pop}
    mutual = {f: sum(1 for a, b in fam_edges[f] if (b, a) in fam_edges[f]) // 2 for f in pop}
    bibs = {f: tc.bib_files(dirs[f]) for f in pop}
    cw = tc.companion_word_fams(rows)
    return {
        "v": v,
        "rows": rows,
        "pop": pop,
        "mss": mss,
        "lines": lines,
        "dirs": dirs,
        "fam_edges": fam_edges,
        "mutual": mutual,
        "bibs": bibs,
        "cw": cw,
        "chain_edges": tc.chain_edges(rows),
        "mss_n": sum(len(mss[f]) for f in pop),
        "with_edge": sorted(f for f in pop if fam_edges[f]),
        "mutual_fams": sorted(f for f in pop if mutual[f]),
        "oneway": sorted(f for f in pop if fam_edges[f] and not mutual[f]),
        "noedge": sorted(f for f in pop if not fam_edges[f]),
        "nobib": sorted(f for f in pop if not fam_edges[f] and not bibs[f]),
        "overview": (ROOT / "overview.tex").read_text(encoding="utf-8", errors="replace").split("\n"),
    }


def count_phrases(m):
    v, rows, pop, cw = m["v"], m["rows"], m["pop"], m["cw"]
    cw_pop = [f for f in pop if rows[f]["companion_word"] == "1"]
    return [
        (f"**{len(pop)}** families carrying **{m['mss_n']}** manuscripts", "population"),
        (f"**{len(v['paps2'])}** families with exactly 2 manuscripts", "repo-wide paps==2"),
        (f"`T0:{v['paps2_tiers']['T0']}`, `T2:{v['paps2_tiers']['T2']}`, "
         f"`T3:{v['paps2_tiers']['T3']}`", "paps==2 tiers"),
        (f"**{len(v['t0_paps2'])}** at T0", "T0 paps==2"),
        (f"**{len(v['first_pass'])}** were read in the first pass "
         f"({', '.join(v['first_pass'])})", "first pass"),
        (f"holds for **{len(v['zero_signal'])}** of the {len(pop)} "
         f"and fails for **{len(v['signal_outliers'])}**", "coverage signal"),
        ("`verification = 2`", "268 verification"),
        (f"Over **{len(rows)}** families that yields **{len(m['chain_edges'])}** edges", "chain edges"),
        (f"fires on **{len(cw)}** families — {', '.join(cw)} — and "
         f"**{sum(1 for f in cw if rows[f]['companions'])}** of them carry a `companions` edge",
         "companion_word"),
        (f"**{len(cw_pop)}** use the word ({', '.join(cw_pop)})", "companion_word in population"),
        (f"**{len(m['with_edge'])}** of the {len(pop)} cite their sibling: "
         f"**{len(m['mutual_fams'])}** mutual pairs and **{len(m['oneway'])}** one-directional",
         "intra-family edges"),
        (f"**{len(m['noedge'])}** cite no sibling, and **{len(m['nobib'])}** of those "
         f"({', '.join(m['nobib'])})", "no-edge families"),
    ]


def file_lines(cache, rel):
    if rel not in cache:
        cache[rel] = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
    return cache[rel]


def check_anchors(lines, cache, problems):
    """Count anchor occurrences; flag the ones that do not resolve."""
    seen, n = set(), 0
    for i, line in enumerate(lines):
        for path, num in ANCHOR.findall(line):
            n += 1
            key = (path, int(num))
            if key in seen:
                continue
            if not (ROOT / path).exists():
                problems.append(f"anchor file absent: {path}:{num} (page line {i + 1})")
                continue
            src = file_lines(cache, path)
            if not 1 <= int(num) <= len(src):
                problems.append(f"anchor line out of range: {path}:{num} "
                                f"(file has {len(src)} lines, page line {i + 1})")
                continue
            seen.add(key)
    return n


def check_blocks(lines, cache, problems):
    """Each fenced block is attributed to the nearest preceding anchor."""
    n, i = 0, 0
    while i < len(lines):
        if not lines[i].startswith("```"):
            i += 1
            continue
        end = next((j for j in range(i + 1, len(lines)) if lines[j].startswith("```")), None)
        if end is None:
            problems.append(f"unterminated fenced block at page line {i + 1}")
            return n
        n += 1
        anchor = None
        for back in range(i - 1, max(i - 10, -1), -1):
            found = list(ANCHOR.finditer(lines[back]))
            if found:
                anchor = found[-1]
                break
        if anchor is None:
            problems.append(f"fenced block at page line {i + 1} has no preceding anchor")
            i = end + 1
            continue
        path, num = anchor.group(1), int(anchor.group(2))
        if not (ROOT / path).exists():
            i = end + 1
            continue
        body = [l for l in lines[i + 1:end] if l.strip()]
        if not body:
            problems.append(f"empty fenced block at page line {i + 1}")
            i = end + 1
            continue
        window = " ".join(file_lines(cache, path)[num - 1:num - 1 + len(body)])
        if norm(" ".join(body)) not in norm(window):
            problems.append(f"block at page line {i + 1} does not match {path}:{num} "
                            f"over {len(body)} lines: {body[0][:60]!r}")
        i = end + 1
    return n


def check_quotes(lines, cache, problems):
    """Each *"…"* quote is pinned to an anchor in its own row (contiguous lines)."""
    n = 0
    for i, line in enumerate(lines):
        hits = list(QUOTE.finditer(line))
        if not hits:
            continue
        top = i
        while top > 0 and lines[top - 1].strip():
            top -= 1
        span_anchor = None
        for sl in lines[top:i]:
            found = list(ANCHOR.finditer(sl))
            if found:
                span_anchor = found[-1]
        for q in hits:
            n += 1
            anchor = next((m for m in ANCHOR.finditer(line) if m.end() <= q.start()), span_anchor)
            if anchor is None:
                problems.append(f"quote at page line {i + 1} has no anchor in its row: "
                                f"{q.group(1)[:60]!r}")
                continue
            path, num = anchor.group(1), int(anchor.group(2))
            if not (ROOT / path).exists() or not 1 <= num <= len(file_lines(cache, path)):
                continue
            if norm(q.group(1)) not in norm(file_lines(cache, path)[num - 1]):
                problems.append(f"quote at page line {i + 1} is not on {path}:{num}: "
                                f"{q.group(1)[:60]!r}")
    return n


def check_counts(flat, m, problems):
    for phrase, label in count_phrases(m):
        if norm(phrase) not in flat:
            problems.append(f"count phrase missing ({label}): {phrase!r}")
    return len(count_phrases(m))


def check_summary_table(lines, m, problems):
    rows = [r for r in (SUM_ROW.match(l) for l in lines) if r]
    fams = sorted(r.group(1) for r in rows)
    if fams != m["pop"]:
        problems.append(f"summary table families {fams} != population {m['pop']}")
    for r in rows:
        fam, disc, shapes, bib, edges, mutual, ln = r.groups()
        want = m["rows"][fam]
        if disc != DISC.get(want["discipline"], want["discipline"]):
            problems.append(f"{fam}: table discipline {disc!r} != ledger {want['discipline']!r}")
        want_shapes = ", ".join(want["shapes"].split("|")) if want["shapes"] else "-"
        if shapes != want_shapes:
            problems.append(f"{fam}: table shapes {shapes!r} != ledger {want_shapes!r}")
        recomputed = {"bib": len(m["bibs"][fam]), "edges": len(m["fam_edges"][fam]),
                      "mutual": m["mutual"][fam]}
        for got, key, label in ((bib, "bib", ".bib"), (edges, "edges", "edges"),
                                (mutual, "mutual", "mutual")):
            if int(got) != recomputed[key]:
                problems.append(f"{fam}: table {label} {got} != recomputed {recomputed[key]}")
        if int(ln) != m["lines"][fam]:
            problems.append(f"{fam}: table anchor overview.tex:{ln} != "
                            f"overview.tex:{m['lines'][fam]}")
    return len(rows)


def check_chain_table(lines, m, problems):
    rows = [r for r in (CHAIN_ROW.match(l) for l in lines) if r]
    fams = sorted(r.group(1) for r in rows)
    if fams != sorted(CHAIN_FAMS):
        problems.append(f"chain table families {fams} != {sorted(CHAIN_FAMS)}")
    for r in rows:
        fam, tier, paps, form, chal, mainres, scope, ver, trace, shapes = r.groups()
        want = m["rows"][fam]
        got = {"tier": tier, "paps": paps, "paps_form": form, "chal": chal, "mainres": mainres,
               "scope_note": scope, "verification": ver, "trace": trace}
        for key, label in (("tier", "tier"), ("paps", "manuscripts"), ("paps_form", "formalized"),
                           ("chal", "challenges"), ("mainres", "main_results"),
                           ("scope_note", "scope note"), ("verification", "verification"),
                           ("trace", "trace")):
            if got[key] != (want[key] or "0"):
                problems.append(f"chain table {fam} {label} {got[key]!r} != ledger "
                                f"{(want[key] or '0')!r}")
        want_shapes = ", ".join(want["shapes"].split("|")) if want["shapes"] else "-"
        if shapes != want_shapes:
            problems.append(f"chain table {fam} shapes {shapes!r} != ledger {want_shapes!r}")
    return len(rows)


def check_family_blocks(lines, m, problems):
    """The 28 per-family blocks: population, manuscripts, titles, citation layer."""
    heads = [(f"{int(h.group(1)):03d}", i) for i, l in enumerate(lines) if (h := HEAD.match(l))]
    fams = sorted(f for f, _ in heads)
    if fams != m["pop"]:
        problems.append(f"family blocks {fams} != population {m['pop']}")
    n_bullets = 0
    for idx, (fam, start) in enumerate(heads):
        if fam not in m["pop"]:
            problems.append(f"{fam}: block for a family outside the population")
            continue
        stop = heads[idx + 1][1] if idx + 1 < len(heads) else len(lines)
        body = [l for l in lines[start:stop] if not l.startswith("## ")]
        bullets = [(BULLET.match(l), k) for k, l in enumerate(body) if BULLET.match(l)]
        targets = [TARGET.match(l).group(1) for l in body if TARGET.match(l)]
        if len(bullets) != 2:
            problems.append(f"{fam}: {len(bullets)} manuscript bullets, expected 2")
            continue
        if len(targets) != 2:
            problems.append(f"{fam}: {len(targets)} manuscript paths, expected 2")
        for (b, k), want in zip(bullets, m["mss"][fam], strict=False):
            seq, anchor, title = b.groups()
            if seq != want["seq"]:
                problems.append(f"{fam}: bullet seq {seq} != subfindings seq {want['seq']}")
            if int(anchor) != m["lines"][fam]:
                problems.append(f"{fam}: bullet anchor overview.tex:{anchor} != "
                                f"overview.tex:{m['lines'][fam]}")
            if title != want["title"]:
                problems.append(f"{fam}/{seq}: quoted title {title!r} != subfindings title "
                                f"{want['title']!r}")
            if norm(title) not in norm(m["overview"][m["lines"][fam] - 1]):
                problems.append(f"{fam}/{seq}: title not verbatim on overview.tex:"
                                f"{m['lines'][fam]}: {title!r}")
            nxt = TARGET.match(body[k + 1]) if k + 1 < len(body) else None
            if nxt is None:
                problems.append(f"{fam}: no path line under the bullet at block line {k + 1}")
            elif nxt.group(1) != want["path"]:
                problems.append(f"{fam}/{seq}: path {nxt.group(1)!r} != subfindings path "
                                f"{want['path']!r}")
            elif not (ROOT / want["path"]).exists():
                problems.append(f"{fam}/{seq}: manuscript absent on disk: {want['path']}")
            n_bullets += 1
        cites = list(CITE.finditer(norm(" ".join(body))))
        if len(cites) != 1:
            problems.append(f"{fam}: {len(cites)} Citation layer lines, expected 1")
            continue
        got = tuple(int(x) for x in cites[0].groups())
        want = (len(m["bibs"][fam]), len(m["fam_edges"][fam]), m["mutual"][fam])
        if got != want:
            problems.append(f"{fam}: citation layer {got} != recomputed {want}")
    return len(heads), n_bullets


def check_lists(flat, m, problems):
    want = {
        "mutual pairs": m["mutual_fams"],
        "one-directional edges": m["oneway"],
        f"{len(m['noedge'])} with no intra-family edge": m["noedge"],
    }
    for kind, ids in want.items():
        if norm(LIST_LINE.format(kind, ", ".join(ids))) not in flat:
            problems.append(f"named list mismatch ({kind}): expected {', '.join(ids)!r}")
    spelled = WORDS[len(m["nobib"])] if len(m["nobib"]) < len(WORDS) else str(len(m["nobib"]))
    needle = norm(f"{spelled} of them ({', '.join(m['nobib'])}) ship no")
    if needle.lower() not in flat.lower():
        problems.append(f"no-.bib sentence mismatch: expected {needle!r}")
    return len(want) + 1


def check_files(_m, problems):
    for rel in VER268:
        if not (ROOT / rel).is_dir():
            problems.append(f"268 verification directory absent: {rel}")
    return len(VER268)


def check(text, m):
    lines = text.split("\n")
    flat = norm(text)
    cache = {}
    problems = []
    n_anchor = check_anchors(lines, cache, problems)
    n_block = check_blocks(lines, cache, problems)
    n_quote = check_quotes(lines, cache, problems)
    n_count = check_counts(flat, m, problems)
    n_sum = check_summary_table(lines, m, problems)
    n_chain = check_chain_table(lines, m, problems)
    n_head, n_bullets = check_family_blocks(lines, m, problems)
    n_list = check_lists(flat, m, problems)
    n_file = check_files(m, problems)
    return {
        "problems": problems,
        "anchors": n_anchor,
        "blocks": n_block,
        "quotes": n_quote,
        "counts": n_count,
        "sum_rows": n_sum,
        "chain_rows": n_chain,
        "heads": n_head,
        "bullets": n_bullets,
        "lists": n_list,
        "files": n_file,
    }


MUTANTS = {
    "paraphrase-as-quote": lambda t: t.replace(
        '*"The unique threshold bound state of the SU(N) BFSS model"*',
        '*"The unique threshold bound state for the SU(N) BFSS model"*'),
    "title-swap": lambda t: t.replace(
        '*"Boundary-field gap"*', '*"Positive eigenvalues of the relative SU(2) BFSS Hamiltonian"*'),
    "chain-tier": lambda t: t.replace("| 032 | T0 | 5 |", "| 032 | T2 | 5 |"),
    "edge-count": lambda t: t.replace("**15** of the 27 cite their sibling",
                                      "**16** of the 27 cite their sibling"),
    "anchor-range": lambda t: t.replace("(`overview.tex:716`)", "(`overview.tex:9999`)"),
    "deleted-block": lambda t: t.replace("### 300 — ", "### 301 — "),
    "bib-count": lambda t: t.replace("| 035 | A&CG | bound, classification | 1 | 0 | 0 |",
                                     "| 035 | A&CG | bound, classification | 3 | 0 | 0 |"),
    "path-missing": lambda t: t.replace(
        "preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/"
        "article.pdf",
        "preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/"
        "paper.pdf"),
    "pop-count": lambda t: t.replace("**27** families carrying", "**28** families carrying"),
    "mutual-list": lambda t: t.replace(
        "The mutual pairs are 041, 077, 217, 265, 268, 286, 302, 368.",
        "The mutual pairs are 077, 217, 265, 268, 286, 302, 368."),
    "block-line": lambda t: t.replace(
        "  journal = {Selecta Mathematica. New Series},", "  journal = {Selecta Math.},"),
    "citation-layer": lambda t: t.replace(
        "Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.\n\n"
        "### 270 — ", "Citation layer: 2 `.bib` files, 3 intra-family edges, 1 mutual pair.\n\n"
        "### 270 — "),
}


def main(argv):
    mutant = "--mutant" in argv
    text = PAGE.read_text(encoding="utf-8")
    m = measured()
    res = check(text, m)
    print(f"== page {PAGE.relative_to(ROOT)}")
    print(f"anchors {res['anchors']}  blocks {res['blocks']}  quotes {res['quotes']}  "
          f"counts {res['counts']}")
    print(f"summary rows {res['sum_rows']}  chain rows {res['chain_rows']}  blocks {res['heads']}  "
          f"bullets {res['bullets']}  lists {res['lists']}  files {res['files']}")
    for p in res["problems"]:
        print(f"PROBLEM {p}")
    print(f"problems {len(res['problems'])}")
    missed = 0
    if mutant:
        print("\n== mutants")
        for name, fn in MUTANTS.items():
            mutated = fn(text)
            if mutated == text:
                print(f"  {name:<20} NOT INJECTED (phrase absent from the page)")
                missed += 1
                continue
            found = check(mutated, m)["problems"]
            if found:
                print(f"  {name:<20} caught: {found[0][:88]}")
            else:
                print(f"  {name:<20} NOT CAUGHT")
                missed += 1
        print(f"mutants caught {len(MUTANTS) - missed}/{len(MUTANTS)}")
    return 1 if (res["problems"] or missed) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
