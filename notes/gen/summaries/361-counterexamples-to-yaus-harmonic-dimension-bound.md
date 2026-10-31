[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 361](../index/differential-geometry/361-counterexamples-to-yaus-harmonic-dimension-bound.md)

# 361 — Counterexamples to Yau's harmonic dimension bound

[Index page](../index/differential-geometry/361-counterexamples-to-yaus-harmonic-dimension-bound.md)

## Original CONTENTS.md summary

[S1:8756] (family entry):

> **361. Failure of integer-degree harmonic dimension comparison.** Disproves Yau's proposed Euclidean dimension bound for harmonic functions of integer growth on manifolds with nonnegative Ricci curvature. For every sufficiently large integer *k*, a complete smooth metric on ℝ3 has at least $`(k+2)^2`$ independent harmonic functions of growth at most *k*, exceeding the Euclidean count $`(k+1)^2`$. The metric may depend on *k*. ([Lean](../../../lean/docs/361.md))

[S2:822] carries the `\resultentry` with two manuscripts —
manuscript 1 [S3] (the even-dimensional counterexample) and
manuscript 2 [S4] (the three-dimensional counterexample). The scope
note names **only** manuscript 1 [S5:5] and states the formalized
result 

> The formalized result disproves the proposed Euclidean upper comparison for dimensions of harmonic functions with integer polynomial growth. It constructs one complete smooth metric with nonnegative Ricci curvature on an even-dimensional Euclidean space, Euclidean near the origin and with asymptotic volume ratio strictly between zero and one, admitting more independent harmonic functions of the prescribed growth degree than the Euclidean count. The construction uses dimension $`16`$ and degree $`50000`$. Separate tangent-cone and cone-spectrum conclusions are not included. [S5:9]

## Undergraduate summary

On flat $`\mathbb R^n`$, the number of **harmonic functions** (functions
whose Laplacian is zero — the "equilibrium" functions, like the
temperature distribution in a steady state) that grow at most like
$`r^k`$ is a well-understood finite number: $`\binom{n+k}{n}`$. For
example, in $`\mathbb R^3`$ with growth degree $`k`$, the count is
$`(k+1)^2`$.

**Yau's proposed bound** said something similar should hold on curved
spaces with nonnegative **Ricci curvature** (a condition on how the
space curves on average): the number of such harmonic functions should
not *exceed* the Euclidean count.

This result says **no** — in two flavors. Manuscript 2 constructs a
metric on $`\mathbb R^3`$ where, for every large $`k`$, there are at
least $`(k+2)^2`$ such functions, more than the Euclidean $`(k+1)^2`$
(the metric can depend on $`k`$). Manuscript 1 sharpens the theme in an
even dimension: a metric on $`\mathbb R^{16}`$ at degree $`50000`$
admits strictly more such functions than the Euclidean count. The
release formalizes manuscript 1 (the even-dimensional one), not the
three-dimensional headline.

## Graduate summary

**Main theorem (manuscript 2, the three-dimensional headline)**
[S4:23–33, S1:8756].
For every sufficiently large integer $`k`$, there exists a complete
smooth metric on $`\mathbb R^3`$ with nonnegative Ricci curvature
admitting at least $`(k+2)^2`$ independent harmonic functions of
growth at most $`k`$, exceeding the Euclidean count
$`(k+1)^2`$ [S4:23–33]. The metric may depend on $`k`$.

**Formalized theorem (manuscript 1, the even-dimensional
counterexample)** [S3:89–97, S5:9].
There exists a complete smooth metric with nonnegative Ricci
curvature on the even-dimensional Euclidean space
$`\mathbb R^{16}`$, Euclidean near the origin and with asymptotic
volume ratio strictly between zero and one, admitting more
independent harmonic functions of growth degree $`50000`$ than the
Euclidean count [S5:9]. Separate tangent-cone and cone-spectrum
conclusions are not formalized [S5:9].

