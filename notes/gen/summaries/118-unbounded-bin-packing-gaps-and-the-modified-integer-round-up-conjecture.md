[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 118](../index/theoretical-computer-science/118-unbounded-bin-packing-gaps-and-the-modified-integer-round-up-conjecture.md)

# 118 — Unbounded bin-packing gaps and the modified integer round-up conjecture

[Index page](../index/theoretical-computer-science/118-unbounded-bin-packing-gaps-and-the-modified-integer-round-up-conjecture.md)

## Original CONTENTS.md summary

[S1:2906] (family entry):

> **118. Bin packing and unbounded configuration-LP gaps.** Disproves the modified integer round-up conjecture of Scheithauer and Terno: the integral bin-packing optimum can exceed its configuration linear-programming value by an arbitrarily large additive constant. Approximating the optimum within any fixed additive constant is also NP-hard, even when every item exceeds 1/6 and each bin holds at most five items. ([Lean](../../../lean/docs/118.md))

[S2:314] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Bin packing** is the classic problem of fitting items into identical
bins of unit capacity. You have a list of item sizes (all in $(0,1]$)
and want to pack them into the fewest bins, where each bin's total load
is at most one. Writing $\mathrm{OPT}$ for the minimum number of bins, the
**configuration LP** is a fractional relaxation: it assigns weights to
all feasible bin "patterns" (sub-multisets of items that fit in one
bin) and minimizes total weight while covering every item's demand.
The LP value is always a lower bound on $\mathrm{OPT}$.

The **Modified Integer Round-Up Conjecture** (Scheithauer and Terno,
1995) asked whether $\mathrm{OPT} \le \lceil \text{LP} \rceil + 1$ always holds:
the integral optimum is at most the LP value, rounded up, plus one.
This family **disproves** that conjecture. For every integer $c \ge 0$,
there is a rational instance where the LP value is exactly $B$ but the
integral optimum exceeds $B + c$ [S4:87–95]. The gap is unbounded.

The construction also settles an algorithmic question: for any fixed
$c$, it is NP-hard to tell whether an instance fits in $B$ bins or
requires more than $B+c$ bins [S4:106–112]. A deterministic polynomial-
time algorithm with a fixed additive constant exists **if and only if**
$P = NP$ [S4:114–117]. All items exceed $1/6$, so each bin holds at
most five items.

## Graduate summary

**Main theorem (unbounded gap)** ([S4:87–95], `thm:unbounded-gap`).
"For every integer $c\ge0$, there is a finite rational bin-packing
instance $I$ and an integer $B$ such that every item size exceeds $1/6$
and $\mathrm{OPT}_{\mathrm{LP}}(I)=B$, $\mathrm{OPT}(I)>B+c$. The equality for the fractional optimum
also holds for the configuration LP whose patterns are subsets of the
individual item copies" [S4:87–95]. The gap is between the restricted
numerical-type LP and the integral optimum, and the same equality holds
for the stronger individual-copy formulation, so both configuration
relaxations are simultaneously defeated.

**Main theorem (additive hardness)** ([S4:106–112], `thm:additive-
hardness`). "For every fixed integer $c\ge0$, it is NP-hard to
distinguish pairs $(I,B)$ such that $I$ packs into $B$ bins from pairs
such that $I$ cannot be packed into $B+c$ bins" [S4:106–112]. The
instance is an explicit rational list; every item size is strictly
greater than $1/6$.

**Corollary (complexity equivalence)** ([S4:114–117], `cor:complexity-
equiv`). "A deterministic polynomial-time algorithm that always uses at
most $\mathrm{OPT}(I)+C$ bins for some absolute constant $C$ exists if and only
if $P=NP$" [S4:114–117]. The forward direction reduces from the
additive-hardness gaps; the reverse direction uses $P=NP$ to solve
bin feasibility exactly by binary search over the bin count.

