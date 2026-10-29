[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 081](../index/real-and-complex-analysis/081-david-semmes-riesz-transform-problem-in-higher-codimension.md)

# 081 — The David–Semmes Riesz-transform problem in higher codimension

[Index page](../index/real-and-complex-analysis/081-david-semmes-riesz-transform-problem-in-higher-codimension.md)

## Original CONTENTS.md summary

The release's blurb [S1:2013] and the catalog abstract [S2:236] state the
family's claim: for $`d\ge4`$ and $`2\le n\le d-2`$, an $`n`$-Ahlfors–David
regular Radon measure on $`\mathbb R^d`$ is uniformly $`n`$-rectifiable
whenever its $`n`$-dimensional Riesz transform is uniformly $`L^2`$-bounded over
all positive hard truncations. This resolves the remaining higher-codimension
range of the David–Semmes Riesz-transform question. The manuscript's
abstract 

> We prove that an $`n`$-Ahlfors–David regular Radon measure on $`\mathbb R^d`$
is uniformly $`n`$-rectifiable if its $`n`$-dimensional Riesz transform is
uniformly bounded from scalar $`L^2(\mu)`$ to vector-valued $`L^2(\mu)`$
over all positive hard truncations, for integers $`d\ge4`$ and
$`2\le n\le d-2`$.
This gives a positive answer to the David–Semmes Riesz-transform question
in its remaining higher-codimension range. The conclusion gives uniform
big pieces of Lipschitz images of Euclidean balls. [S3:35–44]

## Undergraduate summary

A measure $`\mu`$ on $`\mathbb R^d`$ is $`n`$-rectifiable if, in a suitable
sense, it is concentrated on a countable union of $`n`$-dimensional planes.
"Uniformly rectifiable" strengthens this: the approximation by planes must
work at *every* scale and *every* point, with quantitative control.
David and Semmes introduced the uniform version in the early 1990s as the
right geometric hypothesis for singular integral operators to behave
well [S4:69–78].

The Riesz transform $`R_n`$ of a measure $`\mu`$ is a singular integral
operator that measures how much $`\mu`$ fails to look like a flat $`n`$-plane
at each scale. The classical result (codimension one, $`n=d-1`$) is that
$`b`$oundedness of $`R_n`$ on $`L^2(\mu)`$ forces rectifiability. David and Semmes
asked whether the same is true in higher codimension $`n\le d-2`$, and
whether it can be made quantitative — giving explicit Lipschitz constants
and mass fractions in terms of the operator bound. This paper answers that
question affirmatively for all $`d\ge4`$ and $`2\le n\le d-2`$ [S4:61–67].

## Graduate summary

**The theorem** [S4:61–67, `thm:main`]. Let $`d\ge4`$ and
$`2\le n\le d-2`$ be integers. Let $`\mu`$ be an $`n`$-Ahlfors–David regular
Radon measure on $`\mathbb R^d`$ satisfying the uniform $`L^2`$ Riesz-transform
bound 

> $$\|R_{\mu,\varepsilon}f\|_{L^2(\mu;\mathbb R^d)}
 \le C_{\rm R}\|f\|_{L^2(\mu)}.$$
No pointwise principal-value hypothesis is imposed. For a nontrivial
regular support, the integrals in are
absolutely convergent for every $`x`$ and every $`f\in L^2(\mu)`$;
this follows from Lemma below. [S4:39–46]

Then $`\mu`$ is uniformly $`n`$-rectifiable in the sense of Definition
[S4:48–59]: there exist constants $`\theta>0`$ and $`M\ge0`$, depending
only on $`d`$, $`n`$, the AD constant, and the Riesz bound, such that at every
support point and every admissible radius, a Lipschitz $`n`$-disk of
Lipschitz constant $`M`$ carries $`\theta`$-fraction of the ball's mass.

> **theorem**
Let $`d\ge4`$ and $`2\le n\le d-2`$ be integers. Let $`\mu`$ be an
$`n`$-Ahlfors–David regular Radon measure on $`\mathbb R^d`$ satisfying
 . Then $`\mu`$ is uniformly $`n`$-rectifiable in the
sense of Definition . Its constants $`\theta`$ and $`M`$ can
be chosen in terms of $`d,n,C_{\rm AD}`$ and $`C_{\rm R}`$ alone. [S4:61–67]

The proof proceeds through a long geometric-analytic chain: flat-ball
estimates, planar limit analysis, a compactness principle for the height
function, fractional rigidity of oscillatory integrals, excess propagation
across scales, and a packing endpoint argument [S3:46–54]. The
conclusion is quantitative — the constants $`\theta`$ and $`M`$ are
explicit functions of the input bounds — and works at unbounded support.

