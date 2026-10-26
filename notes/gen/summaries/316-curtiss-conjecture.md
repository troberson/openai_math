[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 316](../index/topology/316-curtiss-conjecture.md)

# 316 — Curtis’s conjecture

[Index page](../index/topology/316-curtiss-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:7747] and the catalog abstract [S2:726] state
the family's claim: Curtis's conjecture — in every positive degree, the
mod-two stable Hurewicz image of the sphere is spanned by the images of
the Hopf-invariant-one classes $\eta,\nu,\sigma$ and the
Kervaire-invariant-one classes that exist. The manuscript's abstract
 "We prove Curtis's conjecture: in every positive degree, the mod-two
stable Hurewicz image of the sphere is spanned by the images of
\(\eta,\nu,\sigma\) and the Kervaire-invariant-one classes that exist.
Consequently, Eccles's conjecture holds for every sphere \(S^n\) with
\(n>0\). [S3:8–14]"

## Undergraduate summary

The stable Hurewicz map takes a stable homotopy class of spheres to
its image in stable homology with mod-two coefficients; the "positive
stable Hurewicz image" is the collection of homology classes coming
from classes of positive stem. Curtis's conjecture predicts that this
collection has a very small set of generators: the images of the three
Hopf-invariant-one elements in degrees $1$, $3$, and $7$ (the classical
$\eta$, $\nu$, $\sigma$), together with the images of the
Kervaire-invariant-one elements, which exist only in certain degrees.
The Kervaire invariant is a secondary invariant measured on framed
manifolds, and a class carries it when the corresponding framed manifold
has Arf invariant one. The theorem pins down the entire positive image
[S4:3–22]:

> **theorem**
The image of \(\bigoplus_d>0h_d\) is spanned over \(\mathbb F_2\) by
the Hurewicz images of the Hopf-invariant-one classes
\(\eta,\nu,\sigma\), in degrees \(1,3,7\), and the
Kervaire-invariant-one classes \(\theta_j\), in degrees
\(2^j+1-2\), \(j\ge1\), whenever they exist.
In particular, Curtis's conjecture is true in all positive degrees. [S4:24–31]

The two corollaries give the concrete payoffs. Eccles's conjecture
holds for every positive-dimensional sphere: each nonzero mod-2
spherical class in $H_*(QS^n;\mathbb F_2)$ is either the bottom class $e_n$ or
a nonzero suspension of one of the Hopf images. And the positive stable
Hurewicz image is finite, concentrating on the Hopf degrees $1,3,7$
and the Kervaire degrees $2,6,14,30,62,126$; in particular it vanishes
above degree $126$.

## Graduate summary

**Terminal-level reduction.** The proof is organized around the last
nonzero homology suspension of a spherical class. For a representative
$f_0:S^d\to Q_0S^0$ with successive adjoints, the terms $z_j=h(f_j)$
satisfy $z_{j+1}=\sigma_*z_j=0$ beyond the degree bound, so a nonzero
image has a last nonzero term $z_e$. The argument shows this terminal
class is a square $z_e=w^2$ whose primitive, Steenrod-annihilated root
still has nonzero suspension: at a positive terminal level the
preceding spherical suspension forces the root to have odd degree, and
at level zero fourth powers are excluded by spectrum pairings and
integral characteristic classes. The mapping cone of the next adjoint
then converts the square into a nonzero Steenrod-module extension
[S4:141–180].

**Weight and algebra obstruction.** At a positive level $n$, weight
counts the inputs of an extended power. The weight-$2^k$ primitives are
dual to $M_k(n)=\Sigma^n d_0^n D_k$, where $D_k$ is a binary Dickson
algebra with generator $d_0$ of degree $2^k-1$, and the bottom summand
is $M_0(n)=\Sigma^n\mathbb F_2$. The cone extension on a nonbottom weight, when
its detecting functional lifts from the preceding suspension level, is
possible only for $n=k=1$ in a power-of-two degree; Cartier halving and
an injection on even-degree Tor cycles retain the exponent-floor
information needed for this restriction [S4:141–180].

**Assembly.** At a positive terminal level the obstruction leaves only
the bottom weight, giving stable Hopf detection. At terminal level zero
it forces the root to have leading weight two, so the original class has
leading weight four; Kuhn's theorem bounds its Adams filtration by two
and Browder's identification gives Kervaire detection. Additivity of
the detecting invariants then yields the asserted span [S4:141–180].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Curtis's conjecture is one of the classical open problems about the
mod-2 stable Hurewicz image, recorded in the footnotes of May's 1977
survey. Adams's Hopf-invariant-one theorem identifies the three Hopf
classes; Browder's work relates the framed Kervaire invariant to the
classes $h_j^2$ in the mod-2 Adams spectral sequence; and
Hill--Hopkins--Ravenel's nonexistence theorem restricts the Kervaire
classes to $j\le6$, leaving dimension $126$ as the last possible
Kervaire dimension. The existence of the dimension-$126$ class is given
separately by Lin--Wang--Xu, and is an endpoint result distinct from the
upper bound used to make the positive image finite. Curtis's conjecture
had been known in low degrees and conjecturally in general; the present
proof closes the general case [S4:75–138].

## Consequences

