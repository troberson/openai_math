[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 036](../index/algebraic-and-complex-geometry/036-numerical-semiampleness-and-generalized-minimal-models.md)

# 036 — Numerical semiampleness and generalized minimal models

[Index page](../index/algebraic-and-complex-geometry/036-numerical-semiampleness-and-generalized-minimal-models.md)

## Original CONTENTS.md summary

The release blurb 

> **036. Numerical semiampleness and generalized minimal models.** Proves numerical semiampleness for nef adjoints $`K_X+B+M`$ with $`K_X+B`$ pseudo-effective and M nef rational, for projective klt rational pairs over algebraically closed characteristic-zero fields and smooth compact Kähler rational klt simple-normal-crossing pairs, using Bott–Chern cohomology in the latter case. Separately, projective generalized log canonical rational pairs over such fields admit minimal models for pseudo-effective adjoints and Mori fiber spaces otherwise, with nef b-data fixed. [S1:1017]

This family ships **four** manuscripts, in two pairs. The numerical
semiampleness pair:

Manuscript 1, Kähler adjoints via Bott–Chern cohomology 

> Let $`X`$ be a smooth connected compact Kähler manifold, let $`B`$ be an
effective rational simple normal crossing divisor with coefficients less
than one, and let $`M`$ be a nef rational holomorphic line bundle on $`X`$.
If $`K_X+B`$ is pseudo-effective and $`K_X+B+M`$ is nef, we prove that its
first Chern class in real Bott–Chern cohomology is represented by a semiample
rational line bundle. This numerical statement allows a flat change of line
bundle; it does not assert semiampleness of the original adjoint. [S2:8–16]

Manuscript 2, projective klt rational pairs 

> We prove the Generalised Abundance Conjecture: if $`(X,B)`$ is a projective
klt $`\mathbb Q`$-pair over an algebraically closed field of characteristic zero,
$`K_X+B`$ is pseudo-effective, $`M`$ is a nef $`\mathbb Q`$-Cartier divisor on $`X`$,
and $`K_X+B+M`$ is nef, then $`K_X+B+M`$ is numerically equivalent to a
semiample $`\mathbb Q`$-Cartier divisor on $`X`$. [S4:39–45]

The minimal-model pair:

Manuscript 3, generalized log canonical $`\mathbb Q`$-pairs 

> We resolve the existence form of the minimal-model conjecture for projective
generalized log canonical $`\mathbb Q`$-pairs over algebraically closed fields of
characteristic zero. Such a pair admits a minimal model when its adjoint
divisor is pseudo-effective, and a Mori fibre space otherwise, while keeping
the nef $`\mathbb Q`$-Cartier b-divisor fixed. Taking the nef part to be zero gives
the corresponding result for ordinary log canonical $`\mathbb Q`$-pairs. [S6:9–16]

Manuscript 4, numerical-dimension-one minimal models 

> We resolve the numerical-dimension-one case of the minimal-model conjecture
for smooth connected complex projective varieties of dimension at least three.
If $`K_X`$ is pseudo-effective and $`\kappa_\sigma(X,K_X)=1`$, with
$`\kappa_\sigma`$ defined by section growth with a fixed ample twist, then $`X`$
admits a projective $`\mathbb Q`$-factorial terminal minimal model. [S8:32–38]

## Undergraduate summary

An **adjoint divisor** is a "canonical plus extra" divisor — the
canonical divisor $`K_X`$ (encoding differential forms) plus a boundary
$`B`$ (a weighted collection of subvarieties) plus a nef line bundle $`M`$.
The **abundance conjecture** says that if such an adjoint is nef
(nonnegative on every curve), then it is "semiample" — it has enough
sections to define a map, not just a numerical class.

