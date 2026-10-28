[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 126](../index/theoretical-computer-science/126-exponential-semidefinite-complexity-of-perfect-matching.md)

# 126 — Exponential semidefinite complexity of perfect matching

[Index page](../index/theoretical-computer-science/126-exponential-semidefinite-complexity-of-perfect-matching.md)

## Original CONTENTS.md summary

[S1:3054] (family entry):

> **126. Exponential semidefinite complexity of perfect matching.** Proves that every exact semidefinite lift of the perfect matching polytope has exponential size, answering Rothvoss's polynomial-size lift question negatively. The bound holds even for the positive semidefinite rank of its odd-cut slack matrix after any fixed shift $`0\lt \rho\lt 1`$, allowing arbitrary real positive semidefinite factors. (Lean)

[S2:329] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Perfect matching** is a fundamental combinatorial object: a set of edges
in a graph that pairs up every vertex exactly once. The **perfect matching
polytope** is the convex hull of all perfect-matchings-as-point-vectors —
a geometric shape whose facets (faces) are described by the **odd-cut
inequalities**.

A **semidefinite lift** is a way to represent a polytope as a slice of the
cone of positive semidefinite matrices. The smaller the slice, the "simpler"
the polytope is from an optimization perspective.

**Rothvoss** asked: *does the perfect matching polytope have a
polynomial-size semidefinite lift?* If so, semidefinite programming would
give efficient algorithms for a family of problems currently handled only
by combinatorial methods.

This family answers: **no**. Every exact semidefinite lift has
**exponential** size [S4:37–44]. The proof shows that a certain matrix
associated with the polytope's odd-cut inequalities has exponential
positive semidefinite (PSD) rank, which forces every lift to be
exponentially large [S4:74–80].

## Graduate summary

**Main theorem** ([S4:37–44], `thm:main`). "There is a constant $c>0$ such
that, for every fixed $0<\rho<1$, there is $n_0=n_0(\rho)$ for which
$\mathrm{rank_{psd}} A_n(\rho)\ge2^{cn}$ for every even $n\ge n_0$" [S4:37–44]. Here
$A_n(\rho)$ is the matrix indexed by odd vertex sets $U$ and perfect
matchings $M$ of $K_n$, with entries $|M\cap\delta(U)|-1+\rho$, where
$\delta(U)$ is the edge cut of $U$. The rate $c$ is independent of
$\rho$, though the threshold $n_0$ may deteriorate as $\rho$ tends to one
[S4:51–53].

**Corollary (exact lifts)** ([S4:74–80], `cor:exact-lift`). "There are
constants $c_0>0$ and $n_1$ such that, for every even $n\ge n_1$, both
$A_n(0)$ and $T_n(0)$ have real PSD rank at least $2^{c_0n}$, and every
exact semidefinite lift of $P_n$ has size at least $2^{c_0n}$"
[S4:74–80]. The argument appends scalar blocks to reduce the shifted case
to the unshifted, and invokes the cone-factorization theorem to identify
the PSD rank of the slack matrix with the minimum lift size
[S4:81–100].

**Endpoint remark.** The endpoint $\rho=1$ has a factorization of size
$\binom n2$ (diagonal matrices indexed by edges), so it cannot be included
in the exponential lower bound [S4:46–50].

## History of the conjecture

The problem is framed by **Rothvoss's** question about polynomial-size
semidefinite lifts of the perfect matching polytope. The polytope was
characterized by **Edmonds** in the 1960s using nonnegativity and odd-cut
inequalities [S4:94–96]. The PSD-rank lower bound technique builds on
**Forster's** cone-factorization theorem, which identifies the minimum
lift size with the PSD rank of an associated slack matrix.

The proof method combines several smoothing techniques: **local averaging**
over vertex sets, a **splitting** argument for the parity structure,
**Fourier smoothing** of matrix squares, and a **matching-specific
smoothing** that exploits the structure of perfect matchings in $K_n$.

**Prior (my training data, not this repo).** Rothvoss's question about
polynomial-size lifts of the perfect matching polytope was a prominent open
problem at the intersection of combinatorial optimization and convex
algebraic geometry. An exponential lower bound is a significant negative
result: it rules out semidefinite programming as a general-purpose tool
for the perfect matching polytope. I cannot confirm the specific prior
results independently; the release ships the manuscript as proof.

## Consequences

- **Rothvoss's question is answered negatively.** Every exact semidefinite
  lift of the perfect matching polytope $P_n$ has exponential size
  [S4:74–80].
- **The odd-cut slack matrix has exponential PSD rank.** For every fixed
  shift $0<\rho<1$, the matrix $A_n(\rho)$ has PSD rank
  $2^{\Omega(n)}$ [S4:37–44].
