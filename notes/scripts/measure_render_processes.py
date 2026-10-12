"""Report-only probe: the cost of each population in a fresh process — the pool's per-process price.

A pool pays the module import in every worker, so the serial per-population cost is not the pool's
per-process cost. This probe runs one population per process and prints the wall each process takes,
so the pool's floor is the max of these, not the sum of the in-process costs. Measured 2026-10-12
after the scan changes: `links` 14.59 s and `topics` 16.40 s fresh, each re-running the `extract_links`
child, which is why those two stay in the parent; the 17 fresh processes sum to 42.96 s.

Promoted from `.qwen/tmp/render_pool_probe.py` on 2026-10-12. Not gated: a per-process wall is a
function of a run, so a twice-run byte diff is a timing artifact, not a proof.
"""
import subprocess
import sys
import time

NAMES = ["named-results", "index-design", "names", "proof-density", "index-links",
         "dependency-drift", "scope-exclusions", "verification-dirs", "t0-chains",
         "subfinding-pairs", "README", "counterexample-crosscheck",
         "formalization-faithfulness", "fleet-design", "templates", "links", "topics"]

code = ("import sys; sys.path.insert(0, 'notes/scripts'); import render_reports as R; "
        "R.population_of(sys.argv[1])")

t0 = time.perf_counter()
for name in NAMES:
    t = time.perf_counter()
    subprocess.run([sys.executable, "-c", code, name], check=True, cwd=".")
    print(f"{name:26s} {time.perf_counter() - t:6.2f}")
print(f"{'sum of fresh processes':26s} {time.perf_counter() - t0:6.2f}")
