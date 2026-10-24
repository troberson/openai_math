[Notes](../../README.md) / [Summaries](../README.md) / [Functional analysis](../../index/disciplines/functional-analysis.md) / [Family 325](../../index/functional-analysis/325-complete-crouzeix-conjecture.md)

# 325 — The complete Crouzeix conjecture

[Index page](../../index/functional-analysis/325-complete-crouzeix-conjecture.md)

## Original CONTENTS.md summary

 carries the family entry:

> Resolves the complete Crouzeix conjecture: for every bounded operator $A$ on a complex Hilbert space and every finite matrix-valued polynomial $P$, one has $\lVert P[A]\rVert\le2\sup_{z\in W(A)}\lVert P(z)\rVert$, where $W(A)$ is the numerical range. The constant $2$ is sharp, independent of the matrix size, and valid in infinite dimensions. [S1:746]

The entry links the two manuscripts as "Direct proof [S1:746]" and "Structural proof [S1:746]" .

The first manuscript's title is "A direct proof of the complete Crouzeix
inequality" [S2:1].

The second manuscript's title is "The complete Crouzeix theorem [S6:1]" .

## Undergraduate summary

The numerical range of a matrix is the set of values $u^*Au$ over unit
vectors. It is convex and contains the spectrum. Evaluating a polynomial at
the matrix and taking its norm can be bounded by the largest norm the
polynomial reaches on that set, and the question is the constant.
[S3:55–56] states the complete form: "The complete Crouzeix conjecture asks
whether the constant two holds uniformly in the coefficient dimension $m$, the
base dimension, and the degree."

The coefficients are matrices, not scalars, which is what makes the complete
conjecture harder than the scalar one. [S3:68–70] says why: "Its complete
character is the uniformity in $m$: a scalar proof need not survive matrix
amplification, because coefficient matrices need not commute."

The first manuscript proves the bound directly. [S3:32–33] gives its abstract:
"We give a direct proof of the sharp constant-two numerical-range inequality
for matrix-valued polynomials in all finite base and coefficient dimensions."
The theorem adds the sharpness half: [S3:65] states "The constant two cannot
be decreased uniformly over $n,m$, and $d$." The manuscript is dated [S2:5].

The second manuscript reaches the same result through a structural theorem
and extends it to operators. [S7:46–49] gives its abstract: "We resolve the
complete Crouzeix conjecture by proving the sharp constant-two numerical-range
inequality for every bounded operator on a complex Hilbert space and every
matrix-valued polynomial. No separability assumption is needed." The
manuscript is dated [S6:5].

The scalar case follows. [S7:1084] states the constant's independence: "The
constant is independent of both matrix sizes and the degree."

## Graduate summary

The second manuscript's opening poses the structural question before the
inequality. [S7:60–62] asks it: "Can one choose a single controlled change of
inner product and a single positive boundary density to represent all
matrix-valued analytic evaluations of a matrix?" The metric and the density
depend on the matrix and the enclosing domain, not on the coefficient size or
the function being evaluated.

The metric problem has an attained optimum. [S7:120] states that the
minimization "and has an attained minimum $1\le\kappa^2\le4$. [S7:120]" The
minimizing inner product gives a similarity with condition number at most two
that makes the conformal disk image of the matrix a contraction.

The representation half supplies one density for every test. [S7:146] states
it: "The same $S$, $\Lambda$, and $\kappa$ work for all $m$ and $v$. [S7:146]" The
density is a continuous positive semidefinite function on the unit circle
integrating to the identity.

The scope note records what the formalization carries. [S10:10] gives the
matrix result: "The complete Crouzeix inequality bounds a matrix-valued
polynomial evaluated at a matrix by its maximum norm on the numerical range.
The formalized result proves the bound with constant $2$ for every positive
matrix and coefficient size, every polynomial degree, and arbitrary complex
coefficients. It also proves that no smaller universal constant works.
Normality of the matrix and nonempty interior of its numerical range are not
assumed."

[S10:12] gives the operator result: "The formalization proves the complete
Crouzeix inequality with sharp constant two for every bounded operator on an
arbitrary complex Hilbert space. For every matrix-valued polynomial, its
operator evaluation has norm at most twice its supremum norm on the numerical
range. The same bound holds for finite matrix-valued functions holomorphic
near the closure of the numerical range and for rational functions with poles
outside that closure. No separability assumption is required."

[S10:14] gives the structural result: "For finite matrices in a bounded convex
domain with regular real-analytic Jordan boundary, the structural result gives
an attained optimal similarity with condition number at most two and one
continuous positive boundary density of mass the identity representing every
matrix-valued analytic test. The linked supporting statements include
numerical-range geometry and finite-compression identities."

