[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 372](../index/partial-differential-equations/372-global-uniqueness-in-smooth-isotropic-elasticity.md)

# 372 — Global uniqueness in smooth isotropic elasticity

[Index page](../index/partial-differential-equations/372-global-uniqueness-in-smooth-isotropic-elasticity.md)

## Original CONTENTS.md summary

[S1:8986] (family entry):

> **372. Global uniqueness in smooth isotropic elasticity.** Proves that full static boundary displacement-to-traction data determine both smooth real Lamé moduli on every bounded connected smooth domain in ℝ3, provided *μ* > 0 and $`3\lambda+2\mu\gt 0`$ on the closure. Neither analyticity, proximity to constant coefficients nor prior knowledge near the boundary is required. ([Lean](../../../lean/docs/372.md))

[S2:848] carries the `\resultentry` with a single manuscript [S3].
The scope note states the formalized result:

> The formalization proves global uniqueness in the three-dimensional static isotropic elasticity inverse problem. On a bounded connected smooth domain, let two pairs of smooth real Lamé moduli satisfy $`\mu>0`$ and $`3\lambda+2\mu>0`$ on the closure. If their full displacement-to-traction maps agree, then both Lamé moduli agree throughout the domain. The selected statement is uniqueness; it does not supply a reconstruction algorithm. [S4:9]

## Undergraduate summary

