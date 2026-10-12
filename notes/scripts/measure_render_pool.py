"""Report-only probe: does pooling the in-process populations lower the render wall?

The wall is the extract_links child's wall plus the two populations that need its stdout. This probe
launches the children, pools the 15 child-free populations across processes, then collects links and
topics in the parent and renders the pages, so the wall is measured, not projected. The spawn start
method re-imports this file in each worker, so the work has to sit under the main guard.

Measured 2026-10-12, and the answer was no: pooled 8.39 s against 9.99 s serial, total wall 25.84 s
against 16.983 s unpooled, because pool results never reach the parent's cached `population_of`, so
the jinja render re-computed every population (5.54 s against 0.34 s). The floor is the child.

Promoted from `.qwen/tmp/render_pool_test.py` on 2026-10-12. Not gated: a wall is a function of a run.
"""
import time
from concurrent.futures import ProcessPoolExecutor

import render_reports as R

NAMES = ["named-results", "index-design", "names", "proof-density", "index-links",
         "dependency-drift", "scope-exclusions", "verification-dirs", "t0-chains",
         "subfinding-pairs", "README", "counterexample-crosscheck",
         "formalization-faithfulness", "fleet-design", "templates"]


def work(name: str) -> str:
    """Runs in a worker: the population is a function of the keyed records, so a worker reads them."""
    R.population_of(name)
    return name


def main() -> None:
    t0 = time.perf_counter()
    for name in R.CHILDREN:
        R.launch(name)
    with ProcessPoolExecutor(max_workers=6) as pool:
        list(pool.map(work, NAMES))
    print(f"pooled 15 populations   {time.perf_counter() - t0:6.2f}")
    for name in ("links", "topics"):
        t = time.perf_counter()
        R.population_of(name)
        print(f"{name:22s} {time.perf_counter() - t:6.2f}  wall {time.perf_counter() - t0:6.2f}")
    t = time.perf_counter()
    for fn in R.PAGE_RENDERERS.values():
        fn()
    print(f"{'jinja':22s} {time.perf_counter() - t:6.2f}")
    print(f"{'total wall':22s} {time.perf_counter() - t0:6.2f}")


if __name__ == "__main__":
    main()
