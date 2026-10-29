[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 051](../index/algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md)

# 051 — Kobayashi's canonical-ampleness conjecture

[Index page](../index/algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md)

## Original CONTENTS.md summary

The release's blurb "**051. Kobayashi's canonical-ampleness conjecture.** Every compact connected Kähler manifold of positive complex dimension with no nonconstant entire curve has ample canonical bundle and is therefore projective. This proves Kobayashi's canonical-ampleness conjecture in the smooth compact Kähler setting. [S1:1331]" The manuscript title is
"Canonical ampleness of compact hyperbolic Kähler manifolds [S3:1]" , and its abstract reads: "We prove that every compact connected Kähler manifold of positive
complex dimension containing no nonconstant entire curve has ample
canonical bundle and is projective. This resolves positively Kobayashi's
canonical-ampleness conjecture in the smooth compact Kähler category. [S4:46–49]"

## Undergraduate summary

A complex manifold is Brody hyperbolic if every holomorphic map
$`\mathbb C\to X`$ is constant; on a compact manifold this is equivalent to
Kobayashi hyperbolicity . "A complex manifold is _Brody hyperbolic_ if every holomorphic map
$`\mathbb C\to X`$ is constant. On a compact complex manifold, Brody's theorem
identifies this condition with Kobayashi hyperbolicity, the
nondegeneracy of the intrinsic pseudodistance defined by holomorphic
disc chains . We use ``hyperbolic'' in
this sense throughout. [S5:3–8]" The canonical bundle
$`K_X`$ is the line bundle of holomorphic $`n`$-forms. Kobayashi's
conjecture predicts that the absence of nonconstant entire curves
forces $`K_X`$ to be ample [S5:10–19]. The theorem 

> **Theorem 1.1**
Let $`X`$ be a compact connected Kähler manifold of positive complex
dimension. If every holomorphic map $`\mathbb C\to X`$ is constant, then $`K_X`$ is
ample. In particular, a positive tensor power of $`K_X`$ defines a
holomorphic embedding of $`X`$ into a complex projective space. [S5:21–26]

## Graduate summary

**The analytic core.** The proof begins with compact hyperbolicity,
which bounds the squared $`k`$-norm of the central derivative of every
holomorphic disc by a constant $`D`$ 

> Put $`n=\dim_{\mathbb C}X`$, let $`\mathbb D=\{|z|<1\}`$, and fix a Kähler metric $`k`$.
A disc $`f:\mathbb D\to X`$ has finite area if the integral of
$`k(f'(z),f'(z))`$ over $`\mathbb D`$ is finite. Compact hyperbolicity bounds the squared
$`k`$-norm of the central derivative of every holomorphic disc by a
constant $`D`$. For a closed
real $`(1,1)`$-form $`q`$, evaluated through its associated Hermitian
tensor, use the area and Poisson integrals
$$A_q(f)=\frac1\pi\int_\mathbb D q(f',f')\,\mathrm d S,
 \qquad
 P_q(f)=\frac2\pi\int_\mathbb D\log\frac1{|z|}\,q(f',f')\,\mathrm d S,$$
where $`\mathrm d S`$ is Euclidean area. We maximize
$$k(f'(0),f'(0))+P_q(f)-\delta A_h(f)$$
over finite-area discs with a fixed center, where $`h`$ is a Kähler
metric and $`\delta>0`$. The negative area term gives compactness. Comparing
a maximizing disc with its dilations then gives a linear boundary-area
tail bound. This improves its regularity to continuity on the closed
disc and $`W^{1,p}`$ for some $`p>2`$. [S5:92–112]

A maximizing disc is obtained by a penalized variational problem.
Boundary Sobolev regularity follows from maximality; a weighted
Hardy-space construction gives a boundary-unitary holomorphic frame
and center-fixed variations. The trace of the complex Hessian of the
area functional satisfies the identity 

> the complex second derivatives in these $`n`$ parameter directions,
evaluated at $`t=0`$. The trace of the
complex Hessian of the area functional is then
$$\mathcal L A_h(F_t)=n-A_{R_h}(f),
 \qquad R_h=-i\partial\bar\partial\log\det h,
 \qquad dd^c=i\partial\bar\partial.$$ [S5:121–128]

**Two parameter choices.** $`h=k`$, $`q=R_k`$, $`\delta\to 0`$ gives a
uniform upper bound for the Poisson integral $`P_{R_k}`$, yielding
bounded canonical plurisubharmonic weights and nefness. The choice
$`q=-h`$, $`\delta=1`$ with $`R_h\ge-h`$ gives the pointwise volume
estimate 

> $$h^n\ge e^{-D}\left(\frac{n}{2n+D}\right)^n k^n
 \quad\text{whenever }R_h\ge-h.$$
This estimate is uniform over the indicated metrics, even though the
auxiliary maximizing discs and their regularity constants need not be. [S5:147–157]

**From volume to ampleness.** The negative-sign Aubin–Yau equation
produces metrics $`h_t`$ in the classes $`2\pi c_1(K_X)+t[k]`$; the
uniform volume estimate gives a positive lower bound for their
volumes, so $`\int_X c_1(K_X)^n>0`$ 

