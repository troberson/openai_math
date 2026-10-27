"""Atomic write: a crash must never leave a partial file in the tracked tree.

The rule `notes/development/fleet-design.md` measures: the atomicity grep over `notes/scripts/*.py`
and `notes/scripts/catlib/*.py`, excluding `verify_fleet_design.py` (which carries the pattern as a
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
import tempfile
from pathlib import Path

from catlib.paths import ROOT

STAGING_ROOT = ROOT / ".qwen" / "cache" / "staging"
RECORDS_ROOT = ROOT / ".qwen" / "cache" / "records"


def write_atomic(path: Path, text: str) -> None:
    """Write text to path through a sibling temp name, fsync, then an atomic move onto the target.

    The temp name is unique per call (`mkstemp`), not fixed to `.{name}.tmp`: two concurrent writers to
    the same directory (the two build_index children build_report_templates.py spawns) must not share a
    temp, or one child's move consumes it before the other's and the second raises
    FileNotFoundError. The `mkstemp` prefix keeps it dotted, so it stays out of a page census and the
    atomicity grep; the suffix carries no extension a checker keys on. math-9vt.
    """
    parent = path.parent
    parent.mkdir(parents=True, exist_ok=True)
    fd, tmpname = tempfile.mkstemp(prefix=f".{path.name}.", dir=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmpname, path)
    except BaseException:
        os.unlink(tmpname)
        raise


def cache_text(key: str, artifact: str, text: str) -> None:
    """Land text under the keyed record store. The store is untracked by the `.qwen/*` rule."""
    d = RECORDS_ROOT / key
    d.mkdir(parents=True, exist_ok=True)
    write_atomic(d / artifact, text)


class Staging:
    """Staged writes for a multi-file writer: bytes land untracked, promote() moves them onto the tree.

    With `out_root` set (the writer's `--outdir` flag) promote() is a root override, not a per-file
    fork: every target goes to `out_root / path.relative_to(ROOT)`, the tracked tree is never
    touched, and no record is cached — the record store keys on tracked bytes, so a diff-only
    render must not feed the promote-and-verify assertion.
    """

    def __init__(self, name: str, key: str | None = None, out_root: Path | None = None) -> None:
        self.name = name
        self.key = key
        self.out_root = out_root
        self.root = STAGING_ROOT / name
        self._targets: list[Path] = []
        self._texts: list[str] = []

    def stage(self, path: Path, text: str) -> None:
        """Land text in a numbered slot under the staging root, cache it under the key, record the tracked path."""
        slot = self.root / f"{len(self._targets):04d}"
        slot.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(slot, text)
        if self.key and self.out_root is None:
            cache_text(self.key, str(path.relative_to(ROOT)), text)
        self._targets.append(path)
        self._texts.append(text)

    def staged(self) -> list[Path]:
        """The tracked paths staged so far, in staging order."""
        return list(self._targets)

    def staged_texts(self) -> list[str]:
        """The text staged so far, in staging order — the bytes a `--check-only` run reports without promoting."""
        return list(self._texts)

    def promote(self) -> None:
        """Move every staged slot onto its tracked path, then drop the staging tree. The approval step.

        With `out_root` set, the tracked path is never touched: each slot is written through
        `write_atomic` to `out_root / path.relative_to(ROOT)` (a copy, not a move — the slot must
        survive for the next target), so an out-of-tree render leaves the working tree and the
        record store exactly as they were.
        """
        for i, path in enumerate(self._targets):
            if self.out_root is None:
                path.parent.mkdir(parents=True, exist_ok=True)
                os.replace(self.root / f"{i:04d}", path)
            else:
                target = self.out_root / path.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                write_atomic(target, self._texts[i])
        self._targets = []
        shutil.rmtree(self.root, ignore_errors=True)
