[Notes](../../README.md) / [Summaries](../README.md) / [Differential geometry](../../index/disciplines/differential-geometry.md) / [Family 338](../../index/differential-geometry/338-yaus-uniformization-conjecture.md)

# 338 — Yau's uniformization conjecture

[Index page](../../index/differential-geometry/338-yaus-uniformization-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:8240] and the catalog abstract [S2:774] state
the family's claim: every complete connected noncompact Kähler
manifold with strictly positive holomorphic bisectional curvature is
biholomorphic to complex Euclidean space, resolving Yau's
uniformization conjecture in every complex dimension. The manuscript's
abstract "We prove that every complete connected noncompact Kähler manifold with
strictly positive holomorphic bisectional curvature is biholomorphic to
complex Euclidean space. This resolves Yau's uniformization conjecture
positively in every complex dimension. [S3:84–89]"

## Undergraduate summary

In 1982 Yau asked whether a complete noncompact Kähler manifold with
positive holomorphic bisectional curvature must be biholomorphic to
complex Euclidean space. The one-dimensional case is classical: a
complete noncompact Riemann surface of positive Gaussian curvature is
conformally the plane. In higher dimensions, positive holomorphic
bisectional curvature implies positive real sectional curvature, and
various partial results connect curvature to conformal type, Steinness,
and algebraic embeddings, but each retains additional hypotheses —
bounded curvature, maximal volume growth, or topological
conditions. The manuscript proves the conjecture under pointwise
positivity alone, with no upper curvature bound, no volume-growth
condition, and no topological hypothesis [S4:1–23]:

> **Theorem 1.1**
Let $M$ be a connected noncompact complex manifold of complex dimension
$n\geq1$. If $M$ admits a smooth complete Kähler metric with strictly
positive holomorphic bisectional curvature, then $M$ is biholomorphic
to $\mathbb C^n$. [S4:8–13]

The conclusion identifies the entire complex manifold with $\C^n$; it
does not assert that the given metric is Euclidean.

## Graduate summary

**The Kähler–Ricci flow and scalar comparison.** The proof constructs
a global Kähler–Ricci flow $h_t$ by complete Hermitian approximations
on exhausting domains. Estimates for the metric and its logarithmic
volume loss $\rho(x,t)=\log(\det g/\det h_t)$ pass to the limit without
global curvature control. A spatial weight adapted to the nonnegative
form $g-h_t$ proves scalar comparison before completeness is known;
completeness is a later consequence of the Harnack inequality
[S4:146–224].

**The disc and ellipsoid arguments.** The curvature argument takes
place on the holomorphic cotangent bundle. The boundary squared dual
norm is minimized over holomorphic discs with compact boundary walls
and a vanishing area penalty. A quantitative deformation lemma gives a
viscosity inequality for the disc infimum; optimizing a Hermitian
ellipsoid in each fiber converts it into the scalar comparison. The
infimum equals the evolving squared dual norm, yielding joint
positivity in space and logarithmic time, hence the matrix and scalar
Harnack inequalities [S4:146–224].

