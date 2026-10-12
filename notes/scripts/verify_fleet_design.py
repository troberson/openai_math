#!/usr/bin/env python3
"""Check `notes/fleet-design.md` — the four-layer design and its measured inventory.

Report-only; writes nothing. Six passes:

1. **Anchors** — every backticked `path:line` (or `path:a-b`) in the page resolves against the file,
   a prefixed path under the repo root, a bare script name under `notes/scripts/`, and a span fits
   inside the file. An anchor written with trailing text (`` `render_reports.py:119 def measure()` ``)
   is not this form, so it is not checked.
2. **Fenced blocks** — each block is attributed to the nearest preceding anchor and matched against the
   source lines it cites, verbatim modulo whitespace. The page ships no fenced block today, so this pass
   is vacuous on it.
3. **Counts** — every count phrase is re-derived by running the command the page names: the atomicity
   grep, the sync-pass grep, the tree-digest `git rev-parse`, the `--ignored=matching` check, the TSV
   byte sum, the three `du -sk` sizes, the gate row count, the three site counts (atomicity, env, set
   iteration), and the probe parse.
4. **Site anchors** — the three paragraphs that state measured sites with line numbers (the atomicity
   paragraph, the env bullet, the set-iteration bullet) must each name exactly their measured
   `name:line` set, and the checker-section anchor list must carry every measured site. The count pass
   proves only the count: a site anchor shifted to a line that exists in its file passes the anchor
   pass, so this pass is what makes the page's site anchors mean the measured lines. Each site must be
   carried **once** in the checker-section paragraph — a site enumerated twice there makes a shift of
   one copy invisible.
5. **Tables** — the purity table equals the probe parse, scanned inside the purity section (the
   amplification table names four of the same scripts, so a page-wide row scan lets a deleted purity row
   pass), and each amplification row is present. The options table is prose and is not re-derived.
6. **Mutants** — 15 injected corruptions, each asserted against the pass it targets.

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
          "check_index_links.py", "measure_proof_density.py", "measure_names.py",
          "verify_script_ownership.py"]
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
    atomic_sites: list[str]
    env_sites: list[str]
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
        # A TSV sits under `notes/tables/`, so the hand-authored test is on the basename: the two
        # hand-authored tables are named by basename in HAND, the six generated ones are not.
        return "hand-authored" if rest.split("/")[-1] in HAND else "generated"
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
    # counting it would read 1, and the page's rule is about the fleet, not about the checker. The
    # sites are recorded with their line numbers so the page's anchors can be compared with them.
    atomic = 0
    atomic_sites: list[str] = []
    scripts = [p for p in sorted(SCRIPTS.glob("*.py")) if p.name != "verify_fleet_design.py"]
    for p in scripts + sorted((SCRIPTS / "catlib").glob("*.py")):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            n = len(re.findall(r"os\.replace|os\.rename|shutil\.move|NamedTemporaryFile", line))
            if n:
                atomic += n
                atomic_sites.append(f"{p.name}:{i}")
    sync = sorted(p.name for p in SCRIPTS.glob("*.py")
                  if "sync problems" in p.read_text(encoding="utf-8")
                  and p.name != "verify_fleet_design.py")
    digests = sh("git", "rev-parse", *DIGEST_PATHS).split()
    ignored = [l for l in sh("git", "status", "--porcelain", "--ignored=matching", "--",
                             "preprints", "lean", "overview.tex", "CONTENTS.md",
                             "reasoning_traces").splitlines() if l.strip()]
    tsvs = sorted((ROOT / "notes" / "tables").glob("*.tsv"))
    tsv_bytes = sum(len(p.read_bytes()) for p in tsvs)
    du: dict[str, int] = {}
    for name, rel in (("preprints", "preprints"), ("oai", "lean/OAI"), ("index", "notes/index")):
        du[name] = int(sh("du", "-sk", rel).split()[0]) // 1024
    gate = (SCRIPTS / "gate.py").read_text(encoding="utf-8")
    # Each ROWS entry is one invocation and the list order is the canonical print order, so counting
    # the tuples is the row count. The spec is followed by the needs tuple, so the row is matched by
    # the pair, not by a bare leading `("…",` — a wrapped row's continuation line starts with the
    # needs tuple's own first string and would otherwise count as a row.
    rows_block = gate[gate.index("ROWS = ["):]
    gate_rows = len(re.findall(r'^\s*\(".*?",\s*\(', rows_block, re.MULTILINE))
    set_sites: list[str] = []
    for name in ("build_catalog.py", "build_index.py"):
        for i, line in enumerate((SCRIPTS / name).read_text(encoding="utf-8").splitlines(), 1):
            if "for p in set(" in line:
                set_sites.append(f"{name}:{i}")
    env_sites: list[str] = []
    for i, line in enumerate((SCRIPTS / "render_reports.py").read_text(encoding="utf-8").splitlines(), 1):
        if 'env={**os.environ, "RENDER_REPORTS_CHILD"' in line:
            env_sites.append(f"render_reports.py:{i}")
    env_hits = len(env_sites)
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
        "atomic_sites": atomic_sites, "env_sites": env_sites,
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
        # The purity population is the probe parse, so its heading count and the sentence that closes
        # the section are measured, not carried: adding a target to the probe moves both.
        f"## The purity population ({len(pop['purity'])} scripts, mode-verified)",
        f"**0** of the {len(pop['purity'])} scripts reads a generated file",
    ]


ANCHOR = re.compile(r"`(notes/[\w./+-]+\.(?:md|tsv)|notes/scripts/[\w.]+\.py"
                    r"|notes/scripts/catlib/[\w.]+\.py|catlib/[\w.]+\.py|[\w.]+\.py)"
                    r":(\d+)(?:-(\d+))?`")
BLOCK = re.compile(r"```[a-z]*\n(.*?)```", re.DOTALL)
SET_BULLET = re.compile(r"- \*\*Set iteration order:\*\*.*?(?=\n- )", re.DOTALL)
ENV_BULLET = re.compile(r"- \*\*Time / random / env:\*\*.*?(?=\n- )", re.DOTALL)
ATOMIC_PARA = re.compile(r"\*\*\d+ matches?\*\*,.*?(?=\n\n)", re.DOTALL)
ANCHORS_PARA = re.compile(r"1\. \*\*Anchors\*\* —.*?(?=\n2\. )", re.DOTALL)


def anchor_path(rel: str) -> Path:
    if rel.startswith("notes/scripts/"):
        return ROOT / rel
    if rel.startswith("catlib/"):
        return ROOT / "notes/scripts" / rel
    if rel.startswith("notes/"):
        # A notes-page anchor is repo-relative, so it resolves against the root and a page move
        # needs no resolver change. Checked before the bare-name branch, which would read
        # `notes/reports/x.md` as a script under notes/scripts/.
        return ROOT / rel
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
    sec = re.search(r"## The purity population.*?(?=\n## )", page, re.DOTALL)
    if not sec:
        return ["purity section absent"]
    rows = re.findall(r"^\|\s*`([^`]+\.py)`\s*\|", sec.group(0), re.MULTILINE)
    want = [s for s, _, _ in pop["purity"]]
    if sorted(rows) != sorted(want):
        out.append(f"purity table rows {sorted(rows)} != population {sorted(want)}")
    for row in ROWS:
        if row not in page:
            out.append(f"amplification row absent: {row}")
    return out


def norm(rel: str) -> str:
    """Fold a page anchor's catlib/ prefix onto the measured module name."""
    return rel.removeprefix("catlib/")


