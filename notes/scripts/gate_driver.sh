#!/bin/bash
# Gate driver: run the full gate list once, snapshot every generated artifact by md5, snapshot git
# status, and print the promote-and-verify assertion the gate's own row carries. The twice-run this
# replaces proved determinism by repetition; a writer's bytes are now a pure function of a
# digest-keyed input, landed under the key and then written onto the tracked path, so the assertion
# — cached bytes == promoted bytes for every tracked artifact — is the test, and it cannot produce
# two byte strings. The key is computed from the current `git rev-parse HEAD:<path>` tree digests, so
# a key that no longer matches HEAD makes its records missing and the assertion fails. The md5 and git
# snapshots stay raw. Writes only under .qwen/tmp/reports/.
#
# The post-gate section is what makes the Cost figures on the census page come from this run: the
# driver lands gate-rows.tsv from the report this run printed, the render sweeps the Cost cells from
# it, the swept pages are committed, and the templates are rebuilt from the committed pages (the
# builder reads `git show HEAD:<page>`, so a template can only carry this run's figures after its
# page is committed). The probe runs after the builder, because both write inside the tree the probe's
# key hashes, so the record the census checker reads is landed under the post-render key. The census
# checker is not a gate row: it compares the page against the TSV this run produced, and the gate
# truncates its report at run start, so the row cannot read its own run.
# Launch it detached, one driver at a time, and stop it by process group, never by PID:
#   setsid nohup bash notes/scripts/gate_driver.sh > .qwen/tmp/reports/driver_out.txt 2>&1 < /dev/null &
#   kill -TERM -- -<PGID>
cd "$(dirname "$0")/../.." || exit 1
R=.qwen/tmp/reports
G=notes/scripts/gate.py
snap() {
  { md5sum notes/tables/catalog.tsv notes/tables/sources.tsv notes/tables/links.tsv notes/tables/subfindings.tsv \
      notes/tables/abstracts.tsv notes/tables/formalization-deps.tsv notes/tables/conjecture-standing.tsv \
      notes/tables/topics.tsv;
    find notes/index -type f -print0 | xargs -0 md5sum | sort; } | sort -k2
}
step() {
  local label="$1"
  shift
  echo "== $label"
  "$@"
  local rc=$?
  if [ $rc -ne 0 ]; then
    echo "STEP FAILED: $label (exit $rc)"
    exit $rc
  fi
}
start=$(date -u +%s.%N)
python3 "$G" > "$R/gate_run1.txt" 2>&1
end=$(date -u +%s.%N)
wall=$(python3 -c "print('%.2f' % ($end - $start))")
echo "wall $wall s"
echo "wall $wall s" > "$R/gate_wall.txt"
snap > "$R/gate_md5_run1.txt"
git status --porcelain > "$R/gate_git_run1.txt"
grep -v '^exit 0' "$R/gate_run1.txt" > "$R/gate_failures.txt"
grep 'verify_cache_promotion.py ::' "$R/gate_run1.txt" > "$R/gate_assert.txt"
git diff --stat HEAD > "$R/gate_head_diff.txt"
echo "rows $(wc -l < "$R/gate_run1.txt")  failures $(wc -l < "$R/gate_failures.txt")"
cat "$R/gate_assert.txt"
if [ -s "$R/gate_failures.txt" ]; then
  echo "GATE FAILURES — stopping before the post-gate sweep"
  exit 1
fi
step "land the row times this run printed" python3 notes/scripts/measure_gate_rows.py
step "re-land the check() probe (gate-rows.tsv moved the tree key)" python3 notes/scripts/measure_check_calls.py
step "render the pages from the fresh row times" python3 notes/scripts/render_reports.py
printf '%s\n' "Land the measured figures the gate run produced" "" \
  "The driver lands gate-rows.tsv from the report this run printed and the render sweeps the Cost" \
  "cells from it, so the census page, the fleet page, the index-design page, and the row-times" \
  "table are the writer's bytes for this run, not the previous run's." > "$R/msg_pages.txt"
step "commit the swept pages" git commit -F "$R/msg_pages.txt" notes/scripts/README.md \
  notes/development/fleet-design.md notes/development/index-design.md notes/tables/gate-rows.tsv
step "rebuild the templates from the committed pages" python3 notes/scripts/build_report_templates.py
printf '%s\n' "Rebuild the templates from the committed swept pages" "" \
  "The builder reads git show HEAD:<page>, so the templates carry the Cost cells the render swept" \
  "for this run, and the templates page is the builder's own measurement of the new files." > "$R/msg_templates.txt"
step "commit the templates" git commit -F "$R/msg_templates.txt" notes/templates/report \
  notes/development/templates.md
step "verify script ownership (post-render, so the page is swept)" python3 notes/scripts/verify_script_ownership.py
step "probe the check() calls (post-render, so the key matches)" python3 notes/scripts/measure_check_calls.py
step "build the templates again (the template commit moved templates.md, which is in the builder L1)" python3 notes/scripts/build_report_templates.py
step "verify cache promotion (expect problems 0)" python3 notes/scripts/verify_cache_promotion.py
step "assert the gate ran inside the budget" python3 notes/scripts/check_gate_budget.py
if git status --porcelain .beads/issues.jsonl | grep -q .; then
  printf '%s\n' "Record the gate run in the tracked beads store" "" \
    "The pre-commit hook re-exports the store; a pathspec commit excludes the staged file, so the" \
    "store is committed on its own path to leave the tree clean." > "$R/msg_beads.txt"
  step "commit the beads store" git commit -F "$R/msg_beads.txt" .beads/issues.jsonl
fi
git status --porcelain > "$R/gate_git_after.txt"
echo "clean tree $([ -z "$(cat "$R/gate_git_after.txt")" ] && echo True || echo False)"
cat "$R/gate_git_after.txt"
echo GATE_DONE
