#!/usr/bin/env python3
"""Verify every quotation and source marker in notes/abstracts.md against the shipped files.

The page cites sources as [S1] .. [S33]; the Sources table at the bottom maps S# to a repo-relative
path. Two passes read the same table:

  Pass A (markers) - every marker resolves to a table row, every table path exists on disk, every
                     table row is cited at least once, and every table row is named exactly once.
  Pass B (quotes)  - every “…” span in the page is followed by a marker on the same line and must
                     appear, verbatim modulo whitespace, in the text that marker's file carries:
                     the \resultentry abstracts for overview.tex, the \begin{abstract} bodies for a
                     manuscript .tex, and the whole file for a .tsv or .py. A span containing the
                     ellipsis character is split on it and each part is checked.

Pass B is the load-bearing pass: Pass A proves a file exists, it proves nothing about the text we
attribute to it, so a paraphrase dressed as a quote passes Pass A.

Pass C (counts) re-measures the page's numbers from the corpus by calling
`compare_abstracts.measure()` and requires every count phrase below to appear in the page verbatim.
Passes A/B are silent about counts, and a page whose counts are prose drifts silently: the 2026-10-07
upstream merge moved 13 of the phrases on this page and neither pass noticed. Pass C is what makes
"quote a count only from a fresh report" checkable. The pre-merge reproduction the page quotes is a
probe, not a shipped measurement, and is deliberately not in the phrase list.

Pass D (sync) diffs the page bytes against the bytes `render_reports.py` renders for this page. Pass C
proves the numbers on the page are measured by an independent recount; Pass D proves the page is the
writer's text. Neither proves the other's half: a render-diff reads the writer's own code, so it
cannot catch a number that is wrong in both, and Pass C reads only the phrases in its own list, so it
cannot see prose the list never names.

The self-tests live in `notes/scripts/tests/test_abstracts.py`: they inject the twelve corruptions the
page records — a quotation word altered, a quotation fabricated, a quotation repointed at a table row
that cannot carry it, a marker deleted, a marker absent from the table, a table path missing on disk,
the headline count, a tag-table row, a bucket count, the disagreement count, a multi-abstract
directory name, and a prose count outside the phrase list (visible only to Pass D) — into the page
text in memory and assert the pass that owns each one reports it. This script measures; it no longer
injects.

Usage:
  python3 notes/scripts/verify_abstracts.py
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_abstracts.py -q

Writes nothing. Exit 1 when any check fails.
"""
import re
import sys

import build_catalog as B
import compare_abstracts as CA
from catlib import render as RD
from catlib.paths import LEDGER_TSV, NOTES, ROOT
from catlib.text import collapse_ws
from catlib.tsv import read_rows

PAGE = NOTES / "abstracts.md"

ROW = re.compile(r"^\|\s*(S\d+)\s*\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*$")
MARKER = re.compile(r"\[(S\d+)\]")
QUOTE = re.compile(r"“([^”]+)”")
ABSTRACT = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.DOTALL)
ELLIPSIS = "…"

_OVERVIEW = None
_MEASURED = None

flat = collapse_ws


def overview_text():
    """Every family abstract as the ledger's own parser reads it, whitespace-collapsed.

    A \\resultentry regex over the raw file is not enough: the abstracts contain braces
    ($\\sum_{j\\ge0}$, $\\mathbb R^3$), so a [^{}]* group cannot match them and a regex reader
    silently drops the families whose abstracts are the most math-heavy -- exactly the ones quoted
    on the page. Reusing parse_overview() means the checker sees the text the ledger tags. Cached
    because every [S1] quotation would otherwise re-parse a 1.3 MB file.
    """
    global _OVERVIEW
    if _OVERVIEW is None:
        order, fams = B.parse_overview()
        _OVERVIEW = " ".join(flat(fams[f]["abstract"]) for f in order)
    return _OVERVIEW


def source_text(rel):
    """The text a marker's file carries, whitespace-collapsed. None when the file is absent."""
    p = ROOT / rel
    if not p.is_file():
        return None
    raw = p.read_text(encoding="utf-8", errors="replace")
    if rel == "overview.tex":
        return overview_text()
    if rel.endswith(".tex"):
        envs = [flat(m.group(1)) for m in ABSTRACT.finditer(raw)]
        if not envs:
            return ""
        return " ".join(envs)
    return flat(raw)


def marker_after(text, end):
    """The [S#] marker that follows a closing quote at offset `end`, or None.

    Whitespace, a newline (a wrapped quotation ends on one), and a closing parenthesis are allowed
    between the quote and its marker; anything else means the quotation is unanchored.
    """
    gap = re.match(r"[ \t\r\n)]*", text[end:end + 12])
    tail = text[end + gap.end():end + gap.end() + 6] if gap else text[end:end + 6]
    return MARKER.match(tail) if tail else None


