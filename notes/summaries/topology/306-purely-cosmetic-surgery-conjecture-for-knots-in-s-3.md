[Notes](../../README.md) / [Summaries](../README.md) / [Topology](../../index/disciplines/topology.md) / [Family 306](../../index/topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md)

# 306 — The purely cosmetic surgery conjecture for knots in $S^3$

[Index page](../../index/topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md)

## Original CONTENTS.md summary

The release's blurb [S1:7562] and the catalog abstract [S2:706] state
the family's claim: the purely cosmetic surgery conjecture — distinct
Dehn surgery slopes on a nontrivial smooth knot in $S^3$ never produce
orientation-preservingly homeomorphic manifolds. The statement includes
the meridional slope. The manuscript's abstract "We prove the purely cosmetic surgery conjecture for knots in the three-sphere.
Distinct Dehn surgery slopes on a nontrivial smooth knot never give
orientation-preservingly homeomorphic manifolds. [S3:8–12]"

## Undergraduate summary

Dehn surgery is the standard operation by which one builds a closed
three-manifold from a knot: remove a tubular neighborhood of the knot
and glue it back so that the meridian is filled by a slope $r$ on the
boundary torus. Two fillings are called *purely cosmetic* if they are
homeomorphic by an orientation-preserving map, even though the slopes
$r$ and $s$ are distinct. The purely cosmetic surgery conjecture
predicts that this cannot happen for a nontrivial knot: the slope is
determined by the resulting closed manifold, up to orientation. In
other words, the knot's exterior encodes its filling slope in the
oriented manifold it produces [S4:3–11]:

> Let $K\subset S^3$ be a smooth nontrivial knot. For any
$r,s\in\Q\cup\{\infty\}$, an orientation-preserving homeomorphism
\[
 S^3_r(K)\cong S^3_s(K)
\]
implies $r=s$. [S4:13–20]

The orientation hypothesis is essential: orientation-reversing, or
*chirally* cosmetic, coincidences are a different phenomenon and the
conjecture does not address them [S4:22–27].

## Graduate summary

**The argument's two counts.** The proof is an analytic gauged
comparison of two moduli-counting constructions. The first is an
integer instanton count $\Omega\ne0$ on a closed parameterized
cobordism; the second is an oriented one-dimensional spinor count
whose boundary would force $2^\eta\Omega=0$. The work is to construct
the two counts with compatible metrics, incidence conditions,
determinant lifts, and orientations, so that the two are simultaneously
well-defined and the second's boundary contradicts the first's
nonvanishing [S4:107–216].

**The comparison strategy.** The comparison follows the
nonabelian-monopole cobordism strategy of Pidstrigach--Tyurin and
Okonek--Teleman, with the analytic and instanton-link development of
Feehan--Leness. The ordinary count uses instanton Floer and Donaldson
theory with determinant-one gauge transformations; the negative
direction requires an interval of metrics, a degree-two sphere test,
and a signed sum over two determinant lifts, with the two minimal
lens-wall contributions cancelling under the signs. Symplectic caps
seal the boundary of the cobordism [S4:107–216].

**The remaining case.** The conjecture is the cosmetic filling problem
of Gordon (Conjecture 6.1), recorded as Bleiler's Problem 1.81(A) in
Kirby's list. Gordon and Luecke's theorem that nontrivial surgery on a
nontrivial knot cannot produce $S^3$ settles the meridional case; the
remaining finite slopes had been narrowed by a sequence of obstructions
— Alexander polynomial (Boyer--Lines), Heegaard Floer (Ozsváth--Szabó,
Wang, Wu, Ni--Wu), immersed-curve restrictions (Hanselman), and
crossing- and census-based verification (Futer--Purcell--Schleimer) —
but none closed the general case [S4:31–103].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The cosmetic surgery problem is the three-dimensional analogue of the
question of how much of a filling slope is recoverable from the
resulting closed manifold. Gordon formulated it as the cosmetic
filling problem for knot exteriors, and Bleiler, Hodgson, and Weeks
developed the terminology and distinguished fillings related by a
symmetry of the exterior from those that are not. The meridional case
follows from Gordon and Luecke. Over the following decades a large
body of obstructions accumulated: the Alexander-polynomial method of
Boyer and Lines, the Heegaard Floer approach of Ozsváth--Szabó, Wang,
Wu, and Ni--Wu, the immersed-curve restrictions of Hanselman, the
Jones-polynomial and quantum obstructions of Ichihara--Wu and
Detcherry, and the positive results of Tao (cables and composites),
Stipsicz--Szabó (pretzels), and the equivariant version of
Kotelskiy--Lidman--Moore--Watson--Zibrowius. Futer, Purcell, and
Schleimer combined knot invariants, hyperbolic estimates, and
verified computations to establish the conjecture through 19
crossings and for the one-cusped SnapPy census [S4:31–103].