- **The bound is for the unshifted case as well.** The corollary extends
  the exponential rank to $A_n(0)$ and $T_n(0)$, the slack matrices of
  Edmonds's description [S4:74–80].
- **The endpoint $\rho=1$ is excluded.** A factorization of size
  $\binom n2$ exists at the endpoint, so the exponential bound requires
  $\rho<1$ [S4:46–50].
- **The formalization records only superpolynomial bounds.** The
  comparator stubs capture $n^C$ growth, not the paper's $2^{cn}$
  exponential rate [S6:9–11].

## Section skeleton

The manuscript [S3] is a 59-line root: a 30-line preamble, title block,
abstract [S3:42–47], seven section files [S3:49–57], `\appendix` with a
matching-smoothing section, and a `plain` bibliography [S3:58–59]. The
sections, in order and line count: `introduction` (231),
`local-averaging` (257), `splitting` (90), `fourier-smoothing` (342),
`parity` (284), `matching` (218), `matching-smoothing` (338) — 1,660
section lines. The shipped PDF [S5] is the manuscript in the form the
release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note [S6:9–11] and
**two** comparator stubs, but **no** `main_results` declaration. This is
a structural absence: the scope note links comparator configs, and neither
config has a proved declaration in `lean/OAI/`.

The scope note [S6:9–11] explicitly notes the gap between the paper's result
and the formalization: "The paper proves exponential PSD-rank lower bounds
for positively shifted matching matrices. The linked formalization records
the related superpolynomial lower bounds: for every fixed $C>0$, the PSD
rank of the selected perfect-matching slack matrix exceeds $n^C$ for all
sufficiently large even $n$. [...] These selected statements give
superpolynomial growth. They do not state the paper's exponential bound
for every fixed positive shift" [S6:9–11].

The scope note links **two** comparator configs [S6:17–18]:

- `MatchingAffineLift.lean` [S7] (35 lines) —
  `affine_lift_lower_bound` [S7:27–31]: for every $C>0$, every affine
  lift of the $n$-vertex matching polytope has matrix size
  $> n^C$ for all sufficiently large even $n$; `sorry` at [S7:31].
- `MatchingPSD.lean` [S8:46–48] (55 lines) — `MainClaim` [S8:46–48]: for every
  $C>0$, the PSD rank of the $n$-vertex matching slack matrix is
  $> n^C$ for all sufficiently large even $n$; `main` [S8:50–51],
  `sorry` at [S8:51].

There is no `OAI/**` declaration that proves either theorem, so the
formalization stops at the challenge stubs for both results.

The reading is of source text only — no `lake` or `lean` run elaborates
the library, so the claim here is that the stubs' statements and their
`sorry` exist in the source, not that anything is proved.

## Coverage

The ledger row `fam=126` [S9] records: `tier=T2`, `paps=1`,
`paps_form=0`, `chal=2`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **incomplete**: the scope note links
two comparator configs, but neither has a `main_results` entry or a proved
declaration — a T2 structural absence. The manuscript is unformalized
(`paps_form=0`). The shape flags are `bound|uniform`;
`resolves_named=0` — the result is a lower bound, not a resolution of a
named conjecture; `counterex_broad=1` — the negative answer to Rothvoss's
question has the shape of a counterexample to a polynomial-size lift
claim.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3054], manuscript link [S1:3054] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 126 at [S2:329] |
| S3 | [`preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/source/main.tex`](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/source/main.tex) | 59 | document root; abstract [S3:42–47]; seven `\input` directives [S3:49–57]; 59 lines |
| S4 | [`preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/source/sections/introduction.tex`](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/source/sections/introduction.tex) | 231 | `thm:main` [S4:37–44]; `cor:exact-lift` [S4:74–80]; 231 lines |
| S5 | [`preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf`](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf) | 13817 | the manuscript as shipped |
| S6 | [`lean/docs/126.md`](../../../lean/docs/126.md) | 18 | scope note — Scope at [S6:9–11], comparator links at [S6:17–18] |
| S7 | [`lean/ComparatorChallenges/MatchingAffineLift.lean`](../../../lean/ComparatorChallenges/MatchingAffineLift.lean) | 35 | comparator — `affine_lift_lower_bound` [S7:27–31]; 35 lines |
| S8 | [`lean/ComparatorChallenges/MatchingPSD.lean`](../../../lean/ComparatorChallenges/MatchingPSD.lean) | 55 | comparator — `MainClaim` [S8:46–48], `main` [S8:50–51]; 55 lines |
| S9 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=126`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
