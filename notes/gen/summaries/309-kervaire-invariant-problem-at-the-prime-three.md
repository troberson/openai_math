[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 309](../index/topology/309-kervaire-invariant-problem-at-the-prime-three.md)

# 309 — The Kervaire invariant problem at the prime three

[Index page](../index/topology/309-kervaire-invariant-problem-at-the-prime-three.md)

## Original CONTENTS.md summary

The release's blurb [S1:7628] and the catalog abstract [S2:712] state
the family's claim: the Kervaire invariant problem is solved at the
prime three for the standard Kervaire classes in the mod-three Adams
spectral sequence. The classes survive precisely at indices $`0`$, $`2`$,
and $`3`$, each surviving detection coset carries an element of additive
order three, and there is an order-three Kervaire element in stem
$`322`$. The manuscript's abstract "We solve the Kervaire invariant problem at the prime three for the standard Kervaire classes in the mod-three Adams spectral sequence. These classes survive precisely at indices $`0`$, $`2`$, and $`3`$, and each surviving detection coset contains an element of additive order three. In particular, there is an order-three Kervaire element in stem $`322`$. [S4:1–3]"

## Undergraduate summary

The Kervaire invariant problem asks which elements of the stable
homotopy groups of spheres carry a nontrivial Kervaire invariant, a
secondary invariant defined on a certain family of classes (the
"standard Kervaire classes") that are candidates for being the
bounding classes of framed manifolds. For each prime $`p`$ and each
admissible index one has a candidate class, and the question is which
of these candidates persist — "survive" — as genuine elements of the
stable stem, and what their additive order is. The mod-$`p`$ Adams
spectral sequence is the standard computational tool: a class survives
if it reaches the appropriate page undestroyed by a differential. The
manuscript resolves this at $`p=3`$ [S4:7–22]:

> **theorem**
At the prime three,
$$K=K_3=\{0,2,3\}.$$
Thus the surviving classes occur in stems $`10`$, $`106`$, and $`322`$, and each admits an additive-order-three representative. The class $`b_1`$ and every $`b_j`$ with $`j\geq4`$ fail to survive. [S4:24–30]

The answer is that at the prime three the surviving indices are
exactly $`\{0,2,3\}`$, so the classes land in stems $`10`$, $`106`$, and
$`322`$, each with an additive-order-three representative, and the
class $`b_1`$ together with every $`b_j`$ for $`j\ge4`$ dies.

## Graduate summary

**The two-branch proof structure.** The argument splits into a
nonexistence branch and a construction branch. The nonexistence
branch excludes every index $`j\ge4`$ using a height-six Morava
$`E`$-theory "detector": it builds $`C_9`$ and $`C_3`$ group actions whose
Euler-class bounds force outgoing differentials in the relevant Adams
$`E_2`$-page, so those candidates cannot survive. The construction
branch produces the stem-$`322`$ class from the already-known
additive-order-three stem-$`106`$ class by a truncated extended cube of
a Moore-spectrum map, which is what supplies the genuinely new
order-three element. The two branches together pin down the surviving
set at $`\{0,2,3\}`$ [S4:93–125].

**The unstable consequences.** The classification has concrete
unstable payoffs: the stems $`10`$, $`106`$, and $`322`$ each admit an
additive-order-three Kervaire element, and the death of $`b_1`$ and all
$`b_j`$ for $`j\ge4`$ removes candidate elements in the higher stems that
earlier incomplete computations left undetermined. The stem-$`322`$
element is the farthest-reaching new object the paper establishes
[S4:36–71].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The Kervaire invariant problem is one of the classical open problems
of stable homotopy theory. The $`2`$-primary and general even-prime
cases were settled by the work of Kochman, Woll, and
Kono--Stoll, and the odd-prime picture had been approached through
the Adams and Adams--Novikov spectral sequences. At the prime three
the surviving-index question resisted resolution because the height-six
Morava $`E`$-theory input needed to force the high-index differentials
was not previously available in the required form. The manuscript's
prior-work section records that the known order-three stem-$`106`$
class was the only surviving low-order candidate, and that the
prime-three obstruction to the higher indices was the missing piece
[S4:75–89].

## Consequences

**The Kervaire invariant problem is solved at the prime three.** For
the standard Kervaire classes in the mod-three Adams spectral
sequence, the surviving indices are exactly $`\{0,2,3\}`$; the classes
occur in stems $`10`$, $`106`$, and $`322`$; and each admits an
additive-order-three representative [S4:24–30].

**A new order-three Kervaire element in stem $`322`$.** In particular
there exists an order-three Kervaire element in stem $`322`$,
constructed from the known order-three stem-$`106`$ class via a
truncated extended cube of a Moore-spectrum map [S4:1–3].

