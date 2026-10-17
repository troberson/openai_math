#!/bin/bash
# The driver bead math-rui.6 asked for: run the gate, land the figures the census page reads, render
# the page, rebuild the templates, and verify promotion — in the order the key moves require.
#
# Why this order. The gate driver prints no wall time, so the gate run is bracketed by two UTC date
# reads. `measure_gate_rows.py` is post-gate, not a gate row: the gate driver truncates its report at
# run start, so the row times exist only after the run finishes.
#
# The probe's key hashes `notes/scripts/`, and the render writes `notes/scripts/README.md` — a file
# inside that tree. So the probe must run before the render, and the render's own write moves the
# probe key, so the pair runs twice: the second render reads the record the probe landed under the
# post-write key, and writes identical bytes, which leaves the key where it is. `converge` is that
# pair. The builder reads pages from HEAD, so it runs only after the page commit; and its own output
# `notes/development/templates.md` is in its L1, so the builder runs again after the template commit.
# The render's L1 names `notes/development/templates.md`, so the render must converge again after
# the builder writes it.
#
# The driver writes nothing tracked except through the writers it invokes. It stops on the first
# non-zero exit and names the step that failed. A step that changes nothing is skipped, so a clean
# tree stays clean.
set -u
cd "$(dirname "$0")/../.." || exit 1
R=.qwen/tmp/reports
mkdir -p "$R"

step() {
  label=$1
  shift
  echo "== $label"
  if ! "$@"; then
    echo "STEP FAILED: $label"
    exit 1
  fi
}

# A step whose non-zero exit is the expected state, not a failure. The first probe runs
# before the render, so the pages it loads are the ones the gate run made stale.
step_soft() {
  label=$1
  shift
  echo "== $label"
  "$@" || echo "== $label: non-zero exit, expected before the render"
}

commit() {
  msg=$1
  shift
  if git diff --quiet HEAD -- "$@"; then
    echo "== commit $*: nothing to commit"
    return 0
  fi
  printf '%s\n' "$msg" > "$R/driver_msg.txt"
  step "commit $*" git commit -F "$R/driver_msg.txt" "$@"
}

converge() {
  step_soft "land check() record (pages are stale, so a -1 row is expected)" \
    python3 notes/scripts/measure_check_calls.py
  step "render (sweep the pages to the fresh gate row TSV)" python3 notes/scripts/render_reports.py
  step "land check() record (the pages the checkers read are now current)" \
    python3 notes/scripts/measure_check_calls.py
  step "render again (the render writes inside the probe L1, so the key moved)" \
    python3 notes/scripts/render_reports.py
}

# The gate runs the census checker, which reads the gate row TSV, and the gate's own run lands a
# new TSV. So the pages the checker reads are stale at gate time and the census row fails. Sweep
# the pages to the TSV the previous run landed, then time the gate.
converge

start=$(date -u +%s.%N)
step "gate (82 rows, timed)" bash notes/scripts/gate_driver.sh
end=$(date -u +%s.%N)
wall=$(python3 -c "print('%.2f' % ($end - $start))")
echo "wall $wall s"
# The wall is the driver's own measurement, landed as a record so the budget checker reads the
# number this run produced, not a log the invoker redirected.
echo "wall $wall s" > "$R/gate_wall.txt"

step "land gate row times" python3 notes/scripts/measure_gate_rows.py
converge

# The census checker is not a gate row: its Cost pass compares the page's Cost cells with the gate
# row TSV, and the gate's own run lands a new TSV, so the page it reads is stale at gate time by
# construction. Here it runs after the render that swept the page to this run's TSV.
step "verify script ownership (post-gate, after the render swept the page)" \
  python3 notes/scripts/verify_script_ownership.py
step "assert the gate ran inside the budget" python3 notes/scripts/check_gate_budget.py

commit "Land the measured figures the gate run produced

The render writes the Cost cells, the self-test row figures, the check() counts, the two sums, the
heaviest-row claim, and the tail figures from the gate row TSV and the keyed check_calls.json record
the driver just landed. The render also sweeps the index-design and fleet pages' all-TSV total and
gate-rows row, which the gate run moved, and the TSV is that run's own record.

" notes/scripts/README.md notes/development/index-design.md notes/development/fleet-design.md notes/tables/gate-rows.tsv

step "rebuild templates from HEAD" python3 notes/scripts/build_report_templates.py

commit "Rebuild the census template from the committed page

The builder reads the page's bytes at HEAD, so a slot exists only for a phrase the writer supplies
and the page carries in the commit.

" notes/templates/report/scripts-README.md.j2 notes/development/templates.md

step "rebuild templates again (templates.md is in the builder's L1)" \
  python3 notes/scripts/build_report_templates.py

converge

step "verify cache promotion" python3 notes/scripts/verify_cache_promotion.py

echo "DRIVER_DONE"
git status --porcelain
