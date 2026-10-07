# Conditional families — manual pass

The `conditional` tag in `notes/catalog.tsv` is a keyword match on the family abstract. Reading
the flagged abstracts is the only way to name the hypothesis. This file records that reading:
**what each family assumes, where the assumption sits, and what the formalization covers.**

Five families are genuinely conditional. Five of the original nine flags were false positives
(listed at the end) and are now excluded by the tag.

| Fam | Discipline | Tier | Formalized | Assumption | Where it sits |
|---|---|---|---|---|---|
| 014 | Number theory | T0 | 0 / 8 | three scoped hypotheses, plus an assumed decomposition | sub-claims; headline result is unconditional |
| 125 | Theoretical CS | T3 | 1 / 2 | `P ≠ NP` | lower-bound half only; the algorithm is unconditional |
| 240 | Mathematical logic | T3 | 1 / 2 | Continuum Hypothesis | the *formalized* part; the ZFC main theorem is not formalized |
| 244 | Mathematical logic | T3 | 1 / 1 | `Con(ZF)`; a countable transitive ground model | the theorem's native form (relative consistency) |
| 282 | Mathematical physics | T0 | 0 / 1 | "bounded-local-net and field-reconstruction hypotheses" | all of it; no scope note exists |

## 014 — Restricted geometric Langlands, generic Ramanujan and Arthur parameters

Number theory · T0 · 8 manuscripts · 0 formalized · no scope note.

Three assumptions, each attached to a specific sub-claim, not to the family headline:

1. Geometric Langlands equivalence for tamely ramified `L`-parameters over `F̄_q`:
   *"under the four stated Lie-theoretic characteristic hypotheses"* — **the four hypotheses are
   not enumerated in the abstract.** They live in the manuscript, so this family's assumptions
   cannot be checked from catalog metadata at all.
2. The same conclusion over an arbitrary algebraically closed field of characteristic `p > 0`:
   *"assuming additionally that `p` is very good for the group and `p` does not divide the order
   of the Weyl group."*
3. The Arthur-parameter enhancements: *"Assuming the finite-level Ramanujan–Arthur
   decomposition, constructs global Arthur enhancements…"* — an assumed decomposition statement,
   used as input to a construction.

The headline statement is unconditional: Ramanujan at every place for globally generic cuspidal
representations of split adjoint absolutely simple **exceptional** groups, with no characteristic
or ramification-depth restriction.

Triage note: T0 with 8 manuscripts and no scope note. Every assumption here is readable only in
the PDF. This is the family where the ledger is weakest and the reading matters most.

## 125 — Metric k-median: optimal approximation and fine-grained hardness

Theoretical CS · T3 · 4 configs (`KMedianRecovery`, `KMedianRefinedRecovery`, `KMedianThreshold`,
`MetricKMedian`) · 1 of 2 manuscripts formalized.

Assumption: **`P ≠ NP`**, and it is scoped to the optimality half only.

- Unconditional: the algorithm — *"a polynomial-time (1 + 2/e + ε)-approximation algorithm for
  every fixed ε > 0."*
- Conditional: *"Assuming `P ≠ NP`, the optimal infimum approximation factor is exactly
  `1 + 2/e`."*

The scope note confirms the conditional half is inside the formalization: *"Assuming `P ≠ NP`, it
also proves that the infimum of all polynomial-time approximation factors in this model is exactly
`1 + 2/e`."* So the Lean statement carries `P ≠ NP` as a hypothesis — the result is a
conditional lower bound, not an unconditional one.

## 240 — Shelah's eventual categoricity for AECs with small LS

Mathematical logic · T3 · 1 config (`CHObstruction`) · 1 of 2 manuscripts formalized.

The main theorem is **unconditional**: *"Shelah's eventual categoricity theorem: in ZFC, an
exhaustive class of structures categorical in one sufficiently large cardinal is categorical in
every larger cardinal."*

The conditional statement is a separate result: *"Under the continuum hypothesis, a proposed
specific Hanf threshold need not suffice."*

