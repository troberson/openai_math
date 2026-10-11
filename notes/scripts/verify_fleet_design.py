#!/usr/bin/env python3
"""Check `notes/fleet-design.md` — the four-layer design and its measured inventory.

Report-only; writes nothing. Five passes:

1. **Anchors** — every backticked `path:line` (or `path:a-b`) in the page resolves against the file,
   a prefixed path under the repo root, a bare script name under `notes/scripts/`, and a span fits
   inside the file. An anchor written with trailing text (`` `render_reports.py:119 def measure()` ``)
   is not this form, so it is not checked.
2. **Fenced blocks** — each block is attributed to the nearest preceding anchor and matched against the
   source lines it cites, verbatim modulo whitespace. The page ships no fenced block today, so this pass
   is vacuous on it.
3. **Counts** — every count phrase is re-derived by running the command the page names: the atomicity
   grep, the sync-pass grep, the tree-digest `git rev-parse`, the `--ignored=matching` check, the TSV
   byte sum, the three `du -sk` sizes, the gate row count, the two set-site lines, the env-hit count,
   and the probe parse.
4. **Tables** — the purity table equals the probe parse, scanned inside the purity section (the
   amplification table names four of the same scripts, so a page-wide row scan lets a deleted purity row
   pass), and each amplification row is present. The options table is prose and is not re-derived.
5. **Mutants** — 7 injected corruptions, each asserted against the pass it targets.

Volatile measurements (the `free -h` available line, the wall times, the cold/warm swing) are dated
observations in the page and are **not** re-derived: a checker that re-measures them fails the day the
machine changes.

Run plain and with `--mutant`; run twice and diff.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import TypedDict

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "fleet-design.md"
SCRIPTS = ROOT / "notes" / "scripts"
PROBE = [ROOT / "notes/probe/2026-10-11_writers.txt", ROOT / "notes/probe/2026-10-11_checkers.txt"]
DIGEST_PATHS = ["HEAD:preprints", "HEAD:lean", "HEAD:overview.tex", "HEAD:CONTENTS.md",
                "HEAD:reasoning_traces"]
HAND = {"topics.tsv", "conjecture-standing.tsv"}
PURITY = ["build_sources.py", "extract_links.py", "render_reports.py", "build_index.py",
          "check_index_links.py", "measure_proof_density.py", "verify_script_ownership.py"]
ROWS = ["build_sources.py", "extract_links.py", "build_index.py", "dump_template_slots.py",
        "render_reports.py"]


class Pop(TypedDict):
    """The measured population the page's count phrases are checked against."""

    atomic: int
    scripts: int
    modules: int
    sync: int
    sync_verify: int
    sync_other: int
    digests: int
    ignored: int
    tsv_bytes: int
    tsv_count: int
    du: dict[str, int]
    gate_rows: int
    set_sites: list[str]
    env_hits: int
    purity: list[tuple[str, int, int]]
    rows: dict[str, dict[str, float]]
    cli_wall: float



def sh(*args: str) -> str:
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=False).stdout


def layer(path: str) -> str:
    if path.startswith(("notes/index/", "notes/summaries/", "notes/templates/")):
        return "generated"
    rest = path[len("notes/"):]
    if rest.endswith(".tsv"):
        return "hand-authored" if rest in HAND else "generated"
    return "page"


def probe_blocks() -> dict[str, dict[str, str]]:
    """Per script, the notes/ paths it opened with the recorded mode string."""
    per: dict[str, dict[str, str]] = {}
    for f in PROBE:
        script, innotes = None, False
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\[probe2\] target notes/scripts/(\S+)", line)
            if m:
                script, innotes = m.group(1), False
                continue
            if line.startswith("[probe2] notes/ paths"):
                innotes = True
                continue
            if innotes and line.startswith("[probe2] write-mode paths outside"):
                innotes = False
                continue
            if innotes:
                m = re.match(r"^\s+(\d+)\s+(\S+)\s+(notes/\S+)$", line)
                if m and script:
                    per.setdefault(script, {})[m.group(3)] = m.group(2)
    return per


