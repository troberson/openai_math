[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 117](../index/theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md)

# 117 — Uniform sparsest cut: hardness and semidefinite gaps

[Index page](../index/theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md)

## Original CONTENTS.md summary

[S1:2881] (family entry):

> **117. Uniform sparsest cut: hardness and semidefinite gaps.** Proves that approximating Uniform Sparsest Cut within any fixed constant factor is NP-hard, even with nonnegative rational capacities and unit demands. The Goemans–Linial semidefinite relaxation also has integrality gaps of order at least $`\sqrt{\log n}/(\log\log n)^3`$, approaching the square-root-logarithmic upper bound. ([Lean](../../lean/docs/117.md))

[S1:2888] (the hardness manuscript entry, with its abstract at [S1:2890]):

> [Constant-factor hardness of uniform sparsest cut](../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf)

> We prove that, for every fixed C > 1, approximating Uniform Sparsest Cut within factor C is NP-hard. The output graphs have nonnegative rational capacities and unit demand between every pair of distinct vertices.

[S1:2897] (the gaps manuscript entry, with its abstract at [S1:2899]):

> [Near-square-root logarithmic integrality gaps for uniform sparsest cut](../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf)

> We construct uniform sparsest-cut instances whose Goemans–Linial semidefinite integrality gap is at least $`c\sqrt{\log n}/(\log\log n)^3`$ along a sequence $`n\to\infty`$. The demand is one between every pair of distinct vertices, and the capacities are nonnegative real numbers. This matches the Arora–Rao–Vazirani upper bound up to a power of $`\log\log n`$.

[S2:312] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Sparsest cut** asks: given a network of pipes with capacities, find the
partition of the vertices into two groups that separates the least total
capacity relative to the number of pairs it splits. When every pair of
vertices demands exactly one unit, the denominator is simply $|S|(N-|S|)$,
the size of the smaller group times the size of the larger group.

The family has two papers, addressing two different questions about
this uniform-demand variant:

1. **Hardness** [S4:14–31]: for every fixed $C > 1$, no polynomial-time
   algorithm can approximate Uniform Sparsest Cut within factor $C$.
   The reduction is from 3CNF-SAT and uses no complexity hypothesis
   beyond P $\neq$ NP. The output is a finite undirected graph with
   nonnegative rational capacities and unit demand on every pair.

2. **Integrality gaps** [S5:152–161]: the Goemans–Linial semidefinite
   relaxation (the natural LP relaxation that powers the best known
   approximation algorithm) has instances where the gap between the
   integral optimum and the relaxation value is at least
   $c\sqrt{\log n}/(\log\log n)^3$ along a sequence. This nearly matches
   the Arora–Rao–Vazirani upper bound of $O(\sqrt{\log n})$, off by a
   power of the iterated logarithm.

The two results are complementary: the first says no efficient algorithm
can do better than a constant factor, and the second says the natural
relaxation is essentially as good as any semidefinite approach can be.

## Graduate summary

**Hardness** ([S4:14–31], `thm:main`). "For every fixed real constant
$C>1$, there is a polynomial-time reduction from $3$CNF satisfiability
to finite undirected graphs with nonnegative rational capacities and
exactly unit demands, together with a positive rational threshold $a$,
such that" [S4:16–19]: satisfiable implies $\Phi(G)\le a$,
unsatisfiable implies $\Phi(G)>Ca$ [S4:20–24]. "The graph size and the
bit lengths of all output numbers are polynomial in the formula size,
with constants and exponents allowed to depend on $C$. In particular,
approximating Uniform Sparsest Cut within any fixed factor $C>1$ is
NP-hard" [S4:25–31]. The reduction uses no unproved complexity
hypothesis [S4:34].

**Integrality gaps** ([S5:152–161], `thm:main`). "There are an absolute
constant $c>0$ and capacity instances $C^{(j)}$ on $n_j\to\infty$
vertices, with $\GL(C^{(j)})>0$, such that"
$\OPT(C^{(j)})/\GL(C^{(j)})\ge c\sqrt{\log n_j}/(\log\log n_j)^3$ "for
all sufficiently large $j$. The demand is one between every pair of
distinct vertices" [S5:153–161]. The capacities are nonnegative real
numbers; no regularity is assumed [S5:70–72].

**Proof strategy — hardness** ([S4:128–205]). The reduction has four
interfaces. A satisfying assignment supplies a low-cost cut; a cut with
small cost relative to its separated demand determines a satisfying
assignment [S4:128–131].

*Algebraic testing* [S4:133–153]: a linear-size list of evaluation
vectors on which a quadratic form vanishes only rarely, built from the
Garcia–Stichtenoth tower [S4:136–138]. Tests with bounded query
probabilities and a parity-query law with uniform marginals [S4:139–144].
A valuation decodes a satisfying assignment when approximately
calibrated and order-preserving [S4:147–153].

*Rare-event extraction* [S4:155–163]: conditioning a Boolean response to
a conjunction of independently sampled predicates on success produces a
density with nearly extremal entropy. A clipping argument forces the
density near two values, giving a single valuation [S4:158–163].

