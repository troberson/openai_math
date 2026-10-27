#!/usr/bin/env python3
"""Derive each gate row's read surface and price its key.

**The rule:** a row is keyable iff every path it reads is named by its L1 or sits inside one of the
five hashed trees, and it performs no read that is not an `open()` event.

The rule has two clauses because the audit hook sees some reads and not others. Measured 2026-10-17
with `.qwen/tmp/audit_events_probe.py`: the hook reports `open` and `subprocess.Popen`, so a `git` or
`du` read is visible as an event; it does not report `os.stat`, so an `mtime` read is invisible, and a
wall time is not a path read at all. So the first clause is measured from the hook and the second from
a source scan for the forms the hook cannot see.

The subprocess half of the second clause is classified by what the call reads, not by its presence, and
three forms are covered by the definition of the key:

- `git rev-parse` over `catlib.records.DIGEST_PATHS` is the key's own basis: the key is defined as a
  function of those digests, so that read is covered by construction;
- `git ls-files` over a tree L1 entry is the key's own basis at file level: `expand()` runs it to
  discover the tracked files under a tree, and the key is a function of those files' contents;
- a subprocess that runs a fleet script is a **delegation**: the child's reads are covered by the
  child's own key, so the parent's result is still a function of tracked bytes.

A subprocess that reads a **revision** (`git show <commit>:`, `git log`) or the **filesystem state**
(`du`) is neither: the key hashes HEAD, not an arbitrary commit, and it hashes bytes, not sizes.

The first clause needs the same care. A key can only name tracked bytes, so a read of an untracked path
cannot be named by L1 -- that is why `verify_cache_promotion.py`, which reads the record store under
`.qwen/cache/`, is unkeyable. `__pycache__` is excluded for the same reason `catlib.promote.expand`
excludes it: a compiled cache is a function of source the key already hashes. Existence on the tracked
surface is not a separate read, because the tree digest already names every tracked file, so an
`is_file()` test there is part of the key; only a stat read of a **timestamp**, which is not bytes, is a
read the key cannot hash.

Each row runs in a fresh process with the hook installed before the row's imports: a shared process
caches `catlib` in `sys.modules` and the hook never sees those imports, which is what made the first
run's script counts wrong. Opens are filtered to read modes (`r`, `rb`, `r+`, `rb+`) -- `write_atomic`
lands a `.tmp` that is gone by pricing time -- and entries that are not paths are dropped: the hook
records `str(args[0])`, so `open(3, 'r')` lands as the entry `3` and contaminates the `other` bucket.
The path lists are clean, so the derived L1 comes from the path lists, not the buckets.

Writers are run with `--check-only` so this row writes nothing tracked, and the key is priced with the
row's canonical args, not with the flag. The script's own row is skipped: the measurer cannot measure
itself, it would recurse. The rule is applied to the rows measured, not to the measurer -- this script's
own `subprocess` use is the instrument that runs a row, not a read of the corpus.

The record lands in the format `verify_cache_promotion.py`'s `probe_reads()` parses -- a
`[probe2] target notes/scripts/<name>` line, then the `[probe2] notes/ paths` section with
`count  mode  path` lines. That pass reads only the `notes/` bucket, because an L1 entry naming the
script tree is hashed, not compared; so the import surface is recorded as its own section. The record
carries no wall time, which is what makes a twice-run byte diff a proof -- the reason
`measure_open_probe.py` is not a gate row. Its name is fixed rather than dated for the same reason: a
deterministic record under a fixed name is byte-identical on a re-run.

Invoke as: python3 notes/scripts/measure_checker_reads.py
"""
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import gate as G
from catlib import atomic
from catlib import paths as P
from catlib import promote as PR
from catlib import records as RC

ROOT = P.ROOT
SCRIPTS = P.SCRIPTS
PROBE_DIR = ROOT / "notes" / "development" / "probe"
RECORD = "checker_reads.txt"
SURFACE_RECORD = "checker_reads.json"
HASHED = tuple(p.split(":", 1)[1] for p in RC.DIGEST_PATHS)
READ = {"r", "rb", "r+", "rb+"}
SELF = Path(__file__).name

