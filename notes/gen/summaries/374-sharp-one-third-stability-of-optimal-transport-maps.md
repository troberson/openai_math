[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 374](../index/partial-differential-equations/374-sharp-one-third-stability-of-optimal-transport-maps.md)

# 374 — Sharp one-third stability of optimal transport maps

[Index page](../index/partial-differential-equations/374-sharp-one-third-stability-of-optimal-transport-maps.md)

## Original CONTENTS.md summary

[S1:9018] (family entry):

> **374. Sharp one-third stability of Brenier maps.** For uniform source measure <i>ρ</i> on a compact convex body with interior in dimension at least two, quadratic optimal transport maps satisfy $`\|T_\mu-T_\nu\|_{L^2(\rho)}\le C W_2(\mu,\nu)^{1/3}`$ uniformly over targets in a fixed compact set. The exponent is sharp, even for three-atom targets, disproving Letrouit's conjectured square-root bound. ([Lean](lean/docs/374.md))

[S2:852] carries the `\resultentry` with a single manuscript [S3].
The scope note states the formalized result:

> The formalization proves one-third Hölder stability of Brenier maps from the uniform measure on a compact convex body with nonempty interior in $`\mathbb R^d`$, for every $`d\ge2`$. For targets supported in one fixed nonempty compact set, the $`L^2`$ distance between the unique quadratic optimal maps is at most a constant times the one-third power of the targets' $`2`$-Wasserstein distance. The constant is uniform over those targets. [S4:9]

## Undergraduate summary

**Optimal transport** is the mathematics of moving one shape of matter
into another with as little effort as possible. For the quadratic cost
(move each point along a straight line, cost = distance-squared),
there is a unique cheapest map called the **Brenier map** — think of it
as the function that tells every grain of sand exactly where to land
so the total travel cost is minimal.

A **stability** question asks: if you nudge the target distribution
slightly, how much does the Brenier map move? A **square-root** bound
would say the map moves at most like the square root of the nudge.
This result shows that the best possible exponent is **one-third**, not
square-root: the map moves like the one-third power of the nudge, and
this exponent is **sharp** — meaning you cannot do better.

The proof of sharpness uses a family of **three-atom** target
distributions (mass concentrated at just three points) on a fixed
cube: for these, the map genuinely moves like
$`W_2^{1/3}`$ and no better power works. This **disproves
Letrouit's conjecture** that a uniform square-root bound should
hold [S3:39–47, S4:9–11, S1:9018].

## Graduate summary

