[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 339](../index/differential-geometry/339-katoks-entropy-rigidity-conjecture.md)

# 339 — Katok's entropy rigidity conjecture

[Index page](../index/differential-geometry/339-katoks-entropy-rigidity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:8256] and the catalog abstract [S2:776] state
the family's claim: for closed connected Riemannian manifolds of
dimension at least three with strictly negative sectional curvature,
normalized Liouville measure maximizes entropy for the geodesic flow if
and only if the metric is locally symmetric. The manuscript's abstract
 "For every closed connected smooth Riemannian manifold of dimension at
least three with strictly negative sectional curvature, we prove that
normalized Liouville measure has maximal entropy for the unit-speed
geodesic flow if and only if the metric is locally symmetric. This
resolves Katok's entropy rigidity conjecture positively in these
dimensions, including all rank-one symmetric types at arbitrary scale. [S3:60–67]"

## Undergraduate summary

Katok's entropy rigidity conjecture, formulated in 1982, asks whether
equality in the variational principle for the geodesic flow characterizes
locally symmetric metrics in negative curvature. The topological entropy
measures the exponential growth of orbit complexity; the Liouville
entropy measures the complexity seen by the invariant probability
measure naturally defined by the metric. The variational principle
bounds the latter by the former. Katok proved the surface case
($n=2$) by placing the Liouville entropy below, and the topological
entropy above, the entropy of the constant-curvature metric of the same
area, with rigidity in equality. The surface strategy does not extend
to higher dimensions: Flaminio showed the entropy Hessian is indefinite
at some hyperbolic three-manifolds. The manuscript proves the
conjecture for all $n\ge3$ 

> **theorem**
Suppose $n\ge3$ and every sectional curvature of $g$ is strictly
negative. Then
\[
 h_m_L(\phi_1)=h_{\mathrmtop}(\phi_1)
 \quad\Longleftrightarrow\quad
 \nabla^gR_g=0.
\]
Equivalently, equality holds precisely when the universal Riemannian
cover is a rank-one symmetric space of noncompact type, at an arbitrary
overall scale. [S3:90–100]

The rank-one symmetric conclusion includes real, complex, quaternionic,
and Cayley hyperbolic geometry. Local symmetry need not mean constant
sectional curvature.

## Graduate summary

**Entropy supplies volume data.** The proof's first stage converts
the entropy equality into geometric data. The entropy formula,
Bowen–Ruelle thermodynamic formalism, Gibbs estimates, and Livšic
cohomology give the infinitesimal unstable volume-expansion rate
$J=h+XF$, where $X$ generates the flow. A transfer function produces
two conormal volume forms: one annihilates $E^u$, the other $E^s$,
and flow transport multiplies them by $e^{-ht}$ and $e^{ht}$. Their
controlled derivatives along individual weak leaves provide the initial
data; ambient smoothness is still to be established [S3:162–170].

**Plaque jets and algebraic hulls.** The second and third stages turn
the volume data into formal algebraic structure. Finite jets of actual
plaques and their conormal densities are encoded in finite-dimensional
contracting state spaces. Section 3 (algebraic hulls) takes the
polynomial relations obeyed by actual plaque jets, extracts affine
families of alternative conormal covectors from their solution sets,
and constructs formal affine fields $\mathcal{A}^u, \mathcal{A}^s$
with full ambient Taylor coefficients that are smooth and holonomic
along both actual foliations. All constructions use finite weight
cutoffs; no formal series is assumed to converge [S4:1–12].

**The algebraic dichotomy.** Section 5 studies formal vector fields
preserving the contact form and both affine families. A dilation
determined by the Lyapunov exponents belongs to the symmetry algebra,
and the entropy trace identity gives a constraint on its elements.
Combined with Cartan–Guillemin structure theory, the result is a
dichotomy: a finite-dimensional symmetry algebra supplies formal fields
with values in $E^s, E^u$; an infinite-dimensional one supplies nonzero
stable and unstable directions joined by a formal flat affine
connection [S3:183–196].

**Quantitative realization.** The last two sections turn formal
conclusions into smooth maps. In the infinite alternative, a complete
proper stable ray is constructed; sampling on expanding stable plaques
controls derivatives of truncated unstable translations, whose limits
give actual mixed stable–unstable rectangles that the endpoint geometry
of negative curvature rules out. In the finite alternative, the same
estimates prove smoothness of functions labeling weak unstable leaves,
yielding the globally smooth invariant splitting. The Benoist–Foulon–
Labourie theorem then gives the classical rigidity step
[S3:197–210].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Katok formulated the conjecture and proved the surface case in 1982,
with an additional rigidity statement within the conformal class of a
locally symmetric metric. Flaminio (1995) proved positivity of the
second variation of the entropy gap along fixed-volume metric paths
transverse to the diffeomorphism orbit for higher-dimensional real
hyperbolic metrics, showing equality is locally isolated along each
such path, and produced a hyperbolic three-manifold at which the
Hessian is indefinite. Humbert (2026) proved rigidity throughout a
sufficiently small $C^N$ neighborhood of any fixed real or complex
hyperbolic metric. For more general flows, Foulon (2001) characterized
maximal-entropy measure for contact Anosov flows on three-dimensional
phase spaces by conjugacy to constant-curvature surface geodesic flows;
DeSimoi–Legui–Vinhage–Yang (2020) removed the contact assumption. The
volume-entropy rigidity of Besson–Courtois–Gallot (1995), with the
Cayley correction of Ruan (2024), gives a scale-invariant comparison
from a locally symmetric target; here the symmetric target is a
conclusion, reached through Benoist–Foulon–Labourie (1992) only after
global smoothness of the invariant distributions is established
[S3:121–158].

## Consequences

**Katok's entropy rigidity conjecture is resolved in dimensions
$\ge3$.** For every closed connected smooth Riemannian manifold of
dimension at least three with strictly negative sectional curvature,
entropy equality holds if and only if the metric is locally symmetric
[S3:90–100].

**The symmetric types include all rank-one symmetric spaces of
noncompact type, at arbitrary scale.** The conclusion covers real,
complex, quaternionic, and Cayley hyperbolic geometry in the
dimensions where these occur [S3:96–100].

**The maximal-entropy measure is mutually singular with Liouville
measure off the symmetric set.** When the metric is not locally
symmetric, the unique maximal-entropy probability is mutually singular
with normalized Liouville measure [S3:102–112].

## Section skeleton

**Manuscript** [S3], 9 sections: introduction (in `main.tex`),
preliminaries, normal forms, hulls, symmetries, algebra, realization,
smoothness, and completion (in `main.tex`). Seven `.tex` files under
`build/sections/`. Its root is `build/main.tex`, with a
`references.bib` bibliography [S4]. One figure file
(`figures/mixed-rectangle.tex`).

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — a root `build/main.tex`, 7 `.tex` files under
`build/sections/`, one figure `.tex`, and a `references.bib`
bibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 339 at line 8256. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 776. |
| S3 | [`preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/build/main.tex`](../../../preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/build/main.tex) | 375 | Manuscript main file: title, abstract, introduction, and the completion proof. |
| S4 | [`preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/build/sections/03-hulls.tex`](../../../preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/build/sections/03-hulls.tex) | 994 | The algebraic hull construction: formal affine fields with coherent full ambient Taylor coefficients. |
