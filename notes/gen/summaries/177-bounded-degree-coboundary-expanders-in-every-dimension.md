[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 177](../index/combinatorics/177-bounded-degree-coboundary-expanders-in-every-dimension.md)

# 177 — Bounded-degree coboundary expanders in every dimension

[Index page](../index/combinatorics/177-bounded-degree-coboundary-expanders-in-every-dimension.md)

## Original CONTENTS.md summary

The release's blurb [S1:4140] and the catalog abstract [S2:435]
state the family's claim: for every $`d \ge 3`$ there exist
arbitrarily large finite $`d`$-dimensional simplicial complexes with
**uniformly bounded vertex degrees** and **uniform
$`\mathbb F_2`$ coboundary expansion in every degree below
$`d`$**. Together with the known graph ($`d=1`$) and two-dimensional
($`d=2`$) cases, this establishes the existence of bounded-degree
$`\mathbb F_2`$ coboundary expanders in **every positive
dimension**. The manuscript is *Bounded-degree coboundary
expanders in every dimension* [S3:62, S3:64]; its abstract


> For every integer $`d\ge3`$, we construct arbitrarily large finite
$`d`$-dimensional simplicial complexes with uniformly bounded vertex degrees
and uniform $`\mathbb F_2`$ coboundary expansion in every degree below $`d`$.
Together with the known graph and two-dimensional cases, this establishes
the existence of bounded-degree $`\mathbb F_2`$ coboundary expanders in every
positive dimension. [S3:68–73]

## Undergraduate summary

A **simplicial complex** is a collection of triangles,
tetrahedra, and higher-dimensional faces glued together along
their faces, where if a face is present so are all of its
sub-faces. **Coboundary expansion** is a way of saying the complex
"is connected" at every level: a function on the faces (a
**cochain**) that is far from being a pure coboundary (the
discrete analogue of an exact differential) must have a coboundary
that is itself large — there is no way to hide a
large signal by taking derivatives. **Bounded degree** means each
vertex sits in at most a fixed number of top-dimensional faces,
so the complex is locally small. The result says such
locally-small complexes with strong expansion at every level
exist in every dimension $`d \ge 3`$ — a higher-dimensional
analogue of expander graphs, where $`d=1`$ is just an expander
graph [S3:68–73, S2:435].

## Graduate summary

**The main theorem** [S3:68–73, S4:9]. For every $`d \ge 3`$
there is a sequence of finite pure connected $`d`$-dimensional
simplicial complexes $`X_m`$ such that: (i) the vertex counts tend
to infinity; (ii) every vertex lies in at most $`D`$ top-dimensional
faces, for a single uniform $`D`$; and (iii) there is a positive
constant $`\varepsilon`$ such that in every degree $`i < d`$ and for
every cochain $`f`$,
$`\varepsilon \, \mathrm{dist}(f, \mathrm{Coboundaries}_i)
\le \|\delta f\|`$,
where the distance and norm use the weighted support norm
[induces the expansion constant]. The constants $`D`$ and
$`\varepsilon`$ may depend on $`d`$ [S4:9].

**The all-positive-dimensions conclusion.** The graph
($`d=1`$) and two-dimensional ($`d=2`$) cases are known separately;
this manuscript supplies $`d \ge 3`$, so together they give
bounded-degree $`\mathbb F_2`$ coboundary expanders in every
positive dimension [S3:68–73, S4:9].

**The scope of the formalization.** The scope note states the
formalization constructs the $`d \ge 3`$ expanders, with the
graph and two-dimensional cases carried separately and
**outside** the formalization [S4:9]. The scope note names one
comparator [S4:15]: `CoboundaryExpanders.lean`.

## History of the conjecture

Coboundary expansion in higher-dimensional complexes is the
discrete-hodge-theory analogue of spectral-gap /
Cheeger-type expansion for graphs. The $`d=1`$ case is the
classical expander-graph program (Ramanujan graphs,
Alon-Boppana, etc.); the $`d=2`$ case was established by work on
higher-order expanders. The open problem was to build such
families with **uniformly bounded degree** in **every** $`d \ge
3`$ — a requirement that rules out many naive constructions
whose local degree blows up with the dimension. This manuscript
gives the $`d \ge 3`$ construction, closing the all-positive-
dimensions picture [S3:68–73, S2:435].

**Prior (my training data, not this repo).** I know
higher-order / coboundary expanders and the bounded-degree
requirement, and the $`d=1`$ expander-graph literature. A
**uniformly-bounded-degree, all-degrees-below-$`d`$**
construction for every $`d \ge 3`$ via an infinite-coset and
cosystolic machinery with a gamma-vanishing argument goes
beyond what I can place from training alone; the specific
complexes and the expansion constant's dependence on $`d`$ are not
something I can independently reconstruct.

## Consequences

**Bounded-degree coboundary expanders exist in every $`d \ge 3`$.**
For each such $`d`$, arbitrarily large finite $`d`$-dimensional
complexes with a uniform top-degree bound and a positive
expansion constant in every degree below $`d`$ [S3:68–73,
S4:9, S2:435].

**The all-positive-dimensions picture is complete.** Combined with
$`d=1`$ (graphs) and $`d=2`$, bounded-degree $`\mathbb F_2`$
coboundary expanders exist in every positive dimension
[S3:68–73, S4:9].

**The constants may depend on $`d`$.** The uniformity is in the
sequence (over $`m`$), not across dimensions [S4:9].