**What is excluded.** The variation estimate and the principal-value
corollary are not part of the formalized statement [S5].

## History of the conjecture

David and Semmes developed uniform rectifiability in the early 1990s as a
quantitative form of rectifiability tailored to singular integrals
[S4:69–78]. Among its equivalent descriptions are big pieces of
Lipschitz images and a packing condition on balls where the support fails
to approximate a plane from both sides. The codimension-one case
($`n=d-1`$) was settled by the work of David, Journé, and others; the
higher-codimension case with $`2\le n\le d-2`$ was the remaining gap.

In the codimension-one setting, boundedness of the Riesz transform on
$`L^2(\mu)`$ for an $`(d-1)`$-AD regular measure forces uniform
rectifiability. The higher-codimension problem is substantially harder
because the kernel $`R_n(x,y)=|x-y|^{-(n+1)}(x-y)`$ couples $`n+1`$
coordinates, and the geometric objects are $`n`$-disks in $`d`$-space rather
than hypersurfaces. The proof here introduces flat-ball estimates, a
compactness principle for the height function over $`n`$-planes, and a
fractional rigidity argument for oscillatory integrals to close the gap
[S3:46–54].

**Prior (my training data, not this repo).** The David–Semmes
program and the codimension-one Riesz-rectifiability theorem are classical
in geometric measure theory. The higher-codimension extension is a
genuine open problem that I am not aware of being resolved in the
literature I was trained on. I cannot independently verify this 2026
manuscript's argument.

## Consequences

**Quantitative uniform rectifiability in higher codimension.** For
$`d\ge4`$ and $`2\le n\le d-2`$, the uniform $`L^2`$ Riesz-transform bound
forces big pieces of Lipschitz $`n`$-images with explicit constants, at
every support point and admissible radius [S4:61–67].

**A positive answer to the David–Semmes question.** The Riesz
transform alone — without a variation estimate — suffices to force
uniform rectifiability in its remaining higher-codimension range
[S4:69–78].

**Class-uniform Lipschitz constants.** The Lipschitz constant $`M`$ and
mass fraction $`\theta`$ depend only on the ambient dimension, the
codimension, the AD constant, and the operator bound — not on the
particular measure [S4:61–67].

## Section skeleton

**Manuscript** [S3:35–44], ten numbered sections under `build/sections/`:
introduction [S4], background, flat-balls, planar-limits,
height-compactness, fractional-rigidity, excess-propagation,
packing-endpoint, consequences; one appendix (geometric-conventions).
Root is `build/paper.tex` [S3:30], with a title [S3:30], date [S3:32],
and an 18-entry BibTeX bibliography `references.bib` [S8].

The manuscript ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5]. The formalization proves that bounded Riesz
transforms force quantitative uniform rectifiability in higher codimension:
for $`d\ge4`$ and $`2\le n\le d-2`$, an $`n`$-AD regular measure whose positive
hard truncations have one uniform $`L^2`$ operator bound has big pieces of
Lipschitz images, with the mass fraction and Lipschitz constant depending
only on the dimensions and the stated bounds, at every support point and
admissible radius including unbounded support. The variation and
principal-value corollary is not included. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library has
not been built here.

**The comparator stub** states the quantitative target:

```lean
def QuantitativeFullStatement : Prop :=
  ∀ d n : ℕ, 4 ≤ d → 2 ≤ n → n + 2 ≤ d →
    ∀ C_AD : ℝ, 1 ≤ C_AD → ∀ C_R : ℝ≥0,
      ∃ θ : ℝ, 0 < θ ∧ ∃ M : ℝ≥0,
        ∀ μ : Measure (Ambient d), μ.Regular →
          ADRegularWithConstant n C_AD μ →
          RieszL2BoundedWithConstant n C_R μ →
          BallImageConclusion n μ θ M
```
[S6:42–49]

with the proof obligation `sorry` 

```lean
/-- Class-uniform Lipschitz ball images from fixed AD and hard-truncation L² bounds. -/
theorem quantitative_higher_codimension_riesz_rectifiability : QuantitativeFullStatement := by
  sorry
```
[S6:56–58]

**The proved entry point.** The `main_results` entry names
`OAI.RieszRectifiability.quantitative_higher_codimension_riesz_rectifiability`
in `OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean`,
proved at line 89 

```lean
theorem quantitative_higher_codimension_riesz_rectifiability : QuantitativeFullStatement := by
  intro d n _hd hn hnd C hC D
  cases n with
  | zero => omega
  | succ p =>
    have hnd' : p + 1 ≤ d := by omega
    let G : ℝ := 9 ^ d * C
```
[S7:89–95]

