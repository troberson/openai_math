[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 167](../index/combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md)

# 167 — Pinned distances and a power saving for planar unit distances

[Index page](../index/combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md)

## Original CONTENTS.md summary

The release's blurb [S1:3931] and the catalog abstract [S2:415] state
the family's two-part claim. It **proves the weak pinned
Erd\H{o}s distance conjecture**: for every fixed
$`\varepsilon>0`$, all but $`o(n)`$ points of any $`n`$-point planar set
determine at least $`n^{1-\varepsilon}`$ distinct nonzero
distances. A **complementary theorem** bounds the number of
unit-distance pairs by $`O(n^{4/3-\delta})`$ for an absolute
$`\delta>0`$. Two manuscripts carry the family. The first, *The weak
pinned planar distance theorem* [S3:31, S3:33], abstract


> We prove the weak pinned Erdős distinct-distance conjecture.
For every fixed $`\varepsilon>0`$, all but $`o(n)`$ points of any
$`n`$-point planar set determine at least $`n^{1-\varepsilon}`$ distinct
nonzero distances. [S3:38–41]

The second, *A power saving for planar unit distances* [S4:42,
S4:45], abstract [S4:50]:

We prove a power saving for the planar unit-distance problem: for
some absolute $`\beta<4/3`$, every set of $`n`$ points in the Euclidean
plane determines $`O(n^\beta)`$ unordered pairs at unit distance
[S4:50].

## Undergraduate summary

Pick $`n`$ points in the plane and look at all the pairwise
distances. Erd\H{o}s's distinct-distance problem (1946) asks how
**few** distinct distances those $`n`$ points can determine. The
"pinned" version looks from a single point — a **pin** $`x`$:
how many distinct distances does $`x`$ determine to the other
points? The weak pinned conjecture says that, up to a vanishing
$`fraction`$ of the points as pins, **every** pin sees at least
roughly $`n`$ distinct distances (precisely, at least $`n^{1-
\varepsilon}`$ for any fixed $`\varepsilon>0`$). Separately, the
**unit-distance problem** asks how many pairs of the $`n`$ points can
lie exactly one unit apart; the classical answer is on the order of
$`n^{4/3}`$. This family gives a **power saving** in that unit-
distance count: the bound drops to $`O(n^{4/3-\delta})`$ for some
absolute $`\delta>0`$, a genuine exponent improvement
[S3:38–41, S4:50, S2:415].

## Graduate summary

**The weak pinned distinct-distance theorem** [S3:38–41,
S5:10]. For each fixed $`s>0`$, the largest fraction of ordered
distinct pairs $`(x,y)`$ whose distance from the pin $`x`$ occurs at
least $`n^s`$ times tends to zero as $`n\to\infty`$; equivalently,
for every $`\varepsilon>0`$ the fraction of pins determining fewer
than $`n^{1-\varepsilon}`$ distinct distances tends **uniformly** to
zero [S5:10]. The statement is over **arbitrary** finite planar
point sets, with no regularity hypothesis [S5:10].

**The unit-distance power saving** [S4:50, S5:12]. There are
absolute constants $`C>0`$ and $`1\le\beta<4/3`$ such that every
finite planar point set of size $`n`$ determines at most $`C n^\beta`$
unordered unit-distance pairs; the same constants work for every
$`n`$, a fixed power improvement over the classical exponent $`4/3`$
[S5:12].

**The scope of the formalization.** Only the **pinned** theorem is
formalized and registered. The scope note is explicit that "the
separate unit-distance power-saving theorem is not included"
— it is carried by the `PlanarUnitDistances` comparator stub,
which has no `main_results` entry [S5:10, S5:12, S5:16–19].

## History of the conjecture

The Erd\H{o}s distinct-distance problem (1946) was resolved in 2015
by Guth and Katz, who proved the $`\Omega(n/\log n)`$ lower bound
via the finite-field sum-product machinery transplanted to
$`\mathbb R^2`$. The **pinned** variant asks the same question from
a single vantage point and is strictly more delicate; the weak form
(allowing an $`n^{\varepsilon}`$ loss and an $`o(n)`$ exceptional set
of pins) was a natural open step. The **unit-distance** problem is
one of the oldest in discrete geometry, with the $`\Theta(n^{4/3})`$
bound long known to be essentially tight for the usual algebraic
methods; a power saving below $`4/3`$ is a notable improvement
[S3:38–41, S4:50, S2:415].

