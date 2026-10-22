Notes / Summaries / Convex and metric geometry / [Family 089](../../index/convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md)

# 089 — Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs

## Original CONTENTS.md summary

[S1:254] carries the family entry:

> Resolves the planar and bounded-treewidth cases of the Gupta--Newman--Rabinovich--Sinclair conjecture. Shortest-path metrics of finite connected graphs with arbitrary positive edge lengths embed into real $L_1$ with universal distortion for planar graphs, and distortion depending only on treewidth for bounded-treewidth graphs. The corresponding multicommodity flow--cut gaps are uniformly bounded.

The entry links the two manuscripts as "Planar graph embeddings" and
"Bounded-treewidth embeddings" [S1:254].

The first manuscript's title is `Planar Graph Metrics Embed into $L_1$ with Constant Distortion` [S2:1].

The README dates it September 23, 2026 [S2:13].

The second manuscript's title is `L1 Embeddings of Graphs of Bounded Treewidth` [S18:1].

The README dates it September 23, 2026 [S18:13].

## Undergraduate summary

An **$L_1$ metric** is a distance computed as a sum over coordinates — the
"taxicab" distance. A graph's shortest-path metric is the distance between
vertices measured along edges. The question is how faithfully an $L_1$
embedding can reproduce a graph's shortest-path distances.

The first manuscript settles the planar case. [S3:33–35] states the result:
"We prove that every finite connected planar graph with arbitrary positive
real edge lengths embeds into real $L_1$ with a universal distortion bound.
This resolves the planar embedding conjecture positively."

The second manuscript settles the bounded-treewidth case. [S20:2–6] states
it: "For every fixed treewidth bound, the shortest-path metrics of finite
connected graphs with arbitrary positive real edge lengths embed into real
$L_1$ with uniformly bounded distortion. This resolves the bounded-treewidth
case of the Gupta--Newman--Rabinovich--Sinclair conjecture positively."

The planar question is stated before the proof. [S4:9–11] gives it: "The
planar embedding conjecture asks whether one constant $C$ works for every
planar graph metric, independently of the number of vertices and the edge
lengths. We prove that it does."

The planar theorem's shape is a measure-space representation. [S4:14–17]
opens it: "There is a finite universal constant $C\ge1$ with the following
property. For every finite connected planar graph $G=(V,E)$ with strictly
positive real edge lengths, there exist a measure space $(\Omega,\mathcal
F,\mu)$ and a map" — the display gives the integral identity.

Treewidth measures how tree-like a graph is: a tree has treewidth 1, a
series-parallel graph has treewidth 2, and a graph with a tree decomposition
whose bags hold at most $k$ vertices has treewidth below $k$. The treewidth
theorem is quantified by that bound. [S20:28–31] opens it: "For every integer
$k\ge2$ there is a finite constant $C_k\ge1$ with the following property. If
a finite connected graph $G=(V,E)$ admits a tree decomposition with bags of
size at most $k$, then, for every edge-length function $\ell:E\to(0,\infty)$,
there is a map $F$ from $V$ into a real" — the display gives the distortion
bound.

[S20:39–40] names what the constant does not depend on: "The constant is
independent of the number of vertices, the depth of the decomposition, and
all ratios of edge lengths."

The two results settle two cases of the same conjecture. [S4:24–26] names
the first: "This proves the planar case of the conjecture of Gupta, Newman,
Rabinovich, and Sinclair, which predicts uniformly bounded $L_1$ distortion
in every proper minor-closed family."

The second manuscript names its case and its reach. [S20:45–51] says: "The
bounded-treewidth family is one of the cases of the conjecture of Gupta,
Newman, Rabinovich, and Sinclair, which predicts a uniform $L_1$ distortion
bound for every proper minor-closed graph family. By the
excluded-planar-minor theorem of Robertson and Seymour, our result also gives
a uniform bound for graphs excluding any fixed planar graph as a minor."

