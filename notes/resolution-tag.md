# Resolution-tag yield

Measured 2026-10-06 by static reading of the 372 family abstracts in `overview.tex`. No `lake`,
`lean`, or comparator run. This is the yield check the open task in `notes/README.md` asks for
before any tag rule in `notes/scripts/build_catalog.py` is widened. **No tag was changed.** The
measurement ended in a separate column, recorded under "Decision" below.

Method is the one `notes/conditional.md` records: propose a rule, count what it flags, read every
flagged abstract, and record the flags that reading drops.

## The current rule and what it misses

```
"resolution": r"resolv|proves the .{0,60}conjecture|answers .{0,30}question|settles"
```

It tags 144 of 372 families. The string `proves the … conjecture` is the load-bearing part, and it
is the part that misses: the release's abstracts say *proves Milne's rationality conjecture* (no
`the`), *disproving Kaplansky's zero-divisor conjecture* (a form the pattern does not contain), and
*establishes the fixed-determinant P=W conjecture* (a verb the pattern does not contain).

## Candidate rule

Flag a family when its abstract contains **both**

- a target noun: `conjectur` | `\bquestion` | `\bproblem`, and
- a resolution verb: `prov(e|es|ed|ing)` | `disprov` | `refut` | `resolv` | `answer` | `settl` |
  `establis` | `confirm` | `fail` | `violat` | `counterexample`.

Measured on all 372 abstracts: **233 families flagged, 94 of them untagged today** (144 → 233,
+65%). By tier: T0 37, T3 36, T2 21. By discipline the flags spread over all 17 (max algebraic and
complex geometry 16, group theory 9, differential geometry 9, combinatorics 8, topology 8).

The column as applied reads the overview **title and abstract lowered together** and flags **248**
(T0 91, T2 62, T3 95), so the column-only set is **109**, not 94. The 15 title-scope additions are
corroborated at the manuscript-abstract layer in `notes/named-results.md`; they were **not read
here**, so the precision figure below is measured on the 94 abstract-only flags and says nothing
about the extra 15.

## Reading verdict on the 94 flags

All 94 abstracts were read. **94 are resolutions in kind** — the abstract claims a named
conjecture, question, or problem is proved, disproved, answered, or settled. Nothing was dropped.
Three need qualifiers:

- **277** is the only accidental match: `question` appears in "correlated question distributions",
  a technical noun. The result (exponential threshold repetition for every finite two-player
  one-round entangled game) is a genuine resolution in kind, so the flag is right for the wrong
  reason. This is the "conditional expectation" class from `notes/conditional.md`.
- **080** resolves the sharp Sobolev endpoint of Carleson's convergence problem, not the whole
  problem. **158** rules out five-colourings of the plane, narrowing Hadwiger–Nelson to {6,7}
  without settling it. Both are partial resolutions, and the tag would not say so.

Precision of the candidate rule on this corpus is therefore 94/94 on "resolution in kind", with 1
accidental match and 2 partials. That is a much better yield than `conditional` (9 flagged, 5
genuine) and the same shape as `counterexample` (30 untagged flags, 30 genuine —
`notes/counterexample-tag.md`): the tag omits far more than it mislabels.

## Why the current rule misses each one

| Miss reason | Families |
|---|---|
| `proves <Name>'s …` — no `the` | 30: 001, 006, 019, 031, 033, 038, 040, 051, 055, 066, 091, 105, 159, 164, 173, 203, 205, 240, 258, 288, 315, 316, 338, 339, 341, 342, 350, 356, 369, 375 |
| `disproves` / disprove-form | 29: 048, 049, 050, 053, 054, 059, 072, 076, 100, 132, 155, 157, 162, 185, 195, 196, 197, 249, 272, 284, 294, 305, 307, 320, 321, 329, 351, 352, 374 |
| verb absent from the pattern (establish, confirm, refute, settle, answer) | 10: 043, 052, 057, 083, 088, 102, 127, 146, 243, 319 |
| prove-form other than `proves the` (gerund, infinitive) | 5: 060, 246, 250, 254, 306 |
| target named as a question/problem, not a conjecture | 20: 024, 080, 094, 098, 126, 158, 201, 206, 247, 252, 253, 259, 277, 292, 298, 299, 323, 327, 330, 334 |

