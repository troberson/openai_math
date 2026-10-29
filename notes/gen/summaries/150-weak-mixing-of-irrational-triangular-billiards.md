[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 150](../index/dynamical-systems-and-ergodic-theory/150-weak-mixing-of-irrational-triangular-billiards.md)

# 150 — Weak mixing of irrational triangular billiards

[Index page](../index/dynamical-systems-and-ergodic-theory/150-weak-mixing-of-irrational-triangular-billiards.md)

## Original CONTENTS.md summary

The release's blurb [S1:3591] and the catalog abstract [S2:381] state
the family's claim: the billiard flow in every nondegenerate Euclidean
triangle with at least one angle irrational relative to $`\pi`$ is weakly
mixing for normalized area times uniform direction. This strengthens
ergodicity on the entire irrational-angle class, with no genericity or
Diophantine restrictions. The headline weak-mixing manuscript's abstract


> We prove that the unit-speed billiard flow in every nondegenerate Euclidean
triangle with at least one angle irrational relative to $`\pi`$ is weakly
mixing for normalized Liouville measure. Equivalently, the product of the
flow with itself is ergodic. [S3:31–34]

The family ships two manuscripts: the weak-mixing headline and the
ergodicity statement it subsumes.

## Undergraduate summary

A *billiard* is a ball moving a constant speed inside a triangular
table, reflecting off the edges by the usual law of reflection. Its
*billiard flow* tracks the position and direction of the ball as a
function of time; the natural measure is the area of the triangle times
a uniform distribution over directions (the *Liouville* measure). The
*ergodicity* of the flow means a typical trajectory eventually spreads
uniformly over the whole table-and-direction space; *weak mixing* is
stronger: the flow has no periodic structure, so a typical trajectory
scatters its initial correlation and the product of the flow with itself
is again ergodic — the flow forgets its own phase, not just its
position [S3:31–34]. The family proves weak mixing for **every**
nondegenerate triangle with at least one angle that is irrational
relative to $`\pi`$ — no "typical angle" or Diophantine
restriction needed [S3:31–34, S5:9].

## Graduate summary

**Weak mixing (headline)** [S3:31–34, S2:381]. The unit-speed
billiard flow in every nondegenerate Euclidean triangle with at least
one angle irrational relative to $`\pi`$ is weakly mixing for normalized
Liouville measure; equivalently, the product of the flow with itself is
ergodic. This is stated for the whole irrational-angle class, with no
genericity or Diophantine condition [S3:31–34].

**Ergodicity (companion, the formalized claim)** [S4:41–46, S5:9].
The unit-speed billiard flow in every nondegenerate Euclidean triangle
with at least one angle irrational relative to $`\pi`$ is ergodic for
normalized area times uniform angular measure. The flow is considered
outside the null set of trajectories that hit a vertex; the
formalization constructs the flow there, proves uniqueness of the flight
chain, and establishes measure preservation and the flow law almost
everywhere, with no genericity or Diophantine condition [S4:41–46,
S5:9].

## History of the conjecture

The ergodicity of the billiard flow on triangular tables was a long-
standing open problem: the general (non-rational) triangle case resisted
the tools that worked on rational and on a single generic class of
triangles. The *irrational-angle* regime — triangles with at least
one angle whose measure, as a multiple of $`\pi`$, is irrational
— is where the flow is expected to have no resonant periodic
structure, and hence to mix. The family asserts the full weak-mixing
conclusion on exactly that class, and records the ergodicity statement
(the flow is ergodic, with the flow constructed and shown measure-
preserving almost everywhere) as the formalized foothold [S3:31–34,
S4:41–46, S5:9].

**Prior (my training data, not this repo).** I know the ergodicity
problem for triangular billiards, that rational triangles (all angles
rational multiples of $`\pi`$) carry an integrable family of invariant
curves and are generically *not* ergodic, and that the irrational-angle
regime is where ergodicity is expected. That the *entire* irrational-
angle class is weakly mixing — uniformly, with no Diophantine
restriction on the angle — is, to my knowledge, beyond the
results I was trained on. I cannot independently verify either
manuscript's argument.

## Consequences

**Weak mixing on the irrational-angle class.** The billiard flow in
every nondegenerate Euclidean triangle with at least one angle irrational
relative to $`\pi`$ is weakly mixing for normalized Liouville measure
[S3:31–34, S2:381].

