[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 155](../index/combinatorics/155-a-counterexample-to-periodic-tiling-in-dimension-three.md)

# 155 — A counterexample to periodic tiling in dimension three

[Index page](../index/combinatorics/155-a-counterexample-to-periodic-tiling-in-dimension-three.md)

## Original CONTENTS.md summary

The release's blurb [S1:3711] and the catalog abstract [S2:393] state
the family's claim: a finite translational tile in
$`\mathbb Z^3`$ that tiles space but admits no fully periodic tiling,
disproving the periodic tiling conjecture in the smallest possible
lattice dimension; its unit-cube thickening gives the same
counterexample in $`\mathbb R^3`$, even with arbitrary real
translation vectors. The manuscript is *A translational tile with no
fully periodic tiling in dimension three* [S3:61, S3:63]; its abstract


> We construct a finite translational tile in $`\mathbb Z^3`$ that admits tilings but no fully periodic tiling. Its unit-cube thickening has the same property in $`\mathbb R^3`$, even when arbitrary real translations are allowed. This gives a negative resolution of the periodic tiling conjecture in dimension three. [S3:68]

## Undergraduate summary

A *tile* is a finite set of unit cubes in the integer lattice
$`\mathbb Z^d`$. It *tiles* space if copies of it, moved by
translations, can cover the whole space with no gaps and no
overlaps. A tiling is *fully periodic* if it repeats in every
direction — there is a finite set of translation vectors
such that shifting the tiling by any of them leaves it unchanged
(a tiling that has a period in each coordinate direction). The
*periodic tiling conjecture* asks: if a finite tile tiles the lattice,
must it admit some fully periodic tiling? For many tiles the answer
is yes. This manuscript shows the answer is **no** in dimension three
— and that three is the smallest lattice dimension where this
can fail [S3:68, S4:9].

## Graduate summary

**The headline theorem (registered).** There exists a finite set
$`T`$ of lattice points in $`\mathbb Z^3`$ (nonempty) such that:
$`T`$ tiles (there is a subset $`A\subset\mathbb Z^3`$ with $`T`$
translating to cover $`A`$); no tiling of $`A`$ by translates of $`T`$ is
fully periodic; the unit-cube *thickening* of $`T`$ almost-everywhere
tiles $`\mathbb R^3`$; and no such thickening tiling is
Euclidean-fully-periodic, even with arbitrary real translations; and
$`3`$ is the least lattice dimension in which a tile exists with no
periodic complement [S4:9, S6:23–31].

**The minimal-dimension clause.** The result is not merely that a
non-periodic tile exists in $`\mathbb Z^3`$: dimension three is
established as the **least** lattice dimension where the failure
occurs — in dimensions one and two every finite tile that
tiles admits a fully periodic tiling
[S4:9, S6:8–21].

**What the formalization proves.** The registered declaration
`OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality`
states exactly the headline theorem: the existence of a nonempty
finite $`T\subset`$ ``Lattice 3`` with a tiling $`A`$, no fully
periodic tiling of $`A`$, an a.e. tiling of the thickening, no
Euclidean-fully-periodic thickening tiling, and $`3`$ as the least such
dimension. The OAI tree proves it directly, by assembling the
constructed tile with the minimality lemma


```lean
theorem periodic_tiling_counterexample_and_minimality :
    (∃ T : Finset (Lattice 3), T.Nonempty ∧
      (∃ A : Set (Lattice 3), Tiles T A) ∧
      (∀ A : Set (Lattice 3), Tiles T A → ¬ FullyPeriodic A) ∧
      (∃ A : Set (Space 3), AETiles (Thickening T) A) ∧
      (∀ A : Set (Space 3),
        AETiles (Thickening T) A → ¬ EuclideanFullyPeriodic A)) ∧
    IsLeast {d : ℕ | HasTileWithoutPeriodicComplement d} 3 :=
  ⟨exists_three_dimensional_tile, least_lattice_dimension_three⟩
```
[S6:23–31]

The proof is a real Lean proof (not a `sorry`): it closes with
`⟨exists_three_dimensional_tile, least_lattice_dimension_three⟩`
[S6:31], pairing the explicit three-dimensional tile with the
argument that no dimension below three can carry such a tile.

## History of the conjecture

