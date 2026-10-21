"""Self-test for catlib/atomic.write_atomic's process-safety.

Two concurrent writers to the same directory must not collide on a shared temp name. `write_atomic`
used a fixed sibling temp `.{name}.tmp`, so the two `build_index.py --check-only` children that
`build_report_templates.py` spawns (one per page that calls `build_index_report`) both targeted the
same `.NNNN.tmp`, and one child's `os.replace` consumed the temp before the other's, raising
`FileNotFoundError`. Non-deterministic (trial 1 `[1,0]`, trial 2 `[0,1]`), so the test mirrors the
real shape — several child processes each writing many identically-named files to one directory, as
`build_index` does over its 1,033 pages — and asserts every child lands its full files.

Run: python3 notes/scripts/run_tests.py notes/scripts/tests/test_atomic.py -q
"""

from __future__ import annotations

import concurrent.futures as cf
import os
import subprocess
import sys

from catlib import atomic
from catlib.paths import ROOT

SCRIPTS = ROOT / "notes" / "scripts"
# The real collision is over identically-named targets, so this is the same shape as build_index's
# 1,033 pages; 64 files x 4096 bytes x 4 children is enough to land the collision reliably while
# keeping the child cheap.
N_FILES = 64
N_CHILDREN = 4
N_TRIALS = 3
PAYLOAD = 4096

CHILD = (
    "import sys\n"
    "from pathlib import Path\n"
    "from catlib.atomic import write_atomic\n"
    "d = Path(sys.argv[1])\n"
    f"for i in range({N_FILES}):\n"
    f"    write_atomic(d / f'file{{i}}.txt', 'x' * {PAYLOAD})\n"
)


def _child(dirpath) -> int:
    """Launch one writer child over the shared directory; return its exit code."""
    p = subprocess.run([sys.executable, "-c", CHILD, str(dirpath)],
                       capture_output=True, text=True, cwd=ROOT, check=False,
                       env={**os.environ, "PYTHONPATH": str(SCRIPTS)})
    return p.returncode


def test_concurrent_children_do_not_collide(tmp_path):
    """Every concurrent child lands all N_FILES files in full; the old fixed temp name made at
    least one child raise FileNotFoundError in at least one of N_TRIALS trials."""
    for _ in range(N_TRIALS):
        with cf.ThreadPoolExecutor(max_workers=N_CHILDREN) as ex:
            codes = list(ex.map(lambda _: _child(tmp_path), range(N_CHILDREN)))
        assert all(c == 0 for c in codes), f"a child crashed: codes={codes}"
    for i in range(N_FILES):
        assert (tmp_path / f"file{i}.txt").read_bytes() == b"x" * PAYLOAD, i


def test_single_writer_lands_full_bytes(tmp_path):
    """The unchanged contract: one writer lands the full bytes, and no temp name lingers."""
    target = tmp_path / "one.txt"
    atomic.write_atomic(target, "hello atomic")
    assert target.read_text(encoding="utf-8") == "hello atomic"
    leftovers = [p.name for p in tmp_path.iterdir() if p.name != "one.txt"]
    assert leftovers == [], leftovers
