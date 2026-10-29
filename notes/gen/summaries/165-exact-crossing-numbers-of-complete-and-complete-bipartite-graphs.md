[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 165](../index/combinatorics/165-exact-crossing-numbers-of-complete-and-complete-bipartite-graphs.md)

# 165 — Exact crossing numbers of complete and complete bipartite graphs

[Index page](../index/combinatorics/165-exact-crossing-numbers-of-complete-and-complete-bipartite-graphs.md)

## Original CONTENTS.md summary

The release's blurb [S1:3886] and the catalog abstract [S2:411] state
the family's claim: a resolution of the **Harary–Hill
conjecture** (the crossing number of every complete graph
$`K_n`$) and of **Turan's brickyard problem** in the
**Zarankiewicz formulation** (the crossing number of every complete
bipartite graph $`K_{m,n}`$). Both formulas are exact, and the
classical drawings are proven optimal among all plane drawings with
continuous edge arcs. Two manuscripts carry the family. The first,
*The crossing number of complete graphs* [S3:32, S3:34], abstract


> We prove the Harary–Hill conjecture: for every positive integer $`n`$,
the ordinary crossing number of the complete graph $`K_n`$ is
$$\frac14\left\lfloor\frac n2\right\rfloor
 \left\lfloor\frac{n-1}{2}\right\rfloor
 \left\lfloor\frac{n-2}{2}\right\rfloor
 \left\lfloor\frac{n-3}{2}\right\rfloor.$$ [S3:37–44]

The second, *The crossing number of complete bipartite graphs*
[S4:32, S4:34], abstract [S4:39–47]:

We prove the Zarankiewicz crossing-number conjecture, resolving
Turan's brickyard problem. For all positive integers $`m,n`$, the
ordinary crossing number of the complete bipartite graph $`K_{m,n}`$
is
$`\lfloor\tfrac{m}{2}\rfloor\lfloor\tfrac{m-1}{2}\rfloor
\lfloor\tfrac{n}{2}\rfloor\lfloor\tfrac{n-1}{2}\rfloor`$
[S4:39–47].

## Undergraduate summary

The **crossing number** $`\mathrm{cr}(G)`$ of a graph $`G`$ is the
**fewest** number of times two edges must cross when $`G`$ is drawn in
the plane with the edges as continuous arcs. (Edges that meet at a
vertex do not count; only proper crossings of edge interiors do, and
if the same pair of edges crosses twice, both crossings count.) For
decades, the exact value was unknown for the two most basic graph
families. The **Harary–Hill conjecture** (1960s) proposed a
closed formula for $`\mathrm{cr}(K_n)`$, the complete graph on $`n`$
vertices; the **Zarankiewicz conjecture** proposed one for
$`\mathrm{cr}(K_{m,n})`$, the complete bipartite graph on parts of
size $`m`$ and $`n`$. Both were known to hold for small graph sizes,
but the general formulas resisted proof. This family closes both:
it proves each lower bound (no drawing has fewer crossings than the
formula) and constructs a drawing that attains exactly that many
[S3:37–44, S4:39–47, S5:10, S5:12].

## Graduate summary

**The complete-graph formula** [S3:37–44, S5:10]. For every
$`n\ge3`$,
$`\mathrm{cr}(K_n)={\textstyle\frac14}\lfloor
n/2\rfloor\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor
\lfloor(n-3)/2\rfloor`$. The proof has two halves: a **lower bound**
showing every drawing has at least this many crossings (via a
polynomial/intersection test on node structures), and a **matching
two-page drawing** attaining exactly the bound
[S3:37–44, S5:10, S9:76–80].

**The bipartite formula** [S4:39–47, S5:12]. For every
positive $`m,n`$,
$`\mathrm{cr}(K_{m,n})=\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor
\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor`$. Again two halves: the
**lower bound** (every admissible drawing has at least
$`\mathrm{axisPairs}\,m\times\mathrm{axisPairs}\,n`$ crossings)
and a **balanced-axis drawing** that attains it
[S4:39–47, S5:12, S8:8–11].

**The counting convention.** In both statements crossings are
**spatial points** for continuous simple edge paths, so two edges
that cross more than once contribute one crossing **per** crossing,
not per edge pair [S5:10, S5:12].

**The scope of the formalization.** Both formulas are fully
formalized: the complete-graph equality for every $`n\ge3`$ and the
bipartite equality for every positive $`m,n`$, each with its
attaining drawing, in the same spatial crossings convention
[S5:10, S5:12].

