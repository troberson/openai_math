[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 193](../index/algebra/193-serres-intersection-multiplicity-conjecture.md)

# 193 — Serre's intersection-multiplicity conjecture

[Index page](../index/algebra/193-serres-intersection-multiplicity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4436] and the catalog abstract [S2:469]
state the family's claim: strict positivity of Serre's
intersection multiplicity $\chi^R(M,N)$ for nonzero finitely
generated modules over any regular local ring, provided
$M \otimes_R N$ has finite length and
$\dim M + \dim N = \dim R$. This resolves the Serre
positivity conjecture, including ramified mixed
characteristic. The manuscript is *Positivity of Serre's
Intersection Multiplicity* [S3:35, S3:37]; its abstract


> We prove Serre's positivity conjecture, including ramified mixed
characteristic. If two nonzero finitely generated modules over a regular local
ring have tensor product of finite length and complementary dimensions, then
their intersection multiplicity is strictly positive. [S3:40–45]

## Undergraduate summary

An **intersection multiplicity** counts how many times two
algebraic objects "meet" at a point, weighted by the
geometry of their intersection. In a **regular local ring**
— the algebraic analogue of a smooth point — two
nonzero modules $M$ and $N$ have an intersection
multiplicity $\chi^R(M,N)$ that measures the "size" of
their overlap when they meet at exactly the right
codimension. **Serre's positivity conjecture** asks: is
this number always **positive** (never zero) when the
modules are nonzero, their tensor product has finite
length, and their dimensions add up to the ring's
dimension? The answer, given by this manuscript, is **yes**
— the intersection multiplicity is strictly positive,
even in the hardest setting (ramified mixed characteristic)
[S3:40–45, S2:469].

## Graduate summary

**The main theorem** [S3:40–45, S2:469]. Let $R$ be a
regular local ring and let $M$, $N$ be nonzero finitely
generated $R$-modules such that $M \otimes_R N$ has finite
length and $\dim M + \dim N = \dim R$. Then the
Serre intersection multiplicity
$\chi^R(M,N) > 0$. The result holds in all characteristics,
including the **ramified mixed characteristic** case
(characteristic $p > 0$ with a ramified residue field
extension) [S3:40–45].

**The scope of the formalization.** The family is at tier
T0: the ledger row records `mainres 0`, `paps_form 0`,
`scope_note 0`, `chal 0`, and `verification 0`. There is
no scope note, no comparator challenge, no `main_results`
entry in `formalization.yaml`, and no verification bundle.
The result is entirely unformalized.

## History of the conjecture

**Serre's intersection multiplicity** $\chi^R(M,N)$ was
introduced by Jean-Pierre Serre in the 1950s as a
generalization of the classical intersection number in
algebraic geometry. For two modules over a regular local
ring with complementary dimensions, the intersection
multiplicity is an integer (or rational number, depending
on the definition) that vanishes if the modules do not
"meet properly." The **posability conjecture** --- that
$\chi^R(M,N) > 0$ whenever $M$ and $N$ are nonzero with
$\dim M + \dim N = \dim R$ and $M \otimes_R N$ of
finite length --- was a major open problem in commutative
algebra. The characteristic-zero case was settled by
Lichtenbaum (1971) using $K$-theoretic methods, and the
equal-characteristic case followed. The **mixed
characteristic** case, especially the **ramified**
subcase, remained open: Lichtenbaum's argument uses the
Chow group of $\mathrm{Spec}(R)$, which behaves
differently in mixed characteristic, and the ramification
of the residue field extension introduces an
additional obstruction. This manuscript resolves the
positivity conjecture in full, including ramified mixed
characteristic [S3:40–45, S2:469].

**Prior (my training data, not this repo).** I know
Serre's intersection multiplicity, the Lichtenbaum
positivity result in characteristic zero and equal
characteristic, and that the mixed-characteristic case was
a major open problem. The **ramified mixed characteristic**
resolution --- with the specific descent, length, and
asymptotic machinery in the manuscript's five sections
— is a result I cannot independently verify from
training alone.

## Consequences

**Serre's positivity conjecture is resolved in full.** For
nonzero finitely generated modules $M$, $N$ over a regular
local ring $R$ with $M \otimes_R N$ of finite length and
$\dim M + \dim N = \dim R$, the intersection
multiplicity $\chi^R(M,N) > 0$ [S3:40–45, S2:469].

**The result includes ramified mixed characteristic.** The
hardest case of the conjecture --- mixed characteristic
with a ramified residue field extension --- is covered
[S3:40–45].

**The proof is entirely in the manuscript.** The family
ships no Lean formalization, no comparator challenge, and
no verification bundle; the result rests on the manuscript's
five-section argument [S3:40–45].

## Section skeleton

One manuscript [S3:40–45] (title [S3:35], date [S3:37]) —
`paper.tex` (50 lines) under `build/`, with five sections
under `build/sections/` (`introduction`, `lengths`,
`descent`, `asymptotic`, `positivity`) and a
`references.tex`. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note under
`lean/docs/`, no comparator challenge under
`lean/ComparatorChallenges/`, no `main_results` entry in
`formalization.yaml`, and no verification bundle under the
manuscript directory. The result is **entirely
unformalized**: the release shipped no Lean code, no
challenge stub, and no checking workflow for this family.
The proof rests solely on the manuscript [S3:40–45].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 193 at [S1:4436] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{193} at [S2:469] |
| S3 | [`preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/paper.tex`](../../../preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/paper.tex) | 53 | the single manuscript root; title [S3:35], date [S3:37], abstract [S3:40–45] |
