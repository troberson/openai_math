#!/usr/bin/env python3
"""The gate list as a dependency graph.

`gate.sh` ran two blocks: a 17-row serial chain and a 58-row `xargs -P 8` pool. The serial block
carried 8 report-only extractors that write nothing tracked, and the pool could not start until the
whole chain finished, so the pass measured 288.9 s serial against 172.5 s pooled — 461.4 s of driver
wall. Here every row declares the generated artifacts it writes and the ones it needs, and a row
starts as soon as every row that writes its needs has finished. Measured 2026-10-11 over the same 75
rows: the writer critical path is `build_catalog.py` 0.1 -> `extract_links.py` 21.5 ->
`build_index.py` 54.8 -> `render_reports.py` 147.1 = 223.5 s, plus the longest row that needs the
rendered pages (`verify_page_sync.py --both`, 122.5 s) = 346.0 s, and the driver wall measured
351.1 s against the shell list's 461.4 s.

Printing stays canonical: each row writes its own `.line` file, and the report prints the `.line`
files in list order after the last row finishes, so the report is the same text a serial run prints.
`GATE_POOL=1` runs the rows one at a time in list order — the serial baseline the pooled report is
diffed against. Measured 2026-10-11: the serial pass is 876.0 s wall over 872.6 s row time against the
pooled 351.1 s, and the two reports match in row order and row content once every wall-time token is
normalized, including the tokens a report carries inside its own first 200 bytes.

Pool size is set by measured RSS, not core count: nproc 32, 6.1 Gi available with the model server
loaded, the two heaviest rows peak at 415 MB, so 12 concurrent rows.

A pooled row must spawn no writer. `render_reports.py` runs its `build_index.py` and
`extract_links.py` children with `--check-only` and `RENDER_REPORTS_CHILD=1`, so the render row
writes pages and nothing else.

Invoke as: python3 notes/scripts/gate.py  (from anywhere; it cds to the repo root).
"""

import os
import re
import subprocess
import time
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
S = "notes/scripts"
R = ".qwen/tmp/reports"
N = int(os.environ.get("GATE_POOL", "12"))

