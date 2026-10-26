#!/usr/bin/env python3
"""The open-event probe: every open() a script performs, with its mode, recorded to a tracked file.

Usage:
  python3 notes/scripts/measure_open_probe.py --record <name> <target.py> [args...]   # writes notes/development/probe/<name>.txt
  python3 notes/scripts/measure_open_probe.py <target.py> [args...]                   # stdout only

A multi-target record is built by redirecting stdout and appending, which is how the tracked
`notes/development/probe/2026-10-10_writers.txt` and `_checkers.txt` were made. The gate does not run
this script: its record carries a wall time per target, so a run-1/run-2 byte diff of a record is a
timing artifact, not a proof.

Rule: `sys.addaudithook` on the `open` event records the path and the mode string per path, parent
process only. A path is a write only if a recorded mode contains `w`, `a` or `x`. The AST census maps
a name to a call context and does **not** track branches, so a `write_text` that lives only in a
`--mutant` path is reported as a write in every mode — the probe's mode strings are the authority.

The records are what `notes/development/fleet-design.md`'s purity table and amplification table are
measured from, and `verify_fleet_design.py` parses them. The probe's own record write is dropped from
the printed lists: `notes/development/probe/` is the record's destination, not one of the target's
opens.
"""
from __future__ import annotations

import collections
import contextlib
import io
import runpy
import sys
import time
from pathlib import Path

from catlib.atomic import write_atomic
from catlib.paths import ROOT

PROBE_DIR = ROOT / "notes" / "development" / "probe"

READ_MODES = {"r", "rb", "r+", "rb+"}
WRITE_MODES = {"w", "wb", "a", "ab", "x", "xb", "w+", "wb+", "a+", "ab+", "x+", "xb+"}

TOP_PREFIXES = ("preprints/", "lean/", "notes/", "reasoning_traces/", ".git/")
BUCKET_PREFIXES = ("preprints/", "lean/OAI/", "lean/ComparatorChallenges/", "lean/docs/",
                   "notes/gen/index/", "notes/gen/summaries/", "notes/scripts/", "notes/templates/",
                   "notes/", "reasoning_traces/", ".git/", "upstream_history/")

opens: collections.Counter = collections.Counter()
modes: dict[str, set[str]] = collections.defaultdict(set)


def hook(event: str, args: tuple) -> None:
    if event != "open":
        return
    path = str(args[0])
    opens[path] += 1
    mode = args[1] if len(args) > 1 else None
    if isinstance(mode, str):
        modes[path].add(mode)


def rel(path: str) -> str:
    p = Path(path)
    if p.is_absolute():
        try:
            return str(p.relative_to(ROOT))
        except ValueError:
            return str(p)
    return path


def bucket(path: str) -> str:
    r = rel(path)
    if not r.startswith(TOP_PREFIXES):
        return "abs/other" if r.startswith("/") else "other"
    for pref in BUCKET_PREFIXES:
        if r.startswith(pref):
            return pref
    return "top-level"


def io_counters() -> dict[str, int]:
    out: dict[str, int] = {}
    for line in Path("/proc/self/io").read_text(encoding="utf-8").splitlines():
        key, _, val = line.partition(":")
        out[key.strip()] = int(val.strip())
    return out


def block(target: str, args: list[str], wall: float, before: dict[str, int],
         after: dict[str, int]) -> list[str]:
    repeats = {p: c for p, c in opens.items() if c > 1}
    out = [f"[probe2] target {target} {' '.join(args)}",
           (f"[probe2] wall {wall:.2f}  opens {sum(opens.values())}  distinct {len(opens)}  "
           f"repeats {sum(c - 1 for c in repeats.values())}"),
           (f"[probe2] rchar MB {(after.get('rchar', 0) - before.get('rchar', 0)) / 1e6:.1f}  "
           f"read_bytes MB {(after.get('read_bytes', 0) - before.get('read_bytes', 0)) / 1e6:.1f}"),
           "[probe2] buckets:"]
    for b, c in collections.Counter(bucket(p) for p in opens.elements()).most_common():
        out.append(f"          {b:26} {c}")
    out.append("[probe2] notes/ paths (count  modes  path):")
    for p in sorted(opens):
        r = rel(p)
        if r.startswith("notes/") and not r.startswith("notes/scripts/") \
                and not r.startswith("notes/development/probe/"):
            shown = ",".join(sorted(modes.get(p, set())) or ["?"])
            out.append(f"          {opens[p]:5}  {shown:8} {r}")
    out.append("[probe2] write-mode paths outside notes/:")
    for p in sorted(opens):
        ms = modes.get(p, set())
        if ms and not ms <= READ_MODES:
            r = rel(p)
            if not r.startswith("notes/"):
                out.append(f"          {opens[p]:5}  {','.join(sorted(ms))} {r}")
    return out


def main() -> int:
    argv = sys.argv[1:]
    record = None
    check_only = "--check-only" in argv
    argv = [a for a in argv if a != "--check-only"]
    if argv and argv[0] == "--record":
        record = argv[1]
        argv = argv[2:]
    if not argv:
        print("usage: measure_open_probe.py [--record notes/development/probe/<file>.txt] <target.py> "
              "[args...]")
        return 2
    target, rest = argv[0], argv[1:]
    sys.addaudithook(hook)
    before = io_counters()
    t0 = time.monotonic()
    sys.path.insert(0, str(Path(target).resolve().parent))
    sys.argv = [target, *rest]
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            runpy.run_path(target, run_name="__main__")
    except SystemExit as exc:
        buf.write(f"[probe] target exit code: {exc.code}\n")
    wall = time.monotonic() - t0
    after = io_counters()
    lines = block(target, rest, wall, before, after)
    text = buf.getvalue() + "\n".join(lines) + "\n"
    print(text, end="")
    if record is not None and not check_only:
        write_atomic(PROBE_DIR / f"{record}.txt", text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