## Graduate summary

The first manuscript's route is a cut representation. [S4:42–45] explains the
target: "Conversely, threshold sweeps through real coordinates give such a
representation for every $L_1$ metric on a finite set. Thus we seek weighted
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
"The general preceding bound for $n$-vertex planar metrics is $O(\sqrt{\log
n})$, due to Rao."

The obstacle is Euclidean. [S4:70–73] says: "Newman and Rabinovich showed
that even series-parallel metrics can require $\Omega(\sqrt{\log n})$
distortion into Euclidean space. Thus a constant planar $L_1$ bound requires
a different route."

The first manuscript states a consequence beyond the embedding. [S4:58–62]
gives it: "Gupta et al. showed that its worst value on a fixed graph equals
the worst $L_1$ distortion over all weighted shortest-path metrics on that
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
"The proof gives the existence of $C_k$, without an explicit estimate for its
dependence on $k$."

For rational lengths the construction is algorithmic. [S20:125–128] states
it: "For positive rational edge lengths, these algorithms and Theorem 1 yield
embeddings of distortion at most $(2+\varepsilon)C_k$, for each fixed
$\varepsilon>0$, in fixed-parameter time with respect to $k$."

The scope note records what the formalization carries. [S29:10] gives the
planar result: "The planar case of the Gupta–Newman–Rabinovich–Sinclair
embedding problem asks for a universal distortion bound in $L_1$. The
formalized result gives one constant $C$ for every finite connected planar
graph with arbitrary positive real edge lengths: its weighted shortest-path
metric embeds into real $L_1$ with distortion at most $C$."

The scope note's second paragraph gives the treewidth result. [S29:12] says:
"The formalized result gives a uniform $L_1$ embedding bound for each
bounded-treewidth class. For every bag-size bound $k\ge2$, there is a
constant $C(k)$ such that the weighted shortest-path metric of every nonempty
finite connected graph with a tree decomposition of bag size at most $k$
embeds into finite-dimensional real $L_1$ with distortion at most $C(k)$."

The two declarations are the quantified forms.
`OAI.PlanarL1.planar_graph_metrics_embed_L1` at [S30:96] is the planar
theorem. `OAI.BoundedTreewidthL1.main_theorem` at [S31:135] is the
bounded-treewidth theorem.

The two comparator configs state the targets the release set itself, and each
is a stub. [S32:47] carries `sorry`; [S33:44] carries `sorry`. The scope
note's comparator table links `PlanarL1.lean` and `BoundedTreewidthL1.lean`,
one per formalized result.

## History of the conjecture

The Gupta--Newman--Rabinovich--Sinclair conjecture predicts a uniform $L_1$
distortion bound for every proper minor-closed graph family, cited in both
manuscripts at the lines that state it [S4:24–26] and [S20:45–51]. The first
manuscript's bibliography carries the entry [S5:1] and the second carries it
at [S27:1].

The treewidth-two case was settled before this result. [S20:85] records it:
"Gupta et al. proved the treewidth-two case."

The exact value for treewidth two is known. [S20:86–88] gives it: "The
optimal distortion is $2$, by the upper bound of Chakrabarti, Jaffe, Lee, and
Vincent and the matching lower bound of Lee and Raghavendra."

The pathwidth case was settled by a probabilistic route. [S20:94–97] records
it: "Lee and Sidiropoulos established the bounded-pathwidth case through
stochastic embeddings into trees: each sampled tree metric dominates the graph
metric, while its expected expansion is bounded by a function of the
pathwidth."

