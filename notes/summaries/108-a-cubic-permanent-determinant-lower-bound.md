[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 108](../index/theoretical-computer-science/108-a-cubic-permanent-determinant-lower-bound.md)

# 108 — A cubic permanent–determinant lower bound

[Index page](../index/theoretical-computer-science/108-a-cubic-permanent-determinant-lower-bound.md)

## Original CONTENTS.md summary

[S1:2679] (family entry):

> **108. A cubic permanent–determinant lower bound.** Proves an $\Omega(n^3)$ lower bound for the border determinantal complexity of the $n\times n$ permanent over ℂ. Even coefficientwise limits of determinants of affine-linear matrices require matrix size at least $cn^3$, for an absolute c > 0 and all sufficiently large n; the same bound therefore holds for exact representations. ([Lean](../../lean/docs/108.md))

[S1:2686] (the manuscript entry, with its abstract at [S1:2688]):

> [A cubic lower bound for border determinantal complexity of the permanent](../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf)

> We prove that the complex border determinantal complexity of the $m\times m$ permanent is $\Omega(m^3)$, allowing arbitrary affine-linear determinant representations and coefficientwise limits. It also gives cubic lower bounds for exact determinantal complexity and for the numbers of vertices and edges in affine-linear algebraic branching programs, including coefficientwise limits with a fixed vertex or edge budget.

[S2:294] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Determinantal complexity** asks: how large a matrix must you fill with
linear forms in the variables of a polynomial so that the determinant of
that matrix equals the polynomial? For the *permanent* of an
$m\times m$ matrix (which is like the determinant but without the
signed row permutations), the best lower bound before this work was
$m^2/2$.

The **border** version allows taking a limit: you can approximate the
permanent as closely as you want with determinants of a fixed size
$n$, and the question becomes: how large must $n$ be?

This paper proves that $n \ge c\,m^3$ for some absolute constant $c>0$
and all sufficiently large $m$. The construction works in two stages:

1. **A general geometric theorem** [S4:154–157]: for a polynomial in
   $d$ variables whose leading homogeneous term has degree $r$ and no
   nonzero singular zero, the exact and border determinantal sizes are
   at least $(r-1)(d-1)/(4e)$.

2. **A permanent-specific reduction** [S4:154–257]: construct a
   coefficient polynomial from a permanent of size proportional to $k$
   that has degree linear in $k$ and a smooth zero hypersurface in
   quadratically many variables, turning the product $(r-1)(d-1)$ into
   a cubic in the permanent order.

The bound also applies to algebraic branching programs: computing the
permanent over $\mathbb C$ requires $\Omega(m^3)$ vertices and edges.

## Graduate summary

**Main theorem** ([S4:41–49], `thm:main`). "There exist absolute
constants $c>0$ and $m_0$ such that, for every integer $m\ge m_0$,
$\bar{dc}(\mathrm{per}_m)\ge c m^3$. One may take $c=1/(5\,529\,600e)$ and
$m_0=1408$" [S4:43–49]. The same numerical lower bound holds for exact
determinantal complexity [S4:52]. Over $\mathbb C$, computing $\mathrm{per}_m$
requires $\Omega(m^3)$ vertices and $\Omega(m^3)$ edges in an
affine-linear algebraic branching program, including coefficientwise
limits [S4:55–60].

**Proof strategy** ([S4:154–257]). The construction seeks an affine
restriction of a permanent of size proportional to $k$ that has degree
proportional to $k$ in quadratically many variables and has a smooth
projective zero set [S4:156–158]. With $D=\mathrm{diag}(\theta_1,\ldots,\theta_k)$
and $q=\lfloor(k-1)/3\rfloor$, the coefficient polynomial
$G_D(X)=[s^qt^q]\mathrm{per}_k(X+sI+tD)$ is homogeneous of degree
$r=k-2q$ in the $k^2$ entries of $X$, with $T=\binom{q+2}{2}$ quadratic
in $k$ [S4:160–168]. A linear subspace of dimension quadratic in the
auxiliary matrix size is identified on which the zero hypersurface is
smooth [S4:170–175]. The general polar-degree theorem then gives the
$(r-1)(d-1)$ bound, which at this scale is cubic.

## History of the conjecture

The early matrix-order lower bounds were linear in $m$: **von zur
Gathen** (Babai–Seress) [S4:68], **Meshulam** [S4:70], and **Cai**
[S4:71] all give the scale $\sqrt{2}\,m-O(1)$. **Mignon and Ressayre**
raised the exact bound to $m^2/2$ via Hessian rank comparison
[S4:74–77]; **Cai, Chen, and Li** extended this to positive
characteristic [S4:79]. **Grenet** gave the upper bound
$2^m-1$ via a subset-indexed branching program [S4:82–84].

For the border model, **Landsberg, Manivel, and Ressayre** proved
$\bar{dc}(\mathrm{per}_m)\ge m^2/2$ by studying hypersurfaces with degenerate
duals [S4:96–98]. **This paper raises the exponent from two to three**
in that same model [S4:99].

Geometric singularity methods: **Alper, Bogart, and Velasco** prove
$dc(f)\ge\mathrm{codim}\mathrm{Sing}(f)+1$ under a
codimension condition, which gives only a linear scale for the permanent
[S4:110–116]. The present construction instead finds a coefficient
polynomial from a permanent and a linear subspace on which its zero
hypersurface is smooth [S4:117–120].

For the general polar-degree theorem, the classical top polar degree
$r(r-1)^{d-2}$ is due to **Piene** [S4:139]. The kernel-equation and
Schur-complement reduction also appear in **Sheshadri**'s 2026 preprint
[S4:125–128]. **Kumar and Volk** use such kernel equations for a
quadratic exact lower bound for power sums [S4:129–132].

