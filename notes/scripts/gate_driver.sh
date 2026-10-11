#!/bin/bash
# Gate driver: run the full gate list twice, snapshot every generated artifact by md5, snapshot
# git status, and diff run-vs-run and vs HEAD. Writes only under .qwen/tmp/reports/.
# The run diff normalizes wall-time tokens (`0.53s` -> `Ts`): a row's timing is not a corpus
# measurement, and `measure_checker_needles.py` prints one timing per checker, so a raw run diff
# can never be byte-identical. The md5 and git diffs are raw.
# Launch it detached, one driver at a time, and stop it by process group, never by PID:
#   setsid nohup bash notes/scripts/gate_driver.sh > .qwen/tmp/reports/driver_out.txt 2>&1 < /dev/null &
#   kill -TERM -- -<PGID>
cd "$(dirname "$0")/../.." || exit 1
R=.qwen/tmp/reports
G=notes/scripts/gate.sh
norm() { sed -E 's/[0-9]+\.[0-9]+s/Ts/g' "$1"; }
snap() {
  { md5sum notes/catalog.tsv notes/sources.tsv notes/links.tsv notes/subfindings.tsv \
      notes/abstracts.tsv notes/formalization-deps.tsv notes/conjecture-standing.tsv \
      notes/topics.tsv notes/named-results.tsv 2>/dev/null;
    find notes/index -type f -print0 | xargs -0 md5sum | sort; } | sort -k2
}
bash "$G" > "$R/gate_run1.txt" 2>&1
snap > "$R/gate_md5_run1.txt"
git status --porcelain > "$R/gate_git_run1.txt"
bash "$G" > "$R/gate_run2.txt" 2>&1
snap > "$R/gate_md5_run2.txt"
git status --porcelain > "$R/gate_git_run2.txt"
diff <(norm "$R/gate_run1.txt") <(norm "$R/gate_run2.txt") > "$R/gate_run_diff.txt"
diff "$R/gate_md5_run1.txt" "$R/gate_md5_run2.txt" > "$R/gate_md5_diff.txt"
diff "$R/gate_git_run1.txt" "$R/gate_git_run2.txt" > "$R/gate_git_diff.txt"
git diff --stat HEAD > "$R/gate_head_diff.txt"
echo GATE_DONE
