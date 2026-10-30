[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 337](../index/differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md)

# 337 — Cartan–Hadamard isoperimetry and CAT$(0)$ fillings

[Index page](../index/differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md)

## Original CONTENTS.md summary

[S1:8224] (family entry):

> **337. Sharp Cartan–Hadamard isoperimetry and rigidity.** Proves generalized Cartan–Hadamard isoperimetry in every dimension: in a complete simply connected manifold with sectional curvature at most κ ≤ 0, every finite-volume finite-perimeter set satisfies the sharp comparison with the equal-volume model ball. Bounded positive-volume equality regions for κ = 0 are Euclidean balls. Also proves sharp Euclidean filling bounds for compactly supported integral $`n`$-cycles, $`n`$ ≥ 2, in arbitrary proper CAT(0) spaces.

[S2:774] carries the `\resultentry` with two manuscripts.
Manuscript 1 [S3] (isoperimetry and rigidity) and
Manuscript 2 [S4] (sharp integral fillings in CAT(0) spaces).

## Undergraduate summary

An **isoperimetric inequality** says that, among all shapes with a
given volume, the ball has the smallest surface area. On curved
spaces, the "ball" is replaced by the model ball of the constant
sectional curvature that bounds your space from above. The
**Cartan–Hadamard theorem** says: in a simply connected space with
sectional curvature ≤ 0 (a "non-positively curved" space), geodesics
don't focus, and the geometry is at most as curved as flat Euclidean
space.

The **Cartan–Hadamard isoperimetric conjecture** asked: does the ball
really minimize perimeter in such spaces, in every dimension? The
answer here is **yes**: in a complete simply connected manifold with
sectional curvature at most κ ≤ 0, every finite-volume set has
perimeter at least that of the equal-volume model ball. And in the
flat case (κ = 0), the **rigidity** part says: if a set achieves
equality, it *is* a round Euclidean ball (up to null sets).

The second manuscript extends this to **fillings** in **CAT(0)
spaces** (the metric-space generalization of non-positively curved
spaces): every compactly supported integral $`n`$-cycle, $`n`$ ≥ 2,
bounds a filling with the sharp Euclidean mass bound. The Euclidean
constant is optimal — no filling can do better.

## Graduate summary

**Main theorem 1 (isoperimetry, manuscript 1)** [S3:75–84, S2:774].
In a complete simply connected smooth Riemannian manifold with
sectional curvature at most $`\kappa \le 0`$, every finite-volume set
of finite ambient perimeter has perimeter at least that of the
equal-volume ball in curvature $`\kappa`$. For bounded positive-volume
sets with $`\kappa = 0`$, equality in the Euclidean comparison holds
precisely when the set agrees up to null sets with an open region
isometric, with its induced metric, to a round Euclidean ball.

**Main theorem 2 (sharp fillings, manuscript 2)** [S4:10–17, S2:774].
Every compactly supported integral $`n`$-cycle, $`n \ge 2`$, in a
proper CAT(0) space bounds a compactly supported integral current
with the sharp Euclidean mass bound: the filling's mass is at most
$`C_n`$ times the boundary mass to the power $`(n+1)/n`$, where
$`C_n`$ is the Euclidean isoperimetric coefficient. Integer
multiplicities and the ambient dimension are unrestricted. In
particular, the Euclidean Cartan–Hadamard isoperimetric conjecture
holds in dimensions at least three.

**The two formalized statements** [S5:9, S5:11, S6, S7].
The scope note selects two statements. The main one [S5:9] is the
sharp Euclidean filling inequality in proper CAT(0) spaces. The
second [S5:11] proves the Euclidean coefficient is **optimal**: in
Euclidean space, there is a cycle for which every compactly supported
integral filling has at least the Euclidean mass bound.

## History of the conjecture

The **Cartan–Hadamard isoperimetric conjecture** is a classical
problem in geometric analysis and metric geometry. The Cartan–Hadamard
theorem (1925) establishes that a simply connected complete
Riemannian manifold with sectional curvature ≤ 0 is diffeomorphic to
$`\`\mathbb R^n\``$ and that its universal covering map is a Riemannian
submersion. The isoperimetric question: does the model ball minimize
perimeter among equal-volume sets in such spaces?

