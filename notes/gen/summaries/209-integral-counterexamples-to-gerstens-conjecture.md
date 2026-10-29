[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 209](../index/algebra/209-integral-counterexamples-to-gerstens-conjecture.md)

# 209 — Integral counterexamples to Gersten’s conjecture

[Index page](../index/algebra/209-integral-counterexamples-to-gerstens-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4773] and the catalog abstract [S2:501]
state the family's claim: unrestricted integral Gersten
injectivity, disproved in degrees $`3`$ and $`5`$. Two
explicit two-dimensional ramified regular local rings of
mixed characteristic $`(0,5)`$ have nonzero integral
$`K`$-theory classes that vanish over their fraction
fields. The family ships two manuscripts [S1:4773]:

- *An integral counterexample to Gersten's
  conjecture* [S3:37, S3:39]
- *An integral degree-three Gersten
  counterexample* [S4:25, S4:27]

The degree-five abstract 

> We construct a two-dimensional ramified regular local ring $`A`$ of mixed
characteristic $`(0,5)`$ for which $`K_5(A)\to K_5(\mathrm{Frac} A)`$ has a nonzero
kernel. This disproves Gersten's conjecture in its unrestricted integral
form. [S3:45–48]

The degree-three abstract 

> We construct a two-dimensional ramified regular local ring $`A`$ in mixed
characteristic $`(0,5)`$ for which the integral map
$`K_3(A)\to K_3(\mathrm{Frac} A)`$ has nonzero kernel. This gives a negative
answer to the unrestricted integral Gersten conjecture. [S4:31–34]

## Undergraduate summary

A **local ring** is a collection of numbers (or
functions) focused at a single "point" — think of
the power series a(x) = a_0 + a_1 x + a_2 x^2 + ...
centered at zero. The **K-theory** of a ring is a
sequence of abelian groups K_0, K_1, K_2, ... that
measure different kinds of "topological complexity"
in the ring. The **Gersten conjecture** (proposed in
1970) predicts that for a "nice" ring (regular, of
small dimension), the map from the K-theory of the
ring to the K-theory of its fraction field
(inverting all nonzero elements) should be
**injective** — no information is lost. In
other words, a nonzero K-theory class over the ring
should stay nonzero when you invert all the
nonzero elements. This manuscript pair says
**no** — there exist explicit two-dimensional
rings of mixed characteristic (0, 5) where a
nonzero K_3 class over the ring becomes zero over
the fraction field, and similarly for K_5
[S3:45–48, S4:31–34, S2:501].

## Graduate summary

**The degree-five counterexample** [S3:45–48, S2:501].
There exists a two-dimensional ramified regular local
ring $`A`$ of mixed characteristic $`(0,5)`$ such that
$`K_5(A) 	o K_5(\mathrm{Frac} A)`$ has a
nonzero kernel. This disproves Gersten's conjecture
in its unrestricted integral form in degree five.

**The degree-three counterexample** [S4:31–34, S2:501].
There exists a two-dimensional ramified regular local
ring $`A`$ in mixed characteristic $`(0,5)`$ such that
the integral map $`K_3(A) 	o K_3(\mathrm{Frac}
A)`$ has nonzero kernel. This gives a negative answer
to the unrestricted integral Gersten conjecture in
degree three.

**The scope of the formalization.** The family is at
tier T0: the ledger row records `mainres 0`,
`paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note, no comparator
challenge, no `main_results` entry in
`formalization.yaml`, and no verification bundle. The
result is entirely unformalized.

## History of the conjecture

**Gersten's conjecture** (1970) predicts that for a
regular local ring $`A`$ of dimension $`d`$, the
**Gersten complex** — a chain complex built from
the K-theory of $`A`$ and its residue fields — is
exact. In degree zero this recovers the injectivity
of $`K_d(A) 	o K_d(\mathrm{Frac} A)`$. The
conjecture is known for $`d \leq 2`$ in all
characteristics (Quillen), and for $`d = 3`$ in
characteristic zero (Sweede--Weibel). The **integral**
form (as opposed to the mod-
$`p`$ or rational form) is strictly stronger: it
requires the kernel to vanish over $`\mathbb{Z}`$, not
just over $`\mathbb{Q}`$ or $`\mathbb{Z}/p`$. The
**mixed characteristic** setting
$`(0,p)`$ — where the ring has characteristic
zero but its residue field has characteristic $`p`$
— is the most delicate case, because the
reduction map introduces $`p`$-torsion that can
create kernel elements invisible in characteristic
zero. The two manuscripts construct explicit
two-dimensional ramified regular local rings of
mixed characteristic $`(0,5)`$ with nonzero kernel
elements in $`K_3`$ and $`K_5`$
[S3:45–48, S4:31–34, S2:501].

**Prior (my training data, not this repo).** I know
Gersten's conjecture as a named open problem in
algebraic K-theory, the positive cases for
$`d \leq 2`$ and for $`d = 3`$ in characteristic zero,
and the distinction between the integral and
mod-$`p`$ forms. The **explicit counterexamples in
mixed characteristic $`(0,5)`$** — in both
degrees three and five, for two-dimensional ramified
regular local rings — are results I cannot
independently verify from training alone.

## Consequences

**The unrestricted integral Gersten conjecture is
disproved in degree five.** A two-dimensional ramified
regular local ring of mixed characteristic $`(0,5)`$ has
a nonzero $`K_5`$ class that vanishes over its fraction
field [S3:45–48, S2:501].

**The unrestricted integral Gersten conjecture is
disproved in degree three.** A two-dimensional ramified
regular local ring of mixed characteristic $`(0,5)`$ has
a nonzero $`K_3`$ class that vanishes over its fraction
field [S4:31–34, S2:501].

**The counterexamples are two-dimensional.** Both
constructions work in dimension two, the minimal
dimension where the conjecture is not known
[S3:45–48, S4:31–34].

## Section skeleton

Two manuscripts: [S3:45–48] (title [S3:37], date [S3:39])
— `main.tex` under `build/source/` with sections
under `build/source/sections/` and a `references.bib`;
[S4:31–34] (title [S4:25], date [S4:27]) — `main.tex`
under `build/` with five sections under
`build/sections/` (`introduction`, `model`, `field`,
`integral-class`, `detection`) and a `refs/`
directory. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`, `chal 0`,
and `verification 0`. There is no scope note under
`lean/docs/`, no comparator challenge under
`lean/ComparatorChallenges/`, no `main_results` entry in
`formalization.yaml`, and no verification bundle under
the manuscript directories. The result is **entirely
unformalized**: the release shipped no Lean code, no
challenge stub, and no checking workflow for this
family. The proof rests solely on the two manuscripts
[S3:45–48, S4:31–34].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 209 at [S1:4773] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{209} at [S2:501] |
| S3 | [`preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/main.tex`](../../../preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/main.tex) | 63 | manuscript 1 of 2 (degree-five counterexample); title [S3:37], date [S3:39], abstract [S3:45–48] |
| S4 | [`preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/main.tex`](../../../preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/main.tex) | 43 | manuscript 2 of 2 (degree-three counterexample); title [S4:25], date [S4:27], abstract [S4:31–34] |
