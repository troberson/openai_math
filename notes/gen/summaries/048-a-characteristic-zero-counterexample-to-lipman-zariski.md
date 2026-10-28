[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 048](../index/algebraic-and-complex-geometry/048-a-characteristic-zero-counterexample-to-lipman-zariski.md)

# 048 — A characteristic-zero counterexample to Lipman–Zariski

[Index page](../index/algebraic-and-complex-geometry/048-a-characteristic-zero-counterexample-to-lipman-zariski.md)

## Original CONTENTS.md summary

The release's blurb "**048. A characteristic-zero counterexample to Lipman–Zariski.** Constructs a singular normal affine complex surface with free rank-two tangent sheaf, disproving the characteristic-zero Lipman–Zariski conjecture. [S1:1274]" The manuscript title is
"A singular normal affine surface with free tangent sheaf [S3:1]" , and its abstract reads: "We construct a singular normal affine complex surface whose tangent
sheaf is free of rank two. This disproves the Lipman–Zariski conjecture
in characteristic zero. [S5:2–4]"

## Undergraduate summary

For a finitely generated integral $\mathbb C$-algebra $A$, the derivation
module $\mathrm{Der}_{\mathbb C}(A)=\mathrm{Hom}_A(\Omega^1_{A/\mathbb C},A)$ is the module of
algebraic vector fields on $\mathrm{Spec} A$. On a smooth variety of dimension
$d$ it is locally free of rank $d$. The Lipman–Zariski conjecture asks
for the converse: a complex algebraic variety with locally free tangent
sheaf should be nonsingular . "For a finitely generated integral $\mathbb C$-algebra $A$, write
$$\mathrm{Der}_{\mathbb C}(A)=\mathrm{Hom}_A(\Omega^1_{A/\mathbb C},A).$$
The module $\mathrm{Der}_{\mathbb C}(A)$ consists of the algebraic vector fields on
$\mathrm{Spec} A$. On a smooth variety of dimension $d$, the tangent sheaf is
locally free of rank $d$. The Lipman–Zariski conjecture asks for the
converse: a complex algebraic variety with locally free tangent sheaf
should be nonsingular. In affine terms, it asserts that local freeness
of $\mathrm{Der}_{\mathbb C}(A)$ forces $A$ to be regular. We prove the following. [S5:9–18]" The theorem 

> **theorem**
There exist a finitely generated normal integral $\mathbb C$-algebra $A$ of Krull dimension two and a maximal ideal $\mathfrak m\subset A$ such that
$$\mathrm{Der}_{\mathbb C}(A)\simeq A^{\oplus2},
\qquad A_{\mathfrak m}\text{ is not regular}.$$ [S5:20–26]

Freeness holds on the entire affine surface, which is smooth away from
the marked point [S5:28–31]. The construction first produces an
isolated Gorenstein analytic surface singularity; the passage to
algebraic geometry preserves its completed local ring, from which
tangent freeness descends.

## Graduate summary

**Beyond the known positive criteria.** The analytic singularity has
one exceptional curve of genus $21$ and self-intersection $-10$, with
canonical discrepancy $-5$ and $p_g\ge33$, so $p_g-g-b\ge12$ 

> The analytic singularity constructed here has one exceptional curve of genus $21$
and self-intersection $-10$. Its canonical discrepancy is $-5$, and
$p_g\ge33$, so $p_g-g-b\ge12$. Remark 
proves these calculations. They place the analytic example beyond the
log-canonical and geometric-genus criteria just described. [S5:83–87]

This places the example beyond the log-canonical criteria of
Druel and Graf–Kovács and beyond Graf's geometric-genus and
Bergner–Graf criteria.

**The neighborhood and the vector fields.** Starting from a split
line bundle $L$ with $L^{\otimes4}\simeq K_C$, the zero-section
neighborhood carries the meromorphic two-form
$\sigma=t^{-5}\,dt\wedge dz$ . "Let $C$ be a smooth curve and $L$ a positive line bundle with
$L^{\otimes4}\simeq K_C$. Its dual bundle $L^{-1}$ provides the initial
neighborhood of $C$. In compatible base and fiber coordinates $(z,t)$,
that neighborhood carries the meromorphic two-form
$$\sigma=t^{-5}\,dt\wedge dz.$$
We seek two vector fields of the form
$$v_i=t\bigl(A_i(t,z)t\partial_t+B_i(t,z)\partial_z\bigr),
\qquad i=1,2,$$ [S5:131–142]" Two vector fields
are sought with $\sigma(v_1,v_2)=1+O(t)$. The leading vertical
coefficients are a pair of sections of $L$ with six simple common
zeros, whose corrections must satisfy global residue constraints.

