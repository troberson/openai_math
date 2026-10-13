#!/usr/bin/env python3
"""Prove the promotion protocol: every tracked artifact's bytes equal the bytes under its key.

Four passes, all read-only, writing nothing to the tracked tree:

**A. Registry shape.** The writer set in `catlib/promote.py`'s `ARTIFACTS`, plus the writer the
protocol deliberately excludes, equals the writers table in `notes/scripts/README.md`; `L1` and
`ARTIFACTS` cover the same writer set; `REPORT_PAGES` equals the registry keys in
`catlib/templates.py`; no writer's L1 names a file it writes (a self-read would make the key depend on
its own output, so a write would invalidate the record it just landed); and every L1 file is on disk.

**B. L1 exactness.** The audit-hook open-mode records at
`notes/development/probe/2026-10-12_rr_fleet.txt`,
`notes/development/probe/2026-10-12_seed_quotes.txt`,
`notes/development/probe/2026-10-11_writers.txt` and
`notes/development/probe/2026-10-10_writers.txt` list every `notes/`
path each target opened, with its mode. The registry's L1 must equal that set with the writer's own
outputs removed: a file the writer reads that the key does not name is a cache that can serve stale
bytes, which is the failure mode L1 exists to prevent, and a file the key names that the writer never
opens is a key that invalidates for nothing.

**C. Cache equals disk.** For every writer, the key is recomputed from the registry with the canonical
gate args, and every artifact (a file, or every file under a tree) is compared byte-for-byte with the
cache entry under that key. A missing entry is a problem, and so is a cache that disagrees with the
tracked tree.

The self-tests live in `notes/scripts/tests/test_cache_promotion.py`: eight injected faults, one per
pass, run through pytest. `main()` reads no argv, so `--mutant` is inert. Six faults are injected in
the registry structures the passes take as arguments; two corrupt a cache entry under `.qwen/cache/`,
which is untracked, and are undone by re-writing the disk bytes back. No fault touches a tracked file.
The checker measures; the test file injects.

Usage: python3 notes/scripts/verify_cache_promotion.py
"""
from __future__ import annotations

import re
import sys
from itertools import pairwise

from catlib import templates as T
from catlib.paths import ROOT
from catlib.promote import (
    ARGS,
    ARTIFACTS,
    L1,
    NON_CACHED,
    PAGE_EXTRA,
    PROBE_EXEMPT,
    REPORT_PAGES,
    expand,
    key_for,
)

