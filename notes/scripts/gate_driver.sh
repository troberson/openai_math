#!/bin/bash
# Gate driver: run the full gate list once, snapshot every generated artifact by md5, snapshot git
# status, and print the promote-and-verify assertion the gate's own row carries. The twice-run this
# replaces proved determinism by repetition; a writer's bytes are now a pure function of a
# digest-keyed input, landed under the key and then written onto the tracked path, so the assertion
# — cached bytes == promoted bytes for every tracked artifact — is the test, and it cannot produce
# two byte strings. The key is computed from the current `git rev-parse HEAD:<path>` tree digests, so
# a key that no longer matches HEAD makes its records missing and the assertion fails. The md5 and git
# snapshots stay raw. Writes only under .qwen/tmp/reports/.
# Launch it detached, one driver at a time, and stop it by process group, never by PID:
#   setsid nohup bash notes/scripts/gate_driver.sh > .qwen/tmp/reports/driver_out.txt 2>&1 < /dev/null &
#   kill -TERM -- -<PGID>
cd "$(dirname "$0")/../.." || exit 1
R=.qwen/tmp/reports
G=notes/scripts/gate.py
snap() {
  { md5sum notes/catalog.tsv notes/sources.tsv notes/links.tsv notes/subfindings.tsv \
      notes/abstracts.tsv notes/formalization-deps.tsv notes/conjecture-standing.tsv \
      notes/topics.tsv notes/named-results.tsv 2>/dev/null;
    find notes/index -type f -print0 | xargs -0 md5sum | sort; } | sort -k2
}
python3 "$G" > "$R/gate_run1.txt" 2>&1
snap > "$R/gate_md5_run1.txt"
git status --porcelain > "$R/gate_git_run1.txt"
grep -v '^exit 0' "$R/gate_run1.txt" > "$R/gate_failures.txt"
grep 'verify_cache_promotion.py ::' "$R/gate_run1.txt" > "$R/gate_assert.txt"
git diff --stat HEAD > "$R/gate_head_diff.txt"
echo "rows $(wc -l < "$R/gate_run1.txt")  failures $(wc -l < "$R/gate_failures.txt")"
cat "$R/gate_assert.txt"
echo GATE_DONE
