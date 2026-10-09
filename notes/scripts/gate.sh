#!/bin/bash
# Gate list: every generator, measurement and checker in notes/scripts/. Prints one line per
# invocation with its exit code and writes nothing to the repo; the only files it writes are the
# per-invocation reports under .qwen/tmp/reports/. Run it twice: the two reports must be identical.
# Invoke as: bash notes/scripts/gate.sh  (from anywhere; it cds to the repo root).
cd "$(dirname "$0")/../.." || exit 1
S=notes/scripts
run() {
  name="$1"; shift
  tag="$(echo "$name $*" | tr -c 'A-Za-z0-9' '_')"
  out=".qwen/tmp/reports/gate_${tag}.txt"
  python3 "$S/$name" "$@" > "$out" 2>&1
  echo "exit $? :: $name $* :: $(head -c 200 "$out" | tr '\n' ' ')"
}
# generators (must be byte-identical across runs)
run build_catalog.py
run build_sources.py
run build_index.py
run extract_links.py
run extract_subfindings.py
run extract_formalization_deps.py
run compare_abstracts.py --tsv
run extract_named_results.py
run extract_counterexample_crosscheck.py
run extract_t0_chains.py
run extract_verification_dirs.py
run extract_verification_348.py
run extract_subfinding_pairs.py
run extract_scope_notes.py
run extract_citations.py
run render_reports.py
# measurement
run triage_t0.py
run measure_topics.py --check
run measure_index_sizes.py
run check_index_links.py
run measure_names.py
run measure_proof_density.py --mutant
# checkers: plain then mutant
# refresh_summary_line_counts.py runs FIRST: it rewrites the Lines cells of the summary pages and
# verify_summaries.py flags a stale cell, so the checker must run after the refresh.
run refresh_summary_line_counts.py
for c in verify_summaries verify_abstracts verify_named_results verify_named_conjectures \
         verify_scope_exclusions verify_subfindings verify_subfinding_pairs verify_index_design \
         verify_sources verify_conditional verify_counterexample_crosscheck verify_t0_chains \
         verify_verification_dirs verify_dependency_drift verify_script_ownership \
         verify_findings verify_citations verify_upstream_history; do
  run "$c.py"
  run "$c.py" --mutant
done
run verify_conjecture_standing.py
run verify_conjecture_standing.py --mutant
run check_summary_manuscripts.py
run locate_summary_quotes.py
