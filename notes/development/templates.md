# Templates — the census of the two trees that render every generated page

Built by `notes/scripts/measure_templates.py` (report-only: it writes nothing, and reads only
template text plus the writer's registry). Lines and bytes are of the template file itself; a slot
is a `{{ ` occurrence counted over the whole file. No `lake`, `lean`, `lake exe cache get`, or
comparator run.

**Headline, with the rule that yields it:** report tree: **19** templates, **7,232** lines, **467,677** bytes, **1,457** slots; index tree: **5** templates, **209** lines, **14,981** bytes, **103** slots; all **24** templates: **7,441** lines, **482,658** bytes, **1,560** slots.

## The report tree

`notes/templates/report/*.j2`, rendered by `notes/scripts/render_reports.py`. Needles is the count
of (phrase, label) pairs the builder can derive from that page's checker source by calling its
`count_phrases` / `size_phrases` with the population the checker exports as `population()`;
`NOT DERIVED` is printed, not omitted, when the checker exposes no such call.

| Template | Lines | Bytes | Slots | Page | Checker | Needles |
|---|---|---|---|---|---|---|
| `README.md.j2` | 769 | 74,065 | 71 | `notes/README.md` | `verify_script_ownership.py` | NOT DERIVED |
| `abstracts.md.j2` | 406 | 32,517 | 42 | `notes/reports/abstracts.md` | `verify_abstracts.py` | 45 |
| `counterexample-crosscheck.md.j2` | 1,089 | 45,859 | 87 | `notes/reports/counterexample-crosscheck.md` | `verify_counterexample_crosscheck.py` | 20 |
| `dependency-drift.md.j2` | 229 | 11,558 | 95 | `notes/reports/dependency-drift.md` | `verify_dependency_drift.py` | NOT DERIVED |
| `fleet-design.md.j2` | 459 | 39,907 | 35 | `notes/development/fleet-design.md` | `verify_fleet_design.py` | 20 |
| `formalization-faithfulness.md.j2` | 265 | 11,818 | 65 | `notes/reports/formalization-faithfulness.md` | `verify_faithfulness.py` | 13 |
| `index-design.md.j2` | 245 | 14,250 | 106 | `notes/development/index-design.md` | `verify_index_design.py` | 82 |
| `index-links.md.j2` | 240 | 14,283 | 86 | `notes/development/index-links.md` | `check_index_links.py` | NOT DERIVED |
| `links.md.j2` | 224 | 12,314 | 110 | `notes/reports/links.md` | `extract_links.py` | NOT DERIVED |
| `named-results.md.j2` | 368 | 25,311 | 83 | `notes/reports/named-results.md` | `verify_named_results.py` | 65 |
| `names.md.j2` | 277 | 13,873 | 130 | `notes/reports/names.md` | `measure_names.py` | NOT DERIVED |
| `proof-density.md.j2` | 122 | 8,661 | 66 | `notes/reports/proof-density.md` | `measure_proof_density.py` | NOT DERIVED |
| `scope-exclusions.md.j2` | 328 | 26,788 | 19 | `notes/reports/scope-exclusions.md` | `verify_scope_exclusions.py` | NOT DERIVED |
| `sources.md.j2` | 156 | 9,400 | 29 | `notes/reports/sources.md` | `verify_sources.py` | 31 |
| `subfinding-pairs.md.j2` | 636 | 26,890 | 165 | `notes/reports/subfinding-pairs.md` | `verify_subfinding_pairs.py` | NOT DERIVED |
| `t0-chains.md.j2` | 569 | 34,078 | 62 | `notes/reports/t0-chains.md` | `verify_t0_chains.py` | 12 |
| `templates.md.j2` | 107 | 5,071 | 45 | `notes/development/templates.md` | `verify_script_ownership.py` | NOT DERIVED |
| `topics.md.j2` | 335 | 23,082 | 117 | `notes/reports/topics.md` | `measure_topics.py` | NOT DERIVED |
| `verification-dirs.md.j2` | 408 | 37,952 | 44 | `notes/reports/verification-dirs.md` | `verify_verification_dirs.py` | 16 |
| **report tree** | **19** | **7,232** | **467,677** | **1,457** | | |

## The index tree

`notes/templates/*.j2`, rendered by `notes/scripts/build_index.py` into `notes/index/`. Renders is
the count of pages on disk that the template produced, read from the tree it writes.

| Template | Lines | Bytes | Slots | Renders |
|---|---|---|---|---|
| `discipline.md.j2` | 12 | 876 | 13 | 17 discipline pages |
| `family.md.j2` | 60 | 3,699 | 28 | 372 family pages |
| `index-readme.md.j2` | 61 | 5,701 | 24 | 1 entry point |
| `name.md.j2` | 62 | 3,586 | 27 | 551 name pages |
| `topic.md.j2` | 14 | 1,119 | 11 | 92 topic pages |
| **index tree** | **5** | **209** | **14,981** | **103** | |

## The slot rule

A slot is a `{{ ` occurrence in the template file, counted over the whole file. Slot expressions
are not required to be unique. The gap between `{{ ... }}` expressions and distinct expressions,
over the **24** committed templates, is
**18** repeat expressions over **5** templates —
`fleet-design.md.j2` (7 repeats); `proof-density.md.j2` (2 repeats); `templates.md.j2` (1 repeat); `index-readme.md.j2` (5 repeats); `name.md.j2` (3 repeats) —
where a table row is emitted from the same label more than once. Each report template also carries
a generated header comment whose closing line holds one literal `{{ }}`, so the header contributes
exactly 1 slot to every report template; the header comment is **4** lines and the index templates
have none.

The builder's report line prints a *label* count, which is a different measure from the `{{ `
occurrences in the file it wrote: **41** writer labels against **42** slots in `abstracts.md.j2`,
the 1-slot difference being the header. Quote a slot count with the rule that yields it.

## What the builder can prove, and what it cannot

`notes/scripts/build_report_templates.py` rewrites `git show HEAD:<page>` by replacing every phrase
the writer's slot dict supplies with a slot, so a template's literal text — quotations, anchors,
fenced blocks, and every number the writer does not compute — is byte-exact from the committed
page. A phrase the page wraps across lines is split at the page's own line breaks only when the
writer supplies it as split labels; a phrase the writer supplies as one string is left literal,
which is why every count on this page is a per-row slot: a report template carries no Jinja loop,
so a census that grows grows the slot set.

Needle coverage is reported, not assumed: **9** of **19** pages have a checker whose needle list the
builder can derive, and the per-page counts are the Needles column of the report-tree table above.
For the other **10** the builder prints `checker needles NOT DERIVED (<checker>) - coverage
unverified`, and those pages are proven by the render diff plus their own checkers.

## Registry

registry: **19** entries at `catlib/templates.py:121` — page → checker, with the writer's
population and slot dict recorded beside it. The registry and the tree are checked against each
other: template-without-page **0**, page-without-template **0**.

## What has not been checked

- The builder's `labels`/`hits`/`slots` lines are its own report; this page quotes the census
  measured from the template files, not the builder's per-build printout.
- No template is executed here: the census is text measurement. Proof that a template renders its
  page is `render_reports.py` run twice with the pages byte-identical, plus each page's own checker.
- The index-tree templates are counted and their output is counted; `build_index.py`'s own report
  (links, canonical counts, stale sweep) is not re-checked here — see `notes/development/index-design.md`.
- Needle coverage for the **10** NOT-DERIVED pages is unverified by the builder, by its own report line.
