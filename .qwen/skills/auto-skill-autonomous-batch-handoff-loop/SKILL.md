---
name: autonomous-batch-handoff-loop
description: Run a long unattended batch of work so a compaction cannot lose the plot — a handoff doc as the state carrier, a loop as the cadence, a fixed gate list, stop/escalate rules, and an append-only decision ledger.
source: auto-skill
extracted_at: '2026-10-07T11:35:37.517Z'
---

# Long autonomous batch runs that survive compaction

For a run measured in tens of batches (generate N pages / records / migrations from a corpus), where
the agent doing the work will be compacted many times. Worked out on the OpenAI Research Catalog
(`/home/tamara/Downloads/_Git/math`) for the `notes/summaries/` production plan: 370 pages over 713
manuscripts, sharded into beads issues.

## 1. Handoff and loop are orthogonal — you need both

Asked "handoff document **or** loop?", the answer is not a choice:

- A **handoff document is a state carrier**. It survives compaction.
- A **loop is cadence**. It makes the run wake up without a human typing.

A loop with no handoff file re-derives everything on every wakeup. A handoff file with no loop still
needs a human to say "continue". Say this explicitly when the user frames it as an either/or.

## 2. Write the handoff file before the first batch, not after the first loss

Name it after the work, in the tracked docs dir: `notes/summaries-workflow.md`. Contents, in order:

1. **Loop shape** — one sentence on who does the work (see step 6).
2. **Per-item steps, numbered** — the exact sequence for one page/record, ending at the commit.
3. **Gates** — exact commands, plus the numbers that must not move (step 4).
4. **Stop and escalate rules** (step 5).
5. **Tier/partition table** with counts, so the next session does not re-measure the corpus.
6. **"What not to re-derive"** — pointers to the skill that carries the format, the measured cost
   model, the one-tracker rule, the forbidden commands.
7. **Decision points** — append-only (step 3).

Rules that make it usable after a compaction:

- **Overwrite at each batch boundary; do not append.** Appending turns the resume file into a
  transcript, which is the thing you are trying to escape. Keep it ~60 lines.
- It carries only what the durable stores cannot: the **in-progress item**, the **last gate run's
  numbers**, the **next concrete action**, open decision points.
- **No task list in it.** If the repo tracks issues (bd, beads), the queue lives there and a second
  copy drifts. State that in the file.
- Point at it from the agent-instructions file (`AGENTS.md` repository map) and the docs README. A
  resume file nobody can find is not a resume file.

## 3. Decision ledger: record the ambiguity, do not stop and do not guess silently

Unattended runs die on both failure modes — asking a question nobody answers, and inventing an answer
nobody chose. Protocol the user set (2026-10-07): *"when there are ambiguities, we can record the
decision point and come back to it later. if it is critical or backtracking would create a lot of
rework, choose a different bead."*

Each entry: the decision area, the **provisional choice**, and **what would force a revisit**.

- **Record and continue** when the fix is local to the current item.
- **Claim a different bead** when the fix would rewrite finished items — change batches, come back.
- A decision point that needs work becomes an issue. The ledger is not a task list.
- Pair with: present options as plain text with a recommendation, never an interactive dialog — an
  unattended run cannot answer a dialog.

## 4. Fix the gates before starting, as commands, with the numbers that must not move

A gate is not "check it looks right". Write the commands and the expected reconciliation lines:

```
python3 notes/scripts/build_catalog.py > /tmp/r1.txt && cp notes/catalog.tsv /tmp/c1.tsv
python3 notes/scripts/build_catalog.py > /tmp/r2.txt && cp notes/catalog.tsv /tmp/c2.tsv
diff /tmp/c1.tsv /tmp/c2.tsv && diff /tmp/r1.txt /tmp/r2.txt     # must be byte-identical
python3 notes/scripts/verify_summaries.py --mutant               # zero problems, zero undetected mutants
```

Reconciliation lines that must not move: 372 families, 719 manuscripts, 172 formalized, 416
challenges, 200 `main_results` entries over 189 configs, 242 scope notes, both cross-checks 0.

Quote numbers only from the current run — never from the handoff file's recorded numbers. The file
records them so you notice when they move, not so you can reuse them.

