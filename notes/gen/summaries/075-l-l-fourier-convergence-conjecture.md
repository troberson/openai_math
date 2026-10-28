[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 075](../index/real-and-complex-analysis/075-l-l-fourier-convergence-conjecture.md)

# 075 — The $L\log L$ Fourier-convergence conjecture

[Index page](../index/real-and-complex-analysis/075-l-l-fourier-convergence-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1872] and the catalog abstract [S2:224] state
the family's claim: the ordinary symmetric Fourier partial sums of every
complex-valued $L\log L$ function on the circle converge almost everywhere
along the full sequence, resolving the classical sufficiency conjecture at
the $L\log L$ scale. The manuscript's abstract 

> We prove that the ordinary symmetric Fourier partial sums of every complex-valued function in $L\log L$ on the circle converge almost everywhere to the function along the full sequence. This establishes the classical $L\log L$ sufficiency conjecture. [S3:28–30]

## Undergraduate summary

The Fourier series of a function is the sum of sines and cosines that build
it. A long-standing question in analysis asks how large a function on a
circle can be and still have its Fourier series converge to the function at
almost every point. In 1966 Carleson proved this for square-integrable
functions, and Hunt extended it to every $L^p$ with $p>1$. In 1923
Kolmogorov showed that for merely integrable functions the Fourier series can
diverge almost everywhere, so some extra integrability is genuinely needed.

The natural boundary between what provably converges and what can diverge is
the class $L\log L$: functions whose size is integrable with one extra
logarithmic weight. For over fifty years it was an open conjecture that
$L\log L$ was enough. This paper proves it: every complex-valued $L\log L$
function has Fourier partial sums that converge to the function at almost
every point, along the full sequence of partial sums rather than along a
subsequence [S4:19–25].

The proof is a large combinatorial-entropic construction: it builds a tree
of tiny averaging operations, controls many modulation frequencies with a
single "good set" estimate, and then converts that estimate into the Fourier
series through the Hilbert transform [S4:63–75].

## Graduate summary

**The theorem** [S4:17–26, `thm:main`]. Let $\mathbb T = \mathbb
R/(2\pi\mathbb Z)$ carry normalized Lebesgue measure and write
$S_N f = \sum_{k=-N}^{N}\widehat f(k)e^{ikx}$ for the symmetric partial
sum. For every complex-valued $f \in L\log L(\mathbb T)$ — the Orlicz class
$\{\,f:\int|f|\log(2+|f|)<\infty\,\}$ — there is a measurable null set $N_f$
such that $S_N f(x)\to f(x)$ for $x\notin N_f$, along the full sequence
$N=0,1,2,\ldots$:

> **theorem**
For every complex-valued $f\in L\log L(\mathbb T)$, there is a measurable
set $N_f$ of measure zero such that
$$\lim_{N\to\infty}S_Nf(x)=f(x)
 \qquad (x\in\mathbb T\setminus N_f).$$
The limit is along the full sequence $N=0,1,2,\ldots$. [S4:17–26]

**The good-set integral estimate.** The analytic core is one estimate for a
nonnegative input $\rho$ of mass one and height at most $e^d$, where
$h=\log\log d$ 

> Set $h=\log\log d$ and remove the points where $M\rho>e^{4h}$. The removed set has measure at most
$Ce^{-4h}$, while on its complement we prove
$$\int_{\{M\rho\le e^{4h}\}}\sup_{N\ge0}|S_N\rho|\,d\mu
 \le Cd.$$ [S4:70–75]

The removed set $\{M\rho>e^{4h}\}$ has measure at most $Ce^{-4h}$, and on its
complement $G_\rho=\{M\rho\le e^{4h}\}$ the supremum of the partial sums has
integral at most $Cd$. Stated precisely in unit-period coordinates this is
the truncated integral estimate [S6:33–40, `thm:good-set`]:

> **theorem**
There are absolute constants $C$ and $d_*$ such that, whenever $d\ge d_*$
and $\rho$ is a nonnegative periodic function with
$\int_0^1\rho=1$ and $\rho\le e^d$ almost everywhere,
$$\int_{G_\rho}\sup_{N\ge0}|S_N\rho(x)|\,dx\le Cd.$$ [S6:33–40]

The integral bound is summable against the masses of the height layers of an
$L\log L$ function, and the exceptional sets are summable when the layer
heights are doubly exponential. The layer cost that closes the summation is


> We claim
$$\sum_j m_jd_j<\infty.$$ [S6:297–300]

