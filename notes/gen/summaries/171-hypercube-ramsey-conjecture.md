[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 171](../index/combinatorics/171-hypercube-ramsey-conjecture.md)

# 171 — The hypercube Ramsey conjecture

[Index page](../index/combinatorics/171-hypercube-ramsey-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4008] and the catalog abstract [S2:421] state
the family's claim: the two-color Ramsey number of the $n$-dimensional
binary cube is at most $C2^n$ for an absolute constant $C$, resolving
positively the hypercube Ramsey conjecture of Burr and Erdős. The
manuscript's abstract "We prove that the two-color Ramsey number of the $n$-dimensional binary cube
is at most $C2^n$, where $C$ is an absolute constant. This resolves positively
the hypercube Ramsey conjecture of Burr and Erdős. [S3:37–39]"

## Undergraduate summary

For a finite graph $H$, let $R(H)$ be the least $M$ such that every
red-blue coloring of $K_M$ contains a monochromatic copy of $H$. The
$n$-cube $Q_n$ is the graph on $\{0,1\}^n$ with edges between vertices
differing in one coordinate, so $|V(Q_n)|=2^n$ and its maximum degree
is $n$ [S4:4–8]. The hypercube Ramsey conjecture, raised by Burr and
Erdős in 1975 as the cube case of their $L$-set question, asks whether
a single constant bounds $R(Q_n)/2^n$ for all $n$ [S4:20–30]. The
manuscript answers yes 

> **theorem**
There is an absolute constant $C>0$ such that
\[
R(Q_n)\le C2^n
\qquadfor every integer n\ge0.
\] [S4:10–16]

The lower bound is the standard two-block construction: color the edges
of two large sets red and the crossing edges blue, forcing
$R(Q_n)\ge3\cdot2^{n-1}-1$ [S4:47–62]. The theorem therefore determines
the order of $R(Q_n)$, though it gives no numerical value for $C$ and
does not settle whether $R(Q_n)/2^n$ converges.

## Graduate summary

**Why a constant factor is hard.** The cube's degree and degeneracy
both equal $n$, so the bounded-degeneracy results of Chvátal–Rödl–
Szemerédi–Trotter and Lee, which give linear bounds with constants
depending on the degree, cannot settle the cube question — their
constants may grow with the dimension [S4:64–79]. The upper-bound
program had to handle a target whose degree diverges, and its history
is a sequence of exponent improvements [S4:81–90]: from Beck's 1983
bound and the Graham–Rödl–Ruciński estimate $R(H)<8(8\Delta)^\Delta
|V(H)|$, which for the cube reads $m^{O(\log\log m)}$ in
$m=2^n$, through Shi's polynomial-in-$m$ bound, to Fox–Sudakov's
$n2^{2n+5}$, Conlon–Fox–Sudakov's $2^{2n+6}$, Lee's $2^{2n}+n^2 2^n$,
and Tikhomirov's $2^{2n-cn+1}$ — passing from a growing exponent in
$m$, to a fixed exponent, to an extra logarithmic factor above $m^2$,
to a constant multiple of $m^2$, to $(1+o(1))m^2$, and finally to an
exponent below $2$. The present theorem reaches a constant multiple of
$m$ [S4:81–90].

**The density boundary.** The cube sits at the natural density limit
for the $L$-set program: the first-moment lower bound used by Burr and
Erdős forces a linear Ramsey constant to satisfy
$e(H)/|V(H)|=O(\log|V(H)|)$, and the cube achieves exactly
$\tfrac12\log_2|V(Q_n)|$ edges per vertex, so it tests linear growth at
the largest density the necessary condition permits, beyond every
bounded-degeneracy family [S4:32–45].

**The proof's shape.** The argument works with a hypothetical
counterexample sequence of two disjoint host sides of size $N$ with
$N/2^n\to\infty$, and must retain a constant multiplicative loss while
the host order is only a slowly diverging multiple of $2^n$
[S4:125–180]. It uses a common-neighborhood embedding framework —
Kostochka–Rödl's deterministic lemma and Sudakov's probabilistic
argument, refined by Conlon, Fox–Sudakov, and Lee — together with
patch tiling of the cube into retained pieces whose sizes are chosen
from the host's mass distribution, and a resampling argument over the
patch profiles to recover a full cube in one color [S4:125–180]. A
terminology table at the end of the introduction fixes the vocabulary:
positions, labels, the ratio $C_n=N/2^n$, patch widths, raw laws,
gates, and profiles [S4:192–217].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Burr and Erdős introduced the $L$-set notion in 1975, conjecturing
that every family of uniformly bounded arboricity is an $L$-set, and
raised the cube question separately in Section 7 of that paper
[S4:20–30]. The cube's arboricity, maximum degree, and degeneracy all
equal $n$, so it sits at the boundary of every known positive result:
the Chvátal–Rödl–Szemerédi–Trotter theorem (1983) handles fixed maximum
degree, Lee's 2017 bound handles fixed degeneracy, and both leave the
cube's diverging degree open [S4:64–79]. The upper bound then improved
step by step — Beck (1983), Graham–Rödl–Ruciński (2001), Shi (2001,
2007), Fox–Sudakov (2009), Conlon–Fox–Sudakov (2016), Lee (2017),
Tikhomirov (2024) — each removing a factor of the growing exponent,
until the present constant multiple of $2^n$ closes the gap
[S4:81–90].

