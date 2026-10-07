---
name: reconstruct-unwritten-classification-rule
description: Recover the keyword rule behind counts that a doc quotes but never wrote down — enumerate
  variants against the recorded numbers, build a phrase rule instead of a stem rule, read the
  flag-only set, then write the rule into code so the counts become reproducible.
source: auto-skill
extracted_at: '2026-10-07T15:41:26.914Z'
---

# Reconstructing a classification rule that was never written down

For analysis repos where docs quote counts produced by a **reading pass** ("74 families use
counterexample language, 44 carry the tag, 30 of the 31 untagged flags are genuine") and the regex
that produced them lives nowhere. Worked out on `math-7ej` in
`/home/tamara/Downloads/_Git/math`: `notes/README.md:86-89` and `notes/t0-triage.md:517-521` both
quoted the counterexample numbers while the generator shipped only the narrow `SHAPES` tag. The rule
is now in the generator as `COUNTEREX_PHRASE` / `counterex_broad`, recorded in
`notes/counterexample-tag.md`.

## 0. Prove the numbers are unreproducible before trusting them

Enumerate the plausible rules implied by the doc's own quoted vocabulary and print each one's counts.
Do not assume the doc's vocabulary is the rule.

| candidate (title + abstract, case-folded) | flag | flag-only |
|---|---|---|
| `counterexample\|disprov\|negativ` (unbounded stem) | 90 | 46 |
| `counterexample\|disprov\|\bnegativ` | 75 | 32 |
| phrase rule, abstract only | 72 | 28 |
| **phrase rule, title + abstract** | **74** | **30** |

The recorded 74 / 30-genuine is reproduced only by the last row. A doc-quoted count with no rule
behind it is a reading result, not a measurement: quote it as such, and say so before building on it.

## 1. Score candidates against the recorded numbers, not against the doc's vocabulary

The recorded counts are the target. Two acceptance tests, both required:

- **Count match**: flag total and flag-only total equal the recorded numbers.
- **False-positive exclusion**: the doc names the known false positives (here 348, matched through
  "nonnegatively"). A candidate that flags them is wrong even if its total matches. Find the rest by
  reading the matched sentence of every flag-only family — here "strictly negative sectional
  curvature" (339) and "at every negative time" (355) surfaced the same way.

## 2. Build a phrase rule, not a stem rule

Bare stems over-match on adjectival uses of the word. Phrases carry the semantics:

```python
PHRASE = (r"\bcounterexample|\bdisprov|\brefut|\bviolat|\bfails?\b"
          r"|negative (?:answer|resolution)"
          r"|(?:answer|resolv|settl|conclud|establish)[a-z]*[^.]{0,80}negatively"
          r"|negatively[^.]{0,40}(?:answer|resolv|settl)"
          r"|does not (?:imply|hold|satisfy)")
```

`negative (?:answer|resolution)` is what catches a negative *resolution* (004) where no
counterexample object is exhibited. `[^.]{0,80}` keeps the two halves inside one sentence. Keep
`\b` on both ends of every stem (`\bprov(?:e|es|ed|ing)\b`: "improved" matches through "proved").

## 3. Decide the input scope, and report the delta

Abstract-only vs title+abstract is a real fork with a number attached: 72 vs 74 here, and the two
title-only additions (088, 293) are families whose titles literally say "counterexamples". State
which scope the rule uses in the code comment; a rule whose input scope is unstated cannot be
re-run by anyone.

## 4. Read the flag-only set, family by family

The A-only set is the whole point of the exercise. Print, for each family, the sentence the rule
matched, plus tier and the downstream bucket, then record a verdict per family (genuine in kind /
not). Here: 30 families, all genuine, 25 of them also flagged by the other broad column, 41
manuscripts behind them, and **all 30 sitting outside the target bucket** — i.e. a first-match
consumer hides every one of them. That last line is the argument that decides the design fork.

## 5. Write the rule down

The fix for an unreproducible count is the rule, not a re-quoted number. Put the regex in code with a
comment naming the excluded false positives, and replace the prose counts in every doc that quoted
them with the rule + the counts it reproduces. Then the counts are re-runnable and the doc stops
drifting.

## Pitfalls hit while doing this

- `text.rfind(".\n", 0, m.start)` → `TypeError: slice indices must be integers`: the bound method
  object, not `m.start()`.
- `m = RULE.search(abstract) or RULE.search(title)` gives match offsets from the *other* string, so
  the printed context sentence is from the wrong field. Search one concatenated haystack
  (`hay = title + " " + abstract`) and index into that.
- Columns computed in the row builder (`tier`) are not in the parser's info dict. Read them back from
  the generated artifact with `csv.DictReader(..., delimiter="\t")`, never from the parser.

## Close with what is not checked

The rule is a keyword floor over titles/abstracts: it says a family *uses* counterexample language,
not that it contains one. The per-family verdicts are readings of matched sentences, not of the
manuscripts. What the rule continues to miss is unmeasured — measure it as a negative-control pass
before quoting the flag total as a census.