> Following the Monge–Amp\`ere and volume strategy used by Wu and Yau
 , the negative-sign Aubin–Yau equation produces Kähler metrics $`h_t`$, for $`t>0`$,
in the classes $`2\pi c_1(K_X)+t[k]`$ with $`R_{h_t}=-h_t+t k`$.
Equation gives a positive lower bound for their
volumes. Passing to the limit in cohomology as $`t\downarrow0`$ proves
$`\int_X c_1(K_X)^n>0`$.

The remaining steps use established results with their usual
hypotheses. Holomorphic Morse inequalities make the nef canonical
bundle _big_, meaning that its sections have maximal,
$`n`$-dimensional asymptotic growth. The resulting sections make $`X`$
Moishezon, that is, its meromorphic function field has transcendence
degree $`n`$. A compact Kähler Moishezon manifold is projective.
Finally, the absence of rational curves and the log cone theorem
upgrade bigness to ampleness. The final implication is recorded in
\cite[Lemma 2.1]DiverioTrapani2019; see also
\cite[Lemma 5.1]Diverio2020. All the new estimates are proved
below; the standard existence, envelope, and positivity theorems are
stated at the points where they are used. [S5:159–177]

Holomorphic Morse inequalities make the nef canonical bundle big;
the sections make $`X`$ Moishezon; a compact Kähler Moishezon manifold
is projective; the absence of rational curves and the log cone
theorem upgrade bigness to ampleness.

## History of the conjecture

The metric-curvature line: Wu–Yau proved canonical ampleness from
negative holomorphic sectional curvature on projective manifolds;
Tosatti–Yang extended to compact Kähler; Diverio–Trapani to
quasi-negative curvature; Broder–Stanfield allow Hermitian
pluriclosed metrics . "Theorem gives a positive resolution in the smooth
compact Kähler category. A major preceding advance is the theorem
of Wu and Yau: negative holomorphic sectional curvature of a Kähler metric forces
canonical ampleness on a smooth projective manifold
 . Tosatti and Yang extended that implication to
compact Kähler manifolds without assuming projectivity
 . Diverio–Trapani extended the conclusion to quasi-negative holomorphic
sectional curvature: the curvature is nonpositive everywhere and
strictly negative in every nonzero tangent direction at one point
 . Wu–Yau subsequently gave another proof
covering both the negative and quasi-negative cases
 . Broder–Stanfield allow the negatively curved
metric $`\omega`$ to be Hermitian and pluriclosed, meaning
$`i\partial\bar\partial\omega=0`$, while retaining the ambient
Kähler hypothesis \cite[Theorem 1.1]BroderStanfield2026.
These metric hypotheses give curvature
inequalities unavailable from the absence of entire curves alone.
The present proof begins instead with the derivative bounds supplied
by compact hyperbolicity. [S5:33–51]"

Gromov's Kähler hyperbolicity gives a different sufficient
hypothesis; Chen–Yang proved canonical ampleness under it, distinct
from Brody hyperbolicity [S5:53–60]. Ou's characterization of
uniruled compact Kähler manifolds gives nefness of $`K_X`$ under the
weaker absence of rational curves; the present proof retains a
direct disc proof because it produces bounded canonical potentials
and uses the same Hessian identity as the volume estimate
[S5:62–76].

## Consequences

**Kobayashi's canonical-ampleness conjecture in full.** Every
compact connected Kähler manifold of positive complex dimension
with no nonconstant entire curve has ample canonical bundle and is
projective [S5:21–26]. No projectivity, curvature, or
dimensional hypothesis is imposed beyond Brody hyperbolicity.

**Pluricanonical and semialgebraic consequences.** The result
applies to pluricanonical sections and semialgebraic universal
covers [S12].

## Section skeleton

**Main file** [S4:46–49], 8 sections plus appendix:

1. Introduction [S5]
2. Preliminaries [S6]
3. Extremal discs [S7]
4. Frames and variations [S8]
5. The Hessian identity [S9]
6. Nefness [S10]
7. Volume and ampleness [S11]
8. Consequences [S12]

Appendix: smoothing [S13].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
10 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 051 at line 1331. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 178. |
| S3 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/README.md`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/README.md) | 17 | Manuscript readme: title, author, date. |
| S4 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/main.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/main.tex) | 70 | The main file: abstract and section inputs. |
| S5 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/introduction.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/introduction.tex) | 197 | The theorem, the context, the analytic argument, and the ampleness strategy. |
| S6 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/preliminaries.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/preliminaries.tex) | 107 | Curvature, Green-function, and disc-functional conventions. |
| S7 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/extremal-discs.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/extremal-discs.tex) | 353 | Maximizing discs and boundary regularity. |
| S8 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/frames-variations.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/frames-variations.tex) | 520 | Boundary-unitary frames and centered holomorphic variations. |
| S9 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/hessian.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/hessian.tex) | 199 | The determinant and Hessian identities. |
| S10 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/nefness.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/nefness.tex) | 209 | Bounded canonical potentials and nefness. |
| S11 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/volume-ampleness.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/volume-ampleness.tex) | 360 | The uniform volume estimate and the passage to ampleness. |
| S12 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/consequences.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/consequences.tex) | 64 | Applications to pluricanonical sections and semialgebraic universal covers. |
| S13 | [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/smoothing.tex`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/smoothing.tex) | 230 | The bounded-potential smoothing argument. |
