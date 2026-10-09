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
`1 + 2/e`."* The result is a conditional lower bound, not an unconditional one — **but the
hypothesis is not in the declaration the ledger links**; see the source-check section. The proved
`P ≠ NP`-conditional theorem is in the tree, in a sibling directory of the formalized one.

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

The source check reverses which of the two is in `main_results`: the linked declaration is the
**model construction**, whose hypothesis is the countable transitive ZFC ground model with an
internal strongly inaccessible cardinal. The `Con(ZF)` implication exists only as a `sorry`-stub
comparator link. See the source-check section.

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

## Source check of the three T3 families (read 2026-10-07)

The table above records what the **abstract** assumes. The bead's question is sharper: does the
hypothesis also sit in the **formalized statement**, meaning the `main_results` declaration named in
`lean/formalization.yaml`? Read statically — no build, no `lake`, no comparator — the answer is
**yes for 240, no for 125, and "more than the abstract says" for 244**. The sharp case is confirmed
exactly as stated.

**240 — the hypothesis is in the linked declaration, and the ZFC theorem is not in the tree.**
`main_results` names `OAI.CHObstruction.main` (`lean/formalization.yaml:999`); the declaration sits
at `lean/OAI/ModelTheory/Categoricity/Main.lean:233`:

```
theorem main (hCH : CH.{u}) :
    ∃ (L : ℕ → Type), Countable (Σ n, L n) ∧
      ∃ K : ClassData.{u} L, K.IsAEC ∧ K.HasLSNumber ℵ₀ ∧
        endpoint = hanf (ℵ₀ : Cardinal.{u}) ∧ K.TwoModels endpoint ∧
```

`hCH : CH.{u}` is a literal hypothesis of the theorem, and `CH` is defined locally rather than
taken from Mathlib: `def CH : Prop := (2 : Cardinal.{u}) ^ ℵ₀ = ℵ_ 1` at
`lean/OAI/ModelTheory/Categoricity/Model.lean:101`. The unconditional ZFC theorem is absent: every
categoricity statement in the tree takes `hCH` (a `grep` for `theorem` lines naming `Categorical`
without `hCH` returns nothing), and `lean/docs/240.md` lists only the CH manuscript. The tree is
15 files / 5,089 lines with zero `sorry`, so within its declared scope the CH-conditional result is
carried in full.

**125 — the hypothesis is NOT in the linked declaration.** `main_results` names
`OAI.MetricKMedianRecovery.global_application` (`lean/formalization.yaml:1259`) at
`lean/OAI/Combinatorics/KMedianRecovery/Main.lean:21`, whose statement is `globalApplicationClaim`
(`lean/OAI/Combinatorics/KMedianRecovery/Model.lean:94`):

```
def globalApplicationClaim : Prop :=
  ∃ σ : ℝ, 0 < σ ∧ ∀ a : ℝ, 0 < a → ∃ A : BinaryRandomizedAlgorithm,
```

— an unconditional `(2 - σ) * optimum` randomized-recovery claim. There is no `P ≠ NP` hypothesis
anywhere in the `KMedianRecovery` tree (522 files, 71,509 lines, zero `sorry`). The conditional
threshold result **is** formalized and proved, in a sibling tree the yaml does not link:
`lean/OAI/Combinatorics/KMedian/Threshold.lean:25`

```
theorem threshold (h : Complexity.PNeNP) :
    sInf approximationFactors=1+2/Real.exp 1 := by
```

with `def PNeNP : Prop := P ≠ NP` at `lean/OAI/Combinatorics/KMedian/Hardness/Model.lean:30`, and a
real proof (`le_antisymm infimum_le_threshold` plus `le_csInf approximationFactors_nonempty
(below_threshold_impossible h)`). So the sentence in the 125 section — "the Lean statement carries
`P ≠ NP` as a hypothesis" — is true of the tree and false of the declaration the ledger's `mainres`
points at. The scope note is accurate about the formalization; the `main_results` entry is not the
theorem it describes.

