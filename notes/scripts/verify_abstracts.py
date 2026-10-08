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

--mutant proves the checker discriminates: it corrupts a real quotation, fabricates one, repoints a
real quotation at a file that does not contain it, deletes a marker, names a marker absent from the
table, and points a table row at a path that does not exist -- and requires Pass A/B to flag each
while the real page stays silent.

Usage: python3 notes/scripts/verify_abstracts.py            # check the page
       python3 notes/scripts/verify_abstracts.py --mutant   # discrimination test as well

Writes nothing. Exit 1 when any check fails.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "abstracts.md"

ROW = re.compile(r"^\|\s*(S\d+)\s*\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*$")
MARKER = re.compile(r"\[(S\d+)\]")
QUOTE = re.compile(r"“([^”]+)”")
ABSTRACT = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S)
ELLIPSIS = "…"

sys.path.insert(0, str(ROOT / "notes" / "scripts"))
import build_catalog as B

_OVERVIEW = None


def flat(text):
    return re.sub(r"\s+", " ", text).strip()


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
    return MARKER.match(text[end + gap.end():end + gap.end() + 6])


def parse_table(lines):
    table, dupes = {}, []
    for line in lines:
        m = ROW.match(line)
        if m:
            if m.group(1) in table:
                dupes.append(m.group(1))
            table[m.group(1)] = m.group(2)
    return table, dupes


def check(text, table):
    """-> (problems, stats). Pure: takes the page text so mutants can feed it a modified page."""
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
    stats = {"markers": len(set(MARKER.findall(text))), "sources": len(table),
             "quotes": quotes, "verified": verified}
    return problems, stats


def mutants(text, table):
    """(name, flagged, detail) for each corruption; flagged means Pass A/B caught it.

    Every mutant is built from a real quotation on the real page, so a checker that merely
    re-reads its own regexes and never touches the shipped text cannot pass this test.
    """
    out = []
    q = next(m for m in QUOTE.finditer(text)
             if len(m.group(1)) > 40 and marker_after(text, m.end())
             and table.get(marker_after(text, m.end()).group(1), "").endswith(".tex")
             and "prove" in m.group(1))
    mk = marker_after(text, q.end())
    gap = re.match(r"[ \t\r\n)]*", text[q.end():q.end() + 12]).end()
    mark_start = q.end() + gap
    mark_end = mark_start + len(mk.group(0))

    corrupt = text[:q.start()] + "“" + q.group(1).replace("prove", "disprove", 1) + "”" + text[q.end():]
    probs, st = check(corrupt, table)
    out.append(("quotation word altered", any("not in" in p for p in probs), f"{len(probs)} problem(s): " + "; ".join(probs)[:120]))

    fab = text[:q.start()] + "“the ledger proves every family is formalized in Lean” [S1]\n" + text[q.start():]
    probs, st = check(fab, table)
    out.append(("quotation fabricated", any("not in overview.tex" in p for p in probs),
                f"{len(probs)} problem(s): " + "; ".join(probs)[:120]))

    repoint = text[:mark_start] + "[S31]" + text[mark_end:]
    probs, st = check(repoint, table)
    out.append(("quotation repointed at a file that lacks it",
                any("not in notes/abstracts.tsv" in p for p in probs), f"{len(probs)} problem(s): " + "; ".join(probs)[:120]))

    nomark = text[:mark_start] + text[mark_end:]
    probs, st = check(nomark, table)
    out.append(("marker deleted", any("no [S#] marker" in p for p in probs), f"{len(probs)} problem(s): " + "; ".join(probs)[:120]))

    ghost = text + "\nAn unlisted source [S99] is cited here.\n"
    probs, st = check(ghost, table)
    out.append(("marker absent from the table", any("not in the Sources table" in p for p in probs),
                f"{len(probs)} problem(s): " + "; ".join(probs)[:120]))

    bad = "\n".join(l for l in text.splitlines() if not l.startswith("| S31 |"))
    tbl, _ = parse_table(bad.splitlines())
    tbl["S31"] = "notes/does-not-exist.tsv"
    probs, st = check(bad, tbl)
    out.append(("table path missing on disk", any("does not exist" in p for p in probs),
                f"{len(probs)} problem(s): " + "; ".join(probs)[:120]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", action="store_true", help="run the discrimination test")
    args = ap.parse_args()

    text = PAGE.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    table, dupes = parse_table(lines)

    problems = []
    if not table:
        problems.append("no Sources table rows parsed")
    if dupes:
        problems.append(f"table declares a source twice: {dupes}")
    problems.append("no quotations found") if not QUOTE.search(text) else None

    found, stats = check(text, table)
    problems += found

    for p in problems:
        print(f"PROBLEM {p}")
    print(f"sources {stats['sources']}   markers {stats['markers']}   "
          f"quotations {stats['quotes']}   verified {stats['verified']}")

    if args.mutant:
        if problems:
            print("--- mutants skipped: the real page is not silent")
        else:
            unflagged = 0
            for name, flagged, detail in mutants(text, table):
                print(f"--- mutant {name}: {'FLAGGED' if flagged else 'MISSED'} ({detail})")
                unflagged += 0 if flagged else 1
            problems.append(f"{unflagged} undetected mutants") if unflagged else None

    print(f"{'FAIL' if problems else 'OK'}: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