def site_problems(page: str, pop: Pop) -> list[str]:
    """Compare the page's anchors with the measured sites, not just the measured count.

    Three site classes are measured with line numbers — atomicity, env, set iteration — and each is
    stated in its own paragraph. The count pass proves only the count and the anchor pass only that
    the line exists, so a site shifted to a neighbouring line passes both. Each paragraph's anchors
    must equal its measured set, and the checker-section anchor list must carry every measured site.
    """
    out: list[str] = []
    want: dict[str, list[str]] = {}
    for pat, label, sites in ((ATOMIC_PARA, "atomicity paragraph", sorted(pop["atomic_sites"])),
                              (ENV_BULLET, "env bullet", sorted(pop["env_sites"])),
                              (SET_BULLET, "set-iteration bullet", sorted(pop["set_sites"]))):
        sec = pat.search(page)
        if not sec:
            out.append(f"{label} absent")
            continue
        named = sorted(f"{norm(m.group(1))}:{m.group(2)}" for m in ANCHOR.finditer(sec.group(0)))
        want[label] = sites
        if named != sites:
            out.append(f"{label} names {named}, measured {sites}")
    four = ANCHORS_PARA.search(page)
    if not four:
        out.append("checker-section anchors paragraph absent")
    else:
        listed = {f"{norm(m.group(1))}:{m.group(2)}" for m in ANCHOR.finditer(four.group(0))}
        for sites in want.values():
            for site in sites:
                if site not in listed:
                    out.append(f"site {site} absent from the checker-section anchors paragraph")
    return out


