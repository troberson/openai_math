[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 202](../index/algebra/202-blockwise-alperin-weight-conjecture.md)

# 202 — The blockwise Alperin weight conjecture

[Index page](../index/algebra/202-blockwise-alperin-weight-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4632] and the catalog abstract [S2:487]
state the family's claim: the numerical blockwise Alperin
weight conjecture, proved for every prime and every finite
group — the number of irreducible Brauer characters in
a p-block equals the number of conjugacy classes of its
weights. The manuscript is *The Blockwise Alperin Weight
Conjecture* [S3:69, S3:71]; its abstract 

> \setlength{\emergencystretch}1.5em
\titleThe Blockwise Alperin Weight Conjecture
\authorOpenAI
\dateSeptember 23, 2026 [S3:74–77]

## Undergraduate summary

A finite group can be "decorated" with a prime number
$p$ — this is called a **modular setting**, and it
lets you study the group's symmetries using fields of
characteristic $p$ instead of characteristic zero. In this
setting, the irreducible representations
("characters") of the group break into **blocks**
— smaller families of characters that interact
with each other. The **Alperin weight conjecture** is a
census: it says the number of characters in a certain
subset ("Brauer characters") of a block should equal the
number of **weights** (a combinatorial object attached to
the block — roughly, ways to decompose a
$p$-subgroup into a chain where each link has a
faithful irreducible character). The **blockwise**
version asks this census to hold **block by block**, not
just in total. This manuscript says **yes** — for
every finite group, every prime, every block
[S3:74–77, S2:487].

## Graduate summary

**The main theorem** [S3:74–77, S2:487]. Let $G$
be a finite group and $p$ a prime. For every $p$-block
$B$ of $G$, the number of irreducible Brauer characters
in $B$ equals the number of conjugacy classes of
$B$-weights. This is the numerical (quantitative) form
of the blockwise Alperin weight conjecture.

**The scope of the formalization.** The family is at
tier T0: the ledger row records `mainres 0`,
`paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note, no comparator
challenge, no `main_results` entry in
`formalization.yaml`, and no verification bundle. The
result is entirely unformalized.

## History of the conjecture

The **Alperin weight conjecture** (1986) is one of the
central conjectures in modular representation theory.
It generalizes **Brauer's height-zero conjecture** and
is related to the **k-conjecture** (Feit) and the
**p-defect** structure of blocks. The **blockwise**
version refines the original into a block-by-block
statement. Partial results are known: the conjecture
holds for nilpotent blocks, for blocks with abelian
defect groups, and for several families of finite
groups (alternating groups, symmetric groups in certain
ranges, groups of Lie type in defining characteristic).
The proof strategy in this manuscript uses a
geometric-algebraic approach: it connects block
structure to **curve covers** and **inseparable genus
bounds**, with **differentials**, **valuations**, and a
**specialization** argument [S3:74–77, S2:487].

**Prior (my training data, not this repo).** I know the
Alperin weight conjecture as a named open problem in
modular representation theory, its partial positive
cases, and its connections to the k-conjecture and
Brauer's height-zero conjecture. A **full proof** of the
blockwise numerical form for every finite group and
every prime — via the curve-cover / valuations /
specialization route — is a result I cannot
independently verify from training alone.

## Consequences

**The numerical blockwise Alperin weight conjecture is
proved.** For every finite group, every prime, and every
$p$-block, the Brauer-character count equals the
weight-class count [S3:74–77, S2:487].

**The result is uniform.** No restriction on the group
order, the prime, or the block structure is imposed
[S3:74–77].

## Section skeleton

One manuscript [S3:74–77] (title [S3:69], date [S3:71]) —
`paper.tex` under `build/`, with eight sections under
`build/sections/` (`intro`, `foundations`, `group`,
`twist`, `differentials`, `valuations`,
`specialization`, `consequences`) and a `references.bib`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`, `chal 0`,
and `verification 0`. There is no scope note under
`lean/docs/`, no comparator challenge under
`lean/ComparatorChallenges/`, no `main_results` entry in
`formalization.yaml`, and no verification bundle under
the manuscript directory. The result is **entirely
unformalized**: the release shipped no Lean code, no
challenge stub, and no checking workflow for this
family. The proof rests solely on the manuscript
[S3:74–77].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 202 at [S1:4632] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{202} at [S2:487] |
| S3 | [`preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/paper.tex`](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/paper.tex) | 103 | the single manuscript root; title [S3:69], date [S3:71], abstract [S3:74–77] |
