[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 106](../index/theoretical-computer-science/106-hardness-of-coloring-three-colorable-graphs.md)

# 106 — Hardness of coloring three-colorable graphs

[Index page](../index/theoretical-computer-science/106-hardness-of-coloring-three-colorable-graphs.md)

## Original CONTENTS.md summary

[S1:2629] (family entry):

> **106. Hardness of coloring three-colorable graphs.** It is NP-hard to color a three-colorable graph using any fixed number c ≥ 3 of colors. More strongly, for every fixed $`0\lt \delta\lt 1/3`$, a deterministic polynomial-time reduction from 3SAT produces simple unweighted graphs that are three-colorable in the satisfiable case and have no independent set of size $`\delta n`$ otherwise, where n is the number of vertices. (Lean)

[S1:2636] (the manuscript entry, with its abstract at [S1:2638]):

> Hardness of finding large independent sets in three-colorable graphs

> We prove that, for every fixed $`0\lt \delta\lt 1/3`$, it is NP-hard to distinguish three-colorable graphs from graphs in which every independent set has fewer than δ times the number of vertices. Consequently, for every fixed integer c ≥ 3, finding a proper c-coloring of a three-colorable graph is NP-hard.

[S2:290] carries the `\resultentry`, so the release blurb and the overview agree.
The family title is the coloring form ("Hardness of coloring three-colorable
graphs") while the manuscript title is the independent-set form, and the
overview states the coloring consequence first with the independent-set
statement as "more strongly" — the manuscript puts them in the opposite order
(see the consequences section below).

## Undergraduate summary

A **proper coloring** assigns different colors to adjacent vertices, and an
**independent set** is a set of pairwise nonadjacent vertices [S4:3–4]. For a
nonempty finite graph $G$ with $n$ vertices, $\alpha(G)$ is the maximum
independent-set size [S4:5–6]. Every three-colorable graph has an independent
set of size at least $n/3$, because one of its three color classes has that
size: "every three-colorable graph contains an independent set of size at
least $n/3$" [S4:7–8]. So a graph with independence ratio below $\delta<1/3$
is *not* three-colorable, and the reduction separates the two cases.

The decision problem is **approximate graph coloring**: given a graph promised
to be $k$-colorable, find a proper $c$-coloring for fixed $k\le c$
[S4:42–44]. It is NP-hard even for the promise $k=3$ and any fixed palette
$c\ge3$ — the corollary the family delivers [S4:48–58]. The strength of this
family's statement is that the soundness side is not "not $c$-colorable" but
a *density* bound: every independent set is below $\delta n$, for any fixed
$\delta>0$, no matter how large the palette [S4:12–30].

The graph the reduction outputs is unweighted, simple, and explicitly listed;
the satisfying coloring in the completeness case exists for the whole vertex
set, and the reduction does not ship it [S4:28–29].

## Graduate summary

**Main theorem** ([S4:12–30], `thm:main`). "For every fixed real
$\delta\in(0,\,1/3)$" — in the manuscript's exact form: "for every fixed real
$0<\delta<1/3$, there is a deterministic polynomial-time algorithm $R_\delta$
that maps each explicitly encoded Boolean $3$-CNF formula $\phi$ to a nonempty
finite simple undirected unweighted graph $G_\phi$" [S4:13–16], such that a
satisfiable $\phi$ gives a three-colorable $G_\phi$ and an unsatisfiable
$\phi$ gives $\alpha(G_\phi)<\delta\,|V(G_\phi)|$ [S4:19–22]. Running time
and output size are polynomial in the binary encoding length, with constants
and degree allowed to depend on $\delta$ [S4:25–27]. It suffices to prove it
for rational $\delta$ [S4:32–34], and the density conclusion is strictly
stronger than a chromatic-number lower bound, since adding isolated vertices
preserves chromatic number while pushing the independence ratio toward one
[S4:35–39].

**Corollary** ([S4:48–58], `cor:coloring`). For every fixed pair
$3\le k\le c$, distinguishing $k$-colorable graphs from graphs that are not
$c$-colorable is NP-hard: choose $\delta<\min\{1/3,1/c\}$; a $c$-colorable
graph has an independent set of size at least $n/c$, which the soundness
bound excludes [S4:53–57].

**Construction** (the proof overview [S4:141–212]). The starting problem is
Label Cover, fed by the PCP theorem and parallel repetition [S4:141–146].
The construction replaces one left question at a time by a right question,
building chains of question tuples in the style of the multilayered PCP
[Dinur–Guruswami–Khot–Regev, S4:148–151]. Each tuple carries points that
assign a phase in the circle $\mathbb T=\mathbb R/\mathbb Z$ to every product answer, and a
projection $\pi$ pulls a phase vector back along the chain
[S4:152–154]. Zero-length links between a point and its pullback, and
circle-distance links within each phase space, define a pseudometric; edges
compare a point with the coordinatewise half-shift of another. The edge
threshold forces adjacent vertices to sit more than $1/3$ apart on the
circle, so three half-open intervals color the graph properly [S4:160–162].

For soundness, an independent set yields functions on the tuple phase spaces
with a half-shift sign change and a shared Lipschitz bound; Austin's
dimension-independent approximation (a continuous Friedgut junta theorem)
approximates them by boundedly many answer coordinates [S4:164–168]. Because
product-measure approximation need not survive coordinate identifications by
projections, the construction picks coordinate lists for whole small
subchains with independent rotation variables per layer, and projects the
lists to a common answer set [S4:169–177]. A **distributional alignment
lemma** chooses a law on sets of layers before seeing the lists, assigning
each listed label to a shared index on most sets, via finite minimax, Ramsey
homogenization, and an order-invariant random-array argument
[S4:179–188]. **Coefficient sampling** at geometrically decreasing levels
absorbs uniform phase shifts, and a dimension-independent influence bound
closes the density estimate [S4:190–197]. Only fixed finite rational data
enter the graph, so the probability experiment expands exactly into
unweighted vertices and the reduction is deterministic [S4:199–201].

The final section fixes the constants in dependency order: the list bound
$d$ first, so it cannot depend on the Label Cover alphabets
[S5:6–8]; then $\varepsilon=\delta/8$, $L=64$, the influence constants,
the repetition power [S5:10–17]. The density bound closes at
$6\varepsilon+2\varepsilon=8\varepsilon<\delta$ for every independent set [S5:78–82].

## History of the conjecture

The manuscript positions itself against a named line of approximate-coloring
hardness. **Khanna, Linial and Safra** established hardness of
four-coloring three-colorable graphs, and **Guruswami and Khanna** gave a
different proof with bounded-degree variants [S4:62–66]. The algebraic
promiseConstraintSatisfaction theory of **Barto, Bul\'{\i}n, Krokhin and
Opr\v{s}al** gave hardness of $(2k-1)$-coloring $k$-colorable graphs — five
colors for $k=3$ — and recorded the conjectured hardness for every fixed
$k\le c$ [S4:68–72]. **Guruswami and Sandeep** showed that the ordinary
$d$-to-1 Games Conjecture with perfect completeness implies constant-palette
hardness for three-colorable graphs, via a reduction that first gives small
independent-set density with a $2d$-colorable completeness promise, then
collapses the palette through the arc-graph reduction of **Krokhin, Opr\v{s}al,
Wrochna and \v{Z}ivn\'y** — and that route loses the independent-set
guarantee [S4:74–85]. The manuscript cites the companion release article as
the perfect-completeness premise for $d=2$: "the companion article ...
establishes the ordinary perfect-completeness premise for $d=2$" [S4:86–87]
— this is a citation to the family 105 manuscript, whose page is
[105-2-to-1-games-conjecture-with-perfect-completeness.md](105-2-to-1-games-conjecture-with-perfect-completeness.md).
**Fei, Minzer and Wang** proved the 4-to-1 Games Conjecture with perfect
completeness; combining their corollaries with the same reductions resolves
the constant-palette conjecture, at an eight-colorable promise
[S4:89–95]. Theorem `thm:main` gets the stronger soundness density and the
three-colorability of the entire graph, starting from ordinary projection
Label Cover with no fiber-size bound [S4:96–99]. Conditional antecedents:
**Dinur, Mossel and Regev**'s fish-shaped Label Cover conjecture and
**Braverman, Khot, Lifshitz and Minzer**'s Rich 2-to-1 invariance-principle
result give the same promise under conjectural hypotheses [S4:101–112], and
**Dinur, Khot, Perkins and Safra** plus **Hecht, Minzer and Safra** work in
a deletion model that relaxes completeness [S4:114–122]. The all-vertex
completeness here retains the original promise at every fixed positive
soundness density [S4:123–124]. The algorithmic side keeps narrowing the
quantitative gap: Bansal–Huang–Lee's $O(n^{0.19539})$-color algorithm,
improving Kawarabayashi–Thorup–Yoneda, and post-release preprints by Narang–Tang
and Anand [S4:126–137].

**Prior (my training data, not this repo).** Khanna–Linial–Safra (2000) was
the first constant-palette hardness result, the 4-coloring-three-colorable
conjecture is a long-standing target, and the Guruswami–Sandeep conditional
result is the standard games-conjecture route. I cannot confirm these
results independently; the release ships the manuscript as a proof, and the
Lean layer formalizes the reduction statement itself (see the comparison
below).

## Consequences

- **Constant-palette coloring hardness.** For every fixed $c\ge3$, coloring a
  three-colorable graph with $c$ colors is NP-hard [S3:43–45, S4:48–58] —
  the conjecture-level conclusion the intro says prior combinations reach
  only through the 4-to-1 route [S4:89–95].
- **The density form.** The independent-set statement is stronger than the
  coloring statement: independence ratio below $\delta n$ excludes every
  palette, and it survives in the promise, not as a derived bound
  [S4:12–30].
- **A 2-to-1 consequence.** The manuscript cites the family 105 theorem as
  the perfect-completeness premise for $d=2$ that the Guruswami–Sandeep
  reduction consumes [S4:86–87].
- **Method transfer.** The phase-circle graph and the alignment lemma are
  self-contained ([S4:199–201], `sec:alignment-proof` [S3:54]), so the
  analytic machinery is available for later density results.

## Section skeleton

The root [S3:41–45] includes eight sections in the order [S3:47–54]:
`introduction`, `preliminaries`, `construction`, `lists`, `alignment`,
`coefficient`, `parameters`, `alignment-proof`, followed by `plain` style
bibliography over `references.bib` [S3:55–56]. The section files sit under
`build/source/sections/`. The shipped PDF [S6] is the manuscript in the form
the release distributes; the LaTeX under `build/source/` is the working
source the page cites.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S7], one
comparator stub [S8:76–77], and one `main_results` entry [S10]. The Scope section
states: "the formalized result shows hardness of finding large independent
sets even under a three-colorability promise. For every fixed
$0<\delta<1/3$, a deterministic polynomial-time reduction maps binary 3SAT
formulas to nonempty finite simple graphs" [S7:9], with three-colorable
outputs on satisfiable inputs, largest independent set below $\delta n$
otherwise, and "the complete adjacency-matrix output is included in the
runtime bound" [S7:9].

