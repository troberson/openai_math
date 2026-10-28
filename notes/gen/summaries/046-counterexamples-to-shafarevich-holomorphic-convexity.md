[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 046](../index/algebraic-and-complex-geometry/046-counterexamples-to-shafarevich-holomorphic-convexity.md)

# 046 — Counterexamples to Shafarevich holomorphic convexity

[Index page](../index/algebraic-and-complex-geometry/046-counterexamples-to-shafarevich-holomorphic-convexity.md)

## Original CONTENTS.md summary

The release blurb 

> **046. Shafarevich counterexamples in dimension two and with large fundamental group.** Constructs a smooth projective complex fourfold with large fundamental group whose universal cover contains no positive-dimensional compact analytic subvariety but is neither Stein nor holomorphically convex. A separate smooth projective complex surface already disproves unrestricted Shafarevich holomorphic convexity in dimension two. [S1:1233]

This family ships **two** counterexample manuscripts:

Manuscript 1, the fourfold with large fundamental group 

> We construct a smooth projective complex fourfold with large fundamental group
whose universal cover is not Stein. The universal cover contains no
positive-dimensional compact complex-analytic subvariety, so this disproves
Shafarevich's holomorphic-convexity conjecture even under the
large-fundamental-group hypothesis. [S2:12–18]

Manuscript 2, the surface counterexample 

> We construct a smooth connected projective complex surface whose universal
cover is not holomorphically convex. This disproves the Shafarevich
conjecture on holomorphic convexity in complex dimension two. [S4:46–50]

## Undergraduate summary

Shafarevich's **holomorphic-convexity conjecture** predicted that the
*universal cover* of a smooth hyperbolic projective variety should be
"Stein" — a particularly well-behaved kind of complex space, roughly one
that is as close as possible to being contractible from the analytic
point of view. A natural strengthening demanded *holomorphic convexity*,
a slightly weaker condition: for every point, its "holomorphic hull"
(the set it cannot be separated from by holomorphic functions) should be
compact.

This family shows the conjecture is false in two ways. Manuscript 2
builds a smooth projective *surface* (two complex dimensions) whose
universal cover is not holomorphically convex — the holomorphic hull of
a point on a certain curve is a noncompact union of rational curves.
Manuscript 1 builds a smooth projective *fourfold* (four complex
dimensions) with a genuinely *large* fundamental group (so it is not
some low-complexity degenerate case) whose universal cover contains no
positive-dimensional compact analytic subvariety yet still fails to be
Stein.

## Graduate summary

Both theorems are counterexamples to the Shafarevich
holomorphic-convexity conjecture, in the large-fundamental-group and
dimension-two settings respectively.

**The fourfold.** 

> **theorem**
There exist a smooth connected projective complex fourfold $X$ and a
simple abelian surface $A\subset X$ such that
\beginenumerate
\item $X$ has large fundamental group;
\item $\mathrm{im}\bigl(\pi_1(A)\to\pi_1(X)\bigr)\simeq\mathbb Z$.
\endenumerate
The universal cover $\widetilde X$ contains no positive-dimensional
compact complex analytic subvariety and is not Stein. [S3:17–26]

There is a smooth connected projective complex fourfold $X$ and a simple
abelian surface $A \subset X$ such that $X$ has large fundamental group
and the image of $\pi_1(A)$ in $\pi_1(X)$ is isomorphic to $\mathbb Z$. The
universal cover $\widetilde X$ contains no positive-dimensional compact
complex-analytic subvariety and is not Stein. The large-fundamental-group
hypothesis is met by the rank-one abelian-surface contribution, and the
failure of Steinness is a topological obstruction arising in a closed
piece of the cover.

**The surface.** 

> **Theorem 1.1**
There is a smooth connected projective complex surface $X$ containing a connected nodal curve $Z_0$ with smooth rational irreducible components such that
$$\mathrm{im}\bigl(\pi_1(Z_0)\longrightarrow\pi_1(X)\bigr)
 \quad\text{is infinite}.$$
