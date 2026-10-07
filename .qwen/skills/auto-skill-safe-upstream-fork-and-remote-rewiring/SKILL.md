---
name: safe-upstream-fork-and-remote-rewiring
description: Take a clone of an upstream repo you cannot push to, fork it with gh, and rewire remotes so a bare `git push` can never target upstream — with evidence that nothing was published.
source: auto-skill
extracted_at: '2026-10-07T06:01:22.180Z'
---

# Forking an upstream you cannot push to

Use when a repo was cloned from someone else's org (here: `github.com/openai/math`) and the user
asks "am I committing to *their* repo?", "fork it", or "make push go to the fork". Worked out on
2026-10-06 with local commits already on disk and nothing published.

## 0. Answer the safety question with evidence, not reassurance

There is no git record of "we did not push", so prove it three ways:

```sh
git remote -v                                   # where does origin point?
git log --oneline upstream/main..HEAD           # local commits not in upstream
git push --dry-run                              # destination, without writing
gh auth status
gh api repos/<org>/<repo> --jq '{admin:.permissions.admin, push:.permissions.push}'
```

If `admin` and `push` are both `null`, the token cannot write to upstream at all. Say that, not
"I would not have done it".

## 1. Create the fork — and expect the CLI to be silent

```sh
gh repo fork <org>/<repo> --fork-name <name> --remote --remote-name <local-name>
```

Verified gotcha: this can print **no output** and add **no remote** — `git remote -v` comes back
unchanged. Silence is not failure. Verify server-side before concluding anything:

```sh
gh api repos/<you>/<name> --jq '{fork, parent:.parent.full_name, visibility, sha:.sha}'
```

- If the fork's `sha` equals the upstream head, **forking published nothing**. Publishing happens
  on push, never on fork — say this explicitly, it is the user's real worry.
- The fork defaults to **PUBLIC**. If the content is sensitive, fix visibility *before* the first
  push: `gh repo edit <you>/<name> --visibility private`.
- **Do not re-run `gh repo fork`** — the fork already exists, and re-running re-adds remotes or
  errors. Add the remote by hand: `git remote add <local-name> <fork-url>`.

## 2. Rewire so a bare `git push` can never hit upstream

```sh
git remote rename origin upstream
git remote set-url origin  https://github.com/<you>/<name>.git
git remote set-url --push upstream no-push      # any push to upstream now fails
git remote -v
```

The `--push` line is the load-bearing one: renaming remotes alone still leaves upstream pushable.
`git remote -v` must show `upstream` with a fetch URL **and** a separate push URL of `no-push`.
Confirm the destination with `git push --dry-run` before every real push.

## 3. Keep the work off the mirror branch

```sh
git switch -c notes                             # carries the local commits
git switch main && git reset --hard upstream/main
git branch --set-upstream-to=upstream/main main
```

`main` mirrors upstream; all local work lives on `notes`; publish with `git push -u origin notes`.
Before pushing, list exactly what will become public: `git log --oneline origin/notes..notes`.

## 4. Keep tool state out of the fork

Volatile tool state stays untracked — `.qwen/pending-skills/`, `.qwen/worktrees/`, `.qwen/tmp/`,
`__pycache__/`. Track `.qwen/skills/` only when the project's `AGENTS.md` says the skills are repo
content; otherwise it is tool state too. Stage explicit paths, never `git add -A`.
Generated caches get a scoped `.gitignore` (e.g. `notes/scripts/.gitignore` containing
`__pycache__/`) rather than being deleted.

## Checks before reporting "done"

- `git remote -v`: origin = fork (fetch + push), upstream = fetch-only.
- `git push --dry-run` prints the fork URL.
- Fork visibility is what the user intends.
- The user's commits are on a working branch, `main` matches `upstream/main`.
- Nothing was pushed — and nothing will be until the user says so.