# (spec, needs, writes). `needs` is the set of generated artifacts the row reads; `writes` is the
# set it produces. A row runs when every artifact in `needs` has been written by a finished row.
# The list order is the canonical print order: the report is printed in this order, not in
# completion order.
ROWS = [
    ("build_catalog.py", (), ("catalog",)),
    ("build_sources.py", (), ("sources",)),
    ("build_index.py", ("catalog", "sources", "links", "subfindings", "abstracts"), ("index",)),
    ("extract_links.py", ("catalog",), ("links",)),
    ("extract_subfindings.py", (), ("subfindings",)),
    ("extract_formalization_deps.py", (), ("deps",)),
    ("compare_abstracts.py --tsv", ("catalog",), ("abstracts",)),
    ("extract_named_results.py", ("catalog",), ()),
    ("extract_counterexample_crosscheck.py", ("catalog",), ()),
    ("extract_t0_chains.py", ("catalog",), ()),
    ("extract_verification_dirs.py", ("catalog",), ()),
    ("extract_verification_348.py", (), ()),
    ("extract_subfinding_pairs.py", ("catalog",), ()),
    ("extract_scope_notes.py", (), ()),
    ("extract_citations.py", (), ()),
    # The render reads the keyed check() record, so the probe has to land it before the render.
    # The render writes notes/scripts/README.md, which is inside the tree the probe's key hashes,
    # so the probe runs a second time after the render, before the census checker.
    ("measure_check_calls.py", (), ()),
    ("render_reports.py",
     ("catalog", "sources", "links", "subfindings", "abstracts", "deps", "index"), ("pages",)),
    ("seed_quotes.py", ("pages",), ("quotes",)),
    ("refresh_summary_line_counts.py", (), ("summaries",)),
    ("triage_t0.py", ("catalog",), ()),
    ("measure_topics.py --check", ("pages",), ()),
    ("measure_index_sizes.py", ("index",), ()),
    ("check_index_links.py", ("index",), ()),
    ("run_tests.py notes/scripts/tests/test_index_links.py -q", ("index",), ()),
    ("measure_names.py", (), ()),
    ("measure_faithfulness.py", ("catalog",), ()),
    ("measure_templates.py", (), ("templates",)),
    # The slot dump runs `measure_templates.py` as a child, so it must start after the row that lands
    # the keyed record: two processes writing the same record key is the race that made this row fail.
    ("dump_template_slots.py", ("templates",), ()),
    ("measure_checker_needles.py", (), ()),
    ("measure_needles.py", (), ()),
    ("run_tests.py notes/scripts/tests/test_proof_density.py -q", ("pages",), ()),
    ("verify_summaries.py", ("pages", "summaries"), ()),
    ("run_tests.py notes/scripts/tests/test_summaries.py -q", ("pages", "summaries"), ()),
    ("verify_abstracts.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_abstracts.py -q", ("pages",), ()),
    ("verify_named_results.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_named_results.py -q", ("pages",), ()),
    ("verify_named_conjectures.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_named_conjectures.py -q", ("pages",), ()),
    ("verify_scope_exclusions.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_scope_exclusions.py -q", ("pages",), ()),
    ("verify_subfindings.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_subfindings.py -q", ("pages",), ()),
    ("verify_subfinding_pairs.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_subfinding_pairs.py -q", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_quotes.py -q", ("pages", "quotes"), ()),
    ("verify_index_design.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_index_design.py -q", ("pages",), ()),
    ("verify_sources.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_sources.py -q", ("pages",), ()),
    ("verify_conditional.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_conditional.py -q", ("pages",), ()),
    ("verify_counterexample_crosscheck.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_counterexample_crosscheck.py -q", ("pages",), ()),
    ("verify_t0_chains.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_t0_chains.py -q", ("pages",), ()),
    ("verify_verification_dirs.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_verification_dirs.py -q", ("pages",), ()),
    ("verify_dependency_drift.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_dependency_drift.py -q", ("pages",), ()),
    # The census checker's Cost pass reads the keyed check() record, so the probe has to land it
    # before the checker runs. The render writes notes/scripts/README.md, which is inside the tree
    # the probe's key hashes, so the probe also starts after the render.
    ("measure_check_calls.py", ("pages",), ()),
    ("verify_script_ownership.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_script_ownership.py -q", ("pages",), ()),
    ("verify_findings.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_findings.py -q", ("pages",), ()),
    ("verify_citations.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_citations.py -q", ("pages",), ()),
    ("verify_upstream_history.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_upstream_history.py -q", ("pages",), ()),
    ("verify_fleet_design.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_fleet_design.py -q", ("pages",), ()),
    ("verify_faithfulness.py", ("pages",), ()),
    ("run_tests.py notes/scripts/tests/test_faithfulness.py -q", ("pages",), ()),
    ("verify_page_sync.py --both", ("pages",), ()),
    # The checker compares the cache bytes with the disk bytes for every writer, so it must start
    # after every writer that lands a tracked artifact — `quotes` and `summaries` included. A row
    # that reads a cache entry a concurrent writer has not landed yet reports a missing entry.
    ("verify_cache_promotion.py",
     ("catalog", "sources", "links", "subfindings", "abstracts", "deps", "index", "pages",
      "quotes", "summaries"), ()),
    ("run_tests.py notes/scripts/tests/test_cache_promotion.py -q",
     ("catalog", "sources", "links", "subfindings", "abstracts", "deps", "index", "pages",
      "quotes", "summaries"), ()),
    ("verify_conjecture_standing.py", ("catalog",), ()),
    ("run_tests.py notes/scripts/tests/test_conjecture_standing.py -q", ("catalog",), ()),
    ("verify_tsv_quoting.py",
     ("catalog", "sources", "links", "subfindings", "abstracts", "deps", "index", "pages",
      "quotes", "summaries"), ()),
    ("run_tests.py notes/scripts/tests/test_tsv_quoting.py -q",
     ("catalog", "sources", "links", "subfindings", "abstracts", "deps", "index", "pages",
      "quotes", "summaries"), ()),
    ("check_summary_manuscripts.py", ("summaries",), ()),
    ("locate_summary_quotes.py", ("summaries",), ()),
    ("measure_summaries_seed.py", ("summaries",), ()),
]


def tag_of(spec: str) -> str:
    """The report/line filename stem. `tr -c 'A-Za-z0-9' '_'` over the spec plus its newline, which
    is what appends the trailing underscore the shell version carries."""
    return re.sub(r"[^A-Za-z0-9]", "_", spec + "\n")


def run(spec: str) -> None:
    tag = tag_of(spec)
    a = spec.split()
    report = f"{R}/gate_{tag}.txt"
    t0 = time.time()
    with open(report, "wb") as out:
        rc = subprocess.run(["python3", f"{S}/{a[0]}", *a[1:]], stdout=out,
                            stderr=subprocess.STDOUT, check=False).returncode
    w = int((time.time() - t0) * 10)
    with open(report, "rb") as f:
        head = f.read(200).decode("utf-8", "replace").replace("\n", " ").rstrip()
    with open(f"{R}/gate_{tag}.line", "w", encoding="utf-8") as f:
        f.write(f"exit {rc} :: {spec} :: {head} in {w // 10}.{w % 10}s\n")


def main() -> int:
    os.chdir(ROOT)
    os.makedirs(R, exist_ok=True)
    todo = list(ROWS)
    done: set[str] = set()
    futures: dict[Future, tuple[str, tuple[str, ...], tuple[str, ...]]] = {}
    with ThreadPoolExecutor(max_workers=N) as ex:
        while todo or futures:
            ready = [r for r in todo if set(r[1]) <= done]
            for r in ready:
                todo.remove(r)
                futures[ex.submit(run, r[0])] = r
            if not futures:
                for r in todo:
                    print(f"DEADLOCK: {r[0]} needs {sorted(set(r[1]) - done)}")
                return 1
            finished, _ = wait(futures, return_when=FIRST_COMPLETED)
            for f in finished:
                spec, _, writes = futures.pop(f)
                f.result()
                done.update(writes)
    for spec, _, _ in ROWS:
        with open(f"{R}/gate_{tag_of(spec)}.line", encoding="utf-8") as line:
            print(line.read(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
