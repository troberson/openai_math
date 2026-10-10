# Proof triage notes

Working ledger for categorizing the catalog's proofs by **what a result claims** and **what
kind of evidence ships with it**. This is a reading tool, not a verification tool.

Regenerate the ledger (a few seconds, no Lean):

```sh
python3 notes/scripts/build_catalog.py      # writes notes/catalog.tsv and prints the report
python3 notes/scripts/triage_t0.py          # buckets the 130 T0 families by claim shape
python3 notes/scripts/verify_summaries.py   # checks every citation in notes/summaries/ against the files it names
python3 notes/scripts/verify_summaries.py --mutant  # same, plus the injected-fault self-test
python3 notes/scripts/check_summary_manuscripts.py  # which manuscripts each summaries page reads, and whether the release still names them; report-only
python3 notes/scripts/locate_summary_quotes.py <page.md> [page.md ...]  # where a quotation's text actually sits, when verify_summaries.py reports a miss; report-only
python3 notes/scripts/refresh_summary_line_counts.py  # rewrites the Lines column of the Sources table in every summaries page
python3 notes/scripts/read_manuscript.py <preprints-dir>  # prints a manuscript's abstract, section skeleton and titled statement environments with file:line anchors (--limit N, --all, --sections-only)
python3 notes/scripts/verify_conjecture_standing.py  # checks notes/conjecture-standing.tsv against the ledger and overview.tex
python3 notes/scripts/extract_formalization_deps.py  # writes notes/formalization-deps.tsv and prints the reconciliation
python3 notes/scripts/verify_dependency_drift.py --mutant  # checks notes/dependency-drift.md: anchors, blockquotes, code spans, the patch table, every count
python3 notes/scripts/extract_links.py      # writes notes/links.tsv and prints the per-edge report
python3 notes/scripts/extract_scope_notes.py  # re-measures the 242 `## Scope` sections; report-only, writes nothing
python3 notes/scripts/verify_scope_exclusions.py --mutant  # checks notes/scope-exclusions.md against lean/docs/
python3 notes/scripts/extract_subfindings.py  # writes notes/subfindings.tsv and prints the reconciliation
python3 notes/scripts/verify_subfindings.py --mutant  # checks notes/subfindings.tsv against overview.tex and lean/docs/
python3 notes/scripts/extract_subfinding_pairs.py  # lays out the pairing population; report-only, writes nothing
python3 notes/scripts/verify_subfinding_pairs.py --mutant  # checks notes/subfinding-pairs.md against overview.tex
python3 notes/scripts/verify_conditional.py --mutant  # checks notes/conditional.md against the Lean source it cites
python3 notes/scripts/extract_verification_348.py  # measures the two family-348 verification bundles; report-only, writes nothing
python3 notes/scripts/extract_verification_dirs.py  # the 30 bundles, each one's own entry point, and the README sections that name them; report-only
python3 notes/scripts/verify_verification_dirs.py --mutant  # checks both sections of notes/verification-dirs.md against the bundle files
python3 notes/scripts/measure_index_sizes.py  # the population behind notes/index-design.md, the rendered tables' row counts, and the disk link check; report-only
python3 notes/scripts/verify_index_design.py --mutant  # checks notes/index-design.md: anchors, every count (schema rows read from notes/index/*.tsv), the five tabulated byte sizes
python3 notes/scripts/build_report_templates.py  # rebuilds all fourteen report templates from each committed page and the slot dict its writer supplies (2 args = one page); writes notes/templates/report/<page>.j2
python3 notes/scripts/render_reports.py       # writes notes/sources.md, notes/abstracts.md, notes/named-results.md, notes/index-design.md, notes/names.md, notes/proof-density.md, notes/index-links.md, notes/links.md, notes/dependency-drift.md, notes/verification-dirs.md, notes/scope-exclusions.md, notes/topics.md, notes/t0-chains.md and notes/subfinding-pairs.md from notes/templates/report/; run twice, byte-identical
python3 notes/scripts/build_sources.py      # writes notes/sources.tsv (the LaTeX surface of all 719 manuscripts) and prints the reconciliation
python3 notes/scripts/verify_sources.py --mutant  # checks notes/sources.md against preprints/: every count, every anchor, every directory name
python3 notes/scripts/measure_topics.py     # measures notes/topics.tsv over the four text layers; report-only, writes nothing
python3 notes/scripts/measure_topics.py --check  # re-measures all 92 rows and exits 1 when a recorded count has drifted
python3 notes/scripts/measure_names.py      # the six name layers behind notes/names.md; report-only, writes nothing
python3 notes/scripts/measure_names.py --json  # dumps the 5,842 measured rows plus metadata as JSON
python3 notes/scripts/build_index.py        # writes notes/index/ (1,033 pages + 16 tables) and prints the reconciliation
python3 notes/scripts/check_index_links.py  # checks every link in notes/index/ and CONTENTS.md against the shipped files; report-only
python3 notes/scripts/check_index_links.py --mutant  # self-test: 20 injected broken hrefs (one per category) must all be caught, 7 real hrefs must resolve
python3 notes/scripts/compare_abstracts.py  # compares each manuscript abstract with its family's overview abstract; report-only
python3 notes/scripts/compare_abstracts.py --tsv  # writes notes/abstracts.tsv (372 rows: best-match ratio, relation, both shape sets)
python3 notes/scripts/compare_abstracts.py --mutant  # self-test: 7 injected corruptions must all be caught, 3 controls and 5 synthetic cases must stay right
python3 notes/scripts/verify_abstracts.py --mutant  # checks notes/abstracts.md: every [S#] marker resolves, every quotation is verbatim in the file it names
python3 notes/scripts/measure_proof_density.py  # tests proofs-per-family against tiers and claim shapes; report-only, writes nothing
python3 notes/scripts/measure_proof_density.py --mutant  # self-test: 8 injected corruptions must all be caught, plus a 5-case check of the statistic itself
python3 notes/scripts/extract_counterexample_crosscheck.py  # pairs the 28 counterexample families outside T0 with their main_results declarations and carriers; report-only
python3 notes/scripts/verify_counterexample_crosscheck.py --mutant  # checks notes/counterexample-crosscheck.md: anchors, fenced blocks, quotations, three tables, all 19 counts
python3 notes/scripts/extract_t0_chains.py  # the 2 release-recorded cross-family edges, the 311 literature chain, and the 27 two-manuscript second-pass T0 families; report-only
python3 notes/scripts/verify_t0_chains.py --mutant  # checks notes/t0-chains.md: anchors, fenced blocks, quotations, two tables, 27 blocks with 54 titles and paths, all 12 counts and 4 named lists
python3 notes/scripts/extract_named_results.py  # the headline-statement inventory the manuscript sources carry, cross-tabbed against resolves_named; report-only, writes nothing
python3 notes/scripts/verify_named_results.py --mutant  # checks notes/named-results.md: 61 anchors, 15 bare overview anchors, the 17-row target table, 61 quotations, all 66 counts
python3 notes/scripts/extract_citations.py  # the shared-bibliography graph over the .bib files under preprints/; report-only, writes nothing
python3 notes/scripts/verify_citations.py --mutant  # checks notes/citations.md: work-table rows, anchors, fenced blocks, quotations, every count, against the .bib entries it names
python3 notes/scripts/verify_findings.py --mutant  # checks notes/findings.md: every [Sn:line] marker, every quotation, every quoted count, against the reports it cites
python3 notes/scripts/verify_named_conjectures.py --mutant  # checks notes/named-conjectures.md: statement anchors, quotations, prose citations, the entry set, every Measurements number
python3 notes/scripts/verify_upstream_history.py  # re-derives the 3014888 merge census from git and the ledger, then checks the three upstream_history/ pages: anchors, quotations, links, fenced blocks, the 14 backticked preprints/ slugs, two tables, every count phrase; report-only, writes nothing
python3 notes/scripts/verify_upstream_history.py --mutant  # self-test: 13 injected faults (dead anchor, paraphrase, shifted anchor, dead path/link, renamed slug, altered counts) must all be caught
python3 notes/scripts/verify_script_ownership.py  # checks notes/scripts/README.md: the derived writer set, the file census, naming coverage, shared basenames; report-only, writes nothing
python3 notes/scripts/verify_script_ownership.py --mutant  # self-test: 11 injected faults (one per check form) must each be caught by the check it targets
```

`notes/summaries-workflow.md` is the resume protocol for the summary-page batches: per-page steps,
the batch-boundary gates, stop and escalate rules, and the append-only decision-point record.

## Standing rules

1. **No Lean execution.** `lake`, `lean`, and `comparator` are not run for these notes — a full
   build of the 26,060,031-line `OAI/` library is hours on a desktop. Everything here comes from
   static reading of the text metadata that ships in the repo.
2. **Source-level facts stay labeled source-level.** A ledger column records what a file says,
   not what has been checked. `formalization.yaml` states `review: status: unchecked` and
   `automation: methods: [agent]`; that ceiling applies to every coverage number below.
3. **Absence of formalization is not a red flag.** 547 of 719 manuscripts have no formalized
   main result; in a collection that size, "not formalized" carries almost no signal about
   correctness.
4. **Coverage is four layers, never one percentage.** Report them separately.

## The four coverage layers (they do not agree)

| Layer | Source | Count |
|---|---|---|
| Manuscripts with a formalized main result | `formalization.yaml` → `sources:` | 172 / 719 |
| Families with a scope note | `lean/docs/<NNN>.md` | 242 / 372 |
| Statement/solution pairs | `lean/ComparatorChallenges/*.json` | 416 |
| Catalogued main results | `formalization.yaml` → `status.main_results` | 200 entries / 189 unique configs |

Measured agreement worth knowing: **the manuscript layer and the main-results layer nearly agree at
family level, and the gap is one family.** 135 families have ≥1 formalized manuscript and 136 have
≥1 config listed in `main_results`; the difference is family **342**, which has a `main_results`
entry and no manuscript the overview lists. The yaml's own `sources:` list carries 173 paths, one of
them (`Taming-implies-compatibility-on-four-manifolds-September-23-2026`) named by no family. The
106 families at T2 have a scope note and comparator links, and zero formalized manuscripts.

## Tiers (`tier` column)

Assigned from the scope note's comparator links (`../ComparatorChallenges/X.lean`) crossed with
`status.main_results`:

| Tier | Meaning | Families |
|---|---|---|
| T3 | ≥1 linked config listed in `main_results` | 136 |
| T2 | linked configs exist, none listed in `main_results` (companion/secondary statements) | 106 |
| T1 | scope note with no comparator link | 0 |
| T0 | no scope note, no challenge, no main result | 130 |

T1 is empty in this catalog: every one of the 242 scope notes links at least one challenge file.
T2 is not a failure — those challenges are companion statements, still linked from a family note.
**All 130 T0 families have zero formalized manuscripts**, so T0 is triaged by claim shape: see
`notes/t0-triage.md`, where two reading passes cover all 130 families at abstract level
(44 families / 134 manuscripts in the first pass, then 93 families / 121 manuscripts in the second —
the read-set counts of the 2026-10-06 run, recorded there and not re-derived). `resolves_named` is a
second discriminator there — 86 of the 130 are flagged, including 11 of the 19 families with no shape
tag at all.

## Claim shapes (`shapes` column)

Multi-label tags matched against the family abstract in `overview.tex`. **Not a partition** —
66 families match ≥3 shapes and 57 match none, so `shapes` is a pipe-joined list, not a class.

**The tagged text is the overview abstract, which is a paraphrase of the manuscripts, not their
text.** Over all 719 manuscript comparisons: 0 identical, 0 abridged, 719 divergent; over the 372
family best matches: 0 identical, 0 abridged, 372 divergent (median ratio 0.236). 283 of 372
families disagree with their overview on at least one shape; 89 have none. The overview under-flags
every shape except `resolution`, which it over-flags (144 of 372 families vs 153 of 719 manuscripts).
Read
**`notes/abstracts.md`** before treating a shape tag as a claim about a manuscript; the per-family
record is `notes/abstracts.tsv`.

| Shape | Pattern gist | Families |
|---|---|---|
| uniform | "uniformly", "for every", "arbitrary" | 161 |
| resolution | resolves / proves the conjecture / answers the question / settles | 144 |
| bound | bound, sharp, power-saving, improvement, inequality | 139 |
| counterexample | counterexample, disprove, refute, fails, violation | 44 |
| partial | at most, restricted, in coranks, for fixed, unramified part | 42 |
| classification | if and only if, classified, characterization | 34 |
| density | density | 20 |
| conditional | assuming, we assume, under the … hypothesis, provided that | 5 |
| undecidability | no algorithm, undecidable, unsolvable, negative answer | 4 |

`conditional` families: **014, 125, 240, 244, 282.** The regex only flags them; what each one
actually assumes is read by hand and recorded in **`notes/conditional.md`**, which also lists the
five flags that reading removed. Read that file before calling a family conditional.

Reading the Lean source for the 3 T3 families (2026-10-07) narrows what "the assumption is inside
the formalization" buys. The hypothesis sits in the declaration `main_results` names for **240**
only; **125**'s linked declaration is the unconditional `(2 - σ)` recovery claim and its proved
`P ≠ NP`-conditional threshold theorem lives in a sibling tree the yaml does not link; **244**'s
linked declaration assumes a countable transitive ZFC ground model with an internal strongly
inaccessible cardinal, which is strictly more than the `Con(ZF)` its abstract states. So the claim
is about the **tree**, not the linked declaration, and the family→config join (by title, not by
number) is where the two diverge. `lean/ComparatorChallenges/*.lean` are challenge **stubs**, not
proofs — 416 files carrying 539 `sorry` occurrences, 415 of them at least one, the zero-`sorry`
exception being `HarmonicGrowth.lean` — while **zero** of the 122,458 files under
`lean/OAI/**/*.lean` contain `sorry`. A comparator file states the target the release set itself;
reading it and concluding "the hypothesis is in the formalized statement" is reading the stub.

Tags omit as well as mislabel. Measured 2026-10-06 while reading the T0 abstracts, and written down as
a rule on 2026-10-07: **74 of 372** families use counterexample language in title or abstract and only
**44** carry the `counterexample` tag; all 30 untagged flags are genuine counterexamples in kind.
Treat every shape count in the table as a floor, not a census. The rule, the 30-family reading, and
the three false positives it excludes (348, 339, 355) are in **`notes/counterexample-tag.md`** — the
2026-10-06 counts were a reading result whose regex was never recorded, and no variant of the
vocabulary quoted in this file reproduces them.

**`counterex_broad` is a column, not a shape.** The phrase rule flags 74 families from title +
abstract, so it is carried in its own column and the `counterexample` shape stays at 44. Widening the
shape instead would move 30 families (6 of them in T0) between the first-match buckets in
`triage_t0.py`; measured, **0 of the 30 flag-only families sit in bucket C**, so first match hides
every one of them. Unlike `resolves_named`, this column is a **strict superset** of its tag (tag-only
0), so 44 and 74 are directly comparable floors. Method, the per-family verdicts, and the decision are
in **`notes/counterexample-tag.md`**.

**The counterexample families outside T0 are cross-checked claim by claim.** Population rule:
`counterexample` in `shapes` **and** `tier != T0` — **28** families, **19 at T3 and 9 at T2**. The 28
families carry **28** `main_results` declarations; all 28 resolve, **11** are written against a
carrier `def … : Prop :=` and all 11 carriers resolve through the declaration file's import closure.
The 9 T2 families carry **none**, which is the tier's structural absence rather than a per-family
finding. Of the **52** configs their scope notes link, **24** have no entry: **12** in **8** T3
families, **12** across all **9** T2 families. Pairing a claim with a declaration is a reading step, not
a join — see the traps below. Verdicts for all 28, each resting on a verbatim carrier or statement
quote at its `file:line`, are in **`notes/counterexample-crosscheck.md`**, which also records the bead
prose's "21 T0 counterexample-shaped families" beside the shape rule's **16** without resolving the
gap between them.

**The release records 2 cross-family links, not a graph.** The ledger's `companions` column parses
`result (NNN)` clauses inside the overview abstract, and over 372 families that yields **2** edges:
001 → 032 and 002 → 006. The `companion_word` column (`\bcompanion` in the same abstract) fires on
**9** families and **0** of them carry an edge, so the word gestures at a companion without recording
one. All five families in the three bead-named chains sit at T0 with every coverage column at zero, so
"only as strong as its weakest unformalized link" reads here as *every* link; the third chain,
311 ⇒ Hovey–Strickland, is a literature chain and has no corpus edge at all. The 28 two-manuscript
second-pass families — population rule, per-family pairing judgement, and the intra-family citation
layer measuring **16** of 28 citing their sibling (**9** mutual, **7** one-way, **12** citing none,
**3** of those shipping no `.bib` file at all) — are in **`notes/t0-chains.md`**.

**`resolves_named` is a column, not a shape.** The broad named-target rule (a target noun
*conjecture/question/problem* plus a resolution verb, read over the overview **title and abstract**
lowered together) flags 248 families, so it is carried in its own
column and the `resolution` shape stays at 144. Widening the shape instead would move families out of
the counterexample/bound/classification/undecidability/density buckets in `triage_t0.py`, which
assigns by first match. The two signals are complementary, not nested: 139 families are flagged by
both, 109 only by the column, and 5 only by the tag (003, 010, 082, 103, 261 — targets named as a
*hypothesis/case/estimate/contrast*), for a union of 253. Both are floors. Method, the 94-family
reading verdict (the column-only set as it stood under the abstract-only scope; the set is 109 now
and the extra 15 are corroborated at the manuscript-abstract layer, not read), and the decision are in
**`notes/resolution-tag.md`**.

**The manuscript statements are not where the release names its conjectures.** That is the finding of
**`notes/named-results.md`**, the check that turns the column from a title heuristic into an
evidence-backed one. Over the 7,679 manuscript `.tex` files the headline statements
(`theorem`/`maintheorem`/`thm`) read **2,410** begins, **1,609** of them titled, and **17** of those
titles name a target noun — 17 statements over 17 families, 16 with `rn = 1`. **Zero of the 17 pair a
target noun with a resolve verb in the same title**, and **76 of the 248** flagged families ship no
titled headline theorem at all, so statement captions carry almost none of the signal. Naming sits in
the manuscript's **name** (76 families), its **own abstract** (275), its **prose** (337 under a
±80-character window), and in the overview **title** — which supplies **15** families the
abstract-only rule misses. **The swap is applied: the column is the title ∪ abstract union at 248,
removals 0** (the abstract-only scope it replaced read 233); a strict title+abstract *replacement*
reads 149 (99 removals) and is rejected. `notes/scripts/extract_named_results.py` prints every count
(report-only) and `notes/scripts/verify_named_results.py --mutant` checks the page (12/12 mutants
caught).

**Proof density was tested as a signal and rejected — no column.** `notes/sources.tsv` counts
**20,341** `\begin{proof}` over 719 manuscripts, so proofs-per-family is one command away, and it was
measured against the tiers and the shapes with the decision bar written into the script header before
the data was read (AUC ≥ 0.65 **and** p < 0.01, plus a tex-KB size control at the matching scale —
tex KB per family for the per-family signals, tex KB per manuscript for proofs per manuscript). Raw
proof and statement counts clear the bar on **both** T0 pairs (0.667 / 0.674 and 0.671 / 0.676) and sit
within 0.03 of the per-family control (0.658 / 0.677); proofs per manuscript clears T0 > T2 (0.709) and
T0 > T3 (0.770) and is size-explained on both (control 0.705 / 0.769); the two genuine density measures
separate nothing — 0.485 / 0.458 / 0.474 per statement and 0.502 / 0.467 / 0.472 per KB, the
proof-to-statement ratio being ≈0.97 corpus-wide, tier-independent. No claim shape clears the bar; the
largest effects are the n=5 and n=4 groups. The strongest result in the measurement is **inverse**:
`counterex_broad` families have markedly *fewer* proofs per manuscript (0.356, p 1.22e-04). Direction
runs opposite the naive reading — the least-formalized tier (T0) carries the most proofs per manuscript
because its manuscripts are the physically largest (median 168.2 KB vs 89.0 in T3). The null, the
pre-registered rule, and what was not checked are in **`notes/proof-density.md`**;
`notes/scripts/measure_proof_density.py` re-measures it (report-only, writes nothing; gates 0
problems, statistic self-test 5/5, injected mutants caught 8/8).

**`notes/conjecture-standing.tsv` records a prior, not a fact.** The 139 families flagged by both
`resolves_named` and the `resolution` shape each get a row: the conjecture as the abstract names it,
what the assistant's training data says about its standing as of early 2025, a self-reported
`prior_confidence` (high 42 / medium 84 / low 13), the release's claim, the gap between the two, a
surprise tier (1 not-yet-possible 60, 2 famous-unachieved 64, 3 prior deflates the headline 11, 4 the
prior cannot judge 4), and the `overview.tex` line the row reads. The column is named
`standing_prior_2025` because the number is the prior's account, never the conjecture's status: no
literature was consulted and no manuscript was read. 11 rows are tier-3 deflations — the prior already
holds 174, 175, 184, 188, 204 as theorems — and **145** is the one row where the prior's record
published counterexamples to what the abstract proves. Scheme, counts, and what the table cannot say
are in **`notes/conjecture-standing.md`**; `notes/scripts/verify_conjecture_standing.py` proves every
anchor and rejects any row that asserts consequence.

**`notes/formalization-deps.tsv` is the upstream library graph: 31 rows, 8 fields.** 30 libraries are
declared in `lean/lakefile.lean`, each pinned to a 40-char commit and matched by a
`formalization.yaml` entry; **BernoulliRegular** is the 31st, imported by
`lean/OAI/NumberTheory/Ostmann/Quadratic/QuadraticGaussSign.lean:2` and declared in neither layer, so
it is the one library in the release with no pin of its own — the AINTLIB patch shows it ships inside
the AINTLIB repo as `projects/FltRegularBernoulli/BernoulliRegular/`. Only 11 of the 30 declared
libraries have any direct import, and mathlib carries 56,416 of the 56,702 external import statements.
Two claims the release states do not hold as written: `formalization.yaml` says its list is "ordered
by direct import count" and violates that at 5 positions, and 19 declared libraries import nothing
directly. Import counts are **direct statements only**, over `lean/OAI/**/*.lean` — quote the scope
with the number,
since the whole tree yields OAI 278,523 / Mathlib 56,944. Rules, the `.git` join trap, the manifest
reconciliation (42 packages = 30 declared + 12 transitive, revs matching every pin), and what was not
checked are in **`notes/formalization-deps.md`**.

**`notes/dependency-drift.md` is what that record implies about automated formalization**, written
from three sources only: the deps table, `lean/lakefile.lean` (335 lines), and `lean/patches/`. Its
load-bearing numbers, each with the rule that yields it: **23** patches carrying **160,187** lines in
**734** `diff --git` hunks, **22 of 23** rewriting the dependency's `lean-toolchain` and migrating
**8** distinct versions onto `v4.34.1`; **7** declared libraries with no patch; the pre-resolution
array (**11** libraries, 6,658 lines) being exactly the 11 `lana-agents` URLs and disjoint from the
12-library `post_update` array (153,529 lines), their union being exactly the 23 patched libraries;
**19 of 30** declared libraries with `direct_imports = 0`, **14** of them patched; median patch lines
**2,575** for libraries with any direct import versus **408** for libraries with none. The yaml
ordering claim is reported as a claim with its **5** violations, and transitive imports are marked
unmeasurable without `lake` rather than estimated. **No build was attempted** — pins are declared pins
and patches are asserted-applicable, not verified. `notes/scripts/verify_dependency_drift.py --mutant`
re-checks all 52 anchors, 7 blockquotes, 9 code spans, the 23-row patch table, and every count.

**`notes/links.tsv` is the typed-edge inventory: 22 rows, 7 fields**, every count computed by one
command in 20 seconds. It is the input the index-schema decision needs, so the rows are edge *types*,
not a link list. Three of its numbers reconcile against the ledger and must be quoted with the rule
that yields them: scope notes contain **426** comparator-statement link **occurrences** over **416**
distinct configs (the 10-gap is one config linked twice inside each of 7 docs — `071, 100, 115, 134,
274, 275, 293` — and **0** configs are shared between families, so the ledger's deduped `chal` column
is correctly 416); `formalization.yaml` carries **200** `main_results` entries over **189** unique
configs in **136** families, which is what `mainres` sums to. The bead spec's "168 families with
`mainres>0`" is **not reproduced**; the measured figure is 136.

Two findings in it are load-bearing. **The `main_results` set is one family wider than the formalized
set** — 136 families carry a declaration, 135 carry a formalized manuscript, and the difference is
family **342** alone (0 in the other direction) — so declaring a main result and formalizing a
manuscript are one signal plus one family, not two, and a coverage answer quoting both is quoting one.
And the real manuscript→manuscript layer is the **href, not the title**: **393** release-labelled
`.bib` entries resolve to **391** edges over **156 of 372** families, **104** crossing a family
boundary, plus 211 body hrefs. The title-phrase proxy that the repo previously used reaches 12
cross-family families, so it systematically misses citations; the "only 14 of 372 family titles appear
in the `.bib` files" figure **is** reproduced — by a 6-token lowercased title prefix over the 417 `.bib`
files at glob depth ≤3, counting own-family bibliographies — and the extractor prints it as a report
line, but its scope is 417 of 500 files and it has no ownership test, so it is not the same measurement
as the 12.
The edges are **untyped** —
the release records no builds-on / contrasts-with relation — so an edge is a citation choice, not
consequence. Negatives are rows too: **0** MSC codes over 8,206 files, **0** `keywords` fields in
12,876 bibliography entries, `\keywords` in **12** of 719 manuscript directories, **2** companion
edges (`001→032`, `002→006`). Rules and what was not checked are in **`notes/links.md`**.

**`notes/scope-exclusions.md` is the exclusions reading record: 242 rows, one per scope note.** Every
`lean/docs/<NNN>.md` has exactly two `## ` sections — `## Scope` and `## Comparator links` (242 of 242)
— so the section boundaries are unambiguous, and every citation in the page points inside `## Scope`.
**121 of 242 sections state at least one exclusion, carrying 143 exclusion statements; 121 state
none.** The vocabulary floors, re-measured by `notes/scripts/extract_scope_notes.py` (report-only): the
5-phrase list an earlier pass recorded (`not formalized`, `excluded`, `out of scope`, `does not cover`,
`not covered`) hits **5 of 242** — families 003, 020, 049, 173, 360, per-phrase 0 / 3 / 0 / 1 / 1 — and
the 24-phrase broad list hits **44 of 242**. Quote 44 with that list; an earlier note recorded 42 under
a narrower 24-phrase list, so the number is the rule's, not the corpus's. The load-bearing finding is
the 121: **a scope note is not an exclusions list** — half the notes describe only what was selected,
so "read the scope note to learn what the formalization omits" works for 121 families and not for the
rest. The gap between 5 (keyword) and 121 (reading) is why this page is a reading record and not a
ledger tag. The exclusion rule is recorded with the page: a clause saying an assumption is *not
imposed* widens the formalized claim rather than bounding it, so it is not an entry. `notes/scripts/verify_scope_exclusions.py`
resolves every citation, requires each quotation verbatim on the line it cites **inside the `## Scope`
span**, re-measures all seven table numbers from disk, and flags all six injected mutants.