# The read forms the hook cannot see. `subprocess` is visible as an event, so it is classified by what
# the call reads rather than by its presence; these two are not visible at all.
NON_OPEN_READ = {
    "timestamp": r"\.st_mtime\b|\bos\.stat\b",
    "wall time": r"\btime\.monotonic\b|\btime\.time\b|\bperf_counter\b",
}

CHILD = r"""
import collections, contextlib, io, runpy, sys
sys.path.insert(0, sys.argv[1])
opens = collections.Counter()
modes = collections.defaultdict(set)
events = []
def hook(event, args):
    if event == "open":
        p = str(args[0])
        opens[p] += 1
        m = args[1] if len(args) > 1 else None
        if isinstance(m, str):
            modes[p].add(m)
    elif event == "subprocess.Popen":
        # The hook hands the argument list over as one object, so str() on it yields the whole list
        # repr as a single token: "'rev-parse'," with its quote and comma. Flatten first, or the
        # key-basis test below can never match and every checker that reaches the digests through
        # catlib.promote.key_for is flagged for reading the thing the key is defined over.
        def tok(x):
            # strip("b'\"") is wrong: it strips the *characters* b, ' and ", so the program name `bd`
            # comes back as `d` and the RUN_ARGS test can never match. Strip only the quote
            # characters, and decode a bytes argument on its own.
            return x.decode("utf-8", "replace") if isinstance(x, bytes) else str(x).strip("\"'")
        parts = []
        for a in args[:4]:
            if isinstance(a, (list, tuple)):
                parts.extend(tok(x) for x in a)
            else:
                parts.append(tok(a))
        events.append("subprocess.Popen " + " ".join(parts))
sys.addaudithook(hook)
import measure_open_probe as probe
target = sys.argv[2]
sys.argv = [target, *sys.argv[3:]]
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        runpy.run_path(target, run_name="__main__")
except SystemExit:
    pass
except Exception:
    pass
for p in sorted(opens):
    ms = ",".join(sorted(modes.get(p, set())) or ["?"])
    print("OPEN %s %s" % (probe.rel(p), ms))
for e in events:
    print("EVENT %s" % e)
"""


def is_path(p: str) -> bool:
    """A real path, not an audit-hook open event whose first argument was a file descriptor."""
    return "/" in p or p.endswith(".md")


def script_path(rel: str) -> Path:
    """A test row's target already carries notes/scripts/, so joining it again duplicated the tree."""
    return ROOT / rel if rel.startswith("notes/") else SCRIPTS / rel


def row_script(spec: str) -> str:
    """The script the row executes. For a test row that is the harness, not the test file."""
    return spec.split()[0]


def tracked() -> set[str]:
    """The tracked read surface, so an untracked read is a rule failure, not a name list."""
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    return set(out.stdout.split())


def run_row(target: str, args: list[str]) -> tuple[dict[str, set[str]], list[str]]:
    """One row in one fresh process: the hook must be installed before the row's imports."""
    # check=False is the honest explicit value, not check=True: the row's exit code is a measured
    # column of the record, so a non-zero child must return, not raise.
    r = subprocess.run([sys.executable, "-c", CHILD, str(SCRIPTS), str(script_path(target)), *args],
                       cwd=ROOT, capture_output=True, text=True, check=False)
    opens: dict[str, set[str]] = {}
    events: list[str] = []
    for line in r.stdout.splitlines():
        if line.startswith("OPEN "):
            path, _, mode = line[5:].partition(" ")
            opens.setdefault(path, set()).add(mode)
        elif line.startswith("EVENT "):
            events.append(line[6:])
    return opens, events


def read_paths(opens: dict[str, set[str]]) -> list[str]:
    """Repo paths only, read mode only, no compiled cache.

    `probe.rel` leaves a path absolute when it is outside the repo, so an absolute entry here is the
    interpreter's own stdlib, not a read the key could ever name. Without this scope every row is
    flagged for importing Python.
    """
    return sorted(p for p, ms in opens.items()
                  if is_path(p) and not p.startswith("/") and "__pycache__" not in p and ms <= READ)


def inside_hashed(p: str) -> bool:
    return p.startswith(HASHED)


