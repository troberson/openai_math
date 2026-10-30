[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 298](../index/operator-algebras/298-a-counterexample-to-voiculescus-free-entropy-equality-conjecture.md)

# 298 — A counterexample to Voiculescu’s free-entropy equality conjecture

[Index page](../index/operator-algebras/298-a-counterexample-to-voiculescus-free-entropy-equality-conjecture.md)

## Original CONTENTS.md summary

[S1:7407] (family entry):

> **298. Two notions of free entropy differ even when both are finite.** Constructs a bounded self-adjoint tuple in a tracial von Neumann algebra whose microstates and nonmicrostates free entropies satisfy $`-\infty\lt \chi\lt \chi^*\lt \infty`$. This answers Voiculescu’s finite-entropy equality question negatively: the matrix-approximation and free-Fisher-information definitions differ even when both are finite. ([Lean](../../../lean/docs/298.md))

[S2:690] carries the `\resultentry` with the single manuscript [S3:24, S3:26]. The abstract 

> We answer the finite-entropy equality question for microstates and
nonmicrostates free entropy negatively. We construct a bounded self-adjoint
tuple $`X`$ in a von Neumann algebra with faithful normal tracial state such that
$`-\infty<\chi(X)\leq\chi^*(X)-\tfrac12<\infty`$.
Here $`\chi`$ is the original microstates entropy with an operator-norm
cutoff and a limsup over matrix sizes. The counterexample uses a large but
fixed number of variables. [S3:29–37]

## Undergraduate summary

**Free entropy** is the analogue of classical entropy for random variables
that don't commute. Voiculescu introduced two closely related versions:
the **microstates** free entropy $`\\chi`$, which measures how many ways the
variables can be approximated by matrices, and the **nonmicrostates**
free entropy $`\\chi^*`$, which is defined through a free-Fisher-information
formula and is more tractable analytically.

Voiculescu proved that the two are equal, but his proof only covered the
case where the entropy is $`-\\infty`$. The **finite-entropy equality
question** asked whether the two still agree when both are finite. The
answer is **no** [S3:29–37].

This paper constructs a bounded self-adjoint tuple $`X`$ in a von Neumann
algebra with a faithful normal tracial state, with a **hard quantitative
gap** between the two entropies:
$`-\\infty < \\chi(X) \\le \\chi^*(X) - 1/2 < \\infty`$.
The two notions differ by at least $`1/2`$ even though both are finite.
The counterexample uses a large but fixed number of variables [S4:9] —
it is not a one-variable phenomenon.

## Graduate summary

**Main theorem** [S3:29–37, S2:690].
There exist a von Neumann algebra $`M`$ with a faithful normal tracial
state, and a bounded self-adjoint tuple $`X = (X_1, \\ldots, X_k) \\in
M^k`$, such that the microstates free entropy
$`\\chi(X)`$ and the nonmicrostates free entropy $`\\chi^*(X)`$ satisfy
$`-\\infty < \\chi(X) \\le \\chi^*(X) - 1/2 < \\infty`$. Here $`\\chi`$ is
Voiculescu's original microstates entropy — an operator-norm cutoff with
a limsup over matrix sizes — and $`\\chi^*`$ is the nonmicrostates entropy
defined using free semicircular noise [S4:9]. The tuple has a fixed
finite number of variables.

**The $`1/2`$ gap.** The separation is quantitative, not merely strict
inequality: the construction forces a uniform gap of at least $`1/2`$
between the two entropies. This rules out any theorem that the two
agreement up to a vanishing error in the large-matrix limit [S4:9].

**Fixed finite dimension.** The counterexample is at a fixed, finite $`k`$
[S4:9] — the separation is not an artifact of a limit as the number of
variables grows.

## History of the conjecture

The two definitions of free entropy — microstates and nonmicrostates —
are both due to Voiculescu. The microstates entropy $`\\chi`$ comes from
the original matrix-approximation definition: one counts the volume of
tuples of $`n \\times n`$ matrices that approximate $`X`$ in operator norm,
and takes a scaled limsup as $`n \\to \\infty`$. The nonmicrostates
entropy $`\\chi^*`$ was introduced later through a free-Fisher-information
identity, and is easier to work with analytically because it avoids the
limsup over matrix sizes.