What the formalization actually covers is the conditional part, not the flagship theorem. Scope
note: the formalized result is *"a countable relational language with LS = ℵ₀, an AEC categorical
in every cardinal at least `beth_{(2^{aleph_1})^+}`, with two nonisomorphic models in
`beth_{omega_2} = h(aleph_0)`"* — a CH-based refutation of a proposed Hanf threshold. The note
states explicitly: *"The later canonical-point obstruction and the separate eventual-categoricity
theorem are not included."*

Triage note: the config name `CHObstruction` is the tell. The unconditional ZFC theorem is the
family's headline and is **not** formalized; the formalized statement is the one that assumes CH.

## 244 — The partition principle does not imply choice

Mathematical logic · T3 · 2 configs (`PartitionConsistency`, `PartitionPrinciple`) · 1 of 1
manuscripts formalized.

Assumption: **`Con(ZF)`** — *"Assuming ZF is consistent, constructs a model in which every
surjective image of a set injects into that set, yet AC fails."* This is not a side hypothesis;
relative consistency is the native form of an independence result, so the tag here is expected
rather than a weakness.

A second construction assumes a **countable transitive model of ZFC** (a meta-theoretic ground
model) containing an internal strongly inaccessible cardinal. Scope note: the formalized pair
covers the relative-consistency implication (ZF consistent ⇒ ZF + PP + choice for ordinal-indexed
families + ¬AC consistent); the model-construction result *"assumes a countable transitive model
of ZFC containing an internal strongly inaccessible cardinal"*, and *"the paper's stronger
transitive-model preservation assertions are outside that selected construction."*

## 282 — Scale-to-conformal enhancement in four-dimensional QFT

Mathematical physics · T0 · 1 manuscript · 0 formalized · no scope note.

Assumption, quoted: *"Under the stated bounded-local-net and field-reconstruction hypotheses,
proves that scale symmetry implies local conformal symmetry for four-dimensional unitary
positive-energy theories with discrete bounded-below scaling spectrum of finite multiplicity and
finite scaling support, provided the physical local scale current is divergence-free."*

So the hypotheses are: bounded local net, field reconstruction, unitarity, positive energy,
discrete bounded-below scaling spectrum of finite multiplicity, finite scaling support,
divergence-free local scale current. The abstract names two of them ("stated
bounded-local-net and field-reconstruction hypotheses") without listing them; the rest are folded
into the claim's own conditions.

Scope of the conclusion, from the abstract: *"The conclusion concerns local Ward identities, not a
global conformal action on the whole net."*

Triage note: T0, no scope note, nothing formalized. The hypothesis list is only as precise as the
abstract, and the abstract says "stated" rather than stating.

## Dropped flags (false positives)

The original tag matched 9 families. Reading each abstract showed 5 matches that are not
assumptions:

| Fam | Title | Matched text | Why it is not a conditional result |
|---|---|---|---|
| 023 | Optimal strong inapproximability for 3-LIN | "Proves **unconditionally** that no poly-time algorithm…" | The word is inside "unconditionally". |
| 133 | Exponentially small gaps for 2-to-1 games | "Proves **unconditional** `n^{Ω(k)}` lower bounds" | Same. |
| 224 | Near-critical percolation crossing thresholds | "the **conditional** joint near-critical crossing-threshold laws" | Adjective on a noun ("conditional laws"), not a hypothesis. |
| 290 | Sharp hypercontractivity for the 2-cube | "faithful normal **conditional expectation**" | Technical term: the conditional-expectation operator. |
| 328 | Convergence of the inert Navier–Stokes system | "**without assuming** uniform convexity" | Negation — the absence of an assumption is the point of the theorem. |

Tag rule now in `notes/scripts/build_catalog.py`: match `assuming`, `we assume`, `provided that`,
`conditioned on`, `under the … hypothesis/conjecture/assumption`, and bare `conditional` only when
not followed (within 60 chars, no sentence break) by `expectation|law(s)|probability|measure|
distribution|density` and not preceded by `without`/`no`.

`unconditional` never matched: `\bconditional\b` has no word boundary inside it, so 023 and 133
were dropped by the word-boundary fix alone.

## Consequence for the ledger

`conditional` drops from 9 families to 5. Of those 5, three (125, 240, 244) are T3 with the
assumption inside the formalized statement, and two (014, 282) are T0 with no formalization and no
scope note — i.e. the assumption is stated only in prose, in one case as "the stated …
hypotheses" without enumeration.
