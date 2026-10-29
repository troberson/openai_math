[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 148](../index/dynamical-systems-and-ergodic-theory/148-dimension-formula-for-self-similar-measures-on-the-line.md)

# 148 — The dimension formula for self-similar measures on the line

[Index page](../index/dynamical-systems-and-ergodic-theory/148-dimension-formula-for-self-similar-measures-on-the-line.md)

## Original CONTENTS.md summary

The release's blurb [S1:3550] and the catalog abstract [S2:377] state
the family's claim: for every self-similar measure on the line generated
by finitely many contracting similarities, the Hausdorff dimension
equals
$\min\{1,h_{\mathrm{RW}}/\chi\}$, where $h_{\mathrm{RW}}$ is the
entropy rate of the random composed maps and $\chi$ the average
logarithmic contraction. This resolves the entropy-rate dimension
conjecture without a separation assumption, allowing exact overlaps and
unequal, even signed, contraction ratios. The manuscript's abstract


> We prove that the Hausdorff dimension of every finite real self-similar
measure equals the minimum of one and its random-walk entropy rate divided
by its Lyapunov exponent. Exact overlaps are allowed, and the contraction
ratios may be unequal and negative. This resolves the entropy-rate dimension
conjecture. [S3:46–50]

## Undergraduate summary

A *self-similar measure* on the line is built from a finite set of
contracting similarities $x\mapsto r_i x+t_i$ (with
$|r_i|<1$) together with a set of positive weights: a point is produced
by a random infinite composition indexed by a weighted random sequence,
and the measure is the distribution of its limit. The *Hausdorff
dimension* measures how much the measure spreads over the line, on a
scale from $0$ (a point) to $1$ (spreading along the whole line). The
*random-walk entropy rate* $h_{\mathrm{RW}}$ is how fast a random
composition forgets its past; the *Lyapunov exponent* $\chi$ is the
average logarithmic contraction per step. The entropy-rate dimension
conjecture says the dimension is controlled by the ratio
$h_{\mathrm{RW}}/\chi$. This manuscript proves the formula
$\dim_{\mathrm H}\mu=\min\{1,h_{\mathrm{RW}}/\chi\}$ in full
generality — no open-set or separation condition, exact overlaps
allowed, ratios unequal and negative [S3:46–50, S4:9].

## Graduate summary

**The dimension formula (fully general)** [S3:46–50, S4:9]. For
every finite real self-similar probability measure with positive weights
and contraction ratios of absolute value below one, the lower Hausdorff
dimension equals
$\min\{1,h_{\mathrm{RW}}/\chi\}$, where $h_{\mathrm{RW}}$ is the
entropy rate of the random affine compositions and $\chi$ the
corresponding Lyapunov exponent in the same logarithmic base. The ratios
may be signed and unequal, and exact overlaps are allowed [S4:9].

**The registered declaration.** The `main_results` entry names
`OAI.EntropyRateDimension.entropy_rate_dimension` in
`OAI/MeasureTheory/SelfSimilar/Main.lean`, which is exactly this
headline formula, and it is proven in the OAI tree [S5:59–65]. The
proof reduces to an upper bound (dimension at most the entropy-over-
Lyapunov ratio) and a matching lower bound, then applies antisymmetry
through the coding exponent [S5:62–65].

**The corollaries.** The scope note also records two consequences valid
without exact overlaps: the usual entropy-over-Lyapunov formula for a
common positive contraction ratio, and the attractor formula
$\dim_{\mathrm H}K=\min\{1,s\}$, where $s\ge0$ is the unique
solution of
$\sum_i|r_i|^s=1$; absolute continuity is outside these statements
[S4:11]. The second comparator `SelfSimilarCorollaries.lean` carries
those two corollary theorems.

## History of the conjecture