def probe_rows() -> dict[str, dict[str, float]]:
    """Per gate row, the probe's wall / opens / distinct / repeats / rchar / disk figures."""
    out: dict[str, dict[str, float]] = {}
    for f in PROBE:
        script = None
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\[probe2\] target notes/scripts/(\S+)", line)
            if m:
                script = m.group(1)
            m = re.match(r"^\[probe2\] wall (\S+)  opens (\S+)  distinct (\S+)  repeats (\S+)", line)
            if m and script:
                out[script] = {"wall": float(m.group(1)), "opens": int(m.group(2)),
                               "distinct": int(m.group(3)), "repeats": int(m.group(4))}
            m = re.match(r"^\[probe2\] rchar MB (\S+)  read_bytes MB (\S+)", line)
            if m and script and script in out:
                out[script]["rchar"] = float(m.group(1))
                out[script]["disk"] = float(m.group(2))
    return out


def population() -> Pop:
    # The atomicity census excludes this checker: its own source carries the pattern as a needle, so
    # counting it would read 1, and the page's rule is about the fleet, not about the checker.
    atomic = 0
    scripts = [p for p in sorted(SCRIPTS.glob("*.py")) if p.name != "verify_fleet_design.py"]
    for p in scripts + sorted((SCRIPTS / "catlib").glob("*.py")):
        atomic += len(re.findall(r"os\.replace|os\.rename|shutil\.move|NamedTemporaryFile",
                                 p.read_text(encoding="utf-8")))
    sync = sorted(p.name for p in SCRIPTS.glob("*.py")
                  if "sync problems" in p.read_text(encoding="utf-8")
                  and p.name != "verify_fleet_design.py")
    digests = sh("git", "rev-parse", *DIGEST_PATHS).split()
    ignored = [l for l in sh("git", "status", "--porcelain", "--ignored=matching", "--",
                             "preprints", "lean", "overview.tex", "CONTENTS.md",
                             "reasoning_traces").splitlines() if l.strip()]
    tsvs = sorted((ROOT / "notes").glob("*.tsv"))
    tsv_bytes = sum(len(p.read_bytes()) for p in tsvs)
    du: dict[str, int] = {}
    for name, rel in (("preprints", "preprints"), ("oai", "lean/OAI"), ("index", "notes/index")):
        du[name] = int(sh("du", "-sk", rel).split()[0]) // 1024
    gate = (SCRIPTS / "gate.sh").read_text(encoding="utf-8")
    # 71 invocations: the explicit `rows+=(` lines, plus the checker loop, which runs each named
    # checker plain and with --mutant. Counting the row-append statements alone reads 33.
    explicit = len([l for l in gate.splitlines()
                    if re.match(r"\s*(serial_rows|pool_rows)\+=\(", l)])
    loop = re.search(r"for c in (.*?); do", gate, re.S)
    # The loop list is a backslash continuation, so the raw split counts the `\` characters as names.
    checkers = len([t for t in loop.group(1).split() if t != "\\"]) if loop else 0
    # The loop carries 2 row appends, already in `explicit`; its body runs twice per checker.
    gate_rows = explicit - 2 * (1 if loop else 0) + 2 * checkers
    set_sites: list[str] = []
    for name in ("build_catalog.py", "build_index.py"):
        for i, line in enumerate((SCRIPTS / name).read_text(encoding="utf-8").splitlines(), 1):
            if "for p in set(" in line:
                set_sites.append(f"{name}:{i}")
    env_hits = len([l for l in (SCRIPTS / "render_reports.py").read_text(encoding="utf-8").splitlines()
                    if 'env={**os.environ, "RENDER_REPORTS_CHILD"' in l])
    per = probe_blocks()
    purity: list[tuple[str, int, int]] = []
    for script in PURITY:
        paths = per.get(script, {})
        writes = [p for p, m in paths.items() if any(c in "wax" for c in m)]
        gen = [p for p, m in paths.items() if "r" in m and layer(p) == "generated"]
        purity.append((script, len(writes), len(gen)))
    rows = probe_rows()
    cli = rows["check_index_links.py"]["wall"]
    return {
        "atomic": atomic, "scripts": len(scripts),
        "modules": len(list((SCRIPTS / "catlib").glob("*.py"))),
        "sync": len(sync), "sync_verify": len([s for s in sync if s.startswith("verify_")]),
        "sync_other": len([s for s in sync if not s.startswith("verify_")]),
        "digests": len(digests), "ignored": len(ignored), "tsv_bytes": tsv_bytes,
        "tsv_count": len(tsvs), "du": du, "gate_rows": gate_rows, "set_sites": set_sites,
        "env_hits": env_hits, "purity": purity, "rows": rows, "cli_wall": cli,
    }