**The curve and residue data.** $C$ is constructed on
$\mathbb P^1\times\mathbb P^1$ with fourth-order contact at the marked divisor $Z$
with an auxiliary elliptic curve $\Gamma$; a two-torsion relation
controls the section dimensions and supplies six vectors, giving
genus $21$ and $\deg L=10$ . "\paragraphA curve and normalized residues.
Section constructs $C$ on $\mathbb P^1\times\mathbb P^1$, with
fourth-order contact at $Z$ with an auxiliary elliptic curve $\Gamma$.
A two-torsion relation on $\Gamma$ controls the section dimensions on $C$ and supplies
six vectors in a two-dimensional quadratic space. The resulting curve
has genus $21$, and $\deg L=10$. [S5:151–156]" A trace pairing for
a degree-four map $C\to\mathbb P^1$ transports the vectors, and residue
duality fixes a meromorphic pair $P$ whose local expansions enforce the
determinant condition and cancel the gluing obstructions.

**Lifting and contraction.** The finite transition maps realize a
Hausdorff neighborhood $Y$ of $C$; Grauert's criterion contracts $C$
to a point $x$ of a normal surface $X$ 

> \paragraphHolomorphic lifting and contraction.
Section realizes the finite transition maps as
a Hausdorff surface neighborhood $Y$ of $C$. Set
$\mathcal I=\mathcal O_Y(-C)$ and $\mathcal F=\mathcal T_Y(-\log C)$, the sheaf of vector fields
tangent to $C$. Grauert's criterion contracts the curve to a point
$x$ of a normal surface $X$ . Cohomology of the
successive ideal quotients and the theorem on formal
functions give the cohomological vanishing needed to
lift these jets to holomorphic fields after shrinking, without requiring
an infinite sequence of neighborhood
changes to converge. Their determinant gives a frame on
$Y\setminus C\simeq X\setminus\{x\}$, which normality extends to a
free tangent sheaf on $X$. Adjunction proves that $x$ is singular. [S5:179–191]

The jets lift to holomorphic fields via cohomological vanishing and
the theorem on formal functions. Their determinant frames the punctured
surface, which normality extends to a free tangent sheaf on $X$;
adjunction proves $x$ is singular.

**The algebraic endpoint.** A finite-determinacy argument with a
relation matrix produces an algebraic local ring with the same
completion as $\mathcal O_{X,x}$ 

> \paragraphThe affine algebraic endpoint.
Section combines approximation with the finite
determinacy of equations together with their relations. The latter
method appears in Hironaka's equivalence theorem
\cite[\S3, Theorem 3.3]Hironaka1969 and in Artin's algebraization
of isolated singularities \cite[Theorems 1.10 and 3.8–3.9]Artin1969.
We prove the required finite-determinacy statement with a relation matrix:
the approximated equations and matrix retain their exact zero product.
This produces an algebraic local ring with the same completion as
$\mathcal O_{X,x}$. A finite Jacobian presentation identifies its completed
derivation module with the continuous derivations of that completion.
Faithful flatness descends freeness and the local ring properties.
Finally, shrinking to one affine neighborhood gives the globally free
module in Theorem , while preserving the singular point. [S5:193–206]

Faithful flatness descends freeness, and shrinking to one affine
neighborhood gives the globally free module while preserving the
singular point.

## History of the conjecture

Lipman showed that local freeness of the tangent sheaf forces
normality, so the conjecture asks whether it excludes the remaining
normal singularities. In positive characteristic the assertion fails
even for the hypersurface $xy-z^p=0$ [S5:35–43]. Hochster proved the
positively-graded cone case; Van Straten–Steenbrink the
isolated-singularity case in dimension at least three; Scheja–Storch
the hypersurface case; Källström the locally complete-intersection
case; Greb–Kebekus–Kovács–Peternell the klt case; Druel and
Graf–Kovács the log-canonical case [S5:45–71].

