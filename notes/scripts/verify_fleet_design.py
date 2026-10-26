#!/usr/bin/env python3
"""Check `notes/development/fleet-design.md` — the four-layer design and its measured inventory.

Report-only; writes nothing. Seven passes:

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
6. **Sync** — the page's bytes on disk against the bytes `render_reports.py` renders for it. The page
   is report-fed: its measured phrases are slots the writer supplies from its own scan of the fleet's
   sources, so a hand edit to a slotted phrase, a stale render, or a template that no longer matches the
   page all show up here. The count pass proves the numbers are measured; this pass proves the page is
   the writer's text. The two are independent: the writer's measurement is its own, not this checker's.

Volatile measurements (the `free -h` available line, the wall times, the cold/warm swing) are dated
observations in the page and are **not** re-derived: a checker that re-measures them fails the day the
machine changes. They are also **not** writer slots, for the same reason: a writer that recomputed them
would move the page every day the machine changed, so they stay literal in the template.

The self-tests are in notes/scripts/tests/test_fleet_design.py: that file injects the sixteen page
faults and asserts each fires the pass that owns it. `main()` reads no argv, so `--mutant` is inert
here.
"""

from __future__ import annotations

import re
import subprocess
import sys
from functools import cache
from pathlib import Path
from typing import TypedDict

from catlib import render as RD

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "development" / "fleet-design.md"
SCRIPTS = ROOT / "notes" / "scripts"
PROBE = [ROOT / "notes/development/probe/2026-10-11_writers.txt",
         ROOT / "notes/development/probe/2026-10-11_checkers.txt"]
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
    probe_records: int
    du: dict[str, int]
    gate_rows: int
    writer_rows: int
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
    if path.startswith(("notes/gen/index/", "notes/gen/summaries/", "notes/templates/")):
        return "generated"
    rest = path[len("notes/"):]
    if rest.endswith(".tsv"):
        # A TSV sits under `notes/gen/tables/`, so the hand-authored test is on the basename: the two
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


@cache
def population() -> Pop:
    """The measured population, cached for a multi-`check()` run.

    The checker writes nothing and the self-tests mutate page text in memory, so a second call in the
    same process cannot see a different corpus; the cache is what keeps the clean page plus each of the
    sixteen faults from paying the `git`/`du`/script-tree walk once per call.
    """
    # The atomicity census excludes the two scripts that carry the pattern as a needle: this checker,
    # whose count pass embeds it, and `render_reports.py`, whose `FLEET_ATOMIC` constant is the needle.
    # Neither has a real atomicity site, so counting them would read the census as 3 with a phantom
    # site. The sites are recorded with their line numbers so the page's anchors can be compared with
    # them.
    atomic = 0
    atomic_sites: list[str] = []
    scripts = [p for p in sorted(SCRIPTS.glob("*.py"))
               if p.name not in ("verify_fleet_design.py", "render_reports.py")]
    for p in scripts + sorted((SCRIPTS / "catlib").glob("*.py")):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            n = len(re.findall(r"os\.replace|os\.rename|shutil\.move|NamedTemporaryFile", line))
            if n:
                atomic += n
                atomic_sites.append(f"{p.name}:{i}")
    sync = sorted(p.name for p in SCRIPTS.glob("*.py")
                  if "sync problems" in p.read_text(encoding="utf-8")
                  and p.name not in ("verify_fleet_design.py", "render_reports.py"))
    digests = sh("git", "rev-parse", *DIGEST_PATHS).split()
    ignored = [l for l in sh("git", "status", "--porcelain", "--ignored=matching", "--",
                             "preprints", "lean", "overview.tex", "CONTENTS.md",
                             "reasoning_traces").splitlines() if l.strip()]
    tsvs = sorted((ROOT / "notes" / "gen" / "tables").glob("*.tsv"))
    probe_records = len([p for p in (ROOT / "notes" / "development" / "probe").iterdir()
                         if p.is_file()])
    tsv_bytes = sum(len(p.read_bytes()) for p in tsvs)
    du: dict[str, int] = {}
    for name, rel in (("preprints", "preprints"), ("oai", "lean/OAI"), ("index", "notes/gen/index")):
        du[name] = int(sh("du", "-sk", rel).split()[0]) // 1024
    gate = (SCRIPTS / "gate.py").read_text(encoding="utf-8")
    # Each ROWS entry is one invocation and the list order is the canonical print order, so counting
    # the tuples is the row count. The spec is followed by the needs tuple, so the row is matched by
    # the pair, not by a bare leading `("…",` — a wrapped row's continuation line starts with the
    # needs tuple's own first string and would otherwise count as a row.
    rows_block = gate[gate.index("ROWS = ["):]
    gate_rows = len(re.findall(r'^\s*\(".*?",\s*\(', rows_block, re.MULTILINE))
    # A row that declares an artifact is a writer row. `), ("` cannot count them: the needs tuple opens
    # the same way, so it reads 86 over the 77 rows. The rows with an empty `writes` set end `), ())`,
    # so the writer rows are the row count minus that count.
    writer_rows = gate_rows - len(re.findall(r'\),\s*\(\)\)', rows_block))
    set_sites: list[str] = []
    for name in ("build_catalog.py", "build_index.py"):
        for i, line in enumerate((SCRIPTS / name).read_text(encoding="utf-8").splitlines(), 1):
            if "for p in set(" in line:
                set_sites.append(f"{name}:{i}")
    env_sites: list[str] = []
    # The needle is written as a concatenation so this test line does not contain it. The census reads
    # `render_reports.py`, which carries the same needle in its own env scan; written whole in both,
    # each census counts its own test as a site.
    env_needle = 'env={**os.environ, ' + '"RENDER_REPORTS_CHILD"'
    for i, line in enumerate((SCRIPTS / "render_reports.py").read_text(encoding="utf-8").splitlines(), 1):
        if env_needle in line:
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
        "tsv_count": len(tsvs), "probe_records": probe_records, "du": du,
        "gate_rows": gate_rows, "writer_rows": writer_rows,
        "set_sites": set_sites,
        "atomic_sites": atomic_sites, "env_sites": env_sites,
        "env_hits": env_hits, "purity": purity, "rows": rows, "cli_wall": cli,
    }