**Curtis's conjecture is resolved.** In every positive degree the
mod-2 stable Hurewicz image is spanned over $\mathbb F_2$ by the Hopf
$\eta,\nu,\sigma$ images in degrees $1,3,7$ and the
Kervaire-invariant-one $\theta_j$ images in degrees $2^{j+1}-2$ whenever
they exist [S4:24–31].

**Eccles's conjecture holds for spheres.** For every $n>0$ each nonzero
mod-2 spherical class in $H_*(QS^n;\mathbb F_2)$ is the bottom class $e_n$ or a
nonzero suspension of a Hopf image; the alternatives are the bottom
stably spherical class and the Hopf-invariant-one classes
[S4:51–61].

**The positive image is finite.** It vanishes above degree $126$ and is
supported on the Hopf degrees $1,3,7$ and the Kervaire degrees
$2,6,14,30,62,126$; this is an upper bound, not an assertion of
nonvanishing in every listed degree [S4:74–82].

## Section skeleton

**Manuscript** [S3:8–14], 6 input sections in `build/`:
introduction [S4:24–31], weights, cones, powers, algebra, conclusion; plus
`preamble.tex`. One figure (`build/figures/proof-route.tex`). Its root
is `build/paper.tex`, with a `references.bib` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— a root `build/paper.tex`, one `preamble.tex`, six content `.tex`
files in `build/` (introduction, weights, cones, powers, algebra,
conclusion), one figure under `build/figures/`, and a `references.bib`
bibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 316 at line 7747. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 726. |
| S3 | [`preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/paper.tex`](../../../preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/paper.tex) | 30 | Manuscript main file: title and abstract. |
| S4 | [`preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/introduction.tex`](../../../preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/introduction.tex) | 216 | Introduction: the setup, the Curtis theorem, the two corollaries, the proof outline, and the conventions. |
| S5 | [`preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/references.bib`](../../../preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/references.bib) | 383 | Manuscript bibliography. |

## Bibliography

- Adams, J. F., On the non-existence of elements of Hopf invariant one (1960)
- Adams, J. F., On the cobar construction (1956)
- Adams, J. F., On the structure and applications of the Steenrod algebra (1958)
- Behrens, Mark, Hill, Michael A., Hopkins, Michael J., Mahowald, Mark, Detecting exotic spheres in low dimensions using coker J (2020)
- Browder, William, The Kervaire invariant of framed manifolds and its generalization (1969)
- Bruner, Robert R., May, J. Peter, McClure, James E., Steinberger, Mark, $H_\infty$ Ring Spectra and Their Applications (1986)
- Cartier, P., Une nouvelle opération sur les formes différentielles (1957)
- Cartier, Pierre, Questions de rationalité des diviseurs en géométrie algébrique (1958)
- Cohen, Frederick R., Lada, Thomas J., May, J. Peter, The Homology of Iterated Loop Spaces (1976)
- Curtis, Edward B., The Dyer–Lashof algebra and the $\Lambda$-algebra (1975)
- Dickson, Leonard Eugene, A fundamental system of invariants of the general modular linear group with a solution of the form problem (1911)
- Eccles, Peter J., Zare, Hadi, On the form of potential spherical classes in $H_*Q_0S^0$ (2009)
- Giambalvo, V., Peterson, F. P., $A$-generators for ideals in the Dickson algebra (2001)
- Hahn, Jeremy, Yuan, Allen, Multiplicative structure in the stable splitting of $\Omega SL_n(\mathbb C)$ (2019)
- Hill, Michael A., Hopkins, Michael J., Ravenel, Douglas C., On the nonexistence of elements of Kervaire invariant one (2016)
- Hung, Nguyen H. V., The action of the Steenrod squares on the modular invariants of linear groups (1991)
- Hung, Nguyen H. V., The cohomology of the Steenrod algebra and representations of the general linear groups (2005)
- Hung, Nguyen H. V., Peterson, Franklin P., Spherical classes and the Dickson algebra (1998)
- Hunter, Dana, The Curtis–Wellington spectral sequence through cohomology (2025)
- Kameko, M., Products of projective spaces as Steenrod modules (1990)
- Kuhn, Nicholas J., Localization of André–Quillen–Goodwillie towers, and the periodic homology of infinite loopspaces (2006)
- Kuhn, Nicholas J., Adams filtration and generalized Hurewicz maps for infinite loopspaces (2018)
- Kuhn, Nicholas J., Pereira, Luís Alexandre, Operad bimodules and composition products on André–Quillen filtrations of algebras (2017)
- Lin, Weinan, Wang, Guozhen, Xu, Zhouli, On the Last Kervaire Invariant Problem (2025)
- Madsen, Ib, On the action of the Dyer–Lashof algebra in $H_*(G)$ (1975)
- May, J. Peter, Infinite loop space theory (1977)
- Milnor, John, The Steenrod algebra and its dual (1958)
- Rivera, Manuel, Adams' cobar construction revisited (2022)
- Serre, Jean-Pierre, Cohomologie modulo 2 des complexes d'Eilenberg–MacLane (1953)
- Serre, Jean-Pierre, Homologie singuli\`ere des espaces fibrés. Applications (1951)
- Snaith, V. P., A stable decomposition of $\Omega^n S^n X$ (1974)
- Nguyen Sum, The action of the primitive Milnor operations on the Dickson invariants (2024)
- Wilkerson, C. W., A primer on the Dickson invariants (1983)
- Zare, Hadi, On Spherical Classes in $H_*QS^n$ (2009)
