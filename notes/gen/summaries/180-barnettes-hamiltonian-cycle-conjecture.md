[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 180](../index/combinatorics/180-barnettes-hamiltonian-cycle-conjecture.md)

# 180 — Barnette's Hamiltonian-cycle conjecture

[Index page](../index/combinatorics/180-barnettes-hamiltonian-cycle-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4188] and the catalog abstract [S2:441]
state the family's claim: every finite simple cubic bipartite
planar $`3`$-vertex-connected graph has a Hamiltonian cycle,
**resolving Barnette's conjecture**. Equivalently, every
three-edge path in a finite simple cubic $`3`$-vertex-connected
bipartite Pfaffian graph lies in a Hamiltonian cycle. The
manuscript is *Paired states and Hamiltonian cycles in cubic
bipartite planar graphs* [S3:35, S3:38]; its abstract


> We prove Barnette's conjecture: every finite simple cubic bipartite planar
$`3`$-vertex-connected graph has a Hamiltonian cycle. [S3:43–44]

## Undergraduate summary

A graph is **cubic** when every vertex has exactly three edges
meeting it, and **bipartite** when its vertices split into two
groups with edges only between the groups, so every cycle has
even length. It is **planar** when it can be drawn on a plane
with no crossing edges, and **$`3`$-vertex-connected** when
removing any two vertices leaves the graph in one piece. A
**Hamiltonian cycle** is a single cycle that visits every
vertex exactly once and returns to the start. Barnette's
conjecture, posed in 1972, asked whether every finite
simple graph with all of those properties at once must carry
such a cycle. This manuscript answers yes: the combination
"three edges per vertex, two-colourable, drawable without
crossings, hard to disconnect" forces the existence of a
single tour through every vertex [S3:43–44, S2:441].

## Graduate summary

**The main theorem** [S3:43–44, S4:9]. Every finite
simple cubic bipartite planar graph that is $`3`$-vertex-
connected has a Hamiltonian cycle. Equivalently, every
three-edge path in a finite simple cubic $`3`$-vertex-connected
bipartite **Pfaffian** graph lies in a Hamiltonian cycle
[S1:4188, S2:441]. The proof proceeds by **paired states**:
the graph's planar cubic structure is recast as an exact
dual of a network, where a connected complement of a matching
yields a $`2`$-regular subgraph whose connected component is a
cycle covering every vertex [S4:9].

**The scope of the formalization.** The scope note states the
formalization proves the Hamiltonian-cycle statement for
every such graph — the selected result is the existence
of a cycle visiting every vertex exactly once [S4:9]. The
scope note names one comparator [S4:13–15]:
`BarnetteHamiltonian.lean`.

## History of the conjecture

Barnette's conjecture is a $`1972`$ claim in the Hamiltonian-
cycle literature: the question of when a planar graph carries
a single tour of all its vertices. It was widely believed and
studied for half a century as an open problem in planar graph
theory, with partial results on related cubic planar classes
(bridgeless, snappy, etc.). It is one of the cleanest named
open problems of its era — a single sentence quantifying
four elementary graph properties. This manuscript closes it
with a self-contained argument built on **dual networks and
paired states**, translating the graph hypotheses into
connectivity statements about a complement of a matching and
extracting the spanning cycle from the resulting $`2`$-regular
subgraph [S3:43–44, S2:441].

**Prior (my training data, not this repo).** I know Barnette's
conjecture is a long-standing $`1972`$ open problem in planar
graph theory, and that many related cubic planar classes carry
Hamiltonian cycles. A **complete proof via dual-network paired
states and exact-dual matchings** that closes the general
$`3`$-vertex-connected case goes beyond what I can place from
training alone; the exact-dual construction and the
`Duality.hamiltonian` discharging lemma are not something I can
independently verify from memory.

## Consequences

**Barnette's conjecture is resolved.** Every finite simple
cubic bipartite planar $`3`$-vertex-connected graph has a
Hamiltonian cycle [S3:43–44, S4:9, S2:441].

**The equivalent Pfaffian form.** Every three-edge path in a
finite simple cubic $`3`$-vertex-connected bipartite Pfaffian
graph lies in a Hamiltonian cycle [S1:4188, S2:441].

**The method is the argument.** The proof is a
dual-network / paired-states construction, not a classical
planar-graph case split [S4:9, S6:47–82].

## Section skeleton

One manuscript [S3:43–44] (title [S3:35], date [S3:38]) —
`paper.tex` ($`837`$ lines) under `build/`. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves the
Hamiltonian-cycle statement for every finite simple cubic
bipartite planar $`3`$-vertex-connected graph; the selected
result is the existence of a cycle visiting every vertex
exactly once. The scope note names one comparator
[S4:13–15]: `BarnetteHamiltonian.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry for
this family and the manuscript is **not** in its `sources:`
listing. The comparator `BarnetteHamiltonian.lean` restates the
target `theorem main : MainStatement` with a bare `sorry` body


```lean
theorem main : MainStatement.{u} := by
  sorry