## Consequences

**The $L$-set question, cube case.** The theorem resolves positively
the hypercube Ramsey conjecture of Burr and Erdős, establishing that
the cubes form an $L$-set: one constant $C$ bounds $R(Q_n)/2^n$ for
every $n$ [S4:20–30].

**Transfer to subcubes and their Cartesian powers.** The bound
transfers immediately to any subgraph $H$ of $Q_d$ with
$2^d\le A|V(H)|$ for a fixed $A$, by monotonicity, giving
$R(H)\le CA|V(H)|$; and it extends to Cartesian powers of spanning
subgraphs, so $R(F^{\square k})\le C|V(F)|^k$ for a fixed $C$,
covering Cartesian powers of paths and cycles on $2^d$ vertices
[S4:93–121].

**The diagonal contrast.** The bound is for the *diagonal* Ramsey
number, where the target in both colors grows with $n$; the
off-diagonal results $R(Q_n,K_s)\le c_s 2^n$ for fixed $s$ (Conlon–
Fox–Lee–Sudakov) and the triangle asymptotic
$R(Q_n,K_3)=(1+o(1))2^{n+1}$ (Fiz Pontiveros et al.) are strictly
weaker in this sense and do not imply the diagonal theorem
[S4:125–180].

## Section skeleton

**Manuscript** [S3:37–39], 18 numbered sections under `build/sections/`
plus `proof-inputs.tex` and `regime-table.tex`: introduction [S4:10–16],
regime-guide, reduction-and-notation, general-conventions, bias-versus-
purity, constant-broad-high-neighborhood, very-small-polynomial-width,
small-power-key-grid, asymmetric-pure-patches, intermediate-powers-of-
bias, full-dimensional-cluster-patches, jump-to-large-bias,
two-deep-orientations, patch-tiling-under-9, internal-solver-and-
profiles, high-modes-of-the-tiling, low-modes-geometry,
initial-list-gates-and-resampling, late-dynamics.

The manuscript's root is `build/main.tex`, with a `references.tex`
bibliography (a `thebibliography` block) [S5]. It ships no
`verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 25 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 171 at line 4008. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 421. |
| S3 | [`preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/main.tex`](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/main.tex) | 53 | Main file: title and abstract. |
| S4 | [`preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/sections/01-introduction.tex) | 217 | The main theorem, the Burr--Erd\H{o}s L-set question, the density boundary, the lower bound, the progression of upper bounds, the consequences for related families, the background on embedding and sampling, and the terminology table. |
| S5 | [`preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/references.tex`](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/references.tex) | 227 | The manuscript's bibliography. |

## Bibliography

