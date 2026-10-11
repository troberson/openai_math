---
name: beads-git-only-init
description: Initialize bd (beads) so the issue store lives in git, not Dolt — the no-db config key
  (not an init flag), the .git/info/exclude trap that blocks tracking, export/hook behaviour (bd
  create does not re-export), the agent files `bd init` scaffolds (keep and revise CLAUDE.md), seeding
  an epic with sub-beads (--deps direction, --body-file absolute path, export-and-count before
  committing), encoding a recommended order as a linear dep chain, closing superseded beads with a
  pointer (--reason, epic refuses to close with a child open), and wrapping `bd prime` so its
  push-mandatory context cannot override repo rules.
source: auto-skill
extracted_at: '2026-10-07T08:30:15.038Z'
---

# Initializing beads with a git-tracked issue store

Worked out on `/home/tamara/Downloads/_Git/math` (bd 1.0.4, 2026-10-07): a repo whose conventions are
"commit only when asked, push only to a fork, no Dolt sync". The personal `beads-workflow` skill
describes `no-db: true` as an init-time switch; **that is out of date for 1.0.4** — `bd init --help`
says "Dolt is the default (and only supported) storage backend" and lists no `--no-db` flag. The
git-only mode is a config key, and the rest of the setup is manual.

## 1. no-db is a config key, not an init flag

```bash
bd init --prefix <p> --role maintainer --non-interactive   # creates .beads/ with an embedded Dolt DB
# then edit .beads/config.yaml:  uncomment -> no-db: true
bd config get no-db          # -> true  (this is the check that it took)
```

The embedded Dolt directory stays on disk (`du -sh .beads/embeddeddolt` ≈ 384K) and is still where
`bd config` reads from. It is ignored by `.beads/.gitignore`, so it never enters git. Do not delete it.

## 2. The trap that blocks git tracking: `.git/info/exclude`

`bd init` appends fork protection to `.git/info/exclude`:

```
.beads/
**/RECOVERY*.md
**/SESSION*.md
```

With `.beads/` there, the issue store can never be committed and `git status` shows nothing — the
silent failure mode. Delete the `.beads/` line, keep the two volatile patterns, and say why in a
comment. `.git/info/exclude` is local-only, so this does not touch collaborators or upstream.

Then extend `.beads/.gitignore` for the runtime files it does not cover by default
(`interactions.jsonl`, `hooks/`). Its closing note says "Do NOT add negation patterns here — they
would override fork protection in .git/info/exclude"; once you have removed that fork protection, the
note no longer applies, so record that in the file.

Track: `issues.jsonl`, `config.yaml`, `metadata.json`, `.gitignore`, `README.md`.
Ignore: `embeddeddolt/`, `backup/`, `hooks/`, `interactions.jsonl`, `export-state.json`,
`last-touched`, `.local_version`. Confirm with `git check-ignore -v` on each.

## 3. Export semantics — the file lags the database

- `bd export` writes to **stdout**. To write the tracked file: `bd export -o .beads/issues.jsonl`.
- Auto-export is enabled by default and **throttled to 60s**, so after a burst of `bd create` calls
  the JSONL is stale. Measured: 10 issues in the DB, 1 line in `issues.jsonl`.
- `export.git-add` (default true) auto-**stages** the export. A file can appear staged in
  `git status` without you staging it — check before committing anything else.

So: force an export and count lines before any commit that is supposed to carry the queue.

```bash
bd export -o .beads/issues.jsonl && wc -l < .beads/issues.jsonl
```

## 4. Hooks: init sets `core.hooksPath`, and that gates your commits

`bd init` sets `core.hooksPath = .beads/hooks` (pre-commit, pre-push, prepare-commit-msg,
post-checkout, post-merge). The pre-commit hook is the mechanism that keeps the tracked export fresh —
`BD_GIT_HOOK=1 bd hooks run pre-commit` re-exported all 10 issues.

Test every hook's exit code before trusting a commit or a push; a non-zero `pre-push` blocks pushes:

```bash
for h in pre-commit prepare-commit-msg post-checkout post-merge; do
  BD_GIT_HOOK=1 bd hooks run "$h" >/dev/null 2>&1; echo "$h exit=$?"
done
printf '' | BD_GIT_HOOK=1 bd hooks run pre-push origin <remote-url>; echo "pre-push exit=$?"
```

All 0 here, so beads gates nothing. If you do not want beads touching commits/pushes at all, unset it:
`git config --unset core.hooksPath` (then refresh the export by hand before committing).

## 5. Undo the side effects `bd init` makes

`bd init` (non-interactive) also:

- **Appends a block to `AGENTS.md`** demanding `git push` as mandatory session close, banning markdown
  TODO lists, and banning `MEMORY.md` in favour of `bd remember`. Rewrite the body between the
  `<!-- BEGIN/END BEADS INTEGRATION -->` markers to the repo's real rules; keep the markers.