**`notes/subfindings.tsv` is the per-manuscript table: 1145 rows = 719 manuscript rows + 426
comparator rows, typed by a `kind` column.** Extraction only — every field is copied from a file,
nothing is inferred. `kind=manuscript` rows come from the `\href`s in the **4th field of
`\resultentry`**: family, order within the family, the href's **display title**, the manuscript path,
whether `formalization.yaml` lists that manuscript, and the family's tier. `kind=comparator-link`
rows come from each scope note's `## Comparator links` table: family, order in the table, the named
statement, and the `.lean` file. Fields a kind does not use are empty, so the file stays one
rectangular TSV. The report (fresh run): **719 manuscript rows over 372 families**, **426 comparator
rows over 242 families over 416 distinct `.lean` files**, **0 mismatches** between the ledger's `paps`
and the href count over all 372 families, **172** formalized manuscripts, manuscript-row tiers
**T3=274 T2=201 T1=0 T0=244** (the ledger has **no** T1 family: every family with a scope note links
at least one config), **719 distinct display titles over 719 rows** with **0** titles used by more
than one row, and **167 multi-manuscript families carrying 514 rows**. The display titles are the
release's own structural encoding of sub-findings: family 102 ships five hrefs titled *Unique Games
theorem*, *Optimal Max-Cut hardness*, *Factor-two Vertex Cover hardness*, *Constant-factor Min-UnCut
hardness*, *Directed feedback vertex set hardness*, and its abstract carries exactly those five
claims (read 2026-10-07: the UGC proof plus Max-Cut / Vertex Cover / Min-UnCut / directed FVS
hardness). That matching has now been read for **49 families over 203 manuscripts** in
`notes/subfinding-pairs.md`: **109** of those titles are claimed by an abstract clause, **94** are
claimed by none, and **18** clauses state a sub-finding no title names. The other 516 titles are
recorded, not paired.
`notes/scripts/verify_subfindings.py` re-derives every row from `overview.tex`,
`formalization.yaml`, `lean/docs/`, and the ledger, requires each path and each `.lean` file to exist
on disk, and flags all seven injected mutants including a same-family row swap.

