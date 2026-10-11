"""Atomic write: a crash must never leave a partial file in the tracked tree.

The rule `notes/fleet-design.md` measures: the atomicity grep over `notes/scripts/*.py` and
`notes/scripts/catlib/*.py`, excluding `verify_fleet_design.py` (which carries the pattern as a
needle), read **0** matches before this module. Every writer opened its tracked target directly, so
a crash mid-write left a half-written tracked file.

`write_atomic` writes to a sibling temp name in the same directory, flushes, fsyncs, then replaces the
temp onto the target. Same filesystem, so the move is atomic: the target holds the old bytes or the
new bytes, never a prefix of them. The temp name is dotted, so it never matches a page's own
basename and never lands in a census of the directory.

`Staging` is the multi-file case: a writer that produces more than one tracked file cannot promote
them one at a time and stay crash-safe, because the second file's write is a half-updated tree from
the first promotion onward. `stage()` lands bytes under `.qwen/cache/staging/<name>/`, which the
`.qwen/*` rule in `.gitignore` keeps untracked, and records the tracked path. `promote()` is the
approval: it moves every staged slot onto its tracked path, and a writer calls it only after every
internal check has passed. Killing a writer mid-run leaves the tracked tree untouched.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from catlib.paths import ROOT

STAGING_ROOT = ROOT / ".qwen" / "cache" / "staging"


def write_atomic(path: Path, text: str) -> None:
    """Write text to path through a sibling temp name, fsync, then an atomic move onto the target."""
    parent = path.parent
    parent.mkdir(parents=True, exist_ok=True)
    tmp = parent / f".{path.name}.tmp"
    with tmp.open("w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


class Staging:
    """Staged writes for a multi-file writer: bytes land untracked, promote() moves them onto the tree."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.root = STAGING_ROOT / name
        self._targets: list[Path] = []

    def stage(self, path: Path, text: str) -> None:
        """Land text in a numbered slot under the staging root and record the tracked path it will move to."""
        slot = self.root / f"{len(self._targets):04d}"
        slot.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(slot, text)
        self._targets.append(path)

    def staged(self) -> list[Path]:
        """The tracked paths staged so far, in staging order."""
        return list(self._targets)

    def promote(self) -> None:
        """Move every staged slot onto its tracked path, then drop the staging tree. The approval step."""
        for i, path in enumerate(self._targets):
            path.parent.mkdir(parents=True, exist_ok=True)
            os.replace(self.root / f"{i:04d}", path)
        self._targets = []
        shutil.rmtree(self.root, ignore_errors=True)
