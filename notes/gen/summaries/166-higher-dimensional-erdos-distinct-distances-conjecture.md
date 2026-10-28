[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 166](../index/combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md)

# 166 — The higher-dimensional Erdős distinct-distances conjecture

[Index page](../index/combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:3906] and the catalog abstract [S2:411] state
the family's claim: for every fixed $d\ge3$, any $n\ge2$ distinct
points in $\mathbb R^d$ determine at least $c_d n^{2/d}$ distinct
distances, with $c_d>0$ depending only on the dimension — the
integer-grid order, resolving the higher-dimensional Erdős
distinct-distances conjecture with a constant-factor bound. The
manuscript's abstract "For every fixed integer $d\ge3$, we prove that every set of $n\ge2$ distinct
points in $\mathbb R^d$ determines at least $c_d n^{2/d}$ distinct
distances, where $c_d>0$ depends only on $d$. This resolves the
higher-dimensional Erdős distinct-distances conjecture positively. [S3:9–12]"

## Undergraduate summary

For a finite set $P\subset\mathbb R^d$, write $\Delta(P)$ for the set
of distances between its distinct points, and ask how small
$|\Delta(P)|$ can be for a prescribed cardinality [S4:3–17]. The
higher-dimensional Erdős conjecture predicts a constant multiple of
$n^{2/d}$ distances among any $n$ points, for every fixed $d\ge3$. The
manuscript proves this 

> **theorem**
For every integer $d\ge3$, there is a constant $c_d>0$ such that
every finite set $P\subset\mathbb R^d$ of $n\ge2$ distinct points
satisfies
$$|\Delta(P)|\ge c_d n^{2/d}.$$ [S4:19–26]

The power of $n$ is optimal: the integer grid $\{1,\ldots,t\}^d$ has
$t^d$ points and its squared distances are integers between $1$ and
$d(t-1)^2$, so the grid matches the predicted order
[S4:28–35]. In the plane the square grid gives
$O(n/\sqrt{\log n})$ distances, a different conjectural order.

## Graduate summary

**Why a constant factor is hard.** An estimate
$|\Delta(P)|\ge n^{2/d-o(1)}$ does not by itself imply the theorem:
the ratio $|\Delta(P)|/n^{2/d}$ could tend to zero more slowly than
every negative power of $n$. The proof must therefore exclude every
such sequence without first fixing a power saving, so it argues in the
least dimension in which the theorem could fail and addresses the
multiscale difficulty directly [S4:127–144].

**Four steps.** The proof is organized as four steps
[S4:149–266]. First, select a positive fraction of unordered pairs
whose displacement vectors admit interpolation by homogeneous
polynomials of degree $\lfloor A\rfloor$ at each center, excluding
the sparse-cones obstruction by a symmetric maximal selection
[S4:149–174]. Second, exclude sparse cones at all degree scales — the
central part of the paper — by dividing the point set according to how
successive polynomial equations cut down the dimension of the
varieties containing its points, testing degrees in exponential
windows, and comparing polynomial restriction ranks against the
small-degree coverage [S4:177–212]. Third, turn equal distances into
intersections of flats: for a generic rotated copy, the affine flats
defined by matched pairs carry the interpolation property, Cauchy–Schwarz
gives $\Omega(N^4/M)$ edges, and concentration bounds control the
neighbor families [S4:215–251]. Fourth, sample the retained flats once
with a fixed probability and compare polynomial ranks: a polynomial
of degree at most $\lfloor A\rfloor$ vanishes on every sampled flat but
is nonzero on at least one retained flat, so its restriction violates
local concentration [S4:254–266].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Erdős introduced the distinct-distances problem in 1946
[S4:3–11]. In higher dimensions the bound developed through
incidence estimates for curves and spheres: Clarkson, Edelsbrunner,
Guibas, Sharir, and Welzl bounded the number of pairs realizing a fixed
distance in three dimensions, and Aronov, Pach, Sharir, and Tardos
improved the three-dimensional lower bound to
$\Omega_\varepsilon(n^{77/141-\varepsilon})$ [S4:39–63]. Solymosi and
Vu developed recursive inequalities connecting distance bounds in
lower and higher dimensions, giving $n^{0.5643}$ in dimension three
[S4:64–86]. The rigid-motion approach of Elekes and Sharir was reduced
to incidences by Guth and Katz for the planar bound
$\Omega(n/\log n)$, and extended to higher dimensions by
Bardwell–Evans and Sheffer [S4:87–107]. Tidor, Yu, and Zakharov
proved $n^{2/3-o(1)}$ distinct distances in $\mathbb R^3$; inserting
their bound into the Solymosi–Vu recurrences gives
$n^{8/17-o(1)}$ in dimension four, still below the conjectured $2/d$
[S4:108–123].