**`notes/subfinding-pairs.md` is the pairing itself: 49 blocks, one per family, each quoting the
abstract clause and the display title it names, both with the `overview.tex` line they were verified
on.** Population = (abstract contains one of the release's four multi-claim phrases **and** ships ≥2
manuscripts) ∪ the ten densest families the task names = **49 families, 203 manuscripts**; the task
states 51 for that intersection and the number does not reproduce (the union over the 167
multi-manuscript families is **40**), which the page records with the rules tried and rejected.
Measured on the page: **62** accepted clause pairs, **47** accepted headline pairs, **18** clauses
recorded unmatched, **109** titles claimed, **94** unclaimed, **40** families with at least one
accepted pair, **17** with at least one unmatched clause, **6** pairing a sub-finding with no probe
hit. `notes/scripts/verify_subfinding_pairs.py --mutant` re-checks every quotation against the shipped
line, re-derives every count from the parsed blocks, and flags all seven injected mutants;
`notes/scripts/extract_subfinding_pairs.py` prints the population and the vocabulary counts the page
quotes, and writes nothing.

**`notes/sources.tsv` is the LaTeX source surface of all 719 manuscripts — 14 columns, one row per
manuscript — and `notes/sources.md` states the rules behind them.** A root is a `.tex` declaring
`\documentclass` **at line start**: **724** roots over **719** dirs, so **715** dirs have exactly one
and **4** have more; over the same 719 dirs a substring count of the command name reads **714** and 5,
and the rules differ in one named directory whose second "root" is a bundled PGF documentation macro.
Main-file resolution
(`main.tex` → `paper.tex` → the single root, flag never guess) lands on **main.tex 494, paper.tex 209,
single-root 16, flagged 0**, and picks the same file for all 719 dirs under either root rule. **Every
one of the 719 resolved main files sits under a `build/` directory** — `preprints/` ships build trees,
no top-level LaTeX root. Corpus totals: **7,705** `.tex`, **500** `.bib` (**225** dirs carry none),
**6,019** sections, **16,297** subsections, **316** subsubsections, **20,341** `\begin{proof}` (**1**
dir carries none), **21,288** statement environments, **127,456,942** `.tex` bytes. The theorem figure
is rule-dependent: declared-by-`\newtheorem`-in-dir minus non-statement names is **21,288**, the
six-name list theorem/lemma/proposition/corollary/claim/conjecture is **21,203**, and the 85 gap is
`assumption` 22, `foundation` 13, `auxproposition` 8, `hypothesis` 8, `auxlemma` 7, `standinginput` 5
and 9 names at ≤4.
`notes/scripts/verify_sources.py --mutant` re-derives all 30 quoted phrases from a fresh recount,
requires every backticked directory name to exist, and flags all nine injected mutants.

