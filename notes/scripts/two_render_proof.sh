#!/bin/bash
# Two render_reports.py runs with an md5 snapshot of every generated report page between them.
#
# The proof a template change is a no-op: the two runs must produce byte-identical pages and a
# byte-identical report. The page list is derived from notes/templates/report/*.j2 — the template
# basename minus .j2 IS the page it renders — so the list cannot drift from the writer's own set.
# Reports land under .qwen/tmp/reports/; nothing in the repo is written by this script except the
# pages render_reports.py itself writes.
# Root from git, not from the script's depth: "$(dirname "$0")/../.." is correct only at exactly two
# levels below the root, so the same file run from a staging directory renders the wrong tree.
cd "$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)" || exit 1
R=.qwen/tmp/reports
# Page name == template basename minus .j2 (links.md.j2 renders notes/links.md); md5sum on the .j2
# basenames would fail on files that do not exist.
PAGES=""
for t in notes/templates/report/*.j2; do p="${t##*/}"; PAGES="$PAGES notes/${p%.j2}"; done
echo "pages: $(echo $PAGES | wc -w)"
snap() { md5sum $PAGES > "$1"; }
echo "run 1"; date -u; python3 notes/scripts/render_reports.py > "$R/two_render_1.txt" 2>&1
echo "rc1=$?"; snap "$R/two_render_snap1.md5"
echo "run 2"; date -u; python3 notes/scripts/render_reports.py > "$R/two_render_2.txt" 2>&1
echo "rc2=$?"; snap "$R/two_render_snap2.md5"
echo "=== page md5 diff (empty == byte-identical) ==="
diff "$R/two_render_snap1.md5" "$R/two_render_snap2.md5" && echo "PAGES BYTE-IDENTICAL"
echo "=== report diff ==="
diff "$R/two_render_1.txt" "$R/two_render_2.txt" && echo "REPORTS BYTE-IDENTICAL"
echo "=== git status ==="
git status --short
echo "TWO_RENDER_DONE"
