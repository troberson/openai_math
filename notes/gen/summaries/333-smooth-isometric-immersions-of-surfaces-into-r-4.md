[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 333](../index/differential-geometry/333-smooth-isometric-immersions-of-surfaces-into-r-4.md)

# 333 — Smooth isometric immersions of surfaces into $\mathbb R^4$

[Index page](../index/differential-geometry/333-smooth-isometric-immersions-of-surfaces-into-r-4.md)

## Original CONTENTS.md summary

[S1:8129] (family entry):

> **333. Smooth isometric immersions of surfaces into ℝ⁴.** Every closed smooth Riemannian surface admits a smooth isometric immersion into ℝ⁴, resolving the closed-surface form of the four-dimensional isometric-immersion problem. This includes nonorientable surfaces and metrics of arbitrary Gaussian curvature. ([Lean](../../../lean/docs/333.md))

[S2:766] carries the `\resultentry` with the single manuscript.
The abstract:

> Every closed smooth Riemannian surface admits a smooth isometric immersion into
Euclidean four-space, without an orientability assumption. This resolves the
closed-surface form of the classical four-dimensional isometric-immersion problem. [S3:36–40]

## Undergraduate summary

A **Riemannian surface** is a two-dimensional shape with a rule for
measuring distances and angles on it — a "metric" — that can vary
from point to point. An **isometric immersion** of such a surface into
a higher-dimensional space is a smooth map that preserves all those
measurements: every curve on the surface has the same length after the
map, and every angle between curves is unchanged.

The question is: how many extra dimensions do you need to embed a
surface without distorting it? A flat sheet fits in 3D. A general
surface with arbitrary curvature needs at least 4D. The classical
**four-dimensional isometric-immersion problem** asked: does every
smooth Riemannian surface fit isometrically into ℝ⁴? The answer for
*closed* surfaces (no boundary, like a sphere or a torus) was the open
case. The answer here is **yes**: every closed smooth Riemannian
surface admits a smooth isometric immersion into ℝ⁴, with no
orientability assumption (so nonorientable surfaces like the
Klein bottle are included) and no restriction on curvature.

## Graduate summary

**Main theorem (formalized in part)** [S3:36–40, S2:766, S4:9].
Every closed smooth Riemannian surface $`(M, g)`$ admits a smooth
isometric immersion $`F : M \to \mathbb R^4`$ whose differential
$`dF`$ preserves the Riemannian inner product $`g`$ on every tangent
space. No orientability assumption is imposed; the statement asks for
an **immersion** (an injective differential) rather than an
**embedding** (an injective map).

**The construction** [S3, S2:766].
The manuscript's nine sections carry the proof machinery:
`introduction`, `preliminaries`, `primitive-statement`, `small-modes`,
`exact-correction`, `velocity-loop`, `primitive-realization`,
`geometry-preservation`, `global-construction`. The construction
proceeds by building a **primitive** immersion (a map preserving the
metric up to a correction term), analyzing the **small modes** (the
oscillatory part of the correction), applying an **exact correction**
(killing the residual), closing the **velocity loop** (making the map
periodic on the closed surface), realizing the **primitive** (producing
the actual immersion), verifying **geometry preservation** (the metric
is exactly preserved), and assembling the **global construction**
(the final map).

## History of the conjecture

The **isometric immersions of surfaces** problem is one of the
classical questions in differential geometry, going back to
**Bonnet's theorem** (1850s) and the work of **Darboux**, **Blaschke**,
and **Weyl** in the early 20th century. The question: given a
Riemannian metric on a surface, can it be realized as the induced
metric of a smooth map into Euclidean space?

The **dimension** matters. Every 2D Riemannian metric can be
isometrically embedded in ℝ⁵ (this is classical, following from the
general $`n(n+1)/2`$ bound). The sharp question for surfaces is
whether 4D suffices. The answer is **yes for closed surfaces** (this
paper) and **no in general** (there are metrics in arbitrary
dimensions that require more than $`n(n+1)/2`$ dimensions, but for
surfaces the 4D bound is the right one).

