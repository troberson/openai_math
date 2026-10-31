[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 089](../index/convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md)

# 089 — Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs

[Index page](../index/convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md)

## Original CONTENTS.md summary

 carries the family entry:

> Resolves the planar and bounded-treewidth cases of the Gupta–Newman–Rabinovich–Sinclair conjecture. Shortest-path metrics of finite connected graphs with arbitrary positive edge lengths embed into real $`L_1`$ with universal distortion for planar graphs, and distortion depending only on treewidth for bounded-treewidth graphs. The corresponding multicommodity flow–cut gaps are uniformly bounded. [S1:254]

The entry links the two manuscripts as "Planar graph embeddings [S1:254]" and
"Bounded-treewidth embeddings [S1:254]" .

The first manuscript's title is `Planar Graph Metrics Embed into $`L_1`$ with Constant Distortion` [S2:1].

The README dates it September 23, 2026 [S2:13].

The second manuscript's title is `L1 Embeddings of Graphs of Bounded Treewidth` [S18:1].

The README dates it September 23, 2026 [S18:13].

## Undergraduate summary

An **$`L_1`$ metric** is a distance computed as a sum over coordinates — the
"taxicab" distance. A graph's shortest-path metric is the distance between
vertices measured along edges. The question is how faithfully an $`L_1`$
embedding can reproduce a graph's shortest-path distances.

The first manuscript settles the planar case. [S3:33–35] states the result:
"We prove that every finite connected planar graph with arbitrary positive
real edge lengths embeds into real $`L_1`$ with a universal distortion bound.
This resolves the planar embedding conjecture positively."

The second manuscript settles the bounded-treewidth case. [S20:2–6] states
it: "For every fixed treewidth bound, the shortest-path metrics of finite
connected graphs with arbitrary positive real edge lengths embed into real
$`L_1`$ with uniformly bounded distortion. This resolves the bounded-treewidth
case of the Gupta--Newman--Rabinovich--Sinclair conjecture positively."

The planar question is stated before the proof. [S4:9–11] gives it: "The
planar embedding conjecture asks whether one constant $`C`$ works for every
planar graph metric, independently of the number of vertices and the edge
lengths. We prove that it does."

The planar theorem's shape is a measure-space representation. [S4:14–17]
opens it: "There is a finite universal constant $`C\ge1`$ with the following
property. For every finite connected planar graph $`G=(V,E)`$ with strictly
positive real edge lengths, there exist a measure space $`(\Omega,\mathcal
F,\mu)`$ and a map" — the display gives the integral identity.

Treewidth measures how tree-like a graph is: a tree has treewidth 1, a
series-parallel graph has treewidth 2, and a graph with a tree decomposition
whose bags hold at most $`k`$ vertices has treewidth below $`k`$. The treewidth
theorem is quantified by that bound. [S20:28–31] opens it: "For every integer
$`k\ge2`$ there is a finite constant $`C_k\ge1`$ with the following property. If
a finite connected graph $`G=(V,E)`$ admits a tree decomposition with bags of
size at most $`k`$, then, for every edge-length function $`\ell:E\to(0,\infty)`$,
there is a map $`F`$ from $`V`$ into a real" — the display gives the distortion
bound.

[S20:39–40] names what the constant does not depend on: "The constant is
independent of the number of vertices, the depth of the decomposition, and
all ratios of edge lengths."

The two results settle two cases of the same conjecture. [S4:24–26] names
the first: "This proves the planar case of the conjecture of Gupta, Newman,
Rabinovich, and Sinclair, which predicts uniformly bounded $`L_1`$ distortion
in every proper minor-closed family."

The second manuscript names its case and its reach. [S20:45–51] says: "The
bounded-treewidth family is one of the cases of the conjecture of Gupta,
Newman, Rabinovich, and Sinclair, which predicts a uniform $`L_1`$ distortion
bound for every proper minor-closed graph family. By the
excluded-planar-minor theorem of Robertson and Seymour, our result also gives
a uniform bound for graphs excluding any fixed planar graph as a minor."

## Graduate summary

The first manuscript's route is a cut representation. [S4:42–45] explains the
target: "Conversely, threshold sweeps through real coordinates give such a
representation for every $`L_1`$ metric on a finite set. Thus we seek weighted
cuts that separate each pair in proportion to its graph distance while
charging each edge at most a constant times its length."

