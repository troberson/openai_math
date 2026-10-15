"""The report-template registry, the writer's slot dicts, and the checker-needle derivation.

Three scripts key on this machinery: `build_report_templates.py` builds the 17 report templates
from it, `measure_checker_needles.py` prices the needle derivation, and `measure_templates.py`
measures the census `notes/development/templates.md` quotes. It lives here so the three read one
registry,
not three routes to one builder.

The slot set is the writer's, because the writer's slot dict *is* the template's slot set:
`render_reports.py` builds one dict per page and passes it to the template as `p`, and its split
tables are what give the " a"/" b" labels. A template built from any other list — e.g. the
checker's needle list, which is wider — renders slots the writer never supplies, and Jinja renders
an unknown key as the empty string: the page silently loses text. The page's checker needles are
read too, and reported as coverage (slotted / left literal), never as the slot source.

`render_reports.py` is imported at module level: the POPULATIONS and LABELS dicts are built from
the writer's own functions while this module body runs, so a consumer that imports this package
module must be imported by the writer only inside a function — `measure_templates.py`'s
`registry()` is that deferred import, and importing the writer first would build these dicts
against a half-initialised writer.

The template construction (the whitespace-flexible locate, the split at the page's own line
breaks, the raw-block wrapping, the `git show HEAD:<page>` read) stays in
`build_report_templates.py`: it is the writer's path, and the page read is a revision, which the
package does not own.
"""
from __future__ import annotations

import pathlib
import re
from collections.abc import Callable
from typing import Any

import render_reports as R

SPLIT_LABEL = re.compile(r"^(.* [a-j])$")

