[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 158](../index/combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md)

# 158 — The Euclidean plane cannot be colored with five colors

[Index page](../index/combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md)

## Original CONTENTS.md summary

The release's blurb [S1:3777] and the catalog abstract [S2:399] state
the family's claim: every five-coloring of the Euclidean plane has a
monochromatic pair at distance one, with no restriction on the color
classes. This advances the Hadwiger–Nelson problem: together
with the classical seven-coloring, only six and seven remain possible
chromatic numbers of the plane. The manuscript is *The Euclidean
plane is not five-colorable* [S3:3, S3:5]; its abstract


> We prove that every coloring of the Euclidean plane with five colors has a
monochromatic unit-distance pair, with no regularity assumption on the color
classes. Consequently, the chromatic number of the plane is either six or seven. [S3:9–11]

## Undergraduate summary

The *chromatic number of the plane* is the fewest colors needed to
paint every point of the two-dimensional plane so that any two points
exactly one unit apart get **different** colors. The
Hadwiger–Nelson problem (1950s) asks what that number is. A
coloring is a function assigning a color to each point; it is
*proper* if unit-distance points are never the same color. The
classical upper bound says **seven** colors always suffice (a
hexagonal/triangular-lattice tiling argument), so the answer is at
most seven — and it is at least four. This manuscript closes
the interval's floor: it proves **five** colors do **not** suffice,
so the chromatic number of the plane is now known to be **six or
seven** [S3:9–11, S4:9].

## Graduate summary

**The five-color lower bound** [S3:9–11, S7:124–127].
There is no proper five-coloring of the plane: for every coloring
$`c:\mathbb C\to\{1,\ldots,5\}`$ of unit disk, some pair of
unit-distance points carries the same color. The bound is stated with
**no regularity assumption** on the color classes — not
measurable, not Borel, not continuous — arbitrary colorings
[S4:9, S7:124–127].

**The seven-color upper bound** [S4:9, S8:36–37]. Seven colors
**do** suffice: there is a proper seven-coloring of the plane, and
the construction includes **every boundary point** of the coloring
regions (the choice at a shared edge is a definable one, not a
set-theoretic choice-principle artifact) [S4:9, S8:36–37].

**Together the two bounds pin the answer.** Combining the five-color
impossibility with the seven-color construction narrows the
Hadwiger–Nelson number to $`\{6,7\}`$
[S3:9–11, S4:9, S7:124–127, S8:36–37].

## History of the conjecture

The Hadwiger–Nelson problem asks for the chromatic number of
the unit-distance graph on $`\mathbb R^2`$. The classical
lower-bound history runs from the Moebius-Kantor 4-chromatic unit-
distance graph (no four-coloring) to the eventual elimination of the
five- and six-color hypotheses in turn: the five-color case is the
family's content, and the seven-color upper bound is the
traditional triangular-lattice (hexagonal) coloring. The release's
contribution is to prove the five-color case with **no
measurability hypothesis** — a stronger statement than the
measurable-coloring variants that had been the usual route
[S3:9–11, S4:9].

**Prior (my training data, not this repo).** I know the
Hadwiger–Nelson problem, the 4-to-7 range, and that both the
five-color and the six-color cases had long been open. A **no-
regularity** five-color lower bound (arbitrary colorings, not just
measurable ones) together with a boundary-inclusive seven-color
construction, narrowing the answer to $`\{6,7\}`$, is the specific
advance the family claims. I cannot independently verify the
unit-distance graph rigidity / spectral argument in [S3:9–11] from
training alone.

## Consequences

**Five colors do not suffice.** Every (arbitrary, no-regularity)
five-coloring of the plane has a monochromatic unit-distance pair
[S3:9–11, S7:124–127].

**Seven colors do suffice.** There is a proper seven-coloring of the
plane including every boundary point of the regions
[S4:9, S8:36–37].

**The Hadwiger–Nelson number is 6 or 7.** The two bounds
together pin the plane's chromatic number to $`\{6,7\}`$
[S3:9–11, S4:9].

## Section skeleton

One manuscript [S3:9–11] (title [S3:3], date [S3:5]) — `main.tex`
(27 lines) under `build/`, inputs the sections `introduction`,
`spectral`, `rigidity`, `transfer`, `palettes`, `transitions` (among
others), plus a `references` bibliography. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized results prove **both** that
five colors do not suffice **and** that seven colors do: the lower
bound applies to arbitrary colorings with no measurability or
continuity assumption, and the upper bound includes every boundary
point of the coloring regions [S4:9]. The scope note names two
comparators [S4:15–16]: `EuclideanFiveColor.lean` (the no-
proper-five-coloring claim) and `PlaneColoring.lean` (the proper-
seven-coloring claim).

