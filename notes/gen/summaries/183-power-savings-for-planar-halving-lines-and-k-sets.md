[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 183](../index/combinatorics/183-power-savings-for-planar-halving-lines-and-k-sets.md)

# 183 — Power savings for planar halving lines and $k$-sets

[Index page](../index/combinatorics/183-power-savings-for-planar-halving-lines-and-k-sets.md)

## Original CONTENTS.md summary

The release's blurb [S1:4254] and the catalog abstract
[S2:447] state the family's claim: the planar halving-line
bound improves to $O(n^{4/3-\varepsilon})$ for sets with no
three collinear, with an absolute $\varepsilon > 0$. More
generally, an $n$-point set with no three collinear has
$O(n(k+1)^{1/3-\varepsilon_0})$ strictly separable
$k$-subsets for $1 \leq k \leq n/2$, with an absolute
$\varepsilon_0 > 0$. The constants and positive exponents
are nonquantitative. The manuscript is *A power saving for
planar halving lines* [S3:26, S3:28]; its abstract


> There are absolute constants $\varepsilon>0$ and $C$ such that every
sufficiently large even $n$-point set in the plane with no three collinear
has at most $Cn^{4/3-\varepsilon}$ unordered halving pairs. This gives a
power saving over the classical $O(n^{4/3})$ bound for planar halving lines.
The proof is nonquantitative and does not supply explicit constants. [S3:32–36]

## Undergraduate summary

Place $n$ points in the plane so that no three lie on the
same line. A **halving line** through two of the points is a
line that leaves exactly half of the remaining points on each
side. Counting the **halving pairs** — the pairs of
points that determine a halving line — is a long-standing
problem in discrete geometry. The classical bound says there
are at most roughly $n^{4/3}$ such pairs. This manuscript
sharpens that to $n^{4/3}$ times a factor that is **strictly
smaller** than 1 — a power saving, where the exponent of
the saving is some fixed positive number, without telling you
how big it is [S3:32–36, S2:447]. The same saving
extends to **level switches**: as a line rotates, the number of
times the $k$-th point "crosses over" the line is also bounded
by the same power-saving expression [S4:9].

## Graduate summary

**The main theorem** [S3:32–36, S4:9]. There are
absolute constants $\varepsilon > 0$ and $C$ such that every
sufficiently large even $n$-point set in the plane with no
three collinear has at most $C n^{4/3-\varepsilon}$
unordered halving pairs. The proof is nonquantitative and
does not supply explicit constants [S3:32–36].

**The level-switch bound.** The same power-saving form holds
for **level-switch counts**: for a point set in generic
position, the number of switches at level $k$ is bounded by
$C n^{4/3-\varepsilon}$ [S4:9, S2:447].

**The $k$-set bound.** More generally, an $n$-point set with
no three collinear has $O(n(k+1)^{1/3-\varepsilon_0})$
strictly separable $k$-subsets for $1 \leq k \leq n/2$,
with an absolute $\varepsilon_0 > 0$ [S1:4254, S2:447].

**The scope of the formalization.** The scope note states
the formalization proves the halving-pair bound
$C n^{4/3-\varepsilon}$ and the level-switch bound of the
same form under the additional generic-position assumptions
in the statement; the constants are existential [S4:9]. The
scope note names one comparator [S4:13–15]:
`HalvingLines.lean`.

## History of the conjecture

The halving-line problem is a central question in discrete
geometry, asking how many pairs of points in a planar set
determine a line that bisects the set. The classical
$O(n^{4/3})$ bound, due to Edelsbrunner, is known to be
tight for special constructions and the question of whether
a **power saving** is possible was open. The level-switch
problem — counting how often a sweeping line crosses a
given level — is closely related and the same
$O(n^{4/3})$ barrier applies. The $k$-set problem generalizes
both: a $k$-set is a subset of $k$ points separable from the
rest by a line, and counting them is a fundamental problem in
arrangements. This manuscript provides the first power
saving for halving lines and level switches, and the
corresponding $k$-set bound, with nonquantitative constants
[S3:32–36, S2:447].

**Prior (my training data, not this repo).** I know the
halving-line problem, the classical $O(n^{4/3})$ bound, and
that a power saving was a long-standing open question in
discrete geometry. A **specific proof of a power saving via
perturbation and level-switch counting** with the
halving-count-to-middle-switch-count reduction is not
something I can independently verify from training alone; the
`Perturbation.generic_same_halvingCount` machinery in [S6:9–34]
is not in my recall.

## Consequences

**The planar halving-line bound improves to a power saving.**
Every sufficiently large even $n$-point set with no three
collinear has $O(n^{4/3-\varepsilon})$ halving pairs for an
absolute $\varepsilon > 0$ [S3:32–36, S4:9, S2:447].

**The level-switch bound improves to a power saving.**
Level-switch counts under generic position are bounded by the
same form [S4:9, S2:447].

**The $k$-set bound carries the saving.** Strictly separable
$k$-subsets are bounded by
$O(n(k+1)^{1/3-\varepsilon_0})$ [S1:4254, S2:447].

**The constants are nonquantitative.** The proof does not
supply explicit values for $C$ or $\varepsilon$
[S3:32–36, S4:9].

## Section skeleton

