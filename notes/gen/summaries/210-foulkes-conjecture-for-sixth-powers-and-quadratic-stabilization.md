[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 210](../index/algebra/210-foulkes-conjecture-for-sixth-powers-and-quadratic-stabilization.md)

# 210 — Foulkes’ conjecture for sixth powers and quadratic stabilization

[Index page](../index/algebra/210-foulkes-conjecture-for-sixth-powers-and-quadratic-stabilization.md)

## Original CONTENTS.md summary

The release's blurb [S1:4798] and the catalog abstract [S2:503]
state the family's claim: Foulkes' conjecture for the sixth
symmetric power, proved — for every partition of $`n`$ with
$`n \geq 6`$ and every partition of $`6n`$, the multiplicity of the
latter in the sixth symmetric power of the former is nonnegative.
The quadratic-stabilization companion proves that the canonical
Foulkes–Howe map is surjective for all $`a \geq 6`$ and
$`b \geq 30`$. The family ships two manuscripts [S1:4798]:

- *Foulkes' conjecture for the sixth symmetric power*
  [S3:85, S3:87]
- *Quadratic stabilization of the canonical Foulkes–Howe
  map* [S4:46, S4:48]

The sixth-power abstract 

> We prove the sixth-symmetric-power case of Foulkes' conjecture. For every
integer $`b\ge6`$ and every finite-dimensional complex vector space $`V`$,
there is a $`\mathrm{GL}(V)`$-equivariant injection
$`\mathrm{Sym}^6(\mathrm{Sym}^b V)\mathrel{%
  \BeginAccSupp{method=hex,unicode,ActualText=21AA}%
  \OriginalHookrightarrow\EndAccSupp{}}\mathrm{Sym}^b(\mathrm{Sym}^6 V)`$. [S3:91–94]

The quadratic-stabilization abstract 

> For every finite-dimensional complex vector space $`V`$, we prove that the
canonical Foulkes–Howe map
$`\mathrm{Sym}^b(\mathrm{Sym}^a V)\longrightarrow\mathrm{Sym}^a(\mathrm{Sym}^b V)`$ is surjective whenever
$`a\ge2`$ and $`b\ge a(a-1)`$. This gives a quadratic stabilization bound
independent of $`\dim V`$. [S4:52–56]

## Undergraduate summary

A **partition** of a positive integer $`n`$ is a way to write $`n`$
as a sum of non-increasing positive parts — for
example, $`5 = 3+1+1`$. The **symmetric group** $`S_n`$
(permutations of $`n`$ objects) has a building block for each
partition: an irreducible representation. The **sixth
symmetric power** of a representation $`V`$, written
$`\mathrm{Sym}^6(V)`$, is the part of the six-fold
tensor product of $`V`$ with itself that is invariant under
all permutations of the factors. **Foulkes' conjecture**
(1927) asks: when you decompose
$`\mathrm{Sym}^6(V_\lambda)`$ into irreducible
representations, are all the multiplicities **nonnegative**?
Since multiplicities are counts, this sounds obvious
— but the formula that computes them involves
signed sums, and Foulkes conjectured the final answer is
always nonnegative. This manuscript pair says **yes**
[S3:91–94, S4:52–56, S2:503].

## Graduate summary

**The sixth power** [S3:91–94, S2:503]. Let
$`\lambda`$ be a partition of $`n \geq 6`$. For every
partition $`\mu`$ of $`6n`$, the multiplicity of the Specht
module $`S_\mu`$ in the sixth symmetric power
$`\mathrm{Sym}^6(S_\lambda)`$ is nonnegative.
Equivalently, the Foulkes conjecture holds in degree six.

**The quadratic stabilization** [S4:52–56, S2:503].
The canonical Foulkes–Howe map from the tensor
product of two Schur modules to the corresponding Schur
module is **surjective** for all $`a \geq 6`$ and
$`b \geq 30`$. This is the quadratic-stabilization
property that implies the Foulkes conjecture in the
stable range.

**The scope of the formalization.** The scope note
covers the quadratic-stabilization result [S5:9]: the
canonical Foulkes–Howe map is surjective for
$`a \geq 6`$ and $`b \geq 30`$. The sixth-power
specialization is included only for $`b \geq 30`$, not
for the full $`b \geq 6`$ range of M1 [S5:9]. The scope
note names one comparator [S5:15]: `FoulkesHowe.lean`.

## History of the conjecture

**Foulkes' conjecture** (1927) is one of the oldest
open problems in the representation theory of the
symmetric group. It asks whether the Foulkes
coefficients (multiplicities in symmetric powers of
Specht modules) are always nonnegative. Positive
cases: degree 1 (trivial), degree 2 (classical),
degree 3 (Foulkes 1946), degree 4 (Barratt 1959),
degree 5 (Foulkes 1946, corrected by Howe 1977). The
degree-6 case was the next open case. The **quadratic
stabilization** approach, due to Foulkes and Howe,
reduces the conjecture to a surjectivity statement for
a canonical map between exterior powers of Schur
modules. The two manuscripts attack the degree-6 case
from complementary directions: the first proves the
Foulkes conjecture directly via a branching-graph and
Littlewood–Richardson computation; the second
proves the quadratic-stabilization surjectivity for
$`a \geq 6`$, $`b \geq 30`$ [S3:91–94,
S4:52–56, S2:503].