## Consequences

**The purely cosmetic surgery conjecture is true for knots in
$S^3$.** For any smooth nontrivial knot $K\subset S^3$ and any two
slopes $r,s\in\Q\cup\{\infty\}$, an orientation-preserving
homeomorphism $S^3_r(K)\cong S^3_s(K)$ implies $r=s$. The statement
includes the meridional slope and does not require the homeomorphism
to preserve a surgery core or the knot exterior [S4:13–20].

**The filling slope is an oriented-manifold invariant.** For the
exterior of a nontrivial smooth knot in $S^3$, the Dehn surgery slope
is determined by the oriented closed manifold it produces: no two
distinct slopes yield orientation-preservingly homeomorphic fillings
[S3:8–12].

## Section skeleton

**Manuscript** [S3:8–12], 10 sections under `build/sections/`:
01-introduction [S4:13–20], 02-ordinary, 03-negative, 04-caps, 05-stack,
06-geometry, 07-estimates, 08-indices, 09-analysis, 10-gluing. Plus
two figures under `build/figures/`. Its root is `build/main.tex`, with
a `preamble.tex` and a `references.bib` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— 10 `.tex` files in `build/sections/`, one in the root, one
`preamble.tex`, and two figures under `build/figures/` — and no
non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 306 at line 7562. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 706. |
| S3 | [`preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/main.tex`](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/main.tex) | 26 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/sections/01-introduction.tex) | 261 | Introduction: the setup, the main theorem, the remaining case, the argument, and the organization. |
| S5 | [`preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/references.bib`](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/references.bib) | 657 | Manuscript bibliography. |

## Bibliography

