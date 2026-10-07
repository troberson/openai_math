# AGENTS.md

Companion to `README.md`: context and rules for agents working on the OpenAI Research Catalog
notes. Reading tool, not a verification tool.

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
- Absence of formalization is not a red flag — 560 of 722 manuscripts are unformalized.
- Read `lean/docs/<NNN>.md` before claiming what a family proves; its `## Scope` section states
  the exclusions, which are the load-bearing part.
- Attribute reasoning traces from the table in `README.md`, never by guessing from filenames.
- Bucket the T0 families with `python3 notes/scripts/triage_t0.py` — it reads `notes/catalog.tsv`,
  writes nothing, and reconciles 137 families over 255 manuscripts. Findings live in
  `notes/t0-triage.md`.
- Project skills live in `.qwen/skills/` — `proof-triage` routes ledger work,
  `auto-skill-lean-formalization-coverage-audit` carries the measurement method.

## Testing instructions

- Run the generator twice and diff the output: `notes/catalog.tsv` must be byte-identical.
- Check the report's reconciliation lines after every change: 372 families, 722 manuscripts,
  162 formalized, and both `overview.tex` ↔ `CONTENTS.md` cross-checks reading 0.
- Confirm the discipline table sums to 372 / 235 / 722 / 162.
- Quote a count only from a fresh generator report, never from a previous run's output.
- Confirm a new tag discriminates before quoting it: the `conditional` tag flagged 9 families and
  5 were not assumptions. `notes/conditional.md` is the model for a reading pass.
- Parenthesized manuscript paths need `preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf`; excluding
  `{}` and `\` is what stops a phantom 723rd manuscript.

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