The `main_results` entry links the config
`ComparatorChallenges/RieszQuantitative.json` to the declaration
`OAI.RieszRectifiability.quantitative_higher_codimension_riesz_rectifiability`
in `OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean`. The
OAI `RieszRectifiability` tree is 824 `.lean` files over 65,638 lines with
zero `sorry`.

## Coverage

T3: the family is formalized. The ledger row `fam=081` records `paps 1`,
`paps_form 1`, `tier T3`, `chal 1`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution|bound|uniform`,
`resolves_named 1`, `summary 1`. The family ships one LaTeX manuscript
(root `build/paper.tex`, 10 `.tex` files under `build/sections/`, an
18-entry `references.bib`) and an 824-file Lean formalization with a
scope note and one comparator challenge; it ships no verification bundle
and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 081 at [S1:2013] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry for 081 at [S2:236] |
| S3 | [`preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/paper.tex`](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/paper.tex) | 59 | manuscript root; title [S3:30], date [S3:32], abstract [S3:35–44] |
| S4 | [`preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/sections/00-introduction.tex) | 198 | introduction; the Riesz-bound condition [S4:39–46], uniform rectifiability definition [S4:48–59], the main theorem [S4:61–67], the David–Semmes context [S4:69–78] |
| S5 | [`lean/docs/081.md`](../../../lean/docs/081.md) | 15 | the formalization scope note: the quantitative rectifiability statement and the excluded variation corollary |
| S6 | [`lean/ComparatorChallenges/RieszQuantitative.lean`](../../../lean/ComparatorChallenges/RieszQuantitative.lean) | 62 | comparator stub: the `QuantitativeFullStatement` [S6:42–49] and the target with a `sorry` [S6:56–58] |
| S7 | [`lean/OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean`](../../../lean/OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean) | 125 | the OAI proved entry point `quantitative_higher_codimension_riesz_rectifiability` [S7:89–95] |
| S8 | [`preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/references.bib`](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/references.bib) | 186 | 18-entry BibTeX bibliography |

## Bibliography

- Azzam, Jonas, Mourgoglou, Mihalis, Villa, Michele, Quantitative differentiability on uniformly rectifiable sets (2025)
- Bate, David, Hyde, Matthew, Schul, Raanan, Uniformly rectifiable metric spaces: Lipschitz images, Bi-Lateral Weak Geometric Lemma and corona decompositions (2023)
- David, Guy, Semmes, Stephen, Singular integrals and rectifiable sets in $`\mathbb{R}^n`$. {Au-del\`a} des graphes lipschitziens (1991)
- David, Guy, Semmes, Stephen, Analysis of and on Uniformly Rectifiable Sets (1993)
- Dipierro, Serena, Savin, Ovidiu, Valdinoci, Enrico, Definition of fractional Laplacian for functions with polynomial growth (2019)
- Farag, Hany M., Curvatures of the Melnikov type, Hausdorff dimension, rectifiability, and singular integrals on $`\mathbb{R}^n`$ (2000)
- Fefferman, Charles, Stein, Elias M., $`H^p`$ spaces of several variables (1972)
- Jaye, Benjamin, Nazarov, Fedor, Reflectionless measures for {Calderón–Zygmund} operators I: general theory (2018)
- Jaye, Benjamin, Nazarov, Fedor, Reflectionless measures for {Calderón–Zygmund} operators (2013)
- Mas, Albert, Tolsa, Xavier, Variation for the Riesz transform and uniform rectifiability (2014)
- Mattila, Pertti, Melnikov, Mark S., Verdera, Joan, The Cauchy integral, analytic capacity, and uniform rectifiability (1996)
- Mattila, Pertti, Geometry of Sets and Measures in Euclidean Spaces: Fractals and Rectifiability (1995)
- Nazarov, Fedor, Tolsa, Xavier, Volberg, Alexander, On the uniform rectifiability of AD-regular measures with bounded Riesz transform operator: the case of codimension 1 (2014)
- Hörmander, Lars, The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis (2003)
- Tolsa, Xavier, Riesz transforms and the BAUPP and BWGL criteria for uniform rectifiability (2025)
- Tolsa, Xavier, Interactions between quantitative rectifiability, singular integrals, and boundary value problems for harmonic functions (2026)
- Tolsa, Xavier, Principal values for Riesz transforms and rectifiability (2008)
- Tolsa, Xavier, Uniform measures and uniform rectifiability (2015)