**Prior (my training data, not this repo).** The cubic lower bound for
the border determinantal complexity of the permanent was a major open
problem in geometric complexity theory. The quadratic $m^2/2$ bound of
Landsberg–Manivel–Ressayre (2010) was the state of the art for the
border model, and the Mulmuley–Sohoni program sought (via representation
theory) to establish superpolynomial bounds. A cubic polynomial bound is
a fixed improvement but does not resolve the superpolynomial question. I
cannot confirm these independently; the release ships the manuscript as
a proof.

## Consequences

- **Cubic border determinantal complexity.** The complex border
  determinantal complexity of the $m\times m$ permanent is
  $\Omega(m^3)$, for arbitrary affine-linear determinant representations
  and coefficientwise limits [S4:41–49].
- **Cubic exact determinantal complexity.** The same numerical lower
  bound holds for exact determinantal complexity [S4:52].
- **Cubic algebraic branching program complexity.** Computing
  $\mathrm{per}_m$ over $\mathbb C$ requires $\Omega(m^3)$ vertices and
  $\Omega(m^3)$ edges in affine-linear algebraic branching programs,
  including coefficientwise limits with fixed budget
  [S4:55–60].
- **The exponent improves from 2 to 3.** In the border model, the lower
  bound exponent increases from two (Landsberg–Manivel–Ressayre) to
  three, while the superpolynomial question remains open
  [S4:99].

## Section skeleton

The manuscript [S3] is a 98-line root that includes a `\tableofcontents`
[S3:86] and then nine section files under `build/source/sections/`
[S3:87–95]: `introduction` (257 lines), `models`, `selector`,
`adjugate`, `conductor`, `dimension`, `transfer`, `polar`,
`consequences`, followed by plain-style bibliography over
`references.bib` [S3:96–97]. The shipped PDF [S5] is the manuscript in
the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note [S6]
and two comparator stubs [S7] [S8], but **no `main_results` entry** and
**no formalized manuscript** in the yaml. The scope note covers the
manuscript; the comparator stubs state the target the release set
itself.

The scope note's first paragraph states: "The formalization proves a
cubic lower bound for both exact and border determinantal
representations of the complex $m\times m$ permanent. For
$m\ge1408$, every affine-linear determinant representation of size
$n$, including coefficientwise limits, satisfies
$n\ge m^3/(5529600e)$" [S6:9]. The second paragraph describes the
general supporting theorem: "A general supporting theorem applies to a
polynomial in $d\ge2$ variables whose first nonzero homogeneous Taylor
term has degree $r\ge2$ and no nonzero singular zero. Its exact and
border determinantal sizes are at least $(r-1)(d-1)/(4e)$. The
paper's algebraic-branching-program consequences are outside these
statements" [S6:11].

The `PermanentCubic.lean` stub [S7] (42 lines) defines `Variables`,
`Poly`, `permanentPolynomial`, `affineMatrixPolynomial`,
`HasBorderDeterminant` (coefficientwise limit of affine determinants),
and `HasExactDeterminant`. The theorem
`permanent_cubic_lower_bounds` at [S7:33–38] states the
$m^3/(5529600e)$ bound for both border and exact representations and
closes with `sorry` [S7:38].

The `SmoothInitialForm.lean` stub [S8] (56 lines) defines the same
`Poly`, `affineMatrixPolynomial`, `HasBorderDeterminant`,
`HasExactDeterminant`, and adds `affineSubstitution`. The theorem
`smooth_initial_form_lower_bound` at [S8:35–52] states the
$(r-1)(d-1)/(4e)$ bound for a polynomial whose first nonzero
homogeneous term has the stated smoothness condition, and closes with
`sorry` [S8:52].

The reading is of source text only — no `lake` or `lean` run elaborates
the stubs, so the claim here is that the statement types and the
`sorry` targets exist in the source, not that any proof is present.

## Coverage

The ledger row `fam=108` [S9] records: `tier=T2`, `paps=1`,
`paps_form=0`, `chal=2`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. There is **no formalized manuscript** in the yaml `sources:`
and **no `main_results` entry** — the scope note links the two
comparator configs, but neither carries a `main_results` entry, so the
formalization chain is *absent*, not unformalized. The shape flag is
`bound`; `resolves_named=0` — the blurb names no conjecture with a
resolve verb.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:2679], manuscript link [S1:2686] and abstract [S1:2688] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 108 at [S2:294] |
| S3 | [`preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/source/main.tex`](../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/source/main.tex) | 98 | root (`\documentclass`); abstract [S3:78–85]; `\tableofcontents` [S3:86]; nine `\input` directives [S3:87–95]; 98 lines |
| S4 | [`preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/source/sections/introduction.tex`](../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/source/sections/introduction.tex) | 257 | `thm:main` [S4:41–49]; context [S4:66–152]; proof strategy [S4:154–257]; 257 lines |
| S5 | [`preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf`](../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf) | 15687 | the manuscript as shipped |
| S6 | [`lean/docs/108.md`](../../lean/docs/108.md) | 18 | scope note — the Scope at [S6:9], supporting theorem at [S6:11], two comparator links at [S6:17–18] |
| S7 | [`lean/ComparatorChallenges/PermanentCubic.lean`](../../lean/ComparatorChallenges/PermanentCubic.lean) | 42 | the comparator stub — `permanent_cubic_lower_bounds` at [S7:33–38] |
| S8 | [`lean/ComparatorChallenges/SmoothInitialForm.lean`](../../lean/ComparatorChallenges/SmoothInitialForm.lean) | 56 | the comparator stub — `smooth_initial_form_lower_bound` at [S8:35–52] |
| S9 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=108`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