**Ergodicity (formalized).** The same flow is ergodic for normalized
area times uniform angular measure, with no genericity or Diophantine
condition [S4:41–46, S5:9].

**A constructed flow law.** The flow is constructed outside the null set
of vertex-hitting trajectories, with uniqueness of the flight chain,
measure preservation, and the flow law holding almost everywhere
[S5:9].

## Section skeleton

Two manuscripts:

- **weak mixing (headline)** [S3:31–34] (title [S3:25], date [S3:27]) —
  `main.tex` under `build/`; 938 lines total; one `references.bib`.
- **ergodicity (companion)** [S4] (title [S4:34], date [S4:36]) —
  `main.tex` under `build/source/`; 825 lines total; one
  `references.bib`.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalization proves that the unit-speed
billiard flow in every nondegenerate Euclidean triangle with at least
one angle irrational relative to $`\pi`$ is ergodic for normalized area
times uniform angular measure. It constructs the flow outside the null
set of exceptional trajectories, proves uniqueness of the flight chain
there, and establishes measure preservation and the flow law almost
everywhere; no genericity or Diophantine condition on the irrational
angle is assumed [S5:9]. This is the ergodicity statement (the companion
manuscript's claim), not the headline weak-mixing statement. The scope
note links only the companion manuscript and names one comparator
[S5:13–15]: `IrrationalTriangleBilliard.lean`.

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming the comparator theorem for this family, and
neither manuscript appears in its `sources:` listing. The scope note and
one comparator stub exist, but the release has not registered a single
declaration as a family result. The `IrrationalTriangleBilliard.lean`
comparator states the conclusion as a `sorry`-terminated theorem


```lean
theorem irrational_triangle_billiard (Q : Triangle) (hQ : Q.HasIrrationalAngle) :
    MainConclusion Q := by
  sorry
```
[S6:119–121]

The conclusion `MainConclusion Q` bundles the claims the flow must
satisfy (unit phase measure, nonempty flight chains almost everywhere,
uniqueness of the flight chain, measure preservation, the flow law, and
ergodicity as the final clause) [S6:108–117]. The body is a bare
`sorry`.

**What the OAI tree does carry.** Under the tree's `OAI/Dynamics/`
directory there is a substantial `TriangleBilliards` package (39 files
over 12,363 lines, zero `sorry`) with files matching the flow-construction
machinery the comparison is built on (`MeasurableFlow`,
`MeasurePreservation`, `FlightUniqueness`, `Koopman`, `Generators`,
`SmoothingLp`, `LongTrajectories`, `Main.lean`, `Model.lean`). A
`main_results` registration would link the scope note's comparator to a
declaration in this package, but none is registered. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library has
not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=150` records `paps 2`, `paps_form 0`,
`tier T2`, `chal 1`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes uniform`, `resolves_named 0`, `counterex_broad 0`,
`summary 1`. The family ships two LaTeX manuscripts (938 + 825 lines),
a scope note naming one comparator (itself targeting the ergodicity
claim, not the headline weak-mixing statement), and one
`sorry`-terminated comparator stub. The OAI tree carries one
unregistered formalization package (`OAI/Dynamics/TriangleBilliards`, 39
files over 12,363 lines, zero `sorry`) matching the comparator, but no
`main_results` entry links it and neither manuscript is in
`formalization.yaml`'s `sources:`. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 150 at [S1:3591] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{150} at [S2:381] |
| S3 | [`preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/build/main.tex`](../../../preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/build/main.tex) | 43 | headline manuscript root (weak mixing); title [S3:25], date [S3:27], abstract [S3:30–34] |
| S4 | [`preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026/build/source/main.tex`](../../../preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026/build/source/main.tex) | 825 | companion manuscript root (ergodicity); title [S4:34], date [S4:36], abstract [S4:41–46] |
| S5 | [`lean/docs/150.md`](../../../lean/docs/150.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:13–15] |
| S6 | [`lean/ComparatorChallenges/IrrationalTriangleBilliard.lean`](../../../lean/ComparatorChallenges/IrrationalTriangleBilliard.lean) | 126 | comparator stub: the `irrational_triangle_billiard` theorem [S6:119–120] and the `sorry` [S6:121] |