```
[S5:48–49]

**What the OAI tree does carry.** The
`OAI/Combinatorics/Hamiltonian` package (**31 files over
8,936 lines, zero `sorry`**) carries a **real, non-`sorry`**
proof of the comparator's target. The
`Main.lean` theorem `theorem main : MainStatement.{u}`
[S6:47–82] takes the graph hypotheses, constructs an
exact dual network $`D`$ of the graph's network realization $`N`$,
translates the cubic, bipartite, planar, and
$`3`$-vertex-connected hypotheses across the duality
(`hN`, `hc'`, `h3'`, `hec`, `hcolor`), and discharges the
Hamiltonian-cycle conclusion by the
`Duality.hamiltonian` lemma 

```lean
theorem main : MainStatement.{u} := by
  intro V hV dV G dG hc hb hp h3
  have hdeq : dV = Classical.decEq V := Subsingleton.elim _ _
  subst dV
  have hdrel : dG = fun a b => Classical.propDecidable (G.Adj a b) := Subsingleton.elim _ _
  subst dG
  obtain ⟨E⟩ := hp
  have hconn := h3.connected
  let : Nonempty V := hconn.nonempty
  have horder := cubic_bipartite_order hc hb
  obtain ⟨N,F,f,D,hr,hd⟩ := E.exists_exact_dual hconn
  let : Fintype F := f
  have hN : N.Simple := by
    refine ⟨hr.loopless,?_⟩
    intro e f hef
    apply Subtype.ext
    rw [← hr e,← hr f]
    exact hef
  have hc' : N.graph.IsRegularOfDegree 3 := by rw [hr.graph_eq]; exact hc
  have h3' : ThreeVertexConnected N.graph := hr.graph_eq.symm ▸ h3
  have hec : N.ThreeEdgeConnected := by
    intro A ha ho
    obtain ⟨w,hw⟩ := ho
    exact N.cut_card_three h3' (by omega) A ha ⟨w,Finset.mem_compl.mp hw⟩
  obtain ⟨color⟩ := hb
  let black : V → Prop := fun v => color v = 0
  have hcolor (e : G.edgeSet) : black (N.tail e) ↔ ¬black (N.head e) := by
    have hne := color.valid (G.mem_edgeSet.mp ((hr e).symm ▸ e.property))
    have ht := (color (N.tail e)).isLt
    have hh := (color (N.head e)).isLt
    have hne' : (color (N.tail e)).val ≠ (color (N.head e)).val := fun h => hne (Fin.ext h)
    change color (N.tail e) = 0 ↔ ¬color (N.head e) = 0
    simp only [Fin.ext_iff,Fin.val_zero]
    omega
  have hh := hd.hamiltonian N D hN hc' hec black hcolor
  rwa [hr.graph_eq] at hh
```
[S6:47–82]

The proof closes with
`exact ⟨v,p.map f,hp.map Function.bijective_id⟩`
in `Duality.hamiltonian` and `rwa [hr.graph_eq] at hh` in
`main` — a closed argument, no `sorry` [S6:47–82].

**Registration, not proof.** The OAI tree proves the
comparator's `MainStatement` in full, but the release
registered neither a `main_results` entry nor a `sources:`
listing for it — the gap between the tree and the ledger
is one of **registration**, not of proof. The comparator json
names `OAI.Combinatorics.Hamiltonian.Main` as the solution
module and `OAI.Barnette.main` as the theorem, so the release
set the target and the tree answered it; the ledger simply does
not carry that answer. The release records
`scope: "Partial progress."` and `review: status: unchecked`;
the comparator's `sorry` is the target the release set, and the
proved `main` in the OAI tree is the result the tree carries
without a ledger entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 180 at [S1:4188] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{180} at [S2:441] |
| S3 | [`preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/build/paper.tex`](../../../preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/build/paper.tex) | 837 | the single manuscript root; title [S3:35], date [S3:38], abstract [S3:43–44] |
| S4 | [`lean/docs/180.md`](../../../lean/docs/180.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/BarnetteHamiltonian.lean`](../../../lean/ComparatorChallenges/BarnetteHamiltonian.lean) | 53 | the comparator: the `MainStatement` definition [S5:42–46], the `main` theorem [S5:48] and the `sorry` [S5:49] |
| S6 | [`lean/OAI/Combinatorics/Hamiltonian/Main.lean`](../../../lean/OAI/Combinatorics/Hamiltonian/Main.lean) | 86 | the OAI tree (31 files, 8936 lines, 0 sorry): the real `main : MainStatement` proof [S6:47–82] via an exact-dual network and the `Duality.hamiltonian` lemma |