## Consequences

**The full conjecture, with a constant factor.** The theorem resolves
the higher-dimensional Erdős distinct-distances conjecture positively
for every fixed $d\ge3$, establishing the $n^{2/d}$ lower bound with
an explicit dimension-dependent constant [S4:28–35].

**Optimality and the planar contrast.** The integer grid matches the
bound, so the power of $n$ is optimal; the planar square-grid
construction at $O(n/\sqrt{\log n})$ shows the planar problem has a
different conjectural order [S4:28–35].

**A quantitative gap closed.** The leading exponents from the
Solymosi–Vu recurrences applied to the best known three-dimensional
bound fell below $2/d$; the multiscale argument above closes exactly
that gap [S4:108–123].

## Section skeleton

**Manuscript** [S3:9–12], 11 sections under `build/sections/`:
introduction [S4:19–26], reduction, polynomial, secants, profiles,
sparse-cones, motions, depth, approximation, concentration, and
classical incidence.

The manuscript's root is `build/paper.tex`, with a `references.bib`
bibliography [S5]. It ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 16 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 166 at line 3906. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 411. |
| S3 | [`preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/paper.tex`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/paper.tex) | 28 | Main file: title and abstract. |
| S4 | [`preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/sections/introduction.tex) | 298 | The main theorem, the optimality argument, the history, why the constant factor matters, and the four-step proof overview. |
| S5 | [`preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/references.bib`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/references.bib) | 326 | The manuscript's bibliography. |

## Bibliography

- Ajtai, Miklós, Chvátal, Vašek, Newborn, Monroe M., Szemerédi, Endre, Crossing-Free Subgraphs (1982)
- Aronov, Boris, Pach, János, Sharir, Micha, Tardos, Gábor, Distinct distances in three and higher dimensions (2004)
- The Stacks Project Authors, The Stacks Project (2026)
- Bardwell-Evans, Sam, Sheffer, Adam, A reduction for the distinct distances problem in $\mathbb{R}^d$ (2019)
- Beck, József, On the lattice property of the plane and some problems of Dirac, Motzkin and Erdős in combinatorial geometry (1983)
- Chardin, Marc, Une majoration de la fonction de Hilbert et ses conséquences pour l'interpolation algébrique (1989)
- Chardin, Marc, Philippon, Patrice, Régularité et interpolation (1999)
- Chardin, Marc, Philippon, Patrice, Erratum to ``Régularité et interpolation'' (2002)
- Clarkson, Kenneth L., Edelsbrunner, Herbert, Guibas, Leonidas J., Sharir, Micha, Welzl, Emo, Combinatorial complexity bounds for arrangements of curves and spheres (1990)
- Szemerédi, Endre, Trotter, Jr., William T., Extremal problems in discrete geometry (1983)
- Elekes, György, Kaplan, Haim, Sharir, Micha, On lines, joints, and incidences in three dimensions (2011)
- Elekes, György, Sharir, Micha, Incidences in Three Dimensions and Distinct Distances in the Plane (2011)
- Elekes, György, Tóth, Csaba D., Incidences of not-too-degenerate hyperplanes (2005)
- Fulton, William, Intersection Theory (1998)
- Guth, Larry, Katz, Nets Hawk, On the {Erdős} distinct distances problem in the plane (2015)
- Guth, Larry, Katz, Nets Hawk, Algebraic methods in discrete analogs of the Kakeya problem (2010)
- Hartshorne, Robin, Algebraic Geometry (1977)
- Hatcher, Allen, Algebraic Topology (2002)
- Kaminski, J. Y., Kanel-Belov, A., Teicher, M., Trisecant lemma for nonequidimensional varieties (2008)
- Székely, László A., Crossing Numbers and Hard Erdős Problems in Discrete Geometry (1997)
- Leighton, Frank Thomson, Complexity Issues in VLSI: Optimal Layouts for the Shuffle-Exchange Graph and Other Networks (1983)
- Ran, Ziv, The (dimension + 2)-secant lemma (1991)
- Erdős, P., On sets of distances of $n$ points (1946)
- Solymosi, József, Vu, Van H., Near optimal bounds for the {Erdős} distinct distances problem in high dimensions (2008)
- Stone, A. H., Tukey, John W., Generalized ``sandwich'' theorems (1942)
- Tidor, Jonathan, Yu, Hung-Hsun Hans, Zakharov, Dmitrii, The {Erdős} distinct distances problem in $\mathbb{R}^3$ (2026)
- Walsh, Miguel N., The polynomial method over varieties (2020)
- Walsh, Miguel N., Concentration estimates for algebraic intersections (2023)
- Aksoy Yazici, Esen, {Erdős} distance problem in $\mathbb{R}^d$ (2020)
