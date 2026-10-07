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
  library graph) with `formalization-deps.md` beside it,
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
- Read `lean/docs/<NNN>.md` before claiming what a family proves; its `## Scope` section states
  the exclusions, which are the load-bearing part.
- Attribute reasoning traces from the table in `README.md`, never by guessing from filenames.
- Bucket the T0 families with `python3 notes/scripts/triage_t0.py` — it reads `notes/catalog.tsv`,
  writes nothing, and reconciles 137 families over 255 manuscripts. Findings live in
  `notes/t0-triage.md`.
- Quote `notes/conjecture-standing.tsv` as a prior, never as a literature fact. Its
  `standing_prior_2025` column is the assistant's training-data memory at an early-2025 cutoff,
  self-rated by `prior_confidence`; the repo supplies only `release_claim` and `abstract_line`.
  No row may assert consequence — consequence is external here: only 14 of 372 family titles appear
  in the corpus's own `.bib` files, so intra-corpus consequence is unmeasurable.
- Extract the upstream library graph with `python3 notes/scripts/extract_formalization_deps.py`. It
  reads all 121,734 `lean/OAI/**/*.lean` files, so it takes minutes, not seconds, and it refuses to
  write the TSV when a join breaks. Import counts are over `lean/OAI/**/*.lean` — the whole tree
  yields OAI 277,501 / Mathlib 56,715, not the 276,599 / 56,196 the table records, so quote the scope
  with the number. `lean/lake-manifest.json` is read for the report only, never for a column.
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
  every quotation against the lines it cites, and writes nothing.
- Check `notes/conjecture-standing.tsv` with `python3 notes/scripts/verify_conjecture_standing.py`
  before quoting any row — it proves the 139-row fam set against the ledger, resolves every
  `overview.tex:<n>` anchor to that family's own `\resultentry`, requires `prior_confidence` in
  vocabulary, rejects conjecture names the cited abstract does not use, and rejects consequence
  language.
- Run `python3 notes/scripts/extract_formalization_deps.py` twice and diff: the TSV must be
  byte-identical. Its report reconciles 31 rows = 30 declared + 1 undeclared, 30 lakefile requires
  pinned to 40-char commits, 30 yaml entries, 23 patches over 160,187 lines, 42 manifest packages
  = 30 declared + 12 transitive, 19 declared with zero direct imports, and 5 yaml ordering violations.

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