- **Installs Claude Code integration**: `CLAUDE.md` (with `_Add your … here_` placeholder sections)
  plus `.claude/settings.json` running `bd prime` at SessionStart and PreCompact. **Keep both** —
  Claude Code files are standard in any repo now; deleting them is not the fix (offering deletion drew
  "claude code files are pretty standard now, keep them. revise if necessary"). Revise instead: put
  the rewritten beads block into `CLAUDE.md` too, and fill its `Build & Test` / `Architecture Overview`
  / `Conventions & Patterns` placeholders with real repo facts, verified from a fresh generator report.
  Then prove the two agent files agree:

  ```bash
  diff <(sed -n '/BEGIN BEADS/,/END BEADS/p' AGENTS.md) \
       <(sed -n '/BEGIN BEADS/,/END BEADS/p' CLAUDE.md)
  ```

  Expect exactly the cross-reference line to differ.
- **Adds to the tracked `.gitignore`**: `.dolt/`, `*.db`, `.beads-credential-key`. Keep.

## 6. `bd prime` injects rules that contradict the repo — wrap it

Prime is emphatic and generic, and the hooks call it before you see it. Run it yourself first:

```bash
bd prime | head -40
```

In a repo whose rules are "commit/push only when asked, push only to a fork, no Dolt, findings in
tracked markdown, memory files kept", prime collides on four counts: a "SESSION CLOSE PROTOCOL"
ending in `git add` + `git commit` + `git push` ("NEVER skip this. Work is not done until pushed"),
"Git workflow: beads auto-commit to Dolt, run `git push` at session end", "Memory: use
`bd remember` … Do NOT use MEMORY.md files", and "Prohibited: … markdown files for task tracking".
Prime's text is not configurable.

Fix: append the overrides after prime's output and point the hooks at the wrapper.

```bash
# .beads/prime.sh
#!/usr/bin/env bash
bd prime
cat <<'EOF'

## Repo overrides — these outrank the beads context above
- Do not commit or push unless the user asks. There is no session-end `git push`. `origin` is the
  fork; the upstream is read-only.
- No Dolt in this repo: bd runs in no-db mode and `.beads/issues.jsonl` is the tracked issue store.
  Never run `bd dolt push`.
- Findings are recorded in tracked files under the notes dir. `bd remember` is not the record of
  record, and memory files are kept.
EOF
```

```json
{ "command": "bash .beads/prime.sh", "type": "command" }   // SessionStart and PreCompact
```

Three checks: the JSON parses, the wrapper prints the override block, and the script is not swallowed
by `.beads/.gitignore` (`git check-ignore -v .beads/prime.sh` → exit 1). Name the wrapper in both
agent docs so a later agent does not "restore" the plain `bd prime`.


## 7. Prove nothing is wired to Dolt

```bash
bd dolt remote list                 # -> "No remotes configured."
git config --get beads.sync.remote  # blank
git remote -v                       # unchanged by init
```

Write in the repo's agent docs that there is no Dolt remote and no `bd dolt push`, so a future agent
does not "helpfully" push Dolt history to the fork.

## 8. Seed the queue from the repo's existing markdown TODO list

The point of initializing beads is to retire the markdown list. Create one epic, then children with
non-blocking `discovered-from:<epic>` deps (blocking deps would leave everything un-ready):

```bash
EPIC=$(printf '%s\n' "<umbrella description>" | bd create "Umbrella: ..." --description=- -t epic -p 2 --json | id_of)
printf '%s\n' "$BODY" | bd create "<title>" --description=- -t task -p 1 --deps "discovered-from:$EPIC" --json
bd ready        # children should all be ready
bd graph --all --box
```

Use `--description=-` with stdin for any text containing quotes, apostrophes, or slashes.

- **`bd ready`'s row glyphs are not the status legend.** Measured on bd 1.0.4: each ready row prints
  `○` (its status, open), then `●` as the **priority separator** before `P2`, and the legend at the
  bottom of the same output spells `●` "blocked". A reader scanning the rows sees `●` in every line
  and reads a fully-ready queue as fully blocked. The status glyph is the first one; confirm with the
  JSON and read the field:

  ```bash
  bd list --status=open --json | python3 -c 'import sys,json; d=json.load(sys.stdin); \
  rows=d["data"] if isinstance(d,dict) else d; [print(r["status"], r["priority"], r["id"]) for r in rows]'
  ```

  (Bare array without `BD_JSON_ENVELOPE=1`, envelope `{"data": [...]}` with it.)

**Verify every number you put in a description against the artifact, and scope it.** Here the repo's
follow-up list said "the 28 two-manuscript families"; the ledger says 96 families have exactly 2
manuscripts. The 28 are a named subset of one reading pass. Write the subset with its list and state
the repo-wide count, or the issue becomes a false census.

