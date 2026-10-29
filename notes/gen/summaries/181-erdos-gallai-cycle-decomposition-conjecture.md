[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 181](../index/combinatorics/181-erdos-gallai-cycle-decomposition-conjecture.md)

# 181 — The Erdős–Gallai cycle-decomposition conjecture

[Index page](../index/combinatorics/181-erdos-gallai-cycle-decomposition-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4204] and the catalog abstract [S2:443]
state the family's claim: the edges of every finite simple
undirected graph on $n$ vertices can be partitioned into at
most $Cn$ simple cycles and single edges, for an absolute
constant $C$, **resolving the Erd–Gallai
cycle-decomposition conjecture**. The manuscript is *A linear
cycle-and-edge decomposition of every graph* [S3:40, S3:42];
its abstract 

> We prove that every finite simple undirected graph on $n$ vertices
has an edge partition into at most $Cn$ simple cycles and single
edges, for an absolute constant $C$. This resolves the
Erdős–Gallai cycle decomposition conjecture positively. [S3:48–51]

## Undergraduate summary

A graph's **edges** are its connections, and a **cycle** is a
closed path that visits each of its own vertices once and
returns to the start. A **decomposition** of a graph's edges is
a way to split every edge into exactly one piece so that no
edge appears in two pieces. This manuscript bounds the number
of pieces needed: take any finite simple graph — the
simplest kind, with no loops and no multiple edges — on
$n$ vertices, and its whole edge set can be cut into at most
$Cn$ pieces, each piece either a single cycle or a single
edge, where $C$ is one fixed constant that works for every
graph in the class [S3:48–51, S2:443]. The conjecture
asked for a bound that grew **linearly** in the number of
vertices, not quadratically as the total edge count can be;
the manuscript supplies it, even for the **dense** graphs with
as many as $\binom{n}{2}$ edges [S2:443].

## Graduate summary

**The main theorem** [S3:48–51, S4:9]. There is an
absolute constant $C > 0$ such that every finite simple
undirected graph on $n$ vertices has an edge-disjoint
decomposition into at most $Cn$ pieces, each a simple cycle or
a singleton edge [S4:9]. Edgeless and small graphs are
included; the bound is uniform over all $n$. The Erd–
Gallai cycle-decomposition conjecture, which asked for
precisely this linear bound, is resolved positively
[S2:443].

**The method.** The proof is a **scale-hierarchy** argument:
the graph is peeled layer by layer across geometric scales,
and a **layer-cost** accounting bounds the total number of
pieces by a linear function of the vertex count. The constant
$C$ is produced by a `main_cost_bound` constant whose value
the argument carries rather than specifies [S4:9,
S6:207–216].

**The scope of the formalization.** The scope note states the
formalized result gives one absolute constant $C > 0$ with
the $Cn$ bound, includes edgeless and small graphs, but does
not determine the **optimal** value of $C$ [S4:9]. The scope
note names one comparator [S4:13–15]:
`CycleDecomposition.lean`.

## History of the conjecture

The Erd–Gallai cycle-decomposition question is a
decomposition problem in extremal graph theory, named for two
of the field's founders. The naive bound is trivial: take
every edge as its own piece, giving $\binom{n}{2}$ pieces in
a dense graph. The conjecture asked for a **linear** number
of cycles plus single edges — a bound that stays
proportional to $n$ even as the edge count reaches
$\Theta(n^2)$. Such bounds matter because the number of
cycles needed to cover a graph's edges is a basic measure of
its **cycle-structure complexity**, with applications in
edge-coloring, traffic assignment, and graph decomposition
theory. This manuscript closes the question by producing the
absolute constant $C$ with a scale-hierarchy layer-cost
argument, bounding the piece count linearly for all finite
simple graphs including the densest [S3:48–51, S2:443].

**Prior (my training data, not this repo).** I know the
Erd–Gallai cycle-decomposition conjecture as a named
open problem in extremal graph theory, and that cycle
decomposition bounds are a classical theme. A **complete
linear bound via scale-hierarchy peeling with an explicit
cost accounting** resolving the general finite-simple-graph
case goes beyond what I can place from training alone; the
layer-cost machinery and the `main_cost_bound` constant in
[S6:207–216] are not something I can independently verify from memory.

## Consequences

**The Erd–Gallai cycle-decomposition conjecture is
resolved.** Every finite simple undirected graph on $n$
vertices decomposes into at most $Cn$ cycles and single edges
for an absolute constant $C$ [S3:48–51, S4:9, S2:443].

**The bound is linear, not quadratic.** The piece count stays
proportional to the vertex count even for the densest graphs
with $\Theta(n^2)$ edges [S2:443].