**`notes/verification-dirs.md` records what each of the 30 verification bundles says about itself.**
A `preprints/<slug>/verification/` tree is a finite-arithmetic **certificate** — it checks arithmetic on
a named instance, it does not prove a theorem — and the ledger's `verification` column counts the trees
without saying how to run one. `notes/scripts/extract_verification_dirs.py` applies a six-step
entry-point rule (top-level `verification/README.md`, then a subdirectory `README.md`, then
`README.txt`, then a `main_command` in a named JSON manifest, then a top-level script whose name begins
`verify|reproduce|run|check`, then none): over the 30 bundles **12** ship a top-level `README.md`, **6**
a subdirectory one, **5** a top-level script by name, **1** a subdirectory `README.txt`, and **6 have
none**; the manifest rule fires for **0**, because the two family-348 dirs that declare `main_command`
are claimed by the first rule. A README section names **28** of the 30 (27 `## Verification`, 1
`## Run the verification code`); the **2** unnamed bundles are both family 269 and each ships a single
`verification/rows.txt` — 20 lines, 1436 bytes, the pair **byte-identical** — which the manuscript
typesets with `\lstinputlisting`, so it is a printed data table, not a runnable check.

**`notes/index/` is the rendered index: 1,033 pages and 16 tables, every byte of it generated by
`notes/scripts/build_index.py`.** 372 family pages in 17 discipline dirs, 17 discipline pages, 92 topic
pages, 551 name pages, one entry point (`notes/index/README.md`); 8 node tables (families 372,
manuscripts 719, configs 416, Lean module dirs 559, scope notes 242, traces 10, topics 92, names 5,842)
and 8 edge tables (family-manuscript 719, family-config 416, config-declaration 200, family-lean 200,
citation 391, family-trace 10, family-topic 978, family-name 9,819). The load-bearing limit is that
**the release ships no manuscript→Lean edge**: `formalization.yaml` carries `sources:` (manuscripts)
and `main_results:` (config/declaration/file triples) as two flat lists with nothing joining them, so
the family→Lean reach the index shows is *derived* — family → config (the scope note's comparator
links) → declaration → file — 200 declarations over 189 configs reaching **136 of 372** families, and
formalization stays a per-manuscript flag. The 106 T2 families, whose scope notes link configs that no
`main_results` entry names, render as *absent*, never as unformalized. Fresh report: **48012** relative
links with **0** broken — that is the render-time registry, and `notes/scripts/check_index_links.py`
re-derives the check from disk over every rendered page: **66,107** links, **0** broken, **17,700** of
them resolving to a directory and **48,407** to a file, the 18,095-link difference being registry
under-coverage rather than a disagreement about existence (`notes/index-links.md`); canonical ==
rendered on **six of the seven** coverage counts (372 / 719 / 242 / 416 / 10 / 30) and **not** on
`formalized`, where canonical reads **173** and the rendered pages **172** — the one-path difference is
the yaml `sources:` entry whose manuscript is not in the ledger; `vs ledger` diffs of 0 on tier,
`mainres`, `chal`, `paps`, `paps_form`; ledger and overview family sets equal with **372 pages and 0
absent on disk**; 11 trace files over 10 attributed stems; **0** configs linked by more than one family;
**0** page collisions (max slug length 93); 21 of 372 summary pairings; manuscript links resolving 719 of
719 for main file, `build/` and `README.md`; **drift vs `notes/topics.tsv` 0**; names 5,842 measured /
551 subject pages / 5,291 citation-only / 9,819 edges over 372 families / **0** names with no family /
**10 of 10** trace families covered by a subject name.
Topics are a curated vocabulary in `notes/topics.tsv` (92 terms, hand-authored, with the reading
verdict per term in `notes/topics.md`), measured by `notes/scripts/measure_topics.py` over four texts
per family — title, abstract, scope note, and the derived Lean file paths. A family carries **zero or
more** topics: 978 assignments, median 2 per family, mean 2.63, 372 of 372 families covered, and **4**
terms with no hit at all (`automorphic-forms`, `cluster-algebras`, `machine-learning`,
`tropical-geometry`), kept as measured negatives. Topics are a label on top of the 17 disciplines,
which stay the partition; a listing is a keyword floor, not a judgement.
Names are measured, not curated: `notes/scripts/measure_names.py` reads six layers — family titles,
manuscript directory names, the optional titles of **16,889** statement environments, `main_results`
declaration names, capitalized prose tokens, and `.bib` author surnames — and `notes/names.md` states the
ladder that turns 3,407 title candidates into 551 subject names. The split is the point: a title or
declaration hit is a **subject**, a prose or bibliography hit is a **citation**, and only subjects get a
page. Of 5,842 keys, 551 are subjects and 5,291 are citation-only rows in `notes/index/names.tsv`; 9,819
family-name edges cover all 372 families (26.4 per family, median 7 per name, 68 names on one family, 17
names on 100+), **0** names resolve to no family, and all **10** reasoning-trace families are covered by
subject names. `cauchy` is the ceiling at 232 families and has **no** declaration hit — none of the 200
declaration names contains it.
Pages are generated — edit the generator and re-render, never a page. **Not checked:** proof
correctness, no `.lean` file was opened, citation edges are untyped, the Lean reach is derived and not
shipped, shape counts are keyword floors, no family was read to decide its topics, name pages do not
link from family pages, prose and bib-author name hits are citations with no per-occurrence context, and
no name-to-name edge is built.