**The registration.** The family is at tier T3: the ledger row
records `mainres 2` and `paps_form 1` — the richest T3
registration in this range, with **two** `main_results` entries over
one manuscript. `formalization.yaml` registers
`OAI.EuclideanFiveColor.no_proper_five_coloring` at
`OAI/Geometry/PlaneColoring/Five.lean` and
`OAI.Problem160.properColoring_seven` at
`OAI/Geometry/PlaneColoring/Seven.lean`, and the manuscript is in its
`sources:` listing. The two declarations live in **two different
namespaces** (`OAI.EuclideanFiveColor` and `OAI.Problem160`), so the
family's two halves are registered under distinct names
[S4:9, S4:15–16].

**What the proofs do.** The five-color declaration
`no_proper_five_coloring` states
$`\neg\exists c\colon\mathbb C\to\mathrm{Fin\ 5},\
\mathrm{ProperColoring\ 5\ c}`$, and the OAI tree proves it with a
real Lean proof: it assumes a proper $`c`$, extracts a Borel weak
coloring from it via `proper_to_borel_weak`, and discharges the goal
with the no-measurable-weak-five-coloring lemma


```lean
theorem no_proper_five_coloring : ¬ ∃ c : ℂ → Fin 5, ProperColoring 5 c := by
  rintro ⟨c,hc⟩
  obtain ⟨d,hd,hw⟩ := proper_to_borel_weak hc
  exact no_measurable_weak_five_coloring hd hw
```
[S7:124–127]

The seven-color declaration `properColoring_seven` states that a
proper seven-coloring exists, and the OAI tree proves it by applying
the normalized-cover construction to an explicit triangular-lattice
cover 

```lean
theorem properColoring_seven : ProperColoring 7 :=
  properColoring_seven_of_normalized_cover triangular_lattice_cover
```
[S8:36–37]

Neither proof is a `sorry`. The OAI `PlaneColoring` package (46 files
over 14,661 lines, zero `sorry`) carries the supporting definitions
(`ProperColoring`, `WeakMeasurableColoring`, `proper_to_borel_weak`,
`no_measurable_weak_five_coloring`, `properColoring_seven_of_normalized_cover`,
the `triangular_lattice_cover` witness) that both theorems assemble.

**The comparator stubs.** The `EuclideanFiveColor.lean` comparator
restates `no_proper_five_coloring` with a bare `sorry`
[S5:10–11], and the `PlaneColoring.lean` comparator restates
`properColoring_seven` with an inline `sorry` [S6:15]. The release
records `scope: "Partial progress."` and `review: status: unchecked`;
the comparators' `sorry` bodies are the targets the release set
itself, and the proved versions in the OAI tree are the registered
results.

**Tree measurement (source-level).**

The family registers 2 `main_results` declarations (`OAI.EuclideanFiveColor.no_proper_five_coloring`; `OAI.Problem160.properColoring_seven`); the primary file `OAI/Geometry/PlaneColoring/Five.lean` carries 131 lines with top-level theorem `theorem graph_map_small_mesh_impossible`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 46 files with 49 theorems and 204 defs.

The preprint states 45 theorem environments; the tree carries 1× as many (source-level count, not a proof-quality ratio).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 158 at [S1:3777] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{158} at [S2:399] |
| S3 | [`preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/build/main.tex`](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/build/main.tex) | 27 | the single manuscript root; title [S3:3], date [S3:5], abstract [S3:9–11] |
| S4 | [`lean/docs/158.md`](../../../lean/docs/158.md) | 16 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:15–16] |
| S5 | [`lean/ComparatorChallenges/EuclideanFiveColor.lean`](../../../lean/ComparatorChallenges/EuclideanFiveColor.lean) | 15 | comparator stub (five): the `no_proper_five_coloring` theorem [S5:10] and the `sorry` [S5:11] |
| S6 | [`lean/ComparatorChallenges/PlaneColoring.lean`](../../../lean/ComparatorChallenges/PlaneColoring.lean) | 21 | comparator stub (seven): the `properColoring_seven` theorem [S6:15] |
| S7 | [`lean/OAI/Geometry/PlaneColoring/Five.lean`](../../../lean/OAI/Geometry/PlaneColoring/Five.lean) | 131 | the registered five-color declaration in the OAI tree: the real proof of `no_proper_five_coloring` [S7:124–127] |
| S8 | [`lean/OAI/Geometry/PlaneColoring/Seven.lean`](../../../lean/OAI/Geometry/PlaneColoring/Seven.lean) | 68 | the registered seven-color declaration in the OAI tree: the real proof of `properColoring_seven` [S8:36–37] |
