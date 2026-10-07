# Counterexample-tag yield

Measured 2026-10-06 by static reading of the 372 family titles and abstracts in `overview.tex`; the
rule behind the counts was written down on 2026-10-07 and is recorded below. No `lake`, `lean`, or
comparator run. Method is the one `notes/conditional.md` records: propose a rule, count what it
flags, read every flagged family, record the flags reading drops. **No shape tag was changed** — the
measurement ended in a new column, under "Decision".

## The current rule and what it misses

```
"counterexample": r"counterexample|disprove|refut|fails|violation"
```

Applied to abstracts only, it tags **44 of 372**. Two structural causes of the misses. `disprove` is
a whole word, not a stem, so "disproving" — the form the release's abstracts actually use — is
invisible to it. And titles are never read, so a family whose title says "counterexample" is tagged
only if the abstract repeats the word.

## The recorded counts had no rule behind them

`notes/README.md` and `notes/t0-triage.md` quote "74 flagged, 44 tagged, 31 untagged, 30 genuine".
No variant of the vocabulary those docs quote reproduces them:

| candidate (title + abstract, case-folded) | flag | flag-only |
|---|---|---|
| `counterexample\|disprov\|negativ` (unbounded stem) | 90 | 46 |
| `counterexample\|disprov\|\bnegativ` | 75 | 32 |
| phrase rule, abstract only | 72 | 28 |
| **phrase rule, title + abstract** | **74** | **30** |

The 2026-10-06 pass was a reading pass whose regex was never written down, so its counts were not
re-runnable. Quote them as a reading result, and fix the count by writing the rule, not by
re-quoting the number.

## The rule that reproduces them

```python
COUNTEREX_PHRASE = re.compile(
    r"\bcounterexample|\bdisprov|\brefut|\bviolat|\bfails?\b"
    r"|negative (?:answer|resolution)"
    r"|(?:answer|resolv|settl|conclud|establish)[a-z]*[^.]{0,80}negatively"
    r"|negatively[^.]{0,40}(?:answer|resolv|settl)"
    r"|does not (?:imply|hold|satisfy)")
```

applied to `title + " " + abstract`, case-folded. It is in `notes/scripts/build_catalog.py` as
`counterex_broad()`.

Phrases, not stems: an unbounded `negativ` flags 90 families, most of them adjectival. The phrase
requirement excludes the false positives the earlier pass named — **348** ("answers … nonnegatively"),
**339** ("strictly negative sectional curvature"), **355** ("at every negative time"). None of the
three is tagged, and none is flagged by this rule. `negative (?:answer|resolution)` is what catches
**004**, whose result is a negative *resolution* of Hilbert's tenth problem over **Q** with no
counterexample object exhibited.

Input scope is stated because it changes the count: abstract only yields 72, and the two title-only
additions (**088**, **293**) are families whose titles literally say "counterexamples".

## Reading verdict on the 30 flags

All 30 were read at the matched sentence. **All 30 are counterexamples in kind** — nothing dropped.
Five need qualifiers:

- **004** — a negative resolution, not an exhibited object. The family is in the undecidability set
  (`notes/t0-triage.md` names 004, 206, 242, 247), so the flag is right for the reason "the answer is
  no", not "here is an object".
- **088** — mixed. The headline result *proves* Petty's projection-volume conjecture in the remaining
  dimensions; the counterexamples are the simplex cases named in the title.
