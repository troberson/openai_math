"""The self-tests for `prune_stale()` in `catlib/promote.py`.

The bead's acceptance criterion is a test proving the prune cannot delete a
live key. The registry (ARTIFACTS | NON_CACHED via key_for) is the source of
truth for which keys are live; the prune must delete any key dir not in that
set and leave every key dir that is.

Three faults are tested: a live key survives, a stale key is deleted, and an
empty record store returns 0. The test uses a monkeypatched RECORDS_ROOT in a
temp dir, so no real cache entry is touched.

Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_prune_stale.py -q
"""
import pytest

pytestmark = pytest.mark.mutant


def _live_keys():
    """The current live key set, derived from the registry.

    Mirrors `prune_stale()`'s own tolerance: a NON_CACHED writer with no
    L1 entry (e.g. `measure_open_probe.py`) cannot compute a key, so
    `key_for` raises and the writer is skipped.
    """
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from catlib import promote as P
    keys = set()
    for w in sorted(set(P.ARTIFACTS) | P.NON_CACHED):
        try:
            keys.add(P.key_for(w, P.ARGS.get(w, ())))
        except Exception:
            pass
    return keys


def test_live_key_survives(monkeypatch, tmp_path):
    """A key dir that the registry computes must survive the prune."""
    from catlib import promote as P
    live = _live_keys()
    assert live, "registry produced no keys"
    key = next(iter(live))
    root = tmp_path / "records"
    (root / key).mkdir(parents=True)
    (root / key / "artifact.md").write_text("live", encoding="utf-8")
    monkeypatch.setattr(P, "RECORDS_ROOT", root)
    n = P.prune_stale()
    assert n == 0, f"prune removed {n} dirs, expected 0 (live key deleted)"
    assert (root / key).is_dir(), "live key dir was deleted"
    assert (root / key / "artifact.md").read_text(encoding="utf-8") == "live"


def test_stale_key_is_deleted(monkeypatch, tmp_path):
    """A key dir not in the registry must be deleted by the prune."""
    from catlib import promote as P
    live = _live_keys()
    root = tmp_path / "records"
    stale_key = "stale" + "0" * 28  # 32-hex, not a real key
    assert stale_key not in live
    (root / stale_key).mkdir(parents=True)
    (root / stale_key / "artifact.md").write_text("stale", encoding="utf-8")
    # also create a live key dir so the prune has both to sort
    live_key = next(iter(live))
    (root / live_key).mkdir(parents=True)
    (root / live_key / "artifact.md").write_text("live", encoding="utf-8")
    monkeypatch.setattr(P, "RECORDS_ROOT", root)
    n = P.prune_stale()
    assert n == 1, f"prune removed {n} dirs, expected 1 (the stale key)"
    assert not (root / stale_key).exists(), "stale key dir survived"
    assert (root / live_key).is_dir(), "live key dir was deleted"


def test_empty_store_returns_zero(monkeypatch, tmp_path):
    """An empty record store (no key dirs) returns 0 and does not raise."""
    from catlib import promote as P
    root = tmp_path / "records"
    root.mkdir()
    monkeypatch.setattr(P, "RECORDS_ROOT", root)
    n = P.prune_stale()
    assert n == 0
