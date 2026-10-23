[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 051](../../index/algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md)

# 051 — Kobayashi's canonical-ampleness conjecture

[Index page](../../index/algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1331]: "**051. Kobayashi's canonical-ampleness conjecture.** Every compact connected Kähler manifold of positive complex dimension with no nonconstant entire curve has ample canonical bundle and is therefore projective. This proves Kobayashi's canonical-ampleness conjecture in the smooth compact Kähler setting." The manuscript title is
"Canonical ampleness of compact hyperbolic Kähler manifolds" [S3:1], and its abstract [S4:46–49] reads: "We prove that every compact connected Kähler manifold of positive"

## Undergraduate summary

A complex manifold is Brody hyperbolic if every holomorphic map
$\C\to X$ is constant; on a compact manifold this is equivalent to
Kobayashi hyperbolicity [S5:3–8]. "A complex manifold is _Brody hyperbolic_ if every holomorphic map" The canonical bundle
$K_X$ is the line bundle of holomorphic $n$-forms. Kobayashi's
conjecture predicts that the absence of nonconstant entire curves
forces $K_X$ to be ample [S5:10–19]. The theorem [S5:21–26]:

> **theorem**


## Graduate summary

**The analytic core.** The proof begins with compact hyperbolicity,
which bounds the squared $k$-norm of the central derivative of every
holomorphic disc by a constant $D$ [S5:92–112]:

> Put $n=\dim_{\mathbb C}X$, let $\mathbb D=\{|z|<1\}$, and fix a Kähler metric $k$.

A maximizing disc is obtained by a penalized variational problem.
Boundary Sobolev regularity follows from maximality; a weighted
Hardy-space construction gives a boundary-unitary holomorphic frame
and center-fixed variations. The trace of the complex Hessian of the
area functional satisfies the identity [S5:121–128]:

> the complex second derivatives in these $n$ parameter directions,

**Two parameter choices.** $h=k$, $q=R_k$, $\delta\to 0$ gives a
uniform upper bound for the Poisson integral $P_{R_k}$, yielding
bounded canonical plurisubharmonic weights and nefness. The choice
$q=-h$, $\delta=1$ with $R_h\ge-h$ gives the pointwise volume
estimate [S5:147–157]:

> **equation**


**From volume to ampleness.** The negative-sign Aubin–Yau equation
produces metrics $h_t$ in the classes $2\pi c_1(K_X)+t[k]$; the
uniform volume estimate gives a positive lower bound for their
volumes, so $\int_X c_1(K_X)^n>0$ [S5:159–177]:

> Following the Monge–Amp\`ere and volume strategy used by Wu and Yau

Holomorphic Morse inequalities make the nef canonical bundle big;
the sections make $X$ Moishezon; a compact Kähler Moishezon manifold
is projective; the absence of rational curves and the log cone
theorem upgrade bigness to ampleness.

## History of the conjecture

The metric-curvature line: Wu–Yau proved canonical ampleness from
negative holomorphic sectional curvature on projective manifolds;
Tosatti–Yang extended to compact Kähler; Diverio–Trapani to
quasi-negative curvature; Broder–Stanfield allow Hermitian
pluriclosed metrics [S5:33–51]. "Theorem   gives a positive resolution in the smooth"

Gromov's Kähler hyperbolicity gives a different sufficient
hypothesis; Chen–Yang proved canonical ampleness under it, distinct
from Brody hyperbolicity [S5:53–60]. Ou's characterization of
uniruled compact Kähler manifolds gives nefness of $K_X$ under the
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

**Main file** [S4], 8 sections plus appendix:

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
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 051 at line 1331. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 178. |
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
