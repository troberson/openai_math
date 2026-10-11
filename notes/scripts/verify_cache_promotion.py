#!/usr/bin/env python3
"""Prove the promotion protocol: every tracked artifact's bytes equal the bytes under its key.

Four passes, all read-only, writing nothing to the tracked tree:

**A. Registry shape.** The writer set in `catlib/promote.py`'s `ARTIFACTS`, plus the writer the
protocol deliberately excludes, equals the writers table in `notes/scripts/README.md`; `L1` and
`ARTIFACTS` cover the same writer set; `REPORT_PAGES` equals the registry keys in
`catlib/templates.py`; no writer's L1 names a file it writes (a self-read would make the key depend on
its own output, so a write would invalidate the record it just landed); and every L1 file is on disk.

**B. L1 exactness.** The audit-hook open-mode records at `notes/probe/2026-10-11_writers.txt` and
`notes/probe/2026-10-10_writers.txt` list every `notes/` path each target opened, with its mode. The
registry's L1 must equal that set with the writer's own outputs removed: a file the writer reads that
the key does not name is a cache that can serve stale bytes, which is the failure mode L1 exists to
prevent, and a file the key names that the writer never opens is a key that invalidates for nothing.

**C. Cache equals disk.** For every writer, the key is recomputed from the registry with the canonical
gate args, and every artifact (a file, or every file under a tree) is compared byte-for-byte with the
cache entry under that key. A missing entry is a problem, and so is a cache that disagrees with the
tracked tree.

**D. Mutants.** `--mutant` corrupts one cached page, deletes one cached page, removes one L1 entry the
probe names, adds one L1 entry that is a self-output, drops one writer from `ARTIFACTS`, alters one
`REPORT_PAGES` entry, alters one tracked page on disk, and shifts one writer's canonical args. Each is
asserted against the pass that must catch it, and every mutation is undone before the run ends.

Usage: python3 notes/scripts/verify_cache_promotion.py [--mutant]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from catlib import templates as T
from catlib.promote import (ARTIFACTS, ARGS, L1, NON_CACHED, PAGE_EXTRA, PROBE_EXEMPT,
                            REPORT_PAGES, expand, key_for)
from catlib.paths import ROOT

PROBES = (ROOT / "notes" / "probe" / "2026-10-11_writers.txt",
          ROOT / "notes" / "probe" / "2026-10-10_writers.txt")
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
        for a, b in zip(targets, targets[1:]):
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
    m = re.search(r"### Writers\n(.*?)\n\n", text, re.S)
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
        # by the record.
        want = {path for path in reads[name]
                if not any(path.startswith(own) for own in artifacts[name])}
        got = {str(pp.relative_to(ROOT)) for entry in entries for pp in expand(entry)
               if str(pp.relative_to(ROOT)).startswith("notes/")}
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


def mutate(label: str) -> tuple[dict, dict, tuple, dict]:
    """Apply one mutation to the registry (or to the bytes it checks) and return the mutated inputs."""
    a = {k: tuple(v) for k, v in ARTIFACTS.items()}
    l = {k: tuple(v) for k, v in L1.items()}
    pg = list(REPORT_PAGES)
    ar = {k: tuple(v) for k, v in ARGS.items()}
    if label == "cached page corrupted":
        key = key_for("render_reports.py", ())
        path = CACHE / key / "notes/sources.md"
        path.write_text(path.read_text(encoding="utf-8") + "MUTANT\n", encoding="utf-8")
    elif label == "cached page deleted":
        key = key_for("render_reports.py", ())
        (CACHE / key / "notes/names.md").unlink(missing_ok=True)
    elif label == "L1 entry the probe names removed":
        l["refresh_summary_line_counts.py"] = tuple(
            e for e in l["refresh_summary_line_counts.py"] if e != "notes/t0-triage.md")
    elif label == "L1 entry added that is a self-output":
        l["build_index.py"] = l["build_index.py"] + ("notes/index/",)
    elif label == "writer dropped from ARTIFACTS":
        a.pop("extract_links.py")
        l.pop("extract_links.py")
    elif label == "REPORT_PAGES entry altered":
        pg = [p for p in pg if p != "notes/topics.md"] + ["notes/topics2.md"]
    elif label == "tracked page altered on disk":
        page = ROOT / "notes" / "proof-density.md"
        page.write_text(page.read_text(encoding="utf-8") + "\nMUTANT\n", encoding="utf-8")
    elif label == "canonical args shifted":
        ar["compare_abstracts.py"] = ("--tsv", "extra")
    return a, l, tuple(pg), ar


def restore(label: str) -> None:
    """Undo a byte-level mutation so a mutant run leaves the tree and the cache as it found them."""
    if label in ("cached page corrupted", "cached page deleted"):
        key = key_for("render_reports.py", ())
        rel = "notes/sources.md" if label == "cached page corrupted" else "notes/names.md"
        disk = ROOT / rel
        (CACHE / key / rel).write_bytes(disk.read_bytes())
    elif label == "tracked page altered on disk":
        page = ROOT / "notes" / "proof-density.md"
        text = page.read_text(encoding="utf-8")
        page.write_text(text.replace("\nMUTANT\n", ""), encoding="utf-8")


def main() -> int:
    if "--mutant" not in sys.argv[1:]:
        problems = check(ARTIFACTS, L1, REPORT_PAGES, ARGS, NON_CACHED, PAGE_EXTRA)
        for line in problems:
            print(f"PROBLEM: {line}")
        print(f"\nwriters {len(ARTIFACTS)} + non-cached {len(NON_CACHED)}  "
              f"probed targets {len(probe_reads())}  problems {len(problems)}")
        return 1 if problems else 0

    cases = [
        ("cached page corrupted", "cache != disk"),
        ("cached page deleted", "cache entry missing"),
        ("L1 entry the probe names removed", "L1 drift"),
        ("L1 entry added that is a self-output", "L1 self-read"),
        ("writer dropped from ARTIFACTS", "ARTIFACTS + non-cached writer set"),
        ("REPORT_PAGES entry altered", "REPORT_PAGES"),
        ("tracked page altered on disk", "cache != disk"),
        ("canonical args shifted", "cache entry missing"),
    ]
    print("=== cache promotion mutant self-test ===")
    caught = 0
    for label, needle in cases:
        a, l, pg, ar = mutate(label)
        problems = check(a, l, pg, ar, NON_CACHED, PAGE_EXTRA)
        restore(label)
        hit = [x for x in problems if needle in x]
        if hit:
            caught += 1
            print(f"  caught {label}: {hit[0]}")
        else:
            print(f"  NOT CAUGHT {label}")
    print(f"mutants flagged: {caught} of {len(cases)}")
    return 0 if caught == len(cases) else 1


main()
