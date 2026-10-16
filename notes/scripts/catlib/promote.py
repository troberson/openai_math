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
`notes/development/probe/2026-10-11_writers.txt` and
`notes/development/probe/2026-10-10_writers.txt`, with each writer's own
outputs excluded: a file the writer reads that the key does not name is a cache that can serve stale
bytes, which is the failure mode the exactness check exists to catch.

A trailing `/` in an L1 entry is a tree: it expands to every file under it, sorted. Writers compute
their key inside `main()`, not at import — `catlib/templates.py` imports `render_reports`, whose L1
names the 1,049-file index tree, so a module-level key would make every consumer of the registry pay
that read. `measure_open_probe.py` is deliberately absent: its record carries a wall time per target,
so it is a measurement of a run, not a function of a digest, and a cache would serve stale timings.
"""

from __future__ import annotations

import subprocess
from collections.abc import Callable
from pathlib import Path

from catlib.atomic import RECORDS_ROOT, cache_text, write_atomic
from catlib.paths import ROOT, SCRIPTS
from catlib.records import key as digest_key
from catlib.text import first_group

# The 21 report-fed pages, in the order the registry in `catlib/templates.py` lists them.
REPORT_PAGES = (
    "notes/reports/abstracts.md",
    "notes/development/index-links.md",
    "notes/development/index-design.md",
    "notes/reports/links.md",
    "notes/reports/dependency-drift.md",
    "notes/reports/named-results.md",
    "notes/reports/names.md",
    "notes/reports/proof-density.md",
    "notes/reports/sources.md",
    "notes/reports/verification-dirs.md",
    "notes/reports/scope-exclusions.md",
    "notes/reports/topics.md",
    "notes/reports/t0-chains.md",
    "notes/reports/subfinding-pairs.md",
    "notes/reports/counterexample-crosscheck.md",
    "notes/reports/formalization-faithfulness.md",
    "notes/development/fleet-design.md",
    "notes/development/templates.md",
    "notes/README.md",
    "notes/scripts/README.md",
    "notes/reports/findings.md",
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
    "refresh_summary_line_counts.py": ("notes/tables/catalog.tsv", "notes/reports/counterexample-tag.md",
                                       "notes/reports/sources.md", "notes/reports/t0-triage.md"),
    "build_index.py": ("README.md", "notes/tables/catalog.tsv", "notes/tables/sources.tsv", "notes/tables/topics.tsv",
                       "notes/templates/discipline.md.j2", "notes/templates/family.md.j2",
                       "notes/templates/index-readme.md.j2", "notes/templates/name.md.j2",
                       "notes/templates/topic.md.j2"),
    # The workflow page counts the summaries tree through `catlib.summaries`, so the writer opens
    # every page it counts and the key hashes the tree.
    "render_reports.py": ("README.md", "notes/tables/", "notes/summaries/",
                          "notes/reports/formalization-deps.md", "notes/reports/t0-triage.md",
                          "notes/templates/", "notes/index/",
                          # The fleet page's population scans the fleet's own sources and the two
                          # tracked probe records, so the key must hash them: a key that did not could
                          # serve a page whose site list was measured against a script tree that has
                          # since moved. The top-level `notes/*.md` pages are NOT here — the fleet
                          # population globs their names, it does not open them, and the audit-hook
                          # record names only opens. The `notes/tables/` entry is a tree, not the
                          # eight TSVs the writer used to name: `math-faz.6` moved the 16 generated
                          # tables into that directory, the writer opens all 25, and a tree entry is
                          # the set the audit-hook record names.
                          "notes/scripts/", "notes/development/probe/2026-10-11_writers.txt",
                          "notes/development/probe/2026-10-11_checkers.txt"),
    "build_report_templates.py": REPORT_PAGES,
    # The names measurement is a record producer, not a page writer: its only tracked input is the
    # ledger, which the probe records as the single notes/ path it opens read-only. Its record is the
    # population, so render_reports.py, build_index.py, extract_named_results.py and
    # verify_named_results.py read the store instead of each walking 7,240 .tex files.
    "measure_names.py": ("notes/tables/catalog.tsv",),
    # The seeder reads one page, one source, the 21 summaries pages, and the notes pages those pages
    # declare as sources. `overview.tex` is inside a hashed tree, so the key already covers it; the
    # pair page, the summaries tree and the three cited notes pages are not, so the L1 names them. The
    # probe record `notes/development/probe/2026-10-12_seed_quotes_summaries.txt` justifies this
    # list: it is the first record that names the summaries tree, and the three notes pages appear
    # because a Sources cell can point at a notes page, not only at a manuscript file.
    "seed_quotes.py": ("notes/reports/subfinding-pairs.md", "notes/summaries/", "notes/reports/counterexample-tag.md",
                       "notes/reports/t0-triage.md", "notes/tables/catalog.tsv"),
    # The named-result population is a record producer: its inputs are the ledger and the five hashed
    # trees, plus `measure_names.py`, whose keyed record it reads through `M.measure()`. That record
    # is a function of `measure_names.py`'s source, so the key must hash the source: a key that did
    # not could serve a population whose subject vocabulary came from a measurement that has moved.
    # The probe scope excludes `notes/scripts/`, so the source entry is hashed, not compared.
    "extract_named_results.py": ("notes/tables/catalog.tsv", "notes/scripts/measure_names.py"),
    # The template census reads both template trees, the index tree it counts renders into, and the
    # registry module it reads the page set from. The registry entry is hashed, not compared: the
    # probe's printed scope excludes `notes/scripts/`.
    "measure_templates.py": ("notes/templates/", "notes/index/", "notes/scripts/catlib/templates.py"),
    # The FTS builder reads only the corpus: every `.tex` under `preprints/` and `overview.tex`, both
    # inside the hashed trees. It opens no `notes/` file, so its L1 is empty and the probe scope
    # (which excludes `notes/scripts/`) has nothing to compare.
    "build_index_db.py": (),
    # The gate-row table is a function of the driver's report for the last completed run. The report is
    # untracked scratch under `.qwen/`, so the key hashes its bytes directly; the probe record prints
    # the `notes/` bucket, which cannot name it, so this writer is probe-exempt.
    "measure_gate_rows.py": (".qwen/tmp/reports/gate_run1.txt",),
    # The check()-count probe reads the script tree: the eleven checker sources it loads and the eleven
    # test files it runs, both under `notes/scripts/`. The probe scope excludes that tree, so the entry
    # is hashed, not compared, and the writer is probe-exempt.
    "measure_check_calls.py": ("notes/scripts/",),
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
    # A record producer has no tracked artifact: its bytes land under the keyed store, which the
    # `.qwen/*` rule keeps untracked. The empty tuple is what makes the cache check read it as
    # "no tracked bytes to compare" and the L1 check still prove its inputs.
    "measure_names.py": (),
    "seed_quotes.py": ("notes/tables/quotes.tsv",),
    # The two population producers: report-only scripts whose record is the population, so they have
    # no tracked bytes to compare and the L1 pass is what proves their read surface.
    "extract_named_results.py": (),
    "measure_templates.py": (),
    # The FTS database is untracked by the bead's rule — gitignored, rebuilt by script, never
    # committed — so there are no tracked bytes to compare, and the L1 pass proves its read surface.
    "build_index_db.py": (),
    # The gate-row table is the ninth entry in `catlib.paths.GATE_TSVS`: the per-row wall times of the
    # last completed gate run, landed from the driver's report.
    "measure_gate_rows.py": ("notes/tables/gate-rows.tsv",),
    # The check()-count probe is a record producer: its record is the population the census page's
    # check() sentences quote, and there are no tracked bytes to compare.
    "measure_check_calls.py": (),
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
    # The canonical run is the plain report; `--json` dumps the same population, so a `--json` run
    # does not share the record. The key is the plain run's.
    "measure_names.py": (),
    # The canonical run is the plain report, which lands the TSV; `--tsv` prints the same rows to
    # stdout and `--check-only` measures without writing, so neither shares the plain run's record.
    "seed_quotes.py": (),
    # Report-only producers: the population is the same bytes in every mode, so the record is keyed
    # with no args and a `--check-only` run reads the record the plain run landed.
    "extract_named_results.py": (),
    "measure_templates.py": (),
    # The plain run lands the database; `--check-only` builds in memory and lands nothing, so the
    # canonical key is the plain run's.
    "build_index_db.py": (),
    # The canonical run is the plain run, which lands the TSV; `--check-only` measures the report and
    # lands nothing, so it does not share the plain run's record.
    "measure_gate_rows.py": (),
    # The plain run lands the record; `--check-only` runs the same pytest rows in memory and lands
    # nothing, so the canonical key is the plain run's.
    "measure_check_calls.py": (),
}

# The writers table names one writer the protocol deliberately excludes: `measure_open_probe.py`'s
# record carries a wall time per target, so it is a measurement of a run, not a function of a digest.
NON_CACHED = frozenset({"measure_open_probe.py"})

# The registry covers one writer the page lists as a checker, because its gate row runs first among
# the checkers: `refresh_summary_line_counts.py` rewrites the `Lines` cell of the summaries pages.
PAGE_EXTRA = frozenset({"refresh_summary_line_counts.py"})

# Two writers' L1 cannot be proved against the audit-hook record. `build_report_templates.py` reads
# each page with `git show HEAD:<page>`, a subprocess read the `open` audit event never sees, so the
# record for it carries only the reads its imports perform; its L1 is the page set its own source names.
# `measure_gate_rows.py` reads the gate driver's report under `.qwen/`, outside the `notes/` bucket the
# record prints, so the exactness pass has nothing to compare it with.
PROBE_EXEMPT = frozenset({"build_report_templates.py", "measure_gate_rows.py"})

# The same writer's L1 must be hashed from HEAD, not from the working tree, because that is what it
# reads. Its own output feeds one of the L1 entries: `notes/development/templates.md` tabulates the
# template bytes, so a render after the builder moves that page's bytes and a working-tree key stops
# matching the key the builder used. Hashing the read surface the writer actually reads makes the key
# a function of HEAD.
L1_HEAD = frozenset({"build_report_templates.py"})


def expand(entry: str) -> list[Path]:
    """A repo-relative file, or every file under a repo-relative tree when the entry ends in `/`.

    A tree entry names the source surface the writer reads, so the compiled caches Python writes under
    `__pycache__` are not part of it: they are not UTF-8, they are a function of the source the key
    already hashes, and the audit-hook record does not name them.
    """
    if entry.endswith("/"):
        return sorted(p for p in (ROOT / entry).rglob("*")
                      if p.is_file() and "__pycache__" not in p.parts)
    return [ROOT / entry]


def l1_paths(name: str) -> list[Path]:
    """The writer's declared L1 inputs, expanded, in registry order."""
    return [p for entry in L1[name] for p in expand(entry)]


