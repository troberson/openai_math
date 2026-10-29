[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 185](../index/combinatorics/185-counterexamples-to-infinite-matroid-intersection-and-packing-covering.md)

# 185 — Counterexamples to infinite matroid intersection and packing/covering

[Index page](../index/combinatorics/185-counterexamples-to-infinite-matroid-intersection-and-packing-covering.md)

## Original CONTENTS.md summary

The release's blurb [S1:4295] and the catalog abstract [S2:451]
state the family's claim: a **counterexample** in ZFC to the
unrestricted infinite matroid intersection and packing/
covering conjectures, built from two self-dual partitional
matroids on a countably infinite ground set. The same examples
answer Joó's partitional-matroid question negatively.
The examples are neither finitary nor cofinitary, so
Nash-Williams' original finitary conjecture remains outside
the result. The manuscript is *A Counterexample to the
Infinite Matroid Packing/Covering Conjecture* [S3:70, S3:72];
its abstract 

> We construct in ZFC two self-dual partitional matroids on a countably infinite
common ground set that admit neither a packing/covering partition nor an
intersection witness. This disproves the unrestricted infinite matroid
packing/covering and intersection conjectures and answers Joó's question
for two partitional matroids negatively. The examples are neither finitary
nor cofinitary. [S3:76–81]

## Undergraduate summary

A **matroid** is a structure that abstracts "independence" —
the property a set of vectors has when no one is a combination
of the others, or a set of edges has when it contains no
cycle. **Infinite** matroids extend that to ground sets that
go on forever. Two matroids can **intersect** (share an
independent set together) and can be **packed and covered**
(their ground set split into a part each spans and a part each
fits inside independently). The conjectures said these
operations should always come out with a witness. This
constructs a specific pair of infinite matroids for which the
witness does **not** exist — a counterexample, not a
proof of a positive bound. Because the pair is
"self-dual" (each is its own dual) and "partitional" (its
independent sets are bounded block-by-block), it also answers
a separate question of Jo–Só no [S3:76–81,
S2:451].

## Graduate summary

**The main counterexample** [S3:76–81, S4:9]. In ZFC
there is a countable infinite ground set $`E`$ and two matroids
$`M_0, M_1`$ on it, both full-ground and **self-dual**
($`M_i.dual = M_i`$), such that no two independent sets
$`I_0, I_1`$ (one from each) cover $`E`$ —
$`I_0 \cup I_1 \neq E`$ — and **no** packing/covering
partition exists. This refutes both the unrestricted
infinite matroid **intersection** conjecture (no
intersection witness) and the **packing/covering**
conjecture (no packing/covering partition)
[S4:9, S5:23–30].

**The partitional flavor and the corollaries.** The
construction realizes the matroids as **partitional**
(bounded on each block), so the same pair answers
Jo–Só's partitional-matroid question
negatively; and it yields **separate** counterexamples to the
individual covering and packing conjectures
[S4:11, S6:108–124]. The construction uses ordinary
set theory with Choice and assumes **no finitary
restriction** — the examples are neither finitary nor
cofinitary [S3:76–81, S4:9].

**The scope of the formalization.** The scope note states
the formalization constructs the two self-dual partitional
matroids with no independent covering and no
packing/covering partition, and that the same pair has no
intersection witness [S4:9]. It records separate formalized
consequences for the individual covering and packing
conjectures [S4:11]. The scope note names two comparators
[S4:15–18]: `InfiniteMatroid.lean` (registered) and
`InfiniteMatroidCorollaries.lean` (unregistered).

## History of the conjecture

Infinite matroid theory grew out of Nash-Williams' work on
the **finitary** matroid intersection and packing/covering
conjectures, where the ground set and the matroids have
finite rank constraints. The natural question was whether the
conjectures survive when the finitary restriction is dropped
entirely — the **unrestricted** infinite setting. A
counterexample there is a strong negative result: it shows
the finitary hypotheses are not a technicality. The
partitional-matroid question of Jo–Só is a
parallel named problem asking whether the partitional class
admits the same witnesses. This construction lands a single
pair of self-dual partitional matroids that refutes the
unrestricted intersection and packing/covering conjectures
**and** answers the Jo–Só question, while leaving
the original finitary conjecture intact
[S3:76–81, S2:451].

