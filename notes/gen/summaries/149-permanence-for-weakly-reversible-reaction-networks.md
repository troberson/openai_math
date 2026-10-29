[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 149](../index/dynamical-systems-and-ergodic-theory/149-permanence-for-weakly-reversible-reaction-networks.md)

# 149 — Permanence for weakly reversible reaction networks

[Index page](../index/dynamical-systems-and-ergodic-theory/149-permanence-for-weakly-reversible-reaction-networks.md)

## Original CONTENTS.md summary

The release's blurb [S1:3566] and the catalog abstract [S2:379] state
the family's claim: the permanence conjecture holds for every finite
weakly reversible mass-action system with fixed positive rate
constants — every positive stoichiometric compatibility class, even
an unbounded one, has a common compact convex forward-invariant
absorbing set, so all positive trajectories in that class eventually
share positive lower and finite upper concentration bounds. The
headline classwise-permanence manuscript's abstract 

> We prove the permanence conjecture for finite weakly reversible mass-action
systems with fixed positive reaction rates. Every positive stoichiometric
compatibility class admits one compact convex forward-invariant set that
every positive trajectory in that class enters in finite time, even when
the class is unbounded. The set depends only on the network, the rates, and
the class; the entry time may depend on the initial state. Thus, after its
entry time, every concentration satisfies the same positive lower and
finite upper bounds throughout that class. [S3:44–51]

The family ships two manuscripts: the classwise (uniform) permanence
statement and the per-trajectory boundedness-and-persistence statement
it subsumes.

## Undergraduate summary

A *mass-action system* is a set of chemical reactions whose rate of
each reaction is a monomial in the concentrations. A *stoichiometric
compatibility class* is the affine slice of state space a trajectory
cannot leave (concentrations evolve within a fixed conservation
manifold). A trajectory is *persistent* if no species' concentration
tends to zero, and *bounded* if no concentration runs away to
infinity; the *permanence* of a class means every positive trajectory
in it is both persistent and bounded. A reaction network is
*weakly reversible* when, in its reaction graph, one can travel from
any reaction to any other by a directed path — a natural
"every ingredient is reachable from every other" condition. The family
shows that for every finite weakly reversible system with positive
rates, every positive compatibility class (bounded or unbounded)
admits one common compact convex absorbing set that every positive
trajectory enters in finite time, and that after its entry time every
concentration of every trajectory in the class stays between one
positive lower bound and one finite upper bound [S3:44–51, S5:9].

## Graduate summary

**Classwise (uniform) permanence (headline)** [S3:44–51]. For a
finite weakly reversible mass-action system with fixed positive rates,
every positive stoichiometric compatibility class — even an
unbounded one — admits one compact convex forward-invariant set
$`C`$ that **every** positive trajectory in the class enters in finite
time; $`C`$ depends only on the network, the rates, and the class, while
the entry time may depend on the initial state. After its entry time,
every concentration of every trajectory in the class satisfies the same
positive lower and finite upper bounds [S3:44–51]. This is a
common-absorbing-set statement for the whole class, stronger than a
per-trajectory bound.

**Per-trajectory boundedness and persistence (companion)** [S4:35–40,
S5:9]. For every positive initial condition, the solution exists for
all forward time (a global forward solution), and one
$`\varepsilon\in(0,1)`$ bounds every concentration of every global
forward solution between $`\varepsilon`$ and $`\varepsilon^{-1}`$ for all
nonnegative times; the bound may depend on the network, the rates, and
the initial state, and no boundedness assumption is imposed on the
stoichiometric compatibility class [S4:35–40, S5:9].

## History of the conjecture

The permanence problem for mass-action systems asks when positive
solutions stay bounded above and bounded away from zero for all time.
It is a central question in chemical reaction network theory, tied to
the long-standing persistence analysis of weakly reversible networks.
Classical work (the Horn–Jackson and Feinberg lines of
sufficiency conditions) identified structural regimes where positive
trajectories are persistent, and persistence for weakly reversible
systems is a known foothold; the full permanence statement —
boundedness *and* persistence, for **every** weakly reversible system,
including the unbounded compatibility classes, with a common absorbing
set for the whole class — is the claim this family asserts
[S3:44–51, S4:35–40].

**Prior (my training data, not this repo).** I know the
persistence framework for weakly reversible mass-action systems and
that positive trajectories of such systems stay bounded away from zero
under the standard conditions; boundedness on bounded compatibility
classes is routine, and that is where the classical results land. A
*permanence* result covering the unbounded compatibility classes, and
a single **classwise** compact convex absorbing set shared by every
positive trajectory of the class, is, to my knowledge, beyond the
sufficiency results I was trained on. I cannot independently verify
either manuscript's argument.

## Consequences

**Permanence for weakly reversible mass-action systems (per
trajectory).** Every positive trajectory of a finite weakly reversible
mass-action system with positive rates exists for all forward time and
has every concentration bounded above and bounded away from zero
[S4:35–40, S5:9].

