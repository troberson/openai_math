---
name: generated-index-column-change
description: Add a derived column to a generated ledger/index safely — measure overlap with the
  existing signal before coding, keep broad rules out of first-match chains, prove the change is
  additive by diffing the artifact column by column, then sweep every doc that describes the schema.
source: auto-skill
extracted_at: '2026-10-07T08:19:15.882Z'
---

# Changing a column in a generated index

For repos whose analysis lives in a generated artifact (a TSV ledger, an index, a report) plus
scripts that consume it. Worked out on the OpenAI Research Catalog
(`/home/tamara/Downloads/_Git/math`): `notes/scripts/build_catalog.py` → `notes/catalog.tsv`
(372 rows), consumed by `notes/scripts/triage_t0.py` and described in `notes/README.md`,
`notes/t0-triage.md`, and a project skill.

## 1. Measure overlap with the existing signal before writing code

**Never assume the new rule is a superset of the old one.** Compute the intersection first, on the
same input the generator reads:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("bc", "notes/scripts/build_catalog.py")
bc = importlib.util.module_from_spec(spec); spec.loader.exec_module(bc)
order, fams = bc.parse_overview()          # reuse the generator's own parser
cur = {f for f, i in fams.items() if re.search(bc.SHAPES["resolution"], i["abstract"].lower())}
new = {f for f, i in fams.items() if NOUN.search(...) and VERB.search(...)}
print(len(cur), len(new), len(cur & new), len(cur - new), len(cur | new))
```

Catalog: tag 144, candidate 233, **both 139, tag-only 5, union 238** — not nested. The 5 tag-only
families were the finding: their target is named as a *hypothesis / case / estimate / contrast*, not
a conjecture/question/problem, so the noun list cannot see them. Widening the tag in place would
have destroyed the ability to notice that, and would have made the count look like a clean 144 → 233
improvement.

Report the split (both / A-only / B-only / union) as the headline, not the two totals.

## 2. Placement: separate column vs. a new entry in the multi-label set

Grep every consumer of the multi-label field for **first-match / first-wins** logic before adding to
it. Here `triage_t0.py` assigns T0 buckets by first match over `shapes`, so widening `resolution`
moves families out of the counterexample, bound, classification, undecidability and density buckets —
a taxonomy change disguised as a tag tweak.

A separate column is additive: the shape table stays at 144, the buckets stay put, and the broad rule
is available to readers. Say the reason in a comment at the rule, so the next person does not
"tidy" it into the shared set.

### Not every column is a derived claim

Some columns are **filesystem facts**, and those skip steps 1–3 and 5 entirely: no overlap
measurement, no keyword hygiene, no cross-tab. Presence of a page is the canonical one:

```python
# Page presence is a filesystem fact, not a derived claim: the directory name is the
# discipline lowercased with spaces hyphenated, so the glob is the whole test.
summary_fams = {p.name[:3] for p in (ROOT / "notes" / "summaries").glob("*/*.md")
                if re.match(r"^\d{3}-", p.name)}
```

Key it by the `<NNN>` prefix, not by the directory, so a page misfiled under the wrong discipline
still counts against the right family. Say in the comment why the glob is the whole test.

Give the column a **report line**, not just a value — a column nobody prints is a column nobody
audits, and the line is what a long production loop reads at each batch boundary:

```python
print(f"summary pages       {sum(1 for r in rows if r['summary'])} of {len(rows)} families, "
      f"{sum(int(r['paps']) for r in rows if r['summary'])} manuscripts behind them")
```

Print the second number too (here: manuscripts behind the 2 pages). A count with a denominator
catches a column that flips for the wrong rows; a bare count does not.

## 3. Regex hygiene for keyword rules

Bound both ends of a verb stem. `\bprov(?:e|es|ed|ing)\b` — without the leading boundary,
"improved" matches through the "proved" inside it, which belongs to the `bound` tag's territory.
Same class as the earlier `conditional` false positives ("conditional expectation", "without
assuming"): a keyword rule needs its negatives enumerated by reading, not by intuition.

## 4. Prove the change is additive, on the artifact

Run this before committing; it is the check that catches an accidental change to a neighbouring
column:

```python
import csv
old = list(csv.DictReader(open("/tmp/old.tsv", encoding="utf-8"), delimiter="\t"))   # git show HEAD:...
new = list(csv.DictReader(open("notes/catalog.tsv", encoding="utf-8"), delimiter="\t"))
oldcols, newcols = list(old[0]), list(new[0])
print([c for c in newcols if c not in oldcols], [c for c in oldcols if c not in newcols])
print(sum(1 for o, n in zip(old, new) for c in oldcols if o[c] != n[c]))
```

Expected: added `['resolves_named']`, removed `[]`, **0 differences in pre-existing columns** across
all 372 rows. Also:

- Regenerate twice and diff — the artifact must be byte-identical, and the report identical.
- Re-run every downstream consumer and compare to its *recorded* numbers (buckets C 16, R 50, B 29,
  K 8, U 12, O 2, N 20 over 137 families / 255 manuscripts — unchanged).
- Confirm the generator's reconciliation lines and cross-checks are unchanged (372 / 722 / 162 / 235,
  both `overview.tex` ↔ `CONTENTS.md` cross-checks 0).
- Confirm the new column **discriminates** before quoting it: not all-1, not all-0, no blanks, and
  not a copy of the existing signal (99 families differ from the tag).

## 5. Find where the column actually pays off

Cross-tab the new column against the downstream partition — that is the argument for it:

- 88 of the 137 zero-signal (T0) families flagged; 40 of those sit **outside** the resolution bucket,
  where first match hides them.
- 12 of the 20 families in the "no shape tag at all" bucket are named-conjecture families, so the
  bucket's description ("title is the only signal") stopped being true for half of it.

## 6. Sweep the docs that describe the schema

The change is not done when the generator runs. Grep for the phrases it invalidates and fix each one:
`only signal`, `only discriminator`, `19 columns`, `triaged by claim shape alone`. Update: the column
table, the shape/tag section, the downstream script's docstring, the triage record, and the project
skill (a standing rule, the resource map, the lookup step, the column count, and its `version:`
field). Mark the open task decided for the part you decided and explicitly open for the part you
did not (`counterexample`: 30 genuine untagged families, no column proposed).

Grep the column count as a **number**, not only as a phrase — the same stale integer appears in prose
that does not read like schema documentation. On the 20 → 21 change (2026-10-07) two docs were stale
at once: the column table in `notes/README.md` and the repository map in `AGENTS.md`
("`catalog.tsv` (372 rows, 20 columns)"). Sweep the agent-instructions file too: it is the only doc a
fresh session reads first, and a map that omits a new directory means the next agent never finds it.
When the change adds a directory, the map line and the README command block both need the new path,
and the README gains the checker invocation in its exact flag form (`--mutant`), not just the bare
command.

## 7. Commit and push

Three single-purpose commits, staged by explicit path, never `git add -A`:

1. generator + regenerated artifact
2. the record of the decision (measurement, overlap table, cross-tab, what was not done)
3. the docs + skill that route readers to it

Push only on its own instruction, after `git push --dry-run`, to the fork (`origin`), never
`upstream`.

## 8. Close with what is not checked

The column is computed from abstracts, so "resolves conjecture X" remains the release's claim, not a
checked fact; known accidental matches and partial resolutions carry over from the measurement;
deliberately unadded nouns (`hypothes`) are a new measurement, not a tweak; and what the rule
*continues* to miss (a resolution stated with no target noun and no listed verb) is unmeasured.