def parse_table(lines):
    table, dupes = {}, []
    for line in lines:
        m = ROW.match(line)
        if m:
            if m.group(1) in table:
                dupes.append(m.group(1))
            table[m.group(1)] = m.group(2)
    return table, dupes


def measured():
    """One fresh compare_abstracts.measure() per process: Pass C's source of truth."""
    global _MEASURED
    if _MEASURED is None:
        _MEASURED = CA.measure()
    return _MEASURED


def population():
    """measured() under the name build_report_templates.checker_needles() looks for."""
    return measured()


def count_phrases(m):
    """(phrase, label) for every count the page must carry, rebuilt from a fresh measurement.

    Passes A and B check quotations and markers and are silent about numbers, so a page whose counts
    are prose drifts silently. Each phrase is the exact string the page must contain, compared with
    whitespace collapsed on both sides. The pre-merge reproduction in the floor paragraph is a probe
    (it points the extractor at a historical notes/tables/sources.tsv), not a shipped measurement, so its
    figures are deliberately absent here.
    """
    n, fam = len(m["man"]), m["families"]
    dirs, envs = m["dirs_with_abstract"], m["abstract_envs"]
    mr, fr = m["man_ratio"], m["fam_ratio"]
    mb, fb = m["man_buckets"], m["fam_buckets"]
    bkey = ("<0.30", "0.30-0.50", "0.50-0.70", "0.70-0.90", ">=0.90")
    low = [x for x in m["man"] if x["ratio"] < 0.05]
    dis = sorted(f for f, sh in m["fam_shapes"].items() if sh["ov"] != sh["ms"])
    paps = {r["fam"]: int(r["paps"]) for r in read_rows(LEDGER_TSV)}
    single = sum(1 for f in dis if paps[f] == 1)
    res, und = m["tag_tot"]["resolution"], m["tag_tot"]["undecidability"]
    cond = m["tag_dis"].get("conditional", {"ov-only": [], "ms-only": []})
    minrow = min(m["man"], key=lambda x: x["ratio"])
    out = [
        (f"Over all {n} manuscript comparisons:", "manuscript comparison count"),
        (f"**0 identical, 0 abridged, {n} divergent.**", "headline relation counts"),
        (f"Over the {fam} family best matches: **0 identical, 0 abridged, {fam} divergent.**",
         "family relation counts"),
        (f"Manuscript-level: {n} comparisons", "units bullet (manuscripts)"),
        (f"Family-level: {fam} comparisons", "units bullet (families)"),
        (f"**Abstract environments: {envs} over {dirs} directories.**", "abstract environments"),
        (f"Every one of the {dirs} manuscript directories", "directories with an abstract"),
        (f"reads {dirs} and cannot show this.", "sources.tsv flag column"),
        ((f"| manuscript-level | {n} | {mr['min']:.3f} | {mr['p10']:.3f} | **{mr['median']:.3f}** "
         f"| {mr['p90']:.3f} | {mr['max']:.3f} |"), "manuscript ratio row"),
        ((f"| family-level best match | {fam} | {fr['min']:.3f} | {fr['p10']:.3f} "
         f"| **{fr['median']:.3f}** | {fr['p90']:.3f} | {fr['max']:.3f} |"), "family ratio row"),
        ((f"| count | {' / '.join(str(mb[k]) for k in bkey)} "
         f"| {' / '.join(str(fb[k]) for k in bkey)} |"), "bucket row"),
        (", ".join(f"**{f}** ({m['fam_best'][f]['ratio']:.3f})" for f in m["fam_hi"]),
         "near-identical families"),
        (f"below 0.05: {', '.join(m['fam_lo'])}.", "low best-match families"),
        ((f"**{len(low)} of the {n}** comparisons fall below 0.05, spread over "
         f"**{len({x['fam'] for x in low})}** families."), "manuscript-level floor"),
        (f"The manuscript-level minimum {minrow['ratio']:.3f} is family {minrow['fam']}'s surviving",
         "manuscript-level minimum"),
        (f"man{n}", "tag table header token"),
    ]
    for s in sorted(m["tag_tot"]):
        d = m["tag_dis"].get(s, {"ov-only": [], "ms-only": []})
        t = m["tag_tot"][s]
        out.append(((f"| {s} | {t['ov']} | {t['ms']} | {t['man']} | {len(d['ov-only'])} "
                    f"| {len(d['ms-only'])} |"), f"tag row {s}"))
    out += [
        ((f"**{len(dis)} of {fam} families have at least one shape disagreement between the two "
         f"texts; {fam - len(dis)} have none.**"), "shape disagreement count"),
        ((f"Of the {len(dis)}, {single} are single-manuscript families and {len(dis) - single} are "
         f"multi-manuscript families."), "disagreement manuscript split"),
        ((f"{res['ov']} of {fam} families ({round(100 * res['ov'] / fam)}%) call a resolution in "
         f"the overview, against {res['man']} of {n} manuscripts "
         f"({round(100 * res['man'] / n)}%)"), "resolution over-flag rate"),
        (f"({und['ov']} families vs {und['man']} manuscripts)", "undecidability rate"),
        ((f"{len(m['cond_dis'])} families disagree on the `conditional` tag: "
         f"{len(cond['ov-only'])} flagged by the overview only ({', '.join(cond['ov-only'])}) "
         f"and {len(cond['ms-only'])}"), "conditional disagreements"),
        (f"({res['ov']} of {fam} families vs {res['man']} of {n} manuscripts)",
         "consequence bullet resolution counts"),
        (f"(one row per family, {fam} rows)", "tsv row count (rule paragraph)"),
        (f"— {fam} rows with the best-match ratio", "tsv row count (consequence bullet)"),
        (minrow["dir"][:40], "minimum-ratio manuscript directory"),
    ]
    for fam_id, d, _k in m["multi_dirs"]:
        out.append((f"`{d}`", f"multi-abstract directory {fam_id}"))
    for fam_id in sorted(m["fam_order"], key=lambda f: m["fam_best"][f]["ratio"])[:8]:
        out.append((f"| {fam_id} | {m['fam_best'][fam_id]['ratio']:.3f} |",
                    f"lowest-ratio row {fam_id}"))
    return out