The entropy-rate dimension formula is the one-dimensional case of the
dimension problem for self-similar measures. For decades the formula was
known under a separation (open-set) condition, where overlaps are absent
and the entropy-over-Lyapunov ratio is a clean bound. The open regime —
exact overlaps and unequal, even signed, ratios — is where the
resisted proof: overlaps let the measure concentrate in ways a naive
entropy count misses. This manuscript asserts the formula with no
separation assumption at all [S3:46–50, S4:9].

**Prior (my training data, not this repo).** I know the entropy-over-
Lyapunov dimension bounds for self-similar measures, the open-set
condition regime, and that exact overlaps are the hard case in the
dimension theory of self-similar measures. A proof of the *full* formula
$\dim_{\mathrm H}\mu=\min\{1,h_{\mathrm{RW}}/\chi\}$ for
arbitrary signed, unequal ratios with exact overlaps allowed is, to my
knowledge, beyond the standard results I was trained on. I cannot
independently verify this manuscript's argument.

## Consequences

**The entropy-rate dimension formula (general).**
$\dim_{\mathrm H}\mu=\min\{1,h_{\mathrm{RW}}/\chi\}$ for every
finite real self-similar measure of positive weights and
$|r_i|<1$, with exact overlaps and unequal/signed ratios allowed
[S3:46–50, S4:9].

**The homogeneous corollary.** Under a common positive contraction ratio
and no exact overlaps, the usual entropy-over-Lyapunov formula holds
[S4:11].

**The attractor formula.** The self-similar set $K$ has
$\dim_{\mathrm H}K=\min\{1,s\}$, $s\ge0$ the unique solution of
$\sum_i|r_i|^s=1$ [S4:11].

## Section skeleton

One manuscript [S3:46–50] (title [S3:39], date [S3:41]) — `main.tex`
under `build/` (a 61-line wrapper) plus `sections/`; 1,576 LaTeX lines
total; one `references.bib`. No manuscript ships a `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves
$\dim_H\mu=\min\{1,h_{\mathrm{RW}}/\chi\}$ for the lower
Hausdorff dimension of every finite real self-similar probability
measure with positive weights and nonzero contraction ratios of absolute
value below one. The ratios may be signed and unequal, and exact
overlaps are allowed [S4:9]. It also records two consequences without
exact overlaps — the entropy-over-Lyapunov formula for a common
positive ratio, and the attractor formula
$\dim_H K=\min\{1,s\}$ — with absolute continuity outside the
statements [S4:11]. The scope note names two comparators [S4:15–18]:
the headline `SelfSimilar.lean` and the corollaries
`SelfSimilarCorollaries.lean`.

**The registration.** The `main_results` entry names
`OAI.EntropyRateDimension.entropy_rate_dimension` in
`OAI/MeasureTheory/SelfSimilar/Main.lean` [S5:59–65] —
precisely the headline formula — and the manuscript is in
`formalization.yaml`'s `sources:`. This is the family's headline claim,
so the formalization is registered, not a partial or absent record. The
theorem is proven by a direct Lean proof in the OAI tree


```lean
theorem entropy_rate_dimension {ι : Type uι} [Fintype ι] [Nonempty ι]
    (S : System ι) (μ : Measure ℝ) [IsProbabilityMeasure μ]
    (hμ : S.SelfSimilar μ) :
    lowerHausdorffDimension μ = ENNReal.ofReal (min 1 (S.entropyRate / S.lyapunov)) := by
  rw [S.selfSimilar_dimension μ hμ]
  congr 1
  exact le_antisymm (le_min (S.exponent_le_one μ hμ) (S.exponent_le_rate μ hμ)) (S.exponent_lower_bound μ hμ)