## Section skeleton

One manuscript [S3:68–73] (title [S3:62], date [S3:64]) —
`main.tex` (82 lines) under `build/source/`, inputs sections
`introduction`, `construction`, `geometry`, `homology`,
`expansion`, plus a `references` bibliography. The family ships
no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization constructs bounded-degree
$`\mathbb F_2`$ coboundary expanders in every dimension
$`d \ge 3`$: for each such $`d`$, finite pure connected
$`d`$-dimensional simplicial complexes with vertex counts tending
to infinity, one uniform bound on top-dimensional degree at each
vertex, and one positive coboundary-expansion constant in every
degree below $`d`$, with the constants allowed to depend on $`d`$.
The graph and two-dimensional cases used for the paper's
all-positive-dimensions conclusion are separate [S4:9]. The scope
note names one comparator [S4:15]: `CoboundaryExpanders.lean`.

**The structural absence.** The family is at tier T2: the ledger
row records `mainres 0` and `paps_form 0`. `formalization.yaml`
carries **no** `main_results` entry for this family and the
manuscript is **not** in its `sources:` listing. The comparator
`CoboundaryExpanders.lean` restates the target
`theorem main : MainStatement` with a bare `sorry` body


```lean
theorem main : MainStatement := by
  sorry
```
[S5:91–92]

**What the OAI tree does carry.** The
`OAI/Combinatorics/Coboundary` package (**15 files over 11,206
lines, zero `sorry`**) carries a **real, non-`sorry`** proof of the
comparator's target. The registered-in-name
`Main.lean` theorem
`theorem main : MainStatement` [S6:88–112] reduces to the
positive open inputs, extracts a uniform infinite-coset positive
witness, an actual uniform cosystolic witness, a gamma-vanishing
witness, and an infinite supply of odd primes large enough to
separate them, then discharges both degree cases
($`2d-1`$ and $`2d+1`$) by target-vanishing 

```lean
theorem main : MainStatement := by
  apply reduction_to_positive_open_inputs
  intro d hd
  obtain ⟨Q₁,hQ₁⟩ := uniform_infinite_coset_positive (2*d) (by omega)
  obtain ⟨Q₂,hQ₂⟩ := actual_uniform_cosystolic (2*d) (by omega)
  obtain ⟨Q₃,hQ₃⟩ := uniform_gamma_vanishing (2*d+1)
  obtain ⟨p,hbound,hp⟩ := Nat.exists_infinite_primes (max 3 (max Q₁ (max Q₂ Q₃))+1)
  have hQ : max 3 (max Q₁ (max Q₂ Q₃)) < p := by omega
  have hp2 : p ≠ 2 := by have := le_max_left 3 (max Q₁ (max Q₂ Q₃)); omega
  have ho : Odd p := hp.odd_of_ne_two hp2
  let : Fact p.Prime := ⟨hp⟩
  have h₁ : Q₁ < p := lt_of_le_of_lt ((le_max_left _ _).trans (le_max_right _ _)) hQ
  have h₂ : Q₂ < p := lt_of_le_of_lt
    ((le_max_left _ _).trans ((le_max_right _ _).trans (le_max_right _ _))) hQ
  have h₃ : Q₃ < p := lt_of_le_of_lt
    ((le_max_right _ _).trans ((le_max_right _ _).trans (le_max_right _ _))) hQ
  refine ⟨p,hp,ho,hQ₁ p h₁,?_,hQ₂ p inferInstance h₂⟩
  intro j hj hjd
  constructor
  · apply proZero_of_target_vanishing
    intro m hm
    exact hQ₃ p ho h₃ j hj (2*d-1+1) (by omega) (by omega) m hm
  · apply proZero_of_target_vanishing
    intro m hm
    exact hQ₃ p ho h₃ j hj (2*d+1) (by omega) (by omega) m hm
```
[S6:88–112]

The proof closes with
`exact hQ₃ p ho h₃ j hj (2*d+1) (by omega) (by omega) m hm`
— a closed argument, no `sorry` [S6:112].

**Registration, not proof.** The OAI tree proves the comparator's
`MainStatement` in full, but the release registered neither a
`main_results` entry nor a `sources:` listing for it — the
gap between the tree and the ledger is one of **registration**,
not of proof. The release records `scope: "Partial progress."`
and `review: status: unchecked`; the comparator's `sorry` is the
target the release set, and the proved `main` in the OAI tree is
the result the tree carries without a ledger entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 177 at [S1:4140] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{177} at [S2:435] |
| S3 | [`preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/build/source/main.tex`](../../../preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/build/source/main.tex) | 81 | the single manuscript root; title [S3:62], date [S3:64], abstract [S3:68–73] |
| S4 | [`lean/docs/177.md`](../../../lean/docs/177.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:15] |
| S5 | [`lean/ComparatorChallenges/CoboundaryExpanders.lean`](../../../lean/ComparatorChallenges/CoboundaryExpanders.lean) | 98 | the comparator: the `MainStatement` definition [S5:80–89], the `main` theorem [S5:91] and the `sorry` [S5:92] |
| S6 | [`lean/OAI/Combinatorics/Coboundary/Main.lean`](../../../lean/OAI/Combinatorics/Coboundary/Main.lean) | 118 | the OAI tree (15 files, 11206 lines, 0 sorry): the real `main : MainStatement` proof [S6:88–112] via infinite-coset, cosystolic and gamma-vanishing lemmas |