def check(text, table, counts=None):
    """-> (problems, stats). Pure: takes the page text so mutants can feed it a modified page.

    `counts` is a compare_abstracts.measure() result; Pass C runs only when it is supplied, so the
    quotation/marker mutants do not pay for the corpus scan.
    """
    problems = []
    for s in sorted(set(MARKER.findall(text))):
        if s not in table:
            problems.append(f"marker {s} is not in the Sources table")
    for s, rel in sorted(table.items()):
        p = ROOT / rel
        if not p.is_file():
            problems.append(f"{s} names a path that does not exist: {rel}")
        elif s not in text:
            problems.append(f"{s} ({rel}) is declared in the table and cited nowhere")
    for rel in table.values():
        if rel.endswith(".tex") and source_text(rel) == "":
            problems.append(f"source file has no abstract environment: {rel}")

    quotes = 0
    verified = 0
    for m in QUOTE.finditer(text):
        quotes += 1
        mk = marker_after(text, m.end())
        if not mk:
            problems.append(f"quotation has no [S#] marker: “{m.group(1)[:60]}…”")
            continue
        rel = table.get(mk.group(1))
        if rel is None:
            continue
        hay = source_text(rel)
        parts = [flat(p) for p in m.group(1).split(ELLIPSIS) if len(flat(p)) >= 6]
        missing = [p for p in parts if p not in hay]
        if missing:
            problems.append(f"quotation not in {rel}: “{missing[0][:60]}…”")
        else:
            verified += 1

    phrases = 0
    if counts is not None:
        page = flat(text)
        for phrase, label in count_phrases(counts):
            phrases += 1
            if flat(phrase) not in page:
                problems.append(
                    f"count mismatch ({label}): page does not contain {flat(phrase)!r}")

    sync = RD.sync_problems(PAGE, text)
    problems.extend(sync)

    stats = {"markers": len(set(MARKER.findall(text))), "sources": len(table),
             "quotes": quotes, "verified": verified, "phrases": phrases, "sync": len(sync)}
    return problems, stats


def main():
    text = PAGE.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    table, dupes = parse_table(lines)

    problems = []
    if not table:
        problems.append("no Sources table rows parsed")
    if dupes:
        problems.append(f"table declares a source twice: {dupes}")
    if not QUOTE.search(text):
        problems.append("no quotations found")

    counts = population()
    found, stats = check(text, table, counts)
    problems += found

    for p in problems:
        print(f"PROBLEM {p}")
    print(f"sources {stats['sources']}   markers {stats['markers']}   "
          f"quotations {stats['quotes']}   verified {stats['verified']}   "
          f"count phrases {stats['phrases']}   sync problems {stats['sync']}")

    print(f"{'FAIL' if problems else 'OK'}: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
