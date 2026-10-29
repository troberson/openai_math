[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 196](../index/algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md)

# 196 — A counterexample to Kaplansky's zero-divisor conjecture

[Index page](../index/algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4484] and the catalog abstract [S2:475]
state the family's claim: a finitely presented torsion-free
group $`G`$ whose group algebra
$`\mathbb{F}_2[G]`$ has nonzero zero divisors, disproving
Kaplansky's zero-divisor conjecture. The group has a finite
two-dimensional classifying space. The manuscript is
*A Torsion-Free Group Algebra with Zero Divisors*
[S3:39, S3:41]; its abstract 

> We disprove Kaplansky's zero-divisor conjecture by constructing a finitely presented torsion-free group $`G`$ for which $`\mathbb F_2[G]`$ has nonzero zero divisors. The group admits a finite two-dimensional classifying space. [S3:45]

## Undergraduate summary

A **group algebra** $`\mathbb{F}[G]`$ lets you add up and
multiply "weighted group elements": take a group $`G`$ (a set
of moves you can compose) and a field $`\mathbb{F}`$ (the
allowed "weights"), and form all finite sums
$`\sum c_g\, g`$ where the $`c_g`$ are field elements. You
can multiply these just like polynomials, except the
variables multiply according to the group law. A **zero
divisor** is a nonzero element $`\alpha`$ that you can
multiply by some nonzero $`\beta`$ to get zero.
**Kaplansky's zero-divisor conjecture** says: if $`G`$ is
**torsion-free** (no element returns to the identity after
repeating it finitely many times), then $`\mathbb{F}[G]`$
has **no** zero divisors. This manuscript says **no**
— it constructs a specific finitely presented
torsion-free group where $`\mathbb{F}_2[G]`$ does have
nonzero zero divisors [S3:45, S2:475].

## Graduate summary

**The main theorem** [S3:45, S2:475]. There exists a
finitely presented torsion-free group $`G`$ and nonzero
elements $`\alpha, \beta \in \mathbb{F}_2[G]`$ with
$`\alpha \beta = 0`$. The group $`G`$ admits a finite
two-dimensional classifying space $`K(G,1)`$
[S3:45, S4:11].

**The scope of the formalization.** The scope note states
that the formalized result "constructs a finitely
presented torsion-free group $`G`$ and nonzero elements
$`\alpha,\beta \in \mathbb{F}_2[G]`$ with
$`\alpha\beta=0`$, giving a counterexample" [S4:9]. The
same group admits a finite two-dimensional classifying
space $`K(G,1)`$ [S4:11]. The scope note names one
comparator [S4:17]: `TorsionFreeZeroDivisors.lean`.

## History of the conjecture

**Kaplansky's zero-divisor conjecture** was posed by
Irving Kaplansky in the 1950s and asks whether the group
algebra of a torsion-free group over a field is always
"domain-like" (no zero divisors). The conjecture is known
to be **true** for torsion-free **abelian** groups and for
torsion-free **locally indicable** groups, and it
follows from the **Atiyah conjecture** (itself a deep
open problem in $`L^2`$-index theory) in general. The
**direct-finiteness conjecture** (a one-sided version: if
$`ab = 1`$ then $`ba = 1`$) and the **unit conjecture**
(every unit is a monomial times a field scalar) are
related but distinct. This manuscript **disproves** the
zero-divisor conjecture by constructing a finitely
presented torsion-free group with a finite 2D
classifying space where $`\mathbb{F}_2[G]`$ has nonzero
zero divisors [S3:45, S2:475]. The construction is
explicit and finitely presented, making the counterexample
verifiable in principle.

**Prior (my training data, not this repo).** I know
Kaplansky's zero-divisor conjecture as a classical open
problem in group rings, the known positive cases (abelian,
locally indicable), and its relation to the Atiyah
conjecture. A **disproof by explicit finitely presented
construction** — with a finite 2D classifying
space and nonzero zero divisors in
$`\mathbb{F}_2[G]`$ — is a major result I cannot
independently verify from training alone.

## Consequences

**Kaplansky's zero-divisor conjecture is disproved.** A
finitely presented torsion-free group $`G`$ has
$`\mathbb{F}_2[G]`$ with nonzero zero divisors
[S3:45, S4:9, S2:475].

**The group has a finite 2D classifying space.** The
counterexample group $`G`$ admits a finite
two-dimensional $`K(G,1)`$ [S4:11, S2:475].

**The construction is finitely presented.** The group $`G`$
is given by an explicit finite presentation, making the
counterexample checkable
[S3:45, S4:9].

## Section skeleton

One manuscript [S3:45] (title [S3:39], date [S3:41]) —
`paper.tex` under `build/`, with sections under
`build/sections/` (`topology`, `factors`, `planar`,
`types`, `entropy`) and figures (`block-alignment.tex`,
`band-surgery.tex`). The family ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The scope note describes the
formalized result as constructing "a finitely presented
torsion-free group $`G`$ and nonzero elements
$`\alpha,\beta \in \mathbb{F}_2[G]`$ with
$`\alpha\beta=0`$, giving a counterexample" to
Kaplansky's zero-divisor conjecture. The same group
admits a finite two-dimensional classifying space $`K(G,1)`$
[S4:11]. The scope note names one comparator [S4:17]:
`TorsionFreeZeroDivisors.lean`.