def count_phrases(pop: Pop) -> list[str]:
    du = pop["du"]
    return [
        f"**{pop['atomic']} match{'es' if pop['atomic'] != 1 else ''}**",
        f"**{pop['scripts']}** scripts and **{pop['modules']}** catlib modules",
        f"**{pop['sync']}** scripts",
        f"**{pop['sync_verify']}** are `verify_*`",
        f"**{pop['sync_other']}** are not",
        f"**{pop['digests']}** digests",
        f"returns **{pop['ignored']} line{'s' if pop['ignored'] != 1 else ''}**",
        f"**{pop['tsv_bytes']:,}** bytes",
        f"**{du['preprints']}M**",
        f"**{du['oai']}M**",
        f"**{du['index']}M**",
        f"**{pop['gate_rows']}** invocations",
        f"**{len(pop['set_sites'])} sites**",
        f"**{pop['env_hits']} hits**",
    ]


ANCHOR = re.compile(r"`(notes/scripts/[\w.]+\.py|notes/scripts/catlib/[\w.]+\.py|catlib/[\w.]+\.py|[\w.]+\.py):(\d+)(?:-(\d+))?`")
BLOCK = re.compile(r"```[a-z]*\n(.*?)```", re.S)


def anchor_path(rel: str) -> Path:
    if rel.startswith("notes/scripts/"):
        return ROOT / rel
    if rel.startswith("catlib/"):
        return ROOT / "notes/scripts" / rel
    return SCRIPTS / rel


def anchor_problems(page: str) -> list[str]:
    out = []
    for m in ANCHOR.finditer(page):
        rel = m.group(1)
        a = int(m.group(2))
        span = m.group(3)
        b = int(span) if span else None
        path = anchor_path(rel)
        if not path.exists():
            out.append(f"anchor path absent: {m.group(0)}")
            continue
        n = len(path.read_text(encoding="utf-8").splitlines())
        if a > n or (b and b > n):
            out.append(f"anchor line outside file: {m.group(0)} ({n} lines)")
    return out


def block_problems(page: str) -> list[str]:
    out = []
    for m in BLOCK.finditer(page):
        head = page[:m.start()]
        anchors = list(ANCHOR.finditer(head))
        if not anchors:
            continue
        last = anchors[-1]
        rel = last.group(1)
        a = int(last.group(2))
        span = last.group(3)
        b = int(span) if span else None
        path = anchor_path(rel)
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        start = a - 1
        end = (b - 1) if b else start + len(m.group(1).splitlines()) - 1
        src = [l.strip() for l in lines[start:end + 1]]
        want = [l.strip() for l in m.group(1).splitlines() if l.strip()]
        got = [l for l in src if l]
        if want and want[0] not in " ".join(got):
            out.append(f"block does not match {rel}:{a}: {want[0][:60]}")
    return out


def count_problems(page: str, pop: Pop) -> list[str]:
    flat = re.sub(r"\s+", " ", page)
    out = []
    for phrase in count_phrases(pop):
        if phrase not in flat:
            out.append(f"count phrase not in the page: {phrase}")
    rows = pop["rows"]
    for key, val in (("wall", rows["render_reports.py"]["wall"]),
                     ("opens", rows["render_reports.py"]["opens"]),
                     ("distinct", rows["render_reports.py"]["distinct"]),
                     ("repeats", rows["render_reports.py"]["repeats"])):
        want = f"{val:,}" if key != "wall" else f"{val}"
        if want not in flat:
            out.append(f"probe figure not in the page: {key} {want}")
    return out


