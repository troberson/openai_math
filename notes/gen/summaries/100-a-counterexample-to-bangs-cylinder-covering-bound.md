[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 100](../index/convex-and-metric-geometry/100-a-counterexample-to-bangs-cylinder-covering-bound.md)

# 100 — A counterexample to Bang's cylinder-covering bound

[Index page](../index/convex-and-metric-geometry/100-a-counterexample-to-bangs-cylinder-covering-bound.md)

## Original CONTENTS.md summary

The release's blurb [S1:2452] and the catalog abstract [S2:276] state
the family's claim: the closed regular tetrahedron is covered by
finitely many cylinders with compact triangular perpendicular bases
whose total area is less than half its smallest orthogonal projection
area. This disproves Bang's half-area cylinder-covering bound and the
stronger directionwise normalized conjecture in dimension three. The
headline angular-covers manuscript's abstract 

> A regular tetrahedron admits a finite cylinder covering with compact triangular
perpendicular bases whose total area is less than half its minimum orthogonal
projection area. This disproves the half-area cylinder-covering conjecture.
By affine invariance, the same construction gives a counterexample to the
directionwise normalized half-bound for every nondegenerate tetrahedron. [S3:14–18]

The family ships four manuscripts: the two counterexample constructions
and two companion finite-approximation theorems.

## Undergraduate summary

A *cylinder cover* of a convex body is a finite union of cylinders
whose axes are parallel to some direction
$`v_i`$ and whose perpendicular bases
$`B_i`$ are compact sets in the plane perpendicular to $`v_i`$. The
*perpendicular-base area* of the cover is
$`\sum_i\mathrm{area}(B_i)`$, and the *minimum projection area*
$`\mathrm{proj}_{\min}K`$ is
$`\min_u\mathrm{area}(K|u^\perp)`$ — the smallest area the body
has when projected perpendicular to some direction $`u`$.

Bang's conjecture (generalized from a classical bound) predicts that
every cylinder cover of a convex body $`K`$ has perpendicular-base area
at least
$`\mathrm{proj}_{\min}K/2`$. The family shows this fails in dimension
three: the regular tetrahedron has a finite cylinder cover with
perpendicular-base area strictly below half its minimum projection
area [S3:14–18]. By affine invariance the same construction
gives a counterexample to the *directionwise normalized* half-bound
(the ratio of base area to the projection area in the axis
direction) for every nondegenerate tetrahedron [S3:17–18].
For the explicit small covering parameter $`\varepsilon`$ the
normalized area is
$`1/2-(13/6000)\varepsilon^2+O(\varepsilon^4)`$, giving a strict
quadratic saving [S7:12].

## Graduate summary

**The angular cover** [S3:14–18]. The first manuscript gives a
finite cylinder cover of the regular tetrahedron with compact
triangular perpendicular bases whose total area is strictly less than
half its minimum projection area; the affine invariance of the
normalized form extends the conclusion to every nondegenerate
tetrahedron [S3:17–18].

**The slope-field perturbation** [S5:36–41]. A second,
independent construction: the classical two-cylinder covering of a
regular tetrahedron can be perturbed by a slope field to give finite
covers with total perpendicular base area strictly below half the
minimum projection area, and the covers yield negative answers to both
the half-area question and the directionwise normalized half-bound
[S5:36–41].

**The radial-sweep approximation** [S6:28–35]. A third
counterexample route: radially aligned segment sweeps admit finite
cylinder covers with one triangular base per interval of any tagged
partition; as the partition mesh tends to zero, the total
perpendicular-base area converges to a weighted parameter area, and an
explicit application covers every regular tetrahedron with total base
area below half its minimum projection area [S6:28–35].

**The ruled-set companion** [S4:49–57]. A companion theorem
approximates compact ruled families of line segments by finitely many
cylinders with square intercept tiles, the perpendicular-base area at
most the integral projection cost plus any positive error; the
velocity field is $`C^1`$ and its differential has opposite real
eigenvalues whose magnitudes are strictly below the inverse segment
half-length [S4:49–57].

## History of the conjecture

Bang's 1951 classical result bounds the surface area of a unit ball by
a cylinder cover (in particular, its total perpendicular cross-section
area is at least
$`2\cdot\mathrm{area}(\mathrm{unit disk})=2\pi`$, the half-ball
projection), and the conjectural extension to general convex bodies
was open in dimension three. The family resolves the dimension-three
case negatively for the regular tetrahedron: three independently
motivated constructions (angular, slope-field, radial-sweep) each
produce a strict saving, and the affine-invariance argument extends
the directionwise conclusion to every nondegenerate tetrahedron.

**Prior (my training data, not this repo).** I know Bang's 1951
surface-area bound and the conjectural generalization to arbitrary
convex bodies. A counterexample in dimension three —
let alone the tetrahedron as a witness
— is, to my knowledge, not established in the literature I was
trained on. I cannot independently verify these four manuscripts'
arguments.

## Consequences

**Bang's bound fails in dimension three.** The regular tetrahedron has
a finite cylinder cover with total perpendicular-base area strictly
below half its minimum projection area [S3:14–18,
S5:36–41, S6:28–35].

