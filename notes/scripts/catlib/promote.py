"""Promotion: the cached copy is the record, the write onto the tracked path is the approval.

A writer computes its bytes once, lands them under the digest-keyed record store, and only then
writes them onto the tracked target. Two things follow: the tracked file and the cache entry are the
same bytes by construction, which is the test that replaces the twice-run; and a killed writer leaves
the tracked tree untouched, because the approval is the last step, not the first.

The key is the **builder's** key, not the consumer's: it hashes the five `git rev-parse HEAD:<path>`
tree digests, the builder's own source, the tracked files it reads that sit outside those trees (its
L1 list), and its args. A consumer that changes how it reads must not invalidate records it reads
unchanged.

`L1` and `ARTIFACTS` are the registry: one list per writer, read by the writer (through `key_for`)
and by `verify_cache_promotion.py`, so a writer and its verifier cannot drift into two implementations
of the same join. The L1 lists are derived from the audit-hook open-mode records at
`notes/probe/2026-10-11_writers.txt` and `notes/probe/2026-10-10_writers.txt`, with each writer's own
outputs excluded: a file the writer reads that the key does not name is a cache that can serve stale
bytes, which is the failure mode the exactness check exists to catch.

A trailing `/` in an L1 entry is a tree: it expands to every file under it, sorted. Writers compute
their key inside `main()`, not at import — `catlib/templates.py` imports `render_reports`, whose L1
names the 1,049-file index tree, so a module-level key would make every consumer of the registry pay
that read. `measure_open_probe.py` is deliberately absent: its record carries a wall time per target,
so it is a measurement of a run, not a function of a digest, and a cache would serve stale timings.
"""

from __future__ import annotations

from pathlib import Path

from catlib.atomic import RECORDS_ROOT, cache_text, write_atomic
from catlib.paths import ROOT, SCRIPTS
from catlib.records import key as digest_key

# The seventeen report-fed pages, in the order the registry in `catlib/templates.py` lists them.
REPORT_PAGES = (
    "notes/abstracts.md",
    "notes/index-links.md",
    "notes/index-design.md",
    "notes/links.md",
    "notes/dependency-drift.md",
    "notes/named-results.md",
    "notes/names.md",
    "notes/proof-density.md",
    "notes/sources.md",
    "notes/verification-dirs.md",
    "notes/scope-exclusions.md",
    "notes/topics.md",
    "notes/t0-chains.md",
    "notes/subfinding-pairs.md",
    "notes/counterexample-crosscheck.md",
    "notes/templates.md",
    "notes/README.md",
)

L1: dict[str, tuple[str, ...]] = {
    # The root README.md is the release's trace table: `catlib/yaml.py` reads it for the trace
    # attribution, so every writer that imports that module reads a file the five hashed trees do not
    # cover. It sits outside `notes/`, so the probe's notes/ section cannot prove it; the source names it.
    "build_catalog.py": ("README.md",),
    "build_sources.py": ("notes/tables/catalog.tsv",),
    "extract_links.py": ("notes/tables/catalog.tsv", "README.md"),
    "extract_subfindings.py": ("notes/tables/catalog.tsv",),
    "extract_formalization_deps.py": (),
    "compare_abstracts.py": ("notes/tables/catalog.tsv", "notes/tables/sources.tsv"),
    "refresh_summary_line_counts.py": ("notes/tables/catalog.tsv", "notes/counterexample-tag.md",
                                       "notes/sources.md", "notes/t0-triage.md"),
    "build_index.py": ("README.md", "notes/tables/catalog.tsv", "notes/tables/sources.tsv", "notes/tables/topics.tsv",
                       "notes/templates/discipline.md.j2", "notes/templates/family.md.j2",
                       "notes/templates/index-readme.md.j2", "notes/templates/name.md.j2",
                       "notes/templates/topic.md.j2"),
    "render_reports.py": ("README.md", "notes/tables/abstracts.tsv", "notes/tables/catalog.tsv",
                          "notes/tables/conjecture-standing.tsv", "notes/formalization-deps.md",
                          "notes/tables/formalization-deps.tsv", "notes/tables/links.tsv",
                          "notes/tables/sources.tsv", "notes/tables/subfindings.tsv", "notes/t0-triage.md",
                          "notes/tables/topics.tsv", "notes/templates/", "notes/index/"),
    "build_report_templates.py": REPORT_PAGES,
}