**The registration.** The family is at tier T3: the
ledger row records `mainres 1` and `paps_form 1`.
`formalization.yaml` registers one `main_results`
entry — the
`OAI.KaplanskyCounterexample.finitelyPresented_counterexample`
declaration at
`OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean`
— and the one manuscript is in its `sources:`
listing. The comparator
`TorsionFreeZeroDivisors.lean` is registered [S4:17].

**The comparator stub.** The
`TorsionFreeZeroDivisors.lean` comparator defines
`TorsionFree` (the group torsion-freeness property)
[S5:8–9], `HasFiniteTwoDimensionalClassifyingSpace`
(the finite 2D CW $`K(G,1)`$ property), and `MainTheorem`
— the conjunction of finitely presented,
torsion-free, finite 2D classifying space, and the
existence of nonzero $`\alpha, \beta`$ with
$`\alpha \beta = 0`$ [S5:28–33]. The `theorem main :
MainTheorem` carries a bare `sorry` body
[S5:35–36]:

```lean
def MainTheorem : Prop :=
  ∃ (G : Type) (inst : Group G),
    letI : Group G := inst
    Group.IsFinitelyPresented G ∧ TorsionFree G ∧
    HasFiniteTwoDimensionalClassifyingSpace G ∧
    ∃ α β : MonoidAlgebra (ZMod 2) G, α ≠ 0 ∧ β ≠ 0 ∧ α * β = 0

theorem main : MainTheorem := by
  sorry
```
[S5:28–36]

**What the registered result is.** The OAI tree's
registered declaration `finitelyPresented_counterexample`
[S6:35–40] is a **one-sided-inverses**
(direct-finiteness) statement, not the zero-divisor
statement: it asserts the existence of a field $`K`$ of
characteristic 2, a finitely presented group $`G`$ with an
element of odd prime order, and elements $`a_{\text{out}},
b_{\text{out}}`$ in $`\text{MonoidAlgebra}\, K\, G`$ with
$`a_{\text{out}} \, b_{\text{out}} = 1`$ and
$`b_{\text{out}} \, a_{\text{out}} \neq 1`$
[S6:35–40]. This is the **direct-finiteness**
counterexample (failure of $`ab=1 \Rightarrow ba=1`$), a
related but distinct claim from the zero-divisor
conjecture. The proof discharges by `thm_main.1`, which
assembles the field, the group, the odd-prime-order
element, and the prescribed products from the `Output`
construction 

```lean
theorem finitelyPresented_counterexample :
    ∃ (K : Type) (_ : Field K) (_ : Fintype K) (_ : CharP K 2),
      ∃ (G : Type) (_ : Group G) (_ : Group.IsFinitelyPresented G),
        (∃ (ℓ : ℕ) (_ : ℓ.Prime) (_ : Odd ℓ) (g : G), orderOf g = ℓ) ∧
        ∃ a_out b_out : MonoidAlgebra K G, a_out * b_out = 1 ∧ b_out * a_out ≠ 1 :=
  thm_main.1
```
[S6:35–40]

**What the OAI tree does carry.** The
`OAI/RingTheory/DirectFiniteness` package (**126 files
over 13,310 lines, zero `sorry`**) carries the
`Output` prescribed construction, the finite-search
termination proof, and the one-sided-inverses witness
[S6:35–40].

**The gap between the scope note and the registration.**
The scope note describes the formalized result as the
**zero-divisor** counterexample ($`\alpha\beta = 0`$)
[S4:9], but the registered declaration proves the
**direct-finiteness** counterexample
($`a \, b = 1 \wedge b \, a \neq 1`$) [S6:35–40].
These are related claims about the same group construction
but are **different statements**: zero divisors imply
direct-finiteness failure (take $`\alpha`$ and a nonzero
$`\beta`$ with $`\alpha\beta=0`$; if $`\beta`$ were a unit
then $`\alpha=0`$, contradiction), but the registered
theorem proves the weaker direct-finiteness form, not the
stronger zero-divisor form. The release records
`scope: "Partial progress."` and `review: status:
unchecked`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 196 at [S1:4484] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{196} at [S2:475] |
| S3 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex`](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex) | 108 | the single manuscript root; title [S3:39], date [S3:41], abstract [S3:45] |
| S4 | [`lean/docs/196.md`](../../../lean/docs/196.md) | 17 | the formalization scope note: the scope paragraph [S4:9], the classifying-space sentence [S4:11], and the comparator table [S4:17] |
| S5 | [`lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean`](../../../lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean) | 40 | the comparator: the `TorsionFree` definition [S5:8–9], the `MainTheorem` definition [S5:28–33], the `main` theorem [S5:35] and the `sorry` [S5:36] |
| S6 | [`lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean`](../../../lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean) | 44 | the registered declaration in the OAI tree (126 files, 13310 lines, 0 sorry): the real `finitelyPresented_counterexample` proof [S6:35–40] via `thm_main` and the `Output` prescribed construction |
