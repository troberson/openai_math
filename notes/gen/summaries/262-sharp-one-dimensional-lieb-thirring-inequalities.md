[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 262](../index/mathematical-physics/262-sharp-one-dimensional-lieb-thirring-inequalities.md)

# 262 — Sharp one-dimensional Lieb–Thirring inequalities

[Index page](../index/mathematical-physics/262-sharp-one-dimensional-lieb-thirring-inequalities.md)

## Original CONTENTS.md summary

[S1:6552] (family entry):

> **262. Sharp finite-matrix Lieb–Thirring inequalities and all equality cases.** Proves the sharp one-dimensional Lieb–Thirring inequality for $`1/2 < \gamma < 3/2`$ and arbitrary finite-matrix potentials $`W \geq 0`$ with $`\int \mathrm{tr}(W^{\gamma+1/2}) < \infty`$: the optimal constant is the scalar one-bound-state value, independent of matrix size. All equality cases are direct sums, in one constant unitary basis, of scalar sech$`^2`$ solitons with independent scales and centers, and zero channels. ([Lean](../../../lean/docs/262.md))

[S2:615] carries the `\resultentry`, so the release blurb and the overview agree.
The three manuscripts:

**Sharp one-dimensional Lieb–Thirring constants (scalar)** [S3:6, S3:8]:

> We resolve affirmatively the remaining cases of the scalar one-dimensional
Lieb–Thirring conjecture: for every $`\frac12<\gamma<\frac32`$,
the optimal constant is the one-bound-state constant.
The estimate holds for every nonnegative potential in
$`L^{\gamma+1/2}(\mathbb R)`$, with all negative eigenvalues included. [S3:11–17]

**Sharp inequality for matrix potentials** [S4:3, S4:5]:

> We prove the sharp one-dimensional Lieb–Thirring inequality for every finite
matrix size and every exponent $`1/2<\gamma<3/2`$. The optimal constant is the
scalar one-bound-state constant, independently of the matrix size. The
inequality bounds the full sum of negative eigenvalue moments for every
measurable Hermitian positive semidefinite potential $`W`$ satisfying
$`\int_\mathbb R\mathrm{tr}(W^{\gamma+1/2})<\infty`$. The matrices may have arbitrary rank and
need not commute at different points. [S4:8–16]

**Equality cases in the matrix inequality** [S5:3, S5:5]:

> We classify all equality cases in the sharp one-dimensional Lieb–Thirring
inequality for every finite matrix size and $`1/2<\gamma<3/2`$. For measurable
Hermitian positive semidefinite potentials $`W`$ with
$`\int_\mathbb R\mathrm{tr}(W^{\gamma+1/2})<\infty`$, equality holds precisely for direct sums,
in one constant unitary basis, of scalar one-bound-state solitons and zero
channels. The nonzero solitons may have independent scales and centers. [S5:8–15]

## Undergraduate summary

The **Lieb–Thirring inequality** is a bound on how negative
the "energy levels" (eigenvalues) of a quantum particle can get
when it sits in a potential well: it says the sum of the
negative energy levels, raised to a certain power, is bounded by
a constant times an integral of the potential. The "sharp"
version asks for the **best possible** constant. The first
manuscript pins down the optimal constant in one dimension for
the full range $`1/2 < \gamma < 3/2`$ [S3:12–16, S2:615].
The second extends the inequality to **matrix-valued**
potentials (the potential is a matrix at each point, not just a
number) and shows the same scalar constant is optimal regardless
of the matrix size [S4:9–15]. The third classifies **all
equality cases**: the only potentials that attain the bound are
built from a very specific "sech-squared soliton" shape [S5:9–14].

## Graduate summary