ARTIFACTS: dict[str, tuple[str, ...]] = {
    "build_catalog.py": ("notes/tables/catalog.tsv",),
    "build_sources.py": ("notes/tables/sources.tsv",),
    "extract_links.py": ("notes/tables/links.tsv",),
    "extract_subfindings.py": ("notes/tables/subfindings.tsv",),
    "extract_formalization_deps.py": ("notes/tables/formalization-deps.tsv",),
    "compare_abstracts.py": ("notes/tables/abstracts.tsv",),
    "refresh_summary_line_counts.py": ("notes/summaries/",),
    "build_index.py": ("notes/index/",),
    "render_reports.py": REPORT_PAGES,
    "build_report_templates.py": ("notes/templates/report/",),
}


# The args each writer's gate row runs it with, so the verifier recomputes the same key the writer
# used. A plain run and a `--tsv` run do not share a record, so the canonical invocation is part of the key.
ARGS: dict[str, tuple[str, ...]] = {
    "build_catalog.py": (),
    "build_sources.py": (),
    "extract_links.py": (),
    "extract_subfindings.py": (),
    "extract_formalization_deps.py": (),
    "compare_abstracts.py": ("--tsv",),
    "refresh_summary_line_counts.py": (),
    "build_index.py": (),
    "render_reports.py": (),
    "build_report_templates.py": (),
}

# The writers table names one writer the protocol deliberately excludes: `measure_open_probe.py`'s
# record carries a wall time per target, so it is a measurement of a run, not a function of a digest.
NON_CACHED = frozenset({"measure_open_probe.py"})

# The registry covers one writer the page lists as a checker, because its gate row runs first among
# the checkers: `refresh_summary_line_counts.py` rewrites the `Lines` cell of the summaries pages.
PAGE_EXTRA = frozenset({"refresh_summary_line_counts.py"})

# One writer's L1 cannot be proved against the audit-hook record: `build_report_templates.py` reads
# each page with `git show HEAD:<page>`, a subprocess read the `open` audit event never sees, so the
# record for it carries only the reads its imports perform. Its L1 is the page set its own source names.
PROBE_EXEMPT = frozenset({"build_report_templates.py"})


def expand(entry: str) -> list[Path]:
    """A repo-relative file, or every file under a repo-relative tree when the entry ends in `/`."""
    if entry.endswith("/"):
        return sorted(p for p in (ROOT / entry).rglob("*") if p.is_file())
    return [ROOT / entry]


def l1_paths(name: str) -> list[Path]:
    """The writer's declared L1 inputs, expanded, in registry order."""
    return [p for entry in L1[name] for p in expand(entry)]


def key_for(name: str, args: tuple[str, ...] = ()) -> str:
    """The builder's cache key: tree digests, the builder's source, its L1 inputs, its args."""
    script = SCRIPTS / name
    texts = tuple(p.read_text(encoding="utf-8") for p in l1_paths(name))
    return digest_key(script.read_text(encoding="utf-8"), texts, args)


def artifact_of(path: Path) -> str:
    """The cache artifact name: the repo-relative path, so pages in sibling dirs never collide."""
    return str(path.relative_to(ROOT))


def promote(path: Path, key: str, text: str) -> None:
    """The approval: cache the bytes under the key, then write the same bytes onto the tracked path."""
    cache_text(key, artifact_of(path), text)
    write_atomic(path, text)


def cached_text(path: Path, key: str) -> str | None:
    """The cached bytes for a tracked path under this key, or None when the cache has no entry."""
    p = RECORDS_ROOT / key / artifact_of(path)
    return p.read_text(encoding="utf-8") if p.is_file() else None