**The finite dyadic estimate and its Fourier transfer.** To prove the
estimate, the proof uses a finite binary tree of dyadic intervals. At each
interval it takes half the difference of the averages of a modulated input
on its two children — a delayed Haar kernel — and bounds the integral of the
supremum over all integer modulations by $Cd$, uniformly in the tree depth.
Translation and scale averaging of these kernels, in the dyadic
representation method of Petermichl and Hytönen, produce a nonzero multiple of
the Hilbert kernel; the periodic Hilbert transform then gives the symmetric
Fourier projections through the multiplier identity $S_N\rho =
\chi_{-N}\Pi_{\ge0}(\rho\chi_N)-\chi_{N+1}\Pi_{\ge0}(\rho\chi_{-(N+1)})$
[S6:1–120].

**The entropic core.** The combinatorial proof must control many modulation
frequencies without a loss that grows with their number. It uses three
constructions [S4:96–165]: an entropy-compression lemma producing one common
phase region for a large set of frequencies; a Griffiths–Ginibre
positive-correlation argument bounding the cost of a new noisy observation;
and a separation of information cost from frequency-choice cost on "live
plateaus," where the expected cost per plateau is $O(d/h)$ against total
starting weight $O(h)$, giving the $O(d)$ budget.

**The maximal consequence.** Stein's Banach-space theorem applied to the
sequence $S_0,-S_0,S_1,-S_1,\ldots$ yields the Luxemburg-norm weak-$L^1$
maximal bound [S6:357–371, `cor:fourier-weak-l1`]: with the Orlicz norm
$\|f\|_\Phi$ for $\Phi(t)=t\log(2+t)$,
$\sup_{\lambda>0}\lambda\,\mu\{S^*f>\lambda\}\le C\|f\|_\Phi$.

**Conventions.** The proof works in unit-period coordinates $y=x/(2\pi)$
with characters $\chi_u(y)=e^{2\pi iuy}$ for integer $u$; Shannon entropy,
relative entropy, and Pinsker's inequality are the measure-theoretic tools
[S5:1–73].

## History of the conjecture

The endpoint question sits between three classical benchmarks. Carleson
(1966) proved almost-everywhere convergence in $L^2$ [S4:28–33]; Hunt (1968)
extended it to every $L^p$ for $p>1$ [S4:33–35]; and Kolmogorov (1923) built
an integrable function whose Fourier series diverges almost everywhere
[S4:35–37]. Between these, Sjölin (1969) obtained convergence in
$L\log L\log\log L$ [S4:37–40]; Soria (1985, 1989) developed larger
convergence spaces by extrapolation [S4:40–42]; Antonov (1996) proved
convergence in $L\log L\log\log\log L$ [S4:42–44]; and Arias de Reyna (2002)
introduced the quasi-Banach space QA, which strictly contains both Antonov's
class and Soria's space [S4:44–47].

On the maximal-function side, Lie (2013) gave a time-frequency proof of the
full-sequence maximal bound from QA to weak-$L^1$ [S4:46–50]; Di Plinio and
Fragkos (2025) proved weak-$L^p$ bounds of order $(p-1)^{-1}$ as
$p\downarrow1$, with sparse and weighted endpoint estimates [S4:50–54]; and
Lie (2017) formulated the $L\log L$ conjecture through a weak-$L^1$ maximal
estimate [S4:54–56]. Good-set integral estimates of the type used here also
occur in Lie's near-endpoint argument [S4:69–71].

**Prior (my training data, not this repo).** The $L\log L$ Fourier-convergence
problem is a genuine, long-standing open problem in harmonic analysis — the
natural endpoint between Hunt's $L^p$ ($p>1$) theorem and Kolmogorov's $L^1$
counterexample. I know the classical history (Carleson–Hunt, Sjölin, Soria,
Antonov) and Lie's QA time-frequency work, all consistent with the
manuscript's account. A proof of full-sequence $L\log L$ convergence is, to
my knowledge, not established in the literature I was trained on, and I
cannot independently verify this 2026 manuscript's argument.

## Consequences

**Full-sequence $L\log L$ convergence.** Every complex-valued $L\log L$
function on the circle has symmetric Fourier partial sums converging almost
everywhere along the full sequence, resolving the classical sufficiency
conjecture [S4:17–26].

**A weak-$L^1$ maximal bound.** The convergence theorem implies the
Luxemburg-norm weak-$L^1$ maximal estimate
$\sup_{\lambda>0}\lambda\,\mu\{S^*f>\lambda\}\le C\|f\|_\Phi$ via Stein's
Banach-space theorem [S6:357–371].