**Construction sketch** ([S4:181–276]). The proof reduces from
vertex cover. A graph with $n$ vertices and a cover target $k$ produces
$5B$ rational items with five roles per bin (row, anchor, global
auxiliary, local auxiliary, flag). Two finite rooted trees with
competing depth quotas [S4:185–191] force each vertex to fund one of
two sides; the funded side determines the extracted cover. The
fractional witness uses the four-vertex clique with weight $1/2$ on
each local state [S4:265–270].

**No computational claim for the gap instances.** The unbounded-gap
instances have no stated polynomial-size bound; the integers $P_0$ and
$K$ in the reduction grow rapidly in $c$ and $\rho$ [S5:31–35]. The
hardness result is what places the instances in polynomial encoding
[S4:270–274].

## History of the conjecture

The **configuration LP** and its cutting-stock antecedents go back to
**Gilmore and Gomory** (1961) [S4:12–13]. **Marcotte** (1985, 1986)
exhibited the first instance where the integral round-up property
fails [S4:62–63]. **Scheithauer and Terno** (1995, 1997) conjectured
the modified bound $\mathrm{OPT} \le \lceil \mathrm{OPT}_{\mathrm{LP}} \rceil + 1$ [S4:64–65].

On the algorithmic side, **Fernandez de la Vega and Lueker** (1981)
gave an asymptotic approximation scheme [S4:128–130]. **Karmarkar and
Karp** (1982) obtained an additive bound of order $\log^2 \mathrm{OPT}$ [S4:134–137].
**Rothvoss** (2013) improved this to $\log \mathrm{OPT} \cdot \log\log \mathrm{OPT}$
[S4:138–140]. **Hoberg and Rothvoss** (2017) reached order $\log \mathrm{OPT}$
[S4:141–143]. These logarithmic upper bounds are compatible with the
unbounded additive gap: the constructed instances can grow very rapidly
with the prescribed gap.

Earlier counterexamples by **Caprara, Dell'Amico, Díaz-Díaz, Iori, and
Rizzi** (2015) encoded edge-coloring obstructions to violate the
integer round-up property, but did not establish unbounded additive
gaps [S4:134–136]. **Newman, Neiman, and Nikolov**, and **Eisenbrand,
Pálvölgyi, and Rothvoss** proved logarithmic obstructions for
algorithms restricted to rounding a supplied fractional support [S4:137–139].

The constant-additive question for bin packing was listed among the
open problems in **Williamson and Shmoys** (2011) [S4:5–7].

**Prior (my training data, not this repo).** The Modified Integer
Round-Up Conjecture was a well-known open problem in combinatorial
optimization; its disproof is a significant negative result. The
$P=NP$ equivalence for fixed-additive approximation is a clean
complexity-theoretic corollary. I cannot confirm these independently;
the release ships the manuscript as a proof.

## Consequences

- **Modified Integer Round-Up Conjecture is false.** For every $c\ge0$,
  there is a rational instance with $\mathrm{OPT}_{\mathrm{LP}}(I) = B$ and $\mathrm{OPT}(I) > B+c$,
  so the conjectured $\lceil \mathrm{OPT}_{\mathrm{LP}} \rceil + 1$ bound fails by an
  arbitrarily large additive constant [S4:87–95].
- **No fixed-additive approximation in $P$.** A deterministic
  polynomial-time algorithm with a fixed absolute additive constant
  exists if and only if $P=NP$ [S4:114–117].
- **Constant gap for item sizes $> 1/6$.** Both results hold when
  every item exceeds $1/6$, so each bin contains at most five items
  [S4:91–92].
- **Both configuration formulations defeated.** The gap holds for
  both the numerical-type configuration LP and the stronger
  individual-copy formulation [S4:94–95].

## Section skeleton

The manuscript [S3] is a 27-line root that imports its preamble from
`preamble.tex` [S3:5] and then includes seven section files
[S3:17–24]: `introduction` (277 lines), `trees` (186 lines),
`instance` (547 lines), `completeness` (283 lines), `soundness`
(363 lines), `consequences` (114 lines), followed by `bibliography`
(152 lines) [S3:24]. The shipped PDF [S7] is the manuscript in the
form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S8],
one comparator stub [S9], and one `main_results` declaration [S10] over
the formalized manuscript. This is the strongest tier: the declaration is a
fully proved theorem in `lean/OAI/`.

