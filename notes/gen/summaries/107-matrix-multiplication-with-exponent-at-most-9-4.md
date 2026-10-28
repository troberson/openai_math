[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 107](../index/theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md)

# 107 — Matrix multiplication with exponent at most $9/4$

[Index page](../index/theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md)

## Original CONTENTS.md summary

[S1:2645] (family entry):

> **107. Matrix multiplication with exponent at most 9/4.** Proves $`\omega\le9/4`$ over ℂ, giving $`O_\varepsilon(n^{9/4+\varepsilon})`$ arithmetic operations for square matrix multiplication. In characteristic zero, some inner dimension na with a > 0.465 permits $`n^{2+o(1)}`$ rectangular multiplication. Further square bounds give ω < 2.258 outside finitely many positive characteristics and ω < 2.371054886006746 over every fixed field. (Lean)

The three manuscripts under that family:

[S1:2652] (manuscript 1, abstract at [S1:2654]):

> We prove that the exponent of matrix multiplication over the complex numbers is at most 9/4.

[S1:2661] (manuscript 2, labeled *secondary writeup* by the release; abstract at [S1:2663]):

> Over every field of characteristic zero, we prove that the square matrix-multiplication exponent satisfies ω < 2.258, the dual exponent satisfies α > 0.465, and $`\omega(1,0.709,1)\lt 2.092`$. The strict square and k = 0.709 rectangular bounds also hold over every field except possibly in one finite set of positive characteristics, in the arithmetic-operation model.

[S1:2670] (manuscript 3, abstract at [S1:2672]):

> We prove that the arithmetic exponent of square matrix multiplication over every fixed field satisfies ω < 2.371054886006746. This includes every positive characteristic.

[S2:292] carries the `\resultentry`, so the release blurb and the overview
agree. The family title names the headline bound 9/4; the three manuscripts
prove, in order, 9/4 over ℂ, 2.258 (plus dual and rectangular bounds) in
characteristic zero, and 2.371054886006746 over every fixed field.

## Undergraduate summary

The **exponent of matrix multiplication** ω is the infimum of the real
numbers τ such that, for every ε>0, two $n\times n$ matrices can be
multiplied in $O_\varepsilon(n^{\tau+\varepsilon})$ scalar arithmetic operations —
"the algorithm and its constants may depend on $\varepsilon$" [S3:42–43]. The
classical algorithm gives ω=3; Strassen's seven-product recursion first
beat 3 [S3:51–53]. The family's headline: the exponent over ℂ is at most
**9/4**, so every ε>0 has a complex matrix-multiplication algorithm with
$O_\varepsilon(n^{9/4+\varepsilon})$ arithmetic operations [S3:45–49].

Two derived exponents ride along. The **dual exponent** α is the supremum of
rectangular aspect ratios attainable with exponent 2 [S11:10]; the manuscript
proves α>0.465 [S5:73–77]. The **rectangular exponent** ω(1, k, 1) prices
multiplying an $n\times n^k$ matrix by an $n^k\times n$ matrix: the
manuscript gives ω(1, 0.709, 1)<2.092 [S5:73–77].

The count is **arithmetic** — additions, subtractions, and multiplications in
finite division-free programs, with arbitrary positive exponent slack
[S11:10] — not bit complexity. The third manuscript is honest about the scope:
"the theorem concerns asymptotic arithmetic cost; the counting arguments and
parameter choices do not give bit-complexity or practical crossover
estimates" [S7:65–69].

## Graduate summary

**Manuscript 1** (root [S3], `thm:main` at [S3:45–49]): over ℂ,
"For every $\varepsilon>0$, two $n\times n$ complex matrices can be multiplied using
$O_\varepsilon(n^{9/4+\varepsilon})$ arithmetic operations. In particular,
$\omega\leq9/4$" [S3:46–49]. The paper is a single LaTeX file [S3] with six
sections: tensors and their characters, separating a shared tensor leg, two
polynomial-multiplication inequalities, discrete growth and the arithmetic
exponent, and existence of detecting characters (headings at [S3:37],
[S3:142], [S3:270], [S3:392], [S3:605], [S3:700]).

