"""The self-tests for `notes/scripts/verify_cache_promotion.py`.

The checker proves the promotion protocol in three passes: the registry shape (the writer set against
the writers table, `L1` against `ARTIFACTS`, `REPORT_PAGES` against the templates registry, no L1
self-read, every L1 file on disk), the L1 exactness against the audit-hook records, and cache-equals-
disk for every artifact under the key the registry recomputes. This file injects eight faults, one per
pass, and asserts each fires the pass that owns it.

Five faults are injected in the registry structures the passes take as arguments: an L1 entry the
probe names removed, an L1 entry added that is a self-output, a writer dropped from `ARTIFACTS`, a
`REPORT_PAGES` entry altered, and a writer's canonical args shifted. Three corrupt the cache under
`.qwen/cache/`, which is untracked: a cached page corrupted, a cached page deleted, and a second
cached page corrupted on a different writer's artifact. Each is undone by writing the disk bytes back,
so the run leaves the cache as it found it. No fault touches a tracked file.

The clean test asserts the three passes are silent on the registry as committed. Each fault asserts
the needle is the problem string the pass that owns it prints.

The checker reads no argv and the passes take the registry as arguments, so nothing here writes a
tracked file: the checker writes nothing and the tests write only untracked cache entries.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_cache_promotion.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Faults in the registry structures the passes read, each keyed to the problem string it prints.
REGISTRY_CASES = [
    ("L1 entry the probe names removed", "L1 drift refresh_summary_line_counts.py",
     lambda a, l, pg, ar: (a, {**l, "refresh_summary_line_counts.py":
                               tuple(e for e in l["refresh_summary_line_counts.py"]
                                   if e != "notes/reports/t0-triage.md")}, pg, ar)),
    ("L1 entry added that is a self-output", "L1 self-read: build_index.py",
     lambda a, l, pg, ar: (a, {**l, "build_index.py": l["build_index.py"] + ("notes/index/",)}, pg, ar)),
    ("writer dropped from ARTIFACTS", "ARTIFACTS + non-cached writer set",
     lambda a, l, pg, ar: ({k: v for k, v in a.items() if k != "extract_links.py"},
                           {k: v for k, v in l.items() if k != "extract_links.py"}, pg, ar)),
    ("REPORT_PAGES entry altered", "REPORT_PAGES != catlib/templates registry",
     lambda a, l, pg, ar: (a, l, (*[p for p in pg if p != "notes/reports/topics.md"], "notes/topics2.md"), ar)),
    ("canonical args shifted", "cache entry missing: compare_abstracts.py",
     lambda a, l, pg, ar: (a, l, pg, {**ar, "compare_abstracts.py": ("--tsv", "extra")})),
]

# Faults in the cache entries the byte comparison reads, each keyed to the problem string it prints.
CACHE_CASES = [
    ("cached page corrupted", "notes/reports/sources.md", "cache != disk: render_reports.py notes/reports/sources.md",
     lambda text: text + "MUTANT\n"),
    ("cached page deleted", "notes/reports/names.md", "cache entry missing: render_reports.py notes/reports/names.md",
     None),
    ("second cached page corrupted", "notes/reports/proof-density.md",
     "cache != disk: render_reports.py notes/reports/proof-density.md", lambda text: text + "MUTANT\n"),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_cache_promotion")


@pytest.fixture(scope="module")
def reg(mod):
    return (dict(mod.ARTIFACTS), dict(mod.L1), tuple(mod.REPORT_PAGES), dict(mod.ARGS))


def clean(mod, reg):
    a, l, pg, ar = reg
    return mod.check(a, l, pg, ar, mod.NON_CACHED, mod.PAGE_EXTRA)


def cache_path(mod, rel):
    return mod.CACHE / mod.key_for("render_reports.py", ()) / rel


def test_clean_registry(mod, reg):
    """All three passes are silent on the registry as committed."""
    problems = clean(mod, reg)
    assert not problems, problems[:3]


@pytest.mark.parametrize("label,needle,mut", REGISTRY_CASES)
def test_injected_registry_faults(mod, reg, label, needle, mut):
    """A registry structure altered in memory. The needle is the problem string the pass prints."""
    a, l, pg, ar = reg
    cand = mut(a, l, pg, ar)
    assert cand != (a, l, pg, ar), f"{label}: mutation changed nothing"
    found = mod.check(cand[0], cand[1], cand[2], cand[3], mod.NON_CACHED, mod.PAGE_EXTRA)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


@pytest.mark.parametrize("label,rel,needle,mut", CACHE_CASES)
def test_injected_cache_faults(mod, reg, label, rel, needle, mut):
    """A cache entry corrupted or deleted under the untracked key, restored from the disk bytes.
    The byte comparison is the pass that owns this, so the needle names the artifact it flags."""
    path = cache_path(mod, rel)
    assert path.is_file(), f"{label}: the clean cache entry is absent, so the pass is not being run"
    try:
        if mut is None:
            path.unlink()
        else:
            path.write_text(mut(path.read_text(encoding="utf-8")), encoding="utf-8")
        found = clean(mod, reg)
        assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
    finally:
        path.write_bytes((mod.ROOT / rel).read_bytes())
    assert path.read_bytes() == (mod.ROOT / rel).read_bytes(), f"{label}: restore did not land"


def pad_cells(t):
    """Pad every table cell with two spaces."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = ln
        out.append(padded)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod):
    r"""The writers-table reader (`:126`) splits each row and strips every cell, so padding must read
    the same 15 rows. The byte-exact baseline is the row shape with exactly one space around each cell
    (`^\\| \`([^`]+\\.py)\` \\| \`([^`]+)\` \\|`): it reads 42 table rows on the clean page and 0 on the
    padded page. The reader takes no text argument, so the padded text is fed by swapping the module's
    README path for a shim — no file is written."""
    text = mod.README.read_text(encoding="utf-8")
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    clean = mod.writers_table()
    real = mod.README

    class Shim:
        """A path stand-in that returns the padded page text."""

        def read_text(self, *_args, **_kwargs):
            return cand

    mod.README = Shim()
    padded = mod.writers_table()
    mod.README = real
    assert padded == clean, f"padded writers table reads {len(padded)} rows, clean page {len(clean)}"


