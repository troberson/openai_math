[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 101](../index/convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md)

# 101 — The sharp simplex conjecture for isotropic constants

[Index page](../index/convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md)

## Original CONTENTS.md summary

The release's blurb 

> **101. The sharp simplex conjecture for isotropic constants.** Proves that simplices uniquely maximize the isotropic constant among convex bodies in every dimension, resolving the strong isotropic constant conjecture. Also establishes the sharp entropy lower bound for log-concave probability densities, with equality precisely for invertible affine images of products of one-sided exponential laws. [S1:2486]

The manuscript's own abstract states the two results: "We prove the strong isotropic constant conjecture: in each dimension, simplices are the unique maximizers of the isotropic constant among convex bodies [S1:2495]" [S4:45–47], and, for the entropy bound, "with equality precisely for invertible affine images of products of one-sided exponential laws [S1:2495]" [S4:49–50].

## Undergraduate summary

The isotropic constant of a convex body compares how spread out its uniform
distribution is with how much space the body occupies. For a body `K` in
`n`-dimensional space, form its covariance matrix and its volume; `L_K` is built
from the determinant of the covariance divided by the square of the volume,
raised to a power. [S5:14] "This quantity is unchanged by invertible affine
maps." [S5:14] So `L_K` describes the shape of the body, not the way it sits in
space.

Bourgain's slicing problem asked whether `L_K` is bounded by a constant that does
not grow with dimension. This manuscript asks the sharper question: in each
dimension, which body makes `L_K` as large as possible? "The sharp form, also
called the strong isotropic constant conjecture, asks, in each dimension,
whether a simplex maximizes" the constant. [S5:23–24] The answer is the simplex,
uniquely, and the maximum is an explicit constant. [S4:45–47]

The manuscript proves the analytic form of the same statement: for a log-concave
probability density `f` on `m`-dimensional space, its differential entropy is at
least `m` plus one half the log of the determinant of its covariance. [S4:49–50]
A product of `m` independent exponential variables of mean one has entropy `m`
and identity covariance, so the bound cannot be improved. [S5:87–88] The theorem
"asserts that a log-concave density with identity covariance has entropy [S5:91]" at
least `m`. [S5:91]

The proof is analytic, not geometric. It transports Gaussian measure to the
density by a gradient map, estimates the resulting entropy deficit, and forces
the matrices in that estimate to commute. Every scalar constant in the scalar
inequalities is an exact rational, and a shipped Python script checks the
arithmetic. [S13:6–7]

## Graduate summary

