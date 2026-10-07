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
  `t0-triage.md`, `conditional.md`, `resolution-tag.md`, `counterexample-tag.md`,
  `verification-dirs.md`, `summaries-workflow.md` (the resume protocol for the summary batches),
  `conjecture-standing.tsv` (139 rows, 10 columns — a labeled training-data prior, not a fact) with
  `conjecture-standing.md` beside it, `formalization-deps.tsv` (31 rows, 8 columns — the upstream
  library graph) with `formalization-deps.md` beside it, `links.tsv` (22 rows, 7 columns — the
  typed-edge inventory) with `links.md` beside it, `scope-exclusions.md` (235 rows — what each scope
  note says its formalization leaves out), `subfindings.tsv` (1137 rows — 722 manuscript rows and 415
  comparator rows, typed by a `kind` column) with `subfinding-pairs.md` (49 families, 206 manuscripts —
  the reading pass that pairs abstract clauses with display titles) beside it,
  `summaries/<discipline>/<NNN>-<name>.md`, `notes/scripts/`.
- `.beads/issues.jsonl` is the tracked issue store, in bd no-db mode; see the beads section below.

## Dev environment tips

- Regenerate the ledger with `python3 notes/scripts/build_catalog.py` — stdlib only, runs in
  seconds, writes `notes/catalog.tsv` and prints the report that every number in
  `notes/README.md` comes from.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`. `lean/OAI/` is 121,734 files
  and 25.9M lines; a build is hours on a desktop and buys nothing for categorization.
- Parse `notes/catalog.tsv` with `csv.DictReader(..., delimiter='\t')`, never `split(',')`.
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
- Attribute reasoning traces from the table in `README.md`, never by guessing from filenames.
- Bucket the T0 families with `python3 notes/scripts/triage_t0.py` — it reads `notes/catalog.tsv`,
  writes nothing, and reconciles 137 families over 255 manuscripts. Findings live in
  `notes/t0-triage.md`.
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
- Check `notes/conjecture-standing.tsv` with `python3 notes/scripts/verify_conjecture_standing.py`
  before quoting any row — it proves the 139-row fam set against the ledger, resolves every
  `overview.tex:<n>` anchor to that family's own `\resultentry`, requires `prior_confidence` in
  vocabulary, rejects conjecture names the cited abstract does not use, and rejects consequence
  language.
- Run `python3 notes/scripts/extract_formalization_deps.py` twice and diff: the TSV must be
  byte-identical. Its report reconciles 31 rows = 30 declared + 1 undeclared, 30 lakefile requires
  pinned to 40-char commits, 30 yaml entries, 23 patches over 160,187 lines, 42 manifest packages
  = 30 declared + 12 transitive, 19 declared with zero direct imports, and 5 yaml ordering violations.
- Run `python3 notes/scripts/extract_links.py` twice and diff: the TSV must be byte-identical and the
  report identical. Its report reconciles 22 rows, 415 link occurrences over 405 distinct configs,
  185 `main_results` entries over 178 unique configs in 127 families, 397 release-labelled bib
  entries over 396 resolved edges reaching 158 families, the legacy title proxy at 14 over 417
  `.bib` files (18 any / 12 cross over all 501), 0 MSC hits, 0 bib `keywords` fields, and 12
  `\keywords` directories.

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
