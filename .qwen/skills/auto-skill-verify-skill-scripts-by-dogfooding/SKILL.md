---
name: verify-skill-scripts-by-dogfooding
description: Prove a newly authored skill works — parse its frontmatter, run its script on a good input, a deliberately bad input, and its own template, then fix the checker's false positives.
source: auto-skill
extracted_at: '2026-10-07T06:01:22.180Z'
---

# Verifying a skill you just wrote

Use after authoring a skill that ships a script (audit, generator, validator). The authoring
conventions come from the `skill-writer` skill; this file is the **verification loop** that
skill-writer's structural checklist does not cover. A skill whose script was never executed is a
skill with an unverified claim in it.

## 1. Layout, then measure it

Router `SKILL.md` (≤500 lines) + `references/*.md` (depth) + `assets/*` (templates) +
`scripts/*` (deterministic logic). Copy the frontmatter shape from an existing personal skill
(`head -12 ~/.agents/skills/<some-skill>/SKILL.md`) so the style matches what already loads.

## 2. Parse the frontmatter mechanically

```sh
python3 - <<'PY'
import re, yaml
p = "/abs/path/to/skill/SKILL.md"
t = open(p).read()
m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
d = yaml.safe_load(m.group(1))
print("name:", d["name"], "| desc chars:", len(d["description"]), "| body lines:", t.count("\n"))
assert d["name"] == p.split("/")[-2], "name must match directory"
assert len(d["description"]) <= 1024
PY
```

If PyYAML is missing, fall back to a regex check and say so — do not claim a parse you did not do.

## 3. Run the script on three inputs

| Input | Expected |
|---|---|
| A real, known-good file from the current project | exit 0, only informational notes |
| A deliberately bad file built with `printf` in `/tmp` (missing required heading, forbidden construct, a planted secret literal) | exit 1, with the blocking FAILs named |
| The skill's own `assets/template.*` | clean |

Build the bad file inline in the same shell call, and delete it afterwards. Skipping the bad-input
run is how a checker that never fails gets shipped.

## 4. False positives are bugs in the checker

Every finding on the known-good file is a defect until you have judged it:

- Heuristic allow-lists (imperative verbs, "safe" tokens, filename sets) start too small. Extend
  the list, re-run, and keep going until every remaining note is genuinely informational.
- Repo-wide sweeps need a skip set (`docs/`, `data/`, `verification/`, `node_modules/`,
  `__pycache__/`, `.qwen/`, `.agents/`) or they drown the real signal in noise.
- Informational notes must not change the exit code; only blocking findings may.

## 5. Check memory for a duplicate before saving anything

`ls ~/.qwen/memories/*/ && grep -l <topic> ~/.qwen/memories/*/*.md` — a prior session often
already saved the fact. Keep the superset, delete the newcomer, fix the index line (a dangling
index entry pointing at a deleted file is a bug you can see with `read_file`).

## 6. Report what you ran

Quote the actual audit output (lines/bullets/sections, exit code) rather than asserting the skill
"is valid". State which checks were run and which were not.