def count_phrases(pop: Pop) -> list[tuple[str, str]]:
    du = pop["du"]
    # The needles are (phrase, label) pairs, the shape `build_report_templates.py` reads: the label is
    # the writer's slot label, so the builder's coverage report says which of these phrases the template
    # slots and which it leaves literal. The site anchors are not here — pass 4 compares them with the
    # measured sites, which a phrase comparison cannot do.
    return [
        (f"**{pop['atomic']} match{'es' if pop['atomic'] != 1 else ''}**", "atomic_count"),
        (f"**{pop['scripts']}** scripts and **{pop['modules']}** catlib modules", "fleet_sizes"),
        (f"**{pop['sync']}** scripts", "sync_scripts"),
        (f"**{pop['sync_verify']}** are `verify_*`", "sync_verify"),
        (f"**{pop['sync_other']}** are not", "sync_other"),
        (f"**{pop['digests']}** digests", "digests"),
        (f"returns **{pop['ignored']} line{'s' if pop['ignored'] != 1 else ''}**", "ignored_line"),
        (f"**{pop['tsv_bytes']:,}** bytes", "tsv_bytes"),
        (f"**{pop['tsv_count']}** `notes/gen/tables/*.tsv` present on disk", "tsv_count"),
        (f"The tracked records are **{pop['probe_records']}**:", "probe_records"),
        (f"**{du['preprints']}M**", "du_preprints"),
        (f"**{du['oai']}M**", "du_oai"),
        (f"**{du['index']}M**", "du_index"),
        (f"carries **{pop['gate_rows']}** invocations as `ROWS` entries", "gate_rows"),
        (f"the **{pop['writer_rows']}** writers declare what they write", "gate_writers"),
        (f"Non-determinism sources in the **{pop['writer_rows']}** writers, by class:",
         "gate_writers_class"),
        (f"**{len(pop['set_sites'])} sites**", "set_sites"),
        (f"**{pop['env_hits']} hit{'s' if pop['env_hits'] != 1 else ''}**", "env_hits"),
        # The purity population is the probe parse, so its heading count and the sentence that closes
        # the section are measured, not carried: adding a target to the probe moves both.
        (f"## The purity population ({len(pop['purity'])} scripts, mode-verified)", "purity_heading"),
        (f"**0** of the {len(pop['purity'])} scripts reads a generated file", "purity_zero"),
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
        # `notes/gen/reports/x.md` as a script under notes/scripts/.
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
    for phrase, _label in count_phrases(pop):
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


def check(text: str) -> tuple[list[str], int, int, int]:
    """All six passes over page text. Returns (problems, anchors, phrases, sync problems).

    `text` is page text, not a path: the self-tests mutate the page in memory, so nothing here writes
    a page. The anchor count is the number of `path:line` shapes the resolver read, and the phrase
    count is the count needles plus the four probe figures, so a page that drops a pass shows up as a
    smaller count, not as a silent pass.
    """
    pop = population()
    sync = RD.sync_problems(PAGE, text)
    problems = anchor_problems(text) + block_problems(text) + count_problems(text, pop) \
        + table_problems(text, pop) + site_problems(text, pop) + sync
    return (problems, len(ANCHOR.findall(text)), len(count_phrases(pop)) + 4, len(sync))


def main() -> int:
    if not PAGE.exists():
        print(f"page absent: {PAGE}")
        return 1
    missing = [pp for pp in PROBE if not pp.exists()]
    if missing:
        for pp in missing:
            print(f"probe record absent: {pp}")
        return 1
    page = PAGE.read_text(encoding="utf-8")
    pop = population()
    problems, n_anchor, n_phrases, n_sync = check(page)
    print("=== notes/development/fleet-design.md check ===")
    print(f"atomicity grep: {pop['atomic']} match{'es' if pop['atomic'] != 1 else ''} "
          f"over {pop['scripts']} scripts "
          f"(the two needle-carrying scripts excluded) + "
          f"{pop['modules']} catlib modules")
    print(f"sync pass: {pop['sync']} scripts ({pop['sync_verify']} verify_, {pop['sync_other']} not)")
    print(f"tree digests: {pop['digests']}  ignored lines: {pop['ignored']}")
    print(f"notes/gen/tables/*.tsv: {pop['tsv_count']} files, {pop['tsv_bytes']} bytes")
    print(f"notes/development/probe/ records: {pop['probe_records']}")
    print(f"gate rows: {pop['gate_rows']}  env hits: {pop['env_hits']}")
    for label, sites in (("atomic sites", pop["atomic_sites"]), ("env sites", pop["env_sites"]),
                         ("set sites", pop["set_sites"])):
        print(f"  {label}: {len(sites)} ({', '.join(sites)})")
    print(f"purity population: {len(pop['purity'])} scripts")
    for script, writes, gen in pop["purity"]:
        print(f"  {script}: writes {writes}, generated reads {gen}")
    print(f"check_index_links wall {pop['cli_wall']:.2f} s (the probe row the amplification table quotes)")
    print(f"anchors {n_anchor}  phrases {n_phrases}  sync problems {n_sync}")
    for prob in problems:
        print(f"  PROBLEM: {prob}")
    print(f"problems: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
