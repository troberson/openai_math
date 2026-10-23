[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 060](../../index/algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md)

# 060 — The Global Spherical Shell conjecture

[Index page](../../index/algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1565]: "**060. The Global Spherical Shell conjecture.** Every connected minimal compact complex surface of class VII with $`b_2\gt 0`$ contains a global spherical shell, proving the positive-<i>b</i><sub>2</sub> Global Spherical Shell conjecture. Such a shell is a holomorphically embedded neighborhood of the standard three-sphere in $`\mathbb C^2\setminus\{0\}`$ whose complement is connected."

The manuscript, *Global Spherical Shells on Minimal Surfaces of
Class VII* [S2], has the abstract [S2:75–80]: "We prove the Global Spherical Shell conjecture: every connected minimal"

## Undergraduate summary

A compact complex surface is of class VII if its first Betti number is
one and its Kodaira dimension is $-\infty$. In the minimal case with
$b_2=0$, the surfaces are Hopf and Inoue surfaces. The positive-$b_2$
case is the setting of the Global Spherical Shell conjecture [S2:84–101]:
"A compact complex surface is of _class VII_ if its first Betti"

The theorem [S2:102–115]:

> **theorem**


## Graduate summary

**Kodaira identities and the two reductions.** The compact-surface
identities of Kodaira give $h^{0,1}=1$, $h^{1,0}=h^{2,0}=0$,
$b_2^+=0$, $\chi(\OO_X)=0$, and $K_X^2=-b_2(X)$, so the intersection
form is negative definite [S3:11–21]: "The compact-surface identities of Kodaira give, under the hypotheses of"

Two established reductions apply [S3:23–34]:

> **proposition**


The first is Enoki's theorem (square-zero divisor); the second is the
Dloussky–Oeljeklaus–Toma main theorem ($b_2$ rational curves). The
remaining case requires $C^2<0$ for every nonzero effective divisor,
and the proof produces $b_2$ rational curves on a negative-definite
surface.

**The curve production strategy.** The proof lifts to a cyclic cover
and constructs holomorphic sections with controlled decay. An area
bound with a common exponent constrains the normalizations of the
resulting divisor components [S4:3–17]:

> Proposition   constructs a section with end limits

Residue current arguments in weighted cohomology force the
normalizations to be rational, yielding the required $b_2$ curves
and applying the Dloussky–Oeljeklaus–Toma criterion.

**Deformation and topology.** Kato's deformation theorem then
identifies every such surface [S2:122–135]:

> **corollary**


## History of the conjecture

Kato introduced the shell framework in 1977. Dloussky developed its
description by sequences of blowups and contracting germs in 1984.
Nakamura's classification program included the conjecture as
Working Hypothesis 5.5. The $b_2=1$ case was proved by Teleman;
the $b_2=2$ cycle conclusion by Teleman using gauge theory [S2:160–187].
Gauge theory supplied major advances in the curve-production problem
through the work of Dloussky, Oeljeklaus, and Toma [S2:182–190].

## Consequences

**The positive-$b_2$ Global Spherical Shell conjecture is proved.**
Every connected minimal compact complex surface of class VII with
$b_2>0$ contains a global spherical shell [S2:102–115].

**The deformation type is a primary Hopf surface with $b$ blowups.**
Every such surface deforms to fibers obtained from a primary Hopf
surface by exactly $b_2$ successive point blowups
[S2:122–135].

**The smooth topology is determined.**
$\pi_1(X)\cong\Z$ and
$X\cong_{\text{or}}(S^1\times S^3)\# b\,\overline{\CP^2}$
[S2:122–135].

**The class VII exception in aspherical surface geography is removed.**
A sharpened Euler–signature inequality
$\chi_{\text{top}}(S)\geq \frac{9}{5}|\sigma(S)|$ follows
[S2:143–154].

## Section skeleton

**Main file** [S2], 6 sections under `build/sections/`:

1. Surface invariants and the cyclic cover [S3]
2. Divisor growth and residue currents [S4]
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
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 060 at line 1565. |
| S2 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/paper.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/paper.tex) | 349 | Main file: title, abstract, theorem, corollaries, and section inputs. |
| S3 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/surfaces.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/surfaces.tex) | 287 | Surface invariants, the cyclic cover, and the two reductions. |
| S4 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/curves.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/curves.tex) | 446 | Divisor growth, residue currents, and the area exponent. |
| S5 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/cylinder.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/cylinder.tex) | 583 | The cylinder exclusion of noncompact normalizations. |
| S6 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/weighted.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/weighted.tex) | 846 | The weighted cohomology and current independence. |
| S7 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/compact-data.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/compact-data.tex) | 125 | The compact datum construction. |
| S8 | [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/conclusion.tex`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/sections/conclusion.tex) | 282 | Conclusion and consequences. |