# Newest first: a target is taken from the first record that names it, so the record a re-probe lands
# supersedes the older one for that target. `2026-10-12_seed_quotes_summaries` is the seeder run that
# reads the 21 summaries pages and the notes pages their Sources cells cite — the first record that
# names the summaries tree, so it supersedes the pair-page-only record for that target.
# `2026-10-12_rr_fleet` is the render_reports.py run that captures the fleet census — the writer reads
# the script tree and the two 2026-10-11 records, which the 2026-10-11 record of itself cannot name.
# `2026-10-12_extract_named_results` is the run that proves the population producer's L1: the older
# record for that target names `notes/catalog.tsv`, the ledger's pre-`tables/` path, so the new record
# is what makes the registry's `notes/tables/catalog.tsv` provable.
# `2026-10-12_measure_templates_tables` and `2026-10-12_rr_tables` are the post-`math-faz.6` records:
# the 16 generated tables moved out of `notes/index/` into `notes/tables/`, so the index tree these two
# writers read is 1,033 pages, not 1,049 files, and the older records for those targets name the 16 TSVs
# under the path the writers no longer open.
PROBES = (ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_147.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_332.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_pages.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_summaries.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_build_index_db.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-12_extract_named_results.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-12_measure_templates_tables.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-12_seed_quotes_summaries.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-12_rr_tables.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-12_seed_quotes.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-11_writers.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-10_writers.txt")
README = ROOT / "notes" / "scripts" / "README.md"
CACHE = ROOT / ".qwen" / "cache" / "records"


def probe_reads() -> dict[str, set[str]]:
    """Every notes/ path each probed target opened read-only, from the newest record naming it.

    The records are read newest first and a target is taken from the first record that names it: the
    2026-10-10 record describes the version of `extract_links.py` that pulled `render_reports`
    in-process, and unioning it with the current record would demand L1 entries the current script
    no longer reads.
    """
    out: dict[str, set[str]] = {}
    for probe in PROBES:
        lines = probe.read_text(encoding="utf-8").splitlines()
        targets = [i for i, line in enumerate(lines) if line.startswith("[probe2] target notes/scripts/")]
        targets.append(len(lines))
        for a, b in pairwise(targets):
            name = lines[a].split()[2].split("/")[-1]
            if name in out:
                continue
            section = None
            seen = out.setdefault(name, set())
            for line in lines[a + 1:b]:
                if line.startswith("[probe2]"):
                    m = re.match(r"\[probe2\] (\S+) paths", line)
                    section = m.group(1) if m else None
                    continue
                m = re.match(r"\s+(\d+)\s+(\w+)\s+(\S+)$", line)
                if m and section == "notes/" and m.group(2) == "r":
                    seen.add(m.group(3))
    return out


def norm(entry: str) -> str:
    """Registry and page target cells compared in the same form: no trailing slash."""
    return entry.rstrip("/")


def writers_table() -> dict[str, set[str]]:
    """The writers table in notes/scripts/README.md: script -> the set of target cells it names."""
    text = README.read_text(encoding="utf-8")
    m = re.search(r"### Writers\n(.*?)\n\n", text, re.DOTALL)
    rows: dict[str, set[str]] = {}
    for line in (m.group(1) if m else "").splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 3 or not cells[1].startswith("`"):
            continue
        rows[cells[1].strip("`")] = {norm(p) for p in re.findall(r"`([^`]+)`", cells[2])}
    return rows


def check(artifacts: dict[str, tuple[str, ...]], l1: dict[str, tuple[str, ...]],
         pages: tuple[str, ...], args: dict[str, tuple[str, ...]],
         non_cached: frozenset[str], page_extra: frozenset[str]) -> list[str]:
    """The three measurement passes; returns the problem lines, printing the per-writer counts."""
    p: list[str] = []
    reads = probe_reads()

    table = writers_table()
    if set(artifacts) | set(non_cached) != set(table) | set(page_extra):
        p.append(f"ARTIFACTS + non-cached writer set != writers table: "
                 f"{sorted(set(artifacts) | set(non_cached) ^ set(table) | set(page_extra))}")
    if set(l1) != set(artifacts):
        p.append(f"L1 writer set != ARTIFACTS: {sorted(set(l1) ^ set(artifacts))}")
    if set(pages) != set(T.ALL_PAGES):
        p.append(f"REPORT_PAGES != catlib/templates registry: {sorted(set(pages) ^ set(T.ALL_PAGES))}")
    for name, entries in l1.items():
        for entry in entries:
            for own in artifacts.get(name, ()):
                if norm(entry) == norm(own) or norm(entry).startswith(norm(own)):
                    p.append(f"L1 self-read: {name} names its own output {entry}")
            if not entry.endswith("/") and not (ROOT / entry).is_file():
                p.append(f"L1 entry not on disk: {name} {entry}")

    for name, entries in l1.items():
        if name in PROBE_EXEMPT:
            continue
        if name not in reads:
            p.append(f"L1 unprobed: {name} is not in the audit-hook records")
            continue
        # The probe record prints its `notes/` bucket, so the exactness check is scoped to that
        # bucket. A registry entry outside `notes/` (the root README.md) is proved by the source, not
        # by the record. The record omits `notes/scripts/` and `notes/development/probe/` from its
        # printed paths (the probe's own rule), so the comparison uses the same scope: a registry entry
        # naming the script tree hashes the sources the writer scans, and the record cannot name them.
        want = {path for path in reads[name]
                if not any(path.startswith(own) for own in artifacts[name])}
        got = {str(pp.relative_to(ROOT)) for entry in entries for pp in expand(entry)
               if str(pp.relative_to(ROOT)).startswith("notes/")
               and not str(pp.relative_to(ROOT)).startswith(("notes/scripts/",
                                                             "notes/development/probe/"))}
        if want != got:
            p.append(f"L1 drift {name}: probe names {sorted(want - got)}, "
                     f"registry names {sorted(got - want)}")

    for name, outs in artifacts.items():
        key = key_for(name, args.get(name, ()))
        bad = 0
        total = 0
        for entry in outs:
            paths = expand(entry)
            if not paths:
                p.append(f"artifact tree empty: {name} {entry}")
                continue
            for path in paths:
                total += 1
                cached = CACHE / key / str(path.relative_to(ROOT))
                if not cached.is_file():
                    bad += 1
                    p.append(f"cache entry missing: {name} {path.relative_to(ROOT)}")
                elif cached.read_bytes() != path.read_bytes():
                    bad += 1
                    p.append(f"cache != disk: {name} {path.relative_to(ROOT)}")
        print(f"{name}: key {key} artifacts {total} problems {bad}")
    return p


def main() -> int:
    problems = check(ARTIFACTS, L1, REPORT_PAGES, ARGS, NON_CACHED, PAGE_EXTRA)
    for line in problems:
        print(f"PROBLEM: {line}")
    print(f"\nwriters {len(ARTIFACTS)} + non-cached {len(NON_CACHED)}  "
          f"probed targets {len(probe_reads())}  problems {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
