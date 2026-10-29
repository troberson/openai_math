[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 184](../index/combinatorics/184-coloring-and-independence-in-graphs-with-forbidden-subgraphs.md)

# 184 — Coloring and independence in graphs with forbidden subgraphs

[Index page](../index/combinatorics/184-coloring-and-independence-in-graphs-with-forbidden-subgraphs.md)

## Original CONTENTS.md summary

The release's blurb [S1:4270] and the catalog abstract [S2:449]
state the family's dual claim. **First**, the
Alon–Krivelevich–Sudakov coloring conjecture in
correspondence-coloring form: graphs avoiding any fixed
subgraph $`F`$ need $`O_F(\Delta/\log\Delta)`$ colors when
their maximum degree $`\Delta`$ is sufficiently large.
**Second**, the Ajtai–Erd–Koml–Szemeríi independence
conjecture: for fixed $`r \geq 4`$, every $`n`$-vertex
$`K_r`$-free graph of average degree $`d \geq 2`$ has an
independent set of size $`\Omega_r(n\log d/d)`$. The family
ships two manuscripts [S1:4270]:

- *Correspondence coloring graphs with a forbidden clique*
  [S3:3, S3:5]
- *A logarithmic independence bound for clique-free graphs*
  [S4:6, S4:8]

The independence abstract 

> For every fixed integer $`r\ge4`$, every $`K_r`$-free graph on $`n`$ vertices
with average degree $`d\ge2`$ has an independent set of size at least
$`c_r n\log d/d`$, where $`c_r>0`$ depends only on $`r`$.
This proves the fixed-clique-size independence conjecture of Ajtai,
Erdős, Komlós and Szemerédi. [S4:12–16]

## Undergraduate summary

A graph's **chromatic number** is the fewest colors needed to
paint its vertices so that no edge joins two same-colored
vertices. A **correspondence** (or list) coloring adds a twist:
each vertex carries its own list of allowed colors, and each
edge forbids specific *pairs* of colors between its endpoints,
so the coloring rules can vary from edge to edge. A
**$`K_r`$-free** graph is one that contains no complete
$`r`$-clique on $`r`$ mutually-adjacent vertices. An
**independent set** is a group of vertices with no edges
between them. The independence result says: in a large graph
that has no $`r`$-clique, you can always find a fairly large
set of non-adjacent vertices — and the size of that set
grows when you divide by the graph's average degree and
multiply by its logarithm [S4:12–16, S2:449]. The
coloring result says the same sparsity (no fixed forbidden
subgraph) forces the graph to be colorable with only
order $`\Delta/\log\Delta`$ colors [S3:9–15].

## Graduate summary

**The independence conjecture** [S4:12–16, S5:9]. For
every fixed integer $`r \geq 4`$ there is $`c_r > 0`$ such that
every finite $`K_r`$-free simple graph on $`n`$ vertices with
average degree $`d \geq 2`$ has an independent set of size at
least $`c_r n \log d / d`$. The constant $`c_r`$ depends only on
$`r`$ [S5:9]. This proves the fixed-clique-size independence
conjecture of Ajtai, Erd–Koml–Szemeríi
[S4:12–16].

**The coloring conjecture** [S3:9–15]. For every fixed
integer $`r \geq 4`$, every $`K_r`$-free graph of sufficiently
large maximum degree $`\Delta`$ has correspondence chromatic
number $`O_r(\Delta/\log\Delta)`$, resolving the
Alon–Krivelevich–Sudakov coloring conjecture in the
stronger correspondence-coloring form; the same bound, with a
constant depending on $`F`$, holds when any fixed graph $`F`$ is
excluded as an ordinary subgraph, and ordinary and list
coloring satisfy the same bounds [S3:9–15].

**The scope of the formalization.** The scope note states the
formalized result is the logarithmic improvement in the
independence number of clique-free graphs — the
$`c_r n \log d / d`$ bound with $`c_r`$ depending only on $`r`$
[S5:9]. The scope note names one comparator
[S5:13–15]: `CliqueFreeLog.lean`.

## History of the conjecture

The Ajtai–Erd–Koml–Szemeríi independence
conjecture and the Alon–Krivelevich–Sudakov
coloring conjecture are two of the central open problems in
extremal and structural graph theory, both asking how the
absence of a fixed forbidden structure forces a graph to be
sparse in a quantitative way. The Erd–Renyi-Sel
random-graph heuristic predicted logarithmic corrections in
both the independence and the coloring problems, and the
conjectures assert those corrections are real, not just
heuristic. The correspondence (list) form of the coloring
conjecture is strictly stronger than the ordinary form,
because each edge may carry its own forbidden pair. This
manuscript pair closes both: the independence bound with a
constant depending only on the clique size, and the coloring
bound in the strongest correspondence form, uniformly over
all fixed forbidden subgraphs
[S3:9–15, S4:12–16, S2:449].