**Bounded functions, by approximation.** Every bounded complex-valued
periodic function has full-sequence almost-everywhere convergence, proved by
Fejér approximation reducing to the good-set estimate [S6:130–200].

**The layer summation.** The $L\log L$ function is split into
doubly-exponential height layers; the layer cost $\sum_j m_j d_j<\infty$ and
Borel–Cantelli on the exceptional sets make the tail summable at almost every
point [S6:297–330].

## Section skeleton

**Manuscript** [S3:28–30], 10 numbered sections under `build/sections/` (the
numbering jumps 09 → 11; there is no section 10): introduction [S4],
preliminaries, entropy-foundations, entropy-refinement, thermal, procedure,
capture, paths, assembly, fourier [S6]. Its root is `build/main.tex` [S3:23],
with a title [S3:23] and date [S3:25], a 23-entry BibTeX bibliography
`references.bib` [S11], and two figures (`figures/entropy-skip.tex`,
`figures/snapshot-timing.tex`).

The manuscript ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S7]. The formalization proves, for every measurable
complex-valued function on $\mathbb T$ with
$\int_{\mathbb T}|f|\log(2+|f|)<\infty$, that
$\sum_{k=-N}^{N}\widehat f(k)e^{ikx}\to f(x)$ outside one measurable null
set, along the full sequence $N\to\infty$. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero `sorry`
in the Lean source is not a comparator pass, and the library has not been
built here.

**The comparator stub** states the target with a `sorry`:

```lean
/-- Almost-everywhere convergence of all symmetric Fourier partial sums in L log L. -/
theorem paperMain (f : AddCircle (2 * Real.pi) → ℂ)
    (hfm : AEStronglyMeasurable f AddCircle.haarAddCircle)
    (hfi : Integrable (fun x ↦ ‖f x‖ * Real.log (2 + ‖f x‖))
      AddCircle.haarAddCircle) :
    ∃ E : Set (AddCircle (2 * Real.pi)),
      MeasurableSet E ∧ AddCircle.haarAddCircle E = 0 ∧ ∀ x ∉ E,
        Tendsto
          (fun N : ℕ ↦
            ∑ k ∈ Finset.Icc (-(N : ℤ)) (N : ℤ), fourierCoeff f k * fourier k x)
          atTop (𝓝 (f x)) := by
  sorry
```
[S8:11–22]

**The proved entry point.** `PaperMain.lean` names the release's declaration
`OAI.FourierLLogL.paperMain` and closes it as a thin `simpa` over
`almost_everywhere_fourier_convergence` 

```lean
theorem paperMain (f : AddCircle (2 * Real.pi) → ℂ)
    (hfm : AEStronglyMeasurable f AddCircle.haarAddCircle)
    (hfi : Integrable (fun x ↦ ‖f x‖ * Real.log (2 + ‖f x‖))
      AddCircle.haarAddCircle) :
    ∃ E : Set (AddCircle (2 * Real.pi)),
      MeasurableSet E ∧ AddCircle.haarAddCircle E = 0 ∧ ∀ x ∉ E,
        Tendsto
          (fun N : ℕ ↦
            ∑ k ∈ Finset.Icc (-(N : ℤ)) (N : ℤ), fourierCoeff f k * fourier k x)
          atTop (𝓝 (f x)) := by
  simpa only [circleMeasure, symmetricPartialSum] using
    (almost_everywhere_fourier_convergence f ⟨hfm, hfi⟩)
```
[S9:8–19]

That theorem is proved from `main_of_grid`, which runs the dyadic grid bound
through the affine and good-set reduction 

```lean
theorem main_of_grid (h : Dyadic.GridBound) {f : Torus → ℂ} (hf : MemLLogL f) :
    ∃ E : Set Torus, MeasurableSet E ∧ circleMeasure E = 0 ∧ ∀ x ∉ E,
      Tendsto (fun N : ℕ ↦ symmetricPartialSum f N x) atTop (𝓝 (f x)) :=
  h.unitTreeBound.affine.realGoodBound.goodBound.main_bound_consequence hf
```
[S10:17–20]

The `main_results` entry links the config `ComparatorChallenges/FourierLLogL.json`
to `OAI.FourierLLogL.paperMain` in `OAI/Analysis/FourierLLogL/PaperMain.lean`.
The OAI `FourierLLogL` tree is 155 `.lean` files over 29,181 lines with zero
`sorry`; `main`, `maximal_good_sets`, and `weak_L1_maximal_bound` [S10:17–20] are
its three top-level conclusions.

## Coverage

