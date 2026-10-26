[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 139](../index/theoretical-computer-science/139-subpolynomial-queries-for-log-concave-sampling.md)

# 139 — Subpolynomial queries for log-concave sampling

[Index page](../index/theoretical-computer-science/139-subpolynomial-queries-for-log-concave-sampling.md)

## Original CONTENTS.md summary

[S1:3334] (family entry):

> **139. Subpolynomial query complexity for log-concave sampling.** For C2 potentials with a supplied minimizer and $`I\preceq\nabla^2V\preceq2I`$, proves that sampling within total variation 1/10 requires only $`C_\varepsilon d^\varepsilon`$ exact value-and-gradient queries for every fixed ε > 0. The bound holds on every run, with unrestricted computation between queries. A logarithmic lower bound also holds, so the optimal power-law exponent in this oracle model is zero. ([Lean](lean/docs/139.md))

[S2:355] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Log-concave sampling**: given a potential $V:\mathbb R^d\to\mathbb R$ whose
Hessian satisfies $I\preceq\nabla^2 V\preceq 2I$ (so the density
$e^{-V}$ is log-concave and well-conditioned), draw a sample from the
Gibbs law $\pi_V\propto e^{-V}\,dx$.

The standard approach is to discretize Langevin or Hamiltonian dynamics
and step through the resulting ODE. In $d$ dimensions, those
discretizations need a number of gradient evaluations that grows as a
*positive power* of $d$ — typically $d^{1/6}$, $d^{1/4}$, or $d^{1/3}$
depending on the method and the accuracy metric.

This family asks: **is any positive power of $d$ actually
necessary?** In the exact first-order oracle model — where a query
returns $(V(x),\nabla V(x))$ and computation between queries is
unrestricted — the answer is **no**. The optimal dimension exponent is
**zero**: for every $\varepsilon>0$, $C_\varepsilon d^\varepsilon$
queries suffice [S4:51–65]. A matching $\Omega(\log d)$ lower bound
shows the exponent cannot be driven below zero.

## Graduate summary

**Main theorem** ([S4:51–65], `thm:main`). "In the oracle model above,
for every $\varepsilon>0$ there is $C_\varepsilon<\infty$ such that
$Q(d)\le C_\varepsilon d^\varepsilon$ $(d\ge2)$. There are also
absolute constants $c>0$ and $d_0$ such that $Q(d)\ge c\log d$
$(d\ge d_0)$. The lower bound applies to arbitrary randomized adaptive
first-order algorithms. In particular, $\gamma_*=0$" [S4:51–65].

**The model.** The potential class $\mathcal V_d$ consists of
$C^2$ functions with $V(0)=0$, $\nabla V(0)=0$, and
$I_d\preceq\nabla^2 V(x)\preceq 2I_d$ for all $x$ [S4:20–26]. A query
at $x$ returns the exact pair $(V(x),\nabla V(x))$; queries are
adaptive; computation between queries is unrestricted (no arithmetic
or bit-complexity bound) [S4:32–36]. The budget $Q(d)$ is the smallest
integer such that an algorithm makes at most $q$ queries on *every*
execution and returns $X$ with
$\|\mathcal L(X)-\pi_V\|_{\mathrm{TV}}\le 1/10$ for all
$V\in\mathcal V_d$ [S4:39–45]. The optimal dimension exponent is
$\gamma_*=\limsup_{d\to\infty}\frac{\log Q(d)}{\log d}$ [S4:47–49].

**The upper bound is worst-case.** The $C_\varepsilon d^\varepsilon$
bound holds on every execution, not in expectation. The constants and
the algorithmic approximation orders may depend on $\varepsilon$; no
polylogarithmic query count is asserted [S4:68–74].

**The lower bound is for all algorithms.** The $\Omega(\log d)$ lower
bound applies to arbitrary randomized adaptive first-order algorithms,
so it is not an artifact of a particular construction [S4:63–65].

## History of the conjecture

Log-concave sampling via Langevin or Hamiltonian dynamics is a central
tool in modern probability and optimization. The nonasymptotic
analysis of the unadjusted Langevin algorithm was developed by
**Dalalyan** (2017) and **Durmus et al.** (2017); **Chen et al.**
(2018) analyzed the underdamped method under strong convexity and
smoothness [S4:81–84].

The best prior dimension exponents in this fixed-conditioning,
fixed-accuracy regime were:
- **$\tilde O(d^{1/3})$** — shifted-composition analysis of
  **Altschuler et al.** (2026) and a gradient-only rejection-sampling
  route of **Chen** (2026) [S4:82–86].
- **$\tilde O(d^{1/6})$** — expected-gradient-query bound of
  **Chen** (2026, Theorem 7.1(i)) at fixed relative-entropy accuracy;
  Pinsker's inequality transfers the exponent to TV accuracy
  [S4:96–103].

The construction here uses approximation orders that can depend on the
desired exponent $\varepsilon$ and aims at oracle complexity rather
than practical running time [S4:12–15]. The result determines the
*exponent* to be zero but not the finer growth rate of $Q(d)$: the
upper bound does not assert a polylogarithmic query count
[S4:68–74].

**Prior (my training data, not this repo).** Log-concave sampling and
the $d^{1/6}$-to-$d^{1/3}$ dimension dependence of Langevin/HMC
discretizations are well-established. The claim that the optimal
dimension exponent is *zero* in the exact first-order oracle model with
unrestricted computation is the load-bearing result of the release;
I cannot confirm it as a prior result in my training data, and the
release ships the manuscript as proof.

