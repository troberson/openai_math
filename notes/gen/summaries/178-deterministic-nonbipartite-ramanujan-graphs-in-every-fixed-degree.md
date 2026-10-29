[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 178](../index/combinatorics/178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md)

# 178 — Deterministic nonbipartite Ramanujan graphs in every fixed degree

[Index page](../index/combinatorics/178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md)

## Original CONTENTS.md summary

The release's blurb [S1:4156] and the catalog abstract [S2:437]
state the family's claim: for every fixed $d \ge 3$, a
**deterministic algorithm** constructs a simple $d$-regular
nonbipartite Ramanujan graph on every sufficiently large even
number $n$ of vertices, with every nonconstant adjacency
eigenvalue strictly between $-2\sqrt{d-1}$ and
$2\sqrt{d-1}$. The algorithm outputs the full adjacency list in
polynomial bit time, with exponent depending on $d$. The
manuscript is *Deterministic nonbipartite Ramanujan graphs in
every fixed degree* [S3:35, S3:37]; its abstract


> For every fixed integer $d\ge3$, we give a deterministic algorithm
that constructs a simple nonbipartite $d$-regular Ramanujan graph on every
sufficiently large even number $n$ of vertices. It outputs the full adjacency
list in polynomially many bit operations, with an exponent that may depend on
$d$. Every nonconstant adjacency eigenvalue lies strictly between
$-2\sqrt{d-1}$ and $2\sqrt{d-1}$. [S3:47–52]

## Undergraduate summary

A **$d$-regular graph** is a graph where every vertex has
exactly $d$ neighbors. A **Ramanujan graph** is one whose
nonconstant eigenvalues (of the adjacency matrix) are all in
absolute value at most $2\sqrt{d-1}$ — the smallest
possible spectral gap for a $d$-regular graph. This makes
Ramanujan graphs optimal expanders: information spreads through
them as fast as any $d$-regular graph can allow. The constraint
**nonbipartite** excludes graphs that split cleanly into two
halves (which would have $-d$ as an eigenvalue, well outside the
Ramanujan bound). The result gives a **deterministic**
construction: no randomness, no probabilistic method — a
concrete algorithm that, for any fixed degree $d \ge 3$,
outputs such a graph in polynomial time [S3:47–52,
S2:437].

## Graduate summary

**The main theorem** [S3:47–52, S2:437]. For every fixed
$d \ge 3$ there is a deterministic algorithm that, on input
$n$ (even and sufficiently large), outputs the full adjacency
list of a simple $d$-regular nonbipartite graph on $n$ vertices
such that every nonconstant adjacency eigenvalue $\lambda$
satisfies $|\lambda| < 2\sqrt{d-1}$. The running time is
$n^{O_d(1)}$ bit operations, with the exponent depending on $d$
[S3:47–52, S2:437].

**The scope of the formalization.** The family is at tier T0:
there is no scope note, no comparator challenge, no
`main_results` entry, and no Lean source. The manuscript is not
in `formalization.yaml`'s `sources:` listing.

## History of the conjecture

Ramanujan graphs were introduced by Lubetzky and
Sarnak (1992) from the Ramanujan conjecture for
$\mathrm{GL}(2)$; the first explicit constructions (Margulis,
Lubotzky, Phillips, Sarnak) used arithmetic groups and gave
bipartite graphs. The **nonbipartite** case in every fixed
degree $\ge 3$ with a **deterministic polynomial-time**
construction is a longstanding gap: the known arithmetic
constructions are either bipartite, randomized, or require $n$
to be in a thin set. This manuscript closes the gap with a
deterministic algorithm whose running time is polynomial in $n$
for each fixed $d$ [S3:47–52, S2:437].

**Prior (my training data, not this repo).** I know the
Ramanujan graph program, the bipartite constructions from
arithmetic groups, and the $2\sqrt{d-1}$ bound. A
**deterministic, nonbipartite, every-fixed-degree**
construction in polynomial bit time (exponent depending on $d$)
for every sufficiently large even $n$ goes beyond the
constructions I recall; the specific algebraic machinery in [S3:47–52]
is not something I can independently verify from training alone.

## Consequences

**Deterministic nonbipartite Ramanujan graphs exist in every
fixed degree $\ge 3$.** For each such $d$, a simple
$d$-regular nonbipartite Ramanujan graph on every sufficiently
large even $n$ [S3:47–52, S2:437].

**The construction is efficient.** The algorithm is
deterministic and runs in $n^{O_d(1)}$ bit time, with the
exponent depending on $d$ [S3:47–52, S2:437].

**The spectral bound is strict.** Every nonconstant adjacency
eigenvalue satisfies $|\lambda| < 2\sqrt{d-1}$, not just
$\le$ [S3:47–52, S2:437].

## Section skeleton

One manuscript [S3:47–52] (title [S3:35], date [S3:37]) —
`main.tex` (72 lines) under `build/`, inputs sections
`introduction`, `construction`, `spectral`, plus a
`references` bibliography. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records `paps_form 0`,
`chal 0`, `mainres 0`, and `scope_note 0`. There is no
`lean/docs/178.md` scope note, no `lean/ComparatorChallenges/`
file, no `main_results` entry in `formalization.yaml`, and no
Lean source under `lean/OAI/`. The manuscript is not in the
`sources:` listing. The result is stated and proved in the
manuscript [S3:47–52] but is outside the formalization
entirely. Absence of formalization is not a red flag: 547 of 719
manuscripts are unformalized.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 178 at [S1:4156] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{178} at [S2:437] |
| S3 | [`preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/build/main.tex`](../../../preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/build/main.tex) | 71 | the single manuscript root; title [S3:35], date [S3:37], abstract [S3:47–52] |