This family proves a *numerical* form of semiampleness for these nef
adjoints in two settings: the projective klt rational-pair setting
(manuscript 2) and the smooth compact Kähler setting (manuscript 1),
where only the *cohomology class* of the adjoint is shown to be
represented by a semiample line bundle. Separately, the family resolves
the minimal-model conjecture: such pairs get a **minimal model** when the
adjoint is pseudo-effective (its class is "as positive as possible"), and
a **Mori fiber space** otherwise, with the nef "b-data" fixed throughout
(the minimal-model program's goal of reaching a canonical terminal form).

## Graduate summary

The four theorems split into a numerical-semiampleness pair and a
minimal-model pair, all over algebraically closed characteristic-zero
fields.

**Kähler numerical semiampleness.** 

> **theorem**
Let $`X`$ be a smooth connected compact Kähler manifold, let
$`B\geq0`$ be a rational simple normal crossing divisor whose
coefficients are strictly less than one, and let
$`M\in\mathrm{Pic}(X)\otimes_{\mathbb Z}\mathbb Q`$.
Assume that $`K_X+B`$ is pseudo-effective, $`M`$ is nef, and
$`D=K_X+B+M`$ is nef. Then there is a semiample rational line bundle
$`L`$ on $`X`$ such that
$$c_1(L)=c_1(D)\quad\text{in }H^{1,1}_{\mathrm{BC}}(X,\mathbb R).$$ [S3:19–30]

For a smooth connected compact Kähler manifold $`X`$, an effective
rational SNC boundary $`B`$ with coefficients below one, and a nef rational
line bundle $`M`$: if $`K_X + B`$ is pseudo-effective and $`D = K_X + B + M`$
is nef, then there is a semiample rational line bundle $`L`$ with
$`c_1(L) = c_1(D)`$ in real Bott–Chern cohomology. The statement is
*numerical* — it allows a flat change of line bundle and does not assert
semiampleness of the original adjoint $`D`$ itself.

**Projective klt abundance.** 

> **Theorem 1.1**
Let $`(X,B)`$ be a projective klt $`\mathbb Q`$-pair over an algebraically closed
field of characteristic zero. Suppose that $`K_X+B`$ is pseudo-effective,
and let $`M`$ be a nef $`\mathbb Q`$-Cartier divisor on $`X`$. If
$$D=K_X+B+M$$
is nef, then there is a semiample $`\mathbb Q`$-Cartier divisor $`L`$ on $`X`$ such
that $`D\equiv L`$. [S5:18–30]

For a projective klt $`\mathbb Q`$-pair $`(X, B)`$ over an algebraically closed
characteristic-zero field, with $`K_X + B`$ pseudo-effective and a nef
$`\mathbb Q`$-Cartier $`M`$: if $`D = K_X + B + M`$ is nef, then there is a semiample
$`\mathbb Q`$-Cartier divisor $`L`$ with $`D \equiv L`$ numerically. This is the
Generalised Abundance Conjecture in the stated setting.

**Generalized minimal models.** 

> **theorem**
Let $`k`$ be an algebraically closed field of characteristic zero, and let
$`(X,B+M)`$ be a projective generalized log canonical $`\mathbb Q`$-pair. Thus $`X`$ is
normal and integral, $`B`$ is an effective rational boundary, and $`M`$ is the
trace of a nef rational Cartier divisor on a higher projective birational
model, with $`K_X+B+M`$ $`\mathbb Q`$-Cartier.

There are a normal integral projective variety $`Y`$ and a birational map
$`\phi\colon X\dashrightarrow Y`$ whose inverse contracts no divisors such
that, writing $`B_Y=\phi_*B`$ and taking $`M_Y`$ to be the trace of the same
nef b-divisor, the generalized pair $`(Y,B_Y+M_Y)`$ is log canonical and
$$A_{X,B+M}(E)\le A_{Y,B_Y+M_Y}(E)$$
for every prime divisor $`E`$ over $`Y`$. [S7:16–42]

For a projective generalized log canonical $`\mathbb Q`$-pair $`(X, B + M)`$
(characteristic zero), there is a birational map $`\phi : X
\dashrightarrow Y`$ whose inverse contracts no divisors, taking $`M`$ to the
trace of the same nef b-divisor, such that $`(Y, B_Y + M_Y)`$ is log
canonical and log discrepancies do not increase. This is the existence
form of the minimal-model conjecture for generalized pairs; the nef
b-data is fixed, and the zero-nef-part case is the ordinary
log-canonical result.

**Numerical-dimension-one minimal models.** 

> **theorem**
Let $`X`$ be a smooth connected complex projective variety of dimension
$`n\geq3`$. Suppose that $`K_X`$ is pseudo-effective and
$`\kappa_\sigma(X,K_X)=1`$, with the convention
 . Then there are a normal projective
$`\mathbb Q`$-factorial terminal variety $`Y`$ with $`K_Y`$ nef and
a finite sequence
$`\phi:X\dashrightarrow Y`$ of $`K`$-negative divisorial contractions
and flips. The inverse of $`\phi`$ contracts no prime divisor. On a
common smooth projective resolution $`p:W\to X`$, $`q:W\to Y`$,
compatible canonical divisors satisfy
$$q^*K_Y-p^*K_X\sim_{\mathbb Q,\mathrm{num}}0.$$ [S9:51–68]

For a smooth connected complex projective variety $`X`$ of dimension
$`n \ge 3`$ with $`K_X`$ pseudo-effective and $`\kappa_\sigma(X, K_X) = 1`$
(the section-growth Kodaira dimension with a fixed ample twist), there is
a normal projective $`\mathbb Q`$-factorial terminal $`Y`$ with $`K_Y`$ nef,
reached by a finite sequence of $`K`$-negative divisorial contractions and
flips, and the pullbacks of the compatible canonical divisors agree
numerically.

## history of the conjecture

Prior (my training data, not this repo): the **Generalised Abundance
Conjecture** (Kawamata, Nakayama) extends the classical abundance
conjecture to the adjoint $`K_X + B + M`$ with an arbitrary nef $`\mathbb Q`$-Cartier
summand, and is known in the numerical-dimension-zero case (the
Kawamata-Shokurov base-point-free result) and in low dimension. The
projective klt case in manuscript 2 and the Kähler numerical form in
manuscript 1 (where the conclusion is a cohomology-class statement,
proved via Bott–Chern cohomology rather than the birational machinery)
are the content here for the numerical-semiampleness half. On the
minimal-model side, the minimal-model conjecture for generalized pairs
is a theorem of Birkar (for the log case) in the general setting;
manuscripts 3 and 4 give the projective generalized log-canonical
existence form and the numerical-dimension-one case for smooth
complex projective varieties, the latter through the $`K`$-MMP and a
fixed-ample-twist section-growth construction.

## Consequences

**Numerical semiampleness of nef adjoints** $`K_X + B + M`$ with
$`K_X + B`$ pseudo-effective and $`M`$ nef, in both the projective klt
rational-pair [S5:18–30] and the smooth compact Kähler
[S3:19–30] settings.

**Existence of generalized minimal models and Mori fiber spaces** for
projective generalized log canonical $`\mathbb Q`$-pairs, nef b-data fixed
[S7:16–42].

**A numerical-dimension-one minimal model** for smooth complex projective
threefolds and higher with pseudo-effective $`K_X`$ and
$`\kappa_\sigma(X, K_X) = 1`$ [S9:51–68].

## section skeleton

Four manuscripts, each a single main file with a flat section list.

Manuscript 1 [S2:8–16] `build/main.tex`, eight inputs [S2:2, 18–24]
(preamble; 01-introduction with the theorem at [S3:19], 02-preliminaries,
03-descent, 04-adjoint, 05-zero, 06-cycles, 07-completion).

Manuscript 2 [S4:39–45] `build/main.tex`, nine inputs [S4:49–58]
(introduction with the theorem at [S5:18], preliminaries, reduction,
jet-tools, geometry, frobenius, completion, positive, references).

Manuscript 3 [S6:9–16] `build/main.tex`, fourteen inputs [S6:2, 21–34]
(preamble; 01-introduction with the theorem at [S7:16], 00-conventions,
02-global, 03-cones, 04-product, 05-valuative, 06-cartier, 07-rounding,
08-integral-jump, 09-tower, 10-bounded-presentations, 11-traits,
12-incidence).

Manuscript 4 [S8:32–38] `build/paper.tex`, four inputs [S8:40–43]
(introduction with the theorem at [S9:51], mmp, numerics, conclusion).

## Coverage

T0: four manuscripts, zero comparator challenges, zero `main_results`
entries, zero scope notes. The ledger reads `paps 4`, `paps_form 0`,
`mainres 0`, `chal 0`, `scope_note 0`, `verification 0`, `trace`
empty, `shapes classification`, `resolves_named 0`. Each manuscript
ships a PDF at its directory top level (manuscript 1's is named
`numerical-generalized-abundance.pdf`, the others `paper.pdf`) and a
`build/` LaTeX tree. The catalog entry [S10:150] names all four PDFs.
No `verification/` bundle, no reasoning trace, no scope note, and no
comparator challenge: the family is a pure unformalized four-manuscript
set, the simplest tier in the release.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 036 at line 1017) |
| S2 | [`preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/build/main.tex`](../../../preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/build/main.tex) | 30 | Manuscript 1: abstract, section inputs |
| S3 | [`preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/build/sections/01-introduction.tex) | 160 | Manuscript 1: main theorem (Kähler numerical semiampleness) |
| S4 | [`preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/build/main.tex`](../../../preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/build/main.tex) | 60 | Manuscript 2: abstract, section inputs |
| S5 | [`preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/build/sections/introduction.tex`](../../../preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/build/sections/introduction.tex) | 154 | Manuscript 2: main theorem (projective klt abundance) |
| S6 | [`preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/build/main.tex`](../../../preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/build/main.tex) | 37 | Manuscript 3: abstract, section inputs |
| S7 | [`preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/build/sections/01-introduction.tex) | 262 | Manuscript 3: main theorem (generalized minimal models) |
| S8 | [`preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/build/paper.tex`](../../../preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/build/paper.tex) | 46 | Manuscript 4: abstract, section inputs |
| S9 | [`preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/build/sections/introduction.tex`](../../../preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/build/sections/introduction.tex) | 234 | Manuscript 4: main theorem (num-dim-one minimal models) |
| S10 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 036 at line 150) |