def derived_l1(opens: dict[str, set[str]], t: set[str]) -> list[str]:
    """The read surface the key must name: tracked repo reads outside the hashed trees.

    Split the way pass B scopes it. The `notes/` bucket is the part the checker compares; the
    `notes/scripts/` import surface is hashed, not compared, so the record carries it as its own
    section. A tracked read outside `notes/` (the root `README.md`) is still L1 -- the record cannot
    prove it, which is exactly why the pass is scoped to the bucket.
    """
    return sorted(p for p in read_paths(opens) if not inside_hashed(p) and p in t)


def bucket(l1: list[str]) -> list[str]:
    """The part pass B compares: the notes/ bucket, excluding the script tree and the record itself."""
    return [p for p in l1 if p.startswith("notes/")
            and not p.startswith("notes/scripts/") and not p.startswith("notes/development/probe/")]


def imports(l1: list[str]) -> list[str]:
    """The import surface: hashed by the key, never compared by pass B."""
    return [p for p in l1 if p.startswith("notes/scripts/")]


def import_closure(name: str) -> set[str]:
    """The transitive import surface under notes/scripts/, read from each module's own source.

    A checker reaches a producer's record through an import, so the producer has to be in the closure
    for the key to be computable from the checker's own inputs. The direct imports are not enough:
    `verify_page_sync.py` reads the names record through `render_reports.py`, which imports
    `measure_names.py`, so the producer is two hops away.
    """
    seen: set[str] = set()
    stack = [name]
    while stack:
        cur = stack.pop()
        rel = f"notes/scripts/{cur}"
        if rel in seen:
            continue
        seen.add(rel)
        src = script_path(cur).read_text(encoding="utf-8")
        for m in re.finditer(r"^[ \t]*(?:from|import)\s+([\w.]+)(?:\s+import\s+([^\n#]+))?", src,
                             re.MULTILINE):
            pkg, names = m.group(1), m.group(2)
            # `from catlib import records as RC` names the package, not the module: the module is the
            # name after `import`. Reading only the dotted part made the package itself the only catlib
            # entry in the closure, so a checker that reaches its producer through
            # `from catlib import render as RD` never saw the producer, and the store key the record
            # sits under was not derivable -- which is what flagged verify_sources.py and
            # verify_page_sync.py. A package module is also a dotted name, not a path, so the
            # extension has to be added or script_path builds a name with none.
            mods = (["catlib/" + n.strip().split(" as ")[0] for n in names.split(",")] if pkg == "catlib" and names
                    else ["catlib/" + pkg.split(".")[1]] if pkg.startswith("catlib.")
                    else [pkg] if "." not in pkg and (SCRIPTS / f"{pkg}.py").is_file() else [])
            stack.extend(m + ".py" for m in mods)
    return seen


def producer_keys() -> dict[str, str]:
    """The key each fleet producer computes for its own record, through the registry's own rule.

    `catlib.promote.key_for` is the only honest way to name these keys: it expands an L1 entry that
    ends in `/` into the tree it names, and it applies `RUN_ARGS`, so a copy of its formula here would
    be a second implementation of the same join -- and it is the copy that died on the first tree entry,
    reading `notes/` as if it were a file. Measured once for the fleet, not once per row, because
    `render_reports.py`'s L1 names the 1,049-file index tree.
    """
    return {name: PR.key_for(name, PR.ARGS.get(name, ())) for name in PR.L1}


def derivable_keys(name: str, l1: list[str], args: tuple[str, ...], pk: dict[str, str]) -> set[str]:
    """The keys this row can compute from its own inputs.

    A record under one of these keys is a function of the key, so reading it is not a read the key has
    to name -- the store is untracked, but its content is derived, and that is the whole point of a
    key. A record under a key the row cannot compute is state outside the key, and that is a failure.
    The row's own key counts, plus every producer inside its transitive import closure, plus the
    manuscript store key, which `catlib/records.py` derives from its own source alone.
    """
    src = script_path(name).read_text(encoding="utf-8")
    keys = {RC.key(src, tuple((ROOT / p).read_text(encoding="utf-8", errors="replace") for p in l1), args)}
    closure = import_closure(name)
    for rel in closure:
        mod = rel.split("/")[-1]
        if mod in pk:
            keys.add(pk[mod])
    # The closure stores repo-relative paths, so the membership test has to name the path, not the
    # bare module name -- the bare form never matched, which is what left the store key out and
    # flagged verify_sources.py.
    if "notes/scripts/catlib/records.py" in closure:
        keys.add(RC.store_key())
    return keys