## Columns

| Column | Source | Notes |
|---|---|---|
| `fam` | `overview.tex` `\resultentry{NNN}` | 3-digit family id |
| `discipline` | `\cataloguesection{…}{n}` order | 17 sections; a family belongs to the section above it |
| `title` | `\resultentry` arg 2 | |
| `paps` | `CONTENTS.md` links ∪ `overview.tex` `\href` links | The two mappings agree exactly: 719 links, 0 one-sided |
| `paps_form` | `formalization.yaml` `sources:` ids | Sums to 172 |
| `tier` | scope-note links × `main_results` | See tiers |
| `chal` | comparator links in `lean/docs/<NNN>.md` | |
| `mainres` | of those, count listed in `main_results` | |
| `scope_note` | file exists | 242 total |
| `scope_chars` | length of the `## Scope` section | Rough weight of the exclusions text |
| `verification` | manuscript dirs with a `verification/` subdir | 30 dirs over 22 families; family 348's 2 are one bundle shipped twice. A **count, not a pointer** — see the entry-point record in `notes/verification-dirs.md` |
| `inputs` | manuscript dirs with `INPUTS.md` | 4 dirs over 4 families (057, 157, 251, 259) |
| `covmd` | dirs with `verification/COVERAGE.md` | 2 files, both in family 348 — these bound what a check covers |
| `trace` | `README.md` reasoning-trace table | 10 families; read from the release table, not guessed from filenames |
| `shapes` | abstract keyword match | Multi-label |
| `conditional` | 1 if `conditional` ∈ `shapes` | |
| `resolves_named` | title **or** abstract (lowered together) names a conjecture/question/problem **and** uses a resolution verb | 248 families, the abstract-only scope having read 233; separate from the `resolution` shape (144) so the T0 buckets stay put |
| `counterex_broad` | title **or** abstract matches the counterexample phrase rule | 74 families; a strict superset of the `counterexample` shape (44), kept out of `shapes` so the T0 buckets stay put |
| `companions` | `result NNN` cross-refs in the abstract | |
| `companion_word` | abstract says "companion" | 9 families |
| `versions` | manuscripts sharing a date-stripped dir slug | 2 families, 4 dated re-issues (003, 056) |
| `summary` | a page exists at `notes/summaries/<discipline>/<NNN>-*.md` | Filesystem fact, not a derived claim; 21 of 372 families, 57 manuscripts behind them |