For normal complex surfaces, Graf proved smoothness for
$p_g\le1$ and for $p_g=2$ with a non-tree exceptional divisor;
Bergner–Graf gave the $p_g-g-b\le2$ criterion [S5:73–82].
"where $g$ is the sum of the genera of the exceptional curves and $b$ is
the first Betti number of the resolution's dual graph
\cite[Theorem 1]BergnerGraf2020.
The analytic singularity constructed here has one exceptional curve of genus $21$ [S5:73–82]" The construction here exceeds every one of these bounds.
Biswas–Gurjar–Kolte require logarithmic Kodaira dimension at most one
on the smooth locus, so this affine surface's smooth locus has
logarithmic Kodaira dimension two [S5:89–97].

## Consequences

**The characteristic-zero Lipman–Zariski conjecture is false.** There
exists a singular normal affine complex surface with free rank-two
tangent sheaf [S5:20–26]. No tangent frame near the singular point can
be chosen commuting, by Jörsdörfer's result [S5:71].

**The derivation-blowup question is negative.** A singular variety
with free tangent sheaf cannot be resolved by iterating the blowup at
the module of derivations; every step is the identity, and inserting
normalization does not change this for the normal surface [S5:103–111].

**Logarithmic Kodaira dimension two.** The smooth locus of the affine
surface has logarithmic Kodaira dimension two, outside the
Biswas–Gurjar–Kolte positive case [S5:89–97].

## Section skeleton

**Main file** [S4], 6 sections (numbered files) plus bibliography:

1. Introduction [S5]
2. The curve [S6]
3. The trace pairing and residue data [S7]
4. The finite vector-field jets [S8]
5. Holomorphic lifting and contraction [S9]
6. The affine algebraic endpoint [S10]

Bibliography: `bibliography.tex` [S11].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
6 section `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 048 at line 1274. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 172. |
| S3 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/README.md`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/README.md) | 18 | Manuscript readme: title, author, date. |
| S4 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/paper.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/paper.tex) | 80 | The main file: inputs and bibliography. |
| S5 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/01-introduction.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/01-introduction.tex) | 238 | The abstract, the theorem, the context, and the proof structure. |
| S6 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/02-curve.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/02-curve.tex) | 440 | The genus-21 curve and the auxiliary elliptic curve. |
| S7 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/03-trace.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/03-trace.tex) | 545 | The trace pairing and normalized residue data. |
| S8 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/04-jets.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/04-jets.tex) | 606 | The finite vector-field jets. |
| S9 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/05-analytic.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/05-analytic.tex) | 425 | Holomorphic lifting and Grauert contraction. |
| S10 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/06-algebraization.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/06-algebraization.tex) | 508 | The affine algebraic endpoint. |
| S11 | [`preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/bibliography.tex`](../../../preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/build/bibliography.tex) | 221 | The bibliography. |

## Bibliography

