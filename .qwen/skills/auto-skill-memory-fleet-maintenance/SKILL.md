---
name: memory-fleet-maintenance
description: Run a /dream-style memory-consolidation pass that survives the manager-owned MEMORY.md index — census pointers vs files, re-measure every fact a memory cites against the repo before rewriting, root-cause a registry gap through the frontmatter index gate, measure sizes, fix category values, split only at a usage_scenarios boundary, and report what is left undone honestly.
source: auto-skill
extracted_at: '2026-10-10T20:07:52.881Z'
---

# Maintaining a memory fleet

Use for a memory-maintenance / "dream" pass over `~/.qwen/memories/` (user scope) and
`~/.qwen/projects/<hash>/memory/` (project scope). Worked end to end 2026-10-10 on a 70-file project
fleet plus a 61-file user fleet (post-pass census, §0). Re-measured 2026-10-11 with the §0 commands:
user **67** files / **66** pointers, project **85** files / **85** pointers — the fleet grows between
passes, so re-census rather than quoting the recorded pair. The two scopes have **separate `MEMORY.md`
indexes** — never cross-reference them.

## 0. Census before you touch anything

```sh
cd <memory-dir>
ls -1 */*.md | wc -l                      # memory files
grep -c '^- \[' MEMORY.md                 # index pointers
grep -o '\](\([a-z_]*/[a-z0-9._-]*\.md\))' MEMORY.md | sed 's/](//;s/)//' | sort -u > /tmp/ptrs
ls -1 */*.md | sort -u > /tmp/files
comm -23 /tmp/files /tmp/ptrs    # unindexed memories
comm -13 /tmp/files /tmp/ptrs    # dangling pointers
uniq -d /tmp/ptrs                # duplicate pointers
for f in */*.md; do for k in name description type category keywords usage_scenarios; do
  grep -q "^$k:" "$f" || echo "$f missing $k"; done; done
```

The subdirectory names are a **mix of type names and category names** — measured:
`user/ feedback/ reference/ tool_experience/` (user scope) and
`project/ feedback/ reference/ tool_experience/ common_pitfall/` (project scope). A hard-coded prefix
list silently under-reports: the 5-prefix pattern `(project\|reference\|feedback\|tool_experience\|
common_pitfall)` misses `user/`, which makes every `user/` memory look unindexed. Match `[a-z_]*/`.

Test field **presence** (`grep -q '^<field>:'`), never validity: a present-but-invalid `category:` is
caught by the §2 census, and a validity test here reports every file as broken.

Count pointers with `grep -c '^- \['`, **not** `wc -l`: the last line usually has no trailing
newline, so `wc -l` reads one short. A run of `comm`/`uniq` that prints nothing is a *result* —
report it as 0, not as a failed command. Never pipe a census through `head`: it truncates the list
and under-reports.

Sizes: use `wc -m` (**characters**), not `wc -c`. These files are full of em dashes, curly quotes
and guillemets, so a byte count overstates every size by 5–10% and a "over 2,400" gate misfires.

## 1. The index is manager-owned — plan around it

`MEMORY.md` is **output, not source**. `write_file` and `edit` both report success and echo the new
content, and `stat` shows a fresh mtime, while the file on disk stays the manager's version with its
own (often `…`-truncated) hooks. Measured twice in one session: a 61-line rewrite and a 6-pointer
append both reverted; disk stayed at 55 pointers / 7870 bytes with a 12:59:29 mtime. No registry
file sits alongside it (`ls -la` shows only `MEMORY.md` + the type dirs).

Consequences:

- **Never hand-edit the index to add entries.** Write the memory's own `.md` with complete
  frontmatter — that is what persists — and let the manager rebuild the index.
- **Verify index state from the shell**, never from the tool's echoed content.
- **The index gate is the frontmatter.** A memory gets a pointer iff its frontmatter **parses** and
  its `type:` is one of `user / feedback / project / reference`. A `type:` copied from the category
  list (`tool_experience`, `common_pitfall`, `practice_standard`) is invisible to the indexer, so a
  whole directory of well-written memories sits unindexed. Root-cause a registry gap by reading the
  `type:` values (`grep -h '^type:' */*.md | sort | uniq -c`), fix the **field**, and the index
  rebuilds on the next write.
