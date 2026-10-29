[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 060](../index/algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md)

# 060 — The Global Spherical Shell conjecture

[Index page](../index/algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md)

## Original CONTENTS.md summary

The release's blurb "**060. The Global Spherical Shell conjecture.** Every connected minimal compact complex surface of class VII with $`b_2\gt 0`$ contains a global spherical shell, proving the positive-$`b_2`$ Global Spherical Shell conjecture. Such a shell is a holomorphically embedded neighborhood of the standard three-sphere in $`\mathbb C^2\setminus\{0\}`$ whose complement is connected. [S1:1565]"

The manuscript, *Global Spherical Shells on Minimal Surfaces of
Class VII* [S2], has the abstract "We prove the Global Spherical Shell conjecture: every connected minimal
compact complex surface of class VII with positive second Betti number
contains a global spherical shell. This is a holomorphically embedded
neighborhood of the standard three-sphere in $`\mathbb C^2\setminus\{0\}`$
whose complement is connected. [S2:75–80]"

## Undergraduate summary

A compact complex surface is of class VII if its first Betti number is
one and its Kodaira dimension is $`-\infty`$. In the minimal case with
$`b_2=0`$, the surfaces are Hopf and Inoue surfaces. The positive-$`b_2`$
case is the setting of the Global Spherical Shell conjecture [S2:84–100]:
"A compact complex surface is of _class VII_ if its first Betti
number is one and its Kodaira dimension is $`-\infty`$. The classification
of these non-Kähler surfaces divides according to the second Betti
number. In the minimal case with $`b_2=0`$, work of Bogomolov,
Li–Yau–Zheng, and Teleman leads to the classification by Hopf and
Inoue surfaces .
The positive-$`b_2`$ case is the setting of the Global Spherical Shell
conjecture.

A _global spherical shell_ in a complex surface is a holomorphically
embedded neighborhood of the unit three-sphere in $`\mathbb C^2\setminus\{0\}`$
whose complement is connected. Kato introduced this structure
 . Nakamura's classification program includes the
conjecture that every minimal class VII surface with positive second
Betti number contains such a shell
\cite[Working Hypothesis 5.5]Nakamura1984; see also
 . We prove this assertion. [S2:84–100]"

The theorem 

> **theorem**
Let $`X`$ be a connected compact complex surface with
$$b_1(X)=1,\qquad b_2(X)>0,\qquad \kappa(X)=-\infty.$$
Assume that $`X`$ is minimal: it contains no smooth rational curve of
self-intersection $`-1`$. Then there are an open neighborhood $`U`$ of
$$S^3=\{z\in\mathbb C^2:|z|=1\}
 \quad\text{in }\mathbb C^2\setminus\{0\},$$
an open subset $`\Sigma\subset X`$, and a biholomorphism
$`\phi:U\longrightarrow\Sigma`$ such that $`X\setminus\Sigma`$ is connected. [S2:102–115]

## Graduate summary

**Kodaira identities and the two reductions.** The compact-surface
identities of Kodaira give $`h^{0,1}=1`$, $`h^{1,0}=h^{2,0}=0`$,
$`b_2^+=0`$, $`\chi(\mathcal O_X)=0`$, and $`K_X^2=-b_2(X)`$, so the intersection
form is negative definite "The compact-surface identities of Kodaira give, under the hypotheses of
Theorem ,
$$h^{0,1}(X)=1,\qquad h^{1,0}(X)=h^{2,0}(X)=0,\qquad
 b_2^+(X)=0,\qquad \chi(\mathcal O_X)=0,
 \qquad K_X^2=-b_2(X).$$
These are the numerical identities for class VII surfaces
\cite[Theorem 3]Kodaira1964; see also .
In particular the intersection form on $`H^2(X;\mathbb R)`$ is negative definite.
Our two surface-theoretic reductions are the following established results. [S3:11–21]"

Two established reductions apply 

> **proposition**
Let $`V`$ be a minimal compact complex surface with $`b_1(V)=1`$,
$`\kappa(V)=-\infty`$, and $`b_2(V)>0`$.
\beginenumerate[label=\textup{(\roman*)}]
\item If $`V`$ has a nonzero effective divisor $`C`$ with $`C^2=0`$, then $`V`$
has a global spherical shell.
\item If $`V`$ has exactly $`b_2(V)`$ rational curves, then $`V`$ has a global
spherical shell.
\endenumerate
Here the conclusion supplies an embedded open neighborhood of
$`S^3\subset\mathbb C^2\setminus\{0\}`$ with connected complement in $`V`$. [S3:23–34]