**Manuscript 2** (root [S4], `thm:main`/`thm:square`/`thm:rectangular` at
[S5:72–78]): over ℂ, ω < 1129/500 = 2.258, α > 0.465, and w(0.709) < 2.092
[S5:73–77]. A characteristic-transfer corollary moves the strict square and
k=0.709 inequalities to every field of characteristic zero, or outside one
finite set of positive characteristics, in the same arithmetic model; the
transfer selects two fixed exact rank schemes, realizes their coefficients
over one number field, and specializes their polynomial identities, and "the
exceptional primes are not computed" [S5:80–85]. The certificate machinery
(`thm:certificate` [S4:78], the six-state lower tests `thm:ap` [S4:76], the
asymptotic sum inequality and elementary completion bound in the algebra
section [S4:74]) drives the numerical bounds.

**Manuscript 3** (root [S6], `thm:main` at [S7:57–63]): over every fixed
field $\mathbb F$, $\omega_\mathbb F<2.371054886006746<2.371054887$ [S7:58–62], with
"exact arithmetic algorithms, including in positive characteristic" and
finite choices independent of the input matrices [S7:65–66]. The staggered
joint-extraction theorem (`thm:joint-step` [S6:49]) supplies the
heterogeneous extraction step the family name refers to.

The three results sit on one method line: bilinear algorithms as trilinear
tensors, recursion and tensor product as reductions, approximate algorithms
converted to exact asymptotic ones by Bini's interpolation, and the
Schönhage asymptotic sum inequality plus Strassen's laser method turning
simultaneous products into exponent bounds [S3:51–57]; the formalized
rectangular theorem's citation `CW75ReorderedRectangular` marks the
Coppersmith–Wagner 1975 reordering as the base the 2.092 bound reorders
[S14:25–27].

## History of the conjecture

The manuscript 1 introduction carries the classical line: Strassen's
seven-product algorithm showed recursion beats exponent 3; Bini's
interpolation converts approximate bilinear algorithms into exact asymptotic
algorithms; Schönhage's asymptotic sum inequality turns efficient
simultaneous computations into exponent bounds; Strassen's laser method is
named next [S3:51–57]. The formalized rectangular bound is built on the
reordered Coppersmith–Wagner scheme [S14:25–27], and the square
$2.371054886006746$ constant is the numerical target the staggered
extraction attains over every field [S7:58–62].

**Prior (my training data, not this repo).** The exponent record moved
Strassen (2.807) → Coppersmith–Wagner (2.376) → the family's
ω<2.371054886006746, which breaks the CW barrier; an ω≤9/4 square bound
over ℂ is far from the record, so manuscript 1 reads as a *method paper*
(detecting characters, separations) and the 2.258/2.3710 papers as the
record-line papers. The dual exponent α>0.465 exceeds the CW-era
α≈0.288–0.336 range I recall. I cannot confirm these numbers independently;
the release ships the three manuscripts as proofs, and the Lean layer
formalizes the four named bounds (see the comparison below).

## Consequences

- **The headline square bound.** ω(ℂ) ≤ 9/4, i.e.
  $O_\varepsilon(n^{9/4+\varepsilon})$ arithmetic operations [S3:46–49].
- **The record-line bounds.** ω < 2.258 in characteristic zero,
  ω(1, 0.709, 1) < 2.092, α > 0.465, and ω(F) < 2.371054886006746 over every
  fixed field including positive characteristic [S5:73–77, S7:58–62].
- **Characteristic transfer.** The strict square and k=0.709 bounds extend
  beyond ℂ to characteristic-zero fields and all but finitely many positive
  characteristics [S5:80–85].
- **The dual exponent.** α > 0.465 as a supremum of aspect ratios with
  exponent 2 [S11:10].
- **Shipped certificates.** The two verification bundles check the numerical
  constants byte-for-byte (see coverage) [S17:23] [S18:21].

## Section skeleton