## Coverage tracks exposure, not importance

Per discipline (fams / scope notes / manuscripts / formalized manuscripts):

| Discipline | fams | notes | paps | form |
|---|---|---|---|---|
| Theoretical computer science | 40 | 34 | 73 | 32 |
| Combinatorics | 37 | 33 | 50 | 20 |
| Algebraic and complex geometry | 36 | 8 | 86 | 9 |
| Number theory | 31 | 17 | 58 | 8 |
| Probability and statistical mechanics | 29 | 19 | 105 | 12 |
| Differential geometry | 29 | 15 | 49 | 10 |
| Mathematical physics | 25 | 17 | 59 | 7 |
| Operator algebras | 19 | 15 | 31 | 7 |
| Algebra | 18 | 10 | 29 | 11 |
| Topology | 18 | 3 | 26 | 1 |
| Real and complex analysis | 16 | 10 | 26 | 8 |
| Partial differential equations | 16 | 11 | 29 | 3 |
| Convex and metric geometry | 15 | 13 | 30 | 13 |
| Group theory | 14 | 12 | 22 | 8 |
| Dynamical systems and ergodic theory | 12 | 9 | 19 | 2 |
| Functional analysis | 11 | 10 | 19 | 16 |
| Mathematical logic | 6 | 6 | 8 | 5 |

The columns sum to 372 / 242 / 719 / 172. Functional analysis (16/19 manuscripts) and mathematical
logic (5/8) are nearly covered; topology (1/26) and algebraic geometry (9/86) are nearly not.