**Prior (my training data, not this repo).** I know both the
Ajtai–Erd–Koml–Szemeríi and the
Alon–Krivelevich–Sudakov conjectures as named open
problems in extremal graph theory, and that the
Erd–Renyi-Sel heuristic predicts logarithmic corrections
here. **Complete proofs** of both — the independence
bound with a $`c_r`$ depending only on $`r`$, and the coloring
bound in correspondence form uniformly over forbidden
subgraphs — go beyond what I can place from training
alone; the `exists_optimizer_triangle_bound` and
`maximum_degree_independence` machinery in [S7:22–82] is not
something I can independently verify from memory.

## Consequences

**The Ajtai–Erd–Koml–Szemeríi
independence conjecture is resolved.** Every $`n`$-vertex
$`K_r`$-free graph of average degree $`d \geq 2`$ has an
independent set of size $`\Omega_r(n\log d/d)`$
[S4:12–16, S5:9, S2:449].

**The Alon–Krivelevich–Sudakov coloring
conjecture is resolved in correspondence form.** $`K_r`$-free
graphs of large maximum degree need $`O_r(\Delta/\log\Delta)`$
correspondence colors, and the same holds for any fixed
forbidden subgraph $`F`$ [S3:9–15, S2:449].

**The coloring result is in the strongest form and is
uniform.** Ordinary, list, and correspondence coloring satisfy
the same bound, uniformly over all fixed forbidden subgraphs
[S3:9–15].

## Section skeleton

Two manuscripts: [S3] (title [S3:3], date [S3:5]) —
`main.tex` (25 lines) under `build/`; [S4:12–16] (title [S4:6],
date [S4:8]) — `main.tex` (29 lines) under `build/`. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalized result gives a
logarithmic improvement in the independence number of
clique-free graphs: for every fixed $`r \geq 4`$ there is
$`c_r > 0`$ such that every finite $`K_r`$-free simple graph on
$`n`$ vertices with average degree $`d \geq 2`$ has an
independent set of size at least $`c_r n \log d / d`$, with
$`c_r`$ depending only on $`r`$ [S5:9]. The scope note names one
comparator [S5:13–15]: `CliqueFreeLog.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml`
registers one `main_results` entry — the
`OAI.CliqueFreeLog.logarithmic_independence_bound`
declaration at `OAI/Combinatorics/CliqueFree/Main.lean`
— and the independence manuscript is in its `sources:`
listing. The **correspondence-coloring** manuscript
[S3] is the unregistered half: it has no comparator and no
`main_results` entry
[S3:9–15, S5:9, S5:13–15].

**The comparator stub.** The `CliqueFreeLog.lean` comparator
defines `averageDegree` and restates the target
`theorem logarithmic_independence_bound` with a bare `sorry`
body [S6:7–17]:

```lean
theorem logarithmic_independence_bound (r : ℕ) (hr : 4 ≤ r) :
    ∃ c : ℝ, 0 < c ∧
      ∀ {V : Type} [Fintype V] (G : SimpleGraph V),
        G.CliqueFree r → 2 ≤ averageDegree G →
        c * (Fintype.card V : ℝ) * Real.log (averageDegree G) / averageDegree G ≤
          (G.indepNum : ℝ) := by
  sorry
```
[S6:11–17]

**What the proof does.** The registered
`logarithmic_independence_bound` in the OAI tree is a genuine
proof, not a `sorry`: it obtains the
`exists_optimizer_triangle_bound` constant $`B`$, sets
$`D = 3 + 3B/2`$, and witnesses $`c = 1/(16D)`$; for a given
$`K_r`$-free graph of average degree $`d`$, it cuts the graph to
the set $`A`$ of low-degree vertices (at least $`n/2`$ of them),
transfers the $`K_r`$-freedom and the $`2d`$ degree bound to the
induced subgraph, applies `maximum_degree_independence`, and
discharges the logarithmic comparison by `nlinarith`


