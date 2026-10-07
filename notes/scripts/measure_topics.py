"""Measure a curated topic vocabulary against the four text layers a family ships.

Report-only: writes nothing. Every count in notes/topics.md comes from this report.

A family has four searchable texts, all shipped by the release:

  title    the 2nd argument of its \\resultentry in overview.tex
  abstract the 3rd argument of the same entry
  scope    the text of lean/docs/<NNN>.md, when a scope note exists (235 families)
  path     the Lean file paths reached from the family's comparator configs through
           formalization.yaml main_results (127 families; the release ships no
           manuscript->Lean edge, so this layer is derived, not shipped)

Matching is case-insensitive over those four texts. A term's yield is the number of
families with at least one hit; per-layer counts are reported separately because a
path hit and an abstract hit are not the same kind of evidence — the path layer is
the release's own filing choice, the abstract layer is the release's own prose.

Terms are curated in notes/topics.tsv, not derived: the release ships no topic
vocabulary (0 MSC codes over 8,231 files, 0 bib keywords fields over 12,928 entries,
\\keywords in 12 of 722 manuscript dirs), so there is nothing to derive a term from
and nothing to validate a derived term against. The TSV is the source of truth — the
term, its pattern, the counts it records as evidence, and the reading verdict. Run
with --check to re-measure every row and fail on drift.

The corpus names results by conjecture and by model, not by generic subject words:
its PDE families are "Boltzmann nonuniqueness", "the hot spots conjecture", "De
Giorgi's conjecture in dimension eight", and its probability families are "planar
first-passage percolation", "the Benjamini--Schramm nonuniqueness conjecture", "the
Mezard--Parisi formula for diluted spin glasses". A pattern therefore carries the
subject phrase and the named models the corpus actually uses. Titles are LaTeX, so
an accented name is matched on the letters after the accent escape — "hler" reaches
both K\\"ahler and Kähler, and "erd" reaches every spelling of Erdos.

Run with --families to print, for each term, the titles of the families it flags,
marked T/A/S/P by the layer that hit. That is the reading pass: a term is quotable
only after its flagged families have been read.
"""
from __future__ import annotations

import collections
import csv
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_catalog as B

ROOT = pathlib.Path(__file__).resolve().parents[2]
DOCS = ROOT / "lean" / "docs"
TRIPLE = re.compile(
    r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json\s*\n"
    r"\s*declaration:\s*(\S+)\s*\n\s*file:\s*(\S+)")

# Curated vocabulary lives in notes/topics.tsv, one row per term: the term, its
# pattern, the counts the row records as evidence, a status, and the reading verdict.
# Patterns are case-insensitive and match a stem, not a whole word, so "manifold"
# reaches "manifolds" and "ergodic" reaches "ergodicity". A term with no hit is
# reported as unassigned, not deleted: an unassigned term is a measured statement
# about the corpus, not a defect. Run --check to prove the recorded counts still
# match the corpus; a row whose counts drifted is a stale row, not a rounding
# difference, and --check exits non-zero so a generator can fail on it.
TSV = ROOT / "notes" / "topics.tsv"


def load_vocab(path=TSV):
    """Read the curated vocabulary. The header row fixes the column order."""
    with path.open(encoding="utf-8") as fh:
        return [(r["term"], r["pattern"]) for r in csv.DictReader(fh, delimiter="\t")]


VOCAB = load_vocab()


def scope_text(fam: str) -> str:
    p = DOCS / f"{fam}.md"
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""


def norm(s: str) -> str:
    """Fold the typographic apostrophe to ASCII.

    overview.tex is inconsistent: 76 titles use ASCII ' and 8 use U+2019
    ("Gersten’s conjecture", "Curtis’s conjecture"), so a pattern written with an
    ASCII apostrophe misses a title silently. Folding the text once is cheaper
    than writing ['’] into every one of the 15 apostrophe patterns.
    """
    return s.replace("\u2019", "'")


def lean_paths(fams, docs):
    """family -> set of Lean file paths reached through its comparator configs."""
    _, main_results = B.parse_yaml()
    cfg2file = {}
    yaml = (ROOT / "lean" / "formalization.yaml").read_text(encoding="utf-8")
    for cfg, _decl, fpath in TRIPLE.findall(yaml):
        cfg2file.setdefault(cfg, set()).add(fpath)
    out = collections.defaultdict(set)
    for fam, info in docs.items():
        for cfg in info["configs"]:
            out[fam] |= cfg2file.get(cfg, set())
    return out


