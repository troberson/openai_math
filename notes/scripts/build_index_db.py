#!/usr/bin/env python3
"""Build the SQLite FTS5 layer over the manuscript corpus and measure it.

Writer: `.qwen/cache/records/<key>/fts.json` (the measured counts) and
`.qwen/cache/records/<key>/index.db` (the database). The `.qwen/*` rule keeps both untracked, so the
layer is rebuilt by this script and never committed — the bead's rule for the FTS layer. The key is the
builder's key, so a rebuild after a corpus change lands under a new key and the old record is not reused.

The bead's condition is that the TSV index is too blunt for a term query inside a manuscript body. It is:
the index's four texts are the title, the abstract, the scope note and the derived Lean paths, so a body
term is not in the index at all. `notes/development/index-design.md` records the schema decision and
rejects a graph database on size and on edge semantics; this script answers the narrower question the
bead asks — what a full-text layer costs.

The record carries derived counts, never a wall time: a keyed record is a function of the digest, so the
first run's build time read back on a warm run would be a timing artifact. The build and query walls are
printed as a property of the run, and a page that quotes them names them as a dated observation.

`--check-only` builds the index in memory and prints the same report, landing nothing.

Run: python3 notes/scripts/build_index_db.py [--check-only]
"""
from __future__ import annotations

import json
import sqlite3
import sys
import time

from catlib.atomic import RECORDS_ROOT
from catlib.overview import parse_overview
from catlib.paths import ROOT, owner, rel
from catlib.promote import key_for, prune_stale
from catlib.records import cached

PREPRINTS = ROOT / "preprints"
# The bead names `manifold` as the test term. The rest are body terms the topic vocabulary cannot
# reach: its four texts are title, abstract, scope note and derived Lean paths.
TERMS = ("manifold", "amenable", "eigenvalue", "Ricci flow", "Turan", "Jiang-Su",
         "Landau-Siegel", "semidefinite", "Schoenflies", "Laughlin")
SCHEMA = "CREATE VIRTUAL TABLE docs USING fts5(path, dir, fam, kind, body);"


def dir_fam() -> dict[str, str]:
    """Manuscript directory -> family, keyed by the path component after `preprints`."""
    _, fams = parse_overview()
    out: dict[str, str] = {}
    for fam, entry in fams.items():
        for pap in entry["tex_paps"]:
            out[owner(pap)] = fam
    return out


def corpus() -> list[tuple[str, str, str, str, str]]:
    """(repo-relative path, manuscript dir, family, kind, text) for every .tex file and abstract."""
    mapping = dir_fam()
    rows: list[tuple[str, str, str, str, str]] = []
    for p in sorted(PREPRINTS.rglob("*.tex")):
        d = owner(p)
        rows.append((rel(p), d, mapping.get(d, ""), "manuscript",
                     p.read_text(encoding="utf-8", errors="replace")))
    for fam, entry in sorted(parse_overview()[1].items()):
        rows.append(("overview.tex", "", fam, "abstract", entry["abstract"]))
    return rows


def insert(conn: sqlite3.Connection, rows: list[tuple[str, str, str, str, str]]) -> None:
    """Create the FTS5 table, load every row, and merge the segments.

    A rebuild under a key that already landed drops the table first, so re-running the writer against
    an unchanged corpus is idempotent.
    """
    conn.execute("DROP TABLE IF EXISTS docs")
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO docs(path, dir, fam, kind, body) VALUES (?,?,?,?,?)", rows)
    conn.commit()
    conn.execute("INSERT INTO docs(docs) VALUES('optimize')")
    conn.commit()


def hits(conn: sqlite3.Connection) -> tuple[list[tuple[str, int, float]], float]:
    """(term, hits, query wall) for each probe term, and the total query wall."""
    out: list[tuple[str, int, float]] = []
    total = 0.0
    for term in TERMS:
        t0 = time.perf_counter()
        n = conn.execute("SELECT count(*) FROM docs WHERE body MATCH ?", (f'"{term}"',)).fetchone()[0]
        w = time.perf_counter() - t0
        total += w
        out.append((term, n, w))
    return out, total


def population(rows: list[tuple[str, str, str, str, str]], size: int,
               per_term: list[tuple[str, int, float]]) -> dict:
    """The digest-stable counts. No wall time is recorded — a keyed record is a function of the key."""
    tex = [r for r in rows if r[3] == "manuscript"]
    return {"tex_files": len(tex), "tex_bytes": sum(len(r[4].encode("utf-8")) for r in tex),
            "abstract_rows": len(rows) - len(tex), "fts_rows": len(rows), "db_bytes": size,
            "hits": {t: n for t, n, _w in per_term}}


def report(pop: dict, wall: float, qwall: float, where: str,
           per_term: list[tuple[str, int, float]]) -> list[str]:
    """The report lines: the counts, the build wall, and the per-term query wall."""
    lines = [(f"tex files {pop['tex_files']} bytes {pop['tex_bytes']}  "
              f"abstract rows {pop['abstract_rows']}"),
             f"fts rows {pop['fts_rows']}  build wall {wall:.2f} s  landed {where} bytes {pop['db_bytes']}"]
    for term, n, w in per_term:
        lines.append(f"  {term:14} hits {n:5}  wall {w:.4f} s")
    lines.append(f"query wall total {qwall:.4f} s")
    return lines


def measure(check_only: bool) -> list[str]:
    """The report lines. A check-only run builds in memory and lands nothing."""
    rows = corpus()
    t0 = time.perf_counter()
    if check_only:
        conn = sqlite3.connect(":memory:")
        insert(conn, rows)
        wall = time.perf_counter() - t0
        per_term, qwall = hits(conn)
        conn.close()
        pop = population(rows, 0, per_term)
        return report(pop, wall, qwall, "in memory (check-only)", per_term)
    key = key_for("build_index_db.py", tuple(sys.argv[1:]))
    d = RECORDS_ROOT / key
    d.mkdir(parents=True, exist_ok=True)
    db = d / "index.db"
    conn = sqlite3.connect(str(db))
    insert(conn, rows)
    conn.close()
    wall = time.perf_counter() - t0
    conn = sqlite3.connect(str(db))
    per_term, qwall = hits(conn)
    conn.close()
    pop = population(rows, db.stat().st_size, per_term)
    cached(key, "fts.json", lambda: json.dumps(pop, sort_keys=True))
    prune_stale()
    return report(pop, wall, qwall, rel(db), per_term)


def main(argv: list[str]) -> int:
    check_only = "--check-only" in argv
    for line in measure(check_only):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