**The formalization** [S5:9, S7].
The scope note selects manuscript 1's even-dimensional construction,
*not* the three-dimensional headline in manuscript 2. The comparator
stub `HarmonicGrowth.lean` (104 lines) carries the metric/harmonic
machinery — `RicciNonnegative` [S7:39], `Complete` [S7:59],
`EuclideanNearOrigin` [S7:64], `PositiveSubunitAVR` [S7:77], and
`HarmonicGrowth` [S7:83] — and states
`theorem main : MainClaim` [S7:98] with the `sorry` at [S7:98]. The
`main_results` entry [S6:1303–1305] resolves the declaration
`OAI.HarmonicCounterexample.main` to
`lean/OAI/Geometry/HarmonicGrowth/Main.lean` [S8] (488 lines), entry
of a 36-file OAI tree carrying 0 `sorry`.

## History of the conjecture

The **harmonic dimension** of a Riemannian manifold — the dimension
of the space of harmonic functions of a given polynomial growth
degree — is a classical invariant studied in relation to the
manifold's geometry. In Euclidean space the dimension is exactly
$`\binom{n+k}{n}`$, counting the homogeneous harmonic polynomials of
degree $`\le k`$. **Yau's proposed comparison** asserted that on a
complete manifold with nonnegative Ricci curvature the harmonic
dimension at degree $`k`$ should not exceed the Euclidean value — an
analogue of the way nonnegative Ricci curvature bounds other
geometric quantities (the Bishop–Gromov volume comparison, the
Li–Yau gradient estimate).

The **novel contribution** is the **disproof** of that comparison, in
two forms [S3, S4]: a three-dimensional smooth counterexample where
the count exceeds $`(k+1)^2`$ by one for every large $`k`$ [S4:23–33],
and an even-dimensional ($`\mathbb R^{16}`$, degree $`50000`$)
counterexample with a controlled metric (Euclidean near the origin,
asymptotic volume ratio in $`(0,1)`$) admitting strictly more
functions [S3:89–97, S5:9]. The metric depending on $`k`$ in the
three-dimensional case is the essential flexibility: no *single*
metric serves all degrees.

**Prior (my training data, not this repo).** As of my training
cutoff, Yau's dimension comparison for harmonic functions of
polynomial growth under nonnegative Ricci curvature was a proposed
conjecture, not a theorem, and I am not aware of a published
disproof in the form stated here. The construction of a
nonnegative-Ricci metric with an excess of bounded-growth harmonic
functions is the claimed novelty. I cannot verify the
Riemannian-analytic construction independently from training alone.

## Consequences

- **Yau's harmonic dimension comparison is disproved**
  [S3:89–97, S4:23–33, S5:9]: on complete smooth manifolds with
  nonnegative Ricci curvature, the number of integer-growth harmonic
  functions can exceed the Euclidean count.
- **The three-dimensional counterexample is quantitative**
  [S4:23–33, S1:8756]: for every large $`k`$, a metric on $`\mathbb
  R^3`$ admits at least $`(k+2)^2`$ such functions, exceeding the
  Euclidean $`(k+1)^2`$ by one.
- **The metric may depend on the growth degree** [S1:8756,
  S4:23–33]: the three-dimensional counterexample uses a family of
  metrics indexed by $`k`$, not a single metric serving all degrees.
- **The formalized counterexample is the even-dimensional one**
  [S5:9, S3:89–97]: the release proves the $`\mathbb R^{16}`$, degree
  $`50000`$ construction, not the three-dimensional headline; the
  tangent-cone and cone-spectrum conclusions are not formalized.
- **A finite-arithmetic certificate ships with manuscript 1**
  [S9]: the counting check (`counting-check.py`) and its output are
  the non-Lean evidence bundled with the even-dimensional
  counterexample.

## Section skeleton