**Prior (my training data, not this repo).** I know the Guth–
Katz resolution of the distinct-distance problem and the
$`n^{4/3}`$ unit-distance bound. A proof of the **weak pinned** form
uniformly in $`\varepsilon`$ together with a power saving
$`O(n^{4/3-\delta})`$ for unit distances goes beyond the specific
results I recall; I cannot independently verify the arithmetic-
sequence / number-field model argument in [S3:38–41] from training alone.

## Consequences

**The weak pinned Erd\H{o}s distance conjecture is proved.** For
every $`\varepsilon>0`$, all but $`o(n)`$ pins of an $`n`$-point planar
set determine at least $`n^{1-\varepsilon}`$ distinct nonzero
distances [S3:38–41, S5:10, S2:415].

**A power saving for planar unit distances.** Every $`n`$-point
planar set has $`O(n^{4/3-\delta})`$ unordered unit-distance pairs
for an absolute $`\delta>0`$ [S4:50, S5:12, S2:415].

**The statements are uniform.** The pinned result is uniform in
$`\varepsilon`$, and the unit-distance constants $`C,\beta`$ are
independent of $`n`$ [S5:10, S5:12].

**The formalization covers the pinned theorem only.** The
unit-distance power saving is stated and proved in the manuscript
but is outside the registered Lean statement
[S5:10, S5:12, S5:16–19].

## Section skeleton

Two manuscripts. Manuscript 1 [S3:38–41] (title [S3:31], date [S3:33])
— `main.tex` (55 lines) under `build/`, inputs the sections
`introduction`, `extremal`, `hierarchies`, `smallcells`, `variance`,
`unbounded`, `bounded`, plus a `references` bibliography. Manuscript
2 [S4] (title [S4:42], date [S4:45]) — `main.tex` (62 lines)
under `build/`, plus a `references` bibliography. The family ships
no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:10, S5:12]. The first paragraph formalizes the
pinned theorem: for each fixed $`s>0`$ the largest fraction of
ordered distinct pairs whose pin distance occurs at least $`n^s`$
times tends to zero, so for every $`\varepsilon>0`$ the fraction of
pins determining fewer than $`n^{1-\varepsilon}`$ distances tends
uniformly to zero; it is explicit that "the separate unit-distance
power-saving theorem is not included" [S5:10]. The second paragraph
describes the **unregistered** unit-distance theorem: absolute
constants $`C>0`$ and $`1\le\beta<4/3`$ with at most $`C n^\beta`$
unordered unit-distance pairs [S5:12]. The scope note names two
comparators [S5:16–19]: `PinnedDistances.lean` (registered)
and `PlanarUnitDistances.lean` (unregistered).

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml`
registers one `main_results` entry — the
`OAI.WeakPinned.main` declaration at
`OAI/Geometry/PinnedDistances/Main.lean` — and one manuscript
(the weak-pinned one) is in its `sources:` listing. The registered
declaration is the pinned theorem; the `PlanarUnitDistances.lean`
comparator is a scope-note link with no `main_results` entry
[S5:10, S5:12, S5:16–19].

**What the proof does.** The registered `main` states, for
$`s>0`$, that the worst-case rich-pair fraction
`F n s` tends to zero as $`n\to\infty`$ [S8:29–30]. It
discharges by `mainStatement s hs`, whose body is a genuine Lean
proof: by contradiction it extracts an arithmetic sequence model
from the failing hypothesis (`sequence_arithmetic_model`), realizes
it over a number field in a graph, and rules it out with
`arithmetic_sequence_impossible`, closing the divisibility
estimate by `linarith` 

```lean
theorem mainStatement : MainStatement := by
  classical
  by_contra hfail
  obtain ⟨c,s,γ,hc,hcγ,hγs,hs,hθ,P,C,hcard,hG,hmodels⟩ := sequence_arithmetic_model hfail
  choose L hL ii Z₁ Z₂ t hii h₁ h₂ ht0 ht using hmodels
  let K := fun j => L j
  let (j : ℕ) : NumberField (K j) := hL j
  have hn : Tendsto (fun j => (Fintype.card (C j):ℝ)) atTop atTop := by
    simpa only [Fintype.card_coe, Function.comp_def] using tendsto_natCast_atTop_atTop.comp (graph_card_tendsto hcard)
  apply arithmetic_sequence_impossible (fun j => coreGraph (P j) s (C j)) (Theta s) γ c
    (fun j => Theta s/((j:ℝ)+2)) Z₁ Z₂ h₁ h₂ hθ (hc.trans hcγ) (hγs.trans hs) hc hcγ hn
    (graph_error_tendsto (Theta s)) (fun j => by positivity) _ hG t ht
  intro j
  apply div_le_div_of_nonneg_left hθ.le (by norm_num : (0:ℝ)<2)
  have : 0 ≤ (j : ℝ) := Nat.cast_nonneg j
  linarith