**Chart contraction and the biholomorphism.** Three time parameters
drive the chart construction: physical time $t$ for the flow,
logarithmic time $\tau=\log t$ for Harnack estimates, and the volume
clock $s=\rho(o,t)$ for chart contraction. The volume clock measures
contraction directly: for the transition map from a centered unitary
chart at clock $s$ to one at $u\ge s$,
$|\det F_{s,u}'(0)|=e^{-(u-s)/2}$. Simple connectivity allows the local
inverse charts to continue coherently, and a plurisubharmonic Liouville
argument gives a contraction exponent valid on every fixed compact
set. Polynomial automorphisms with constant Jacobian normalize the
volume jets; inverse iteration makes the corrected inverse charts
converge to an injective holomorphic map $M\to\C^n$, and a forward
degree bound rules out a finite maximal radius in the image, proving
the map is onto [S4:146–224].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The one-dimensional case follows from Cohn–Vossen's topology theorem
and the parabolicity theorem of Blanc–Fiala–Huber. The compact analogue,
the Frankel conjecture, was resolved by Mori and by Siu–Yau: positive
holomorphic bisectional curvature characterizes complex projective
space. Greene–Wu showed that positive real sectional curvature yields
Steinness; Mok obtained an affine-algebraic embedding under positive
bisectional curvature with maximal volume growth and quadratic
scalar-curvature decay. Chen–Zhu proved intrinsic growth and
average-curvature estimates under pointwise positive bisectional
curvature. On the flow side, Cao's Harnack estimates for
Kähler–Ricci flow are an analytic antecedent; Chau–Tam established
uniformization under bounded nonnegative bisectional curvature and
maximal volume growth; Liu proved the same under nonnegative
bisectional curvature and maximal volume growth without an upper
curvature bound, using a Gromov–Hausdorff approach. Recent
surface-dimensional results by Datar, Pingali, and Seshadri, and by
Wu, remove some assumptions at infinity for complex surfaces. The
finite-mass approach of Datar, Pingali, and Seshadri and the
$m$-Hessian capacity of Dat extend the problem to higher dimensions
under additional hypotheses [S4:27–142].

## Consequences

**Yau's uniformization conjecture is resolved.** Every complete
connected noncompact Kähler manifold with strictly positive holomorphic
bisectional curvature is biholomorphic to $\C^n$, in every complex
dimension, under no upper curvature bound, volume-growth condition, or
topological hypothesis [S4:8–13].

**The manifold is Stein and contractible.** The pointwise positivity
hypothesis implies both properties as a consequence of the
biholomorphism to $\C^n$ [S4:15–23].

**A complete Kähler–Ricci flow with scalar comparison is constructed
without global curvature control.** The flow exists on all positive
time, and scalar comparison holds before completeness is established;
completeness follows from the Harnack inequality
[S4:146–224].

## Section skeleton