T3: the family is formalized. The ledger row `fam=075` records `paps 1`,
`paps_form 1`, `tier T3`, `chal 1`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution|partial`,
`resolves_named 1`, `summary 1`. The family ships one LaTeX manuscript (a
root `build/main.tex`, 10 `.tex` files under `build/sections/`, a 23-entry
`references.bib`, two figures) and a 155-file Lean formalization with a
scope note and one comparator challenge; it ships no verification bundle and
no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 075 at [S1:1872] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry for 075 at [S2:224] |
| S3 | [`preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/main.tex`](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/main.tex) | 44 | manuscript root; title at [S3:23], date [S3:25], abstract [S3:28–30] |
| S4 | [`preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/01-introduction.tex) | 197 | the main theorem [S4:17–26]; the good-set estimate [S4:70–75]; the literature history [S4:28–56]; the structural argument [S4:96–165] |
| S5 | [`preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/02-preliminaries.tex`](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/02-preliminaries.tex) | 73 | unit-period coordinates, characters, and the entropy notation [S5:1–73] |
| S6 | [`preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/11-fourier.tex`](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/11-fourier.tex) | 392 | the truncated integral estimate [S6:33–40]; the layer cost [S6:297–300]; the weak-$L^1$ corollary [S6:357–371] |
| S7 | [`lean/docs/075.md`](../../../lean/docs/075.md) | 16 | the formalization scope note: the proven statement and the \`Partial progress.\` / \`unchecked\` status |
| S8 | [`lean/ComparatorChallenges/FourierLLogL.lean`](../../../lean/ComparatorChallenges/FourierLLogL.lean) | 24 | the comparator stub: the target statement with a \`sorry\` [S8:11–22] |
| S9 | [`lean/OAI/Analysis/FourierLLogL/PaperMain.lean`](../../../lean/OAI/Analysis/FourierLLogL/PaperMain.lean) | 21 | the proved entry point: \`OAI.FourierLLogL.paperMain\` as a \`simpa\` over \`almost_everywhere_fourier_convergence\` [S9:8–19] |
| S10 | [`lean/OAI/Analysis/FourierLLogL/Main.lean`](../../../lean/OAI/Analysis/FourierLLogL/Main.lean) | 43 | the real statement: \`main_of_grid\`, \`maximal_good_sets\`, \`weak_L1_maximal_bound\` [S10:17–20] |
| S11 | [`preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/references.bib`](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/references.bib) | 278 | 23-entry BibTeX bibliography |

## Bibliography

- Antonov, N. Yu., Convergence of Fourier series (1996)
- Arias-de-Reyna, Juan, Pointwise convergence of Fourier series (2002)
- Carleson, Lennart, On convergence and growth of partial sums of Fourier series (1966)
- Carro, María J., Mastyło, Mieczysław, Rodríguez-Piazza, Luis, Almost everywhere convergent Fourier series (2012)
- Chang, Mei-Chu, A polynomial bound in Freiman's theorem (2002)
- Cover, Thomas M., Thomas, Joy A., Elements of Information Theory (2006)
- Fefferman, Charles, Pointwise convergence of Fourier series (1973)
- Fefferman, Charles L., Erratum: Pointwise convergence of Fourier series (1997)
- Ginibre, Jean, General formulation of Griffiths' inequalities (1970)
- Hunt, Richard A., On the convergence of Fourier series (1968)
- Kolmogoroff, Andrey, Une série de Fourier–Lebesgue divergente presque partout (1923)
- Lacey, Michael, Thiele, Christoph, A proof of boundedness of the Carleson operator (2000)
- Lee, James R., Covering the large spectrum and generalized Riesz products (2017)
- Lie, Victor, Pointwise convergence of Fourier series (I). On a conjecture of Konyagin (2017)
- Lie, Victor, On the boundedness of the Carleson operator near $L^1$ (2013)
- Sjölin, Per, An inequality of Paley and convergence a.e. of Walsh–Fourier series (1969)
- Hytönen, Tuomas, On Petermichl's dyadic shift and the Hilbert transform (2008)
- Petermichl, Stefanie, Dyadic shifts and a logarithmic estimate for Hankel operators with matrix symbol (2000)
- Di Plinio, Francesco, Fragkos, Anastasios, The weak-type Carleson theorem via wave packet estimates (2025)
- Soria, Fernando, Note on differentiation of integrals and the halo conjecture (1985)
- Soria, Fernando, On an extrapolation theorem of {Carleson–Sjölin} type with applications to a.e. convergence of Fourier series (1989)
- Stein, Elias M., On limits of sequences of operators (1961)
- Ville, Jean, Étude critique de la notion de collectif (1939)