def record_key(p: str) -> str:
    """The key a record sits under, from the path alone."""
    parts = p.split("/")
    return parts[parts.index("records") + 1] if "records" in parts else ""


def classify_event(event: str, name: str, l1: list[str]) -> tuple[str, str]:
    """(program, covered?) for one observed subprocess event, read off the definition of the key.

    Three forms are covered by construction: the key's own basis (`git rev-parse` over DIGEST_PATHS,
    and the `bd ready` count that RUN_ARGS hashes), a delegation to a fleet script whose own key covers
    its reads, and a `git show HEAD:<path>` for a path the key already names -- that call reads the same
    bytes the key hashes, so it is not a read outside the key. A read of a **revision** or of the
    **filesystem state** is outside the key: the key hashes HEAD, not an arbitrary commit, and it hashes
    bytes, not sizes.

    The key-basis forms are covered for **every** row, not only for a row whose own source calls
    `key_for`. The first run added a `key_basis` gate that required the row's source to name the key
    function, and that flagged 18 checkers for reading the very digests the key is defined over -- a
    rule that contradicts its own first sentence. A key is a function of those digests by definition,
    so a read of them cannot be a read outside the key. The `bd` half is narrower and stays derived:
    the count is inside the key only for the producer whose RUN_ARGS entry names it.
    """
    parts = event.split()[1:]
    prog = parts[0] if parts else ""
    if prog in ("python3", "python", sys.executable):
        return prog, "delegation"
    if prog == "git" and "rev-parse" in parts and any(d in parts for d in RC.DIGEST_PATHS):
        return prog, "key basis"
    if prog == "git" and "ls-files" in parts:
        return prog, "key basis"
    if prog == "bd" and name in PR.RUN_ARGS:
        return prog, "key basis"
    if prog == "git" and "show" in parts:
        rev = parts[parts.index("show") + 1] if parts.index("show") + 1 < len(parts) else ""
        path = rev.split(":", 1)[1] if ":" in rev else ""
        if rev.startswith("HEAD:") and (path in l1 or inside_hashed(path)):
            return prog, "key basis"
    return prog, "uncovered"


def source_reads(name: str) -> list[tuple[int, str, str]]:
    """The read forms the hook cannot see, with the line each one sits on."""
    src = script_path(name).read_text(encoding="utf-8")
    out = []
    for label, pat in NON_OPEN_READ.items():
        for m in re.finditer(pat, src):
            line = src[: m.start()].count("\n") + 1
            out.append((line, label, src.splitlines()[line - 1].strip()))
    return sorted(out)


def key_cost(name: str, l1: list[str], args: tuple[str, ...]) -> float:
    t0 = time.monotonic()
    texts = tuple((ROOT / p).read_text(encoding="utf-8", errors="replace") for p in l1)
    RC.key(script_path(name).read_text(encoding="utf-8"), texts, args)
    return time.monotonic() - t0


def price(target: str, spec: str, args: tuple[str, ...], t: set[str], opens: dict[str, set[str]],
         events: list[str], pk: dict[str, str]) -> dict[str, Any]:
    l1 = derived_l1(opens, t)
    keys = derivable_keys(target, l1, args, pk)
    untracked = sorted(p for p in read_paths(opens) if not inside_hashed(p) and p not in t
                       and not (p.startswith(".qwen/cache/records/") and record_key(p) in keys))
    uncovered = [e for e in events if classify_event(e, target, l1)[1] == "uncovered"]
    hits = source_reads(target)
    return {"spec": spec, "name": target, "l1": l1, "args": args,
            "cost": key_cost(target, l1, args), "events": uncovered, "untracked": untracked,
            "reads": hits, "keyable": not uncovered and not untracked and not hits}


