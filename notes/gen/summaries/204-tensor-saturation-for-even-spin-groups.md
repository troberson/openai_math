[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 204](../index/algebra/204-tensor-saturation-for-even-spin-groups.md)

# 204 — Tensor saturation for even spin groups

[Index page](../index/algebra/204-tensor-saturation-for-even-spin-groups.md)

## Original CONTENTS.md summary

The release's blurb [S1:4666] and the catalog abstract [S2:491]
state the family's claim: saturation factor one for
$`\mathrm{Spin}(2n)`$, $`n \geq 2`$ — for
three dominant integral weights whose sum lies in the
root lattice, an invariant at any common positive
integral dilation already gives an invariant at the
original weights. This resolves the type-$`D`$ part of
the simply-laced saturation conjecture. The manuscript
is *Tensor saturation for even spin groups* [S3:43,
S3:45]; its abstract 

> \maketitle
\beginabstract
We prove the saturation conjecture for $`\mathrm{Spin}(2n)`$, $`n\ge2`$.
If three dominant integral weights sum to an element of the root lattice, [S3:47–50]

## Undergraduate summary

A **symmetric group** (think: permutations of objects)
has a well-understood "building block" structure for
its representations — the **tensor product
decomposition** says when the tensor product of three
representations contains a trivial representation. The
**saturation conjecture** asks: if the tensor product
of three "scaled-up" representations contains a
trivial representation, does the original (unscaled)
triple also contain one? For **simply-laced** Lie
groups (the $`\mathrm{SL}(n)`$, $`E_6`$, $`E_7`$, $`E_8`$
families), the answer was conjectured to be **yes**
with factor one (no scaling needed). The **even spin
groups** $`\mathrm{Spin}(2n)`$ are the type-$`D`$
simply-laced groups — the "rotations in even
dimensions" with a double cover. This manuscript says
**yes** for type $`D`$: if $`n \geq 2`$ and three
dominant weights sum to a root-lattice element, then
an invariant at any positive dilation gives one at the
original weights [S3:47–50, S2:491].

## Graduate summary

**The main theorem** [S3:47–50, S2:491]. Let
$`G = \mathrm{Spin}(2n)`$ with $`n \geq 2`$. Let
$`\lambda_1, \lambda_2, \lambda_3`$ be dominant
integral weights of $`G`$ such that
$`\lambda_1 + \lambda_2 + \lambda_3`$ lies in the root
lattice. Then for every positive integer $`t`$, if
$`\mathrm{Hom}_G(\mathbf{1},
V(\lambda_1)^{\otimes t} \otimes
V(\lambda_2)^{\otimes t} \otimes
V(\lambda_3)^{\otimes t}) \neq 0`$, then
$`\mathrm{Hom}_G(\mathbf{1},
V(\lambda_1) \otimes V(\lambda_2) \otimes
V(\lambda_3)) \neq 0`$. This is the saturation factor
one property for type $`D`$.

**The scope of the formalization.** The family is at
tier T0: the ledger row records `mainres 0`,
`paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note, no comparator
challenge, no `main_results` entry in
`formalization.yaml`, and no verification bundle. The
result is entirely unformalized.

## History of the conjecture

The **saturation conjecture** for simply-laced Lie
groups was formulated in the 2000s and asks whether the
tensor product of three irreducible representations
contains a trivial representation whenever a positive
integral dilation does. The **factor one** form
($`t = 1`$ suffices if any $`t`$ works) is the strongest
version. Known results: factor one is proved for
$`\mathrm{SL}(2)`$ (classical), $`\mathrm{SL}(3)`$
(saturation, using geometry of moment maps), and for
$`E_8`$ (a special case). The type-$`D`$ case
($`\mathrm{Spin}(2n)`$) was the remaining
simply-laced family. The proof in this manuscript uses
**real schedules** and **lattice continuation** to
reduce the representation-theoretic question to a
combinatorial-geometric one, with **moment knots** and
**zero-tail completion** providing the key geometric
machinery [S3:47–50, S2:491].

**Prior (my training data, not this repo).** I know
the saturation conjecture as a named open problem in
the representation theory of simply-laced Lie groups,
the known cases for $`\mathrm{SL}(2)`$,
$`\mathrm{SL}(3)`$, and $`E_8`$, and the general
factor-one formulation. The **type-$`D`$ proof**
— for $`\mathrm{Spin}(2n)`$, $`n \geq 2`$,
via real schedules, lattice continuation, and moment
knots — is a result I cannot independently
verify from training alone.

## Consequences

**The type-$`D`$ part of the simply-laced saturation
conjecture is resolved.** Factor one holds for
$`\mathrm{Spin}(2n)`$, $`n \geq 2`$
[S3:47–50, S2:491].

**The result is uniform in $`n`$.** No restriction on
the rank $`n \geq 2`$ is imposed [S3:47–50].

## Section skeleton

One manuscript [S3:47–50] (title [S3:43], date [S3:45])
— `main.tex` under `build/`, with six sections
under `build/sections/` (`01-introduction`,
`02-real-schedules`, `03-lattice-continuation`,
`04-moment-knots`, `05-columns`,
`06-zero-tail-completion`) and a `references.bib`. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`, `chal 0`,
and `verification 0`. There is no scope note under
`lean/docs/`, no comparator challenge under
`lean/ComparatorChallenges/`, no `main_results` entry in
`formalization.yaml`, and no verification bundle under
the manuscript directory. The result is **entirely
unformalized**: the release shipped no Lean code, no
challenge stub, and no checking workflow for this
family. The proof rests solely on the manuscript
[S3:47–50].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 204 at [S1:4666] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{204} at [S2:491] |
| S3 | [`preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/main.tex`](../../../preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/main.tex) | 62 | the single manuscript root; title [S3:43], date [S3:45], abstract [S3:47–50] |
