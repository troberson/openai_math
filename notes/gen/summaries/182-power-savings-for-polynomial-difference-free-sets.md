[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 182](../index/combinatorics/182-power-savings-for-polynomial-difference-free-sets.md)

# 182 — Power savings for polynomial-difference-free sets

[Index page](../index/combinatorics/182-power-savings-for-polynomial-difference-free-sets.md)

## Original CONTENTS.md summary

The release's blurb [S1:4220] and the catalog abstract [S2:445]
state the family's claim: for every fixed intersective integer
polynomial $`h`$ of degree $`k \geq 2`$ with positive leading
coefficient, a subset of $`\{1,\ldots,N\}`$ avoiding nonzero
values $`h(1),h(2),\ldots`$ as differences has size
$`O_h(N^{1-c_k})`$ with $`c_k > 0`$ depending only on the degree.
For prime arguments, a power saving also holds when $`h`$ has a
unit root modulo every modulus. The family ships three
manuscripts [S1:4220]:

- *A power saving for intersective polynomial differences with
  an exponent depending only on the degree* [S3:43, S3:46]
- *A Power Saving for Polynomial Differences at Prime
  Arguments* [S4:49, S4:51]
- *A power saving for square-difference-free sets*
  [S5:37, S5:39]

The square-difference-free abstract 

> We prove that there are absolute constants $`c>0`$ and $`C<\infty`$ such that
every set $`A\subseteq\{1,\ldots,N\}`$ with no nonzero square difference
satisfies $`|A|\le C N^{1-c}`$. This answers the fixed-power question posed
by Green and Sawhney. [S5:43–46]

## Undergraduate summary

A set of integers is **difference-free** with respect to a
collection of forbidden values when no two of its elements are
separated by one of those values. The simplest case: a set with
no two elements whose difference is a perfect square. A
**power saving** is a density bound that says such a set can
occupy at most a fraction $`N^{-c}`$ of the first $`N`$ integers,
for some positive $`c`$ — it is strictly smaller than a
positive fraction, but not as small as logarithmic. The
family's three papers study when a set avoiding the values of
a polynomial $`h`$ as differences must have this kind of
power-saving density, and they show the exponent $`c`$ can be
made to depend only on the **degree** of $`h`$, not on its
specific coefficients [S3:51–57, S4:55–63,
S5:43–46].

## Graduate summary

**The intersective result** [S3:51–57, S2:445]. For
each degree $`k \geq 2`$ there is an exponent $`c_k > 0`$ such
that, for every intersective polynomial $`h`$ of degree $`k`$ with
positive leading coefficient, a set $`A \subseteq
\{1,\ldots,N\}`$ whose pairwise differences avoid all
nonzero values $`h(1),h(2),\ldots`$ satisfies
$`|A| = O_h(N^{1-c_k})`$. The implied constant may depend on
$`h`$, but the power-saving exponent depends **only** on the
degree $`k`$ [S3:51–57].

**The prime-argument result** [S4:55–63, S2:445]. When
the avoidance condition is restricted to **prime** arguments
— the differences avoid $`h(p)`$ for primes $`p`$ — a
power saving holds under the weaker hypothesis that $`h`$ has a
unit root modulo every modulus, with the exponent allowed to
depend on $`h`$ [S4:55–63].

**The square-difference-free result** [S5:43–46, S6:9].
There are absolute constants $`c > 0`$ and $`C`$ such that every
$`A \subseteq \{1,\ldots,N\}`$ with no nonzero square
difference satisfies $`|A| \leq C N^{1-c}`$. This answers the
fixed-power question posed by Green and Sawhney
[S5:43–46]. The bound is uniform for every integer
$`N \geq 1`$ [S6:9].

**The scope of the formalization.** The scope note states the
formalization proves the square-difference-free power saving
— the absolute-constant $`C N^{1-c}`$ bound for sets with
no nonzero square difference, uniform in $`N`$ [S6:9]. The scope
note names one comparator [S6:13–15]:
`SquareDifference.lean`.

## History of the conjecture

The question of how large a subset of $`\{1,\ldots,N\}`$ can
be when its differences avoid a given set of values is a
central theme in additive combinatorics. The special case of
**square-difference-free** sets — sets with no two
elements separated by a perfect square — was posed by
Green and Sawhney as a fixed-power question: can one prove a
power saving with an **absolute** constant, independent of
$`N`$? More generally, the theory of **intersective polynomials**
(polynomials with a root modulo every modulus) provides a
framework in which the degree, not the specific coefficients,
controls the density bound. This manifold closes the
square-difference-free case and extends the method to general
intersective polynomials and to prime-argument variants
[S3:51–57, S4:55–63, S5:43–46].

**Prior (my training data, not this repo).** I know
square-difference-free sets and intersective polynomials as
classical objects in additive combinatorics, and that power-
saving bounds for such sets are a standard target. The
specific **degree-only** exponent result for intersective
polynomials and the **absolute-constant** bound for
square-difference-free sets going beyond the Green–
Sawhney question are not something I can independently verify
from training alone; the scale-hierarchy and uniform-induction
machinery in [S8:83–91] is not something I can recall.

## Consequences

**The square-difference-free power saving is resolved.**
There are absolute constants $`c > 0`$ and $`C`$ such that every
square-difference-free $`A \subseteq \{1,\ldots,N\}`$
satisfies $`|A| \leq C N^{1-c}`$, uniform in $`N`$
[S5:43–46, S6:9, S2:445].

**The intersective polynomial-difference power saving holds
with a degree-only exponent.** For each $`k \geq 2`$,
$`c_k > 0`$ depends only on $`k`$ [S3:51–57, S2:445].