The `main_results` entry [S10:1317–1319] names
`OAI.LargeIndependentSets.mainTheoremReal` in
`lean/OAI/Combinatorics/IndependentSets/Main.lean`. In the source the
theorem is stated and closed: "theorem mainTheoremReal : ∀ δ : ℝ, 0 < δ →
δ < 1 / 3 → Nonempty (RealGraphReduction δ) := by intro δ hδ _hδ3"
[S9:124–126], built from `PCP.ExpanderTables.exists_base_table`,
`finite_graph_reduction`, and `LCInput.uniform_repetition`
[S9:127–131]. `grep` finds **zero** `sorry` in the whole
`lean/OAI/Combinatorics/IndependentSets/` tree (11 files).

The comparator stub [S8:76–77] defines `RealGraphReduction` — the graph, the
machine, the output-size bound, the completeness and soundness fields
[S8:64–73] — and the target statement "$```lean
theorem mainTheoremReal : ∀ δ : ℝ, 0 < δ → δ < 1 / 3 → Nonempty (RealGraphReduction δ) := by
```
[S8:76–77]$" ends in
`sorry` at [S8:78]. The proved copy is the one the `main_results` entry
names [S9:124–135]. The reading is of source text only — no `lake` or `lean`
run elaborates the proof, so the claim here is that the proof body exists
in the source, not that the file compiles.

## Coverage

The ledger row `fam=106` [S11] records the tier and the counts: `tier=T3`,
`paps=1`, `paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`,
`verification=0`, `trace=`. This is the strong single-manuscript coverage
shape, as family 105: the manuscript is a formalization source and the one
`main_results` entry names the reduction theorem the manuscript's `thm:main`
states [S4:12–30]. The shape flag is `uniform`, and `resolves_named=0` —
the blurb names no conjecture with a resolve verb, so the family title's
conjecture-level claim ("Hardness of coloring three-colorable graphs") has
no ledger verb support. There is no verification bundle and no reasoning
trace; the shipped PDF [S6] and the Lean layer [S7] [S8:76–77] [S9:124–126] [S10] are the
two evidence surfaces.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2629], the manuscript link [S1:2636], and the manuscript abstract [S1:2638]. The release's inline code spans stay as backticked markdown, and the release's italic markup is folded to the plain word |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 106 at [S2:290] |
| S3 | [`preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/main.tex`](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/main.tex) | 57 | root (`\documentclass`); abstract [S3:40–46]; the eight-section include order [S3:47–54] |
| S4 | [`preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/introduction.tex`](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/introduction.tex) | 212 | the coloring and independent-set definitions [S4:3–10]; the main theorem [S4:12–30]; the coloring corollary [S4:48–58]; the history [S4:62–137]; the proof overview [S4:141–212] |
| S5 | [`preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/parameters.tex`](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/parameters.tex) | 87 | the parameter choice order [S5:4–8]; the fixed constants [S5:10–17]; the closing density bound [S5:70–87] |
| S6 | [`preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf`](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf) | 14770 | the manuscript as shipped |
| S7 | [`lean/docs/106.md`](../../../lean/docs/106.md) | 15 | scope note — the formalization's Scope at [S7:9] and its comparator link |
| S8 | [`lean/ComparatorChallenges/IndependentSets.lean`](../../../lean/ComparatorChallenges/IndependentSets.lean) | 84 | the comparator stub — `RealGraphReduction` at [S8:64–73] and `mainTheoremReal` at [S8:76–78] with its `sorry` |
| S9 | [`lean/OAI/Combinatorics/IndependentSets/Main.lean`](../../../lean/OAI/Combinatorics/IndependentSets/Main.lean) | 152 | the formalized file — `mainTheoremReal` proved at [S9:124–135] |
| S10 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming the declaration, at [S10:1317–1319] |
| S11 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=106`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