def measure(vocab=VOCAB):
    order, fams = B.parse_overview()
    docs = B.parse_docs()
    paths = lean_paths(fams, docs)
    texts = {f: (norm(fams[f]["title"]), norm(fams[f]["abstract"]), norm(scope_text(f)),
                norm(" ".join(sorted(paths.get(f, ())))
                 + " " + " ".join(sorted({p.split("/")[1] for p in paths.get(f, ())
                                          if len(p.split("/")) > 1}))))
             for f in fams}
    rows = []
    for term, pattern in vocab:
        rx = re.compile(pattern, re.I)
        hit = {"title": set(), "abstract": set(), "scope": set(), "path": set()}
        for f, (t, a, s, p) in texts.items():
            if rx.search(t):
                hit["title"].add(f)
            if rx.search(a):
                hit["abstract"].add(f)
            if s and rx.search(s):
                hit["scope"].add(f)
            if p and rx.search(p):
                hit["path"].add(f)
        famset = set().union(*hit.values())
        rows.append({"term": term, "pattern": pattern, "families": famset, **{
            k: v for k, v in hit.items()}})
    return rows, texts


def main(argv=()):
    rows, texts = measure()
    if "--check" in argv:
        with TSV.open(encoding="utf-8") as fh:
            recorded = list(csv.DictReader(fh, delimiter="\t"))
        problems = []
        terms = [r["term"] for r in recorded]
        if len(terms) != len(set(terms)):
            problems.append(f"duplicate terms in {TSV.name}")
        measured = {r["term"]: r for r in rows}
        for rec in recorded:
            row = measured.get(rec["term"])
            if row is None:
                problems.append(f"{rec['term']}: pattern does not compile to a row")
                continue
            want = len(row["families"])
            for col, got in (("fams", want), ("title", len(row["title"])),
                             ("abstract", len(row["abstract"])),
                             ("scope", len(row["scope"])), ("path", len(row["path"]))):
                if int(rec[col]) != got:
                    problems.append(f"{rec['term']}.{col}: recorded {rec[col]}, "
                                    f"measured {got}")
            status = "assigned" if want else "negative"
            if rec["status"] != status:
                problems.append(f"{rec['term']}.status: recorded {rec['status']}, "
                                f"measured {status}")
        covered = set().union(*[r["families"] for r in rows])
        if len(covered) != len(texts):
            problems.append(f"{len(texts) - len(covered)} families carry no topic")
        print(f"topics.tsv check    {len(recorded)} terms, "
              f"{len(covered)} of {len(texts)} families covered, "
              f"problems {len(problems)}")
        for p in problems:
            print(f"  {p}")
        sys.exit(1 if problems else 0)
    if "--families" in argv:
        for r in sorted(rows, key=lambda r: -len(r["families"])):
            print(f"== {r['term']}  {len(r['families'])}")
            for f in sorted(r["families"]):
                mark = "".join(c for c, k in (("T", "title"), ("A", "abstract"),
                                              ("S", "scope"), ("P", "path"))
                              if f in r[k])
                print(f"  {f} {mark:4s} {texts[f][0]}")
        return
    print(f"vocabulary terms      {len(rows)}  over {len(texts)} families")
    print(f"{'term':34s} {'fams':>5} {'title':>6} {'abst':>6} {'scope':>6} {'path':>5}")
    for r in sorted(rows, key=lambda r: -len(r["families"])):
        print(f"{r['term']:34s} {len(r['families']):5d} {len(r['title']):6d} "
              f"{len(r['abstract']):6d} {len(r['scope']):6d} {len(r['path']):5d}")
    zero = [r["term"] for r in rows if not r["families"]]
    print(f"unassigned terms      {len(zero)}  {zero}")
    covered = set().union(*[r["families"] for r in rows]) if rows else set()
    print(f"families covered      {len(covered)} of {len(texts)}  uncovered "
          f"{len(texts) - len(covered)}")
    counts = collections.Counter(len(r["families"]) for r in rows)
    print("yield histogram       " + "  ".join(f"{k}:{counts[k]}"
                                               for k in sorted(counts)))
    topics = collections.Counter(len([r for r in rows if f in r["families"]])
                                 for f in texts)
    print("topics per family     " + "  ".join(f"{k}:{topics[k]}"
                                              for k in sorted(topics)))
    print(f"topic assignments     {sum(len(r['families']) for r in rows)}")


if __name__ == "__main__":
    main(sys.argv[1:])