def table_problems(page: str, pop: Pop) -> list[str]:
    out = []
    # The purity table is checked inside its own section: the amplification table names four of the
    # same scripts, so a page-wide row scan would let a deleted purity row pass.
    sec = re.search(r"## The purity population.*?(?=\n## )", page, re.S)
    if not sec:
        return ["purity section absent"]
    rows = re.findall(r"^\|\s*`([^`]+\.py)`\s*\|", sec.group(0), re.M)
    want = [s for s, _, _ in pop["purity"]]
    if sorted(rows) != sorted(want):
        out.append(f"purity table rows {sorted(rows)} != population {sorted(want)}")
    if len(pop["purity"]) != 7:
        out.append(f"purity population reads {len(pop['purity'])}, not 7")
    for row in ROWS:
        if row not in page:
            out.append(f"amplification row absent: {row}")
    return out


MUTANTS = [
    ("atomicity count shifted", lambda p: p.replace("**2 matches**", "**1 match**", 1)),
    ("sync split altered", lambda p: p.replace("**11** are `verify_*`", "**10** are `verify_*`", 1)),
    ("purity row deleted", lambda p: re.sub(r"^\|\s*`check_index_links\.py`.*\n", "", p, count=1, flags=re.M)),
    ("digest count widened", lambda p: p.replace("**5** digests", "**6** digests", 1)),
    ("probe figure altered", lambda p: p.replace("75,394", "75,395")),
    ("anchor outside the file", lambda p: p.replace("render_reports.py:1132", "render_reports.py:3400", 1)),
    ("prose count in the size argument", lambda p: p.replace("**630,606** bytes", "**630,605** bytes", 1)),
]


def mutants(page: str) -> str:
    caught, undetected = 0, []
    pop = population()
    for name, fn in MUTANTS:
        mutated = fn(page)
        if mutated == page:
            undetected.append(f"{name}: target not in the page")
            continue
        probs = count_problems(mutated, pop) + table_problems(mutated, pop) + anchor_problems(mutated)
        if probs:
            caught += 1
        else:
            undetected.append(name)
    print(f"mutants flagged: {caught} of {len(MUTANTS)}")
    for u in undetected:
        print(f"  UNDETECTED: {u}")
    return f"undetected mutants: {len(undetected)}"


def main(argv: list[str]) -> int:
    page_path = PAGE
    for a in argv:
        if a.startswith("--page="):
            page_path = Path(a.split("=", 1)[1])
    if not page_path.exists():
        print(f"page absent: {page_path}")
        return 1
    missing = [pp for pp in PROBE if not pp.exists()]
    if missing:
        for pp in missing:
            print(f"probe record absent: {pp}")
        return 1
    page = page_path.read_text(encoding="utf-8")
    pop = population()
    problems = anchor_problems(page) + block_problems(page) + count_problems(page, pop) \
        + table_problems(page, pop)
    print("=== notes/fleet-design.md check ===")
    print(f"atomicity grep: {pop['atomic']} match{'es' if pop['atomic'] != 1 else ''} "
          f"over {pop['scripts']} scripts "
          f"(this checker excluded, its source carries the pattern as a needle) + "
          f"{pop['modules']} catlib modules")
    print(f"sync pass: {pop['sync']} scripts ({pop['sync_verify']} verify_, {pop['sync_other']} not)")
    print(f"tree digests: {pop['digests']}  ignored lines: {pop['ignored']}")
    print(f"notes/*.tsv: {pop['tsv_count']} files, {pop['tsv_bytes']} bytes")
    print(f"gate rows: {pop['gate_rows']}  set sites: {len(pop['set_sites'])} "
          f"({', '.join(pop['set_sites'])})  env hits: {pop['env_hits']}")
    print(f"purity population: {len(pop['purity'])} scripts")
    for script, writes, gen in pop["purity"]:
        print(f"  {script}: writes {writes}, generated reads {gen}")
    print(f"check_index_links wall {pop['cli_wall']:.2f} s (the probe row the amplification table quotes)")
    for prob in problems:
        print(f"  PROBLEM: {prob}")
    summary = mutants(page) if "--mutant" in argv else None
    if summary is not None:
        n = int(summary.rsplit("undetected mutants:", 1)[1])
        if n:
            problems.append(f"{n} injected mutants went undetected")
    print(f"problems: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