- An unindexed memory file is a **registry gap, not a broken link**. Report it as such, with the
  counts, and say the fix needs the memory manager. Do not "fix" it by writing a parallel index.

## 2. Fix `category` values against the fixed list

```sh
grep -h '^category:' */*.md | sort | uniq -c
```

`type:` (user / feedback / project / reference) and `category:` are **different fields**. The
category list is fixed: `basic_information, hobbies, communication_preference, behavior_habit,
project_introduction, tech_stack, build_configuration, dependency_configuration, ide_configuration,
scm_configuration, environment_configuration, code_standard, practice_standard, testing_standard,
comment_standard, tool_experience, mcp_experience, common_pitfall, important_decision, task_summary`.
Values copied from the type names (`feedback`, `reference`, `project`) are the usual offenders — map
them by what the memory *is*: a durable working habit → `behavior_habit`; a tool quirk →
`tool_experience`; a repo trap → `common_pitfall`. Never invent a nested category.

## 2b. Facts decay faster than rules — verify against the repo before rewriting

In a repo where work lands between passes, **the dominant failure is not duplication, it is a memory
whose fact has inverted.** Measured 2026-10-11 on a 77-file project fleet: 7 of 77 memories asserted a
state the repo no longer had, and only 2 pairs were genuine duplicates. Work the facts first.

For every memory naming a file, function, count, path, queue, or line number, re-measure it before you
touch the file:

- `ls <path>` / `grep -l <symbol> notes/scripts/*.py` — does the thing exist?
- `grep -c` / `find … | wc -l` / `grep -o … | wc -l` — is the count the memory quotes still the count?
- `bd ready` / the generator's report / the page's own table — for a queue, a census, a tier count.

Stale claims found in one pass, all caught by a one-line shell measure: "atomic promotion is 0 %
implemented" (the registry `catlib/promote.py` existed); "404 sorries" (measured 539 over 416 files);
"121,734 files / 25.9M lines" (measured 122,458 / 26,060,031); "67 invocations over 49 scripts,
2,006 s per pass" (measured 2026-10-11: **75** invocations over **56** scripts — the row count moves
with every bead, so re-count from `notes/scripts/gate.py`'s `ROWS`); "387 lines" (measured 503);
"nothing implemented, only `.1` claimable" (the epic was closed); "15 scripts carry a sync pass"
(measured 2026-10-11: **13**, all checkers — `grep -rlE 'sync problems' notes/scripts/*.py | wc -l`).

**When a fact inverts, rename the file and delete the old one.** The slug is part of the retrieval
surface: a file named `writers-have-no-atomic-promotion.md` keeps asserting the false claim even after
its body is rewritten, and a future agent reads the name before the body. Write the new file with
complete frontmatter, confirm it gets indexed, then `rm` the old one, then re-run the §0 census — the
dangling pointer to a deleted file clears itself on the next index regeneration, so do not hand-edit the
index to remove it.