*Cut variance to rare event* [S4:165–177]: a candidate cut is a
$\{0,1\}$-valued function of scores. Small resampling cost forces the cut
color to retain a signal from at least one amplitude scale. Smoothed
comparison paths produce the successful conjunction response. Every error
is proportional to the cut variance [S4:175–177].

*Exact uniform demands* [S4:179–194]: grid rounding of scores to truth
tables, box subdivision for rational capacities and demand masses, key
replication for vertex counts, and heavy edges preventing small-ratio
cuts from separating copies [S4:183–194].

**Proof strategy — gaps** ([S5:198–283]). The construction has two tasks:
build a negative-type semimetric with large average distance, and force
every $\ell_1$ contraction to have small average distance [S5:199–201].

*Common parameter space* [S5:204–216]: $S$ rounded charts on the cube
$(-2,2)^m$, each partitioning into cells by hyperplanes. Directions are
fixed before choosing any contraction; every unit direction has small
projections in at least half the charts [S5:212–216].

*Large distances, small interface costs* [S5:219–233]: a common smooth
feature map gives squared distances approximating $c_*\sqrt m\,|\theta-\eta|$.
Gaussian-kernel repair (Schoenberg) fixes triangle inequalities with only
a logarithmic loss at interfaces [S5:224–233].

*Simultaneous constraints* [S5:235–255]: a contraction $F:V\to\ell_1^D$
induces functions $f_s$ on the cube. Small jumps across interfaces express
gradients as combinations of normals, with total budget $Cm(\log m)^2$.
The Maurey–Pisier Gaussian rotation method converts this into
$\mathbb E\|F(v_1(\theta))-F(v_1(\eta))\|_1\le C\sqrt m(\log m)^{5/2}$, uniform
in $D$ [S5:243–255].

*Uniform copies and capacities* [S5:257–283]: multiplicities approximate
the first-chart measure while keeping every vertex of $V$. Cut-cone
duality supplies capacities with unit demand. The gap conversion is
$m/(\sqrt m(\log m)^{5/2})$ with $\log n\asymp m\log m$, yielding the
power 3 on $\log\log n$ [S5:272–280].

## History of the conjecture

The flow–cut approach to sparsest cut was developed by **Leighton and
Rao**, who gave logarithmic approximation guarantees via multicommodity
flow [S4:47]. **Arora, Rao, and Vazirani** improved the approximation
factor to $O(\sqrt{\log N})$ using semidefinite programming [S4:48];
their treatment of the unweighted uniform objective appears in their
2009 paper [S4:49].

Exact hardness of finding sparsest cuts is due to **Matula and
Shahrokhi** [S4:52]. **Bonsma, Broersma, Patel, and Pyatkin** proved
NP-completeness for unweighted graphs with the cardinality-product
denominator [S4:53].

Previous approximation lower bounds for Uniform Sparsest Cut depend on
complexity assumptions: **Ambühl, Mastrolilli, and Svensson** showed a
PTAS would yield sub-exponential SAT [S4:56]. **Raghavendra, Steurer,
and Tulsiani** established arbitrarily large constant-factor gaps for
Balanced Separator under the Small-Set Expansion hypothesis [S4:58–59],
which by the standard recursive reduction yields Uniform Sparsest Cut
hardness [S4:62–81]. The nonuniform hardness under Unique Games is due
to **Chawla, Krauthgamer, Kumar, Rabani, and Sivakumar** [S4:85–89].

For the integrality gaps, **Devanur, Khot, Saket, and Vishnoi** obtained
an $\Omega(\log\log n)$ gap, refuting the uniform constant-gap
conjecture [S5:180]. **Kane and Meka** proved
$\exp(\Omega(\sqrt{\log\log n}))$ [S5:182]. For arbitrary demands,
**Khot and Vishnoi** disproved the Goemans–Linial Conjecture
[**Khot–Vishnoi**, S5:188], and **Naor and Young** obtained the sharp
$\Omega(\sqrt{\log n})$ lower bound [S5:193]. The geometric line is
**Cheeger, Kleiner, and Naor** (Heisenberg group) [S5:190]; they explain
explicitly that their bounded-doubling examples have constant average
distortion into a line, so their construction cannot yield a diverging
uniform gap [S5:194–195].

**Prior (my training data, not this repo).** The uniform-demand
integrality gap was a long-standing open problem after the
constant-gap conjecture was disproved for arbitrary demands. The
$\sqrt{\log n}$ rate for the uniform case was expected to be the right
order given the ARV upper bound, but no construction achieved it. The
unconditional constant-factor hardness was expected to be difficult
because the uniform denominator constrains the standard gap-amplification
reductions. I cannot confirm independently; the release ships both
manuscripts as proofs.

## Consequences

- **Unconditional NP-hardness of constant-factor approximation.**
  For every fixed $C>1$, approximating Uniform Sparsest Cut within
  factor $C$ is NP-hard, with no complexity hypothesis beyond P $\neq$ NP
  [S4:14–31].