`notes/tables/conjecture-standing.tsv` carries no row for family 089, so the
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

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `overview.tex` | 859 | Family entry, line 254 |
| S2 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/README.md` | 20 | Manuscript 1 title, date, citation |
| S3 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/main.tex` | 51 | Abstract, lines 33–35 |
| S4 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/introduction.tex` | 239 | Conjecture, theorem, history, proof outline |
| S5 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/references.bib` | 223 | Bibliography entries |
| S6 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/column-realization.tex` | 49 | Column realization figure |
| S7 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/surviving-seeds.tex` | 67 | Surviving seeds figure |
| S8 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/two-portals.tex` | 39 | Two portals figure |
| S9 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/sets.tex` | 240 | Threshold sets and local coordinates |
| S10 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/scale-setup.tex` | 138 | Scales and the local experiment |
| S11 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/ordered.tex` | 406 | Ordered fields and separation on the two arcs |
| S12 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/main-packing.tex` | 510 | The main update and a packing bound for secondary seeds |
| S13 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/secondary.tex` | 266 | The secondary update |
| S14 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/geometry.tex` | 452 | Columns and thin bands |
| S15 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/interpolation.tex` | 454 | Interpolation by single-source distance functions |
| S16 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/assembly.tex` | 274 | Preserving charts and assembling the embedding |
| S17 | `preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/consequences.tex` | 75 | A consequence for almost-embeddable families |
| S18 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/README.md` | 20 | Manuscript 2 title, date, citation |
| S19 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/main.tex` | 63 | Document structure |
| S20 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/01-introduction.tex` | 265 | Abstract, theorem, history, proof outline |
| S21 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/02-cut-laws.tex` | 468 | Cut measures and transport along a decomposition |
| S22 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/03-particles.tex` | 279 | Particles and reservations |
| S23 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/04-perturbations.tex` | 219 | Separating pairs in a common bag |
| S24 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/05-anchors.tex` | 326 | The anchor construction |
| S25 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/06-lower-comparison.tex` | 420 | Uniform lower comparison |
| S26 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/07-conclusion.tex` | 36 | Completing the embedding |
| S27 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/bibliography.tex` | 128 | Bibliography entries |
| S28 | `preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/figures/anchor-reservations.tex` | 45 | Anchor reservations figure |
| S29 | `lean/docs/089.md` | 19 | Scope note |
| S30 | `lean/OAI/Combinatorics/PlanarL1/Embedding.lean` | 124 | `PlanarL1.planar_graph_metrics_embed_L1` |
| S31 | `lean/OAI/Combinatorics/TreewidthL1/Main.lean` | 188 | `BoundedTreewidthL1.main_theorem` |
| S32 | `lean/ComparatorChallenges/PlanarL1.lean` | 51 | Stub, `sorry` at line 47 |
| S33 | `lean/ComparatorChallenges/BoundedTreewidthL1.lean` | 50 | Stub, `sorry` at line 44 |

## Links

- [S1](../../../overview.tex)
- [S2](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/README.md)
- [S3](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/main.tex)
- [S4](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/introduction.tex)
- [S5](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/references.bib)
- [S6](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/column-realization.tex)
- [S7](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/surviving-seeds.tex)
- [S8](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/figures/two-portals.tex)
- [S9](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/sets.tex)
- [S10](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/scale-setup.tex)
- [S11](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/ordered.tex)
- [S12](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/main-packing.tex)
- [S13](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/secondary.tex)
- [S14](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/geometry.tex)
- [S15](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/interpolation.tex)
- [S16](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/assembly.tex)
- [S17](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/sections/consequences.tex)
- [S18](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/README.md)
- [S19](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/main.tex)
- [S20](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/01-introduction.tex)
- [S21](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/02-cut-laws.tex)
- [S22](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/03-particles.tex)
- [S23](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/04-perturbations.tex)
- [S24](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/05-anchors.tex)
- [S25](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/06-lower-comparison.tex)
- [S26](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/07-conclusion.tex)
- [S27](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/bibliography.tex)
- [S28](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/figures/anchor-reservations.tex)
- [S29](../../../lean/docs/089.md)
- [S30](../../../lean/OAI/Combinatorics/PlanarL1/Embedding.lean)
- [S31](../../../lean/OAI/Combinatorics/TreewidthL1/Main.lean)
- [S32](../../../lean/ComparatorChallenges/PlanarL1.lean)
- [S33](../../../lean/ComparatorChallenges/BoundedTreewidthL1.lean)

## Bibliography

**19 entries** from `references.bib`:
- Linial, Nathan, London, Eran, Rabinovich, Yuri. *The geometry of graphs and some of its algorithmic applications*. (1995) [LLR95]
- Gupta, Anupam, Newman, Ilan, Rabinovich, Yuri, Sinclair, Alistair. *Cuts, Trees and {$\ell_1$}-Embeddings of Graphs*. (2004) [GNRS04]
- Rao, Satish. *Small distortion and volume preserving embeddings for planar and {Euclidean} metrics*. (1999) [Rao99]
- Okamura, Haruko, Seymour, Paul D.. *Multicommodity flows in planar graphs*. (1981) [OS81]
- Chakrabarti, Amit, Jaffe, Alexander, Lee, James R., Vincent, Justin. *Embeddings of topological graphs: Lossy invariants, linearization, and 2-sums*. (2008) [CJLV08]
- Sidiropoulos, Anastasios. *Non-positive curvature and the planar embedding conjecture*. (2013) [Sidiropoulos13]
- Filtser, Arnold. *A Face Cover Perspective to {$\ell_1$} Embeddings of Planar Graphs*. (2025) [Filtser25]
- Aumann, Yonatan, Rabani, Yuval. *An {$O(\log k)$} Approximate Min-Cut Max-Flow Theorem and Approximation Algorithm*. (1998) [AR98]
- Klein, Philip N., Plotkin, Serge A., Rao, Satish. *Excluded Minors, Network Decomposition, and Multicommodity Flow*. (1993) [KPR93]
- Chekuri, Chandra, Gupta, Anupam, Newman, Ilan, Rabinovich, Yuri, Sinclair, Alistair. *Embedding {$k$}-Outerplanar Graphs into {$\ell_1$}*. (2006) [CGNRS06]
- … and 9 more

**18 entries** from `bibliography.tex`:
- [AFGN22] Ittai Abraham, Arnold Filtser, Anupam Gupta, and Ofer Neiman. Metric embedding via shortest path decompositions. \emph{S…
- [AR98] Yonatan Aumann and Yuval Rabani. An $O(\log k)$ approximate min-cut max-flow theorem and approximation algorithm. \emph{…
- [CJLV08] Amit Chakrabarti, Alexander Jaffe, James R. Lee, and Justin Vincent. Embeddings of topological graphs: Lossy invariants,…
- [ChalermsookEtAl] Parinya Chalermsook, Matthias Kaul, Matthias Mnich, Joachim Spoerhase, Sumedha Uniyal, and Daniel Vaz. Approximating spa…
- [CGNRS06] Chandra Chekuri, Anupam Gupta, Ilan Newman, Yuri Rabinovich, and Alistair Sinclair. Embedding $k$-outerplanar graphs int…
- [CKR] Eden Chlamt{\'a}{\v c}, Robert Krauthgamer, and Prasad Raghavendra. Approximating sparsest cut in graphs of bounded tree…
- [CohenAddadMomkeVerdugo] Vincent Cohen-Addad, Tobias M{\"o}mke, and Victor Verdugo. A 2-approximation for the bounded treewidth sparsest cut prob…
- [ConroyFiltser25] Jonathan Conroy and Arnold Filtser. How to protect yourself from threatening skeletons: Optimal padded decompositions fo…
- [FiltserEtAl] Arnold Filtser, Tobias Friedrich, Davis Issac, Nikhil Kumar, Hung Le, Nadym Mallek, and Ziena Zeif. Optimal padded decom…
- [GNRS] Anupam Gupta, Ilan Newman, Yuri Rabinovich, and Alistair Sinclair. Cuts, trees and $\ell_1$-embeddings of graphs. \emph{…
- … and 8 more