The first is Enoki's theorem (square-zero divisor); the second is the
Dloussky–Oeljeklaus–Toma main theorem ($`b_2`$ rational curves). The
remaining case requires $`C^2<0`$ for every nonzero effective divisor,
and the proof produces $`b_2`$ rational curves on a negative-definite
surface.

**The curve production strategy.** The proof lifts to a cyclic cover
and constructs holomorphic sections with controlled decay. An area
bound with a common exponent constrains the normalizations of the
resulting divisor components 

> Proposition constructs a section with end limits
$`(1,0)`$ for any prescribed finite decay rate of the holomorphic
structure. Before choosing that rate, we prove an area bound with an
exponent $`A`$ depending only on the lifted geometry. We then choose the
holomorphic structures to decay faster than this common exponent.

Our goal is to constrain the normalizations of the resulting divisor
components. A holomorphic differential on a normalization defines a
closed current on $`Y`$. We place currents with exponential mass bounds
in fixed weighted cohomology spaces and prove that currents carried by
distinct curves have independent classes. The scalar degree-one group vanishes,
so scalar differentials satisfying the mass bound cannot occur. This
will force genus zero here; Section will exclude the
remaining noncompact normalizations, using the same scalar obstruction
and the finite-dimensional cohomology for a fixed bundle $`E`$. [S4:3–17]

Residue current arguments in weighted cohomology force the
normalizations to be rational, yielding the required $`b_2`$ curves
and applying the Dloussky–Oeljeklaus–Toma criterion.

**Deformation and topology.** Kato's deformation theorem then
identifies every such surface 

> **corollary**
Let $`X`$ satisfy the hypotheses of Theorem , and put
$`b=b_2(X)`$. There is a small one-parameter deformation
$`\mathcal X\to\Delta`$ over a disk about $`0`$, with $`\mathcal X_0\simeq X`$,
such that every nonzero fiber is obtained from a primary Hopf surface by
exactly $`b`$ successive point blowups. The centers may be infinitely near.
Moreover,
$$\pi_1(X)\cong\mathbb Z,\qquad
 X\cong_{\mathrm{or}}(S^1\times S^3)\\\#\,b\,\overline{\mathbb{CP}}^{\,2},$$
where the second is an orientation-preserving diffeomorphism for the
complex orientation of $`X`$. [S2:122–135]

## History of the conjecture

Kato introduced the shell framework in 1977. Dloussky developed its
description by sequences of blowups and contracting germs in 1984.
Nakamura's classification program included the conjecture as
Working Hypothesis 5.5. The $`b_2=1`$ case was proved by Teleman;
the $`b_2=2`$ cycle conclusion by Teleman using gauge theory [S2:160–187].
Gauge theory supplied major advances in the curve-production problem
through the work of Dloussky, Oeljeklaus, and Toma [S2:182–190].

## Consequences

**The positive-$`b_2`$ Global Spherical Shell conjecture is proved.**
Every connected minimal compact complex surface of class VII with
$`b_2>0`$ contains a global spherical shell [S2:102–115].

**The deformation type is a primary Hopf surface with $`b`$ blowups.**
Every such surface deforms to fibers obtained from a primary Hopf
surface by exactly $`b_2`$ successive point blowups
[S2:122–135].

**The smooth topology is determined.**
$`\pi_1(X)\cong\Z`$ and
$`X\cong_{\text{or}}(S^1\times S^3)\\# b\,\overline{\CP^2}`$
[S2:122–135].

**The class VII exception in aspherical surface geography is removed.**
A sharpened Euler–signature inequality
$`\chi_{\text{top}}(S)\geq \frac{9}{5}|\sigma(S)|`$ follows
[S2:143–154].

## Section skeleton

**Main file** [S2], 6 sections under `build/sections/`:

1. Surface invariants and the cyclic cover [S3]
2. Divisor growth and residue currents [S4:3–17]
3. Cylinder [S5]
4. Weighted [S6]
5. Compact data [S7]
6. Conclusion [S8]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
7 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 060 at line 1565. |
| S2 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/paper.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/paper.tex) | 349 | Main file: title, abstract, theorem, corollaries, and section inputs. |
| S3 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/surfaces.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/surfaces.tex) | 287 | Surface invariants, the cyclic cover, and the two reductions. |
| S4 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/curves.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/curves.tex) | 446 | Divisor growth, residue currents, and the area exponent. |
| S5 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/cylinder.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/cylinder.tex) | 583 | The cylinder exclusion of noncompact normalizations. |
| S6 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/weighted.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/weighted.tex) | 846 | The weighted cohomology and current independence. |
| S7 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/compact-data.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/compact-data.tex) | 125 | The compact datum construction. |
| S8 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/conclusion.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/conclusion.tex) | 282 | Conclusion and consequences. |