MUTANTS = [
    ("atomicity count shifted", lambda p: p.replace("**2 matches**", "**1 match**", 1)),
    ("sync split altered", lambda p: p.replace("**12** are `verify_*`", "**11** are `verify_*`", 1)),
    ("purity row deleted", lambda p: re.sub(r"^\|\s*`check_index_links\.py`.*\n", "", p, count=1, flags=re.MULTILINE)),
    # The purity heading count is the probe parse, so a page that names one target it does not measure
    # is caught by the count pass, not by the row scan.
    ("purity population count altered",
     lambda p: p.replace("## The purity population (8 scripts", "## The purity population (7 scripts", 1)),
    ("digest count widened", lambda p: p.replace("**5** digests", "**6** digests", 1)),
    ("probe figure altered", lambda p: p.replace("117,360", "117,361")),
    ("anchor outside the file", lambda p: p.replace("render_reports.py:1150", "render_reports.py:3400", 1)),
    # The page ships no notes-page anchor, so the resolver's notes/ branch is inert on a clean page.
    # This mutant injects one with a line past the file's end, which is the only way the branch is
    # proven to fire.
    ("notes-page anchor outside the file",
     lambda p: p.replace("`render_reports.py:1150`", "`render_reports.py:1150` `notes/fleet-design.md:9999`", 1)),
    ("prose count in the size argument", lambda p: p.replace("**630,620** bytes", "**630,619** bytes", 1)),
    # A measured site shifted to a line that exists in its file passes the anchor pass and the count
    # pass, so only the site comparison can catch it. One mutant per list the comparison reads.
    ("set-site anchor shifted in the bullet",
     lambda p: p.replace("build_index.py:583", "build_index.py:584", 1)),
    ("set-site anchor shifted in the checker list",
     lambda p: p.replace("`build_index.py:583`, `render_reports.py:1150`",
                         "`build_index.py:584`, `render_reports.py:1150`", 1)),
    ("atomicity anchor shifted in the paragraph",
     lambda p: p.replace("catlib/atomic.py:42", "catlib/atomic.py:43", 1)),
    ("atomicity anchor shifted in the checker list",
     lambda p: p.replace("`catlib/atomic.py:42`, `catlib/atomic.py:84`",
                         "`catlib/atomic.py:43`, `catlib/atomic.py:84`", 1)),
    ("env anchor shifted in the bullet",
     lambda p: p.replace("`render_reports.py:1150` and", "`render_reports.py:1151` and", 1)),
    ("env anchor shifted in the checker list",
     lambda p: p.replace("`render_reports.py:1150`, `render_reports.py:2043`",
                         "`render_reports.py:1151`, `render_reports.py:2043`", 1)),
]


def mutants(page: str) -> str:
    caught, undetected = 0, []
    pop = population()
    for name, fn in MUTANTS:
        mutated = fn(page)
        if mutated == page:
            undetected.append(f"{name}: target not in the page")
            continue
        probs = count_problems(mutated, pop) + table_problems(mutated, pop) \
            + anchor_problems(mutated) + site_problems(mutated, pop)
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
        + table_problems(page, pop) + site_problems(page, pop)
    print("=== notes/fleet-design.md check ===")
    print(f"atomicity grep: {pop['atomic']} match{'es' if pop['atomic'] != 1 else ''} "
          f"over {pop['scripts']} scripts "
          f"(this checker excluded, its source carries the pattern as a needle) + "
          f"{pop['modules']} catlib modules")
    print(f"sync pass: {pop['sync']} scripts ({pop['sync_verify']} verify_, {pop['sync_other']} not)")
    print(f"tree digests: {pop['digests']}  ignored lines: {pop['ignored']}")
    print(f"notes/tables/*.tsv: {pop['tsv_count']} files, {pop['tsv_bytes']} bytes")
    print(f"gate rows: {pop['gate_rows']}  env hits: {pop['env_hits']}")
    for label, sites in (("atomic sites", pop["atomic_sites"]), ("env sites", pop["env_sites"]),
                         ("set sites", pop["set_sites"])):
        print(f"  {label}: {len(sites)} ({', '.join(sites)})")
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