**Directionwise normalized half-bound also fails.** By affine
invariance the directionwise conclusion extends to every nondegenerate
tetrahedron [S3:17–18, S5:40–41, S6:34–35].

**Explicit saving.** For the covering parameter $`\varepsilon`$ the
normalized area is
$`1/2-(13/6000)\varepsilon^2+O(\varepsilon^4)`$ [S7:12] — the
saving is quadratic in $`\varepsilon`$.

## Section skeleton

Four manuscripts:

- **angular covers** [S3:14–18] (title [S3:8], date [S3:10]) — `main.tex`
  under `build/`; 1,445 lines total.
- **ruled sets** [S4] (title [S4:43], date [S4:45]) — `main.tex`
  under `build/`; 947 lines total.
- **slope field** [S5] (title [S5:30], date [S5:32]) — `main.tex`
  under `build/`; 1,742 lines total.
- **radial sweeps** [S6] (title [S6:22], date [S6:24]) —
  `main.tex` under `build/`; 2,014 lines total.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S7:12]. The formalized counterexample is a finite
cover of the regular tetrahedron by cylinders with compact triangular
perpendicular bases whose total area is strictly below the half-area
bound; for the explicit small parameter $`\varepsilon`$ the normalized
area is
$`1/2-(13/6000)\varepsilon^2+O(\varepsilon^4)`$. A companion theorem
gives a counterexample to the directionwise normalized half-bound
[S7:12]. The scope note **excludes** the affine extension to every
nondegenerate tetrahedron; the selected statements are the
regular-tetrahedron ones [S7:22]. It names four comparator rows to
three distinct configs: `CylinderCovering.lean` is linked twice
(counterexample aggregate, and ruled-set approximation within the
same aggregate), plus `TriangularCovering.lean` and `RuledCovering.lean`
[S7:28–35].

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming any comparator theorem for this family,
and none of the four manuscripts appears in its `sources:` listing.
The scope note and three comparator stubs exist, but the release has
not registered a single declaration as a family result. The
`TriangularCovering.lean` comparator states the three-part claim
(assembly, asymptotic, normalized counterexample) as a
`sorry`-terminated theorem [S8:62–66]:

```lean
theorem main : A_min = H ∧ MainAsymptotic ∧ NormalizedCounterexample := by
  sorry
```
[S8:65–66]

**What the OAI tree does carry.** Under the tree's
`OAI/Geometry/` directory there are three substantial packages matching
the three distinct comparators: `CylinderCovering` (602 files,
64,073 lines), `RuledCovering` (30 files, 4,303 lines), and
`TriangularCovering` (9 files, 2,247 lines) — 641 files over
70,623 lines, zero `sorry`. A `main_results` registration would link
the scope note's three configs to declarations in these packages, but
none is registered. The release records `scope: "Partial progress."`
and `review: status: unchecked`; zero `sorry` in the Lean source is
not a comparator pass, and the library has not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=100` records `paps 4`, `paps_form 0`,
`tier T2`, `chal 3`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes counterexample|bound`, `resolves_named 1`,
`counterex_broad 1`, `summary 1`. The family ships four LaTeX
manuscripts (1,445 + 947 + 1,742 + 2,014 lines), a scope note naming
three distinct comparator configs (in four table rows, with
`CylinderCovering.lean` linked twice), and three
`sorry`-terminated comparator stubs. The OAI tree carries three
unregistered formalization packages under `OAI/Geometry/` (641 files
over 70,623 lines, zero `sorry`) matching the three comparators, but
no `main_results` entry links them and none of the four manuscripts
is in `formalization.yaml`'s `sources:`. The family ships no
verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 100 at [S1:2452] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{100} at [S2:276] |
| S3 | [`preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/build/main.tex`](../../../preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/build/main.tex) | 34 | headline angular-covers manuscript; title [S3:8], date [S3:10], abstract [S3:14–18] |
| S4 | [`preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/build/main.tex`](../../../preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/build/main.tex) | 68 | ruled-set approximation manuscript; title [S4:43], date [S4:45], abstract [S4:49–57] |
| S5 | [`preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/build/main.tex`](../../../preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/build/main.tex) | 56 | slope-field perturbations manuscript; title [S5:30], date [S5:32], abstract [S5:36–41] |
| S6 | [`preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/build/main.tex`](../../../preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/build/main.tex) | 48 | radial-sweep approximation manuscript; title [S6:22], date [S6:24], abstract [S6:28–35] |
| S7 | [`lean/docs/100.md`](../../../lean/docs/100.md) | 37 | the formalization scope note: the scope paragraph [S7:12], the exclusion line [S7:22], and the four-row comparator table [S7:28–35] |
| S8 | [`lean/ComparatorChallenges/TriangularCovering.lean`](../../../lean/ComparatorChallenges/TriangularCovering.lean) | 72 | triangular-cover comparator stub: the `NormalizedCounterexample` def [S8:62–63], the `main` theorem [S8:65], and the `sorry` [S8:66] |