```lean
theorem logarithmic_independence_bound (r : ℕ) (hr : 4 ≤ r) :
    ∃ c : ℝ, 0 < c ∧
      ∀ {V : Type} [Fintype V] (G : SimpleGraph V),
        G.CliqueFree r → 2 ≤ averageDegree G →
        c * (Fintype.card V : ℝ) * Real.log (averageDegree G) / averageDegree G ≤
          (G.indepNum : ℝ) := by
  classical
  obtain ⟨B,hB,htri⟩ := exists_optimizer_triangle_bound.{0} (r-2)
  let D : ℝ := 3+3*B/2
  have hD : 0 < D := by dsimp [D]; positivity
  refine ⟨1/(16*D),by positivity,?_⟩
  intro V _ G hf hd
  let d : ℝ := averageDegree G
  have hd2 : 2 ≤ d := hd
  have hdpos : 0 < d := by linarith
  have hn : (Fintype.card V : ℝ) ≠ 0 := by
    intro hn
    have hz : averageDegree G = 0 := by simp [averageDegree,hn]
    rw [hz] at hd
    norm_num at hd
  have hsum : (∑ v, (G.degree v : ℝ)) = (Fintype.card V : ℝ)*d := by
    rw [sum_degrees_real]
    dsimp [d, averageDegree]
    field_simp
  let A : Finset V := univ.filter fun v ↦ (G.degree v : ℝ) ≤ 2*d
  have hAcard : (Fintype.card V : ℝ)/2 ≤ (Fintype.card (A : Set V) : ℝ) := by
    have he : Fintype.card (A : Set V) = A.card := Fintype.card_coe A
    rw [he]
    exact degree_cutoff_card G hdpos hsum
  have hk : r-2+2 = r := Nat.sub_add_cancel (by omega)
  have hfree : (G.induce (A : Set V)).CliqueFree (r-2+2) := by
    rw [hk]
    exact (G.cliqueFree_induce_iff _ _).2 hf.cliqueFreeOn
  have hdeg (v : (A : Set V)) : ((G.induce (A : Set V)).degree v : ℝ) ≤ 2*d := by
    have hv : (G.degree v : ℝ) ≤ 2*d := (mem_filter.1 v.property).2
    exact (Nat.cast_le.2 (degree_induce_le G A v)).trans hv
  have hmax := maximum_degree_independence (r-2) hB.le (by linarith : 3 ≤ 2*d)
    htri (G.induce (A : Set V)) hfree hdeg
  have hi : ((G.induce (A : Set V)).indepNum : ℝ) ≤ G.indepNum :=
    Nat.cast_le.2 (indepNum_induce_le G A)
  have hlog : Real.log d ≤ Real.log (2*d) :=
    Real.log_le_log hdpos (by linarith)
  have hlog0 : 0 ≤ Real.log d := Real.log_nonneg (by linarith)
  have hnum : (Fintype.card V : ℝ)*Real.log d/2 ≤
      (Fintype.card (A : Set V) : ℝ)*Real.log (2*d) := by
    have h1 := mul_le_mul_of_nonneg_right hAcard hlog0
    have h2 := mul_le_mul_of_nonneg_left hlog (Nat.cast_nonneg (α := ℝ) (Fintype.card (A : Set V)))
    nlinarith
  have hden : 0 < 8*D*d := by positivity
  have hcompare := div_le_div_of_nonneg_right hnum hden.le
  change (Fintype.card (A : Set V) : ℝ)*Real.log (2*d)/(4*D*(2*d)) ≤ _ at hmax
  have heq : (1/(16*D))*(Fintype.card V : ℝ)*Real.log d/d =
      ((Fintype.card V : ℝ)*Real.log d/2)/(8*D*d) := by
    field_simp
    ring
  change (1/(16*D))*(Fintype.card V : ℝ)*Real.log d/d ≤ _
  rw [heq]
  apply hcompare.trans
  have hdeneq : 8*D*d = 4*D*(2*d) := by ring
  rw [hdeneq]
  exact hmax.trans hi
```
[S7:22–82]

The proof closes with `exact hmax.trans hi` — the
induced-subgraph independence bound transferred up to the
whole graph, no `sorry` [S7:22–82].

**What the OAI tree does carry.** The
`OAI/Combinatorics/CliqueFree` package (**31 files over 5,539
lines, zero `sorry`**) carries the supporting machinery:
the `MaxDegree` optimizer and `exists_optimizer_triangle_bound`
constant, the `degree_cutoff_card` low-degree set bound, the
`maximum_degree_independence` independence lemma, and the
`averageDegree` definition that `logarithmic_independence_bound`
assembles [S7:22–82].

**The unregistered coloring result.** The correspondence-
coloring manuscript [S3] proves the
Alon–Krivelevich–Sudakov bound in correspondence
form for every fixed forbidden subgraph [S3:9–15], but
it carries **no comparator and no registration** — it is
outside the formalization entirely. The release records
`scope: "Partial progress."` and `review: status: unchecked`;
the comparator's `sorry` is the target the release set for the
independence half, and the proved
`logarithmic_independence_bound` in the OAI tree is the
registered result.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 184 at [S1:4270] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{184} at [S2:449] |
| S3 | [`preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/build/main.tex`](../../../preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/build/main.tex) | 25 | manuscript 1 of 2: correspondence coloring with a forbidden clique (UNREGISTERED); title [S3:3], date [S3:5], abstract [S3:9–15] |
| S4 | [`preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/build/main.tex`](../../../preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/build/main.tex) | 29 | manuscript 2 of 2: the logarithmic independence bound (REGISTERED); title [S4:6], date [S4:8], abstract [S4:12–16] |
| S5 | [`lean/docs/184.md`](../../../lean/docs/184.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:13–15] |
| S6 | [`lean/ComparatorChallenges/CliqueFreeLog.lean`](../../../lean/ComparatorChallenges/CliqueFreeLog.lean) | 21 | the comparator: the `averageDegree` definition [S6:7–9], the `logarithmic_independence_bound` theorem [S6:11–16] and the `sorry` [S6:17] |
| S7 | [`lean/OAI/Combinatorics/CliqueFree/Main.lean`](../../../lean/OAI/Combinatorics/CliqueFree/Main.lean) | 88 | the registered declaration in the OAI tree (31 files, 5539 lines, 0 sorry): the real `logarithmic_independence_bound` proof [S7:22–82] via the `exists_optimizer_triangle_bound` constant, a degree cutoff, and `maximum_degree_independence` |