**Main theorem (one-third stability)** [S3:39–47, S1:9018, S4:9].
For the uniform probability measure $`\`\rho``$ on a compact convex
body with nonempty interior in $`\`\mathbb R^d``$, $``d\ge 2`$`, the
quadratic optimal transport map satisfies
$`\`|T_\mu - T_\nu|_{L^2(\rho)} \le C \, W_2(\mu,\nu)^{1/3}``$
uniformly over targets supported in a fixed nonempty compact set,
with the constant $`C`$ independent of the target [S3:39–47, S4:9].

**Sharpness (three-atom counterexample)** [S3:39–47, S4:11,
S1:9018].
On a fixed cube, pairs of three-atom target measures violate every
analogous bound with exponent greater than $`1/3`$. In
particular, the conjectured uniform square-root estimate fails
[S4:11].

**The formalization is T2, not T3** [S4, S5, S6].
The scope note [S4:9] and one comparator stub [S5] are present, but
there is **no** `main_results` entry and **no** proved OAI tree
[S6]. The comparator stub `Brenier.lean` (108 lines) carries the
measure/Wasserstein/Brenier-map machinery (`uniformMeasure`,
`wasserstein2`, `IsQuadraticOptimalMap`, `mapL2Dist`, `cube`,
`HasExactlyThreeAtoms`) and states **two** challenge theorems:
`theorem one_third_stability` [S5:73] with `sorry` [S5:86], and
`theorem one_third_exponent_is_sharp` [S5:88] with `sorry`
[S5:102] (2 in this stub). The T2 shape is "scope note plus
comparator stub, no `main_results` entry, no OAI tree."

**The formalization is symmetric with the manuscript** [S4:9–11, S5].
The scope note names the single manuscript [S4:5] and formalizes
**both** the stability bound and the sharp three-atom counterexample
[S4:9–11], matching the manuscript's two-part theorem [S3:39–47].
The comparator stubs encode both: the stability bound as
`theorem one_third_stability` and the sharpness as
`theorem one_third_exponent_is_sharp` [S5:73, S5:88].

## History of the conjecture

The **Brenier map** (Brenier 1991) is the gradient of a convex
potential giving the unique quadratic optimal transport map between
two probability measures. **Stability of Brenier maps** — how
sensitive the map is to perturbations of the target — is a central
question in optimal transport. The **Letrouit conjecture** proposed a
uniform square-root ($`W_2^{1/2}`$) bound for the $`L^2`$ stability
of Brenier maps, which would be the natural interpolation between
the trivial Lipschitz bound and the best-known results.

The **novel contribution** is the **sharp one-third exponent with a
counterexample to the square-root conjecture** [S3:39–47, S4:9–11]:
not only does the one-third bound hold uniformly [S4:9], but the
exponent is **optimal** — three-atom targets on a fixed cube force
$`W_2^{1/3}`$ and disprove the conjectured $`W_2^{1/2}`$ bound
[S4:11]. The proof uses a decomposition into **cells** [S3:53],
**moment** comparisons [S3:54], a **finite stability** estimate
[S3:55], and a **gradient** bound [S3:56]; the sharpness uses the
three-atom construction [S3:52] and a direct computation showing
any exponent above $`1/3`$ fails.

**Prior (my training data, not this repo).** As of my training
cutoff, stability bounds for Brenier maps were an active area in
optimal transport, with the exact exponent in terms of the
Wasserstein distance being a key open question. The square-root
conjecture of Letrouit was a natural hypothesis, and its
disproof by a three-atom counterexample, together with the sharp
one-third bound, was at the frontier of the regularity theory of
optimal maps. I cannot verify the transport estimates
independently from training alone.

## Consequences

- **One-third Hölder stability** [S3:39–47, S1:9018, S4:9]: the
  $`L^2`$ distance between Brenier maps is bounded by a constant
  times $`W_2(\mu,\nu)^{1/3}`$, uniformly over targets in a fixed
  compact set.
- **The exponent is sharp** [S3:39–47, S4:11, S1:9018]: three-atom
  targets on a fixed cube violate every bound with exponent greater
  than $`1/3`$.
- **Letrouit's square-root conjecture is disproved**
  [S4:11, S1:9018]: the conjectured uniform
  $`W_2^{1/2}`$ estimate fails.
- **The constant is uniform** [S4:9, S1:9018]: the stability
  constant does not depend on the target, only on the fixed compact
  set and the dimension.
- **The result is T2, a challenge not a proof** [S5, S6]: two
  comparator stubs carry 2 `sorry` occurrences [S5:86, S5:102]
  and there is no `main_results` entry or OAI tree.

## Section skeleton

One manuscript, `build/source/main.tex` root (61 lines). The root
declares the theorem environments and macros inline [S3:2–32], the
title at [S3:35], the date at [S3:37], the abstract at [S3:39–47],
and 6 `input` files [S3:51–56]: `introduction`, `sharpness`,
`cells`, `moments`, `finite_stability`, `gradient`, plus a BibTeX
`references`. **No verification bundles.**

## Coverage

The ledger row `fam=374` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=657`, `verification=0`, `trace=0`,
`companions=`. The T2 shape is "scope note plus comparator stub,
no `main_results` entry, no OAI tree." The single comparator stub
carries 2 `sorry` [S5:86, S5:102]. The shape flags are
`shapes=bound|uniform`, `resolves_named=1`, `counterex_broad=1`,
`covmd=0` — a **bound**-type result (the one-third stability bound)
with a **uniform** character (the constant is uniform over targets),
`resolves_named=1` for the named "Letrouit's conjecture" resolved by
the three-atom counterexample, and `counterex_broad=1` for the
three-atom sharpness construction. The family has no verification
bundle and no trace. Note `paps_form=0`: the manuscript does not
appear in `formalization.yaml`'s `sources:` list, and there is no
`main_results` entry — the T2 formalization is the scope note's
description and the comparator's two challenge statements only,
with no proved Lean surface.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:9018] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 374 at [S2:852] |
| S3 | [`preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/main.tex`](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/main.tex) | 60 | the `\documentclass` root — 61 lines, title [S3:35], date [S3:37], abstract [S3:39–47], 6 `input` files [S3:51–56] |
| S4 | [`lean/docs/374.md`](../../../lean/docs/374.md) | 17 | scope note — names the single manuscript [S4:5]; Scope at [S4:9–11], comparator link at [S4:15] |
| S5 | [`lean/ComparatorChallenges/Brenier.lean`](../../../lean/ComparatorChallenges/Brenier.lean) | 108 | comparator stub — 108 lines, `theorem one_third_stability` [S5:73], `sorry` [S5:86], `theorem one_third_exponent_is_sharp` [S5:88], `sorry` [S5:102] |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=374`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