PROBES = (
          ROOT / "notes" / "development" / "probe" / "2026-10-16_rr_fleet.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_sweep.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_sweep.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_mt_sweep.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_098.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_098.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_196.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_196.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_195.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_195.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_052.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_052.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_050.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_050.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_047.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_047.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_324.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_324.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_088.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_088.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_072.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_072.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_244.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_244.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_243.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_243.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_325.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_325.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_049.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_049.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_254.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_254.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_039.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_039.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_331.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_331.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_042.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_seed_quotes_042.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_mt_templates.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_workflow.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_findings.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_mt_findings.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_census.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_mt_census.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_rr_fold.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-15_mt_fold.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_352.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_351.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_349.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_348.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_347.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_346.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_345.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_344.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_334.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-14_seed_quotes_pages.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_258.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_259.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_156.txt",
          ROOT / "notes" / "development" / "probe" / "2026-10-13_seed_quotes_147.txt",
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


RUN_ARGS: dict[str, Callable[[], tuple[str, ...]]] = {
    # The workflow page renders the ready-queue length, read through a subprocess the `open`
    # audit event never sees and no tree digest covers, so a bead close invalidates the record the
    # way a file change does. The fork head is not read: the page records it as a dated literal,
    # because the commit that lands a measured head moves the head the next measurement names.
    "render_reports.py": lambda: (str(bd_ready_count()),)
}


def git_short(ref: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", ref],
                          check=True, capture_output=True).stdout.decode("utf-8").strip()


def bd_ready_count() -> int:
    """The ready-queue length, read from the tally line bd prints for itself."""
    out = subprocess.run(["bd", "ready"], check=True, capture_output=True).stdout.decode("utf-8")
    return int(first_group(r"Ready: (\d+) issues", out) or 0)


def key_for(name: str, args: tuple[str, ...] = ()) -> str:
    """The builder's cache key: tree digests, the builder's source, its L1 inputs, its args."""
    script = SCRIPTS / name
    if name in L1_HEAD:
        texts = tuple(subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{p.relative_to(ROOT)}"],
                                     check=True, capture_output=True).stdout.decode("utf-8")
                      for p in l1_paths(name))
    else:
        texts = tuple(p.read_text(encoding="utf-8") for p in l1_paths(name))
    fn = RUN_ARGS.get(name)
    extra = () if fn is None else fn()
    return digest_key(script.read_text(encoding="utf-8"), texts, tuple(args) + extra)


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