- M. Artin, _Algebraic approximation of structures over complete local rings_, Publ. Math. IHÉS **36** (1969), 23–58. doi:10.1007/BF02684596.
- The Stacks Project Authors, _The Stacks Project_, Tag 00IN (Artin–Rees), Tag 00MA (exactness on finite modules), Tag 00MC (faithful flatness of completion), Tag 07NV (dimension and completion), Tag 07NY (regularity and completion), and Tag 0C23 (normality of completion). Accessed 23 September 2026.
- The Stacks Project Authors, _The Stacks Project_, Tag 07QY (approximation over henselian local G-rings) and Tag 07QZ (approximation in pointed étale neighborhoods). Accessed 23 September 2026.
- The Stacks Project Authors, _The Stacks Project_, Tag 04GN (construction of henselization), Tag 06LJ (completion of a henselization), and Tag 0A1W (algebraic elements of a completion). Accessed 23 September 2026.
- P. Barajas, E. Chávez-Martínez and A. Romano-Velázquez, _The blow-up of a singularity at the module of derivations_, 2026. arXiv:2510.07607v2.
- I. Biswas, R. V. Gurjar and S. U. Kolte, _On the Zariski–Lipman conjecture for normal algebraic surfaces_, J. Lond. Math. Soc. **90** (2014), no. 1, 270–286. doi:10.1112/jlms/jdu021; arXiv:1403.5613v1.
- H. Cartan, _Faisceaux analytiques sur les variétés de Stein_, Séminaire Henri Cartan **4** (1951–1952), exposé 18, 1–10. Numdam.
- S. D. Cutkosky, _Étoiles and valuations_, J. Pure Appl. Algebra **221** (2017), no. 3, 588–610. doi:10.1016/j.jpaa.2016.07.007.
- J.-P. Demailly, _Complex Analytic and Differential Geometry_, author's lecture notes, version of 21 June 2012. Author's text.
- S. Druel, _The Zariski–Lipman conjecture for log canonical spaces_, Bull. Lond. Math. Soc. **46** (2014), no. 4, 827–835. doi:10.1112/blms/bdu040.
- H. Bergner and P. Graf, _The Lipman–Zariski conjecture in genus one higher_, Forum Math. Sigma **8** (2020), e21, 16 pp. doi:10.1017/fms.2020.19.
- P. Graf, _The Lipman–Zariski conjecture in low genus_, Int. Math. Res. Not. **2021** (2021), no. 1, 426–441. doi:10.1093/imrn/rnz154; arXiv:1801.05753v2.
- P. Graf, _The violation of the Lipman–Zariski conjecture in positive characteristic_, J. Algebra **601** (2022), 115–128. doi:10.1016/j.jalgebra.2022.03.004; arXiv:2201.06646v2.
- H. Grauert, _Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen_, Publ. Math. IHÉS **5** (1960), 5–64. doi:10.1007/BF02684746; correction, Publ. Math. IHÉS **16** (1963), 35–36, doi:10.1007/BF02684291.
- H. Grauert, _Über Modifikationen und exzeptionelle analytische Mengen_, Math. Ann. **146** (1962), 331–368. doi:10.1007/BF01441136.
- D. Greb, S. Kebekus, S. J. Kovács and T. Peternell, _Differential forms on log canonical spaces_, Publ. Math. IHÉS **114** (2011), 87–169. doi:10.1007/s10240-011-0036-0.
- A. Grothendieck, _Sur la classification des fibrés holomorphes sur la sph\`ere de Riemann_, Amer. J. Math. **79** (1957), 121–138. doi:10.2307/2372388.
- R. Hartshorne, _Residues and Duality_, Lecture Notes in Mathematics, vol. 20, Springer-Verlag, Berlin, 1966. doi:10.1007/BFb0080482.
- R. Hartshorne, _Algebraic Geometry_, Graduate Texts in Mathematics, vol. 52, Springer-Verlag, New York, 1977. doi:10.1007/978-1-4757-3849-0.
- H. Hironaka, _Formal line bundles along exceptional loci_, in _Algebraic Geometry_ (Papers presented at the Bombay Colloquium, 1968), Tata Inst. Fund. Res. Stud. Math., vol. 4, Oxford University Press, London, 1969, 201–218. TIFR text.
- M. Hochster, _The Zariski–Lipman conjecture in the graded case_, J. Algebra **47** (1977), no. 2, 411–424. doi:10.1016/0021-8693(77)90232-0.
- C. Jörder, _A weak version of the Lipman–Zariski conjecture_, Math. Z. **278** (2014), 893–899. doi:10.1007/s00209-014-1337-z; arXiv:1311.5141v1.
- P. Graf and S. J. Kovács, _An optimal extension theorem for 1-forms and the Lipman–Zariski conjecture_, Doc. Math. **19** (2014), 815–830. doi:10.4171/DM/465.
- R. Källström, _The Zariski–Lipman conjecture for complete intersections_, J. Algebra **337** (2011), no. 1, 169–180. doi:10.1016/j.jalgebra.2011.05.003. Corrected version: arXiv:1003.4241v6, 2018.
- J. Lipman, _Free derivation modules on algebraic varieties_, Amer. J. Math. **87** (1965), no. 4, 874–898. doi:10.2307/2373252.
- H. Grauert and R. Remmert, _Coherent Analytic Sheaves_, Grundlehren der mathematischen Wissenschaften, vol. 265, Springer-Verlag, Berlin, 1984. doi:10.1007/978-3-642-69582-7.
- J.-P. Serre, _Un théor\`eme de dualité_, Comment. Math. Helv. **29** (1955), 9–26. doi:10.1007/BF02564268.
- J.-P. Serre, _Géométrie algébrique et géométrie analytique_, Ann. Inst. Fourier **6** (1956), 1–42. doi:10.5802/aif.59.
- D. van Straten and J. Steenbrink, _Extendability of holomorphic differential forms near isolated hypersurface singularities_, Abh. Math. Sem. Univ. Hamburg **55** (1985), 97–110. doi:10.1007/BF02941491.
- G. Scheja and U. Storch, _Differentielle Eigenschaften der Lokalisierungen analytischer Algebren_, Math. Ann. **197** (1972), 137–170. doi:10.1007/BF01419591.
- H. Flenner and M. Zaidenberg, _Rational curves and rational singularities_, 2001. arXiv:math/0109221v1.