The declarations are the quantified forms. `OAI.CompleteCrouzeix.main` at
[S11:61] is typed `UniversalBound 2 ∧ ∀ C : ℝ, UniversalBound C → 2 ≤ C`, so
the bound and its sharpness sit in one declaration.
`OAI.DirectCrouzeix.complete_crouzeix` at [S12:65] is `UniversalBound 2`.
`OAI.StructuralCrouzeixReference.challenge` at [S13:7] pairs the endpoint
statement with admissibility of the unit disk.

The family carries five comparator configs against two manuscripts, and each
config is a stub. [S14:35] carries `sorry`; [S15:34] carries `sorry`;
[S16:212] carries `sorry`; [S17:152] carries `sorry`; [S18:118] carries
`sorry`. The JSON targets name the declarations the release set:
`DirectCrouzeix` asks for `OAI.DirectCrouzeix.complete_crouzeix` and
`OAI.DirectCrouzeix.uniform_sharpness` in `OAI.Analysis.DirectCrouzeix.Main`;
`CompleteCrouzeix` asks for `OAI.CompleteCrouzeix.main` in
`OAI.Analysis.NumericalRange.Main`; `StructuralCrouzeix` asks for
`OAI.StructuralCrouzeixReference.challenge`; `CrouzeixHilbert` asks for
`OAI.CrouzeixHilbert.hilbert`; and `HilbertCrouzeix` asks for four geometry
and compression statements in `OAI.Analysis.HilbertCrouzeix.Main`. All five
permit the same three axioms: `propext`, `Quot.sound`, `Classical.choice`.

## History of the conjecture

The scalar question is Crouzeix's, and the first manuscript records the
published bounds. [S3:75–76] gives the dates and the first number: "Crouzeix
formulated the scalar constant-two question in 2004 and proved a universal
complete bound of $11.08$ in 2007", with the bibliography entries at [S4:36]
and [S4:41].

The constant two was known for small matrices before this result.
[S3:85–88] records the order-two case: "For all base matrices of order two,
Badea, Crouzeix, and Delyon obtained the complete constant two. In the
nonnormal case, they make the conformal image of the matrix a contraction by a
similarity with condition number at most two, using the numerical-range
ellipse", whose entry is [S4:13]. The condition-number bound in the second
manuscript's structural theorem is the same shape, for a general admissible
domain.

The gap the complete form closes is recorded in the first manuscript's own
comparison. [S3:99–100] states it: "The scalar results fix $m=1$, while the
latter complete result restricts the base dimension;" — the scalar proofs pin
the coefficient dimension at one, and the most recent complete result pins the
base dimension. The theorem leaves both independent. The second manuscript
cites the same order-two result at [S8:17], and both manuscripts ship a
figure of the numerical range and its conformal image, [S5:1] and [S9:1].

`notes/tables/conjecture-standing.tsv` carries no row for family 325, so the
prior on the conjecture's standing is not recorded in the release's own
reading. The claim in the entry is the record.

## Consequences

The constant is sharp and dimension-free. [S3:65] proves the bound cannot be
lowered uniformly, and [S7:1084] states the constant's independence of the two
matrix sizes. The overview entry says the same in its own words: the constant
is sharp, independent of the matrix size, and valid in infinite dimensions.

The operator form removes hypotheses the published results carried. [S10:10]
says normality and nonempty interior are not assumed, and [S10:12] says no
separability assumption is required and the bound extends to holomorphic
functions near the closure of the numerical range and to rational functions
with poles outside it. The published bound of $11.08$ and the bound
$1+\sqrt2$ both sat under extra conditions.

The structural theorem is the part that reaches past the inequality.
[S7:120] gives the attained optimum with condition number at most two, and
[S7:146] gives one density representing every matrix-valued test. That is a
metric statement about the numerical range, and it is why the family carries
five comparator configs against two manuscripts.