The headline families show the same skew: **001, 002, 004, 006, 010, 011, 014, 016, 018, 019 have
no scope note at all**, while all 10 families with published reasoning traces (007, 017, 087, 102,
159, 197, 221, 271, 287, 362) do. Coverage follows what the release exposed to checking, not what
the community will scrutinize.

## Reading traps (all of these have produced false numbers here once)

- **`\newcommand` definitions count in a substring.** `overview.tex:28` defines `\cataloguesection`
  and `overview.tex:35` defines `\resultentry`, so a substring count of the command name reads 18 and
  373. Require the command at line start: **17** and **372**. The brace-qualified substring
  (`\resultentry{`) reads 372 only because each definition writes `}[n]{` after the name.
- **Parenthesized paths.** `preprints/Sharp-integral-fillings-in-CAT(0)-spaces-…/paper.pdf`.
  Use `preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf`. Excluding `{}` and `\` matters too: a greedy
  match in `overview.tex` otherwise swallows the `}\enspace\textperiodcentered\enspace\href{`
  separator and invents a 723rd manuscript.
- **`[^)]*` is not a markdown link scanner.** The same `CAT(0)` directory breaks a link-target regex:
  `\]\(([^)]*)\)` truncates the href at `(0)`, the truncated target does not exist, and a link checker
  reports a broken link the release does not ship. Walk forward from `](` tracking paren depth
  (`check_index_links.md_links`), and take **0 broken links** as the baseline, not 1.
- **Namespace-qualified declarations.** `theorem RowColumn.occupied_overlap` inside
  `namespace OAI` is `OAI.RowColumn.occupied_overlap`. Match the qualified tail against file text.
- **`axiom` in prose.** `^\s*axiom\s` hits doc-comment English, not real axioms.
- **`solution_module` is an import shim.** A config's file can be a single `import` line; the
  proof lives in the transitive import closure. Any `sorry`/axiom scan over a shim is meaningless.
- **A comparator file is a stub, not a proof.** `lean/ComparatorChallenges/*.lean` carry 539
  `sorry` occurrences over 416 files (415 with at least one; the exception is `HarmonicGrowth.lean`),
  while zero of the 122,458 files under `lean/OAI/**/*.lean` contain `sorry`. Reading a comparator
  file to ask "what does the formalization assume?" reads the target the release set itself, not the
  proved statement. Ask which declaration `main_results` names, then read that file.
- **A declaration name is a yaml fact, not a string in the Lean file.** `OAI.CHObstruction.main`
  is assembled from namespaces; it does not occur verbatim in `Main.lean`. Anchor such a citation to
  its `lean/formalization.yaml` line (the file has exactly one `main_results:` key, at line 972,
  carrying 200 entries over 189 distinct configs) and cite the Lean file separately for the statement.
- **`rg -f` with patterns ending in `\n`** fails ("the literal `\n` is not allowed in a regex").
- **Keyword tags are not claims.** The `conditional` tag flagged 9 families; reading the abstracts
  showed 5 were not assumptions — "unconditionally" (word boundary), "conditional expectation" and
  "conditional laws" (technical nouns), and "without assuming uniform convexity" (a negation that
  is the theorem's point). Any shape tag needs a reading pass before it is quoted as a property of
  a family. See `notes/conditional.md`.
- **The overview abstract is not the manuscript abstract.** Every shape tag is matched against the
  `overview.tex` text, which is a third-person rewrite: `We prove X` becomes `Proves X`. Measured
  2026-10-07 over all 719 manuscript abstracts: **0 identical, 0 abridged, 719 divergent**, median
  character ratio 0.126 (family best match: median 0.236). A tag is therefore a claim about the
  catalog's summary of a family, not about any manuscript — 283 of 372 families disagree with their
  overview on at least one shape. See `notes/abstracts.md`.
- **`notes/sources.tsv`'s `abstract` column is a flag, not a count.** It records whether a manuscript
  directory ships an `abstract` environment (719 of 719 do). The corpus contains **722** environments
  over those 719 directories — 057, 039 and 056 each ship two — so a gate written as
  `environments == 719` fails on correct data.
- **A quoted count with no rule behind it.** The counterexample numbers this file printed for a day
  (74 / 44 / 31 / 30) came from a reading pass whose regex was never written down, and no variant of
  the vocabulary the prose quoted reproduces them (unbounded `negativ` → 90; `\bnegativ` → 75;
  abstract-only phrase rule → 72). A count is only a measurement once the rule that yields it is in
  code. Fixed 2026-10-07 by writing `COUNTEREX_PHRASE` in the generator, which reproduces 74 / 30
  and excludes the three named false positives. See `notes/counterexample-tag.md`.
- **"Has a formalized main result" is not "has a formalized counterpart for the refutation".** The
  population outside T0 is **28** families — **19** at T3 and **9** at T2 — all 28 carry `main_results`
  declarations and all 28 resolve, yet in family 172 the entries state a positive classification
  (`Ramsey a ↔ FieldCriterion a`) and a 12-point
  spherical witness while the config carrying the disproven transitive-Ramsey claim has no entry;
  family 197's formalized group carries a prime-order torsion hypothesis that the blurb's "torsion-free"
  adjective does not; family 347 states a degenerate fixed-point instance, not the nondegenerate
  22-dimensional claim. Recorded 2026-10-07 in `notes/counterexample-crosscheck.md`, with every carrier
  body quoted at its `file:line`.
- **`counterex_broad` is a `'0'`/`'1'` column, so truthiness is a tier census.**
  `if r["counterex_broad"]:` is true for all 372 rows — `'0'` is a non-empty string — and reports 372
  families / 136 T3 / 106 T2 / 130 T0, which are the tier counts, not the flag counts. Compare with
  `== "1"`: **74** families, **21 T0 / 35 T3 / 18 T2**. Caught in the crosscheck checker on the first
  run.
- **`sorry` has two counting rules over the same files.** Over the 52 comparator configs behind the
  28-family population: **55** occurrences counting each distinct config file once, **58** counting
  scope-note link occurrences — family 100 links `CylinderCovering` four times. A per-family `set()`
  and a per-link scan disagree by 3 on correct data, so quote the number with the rule.
- **`Path` vs `str` in a membership test.** `verification`, `inputs`, and `covmd` read 0 for all 372
  rows: the reference sets held `Path` objects (`p.parent`) while the tested values were strings
  (`Path(p).parts[-2]`), and `str in {Path(...)}` is false for every family. A column that is
  silently zero is indistinguishable from a column that is genuinely empty unless the generator
  prints the repo-wide sum — which it now does. Fixed 2026-10-06 by keying the reference sets on
  `.name`; the sums are 30 / 4 / 2, and no basename collision exists (30/30, 4/4, 2/2 unique).
- **Manuscript ownership is not `parts[-2]`.** A manuscript path is
  `preprints/<dir>/…/file.pdf`, and the owner is the component **after** `preprints`. Keying by
  `parts[-2]` files manuscripts under `build/` and `sections/` — 8 pseudo-directories — and every
  cross-family exclusion then matches nothing, silently. Measured 2026-10-07 in
  `notes/scripts/extract_links.py`; the same rule is why the ledger's `verification`/`inputs`/`covmd`
  sums are keyed on `.name`.
- **A bead's family count is a reading-pass subset, not a population.** "The 28 two-manuscript
  families with no coverage signal" was the bead's prose; the reading record is **27** families over
  **54** manuscripts, and it reproduces only under three conditions at once: `tier == T0`,
  `paps == 2`, and the family id appearing between `## Second pass: the remaining 93 families` and
  `## What the triage shows` in `notes/t0-triage.md`. `paps == 2` alone reads **96** families
  (`T3:41`, `T0:35`, `T2:20`); T0 ∩ `paps == 2` reads **35**, 8 of them already read in the first
  pass, leaving **27**. "No coverage signal" then holds for **26** of the 27 — 268 carries
  `verification = 2`. Quote 27 with all three conditions, never as a census of two-manuscript families.
- **A bare `\bMSC\b` scan is not the MSC rule.** It returns 14 hits over 13 files, all prose:
  `type = {MSc thesis}`, "2-primary class groups", "primary classical construction". The shipped rule
  (`MSC 20xx | \msc | mscclass | "Mathematics Subject Classification" | Primary nnXxx`, over 8,206
  files) returns **0**, which is the finding: the release ships no classification vocabulary.
- **A coverage file is not coverage.** Family 318 ships `SUPPORT-COVERAGE.md`, which names
  `support/r-ce/ce_certificate.py`, its `.json`/`.txt` transcripts, `BUILDING.md`, and
  `SUPPORT-COVERAGE.json`. None of those paths exist on disk or in git. The ledger has no column for
  `SUPPORT-COVERAGE.md` (1 file repo-wide) and no way to express "named, not shipped".
- **The `verification` column is a count, not a pointer.** It reads 30 over 22 families and the family
  set joins cleanly, so it is a correct count — but it says nothing about how to run a bundle, and
  6 of the 30 bundles ship no entry point at all. A README section names 28 of the 30 (27
  `## Verification`, 1 `## Run the verification code`); the **2** it never mentions are both family
  269, and each ships a single `verification/rows.txt` — 20 lines, 1436 bytes, the two files
  **byte-identical**, typeset into the manuscript by `\lstinputlisting` and carrying no program.
  Measured 2026-10-07 by `notes/scripts/extract_verification_dirs.py`; recorded with every bundle's
  own entry point in `notes/verification-dirs.md`.
- **"No hypothesis is imposed" is not an exclusion.** Scope sections say things like "No nuclearity,
  simplicity, trace, or comparison hypothesis is imposed" and "No measurability hypothesis is needed".
  Those widen the formalized claim; they bound nothing. A reader who tags them as exclusions inflates
  the count of what the formalization leaves out. Recorded 2026-10-07 in the reading pass behind
  `notes/scope-exclusions.md`, where such clauses are not entries.
- **A keyword floor is not the exclusions count.** The 5-phrase list hits 5 of 242 sections and the
  24-phrase list hits 44; reading all 242 finds exclusions in 121. Quote the floor with its phrase
  list, never as the number of families with exclusions.
- **The 4th `\resultentry` field is not group-splittable.** It is a run of `\href{…}{…}` separated by
  `\enspace\textperiodcentered\enspace`, and a regex that splits on brace groups silently mis-slices
  once a display title contains a brace. Walk the braces with an escape-parity count
  (`build_catalog.read_args`): an odd number of leading backslashes means the brace is escaped and
  does not open or close a group. `extract_subfindings.py` uses that reader for both fields.
- **426 comparator rows and 416 configs are both correct.** Seven scope notes (071, 100, 115, 134,
  274, 275, 293) link the same `.lean` file twice inside their own table, so the table has 10
  occurrences more than the deduped config set — the same 10-gap `notes/links.tsv` records. A
  per-family `set()` over a comparator table drops those 10 rows and reports 416 rows, which is not
  what the notes contain.
- **A display title is not a claim about the abstract.** The 719 titles are what the release writes
  as link text; nothing in the repo states that a title corresponds to a clause of the abstract. The
  pairing has now been read for 49 families (`notes/subfinding-pairs.md`) and it is a reading call,
  not a release encoding: 94 of the 203 titles in that population are claimed by no clause, and 18
  clauses name a result no title names. Outside that population a title is still a label, not a
  sub-result.
- **A display title is not the manuscript's title.** The `preprints/` directory name carries the full
  manuscript title; the `\href` display text in `overview.tex` is a short label the release chose, and
  they diverge — "Maximum number of bases" sits in
  `The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026`, and
  "Correspondence coloring graphs with a forbidden clique" drops the "clique-free" its directory name
  carries. Pairing must use the display text, and a title quoted from a directory name will not
  validate.
- **Shipped display titles are not consistently encoded.** En dash vs source dashes, capitalised vs
  lowercase, accent normalised vs raw, all inside one family: 262:1 and 262:2 read `Lieb--Thirring`
  while 262:3 reads `Lieb–Thirring`; 291:1 capitalises "Stability" and 291:3 does not. A normalised
  title string is not verbatim on the line, so a quotation has to copy the shipped bytes.
- **The abstract keeps raw LaTeX, the display titles do not.** `K\"ahler`, `Bogomolov--Pop`,
  `\'etale`, `\textquotesingle`, `Szab\'o` appear in the abstract while the same family's titles carry
  `Kähler` and en dashes. A clause quote and a title quote on the same line follow different
  conventions; normalize neither.
- **A quoted family count can have no reproducible rule.** The pairing task states 51 families for
  "≥2 manuscripts and multi-claim language"; all four of its phrase counts reproduce (25 / 35 / 5 / 1,
  the second needing the stem `independ`) and the intersection over the 167 multi-manuscript families
  is **40**, not 51. Nine of the ten densest families it names are outside its own probe set. Same
  shape as the counterexample 74 / 30 gap in `notes/counterexample-tag.md`: quote the rule with the
  number.
- **`independ` is not a multi-claim marker.** 13 of the 40 probe-hit families hit on a technical use —
  "independent traces", "independence number", "independent set", "independent entries", "independent
  of matrix size", "independent uniform site potentials", "independent harmonic functions" — and 7
  families pair sub-findings with **no** probe hit, because their language is "Companion results
  prove", "also gives", "The family also proves", "A further result resolves". A probe over the
  release's four phrases is a population floor, and a pass that probes only it finds nothing.

## Open tasks

Tracked in bd, not in this file: `bd ready` is the live queue, `bd list --status=open` every open
issue, `bd list --status=closed` the completed ones. The checkbox list that used to sit here was a
second copy of the queue and it has been deleted; each completed item is a closed issue whose close
reason carries the outcome, and the detail lives in `notes/conditional.md`, `notes/t0-triage.md`,
and `notes/resolution-tag.md`.
