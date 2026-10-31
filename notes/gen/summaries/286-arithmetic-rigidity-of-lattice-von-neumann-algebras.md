[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 286](../index/operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md)

# 286 — Arithmetic rigidity of lattice von Neumann algebras

[Index page](../index/operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md)

## Original CONTENTS.md summary

[S1:7143] (family entry):

> **286. Rigidity and arithmetic of lattice von Neumann algebras.** Classifies finite-index bimodules between scalar-twisted group factors of ICC groups commensurable with property-$`(T)`$ lattices over characteristic-zero local fields and arbitrary ICC group factors. Every such bimodule is a summand of finite sums of models arising from finite-index subgroup isomorphisms and finite-dimensional projective representations. The classification also recovers the group, scalar cocycle and amplification scale up to the stated stable equivalence.

[S2:666] carries the `\resultentry` with both manuscripts, so the release blurb and the overview agree.
The two companion manuscripts [S3:47, S3:49, S4:84, S4:86]:

> We prove arithmetic exhaustion for bifinite correspondences between
arbitrarily scalar-twisted group factors of ICC groups commensurable with
property-$`(T)`$ lattices over characteristic-zero local fields and twisted
group factors of arbitrary countable ICC groups. Every such correspondence
is a closed summand of a finite direct sum of models obtained from actual
finite-index subgroup isomorphisms and finite-dimensional projective
representations of the matched cocycle ratio. The proof includes reducible
products, mixed real and finite places, and quaternionic and Cayley
rank-one factors. [S3:52–62]

> We prove stable canonical recovery for scalar-twisted group factors of ICC
groups commensurable with property-$`(T)`$ lattices over characteristic-zero
local fields. Every specified stable isomorphism to a scalar-twisted
factor of any countably infinite ICC group recovers the group, the cocycle
up to a normalized cochain, and equal amplification scales, with an
implementing partial isometry in the given matrix corners. We compute the
arithmetic correspondence subcategory for arbitrary countable ICC groups,
including all bounded maps, summands, conjugates, and Connes fusion, and
combine it with the companion's arithmetic exhaustion theorem.
Multiplication also recovers arbitrary finite-index factor neighbors,
with the exact projective condition on the matched cocycle ratio. [S4:89–101]

## Undergraduate summary

A **von Neumann algebra** is a mathematical object that encodes the
symmetries of a quantum system. A **group factor** is built from a discrete
group: it records the group's multiplication in the form of operators on a
Hilbert space. Two group factors can be isomorphic as algebras even when
their underlying groups are not — the algebra "forgets" which group built it.

The question is: how much of the original group can you recover from the
algebra alone? For groups with **property (T)** — a rigidity condition
meaning every representation with almost-invariant vectors has a genuine
invariant vector — these two papers show that the answer is: almost
everything. The group, the cocycle (a 2-cocycle encoding a possible twist of
the multiplication), and the amplification scale all recover from the factor
isomorphism [S3:52–62, S4:89–101, S2:666].

The first paper proves **arithmetic exhaustion**: every finite correspondence
between such group factors decomposes into a finite sum of "models" built
from actual subgroup isomorphisms and projective representations. The second
paper proves **stable canonical recovery**: every stable isomorphism recovers
the group, cocycle, and scale, and combines with the first to give a full
classification.

## Graduate summary

**The lattice class** [S5:14–30, S6:29–45].
Both manuscripts work with the class $`\mathscr{K}`$ of countably infinite ICC
groups abstractly commensurable with a lattice in a finite nonempty product
$`G = \prod_{i=1}^{r} G_i`$ where each $`G_i = \mathbf{H}_i(k_i)^+`$ with
$`k_i`$ equal to $`\mathbb{R}`$, $`\mathbb{C}`$, or a finite extension of
$`\mathbb{Q}_p`$; $`\mathbf{H}_i`$ connected, adjoint, absolutely simple over
$`k_i`$; each $`G_i`$ noncompact with Kazhdan's property $`(T)`$. No
irreducibility, cocompactness, product decomposition, or torsion hypothesis
is imposed on the lattice.

**Arithmetic exhaustion** (Manuscript 1) [S3:52–62, S5:1–30].
Every bifinite correspondence between scalar-twisted group factors of ICC
groups in $`\mathscr{K}`$ and twisted group factors of arbitrary countable ICC
groups is a closed summand of a finite direct sum of models obtained from
actual finite-index subgroup isomorphisms and finite-dimensional projective
representations of the matched cocycle ratio. The proof includes reducible
products, mixed real and finite places, and quaternionic and Cayley
rank-one factors. The geometry must be constructed inside the
correspondence; no boundary or ambient Lie group is initially available on
the comparison side [S5:1–335].

**Stable canonical recovery** (Manuscript 2) [S4:89–101, S6:1–45].
Every specified stable isomorphism from a scalar-twisted group factor of an
ICC group in $`\mathscr{K}`$ to a scalar-twisted factor of any countably
infinite ICC group recovers the group, the cocycle up to a normalized
cochain, and equal amplification scales, with an implementing partial
isometry in the given matrix corners. The algebraic calculation identifies
every bounded map, summand, and composition of the arithmetic models for
arbitrary countable ICC groups. Multiplication recovers arbitrary
finite-index factor neighbors with the exact projective condition on the
matched cocycle ratio [S6:1–413].

