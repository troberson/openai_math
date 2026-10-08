# AGENTS.md

Companion to `README.md`: context and rules for agents working on the OpenAI Research Catalog
notes. Reading tool, not a verification tool. `CLAUDE.md` is a pointer here — every agent rule
lives in this file and nowhere else.

## Repository map

- `overview.tex` lists the 372 families as `\resultentry{NNN}` entries inside 17
  `\cataloguesection`s — the release's own claims, not ours.
- `preprints/` holds the 722 manuscripts, one directory each.
- `lean/` holds the formalization: `OAI/` source, `docs/<NNN>.md` scope notes,
  `ComparatorChallenges/*.json`, and `formalization.yaml`.
- `reasoning_traces/` holds 10 published traces in 11 files — the Mézard–Parisi trace ships as
  both `.pdf` and `.tex`.
- `notes/` is the reading ledger: `catalog.tsv` (372 rows, 22 columns), `README.md`,
  `t0-triage.md`, `conditional.md`, `resolution-tag.md`, `counterexample-tag.md`, `proof-density.md`,
  `counterexample-crosscheck.md` (the 28 counterexample-shaped families outside T0, each claim paired
  with the `main_results` declaration that corresponds to it),
  `t0-chains.md` (the 2 cross-family edges the release records, the literature chain behind 311, and
  the 28 two-manuscript second-pass families with their intra-family citation layer),
  `verification-dirs.md` (the 30 bundles, each one's own entry point, and the family-348 reading),
  `summaries-workflow.md` (the resume protocol for the summary batches),
  `conjecture-standing.tsv` (139 rows, 10 columns — a labeled training-data prior, not a fact) with
  `conjecture-standing.md` beside it, `formalization-deps.tsv` (31 rows, 8 columns — the upstream
  library graph) with `formalization-deps.md` beside it and `dependency-drift.md` (what that record
  implies, read off the pins, the 23 patches, and the lakefile mechanics) beside both,
  `links.tsv` (22 rows, 7 columns — the
  typed-edge inventory) with `links.md` beside it, `scope-exclusions.md` (235 rows — what each scope
  note says its formalization leaves out), `subfindings.tsv` (1137 rows — 722 manuscript rows and 415
  comparator rows, typed by a `kind` column) with `subfinding-pairs.md` (49 families, 206 manuscripts —
  the reading pass that pairs abstract clauses with display titles) beside it,
  `index-design.md` (the index schema decision — store, location, granularity, topic vocabulary — with
  the measured node and edge population that justifies it), `index/` (the rendered index, all of it
  generated: 372 family pages in 17 discipline dirs, 17 discipline pages, 92 topic pages, 552 name
  pages, one entry point, 8 node tables and 8 edge tables),
  `topics.tsv` (92 rows, 9 columns — the curated topic vocabulary: term, pattern, family yield, the
  four per-layer counts, status, page) with `topics.md` beside it,
  `names.md` (the name layer — six sources, the subject/citation rule, the rejection ladder, the
  family-title escape, the recorded decisions) with `index/names.tsv` (5,859 rows) beside it,
  `sources.tsv` (722 rows, 14 columns — the LaTeX source surface of each manuscript: root count,
  resolved main file, section/proof/statement-environment counts, `.bib` count, `.tex` bytes) with
  `sources.md` beside it,
  `named-results.md` (the named-result inventory the manuscript **statements** carry — 17 target-named
  headline statements over 17 families, the three-layer naming record, and the applied 233 → 248
  `resolves_named` scope swap) with `named-results.tsv` **absent** beside it — the page is
  report-fed, not table-fed,
  `summaries/<discipline>/<NNN>-<name>.md`, `notes/scripts/`.
- `.beads/issues.jsonl` is the tracked issue store, in bd no-db mode; see the beads section below.

## Dev environment tips

- Regenerate the ledger with `python3 notes/scripts/build_catalog.py` — stdlib only, runs in
  seconds, writes `notes/catalog.tsv` and prints the report that every number in
  `notes/README.md` comes from.
- Render the index with `python3 notes/scripts/build_index.py` — it imports the joins from
  `build_catalog.py` and the name measurement from `measure_names.py`, writes `notes/index/`
  (1,034 pages + 16 tables, 15M), and prints the report every count in it comes from. There is
  **no manuscript→Lean edge in the release**: `formalization.yaml`
  carries `sources:` (manuscripts) and `main_results:` (config/declaration/file triples) as two flat
  lists with nothing linking them, so the index renders the chain the yaml does support — family →
  config (scope-note links) → declaration → file, 185 declarations over 178 configs reaching 127 of
  372 families — and keeps formalization a per-manuscript flag. A family whose scope note links configs
  that no `main_results` entry names renders as *absent*, never as unformalized. Page slugs are
  mechanical (NFKD, strip combining marks, drop `$`/apostrophes/`\command`, lowercase, non-alphanumerics
  → `-`, leading `the-` dropped): 0 collisions, max length 93. Index↔summary pairing is by family
  number only — 12 of 372 families have a summary page.
- Names are a measured layer, not a curated one: `python3 notes/scripts/measure_names.py` (report-only,
  ~42 s; `--json` dumps the rows) reads six layers — family titles, manuscript directory names, the
  optional titles of 15,755 statement environments, `main_results` declaration names, capitalized prose
  tokens, and `.bib` author surnames. **A title or declaration hit is a subject; a prose or
  bibliography hit is a citation, and only subjects get a page** — 552 pages over 5,859 measured keys,
  5,307 citation-only rows. Quote the split with the rule, never as one count. The mid-sentence
  capitalization test is the name-versus-word gate (`mid >= 3 and low <= max(1, mid // 2)`), and the
  acronym and LaTeX-macro tests are judged on the **dominant surface form over all six layers**: a
  `\cite{OpenAIWidth}` that leaks into a theorem-environment title never appears as prose, so a
  prose-only view cannot see it. `cauchy` reaches 233 families and has **zero** declaration hits — none
  of the 185 declaration names contains it, which is a fact about the release, not an extractor gap.
- Topics come from the hand-authored vocabulary at `notes/topics.tsv`, never from derivation, and
  measure it with `python3 notes/scripts/measure_topics.py` (`--check` re-measures all 92 rows and
  exits 1 when a recorded count has drifted). Keep that file **outside** `notes/index/`: the index
  tree is fully generated and a hand-edited file inside it is overwritten by the next build. A family
  carries **zero or more** topics (median 2, mean 2.61 over 971 assignments) — topics are a label on
  top of the 17 disciplines, which stay the partition — and a term with no hit is kept as a measured
  negative (4 of 92), not deleted. A listing is a keyword floor over four texts (title, abstract,
  scope note, derived Lean paths); quote per-layer counts, never just the yield.
- Match an accented name on the letters **after** the accent escape: `hler` reaches both `K\"ahler`
  and `Kähler`, `erd` reaches every spelling of Erdős. `overview.tex` apostrophes are inconsistent
  (76 titles ASCII `'`, 8 U+2019), so the text layer folds U+2019 → ASCII before matching. Probe a
  narrowing with the **shipped** pattern: `\balgorithm` reaches 24 families, the shipped
  `algorithm\b` reaches 23, and a probe with the looser stem manufactures an exclusion that the
  shipped pattern does not produce.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`. `lean/OAI/` is 121,734 files
  and 25.9M lines; a build is hours on a desktop and buys nothing for categorization.
- Parse `notes/catalog.tsv` with `csv.DictReader(..., delimiter='\t')`, never `split(',')`.
- Count `\cataloguesection` and `\resultentry` by the command at line start: **17** and **372**.
  `overview.tex:28` and `overview.tex:35` define both with `\newcommand`, so a substring count of the
  command name reads 18 and 373.
- Same trap in `preprints/`: a manuscript's root is the `.tex` with `\documentclass` **at line start**
  — **718** dirs have exactly one, **4** have two. A substring count of the command name reads 717 and
  5; the one differing dir (`Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026`) ships a
  bundled PGF documentation macro that defines a macro *mentioning* the command. Main-file resolution
  (prefer a root named `main.tex`, then `paper.tex`, then the single root; flag, never guess, a
  multi-root dir with neither) answers the same file for all 722 dirs under either rule. **Every one of
  the 722 resolved main files sits under a `build/` directory** — there is no top-level LaTeX root
  anywhere in `preprints/`, so a `parts[-2]`-style path read is not a manuscript location here.
- Quote a theorem count with its rule. `\begin{X}` for X declared by `\newtheorem` in the same dir,
  minus the non-statement names (`definition`, `remark`, `example`, `notation`, `convention`,
  `procedure`, `construction`, `scope`, `abstract`), is **21,402**; the six-name list
  theorem/lemma/proposition/corollary/claim/conjecture is **21,317**. The 85 gap is `assumption` 22,
  `foundation` 13, `auxproposition` 8, `hypothesis` 8, `auxlemma` 7 and 10 names at ≤5.
  `notes/sources.tsv` carries the declared-rule figure.
- Label source-level facts as source-level. `lean/formalization.yaml` states
  `scope: "Partial progress."`, `automation: methods: [agent]`, `review: status: unchecked`.
  Zero `sorry` in source is not a comparator pass, and it does not mean the library elaborates.
- Report coverage as four layers, never one percentage: 162/722 manuscripts, 235/372 scope notes,
  405 comparator challenges, 185 `main_results` entries over 178 unique configs.
- Treat claim shape as multi-label — 66 families match ≥3 shapes, 57 match none — so a tag is a
  floor, not a census. Keep `resolves_named` and `counterex_broad` ledger columns, not shapes: that
  is what leaves the first-match T0 buckets in `triage_t0.py` untouched.
- Quote a count only with the rule that yields it. The counterexample figures were quoted from a
  reading pass for a day before `COUNTEREX_PHRASE` was written into the generator; no stem variant of
  the quoted vocabulary reproduces 74 / 30. See `notes/counterexample-tag.md`.
- Absence of formalization is not a red flag — 560 of 722 manuscripts are unformalized.
- Read `lean/docs/<NNN>.md` before claiming what a family proves; its `## Scope` section is the
  load-bearing part. It is not an exclusions list, though: **120 of 235 sections state no exclusion
  at all**, and a clause saying an assumption is *not imposed* widens the formalized claim rather
  than bounding it. The read record is `notes/scope-exclusions.md`; re-measure its floors with
  `python3 notes/scripts/extract_scope_notes.py` (report-only) — the 5-phrase list hits 5 of 235 and
  the 24-phrase list hits 44, while reading finds exclusions in 115. Quote a floor with its phrase
  list, never as the number of families with exclusions.
- A `lean/ComparatorChallenges/*.lean` file is a challenge **stub**, not a proof: 405 files carrying
  509 `sorry` occurrences, 404 of them at least one (the zero-`sorry` exception is
  `HarmonicGrowth.lean`), while **zero** of the 121,734 files under `lean/OAI/**/*.lean` contain
  `sorry`. A comparator file states the target the release set itself; the proved version, where it
  exists, lives under `lean/OAI/`. To ask what a formalization assumes, resolve the declaration
  `main_results` names in `lean/formalization.yaml` and read that file — a fully-qualified name like
  `OAI.CHObstruction.main` is a yaml fact and does not occur verbatim in the Lean source.
- Cross-check a claim shape against the formalization with
  `python3 notes/scripts/extract_counterexample_crosscheck.py` — report-only, 0.25 s. Its population
  rule is `counterexample` in the ledger `shapes` column **AND** `tier != T0`: **28** families,
  **18 at T3 and 10 at T2**. The shape fires on **44** families corpus-wide, **16** of them at T0 —
  the bead prose's "21 T0 counterexample-shaped families" is a reading-pass count, not this rule's,
  and both numbers are recorded in the page. `counterex_broad` is a **'0'/'1' ledger column** (74 ones:
  22 T0, 33 T3, 19 T2); a truthiness test over `csv.DictReader` rows counts all 372, so compare with
  `== "1"`.
- Pair a claim with a declaration through the **scope note**, never through the yaml:
  `formalization.yaml` carries no family key, so family→config comes only from the
  `\.\./ComparatorChallenges/(X)\.lean` links inside `lean/docs/<NNN>.md`. Of the **51** configs the 28
  scope notes link, **27** carry a `main_results` entry and **24** carry none — **11** of those gaps sit
  in **7** T3 families, **13** across the 10 T2 families. A T2 family with zero entries is a structural
  absence; a T3 family whose entry is a *positive* classification while the disproven conjecture's
  config has no entry (family 172) is a claim-level gap, and that distinction is the page's finding.
- `theorem main : MainStatement :=` is opaque. The content lives in a `def <Carrier> : Prop :=` reached
  through the declaration file's **import closure** (BFS over `import OAI.*`), not through the directory
  layout — **11** of the 27 declarations are carrier-typed, and a verdict that quotes only the `main`
  line quotes nothing.
- `sorry` in a comparator stub has two rules: **53** over the 51 distinct config files behind the
  population, **56** over scope-note link **occurrences** (the 3-gap is family 100's four links to
  `CylinderCovering`). Quote the figure with the rule; the extractor prints the per-link number and the
  checker counts distinct files.
- A `preprints/<slug>/verification/` bundle is a finite-arithmetic **certificate**, not a proof, and the
  ledger's `verification` column is a count, not a pointer. Measure the entry point with
  `python3 notes/scripts/extract_verification_dirs.py`: over the 30 bundles, **12** ship a top-level
  `verification/README.md`, **6** a subdirectory one, **5** a top-level script whose name begins
  `verify`/`reproduce`/`run`/`check`, **1** a `README.txt`, and **6 have none** — for 4 of those the run
  command lives in the manuscript README, and for the **2** bundles no README section names at all (both
  family 269) there is no command anywhere: each ships one `verification/rows.txt`, byte-identical
  between them and typeset into the manuscript by `\lstinputlisting`, so the ledger column is the only
  machine-readable pointer. A README section names 28 of the 30 (27 `## Verification`, 1
  `## Run the verification code`). Quote the class counts with the extractor's rule, never as coverage.
- Attribute reasoning traces from the table in `README.md`, never by guessing from filenames.
- Bucket the T0 families with `python3 notes/scripts/triage_t0.py` — it reads `notes/catalog.tsv`,
  writes nothing, and reconciles 137 families over 255 manuscripts. Findings live in
  `notes/t0-triage.md`.
- Measure the chains and the 28 with `python3 notes/scripts/extract_t0_chains.py` — report-only, writes
  nothing. Reproducing the bead's 28 needs **three** conditions at once: `tier == T0`, `paps == 2`, and
  the family id appearing between `## Second pass: the remaining 93 families` and `## What the triage
  shows` in `notes/t0-triage.md`. Repo-wide there are **96** families with exactly 2 manuscripts
  (`T0:36`, `T2:20`, `T3:40`) and **36** of them are T0, 8 read in the first pass — so 28 is a
  reading-pass subset, never a census, and "no coverage signal" holds for **27** of them (268 carries
  `verification = 2`). The release records a cross-family link only as a `result (NNN)` clause in the
  overview abstract, which is what the ledger's `companions` column parses: **2** edges over 372
  families. `companion_word` (`\bcompanion` in the same abstract) fires on **10** families and **0** of
  them carry a `companions` edge — the word is not a link. Findings live in `notes/t0-chains.md`.
- Quote `notes/conjecture-standing.tsv` as a prior, never as a literature fact. Its
  `standing_prior_2025` column is the assistant's training-data memory at an early-2025 cutoff,
  self-rated by `prior_confidence`; the repo supplies only `release_claim` and `abstract_line`.
  No row may assert consequence. Intra-corpus citation edges exist and are measured — 397
  release-labelled `.bib` entries resolve to 396 manuscript→manuscript edges over 158 of 372
  families, 105 crossing a family boundary (`notes/links.tsv`) — but the edges are **untyped**: the
  release records no builds-on / contrasts-with relation, so an edge is a citation choice, not
  consequence. The "only 14 of 372 family titles appear in the corpus's `.bib` files" figure this tip
  used to carry **is** reproduced — by a 6-token lowercased title prefix over the 417 `.bib` files at
  glob depth ≤3, counting own-family bibliographies — but its conclusion ("these manuscripts do not
  cite each other") does not follow; see `notes/links.md`.
- Extract the upstream library graph with `python3 notes/scripts/extract_formalization_deps.py`. It
  reads all 121,734 `lean/OAI/**/*.lean` files, so it takes minutes, not seconds, and it refuses to
  write the TSV when a join breaks. Import counts are over `lean/OAI/**/*.lean` — the whole tree
  yields OAI 277,501 / Mathlib 56,715, not the 276,599 / 56,196 the table records, so quote the scope
  with the number. `lean/lake-manifest.json` is read for the report only, never for a column.
- Read `lean/lakefile.lean` (335 lines) with two delimiters in mind. Package labels are wrapped in
  guillemets — `«doc-gen4»`, `«iut»`, `«schoenflies-lean»` — while the deps table keys them plain, so
  any join between the two must strip them first. The two patch-phase arrays list names with **one**
  leading backtick and no closing delimiter, so `` `([^`]+)` `` finds **0** of the 11 pre-resolution
  and 12 `post_update` names; parse with `` re.findall(r"`([^\s`,\]]+)", array_text) ``. Patch
  filenames are built by code (`lean/lakefile.lean:193`), not hand-named, so the `-lean4341` suffix is
  a fact about the toolchain, not a convention.
- Extract the typed-edge inventory with `python3 notes/scripts/extract_links.py` — 20 seconds, writes
  `notes/links.tsv`, prints the report every count in it comes from. Quote an edge with its rule:
  415 is scope-note link **occurrences** and 405 is **distinct configs** (the 10-gap is one config
  linked twice inside each of 7 docs; the ledger `chal` column is the deduped 405), and the ledger
  `mainres` column sums to 178 unique configs while the yaml carries 185 entries. Manuscript
  ownership is the path component after `preprints`, never `parts[-2]` — keying by `parts[-2]` files
  manuscripts under `build/` and `sections/` and silently makes every cross-family exclusion match
  nothing. The report also reproduces the legacy title proxy (14 over 417 `.bib` files at depth ≤3) so
  the figure the older docs quote is checkable against a command, not just against prose.
- Extract the per-manuscript table with `python3 notes/scripts/extract_subfindings.py` — writes
  `notes/subfindings.tsv` (722 manuscript rows + 415 comparator rows) and prints the reconciliation.
  Read the 4th `\resultentry` field with `build_catalog.read_args`, never with a regex group split:
  the field is a run of `\href{…}{…}` and a group split mis-slices as soon as a display title carries
  a brace. Quote 415 as comparator-table **rows** and 405 as **distinct configs** — the 10-gap is the
  same 7 docs `links.tsv` records (071, 100, 115, 134, 274, 275, 293), so a per-family `set()` over a
  table reports 405 rows and is wrong. A display title is link text, not a sub-result, and it is not
  the manuscript's own title — the `preprints/` directory name is. Pairing has been read for 49
  families (206 manuscripts) in `notes/subfinding-pairs.md`: 64 sub-finding clause pairs and 47 headline
  clause pairs accepted, 18 clauses recorded unmatched, 111 of 206 titles claimed by a clause and 95 by
  none. Quote the display text verbatim — the release is inconsistent about capitalization
  (`Correspondence coloring graphs…` vs `Equivariant Jiang--Su Stability…`) and about dashes
  (`Lieb--Thirring` vs `Lieb–Thirring`), so a normalized title is not verbatim.
- Extract the pairing population with `python3 notes/scripts/extract_subfinding_pairs.py` — report-only,
  writes nothing. Its population rule is (probe phrases `also prove`, `independ`, `also establish`,
  `as a consequence`) AND ≥2 manuscripts, union the ten named densest targets: 49 families, 206
  manuscripts. **The bead's "51 of them also use multi-claim language" does not reproduce.** The four
  per-phrase counts (25 / 35 / 5 / 1) reproduce exactly over all 372 abstracts only when the second is
  read as the stem `independ` (`independent` gives 34), and their union over the 167 multi-manuscript
  families is 40, not 51 — nine of the bead's ten named densest targets sit outside its own 40. Rules
  tried and rejected: `also` (56), `both ` (48), `companion` (10), `together` (8), ≥2 prove-verbs (33),
  ≥2 sentences with a prove-verb (32), ≥3 sentences (73). Same shape as the counterexample 74 / 30 case;
  see `notes/counterexample-tag.md` and the population section of `notes/subfinding-pairs.md`.
- Compare the two abstracts a family ships with `python3 notes/scripts/compare_abstracts.py` — report
  only, `--tsv` writes `notes/abstracts.tsv`. **The `overview.tex` abstract is a rewritten paraphrase,
  not the manuscript abstract: 0 of 722 manuscript comparisons and 0 of 372 family best matches read
  identical or abridged.** The claim-shape tags are keyed to that paraphrase, so a tag is a claim about
  the summary, not about the manuscript. Median family best match is 0.236; 282 of 372 families
  disagree with the overview on at least one shape. The overview under-flags every shape except
  `resolution`, which it over-flags (144 of 372 families vs 153 of 722 manuscripts). For a
  multi-manuscript family a low per-manuscript ratio is expected — the overview is a synthesis of
  several manuscripts (368 merges $p\le2$ with $p>2$; 240 merges a ZFC theorem with a CH obstruction),
  so quote the unit with the number. See `notes/abstracts.md`.
- Extract the named-result inventory the manuscript **statements** carry with
  `python3 notes/scripts/extract_named_results.py` — report-only, writes nothing; run it twice and diff,
  the 185-line report is byte-identical. Headline statements are `theorem`/`maintheorem`/`thm` begins:
  2,270 begins, **1,498 titled per line** (a whole-text scan reads 1,508 because 10 titles span a
  newline). **Zero of the 17 target-named headline titles pair a target noun with a resolve verb** — the
  release names conjectures in manuscript names, abstracts and prose, and in the overview **title**, not
  in statement captions, so `resolves_named` is evidence-backed by the record rather than by theorem
  text. Match `build_catalog.TARGET_NOUN` **case-insensitively** on directory names, theorem titles and
  overview titles: the ledger rule sees lowercase abstracts, and a case-sensitive match on those
  capitalized surfaces undercounts. The applied scope is a **union** — title ∪ abstract, both lowered
  together, 233 → 248 with removals 0; the 15 additions are 022 039 044 096 097 151 156 192 209 263
  289 293 297 347 367. A strict title+abstract *replacement* reads 149 (99 removals) and a
  case-sensitive raw-title read yields 147 (100 removals) — quote which scope you mean.
  Findings: `notes/named-results.md`.
- `notes/sources.tsv`'s `abstract` column is a per-directory **flag**, not an occurrence count: the
  corpus ships 725 `abstract` environments over 722 manuscript directories (057, 039 and 056 each ship
  two), and every one of the 722 directories has at least one.
- A proof **count** is a document-length proxy, not a density. Tested 2026-10-08 with the decision bar
  written into the script header before the data was read (AUC ≥ 0.65 **and** p < 0.01, plus a tex-KB
  size control at the matching scale): raw proofs and statements per family clear T0 > T3 (0.676 /
  0.678) only, and are within 0.03 of the size control there (0.784); proofs per manuscript clears
  T0 > T2 (0.697) and T0 > T3 (0.782) and is size-explained on both (control 0.691 / 0.784); the two
  genuine density measures are NULL on every tier pair — proofs per statement 0.491 / 0.456 / 0.466,
  proofs per KB 0.503 / 0.453 / 0.457, the ratio being ≈0.97 corpus-wide and tier-independent — and no
  claim shape clears the bar. Direction is opposite the naive reading: T0, the least-formalized tier,
  carries the most proofs per manuscript (median 30.0) because its manuscripts are the largest (168.9
  KB vs 86.0 in T3). **No ledger column was added.** Findings in `notes/proof-density.md`.
- Project skills live in `.qwen/skills/` — `proof-triage` routes ledger work,
  `auto-skill-lean-formalization-coverage-audit` carries the measurement method.

## Testing instructions

- Nothing here builds and there is no test suite; the generator report is the test.
- Run the generator twice and diff the output: `notes/catalog.tsv` must be byte-identical.
- Check the report's reconciliation lines after every change: 372 families, 722 manuscripts,
  162 formalized, 235 scope notes, 405 challenges, 185 `main_results` entries over 178 configs,
  and both `overview.tex` ↔ `CONTENTS.md` cross-checks reading 0.
- Confirm the discipline table sums to 372 / 235 / 722 / 162.
- Quote a count only from a fresh generator report, never from a previous run's output.
- Confirm a new tag discriminates before quoting it: the `conditional` tag flagged 9 families and
  5 were not assumptions. `notes/conditional.md` is the model for a reading pass.
- Parenthesized manuscript paths need `preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf`; excluding
  `{}` and `\` is what stops a phantom 723rd manuscript.
- Check every `notes/summaries/` page with `python3 notes/scripts/verify_summaries.py --mutant`
  before reporting it green — it resolves every `[Sn:line]` marker against the shipped file, checks
  every quotation against the lines it cites, counts a File cell that resolves under both roots as a
  problem, and writes nothing. `--mutant` corrupts one real quotation in each form the page uses
  (inline, inline wrapped across lines, block quote) and invents one, so quote the report by its form
  names: a page with no quotation marks at all is proven only by the block-quote mutant.
- Check `notes/abstracts.md` with `python3 notes/scripts/verify_abstracts.py --mutant` before quoting
  any of its counts — it resolves every `[S#]` marker to a Sources-table row, requires every row cited
  at least once and every table path to exist, and checks every quotation verbatim-modulo-whitespace
  against the text its marker's file carries. Read `overview.tex` through
  `build_catalog.parse_overview()`, never with a `\resultentry` regex: the abstracts contain braces, so
  a `[^{}]*` group silently drops the math-heavy families, which are the ones being quoted.
  `python3 notes/scripts/compare_abstracts.py --tsv` writes `notes/abstracts.tsv`; run it twice and
  diff — 372 rows byte-identical — and `--mutant` must catch all 7 injected corruptions.
- Check `notes/named-results.md` with `python3 notes/scripts/verify_named_results.py --mutant` before
  quoting any of its counts — it resolves every `path:line` anchor and every bare `:NNN` overview anchor
  against `famline`, re-derives all 64 count phrases from `extract_named_results.population()`, checks
  the 17-row target table against that population and the ledger, matches every `*"…"*` quotation against
  the file its pinned anchor names, and flags twelve injected mutations. It writes nothing; run it twice
  and diff — the report is identical. Quote a quotation's anchor as the checker pins it: a manuscript
  sentence wraps across 1–4 source lines, so the anchor is the **prose-coordinate** line the extractor
  reports, not the line the sentence ends on.
- Run `python3 notes/scripts/measure_proof_density.py --mutant` before quoting a proof-density figure —
  it re-derives every AUC and p from `notes/sources.tsv` joined to `notes/catalog.tsv` by family
  number, gates on the population (722 rows, 722 distinct dirs, 372 families on both sides, per-family
  source rows == ledger `paps`, 20,449 proofs, 21,402 statements, tier counts 127/108/0/137, positive
  `tex_bytes`, every source dir present under `preprints/`), self-tests the statistic against 5
  hand-computed AUCs, and flags 8 injected corruptions. It writes nothing; run it twice and diff — the
  report must be identical. Ties score 0.5, so `([1,2,3],[0,1,2])` is **7/9**, not 6/9, and the ranks
  must be assigned over the **jointly sorted** pooled sample — sorting each group and concatenating
  gives every AUC as 0.000 with absurd p-values.
- Check `notes/scope-exclusions.md` with `python3 notes/scripts/verify_scope_exclusions.py --mutant`
  before quoting any entry — it requires exactly one row per scope note on disk, checks every
  `lean/docs/NNN.md:<line>` anchor falls inside that file's `## Scope` span, requires each quotation
  verbatim on the line it cites, re-measures all seven Measurements-table numbers from the files, and
  flags six injected mutants including a paraphrase dressed as a quote. `extract_scope_notes.py` is
  report-only: it writes nothing and is where the page's counts come from.
- Check `notes/subfindings.tsv` with `python3 notes/scripts/verify_subfindings.py --mutant` before
  quoting a row — it re-derives every manuscript row from `overview.tex` (path, display title,
  formalized flag, tier) and every comparator row from its scope note's table **in order**, requires
  each path and each `.lean` file to exist on disk, requires each family's row count to equal the
  ledger's `paps`, requires `seq` to run 1..n per family and kind, rejects a field a kind never fills,
  and flags seven injected mutants including a same-family row swap. Run
  `python3 notes/scripts/extract_subfindings.py` twice and diff: the TSV must be byte-identical.
- Run `python3 notes/scripts/extract_subfinding_pairs.py` twice and diff: the report must be identical.
- Run `python3 notes/scripts/measure_index_sizes.py` twice and diff: the report must be identical. It
  writes nothing, and every count in `notes/index-design.md` comes from it. It prints two byte sums
  that are not interchangeable — `ledger set bytes (5 named TSVs)` **296283** and
  `all notes/*.tsv bytes` **541463** — and an INDEX section whose table row counts are read from the
  generated files under `notes/index/`, not derived from the upstream counts they were built from.
- Check `notes/index-design.md` with `python3 notes/scripts/verify_index_design.py --mutant` before
  quoting the schema — it resolves every backticked `path:line` anchor of any extension (a mistyped
  extension fails, it is not skipped), matches each fenced block against the nearest preceding anchor,
  re-derives all 82 count and byte phrases from `measure_index_sizes.population()` (schema-table row
  counts from the rendered TSVs themselves; byte phrases scoped to the five TSVs the page tabulates,
  so `sources.tsv` and `topics.tsv` are not demanded), and flags thirteen injected mutations. It
  writes nothing.
- Run `python3 notes/scripts/build_sources.py` twice and diff: `notes/sources.tsv` must be
  byte-identical and the report identical. Its report reconciles 722 rows over 722 preprint dirs, 0
  dirs with no `subfindings.tsv` manuscript row, 0 subfindings slugs absent from disk, 0 empty or
  missing PDFs, 0 families outside the ledger, 0 per-family row-count differences against the ledger's
  `paps`, and 0 manuscript-path differences between `overview.tex` and `sources.tsv` in either
  direction — the last three being the independent check, since they re-parse `overview.tex` with
  `build_catalog.parse_overview()` instead of trusting the table's own source.
- Check `notes/sources.md` with `python3 notes/scripts/verify_sources.py --mutant` before quoting any
  figure — it re-derives all 30 count phrases from a fresh recount over `preprints/` (root
  distribution, main-file outcomes, single-root names, column sums, the six-name environment total and
  its per-name gap), requires every backticked manuscript directory name on the page to exist,
  resolves every `path:line` anchor of any extension, matches each fenced block against the nearest
  preceding anchor, and requires every `pdf` on disk non-empty, every `main_tex` present and declaring
  `\documentclass` at line start, every `fam` in the ledger, and every family's row count equal to
  `paps`. It flags nine injected mutants and writes nothing.
- Check `notes/subfinding-pairs.md` with `python3 notes/scripts/verify_subfinding_pairs.py --mutant`
  before quoting any count from it — it requires exactly one block per population family and none
  outside, resolves each block's `overview.tex` anchor to that family's `\resultentry` line, checks
  `n` against `subfindings.tsv` and the tier against the ledger, requires every quoted clause and
  every quoted title to be verbatim on that line, requires each `[fam:seq]` to resolve to a manuscript
  row of the block's own family, requires `claimed` and `unclaimed` to be disjoint and to cover the
  family's full `1..n` exactly once, re-measures the ten Summary-table numbers from the parsed lines,
  and flags seven injected mutants including a paraphrase dressed as a quote. It writes nothing.
- Check `notes/conditional.md` with `python3 notes/scripts/verify_conditional.py --mutant` before
  quoting the source check — it attributes each fenced block to the nearest preceding `file:line`
  anchor and matches every block line, resolves each `*"…"*` prose quotation and each inline
  `name → file:line` citation against the shipped file, and flags five injected mutants. It reports
  **15 unanchored prose quotations** — the pre-existing abstract and scope-note quotes in the
  per-family sections, which carry no line anchors and are therefore not verified. It writes nothing.
- Check `notes/counterexample-crosscheck.md` with
  `python3 notes/scripts/verify_counterexample_crosscheck.py --mutant` before quoting any of its counts
  — it recomputes the population, tier split, ledger sums, per-family config/entry/gap counts, the
  carrier-typed count, and the stub and `sorry` totals from `notes/catalog.tsv`, `overview.tex`,
  `lean/formalization.yaml`, `lean/docs/`, and `lean/ComparatorChallenges/`, and matches all 19 count
  phrases against that recomputation. Layout is enforced, not cosmetic: a fenced block is attributed to
  the **nearest preceding** anchor (so an anchor line goes *before* its block), and each `*"…"*`
  quotation is pinned to the anchor in its **own line** (so a claim quote's anchor sits at the start of
  the quote, not at its end). Verbatim means the bytes on the cited line — a de-LaTeXed `Gyárfás's`
  fails against `overview.tex:405`, which ships `Gy\'arf\'as's`. It requires the 28-row summary table,
  the 11-row T3 gap table, and the 10-row T2 table to equal the recomputation, and requires each of the
  27 entries to cite its yaml block at the `- comparator_config:` line — the extractor's yaml anchor is
  the `file:` line, so a 3-line entry block starts at `file-line − 2` — its statement anchor at the line
  where the declaration opens, and the carrier's definition anchor. It flags thirteen injected mutants
  and writes nothing. Run `python3 notes/scripts/extract_counterexample_crosscheck.py` twice and diff:
  the report must be identical.
- Check `notes/t0-chains.md` with `python3 notes/scripts/verify_t0_chains.py --mutant` before quoting
  any of its counts — it resolves every `file:line` anchor (`.bib` files included), matches each fenced
  block against the **nearest preceding** anchor as joined text against the same number of source lines
  (so a one-line overview abstract re-wrapped across page lines still matches), pins each `*"…"*`
  quotation to the anchor in its own line or in the contiguous lines above it, re-derives the 12 count
  phrases and the 4 named family lists, requires the 28-row summary table and the 5-row chain table to
  equal the ledger, and requires each of the 28 blocks to carry exactly 2 manuscript bullets whose title
  is verbatim on the family's `\resultentry` line and whose path exists on disk. It flags twelve
  injected mutants and writes nothing. Run `python3 notes/scripts/extract_t0_chains.py` twice and diff:
  the report must be identical — 28 families over 56 manuscripts, 27 with zero coverage signal, 2 chain
  edges over 372 families, 10 `companion_word` families carrying 0 edges, 16 families citing their
  sibling (9 mutual, 7 one-way), and 8 reconciliation lines reading True.
- Measure the verification bundles with `python3 notes/scripts/extract_verification_dirs.py` (the 30
  bundles, which README section names them, and each bundle's entry point) and
  `python3 notes/scripts/extract_verification_348.py` (the family-348 pair); run each twice and diff:
  the report must be identical. Both read the bundles as text and run nothing. Check
  `notes/verification-dirs.md` with `python3 notes/scripts/verify_verification_dirs.py --mutant` before
  quoting either of its sections — it re-derives every bold count from the files on disk, resolves every
  `file:line` anchor, matches each fenced block line, checks each quotation against the anchored lines
  (a quotation with an anchor in its own table row must match at the anchored line exactly, so a shifted
  anchor is caught), re-checks the ledger's `verification`/`inputs`/`covmd` claims from
  `notes/catalog.tsv`, requires the entry-point table to carry one row per bundle in slug order with the
  family that slug belongs to, requires the two family-269 `rows.txt` files to be byte-identical,
  re-checks that every artifact `COVERAGE.md` names is on disk, and flags eighteen injected mutants
  including an abbreviated anchor and a deleted table row. It writes nothing.
- Check `notes/conjecture-standing.tsv` with `python3 notes/scripts/verify_conjecture_standing.py`
  before quoting any row — it proves the 139-row fam set against the ledger, resolves every
  `overview.tex:<n>` anchor to that family's own `\resultentry`, requires `prior_confidence` in
  vocabulary, rejects conjecture names the cited abstract does not use, and rejects consequence
  language.
- Run `python3 notes/scripts/extract_formalization_deps.py` twice and diff: the TSV must be
  byte-identical. Its report reconciles 31 rows = 30 declared + 1 undeclared, 30 lakefile requires
  pinned to 40-char commits, 30 yaml entries, 23 patches over 160,187 lines, 42 manifest packages
  = 30 declared + 12 transitive, 19 declared with zero direct imports, and 5 yaml ordering violations.
- Check `notes/dependency-drift.md` with `python3 notes/scripts/verify_dependency_drift.py --mutant`
  before quoting any dependency figure — it resolves all 52 `path:line` anchors (bare `:NNN` anchors
  against the nearest explicit file), matches all 7 blockquotes and every checked code span verbatim
  against `lean/lakefile.lean`, `lean/formalization.yaml`, the deps TSV, and the patch files, requires
  the 23-row patch table to equal the TSV row by row in descending order, requires each named library
  list to equal the measured set, and flags nine injected mutants. Its report reconciles the three
  surfaces independently: TSV patch lines == on-disk line sum == 160,187; the 11-library
  pre-resolution array == the 11 `lana-agents` URLs, disjoint from the 12-library `post_update` array,
  union == the 23 patched libraries; 19 zero-import with 14 patched and 5 not; medians 2,575 (any
  import) vs 408 (none). Run it twice and diff — the report must be identical. It writes nothing and
  never scans `lean/OAI/**/*.lean`; import counts come from the TSV.
- Run `python3 notes/scripts/extract_links.py` twice and diff: the TSV must be byte-identical and the
  report identical. Its report reconciles 22 rows, 415 link occurrences over 405 distinct configs,
  185 `main_results` entries over 178 unique configs in 127 families, 397 release-labelled bib
  entries over 396 resolved edges reaching 158 families, the legacy title proxy at 14 over 417
  `.bib` files (18 any / 12 cross over all 501), 0 MSC hits, 0 bib `keywords` fields, and 12
  `\keywords` directories.
- Run `python3 notes/scripts/build_index.py` twice and diff: `notes/index/` must be byte-identical and
  the report identical. Its report reconciles 372 family pages + 17 discipline pages + 92 topic pages
  + 552 name pages + 1 entry point (1,034 pages, 16 tables), 47354 relative links with 0 broken,
  canonical == rendered on families 372 / manuscripts 722 / formalized 162 / scope notes 235 /
  challenges 405 / traces 10 /
  verification dirs 30, `vs ledger` diffs of 0 on tier, `mainres`, `chal`, `paps` and `paps_form`,
  ledger↔overview family sets equal with 372 pages and 0 pages absent on disk, 11 trace files over 10
  attributed stems, 396 citation edges, 185 family-lean rows over 127 families, 405 configs (json 405,
  lean 405, 178 with a declaration, 0 linked by more than one family), 554 module dirs, 12 of 372
  summary pairings, 0 page collisions, manuscript links resolving for 722 of 722 on main file, `build/`
  and `README.md`, `drift vs notes/topics.tsv 0`, and the names line — 5,859 measured, 552 subject
  (552 pages), 5,307 citation-only, 9,883 edges over 372 families, 0 names with no family, 67
  singletons, max (233, `cauchy`), 329 with >1 prose spelling, trace families 10 of 10. Quote an index
  count with the report line it came from; the index is generated, so edit the generator and re-render
  rather than editing a page.
- Check the rendered index against the shipped files with
  `python3 notes/scripts/check_index_links.py` — report-only, ~1 s, exits non-zero on a broken link.
  It re-derives the check from disk: 1,034 pages, 65,690 links, 0 broken, of which 16,818 resolve to a
  directory (`manuscript-dir`, `latex-build-tree`, `lean-dir`, `verification-dir`, `index-dir`) and
  48,872 to a file, every shipped-file category equal to a fresh `build_catalog.py` count. The render
  report's 47,354 links are the registry's subset; the 18,336-link difference is registry
  under-coverage, not a disagreement about existence — both report 0 broken. Link scanning must be
  paren-balanced: `[^)]*` truncates
  `preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf` and invents a broken
  link, so the baseline is 0 broken links, not 1. `--mutant` runs the self-test (20 injected hrefs, one
  per category, all caught; 7 real hrefs, all resolving). Findings: `notes/index-links.md`.
- Run `python3 notes/scripts/measure_names.py` before quoting a name count: it re-derives every figure
  in `notes/names.md` from the corpus (6,975 `.tex` files, 15,755 titled statement environments,
  12,707 `.bib` entries over 5,831 author keys, 3,404 title candidates, 2,847 rejections by bucket).
  It writes nothing, so the pages are not its test — `notes/names.md` is the document it checks.
- Run `python3 notes/scripts/measure_topics.py --check` before quoting any topic count: it re-measures
  all 92 rows of `notes/topics.tsv` and exits 1 when a recorded per-layer count has drifted. Its
  report yields 92 terms over 372 families, 4 unassigned terms, 372 of 372 families covered, 971
  assignments, and the per-family topic histogram `1:97 2:100 3:86 4:53 5:19 6:13 7:2 8:1 9:1`. Quote a
  term with its per-layer counts, not its yield alone — a yield of 24 can be 2 titles and 16 scope
  notes.

## PR instructions

- Commit only when asked. One purpose per commit; stage explicit paths, never `git add -A`.
- Work on the `notes` branch. Keep `main` mirroring `upstream/main`.
- Push only to `origin` — `github.com/troberson/openai_math`, the fork. `upstream` is
  `github.com/openai/math` and is read-only. Confirm the destination with `git push --dry-run`.
- Track `.qwen/skills/` as repo content. Keep volatile tool state untracked: the rest of `.qwen/`
  (`pending-skills/`, `worktrees/`, `tmp/`) and `__pycache__/`.
- Match the existing message style: short imperative subject, blank line, body that explains why.
- Record manual reading findings as tracked files under `notes/`, one entry per family, stating
  exactly what each assumes and where the assumption sits.
- End coverage answers with what has not been checked.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project tracks issues with **bd (beads)** in **no-db mode**: `.beads/issues.jsonl` is the
issue store and it is tracked in git. There is no Dolt remote and no `bd dolt push` — the queue
travels with the `notes` branch like any other tracked file. Prefix is `math`.

- Find available work with `bd ready`, inspect with `bd show <id>`, claim with
  `bd update <id> --claim`, finish with `bd close <id>`; `bd prime` prints the workflow context.
- `bd ready` is the live queue. `notes/README.md` records findings, not task state — the task list
  lives only in bd, so nothing is tracked twice.
- The beads git hooks are active (`core.hooksPath` = `.beads/hooks`); the pre-commit hook re-exports
  `.beads/issues.jsonl` and stages it, so the tracked store is current in the commit whose work it
  records. By hand: `bd export -o .beads/issues.jsonl`.
- Findings belong in tracked files under `notes/`, not in bd memories — `bd remember` is not the
  record of record here.
- Repo rules outrank this section: commit only when asked, push only to `origin` (the fork) and
  only when asked, and never run `lake`, `lean`, `comparator`, or `bd dolt push`.
- `.claude/settings.json` runs `.beads/prime.sh` at SessionStart and PreCompact — `bd prime`
  followed by these same overrides, because stock `bd prime` demands a session-end `git push`,
  a Dolt remote, and `bd remember`, none of which apply here.
- `CLAUDE.md` is a pointer to this file, so beads rules live here only. A future `bd init` may
  re-insert its own block into `CLAUDE.md`; delete it.
<!-- END BEADS INTEGRATION -->