## 5. Stop and escalate rules, written down in advance

- **Stop the batch** when a gate fails **twice on the same item**. Two failures mean the checker or
  the format is wrong, not the item; fix that first, in its own commit. Grinding through a repeated
  failure is how a run produces 40 subtly wrong pages.
- **Stop the run** when a higher-priority issue becomes ready. A batch queue at the floor of the
  queue exists so the loop cannot outrank real work — check `bd ready` at each boundary.
- **Never fabricate an ungroundable item.** Record it as blocked with the specific reason (what the
  sources do not state) and leave its ledger row 0. A filled row is a claim.

## 6. Check the hardware before adopting a fan-out design

Delegation guidance in agent descriptions does not survive contact with a single-GPU box running a
local model server. The user's ruling (2026-10-07): *"do not launch subagents. we are running locally
on a single gpu and it ends up being more inefficient to keep switching context per subagent turn."*
So the loop is **parent-only and sequential**: one item, one batch, one commit at a time. Write the
constraint into the handoff file, because a post-compaction session otherwise re-adopts the
parallel design that the hardware forbids.

## 7. Loop prompt: a pointer, not a state dump

Self-paced wakeups beat a timer — a timer fires mid-item. Keep the prompt short and stateless:

> Read `notes/summaries-workflow.md`. Run the gates. Take the next ready P4 issue under `math-ckd`,
> claim it, write one batch, commit, close. Stop if a P1/P2 issue is ready.

Every clause earns its place: read the protocol (state), run gates (verification), next ready issue
(priority), one batch (bounded unit), stop condition (queue discipline). Anything in the prompt that
describes *current* state is a bug — that state belongs in the handoff file.

## 8. Commit discipline under a standing authorization

A "take all recommendations" answer can authorize commits for the whole plan. The grant covers
exactly that: commit each batch when its gates pass, explicit paths, one purpose per commit, never
`--no-verify`. It does not extend past the plan. In a beads repo the pre-commit hook re-exports and
stages the issue store, so the store travels in the commit whose work it records — stage it
explicitly with the code it describes. Two things that came out the other way in practice: a
**pathspec** commit (`git commit -q -F - -- <paths>`) excludes other staged paths, so a staged issue
store survives into a later commit instead of riding along; and the hook's auto-export can fail with
`.git/index.lock` because it races the commit process itself — harmless, export by hand
(`bd export -o .beads/issues.jsonl`) and commit the store on its own.

Push is a **separate grant** and it is cadence-scaled, not per-commit. The user set it for this run
(2026-10-07): "you can push periodically during the loop but lets keep it to about once per hour."
So: push at roughly hourly boundaries, to the fork only, never on every commit. Record the cadence in
the handoff file — a post-compaction session that reads "push only on its own instruction" will
otherwise stall the backup, and one that reads the grant too loosely will push on every batch.

**A cadence is a batching rule, not a timer.** Clarified by the user on 2026-10-08: *"we shouldn't
sleep just to meet the cadence. my primary concern was that sometimes we do several commits in a row,
within a couple minutes and I didn't want to push every time."* So the interval is the **minimum
spacing between pushes**, never a reason to idle, sleep, or manufacture work to fill a window: push
when a batch of commits has accumulated and the interval has elapsed, and say in the report how many
commits the push carried. Idling to hit an interval converts a batch cadence into a polling loop and
buys nothing.

## 9. Pre-flight, before the first wakeup

- Queue exists, sits at the intended priority, and `bd ready` shows the batches in order.
- Handoff file committed and reachable from the agent-instructions file.
- Gate commands run green once, by hand, right now.
- Cost model measured on the finished examples (here: 1 manuscript → 15 sources / 173 markers;
  8 manuscripts → 32 sources / 272 markers; sources ≈ 4 per manuscript) so a batch can be sized.
- Standing authorization recorded, including its limits.

## What the handoff file cannot carry

It is not a substitute for verification: it cannot tell you a page is correct, only that a checker
says so. It cannot tell you the corpus still matches the recorded tier counts — re-measure if a
number is going into a commit message. It does not survive a rebase of the docs dir. And it is
silent on why a decision was made, which is why the decision ledger records the revisit condition,
not just the choice.