# The measured population per page, taken from the same call render_reports.py makes when it renders.
# The writer's slot dict is built from it, and the page's checker is handed the same object so its
# needle list is derived, not transcribed.
POPULATIONS: dict[str, Callable[[], Any]] = {
    "notes/reports/sources.md": R.measure,
    "notes/reports/abstracts.md": R.CA.measure,
    "notes/reports/named-results.md": R.en.population,
    "notes/development/index-design.md": R.M.population,
    "notes/reports/names.md": R.names_population,
    "notes/reports/proof-density.md": R.proof_density_population,
    "notes/development/index-links.md": R.index_links_population,
    # Both links pages read the SAME cached population. render_reports.py:3262 builds its topics
    # population from population_of("links"), and population_of is @cache'd, so the links walk is paid
    # once per process. Calling R.links_population() directly here made notes/reports/topics.md re-run the
    # walk notes/reports/links.md had already paid — measured 23.34 s of labels for topics against 19.23 s for
    # links in one builder process.
    "notes/reports/links.md": lambda: R.population_of("links"),
    "notes/reports/dependency-drift.md": R.drift_population,
    "notes/reports/verification-dirs.md": R.verification_dirs_population,
    "notes/reports/scope-exclusions.md": R.scope_exclusions_population,
    # topics.md needs the links labels too: its MSC/keywords figures are measured by extract_links.py
    # and derived in links_full, so its population is links_full over the links population.
    "notes/reports/topics.md": lambda: R.topics_population(R.links_full(R.population_of("links"))),
    "notes/reports/t0-chains.md": R.t0_chains_population,
    # subfinding-pairs.md's population is the pairing report's own, imported from
    # extract_subfinding_pairs.py, plus the reading record parsed back out of the page.
    "notes/reports/subfinding-pairs.md": R.subfinding_pairs_population,
    # notes/README.md is derived from the ledger alone plus the yaml's sources/main_results counts.
    "notes/README.md": R.readme_population,
    # counterexample-crosscheck.md re-runs the crosscheck extractor's own report-only helpers
    # (main_results / scope_note / declaration_statement / carrier) over the ledger population.
    "notes/reports/counterexample-crosscheck.md": R.crosscheck_population,
    # formalization-faithfulness.md's population is measure_faithfulness.py's own report-only
    # measurement, imported by the writer.
    "notes/reports/formalization-faithfulness.md": R.faithfulness_population,
    # fleet-design.md's population is the writer's own scan of the fleet's sources — the atomicity
    # grep, the sync census, the digests, the du sizes, the gate rows, the three site lists, the probe
    # parse. The page's checker measures the same figures with its own reads: a checker that compared
    # the page with the writer's numbers would prove nothing about them.
    "notes/development/fleet-design.md": R.fleet_population,
    # templates.md's census is measure_templates.population(); the page also compares a template's slot
    # count with the writer's label count, so the abstracts label count travels inside the population —
    # the same CA.measure() call abstracts_page() makes.
    "notes/development/templates.md": lambda: R.templates_population(len(R.abstracts_phrases(R.CA.measure()))),
    # notes/scripts/README.md's census is the writer's own tree walk. The page's checker walks the same
    # trees with its own rule, so the two measurements are independent by construction.
    "notes/scripts/README.md": R.ownership_population,
    # findings.md's summary-page and index-link counts move when a summary page is added, so the page's
    # slots are the writer's measurement of the summaries tree, the ledger, and the cached index scan.
    "notes/reports/findings.md": R.findings_population,
}
# The writer's own slot dict per page. These are the calls render_reports.py makes when it renders,
# so the labels and phrase strings the template gets are the writer's by construction.
LABELS: dict[str, Callable[[], dict[str, str]]] = {
    "notes/reports/sources.md": lambda: R.phrases(POPULATIONS["notes/reports/sources.md"]()),
    "notes/reports/abstracts.md": lambda: R.abstracts_phrases(POPULATIONS["notes/reports/abstracts.md"]()),
    "notes/reports/named-results.md": lambda: R.named_results_phrases(POPULATIONS["notes/reports/named-results.md"]()),
    "notes/development/index-design.md": lambda: R.index_phrases(
        POPULATIONS["notes/development/index-design.md"]()),
    "notes/reports/names.md": lambda: R.names_phrases(POPULATIONS["notes/reports/names.md"]()),
    "notes/reports/proof-density.md": lambda: R.proof_density_phrases(POPULATIONS["notes/reports/proof-density.md"]()),
    "notes/development/index-links.md": lambda: R.index_links_phrases(
        POPULATIONS["notes/development/index-links.md"]()),
    # links.md prints the MSC/keywords/bibliography figures formatted (**8,206**, 13,802), while
    # links_full also carries each as an unformatted string for the topics page, which prints them
    # bare (render_reports.py:2412). Requiring a raw label in the links page aborts the build with
    # NOT FOUND, so the links template's label dict drops them: they are the topics page's slots.
    "notes/reports/links.md": lambda: {k: v for k, v in R.links_phrases(POPULATIONS["notes/reports/links.md"]()).items()
                               if not k.startswith("raw_")},
    "notes/reports/dependency-drift.md": lambda: R.drift_phrases(POPULATIONS["notes/reports/dependency-drift.md"]()),
    "notes/reports/verification-dirs.md": lambda: R.verification_dirs_phrases(
        POPULATIONS["notes/reports/verification-dirs.md"]()),
    "notes/reports/scope-exclusions.md": lambda: R.scope_exclusions_phrases(
        POPULATIONS["notes/reports/scope-exclusions.md"]()),
    "notes/reports/topics.md": lambda: R.topics_phrases(POPULATIONS["notes/reports/topics.md"]()),
    "notes/reports/t0-chains.md": lambda: R.t0_chains_phrases(POPULATIONS["notes/reports/t0-chains.md"]()),
    "notes/reports/subfinding-pairs.md": lambda: R.subfinding_pairs_phrases(
        POPULATIONS["notes/reports/subfinding-pairs.md"]()),
    "notes/README.md": lambda: R.readme_phrases(POPULATIONS["notes/README.md"]()),
    "notes/reports/counterexample-crosscheck.md": lambda: R.crosscheck_phrases(
        POPULATIONS["notes/reports/counterexample-crosscheck.md"]()),
    "notes/reports/formalization-faithfulness.md": lambda: R.faithfulness_phrases(
        POPULATIONS["notes/reports/formalization-faithfulness.md"]()),
    "notes/development/fleet-design.md": lambda: R.fleet_phrases(
        POPULATIONS["notes/development/fleet-design.md"]()),
    "notes/development/templates.md": lambda: R.templates_phrases(
        POPULATIONS["notes/development/templates.md"]()),
    "notes/scripts/README.md": lambda: R.ownership_phrases(POPULATIONS["notes/scripts/README.md"]()),
    "notes/reports/findings.md": lambda: R.findings_phrases(POPULATIONS["notes/reports/findings.md"]()),
}
PHRASE_FNS = ("count_phrases", "size_phrases")
ALL_PAGES = {
    "notes/reports/abstracts.md": "verify_abstracts.py",
    "notes/development/index-links.md": "check_index_links.py",
    "notes/development/index-design.md": "verify_index_design.py",
    # links.md has no page checker: its counts come from the gated writer extract_links.py, which
    # prints its report and writes notes/tables/links.tsv and carries no count_phrases/size_phrases, so
    # the builder reports this coverage as NOT DERIVED.
    "notes/reports/links.md": "extract_links.py",
    # dependency-drift.md's checker takes no count_phrases/size_phrases: its needles are inline
    # want() calls inside check(), so the builder reports this coverage as NOT DERIVED.
    "notes/reports/dependency-drift.md": "verify_dependency_drift.py",
    "notes/reports/named-results.md": "verify_named_results.py",
    "notes/reports/names.md": "measure_names.py",
    "notes/reports/proof-density.md": "measure_proof_density.py",
    "notes/reports/sources.md": "verify_sources.py",
    # verification-dirs.md's checker exports population() (its measure()), so the builder derives its
    # needle list from the checker itself; the page is also proven by the render diff plus the
    # checker's own mutants.
    "notes/reports/verification-dirs.md": "verify_verification_dirs.py",
    # scope-exclusions.md's checker has no count_phrases/size_phrases at all: its needles are the
    # inline COUNTS/NONE_LINE regexes plus the measured() table labels, so the builder reports this
    # coverage as NOT DERIVED and the page is proven by the render diff plus the checker's own mutants.
    "notes/reports/scope-exclusions.md": "verify_scope_exclusions.py",
    # topics.md has no page checker: its counts come from the gated report-only measure_topics.py,
    # which prints the report every count on the page comes from and carries no count_phrases/
    # size_phrases, so the builder reports this coverage as NOT DERIVED. The page is proven by the
    # render diff plus measure_topics.py --check, which re-measures all 92 recorded rows.
    "notes/reports/topics.md": "measure_topics.py",
    # t0-chains.md's checker exports population() (its measured()), so the builder derives its needle
    # list from the checker itself; the page is also proven by the render diff plus its own mutants.
    "notes/reports/t0-chains.md": "verify_t0_chains.py",
    # subfinding-pairs.md's checker takes parsed inputs and has no module-level count_phrases, so its
    # needles cannot be derived: the builder reports this coverage as NOT DERIVED and the page is
    # proven by the render diff plus the checker's own 7 mutants, which pin every quoted clause and
    # title to the family's \resultentry line.
    "notes/reports/subfinding-pairs.md": "verify_subfinding_pairs.py",
    # notes/README.md has no page checker at all: it is the ledger's reading guide, and the only
    # script that checks any part of it is verify_script_ownership.py, which verifies the command
    # block and the ownership census rows and carries no count_phrases/size_phrases. The builder
    # therefore reports this coverage as NOT DERIVED, and the page is proven by the twice-render
    # byte-identity diff plus that checker's plain run and its 16 mutants.
    "notes/README.md": "verify_script_ownership.py",
    # counterexample-crosscheck.md's checker exports population() and count_phrases(), so the builder
    # derives its needle list from the checker itself - as it now does for the six other report-fed
    # pages, whose per-page counts are the Needles column of the templates census.
    "notes/reports/counterexample-crosscheck.md": "verify_counterexample_crosscheck.py",
    # formalization-faithfulness.md's checker exports population() and count_phrases(), so the builder
    # derives its needle list from the checker itself, as it does for the crosscheck page.
    "notes/reports/formalization-faithfulness.md": "verify_faithfulness.py",
    # fleet-design.md's checker exports population() and count_phrases(), so the builder derives its
    # needle list from the checker itself. The page's dated observations (the free -h line, the wall
    # times, the cold/warm swing) are deliberately NOT slots: a writer that recomputed them would move
    # the page the day the machine changed, so they stay literal in the template.
    "notes/development/fleet-design.md": "verify_fleet_design.py",
    # templates.md has no page checker of its own: its census comes from the gated report-only
    # measure_templates.py, and the script that checks any part of it is verify_script_ownership.py,
    # which verifies the census rows and carries no count_phrases/size_phrases, so the builder reports
    # this coverage as NOT DERIVED. The page is proven by the twice-render byte-identity diff plus that
    # checker's plain run and its mutants.
    "notes/development/templates.md": "verify_script_ownership.py",
    # notes/scripts/README.md is the script census. Its checker, verify_script_ownership.py, derives the
    # writer set from the scripts' own sources and compares the census count cells with the trees on disk;
    # it carries no count_phrases/size_phrases, so the builder reports this coverage as NOT DERIVED. The
    # page is proven by the render diff plus that checker's plain run and its extracted mutants.
    "notes/scripts/README.md": "verify_script_ownership.py",
    # findings.md is the reading synthesis. Its checker, verify_findings.py, runs seven passes over the
    # page's sources, quotations, ledger rows, tables, report lines, records and closing block; the
    # summary-page and index-link counts are now writer slots, so the render diff is the pass that proves
    # them. The checker carries no count_phrases/size_phrases, so the builder reports NOT DERIVED.
    "notes/reports/findings.md": "verify_findings.py",
}
# The template file name per page. The builder names a template by the page's basename, so the two
# README.md pages collide: notes/README.md owns README.md.j2 and the scripts census takes
# scripts-README.md.j2. The writer's page function reads the same name from here.
TEMPLATE_NAME = {"notes/scripts/README.md": "scripts-README.md.j2"}


