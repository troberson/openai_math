[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 063](../../index/algebraic-and-complex-geometry/063-generalized-mukai-conjecture.md)

# 063 — The generalized Mukai conjecture

[Index page](../../index/algebraic-and-complex-geometry/063-generalized-mukai-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1597]: "**063. The generalized Mukai conjecture.** Proves the generalized Mukai conjecture: every positive-dimensional smooth complex projective Fano manifold of dimension *n*, Picard number *ρ* and pseudoindex *ι* satisfies $`\rho(\iota-1)\le n`$, with equality exactly for $`(\mathbb P^{\iota-1})^\rho`$. Here the pseudoindex is the least anticanonical degree of a rational curve."

The manuscript, *The generalized Mukai conjecture* [S2], has the
abstract [S2:33–36]: "We prove the generalized Mukai conjecture: every positive-dimensional"

## Undergraduate summary

A Fano manifold is a smooth complex projective variety with ample
anticanonical divisor. Its pseudoindex is the smallest anticanonical
degree of an irreducible rational curve [S3:3–15]: "A Fano manifold is a smooth connected complex projective variety $X$"

The theorem [S3:22–33]:

> **theorem**


The bound says the Picard number times the pseudoindex minus one
cannot exceed the dimension. Equality forces the manifold to be a
product of projective spaces.

## Graduate summary

**The quantum-correspondence strategy.** The proof works in
quantum cohomology. Small quantum multiplication by a numerical
basis of divisor classes gives commuting matrices whose entries
encode two-point Gromov--Witten invariants [S3:76–91]:

> Write $r=\rho_X$ and $\iota=\iota_X$. If $\iota=1$, the inequality

The key difficulty is producing $r$ independent curve degrees
without assuming quantum cohomology is semisimple. The argument
uses a descendant lower bound (on the space of stable maps,
contracting components away from the marking and pushing forward
the virtual class to a weighted projective stack [S5]), a spectral
independence argument, and an alternating trace computation.

**The spectral independence.** A finite-shift recurrence for
descendant vectors gives an exponential upper bound. If all joint
eigenvalue tuples satisfied polynomial relations, the recurrence
would force subexponential decay, contradicting the descendant
lower bound. Thus one tuple has $r$ algebraically independent
coordinates [S3:110–127]:

> Here the divisor and recursion identities give a finite-shift

The alternating trace of matrix-valued differentials, computed in
a common triangular basis versus the fixed cohomology basis,
detects the nonzero product in independent curve degrees. The
argument applies to nonsemisimple commuting matrices.

**The equality case.** At equality all selected degrees are
minimal, so the nonzero quantum product implies a chain of actual
rational curves. The ordered-chain bound gives the dimension
estimate [S8:25–36]:

> 7

And Occhetta's product characterization identifies the manifold
[S8:43–50]:

> **theorem**


The numerically independent unsplit covering families with
anticanonical degrees summing to $n$ force the product of
projective spaces.

## History of the conjecture

Mukai's original index bound dates to 1988. Wiśniewski introduced
the pseudoindex and proved that $2\iota > n+2$ forces $\rho = 1$.
Bonavero, Casagrande, Debarre, and Druel established the bound for
dimension at most four and for smooth toric Fano manifolds in
certain ranges. Andreatta, Chierici, and Occhetta extended to
dimension five. Novelli and Occhetta handled large pseudoindex
$\iota \ge (n+3)/3$; Novelli later enlarged to $\iota > n/3$
[S3:35–64]. For special symmetry classes, Casagrande (toric),
Pasquier (horospherical), and Gagliardi--Hofscheier--Pearson
(spherical) settle the bound [S3:46–54]. The theorem here
imposes no restriction on dimension, Picard number, or geometry.

## Consequences

**The generalized Mukai conjecture is proved in full generality.**
Every positive-dimensional smooth complex projective Fano manifold
satisfies $\rho(\iota-1) \le n$ [S3:22–33].

**The equality case is classified.** Equality holds if and only if
$X \cong (\mathbb P^{\iota-1})^{\rho}$ [S3:22–33].

**The proof works without semisimplicity.** The quantum
correspondence argument does not assume quantum cohomology is
semisimple, so it covers nonsemisimple Fano manifolds [S3:110–127].

## Section skeleton

**Main file** [S2], 6 sections under `build/sections/`:

1. Introduction [S3]
2. Setup (quantum cohomology) [S4]
3. Descendants (point-descendant lower bound) [S5]
4. Spectral (eigenvalue independence) [S6]
5. Trace (alternating trace and curve correspondences) [S7]
6. Equality (ordered-chain bound and product characterization) [S8]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
7 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 063 at line 1597. |
| S2 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/main.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/main.tex) | 48 | Main file: title, abstract, and section inputs. |
| S3 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/introduction.tex) | 137 | The Fano setup, the theorem, prior work, and the quantum-correspondence proof strategy. |
| S4 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/setup.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/setup.tex) | 136 | Quantum cohomology setup and the divisor matrices. |
| S5 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/descendants.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/descendants.tex) | 424 | The point-descendant lower bound. |
| S6 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/spectral.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/spectral.tex) | 168 | The spectral independence of the joint eigenvalue tuples. |
| S7 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/trace.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/trace.tex) | 204 | The alternating trace and the independent curve correspondences. |
| S8 | [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/equality.tex`](../../../preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/equality.tex) | 157 | The equality case: ordered-chain bound and Occhetta's product characterization. |
