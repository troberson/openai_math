[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 082](../index/real-and-complex-analysis/082-maximal-and-variational-bounds-for-the-triangular-hilbert-transform.md)

# 082 — Maximal and variational bounds for the triangular Hilbert transform

[Index page](../index/real-and-complex-analysis/082-maximal-and-variational-bounds-for-the-triangular-hilbert-transform.md)

## Original CONTENTS.md summary

The release's blurb [S1:2029] and the catalog abstract [S2:238] state the
family's claim: maximal and annular $`r`$-variation bounds for the triangular
Hilbert transform, for every $`r>2`$, from complex $`L^3(\mathbb R^2)\times
L^3(\mathbb R^2)`$ to $`L^{3/2}(\mathbb R^2)`$, with the maximal estimate
controlling both hard truncation endpoints and yielding joint
almost-everywhere and norm convergence. The family ships three manuscripts
in a versioning chain; the current (highest) manuscript's abstract


> We prove a uniform $`L^3\times L^3\times L^3`$ estimate for the dyadic
triangular Hilbert form with unrestricted real inputs. The sum of the
absolute local contributions over any finite set of scales is bounded
by forty times the product of the input norms. In particular, the bound
allows coefficients of modulus at most one to vary independently among
admissible interval triples. [S6:8–14]

## Undergraduate summary

The bilinear Hilbert transform $`B(F,G)(x)`$ averages two functions against
a kernel supported on a triangle in the $`(\xi,\eta)`$ frequency plane. Its
triangular variant restricts the averaging to a one-sided (triangular)
region, which makes the kernel non-oscillatory and the analysis
substantially different from the classical bilinear case.

The "maximal" operator $`B_*(F,G)`$ takes the supremum of the bilinear
expression over all finite truncation intervals of the kernel. The
$`L^3\times L^3\to L^{3/2}`$ bound for $`B_*`$ is a strong endpoint estimate
at the symmetric point $`(3,3,3/2)`$: it controls the worst-case
truncation uniformly, not just the limit. The three manuscripts sharpen
and extend this estimate in sequence: first the pointwise maximal bound
[S3:7–14], then the full annular $`r`$-variation estimate for $`r>2`$
[S5:27–33], and finally a uniform $`L^3`$ bound for the dyadic
triangular form with unrestricted real inputs [S6:8–14].

## Graduate summary

**The versioning chain.** The three manuscripts are a nesting of
estimates for the same triangular Hilbert bilinear form.

The first (maximal) proves 

> **theorem**
There is an absolute constant $`C`$ such that, for every pair of complex
functions $`F,G\in L^3(\mathbb R^2)`$,
$$\|B_*(F,G)\|_{L^{3/2}(\mathbb R^2)}
 \le C\|F\|_{L^3(\mathbb R^2)}\|G\|_{L^3(\mathbb R^2)}.$$
The supremum is over both finite hard truncation endpoints. [S4:16–24]

The supremum is over both finite hard truncation endpoints, chosen
separately at each spatial point — stronger than a uniform bound for
each individual truncation [S4:26–32]. The joint principal value
$`B(F,G)=\lim_{\varepsilon\downarrow 0,\, R\uparrow\infty}
B_{\varepsilon,R}(F,G)`$ is obtained as a consequence.

The second (annular variation) proves the full $`r`$-variation estimate


> **Theorem 1.1**
For every real $`r>2`$ there is a finite constant $`C_r`$ such that
$$\|V_r(F,G)\|_{L^{3/2}(\mathbb R^2)}
 \le C_r\|F\|_{L^3(\mathbb R^2)}\|G\|_{L^3(\mathbb R^2)}$$
for all complex $`F,G\in L^3(\mathbb R^2)`$. [S5:27–33]

for every $`r>2`$, which subsumes the maximal estimate by taking a single
increment [S5:36–39]. The variation estimate gives almost everywhere
and $`L^{3/2}`$ norm convergence of the truncated integrals.

The third (dyadic $`L^3`$ bound) proves a uniform
$`L^3\times L^3\times L^3`$ estimate for the dyadic triangular form
with unrestricted real inputs, allowing coefficients of modulus at most
one to vary independently among admissible interval triples
[S6:8–14].

**The proof strategy.** The v1 proof proceeds through a matrix-analytic
decomposition of the triangular kernel, a trace estimate for the
resulting integral operators, a heat-kernel smoothing argument, and a
jumps argument to pass from smoothed to pointwise bounds
[S3:16–22]. The maximal step converts these to a single $`L^{3/2}`$
majorant controlling all truncation choices simultaneously.

## History of the conjecture

The bilinear Hilbert transform was conjectured by Fefferman and proved
by Coifman, Lacey, and Pisier in 1991. The triangular variant, where the
kernel is supported on a one-sided triangle, was studied by Lacey,
Pisier, and Tchamitchian; the endpoint $`(3,3,3/2)`$ estimate for the
maximal triangular form was a long-standing open question. The present
papers prove that estimate, and the v2 and v3 papers extend it to the
variation and dyadic settings.