- K. Azuma, Weighted sums of certain dependent random variables, _Tohoku Mathematical Journal_ (2) **19** (1967), no. 3, 357–367.  .
- J. Beck, An upper bound for diagonal Ramsey numbers, _Studia Scientiarum Mathematicarum Hungarica_ **18** (1983), no. 2–4, 401–406.
- V. Chvátal, V. Rödl, E. Szemerédi and W. T. Trotter, Jr., The Ramsey number of a graph with bounded maximum degree, _Journal of Combinatorial Theory, Series B_ **34** (1983), no. 3, 239–243.  .
- D. Conlon, Hypergraph packing and sparse bipartite Ramsey numbers, _Combinatorics, Probability and Computing_ **18** (2009), no. 6, 913–923.  .
- D. Conlon, J. Fox, C. Lee and B. Sudakov, Ramsey numbers of cubes versus cliques, _Combinatorica_ **36** (2016), 37–70.  .
- D. Conlon, J. Fox and B. Sudakov, Short proofs of some extremal results II, _Journal of Combinatorial Theory, Series B_ **121** (2016), 173–196.  .
- N. Dirr, P. W. Dondl, G. R. Grimmett, A. E. Holroyd and M. Scheutzow, Lipschitz percolation, _Electronic Communications in Probability_ **15** (2010), 14–21.  .
- S. A. Burr and P. Erdős, On the magnitude of generalized Ramsey numbers for graphs, in _Infinite and Finite Sets_, Vol. I (Keszthely, 1973), Colloquia Mathematica Societatis János Bolyai **10**, North-Holland, Amsterdam, 1975, pp. 215–240.  .
- H. Finner, A generalization of Hölder's inequality and some probability inequalities, _The Annals of Probability_ **20** (1992), no. 4, 1893–1901.  .
- D. A. Freedman, On tail probabilities for martingales, _The Annals of Probability_ **3** (1975), no. 1, 100–118.  .
- R. Gandhi, S. Khuller, S. Parthasarathy and A. Srinivasan, Dependent rounding and its applications to approximation algorithms, _Journal of the ACM_ **53** (2006), no. 3, 324–360.  .
- W. T. Gowers, A new proof of Szemerédi's theorem for arithmetic progressions of length four, _Geometric and Functional Analysis_ **8** (1998), no. 3, 529–551.  .
- R. L. Graham, V. Rödl and A. Ruciński, On bipartite graphs with linear Ramsey numbers, _Combinatorica_ **21** (2001), no. 2, 199–209.  .
- B. Haeupler, B. Saha and A. Srinivasan, New constructive aspects of the Lovász Local Lemma, _Journal of the ACM_ **58** (2011), no. 6, Article 28, 1–28.  .
- P. Hall, On representatives of subsets, _Journal of the London Mathematical Society_ (1) **10** (1935), no. 1, 26–30.  .
- R. W. Hamming, Error detecting and error correcting codes, _Bell System Technical Journal_ **29** (1950), no. 2, 147–160.  .
- W. Hoeffding, Probability inequalities for sums of bounded random variables, _Journal of the American Statistical Association_ **58** (1963), no. 301, 13–30.  .
- S. Kakutani, A generalization of Brouwer's fixed point theorem, _Duke Mathematical Journal_ **8** (1941), no. 3, 457–459.  .
- C. Lee, Ramsey numbers of degenerate graphs, _Annals of Mathematics_ (2) **185** (2017), no. 3, 791–829.  .
- P. Erdős and L. Lovász, Problems and results on $3$-chromatic hypergraphs and some related questions, in _Infinite and Finite Sets_ (Keszthely, 1973), Colloquia Mathematica Societatis János Bolyai **10** (1975), 609–627.  .
- G. O. Mota, G. N. Sárközy, M. Schacht and A. Taraz, Ramsey numbers for bipartite graphs with small bandwidth, _European Journal of Combinatorics_ **48** (2015), 165–176.  .
- G. Fiz Pontiveros, S. Griffiths, R. Morris, D. Saxton and J. Skokan, The Ramsey number of the clique and the hypercube, _Journal of the London Mathematical Society_ **89** (2014), no. 3, 680–702.  .
- G. Fiz Pontiveros, S. Griffiths, R. Morris, D. Saxton and J. Skokan, On the Ramsey number of the triangle and the cube, _Combinatorica_ **36** (2016), 71–89.  .
- F. P. Ramsey, On a problem of formal logic, _Proceedings of the London Mathematical Society_ (2) **30** (1930), 264–286.  .
- A. V. Kostochka and V. Rödl, On graphs with small Ramsey numbers, _Journal of Graph Theory_ **37** (2001), no. 4, 198–204.  .
- L. Shi, Cube Ramsey numbers are polynomial, _Random Structures & Algorithms_ **19** (2001), no. 2, 99–101.  .
- L. Shi, The tail is cut for Ramsey numbers of cubes, _Discrete Mathematics_ **307** (2007), no. 2, 290–292.  .
- P. Erdős and J. Spencer, Lopsided Lovász Local Lemma and Latin transversals, _Discrete Applied Mathematics_ **30** (1991), nos. 2–3, 151–154.  .
- D. G. Harris and A. Srinivasan, Algorithmic and enumerative aspects of the Moser–Tardos distribution, _ACM Transactions on Algorithms_ **13** (2017), no. 3, Article 33, 1–40.  .
- J. Fox and B. Sudakov, Density theorems for bipartite graphs and related Ramsey-type results, _Combinatorica_ **29** (2009), no. 2, 153–196.  .
- B. Sudakov, A few remarks on Ramsey–Turán-type problems, _Journal of Combinatorial Theory, Series B_ **88** (2003), no. 1, 99–106.  .
- L. Lu and L. A. Székely, Using Lovász local lemma in the space of random injections, _The Electronic Journal of Combinatorics_ **14** (2007), no. 1, Research Paper 63.  .
- R. A. Moser and G. Tardos, A constructive proof of the general Lovász Local Lemma, _Journal of the ACM_ **57** (2010), no. 2, Article 11, 1–15.  .
- K. Tikhomirov, A remark on the Ramsey number of the hypercube, _European Journal of Combinatorics_ **120** (2024), article 103954.  . Preprint:  .