## 8b. Turning measured options into an epic with sub-beads

When an investigation ends in priced options, the follow-through is one epic plus one bead per fix.
The syntax details that cost time:

```bash
bd create "<umbrella>" --type epic --priority P2 --body-file /abs/path/epic.md      # ABSOLUTE path
bd create "<fix title>" --parent <epic> --priority P2 --body-file /abs/path/b1.md
bd create "<close>"    --parent <epic> --priority P2 --deps "epic.1,epic.2" --body-file /abs/path/b6.md
bd show <close-id>      # DEPENDS ON: epic.1 epic.2 ...  — verify the direction, do not assume it
```

- **`--deps` direction.** Bare ids mean *this issue depends on those*. A `blocks:` prefix makes the
  **new** issue the blocker of the named one — the inverse of what you asked for, and it silently
  empties `bd ready`. Use bare ids for a dependent; verify with `bd show`.
- **`--body-file` needs an absolute path**; a relative one fails. For inline text use
  `--description=-` with stdin.
- `bd create --help` lists `--type (bug|feature|task|epic|chore|decision)`.
- **Give the close-out bead deps on every fix bead.** It then stays out of `bd ready` until the work
  lands, which is what you want for a "sweep the docs and run the full gate" bead.

**What goes in each body.** The epic carries the baseline measurement with its rule, the concentration
("4 rows = 58 % of a pass"), and the **scope boundary against other tracked epics** ("this epic is
wall time; the join refactoring epic does not overlap; the read cache belongs here"). Each fix bead
carries: the measured evidence, the change, the **measured saving**, the **risk to the byte-identity
proof**, and its **prove list** (which checkers, plain and `--mutant`, which gate rows, the lint
driver, the promote-and-verify assertion). A body with a prove list is a bead a later session can
execute cold.

**Then export before you commit** — `bd create` does not re-export the tracked store (§3):

```bash
bd export -o .beads/issues.jsonl && wc -l < .beads/issues.jsonl && grep -c '<prefix>' .beads/issues.jsonl
```

Measured: after creating 7 issues the file still read 105 lines with **zero** of them. Commit the
store as its **own commit** (one purpose per commit), then the code/docs as separate commits, and
confirm with `git show --stat` that the code commit carries no store lines (the pre-commit hook
re-exports and stages them otherwise).

**When the instruction is "add these as beads, don't claim them / don't begin implementation":**
create, export, commit, push, and **stop**. Report the ids, the dependency verification, the commit
shas, and say explicitly that the new rows sit in `bd ready` as *not-claimable* work. Claiming one is
the failure mode the instruction exists to prevent.

## 8c. Encoding a recommended order, and superseding beads a new epic absorbs

**Recommended sequence ⇒ linear dependency chain, not a flat sibling set.** Give each child `--deps`
on its predecessor:

```bash
bd create "step 2 ..." --parent <epic> --priority P2 --deps "<epic>.1" --body-file /abs/b2.md
bd show <epic>.2      # DEPENDS ON: <epic>.1
bd ready              # only .1 is claimable — the order is now enforced by the tracker
```

This is how "go with your recommendation" survives into a later session: the queue itself refuses the
out-of-order claim. Verify with `bd ready` that exactly one new row appeared.

**When a new design subsumes beads that already exist, close them with a pointer — never delete,
never leave them open next to their replacement.** Two epics carrying the same fixes makes `bd ready`
a lie.

```bash
bd close <epic>.1 --reason "Superseded by <new>.4 — <what replaces it>."
bd close <epic>.4 --reason "Superseded by <new>.4. The <scope rule> survives, restated as: <rule>."
bd close <epic>.5 --reason "Moved into <new>.5, which adds the <precondition> this bead needed."
```

- `bd close` takes `--reason` (and `--reason-file`); there is **no `--note`**.
- **An epic refuses to close while a child is open.** Close the absorbed children, keep the doc-sweep
  child open, and the epic stays open legitimately — say so in the report.
- Record in each reason **what survives** from the old bead, not only what is superseded, and record
  **where** it moved, so the store and the docs agree.
- Re-scope in the same pass as the creation, then export and count both prefixes:
  `grep -c '<new-prefix>' .beads/issues.jsonl && grep -c '<old-prefix>' .beads/issues.jsonl`.

Report the ready-queue delta with its cause (5 closed, 1 newly claimable ⇒ 24 → 19), never as a bare
count.

## 9. Do not commit unasked

bd stages `.beads/issues.jsonl` on its own. Report the change, propose the split (setup + git wiring;
agent-docs section as its own commit), and wait for the word "commit". Push only on its own
instruction, after `git push --dry-run`, to the writable remote only.