The release's own record is source-level. The scope note says the formalized
claims exist and names their declarations; the five comparator configs carry
`sorry`; no Lean run in this repository proves any of them elaborates.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 746 |
| S2 | [`preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/README.md`](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/README.md) | 18 | Manuscript 1 title, date, citation |
| S3 | [`preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex`](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex) | 623 | Abstract, theorem, introduction, history |
| S4 | [`preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/references.tex`](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/references.tex) | 105 | Bibliography entries |
| S5 | [`preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/figures/normal.tex`](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/figures/normal.tex) | 21 | Numerical-range figure |
| S6 | [`preprints/The-complete-Crouzeix-theorem-September-23-2026/README.md`](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/README.md) | 18 | Manuscript 2 title, date, citation |
| S7 | [`preprints/The-complete-Crouzeix-theorem-September-23-2026/build/main.tex`](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/build/main.tex) | 1523 | Abstract, structural theorem, representation theorem, corollaries |
| S8 | [`preprints/The-complete-Crouzeix-theorem-September-23-2026/build/references.tex`](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/build/references.tex) | 125 | Bibliography entries |
| S9 | [`preprints/The-complete-Crouzeix-theorem-September-23-2026/build/figures/coordinates.tex`](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/build/figures/coordinates.tex) | 36 | Conformal-coordinate figure |
| S10 | [`lean/docs/325.md`](../../../lean/docs/325.md) | 24 | Scope note |
| S11 | [`lean/OAI/Analysis/NumericalRange/Main.lean`](../../../lean/OAI/Analysis/NumericalRange/Main.lean) | 70 | `CompleteCrouzeix.main` |
| S12 | [`lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean`](../../../lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean) | 119 | `DirectCrouzeix.complete_crouzeix` |
| S13 | [`lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean`](../../../lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean) | 12 | `StructuralCrouzeixReference.challenge` |
| S14 | [`lean/ComparatorChallenges/DirectCrouzeix.lean`](../../../lean/ComparatorChallenges/DirectCrouzeix.lean) | 44 | Stub, `sorry` at line 35 |
| S15 | [`lean/ComparatorChallenges/CompleteCrouzeix.lean`](../../../lean/ComparatorChallenges/CompleteCrouzeix.lean) | 39 | Stub, `sorry` at line 34 |
| S16 | [`lean/ComparatorChallenges/StructuralCrouzeix.lean`](../../../lean/ComparatorChallenges/StructuralCrouzeix.lean) | 216 | Stub, `sorry` at line 212 |
| S17 | [`lean/ComparatorChallenges/CrouzeixHilbert.lean`](../../../lean/ComparatorChallenges/CrouzeixHilbert.lean) | 158 | Stub, `sorry` at line 152 |
| S18 | [`lean/ComparatorChallenges/HilbertCrouzeix.lean`](../../../lean/ComparatorChallenges/HilbertCrouzeix.lean) | 143 | Stub, `sorry` at line 118 |

## Bibliography