**Elasticity** is the physics of how materials deform under force. An
**isotropic elastic material** is one whose mechanical response is the
same in every direction — like rubber or glass. Two numbers, the
**Lamé moduli** $`\`lambda`$` and $`\`mu`$`, capture the material's
stiffness: $`\`mu`$` controls resistance to shear, $`\`lambda`$` to
compression.

The **inverse problem** in elasticity asks: can you determine the
material parameters ($`\`lambda`$`, $`\`mu`$`) inside a 3D body by
measuring only what happens at the surface? You apply a displacement
to the boundary and measure the resulting traction (force per unit
area). The map from displacement to traction is the
**displacement-to-traction map**.

This result says: **yes**, the displacement-to-traction map
determines both Lamé moduli throughout the body, for any smooth
bounded 3D domain, as long as the material is physically admissible
($`\`mu > 0`$` and $`\`3\lambda + 2\mu > 0`$`, which rules out exotic
negative-stiffness materials). No analyticity is needed, no
prior knowledge near the boundary, and no assumption that the
material is close to a constant one [S3:45–47, S4:9].

## Graduate summary

**Main theorem (global uniqueness)** [S3:45–47, S1:8986, S4:9].
On every bounded connected smooth domain $`\`\Omega \subset
\mathbb R^3`$\`, let $`(\lambda_1, \mu_1)`$ and $`(\lambda_2, \mu_2)`$
be two pairs of smooth real Lamé moduli with
$`\`mu_i > 0`$` and $`\`3\lambda_i + 2\mu_i > 0`$` on
$`\`\overline{\Omega}`$` for $``i = 1, 2`$`. If the full static
displacement-to-traction maps agree, then
$`\`\lambda_1 = \lambda_2`$` and $`\`\mu_1 = \mu_2`$` throughout
$`\`\Omega`$` [S3:45–47, S4:9].

**The stated exclusion** [S4:9].
The selected statement is uniqueness; it does not supply a
reconstruction algorithm. The result is an identification
statement, not a constructive recovery procedure.

**The formalization is T2, not T3** [S4, S5, S6].
The scope note [S4:9] and one comparator stub [S5] are present, but
there is **no** `main_results` entry and **no** proved OAI tree
[S6]. The comparator stub `ElasticityUniqueness.lean` (110 lines)
carries the domain/Lamé-moduli/boundary-data machinery (definitions
of `SmoothBoundary`, `Admissible`, `WeakSolution`, `DN`) and states
`def MainClaim : Prop` [S5:96], with
`theorem global_uniqueness : MainClaim` [S5:103] and the `sorry`
at [S5:104] (1 in this stub). The T2 shape is "scope note plus
comparator stub, no `main_results` entry, no OAI tree."

**The formalization is symmetric with the manuscript** [S4:9, S5].
The scope note names the single manuscript [S4:5] and states the
global uniqueness as the formalized result [S4:9], which is the
manuscript's own abstract theorem [S3:45–47]. The comparator stub
encodes the same statement: two admissible Lamé-moduli pairs with
equal displacement-to-traction maps are equal throughout the domain
[S5:96–103].

## History of the conjecture

The **elasticity inverse problem** is the analog of Calderón's
(1982) conductivity inverse problem for the equations of linear
elasticity. The classical result of **Sakaguchi** (1985) established
uniqueness for the 3D anisotropic elastic inverse problem under
analyticity assumptions. Subsequent work by **Bae–Kim**,
**Rasmussen–Uhlmann**, and **Valko** extended uniqueness to
isotropic settings with varying regularity and boundary data
assumptions.

The **novel contribution** is the **smooth, non-analytic, full-domain
uniqueness** [S3:45–47, S4:9]: both Lamé moduli are determined by
the full displacement-to-traction map on every bounded connected
smooth 3D domain, under only the physical positivity conditions
$`\`mu > 0`$` and $`\`3\lambda + 2\mu > 0`$`, with **no** analyticity,
**no** proximity-to-constant, and **no** boundary-prior-knowledge
hypothesis. The proof uses a boundary-reduction to flat geometry
[S3:51–52], analytic estimates in the boundary layer [S3:53],
physical amplitude analysis [S3:54], transport matching [S3:55],
and coefficient recovery [S3:56].

**Prior (my training data, not this repo).** As of my training
cutoff, uniqueness for the 3D isotropic elasticity inverse problem
was known under analyticity or smallness assumptions, and removing
the analyticity requirement while keeping the full-domain
identification was an active direction in the inverse problems
community. I cannot verify the complex-analysis-based reconstruction
arguments independently from training alone.

## Consequences

- **Global uniqueness of both Lamé moduli** [S3:45–47, S1:8986,
  S4:9]: the full displacement-to-traction map determines both
  smooth real Lamé moduli on every bounded connected smooth 3D
  domain under the positivity conditions.
- **No analyticity required** [S1:8986, S4:9]: the moduli need only
  be smooth, not analytic.
- **No prior knowledge near the boundary** [S1:8986]: the
  identification holds without knowing the coefficients in any
  boundary neighborhood.
- **Uniqueness only, no reconstruction** [S4:9]: the formalized
  statement is an identification theorem; it does not provide a
  recovery algorithm.
- **The result is T2, a challenge not a proof** [S5, S6]: the
  comparator stub carries `theorem global_uniqueness` with a
  `sorry` [S5:104] and there is no `main_results` entry or OAI
  tree.

## Section skeleton

One manuscript, `build/main.tex` root (63 lines). The root declares
the theorem environments and macros inline [S3:2–30], the title at
[S3:38], the date at [S3:40], the abstract at [S3:45–47], and 6
`input` files [S3:51–56]: `introduction`, `boundary-reduction`,
`analytic-estimates`, `physical-amplitudes`, `transport-matching`,
`coefficient-recovery`, plus a BibTeX `references`. **No
verification bundles.**

## Coverage

The ledger row `fam=372` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=432`, `verification=0`, `trace=0`,
`companions=`. The T2 shape is "scope note plus comparator stub,
no `main_results` entry, no OAI tree." The single comparator stub
carries 1 `sorry` [S5:104]. The shape flags are
`shapes=bound`, `resolves_named=0`, `counterex_broad=0`,
`covmd=0` — a **bound**-type result (the displacement-to-traction
map as the measurement bound) with no named conjecture in the title
and no counterexample tag. The family has no verification bundle
and no trace. Note `paps_form=0`: the manuscript does not appear in
`formalization.yaml`'s `sources:` list, and there is no
`main_results` entry — the T2 formalization is the scope note's
description and the comparator's challenge only, with no proved
Lean surface.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8986] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 372 at [S2:848] |
| S3 | [`preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/build/main.tex`](../../../preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/build/main.tex) | 63 | the `\documentclass` root — 63 lines, title [S3:38], date [S3:40], abstract [S3:45–47], 6 `input` files [S3:51–56] |
| S4 | [`lean/docs/372.md`](../../../lean/docs/372.md) | 15 | scope note — names the single manuscript [S4:5]; Scope at [S4:9], comparator link at [S4:15] |
| S5 | [`lean/ComparatorChallenges/ElasticityUniqueness.lean`](../../../lean/ComparatorChallenges/ElasticityUniqueness.lean) | 110 | comparator stub — 110 lines, `def MainClaim` [S5:96], `theorem global_uniqueness` [S5:103], `sorry` [S5:104] |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=372`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
