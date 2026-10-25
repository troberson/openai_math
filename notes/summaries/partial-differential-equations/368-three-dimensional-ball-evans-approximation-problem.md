[Notes](../../README.md) / [Summaries](../README.md) / [Partial differential equations](../../index/disciplines/partial-differential-equations.md) / [Family 368](../../index/partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md)

# 368 — The three-dimensional Ball–Evans approximation problem

[Index page](../../index/partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md)

## Original CONTENTS.md summary

The release's blurb [S1:8904] and the catalog abstract [S2:837] state
the family's claim: every $W^{1,p}$ homeomorphism between arbitrary
bounded domains in $\mathbb R^3$, for $1\le p<\infty$, is a strong
$W^{1,p}$ limit of smooth diffeomorphisms onto the same target.
The family ships two manuscripts, one per exponent range. The
$1\le p\le 2$ abstract "We resolve the three-dimensional Ball–Evans approximation problem for
$1\le p\le2$. Every $W^{1,p}$ homeomorphism between arbitrary bounded domains
in $\mathbb R^3$ is a strong $W^{1,p}$ limit of smooth diffeomorphisms onto the same
target. [S3:53–58]" The $p>2$ abstract
 "We resolve the three-dimensional Ball–Evans approximation problem for every
finite $p>2$. Every $W^{1,p}$ homeomorphism between arbitrary bounded domains
in $\mathbb R^3$ can be approximated strongly in $W^{1,p}$ by smooth diffeomorphisms
onto the same target. [S5:53–58]"

## Undergraduate summary

The Ball–Evans problem asks whether Sobolev approximation of a
homeomorphism can preserve global injectivity. In nonlinear elasticity,
injectivity expresses noninterpenetration; the derivative records local
deformation. Convolution smooths but destroys injectivity. The question
is whether smooth diffeomorphisms onto exactly the same target
approximate the original map strongly in $W^{1,p}$. The $1\le p\le2$
manuscript states the theorem 

> **Theorem 1.1**
Let $\Omega,\Lambda\subset\mathbb R^3$ be nonempty bounded connected open sets, let $1\le p\le2$, and let $f:\Omega\to\Lambda$ be a homeomorphism in $W^{1,p}(\Omega;\mathbb R^3)$. There exist $C^\infty$ diffeomorphisms $f_j:\Omega\to\Lambda$, each belonging to $W^{1,p}(\Omega;\mathbb R^3)$, such that
$$\label{main:convergence}
\int_\Omega\bigl( |f_j-f|^p+|Df_j-Df|^p\bigr)\,dx\longrightarrow0.$$ [S4:29–34]

The $p>2$ manuscript states its counterpart 

> **Theorem 1.1**
Let $\Omega,\Lambda\subset\mathbb R^3$ be bounded domains, let $2<p<\infty$,
and let $f:\Omega\to\Lambda$ be a homeomorphism in
$W^{1,p}(\Omega;\mathbb R^3)$. There exist $C^\infty$ diffeomorphisms
$f_j:\Omega\to\Lambda$, each belonging to
$W^{1,p}(\Omega;\mathbb R^3)$, such that
$$\label{main:convergence}
\int_\Omega\bigl( |f_j-f|^p+|Df_j-Df|^p\bigr)\,dx\longrightarrow0.$$ [S6:25–34]

No boundary regularity, boundary extension, inverse Sobolev
regularity, or nonvanishing Jacobian is assumed [S4:36].

## Graduate summary

**The $1\le p\le2$ construction.** The proof first replaces $f$ by a
locally bi-Lipschitz homeomorphism with small strong Sobolev error,
using a budget that charges each curve or surface crossing to the
corresponding target edge or face. On retained compact sets where
$Df$ has fixed positive rank, the derivative is recovered through
rank-sensitive radial and disk constructions. Uncontrolled cells are
filled by radial collapse bounded by boundary energy. The final stage
smooths the PL map with fine value tolerances and positive local
degrees [S4:79–130].

**The $p>2$ construction.** The complementary range uses a
quantizer that reduces the variable target to a two-dimensional
polyhedral complex. Deficient-rank data are retained on rectangular
faces, and their scalar gradients are realized by source walls with
annular and disk geometry. Guards pin the wall labels; the lower
bound grows as the mesh scale tends to zero because $p>2$.
Nearly sharp energy bounds plus uniform convexity give strong
gradient approximation [S6:65–130].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace.

## History of the conjecture

The planar theory is complete: Iwaniec–Kovalev–Onninen for
$1<p<\infty$ and Hencl–Pratelli for $p=1$ [S4:38–55]. In dimensions
$n\ge4$, Campbell–Hencl–Tengvall constructed counterexamples for
$1\le p<\lfloor n/2\rfloor$ with Jacobians of both signs
[S4:56–63]. In dimension three, Hencl–Mály's orientation theorem gives
$\det Df\ge0$ a.e., removing the sign obstruction [S4:65–70].
Piecewise-affine smoothing in dimensions three and four is due to
Campbell–D'Onofrio–Vitek [S4:71–77].

## Consequences

**The full three-dimensional range is resolved.** Every
$W^{1,p}$ homeomorphism between bounded domains in $\mathbb R^3$
for $1\le p<\infty$ is a strong $W^{1,p}$ limit of smooth
diffeomorphisms onto the same target [S4:29–34], [S6:25–34].

**No boundary or Jacobian hypothesis.** The theorem requires no
boundary regularity, no boundary extension, no inverse Sobolev
regularity, and no nonvanishing Jacobian [S4:36].

**Dimension three is the critical case.** The sign obstruction
present in $n\ge4$ is absent in dimension three due to the
orientation theorem, making the problem solvable [S4:65–70].

## Section skeleton

**Manuscript 1** [S3:53–58] ($1\le p\le2$), 5 sections under
`build/sections/`: introduction [S4:29–34], smoothing, low-tools,
low-assembly, conclusion. Its root is `build/main.tex` with a
`references.bib` bibliography.

**Manuscript 2** [S5:53–58] ($p>2$), 8 sections under
`build/sections/` (including an appendix): introduction [S6:25–34],
high-preparation, quantizers, walls, mesh, high-assembly,
and smoothing (appendix). Its root is `build/main.tex` with a
`references.bib` bibliography.

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts, each a root `build/main.tex`, sections under
`build/sections/`, and a `references.bib` — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 368 at line 8904. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 837. |
| S3 | [`preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/build/main.tex`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/build/main.tex) | 70 | Manuscript 1 main file ($1\le p\le2$): title and abstract. |
| S4 | [`preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/build/sections/01-introduction.tex) | 252 | Manuscript 1 introduction: the theorem, prior work, and proof strategy. |
| S5 | [`preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/build/main.tex`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/build/main.tex) | 73 | Manuscript 2 main file ($p>2$): title and abstract. |
| S6 | [`preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/build/sections/01-introduction.tex) | 251 | Manuscript 2 introduction: the theorem, prior work, and proof strategy. |
