"""Report-only probe: price the four candidate scans before any of them is written into the script.

Each candidate is measured against the rule it must reproduce, so the numbers are measurements, not
projections: the early-exit import scan against the whole-file findall, the single-pass norm against
the four-regex norm, the MSC prefilter against the bare scan, and one 372-alternative regex pass over
the blob against 372 str.find passes. Measured 2026-10-12: the import header (5.45 → 3.27 s, counts
equal 334,577 both ways) and the MSC gate (1.97 → 0.11 s, hits 0 both ways) were accepted; the
single-pass norm (3.48 s, outputs not equal) and the alternation (4.33 s) were rejected.

Promoted from `.qwen/tmp/links_scan_probe.py` on 2026-10-12. Not gated: a candidate's wall is a
function of a run, and the accepted rules are already in `extract_links.py`.
"""
import re
import time
from collections import Counter
from pathlib import Path

import build_catalog as bc
import extract_links as E
from catlib.paths import OAI_DIR as SOURCE
from catlib.paths import PREPRINTS

listed = {Path(p).parts[1] for ps in bc.parse_contents().values() for p in ps}
tex_files = [p for p in sorted(PREPRINTS.glob("**/*.tex")) if E.owner(p) in listed]
bib_files = [p for p in sorted(PREPRINTS.glob("**/*.bib")) if E.owner(p) in listed]
lean = sorted(SOURCE.glob("**/*.lean"))

IMPORT = re.compile(r"^\s*import\s+([A-Za-z_][A-Za-z0-9_.]*)", re.MULTILINE)


def whole_file() -> Counter:
    c: Counter[str] = Counter()
    for p in lean:
        for root in IMPORT.findall(p.read_text(encoding="utf-8", errors="replace")):
            c[root.split(".")[0]] += 1
    return c


def early_exit() -> Counter:
    """Imports sit at the top of a Lean file: stop at the first line that is not blank, a comment,
    an import, an opening module/def header, or an `open`/`namespace` line."""
    c: Counter[str] = Counter()
    for p in lean:
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith(("--", "/--", "-/")):
                continue
            if s.startswith("import "):
                for tok in s[len("import "):].split():
                    if re.match(r"[A-Za-z_][A-Za-z0-9_.]*", tok):
                        c[tok.split(".")[0]] += 1
                continue
            if s.startswith(("open ", "namespace ", "set_option ", "--")):
                continue
            break
    return c


t = time.perf_counter()
a = whole_file()
t_whole = time.perf_counter() - t
t = time.perf_counter()
b = early_exit()
t_early = time.perf_counter() - t
print(f"import scan  whole-file findall {t_whole:6.2f} s  early-exit {t_early:6.2f} s  "
      f"counts equal {a == b}  hits {sum(a.values())} vs {sum(b.values())}")

texts = [p.read_text(encoding="utf-8", errors="replace") for p in tex_files]
t = time.perf_counter()
n1 = [E.norm(x) for x in texts]
t_norm = time.perf_counter() - t

SUB = re.compile(r"'s\b|[^a-z0-9]+")
THE = re.compile(r"(?<!\w)the(?!\w)")


def norm_fast(s: str) -> str:
    s = s.lower().replace("\u2019", "'").replace("\u2018", "'")
    s = SUB.sub(" ", s)
    s = THE.sub(" ", s)
    return " ".join(s.split())


t = time.perf_counter()
n2 = [norm_fast(x) for x in texts]
t_fast = time.perf_counter() - t
print(f"norm         four-regex {t_norm:6.2f} s  single-pass {t_fast:6.2f} s  "
      f"outputs equal {n1 == n2}")

msc = re.compile(r"MSC\s?-?\s?20\d\d|MSC\s*:|\\msc\b|mscclass|Mathematics Subject Classification"
                 r"|Primary\s*:?\s*\d{2}\s?[A-Z]\s?xx", re.IGNORECASE)
t = time.perf_counter()
h1 = sum(len(msc.findall(x)) for x in texts + [p.read_text(encoding="utf-8", errors="replace") for p in bib_files])
t_msc = time.perf_counter() - t
t = time.perf_counter()
h2 = 0
for x in texts:
    low = x.lower()
    if "msc" in low or "subject classification" in low:
        h2 += len(msc.findall(x))
t_pre = time.perf_counter() - t
print(f"MSC scan     bare {t_msc:6.2f} s  prefilter {t_pre:6.2f} s  hits {h1} vs {h2}")

blob = E.Blob({E.owner(p): " ".join(n) for p, n in zip(tex_files, n1, strict=True)})
titles = {r["fam"]: r["title"] for r in E.ledger_rows()}
phrases = sorted({E.norm(t2) for t2 in titles.values() if E.norm(t2)})
t = time.perf_counter()
r1 = {E.norm(t2) for t2 in titles.values() if E.norm(t2) and blob.find(E.norm(t2))}
t_find = time.perf_counter() - t
t = time.perf_counter()
big = re.compile("|".join(re.escape(p) for p in phrases))
hits = {m.group(0) for m in big.finditer(blob.blob)}
t_alt = time.perf_counter() - t
print(f"phrase layer {len(phrases)} phrases over {len(blob.blob)/1e6:.1f} MB: "
      f"372 str.find {t_find:6.2f} s  one alternation {t_alt:6.2f} s  sets equal {r1 == hits}")
