#!/usr/bin/env python3
"""Write the check()-call counts for the eleven checkers whose self-tests are extracted.

The record is the product: `check_calls.json` lands under `.qwen/cache/records/<key>/`, keyed by the
script tree's git digest (the checker sources and the test files both live in that tree) plus the
canonical args. There is no tracked artifact, so this is a record producer and the census names the
record, not a page.

The harness patches `importlib.util.spec_from_file_location`, because the conftest's `load` fixture
builds each checker with exactly that call: wrapping `check` at load time is what counts the calls the
tests actually make. The checkers are loaded by bare name (`verify_findings`), so the target list is
bare names without `.py`, and the test file is the checker name with `verify_` dropped.

The counts are the population the census page's `check()` sentences quote. The baseline recorded here
is the probe's measurement of 2026-10-13; a run that disagrees prints the difference, which is the
point of gating the probe: an ungated baseline drifts with nothing to catch it.

Usage: python3 notes/scripts/measure_check_calls.py [--check-only]
"""
from __future__ import annotations

import importlib.util as iu
import json
import sys

import pytest
from catlib.paths import SCRIPTS
from catlib.promote import key_for, prune_stale
from catlib.records import cached

KEY = key_for("measure_check_calls.py", tuple(sys.argv[1:]))

TARGETS = [
    "verify_findings",
    "verify_faithfulness",
    "verify_sources",
    "verify_index_design",
    "verify_fleet_design",
    "verify_verification_dirs",
    "verify_named_results",
    "verify_citations",
    "verify_t0_chains",
    "verify_dependency_drift",
    "verify_subfinding_pairs",
]

# The probe's measurement of 2026-10-13, the baseline the census page's check() sentences carry.
BASELINE = {
    "verify_findings": 9,
    "verify_faithfulness": 33,
    "verify_sources": 15,
    "verify_index_design": 17,
    "verify_fleet_design": 23,
    "verify_verification_dirs": 21,
    "verify_named_results": 15,
    "verify_citations": 12,
    "verify_t0_chains": 17,
    "verify_dependency_drift": 12,
    "verify_subfinding_pairs": 11,
}


def count_calls(targets: list[str]) -> dict[str, int]:
    """Run one pytest row per checker, counting the calls its module's check() receives.

    A checker whose module exposes no `check` is recorded as -1, so a missing pass is a row the report
    prints, not a zero that reads like a low count. A pytest row that exits non-zero is recorded the
    same way: the count is meaningless when the tests fail.
    """
    orig = iu.spec_from_file_location
    counts: dict[str, int] = {}

    def spec_from_file_location(name, location, *a, **k):
        spec = orig(name, location, *a, **k)
        if spec is None or spec.loader is None:
            return spec
        if name in targets:
            real_exec = spec.loader.exec_module

            def exec_module(mod):
                real_exec(mod)
                orig_check = getattr(mod, "check", None)
                if orig_check is None:
                    counts[name] = -1
                    return

                def wrapper(*args, **kw):
                    counts[name] += 1
                    return orig_check(*args, **kw)

                mod.check = wrapper

            spec.loader.exec_module = exec_module
            counts[name] = 0
        return spec

    # Assignment, not setattr: ruff flags a constant setattr (B010). The wrapper's signature is
    # deliberately looser than the stdlib function's, so the rebinding needs the mypy ignore —
    # the same form the conftest's monkeypatch fixture uses.
    iu.spec_from_file_location = spec_from_file_location  # type: ignore[assignment]
    try:
        for t in targets:
            counts[t] = 0
            code = pytest.main(["-q", str(SCRIPTS / "tests" / f"test_{t.removeprefix('verify_')}.py")])
            if code != 0:
                counts[t] = -1
    finally:
        iu.spec_from_file_location = orig
    return counts


def report(counts: dict[str, int]) -> None:
    bad = [t for t in TARGETS if counts[t] != BASELINE[t]]
    print(f"record key {KEY}")
    print(f"checkers {len(TARGETS)}  rows run {len(counts)}")
    for t in TARGETS:
        note = "" if counts[t] == BASELINE[t] else f"   baseline {BASELINE[t]}"
        print(f"{t:26} check calls {counts[t]}{note}")
    print(f"total check calls {sum(v for v in counts.values() if v > 0)}")
    print(f"baseline disagreements {len(bad)} {bad}")


def main() -> int:
    def build() -> str:
        return json.dumps(count_calls(TARGETS), indent=1)

    # A warm run reads the record: the key hashes the script tree, so a run that changes nothing
    # reads the bytes the first run landed and pays no pytest rows. --check-only builds without
    # landing, so the measurement is the same and the store is untouched.
    if "--check-only" in sys.argv[1:]:
        counts = json.loads(build())
    else:
        counts = json.loads(cached(KEY, "check_calls.json", build))
        prune_stale()
    report(counts)
    return 1 if any(counts[t] < 0 for t in TARGETS) else 0


if __name__ == "__main__":
    sys.exit(main())