The orientability question is significant: many classical results
assume the surface is orientable (e.g., the Gauss–Bonnet theorem
requires a choice of orientation). The present result removes that
assumption, so the theorem applies to the Klein bottle and the
nonorientable genus-1 surface as well.

**Prior (my training data, not this repo).** The 4D isometric
immersion problem for closed surfaces is a genuine open problem in
differential geometry as of my training cutoff. The specific
construction (primitive → small modes → exact correction → velocity
loop) and the explicit removal of the orientability hypothesis are the
novel contributions claimed here. I cannot verify the geometric
analysis independently from training alone.

## Consequences

- **The closed-surface 4D isometric-immersion problem is resolved**
  [S3:36–40, S2:766, S4:9]: every closed smooth Riemannian surface
  admits a smooth isometric immersion into ℝ⁴.
- **No orientability assumption is needed** [S4:9]: the theorem
  applies to nonorientable surfaces (Klein bottle, nonorientable
  genus-$`g`$ surfaces) as well as orientable ones.
- **Arbitrary Gaussian curvature is included** [S1:8129]: the
  metric's curvature is not restricted — positive, negative, or
  mixed-curvature surfaces all admit the immersion.
- **Immersion, not embedding** [S4:9]: the statement guarantees an
  injective differential (local embedding) but does not exclude global
  self-intersections of the image in ℝ⁴.

## Section skeleton

One manuscript [S3:36–40]. Root `build/main.tex` (52 lines;
`\documentclass` at [S3:2], title at [S3:32], date at [S3:34],
abstract at [S3:36–40]). Nine `input` section files under `build/`:
`introduction`, `preliminaries`, `primitive-statement`, `small-modes`,
`exact-correction`, `velocity-loop`, `primitive-realization`,
`geometry-preservation`, `global-construction`. A `refs.bib`
bibliography. **No verification bundle.**

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note
[S4:9], one comparator stub [S5], and **no** `main_results` entry and
**no** OAI tree. The T2 shape is "scope note and comparator stub
present, no proved OAI tree and no `main_results` entry."

The scope note [S4:9] selects the main statement: every closed smooth
Riemannian surface admits a smooth isometric immersion into
$`\mathbb R^4`$, the differential preserves the Riemannian inner
product on every tangent space, no orientability assumption, immersion
rather than embedding.

The single comparator stub carries 1 `sorry`.
`SurfaceImmersion.lean` (49 lines) states
`def IsSmoothIsometricImmersion` [S5:26] and
`theorem smooth_isometric_immersion` [S5:40] with the `sorry` at
[S5:42]. The stub defines a `SmoothMetric` structure and the
`IsSmoothIsometricImmersion` predicate (the differential preserves the
metric), and states the main theorem over a closed smooth surface. The
manuscript's nine-section construction (primitive → small modes →
exact correction → velocity loop → primitive realization → geometry
preservation → global construction) has no Lean counterpart: the
formalization states the conclusion in one 49-line stub with a `sorry`,
and the 9 sections have no file-level correspondence in the Lean tree.

## Coverage

The ledger row `fam=333` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=310`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stub present, no `main_results`
entry, no proved OAI tree." The single comparator stub carries 1
`sorry`. The shape flags are `shapes=resolution|uniform`,
`resolves_named=1`, `counterex_broad=0`, `covmd=0` — a
resolution family (the closed-surface 4D immersion problem is
resolved), with a named conjecture in the title, with no coverage
document in the manuscript directory. Note `paps_form=0`: the scope
note names the manuscript, but the manuscript does not appear in
`formalization.yaml`'s `sources:` list (there is no `main_results`
entry), so the per-manuscript formalized flag stays 0 even at tier T2.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8129] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 333 at [S2:766] |
| S3 | [`preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/build/main.tex`](../../../preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/build/main.tex) | 54 | the `\documentclass` root — title [S3:32], date [S3:34], abstract [S3:36–40] |
| S4 | [`lean/docs/333.md`](../../../lean/docs/333.md) | 15 | scope note — Scope at [S4:9] and the comparator link |
| S5 | [`lean/ComparatorChallenges/SurfaceImmersion.lean`](../../../lean/ComparatorChallenges/SurfaceImmersion.lean) | 49 | comparator stub — 49 lines, 1 `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=333`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