This was known in dimension 2 (classical) and in special cases in
higher dimensions. The general $`n \ge 3\`$ case, with the sharp
equality characterization, was the open problem. The present result
resolves it in every dimension, with the rigidity statement (equality
implies a round ball) being the sharp form.

The **CAT(0) filling** result extends the isoperimetric inequality
from Riemannian manifolds to the broader class of CAT(0) spaces
(metric spaces where geodesic triangles are thinner than Euclidean
triangles). The sharp Euclidean mass bound for integral cycles in
CAT(0) spaces, with optimal constants and unrestricted multiplicities,
is the metric-space generalization.

**Prior (my training data, not this repo).** The Cartan–Hadamard
isoperimetric conjecture in general dimensions is a genuine open
problem in geometric analysis as of my training cutoff. The specific
construction (Sobolev comparison, profile analysis, equality
regularity) and the CAT(0) filling machinery (radial flows, Sobolev
inequalities, chord decomposition) are the novel contributions claimed
here. I cannot verify the geometric analysis independently from
training alone.

## Consequences

- **The Cartan–Hadamard isoperimetric conjecture is resolved in
  every dimension** [S3:75–84, S2:774]: in a complete simply
  connected manifold with sectional curvature ≤ κ, every
  finite-volume finite-perimeter set has perimeter at least that
  of the equal-volume model ball.
- **Euclidean equality rigidity** [S3:75–84, S2:774]: for κ = 0,
  a bounded positive-volume set achieving equality in the
  isoperimetric inequality is (up to null sets) a round Euclidean
  ball.
- **Sharp Euclidean filling bounds in CAT(0) spaces** [S4:10–17,
  S2:774]: every compactly supported integral $`n`$-cycle,
  $`n \ge 2`$, in a proper CAT(0) space has a filling with the
  sharp Euclidean mass bound.
- **The Euclidean isoperimetric coefficient is optimal** [S5:11,
  S6]: in Euclidean space, no filling can beat the Euclidean mass
  bound.
- **Unrestricted multiplicities and dimension** [S4:10–17, S5:9]:
  the filling bound holds for arbitrary integer multiplicities and
  in any ambient dimension.

## Section skeleton

Two manuscripts, both with `build/main.tex` roots.
Manuscript 1 [S3] (isoperimetry, 99 lines): 9 `input` section files
under `sections/`: `01-introduction`, `02-maps`, `03-sobolev`,
`04-profile`, `05-comparison`, `06-dimensions`,
`07-equality-regularity`, `08-rigidity`, `09-consequences`.
Manuscript 2 [S4] (fillings, 48 lines): 8 `input` section files under
`sections/`: `01-introduction`, `02-currents`, `03-radial`,
`04-sobolev`, `05-minimizer`, `06-chords`, `07-conclusion`,
`08-classical`. A `references.bib` bibliography in each.
**No verification bundles.**

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note
[S5:9], two comparator stubs [S6, S7], and **no** `main_results` entry
and **no** OAI tree. The T2 shape is "scope note and comparator stubs
present, no proved OAI tree and no `main_results` entry."

The scope note [S5:9, S5:11] selects two statements. The main one
[S5:9] is the sharp Euclidean filling inequality for compactly
supported integral $`n`$-cycles in proper CAT(0) spaces,
$`n \ge 2`$: a filling with mass at most $`C_n\`$ times the boundary
mass to the power $`(n+1)/n`$. The second [S5:11] proves the
Euclidean coefficient is optimal: in Euclidean space, a cycle
exists for which every filling has at least that mass.

The two comparator stubs each carry 1 `sorry`.
`FillingCoefficient.lean` (130 lines) states
`theorem coefficient_optimal` [S6:120] with the `sorry` at [S6:126].
`SharpCAT0Filling.lean` (146 lines) states
`theorem sharp_integral_filling` [S7:135] with the `sorry` at [S7:142].
Neither comparator config carries a `main_results` entry, and no
proved OAI tree exists under `lean/OAI/` for this family. The reading
is of source text only.

## Coverage

The ledger row `fam=337` [S8] records the tier and the counts:
`tier=T2`, `paps=2`, `paps_form=0`, `chal=2`, `mainres=0`,
`scope_note=1`, `scope_chars=686`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stubs present, no `main_results`
entry, no proved OAI tree." The two comparator stubs together carry 2
`sorry`. The shape flags are `shapes=bound|partial|uniform`,
`resolves_named=0`, `counterex_broad=0`, `covmd=0` — a
bound-resolution family (resolving the Cartan–Hadamard isoperimetric
conjecture), with a partial (two complementary manuscripts) and
uniform (dimension-free) quantifier, with no counterexample, no
coverage document, and no reasoning trace. Note `paps_form=0`: the
scope note names the manuscripts, but the manuscripts do not appear
in `formalization.yaml`'s `sources:` list (there is no
`main_results` entry), so the per-manuscript formalized flag stays 0
even at tier T2.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8224] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 337 at [S2:774] |
| S3 | [`preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/build/main.tex`](../../../preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/build/main.tex) | 98 | the `\documentclass` root (manuscript 1, isoperimetry) — title [S3:68–69], date [S3:71], abstract [S3:75–84] |
| S4 | [`preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/build/main.tex`](<../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/build/main.tex>) | 33 | the `\documentclass` root (manuscript 2, fillings) — title [S4:4], date [S4:6], abstract [S4:10–17] |
| S5 | [`lean/docs/337.md`](../../../lean/docs/337.md) | 18 | scope note — Scope at [S5:9] and [S5:11], comparator links at [S5:15–18] |
| S6 | [`lean/ComparatorChallenges/FillingCoefficient.lean`](../../../lean/ComparatorChallenges/FillingCoefficient.lean) | 130 | comparator stub 1 (optimal coefficient) — 130 lines, 1 `sorry` |
| S7 | [`lean/ComparatorChallenges/SharpCAT0Filling.lean`](../../../lean/ComparatorChallenges/SharpCAT0Filling.lean) | 146 | comparator stub 2 (sharp filling in CAT(0)) — 146 lines, 1 `sorry` |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=337`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
