[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 093](../index/convex-and-metric-geometry/093-dimension-free-logarithmic-sobolev-inequality-for-subgaussian-log-concave-measures.md)

# 093 — Dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures

[Index page](../index/convex-and-metric-geometry/093-dimension-free-logarithmic-sobolev-inequality-for-subgaussian-log-concave-measures.md)

## Original CONTENTS.md summary

The release's blurb [S1:2304] and the catalog abstract [S2:262] state
the family's claim: every centered log-concave probability measure on
$\mathbb R^n$ with linear subgaussian parameter $a$ satisfies a
logarithmic Sobolev inequality with universal constant $Ca^2$,
independent of dimension. The manuscript's abstract 

> We prove that every centered log-concave probability measure with a
Lebesgue density on $\mathbb R^n$ and linear subgaussian parameter $a$
satisfies $\mathrm{Ent}_\mu(f^2)\le Ca^2\int|Df|^2\,d\mu$
for compactly supported smooth $f$, with one universal constant $C$.
This resolves positively the dimension-free logarithmic Sobolev conjecture
for subgaussian log-concave measures. [S3:55–60]

## Undergraduate summary

A logarithmic Sobolev inequality (LSI) bounds the entropy of a
function's square by its Dirichlet energy:
$\mathrm{Ent}_\mu(f^2)\le C\int|Df|^2\,d\mu$.
The constant $C$ controls Gaussian concentration of Lipschitz
functions and, through the Otto–Villani implication, a
transport–entropy inequality. For a log-concave measure
(density $\rho$ with $\log\rho$ concave), the natural question is
whether Gaussian tails of all *linear* functions already force the LSI,
with a constant that does not grow with the dimension.

The answer here is yes. A measure is "linearly $a$-subgaussian"
[S4:18–22] if every one-dimensional projection has
subgaussian parameter at most $a$. Under that hypothesis and
log-concavity, the LSI holds with a universal constant times $a^2$
[S4:26–36]. No smoothness of the density or positive
curvature bound is required [S4:38–41].

## Graduate summary

**The main theorem** [S4:26–36, `thm:main`]. There is an
absolute constant $C<\infty$ such that for every $n\ge1$, every
centered log-concave probability measure $\mu$ with a Lebesgue
density on $\mathbb R^n$, and every $a>0$ satisfying the
linearly-$a$-subgaussian condition,

> **Theorem 1.1**
There is an absolute constant $C<\infty$ with the following property.
For every $n\ge1$, every centered log-concave probability measure
$\mu$ with a Lebesgue density on $\mathbb R^n$, and every $a>0$
satisfying for $X\sim\mu$,
$$\mathrm{Ent}_\mu(f^2)\le C a^2\int_{\mathbb R^n}|Df|^2\,d\mu
 \qquad\text{for every }f\in C_c^\infty(\mathbb R^n).$$
The same constant works in every dimension. [S4:26–36]

The same constant works in every dimension.

**The transport–entropy corollary** [S4:57–65,
`cor:intro-transport`]. Under the same hypotheses,
$W_2(\nu,\mu)^2\le Ca^2\,H(\nu\mid\mu)$ for every
$\nu\in\mathcal P_2(\mathbb R^n)$, with the same absolute
constant $C$.

**The conjecture resolved.** Bizeul formulated the sufficiency of
uniformly subgaussian linear marginals for the dimension-free LSI
within the log-concave class in 2023 

> Bizeul formulated their sufficiency within the log-concave class in 2023
\cite[Conjecture 2]Bizeul2026. Theorem resolves
this conjecture for centered log-concave laws with a Lebesgue density,
under the precise marginal condition
 . [S4:94–98]

Prior bounds carried dimension dependence: Bobkov's norm-based
criterion gives order $na^2$; Bizeul's improvement gives order
$\sqrt n\,a^2$; and Bizeul obtained the dimension-free conclusion
restricted to rotationally invariant log-concave laws
[S4:100–114].

## History of the conjecture

Gross connected the Gaussian LSI with hypercontractivity and
established the framework of dimension-independent constants. Bakry
and \'Emery gave the LSI for a density $e^{-V}$ with
$D^2V\ge\kappa\,\mathrm{Id}$, constant at most
$\kappa^{-1}$; log-concavity alone gives only $D^2V\ge0$
[S4:72–80]. Herbst's argument shows that an LSI implies
Gaussian concentration, and under log-concavity the converse
direction holds through Milman's isoperimetric theorem and
Bobkov's lemma, so the linear-subgaussian hypothesis is
necessary up to universal constants [S4:84–93].

**Prior (my training data, not this repo).** I know Gross's
LSI–hypercontractivity theorem, the Bakry–\'Emery
curvature condition, Herbst's argument, the Otto–Villani
transport–entropy implication, and Bobkov's norm-based LSI
criterion. Bizeul's 2023 conjecture (conjecture 2 in his 2026
publication) asking whether uniform subgaussianity of linear
marginals suffices for a dimension-free LSI in the log-concave class
is, to my knowledge, a question that was open in the literature I
was trained on. I cannot independently verify this manuscript's
argument.