**Classwise absorbing set.** Every positive stoichiometric compatibility
class, even an unbounded one, has a common compact convex forward-
invariant set that every positive trajectory in the class enters in
finite time [S3:44–51].

**A uniform-in-time $`\varepsilon`$ bound.** One $`\varepsilon\in(0,1)`$
bounds every concentration of every global forward solution between
$`\varepsilon`$ and $`\varepsilon^{-1}`$ for all nonnegative times [S5:9].

## Section skeleton

Two manuscripts:

- **classwise permanence (headline)** [S3:44–51] (title [S3:38], date
  [S3:40]) — `main.tex` under `build/`; 990 lines total; one
  `references.bib`.
- **boundedness + persistence (companion)** [S4] (title [S4:29], date
  [S4:31]) — `paper.tex` under `build/`; 1,252 lines total; one
  `references.bib`.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalization proves the boundedness and
persistence conjectures for mass-action systems: for every finite
weakly reversible reaction network with positive constant reaction
rates and every strictly positive initial state, a global forward
solution exists, and one $`\varepsilon\in(0,1)`$ bounds every
concentration of every global forward solution between $`\varepsilon`$
and $`\varepsilon^{-1}`$ for all nonnegative times; the bound may depend
on the network, the rates, and the initial state [S5:9]. This is the
per-trajectory statement (the companion manuscript's claim), not the
headline classwise common-absorbing-set statement. The scope note links
only the companion manuscript and names one comparator [S5:13–15]:
`MassAction.lean`.

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming the comparator theorem for this family, and
neither manuscript appears in its `sources:` listing. The scope note and
one comparator stub exist, but the release has not registered a single
declaration as a family result. The `MassAction.lean` comparator states
the global boundedness-and-persistence claim as a `sorry`-terminated
theorem 

```lean
theorem global_bounded_persistent_solution :
    ∀ (d : ℕ) (N : ReactionNetwork d) (κ : Reaction N → ℝ),
      0 < d → WeaklyReversible N → (∀ e, 0 < κ e) →
      ∀ x0 : Fin d → ℝ, PositiveState x0 →
      ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
        (∃ x : ℝ → (Fin d → ℝ), IsGlobalForwardSolution N κ x0 x) ∧
        ∀ x : ℝ → (Fin d → ℝ), IsGlobalForwardSolution N κ x0 x →
        ∀ t : ℝ, 0 ≤ t → ∀ i : Fin d, ε ≤ x t i ∧ x t i ≤ ε⁻¹ := by
  sorry
```
[S6:46–54]

**What the OAI tree does carry.** Under the tree's `OAI/Analysis/`
directory there is a substantial `MassAction` package (71 files over
7,758 lines, zero `sorry`) with subfiles matching the affine-
certificate and compact-bounds machinery the comparison is built on
(`CompactBounds`, `BarrierTrapping`, `FixedMinimum`, the `Affine*`
certificate files, `ODEGlobal`, `LocalExistence`, `Main.lean`,
`Model.lean`). A `main_results` registration would link the scope note's
comparator to a declaration in this package, but none is registered.
The release records `scope: "Partial progress."` and
`review: status: unchecked`; zero `sorry` in the Lean source is not a
comparator pass, and the library has not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=149` records `paps 2`, `paps_form 0`,
`tier T2`, `chal 1`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes resolution|bound|uniform`, `resolves_named 1`,
`counterex_broad 0`, `summary 1`. The family ships two LaTeX
manuscripts (990 + 1,252 lines), a scope note naming one comparator
(itself targeting the per-trajectory boundedness+persistence claim, not
the headline classwise absorbing-set statement), and one
`sorry`-terminated comparator stub. The OAI tree carries one
unregistered formalization package (`OAI/Analysis/MassAction`, 71 files
over 7,758 lines, zero `sorry`) matching the comparator, but no
`main_results` entry links it and neither manuscript is in
`formalization.yaml`'s `sources:`. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 149 at [S1:3566] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{149} at [S2:379] |
| S3 | [`preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/build/main.tex`](../../../preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/build/main.tex) | 62 | headline manuscript root (classwise permanence); title [S3:38], date [S3:40], abstract [S3:44–51] |
| S4 | [`preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/build/paper.tex`](../../../preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/build/paper.tex) | 47 | companion manuscript root (boundedness + persistence); title [S4:29], date [S4:31], abstract [S4:35–40] |
| S5 | [`lean/docs/149.md`](../../../lean/docs/149.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:13–15] |
| S6 | [`lean/ComparatorChallenges/MassAction.lean`](../../../lean/ComparatorChallenges/MassAction.lean) | 60 | comparator stub: the `global_bounded_persistent_solution` theorem [S6:46–53] and the `sorry` [S6:54] |