**Prior (my training data, not this repo).** I know Nash-
Williams' finitary matroid intersection and that the
unrestricted infinite case is a natural open generalization,
and that partitional matroids are the block-bounded class. A
**specific ZFC construction of two self-dual partitional
matroids with no independent cover and no intersection
witness** — and its use to answer the Jo–Só
partitional question negatively — goes beyond what I can
place from training alone; the concrete-rank, basis-system,
and `rayMatroid` machinery in [S7:12–46] is not something I can
independently verify from memory.

## Consequences

**The unrestricted infinite matroid intersection
conjecture is disproved.** Two self-dual partitional matroids
on a countable infinite ground set have no intersection
witness [S3:76–81, S4:9, S2:451].

**The unrestricted infinite matroid packing/covering
conjecture is disproved.** The same pair admits no
packing/covering partition [S3:76–81, S4:9, S2:451].

**Jo–Só's partitional-matroid question is
answered negatively.** The pair is partitional, so the
negative extends to the partitional class [S4:9,
S6:108–117].

**The finitary conjecture is untouched.** The examples are
neither finitary nor cofinitary, so Nash-Williams' original
finitary result remains valid [S3:76–81, S4:9].

## Section skeleton

One manuscript [S3:76–81] (title [S3:70], date [S3:72]) —
`paper.tex` (99 lines) under `build/`, with a `references`
bibliography and a `figures` directory. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization constructs two
self-dual partitional matroids on one countably infinite
ground set that admit neither an independent covering nor a
packing/covering partition; the same pair has no
intersection witness, so it also refutes the unrestricted
infinite matroid intersection conjecture [S4:9]. Separate
formalized consequences give counterexamples to the
individual covering and packing conjectures, in ordinary
set theory with Choice and no finitary restriction
[S4:11]. The scope note names two comparators
[S4:15–18]: `InfiniteMatroid.lean` and
`InfiniteMatroidCorollaries.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml`
registers one `main_results` entry — the
`OAI.InfiniteMatroidCounterexample.main` declaration at
`OAI/Combinatorics/InfiniteMatroid/Main.lean` — and the
one manuscript is in its `sources:` listing. The
`InfiniteMatroidCorollaries.lean` comparator is a scope-note
link with **no** `main_results` entry
[S4:9, S4:11, S4:15–18].

**The comparator stub.** The `InfiniteMatroid.lean` comparator
defines `HasPackingCovering` and restates the target
`theorem main` — the countable-infinite ground set with
two full-ground self-dual matroids, no independent cover, and
no packing/covering — with a bare `sorry` body
[S5:14–30]:

```lean
theorem main :
    Countable E ∧ Infinite E ∧
    ∃ M₀ M₁ : Matroid E,
      M₀.E = Set.univ ∧ M₁.E = Set.univ ∧
      M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
      (∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ Set.univ) ∧
      ¬ HasPackingCovering M₀ M₁ := by
  sorry
```
[S5:23–30]

**What the proof does.** The registered `main` in the OAI tree
is a genuine construction, not a `sorry`: it obtains a
concrete rank $`R`$ and a basis system $`S`$, forms a self-dual
matroid $`Q`$ from $`S`$, packages $`Q`$ into the two ray matroids
`rayMatroid Q false` and `rayMatroid Q true`, proves they are
full-ground and self-dual, obtains `no_independent_cover`
from the antitone rank and the basis property $`hb`$, and
discharges the no-packing/covering clause by
`independent_cover_of_packing_covering` contra