The scope note states: "The formalized results rule out a universal
additive bound for the configuration linear program in bin packing.
For every integer $c\ge0$, there are an integer $B$ and a rational
instance with $5B$ items whose individual-copy and size-type
configuration-LP values both equal $B$, but whose integral optimum is
greater than $B+c$. Distinguishing a packing in $B$ bins from the
absence of one in $B+c$ bins is NP-hard for each fixed $c$. A
deterministic polynomial-time algorithm with a fixed absolute additive
allowance exists exactly when $P=NP$; under that equality, an optimal
algorithm is constructed" [S8:9].

The `BinPackingGap.lean` comparator stub [S9] (379 lines) defines the
full bin-packing theory: `Instance` [S9:66], `Packing`, `opt` [S9:82],
`IndividualConfiguration`, `NumericalSize`, and the NP-hardness and
$P=NP$ machinery. The `main_results` statement at [S9:370–378] states
all four components as a conjunction, and `theorem main` at
[S9:378] closes with `sorry`.

The formalized declaration `OAI.BinPackingGap.main_results` in
`Main.lean` [S10] (28 lines) is the **proved** version. At
[S10:7–28] the theorem conjoins four results: the structural additive
gap, the packing-gap NP-hardness, the $P=NP$ equivalence for absolute
additive algorithms, and the constructive algorithm under $P=NP$.
The proof is a single `refine` that instantiates four named lemmas
from the `OAI.Computability.BinPacking.Results.Aggregate` module.
There is no `sorry` in this file.

The reading is of source text only — no `lake` or `lean` run elaborates
the library, so the claim here is that the declaration and its proof
terms exist in the source, not that the library elaborates.

## Coverage

The ledger row `fam=118` [S11] records: `tier=T3`, `paps=1`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is complete: the scope note links
the comparator config, and the `main_results` entry names a fully
proved declaration. The shape flags are `resolution|counterexample|partial`;
`resolves_named=1` — the blurb names the Modified Integer Round-Up
Conjecture with a resolve verb; `counterex_broad=1`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2906], manuscript link [S1:2906] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 118 at [S2:314] |
| S3 | [`preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/main.tex`](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/main.tex) | 27 | document body; abstract [S3:9–16]; eight `\input` directives [S3:17–24]; 27 lines |
| S4 | [`preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/introduction.tex`](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/introduction.tex) | 276 | `thm:unbounded-gap` [S4:87–95]; `thm:additive-hardness` [S4:106–112]; `cor:complexity-equiv` [S4:114–117]; history [S4:3–85]; construction overview [S4:181–276]; 277 lines |
| S5 | [`preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/instance.tex`](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/instance.tex) | 547 | `thm:reduction` [S5:4–15]; 547 lines |
| S6 | [`preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/consequences.tex`](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/consequences.tex) | 114 | `thm:unbounded-gap` proof [S6:11–23]; `thm:additive-hardness` proof [S6:58–68]; `cor:complexity-equiv` proof [S6:70–87]; 114 lines |
| S7 | [`preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf`](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf) | 13408 | the manuscript as shipped |
| S8 | [`lean/docs/118.md`](../../../lean/docs/118.md) | 15 | scope note — Scope at [S8:9], comparator link at [S8:14] |
| S9 | [`lean/ComparatorChallenges/BinPackingGap.lean`](../../../lean/ComparatorChallenges/BinPackingGap.lean) | 378 | the comparator — `Instance` [S9:66], `opt` [S9:82], `main_results` statement and `sorry` at [S9:370–378]; 379 lines |
| S10 | [`lean/OAI/Computability/BinPacking/Main.lean`](../../../lean/OAI/Computability/BinPacking/Main.lean) | 34 | the formalized declaration — `main_results` theorem, fully proved, at [S10:7–28]; 28 lines |
| S11 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=118`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