## Consequences

- **The dimension exponent is zero.** For every $\varepsilon>0$,
  $C_\varepsilon d^\varepsilon$ exact first-order queries suffice for
  TV-accuracy $1/10$ on every execution
  [S4:51–65][S1:3334].
- **A logarithmic lower bound matches.** $Q(d)\ge c\log d$ eventually,
  for arbitrary randomized adaptive first-order algorithms, so the
  infimal polynomial exponent is exactly zero
  [S4:58–64][S1:3334].
- **The bound is worst-case, not expected.** The query budget is a
  deterministic cap on every execution; no averaging over random seeds
  is taken [S4:40–45].
- **The model is deliberately loose.** Computation between queries is
  unrestricted; no arithmetic or bit-complexity bound is imposed or
  deduced [S4:33–36][S6:9].
- **The result determines the exponent, not the rate.** The upper
  bound does not assert a polylogarithmic query count; the finer
  growth of $Q(d)$ between $\log d$ and $d^\varepsilon$ is left open
  [S4:68–74].

## Section skeleton

The manuscript [S3] is a 74-line root: preamble, title, abstract
[S3:47–56], and nine section files [S3:57–65] (under `build/sections/`).
The sections, in order and line count: `introduction` (269),
`preliminaries` (275), `jets` (317), `divergence`, `centering`,
`numerics`, `implementation`, `sampling` (435), `lower` (379). The
proof develops the high-order jet approximation machinery (jets,
divergence, centering), implements the sampler (implementation,
sampling), and proves the lower bound (lower). The shipped PDF [S5]
is the manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note
[S6:9], one comparator stub [S7:81–87], and **one** `main_results`
declaration — the formalization is **complete at the declaration
level**.

The scope note [S6:9] states the formalized result: "The formalized
result determines the dimension exponent of exact value-and-gradient
query complexity for well-conditioned log-concave sampling. For
potentials with $V(0)=0$, $\nabla V(0)=0$, and $I\le\nabla^2V\le2I$,
the least worst-case query budget achieving total-variation error at
most $1/10$ is at most $C_\varepsilon d^\varepsilon$ for every
$\varepsilon>0$, and at least $c\log d$ eventually. Hence the infimal
polynomial exponent is zero. Algorithms may be measurable, randomized,
and adaptive; arithmetic and bit costs are not bounded" [S6:9].

The scope note links a single comparator config
[`LogConcaveQuery.lean`] [S6:15]. That config carries one
`main_results` entry:

- `OAI.LogConcaveSampling.exact_source_main` in
  `OAI/Probability/LogConcave/Main.lean`.

The `LogConcaveQuery.lean` comparator stub [S7:81–87] (93 lines) defines the
oracle model — `Point`, `Reply`, `Transcript`, the `Admissible`
structure (the Hessian bounds), the Gibbs law
(`gibbsDensity`, `partition`, `gibbs`), the `OracleAlgorithm`
structure with its `history` and `run`, the `CanSample` predicate,
`queryComplexity`, `ExponentBound`, and `gammaStar` — and carries one
statement:

- `exact_source_main` [S7:81–87] — the conjunction of the upper bound
  ($\forall\varepsilon>0,\;\exists C,\;\forall d\ge2$:
  $Q(d)\le C\cdot d^\varepsilon$), the lower bound
  ($\exists c>0, d_0$: $Q(d)\ge c\log d$ for $d\ge d_0$), and
  $\gamma_* = 0$; `sorry` at [S7:87].

The comparator still carries its `sorry`, but the declaration
`OAI.LogConcaveSampling.exact_source_main` exists in the library's
`main_results` list, so the challenge is registered as a target the
release set itself with a named entry point. The reading is of source
text only — no `lake` or `lean` run elaborates the library, so the
claim here is that the statement and its `sorry` exist in the source,
not that the declaration is proved.

## Coverage

The ledger row `fam=139` [S8] records: `tier=T3`, `paps=1`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration
level**: the single `LogConcaveQuery.lean` comparator config carries
one `main_results` declaration,
`OAI.LogConcaveSampling.exact_source_main`. The manuscript is
formalized (`paps_form=1`). The shape flags are `bound|uniform`;
`resolves_named=0`; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3334], manuscript link [S1:3341] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 139 at [S2:355] |
| S3 | [`preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/main.tex`](../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/main.tex) | 74 | document root; abstract [S3:47–56]; nine section `\input` directives [S3:57–65]; 74 lines |
| S4 | [`preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/introduction.tex`](../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/introduction.tex) | 269 | `thm:main` [S4:51–65]; 269 lines |
| S5 | [`preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf`](../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf) | 20166 | the manuscript as shipped |
| S6 | [`lean/docs/139.md`](../../lean/docs/139.md) | 15 | scope note — Scope at [S6:9], comparator link at [S6:15] |
| S7 | [`lean/ComparatorChallenges/LogConcaveQuery.lean`](../../lean/ComparatorChallenges/LogConcaveQuery.lean) | 93 | comparator — `exact_source_main` [S7:81–87] `sorry` [S7:87]; 93 lines |
| S8 | [`notes/gen/tables/catalog.tsv`](../../notes/gen/tables/catalog.tsv) | 373 | the ledger row `fam=139`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