def checker_needles(checker: pathlib.Path) -> list[tuple[str, str]]:
    """The page checker's (phrase, label) needles - read for the coverage report, never as slots.

    The checker source is exec'd with the trailing bare `main()` call removed when the module has no
    `if __name__` guard (verify_index_design.py and verify_sources.py run their page check on
    import, which raises SystemExit).
    """
    src = checker.read_text(encoding="utf-8")
    if 'if __name__ == "__main__"' not in src:
        src = src[: src.rindex("\nmain()")]
    ns: dict[str, Any] = {"__name__": "checker_source", "__file__": str(checker)}
    # The needles come from the checker's own source, so the module is loaded by exec.
    exec(compile(src, checker.name, "exec"), ns)  # pylint: disable=exec-used
    out: list[tuple[str, str]] = []
    for fn_name in PHRASE_FNS:
        fn = ns.get(fn_name)
        if callable(fn):
            pop = ns.get("population")
            try:
                out.extend(fn(pop()) if callable(pop) else fn({}))
            except (TypeError, KeyError):
                continue
    return out


def group_labels(labels: dict[str, str]) -> dict[str, list[tuple[str, str]]]:
    """{base label: [(slot label, phrase part), ...]} in the writer's a/b/c order."""
    groups: dict[str, list[tuple[str, str]]] = {}
    for lab, val in labels.items():
        m = SPLIT_LABEL.match(lab)
        base = lab[:-2] if m else lab
        groups.setdefault(base, []).append((lab, val))
    for parts in groups.values():
        parts.sort()
    return groups