## Consequences

**Dimension-free LSI.** The logarithmic Sobolev constant of a
centered log-concave law is bounded by a universal multiple of the
squared linear subgaussian parameter, uniformly over all dimensions
[S4:26–36].

**Transport–entropy inequality.** The quadratic
transport–entropy constant is bounded by the same $Ca^2$
[S4:57–65].

**Gaussian concentration.** All Lipschitz functions concentrate
Gaussianly with variance proxy $Ca^2$ [S4:84–88].

## Section skeleton

One manuscript [S3:55–60] (title [S3:48–49], date [S3:51]) —
seven `.tex` section files under `build/sections/`
(introduction, calculus, critical, prediction, hierarchy, matrices,
observations) plus the root `main.tex`; two figures
(`figures/proof-dependencies.tex`, `glyph-mappings.tex`); a
20-entry `references.bib` [S5]. Total 4,989 lines. No manuscript
ships a `verification/` bundle.

## Comparison with the formalized statement

Nothing is formalized. The ledger row `fam=093` records
`paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`; there is no
entry in `lean/docs/`, no comparator stub, and no OAI tree for this
family. The release registers no scope note, no `main_results`
declaration, and no Lean source for this result.

## Coverage

T0: the family is not formalized. The ledger row `fam=093` records
`paps 1`, `paps_form 0`, `tier T0`, `chal 0`, `mainres 0`,
`scope_note 0`, `verification 0`, `trace` empty,
`shapes bound|uniform`, `resolves_named 0`, `summary 1`. The family
ships one LaTeX manuscript of 4,989 lines over 8 files, a 20-entry
BibTeX bibliography, and no verification bundle, no reasoning trace,
and no Lean formalization of any kind.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 093 at [S1:2304] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{093} at [S2:262] |
| S3 | [`preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/main.tex`](../../../preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/main.tex) | 75 | manuscript root; title [S3:48–49], date [S3:51], abstract [S3:55–60] |
| S4 | [`preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/sections/01-introduction.tex) | 254 | introduction; the main theorem [S4:26–36], the subgaussian definition [S4:18–22], the Bizeul conjecture citation [S4:94–98], and the prior-work paragraph [S4:72–80] |
| S5 | [`preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/references.bib`](../../../preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/references.bib) | 227 | 20-entry BibTeX bibliography |

## Bibliography

- It{\^o}, Kiyosi, Multiple Wiener integral (1951)
- Araki, Huzihiro, Yamagami, Shigeru, An inequality for Hilbert–Schmidt norm (1981)
- Bakry, Dominique, Émery, Michel, Diffusions hypercontractives (1985)
- Beigi, Salman, Sandwiched {Rényi} divergence satisfies data processing inequality (2013)
- Bizeul, Pierre, On the log-Sobolev constant of log-concave vectors (2026)
- Bobkov, Sergey G., Isoperimetric and analytic inequalities for log-concave probability measures (1999)
- Chen, Yuansi, Eldan, Ronen, Localization schemes: A framework for proving mixing bounds for Markov chains (2025)
- Eldan, Ronen, Koehler, Frederic, Zeitouni, Ofer, A spectral condition for spectral gap: fast mixing in high-temperature Ising models (2022)
- Gross, Leonard, Logarithmic Sobolev inequalities (1975)
- Guo, Dongning, Shamai (Shitz), Shlomo, Verdú, Sergio, Mutual information and minimum mean-square error in Gaussian channels (2005)
- Kim, Young-Heon, Milman, Emanuel, A generalization of Caffarelli's contraction theorem via (reverse) heat flow (2012)
- Klartag, Bo'az, Lehec, Joseph, Isoperimetric inequalities in high-dimensional convex sets (2025)
- Klartag, Bo'az, Putterman, Eli, Spectral monotonicity under Gaussian convolution (2023)
- Ledoux, Michel, Concentration of measure and logarithmic Sobolev inequalities (1999)
- Lieb, Elliott H., Convex trace functions and the Wigner–Yanase–Dyson conjecture (1973)
- Milman, Emanuel, Isoperimetric and concentration inequalities: Equivalence under curvature lower bound (2010)
- Otto, Felix, Villani, Cédric, Generalization of an Inequality by Talagrand and Links with the Logarithmic Sobolev Inequality (2000)
- Rothaus, O. S., Hypercontractivity and the Bakry–Emery criterion for compact Lie groups (1986)
- Tropp, Joel A., Second-order matrix concentration inequalities (2018)
- Viaclovsky, Jeff, Differential Analysis, MIT 18.156: Lecture Notes (2004)