Manuscript 1 [S3] is a single LaTeX file, `paper.tex` (no `\input`s), with
six sections at [S3:37], [S3:142], [S3:270], [S3:392], [S3:605], [S3:700].
Manuscript 2's root [S4] includes fifteen files in the order [S4:72–87]:
`introduction`, `rectangular/02-tensor-preliminaries`, `tex/algebra`,
`tex/values`, `tex/ap`, `tex/certificate-w`, `tex/certificate`,
`tex/conclusion`, `rectangular/04-label-trees`, `rectangular/05-completion`,
`rectangular/06-optimization`, `rectangular/07-certificates`,
`rectangular/08-comparison`, `tex/barrier-coefficients`,
`tex/reproducibility`. Manuscript 3's root [S6] includes eight sections
[S6:47–53]: `introduction`, `foundations`, `joint-extraction`, `recovery`,
`staggering`, `leaf-volumes`, `parameters`, then `parameter-tables` after a
page break [S6:56]. The three shipped PDFs [S8] [S9] [S10] are the
manuscripts in the form the release distributes.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S11], two
comparator stubs [S12:118–120] [S13], and four `main_results` entries over two
configs [S16:1389–1403]. The first scope paragraph: "the formalized results
bound the complex matrix-multiplication exponent by $\omega(\mathbb C)\le9/4$,
the dual exponent by $\alpha>0.465$, and the rectangular exponent at aspect
ratio $0.709$ by $\omega(\mathbb C;1,0.709,1)<2.092$" [S11:10], and "the
square bound implies the paper's weaker $2.258$ headline bound" [S11:10]. The
second paragraph: "the formalized result gives the unconditional bound
$\omega(F)<2.371054886006746$ for every field $F$, including finite fields
and fields of positive characteristic" [S11:12], and "no numerical
inequalities remain as hypotheses" [S11:12].

