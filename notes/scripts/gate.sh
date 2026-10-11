#!/bin/bash
# Gate list: every generator, measurement and checker in notes/scripts/. Prints one line per
# invocation with its exit code, its wall time, and the first 200 bytes of its report; the only
# files it writes are the per-invocation reports and line files under .qwen/tmp/reports/.
#
# The writer block runs serially in the listed order — its order is the dependency chain. The
# read-only block runs in a bounded pool (`GATE_POOL`, default 8 rows) and prints its lines in the
# canonical order of the list, so the report is the same bytes a serial run prints. `GATE_POOL=1`
# runs the whole list serially, which is the baseline the pooled report is diffed against.
# Invoke as: bash notes/scripts/gate.sh  (from anywhere; it cds to the repo root).
cd "$(dirname "$0")/../.." || exit 1
S=notes/scripts
R=.qwen/tmp/reports
N="${GATE_POOL:-8}"
mkdir -p "$R"

# writers, in dependency order; refresh_summary_line_counts.py runs FIRST among the checkers
# because it rewrites the Lines cells of the summary pages and verify_summaries.py flags a stale cell
serial_rows=()
serial_rows+=("build_catalog.py")
serial_rows+=("build_sources.py")
serial_rows+=("build_index.py")
serial_rows+=("extract_links.py")
serial_rows+=("extract_subfindings.py")
serial_rows+=("extract_formalization_deps.py")
serial_rows+=("compare_abstracts.py --tsv")
serial_rows+=("extract_named_results.py")
serial_rows+=("extract_counterexample_crosscheck.py")
serial_rows+=("extract_t0_chains.py")
serial_rows+=("extract_verification_dirs.py")
serial_rows+=("extract_verification_348.py")
serial_rows+=("extract_subfinding_pairs.py")
serial_rows+=("extract_scope_notes.py")
serial_rows+=("extract_citations.py")
serial_rows+=("render_reports.py")
serial_rows+=("refresh_summary_line_counts.py")

# the read-only block: measurement rows, then every checker plain and with --mutant
pool_rows=()
pool_rows+=("triage_t0.py")
pool_rows+=("measure_topics.py --check")
pool_rows+=("measure_index_sizes.py")
pool_rows+=("check_index_links.py")
pool_rows+=("check_index_links.py --mutant")
pool_rows+=("measure_names.py")
pool_rows+=("measure_faithfulness.py")
pool_rows+=("measure_templates.py")
pool_rows+=("dump_template_slots.py")
pool_rows+=("measure_checker_needles.py")
pool_rows+=("measure_proof_density.py --mutant")
for c in verify_summaries verify_abstracts verify_named_results verify_named_conjectures \
         verify_scope_exclusions verify_subfindings verify_subfinding_pairs verify_index_design \
         verify_sources verify_conditional verify_counterexample_crosscheck verify_t0_chains \
         verify_verification_dirs verify_dependency_drift verify_script_ownership \
         verify_findings verify_citations verify_upstream_history verify_fleet_design \
         verify_page_sync verify_faithfulness; do
  pool_rows+=("$c.py")
  pool_rows+=("$c.py --mutant")
done
pool_rows+=("verify_cache_promotion.py")
pool_rows+=("verify_cache_promotion.py --mutant")
pool_rows+=("verify_conjecture_standing.py")
pool_rows+=("verify_conjecture_standing.py --mutant")
pool_rows+=("check_summary_manuscripts.py")
pool_rows+=("locate_summary_quotes.py")

line_of() { echo "$R/gate_$(echo "$1" | tr -c 'A-Za-z0-9' '_').line"; }
row() {
  spec="$1"
  tag="$(echo "$spec" | tr -c 'A-Za-z0-9' '_')"
  read -ra a <<< "$spec"
  t0=$(date +%s%N)
  python3 "$S/${a[0]}" "${a[@]:1}" > "$R/gate_${tag}.txt" 2>&1
  rc=$?
  w=$(( ( $(date +%s%N) - t0 ) / 100000000 ))
  printf 'exit %s :: %s :: %s in %s.%ss\n' "$rc" "$spec" \
    "$(head -c 200 "$R/gate_${tag}.txt" | tr '\n' ' ')" "$((w / 10))" "$((w % 10))" \
    > "$(line_of "$spec")"
}
export S R
export -f line_of row

for spec in "${serial_rows[@]}"; do
  row "$spec"
  cat "$(line_of "$spec")"
done

printf '%s\n' "${pool_rows[@]}" | xargs -P "$N" -I{} bash -c 'row "{}"'
for spec in "${pool_rows[@]}"; do
  cat "$(line_of "$spec")"
done