- L. V. Ahlfors, _Complex Analysis_, third ed., McGraw–Hill, New York, 1979.
- L. V. Ahlfors, _Complex Analysis_, third ed., McGraw–Hill, New York, 1979.
- W. Arveson, Subalgebras of $C^*$-algebras II, _Acta Math._ **128** (1972), 271–308.
- C. Badea, M. Crouzeix, and B. Delyon, Convex domains and $K$-spectral sets, _Math. Z._ **252** (2006), 345–365. doi:10.1007/s00209-005-0857-y.
- C. Badea, M. Crouzeix, and B. Delyon, Convex domains and $K$-spectral sets, _Math. Z._ **252** (2006), 345–365.
- B. Beckermann, Image numérique, GMRES et polyn{\^o}mes de Faber, _C. R. Math._ **340** (2005), 855–860. doi:10.1016/j.crma.2005.04.027.
- B. Beckermann, Image numérique, GMRES et polyn\^omes de Faber, _C. R. Math._ **340** (2005), 855–860.
- B. Beckermann and M. Crouzeix, Faber polynomials of matrices for non-convex sets, _Jaen J. Approx._ **6** (2014), 219–231. arXiv:1310.1356v1.
- M. Crouzeix, Bounds for analytical functions of matrices, _Integral Equations Operator Theory_ **48** (2004), 461–477. doi:10.1007/s00020-002-1188-6.
- M. Crouzeix, Numerical range and functional calculus in Hilbert space, _J. Funct. Anal._ **244** (2007), 668–690. doi:10.1016/j.jfa.2006.10.013.
- B. Beckermann and M. Crouzeix, Faber polynomials of matrices for non-convex sets, _Jaen J. Approx._ **6** (2014), 219–231.
- M. Crouzeix, Bounds for analytical functions of matrices, _Integral Equations Operator Theory_ **48** (2004), 461–477. doi:10.1007/s00020-002-1188-6.
- M. Crouzeix, Numerical range and functional calculus in Hilbert space, _J. Funct. Anal._ **244** (2007), 668–690. doi:10.1016/j.jfa.2006.10.013.
- B. Delyon and F. Delyon, Generalization of von Neumann's spectral sets and integral representation of operators, _Bull. Soc. Math. France_ **127** (1999), 25–41. doi:10.24033/bsmf.2340.
- B. Delyon and F. Delyon, Generalization of von Neumann's spectral sets and integral representation of operators, _Bull. Soc. Math. France_ **127** (1999), 25–41.
- M. Crouzeix and A. Greenbaum, _A new proof that the numerical range is a complete $2$-spectral set for weighted shift matrices_, arXiv:2508.12768v1, August 18, 2025.
- P. Å hag, R. Czy{\.z}, and J. Virtanen, _The complete Crouzeix conjecture in dimension three and the Clou\^atre–Ostermann–Ransford conjecture_, arXiv:2608.27346v4, September 21, 2026.
- P. Å hag, R. Czy{\.z}, and J. Virtanen, _The complete Crouzeix conjecture in dimension three and the Clou\^atre–Ostermann–Ransford conjecture_, arXiv:2608.27346v4, September 21, 2026.
- F. Hausdorff, Der Wertvorrat einer Bilinearform, _Math. Z._ **3** (1919), 314–316. doi:10.1007/BF01292610.
- F. Hausdorff, Der Wertvorrat einer Bilinearform, _Math. Z._ **3** (1919), 314–316.
- S. Jin, _The numerical range is a $2$-spectral set_, Preprints.org 202607.1919, version 4, August 7, 2026.
- S. Jin, _The numerical range is a $2$-spectral set_, Preprints.org 202607.1919, version 4, August 7, 2026.
- V. E. Katsnelson, A. Ya. Kheifets, and P. M. Yuditskii, An abstract interpolation problem and the extension theory of isometric operators, in _Topics in Interpolation Theory_, OTAA **95**, Birkhäuser, 1997, 283–298. Preprint version: arXiv:0706.1896v1.
- Q. Luo, _Two boundary-certificate proofs of the Crouzeix theorem: Fiberwise Fourier recurrence and defect-Gram telescoping_, Preprints.org 202608.1661, version 2, August 28, 2026.
- Q. Luo, _Two boundary-certificate proofs of the Crouzeix theorem: Fiberwise Fourier recurrence and defect-Gram telescoping_, Preprints.org 202608.1661, version 2, August 28, 2026.
- OpenAI, _The complete Crouzeix theorem: optimal similarity and a common positive boundary representation_, OpenAI Math Release preprint OAI:The-complete-Crouzeix-theorem-September-23-2026, 2026.
- OpenAI, _A direct proof of the complete Crouzeix inequality_, OpenAI Math Release preprint OAI:A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026, 2026.
- M. Crouzeix and C. Palencia, The numerical range is a $(1+\sqrt{2})$-spectral set, _SIAM J. Matrix Anal. Appl._ **38** (2017), 649–655. doi:10.1137/17M1116672.
- M. Crouzeix and C. Palencia, The numerical range is a $(1+\sqrt2)$-spectral set, _SIAM J. Matrix Anal. Appl._ **38** (2017), 649–655.
- V. I. Paulsen, Completely bounded homomorphisms of operator algebras, _Proc. Amer. Math. Soc._ **92** (1984), 225–228.
- C. Pommerenke, _Boundary Behaviour of Conformal Maps_, Springer-Verlag, 1992.
- R. T. Rockafellar, _Convex Analysis_, Princeton University Press, 1970.
- C. Runge, Zur Theorie der eindeutigen analytischen Functionen, _Acta Math._ **6** (1885), 229–244. doi:10.1007/BF02400416.
- E. Lorist and F. L. Schwenninger, _A solution to Crouzeix's conjecture_, arXiv:2608.03841v2, August 17, 2026.
- T. Ransford and F. L. Schwenninger, Remarks on the Crouzeix–Palencia proof that the numerical range is a $(1+\sqrt{2})$-spectral set, _SIAM J. Matrix Anal. Appl._ **39** (2018), 342–345. doi:10.1137/17M1143757.
- E. Lorist and F. L. Schwenninger, _A solution to Crouzeix's conjecture_, arXiv:2608.03841v2, August 17, 2026.
- T. Ransford and F. L. Schwenninger, Remarks on the Crouzeix–Palencia proof that the numerical range is a $(1+\sqrt{2})$-spectral set, _SIAM J. Matrix Anal. Appl._ **39** (2018), 342–345. doi:10.1137/17M1143757.
- P. Stein, Some General Theorems on Iterants, _J. Res. Nat. Bur. Stand._ **48** (1952), 82–83.
- B. Beckermann and N. Stylianopoulos, _Bergman Orthogonal Polynomials and the Grunsky Matrix_, Constr. Approx. **47** (2018), 211–235. doi:10.1007/s00365-017-9381-7.
- B. Beckermann and N. Stylianopoulos, Bergman Orthogonal Polynomials and the Grunsky Matrix, _Constr. Approx._ **47** (2018), 211–235.
- B. Sz.-Nagy, Sur les contractions de l'espace de Hilbert, _Acta Sci. Math. (Szeged)_ **15** (1953), 87–92.
- O. Toeplitz, Das algebraische Analogon zu einem Satze von Fejér, _Math. Z._ **2** (1918), 187–197. doi:10.1007/BF01212904.
- O. Toeplitz, Das algebraische Analogon zu einem Satze von Fejér, _Math. Z._ **2** (1918), 187–197.
- M. S. Brodski\uı, Unitary operator colligations and their characteristic functions, _Russian Math. Surveys_ **33**:4 (1978), 159–191.
