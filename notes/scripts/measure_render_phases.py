"""Report-only probe: main()'s phase wall with concurrent children — cumulative, in main() call order.

Promoted from `.qwen/tmp/render_phase_probe2.py` on 2026-10-12. Not gated: a phase wall is a function
of a run, so a twice-run byte diff of this report is a timing artifact, not a proof. Run it by hand
before and after a change to `render_reports.py`'s child launch or its population order.
"""
import time

import render_reports as R

t0 = time.perf_counter()
for name in R.CHILDREN:
    R.launch(name)
print(f"launch                {time.perf_counter() - t0:6.2f}")

total = 0.0
for name in ["named-results", "index-design", "names", "proof-density", "index-links",
             "dependency-drift", "scope-exclusions", "verification-dirs", "t0-chains",
             "subfinding-pairs", "README", "counterexample-crosscheck",
             "formalization-faithfulness", "fleet-design", "templates", "links", "topics"]:
    t = time.perf_counter()
    R.population_of(name)
    dt = time.perf_counter() - t
    total += dt
    print(f"{name:26s} {dt:6.2f}  cum {total:6.2f}  wall {time.perf_counter() - t0:6.2f}")

t = time.perf_counter()
for fn in R.PAGE_RENDERERS.values():
    fn()
print(f"{'page renders (jinja)':26s} {time.perf_counter() - t:6.2f}")
print(f"{'total wall':26s} {time.perf_counter() - t0:6.2f}")