```
[S8:12–27]

The proof is not a `sorry`: it ends `intro j; apply
div_le_div_of_nonneg_left hθ.le (by norm_num : (0:ℝ)<2); ...;
linarith` [S8:24–27].

**What the OAI tree does carry.** The
`OAI/Geometry/PinnedDistances` package (48 files over 15,879 lines,
zero `sorry`) carries the supporting machinery (`Plane`,
`richPairs`, `pairFraction`, the `F` worst-case definition,
`sequence_arithmetic_model`, the number-field `NumberField` /
`graph_card_tendsto` realization, `arithmetic_sequence_impossible`)
that `mainStatement` assembles [S8:12–27, S8:29–30].

**The comparator stubs.** The registered `PinnedDistances.lean`
comparator restates `main` —
`Tendsto (fun n => F n s) atTop (𝓝 0)` — with a bare `sorry`
body [S6:29–30]:

```lean
  sorry
```
[S6:30]

The unregistered `PlanarUnitDistances.lean` comparator restates the
unit-distance power saving
— $`\exists C,\beta,\ 0<C\wedge1\le\beta
\wedge\beta<4/3,\ \forall n,\ u(n)\le C n^\beta`$ —
with a bare `sorry` [S7:19–21]. The release records
`scope: "Partial progress."` and `review: status: unchecked`; the
comparators' `sorry` bodies are the targets the release set itself,
and the proved `main` in the OAI tree is the registered result.

**Tree measurement (source-level).**

The `main_results` entry OAI.WeakPinned.main resolves to `OAI/Geometry/PinnedDistances/Main.lean` (37 lines); the top-level theorem is `theorem mainStatement`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 48 files with 41 theorems and 199 defs.

The preprint states 49 theorem environments while the tree carries only 41 (0.84×), indicating a focused sub-formalization (source-level).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 167 at [S1:3931] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{167} at [S2:415] |
| S3 | [`preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/build/main.tex`](../../../preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/build/main.tex) | 55 | manuscript 1 (weak pinned): title [S3:31], date [S3:33], abstract [S3:38–41] |
| S4 | [`preprints/A-power-saving-for-planar-unit-distances-September-23-2026/build/main.tex`](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/build/main.tex) | 62 | manuscript 2 (unit-distance power saving): title [S4:42], date [S4:45], abstract [S4:50] |
| S5 | [`lean/docs/167.md`](../../../lean/docs/167.md) | 19 | the formalization scope note: the pinned scope paragraph [S5:10], the unit-distance paragraph [S5:12], and the comparator table [S5:16–19] |
| S6 | [`lean/ComparatorChallenges/PinnedDistances.lean`](../../../lean/ComparatorChallenges/PinnedDistances.lean) | 36 | registered comparator: the `main` theorem [S6:29] and the `sorry` [S6:30] |
| S7 | [`lean/ComparatorChallenges/PlanarUnitDistances.lean`](../../../lean/ComparatorChallenges/PlanarUnitDistances.lean) | 25 | unregistered comparator: the `main` theorem [S7:19–20] and the `sorry` [S7:21] |
| S8 | [`lean/OAI/Geometry/PinnedDistances/Main.lean`](../../../lean/OAI/Geometry/PinnedDistances/Main.lean) | 37 | the registered declaration in the OAI tree: the `main` statement [S8:29–30] and the real proof of `mainStatement` [S8:12–27] |
