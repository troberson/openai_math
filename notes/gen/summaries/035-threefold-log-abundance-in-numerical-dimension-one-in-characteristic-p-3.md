[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 035](../index/algebraic-and-complex-geometry/035-threefold-log-abundance-in-numerical-dimension-one-in-characteristic-p-3.md)

# 035 — Threefold log abundance in numerical dimension one in characteristic $p>3$

[Index page](../index/algebraic-and-complex-geometry/035-threefold-log-abundance-in-numerical-dimension-one-in-characteristic-p-3.md)

## Original CONTENTS.md summary

The release blurb 

> **035. Log-canonical threefold abundance in numerical dimension one.** Proves log abundance for projective log canonical threefold pairs over algebraically closed fields of characteristic p > 3 when the effective boundary is rational and the ℚ-Cartier adjoint is nef of numerical dimension one. The adjoint is semiample, without requiring the original variety to be terminal or ℚ-factorial. [S1:992]

This family ships **two** manuscripts. Their abstracts:

Manuscript 1, log-canonical threefold log abundance 

> We prove the numerical-dimension-one case of log abundance for threefolds
over algebraically closed fields of characteristic $p>3$. If $(X,B)$ is a
projective log canonical threefold pair with effective rational boundary,
and $K_X+B$ is $\mathbb Q$-Cartier, nef, and of numerical dimension one, then
$K_X+B$ is semiample. Neither terminality nor $\mathbb Q$-factoriality of $X$
is required. [S2:40–47]

Manuscript 2, terminal threefold abundance 

> Let $X$ be a projective $\mathbb Q$-factorial terminal threefold over an
algebraically closed field of characteristic $p>3$. We prove the
numerical-dimension-one case of abundance: if $K_X$ is nef with
$\nu(K_X)=1$, then $K_X$ is semiample and $\kappa(X,K_X)=1$. [S4:10–15]

## Undergraduate summary

The "Kodaira dimension" $\kappa(X)$ of a variety $X$ measures how many
independent holomorphic differential forms $X$ carries — roughly, how
close $X$ is to being "of general type." A natural conjecture, the
**abundance conjecture**, says that if the canonical divisor $K_X$
(the "differential-form line bundle") is "nef" (non-negative on every
curve) and has "numerical dimension" $\nu(K_X)$, then $K_X$ is
semiample — it has enough sections to actually reach dimension
$\nu(K_X)$, not just numerical dimension.

This family proves the $p > 3$ characteristic version of the
numerical-dimension-one case, in two flavors. Manuscript 1 is the
**log-canonical** version: you may add an effective "boundary" divisor
$B$ (a weighted collection of subvarieties), and the combination
$K_X + B$ is semiample under the nef / numerical-dimension-one
hypothesis, without assuming $X$ is terminal or $\mathbb Q$-factorial.
Manuscript 2 is the plain **terminal** version: for a $\mathbb Q$-factorial
terminal threefold, nef $K_X$ with $\nu(K_X) = 1$ is semiample and
$\kappa(X, K_X) = 1$.

## Graduate summary

Both theorems are numerical-dimension-one abundance statements for
threefolds in positive characteristic $p > 3$, with manuscript 1 the
log version and manuscript 2 the terminal version.

**Log-canonical log abundance.** 

> **Theorem 1.1**
Let $k$ be an algebraically closed field of characteristic $p>3$.
Let $(X,B)$ be a projective log canonical threefold pair over $k$,
where $X$ is normal, $B$ is an effective $\mathbb Q$-divisor, and $K_X+B$
is $\mathbb Q$-Cartier. If $K_X+B$ is nef and has numerical dimension one,
then $K_X+B$ is semiample. [S3:15–21]

For a projective log canonical threefold pair $(X, B)$ over an
algebraically closed field of characteristic $p > 3$, with $X$ normal,
$B$ an effective $\mathbb Q$-divisor, and $K_X + B$ $\mathbb Q$-Cartier: if $K_X + B$
is nef and of numerical dimension one, then $K_X + B$ is semiample.
The notable hypotheses dropped compared to the complex-number
literature are **terminality** and **$\mathbb Q$-factoriality** of the
original variety — the boundary coefficients are the rational numbers
allowed by log canonicity, and neither singularity assumption is
required of $X$.