- **206** — counterexamples *and* undecidability in one family; the flag covers the first half.
- **307** — the matched sentence is about the **companion** ("A companion gives the analogous failure
  for reduced coarse assembly, disproving the rational coarse Novikov conjecture"), not the headline
  result.
- **284** — a refutation in bound shape: it shows the randomized–quantum exponent is sharp, ruling
  out every smaller power. Genuine, and the reason the flag is not the same as bucket C.

Precision on this corpus is therefore **30/30 on "counterexample in kind"**, with 0 dropped and 5
qualified. Same shape as `resolution` (94 flagged, 94 genuine, `notes/resolution-tag.md`) and much
better than `conditional` (9 flagged, 5 genuine, `notes/conditional.md`): the tag omits far more than
it mislabels.

## Why the tag misses each one

| Miss reason | Families |
|---|---|
| `disprove` is a word, not a stem — "disproving" is invisible | 13: 048, 049, 050, 076, 132, 156, 195, 196, 249, 284, 307, 359, 374 |
| negative-answer phrasing with no counterexample noun | 15: 004, 098, 126, 201, 206, 247, 252, 257, 259, 292, 298, 324, 330, 334, 358 |
| title-only — the abstract carries no counterexample vocabulary at all | 2: 088, 293 |

Scope compounds all three: **14 of the 30 titles contain the tag's own vocabulary**, which the
abstract-only scope never reads.

## Per-family record

| Fam | Tier | Bucket | Title | Matched phrase | Verdict |
|---|---|---|---|---|---|
| 004 | T0 | R | Hilbert's tenth problem over $\mathbb Q$ | resolving … negatively | counterexample in kind — negative resolution, no object exhibited |
| 048 | T0 | K | A characteristic-zero counterexample to Lipman--Zariski | disprov | counterexample — surface with free rank-two tangent sheaf |
| 049 | T3 | N | A stable-coordinate counterexample in four variables | disprov | counterexample — polynomial that is not a coordinate |
| 050 | T3 | N | A counterexample to Griffiths' positivity conjecture | disprov | counterexample — ample rank-two bundles on $\mathbb P^1\times\mathbb P^1$ |
| 076 | T3 | B | Ultraflat real Littlewood polynomials | disprov | counterexample — merit factors tend to infinity, against Turyn |
| 088 | T3 | B | Petty's projection-volume conjecture and simplex counterexamples | title only | mixed — proves the conjecture, counterexamples are the simplex cases |
| 098 | T3 | N | A negative answer to the Lang--Plaut problem | answers … negatively | counterexample — compact doubling set with no bi-Lipschitz embedding |
| 126 | T2 | B | Exponential semidefinite complexity of perfect matching | answering Rothvoss's … negatively | counterexample — every exact semidefinite lift is exponential |
| 132 | T3 | N | A counterexample to the quadratic sensitivity conjecture | disprov | counterexample — total Boolean functions with $\mathrm{bs}(f)\ge s(f)^\alpha$, $\alpha>2$ |
| 156 | T3 | N | Borsuk's conjecture fails in dimension nine | disprov | counterexample — compact set in $\mathbb R^9$ needing ten smaller-diameter sets |
| 195 | T0 | N | A counterexample to the small Cohen--Macaulay module conjecture | disprov | counterexample — 3-dimensional complete local domain over $\mathbb C$ |
| 196 | T3 | N | A counterexample to Kaplansky's zero-divisor conjecture | disprov | counterexample — torsion-free group with zero divisors in $\mathbb F_2[G]$ |
| 201 | T0 | K | A counterexample to Kurosh's division-ring problem | answers … negatively | counterexample — countable division ring algebraic over its center |
| 206 | T2 | O | Finite lattice representation: counterexamples and undecidability | answering … negatively | counterexample in kind, qualified — the family also carries undecidability |
| 247 | T2 | O | An infinite finitely presented residually finite $2$-group | answering the finitely presented Burnside problem negatively | counterexample in kind — negative resolution |
| 249 | T2 | N | A finitely generated counterexample to Eilenberg--Ganea | disprov | counterexample — cohomological dimension 2, geometric dimension 3 |
| 252 | T3 | N | A non-residually-finite torsion-free hyperbolic group | answering the residual-finiteness question negatively | counterexample in kind — negative resolution |
| 257 | T3 | N | A hyperbolic group with no geometric CAT(0) action | answers negatively | counterexample in kind — negative resolution |
| 259 | T0 | B | A group without fixed price | answering the general fixed-price problem negatively | counterexample in kind — two pmp actions of different costs |
| 284 | T0 | B | The optimal randomized--quantum query exponent | disprov | counterexample in kind, qualified — refutation in bound shape (exponent sharp) |
| 292 | T2 | N | A counterexample to Kirchberg's norm-ultrapower embedding problem | answers … negatively | counterexample — separable $C^*$-algebra with no unital norm-ultrapower embedding |
| 293 | T3 | N | A counterexample to the hyperinvariant-subspace problem | title only | counterexample — quasinilpotent operator with no hyperinvariant subspace |
| 298 | T2 | B | A counterexample to Voiculescu's free-entropy equality conjecture | answers Voiculescu's finite-entropy equality question negatively | counterexample — the abstract names the target differently from the title |
| 307 | T2 | B | Failure of rational injectivity for maximal coarse assembly | disprov | counterexample in kind, qualified — the matched sentence is the companion's claim |
| 324 | T3 | R | Lipschitz equivalence without linear isomorphism | resolving the separable Lipschitz-isomorphism problem negatively | counterexample in kind — negative resolution |
| 330 | T2 | B | A negative answer to Kalton's Lipschitz-free approximation question | answering Kalton's question negatively | counterexample — countable uniformly discrete space |
| 334 | T3 | N | A smooth surface metric with no local immersion in $\mathbb R^3$ | answers … negatively | counterexample in kind — negative resolution |
| 358 | T3 | N | A three-manifold with no conjugate points and no nonpositively curved metric | answers negatively | counterexample — fails in dimension three |
| 359 | T3 | B | Negative Kähler curvature without bounded holomorphic coordinates | disprov | counterexample — contractible domain in $\mathbb C^3$ |
| 374 | T2 | B | Sharp one-third stability of optimal transport maps | disprov | counterexample — disproving Letrouit's conjectured square-root bound |

Buckets are `notes/scripts/triage_t0.py`'s first-match assignment on the current `shapes` column.

## What widening the tag would change

Widening `SHAPES["counterexample"]` from 44 to 74 moves families between the T0 buckets, because
`triage_t0.py` assigns buckets by **first match**. Measured on the current ledger:

| Bucket | now | widened |
|---|---|---|
| C counterexample | 16 | 22 |
| R resolution | 50 | 49 |
| B bound | 29 | 27 |
| K classification | 8 | 6 |
| U uniform | 12 | 12 |
| O other | 2 | 2 |
| N untagged | 20 | 19 |

Six T0 families move, all into C: 004 (from R), 048 (from K), 195 (from N), 201 (from K), 259 (from
B), 284 (from B). Every recorded bucket count in `notes/t0-triage.md` would stop matching.

The decisive number: **0 of the 30 flag-only families sit in bucket C** (they are N 14, B 10, R 2,
K 2, O 2). First match hides every one of them, so the widening is a re-assignment of the reading
order, not a discovery.

## Decision (2026-10-07): a separate column, not a widened tag

`notes/scripts/build_catalog.py` now writes a 22nd column, **`counterex_broad`**, carrying the phrase
rule. `SHAPES["counterexample"]` is unchanged, so the shape table stays at 44 and the first-match
buckets are untouched — re-run after the change, they are C 16, R 50, B 29, K 8, U 12, O 2, N 20 over
137 families / 255 manuscripts / 0 formalized, identical to the record in `notes/t0-triage.md`.

Fresh generator report: **`counterex_broad` 74 of 372 families, `counterexample` tag 44, tag-only 0,
flag-only 30.** By tier T3 33, T2 19, T1 0, T0 22; 120 manuscripts behind the flagged families.
Unlike `resolves_named`, this column **is** a strict superset of its tag (tag-only 0), so the two
counts are directly comparable: the tag is the floor, the column is the wider floor.

Additivity evidence, all from the run that produced this file: regeneration twice is byte-identical;
the column-by-column diff against `HEAD` shows added `['counterex_broad']`, removed `[]`, **0
differences in pre-existing columns** across 372 rows; the reconciliation lines are unchanged (372
families, 722 manuscripts, 162 formalized, 405 challenges, 185 `main_results` entries over 178
configs, 235 scope notes, both `overview.tex` ↔ `CONTENTS.md` cross-checks 0); the column
discriminates (74 ones, 298 zeros, no blanks, differs from the tag in 30 rows).

### Rejected: the named-target conjunction

Requiring a target noun (`conjectur | \bquestion | \bproblem`) together with a counterexample verb
gives **54** families with **tag-only 12** — 046, 151, 190, 192, 209, 244, 278, 289, 297, 318, 347,
361. Twelve tagged families name no conjecture, question, or problem in the abstract, so the
conjunction is not a superset and cannot carry the "the tag under-covers" job that this column does.
It is a narrower, differently-shaped signal; not adopted.

### What the column adds

25 of the 30 flag-only families also carry `resolves_named = 1`, and 41 manuscripts sit behind them.
By tier the flag-only set is T0 6, T2 9, T3 15; by bucket N 14, B 10, R 2, K 2, O 2. Inside T0 the
column flags 22 of 137 families, of which 16 are in bucket C and 6 are not — the six are exactly the
families the widening would have moved, which is the argument for the column: the signal is available
to readers without re-cutting the reading order.

## Not checked

- The rule is a keyword floor over titles and abstracts. It says a family *uses* counterexample
  language, not that its manuscript contains one.
- The 30 verdicts are readings of the sentence the rule matched, not of the manuscripts. No
  manuscript was read, no conjecture identified in the literature, no formalized statement compared
  with the claim (no Lean run).
- The 44 tagged families were not re-read in this pass; only the 30 flag-only families were.
- Precision was measured on the flags the rule raises. **What it continues to miss is unmeasured** —
  a counterexample stated with none of these phrases (e.g. "the unique solution does not exist", "no
  such metric exists") is not in the rule. A negative-control pass over the 298 unflagged families is
  the next measurement, and the flag total should not be quoted as a census before it is run.
- `fails` is in the rule with an optional `s` (`\bfails?\b`), which is the one stem kept uninflected
  for breadth; its false-positive rate on this corpus was not measured beyond the 30 read here.
