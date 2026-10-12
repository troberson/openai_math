"""Report-only probe: phase timings inside `extract_links.py`'s `main()`.

The cProfile totals attribute cost to functions, not to phases, so this probe wraps the reads the
script performs and prints the wall each phase takes: the .bib walk, the .tex walk, the OAI import
scan, the blob build, the 372-phrase searches, and the MSC scan. Attribution is relative — cProfile
inflates absolutes, so the phase numbers here are the ones to quote.

Promoted from `.qwen/tmp/links_phase_probe.py` on 2026-10-12. Not gated: a phase wall is a function of
a run. Run it before and after a change to the import scan or the MSC rule.
"""
import re
import time
from pathlib import Path

from catlib.paths import OAI_DIR as SOURCE, PREPRINTS

import build_catalog as bc
import extract_links as E

t0 = time.perf_counter()
marks: list[tuple[str, float]] = []


def mark(name: str) -> None:
    marks.append((name, time.perf_counter() - t0))


# the file lists the script builds
listed = {Path(p).parts[1] for ps in bc.parse_contents().values() for p in ps}
bib_files = [p for p in sorted(PREPRINTS.glob("**/*.bib")) if E.owner(p) in listed]
tex_files = [p for p in sorted(PREPRINTS.glob("**/*.tex")) if E.owner(p) in listed]
mark("glob .bib/.tex")

t = time.perf_counter()
txts = [p.read_text(encoding="utf-8", errors="replace") for p in SOURCE.glob("**/*.lean")]
mark(f"read 122,458 .lean ({len(txts)} files)")

t = time.perf_counter()
pat = re.compile(r"^\s*import\s+([A-Za-z_][A-Za-z0-9_.]*)", re.MULTILINE)
tot = 0
for txt in txts:
    for root in pat.findall(txt):
        tot += 1
mark(f"import-root findall over the read texts ({tot} hits)")

t = time.perf_counter()
tot2 = 0
for p in SOURCE.glob("**/*.lean"):
    txt = p.read_text(encoding="utf-8", errors="replace")
    tot2 += len(pat.findall(txt))
mark(f"read+findall in one loop ({tot2} hits)")

t = time.perf_counter()
bib_txts = [p.read_text(encoding="utf-8", errors="replace") for p in bib_files]
mark(f"read {len(bib_files)} .bib")

t = time.perf_counter()
tex_txts = [p.read_text(encoding="utf-8", errors="replace") for p in tex_files]
mark("read " + str(len(tex_files)) + " .tex")

t = time.perf_counter()
normed = [E.norm(t2) for t2 in tex_txts]
mark("norm() over the .tex texts")

t = time.perf_counter()
blob = E.Blob({E.owner(p): " ".join(n) for p, n in zip(tex_files, normed)})
mark("blob build")

titles = {r["fam"]: r["title"] for r in E.ledger_rows()}
t = time.perf_counter()
for title in sorted(titles.values()):
    blob.find(E.norm(title))
mark(f"372 phrase searches over the {len(blob.blob)/1e6:.1f} MB blob")

t = time.perf_counter()
msc = 0
for txt in tex_txts + bib_txts:
    msc += len(E.MSC.findall(txt))
mark(f"MSC scan over {len(tex_txts)+len(bib_txts)} texts")

prev = 0.0
for name, cum in marks:
    print(f"{name:44s} {cum - prev:6.2f}  cum {cum:6.2f}")
    prev = cum
