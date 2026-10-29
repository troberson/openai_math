[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 173](../index/combinatorics/173-seymours-second-neighborhood-conjecture.md)

# 173 — Seymour's second-neighborhood conjecture

[Index page](../index/combinatorics/173-seymours-second-neighborhood-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4049] and the catalog abstract [S2:427]
state the family's claim: **Seymour's second-neighborhood
conjecture** is proved — every nonempty finite oriented graph
has a vertex with at least as many vertices at directed distance
exactly two as at directed distance one. Oriented graphs are
arbitrary apart from the exclusion of loops and oppositely directed
edge pairs. The manuscript is *A proof of Seymour's
second-neighborhood conjecture* [S3:29, S3:31]; its abstract


> We prove that every nonempty finite oriented graph has a vertex with at least
as many vertices at directed distance two as at directed distance one.
This resolves Seymour's second neighborhood conjecture positively. [S3:35–37]

## Undergraduate summary

An **oriented graph** is a directed graph with no loop (an edge
from a vertex to itself) and no two opposite edges between the same
pair. For a vertex $v$, its **first out-neighbors** are the
vertices you can reach by one directed edge; its **second
out-neighbors** are the vertices you can reach by exactly two
directed edges, excluding $v$ and its first neighbors. Seymour's
conjecture says that in any nonempty finite oriented graph, some
vertex has **at least as many** second out-neighbors as first
out-neighbors — the graph "spreads out" at the second step.
Think of a rumor going one step from a person: the number of people
who hear it at the second generation is never smaller at its best
seed. This manuscript proves that always
[S3:35–37, S2:427].

## Graduate summary

**The main theorem** [S3:35–37, S4:9]. For every nonempty
finite type $V$ and every oriented relation $r : V \to V \to
\mathrm{Prop}$ (loopless, asymmetric), there exists a vertex $v$
such that $|N_1(v)| \le |N_2(v)|$, where $N_1(v)$ is the first
out-neighborhood and $N_2(v)$ the second out-neighborhood
(vertices at directed distance exactly two, with $v$ and $N_1(v)$
excluded; sinks are included in the count) [S3:35–37, S4:9].

**The count conventions.** The second neighborhood excludes the
initial vertex and its first neighbors and counts vertices at
directed distance **exactly** two; a vertex with no out-neighbors
(a sink) has empty first neighborhood and is counted
[S4:9].

**The scope of the formalization.** The formalization proves the
full second-neighborhood assertion for arbitrary finite oriented
graphs [S4:9].

## History of the conjecture

Seymour conjectured the second-neighborhood property in the study
of directed graphs and their neighborhood expansion; it is a
natural directed analogue of minimum-degree / expansion questions.
The conjecture was verified for special classes (orientations of
trees, certain tournaments, bounded out-degree cases) and was a
standing open problem in the general finite oriented setting. This
manuscript gives the general proof, reducing a minimal counterexample
to a strict-subset growth that pruning forecloses
[S3:35–37, S2:427].

**Prior (my training data, not this repo).** I know the name
Seymour's second-neighborhood conjecture and its statement. A
**general finite** proof, via a counterexample-reduction to a
strict-subset-growth contradiction with an extremal pruning
argument, goes beyond the special cases I recall; I cannot
independently verify the reduction / pruning machinery in [S3:35–37]
from training alone.

## Consequences

**Seymour's second-neighborhood conjecture is resolved.** Every
nonempty finite oriented graph has a vertex with at least as many
second out-neighbors as first out-neighbors [S3:35–37,
S4:9, S2:427].

**The result is unrestricted in the graph.** Only the oriented
condition (no loops, no opposite-edge pairs) is required; the
graph may otherwise be arbitrary [S1:4049, S4:9].

**The second-neighborhood count is fixed.** Distance exactly two,
excluding the vertex and first neighbors, including sinks
[S4:9].

## Section skeleton