```lean
theorem main :
    Countable E ∧ Infinite E ∧
    ∃ M₀ M₁ : Matroid E,
      M₀.E = Set.univ ∧ M₁.E = Set.univ ∧
      M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
      (∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ Set.univ) ∧
      ¬ HasPackingCovering M₀ M₁ := by
  obtain ⟨R,hK⟩ := exists_concrete_rank
  obtain ⟨S,hS⟩ := R.exists_basisSystem hK
  let Q : Matroid E0 := S.matroid
  have hE : Q.E = Set.univ := S.ground
  have hQ : Q.dual = Q := S.self_dual
  have hanti : ∀ ⦃X Y : Set D⦄, X ∈ R.ultra → Y ∈ R.ultra → X ⊆ Y →
      R.rank Y ≤ R.rank X :=
    fun _ _ hX hY hXY ↦ R.antitone hX hY (R.ideal.modSubset_of_subset hXY)
  have hb : ∀ B, Q.IsBase B → (Prod.mk · false) ⁻¹' B ∈ R.ultra →
      ((Prod.mk · true) ⁻¹' B)ᶜ ∈ R.ultra ∧
      R.rank ((Prod.mk · true) ⁻¹' B)ᶜ < R.rank ((Prod.mk · false) ⁻¹' B) := by
    intro B hB hl
    have ha : R.Admissible B := hS B ((S.isBase_iff B).mp hB)
    rcases ha with ha | ha
    · exact ha.2
    · exact (ha.1 hl).elim
  have hn : ∀ I J : Set E, (rayMatroid Q false).Indep I →
      (rayMatroid Q true).Indep J → I ∪ J ≠ Set.univ :=
    no_independent_cover Q R.ultra R.rank hanti hb
  refine ⟨inferInstance, inferInstance, rayMatroid Q false, rayMatroid Q true,
    rayMatroid_ground Q hE false, rayMatroid_ground Q hE true,
    rayMatroid_selfDual Q hE hQ false, rayMatroid_selfDual Q hE hQ true, hn, ?_⟩
  intro h
  obtain ⟨I,J,hI,hJ,hIJ⟩ := independent_cover_of_packing_covering
    (rayMatroid Q false) (rayMatroid Q true)
    (rayMatroid_ground Q hE false) (rayMatroid_ground Q hE true)
    (rayMatroid_selfDual Q hE hQ false) (rayMatroid_selfDual Q hE hQ true) h
  exact hn I J hI hJ hIJ
```
[S7:12–46]

The proof closes with `exact hn I J hI hJ hIJ` —
contradicting a would-be packing/covering by the
no-independent-cover lemma, no `sorry` [S7:12–46].

**What the OAI tree does carry.** The
`OAI/Combinatorics/InfiniteMatroid` package (**33 files over
4,477 lines, zero `sorry`**) carries the supporting machinery:
the `TransfiniteConstruction` and `exists_concrete_rank`, the
basis-system `exists_basisSystem`, the `rayMatroid`
packaging with `rayMatroid_ground` and `rayMatroid_selfDual`,
the `PackingCovering` `HasPackingCovering` definition and
`independent_cover_of_packing_covering`, and the
`no_independent_cover` lemma that `main` assembles
[S7:12–46].

**The unregistered corollaries.** The
`InfiniteMatroidCorollaries.lean` comparator restates two more
results as `sorry` bodies with no `main_results` entry:
`partitional_intersection_counterexample` — the same pair
made explicitly **partitional**, with no intersection witness
[S6:108–117] — and
`separate_covering_packing_counterexamples` — separate
counterexamples to the individual covering and packing
conjectures [S6:119–124]. These corollary statements are
registered in neither the yaml nor the ledger; the release
records `scope: "Partial progress."` and `review: status:
unchecked`, and the proved `main` in the OAI tree is the
registered result.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 185 at [S1:4295] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{185} at [S2:451] |
| S3 | [`preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/build/paper.tex`](../../../preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/build/paper.tex) | 99 | the single manuscript root; title [S3:70], date [S3:72], abstract [S3:76–81] |
| S4 | [`lean/docs/185.md`](../../../lean/docs/185.md) | 18 | the formalization scope note: the construction paragraph [S4:9], the corollary paragraph [S4:11], and the comparator table [S4:15–18] |
| S5 | [`lean/ComparatorChallenges/InfiniteMatroid.lean`](../../../lean/ComparatorChallenges/InfiniteMatroid.lean) | 34 | registered comparator: the `HasPackingCovering` definition [S5:14–21], the `main` theorem [S5:23–29] and the `sorry` [S5:30] |
| S6 | [`lean/ComparatorChallenges/InfiniteMatroidCorollaries.lean`](../../../lean/ComparatorChallenges/InfiniteMatroidCorollaries.lean) | 128 | unregistered comparator: the `partitional_intersection_counterexample` theorem [S6:108–116] with `sorry` [S6:117], and the `separate_covering_packing_counterexamples` theorem [S6:119–123] with `sorry` [S6:124] |
| S7 | [`lean/OAI/Combinatorics/InfiniteMatroid/Main.lean`](../../../lean/OAI/Combinatorics/InfiniteMatroid/Main.lean) | 51 | the registered declaration in the OAI tree (33 files, 4477 lines, 0 sorry): the real `main` proof [S7:12–46] via a concrete rank, a basis system, `rayMatroid`, and `no_independent_cover` |