## Per-family record

| Fam | Tier | Title | Why untagged today | Verb matched | Reading verdict |
|---|---|---|---|---|---|
| 001 | T0 | Milne's rationality conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 006 | T0 | Goldfeld's conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 019 | T0 | The $p$-adic section conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 024 | T2 | An asymptotic formula for the number of totients | verb not in pattern | `answer` | resolution |
| 031 | T0 | Uchida's conjecture for open Galois homomorphisms | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 033 | T2 | Campana's orbifold Iitaka conjecture and logarithmic | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 038 | T0 | Fujita's freeness conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 040 | T0 | Bloch's conjecture for complex surfaces | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 043 | T0 | $P=W$ for fixed-determinant moduli spaces | verb not in pattern | `Prove` | resolution |
| 048 | T0 | A characteristic-zero counterexample to Lipman--Zari | disproves / disprove-form | `disprov` | resolution |
| 049 | T3 | A stable-coordinate counterexample in four variables | disproves / disprove-form | `disprov` | resolution |
| 050 | T3 | A counterexample to Griffiths' positivity conjecture | disproves / disprove-form | `disprov` | resolution |
| 051 | T0 | Kobayashi's canonical-ampleness conjecture | proves <Name>'s … (no 'the') | `prove` | resolution |
| 052 | T3 | Tangent-bundle splittings and universal covers | verb not in pattern | `proving` | resolution |
| 053 | T0 | A counterexample to Pixton's original completeness c | disproves / disprove-form | `disprov` | resolution |
| 054 | T0 | Counterexamples to Kuznetsov's rationality conjectur | disproves / disprove-form | `disprov` | resolution |
| 055 | T0 | Toda's Gepner conjecture and large-volume stability | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 057 | T0 | Campana's abelianity conjecture and special varietie | verb not in pattern | `Prove` | resolution |
| 059 | T0 | Counterexamples to Zariski's multiplicity conjecture | disproves / disprove-form | `Disprov` | resolution |
| 060 | T0 | The Global Spherical Shell conjecture | prove-form other than 'proves the' | `proving` | resolution |
| 066 | T0 | Bounded klt complements for Fano contractions | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 072 | T3 | Brennan's conjecture and a counterexample to Kraetze | disproves / disprove-form | `Prove` | resolution |
| 076 | T3 | Ultraflat real Littlewood polynomials | disproves / disprove-form | `disprov` | resolution |
| 080 | T0 | The Sobolev endpoint in Carleson's Schr\"odinger con | proves <Name>'s … (no 'the') | `Prove` | partial — resolves the sharp endpoint case, not the whole problem |
| 083 | T2 | Stein's conjecture for Hilbert transforms along Lips | verb not in pattern | `Prove` | resolution |
| 088 | T3 | Petty's projection-volume conjecture and simplex cou | verb not in pattern | `Prove` | resolution |
| 091 | T3 | The logarithmic Brunn--Minkowski conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 094 | T3 | Subpolynomial dimension reduction in $L_p$ | verb not in pattern | `answer` | resolution |
| 098 | T3 | A negative answer to the Lang--Plaut problem | verb not in pattern | `answer` | resolution |
| 100 | T2 | A counterexample to Bang's cylinder-covering bound | disproves / disprove-form | `disprov` | resolution |
| 102 | T3 | The Unique Games Conjecture and optimal approximatio | verb not in pattern | `Prove` | resolution |
| 105 | T3 | The 2-to-1 Games Conjecture with perfect completenes | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 126 | T2 | Exponential semidefinite complexity of perfect match | verb not in pattern | `Prove` | resolution |
| 127 | T3 | The asymptotic Gotsman--Linial conjecture | verb not in pattern | `Prove` | resolution |
| 132 | T3 | A counterexample to the quadratic sensitivity conjec | disproves / disprove-form | `disprov` | resolution |
| 146 | T2 | Sinai's positive-entropy conjecture for the standard | verb not in pattern | `Prove` | resolution |
| 155 | T3 | A counterexample to periodic tiling in dimension thr | disproves / disprove-form | `disprov` | resolution |
| 157 | T2 | Counterexamples to the Hadwiger and Colin de Verdi\` | disproves / disprove-form | `Disprov` | resolution |
| 158 | T3 | The Euclidean plane cannot be colored with five colo | proves <Name>'s … (no 'the') | `Prove` | partial — narrows the range (rules out 5), does not settle the chromatic number |
| 159 | T2 | Erd\H{o}s's reciprocal-sum conjecture and quasipolyn | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 162 | T3 | Counterexamples to Ryser's covering and Gy\'arf\'as' | disproves / disprove-form | `Disprov` | resolution |
| 164 | T0 | Hindman's finite sums and products conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 173 | T3 | Seymour's second-neighborhood conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 185 | T3 | Counterexamples to infinite matroid intersection and | disproves / disprove-form | `Disprov` | resolution |
| 195 | T0 | A counterexample to the small Cohen--Macaulay module | disproves / disprove-form | `disprov` | resolution |
| 196 | T3 | A counterexample to Kaplansky's zero-divisor conject | disproves / disprove-form | `disprov` | resolution |
| 197 | T3 | Nonsofic groups and group-ring counterexamples | disproves / disprove-form | `disprov` | resolution |
| 201 | T0 | A counterexample to Kurosh's division-ring problem | verb not in pattern | `answer` | resolution |
| 203 | T0 | Donovan's conjecture over fields and discrete valuat | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 205 | T3 | Saxl's conjecture and universal tensor squares | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 206 | T2 | Finite lattice representation: counterexamples and u | verb not in pattern | `answer` | resolution |
| 240 | T3 | Shelah's eventual categoricity conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 243 | T3 | Choiceless counting does not capture polynomial time | verb not in pattern | `Confirm` | resolution |
| 246 | T2 | Cannon's conjecture | prove-form other than 'proves the' | `proving` | resolution |
| 247 | T2 | An infinite finitely presented residually finite $2$ | verb not in pattern | `answer` | resolution |
| 249 | T2 | A finitely generated counterexample to Eilenberg--Ga | disproves / disprove-form | `disprov` | resolution |
| 250 | T3 | The Boone--Higman conjecture and higher finiteness | prove-form other than 'proves the' | `proving` | resolution |
| 252 | T3 | A non-residually-finite torsion-free hyperbolic grou | verb not in pattern | `answer` | resolution |
| 253 | T3 | An infinite finitely presented simple amenable group | verb not in pattern | `answer` | resolution |
| 254 | T3 | Classifying spaces and geometric obstructions for Ar | prove-form other than 'proves the' | `proving` | resolution |
| 258 | T0 | Gersten's conjecture for one-relator groups | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 259 | T0 | A group without fixed price | verb not in pattern | `answer` | resolution |
| 272 | T2 | Entanglement without secret key and the PPT-square c | disproves / disprove-form | `disprov` | resolution |
| 277 | T3 | Threshold repetition for entangled games | proves <Name>'s … (no 'the') | `Prove` | accidental match — 'question distributions' is a technical noun; the result is a genuine resolution in kind |
| 284 | T0 | The optimal randomized--quantum query exponent | disproves / disprove-form | `disprov` | resolution |
| 288 | T2 | Kadison's similarity conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 292 | T2 | A counterexample to Kirchberg's norm-ultrapower embe | verb not in pattern | `answer` | resolution |
| 294 | T3 | A counterexample to Kaplansky's quasitrace conjectur | disproves / disprove-form | `Disprov` | resolution |
| 298 | T2 | A counterexample to Voiculescu’s free-entropy equali | verb not in pattern | `answer` | resolution |
| 299 | T3 | The Kirchberg--R\o rdam character criterion | verb not in pattern | `answer` | resolution |
| 305 | T0 | Counterexamples to disk embedding and Wall's manifol | disproves / disprove-form | `fail` | resolution |
| 306 | T0 | The purely cosmetic surgery conjecture for knots in  | prove-form other than 'proves the' | `proving` | resolution |
| 307 | T2 | Failure of rational injectivity for maximal coarse a | disproves / disprove-form | `fail` | resolution |
| 315 | T0 | The four-dimensional Singer conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 316 | T0 | Curtis’s conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 319 | T0 | Counterexamples to the Hahn--Wilson conjecture at he | verb not in pattern | `Refut` | resolution |
| 320 | T0 | A four-dimensional counterexample to Borel rigidity | disproves / disprove-form | `disprov` | resolution |
| 321 | T0 | A counterexample to Wall's finite D(2) conjecture | disproves / disprove-form | `disprov` | resolution |
| 323 | T2 | Relative independence of the separable quotient prob | verb not in pattern | `Establis` | resolution |
| 327 | T3 | Markov type characterizes superreflexivity | verb not in pattern | `Prove` | resolution |
| 329 | T3 | A counterexample to Pietsch's metric-entropy duality | disproves / disprove-form | `Disprov` | resolution |
| 330 | T2 | A negative answer to Kalton's Lipschitz-free approxi | verb not in pattern | `answer` | resolution |
| 334 | T3 | A smooth surface metric with no local immersion in $ | verb not in pattern | `answer` | resolution |
| 338 | T0 | Yau's uniformization conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 339 | T0 | Katok's entropy rigidity conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 341 | T0 | Donaldson's hypersymplectic deformation conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 342 | T3 | Donaldson's tamed-to-compatible conjecture | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 350 | T3 | Yau's nodal conjecture: surfaces and counterexamples | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 351 | T0 | Scalar curvature detects four-dimensional Ricci-flow | disproves / disprove-form | `Prove` | resolution |
| 352 | T0 | Finite-time singularity of Calabi flow | disproves / disprove-form | `Disprov` | resolution |
| 356 | T3 | Gigli's characterization of Alexandrov curvature | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 369 | T2 | The hot spots conjecture for simply connected planar | proves <Name>'s … (no 'the') | `Prove` | resolution |
| 374 | T2 | Sharp one-third stability of optimal transport maps | disproves / disprove-form | `disprov` | resolution |
| 375 | T0 | De Giorgi's conjecture in dimension eight | proves <Name>'s … (no 'the') | `Prove` | resolution |

## What widening would change

`shapes` is a pipe-joined multi-label column, so widening `resolution` changes: the shape table in
`notes/README.md` (144 → 248 under the applied scope, 144 → 233 under the abstract-only scope this
file measured); the T0 bucket counts in `notes/scripts/triage_t0.py`, which assign
buckets by **first match** in the order resolution, counterexample, bound, classification,
undecidability, density, conditional, partial, uniform — 29 of the 94 flags are counterexample-form
("disproves X's conjecture"), and those families are already in the C bucket, so widening moves
families out of C, B, K, U, N into R. The 137/255 T0 totals and every coverage layer are unaffected;
`conditional` is unaffected.

## Decision (2026-10-07): a separate column, not a widened tag

`notes/scripts/build_catalog.py` now writes a 20th column, **`resolves_named`**, carrying the
candidate rule. The `resolution` entry in `SHAPES` is unchanged, so the shape table stays at 144 and
the first-match buckets in `triage_t0.py` are untouched — re-run after the change, the buckets are
C 16, R 50, B 29, K 8, U 12, O 2, N 20 over 137 families / 255 manuscripts / 0 formalized, identical
to the record in `notes/t0-triage.md`.

```python
TARGET_NOUN  = r"conjectur|\bquestion|\bproblem"
RESOLVE_VERB = (r"\bprov(?:e|es|ed|ing)\b|\bdisprov|\brefut|\bresolv|\banswer|\bsettl|\bestablis"
                r"|\bconfirm|\bfail|\bviolat|\bcounterexample")
