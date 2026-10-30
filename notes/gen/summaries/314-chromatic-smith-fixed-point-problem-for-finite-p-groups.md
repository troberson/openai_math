[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 314](../index/topology/314-chromatic-smith-fixed-point-problem-for-finite-p-groups.md)

# 314 — The chromatic Smith fixed-point problem for finite $p$-groups

[Index page](../index/topology/314-chromatic-smith-fixed-point-problem-for-finite-p-groups.md)

## Original CONTENTS.md summary

[S1:7717] (family entry):

> **314. Cyclic length and chromatic fixed-point loss.** Determines the optimal chromatic loss from geometric <i>H</i>-fixed points to geometric <i>G</i>-fixed points for every subgroup <i>H</i> of a finite <i>p</i>-group <i>G</i>. At every nonnegative height, the loss equals the shortest subnormal-chain length from <i>H</i> to <i>G</i> with cyclic quotients. Each quotient counts once regardless of order, and finite spectra witness sharpness.

[S2:724] carries the `\resultentry` with the single manuscript [S3:3, S3:5]. The abstract:

> For a finite $`p`$-group $`G`$ and a subgroup $`H`$, we prove that the optimal chromatic fixed-point loss equals the shortest length of a subnormal chain from $`H`$ to $`G`$ with cyclic quotients. The equality holds at every prime and every nonnegative height, resolving positively the equality proposed by Kuhn and Lloyd. [S3:8–10]

## Undergraduate summary

In equivariant stable homotopy, a **finite $`p`$-group** $`G`$ acts on a
spectrum, and the **fixed points** $`X^H`$ capture the part of the
spectrum "visible" to a subgroup $`H`$. The **chromatic fixed-point
problem** asks: how much chromatic (i.e., height-sensitive) information
is lost when you pass from $`X^H`$ to $`X^G`$?

The answer here is group-theoretic: the optimal loss at every chromatic
height equals the **shortest subnormal chain length** from $`H`$ to $`G`$
where each quotient in the chain is cyclic. A subnormal chain is a
sequence of subgroups $`H = G_0 \triangleleft G_1 \triangleleft \cdots
\triangleleft G_k = G`$ where each step is a normal inclusion; the
"cyclic quotients" condition means each $`G_{i+1}/G_i`$ is finite cyclic.

This resolves positively the equality proposed by Kuhn and Lloyd, who
conjectured that the chromatic loss should be governed by precisely
this group-theoretic invariant.

## Graduate summary

**The chromatic fixed-point loss formula** [S3:8–10, S2:724].
For a finite $`p`$-group $`G`$ and a subgroup $`H \leq G`$, the optimal
chromatic fixed-point loss — measured as the difference between the
chromatic height at which $`X^H`$ and $`X^G`$ agree — equals the shortest
length of a subnormal chain from $`H`$ to $`G`$ with cyclic quotients. The
equality holds at every prime and every nonnegative height.

**Order-independence of the quotient count** [S1:7717].
Each cyclic quotient in the subnormal chain counts once regardless of
the order in which the chain is taken: the loss depends only on the
group-theoretic invariant, not on the particular chain realization.

**Sharpness witnessed by finite spectra** [S1:7717].
The bound is sharp: for every such pair $`(H, G)`$ and every height,
there exists a finite spectrum $`X`$ for which the chromatic loss from
$`X^H`$ to $`X^G`$ attains the subnormal-chain-length bound exactly.

## History of the conjecture

The chromatic Smith fixed-point problem sits at the intersection of
equivariant stable homotopy theory and the chromatic filtration.
Smith's original theorem (1965) relates the fixed points of a finite
$`p`$-group action on a space to the group's $`p`$-primary structure. The
chromatic generalization asks how much of the chromatic height
information is "visible" at the level of fixed points, and how the
visibility degrades as one passes from smaller subgroups to the full
group.

Kuhn and Lloyd proposed that the optimal loss should be governed by a
group-theoretic invariant — specifically, the shortest subnormal chain
length with cyclic quotients — but left the equality open. This paper
closes that question: the formula holds at every prime and every
nonnegative height, and finite spectra achieve the bound.

**Prior (my training data, not this repo).** Smith's theorem in
equivariant $`K`$-theory and the chromatic generalization via the
Morava $`E`$-theories are well established. The positive resolution of
the Kuhn–Lloyd equality, with the cyclic-quotient subnormal chain
length as the exact invariant and the sharpness witnesses by finite
spectra, is the novel contribution claimed here; I cannot verify the
chromatic $`E`$-theory computations independently from training alone.

## Consequences

- **The Kuhn–Lloyd equality is resolved positively** [S3:8–10,
  S2:724]: the optimal chromatic fixed-point loss equals the shortest
  subnormal-chain length from $`H`$ to $`G`$ with cyclic quotients, at
  every prime and every nonnegative height.
- **The invariant is group-theoretic, not homotopical** [S3:9, S1:7717]:
  the loss depends only on the subgroup structure of $`G`$ and $`H`$, not
  on the particular spectrum being acted on.
- **Each quotient counts once regardless of order** [S1:7717]: the
  cyclic-quotient condition is order-independent, so the formula is
  well-defined without specifying a particular chain.
- **Finite spectra witness sharpness** [S1:7717]: the bound is not
  merely an upper bound; for every pair $`(H, G)`$ there is a finite
  spectrum attaining it.

## Section skeleton

One manuscript [S3:8–10]. Root `build/paper.tex` (22 lines), sections
under `build/sections/`: `01-introduction`, `02-background`,
`03-characters`, `04-congruences`, `05-profinite`, `06-gluing`,
`07-support`. No verification bundle.

## Comparison with the formalized statement

This family is **not formalized**. It sits at tier **T0** in the ledger
[S4]: no scope note, no comparator stub, no `main_results` entry, no
proved OAI tree. The T0 shape is "no formalization at all in the
release."

The absence is part of the coverage skew the ledger records: the
chromatic and equivariant families in the catalog are among the
thinnest formalized, and a fixed-point loss formula governed by
subnormal chain lengths is of just this kind. The reading of the
manuscript above is of source text only.

## Coverage

The ledger row `fam=314` [S4] records the tier and the counts:
`tier=T0`, `paps=1`, `paps_form=0`, `chal=0`, `mainres=0`,
`scope_note=0`, `scope_chars=0`, `verification=0`, `trace=`. The T0
shape is "no formalization at all." The shape flags are
`shapes=bound|uniform`, `resolves_named=0`, `counterex_broad=0`,
`covmd=0` — a bound/uniform family recording the exact chromatic
fixed-point loss formula, with no formalization record in the release.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7717] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 314 at [S2:724] |
| S3 | [`preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/build/paper.tex`](../../../preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/build/paper.tex) | 19 | manuscript; title [S3:3], date [S3:5], abstract [S3:8–10] |
| S4 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=314`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
