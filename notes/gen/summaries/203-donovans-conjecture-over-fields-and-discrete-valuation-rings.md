[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 203](../index/algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md)

# 203 — Donovan's conjecture over fields and discrete valuation rings

[Index page](../index/algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md)

## Original CONTENTS.md summary

The release's blurb [S1:4641] and the catalog abstract [S2:489]
state the family's claim: Donovan's conjecture, proved in
bounded-defect order — over each fixed algebraically
closed field of characteristic $p$, blocks of finite
groups with bounded defect-group order carry only
finitely many Morita-equivalence classes, for every
prime $p$. The integral form over complete mixed-
characteristic discrete valuation rings with
algebraically closed residue field is also proved.
The family ships two manuscripts [S1:4641]:

- *Donovan's Conjecture over Algebraically Closed
  Fields* [S3:8, S3:10]
- *Integral Donovan Finiteness over Witt Vectors*
  [S5:4, S5:6]

The algebraically-closed-fields abstract 

> We prove Donovan's conjecture over every algebraically closed field
$K$ of characteristic $p>0$. For each fixed $K$ and bound on
defect-group order, blocks of finite groups represent only finitely
many $K$-linear Morita equivalence classes. The defect groups need
not be abelian, and the result includes $p=2$.
\endabstract [S4:2–7]

The Witt-vectors abstract 

> We prove integral Donovan finiteness: for every prime $p$ and positive
integer $M$, the blocks of all finite groups with defect groups of order
at most $M$ have only finitely many Morita equivalence classes over
$W(\overline{\mathbb F}_p)$. The defect groups need not be abelian,
and the result includes $p=2$. The same bounded-defect finiteness holds
over each fixed complete discrete valuation ring of characteristic zero [S5:8–14]

## Undergraduate summary

A **finite group** has a natural "building set" of
representations — ways the group acts on a vector
space. In **modular representation theory**, you study
these representations over fields of prime characteristic
$p$ instead of characteristic zero. The representations
sort into **blocks** — families that interact
with each other. Each block has a **defect group**, a
$p$-subgroup that measures how far the block is from
being "semisimple" (trivial). **Morita equivalence** is
a notion of "same representation theory": two blocks
are Morita equivalent if their module categories are
equivalent. **Donovan's conjecture** asks: fix a
$p$-group $P$. Are there only finitely many
non-Morita-equivalent blocks with defect group
$P$? This manuscript pair says **yes** — for
every prime, every algebraically closed field of
characteristic $p$, and every bound on the
defect-group order, there are finitely many such
blocks [S4:2–7, S5:8–14, S2:489].

## Graduate summary

**The field result** [S4:2–7, S2:489]. Fix a
prime $p$, an algebraically closed field $K$ of
characteristic $p$, and a positive integer $M$. There
are only finitely many $K$-linear Morita-equivalence
classes of blocks of finite groups whose defect groups
have order at most $M$. The defect groups need not be
abelian, and the result includes $p = 2$.

**The integral result** [S5:8–14, S2:489]. For
every prime $p$ and positive integer $M$, the blocks of
all finite groups with defect groups of order at most
$M$ have only finitely many Morita-equivalence classes
over $W(\overline{\mathbb{F}}_p)$ (the ring of Witt
vectors over the algebraic closure of
$\mathbb{F}_p$). The same bounded-defect finiteness
holds over each fixed complete discrete valuation ring
of characteristic zero with algebraically closed
residue field of characteristic $p$, including ramified
rings.

**The scope of the formalization.** The family is at
tier T0: the ledger row records `mainres 0`,
`paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note, no comparator
challenge, no `main_results` entry in
`formalization.yaml`, and no verification bundle. The
result is entirely unformalized.

## History of the conjecture

**Donovan's conjecture** (1972) is a central finiteness
problem in modular representation theory. It asks
whether, for a fixed finite $p$-group $P$, there are
only finitely many Morita-equivalence classes of
blocks with defect group $P$. The conjecture is known
for abelian defect groups (**Puig's theorem**, the
**Kessar–Linckelmann** program for nilpotent
blocks), for $p = 2$ in the principal-block case, and
several other families. The bounded-defect-order form
proves a uniform finiteness statement across **all**
$P$ of order at most $M$, which is strictly stronger
than fixing $P$. The two manuscripts attack the
conjecture from complementary directions: the first
establishes the field form via a geometric-combinatorial
classification of block families with bounded defect,
and the second lifts to the integral (Witt-vectors /
mixed-characteristic DVR) setting via a rigidity and
Sylow-structure argument [S4:2–7, S5:8–14,
S2:489].

**Prior (my training data, not this repo).** I know
Donovan's conjecture as a named open problem in modular
representation theory, Puig's theorem for abelian defect
groups, and the known positive cases. The **full
bounded-defect-order proof** — for every prime
including $p = 2$, for non-abelian defect groups, over
both algebraically closed fields and complete mixed-
characteristic DVRs — is a result I cannot
independently verify from training alone.

## Consequences

**Donovan's conjecture is proved in bounded-defect
order.** For every prime, every algebraically closed
field of characteristic $p$, and every defect-order
bound $M$, there are finitely many Morita-equivalence
classes [S4:2–7, S2:489].

**The integral form is also proved.** The same
finiteness holds over Witt vectors and over complete
mixed-characteristic DVRs with algebraically closed
residue field, including ramified rings
[S5:8–14, S2:489].

**The result includes $p = 2$.** No odd-prime
restriction is imposed [S4:2–7, S5:8–14].

## Section skeleton

Two manuscripts: [S3] (title [S3:8], date [S3:10])
— `main.tex` under `build/` with nine sections
under `build/sections/` (`00_introduction` through
`08_periodicity`); [S5:8–14] (title [S5:4], date [S5:6])
— `main.tex` under `build/` with seven sections
under `build/sections/` (`01_introduction` through
`07_assembly`). The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`, `chal 0`,
and `verification 0`. There is no scope note under
`lean/docs/`, no comparator challenge under
`lean/ComparatorChallenges/`, no `main_results` entry in
`formalization.yaml`, and no verification bundle under
the manuscript directories. The result is **entirely
unformalized**: the release shipped no Lean code, no
challenge stub, and no checking workflow for this
family. The proof rests solely on the two manuscripts
[S4:2–7, S5:8–14].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 203 at [S1:4641] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{203} at [S2:489] |
| S3 | [`preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/main.tex`](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/main.tex) | 29 | manuscript 1 of 2 (algebraically closed fields); title [S3:8], date [S3:10] |
| S4 | [`preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/sections/00_introduction.tex`](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/sections/00_introduction.tex) | 242 | manuscript 1's abstract [S4:2–7] |
| S5 | [`preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/main.tex`](../../../preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/main.tex) | 31 | manuscript 2 of 2 (Witt vectors); title [S5:4], date [S5:6], abstract [S5:8–14] |