**Never store a number a fresh run re-derives.** A script's line count, a live queue size, a tier count,
a census total all drift with every bead. Replace the number with the command that prints it ("re-measure
from `bd ready`", "read the tier table from `notes/README.md`"). Measured drift: one script's line count
went 387 → 503 in four days.

## 3. Compress by moving procedure into skills, not by trimming rules

Frontmatter (name, description, keywords, usage_scenarios) is ~700 characters of fixed cost, so a
2,400-character budget leaves ~1,700 for the body. Order of operations:

1. **Point at the owner.** If a skill carries the mechanics (`AGENTS.md`-style repos put procedures
   in skills, not memories), replace the procedure text with a one-line pointer to it. Same for a
   fact that lives in another memory — one owner, one pointer.
2. **Drop dated incident narrative** — the play-by-play of how a number was discovered. Keep the
   date on a ruling, drop the story around it.
3. **Drop anything a fresh run re-derives** — counts a generator prints, live queue sizes, current
   HEAD. Add "never quote the live count from this memory; the command is `bd ready`".
4. **Keep every durable rule, plus `Why:` and `How to apply:` verbatim in substance.** A compression
   that loses a rule is worse than one that stays over the bar.

Measured 2026-10-10 on 20 over-bar files: **steps 1–3 buy 3–12 % on the first pass and most files are
still over 2,400 afterwards — budget a second pass of the same steps**, which buys the rest. Size
estimates land 10–15 % high, so target ~2,200 to land ≤2,400. Cheapest levers, measured per cut:
one keyword ≈35–45 chars, one `usage_scenario` ≈40–50, a shortened `description` ≈40–60, a dropped
shell snippet ≈90, a deleted dated incident narrative ≈80–130, pointing at the owning skill / tracked
file / sibling memory instead of restating ≈110–230.

When trimming stalls, **split at a semantic retrieval boundary** — that is the biggest yield, and it
beats more trimming on a dense rule list (measured: a 2,667-char rule list split into 1,700 + 1,250
with a pointer line in each half). A split is only legitimate if each half is independently retrievable
and no rule is lost; give the new file complete frontmatter and confirm it gets indexed.

**The checkable test is the file's own `usage_scenarios`.** If they already name two distinct tasks,
the boundary is real and the split is legitimate. If the memory is one rule with one `Why:`, compress it
and do not split — splitting a single rule cuts at a character position, not a retrieval boundary.
Measured 2026-10-11: 3 files split (2,788 → 2,243 + 1,942; 2,408 → 2,088 + 1,697; 2,406 → 1,896 + 1,664)
and 5 left whole at 2,065–2,402. Put a pointer line in each half.

## 4. Merge duplication by ownership, not by deletion

When two memories restate the same rule, pick the owner (the narrower, named topic), move the rule
there, and leave a pointer in the other. Delete only after the replacement is on disk and the
surviving text is verified — and only when no unique rule lives in the file. "Nothing pruned" is a
legitimate result of a maintenance pass; say it plainly.

Before writing any new memory, check for a duplicate:
`ls -1 */*.md; grep -l <topic> */*.md`.

## 5. Tool gates that bite here

- `write_file` / `edit` require a real `read_file` on that exact path **immediately before** the
  call. A read early in a long tool sequence, and any "file was restored" notice, do not satisfy it.
  A windowed read is enough for `edit`.
- **A shell `cat`/`sed` dump is not a prior read.** `write_file` on an existing memory was rejected
  ("has not been read in this session … overwriting replaces every byte") after the only prior view of
  that file was a shell `cat`. A `read_file` on that exact path in the **immediately preceding message**
  does satisfy it: measured 2026-10-11, `read_file` → `write_file` succeeded 8 times in one pass on
  memory files. So the gate is the prior read, not the tool. Prefer `edit` for a trim (it needs only a
  windowed read); use `write_file` for a rewrite, a split's new file, or a rename.
- **The prior-read record expires when the read's result is compacted out of context.** A long
  maintenance pass hits this repeatedly: `edit` fails with "File … has not been read in this session"
  right after a successful `edit` on the same file. Fix: re-`read_file`, then `edit` in the
  **immediately following message** — do not interleave a shell command between them.
- **`old_string` must be copied from the read output, never authored from memory** — a remembered
  paraphrase gives "0 occurrences found, no edits made". If an edit fails on target text you
  reconstructed, re-read and check whether the target exists at all before retrying.
- A shell `sed`/`cat` dump is **not** a prior read; only `read_file` satisfies enforcement.
- A compound shell command ending in a non-matching `grep` exits 1. That is not a failure; read the
  stdout.
- Relative dates in memories → absolute dates, every pass.

## 6. Report

Deliver what the task asks (consolidated / updated / pruned) plus **what was not done**: files still
over the size bar with their counts, the index registry gap, and any repo state the pass left
untouched (`git status --porcelain` — an auto-skill directory created by the generator is often
untracked; report it, do not stage it unasked). Quote counts from the census commands you ran, not
from the tool responses you saw.
