#!/bin/bash
# Wall-clock cost of every checker, plain and with --mutant. Report-only: writes nothing.
#
# The checker list is derived from disk (notes/scripts/verify_*.py), never written out by hand:
# a hardcoded list is what made the first version of this probe drift from the gate's own list.
# Not a gate.sh row — it runs every checker twice, so it costs more than the gate's checker
# section alone; it is the tool that answers "which checker is the gate's cost".
# Root from git, not from the script's depth: "$(dirname "$0")/../.." is correct only at exactly two
# levels below the root.
cd "$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)" || exit 1
for f in notes/scripts/verify_*.py; do
  for mode in "" "--mutant"; do
    start=$(date +%s.%N)
    python3 "$f" $mode > /dev/null 2>&1
    code=$?
    end=$(date +%s.%N)
    printf '%-38s %-9s %6s  exit %s\n' "${f#notes/scripts/}" "${mode:-plain}" \
      "$(printf '%.1f' "$(echo "$end - $start" | bc)")" "$code"
  done
done
echo "COSTS_DONE"
