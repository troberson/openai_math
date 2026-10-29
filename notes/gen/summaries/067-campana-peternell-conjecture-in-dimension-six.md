[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 067](../index/algebraic-and-complex-geometry/067-campana-peternell-conjecture-in-dimension-six.md)

# 067 — The Campana–Peternell conjecture in dimension six

[Index page](../index/algebraic-and-complex-geometry/067-campana-peternell-conjecture-in-dimension-six.md)

## Original CONTENTS.md summary

The release's blurb "**067. The Campana–Peternell conjecture in dimension six.** Proves the Campana–Peternell conjecture in complex dimension six: every smooth connected complex projective Fano sixfold with nef tangent bundle is rational homogeneous. [S1:1679]" The manuscript abstract
 reads: "We prove that every smooth connected complex projective Fano sixfold with nef
tangent bundle is rational homogeneous, resolving the Campana–Peternell
conjecture in complex dimension six.
As a consequence, a connected compact Kähler manifold $`X`$ with nef
holomorphic tangent bundle and
$`\dim_{\mathbb C}X-\widetilde q(X)\leq6`$ has ordinary universal cover
$`F\times\mathbb C^{\widetilde q(X)}`$, where $`F`$ is a rational homogeneous
manifold and $`\widetilde q(X)`$ is the maximal irregularity of a connected
finite étale cover. [S3:36–44]"

## Undergraduate summary

A smooth projective variety is *Fano* if its anticanonical bundle
is ample, and its tangent bundle is *nef* if it has nonnegative
degree on every curve. Rational homogeneous varieties (quotients
$`G/P`$ of a semisimple group by a parabolic) always have nef
tangent bundles. The Campana–Peternell conjecture asks whether the
converse holds among Fano varieties: does nefness of the tangent
bundle force the variety to be rational homogeneous? The theorem


> **Theorem 1.1**
Every smooth connected complex projective Fano variety of dimension six
with nef tangent bundle is rational homogeneous. [S4:23–26]

For a sixfold, the prior work covers every Picard number
$`\rho(X)\ge2`$ via Kanemitsu; only Picard number one remains, and
characterization results reduce that to pseudoindices four and
five . "Kanemitsu also proved that a smooth complex Fano $`n`$-fold with nef
tangent bundle is rational homogeneous whenever $`\rho(X)>n-5`$
\cite[Theorem 0.2]Kanemitsu2016. For a sixfold, this covers every
$`\rho(X)\geq2`$, leaving only Picard number one. In that range,
standard characterization results reduce the problem to pseudoindices
four and five. Watanabe treated the pseudoindex-four sixfold case
\cite[Theorem 2.4]Watanabe2021. We include an independent intersection
argument for it; the principal new step is pseudoindex five, where a
characteristic-number constraint leads to the Grassmannian. [S4:42–50]"

## Graduate summary

**The pseudoindex split.** The principal new step is
pseudoindex five. The pseudoindex is the least anticanonical
degree of a rational curve; for the remaining sixfold case it is
four or five, and the pseudoindex-four case has an independent
intersection argument [S5]. The pseudoindex-five case is where the
new machinery is needed [S4:42–50].

**Two uses of the universal family.** Nefness gives smoothness
and deformation properties of the family of minimal rational
curves, but those do not by themselves identify the threefold of
tangent directions. The proof uses the universal family in two
ways — as a family of curves over its parameter space and as a
family of threefolds over $`X`$ — and the compatibility of these two
maps gives a characteristic-number identity that determines the
projective variety of tangent directions . "We extract additional information by
using the universal family in two ways: as a family of rational curves
over their parameter space, and as a family of threefolds over $`X`$.
The compatibility of these two maps yields a characteristic-number
identity strong enough to determine the projective variety of tangent
directions. [S4:53–60]"

**The VMRT and the Grassmannian.** The variety of minimal
rational tangents (VMRT) is then constrained by characteristic
classes and the geometry of minimal curves. The sectional-genus
formula and a Grothendieck–Riemann–Roch characteristic-number
calculation force the tangent directions to be the Segre threefold
$`\mathbb P^1\times\mathbb P^2\subset\mathbb P^5`$, which is the
VMRT of the Grassmannian $`G(2,5)`$ and [S6]. "The sectional-genus
formula excludes $`u=4`$ and forces $`L^3=3`$ when $`u=8/3`$.
The variety of minimal rational tangents is consequently the Segre
threefold $`\mathbb P^1\times\mathbb P^2\subset\mathbb P^5`$. [S4:129–131]"

## History of the conjecture

Mori characterized projective space by ampleness of the tangent
bundle, which makes the corresponding nef question natural.
Campana and Peternell proved the conjecture in dimensions at most
three and for fourfolds of Picard number greater than one; the
remaining fourfold case was settled by Mok's and Hwang's study of
tangent directions of minimal rational curves [S4:20–35].

Watanabe proved the fivefold case of Picard number greater than
one, and Kanemitsu completed the fivefold classification and the
$`\rho>n-5`$ range [S4:37–42]. Hwang removed the fourth-Betti-number
hypothesis from Mok's argument, giving the VMRT classification
used here [S4:70–76].

## Consequences

**The sixfold Campana–Peternell conjecture.** Every smooth
connected complex projective Fano sixfold with nef tangent bundle
is rational homogeneous [S4:23–26].

**A Kähler universal-cover consequence.** A connected compact
Kähler manifold with nef holomorphic tangent bundle and
$`\dim X-\widetilde q(X)\le6`$ has universal cover
$`F\times\mathbb C^{\widetilde q(X)}`$ with $`F`$ rational
homogeneous [S3:36–44].

## Section skeleton

**Main file** [S3:36–44], 7 sections under `build/sections/`:
introduction [S4], $`p_1`$-cohomology, minimal curves,
pseudoindex-four [S5], characteristic classes, grassmannian
[S6], conclusion [S7].

The family also ships a finite-arithmetic certificate [S8]
(ledger `verification 1`).

## Coverage

T0: no Lean, no scope note, no comparator challenge, no
reasoning trace. Nothing about this family's theorem is
machine-checked. The ledger reads `paps_form 0`, `mainres 0`,
`scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
8 `.tex` files under `build/` and one `verification/verify.py`
certificate.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 067 at line 1679. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 208. |
| S3 | [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/main.tex`](../../../preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/main.tex) | 63 | Main file: title, abstract, and section inputs. |
| S4 | [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/01-introduction.tex`](../../../preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/01-introduction.tex) | 221 | The theorem, the prior cases, the pseudoindex split, the VMRT method, and the Grassmannian conclusion. |
| S5 | [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/03-pseudoindex-four.tex`](../../../preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/03-pseudoindex-four.tex) | 202 | The independent pseudoindex-four intersection argument. |
| S6 | [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/06-grassmannian.tex`](../../../preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/06-grassmannian.tex) | 167 | The pseudoindex-five characteristic-number constraint and the Grassmannian. |
| S7 | [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/07-conclusion.tex`](../../../preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/07-conclusion.tex) | 138 | The conclusion. |
| S8 | [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/verification/verify.py`](../../../preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/verification/verify.py) | 167 | The finite-arithmetic certificate. |