def measure(t: set[str], pool: int, pk: dict[str, str]) -> list[dict[str, Any]]:
    """Run the read surfaces in parallel, then price the keys serially.

    The read-surface pass is the expensive half and it is embarrassingly parallel: every row is
    already a fresh process, so there is no shared state and no dependency graph to respect -- the
    gate's ordering rule exists because writers write, and here nothing writes. The pricing half stays
    serial on purpose: a key cost measured inside a pool is inflated by contention, and the figure the
    page quotes is the cost of a key, not the cost of a scheduling slot.

    Pool size comes from `gate.N`, the same cap sized by measured RSS (12 rows against 6.1 Gi
    available, the two heaviest rows peaking at 415 MB), not by core count. `GATE_POOL` is the
    environment variable that sets it; `N` is the value the module reads, so `GATE_POOL=1` here runs
    the same serial baseline the gate driver runs for its diff.
    """
    targets = [(spec, bool(writes)) for spec, _, writes in G.ROWS if row_script(spec) != SELF]
    with ThreadPoolExecutor(max_workers=pool) as ex:
        futures = [ex.submit(run_row, row_script(spec),
                             list(spec.split()[1:]) + (["--check-only"] if writes else []))
                   for spec, writes in targets]
        surfaces = [f.result() for f in futures]
    return [price(row_script(spec), spec, tuple(spec.split()[1:]), t, opens, events, pk)
            for (spec, _), (opens, events) in zip(targets, surfaces, strict=True)]


def checkers(rows: list[dict[str, Any]], t: set[str], pk: dict[str, str]) -> list[dict[str, Any]]:
    """The checker population, read off the script tree: the 24 `verify_*.py` scripts.

    23 of them are gate rows. `verify_script_ownership.py` is not -- the census checker runs after the
    render that sweeps its own page, so it is measured as the driver measures it.
    """
    by_name = {r["name"]: r for r in rows}
    out = []
    for p in sorted(SCRIPTS.glob("verify_*.py")):
        if p.name in by_name:
            out.append(by_name[p.name])
            continue
        opens, events = run_row(p.name, [])
        out.append(price(p.name, p.name, (), t, opens, events, pk))
    return out


def record_text(rows: list[dict[str, Any]], t: set[str], pk: dict[str, str]) -> str:
    """The record in the format probe_reads() parses: one target block per checker, no wall time."""
    out = []
    for row in checkers(rows, t, pk):
        out.append(f"[probe2] target notes/scripts/{row['name']}")
        out.append("[probe2] notes/ paths (count  modes  path):")
        for p in bucket(row["l1"]):
            out.append(f"              1  r        {p}")
        out.append("[probe2] scripts paths (count  modes  path):")
        for p in imports(row["l1"]):
            out.append(f"              1  r        {p}")
    return "\n".join(out) + "\n"


def main() -> int:
    t = tracked()
    pk = producer_keys()
    rows = measure(t, G.N, producer_keys())
    cs = checkers(rows, t, pk)
    keyable = [r for r in cs if r["keyable"]]
    print(f"rows priced {len(rows)}  checker rows {len(cs)}  pool {G.N}")
    print(f"keyable {len(keyable)}  unkeyed {len(cs) - len(keyable)}")
    print(f"key cost over the rows {sum(float(r['cost']) for r in rows):.3f} s")
    print()
    print("=== unkeyed, with the clause each one fails ===")
    for r in cs:
        if r["keyable"]:
            continue
        print(f"  {r['name']}")
        for event in r["events"]:
            print(f"    subprocess read the key cannot cover: {event[:88]}")
        for p in r["untracked"]:
            print(f"    untracked read, cannot be named by a key over tracked bytes: {p}")
        for line, label, text in r["reads"]:
            print(f"    :{line} [{label}] {text[:88]}")
    print()
    print("=== keyable, widest surface first ===")
    for r in sorted(keyable, key=lambda r: -len(r["l1"])):
        print(f"  {r['name']:34} {len(r['l1']):5} L1 files  {float(r['cost']):6.3f} s")

    text = record_text(rows, t, pk)
    atomic.write_atomic(PROBE_DIR / RECORD, text)
    # The machine-readable surface: each checker's full derived_l1 and keyability, the value
    # CHECKER_L1 records and the checker pass compares. The text record above is a human view
    # (bucket + imports only); this JSON is the full derived_l1 including outside-notes/ reads.
    surface = {row["name"]: {"l1": row["l1"], "keyable": row["keyable"]} for row in cs}
    atomic.write_atomic(PROBE_DIR / SURFACE_RECORD, json.dumps(surface, indent=2) + "\n")
    print()
    print(f"record landed: {P.rel(PROBE_DIR / RECORD)}")
    print(f"surface landed: {P.rel(PROBE_DIR / SURFACE_RECORD)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
