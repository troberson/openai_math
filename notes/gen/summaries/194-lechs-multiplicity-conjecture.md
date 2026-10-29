[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 194](../index/algebra/194-lechs-multiplicity-conjecture.md)

# 194 — Lech's multiplicity conjecture

[Index page](../index/algebra/194-lechs-multiplicity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4452] and the catalog abstract [S2:471]
state the family's claim: Hilbert–Samuel multiplicity
cannot decrease under a flat local homomorphism of nonzero
Noetherian local rings — $`e(R) \leq e(S)`$ —
resolving Lech's multiplicity conjecture in every dimension
and characteristic. The manuscript is *Lech's multiplicity
conjecture* [S3:53, S3:55]; its abstract 

> We prove Lech's multiplicity conjecture: Hilbert–Samuel multiplicity
cannot decrease under a flat local homomorphism of nonzero Noetherian
local rings. The result holds in arbitrary dimension, with no restrictions
on the residue fields or characteristics. [S3:60–63]

## Undergraduate summary

Think of two **rings** $`R`$ and $`S`$, where $`R \to S`$ is a
**flat** map (roughly: the map doesn't create hidden
torsion) and both are **local** (they have one "maximal
point"). A **multiplicity** $`e`$ is a number that measures
the "size" of a local ring — how many ways its
elements fill up the neighborhood of the maximal point.
The question is: can a flat map make the target ring
"smaller" than the source, as measured by this number?
The answer is **no** — the multiplicity of $`S`$ is
always at least the multiplicity of $`R`$. This holds in
every dimension and every characteristic, with no
restrictions on the residue fields
[S3:60–63, S2:471].

## Graduate summary

**The main theorem** [S3:60–63, S4:9]. For every flat
local homomorphism $`(R,\mathfrak{m}) \to
(S,\mathfrak{n})`$ of nonzero Noetherian local rings, the
Hilbert–Samuel multiplicity satisfies
$`e(R) \leq e(S)`$ [S3:60–63]. The result holds in
arbitrary dimension, with no restrictions on the residue
fields or characteristics [S3:60–63]. The proof
follows Dutta's approach via Frobenius: in characteristic
$`p`$, the multiplicity is bounded by a
**Dutta multiplicity** $`\mu_p(F)`$ computed from the
Frobenius pushforward of a short complex $`F`$; the
characteristic-zero and mixed-characteristic cases reduce
to the characteristic-$`p`$ case
[S4:9, S5:62–70].

**The scope of the formalization.** The scope note states
the formalization proves Hilbert–Samuel multiplicity
cannot decrease under a flat local homomorphism of nonzero
Noetherian local rings. The proof follows Dutta's approach
via Frobenius, characteristic-zero, and mixed-characteristic
reductions; a characteristic-$`p`$ Dutta-lemma package is
included, and the characteristic-zero and mixed-characteristic
steps are reduced to finitely many explicitly listed cases
[S4:9]. The scope note names one comparator [S4:15]:
`DuttaDomain.lean`.

## History of the conjecture

**Lech's multiplicity conjecture** was posed by
Krzysztof Lech in the 1980s and asks whether
Hilbert–Samuel multiplicity is monotone under flat
local homomorphisms of Noetherian local rings. The
conjecture is a natural generalization of the classical
fact that embedding dimension does not increase under flat
maps. For decades, partial results covered special cases:
the equality $`e(R) = e(S)`$ when $`R \to S`$ is a
**regular** map, and the inequality in
characteristic zero via **K-theoretic** methods
(Lichtenbaum, 1971). The general case in arbitrary
characteristic was open. The key obstruction in mixed
characteristic is the failure of the **Frobenius**
endomorphism to be flat, which breaks the standard
comparative-geometry argument. This manuscript resolves
the conjecture in full by combining three reductions:
Frobenius (characteristic $`p`$), characteristic zero, and
mixed characteristic [S3:60–63, S2:471].

**Prior (my training data, not this repo).** I know
Lech's multiplicity conjecture as a named open problem in
commutative algebra, the partial results in
characteristic zero and for regular maps, and that the
mixed-characteristic case was the principal obstruction.
The **full resolution** via Frobenius, characteristic-zero,
and mixed-characteristic reductions — with the
specific Dutta-lemma package and finitely many explicitly
listed cases — is a result I cannot independently
verify from training alone.

## Consequences

**Lech's multiplicity conjecture is resolved.** For every
flat local homomorphism of nonzero Noetherian local rings,
$`e(R) \leq e(S)`$ [S3:60–63, S4:9, S2:471].

**The result covers all dimensions and characteristics.**
No restrictions on the residue fields or on the
characteristic of the rings [S3:60–63].

**The reduction is to finitely many cases.** The
characteristic-zero and mixed-characteristic steps reduce
to finitely many explicitly listed cases
[S4:9].

## Section skeleton

One manuscript [S3:60–63] (title [S3:53], date [S3:55]) —
`main.tex` (360 lines) under `build/`, with six sections
under `build/sections/` (`lengths`, `charp`, `charzero`,
`mixed`, `reductions`, `complex`) and a
`references.tex`. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves
Hilbert–Samuel multiplicity cannot decrease under a
flat local homomorphism of nonzero Noetherian local rings.
The proof follows Dutta's approach via Frobenius,
characteristic-zero, and mixed-characteristic reductions; a
characteristic-$`p`$ Dutta-lemma package is included, and
the characteristic-zero and mixed-characteristic steps are
reduced to finitely many explicitly listed cases [S4:9].
The scope note names one comparator [S4:15]:
`DuttaDomain.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry
for this family and the manuscript is **not** in its
`sources:` listing. There is **no OAI tree** for this
family: no directory under `lean/OAI/` carries this
result. The comparator `DuttaDomain.lean` defines the
Hilbert–Samuel multiplicity (`multiplicity`), the
Frobenius complex machinery (`frobeniusComplex`,
`shortEuler`, `duttaSequence`, `duttaMultiplicity`), and
the target proposition `DuttaDomainClaim` — for a
short complex $`F`$ over a complete characteristic-$`p`$
domain $`D`$, the Hilbert–Samuel multiplicity of $`D`$
is bounded by the Dutta multiplicity
$`\mu_p(F)`$ 

```lean
def DuttaDomainClaim : Prop :=
  ∀ (D : Type u) [CommRing D] [IsNoetherianRing D] [IsLocalRing D] [IsDomain D]
    [IsAdicComplete (IsLocalRing.maximalIdeal D) D]
    (p : ℕ) [Fact p.Prime] [CharP D p]
    (F : CochainComplex (ModuleCat.{u} D) ℤ), IsShortComplex D F →
      (∀ n i,IsFiniteLength D ((frobeniusComplex D p n F).homology i)) ∧
      Tendsto (duttaSequence D p F) atTop (𝓝 (duttaMultiplicity D p F)) ∧
      multiplicity D ≤ duttaMultiplicity D p F
end Lech
```
[S5:62–70]

The single theorem `dutta_domain` restates this claim with
a bare `sorry` body 

```lean
theorem dutta_domain : DuttaDomainClaim.{u} := by
  sorry
```
[S5:74–75]

**No proof exists in the Lean library.** Unlike the T2
sub-shape where the OAI tree carries a real proof that is
simply unregistered, here there is **no OAI tree at all** —
no directory, no files, no proof of any part of the
comparator's target. The scope note describes a full
proof strategy (Frobenius, characteristic-zero, and
mixed-characteristic reductions) and names a
characteristic-$`p`$ Dutta-lemma package, but no Lean code
implements any of it. The gap is **total absence**, not
registration. The release records `scope: "Partial
progress."` and `review: status: unchecked`; the
comparator's `sorry` is the target the release set, and no
Lean proof of `dutta_domain` exists in the library.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 194 at [S1:4452] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{194} at [S2:471] |
| S3 | [`preprints/Lechs-multiplicity-conjecture-September-23-2026/build/main.tex`](../../../preprints/Lechs-multiplicity-conjecture-September-23-2026/build/main.tex) | 360 | the single manuscript root; title [S3:53], date [S3:55], abstract [S3:60–63] |
| S4 | [`lean/docs/194.md`](../../../lean/docs/194.md) | 17 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:15] |
| S5 | [`lean/ComparatorChallenges/DuttaDomain.lean`](../../../lean/ComparatorChallenges/DuttaDomain.lean) | 81 | the comparator: the `DuttaDomainClaim` definition [S5:62–70], the `dutta_domain` theorem [S5:74] and the `sorry` [S5:75] |