**The two theorems and their equivalence.** The entropy theorem and the simplex
theorem are the same statement in dimensions `m` and `n = m − 1`. "The
calculation identifies equality in the body inequality with entropy equality in
one higher dimension. The support of the resulting exponential product then
determines the body." [S11:8–10] The entropy bound is `h(f) ≥ m + ½ log det
Cov(f)` for a log-concave probability density on `R^m`, with equality exactly for
affine images of products of one-sided exponential laws. [S4:49–50] The simplex
bound is `L_K ≤ (n!)^{1/n} / ((n+1)^{(n+1)/(2n)} √(n+2))`, with equality if and
only if `K` is a simplex. [S4:45–47]

**Why the sharp form is a different question.** "The distinction is substantial:
a universal bound does not identify the extremal value or an extremizing body."
[S5:25–26] The manuscript states its position plainly: "We prove the sharp
inequality for arbitrary convex bodies and classify all equality cases."
[S5:36–37]

**The transport.** The proof assumes first that `f = e^{−V}` is smooth with
Hessian bounded above and below by positive multiples of the identity. A gradient
map transports standard Gaussian measure to `f`, and `J = D²φ` is the
reparametrized Jacobian: "Brenier's theorem and Caffarelli's regularity and
contraction theory supply this positive definite matrix field and its uniform
bounds." [S5:113–116] "There are two objectives. [S6:13]" "We choose affine
coordinates in which a reparametrization of the transport Jacobian has mean
zero." [S6:13–14] "The resulting estimate contains an additional nonnegative
term measuring separation between eigenvalues; retaining this term is essential
in the matrix argument that follows." [S6:15–18]

Two features of the parametrization drive the proof. [S5:126] The normalization
is nonlinear: "This nonlinear normalization is proved by a homotopy and a
compactness argument; ordinary covariance normalization does not give the
required identity." [S5:128–130] And the energy estimate keeps its
eigenvalue-separation term, because "Discarding that term would lose the control
needed for matrix functions whose derivatives do not commute." [S5:133–134]

**The matrix estimate.** The transport estimate controls the Gaussian energy of
the reparametrized Jacobian, but its degree-one part has no Poincaré surplus.
"We use that part to choose a matrix supporting plane for the log determinant. [S7:6–7]"
[S7:6–7] The higher chaoses "supply the coercivity needed to prove the entropy
bound." [S7:8] "We retain a strict remainder that will also identify the equality
cases." [S7:9] The estimate "has both noncommuting matrix terms and scalar
divided differences"; "A commutator square controls the former. One scalar
inequality absorbs the cost of the supporting plane and the terms without
derivatives." [S5:150–153] "A second controls the divided differences, charging
their off-diagonal error to the eigenvalue-separation term retained earlier."
[S5:153–155] "After this cancellation, the entropy deficit is bounded above by a
quadratic expression that is nonpositive on every chaos of degree at least two."
[S5:156–158]

**The two scalar estimates.** "The matrix argument has reduced the entropy
inequality to two estimates." [S8:3] The first absorbs the part depending on the
first Gaussian chaos using a second moment; the second controls the remaining
quadratic form, one pair of eigenvalues at a time. [S8:3] "All finite decimals
below denote exact rational numbers." [S8:10–11] "in particular, none of the
bounds in this section is inferred from numerical sampling." [S8:14–15] The
rigidity weight is "continuous and nonnegative, vanishes only at [S7:21]" the value
`1`. [S7:21–22]

**Rigidity.** Equality is studied by applying the strict remainder to smooth
densities whose entropy gaps tend to zero. "The same approximation will let us
study equality by applying the strict remainder estimate to smooth densities
whose entropy gaps tend to zero." [S9:5–7] "For equality, it is essential that
this remainder applies to nearly sharp densities." [S5:163–164] "The expected
extremizers have restricted support and affine potentials, so equality cannot be
studied solely within the smooth, uniformly convex class." [S5:164–166] "We
approximate an arbitrary equality density while preserving entropy and
covariance." [S5:166–167]

"The local compatibility of this limiting Jacobian is decisive. [S5:174]" "The
constant and linear terms of its mixed-derivative identities force the symmetric
matrices" `X_r` to commute. [S5:175–176] "Commuting real symmetric matrices
admit a common orthonormal eigenbasis." "The structural step is local: [S10:6–7]"
the first two nonconstant terms of `q(A(x))` "force the coefficients of a linear
symmetric matrix field" to commute whenever `q(A)` is a Jacobian. [S10:6–8]
The commutation argument uses only the nonvanishing of the two endpoint
`q`-derivatives, "isolating a potentially reusable algebraic step. [S5:179–180]" "No
uniform Hessian bounds on the smooth approximants are required." [S5:180–181]
"Their affine normalizations are controlled only after the limiting law and its
covariance have been identified." [S5:181–182]

**Approximation.** "requires a potential with positive, bounded Hessian. We
remove those restrictions while preserving the entropy, covariance, and first
moments." [S9:3–5] "The elementary tail estimate below supplies a common
integrable bound for the approximation, including its entropy integrand."
[S9:14–15] "Dominated convergence therefore proves convergence of the
normalizing constants, first moments, second moments, and the integrals" of the
entropy. [S9:185–186] The covariance of the limit is positive definite, because
"zero variance in a nonzero direction would concentrate this Lebesgue density on
an affine hyperplane." [S9:201–202]

**Geometry.** The cone over `K` carries an exponential density whose entropy and
covariance are, up to a dimensional constant, those of the uniform distribution
on `K`. "The cone has nonempty interior, and its only point at height zero is
the origin." [S11:22–23] Equality forces the density to be an affine image of a
product of exponentials; "it has positive density on the interior of the cone,
and this interior is dense in the cone." [S11:74–75] "The orthant also has the
origin as its unique extreme point." Invertible affine maps preserve extreme
points, so the cone is an affine image of the positive orthant. [S11:84–85]
Normalizing the generating rays to height one gives points that are
"consequently affinely independent in the height-one hyperplane. [S11:100–101]" The limit is
therefore a simplex. [S11:100–101] The figure "illustrates the normalization of the generating
rays in this step." [S11:101–102] "For the determinant identity, subtract the
first column from the" others. [S11:110–111] In dimension one, "every convex
body is an interval, hence a simplex, and the constant is" `1/√12`.
[S11:126–127]

**The certificate.** The appendix proves the scalar bounds by exact rational
arithmetic. "The finite certificates below concern entire intervals: their
validity follows from coefficient bounds and polynomial positivity, with no
sampling assumption." "it uses rational arithmetic only. [S12:37]" [S12:36–37] The
shipped script reproduces the certificate "using only Python's standard
library." [S13:2] "All input decimals, polynomial operations, enclosures, and
comparisons are exact fractions." [S13:6–7] "Printed decimals are rounded
OUTWARDS; no float is used." [S13:7] "This program checks their rational
hypotheses and consequences; it is not a formal proof assistant for those
calculus statements." [S13:13–14]

## History of the conjecture

Prior (my training data, not repo text): the slicing problem is Bourgain's, from
the mid-1980s, asking for a dimension-free bound on the largest hyperplane
section of a convex body of unit volume. Bourgain's bound carried an
`O(n^{1/4})` factor; Klartag removed it. Stochastic localization, introduced by
Eldan, produced subpolynomial bounds, and Klartag and Lehec obtained a
dimension-free bound in 2023 using Guan's covariance estimate. The strong
isotropic constant conjecture — that a simplex maximizes `L_K` — was
conjectured by Campi, Colesanti, and Gronchi, who proved the bound in the plane;
Saroglou proved uniqueness there. Rademacher showed that a simplicial polytope
maximizing `L_K` must be a simplex. Fradelizi and Marín Sola formulated the sharp
entropy statement and proved its equivalence with the simplex bound; Melbourne,
Nayar, and Roberto proved the sharp entropy bound in dimension one. The
Bobkov–Madiman relation between entropy bounds and the slicing problem is the
standard route from analysis to the convex-geometric statement.

The manuscript's own account of this prior work: "In the plane, Campi, Colesanti,
and Gronchi proved the simplex bound, and Saroglou established uniqueness of the
maximizing body" [S5:28–29]; "Bobkov and Madiman developed the relation between
entropy bounds for log-concave measures and the slicing problem" [S5:94–95]; "In
dimension one, Melbourne, Nayar, and Roberto proved the sharp bound, attained by
a one-sided exponential distribution" [S5:99–100].

## Consequences

The sharp simplex bound implies the nonsymmetric Mahler inequality
`|K| |K°| ≥ (n+1)^{n+1} / (n!)^2` for a convex body with the origin in its
interior, through Klartag's exponential-measure argument on convex cones. The
equality classification transfers to bodies through the same cone construction,
so the bodies attaining the bound are the simplices. [S11:8–10]

The commutation step is recorded as reusable: only the nonvanishing of `q'(0)`
and `q''(0)` is used, not the full scalar machinery. [S5:179–180] The rigidity
argument needs no uniform Hessian bounds on the approximating potentials, which
is what lets the equality class include densities with restricted support.
"We can now bound the normalizing matrices uniformly, without any uniform
Hessian bounds on the approximating potentials." [S10:217–218] "Every invertible
affine image remains log-concave and has the same entropy gap by affine
invariance." [S10:251–252]