The machinery runs through threshold sets and local coordinates [S9:1],
scales and the local experiment [S10:1], ordered fields and separation on the
two arcs [S11:1], the main update and the packing bound for secondary seeds
[S12:1], the secondary update [S13:1], columns and thin bands [S14:1],
interpolation by single-source distance functions [S15:1], and preserving
charts and assembling the embedding [S16:1], with the figures at [S6:1],
[S7:1] and [S8:1].

The general bound before this result was logarithmic. [S4:66–67] records it:
"The general preceding bound for $`n`$-vertex planar metrics is $`O(\sqrt{\log
n})`$, due to Rao."

The obstacle is Euclidean. [S4:70–73] says: "Newman and Rabinovich showed
that even series-parallel metrics can require $`\Omega(\sqrt{\log n})`$
distortion into Euclidean space. Thus a constant planar $`L_1`$ bound requires
a different route."

The first manuscript states a consequence beyond the embedding. [S4:58–62]
gives it: "Gupta et al. showed that its worst value on a fixed graph equals
the worst $`L_1`$ distortion over all weighted shortest-path metrics on that
graph~\cite[Section~3, Theorem~3.2]{GNRS04}. Hence Theorem~\ref{thm:main}
also gives a universal bound for the undirected fractional flow--cut gap on
planar graphs, with arbitrary demands."

For the unrestricted planar case, two extra mechanisms carry the proof.
[S4:112–117] names them: "For unrestricted planar metrics, two additional
mechanisms provide the needed control: component separation limits which
pairs need further updates, and interpolation makes local formulas agree
exactly at their interfaces."

The manuscript carries a section on consequences for almost-embeddable
families [S17:1].

The second manuscript's route is a direct cut construction on a tree
decomposition. [S20:103–104] states the choice: "We instead construct cut
measures directly on a tree decomposition, allowing arbitrary branching."

Its machinery runs through cut measures and transport along a decomposition
[S21:1], particles and reservations [S22:1], separating pairs in a common bag
[S23:1], the anchor construction [S24:1], uniform lower comparison [S25:1],
and completing the embedding [S26:1], with the figure at [S28:1].

The second manuscript names what the proof does not give. [S20:43–45] says:
"The proof gives the existence of $`C_k`$, without an explicit estimate for its
dependence on $`k`$."

For rational lengths the construction is algorithmic. [S20:125–128] states
it: "For positive rational edge lengths, these algorithms and Theorem 1 yield
embeddings of distortion at most $`(2+\varepsilon)C_k`$, for each fixed
$`\varepsilon>0`$, in fixed-parameter time with respect to $`k`$."

The scope note records what the formalization carries. [S29:10] gives the
planar result: "The planar case of the Gupta–Newman–Rabinovich–Sinclair
embedding problem asks for a universal distortion bound in $`L_1`$. The
formalized result gives one constant $`C`$ for every finite connected planar
graph with arbitrary positive real edge lengths: its weighted shortest-path
metric embeds into real $`L_1`$ with distortion at most $`C`$."

The scope note's second paragraph gives the treewidth result. [S29:12] says:
"The formalized result gives a uniform $`L_1`$ embedding bound for each
bounded-treewidth class. For every bag-size bound $`k\ge2`$, there is a
constant $`C(k)`$ such that the weighted shortest-path metric of every nonempty
finite connected graph with a tree decomposition of bag size at most $`k`$
embeds into finite-dimensional real $`L_1`$ with distortion at most $`C(k)`$."

The two declarations are the quantified forms.
`OAI.PlanarL1.planar_graph_metrics_embed_L1` at [S30:96] is the planar
theorem. `OAI.BoundedTreewidthL1.main_theorem` at [S31:135] is the
bounded-treewidth theorem.

The two comparator configs state the targets the release set itself, and each
is a stub. [S32:47] carries `sorry`; [S33:44] carries `sorry`. The scope
note's comparator table links `PlanarL1.lean` and `BoundedTreewidthL1.lean`,
one per formalized result.

## History of the conjecture

The Gupta--Newman--Rabinovich--Sinclair conjecture predicts a uniform $`L_1`$
distortion bound for every proper minor-closed graph family, cited in both
manuscripts at the lines that state it [S4:24–26] and [S20:45–51]. The first
manuscript's bibliography carries the entry [S5:1] and the second carries it
at [S27:1].

The treewidth-two case was settled before this result. [S20:85] records it:
"Gupta et al. proved the treewidth-two case. [S20:85]"

The exact value for treewidth two is known. [S20:86–88] gives it: "The
optimal distortion is $`2`$, by the upper bound of Chakrabarti, Jaffe, Lee, and
Vincent and the matching lower bound of Lee and Raghavendra."

The pathwidth case was settled by a probabilistic route. [S20:94–97] records
it: "Lee and Sidiropoulos established the bounded-pathwidth case through
stochastic embeddings into trees: each sampled tree metric dominates the graph
metric, while its expected expansion is bounded by a function of the
pathwidth."

`notes/data/conjecture-standing.tsv` carries no row for family 089, so the
prior on the conjecture's standing is not recorded in the release's own
reading. The claim in the entry is the record.

## Consequences

The planar case is settled with a universal constant, and the flow--cut
consequence follows from the identity Gupta et al. established [S4:58–62].
The bounded-treewidth case is settled with a constant that depends on the
width bound and not on the graph size [S29:12].

The two results share the conjecture and the cut-measure method, and the
second manuscript's excluded-planar-minor corollary reaches past planarity
[S20:45–51]. The family carries two comparator configs against two
manuscripts, one per formalized claim.

The constants are existential. [S20:43–45] states the limit for the treewidth
constant, and the scope note records the same shape for the formalized bound
[S29:12].

The release's own record is source-level. The scope note says the formalized
claims exist and names their declarations; the two comparator configs carry
`sorry`; no Lean run in this repository proves either elaborates.

**Tree measurement (source-level).**

The family registers 2 `main_results` declarations (`OAI.PlanarL1.planar_graph_metrics_embed_L1`; `OAI.BoundedTreewidthL1.main_theorem`); the primary file `OAI/Combinatorics/PlanarL1/Embedding.lean` carries 124 lines with top-level theorem `theorem planar_graph_metrics_embed_L1`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 63 files, 27 theorems, 664 defs.

The preprint states 59 theorem environments while the tree carries only 27 (0.46×), indicating a focused sub-formalization (source-level).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 861 | Family entry, line 254 |
| S2 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/README.md`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/README.md) | 20 | Manuscript 1 title, date, citation |
| S3 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/main.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/main.tex) | 51 | Abstract, lines 33–35 |
| S4 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/introduction.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/introduction.tex) | 239 | Conjecture, theorem, history, proof outline |
| S5 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/references.bib`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/references.bib) | 223 | Bibliography entries |
| S6 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/column-realization.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/column-realization.tex) | 49 | Column realization figure |
| S7 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/surviving-seeds.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/surviving-seeds.tex) | 67 | Surviving seeds figure |
| S8 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/two-portals.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/two-portals.tex) | 39 | Two portals figure |
| S9 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/sets.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/sets.tex) | 240 | Threshold sets and local coordinates |
| S10 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/scale-setup.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/scale-setup.tex) | 138 | Scales and the local experiment |
| S11 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/ordered.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/ordered.tex) | 406 | Ordered fields and separation on the two arcs |
| S12 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/main-packing.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/main-packing.tex) | 510 | The main update and a packing bound for secondary seeds |
| S13 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/secondary.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/secondary.tex) | 266 | The secondary update |
| S14 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/geometry.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/geometry.tex) | 452 | Columns and thin bands |
| S15 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/interpolation.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/interpolation.tex) | 454 | Interpolation by single-source distance functions |
| S16 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/assembly.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/assembly.tex) | 274 | Preserving charts and assembling the embedding |
| S17 | [`preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/consequences.tex`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/consequences.tex) | 75 | A consequence for almost-embeddable families |
| S18 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/README.md`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/README.md) | 20 | Manuscript 2 title, date, citation |
| S19 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/main.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/main.tex) | 63 | Document structure |
| S20 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/01-introduction.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/01-introduction.tex) | 265 | Abstract, theorem, history, proof outline |
| S21 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/02-cut-laws.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/02-cut-laws.tex) | 468 | Cut measures and transport along a decomposition |
| S22 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/03-particles.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/03-particles.tex) | 279 | Particles and reservations |
| S23 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/04-perturbations.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/04-perturbations.tex) | 219 | Separating pairs in a common bag |
| S24 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/05-anchors.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/05-anchors.tex) | 326 | The anchor construction |
| S25 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/06-lower-comparison.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/06-lower-comparison.tex) | 420 | Uniform lower comparison |
| S26 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/07-conclusion.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/07-conclusion.tex) | 36 | Completing the embedding |
| S27 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/bibliography.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/bibliography.tex) | 128 | Bibliography entries |
| S28 | [`preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/figures/anchor-reservations.tex`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/figures/anchor-reservations.tex) | 45 | Anchor reservations figure |
| S29 | [`lean/docs/089.md`](../../../lean/docs/089.md) | 19 | Scope note |
| S30 | [`lean/OAI/Combinatorics/PlanarL1/Embedding.lean`](../../../lean/OAI/Combinatorics/PlanarL1/Embedding.lean) | 124 | `PlanarL1.planar_graph_metrics_embed_L1` |
| S31 | [`lean/OAI/Combinatorics/TreewidthL1/Main.lean`](../../../lean/OAI/Combinatorics/TreewidthL1/Main.lean) | 188 | `BoundedTreewidthL1.main_theorem` |
| S32 | [`lean/ComparatorChallenges/PlanarL1.lean`](../../../lean/ComparatorChallenges/PlanarL1.lean) | 51 | Stub, `sorry` at line 47 |
| S33 | [`lean/ComparatorChallenges/BoundedTreewidthL1.lean`](../../../lean/ComparatorChallenges/BoundedTreewidthL1.lean) | 50 | Stub, `sorry` at line 44 |