**Terminal abundance.** 

> **theorem**
Let $X$ be a normal projective $\mathbb Q$-factorial threefold over an
algebraically closed field $k$ of characteristic $p>3$. Suppose that
$X$ has terminal singularities and that $K_X$ is nef with
$\nu(K_X)=1$. Then some positive Cartier multiple of $K_X$ has at
least two independent global sections. In particular,
$\kappa(X,K_X)=1$ and $K_X$ is semiample. [S5:14–21]

For a normal projective $\mathbb Q$-factorial terminal threefold $X$ over an
algebraically closed field of characteristic $p > 3$ with $K_X$ nef and
$\nu(K_X) = 1$: some positive Cartier multiple of $K_X$ has at least
two independent global sections, so $\kappa(X, K_X) = 1$ and $K_X$ is
semiample. No assumption is made on the first Betti number,
irregularity, or the Albanese variety.

## history of the conjecture

Prior (my training data, not this repo): the abundance conjecture is a
central open problem in birational geometry, known in the
numerical-dimension-zero case (Miyaoka, in characteristic zero and
now in mixed/positive characteristic) and for various low-dimension
and special-fiber scenarios. The numerical-dimension-one case for
threefolds in positive characteristic is the content here. Manuscript
1's log-canonical extension removes the terminal and $\mathbb Q$-factorial
hypotheses that the classical Miyaoka-style argument carries; the
log boundary $B$ lets you absorb the adjunction data from a fibration
into a pair. Manuscript 2's terminal version is the plain
canonical-divisor statement in the $\mathbb Q$-factorial terminal setting.
Both resolve the numerical-dimension-one slice of the abundance
conjecture in the stated characteristic range.

## Consequences

**Log-canonical threefold log abundance in numerical dimension one**
for $p > 3$, without terminality or $\mathbb Q$-factoriality of the original
variety [S3:15–21].

**Terminal threefold abundance in numerical dimension one** for
$p > 3$: nef $\nu(K_X) = 1$ canonical divisor is semiample with
$\kappa(X, K_X) = 1$, no Betti-number or Albanese hypothesis
[S5:14–21].

## section skeleton

Two manuscripts, each a single main file with a flat section list.

Manuscript 1 [S2:40–47] `build/main.tex`, seven inputs [S2:48–54]
(introduction with the theorem at [S3:15], foundations, boundary,
isolation, torsion, cycle, bibliography).

Manuscript 2 [S4:10–15] `build/paper.tex`, seven inputs [S4:3, 18–23]
(preamble; introduction with the theorem at [S5:14], preparation,
slopes, jets, laurent, cartier).

## Coverage

T0: two manuscripts, zero comparator challenges, zero `main_results`
entries, zero scope notes. The ledger reads `paps 2`, `paps_form 0`,
`mainres 0`, `chal 0`, `scope_note 0`, `verification 0`, `trace`
empty, `shapes bound|classification`, `resolves_named 0`. Each
manuscript ships a `paper.pdf` at its directory top level and a
`build/` LaTeX tree. The catalog entry [S6:148] names both PDFs. No
`verification/` bundle, no reasoning trace, no scope note, and no
comparator challenge: the family is a pure unformalized
manuscript pair, the simplest tier in the release.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 035 at line 992) |
| S2 | [`preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/build/main.tex`](../../../preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/build/main.tex) | 55 | Manuscript 1: abstract, section inputs |
| S3 | [`preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/build/sections/introduction.tex`](../../../preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/build/sections/introduction.tex) | 112 | Manuscript 1: main theorem (log abundance, num dim 1) |
| S4 | [`preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/build/paper.tex`](../../../preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/build/paper.tex) | 29 | Manuscript 2: abstract, section inputs |
| S5 | [`preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/build/sections/introduction.tex`](../../../preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/build/sections/introduction.tex) | 206 | Manuscript 2: main theorem (abundance, terminal, num dim 1) |
| S6 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 035 at line 148) |
