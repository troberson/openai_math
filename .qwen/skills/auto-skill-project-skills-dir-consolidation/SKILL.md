---
name: project-skills-dir-consolidation
description: Merge a project's skills split across .qwen/skills and .agents/skills into one directory, track it in git with a re-inclusion .gitignore, and fix every document that still names the abandoned path.
source: auto-skill
extracted_at: '2026-10-07T06:20:08.050Z'
---

# Consolidating a split project-skills directory

Use when a project's skills sit in **both** `<project>/.qwen/skills/` and
`<project>/.agents/skills/`, and the user asks to pick one — "forget the .agents plan and only use
.qwen" — usually together with "we want to track `.qwen` in this repo". Worked end to end on
2026-10-06 in the OpenAI math catalog repo.

## 0. Know the discovery rule before moving anything

Qwen Code discovers **project** skills in both locations (verified 2026-10-06 in the installed
chunks: `PROJECT_SKILL_DIRS=[".qwen",".agents"]`, `SKILLS_DIR="skills"`). So relocating a skill
tree is **lossless** — no settings change, no restart; the skill list refreshes live.

The asymmetry that causes the split: auto-skill generation writes new skills to `.qwen/skills/`,
and auto-skill maintenance only manages `.qwen/skills/auto-skill-*`. A hand-authored tree parked in
`.agents/skills/` stays discoverable, but the next generated skill re-creates `.qwen/skills/` and
the tree splits again. **If the user wants exactly one directory, `.qwen/skills/` is the one that
stays whole.** Ask which they want; do not assume the tool-agnostic `.agents` layout.

## 1. Inventory both trees and check for collisions first

```sh
find .agents -type f | sort
find .qwen   -type f | sort
ls .agents/skills .qwen/skills
```

Compare **directory names**, not file contents. Only move when the two sets are disjoint. On a name
collision, diff the two `SKILL.md` files, keep the more complete one, and say which won — never move
over a same-named skill. "Make sure you don't clobber any duplicates" is satisfied by this check,
not by a force flag.

## 2. Move, then remove the emptied source tree

Plain `mv` of each skill directory. Delete the source tree only after `find <src> -type f` returns
nothing, and confirm the target count equals the pre-move total.

## 3. Track the skills, ignore the rest of the tool directory

```
.qwen/*
!.qwen/skills/
__pycache__/
```

**Single star, not `**`.** `*` does not cross `/`, so files under `.qwen/skills/` are unmatched by
`.qwen/*` and stay addable once the directory itself is re-included. A `**` pattern matches those
files themselves, and git cannot re-include a file whose parent path is excluded — the directory
negation alone would not rescue them. Verify rather than assume:

```sh
git check-ignore -v .qwen/pending-skills .qwen/skills/<one-skill>/SKILL.md
git add -n .qwen
```

Expected: volatile state (`pending-skills/`, `worktrees/`, `tmp/`, `settings.json`) ignored; every
`SKILL.md` listed by `git add -n`. Quote this output in the report — it is the evidence that the
re-inclusion works.

## 4. Fix every document that names the abandoned path

```sh
grep -rn "\.agents" notes .qwen AGENTS.md README.md
```

Two classes of stale text, both needing targeted edits (not section rewrites):

- **`AGENTS.md`** — the bullet naming the skills home, and the "never commit tool state" bullet,
  which *inverts*: it becomes "track `.qwen/skills/`; keep `pending-skills/`, `worktrees/`, `tmp/`,
  `__pycache__/` untracked". Re-audit with the `agents-md` skill's script afterwards.
- **Skills that give tracking advice** contradicting the new rule (an auto-skill saying `.qwen/`
  stays untracked). Update the advice to name volatile state specifically and defer the skills
  question to the project's `AGENTS.md`.

Also update any memory that recorded the split as the current state.

## 5. Expect auto-skill frontmatter names to differ from directory names

`auto-skill-foo/SKILL.md` carries `name: foo`. That is how the generator writes them, and discovery
works — confirm from the live skill list. Do not "fix" the name to match the directory.

## 6. Commit, then say what a push publishes

One purpose per commit: `.gitignore` + `AGENTS.md` + the skill files, staged by explicit path.
Flag two consequences before pushing: a root `.gitignore` is **new repo content** that upstream may
not have, and tracking the skills means **the push publishes them**.

## Checks before reporting "done"

- Source tree gone; target directory holds every skill; counts match the inventory.
- `git check-ignore -v` and `git add -n` output quoted, not paraphrased.
- No remaining references to the abandoned directory.
- `AGENTS.md` audit exit code quoted.
- Stated explicitly: which files become public on the next push.