## Bibliography

- Yonatan Aumann and Yuval Rabani. An $`O(\log k)`$ approximate min-cut max-flow theorem and approximation algorithm. _SIAM Journal on Computing_ **27**(1):291–301, 1998. doi:10.1137/S0097539794285983.
- James R. Lee and Prasad Raghavendra. Coarse differentiation and multi-flows in planar graphs. _Discrete & Computational Geometry_ **43**(2):346–362, 2010. doi:10.1007/s00454-009-9172-4.
- Abraham, Ittai, Filtser, Arnold, Gupta, Anupam, Neiman, Ofer, Metric Embedding via Shortest Path Decompositions (2022)
- Ittai Abraham, Arnold Filtser, Anupam Gupta, and Ofer Neiman. Metric embedding via shortest path decompositions. _SIAM Journal on Computing_ **51**(2):290–314, 2022. doi:10.1137/19M1296021.
- Aumann, Yonatan, Rabani, Yuval, An $`O(\log k)`$ Approximate Min-Cut Max-Flow Theorem and Approximation Algorithm (1998)
- Chakrabarti, Amit, Jaffe, Alexander, Lee, James R., Vincent, Justin, Embeddings of topological graphs: Lossy invariants, linearization, and 2-sums (2008)
- Amit Chakrabarti, Alexander Jaffe, James R. Lee, and Justin Vincent. Embeddings of topological graphs: Lossy invariants, linearization, and 2-sums. In _49th Annual IEEE Symposium on Foundations of Computer Science_, pp. 761–770. IEEE, 2008. doi:10.1109/FOCS.2008.79.
- Parinya Chalermsook, Matthias Kaul, Matthias Mnich, Joachim Spoerhase, Sumedha Uniyal, and Daniel Vaz. Approximating sparsest cut in low-treewidth graphs via combinatorial diameter. _ACM Transactions on Algorithms_ **20**(1), Article 6, pp. 1–20, 2024. doi:10.1145/3632623.
- Chalopin, Jérémie, Chepoi, Victor, Naves, Guyslain, Isometric Embedding of Busemann Surfaces into $`L_1`$ (2015)
- Chekuri, Chandra, Gupta, Anupam, Newman, Ilan, Rabinovich, Yuri, Sinclair, Alistair, Embedding $`k`$-Outerplanar Graphs into $`\ell_1`$ (2006)
- Chandra Chekuri, Anupam Gupta, Ilan Newman, Yuri Rabinovich, and Alistair Sinclair. Embedding $`k`$-outerplanar graphs into $`\ell_1`$. _SIAM Journal on Discrete Mathematics_ **20**(1):119–136, 2006. doi:10.1137/S0895480102417379.
- Vincent Cohen-Addad, Tobias Mömke, and Victor Verdugo. A 2-approximation for the bounded treewidth sparsest cut problem in FPT time. _Mathematical Programming_ **206**:479–495, 2024. doi:10.1007/s10107-023-02044-1.
- Jonathan Conroy and Arnold Filtser. How to protect yourself from threatening skeletons: Optimal padded decompositions for minor-free graphs. In _57th Annual ACM Symposium on Theory of Computing_, pp. 2281–2292. ACM, 2025. doi:10.1145/3717823.3718252.
- James R. Lee and Anastasios Sidiropoulos. On the geometry of graphs with a forbidden minor. In _41st Annual ACM Symposium on Theory of Computing_, pp. 245–254. ACM, 2009. doi:10.1145/1536414.1536450.
- Filtser, Arnold, A Face Cover Perspective to $`\ell_1`$ Embeddings of Planar Graphs (2025)
- Arnold Filtser, Tobias Friedrich, Davis Issac, Nikhil Kumar, Hung Le, Nadym Mallek, and Ziena Zeif. Optimal padded decomposition for bounded treewidth graphs. _TheoretiCS_ **4**, Article 22, pp. 1–39, 2025. doi:10.46298/theoretics.25.22.
- James R. Lee and Daniel E. Poore. On the 2-sum embedding conjecture. In _29th Annual Symposium on Computational Geometry_, pp. 197–206. ACM, 2013. doi:10.1145/2462356.2492436.
- Gupta, Anupam, Newman, Ilan, Rabinovich, Yuri, Sinclair, Alistair, Cuts, Trees and $`\ell_1`$-Embeddings of Graphs (2004)
- Anupam Gupta, Ilan Newman, Yuri Rabinovich, and Alistair Sinclair. Cuts, trees and $`\ell_1`$-embeddings of graphs. _Combinatorica_ **24**(2):233–269, 2004. doi:10.1007/s00493-004-0015-x. Author manuscript.
- Anupam Gupta, Kunal Talwar, and David Witmer. Sparsest cut on bounded treewidth graphs: Algorithms and hardness results. In _45th Annual ACM Symposium on Theory of Computing_, pp. 281–290. ACM, 2013. doi:10.1145/2488608.2488644. Full version: arXiv:1305.1347.
- Hurkens, C. A. J., Schrijver, Alexander, Tardos, Éva, On Fractional Multicommodity Flows and Distance Functions (1988)
- Klein, Philip N., Plotkin, Serge A., Rao, Satish, Excluded Minors, Network Decomposition, and Multicommodity Flow (1993)
- Krauthgamer, Robert, Lee, James R., Rika, Havana, Flow-Cut Gaps and Face Covers in Planar Graphs (2019)
- Kumar, Nikhil, An Approximate Generalization of the Okamura–Seymour Theorem (2025)
- Lee, James R., Raghavendra, Prasad, Coarse Differentiation and Multi-flows in Planar Graphs (2010)
- Lee, James R., Sidiropoulos, Anastasios, On the Geometry of Graphs with a Forbidden Minor (2009)
- Linial, Nathan, London, Eran, Rabinovich, Yuri, The geometry of graphs and some of its algorithmic applications (1995)
- Nathan Linial, Eran London, and Yuri Rabinovich. The geometry of graphs and some of its algorithmic applications. _Combinatorica_ **15**(2):215–245, 1995. doi:10.1007/BF01200757.
- Newman, Ilan, Rabinovich, Yuri, A Lower Bound on the Distortion of Embedding Planar Metrics into Euclidean Space (2003)
- OpenAI. Planar Graph Metrics Embed into $`L_1`$ with Constant Distortion. OpenAI Math Release preprint OAI:Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026, 2026.
- Okamura, Haruko, Seymour, Paul D., Multicommodity flows in planar graphs (1981)
- OpenAI, {$`L_1`$ Embeddings of Graphs of Bounded Treewidth} (2026)
- James R. Lee and Anastasios Sidiropoulos. Pathwidth, trees, and random embeddings. _Combinatorica_ **33**(3):349–374, 2013. doi:10.1007/s00493-013-2685-8.
- Rao, Satish, Small distortion and volume preserving embeddings for planar and Euclidean metrics (1999)
- Sidiropoulos, Anastasios, Non-positive curvature and the planar embedding conjecture (2013)
- Neil Robertson and P. D. Seymour. Graph minors. V. Excluding a planar graph. _Journal of Combinatorial Theory, Series B_ **41**(1):92–114, 1986. doi:10.1016/0095-8956(86)90030-4.
- Eden Chlamtáč, Robert Krauthgamer, and Prasad Raghavendra. Approximating sparsest cut in graphs of bounded treewidth. In _APPROX/RANDOM 2010_, Lecture Notes in Computer Science, vol. 6302, pp. 124–137. Springer, 2010. doi:10.1007/978-3-642-15369-3\_10. Full version: arXiv:1006.3970v2.