The periodic tiling (or "is every aperiodic tiling aperiodic in the
periodic sense?") question sits in the geometry of tiling and
combinatorial group theory. In one dimension every translation tile
of $`\mathbb Z`$ is periodic, and the question has a long history in
the two-dimensional case, closely related to the classical
periodicity/aperiodicity of domino and polyomino tilings. The
release's claim is a **three-dimensional** counterexample with the
added **minimality** content: three is the first dimension in which a
finite tile can tile without any fully periodic tiling. The
unit-cube thickening extends the lattice counterexample to
$`\mathbb R^3`$ with arbitrary real translation vectors, matching the
form of the Euclidean question
[S3:68, S4:9].

**Prior (my training data, not this repo).** I know the
one- and two-dimensional periodicity facts for translation tiles, and
that the three-dimensional case is where the question is
nontrivial. A concrete finite tile in $`\mathbb Z^3`$ that tiles but
has **no** fully periodic tiling, together with the **minimality**
statement (three is the least such dimension), and its extension to
$`\mathbb R^3`$ with real translations, goes beyond the specific
constructions I recall; I cannot independently verify the tile or the
minimality argument from training alone.

## Consequences

**The periodic tiling conjecture is false in dimension three.**
There is a finite translational tile in $`\mathbb Z^3`$ that tiles
but admits no fully periodic tiling [S3:68, S4:9, S6:23–31].

**Dimension three is minimal.** No tile in $`\mathbb Z^d`$ for
$`d<3`$ exhibits the failure; three is the least lattice dimension
where a tile can tile without a fully periodic tiling
[S4:9, S6:8–21].

**The failure survives thickening to $`\mathbb R^3`$.** The
unit-cube thickening tiles $`\mathbb R^3`$ almost everywhere but
admits no Euclidean-fully-periodic tiling, even with arbitrary real
translation vectors [S3:68, S4:9, S6:23–31].

## Section skeleton

One manuscript [S3:68] (title [S3:61], date [S3:63]) — `paper.tex`
under `build/`, 98 lines; one `references.bib`. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized counterexample is a finite tile
in $`\mathbb Z^3`$ that tiles but has no complement invariant under a
finite-index subgroup; its unit-cube thickening tiles $`\mathbb R^3`$
almost everywhere but admits no fully periodic tiling even with
arbitrary real translations, and dimension three is established as
the least lattice dimension where this failure occurs [S4:9]. The
scope note names one comparator [S4:13–15]:
`PeriodicTilingThree.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml` registers
one `main_results` entry naming the headline theorem
`OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality`
at `OAI/Geometry/PeriodicTiling/Counterexample.lean`, and the
manuscript is in its `sources:` listing. The registered declaration
carries a genuine Lean proof in the OAI tree [S6:23–31].

**What the proof does.** The theorem closes by pairing two
components the library proves separately: the explicit
three-dimensional tile
(`exists_three_dimensional_tile`) and the minimality lemma
(`least_lattice_dimension_three`), which shows that any tile in a
dimension below three that tiles must have a fully periodic
complement [S6:31, S6:8–21]. The OAI `PeriodicTiling` package
(122 files over 16,899 lines, zero `sorry`) carries the supporting
definitions of ``Tiles``, ``FullyPeriodic``, ``Thickening``,
``AETiles``, ``EuclideanFullyPeriodic``, and ``HasTileWithoutPeriodicComplement``
that the two components assemble.

**The comparator stub.** The `PeriodicTilingThree.lean` comparator
restates the same headline theorem with a bare `sorry` body


```lean
theorem periodic_tiling_counterexample_and_minimality :
    (∃ T : Finset (Lattice 3), T.Nonempty ∧
      (∃ A : Set (Lattice 3), Tiles T A) ∧
      (∀ A : Set (Lattice 3), Tiles T A → ¬ FullyPeriodic A) ∧
      (∃ A : Set (Space 3), AETiles (Thickening T) A) ∧
      (∀ A : Set (Space 3),
        AETiles (Thickening T) A → ¬ EuclideanFullyPeriodic A)) ∧
    IsLeast {d : ℕ | HasTileWithoutPeriodicComplement d} 3 := by
  sorry
```
[S5:52–60]

The release records `scope: "Partial progress."` and
`review: status: unchecked`; the comparator's `sorry` is the target
the release set itself, and the proved version in the OAI tree is the
registered result.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 155 at [S1:3711] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{155} at [S2:393] |
| S3 | [`preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/paper.tex`](../../../preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/paper.tex) | 98 | the single manuscript root; title [S3:61], date [S3:63], abstract [S3:68] |
| S4 | [`lean/docs/155.md`](../../../lean/docs/155.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/PeriodicTilingThree.lean`](../../../lean/ComparatorChallenges/PeriodicTilingThree.lean) | 66 | comparator stub: the `periodic_tiling_counterexample_and_minimality` theorem [S5:52–59] and the `sorry` [S5:60] |
| S6 | [`lean/OAI/Geometry/PeriodicTiling/Counterexample.lean`](../../../lean/OAI/Geometry/PeriodicTiling/Counterexample.lean) | 35 | the registered declaration in the OAI tree: the real proof of `periodic_tiling_counterexample_and_minimality` [S6:23–31] |