The symmetric point $`(3,3,3/2)`$ is the endpoint of the known range:
interpolating from $`L^2\times L^2\to L^1`$ (trivial by
Cauchy–Schwarz) and $`L^\infty\times L^\infty\to L^\infty`$
(bounded operators) gives $`L^{p}\times L^{p}\to L^{p/2}`$ for $`p\in(2,\infty)`$,
and $`p=3`$ is the first integer at the endpoint where the maximal
estimate is nontrivial.

**Prior (my training data, not this repo).** The bilinear Hilbert
transform and its triangular variant are classical objects in
harmonic analysis; I know the Coifman–Lacey–Pisier theorem
and the Lacey–Pisier–Tchamitchian work on the triangular
case. A maximal $`L^3\times L^3\to L^{3/2}`$ estimate for the
triangular form is, to my knowledge, not established in the
literature I was trained on. I cannot independently verify these
2026 manuscripts' arguments.

## Consequences

**Pointwise maximal endpoint estimate.** For all complex
$`F,G\in L^3(\mathbb R^2)`$, $`\|B_*(F,G)\|_{L^{3/2}}\le
C\|F\|_3\|G\|_3`$ with both truncation endpoints under one
majorant [S4:16–24].

**Annular $`r`$-variation for $`r>2`$.** The full annular $`r`$-variation of
the triangular Hilbert transform is bounded in
$`L^3\times L^3\to L^{3/2}`$ for every $`r>2`$, yielding joint
almost-everywhere and norm convergence [S5:27–33].

**Dyadic $`L^3`$ bound.** A uniform $`L^3\times L^3\times L^3`$
estimate for the dyadic triangular form with unrestricted real inputs,
allowing sign-varying coefficients [S6:8–14].

**Almost-everywhere convergence.** The maximal estimate gives a
common full-measure set on which all truncated integrals are defined,
and the maximal output is almost everywhere measurable [S7].

## Section skeleton

Three manuscripts, a versioning chain:

- **v1** `The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026`
  — root `build/main.tex` [S3:7–14] (title [S3:2], date [S3:4]), seven
  `.tex` files under `build/sections/` (introduction [S4:16–24], matrix, trace,
  heat, jumps, maximal, consequences), two figures
  (`figures/masks.tex`, `figures/triangle.tex`), a shared `preamble.tex`,
  a 15-entry `references.bib` [S10].
- **v2** `Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026`
  — root `build/main.tex` (title, date, abstract), sections under
  `build/sections/` (introduction [S5:27–33], and further sections),
  `references.bib`.
- **v3** `An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026`
  — root `build/main.tex` [S6:8–14] (title [S6:3], date [S6:5]), five
  `.tex` files under `build/sections/` (introduction, matrix, trace,
  dyadic, summation), `references.bib`.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S7]. The formalization proves the symmetric maximal
estimate for the triangular Hilbert transform: for arbitrary complex
$`F,G\in L^3(\mathbb R^2)`$, the $`L^{3/2}`$ norm of the supremum over all
finite hard-truncation intervals is at most $`C\|F\|_3\|G\|_3`$ for one
absolute constant $`C`$. It also establishes a common full-measure set on
which the truncated integrals are defined and almost-everywhere
measurability of the maximal output. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library has
not been built here.

**The comparator stub** states the target:

```lean
def MainEstimate : Prop :=
  ∃ C : ℝ≥0, ∀ F G : Plane → ℂ,
    MemLp F 3 volume → MemLp G 3 volume →
    (∀ᵐ z ∂volume, GoodPoint F G z) ∧
    AEMeasurable (maximal F G) volume ∧
    maximalNorm F G ≤ (C : ℝ≥0∞) * eLpNorm F 3 volume * eLpNorm G 3 volume
```
[S8:40–45]

with the proof obligation `sorry` 

```lean
theorem main_estimate : MainEstimate := by
  sorry
```
[S8:50–51]

**The proved entry point.** The `main_results` entry names
`OAI.TriangularHilbert.main_estimate` in
`OAI/Analysis/TriangularHilbert/Main.lean`, proved at line 38


```lean
theorem main_estimate : MainEstimate := by
  refine ⟨mainConstant,fun F G hF hG => ⟨ae_goodPoint F G hF hG,aemeasurable_maximal F G hF hG,?_⟩⟩
  rw [maximalNorm_eq_cyclicNorm F G hF hG]
  simpa only [eLpNorm_cyclicB hF,eLpNorm_cyclicC hG] using
    cyclicNorm_le (cyclicB F) (cyclicC G) (memLp_cyclicB hF) (memLp_cyclicC hG)
```
[S9:38–42]