One manuscript [S3:32–36] (title [S3:26], date [S3:28]) —
`main.tex` (53 lines) under `build/`, inputs sections
`introduction`, `finite`, `rank-limits`, `differentiability`,
`zoom`, `spatial`, `boundary`, `recurrence`, plus a
`references` bibliography. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves that some
absolute $\varepsilon > 0$ and $C$ bound the number of
halving pairs by $C n^{4/3-\varepsilon}$ for every
sufficiently large even $n$ and every $n$-point set with no
three collinear. It also proves a bound of the same form for
all level-switch counts under the additional generic-position
assumptions in the statement. The constants are existential
[S4:9]. The scope note names one comparator [S4:13–15]:
`HalvingLines.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry for
this family and the manuscript is **not** in its `sources:`
listing. The comparator `HalvingLines.lean` restates the
target `theorem power_bounds` — a conjunction of the
halving-pair and level-switch power-saving bounds —
with a bare `sorry` body 

```lean
theorem power_bounds :
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ, ∃ n₀ : ℕ,
      ∀ n : ℕ, Even n → n₀ ≤ n → ∀ P : Fin n → Point,
        GeneralPosition P → (halvingCount P : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) ∧
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ,
      ∀ n : ℕ, 1 ≤ n → ∀ P : Fin n → Point, Generic P →
        ∀ k : ℕ, k ≤ n → (switchCount P k : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) :=
  sorry
```
[S5:45–52]

**What the OAI tree does carry.** The
`OAI/Combinatorics/HalvingLines` package (**47 files over
18,237 lines, zero `sorry`**) carries a **real, non-`sorry`**
proof of the comparator's target. The `Main.lean`
`theorem halving_power` [S6:9–22] reduces the halving
count to a level-switch count via
`Perturbation.generic_same_halvingCount` and
`halvingCount_eq_middle_switchCount`, then discharges by
`all_ranks_power`; the `theorem power_bounds`
[S6:27–34] assembles the two conjuncts as
`⟨halving_power, all_ranks_power⟩` 

```lean
theorem halving_power :
    ∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ, ∃ n₀ : ℕ,
      ∀ n : ℕ, Even n → n₀ ≤ n → ∀ P : Fin n → Point,
        GeneralPosition P → (halvingCount P : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε) := by
  obtain ⟨ε,hε,C,hbound⟩ := all_ranks_power
  refine ⟨ε,hε,C,2,?_⟩
  intro n heven hn P hP
  obtain ⟨m,hm⟩ := heven
  have hn' : n=2*m := by omega
  clear hm
  subst n
  obtain ⟨Q,hQ,hcount⟩ := Perturbation.generic_same_halvingCount hP
  rw [hcount,halvingCount_eq_middle_switchCount (by omega : 0 < m) Q hQ]
  exact hbound (2*m) (by omega) Q hQ m (by omega)
end PlanarHalving

namespace PlanarHalving

theorem power_bounds :
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ, ∃ n₀ : ℕ,
      ∀ n : ℕ, Even n → n₀ ≤ n → ∀ P : Fin n → Point,
        GeneralPosition P → (halvingCount P : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) ∧
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ,
      ∀ n : ℕ, 1 ≤ n → ∀ P : Fin n → Point, Generic P →
        ∀ k : ℕ, k ≤ n → (switchCount P k : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) :=
  ⟨halving_power, all_ranks_power⟩
```
[S6:9–34]

The proof closes with
`exact hbound (2*m) (by omega) Q hQ m (by omega)` in
`halving_power` and `⟨halving_power, all_ranks_power⟩`
in `power_bounds` — a closed argument, no `sorry`
[S6:9–34].

**Registration, not proof.** The OAI tree proves the
comparator's `power_bounds` in full, but the release
registered neither a `main_results` entry nor a `sources:`
listing for it — the gap between the tree and the ledger
is one of **registration**, not of proof. The comparator json
names `OAI.Combinatorics.HalvingLines.Main` as the solution
module and `OAI.PlanarHalving.power_bounds` as the theorem,
so the release set the target and the tree answered it; the
ledger simply does not carry that answer. The release records
`scope: "Partial progress."` and `review: status: unchecked`;
the comparator's `sorry` is the target the release set, and
the proved `power_bounds` in the OAI tree is the result the
tree carries without a ledger entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 183 at [S1:4254] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{183} at [S2:447] |
| S3 | [`preprints/A-power-saving-for-planar-halving-lines-September-25-2026/build/main.tex`](../../../preprints/A-power-saving-for-planar-halving-lines-September-25-2026/build/main.tex) | 53 | the single manuscript root; title [S3:26], date [S3:28], abstract [S3:32–36] |
| S4 | [`lean/docs/183.md`](../../../lean/docs/183.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/HalvingLines.lean`](../../../lean/ComparatorChallenges/HalvingLines.lean) | 56 | the comparator: the `power_bounds` theorem [S5:45–51] and the `sorry` [S5:52] |
| S6 | [`lean/OAI/Combinatorics/HalvingLines/Main.lean`](../../../lean/OAI/Combinatorics/HalvingLines/Main.lean) | 38 | the OAI tree (47 files, 18237 lines, 0 sorry): the real `power_bounds` proof [S6:27–34] via `halving_power` (perturbation + level-switch counting) and `all_ranks_power` |