## History of the conjecture

The crossing number is a central invariant of topological graph
theory, introduced in the 1940s–50s. The Harary–Hill
formula for $`K_n`$ was conjectured in the 1960s from the geometry of
the two-page (antiprism-like) drawing, verified for small $`n`$ by
case analysis, and long believed true but unproved in general.
Turán's brickyard problem (1947) asks for the minimum
crossings of a straight-line drawing of a complete bipartite graph;
its Zarankiewicz-formulation is the arc-drawing version studied
here. Both are among the most prominent open problems in
topological combinatorics, now resolved
[S3:37–44, S4:39–47, S5:10, S5:12].

**Prior (my training data, not this repo).** I know the crossing
number, the Harary–Hill and Zarankiewicz conjectures, and
their small-$`n`$ verifications. **General** proofs of **both**
closed formulas — a lower bound plus an exact attaining
drawing, under the spatial-crossings-counting-repeats convention,
for all $`n`$ and all $`m,n`$ — go beyond the partial results I
recall; I cannot independently verify the polynomial intersection
test or the balanced-axis construction in [S3, S4] from training
alone.

## Consequences

**The Harary–Hill conjecture is proved.** For every
$`n\ge3`$, the crossing number of $`K_n`$ is exactly
$`\tfrac14\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor
\lfloor(n-2)/2\rfloor\lfloor(n-3)/2\rfloor`$
[S3:37–44, S5:10].

**The Zarankiewicz crossing-number conjecture is proved.** For
every positive $`m,n`$, the crossing number of $`K_{m,n}`$ is exactly
$`\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor\lfloor n/2\rfloor
\lfloor(n-1)/2\rfloor`$ [S4:39–47, S5:12].

**The classical drawings are optimal.** Both statements come with a
construction attaining the bound, so no drawing with continuous
edge arcs can do better [S3:37–44, S4:39–47, S5:10,
S5:12].

**The counting convention is spatial.** Repeated crossings of one
edge pair count separately, fixing the convention the formulas are
under [S5:10, S5:12].

## Section skeleton

Two manuscripts. Manuscript 1 [S3:37–44] (title [S3:32], date [S3:34])
— `main.tex` (942 lines) under `build/`, with the
`interpolation`, `two-page`, and `local-pairing` figure macros and a
`references` bibliography. Manuscript 2 [S4] (title [S4:32], date
[S4:34]) — `paper.tex` (65 lines) under `build/`, inputs the
sections `introduction`, `normalization`, `intersections`,
`subspaces`, `detector`, `conclusion`, plus the `chord-pairing` and
`triangular-grid` figure macros and a `references` bibliography. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:10, S5:12]. The first paragraph formalizes the
complete-graph formula: for every $`n\ge3`$,
$`\mathrm{cr}(K_n)={\textstyle\frac14}\lfloor
n/2\rfloor\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor
\lfloor(n-3)/2\rfloor`$, proving the lower bound and constructing a
matching two-page drawing, with crossings as spatial points so
repeated crossings of one edge pair count separately
[S5:10]. The second paragraph formalizes the bipartite formula: for
every positive $`m,n`$,
$`\mathrm{cr}(K_{m,n})=\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor
\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor`$, with the same spatial
crossing convention [S5:12]. The scope note names two comparators
[S5:16–19]: `CompleteCrossing.lean` and
`BipartiteCrossing.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 2` and `paps_form 2` — **both** manuscripts in
`formalization.yaml`'s `sources:` listing, and **both** comparators
registered. `formalization.yaml` registers
`OAI.Paper170.complete_graph_crossing_number` at
`OAI/Combinatorics/CompleteCrossing/Main.lean` and
`OAI.Zarankiewicz.mainTarget_proof` at
`OAI/Combinatorics/Crossing/Main.lean`. The two declarations live in
**two different namespaces** (`OAI.Paper170` and `OAI.Zarankiewicz`)
and in **two different packages**, so the two halves of the family
are registered independently
[S5:10, S5:12, S5:16–19].

**What the proofs do.** The bipartite declaration
`mainTarget_proof` states, for every positive $`m,n`$, that a drawing
of $`K_{m,n}`$ attaining $`\mathrm{axisPairs}\,m
\times\mathrm{axisPairs}\,n`$ crossings exists **and** that no
admissible drawing has fewer. The OAI tree proves it with a genuine
Lean proof: it takes a balanced-axis realization $`R`$ and discharges
both conjuncts from the drawing witness and the crossing lower bound