**The constant is existential.** The argument produces the
constant $C$ without determining its optimal value
[S4:9, S6:207–216].

## Section skeleton

One manuscript [S3:48–51] (title [S3:40], date [S3:42]) —
`main.tex` ($260$ lines) under `build/`, with a `references`
bibliography and a `figures` directory. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized result gives one
absolute constant $C > 0$ such that every finite simple graph
on $n$ vertices has an edge-disjoint decomposition into at
most $Cn$ cycles or singleton edges; edgeless and small
graphs are included. The **optimal value of $C$ is not
determined** — an open parameter, not a scope gap, since
the formalized statement carries the full existential
[S4:9]. The scope note names one comparator
[S4:13–15]: `CycleDecomposition.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml`
registers one `main_results` entry — the
`OAI.ErdosGallai.erdos_gallai` declaration at
`OAI/Combinatorics/CycleDecomposition/Main.lean` — and
the one manuscript is in its `sources:` listing. The
comparator `CycleDecomposition.lean` is registered
[S4:9, S4:13–15].

**The comparator stub.** The comparator restates the target
`theorem erdos_gallai : MainStatement` with a bare `sorry`
body 

```lean
def MainStatement : Prop :=
  ∃ C : ℝ, 0 < C ∧ ∀ (n : ℕ) (G : SimpleGraph (Fin n)),
    ∃ k : ℕ, EdgeDecomposition G k ∧ (k : ℝ) ≤ C * n

theorem erdos_gallai : MainStatement := by
  sorry
```
[S5:27–32]

**What the proof does.** The registered `erdos_gallai` in the
OAI tree is a genuine proof, not a `sorry`: it obtains the
`main_cost_bound` constant $C$, then for a given $n$ and
graph $G$ witnesses the decomposition via
`decompositionCost G`, translates the cost bound across the
cardinality identification, and discharges the linear
inequality by `nlinarith` against the induction-$\Phi$
bounds 

```lean
theorem erdos_gallai : MainStatement := by
  obtain ⟨C,hC,hcost⟩ := main_cost_bound
  refine ⟨C,hC,?_⟩
  intro n G
  refine ⟨decompositionCost G,decompositionCost_spec G,?_⟩
  have hh := hcost (Fin n) G
  simp only [Fintype.card_fin] at hh
  have hp := mul_le_mul_of_nonneg_left (Batch.inductionPhi_bounds n).2
    (mul_nonneg hC.le (Nat.cast_nonneg n : (0:ℝ) ≤ _))
  nlinarith only [hh,hp]
```
[S6:207–216]

The proof closes with `nlinarith only [hh,hp]` — a
linear bound discharged by the linear-arithmetic tactic, no
`sorry` [S6:207–216].

**What the OAI tree does carry.** The
`OAI/Combinatorics/CycleDecomposition` package (**34 files
over 21,451 lines, zero `sorry`**) carries the full
scale-hierarchy machinery: the `Layers` and `LayerCosts`
accounting, the `PrefixSelection` prefix bound, the
`Batch*` peeling and resolution lemmas, the `ScaleHierarchy`
geometry, and the `main_cost_bound` constant that
`erdos_gallai` assembles [S6:207–216].

**The open parameter.** The scope note records that the
optimal value of $C$ is not determined [S4:9]. The
formalization proves the **existential** — that some
absolute $C$ works — and its `main_cost_bound`
supplies one, but it does not sharpen $C$ to a best
constant. The release records `scope: "Partial progress."`
and `review: status: unchecked`; the comparator's `sorry` is
the target the release set, and the proved `erdos_gallai` in
the OAI tree is the registered result.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 181 at [S1:4204] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{181} at [S2:443] |
| S3 | [`preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/build/main.tex`](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/build/main.tex) | 260 | the single manuscript root; title [S3:40], date [S3:42], abstract [S3:48–51] |
| S4 | [`lean/docs/181.md`](../../../lean/docs/181.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/CycleDecomposition.lean`](../../../lean/ComparatorChallenges/CycleDecomposition.lean) | 38 | the comparator: the `MainStatement` definition [S5:27–29], the `erdos_gallai` theorem [S5:31] and the `sorry` [S5:32] |
| S6 | [`lean/OAI/Combinatorics/CycleDecomposition/Main.lean`](../../../lean/OAI/Combinatorics/CycleDecomposition/Main.lean) | 226 | the registered declaration in the OAI tree (34 files, 21451 lines, 0 sorry): the real `erdos_gallai` proof [S6:207–216] via the `main_cost_bound` constant and a `nlinarith` discharge |
