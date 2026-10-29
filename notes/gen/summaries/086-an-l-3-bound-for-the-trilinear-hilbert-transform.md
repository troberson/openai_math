[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 086](../index/real-and-complex-analysis/086-an-l-3-bound-for-the-trilinear-hilbert-transform.md)

# 086 — An $L^3$ bound for the trilinear Hilbert transform

[Index page](../index/real-and-complex-analysis/086-an-l-3-bound-for-the-trilinear-hilbert-transform.md)

## Original CONTENTS.md summary

The release's blurb [S1:2111] and the catalog abstract [S2:246] state
the family's claim: it proves the principal-value trilinear Hilbert
transform with shifts $`x-t`$, $`x-2t`$, $`x-3t`$ is bounded from
$`L^3(\mathbb R)^3`$ to $`L^1(\mathbb R)`$, the $`L^3`$ exponent case of the
standard trilinear Hilbert transform conjecture for the fixed slopes
$`1,2,3`$. The manuscript's abstract "We prove that the trilinear Hilbert transform with fixed slopes $`1,2,3`$ maps
$`L^3(\mathbb R)\times L^3(\mathbb R)\times L^3(\mathbb R)`$ to $`L^1(\mathbb R)`$, resolving this case of
the trilinear Hilbert transform conjecture. [S3:10–12]"

## Undergraduate summary

The operator multiplies three shifted copies of its inputs and
integrates against the principal value of $`1/t`$:

$$T(f_1,f_2,f_3)(x)
 =\mathrm{p.v.}\int_{\mathbb R}
 f_1(x-t)f_2(x-2t)f_3(x-3t)\,\frac{dt}{t}.$$

The question is which input exponents make $`T`$ bounded. The family
proves the symmetric $`L^3`$ case — each input in $`L^3(\mathbb R)`$,
output in $`L^1(\mathbb R)`$ [S4:1–9]:

> **theorem**
There is a finite constant $`C`$ such that
$$\lVert T(f_1,f_2,f_3)\rVert_{L^1(\mathbb R)}
 \le C\prod_{j=1}^3\lVert f_j\rVert_{L^3(\mathbb R)}
 \qquad(f_1,f_2,f_3\in\mathcal S(\mathbb R)).$$
Consequently $`T`$ has a unique bounded trilinear extension from
$`L^3(\mathbb R)\times L^3(\mathbb R)\times L^3(\mathbb R)`$ to $`L^1(\mathbb R)`$. [S4:11–20]

The principal value removes a symmetric interval about the origin; the
estimate extends $`T`$ uniquely as a bounded trilinear operator from
three $`L^3(\mathbb R)`$ inputs to $`L^1(\mathbb R)`$.

## Graduate summary

**Why the $`L^3`$ endpoint is hard.** The $`L^3`$ case is the critical
exponent of the standard conjecture for the fixed slopes $`1,2,3`$; the
full conjecture asks for a broader range of exponents [S4:22–33]. The
difficulty is the interaction of cancellation across scales with
quadratic modulation: the coefficients $`c=(-1,3,-3,1)`$ annihilate
$`(x+jt)^a`$ for $`a=0,1,2`$, so matched quadratic phases can persist in
the associated four-linear form, and quantitative information at one
scale must be organized so that this persistence does not accumulate a
loss proportional to the number of scales [S4:34–53].

**Three features of the scale summation.** The inverse theorem of
Leng, Sah and Sawhney supplies the structural input; its degree-two
case is used together with continuous chart and localization
statements the manuscript proves for the singular integral. The proof
of the summation has three features. First, private orthogonal
coordinates make the coefficients of each selected column recoverable,
and a compression lemma controls inherited projections uniformly in
spatial depth, with a logarithmic loss in a common budget
[S4:55–60]. Second, curvature is localized jointly in all four
arguments, and a short-block comparison gives a power of block length
whose exponent tends to zero as the auxiliary exponent decreases to
two [S4:62–68]. Third, each matched column receives one fixed mode
expansion, and frequency graphs separate square-summable errors from
coherent components with hereditary representatives
[S4:70–78].