One manuscript [S3:35–37] (title [S3:29], date [S3:31]) —
`main.tex` (47 lines) under `build/source/`, inputs the sections
`00-introduction`, `01-reduction`, `02-pruning`,
`03-incompatibility`, `04-weighted-consequences`,
`05-directed-cycle-consequences`, plus a `references`
bibliography. The family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves that every
nonempty finite oriented graph has a vertex with at least as many
second out-neighbors as first out-neighbors, where the second
neighborhood consists of vertices at directed distance exactly two,
with the initial vertex and first neighbors excluded and sinks
included [S4:9]. The scope note names one comparator
[S4:13–15]: `SeymourSecondNeighborhood.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml`
registers one `main_results` entry — the
`OAI.SeymourSecondNeighborhood.exists_goodVertex` declaration at
`OAI/Combinatorics/SecondNeighborhood/Main.lean` — and one
manuscript is in its `sources:` listing. The registered
declaration is exactly the conjecture: a good vertex (first
neighborhood at most the second) exists [S4:9, S4:13–15].

**The comparator stub.** The `SeymourSecondNeighborhood.lean`
comparator restates the target `theorem exists_goodVertex` with a
bare `sorry` body 

```lean
theorem exists_goodVertex (r : V → V → Prop) (hr : IsOriented r) :
    ∃ v, GoodVertex r v := by
  sorry
```
[S5:34–36]

**What the proof does.** The registered `exists_goodVertex` in the
OAI tree is a genuine proof, not a `sorry`: it argues by
contradiction, converting a putative counterexample into one
(`counterexample_iff_not_conjecture`), reducing it to a minimal
growth instance (`counterexample_reduction`), and discharging the
growth with the extremal no-strict-subset-growth pruning lemma
[Extremal.no_strictSubsetGrowth_of_pruning]


```lean
theorem exists_goodVertex (r : V → V → Prop) (hr : IsOriented r) :
    ∃ v, GoodVertex r v := by
  classical
  by_contra h
  have hcounter : Counterexample r := (counterexample_iff_not_conjecture r).mpr h
  obtain ⟨n, hn, g, hg, hpos, hgrowth⟩ := counterexample_reduction hr hcounter
  let : Nonempty (Fin n) := ⟨⟨0, hn⟩⟩
  exact Extremal.no_strictSubsetGrowth_of_pruning hg hpos (Pruning.pruning g) hgrowth
```
[S6:11–18]

The proof ends `exact
Extremal.no_strictSubsetGrowth_of_pruning hg hpos
(Pruning.pruning g) hgrowth` — a closed contradiction, no
`sorry` [S6:16–18].

**What the OAI tree does carry.** The
`OAI/Combinatorics/SecondNeighborhood` package (43 files over 4,861
lines, zero `sorry`) carries the supporting machinery: the
`Counterexample` type and `counterexample_iff_not_conjecture`,
`counterexample_reduction` (the minimal-instance reduction), the
`Pruning.pruning` construction, and the `Extremal` no-strict-
subset-growth contradiction that `exists_goodVertex` assembles
[S6:11–18].

The release records `scope: "Partial progress."` and
`review: status: unchecked`; the comparator's `sorry` is the target
the release set, and the proved `exists_goodVertex` in the OAI tree
is the registered result.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 173 at [S1:4049] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{173} at [S2:427] |
| S3 | [`preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/source/main.tex`](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/source/main.tex) | 47 | the single manuscript root; title [S3:29], date [S3:31], abstract [S3:35–37] |
| S4 | [`lean/docs/173.md`](../../../lean/docs/173.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/SeymourSecondNeighborhood.lean`](../../../lean/ComparatorChallenges/SeymourSecondNeighborhood.lean) | 40 | the comparator: the `exists_goodVertex` theorem [S5:34–35] and the `sorry` [S5:36] |
| S6 | [`lean/OAI/Combinatorics/SecondNeighborhood/Main.lean`](../../../lean/OAI/Combinatorics/SecondNeighborhood/Main.lean) | 22 | the registered declaration in the OAI tree: the real `exists_goodVertex` proof [S6:11–18] closing by a counterexample-reduction / pruning contradiction |