The `main_results` entries [S16:1389–1403] name:
`OAI.MatrixAllFields.MatrixMultiplication.AllFieldMain.omega_lt_source_constant`
in `AllFieldsBound.lean`, and `OAI.MatrixMultiplication.{complex_omega_le_nine_quarters,
complex_alpha_gt_93_div_200, complex_rectangular_omega_lt_523_div_250}` in
`Main.lean`. In the source all four are stated and closed: "```lean
theorem complex_omega_le_nine_quarters : Arithmetic.omega ℂ ≤ (9 : ℝ) / 4 := AuxiliarySeparation.omega_le_nine_quarters
```
[S14:14–16]"
, "```lean
theorem complex_alpha_gt_93_div_200 : (93 : ℝ) / 200 < Arithmetic.complexAlpha := DualExponentBound.alpha_gt
```
[S14:19–21]" , "```lean
theorem complex_rectangular_omega_lt_523_div_250 : Arithmetic.rectangularOmega ℂ ((709 : ℝ) / 1000) < (523 : ℝ) / 250 := CW75ReorderedRectangular.rectangularOmega_lt_target
```
[S14:25–27]" , and "```lean
theorem omega_lt_source_constant (F : Type u) [Field F] : Arithmetic.omega F < (2371054886006746 : ℝ) / 10 ^ 15 ∧ (2371054886006746 : ℝ) / 10 ^ 15 < (2371056 : ℝ) / 10 ^ 6 := by
```
[S15:17–19]"
[S15:17–19] — each an `Arithmetic.omega` / `Arithmetic.complexAlpha` /
`Arithmetic.rectangularOmega` inequality proved by named lemmas
(`AuxiliarySeparation`, `DualExponentBound`, `CW75ReorderedRectangular`,
`AllFieldOrderedLimits` plus the stage lemmas [S15:20–25]). `grep` finds
**zero** `sorry` in both formalized files.

The two comparator stubs carry the same targets: "```lean
theorem complex_omega_le_nine_quarters : Arithmetic.omega ℂ ≤ (9 : ℝ) / 4 := by sorry
```
[S12:118–120]" (the
stub's `complex_omega_le_nine_quarters` ends in `sorry`), its two siblings at
[S12:122–128], and `omega_lt_source_constant` with `sorry` at [S13:109–112].
A comparator stub is a target the release set itself; the proved versions are
the ones the `main_results` entries name. The reading is of source text only
— no `lake` or `lean` run elaborates the proofs, so the claim here is that
the proof bodies exist in the source, not that the files compile.

## Coverage

The ledger row `fam=107` [S19] records the tier and the counts: `tier=T3`,
`paps=3`, `paps_form=3`, `chal=2`, `mainres=2`, `scope_note=1`,
`verification=2`, `trace=`. This is the densest coverage shape in the queue:
all three manuscripts are formalization sources, the four `main_results`
entries cover all three named bounds plus the all-fields bound over two
configs, and the family ships **two verification bundles** — the release's
finite-arithmetic certificates. Manuscript 2's bundle [S17:23] ships a
top-level `verification/README.md` whose inventory command checks the listed
file sets, byte counts, and hashes against `BUILD-INPUTS.json`: "the command
reads `BUILD-INPUTS.json` and `certificate/package-manifest.json`. A zero
exit status and a line beginning `PASS:` mean the listed file sets, byte
counts, and hashes match. This command does not run the numerical checks"
[S17:23], with two numerical packages (`certificate/`, `certificates/`)
documented inside [S17:3–9]. Manuscript 3's bundle has no README; its run
command lives in the manuscript README: "use Python 3.10 or later with
`mpmath==1.3.0`, as specified in `verification/data/requirements.txt`. Keep
assertions enabled" [S18:21], running `verify_parameters.py` in interval
modes [S18:21–25]. The shape flags are `bound|classification`, and
`resolves_named=0` — the family title names a bound, not a conjecture, so
the ledger verb rule has nothing to fire on.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2645], the three manuscript entries [S1:2652], [S1:2661], [S1:2670], and their abstracts [S1:2654], [S1:2663], [S1:2672]. The release's inline code spans stay as backticked markdown, and the release's italic markup and HTML entities are folded to the plain word |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 107 at [S2:292] |
| S3 | [`preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/paper.tex`](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/paper.tex) | 1022 | root (`\documentclass`); abstract [S3:32–35]; the exponent definition [S3:39–43]; the main theorem [S3:45–49]; the history paragraph [S3:51–57]; the six section headings at [S3:37], [S3:142], [S3:270], [S3:392], [S3:605], [S3:700] |
| S4 | [`preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/build/main.tex`](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/build/main.tex) | 90 | root (`\documentclass`); abstract [S4:63–69]; the fifteen-file include order [S4:72–87] |
| S5 | [`preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/build/introduction.tex`](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/build/introduction.tex) | 307 | the three-bound main theorem [S5:72–78]; the characteristic-transfer corollary [S5:80–85] |
| S6 | [`preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/build/main.tex`](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/build/main.tex) | 61 | root (`\documentclass`); abstract [S6:42–46]; the eight-section include order [S6:47–56] |
| S7 | [`preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/build/sections/introduction.tex`](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/build/sections/introduction.tex) | 161 | the main theorem [S7:57–63]; the exactness and cost-scope notes [S7:65–69] |
| S8 | [`preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf`](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf) | 10350 | manuscript 1 as shipped |
| S9 | [`preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf`](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf) | 16344 | manuscript 2 as shipped |
| S10 | [`preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf`](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf) | 16361 | manuscript 3 as shipped |
| S11 | [`lean/docs/107.md`](../../../lean/docs/107.md) | 19 | scope note — the two Scope paragraphs at [S11:10] and [S11:12] |
| S12 | [`lean/ComparatorChallenges/MatrixMultiplication.lean`](../../../lean/ComparatorChallenges/MatrixMultiplication.lean) | 132 | the comparator stub — the three target theorems at [S12:118–128] |
| S13 | [`lean/ComparatorChallenges/MatrixFields.lean`](../../../lean/ComparatorChallenges/MatrixFields.lean) | 116 | the comparator stub — `omega_lt_source_constant` at [S13:109–112] |
| S14 | [`lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean`](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean) | 31 | the formalized file — the three proved theorems at [S14:14–16], [S14:19–21], [S14:25–27] |
| S15 | [`lean/OAI/LinearAlgebra/MatrixFields/Conclusions/AllFieldsBound.lean`](../../../lean/OAI/LinearAlgebra/MatrixFields/Conclusions/AllFieldsBound.lean) | 34 | the formalized file — `omega_lt_source_constant` proved at [S15:17–25] |
| S16 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the four `main_results` entries over two configs, at [S16:1389–1403] |
| S17 | [`preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/verification/README.md`](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/verification/README.md) | 23 | the verification bundle — the inventory-check run command at [S17:17–23] |
| S18 | [`preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/README.md`](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/README.md) | 29 | the manuscript README — its `## Verification` run command at [S18:19–25] |
| S19 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=107`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- J. Alman, R. Duan, V. Vassilevska Williams, Y. Xu, Z. Xu, and R. Zhou, More asymmetry yields faster matrix multiplication, in _Proc. 2025 Annual ACM-SIAM Symposium on Discrete Algorithms_, SIAM, 2025, 2005–2039. doi:10.1137/1.9781611978322.63.
- D. Bini, Relations between exact and approximate bilinear algorithms. Applications, _Calcolo_ **17** (1980), 87–97. doi:10.1007/BF02575865.
- M. Christandl, P. Vrana, and J. Zuiddam, Universal points in the asymptotic spectrum of tensors, _J. Amer. Math. Soc._ **36** (2023), 31–79. doi:10.1090/jams/996.
- R. Duan, H. Wu, and R. Zhou, Faster matrix multiplication via asymmetric hashing, in _Proc. 64th IEEE Annual Symposium on Foundations of Computer Science_, IEEE, 2023, 2129–2138. doi:10.1109/FOCS57990.2023.00130.
- E. Dupont, M. Eisenberger, B. Kozlovskii, A. Mehrabian, F. J. R. Ruiz, A. See, R. Zhou, J. Alman, V. Vassilevska Williams, and M. Balog, Improving the matrix multiplication exponent with modern optimization and AlphaEvolve, preprint, 2026. arXiv:2608.16884.
- F. Le Gall, Powers of tensors and fast matrix multiplication, in _Proc. 39th International Symposium on Symbolic and Algebraic Computation_, ACM, 2014, 296–303. Full version: arXiv:1401.7714v1.
- E. Kowalski, _An introduction to the representation theory of groups_, Graduate Studies in Mathematics **155**, American Mathematical Society, 2014. doi:10.1090/gsm/155. Author version: _Representation theory_, February 17, 2017, Section 2.6.
- A. Schönhage, Partial and total matrix multiplication, _SIAM J. Comput._ **10** (1981), 434–455. doi:10.1137/0210032.
- A. M. Davie and A. J. Stothers, Improved bound for complexity of matrix multiplication, _Proc. Roy. Soc. Edinburgh Sect. A_ **143** (2013), 351–369. doi:10.1017/S0308210511001648.
- A. J. Stothers, _On the complexity of matrix multiplication_, Ph.D. thesis, University of Edinburgh, 2010. hdl:1842/4734.
- V. Strassen, Gaussian elimination is not optimal, _Numer. Math._ **13** (1969), 354–356. doi:10.1007/BF02165411.
- V. Strassen, The asymptotic spectrum of tensors and the exponent of matrix multiplication, in _Proc. 27th Annual Symposium on Foundations of Computer Science_, IEEE, 1986, 49–54. doi:10.1109/SFCS.1986.52.
- V. Strassen, Relative bilinear complexity and matrix multiplication, _J. Reine Angew. Math._ **375/376** (1987), 406–443. doi:10.1515/crll.1987.375-376.406.
- V. Strassen, The asymptotic spectrum of tensors, _J. Reine Angew. Math._ **384** (1988), 102–152. doi:10.1515/crll.1988.384.102.
- A. Tychonoff, Ein Fixpunktsatz, _Math. Ann._ **111** (1935), 767–776. doi:10.1007/BF01472256.
- J. Alman and V. Vassilevska Williams, A refined laser method and faster matrix multiplication, _TheoretiCS_ **3** (2024), Article 21, 1–32. doi:10.46298/theoretics.24.21. Conference version in SODA 2021, 522–539.
- V. Vassilevska Williams, Multiplying matrices faster than Coppersmith–Winograd, in _Proc. 44th Annual ACM Symposium on Theory of Computing_, ACM, 2012, 887–898. doi:10.1145/2213977.2214056. Expanded corrected author version: _Multiplying matrices in $O(n^{2.373})$ time_, July 1, 2014.
- V. Vassilevska Williams, Y. Xu, Z. Xu, and R. Zhou, New bounds for matrix multiplication: from alpha to omega, in _Proc. 2024 Annual ACM-SIAM Symposium on Discrete Algorithms_, SIAM, 2024, 3792–3835. doi:10.1137/1.9781611977912.134.
- D. Coppersmith and S. Winograd, Matrix multiplication via arithmetic progressions, _J. Symbolic Comput._ **9** (1990), 251–280. doi:10.1016/S0747-7171(08)80013-2.