**The operator bound reduces to a local estimate.** The outer section
reduces the operator estimate to a uniform maximal-function bound for
local forms; the uniform local estimate bounds the constants
independently of the depth parameter $`N`$ [S5:1–56]:

> **theorem**
For some $`q\in(2,3)`$, the constants $`C_N(q)`$ are bounded independently
of $`N`$. [S5:58–61]

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The bilinear predecessor was treated by Lacey and Thiele. Tao obtained
cancellation for truncated multilinear Hilbert transforms, improving
the elementary logarithmic truncation bound to a sublogarithmic one
and establishing a connection with higher-order uniformity. The
straight-line trilinear boundedness problem remained open in the
account of Hu and Lie; their results for curved transforms address a
different source of oscillation [S4:34–53]. The structural input comes
from the inverse theorem of Leng, Sah and Sawhney, whose degree-two
case provides the quantitative structure the proof organizes
[S4:48–53].

## Consequences

**The $`L^3`$ exponent case of the standard conjecture.** The theorem
resolves affirmatively the $`L^3\times L^3\times L^3 \to L^1`$ case of
the standard trilinear Hilbert transform conjecture for the fixed
slopes $`1,2,3`$, and extends $`T`$ as a bounded trilinear operator
[S4:22–33]. The result concerns the displayed fixed operator; it does
not cover the broader exponent range the full conjecture asks for
[S4:22–30].

**A reusable compression and counting toolbox.** The compression lemma
and the finite sparse counting lemma isolate tools for other
progression forms with the same projection and cancellation
structures [S4:62–78], so the argument is organized to transfer
beyond this particular operator.

## Section skeleton

**Manuscript** [S3:10–12], 10 sections under `build/sections/`:
introduction [S4:11–20], outer [S5:58–61], compression, charts, base,
localization, sides, linearization, counting, and completion.

The manuscript's root is `build/paper.tex`, with a `references.bib`
bibliography [S6]. It ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 12 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 086 at line 2111. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 246. |
| S3 | [`preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/paper.tex`](../../../preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/paper.tex) | 28 | Main file: title and abstract. |
| S4 | [`preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/sections/introduction.tex`](../../../preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/sections/introduction.tex) | 103 | The operator, the main L3 theorem, the conjecture's standing, and the three features of the proof. |
| S5 | [`preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/sections/outer.tex`](../../../preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/sections/outer.tex) | 182 | The uniform local estimate the operator bound reduces to. |
| S6 | [`preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/references.bib`](../../../preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/references.bib) | 65 | The manuscript's bibliography. |

## Bibliography

- David V. Cruz-Uribe, José María Martell, Carlos Pérez, Weights, Extrapolation and the Theory of Rubio de Francia (2011)
- W. T. Gowers, Julia Wolf, Linear forms and quadratic uniformity for functions on $`\mathbb{Z}_N`$ (2010)
- Ben Green, Terence Tao, The quantitative behaviour of polynomial orbits on nilmanifolds (2012)
- Martin Henk, Successive Minima and Lattice Points (2002)
- Bingyang Hu, Victor Lie, On the curved trilinear Hilbert transform (2023)
- Bingyang Hu, Victor Lie, On the boundedness of the curved trilinear Hilbert transform and the curved $`n`$-linear maximal operator in the quasi-Banach regime (2025)
- Michael Lacey, Christoph Thiele, $`L^p`$ estimates on the bilinear Hilbert transform for $`2<p<\infty`$ (1997)
- Michael Lacey, Christoph Thiele, On Calderón's conjecture (1999)
- James Leng, Ashwin Sah, Mehtaab Sawhney, Quasipolynomial bounds on the inverse theorem for the Gowers $`U^{s+1}[N]`$-norm (2024)
- Vladimir A. Mikhailets, Aleksandr A. Murach, General forms of the Menshov–Rademacher, Orlicz, and Tandori theorems on orthogonal series (2011)
- Giorgis Petridis, New proofs of Plünnecke-type estimates for product sets in groups (2012)
- Terence Tao, Cancellation for the multilinear Hilbert transform (2015)