The proof reduces to a `cyclicNorm_le` estimate through a
reflection-based change of coordinates that converts the triangular
maximal operator to a cyclic (two-sided) form. The `main_results` entry
links the config `ComparatorChallenges/TriangularHilbert.json` to the
declaration `OAI.TriangularHilbert.main_estimate` in
`OAI/Analysis/TriangularHilbert/Main.lean`. The OAI `TriangularHilbert`
tree is 105 `.lean` files over 10,861 lines with zero `sorry`.

## Coverage

T3: the family is formalized. The ledger row `fam=082` records `paps 3`,
`paps_form 1`, `tier T3`, `chal 1`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution|bound|uniform`,
`summary 1`. The family ships three LaTeX manuscripts (v1 formalized,
v2 and v3 extending it), a scope note, one comparator challenge and one
`main_results` entry; it ships no verification bundle and no reasoning
trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 082 at [S1:2029] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry for 082 at [S2:238] |
| S3 | [`preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/main.tex`](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/main.tex) | 25 | v1 (maximal) manuscript root; title [S3:2], date [S3:4], abstract [S3:7–14] |
| S4 | [`preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/sections/introduction.tex) | 145 | v1 introduction; the main theorem [S4:16–24], the truncation strength and principal value [S4:26–32] |
| S5 | [`preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/sections/introduction.tex`](../../../preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/sections/introduction.tex) | 201 | v2 (annular variation) introduction; the full variation theorem [S5:27–33], the maximal consequence [S5:36–39] |
| S6 | [`preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/build/main.tex`](../../../preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/build/main.tex) | 23 | v3 (dyadic L3 bound) manuscript root; title [S6:3], date [S6:5], abstract [S6:8–14] |
| S7 | [`lean/docs/082.md`](../../../lean/docs/082.md) | 15 | the formalization scope note: the symmetric maximal estimate and the excluded variation corollary |
| S8 | [`lean/ComparatorChallenges/TriangularHilbert.lean`](../../../lean/ComparatorChallenges/TriangularHilbert.lean) | 57 | comparator stub: the `MainEstimate` [S8:40–45] and the target with a `sorry` [S8:50–51] |
| S9 | [`lean/OAI/Analysis/TriangularHilbert/Main.lean`](../../../lean/OAI/Analysis/TriangularHilbert/Main.lean) | 47 | the OAI proved entry point `main_estimate` [S9:38–42] |
| S10 | [`preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/references.bib`](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/references.bib) | 211 | 15-entry BibTeX bibliography |

## Bibliography

- Christ, Michael, Durcik, Polona, Roos, Joris, Trilinear smoothing inequalities and a variant of the triangular Hilbert transform (2021)
- Daletskii, Yu. L., Integration and differentiation of functions of Hermitian operators depending on a parameter (1957)
- Demeter, Ciprian, Thiele, Christoph, On the two-dimensional bilinear Hilbert transform (2010)
- Durcik, Polona, Kovač, Vjekoslav, Škreb, Kristina Ana, Thiele, Christoph, Norm-variation of ergodic averages with respect to two commuting transformations (2019)
- Durcik, Polona, Kovač, Vjekoslav, Thiele, Christoph, Power-type cancellation for the simplex Hilbert transform (2019)
- Durcik, Polona, Roos, Joris, Averages of simplex Hilbert transforms (2021)
- Durcik, Polona, An $`L^4`$ estimate for a singular entangled quadrilinear form (2015)
- Grafakos, Loukas, Oliveira e Silva, Diogo, Pramanik, Malabika, Seeger, Andreas, Stovall, Betsy, Some problems in harmonic analysis (2017)
- Hardy, G. H., Littlewood, J. E., A maximal theorem with function-theoretic applications (1930)
- Hsu, Martin, Lin, Fred Yu-Hsiang, Smoothing inequalities for corner-type bilinear averages: geometric characterization and applications (2026)
- Kovač, Vjekoslav, Thiele, Christoph, Zorin-Kranich, Pavel, Dyadic triangular Hilbert transform of two general functions and one not too general function (2015)
- Kovač, Vjekoslav, Bellman function technique for multilinear estimates and an application to generalized paraproducts (2011)
- Kovač, Vjekoslav, Boundedness of the twisted paraproduct (2012)
- Kwong, Man Kam, Inequalities for the powers of nonnegative Hermitian operators (1975)
- Lewis, Adrian S., The convex analysis of unitarily invariant matrix functions (1995)
- Lin, Fred Yu-Hsiang, Slavíková, Lenka, Rough averages of triangular Hilbert transforms (2026)
- Tao, Terence, Cancellation for the multilinear Hilbert transform (2016)
- Zorin-Kranich, Pavel, Cancellation for the simplex Hilbert transform (2017)
