"""Diff an out-of-tree render against the tracked tree.

Usage: python3 notes/scripts/diff_outdir.py <outdir> [in-tree-root]

Walks every file under <outdir>, maps it to the in-tree path (relative to the repo root,
or <in-tree-root> when given), and compares bytes. Reports:

  ok      — file exists in both, bytes match
  stale   — file exists in both, bytes differ (the in-tree copy is behind the writer)
  missing — file is in the outdir but absent from the in-tree tree (a new file the
            writer produced that has not been promoted)

Exits 1 when any file is stale or missing, 0 when every file is ok.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def main(argv: list[str]) -> int:
    if len(argv) < 2 or len(argv) > 3:
        print(f"usage: {argv[0]} <outdir> [in-tree-root]", file=sys.stderr)
        return 2
    outdir = Path(argv[1]).resolve()
    in_root = Path(argv[2]).resolve() if len(argv) == 3 else ROOT
    if not outdir.is_dir():
        print(f"not a directory: {outdir}", file=sys.stderr)
        return 2

    n_ok = n_stale = n_missing = 0
    for f in sorted(outdir.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(outdir)
        target = in_root / rel
        if not target.is_file():
            print(f"missing  {rel}")
            n_missing += 1
            continue
        if f.read_bytes() == target.read_bytes():
            n_ok += 1
        else:
            print(f"stale    {rel}")
            n_stale += 1

    print(f"\nfiles checked {n_ok + n_stale + n_missing}  ok {n_ok}  stale {n_stale}  missing {n_missing}")
    return 1 if (n_stale or n_missing) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