**Prior (my training data, not this repo).** I know
the Foulkes conjecture as a named open problem in
symmetric group representation theory, the positive
cases through degree 5, and the Foulkes–Howe
quadratic-stabilization program. The **degree-6 proof**
and the **stabilization for $`a \geq 6`$, $`b \geq 30`$**
are results I cannot independently verify from training
alone.

## Consequences

**The sixth case of Foulkes' conjecture is proved.**
For every partition of $`n \geq 6`$, the Foulkes
coefficients in degree six are nonnegative
[S3:91–94, S2:503].

**The quadratic stabilization is proved in the stable
range.** The canonical Foulkes–Howe map is
surjective for $`a \geq 6`$ and $`b \geq 30`$
[S4:52–56, S2:503].

## Section skeleton

Two manuscripts: [S3:91–94] (title [S3:85], date [S3:87])
— `main.tex` under `build/` with sections under
`build/sections/`; [S4:52–56] (title [S4:46], date [S4:48])
— `paper.tex` under `build/` with sections under
`build/sections/`. M1 ships a `verification/` bundle
with `programs/`, `support/`, and
`verify_computations.py`. M2 ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The scope note covers the
quadratic stabilization: the canonical Foulkes–Howe
map is surjective for $`a \geq 6`$ and $`b \geq 30`$,
with the sixth-power specialization included only for
$`b \geq 30`$ [S5:9]. The scope note names one
comparator [S5:15]: `FoulkesHowe.lean`.

**The registration.** The family is at tier T3: the
ledger row records `mainres 1` and `paps_form 1`.
`formalization.yaml` registers one `main_results`
entry: `OAI.FoulkesHowe.
canonical_foulkes_howe_surjective` at
`OAI/RepresentationTheory/FoulkesHowe/Stabilization.
lean`. The one registered manuscript (M2, quadratic
stabilization) is in the `sources:` listing. The other
manuscript (M1, sixth power) is **not** in the yaml
`sources:` listing.

**The comparator stub.** The `FoulkesHowe.lean`
comparator states
`theorem canonical_foulkes_howe_surjective` [S6:42]
with a bare `sorry` body [S6:44]:

```lean
theorem canonical_foulkes_howe_surjective :
    ∀ (V : Type u) [AddCommGroup V] [Module ℂ V] [FiniteDimensional ℂ V] (a b : ℕ), 2 ≤ a → a * (a - 1) ≤ b → ∃ μ : SymPow b (SymPow a V) →ₗ[ℂ] SymPow a (SymPow b V), IsFoulkesMap a b V μ ∧ Function.Surjective μ ∧ ∀ ν : SymPow b (SymPow a V) →ₗ[ℂ] SymPow a (SymPow b V), IsFoulkesMap a b V ν → ν = μ := by
  sorry
```
[S6:42–44]

**What the OAI tree carries.** One OAI package carries
a real non-`sorry` proof:

- `OAI/RepresentationTheory/FoulkesHowe` (**77 files
  over 6,095 lines, zero `sorry`**): the
  `canonical_foulkes_howe_surjective` theorem [S7:15].

The release records `scope: "Partial progress."` and
`review: status: unchecked`. The comparator `sorry`
stub is answered by a real proof in the OAI tree. The
sixth-power manuscript (M1) is entirely unregistered.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 210 at [S1:4798] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{210} at [S2:503] |
| S3 | [`preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/build/main.tex`](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/build/main.tex) | 120 | manuscript 1 of 2 (sixth symmetric power); title [S3:85], date [S3:87], abstract [S3:91–94] |
| S4 | [`preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/build/paper.tex`](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/build/paper.tex) | 474 | manuscript 2 of 2 (quadratic stabilization); title [S4:46], date [S4:48], abstract [S4:52–56] |
| S5 | [`lean/docs/210.md`](../../../lean/docs/210.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:15] |
| S6 | [`lean/ComparatorChallenges/FoulkesHowe.lean`](../../../lean/ComparatorChallenges/FoulkesHowe.lean) | 50 | the comparator: the `theorem canonical_foulkes_howe_surjective` [S6:42] and the `sorry` [S6:44] |
| S7 | [`lean/OAI/RepresentationTheory/FoulkesHowe/Stabilization.lean`](../../../lean/OAI/RepresentationTheory/FoulkesHowe/Stabilization.lean) | 51 | the registered declaration in the OAI tree (77 files, 6095 lines, 0 sorry): the real `canonical_foulkes_howe_surjective` theorem [S7:15] |