```
[S5:59–65]

The proof rewrites the dimension as the coding exponent, then closes it
with
`le_antisymm (le_min (exponent_le_one) (exponent_le_rate))
(exponent_lower_bound)` — an upper and a lower bound meeting at the
same value [S5:63–65]. The 64-file `OAI/MeasureTheory/SelfSimilar`
package carries the coding and entropy-rate machinery; it is 64 files
over 12,093 lines with zero `sorry`. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library has
not been built here.

## Coverage

T3: the family is formally registered. The ledger row `fam=148` records
`paps 1`, `paps_form 1`, `tier T3`, `chal 2`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution|uniform`,
`resolves_named 1`, `summary 1`. The family ships one 1,576-line LaTeX
manuscript, a scope note naming two comparators, and the registered
`main_results` declaration `OAI.EntropyRateDimension.entropy_rate_dimension`
— the headline dimension formula — proven in the 64-file
`SelfSimilar` OAI tree. The manuscript is in `formalization.yaml`'s
`sources:`. The family ships no verification bundle and no reasoning
trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 148 at [S1:3550] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{148} at [S2:377] |
| S3 | [`preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/main.tex`](../../../preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/main.tex) | 61 | the single manuscript root; title [S3:39], date [S3:41], abstract [S3:46–50] |
| S4 | [`lean/docs/148.md`](../../../lean/docs/148.md) | 18 | the formalization scope note: the scope paragraph [S4:9], the consequences paragraph [S4:11], and the two-row comparator table [S4:15–18] |
| S5 | [`lean/OAI/MeasureTheory/SelfSimilar/Main.lean`](../../../lean/OAI/MeasureTheory/SelfSimilar/Main.lean) | 69 | the OAI proven `entropy_rate_dimension` theorem [S5:59–65] |
| S6 | [`preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/references.bib`](../../../preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/references.bib) | 321 | the manuscript's BibTeX bibliography |

## Bibliography

- Baker, Simon, Iterated function systems with super-exponentially close cylinders (2021)
- Breuillard, Emmanuel, Varjú, Péter P., On the dimension of Bernoulli convolutions (2019)
- Bárány, Balázs, Verma, Manuj, Hausdorff dimension of self-similar measures and sets with common fixed point structure (2026)
- Erdős, Paul, On a family of symmetric Bernoulli convolutions (1939)
- Feng, De-Jun, Hu, Huyi, Dimension theory of iterated function systems (2009)
- Feng, De-Jun, Feng, Zhou, Dimension of homogeneous iterated function systems with algebraic translations (2025)
- Galicer, Daniel, Saglietti, Santiago, Shmerkin, Pablo, Yavicoli, Alexia, $L^q$ dimensions and projections of random measures (2016)
- Garsia, Adriano M., Entropy and singularity of infinite convolutions (1963)
- Hochman, Michael, On self-similar sets with overlaps and inverse theorems for entropy (2014)
- Hutchinson, John E., Fractals and self-similarity (1981)
- Käenmäki, Antti, Orponen, Tuomas, Absolute continuity in families of parametrised non-homogeneous self-similar measures (2023)
- Moran, P. A. P., Additive functions of intervals and Hausdorff measure (1946)
- Bárány, Balázs, Käenmäki, Antti, Super-exponential condensation without exact overlaps (2021)
- Peres, Yuval, Solomyak, Boris, Absolute continuity of Bernoulli convolutions, a simple proof (1996)
- Rapaport, Ariel, Proof of the exact overlaps conjecture for systems with algebraic contractions (2022)
- Rapaport, Ariel, Varjú, Péter P., Self-similar measures associated to a homogeneous system of three maps (2024)
- Saglietti, Santiago, Shmerkin, Pablo, Solomyak, Boris, Absolute continuity of non-homogeneous self-similar measures (2018)
- Simon, Károly, Overlapping cylinders: the size of a dynamically defined Cantor-set (1996)
- Solomyak, Boris, On the random series $\sum\pm\lambda^n$ (an Erdős problem) (1995)
- Varjú, Péter P., Absolute continuity of Bernoulli convolutions for algebraic parameters (2019)
- Varjú, Péter P., Entropy rates in the dimension theory of self-similar measures (2026)
- Wang, Zhiren, Quantitative density under higher rank abelian algebraic toral actions (2011)
- Varjú, Péter P., On the dimension of Bernoulli convolutions for all transcendental parameters (2019)