**Manuscript** [S3:84–89], 9 sections under `build/sections/`:
introduction [S4:8–13], preliminaries, flow, discs, variation, ellipsoids,
charts, dynamics, uniformization. No figures. Its root is
`build/main.tex`, with a `bibliography.tex` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — a root `build/main.tex`, 9 `.tex` files under
`build/sections/`, and a `bibliography.tex` bibliography; no figures
— and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 338 at line 8240. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 774. |
| S3 | [`preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/main.tex`](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/main.tex) | 101 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/sections/introduction.tex`](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/sections/introduction.tex) | 258 | Introduction: the main theorem, antecedents, the structure of the proof, and conventions. |
| S5 | [`preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/bibliography.tex`](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/bibliography.tex) | 424 | Manuscript bibliography. |

## Bibliography

- A. D. Aleksandrov, _Almost everywhere existence of the second differential of a convex function and some properties of convex surfaces connected with it_, Uchenye Zapiski Leningradskogo Gosudarstvennogo Universiteta, no. 37, Seriya Matematicheskikh Nauk **6** (1939), 3–35 (Russian).
- E. Andersén, _Volume-preserving automorphisms of $\mathbb C^n$_, Complex Variables Theory Appl. **14** (1990), nos. 1–4, 223–235. doi:10.1080/17476939008814422.
- The Stacks Project Authors, _The Stacks Project_, Lemma 10.51.4, ``Krull's intersection theorem,'' Tag 00IP.   (accessed September 23, 2026).
- M. Braverman, O. Milatovic, and M. A. Shubin, _Essential self-adjointness of Schrödinger-type operators on manifolds_, Russian Math. Surveys **57** (2002), no. 4, 641–692. doi:10.1070/RM2002v057n04ABEH000532; arXiv:math/0201231v3.
- H.-D. Cao, _On Harnack's inequalities for the Kähler–Ricci flow_, Invent. Math. **109** (1992), 247–263. doi:10.1007/BF01232027.
- J. Chu, _$C^{2,\alpha}$ regularities and estimates for nonlinear elliptic and parabolic equations in geometry_, Calc. Var. Partial Differential Equations **55** (2016), article 8. doi:10.1007/s00526-015-0948-5; arXiv:1410.3354v3.
- S. Cohn-Vossen, _Kürzeste Wege und Totalkrümmung auf Flächen_, Compositio Math. **2** (1935), 69–133.  .
- M. G. Crandall, H. Ishii, and P.-L. Lions, _User's guide to viscosity solutions of second order partial differential equations_, Bull. Amer. Math. Soc. (N.S.) **27** (1992), no. 1, 1–67. doi:10.1090/S0273-0979-1992-00266-5; arXiv:math/9207212v1.
- Truong Dinh Dat, _An $m$-Hessian approach to Yau uniformization conjecture_, preprint (2026), arXiv:2609.18171v1.
- Ved Datar, Vamsi Pritham Pingali, and Harish Seshadri, _Uniformisation of complete Kähler surfaces with positive sectional curvature_, preprint (2026), arXiv:2604.11220v1.
- Ved V. Datar, Vamsi Pritham Pingali, and Harish Seshadri, _The top Yau–Yang conjecture for Kähler manifolds with positive sectional curvature_, preprint (2026), arXiv:2606.19806v1.
- J.-P. Demailly, _Estimations $L^2$ pour l'opérateur $\bar\partial$ d'un fibré vectoriel holomorphe semi-positif au-dessus d'une variété kählérienne compl\`ete_, Ann. Sci. École Norm. Sup. (4) **15** (1982), no. 3, 457–511. doi:10.24033/asens.1434.
- J.-P. Demailly, _Complex Analytic and Differential Geometry_, Open Content Book, version of June 21, 2012.  .
- L. C. Evans, _Partial Differential Equations_, second edition, Graduate Studies in Mathematics, vol. 19, American Mathematical Society, Providence, RI, 2010.
- M. Gromov, _Curvature, diameter and Betti numbers_, Comment. Math. Helv. **56** (1981), 179–195. doi:10.1007/BF02566208.
- A. Huber, _On subharmonic functions and differential geometry in the large_, Comment. Math. Helv. **32** (1957/58), 13–72. doi:10.1007/BF02564570.
- L. Hörmander, _$L^2$ estimates and existence theorems for the $\bar\partial$ operator_, Acta Math. **113** (1965), 89–152. doi:10.1007/BF02391775.
- F. John, _Extremum problems with inequalities as subsidiary conditions_, in _Studies and Essays Presented to R. Courant on his 60th Birthday, January 8, 1948_, Interscience, New York, 1948, pp. 187–204. Publisher's later reprint.
- B. L. Kotschwar, _A local version of Bando's theorem on the real-analyticity of solutions to the Ricci flow_, Bull. Lond. Math. Soc. **45** (2013), no. 1, 153–158. doi:10.1112/blms/bds074; arXiv:1111.0355v1.
- O. A. Ladyzhenskaya, V. A. Solonnikov, and N. N. Ural'tseva, _Linear and Quasi-linear Equations of Parabolic Type_, translated by S. Smith, Translations of Mathematical Monographs, vol. 23, American Mathematical Society, Providence, RI, 1968; reprinted with corrections, 1988.
- G. Liu, _Three circle theorems on Kähler manifolds and applications_, preprint (2013; version 3, 2014), arXiv:1308.0710v3. The cited plurisubharmonic Liouville theorem is Theorem 9 of this version.
- G. Liu, _On Yau's uniformization conjecture_, Camb. J. Math. **7** (2019), nos. 1–2, 33–70. doi:10.4310/CJM.2019.v7.n1.a2; arXiv:1606.08958v2.
- F. Forstnerič and F. Lárusson, _Oka properties of groups of holomorphic and algebraic automorphisms of complex affine space_, Math. Res. Lett. **21** (2014), no. 5, 1047–1067. doi:10.4310/MRL.2014.v21.n5.a7; arXiv:1402.4342v3.
- N. Wiener and P. Masani, _The prediction theory of multivariate stochastic processes. I. The regularity condition_, Acta Math. **98** (1957), 111–150. doi:10.1007/BF02404472.
- N. Mok, _An embedding theorem of complete Kähler manifolds of positive bisectional curvature onto affine algebraic varieties_, Bull. Soc. Math. France **112** (1984), 197–258. doi:10.24033/bsmf.2005.
- S. Mori, _Projective manifolds with ample tangent bundles_, Ann. of Math. (2) **110** (1979), no. 3, 593–606. doi:10.2307/1971241.
- A. McIntosh and A. J. Morris, _Finite propagation speed for first order systems and Huygens' principle for hyperbolic equations_, Proc. Amer. Math. Soc. **141** (2013), no. 10, 3515–3527. doi:10.1090/S0002-9939-2013-11661-8; arXiv:1201.1818v2.
- A. Newlander and L. Nirenberg, _Complex analytic coordinates in almost complex manifolds_, Ann. of Math. (2) **65** (1957), no. 3, 391–404. doi:10.2307/1970051.
- E. A. Poletsky, _Plurisubharmonic functions as solutions of variational problems_, in _Several Complex Variables and Complex Geometry_, Part 1 (Santa Cruz, CA, 1989), Proc. Sympos. Pure Math., vol. 52, Part 1, American Mathematical Society, Providence, RI, 1991, pp. 163–171. doi:10.1090/pspum/052.1/1128523.
- R. Richberg, _Stetige streng pseudokonvexe Funktionen_, Math. Ann. **175** (1968), 257–286. doi:10.1007/BF02063212.
- B. Berndtsson and J.-P. Rosay, _Quasi-isometric vector bundles and bounded factorization of holomorphic matrices_, Ann. Inst. Fourier (Grenoble) **53** (2003), no. 3, 885–901. doi:10.5802/aif.1964.
- J.-P. Rosay, _Poletsky theory of disks on holomorphic manifolds_, Indiana Univ. Math. J. **52** (2003), no. 1, 157–170. doi:10.1512/iumj.2003.52.2170.
- J.-P. Rosay and W. Rudin, _Holomorphic maps from $\mathbb C^n$ to $\mathbb C^n$_, Trans. Amer. Math. Soc. **310** (1988), no. 1, 47–86. doi:10.2307/2001110.
- P. Li and R. Schoen, _$L^p$ and mean value properties of subharmonic functions on Riemannian manifolds_, Acta Math. **153** (1984), 279–301. doi:10.1007/BF02392380.
- W.-X. Shi, _Deforming the metric on complete Riemannian manifolds_, J. Differential Geom. **30** (1989), no. 1, 223–301. doi:10.4310/jdg/1214443292.
- Yuang Shi, _Minimal degrees, volume growth, and curvature decay on complete Kähler manifolds_, Int. Math. Res. Not. IMRN **2026**, article rnag080; arXiv:2511.01263v3.
- F. Lárusson and R. Sigurdsson, _Plurisubharmonicity of envelopes of disc functionals on manifolds_, J. reine angew. Math. **555** (2003), 27–38. doi:10.1515/crll.2003.013; arXiv:math/0111251v2.
- T. Coulhon and A. Sikora, _Gaussian heat kernel upper bounds via the Phragmén–Lindelöf theorem_, Proc. Lond. Math. Soc. (3) **96** (2008), no. 2, 507–544. doi:10.1112/plms/pdm050; arXiv:math/0609429v1.
- A. Chau and L.-F. Tam, _On the complex structure of Kähler manifolds with nonnegative curvature_, J. Differential Geom. **73** (2006), no. 3, 491–530. doi:10.4310/jdg/1146169936; arXiv:math/0504422v3.
- A. Chau and L.-F. Tam, _On the simply connectedness of nonnegatively curved Kähler manifolds and applications_, Trans. Amer. Math. Soc. **363** (2011), no. 12, 6291–6308. doi:10.1090/S0002-9947-2011-05223-2; arXiv:0806.2457v1.
- A. Chau and L.-F. Tam, _On the Steinness of a class of Kähler manifolds_, J. Differential Geom. **79** (2008), no. 2, 167–183. doi:10.4310/jdg/1211512638; arXiv:math/0610535v2.
- M.-C. Lee and L.-F. Tam, _Chern–Ricci flows on noncompact complex manifolds_, J. Differential Geom. **115** (2020), no. 3, 529–564. doi:10.4310/jdg/1594260018; arXiv:1708.00141v2.
- L. Ni and L.-F. Tam, _Poincaré–Lelong equation via the Hodge–Laplace heat equation_, Compos. Math. **149** (2013), 1856–1870. doi:10.1112/S0010437X12000322; arXiv:1109.6102v2.
- L. Ni and L.-F. Tam, _Plurisubharmonic functions and the structure of complete Kähler manifolds with nonnegative curvature_, J. Differential Geom. **64** (2003), no. 3, 457–524. doi:10.4310/jdg/1090427001; arXiv:math/0304096v1.
- C. D. Hill and M. Taylor, _Integrability of rough almost complex structures_, J. Geom. Anal. **13** (2003), no. 1, 163–172. doi:10.1007/BF02931002; arXiv:0710.2310v2.
- G. Teschl, _Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators_, Graduate Studies in Mathematics, vol. 99, American Mathematical Society, Providence, RI, 2009. Author's first-edition PDF, version 12 February 2009.
- D. Gilbarg and N. S. Trudinger, _Elliptic Partial Differential Equations of Second Order_, second edition, reprint of the 1998 edition, Classics in Mathematics, Springer-Verlag, Berlin, 2001. doi:10.1007/978-3-642-61798-0.
- S. Bera and K. Verma, _Uniform non-autonomous basins of attraction_, Invent. Math. **238** (2024), 995–1040. doi:10.1007/s00222-024-01295-9; arXiv:2211.15169v4.
- R. E. Greene and H. Wu, _$C^\infty$ approximations of convex, subharmonic, and plurisubharmonic functions_, Ann. Sci. École Norm. Sup. (4) **12** (1979), no. 1, 47–84. doi:10.24033/asens.1361.
- R. E. Greene and H. Wu, _$C^\infty$ convex functions and manifolds of positive curvature_, Acta Math. **137** (1976), 209–245. doi:10.1007/BF02392418.
- Jingcao Wu, _Conditional uniformization of Kähler surfaces_, preprint (2026), arXiv:2609.18506v1.
- P. Li and S.-T. Yau, _On the parabolic kernel of the Schrödinger operator_, Acta Math. **156** (1986), 153–201. doi:10.1007/BF02399203.
- Y.-T. Siu and S.-T. Yau, _Compact Kähler manifolds of positive bisectional curvature_, Invent. Math. **59** (1980), no. 2, 189–204. doi:10.1007/BF01390043.
- S.-T. Yau, _Survey on partial differential equations in differential geometry_, in _Seminar on Differential Geometry_ (S.-T. Yau, ed.), Ann. of Math. Stud., vol. 102, Princeton University Press, Princeton, NJ, and University of Tokyo Press, Tokyo, 1982, pp. 3–71. doi:10.1515/9781400881918-002 (digital reprint).
- P. Souplet and Q. S. Zhang, _Sharp gradient estimate and Yau's Liouville theorem for the heat equation on noncompact manifolds_, Bull. London Math. Soc. **38** (2006), no. 6, 1045–1053. doi:10.1112/S0024609306018947; arXiv:math/0502079v1.
- B.-L. Chen and X.-P. Zhu, _Volume growth and curvature decay of positively curved Kähler manifolds_, Pure Appl. Math. Q. **1** (2005), no. 1, 68–108. doi:10.4310/PAMQ.2005.v1.n1.a4; arXiv:math/0211374v1.
- B.-L. Chen and X.-P. Zhu, _Positively curved complete noncompact Kähler manifolds_, Acta Math. Sci. Ser. B (Engl. Ed.) **29** (2009), no. 4, 829–845. doi:10.1016/S0252-9602(09)60073-4; arXiv:math/0211373v1.