**The higher-index candidates die.** The class $`b_1`$ and every $`b_j`$
with $`j\ge4`$ fail to survive at the prime three, so those stems carry
no Kervaire element [S4:24–30].

## Section skeleton

**Manuscript** [S3], 8 sections under `build/sections/`:
introduction [S4], detector, coefficients, subgroup, ascent, cube,
finite, and recurrence (the appendix). Plus one figure
(`build/figures/ascent-forcing.tex`). Its root is `build/paper.tex`,
with a `pdf-glyphs.tex` and a `references.tex` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— 8 `.tex` files under `build/sections/`, a root `build/paper.tex`,
one `pdf-glyphs.tex`, one figure under `build/figures/`, and a
`references.tex` bibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 309 at line 7628. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 712. |
| S3 | [`preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/paper.tex`](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/paper.tex) | 76 | Manuscript main file: title and documentclass. |
| S4 | [`preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/sections/introduction.tex) | 131 | Introduction: the abstract, the setup, the main classification theorem, the unstable consequences, the prior work and prime-three obstruction, the proof structure, and the conventions. |
| S5 | [`preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/references.tex`](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/references.tex) | 256 | Manuscript bibliography. |

## Bibliography

- Steven Amelotte, _The fibre of the degree $`3`$ map, Anick spaces and the double suspension_, Proceedings of the Edinburgh Mathematical Society **63** (2020), 830–843. arXiv:1908.05302v1.
- Gabriel Angelini-Knoll, Mark Behrens, Eva Belmont, and Hana Jia Kong, _A deformation of Borel equivariant homotopy_, Advances in Mathematics **484** (2026), 110698. doi:10.1016/j.aim.2025.110698; arXiv:2308.01873v3.
- William Browder, _The Kervaire invariant of framed manifolds and its generalization_, Annals of Mathematics (2) **90** (1969), 157–186. doi:10.2307/1970686.
- V. G. Drinfeld, _Elliptic modules_, Mathematics of the USSR-Sbornik **23** (1974), 561–592. doi:10.1070/SM1974v023n04ABEH001731.
- Zhipeng Duan, Michael A. Hill, Guchuan Li, Yutao Liu, XiaoLin Danny Shi, Guozhen Wang, and Zhouli Xu, _Periodicity and finite complexity in higher real $`K`$-theories_, preprint, 2025. arXiv:2512.01161v2.
- Michael J. Hopkins and Benedict H. Gross, _The rigid analytic period mapping, Lubin–Tate space, and stable homotopy theory_, Bulletin of the American Mathematical Society **30** (1994), 76–86. doi:10.1090/S0273-0979-1994-00438-0; arXiv:math/9401220.
- Jeremy Hahn, Andrew Senger, and Dylan Wilson, _Odd primary analogs of Real orientations_, Geometry & Topology **27** (2023), 87–129. doi:10.2140/gt.2023.27.87.
- Michael A. Hill, _Recent computational work on $`EO_n`$_, in _Homotopy Theory_, Oberwolfach Reports **4** (2007), 2698–2701, report on joint work with Michael J. Hopkins and Douglas C. Ravenel. Report 45/2007.
- Michael A. Hill, Michael J. Hopkins, and Douglas C. Ravenel, _On the $`3`$-primary Arf–Kervaire invariant problem_, work in progress, 14 September 2011. Author manuscript.
- Michael A. Hill, Michael J. Hopkins, and Douglas C. Ravenel, _On the nonexistence of elements of Kervaire invariant one_, Annals of Mathematics (2) **184** (2016), 1–262. doi:10.4007/annals.2016.184.1.1.
- Taira Honda, _Formal groups and zeta-functions_, Osaka Journal of Mathematics **5** (1968), 199–213. Publisher text.
- Paul G. Goerss and Michael J. Hopkins, _Moduli spaces of commutative ring spectra_, in _Structured Ring Spectra_, Andrew Baker and Birgit Richter (eds.), London Mathematical Society Lecture Note Series **315**, Cambridge University Press, Cambridge, 2004, pp. 151–200. doi:10.1017/CBO9780511529955.009; 52-page author preprint.
- Larry A. Lambe, _Resolutions via homological perturbation_, Journal of Symbolic Computation **12** (1991), 71–87. doi:10.1016/S0747-7171(08)80140-X.
- Michel Lazard, _Sur les groupes de Lie formels \`a un param\`etre_, Bulletin de la Société Mathématique de France **83** (1955), 251–274. Numdam text.
- Maria Basterra and Michael A. Mandell, _The multiplication on $`BP`$_, Journal of Topology **6** (2013), 285–310. doi:10.1112/jtopol/jts032.
- J. Peter May, _The cohomology of restricted Lie algebras and of Hopf algebras_, Journal of Algebra **3** (1966), 123–146. doi:10.1016/0021-8693(66)90009-3; Author text.
- J. Peter May, _A general algebraic approach to Steenrod operations_, in _The Steenrod Algebra and its Applications_, Lecture Notes in Mathematics **168**, Springer, Berlin, 1970, pp. 153–231. Author text.
- Lennart Meier, XiaoLin Danny Shi, and Mingcong Zeng, _The localized slice spectral sequence, norms of Real bordism, and the Segal conjecture_, Advances in Mathematics **412** (2023), 108804. doi:10.1016/j.aim.2022.108804; arXiv:2008.04963v4.
- Pierre Berthelot and William Messing, _Théorie de Dieudonné cristalline I_, Astérisque **63** (1979), 17–37. Numdam text.
- Haynes R. Miller, Douglas C. Ravenel, and W. Stephen Wilson, _Periodic phenomena in the Adams–Novikov spectral sequence_, Annals of Mathematics (2) **106** (1977), 469–516. doi:10.2307/1971064.
- J. S. Milne, _Class Field Theory_, version 4.03, 2020. Author course notes.
- John Milnor, _The Steenrod algebra and its dual_, Annals of Mathematics (2) **67** (1958), 150–171. Public text.
- Ching-Li Chai and Frans Oort, _Moduli of abelian varieties and $`p`$-divisible groups_, in _Arithmetic Geometry_, Henri Darmon, David Alexandre Ellwood, Brendan Hassett, and Yuri Tschinkel (eds.), Clay Mathematics Proceedings **8**, American Mathematical Society, Providence, RI, 2009, pp. 441–536. Publisher volume.
- Daniel Quillen, _On the formal group laws of unoriented and complex cobordism theory_, Bulletin of the American Mathematical Society **75** (1969), 1293–1298. doi:10.1090/S0002-9904-1969-12401-8.
- Douglas C. Ravenel, _The non-existence of odd primary Arf invariant elements in stable homotopy_, Mathematical Proceedings of the Cambridge Philosophical Society **83** (1978), 429–443. doi:10.1017/S0305004100054712.
- Douglas C. Ravenel, _Complex Cobordism and Stable Homotopy Groups of Spheres_, second edition, AMS Chelsea Publishing **347**, American Mathematical Society, Providence, RI, 2004. Author's online edition.
- Eva Belmont and Rin Ray, _Towards the $`p=3`$ Kervaire Invariant Problem: The $`E_2`$-page for the homotopy fixed points spectral sequence computing $`\pi_*(E_6^{hC_9})`$_, preprint, 2025. arXiv:2507.10157v1.
- Rin Ray, _Moduli Stacks of $`G`$-Curves in Homotopy Theory at Height $`p-1`$_, preprint, 2026. arXiv:2509.23428v2.
- Paul S. Selick, _A reformulation of the Arf invariant one mod $`p`$ problem and applications to atomic spaces_, Pacific Journal of Mathematics **108** (1983), 431–450. Publisher text.
- Julio Rubio and Francis Sergeraert, _Constructive Homological Algebra and Applications_, preprint, version 3, 2013. arXiv:1208.3816v3.
- Eva Belmont and Katsumi Shimomura, _Beta families arising from a $`v_2^9`$ self map on $`S/(3,v_1^8)`$_, Algebraic & Geometric Topology **23** (2023), 4349–4378. doi:10.2140/agt.2023.23.4349; arXiv:2109.01059v2.
- J. P. C. Greenlees and Brooke Shipley, _Fixed point adjunctions for equivariant module spectra_, Algebraic & Geometric Topology **14** (2014), 1779–1799. doi:10.2140/agt.2014.14.1779.
- Matthias Strauch, _Galois actions on torsion points of one-dimensional formal modules_, Journal of Number Theory **130** (2010), no. 3, 528–533. doi:10.1016/j.jnt.2009.10.004; arXiv:0709.3542v1 (preprint version).
- Jonathan Lubin and John Tate, _Formal complex multiplication in local fields_, Annals of Mathematics (2) **81** (1965), 380–387. doi:10.2307/1970622.
- Jonathan Lubin and John Tate, _Formal moduli for one-parameter formal Lie groups_, Bulletin de la Société Mathématique de France **94** (1966), 49–59. doi:10.24033/bsmf.1633.
- Hirosi Toda, _Extended $`p`$-th powers of complexes and applications to homotopy theory_, Proceedings of the Japan Academy **44** (1968), 198–203. doi:10.3792/pja/1195521243.
- Hirosi Toda, _An important relation in homotopy groups of spheres_, Proceedings of the Japan Academy **43** (1967), 839–842. doi:10.3792/pja/1195521423.
- Michael Rapoport and Thomas Zink, _On the Drinfeld moduli problem of $`p`$-divisible groups_, Cambridge Journal of Mathematics **5** (2017), 229–279. doi:10.4310/CJM.2017.v5.n2.a2.