The manuscript states no open problem. The open questions that lie outside its
scope are whether the commutation lemma applies to other transport problems, and
whether the exact-rational certificate method extends to bounds whose scalar
constants are not rational.

## Comparison with the formalized statement

Family 101 is at tier T0: no Lean formalization, no scope note, no comparator
challenge, no reasoning trace. The release's blurb: "Proves that simplices
uniquely maximize the isotropic constant among convex bodies in every dimension,
resolving the strong isotropic constant conjecture." [S1:2486] The overview entry
names the family "The sharp simplex conjecture for isotropic constants [S1:2486]".
[S2:278]

The one evidence artifact is the verification bundle. Its README states that "The
scalar certificate checker uses only Python 3's standard library and exact
rational arithmetic" [S3:21–22], that "A successful run exits with status zero
and ends with `ALL CHECKS PASSED`" [S3:28], and that "It checks the rational
bounds used in the scalar estimates; the analytic inputs are proved in the
paper's appendix." [S3:29–30] That is a finite-arithmetic certificate for the
scalar constants. It is not a proof of the transport, matrix, rigidity, or
geometry arguments, and it is not a Lean check.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | Family 101's block, at line 2486 |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 101's `\resultentry`, at line 278 |
| S3 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/README.md`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/README.md) | 30 | The verification bundle's run command and scope |
| S4 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/main.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/main.tex) | 64 | Title, date, abstract |
| S5 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/introduction.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/introduction.tex) | 192 | The two theorems, prior work, ideas of the proof |
| S6 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/transport.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/transport.tex) | 552 | Transport map, normalization, energy estimate |
| S7 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/matrix.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/matrix.tex) | 585 | Entropy deficit, matrix estimate, the two scalar propositions |
| S8 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/scalar.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/scalar.tex) | 486 | The two scalar estimates, exact rational constants |
| S9 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/approximation.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/approximation.tex) | 206 | Removing smoothness, passage to the limit |
| S10 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/rigidity.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/rigidity.tex) | 254 | Commutation, diagonalization, equality classification |
| S11 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/geometry.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/geometry.tex) | 169 | Cone construction, simplex equality cases |
| S12 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/certificate.tex`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/certificate.tex) | 612 | The scalar certificates |
| S13 | [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/verification/verify_scalar.py`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/verification/verify_scalar.py) | 512 | The exact-rational checker |