**The Connes–Popa problems.** Connes proved countability of the fundamental
group of a property-$`(T)`$ group factor (1980); his later problems ask
whether nonisomorphic ICC property-$`(T)`$ groups have nonisomorphic factors,
and ask for the fundamental groups. Popa's stronger stable formulation asks
for recovery of the given isomorphism up to a character and inner conjugacy,
with amplification scale one. These papers answer the stable formulation for
the lattice class [S6:9–14].

## History of the conjecture

The rigidity of property-$`(T)`$ group factors goes back to Connes (1980) for
countability of the fundamental group, and Connes's 1994 appendix problems
ask for the stronger isomorphism-class and fundamental-group computations.
Popa (2007) formulated the stable recovery problem in its sharp form. The
machinery of finite correspondences and bimodules over von Neumann algebras
comes from Jones (1980) and Ocneanu (1991). The specific arithmetic
exhaustion — that the analytic relation of finite correspondence is
*exhausted* by algebraic models (subgroup isomorphisms and projective
representations) — is the new contribution. The two papers are written as
companions: the first proves the geometric exhaustion, the second performs
the algebraic calculation and combines the two. The lattice class covers
products of higher-rank real groups, nonarchimedean groups over local fields
of characteristic zero, and the quaternionic and Cayley rank-one property-$`(T)`$
groups [S5:1–30, S6:1–45].

**Prior (my training data, not this repo).** Connes's rigidity results for
property-$`(T)`$ factors, Popa's deformation/rigidity program, and the
bimodule machinery are standard in von Neumann algebra theory. The
arithmetic exhaustion for the specific lattice class with mixed real and
finite places, plus the stable recovery with exact cocycle and scale
recovery, are the novel contributions; I cannot confirm the technical
estimates independently from training alone.

## Consequences

- **Arithmetic exhaustion for the lattice class** [S3:52–62]: every bifinite
  correspondence between scalar-twisted group factors of ICC groups in
  $`\mathscr{K}`$ and arbitrary ICC group factors is a closed summand of
  finite sums of algebraic models, with the proof covering reducible
  products, mixed places, and rank-one factors.
- **Stable canonical recovery** [S4:89–101]: every stable isomorphism
  recovers the group, cocycle (up to a normalized cochain), and amplification
  scale, with an implementing partial isometry — answering Connes's and
  Popa's problems for the lattice class.
- **The correspondence subcategory is computed** [S4:89–101]: for
  arbitrary countable ICC groups, all bounded maps, summands, conjugates,
  and Connes fusion of the arithmetic models are identified, and
  multiplication recovers finite-index factor neighbors with the exact
  projective condition.

## Section skeleton

Two companion manuscripts. Manuscript 1 [S3:52–62]: root `build/main.tex` (87
lines), 12 sections under `build/sections/` (00-introduction [S5],
00-models, 01-setup, 02-links, 03-transfer, 04-finite-panels, 05-ray-estimates,
06-isolated-scales, 07-real-panels, 08-heights, 09-locality, 10-gluing,
11-arithmetic-recovery), 2 figures. Manuscript 2 [S4:89–101]: root
`build/paper.tex` (112 lines), 5 sections under `build/sections/`
(01-introduction [S6], 02-models, 03-calculus, 04-endpoints, 05-examples),
1 figure. No verification bundle.

## Comparison with the formalized statement

The release does **not** formalize this family. There is no scope note under
`lean/docs/`, no comparator challenge stub under `lean/ComparatorChallenges/`,
and no `main_results` entry in `lean/formalization.yaml` naming it. The
ledger records `scope_note=0`, `chal=0`, and `mainres=0` [S7]. The
formalization gap is total: both the exhaustion and the recovery theorems
exist only as the manuscripts' LaTeX.

## Coverage

The ledger row `fam=286` [S7] records the tier and the counts:
`tier=T0`, `paps=2`, `paps_form=0`, `chal=0`, `mainres=0`,
`scope_note=0`, `verification=0`, `trace=`. The whole row is the coverage
signature: no scope note, no comparator, no `main_results` entry, and no
verification bundle, so the family sits entirely outside the release's
checking workflow. The shape flags are `classification|uniform`,
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7143] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 286 at [S2:666] |
| S3 | [`preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/build/main.tex`](../../../preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/build/main.tex) | 87 | manuscript 1 (arithmetic exhaustion); title [S3:47], date [S3:49], abstract [S3:52–62] |
| S4 | [`preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/build/paper.tex`](../../../preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/build/paper.tex) | 112 | manuscript 2 (stable recovery); title [S4:84], date [S4:86], abstract [S4:89–101] |
| S5 | [`preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/build/sections/00-introduction.tex`](../../../preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/build/sections/00-introduction.tex) | 335 | manuscript 1 introduction; lattice class [S5:14–30] |
| S6 | [`preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/build/sections/01-introduction.tex) | 413 | manuscript 2 introduction; lattice class [S6:29–45] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=286`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