Voiculescu proved $`\\chi = \\chi^*`$ under a $`-\\infty`$ hypothesis.
The finite-entropy case — where both are finite — was the open half.
This paper [S3:29–37] settles it negatively with a quantitative
counterexample. The construction is visible in the section skeleton
(`fisher`, `signal`, `flow`, `blocks`), using a flow/blocks argument
to build the separation.

**Prior (my training data, not this repo).** The microstates and
nonmicrostates free entropies are both classical objects in free
probability, and their equality outside the $`-\\infty`$ case was a known
open question. A bounded finite-dimensional counterexample with a
uniform $`1/2`$ gap is the novel contribution claimed here; I cannot
verify the free-probabilistic construction independently from training
alone.

## Consequences

- **The finite-entropy equality question is answered negatively**
  [S3:29–37, S2:690]: there is a bounded self-adjoint tuple in a
  tracial von Neumann algebra with
  $`-\\infty < \\chi(X) \\le \\chi^*(X) - 1/2 < \\infty`$. This is the
  named counterexample the ledger's `resolves_named` and
  `counterex_broad` flags record.
- **A uniform quantitative gap** [S3:32–33]: the separation is at least
  $`1/2`$, so the two entropies cannot be reconciled by any vanishing
  large-matrix error.
- **A fixed-finite-variable counterexample** [S4:9]: the separation
  occurs at a fixed, finite number of variables, not in an asymptotic
  limit in $`k`$.
- **The two definitions of free entropy are genuinely distinct** 
  [S3:29–37, S4:9]: the matrix-approximation and free-Fisher-information
  definitions differ even when both are finite.

## Section skeleton

One manuscript [S3:29–37]. Root `build/paper.tex` (53 lines), abstract in the
root [S3:29–37]. Sections under `build/sections/`: `01-introduction`,
`02-conventions`, `03-fisher`, `04-signal`, `05-flow`, `06-blocks`,
plus a `references.tex`. No verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note [S4:9]
and one comparator stub [S5]. There is **no** `main_results` entry, and
no proved OAI tree. The T2 shape is "scope note and comparator stubs
exist, but no `main_results` entry and no proved OAI tree."

The scope note [S4:9] selects the finite-entropy separation: a bounded
self-adjoint tuple $`X`$ in a von Neumann algebra with a faithful normal
tracial state such that
$`-\\infty < \\chi(X) \\le \\chi^*(X) - 1/2 < \\infty`$, with $`\\chi`$ the
microstates entropy (operator-norm cutoff, limsup over matrix sizes) and
$`\\chi^*`$ the nonmicrostates entropy (free semicircular noise), at a
fixed finite number of variables [S4:9].

The single comparator stub carries 1 `sorry`:
`FiniteEntropySeparation.lean` (125 lines) with `theorem main` at
[S5:108] and the `sorry` at [S5:119]. The statement the release set for
the comparator is the finite-entropy separation itself; no proved copy
exists under `lean/OAI/`. The reading is of source text only.

## Coverage

The ledger row `fam=298` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=682`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stub exist, with no `main_results`
entry." The single comparator stub carries 1 `sorry`. The shape flags
are `shapes=counterexample|bound`, `counterex_broad=1`,
`resolves_named=1` — this is a counterexample family resolving
Voiculescu's finite-entropy equality question.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7407] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 298 at [S2:690] |
| S3 | [`preprints/A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026/build/paper.tex`](../../../preprints/A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026/build/paper.tex) | 46 | manuscript (root); title [S3:24], date [S3:26], abstract [S3:29–37] |
| S4 | [`lean/docs/298.md`](../../../lean/docs/298.md) | 15 | scope note — Scope at [S4:9] and the comparator link `FiniteEntropySeparation.lean` |
| S5 | [`lean/ComparatorChallenges/FiniteEntropySeparation.lean`](../../../lean/ComparatorChallenges/FiniteEntropySeparation.lean) | 125 | comparator stub — 125 lines, 1 `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=298`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