def test_tree_entries_hash_only_tracked_files(monkeypatch):
    """A tree L1 entry expands to the tracked files, so an untracked file under the tree
    moves neither the expansion nor the writer's key: the record is a function of the
    tracked read surface, and a scratch probe under the tree is not part of it. The proof
    is the writer's own key — `render_reports.py` names `notes/tables/` as a tree, and the
    key is identical with an untracked file sitting in that tree. RUN_ARGS carries a live
    bd count for this writer, so it is pinned to a constant and both reads see the same
    count; the only thing that may move is the surface. An explicit file entry is
    unaffected by the rule: `measure_gate_rows.py` names its untracked driver report by path.
    """
    from catlib import promote as PR

    scratch = PR.ROOT / "notes" / "tables" / ".expansion-scratch.txt"
    assert not scratch.exists(), "a stale scratch file would move the before key too"
    monkeypatch.setitem(PR.RUN_ARGS, "render_reports.py", lambda: ())
    before_exp = PR.expand("notes/tables/")
    before_key = PR.key_for("render_reports.py", ())
    assert PR.expand("README.md") == [PR.ROOT / "README.md"], "an explicit file entry must stay as declared"
    scratch.write_text("scratch\n")
    try:
        mid_exp = PR.expand("notes/tables/")
        mid_key = PR.key_for("render_reports.py", ())
    finally:
        scratch.unlink()
    after_key = PR.key_for("render_reports.py", ())
    extra = {str(p) for p in mid_exp} - {str(p) for p in before_exp}
    assert mid_exp == before_exp, f"an untracked file in the tree entered the expansion: {sorted(extra)}"
    assert before_key == mid_key == after_key, "the key moved while an untracked file sat in the tree"