```

`\bprov(?:e|es|ed|ing)\b` needs both boundaries: without the leading one, "improved" matches through
the "proved" inside it, which is the `bound` tag's own territory.

Fresh generator report: **`resolves_named` 248 families, `resolution` tag 144, union 253.** By tier
T3 95, T2 62, T1 0, T0 91. Under the abstract-only scope the same report read 233 families, union
238, by tier T3 88, T2 57, T1 0, T0 88. The column is **not a superset** of the tag:

| | Families |
|---|---|
| flagged by both | 139 |
| tag-only (tag yes, column no) | 5: 003, 010, 082, 103, 261 |
| column-only (column yes, tag no) | 109 — of which the 94 abstract-only flags are the set read in this file |

The 5 tag-only families are resolutions the noun list cannot see, because their target is named as a
*hypothesis / case / estimate / contrast*, not as a conjecture, question, or problem:

| Fam | Target as written in the abstract |
|---|---|
| 003 | "resolving the quasi-Riemann **hypothesis**" |
| 010 | "resolving the dyadic Fontaine--Mazur **case**" |
| 082 | "settles the triangular Hilbert transform **estimate**" |
| 103 | "resolving derandomization for bounded-error logarithmic-space computation" |
| 261 | "Resolves the predicted spectral **contrast**" |

So the two signals are complementary, not nested: 253 families are named-target resolutions by at
least one of them, and a family can be tagged and uncolumned. Quote them as two floors.

`hypothes` is **not** in `TARGET_NOUN`, and adding it is a new measurement, not a tweak — it would
also catch "under the hypothesis" phrasing that the `conditional` tag already owns. Not done.

### What the column adds inside T0

T0 has no coverage signal, so `shapes` was its only discriminator. The column is a second one: **91 of
the 137 T0 families are flagged, 46 are not** (88 / 49 under the abstract-only scope). Cross-tabbed
against the first-match buckets (`triage_t0.py`, bucket: column=1 / column=0):

| Bucket | 1 / 0 | Reading |
|---|---|---|
| C counterexample | 13 / 3 | disprove-form resolutions, already the cheapest T0 checks |
| R resolution | 48 / 2 | the 2 column-negatives are 010 and 103, both tag-only |
| B bound | 7 / 22 | |
| K classification | 4 / 4 | |
| U uniform | 5 / 7 | |
| O other | 2 / 0 | |
| N untagged | 12 / 8 | **the payoff** |

43 flagged T0 families (60 manuscripts) sit outside bucket R — first match assigns them elsewhere, so
the bucket table alone never shows them as named-target resolutions.

The N bucket is described in `notes/t0-triage.md` as "no shape tag at all — title is the only signal".
Half of it is now not title-only; all 12 are named-conjecture families: 019, 031, 043, 051, 060, 164,
195, 258, 306, 316, 338, 341. Those are the T0 families where the abstract names a conjecture and the
`resolution` pattern matched none of its verbs, which is exactly the miss this file measures.

## Not checked

- Every judgment here is from the release's own abstract. No manuscript was read, so "resolves
  conjecture X" remains the release's claim, not a checked fact.
- No conjecture was identified in the literature, and no formalized statement was compared with the
  claim (no Lean run).
- The reading in this file is measured on abstracts only. Titles were not read, and `CONTENTS.md`
  abstracts were not cross-checked against `overview.tex` for this measurement. The applied column
  does read the title, so the 15 title-scope additions sit outside every verdict recorded here.
- The `resolves_named` column inherits every ceiling above: it is computed from the overview title
  and abstract, it is
  not a claim, and the 5 tag-only families were read only as the abstract fragment around
  `resolv`/`settl` — their full abstracts were not read, so a target noun could exist outside the
  matched window.
- Precision was measured on the flags the candidate rule raises. What it would *continue* to miss
  (a resolution stated with no target noun and no listed verb) was not measured.