- Abreu, Miguel, {Kähler} geometry of toric varieties and extremal metrics (1998)
- Akbulut, Selman, Ozbagci, Burak, On the topology of compact Stein surfaces (2002)
- Aronszajn, Nachman, A unique continuation theorem for solutions of elliptic partial differential equations or inequalities of second order (1957)
- Atiyah, M. F., Singer, I. M., The index of elliptic operators. III (1968)
- Atiyah, M. F., Patodi, V. K., Singer, I. M., Spectral asymmetry and Riemannian geometry. I (1975)
- Auroux, Denis, Katzarkov, Ludmil, A degree doubling formula for braid monodromies and Lefschetz pencils (2008)
- Bleiler, Steven A., Hodgson, Craig D., Weeks, Jeffrey R., Cosmetic surgery on knots (1999)
- Boyer, Steven, Lines, Daniel, Surgery formulae for Casson's invariant and extensions to homology lens spaces (1990)
- Culler, Lucas, Daemi, Aliakbar, Xie, Yi, Surgery, polygons and $SU(N)$-Floer homology (2020)
- Daemi, Aliakbar, Lidman, Tye, Miller Eismeier, Mike, Filtered instanton homology and cosmetic surgery (2025)
- Detcherry, Renaud, A quantum obstruction for purely cosmetic surgeries (2026)
- Dolgachev, Igor, Weighted projective varieties (1982)
- Donaldson, S. K., Kronheimer, P. B., The Geometry of Four-Manifolds (1990)
- Donaldson, S. K., Floer Homology Groups in Yang–Mills Theory (2002)
- Donaldson, S. K., Lefschetz pencils on symplectic manifolds (1999)
- Eliashberg, Yakov M., Thurston, William P., Confoliations (1998)
- Eliashberg, Yakov, A few remarks about symplectic filling (2004)
- Feehan, Paul M. N., Leness, Thomas G., PU(2) monopoles. I: Regularity, Uhlenbeck compactness, and transversality (1998)
- Feehan, Paul M. N., Leness, Thomas G., PU(2) monopoles and links of top-level Seiberg–Witten moduli spaces (2001)
- Feehan, Paul M. N., Leness, Thomas G., PU(2) monopoles. II: Top-level Seiberg–Witten moduli spaces and Witten's conjecture in low degrees (2001)
- Fintushel, Ronald, Stern, Ronald J., Rational blowdowns of smooth 4-manifolds (1997)
- Floer, Andreas, An instanton-invariant for 3-manifolds (1988)
- Futer, David, Purcell, Jessica S., Schleimer, Saul, Excluding cosmetic surgeries on hyperbolic $3$-manifolds (2025)
- Gabai, David, Foliations and the topology of 3-manifolds. III (1987)
- Ghosh, Sudipta, Sivek, Steven, Zentner, Raphael, Rational homology 3-spheres and $\mathrm{SL}(2,\mathbb C)$ representations (2023)
- Giroux, Emmanuel, Géométrie de contact: de la dimension trois vers les dimensions supérieures (2002)
- Gordon, C. McA., Dehn surgery on knots (1991)
- Gordon, C. McA., Luecke, J., Knots are determined by their complements (1989)
- Gramain, André, Le type d'homotopie du groupe des difféomorphismes d'une surface compacte (1973)
- Guillemin, Victor, {Kähler} structures on toric varieties (1994)
- Hanselman, Jonathan, Heegaard Floer homology and cosmetic surgeries in $S^3$ (2023)
- Ichihara, Kazuhiro, Wu, Zhongtao, A note on Jones polynomial and cosmetic surgery (2019)
- Kawasaki, Tetsuro, The Riemann–Roch theorem for complex V-manifolds (1979)
- Kirby, Rob, Problems in low-dimensional topology (1997)
- Kotelskiy, Artem, Lidman, Tye, Moore, Allison H., Watson, Liam, Zibrowius, Claudius, Cosmetic operations and Khovanov multicurves (2024)
- Kronheimer, P. B., Mrowka, T. S., Witten's conjecture and Property P (2004)
- Kronheimer, P. B., Mrowka, T. S., Embedded surfaces and the structure of Donaldson's polynomial invariants (1995)
- Kronheimer, Peter, Mrowka, Tomasz, Knots, sutures, and excision (2010)
- Lockhart, Robert B., McOwen, Robert C., Elliptic differential operators on noncompact manifolds (1985)
- Massuyeau, Gwénaël, An introduction to the abelian Reidemeister torsion of three-dimensional manifolds (2011)
- Ni, Yi, Wu, Zhongtao, Cosmetic surgeries on knots in $S^3$ (2015)
- Okonek, Christian, Teleman, Andrei, Quaternionic monopoles (1996)
- Mu{\ n}oz, Vicente, Ring structure of the Floer cohomology of $\Sigma\times S^1$ (1999)
- Mu{\ n}oz, Vicente, Fukaya–Floer homology of $\Sigma\times S^1$ and applications (1999)
- Pidstrigach, Victor, Tyurin, Andrei, Localisation of the Donaldson's invariants along Seiberg–Witten classes (1995)
- Ren, Qiuyu, Cosmetic surgery on satellite knots (2025)
- Sivek, Steven, Donaldson invariants of symplectic manifolds (2015)
- Smale, Stephen, An infinite dimensional version of Sard's theorem (1965)
- Smith, Ivan, Lefschetz pencils and divisors in moduli space (2001)
- Stipsicz, András I., Szabó, Zoltán, Purely cosmetic surgeries and pretzel knots (2021)
- Tao, Ran, Cable knots do not admit cosmetic surgeries (2019)
- Tao, Ran, Knots admitting purely cosmetic surgeries are prime (2022)
- Taubes, Clifford Henry, More constraints on symplectic forms from Seiberg–Witten invariants (1995)
- Taylor, Michael E., Pseudodifferential Operators and Nonlinear PDE (1991)
- Ozsváth, Peter S., Szabó, Zoltán, Knot Floer homology and rational surgeries (2011)
- Uhlenbeck, Karen K., Connections with $L^p$ bounds on curvature (1982)
- Uhlenbeck, Karen K., Removable singularities in Yang–Mills fields (1982)
- Wang, Jiajun, Cosmetic surgeries on genus one knots (2006)
- Wu, Zhongtao, Cosmetic surgery in $L$-space homology spheres (2011)