```lean
theorem mainTarget_proof : MainTarget := by
  intro m n hm hn
  obtain ⟨R⟩ := nonempty_balancedAxisRealization m n
  exact ⟨⟨R.drawing,R.crossingCount_eq⟩,crossing_lower_bound m n⟩
```
[S8:8–11]

The complete-graph declaration
`complete_graph_crossing_number` states
$`\mathrm{ordinaryCrossingNumber}(K_n)=\mathrm{hill}(n)`$ for
$`n\ge3`$, and the OAI tree proves it by antisymmetry: the upper
bound from a matching drawing $`D`$ with `crossingCount D = hill n`,
and the lower bound from the `hill n \le crossingCount D` lemma


```lean
theorem complete_graph_crossing_number (n : ℕ) (hn : 3 ≤ n) :
    ordinaryCrossingNumber (completeGraph n) = hill n := by
  obtain ⟨D, hD⟩ := complete_graph_upper_bound n hn
  apply Nat.le_antisymm
  · rw [← hD]
```
[S9:76–80]

Neither proof is a `sorry`.

**What the OAI trees do carry.** The two registered declarations
live in separate packages. The `OAI/Combinatorics/Crossing` package
(339 files over 20,617 lines, zero `sorry`) carries the bipartite
machinery (`AdmissibleDrawing`, `crossingCount`, `axisPairs`,
`nonempty_balancedAxisRealization`, `crossing_lower_bound`); the
`OAI/Combinatorics/CompleteCrossing` package (46 files over 18,046
lines, zero `sorry`) carries the complete-graph machinery
(`completeGraph`, `hill`, `node`, `polynomialTest`,
`complete_graph_upper_drawing`, `crossingTuples_card`)
[S8:8–11, S9:76–80].

**The comparator stubs.** The registered `CompleteCrossing.lean`
comparator restates `complete_graph_crossing_number` with a bare
`sorry` body 

```lean
theorem complete_graph_crossing_number (order : ℕ) (at_least_three : 3 ≤ order) :
    ordinaryCrossingNumber (completeGraph order) = hill order := by
  sorry
```
[S6:81–83]

The registered `BipartiteCrossing.lean` comparator restates
`mainTarget_proof` with a bare `sorry` [S7:60–61]. The release
records `scope: "Partial progress."` and `review: status: unchecked`;
the comparators' `sorry` bodies are the targets the release set
itself, and the proved versions in the OAI trees are the registered
results.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 165 at [S1:3886] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{165} at [S2:411] |
| S3 | [`preprints/The-crossing-number-of-complete-graphs-September-23-2026/build/main.tex`](../../../preprints/The-crossing-number-of-complete-graphs-September-23-2026/build/main.tex) | 942 | manuscript 1 (complete graphs): title [S3:32], date [S3:34], abstract [S3:37–44] |
| S4 | [`preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/build/paper.tex`](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/build/paper.tex) | 65 | manuscript 2 (complete bipartite graphs): title [S4:32], date [S4:34], abstract [S4:39–47] |
| S5 | [`lean/docs/165.md`](../../../lean/docs/165.md) | 19 | the formalization scope note: the complete-graph scope paragraph [S5:10], the bipartite paragraph [S5:12], and the comparator table [S5:16–19] |
| S6 | [`lean/ComparatorChallenges/CompleteCrossing.lean`](../../../lean/ComparatorChallenges/CompleteCrossing.lean) | 89 | registered comparator (complete): the `complete_graph_crossing_number` theorem [S6:81–82] and the `sorry` [S6:83] |
| S7 | [`lean/ComparatorChallenges/BipartiteCrossing.lean`](../../../lean/ComparatorChallenges/BipartiteCrossing.lean) | 67 | registered comparator (bipartite): the `mainTarget_proof` theorem [S7:60] and the `sorry` [S7:61] |
| S8 | [`lean/OAI/Combinatorics/Crossing/Main.lean`](../../../lean/OAI/Combinatorics/Crossing/Main.lean) | 34 | the registered bipartite declaration in the OAI tree: the real proof of `mainTarget_proof` [S8:8–11] |
| S9 | [`lean/OAI/Combinatorics/CompleteCrossing/Main.lean`](../../../lean/OAI/Combinatorics/CompleteCrossing/Main.lean) | 91 | the registered complete-graph declaration in the OAI tree: the real proof of `complete_graph_crossing_number` [S9:76–80] |