- **Near-optimal integrality gap for the GL relaxation.** The
  Goemans–Linial SDP has integrality gaps of
  $\Omega(\sqrt{\log n}/(\log\log n)^3)$ for uniform demands, matching
  the ARV upper bound up to a power of $\log\log n$
  [S5:152–161].
- **No polynomial-time approximation below the constant barrier.**
  The hardness result rules out a PTAS for Uniform Sparsest Cut under
  P $\neq$ NP, unconditionally [S4:25–31].
- **The uniform case separates from the general case.** The general-demand
  $\Omega(\sqrt{\log n})$ gap of Naor–Young does not imply the uniform
  conclusion [S5:194–195].

## Section skeleton

The hardness manuscript [S3] is an 83-line root that includes a
`\tableofcontents` [S3:72] and then eight section files under
`build/source/sections/` [S3:73–80]: `00-introduction` (218 lines),
`01-pencil`, `02-bit-tests`, `03-events`, `04-entropy`, `05-scores`,
`06-paths`, `07-finite-graph`, followed by plain-style bibliography over
`references.bib` [S3:81–82]. The shipped PDF [S6] is the manuscript in
the form the release distributes.

The gaps manuscript [S5] is a 340-line single-file document with all
content in the root. It includes six section files [S5:327–332]:
`directions`, `kernel`, `repair`, `metric`, `contraction`, `reduction`,
plus an appendix `directions-proof` [S5:334–335], followed by plain-style
bibliography over `references.bib` [S5:338–339]. The shipped PDF [S7]
is the manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S8],
one comparator stub [S9], and one `main_results` entry. The scope note
covers the gaps manuscript only, not the hardness manuscript. The
`main_results` entry names `OAI.UniformSparsestCut.mainGap` in
`OAI/Combinatorics/SparsestCut/Main.lean`.

The scope note's single paragraph states: "The formalized result gives
integrality gaps for the Goemans–Linial relaxation of uniform sparsest
cut. Along a sequence of instance sizes $n\to\infty$, the ratio of the
integral optimum to the positive relaxation optimum is at least
$c\sqrt{\log n}/(\log\log n)^3$ for one absolute $c>0$. Every unordered
pair has unit demand, and the relaxation uses squared Euclidean
distances satisfying the triangle inequalities. The result is an
existential sequence, not a bound for every size or a computational
hardness theorem" [S8:9].

The `UniformSparsestCut.lean` stub [S9] (55 lines) defines the
`Capacity` structure (nonnegative, symmetric, zero diagonal), `pairSum`,
`cutRatio`, `OPT` (infimum over all nontrivial cuts), `NegativeType`
(Hilbert-space representation plus triangle inequalities), `Feasible`
(negative type with unit total mass), and `glValue` (infimum over
feasible negative-type semimetrics). The single theorem `mainGap` at
[S9:40–49] states the existential sequence with the
$c\sqrt{\log n}/(\log\log n)^3$ gap and closes with `sorry` [S9:49].

The reading is of source text only — no `lake` or `lean` run elaborates
the stub, so the claim here is that the statement type and the `sorry`
target exist in the source, not that any proof is present.

## Coverage

The ledger row `fam=117` [S10] records: `tier=T3`, `paps=2`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalized manuscript is the gaps paper (the only one in
the yaml `sources:`). The scope note covers the gaps manuscript only.
The `main_results` entry is `UniformSparsestCut.mainGap`. The hardness
manuscript is outside the scope note and the yaml. The shape flags are
`bound` and `uniform`; `resolves_named=0` — the blurb names no
conjecture with a resolve verb.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:2881], hardness link [S1:2888] and abstract [S1:2890], gaps link [S1:2897] and abstract [S1:2899] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 117 at [S2:312] |
| S3 | [`preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/build/source/main.tex`](../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/build/source/main.tex) | 83 | root (`\documentclass`); abstract [S3:69–71]; `\tableofcontents` [S3:72]; eight `\input` directives [S3:73–80]; 83 lines |
| S4 | [`preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/build/source/sections/00-introduction.tex`](../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/build/source/sections/00-introduction.tex) | 217 | `thm:main` [S4:14–31]; context [S4:34–112]; proof structure [S4:128–205] |
| S5 | [`preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/build/source/main.tex`](../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/build/source/main.tex) | 339 | root (`\documentclass`); abstract [S5:46–52]; `thm:main` [S5:152–161]; context [S5:163–195]; proof strategy [S5:198–283]; six section inputs [S5:327–332]; appendix [S5:334–335]; 340 lines |
| S6 | [`preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf`](../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf) | 22059 | the hardness manuscript as shipped |
| S7 | [`preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf`](../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf) | 14288 | the gaps manuscript as shipped |
| S8 | [`lean/docs/117.md`](../../lean/docs/117.md) | 15 | scope note — the Scope at [S8:9] and one comparator link at [S8:15] |
| S9 | [`lean/ComparatorChallenges/UniformSparsestCut.lean`](../../lean/ComparatorChallenges/UniformSparsestCut.lean) | 55 | the comparator stub — `mainGap` at [S9:40–49] |
| S10 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=117`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