Two manuscripts, both with `build/paper.tex` roots.
Manuscript 1 [S3] (even-dimensional counterexample, 109 lines): 9
`input` files [S3:99–108]: `introduction`, `links`, `counting`,
`algebra`, `geometry`, `transmission`, `conclusion`,
`finite-selection`, `bibliography`. Manuscript 2 [S4]
(three-dimensional counterexample, 42 lines): 8 `input` files
[S4:34–41]: `introduction`, `crossings`, `angular-program`,
`geometry`, `transfer`, `matching`, `growth`, `bibliography`.
Manuscript 1 ships a **verification bundle** [S9]
(`counting-check.py` with `README.md` and `counting-check-output.txt`);
manuscript 2 ships none.

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note
[S5:9], one comparator stub [S7], **one** `main_results` entry
[S6:1303–1305], and one proved OAI tree [S8]. The T3 shape is "scope
note, comparator stub, `main_results` entry, and proved OAI tree (0
`sorry`)."

The formalization is **asymmetric with the headline**: the scope note
names only manuscript 1 [S5:5] (the even-dimensional counterexample,
$`\mathbb R^{16}`$ at degree $`50000`$), and states that as the formalized
result [S5:9], while the family's headline in the catalog is the
three-dimensional example [S1:8756]. The comparator stub
`HarmonicGrowth.lean` (104 lines) carries the metric/harmonic-growth
predicates and states `theorem main : MainClaim` [S7:98] with the
`sorry` at [S7:98] (1 in this stub). The `main_results` entry
[S6:1303–1305] resolves `OAI.HarmonicCounterexample.main` to
`lean/OAI/Geometry/HarmonicGrowth/Main.lean` [S8] (488 lines), entry
of a 36-file OAI tree carrying 0 `sorry`. The reading is of source
text only.

## Coverage

The ledger row `fam=361` [S10] records the tier and the counts:
`tier=T3`, `paps=2`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=575`, `verification=1`, `inputs=0`,
`trace=`. The T3 shape is "scope note, comparator stub,
`main_results` entry, and proved OAI tree (0 `sorry`)." The single
comparator stub carries 1 `sorry` [S7:98]. The shape flags are
`shapes=counterexample|bound|partial|uniform`, `resolves_named=0`,
`counterex_broad=1`, `covmd=0` — a **counterexample** (to Yau's
comparison) carrying a **bound** (the growth degree) and **partial**
(the metric may depend on $`k`$) and **uniform** (the excess holds for
every large $`k`$) character, with a named bound in the title. The
`verification=1` is the finite-arithmetic certificate [S9] bundled
with manuscript 1. Note `paps_form=1`: only manuscript 1 (the
even-dimensional counterexample) appears in `formalization.yaml`'s
`sources:` list; manuscript 2 (the three-dimensional headline) does
not — the scope note [S5:5] names only manuscript 1.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8756] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 361 at [S2:822] |
| S3 | [`preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/build/paper.tex`](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/build/paper.tex) | 109 | the `\documentclass` root (manuscript 1, the even-dimensional counterexample, the formalized one) — 109 lines, title [S3:83], date [S3:85], abstract [S3:89–97], 9 `input` files [S3:99–108] |
| S4 | [`preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/build/paper.tex`](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/build/paper.tex) | 42 | the `\documentclass` root (manuscript 2, the three-dimensional counterexample) — 42 lines, title [S4:18], date [S4:20], abstract [S4:23–33], 8 `input` files [S4:34–41] |
| S5 | [`lean/docs/361.md`](../../../lean/docs/361.md) | 15 | scope note — names only manuscript 1; Scope at [S5:9], comparator link at [S5:15] |
| S6 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry — [S6:1303–1305] |
| S7 | [`lean/ComparatorChallenges/HarmonicGrowth.lean`](../../../lean/ComparatorChallenges/HarmonicGrowth.lean) | 104 | comparator stub — 104 lines, `def MainClaim` [S7:92], `theorem main : MainClaim` [S7:98], `sorry` [S7:98] |
| S8 | [`lean/OAI/Geometry/HarmonicGrowth/Main.lean`](../../../lean/OAI/Geometry/HarmonicGrowth/Main.lean) | 488 | proved OAI declaration — 488 lines, 0 `sorry`; 36 files under the tree |
| S9 | [`preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/verification/counting-check.py`](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/verification/counting-check.py) | 84 | finite-arithmetic certificate — the shipped counting check, with its `README.md` and `counting-check-output.txt` |
| S10 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=361`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