**Sharp scalar one-dimensional Lieb–Thirring constant**
[S3:12–16, S2:615]. For
every
$`1/2 < \gamma < 3/2`$
and
every
nonnegative
$`W \in L^{\gamma+1/2}(\mathbb R)`$,
the full negative-eigenvalue moment of
$`-d^2/dx^2 - W`$
is bounded by the one-bound-state constant times
$`\int W^{\gamma+1/2}`$,
with all negative eigenvalues included. The constant is optimal and is
attained by $`(r+1)\mathrm{sech}^2(rx)`$, where
$`r = (\gamma - 1/2)^{-1}`$
[S6:9]. This resolves the remaining cases of the scalar one-dimensional
Lieb–Thirring conjecture [S3:12–16].

**Matrix-potential inequality** [S4:9–15, S2:615]. For every finite
matrix size and every
$`1/2 < \gamma < 3/2`$,
the full sum of negative eigenvalue moments for every measurable
Hermitian positive semidefinite potential $`W`$ with
$`\int \mathrm{tr}(W^{\gamma+1/2}) < \infty`$
is bounded by the scalar one-bound-state constant independently of the
matrix size; the matrices may have arbitrary rank and need not commute
at different points.

**Equality cases** [S5:9–14, S2:615]. Equality in the matrix inequality
holds precisely for direct sums, in one constant unitary basis, of
scalar one-bound-state (soliton) potentials and zero channels; the
nonzero solitons may have independent scales and centers.

## History of the conjecture

The **Lieb–Thirring conjecture** (1976, Lieb and Thirring) predicted the
sharp constant in the Lieb–Thirring inequality. The constant was known
in one dimension for a subrange of exponents (via the classical results
of Lieb, Solomon, and others), and in higher dimensions for the
"nonrelativistic" range
$`\gamma > (d-1)/2`$,
but the one-dimensional range $`1/2
< \gamma < 3/2`$
had remaining open cases — in particular the extremal end near $`\gamma
= 1/2`$.
The first manuscript [S3:12–16] resolves those remaining scalar cases in
full. The **matrix-valued** extension [S4:9–15] is the spin-orbit-
coupled version of the inequality: the potential is a matrix at each
point, and the result shows the scalar constant survives arbitrary
matrix size and non-commutativity. The **equality-case classification**
[S5:9–14] characterizes exactly which potentials attain the bound,
showing they are precisely the direct sums of one-bound-state solitons
and zero channels.

**Prior (my training data, not this repo).** The Lieb–Thirring
inequality, the one-bound-state constant, and the sech$`^2`$ soliton are
standard in mathematical physics and spectral theory. The full
resolution of the scalar one-dimensional range $`1/2
< \gamma < 3/2`$,
the matrix-valued extension with the size-independent constant, and the
complete equality-case classification are the novel contributions. I
cannot confirm these independently from training alone.

## Consequences

- **The
scalar one-dimensional Lieb–Thirring constant determined**
  [S3:12–16, S2:615]:
  for
  every
  $`1/2 < \gamma < 3/2`$,
the optimal constant is the one-bound-state value, resolved for all
negative eigenvalues.
- **The
matrix extension with a size-independent constant** [S4:9–15]: the
scalar one-bound-state constant is optimal for arbitrary finite matrix
size, with non-commuting matrix potentials allowed.
- **All
equality cases classified** [S5:9–14]: the extremizers are precisely the
direct sums, in one constant unitary basis, of scalar one-bound-state
solitons with independent scales and centers, and zero channels.

## Section skeleton

Three manuscripts. [S3:11–17] (title [S3:6], date [S3:8]) — `main.tex` under
`build/`. [S4:8–16] (title [S4:3], date [S4:5]) — `main.tex` under `build/`.
[S5:8–15] (title [S5:3], date [S5:5]) — `main.tex` under `build/`. The family
ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S6],
one comparator stub [S7], and one `main_results` entry [S9]. The scope
note links **only the scalar-constants manuscript** [S3:11–17] [S6:5]; the
matrix-potential [S4:8–16] and equality-case [S5:8–15] manuscripts are outside the
formalization. The recorded scope [S6:9] is the sharp one-dimensional
scalar Lieb–Thirring constant for
$`1/2 < \gamma < 3/2`$:
for
every
nonnegative
$`W \in L^{\gamma+1/2}(\mathbb R)`$,
the full negative-eigenvalue moment of
$`-d^2/dx^2 - W`$
is bounded by the one-bound-state constant times the potential integral.
The constant is optimal and is attained by
$`(r+1)\mathrm{sech}^2(rx)`$ with
$`r = (\gamma - 1/2)^{-1}`$;
no finite spectral cutoff is imposed [S6:9].