**The prime-argument power saving holds under the unit-root
hypothesis.** The exponent may depend on $`h`$
[S4:55–63, S2:445].

## Section skeleton

Three manuscripts:
[S3] (title [S3:43], date [S3:46]) —
`manuscript/main.tex` ($`75`$ lines) under `build/manuscript/`;
[S4] (title [S4:49], date [S4:51]) — `main.tex`
($`78`$ lines) under `build/`; [S5:43–46] (title [S5:37], date
[S5:39]) — `main.tex` ($`60`$ lines) under `build/`. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S6:9]. The formalization proves a **fixed
power saving** for sets with no nonzero square difference:
there are absolute constants $`c > 0`$ and $`C`$ such that every
$`A \subseteq \{1,\ldots,N\}`$ satisfying $`a - b \neq m^2`$
for all $`a,b \in A`$ and integers $`m \geq 1`$ has
$`|A| \leq C N^{1-c}`$, uniform for every $`N \geq 1`$
[S6:9]. The scope note names one comparator [S6:13–15]:
`SquareDifference.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry for
this family and the manuscripts are **not** in its `sources:`
listing. The comparator `SquareDifference.lean` restates the
target `theorem power_saving` with a bare `sorry` body


```lean
theorem power_saving :
    ∃ c C : ℝ, 0 < c ∧ ∀ N : ℕ, 1 ≤ N → ∀ A : Finset ℤ,
      A ⊆ Finset.Icc 1 (N : ℤ) → SquareDifference.IsSquareDifferenceFree A →
        (A.card : ℝ) ≤ C * (N : ℝ) ^ (1 - c) := by
  sorry
```
[S7:10–14]

**What the OAI tree does carry.** The
`OAI/Combinatorics/SquareDifference` package (**81 files over
24,221 lines, zero `sorry`**) carries a **real, non-`sorry`**
proof of the comparator's target. The `Main.lean` theorem
`theorem power_saving` [S8:83–91] obtains the
`nat_power_saving` constants, then for a given $`N`$ and
square-difference-free set $`A \subseteq \{1,\ldots,N\}`$,
translates $`A`$ to natural numbers via `natTranslate`, applies
the natural-number power saving, and discharges the
integer-to-natural equivalence by
`natTranslate_card` 

```lean
theorem power_saving :
    ∃ c C : ℝ, 0 < c ∧ ∀ N : ℕ, 1 ≤ N → ∀ A : Finset ℤ,
      A ⊆ Finset.Icc 1 (N : ℤ) → IsSquareDifferenceFree A →
        (A.card : ℝ) ≤ C * (N : ℝ) ^ (1 - c) := by
  obtain ⟨c,C,hc,h⟩ := nat_power_saving
  refine ⟨c,C,hc,?_⟩
  intro N hN A hA hf
  have hh := h N hN (natTranslate A) (natTranslate_sub N A hA) (natTranslate_free N A hA hf)
  rwa [natTranslate_card N A hA] at hh
```
[S8:83–91]

The proof closes with
`rwa [natTranslate_card N A hA] at hh` — a
cardinality-preserving translation, no `sorry`
[S8:83–91].

**Registration, not proof.** The OAI tree proves the
comparator's `power_saving` in full, but the release
registered neither a `main_results` entry nor a `sources:`
listing for it — the gap between the tree and the ledger
is one of **registration**, not of proof. The comparator json
names `OAI.Combinatorics.SquareDifference.Main` as the
solution module and `OAI.SquareDifference.power_saving` as the
theorem, so the release set the target and the tree answered
it; the ledger simply does not carry that answer. Moreover,
the scope note covers only the square-difference-free
manuscript [S6:9], leaving the intersective and prime-argument
papers [S3, S4] outside the formalization's scope entirely.
The release records `scope: "Partial progress."` and
`review: status: unchecked`; the comparator's `sorry` is the
target the release set, and the proved `power_saving` in the
OAI tree is the result the tree carries without a ledger
entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 182 at [S1:4220] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{182} at [S2:445] |
| S3 | [`preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/manuscript/main.tex`](../../../preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/manuscript/main.tex) | 75 | manuscript 1 of 3: intersective polynomial differences; title [S3:43], date [S3:46], abstract [S3:51–57] |
| S4 | [`preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/main.tex`](../../../preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/main.tex) | 78 | manuscript 2 of 3: prime-argument polynomial differences; title [S4:49], date [S4:51], abstract [S4:55–63] |
| S5 | [`preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/build/main.tex`](../../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/build/main.tex) | 60 | manuscript 3 of 3: square-difference-free sets; title [S5:37], date [S5:39], abstract [S5:43–46] |
| S6 | [`lean/docs/182.md`](../../../lean/docs/182.md) | 15 | the formalization scope note: the scope paragraph [S6:9] and the comparator table [S6:13–15] |
| S7 | [`lean/ComparatorChallenges/SquareDifference.lean`](../../../lean/ComparatorChallenges/SquareDifference.lean) | 18 | the comparator: the `IsSquareDifferenceFree` definition [S7:7–8], the `power_saving` theorem [S7:10–13] and the `sorry` [S7:14] |
| S8 | [`lean/OAI/Combinatorics/SquareDifference/Main.lean`](../../../lean/OAI/Combinatorics/SquareDifference/Main.lean) | 97 | the OAI tree (81 files, 24221 lines, 0 sorry): the real `power_saving` proof [S8:83–91] via `nat_power_saving` and a `natTranslate` bridge |