**244 — the linked declaration assumes strictly more than `Con(ZF)`.** `main_results` names
`OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice`
(`lean/formalization.yaml:1363`) at
`lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean:34`, whose last hypotheses
(`lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean:39`) are:

```
    (choice : Realize M.sets SetFormula.choice Fin.elim0)
    (small : M.sets.Countable)
    {K : ZFSet.{u}} (hK : K ∈ M.sets) (standard : GroundStandardInaccessible M K) :
```

Above them sit six realized ZF axioms (`pairing`, `unions`, `powers`, `separation`, `collection`,
`infinite`), `choice` among them — so the hypothesis is a **countable transitive ground model of
ZFC containing an internal strongly inaccessible cardinal**, and the conclusion is a transitive
inner model `N` with `partitionPrinciple` and `¬ choice`. The `Con(ZF)` form the abstract states
exists only as a challenge stub, `lean/ComparatorChallenges/PartitionConsistency.lean:318`:

```
theorem main_consistency :
    Consistent SetLanguage.ZF → Consistent SetLanguage.targetTheory := by
  sorry
```

(`def Consistent (T : Theory) : Prop := ∀ n, ¬ Derives (T.at n) .bot` at `:107`).
`PartitionConsistency` appears nowhere in `lean/formalization.yaml` — 0 occurrences — it is a
comparator link in the scope note (`lean/docs/244.md:18`). The yaml's 200 `main_results` entries
(189 distinct configs) carry exactly one `Partition*` config: `ComparatorChallenges/PartitionPrinciple.json`
at `lean/formalization.yaml:1449`, pointing at the `Separation.lean` declaration above. The scope
note's lead paragraph (`lean/docs/244.md:9`) says *"The formalization proves the
relative-consistency implication: if ZF is consistent, then so is ZF with the Partition Principle,
Choice for ordinal-indexed families, and failure of the Axiom of Choice."* — which the linked
declaration does not state: a scope-note/`main_results` mismatch, not a missing result.

**Why the comparator files mislead here.** `lean/ComparatorChallenges/*.lean` are challenge
**stubs**, not proofs: 416 files carrying 539 `sorry` occurrences, 415 of them at least one
(distribution 1:363, 2:25, 3:16, 4:6, 6:1, 9:1, 11:2, 17:1; the single zero-`sorry` file is
`HarmonicGrowth.lean`). By contrast, **zero** of the 122,458 files under `lean/OAI/**/*.lean`
contain `sorry`. A comparator file states the target the release set itself; the proved version of
that statement, where it exists, lives under `lean/OAI/`. Reading a comparator file and concluding
"the hypothesis is in the formalized statement" is reading the stub.

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

`conditional` drops from 9 families to 5. Of those 5, three (125, 240, 244) are T3 and two (014,
282) are T0 with no formalization and no scope note — i.e. the assumption is stated only in prose,
in one case as "the stated … hypotheses" without enumeration.

The source check narrows what "T3" buys. Only **240** has the abstract's hypothesis inside the
declaration `main_results` names. **125**'s linked declaration is unconditional; its conditional
theorem is proved in a sibling tree the yaml does not link. **244**'s linked declaration assumes a
countable transitive ZFC ground model with an internal strongly inaccessible cardinal, which is
strictly more than the `Con(ZF)` the abstract states. So "the assumption is inside the formalized
statement" is a claim about the **tree**, not about the linked declaration, and the family→config
join (by title, not by number) is where the two can diverge.

Not checked: nothing here was built. No `lake`, no `lean`, no comparator was run, so nothing
proves these files elaborate; the `sorry` counts are lexical matches, not a comparator pass.
`python3 notes/scripts/verify_conditional.py` resolves the 5 fenced blocks (14 lines), the 7 inline
`name → file:line` citations, and the 1 anchored prose quotation in the source-check section
against the shipped files, and catches all 5 injected mutants. It reports **15 unanchored prose
quotations** — the pre-existing abstract and scope-note quotes in the per-family sections above,
which carry no line anchors and are therefore not verified.