The `main_results` entry [S9:1399–1401] names
`OAI.SharpLiebThirring.sharp_lieb_thirring` in
`lean/OAI/Analysis/LiebThirring/Main.lean`. In the source, the theorem
`sharp_lieb_thirring` is stated and closed at [S8:38]. `grep` finds
**zero** `sorry` in the whole `lean/OAI/Analysis/LiebThirring/` tree (62
`.lean` files).

The one comparator stub [S7] states `sharp_lieb_thirring` at [S7:94] and
ends in `sorry` ([S7:95]). The proved copy lives under `lean/OAI/`. A
comparator stub is a target the release set itself; the proved version,
where it exists, lives under `lean/OAI/`. The reading is of source text
only — no `lake` or `lean` run elaborates the proof.

**Tree measurement (source-level).**

The `main_results` entry OAI.SharpLiebThirring.sharp_lieb_thirring resolves to `OAI/Analysis/LiebThirring/Main.lean` (56 lines); the top-level theorem is `theorem sharp_lieb_thirring`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 62 files, 13 theorems, 224 defs.

The preprint states 37 theorem environments while the tree carries only 13 (0.35×), indicating a focused sub-formalization (source-level).

## Coverage

The ledger row `fam=262` [S10] records the tier and the counts:
`tier=T3`, `paps=3`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `verification=0`, `trace=`. The `paps_form=1` against
`paps=3` is the coverage signature: the scope note links only the
scalar-constants manuscript [S6:5], and the single `main_results` entry
over that config reaches the scalar sharp constant for
$`1/2 < \gamma < 3/2`$
[S6:9]. The matrix-potential manuscript [S4:8–16] and the equality-case
manuscript [S5:8–15] are outside the formalization — no scope-note source
entry, no comparator stub, and no `main_results` entry for either — so
the matrix extension and the equality-classification claims remain
unformalized. There is no verification bundle and no reasoning trace.
The shape flags are `bound|uniform`, and `resolves_named=0` — the blurb
states the sharp-constant result without naming a conjecture in the
resolve form the ledger flags.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6552] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 262 at [S2:615] |
| S3 | [`preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/build/main.tex`](../../../preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/build/main.tex) | 29 | manuscript 1 of 3 (scalar constants, the one the scope note links); title [S3:6], date [S3:8], abstract [S3:12–16] |
| S4 | [`preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/build/main.tex`](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/build/main.tex) | 26 | manuscript 2 of 3 (matrix-potential inequality); title [S4:3], date [S4:5], abstract [S4:9–15] |
| S5 | [`preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/build/main.tex`](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/build/main.tex) | 29 | manuscript 3 of 3 (equality cases); title [S5:3], date [S5:5], abstract [S5:9–14] |
| S6 | [`lean/docs/262.md`](../../../lean/docs/262.md) | 15 | scope note — links only the scalar-constants manuscript [S6:5], states the formalized scope at [S6:9], and its one comparator link at [S6:15] |
| S7 | [`lean/ComparatorChallenges/LiebThirring.lean`](../../../lean/ComparatorChallenges/LiebThirring.lean) | 100 | comparator stub — `sharp_lieb_thirring` at [S7:94] with its `sorry` at [S7:95] |
| S8 | [`lean/OAI/Analysis/LiebThirring/Main.lean`](../../../lean/OAI/Analysis/LiebThirring/Main.lean) | 56 | the formalized file — `sharp_lieb_thirring` at [S8:38] |
| S9 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.SharpLiebThirring.sharp_lieb_thirring`, at [S9:1399–1401] |
| S10 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=262`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