In the simply connected universal cover of $X$, a connected component above $Z_0$ is a closed, connected, noncompact, locally finite union of compact rational curves. The holomorphic hull of any one of its points is noncompact. In particular, this universal cover is not holomorphically convex. [S5:19–26]

There is a smooth connected projective complex surface $X$ containing a
connected nodal curve $Z_0$ with smooth rational irreducible components
whose image in $\pi_1(X)$ is infinite. In the simply connected universal
cover, a connected component above $Z_0$ is a closed, connected,
noncompact, locally finite union of compact rational curves, and the
holomorphic hull of any one of its points is noncompact — so the
universal cover is not holomorphically convex. This is the
dimension-two refutation of the unrestricted conjecture.

## history of the conjecture

Prior (my training data, not this repo): Shafarevich's conjecture, in
the form relevant here, asks that the universal cover of a smooth
hyperbolic projective variety be Stein (or, weakened, holomorphically
convex), so that the variety inherits strong negative-curve and
functionality constraints. The conjecture is known in a range of
cases, including when the fundamental group is large in a strong
sense, and in low dimension under additional hypotheses. The
surface counterexample in manuscript 2 refutes the *unrestricted*
dimension-two statement; the fourfold counterexample in manuscript 1
refutes it even when the fundamental group is large (the obstruction
is a closed, finite-cover, non-Stein piece of the universal cover
rather than an infinite-dimensional one).

## Consequences

**A surface counterexample in dimension two.** A smooth projective
complex surface whose universal cover is not holomorphically convex
[S5:19–26].

**A fourfold counterexample with large fundamental group.** A smooth
projective complex fourfold, $\pi_1$ large, whose universal cover is
not Stein and contains no positive-dimensional compact analytic
subvariety [S3:17–26].

Together these refute Shafarevich's holomorphic-convexity conjecture
both in dimension two and under the large-fundamental-group hypothesis.

## section skeleton

Two manuscripts, each a single main file with a flat section list.

Manuscript 1 [S2:12–18] `build/main.tex`, eight inputs [S2:3, 21–27]
(preamble; 01-introduction with the theorem at [S3:17], 02-reduction,
03-paths, 04-geometry, 05-models, 06-image, 07-projective).

Manuscript 2 [S4:46–50] `build/main.tex`, six inputs [S4:53–58]
(01-introduction with the theorem at [S5:19], 02-weighted, 03-family,
04-involution, 05-quotient, 06-surface).

## Coverage

T0: two manuscripts, zero comparator challenges, zero `main_results`
entries, zero scope notes. The ledger reads `paps 2`, `paps_form 0`,
`mainres 0`, `chal 0`, `scope_note 0`, `verification 0`, `trace`
empty, `shapes counterexample`, `resolves_named 0`. Each manuscript
ships a PDF at its directory top level (manuscript 1's is named
`large-fundamental-group-non-stein.pdf`, manuscript 2's is
`paper.pdf`) and a `build/` LaTeX tree. The catalog entry [S6:168]
names both PDFs. No `verification/` bundle, no reasoning trace, no
scope note, and no comparator challenge: the family is a pure
unformalized counterexample pair, the simplest tier in the release.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 046 at line 1233) |
| S2 | [`preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/build/main.tex`](../../../preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/build/main.tex) | 30 | Manuscript 1: abstract, section inputs |
| S3 | [`preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/build/sections/01-introduction.tex) | 191 | Manuscript 1: main theorem (fourfold, non-Stein universal cover) |
| S4 | [`preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/build/main.tex`](../../../preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/build/main.tex) | 61 | Manuscript 2: abstract, section inputs |
| S5 | [`preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/build/sections/01-introduction.tex) | 170 | Manuscript 2: main theorem (surface, non-convex universal cover) |
| S6 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 046 at line 168) |
