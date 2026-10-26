[Notes](../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 203](../index/algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md)

# 203 — Donovan's conjecture over fields and discrete valuation rings

[Index page](../index/algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md)

## Original CONTENTS.md summary

The release's blurb [S1:4632] and the catalog abstract [S2:487] state
the family's claim: Donovan's conjecture over each fixed algebraically
closed field of characteristic $p$ — for each bound on defect-group
order, blocks of finite groups belong to only finitely many Morita
equivalence classes, for every prime — together with the integral form
over each fixed complete mixed-characteristic discrete valuation ring
with algebraically closed residue field. The field manuscript's abstract
 "We prove Donovan's conjecture over every algebraically closed field
\(K\) of characteristic \(p>0\). For each fixed \(K\) and bound on
defect-group order, blocks of finite groups represent only finitely
many \(K\)-linear Morita equivalence classes. The defect groups need
not be abelian, and the result includes \(p=2\). [S4:2–6]"

## Undergraduate summary

In modular representation theory a $p$-block of a finite group algebra
groups the simple modules that are linked by their defect, a $p$-subgroup
measuring how far the block is from being semisimple. Two blocks are
Morita equivalent when their module categories are equivalent, so a block
is classified up to Morita equivalence by the full structure of its
representations, not just its simple modules. Donovan's conjecture asks
whether fixing a defect group leaves only finitely many Morita classes of
blocks with that defect [S4:12–25]. The field manuscript states the
conjecture in a bounded-order form and proves it 

> **theorem**
Fix a prime \(p\), an algebraically closed field \(K\) of
characteristic \(p\), and a positive integer \(M\).
As \(G\) ranges over finite groups and \(b\) over block idempotents of
\(KG\) with defect groups of order at most \(M\), only finitely many
\(K\)-linear Morita equivalence classes of \(KGb\) occur.
In particular, over this field \(K\), Donovan's conjecture holds for every finite
\(p\)-group, including nonabelian groups. [S4:27–36]

The bounded-order form is equivalent to fixing one defect group, since
there are only finitely many isomorphism types of groups of bounded
order [S4:38–42]. The defect groups may be nonabelian, and the result
includes $p=2$.

## Graduate summary

**The field theorem and its two uniformity problems.** The proof must
control two things a defect bound does not itself bound: the Cartan
entries (composition multiplicities in projective covers), and the field
of definition of the basic algebras. A Cartan-entry bound gives a
dimension bound through the Brauer–Feit bound on ordinary characters, and
a bounded dimension together with a bounded finite field of definition
leaves finitely many multiplication tables [S4:104–116]. The multiplicity
problem is the harder one: in a group of Lie type finite tori can grow even
when the chosen block has small defect, so a bound for a principal block
with small Sylow subgroup does not address it. The geometric construction
counts indecomposable projective factors rather than their vector-space
dimensions and estimates characters after projection to the chosen block
[S4:104–142].

**The proof's new ingredients.** Four constructions address the still
unbounded parameters. Two are the main outputs: a uniform Cartan bound for
quasisimple blocks of bounded defect, and an equivariant comparison that
controls the multiplication and descent data of the crossed extensions.
The remaining two treat the classical-rank case (projective cones under
Harish–Chandra moves) and the cuspidal endpoint (modular Harish–Chandra
induction on unbounded-rank cuspidal labels). The final extension argument
proves finiteness over $k=\overline{\mathbb F}_p$ and then transfers the
finite list to the fixed algebraically closed field $K$ [S4:146–242].

**The integral companion over the Witt ring.** The second manuscript
proves the integral assertion over the Witt ring $W(\overline{\mathbb F}_p)$,
which is stronger than the field assertion because it concerns integral
module categories including their lattice structure [S6:9–17]:

> **theorem**
Let $p$ be a prime, let $\mathcal O=W(\overline{\mathbb F}_p)$, and let
$M\geq1$ be an integer.  As $G$ ranges over all
finite groups and $b$ ranges over all blocks of $\mathcal O G$ whose defect
groups have order at most $M$, the algebras $\mathcal O G b$ belong to only
finitely many $\mathcal O$-linear Morita equivalence classes. [S6:19–25]

The corollary extends the conclusion to each fixed complete
mixed-characteristic discrete valuation ring with algebraically closed
residue field, ramification allowed and no splitting hypothesis required
[S6:38–52]. The proof refines the field manuscript's integral operators to
obtain exact equivariance over the Witt ring itself, in three successive
steps: exact comparison, based finiteness, and removal of the unbounded
normal $p'$-kernel [S6:136–190].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

Donovan's conjecture is attributed to Peter Donovan and appears as
Conjecture M in Alperin's account of problems in group representation
theory. Its Cartan-boundedness component grows out of a question of
Brauer, and Hiss emphasized the additional rationality obstruction;
Kessar proved that field-valued Donovan finiteness separates into Cartan
boundedness and bounded Morita–Frobenius numbers [S4:56–98]. Partial
results include Scopes (symmetric-group blocks) and Kessar (their double
covers), Jost (unipotent blocks of general linear groups), Eaton–Livesey
(abelian $2$-groups), and the integral finiteness criterion of
Eaton–Eisele–Livesey with Farrell–Kessar's rationality bounds. The
present two-manuscript pair closes the field case for every prime and
nonabelian defect group, and the integral Witt-ring case as its companion;
the field proof is independent of the integral companion [S4:56–98].

## Consequences

**The finite list bounds the block's invariants.** Over the fixed field
$K$ the resulting finite list bounds Cartan entries, Loewy lengths of
basic algebras, and, in each fixed degree, dimensions of extension
groups between simple modules [S4:38–42]. A Cartan-entry bound gives the
required dimension bound through the Brauer–Feit bound, so the finiteness
assertion yields uniform control of these invariants across all blocks of
bounded defect [S4:104–116].

**The integral statement extends the field basic algebras.** The integral
theorem's finite list also represents all field basic algebras — the
reduction corollary records that the resulting finite integral list covers
the residue-field case, and the fixed-coefficient-ring corollary is proved
by scalar extension [S6:180–190]. The two manuscripts together give
bounded-defect finiteness over every algebraically closed field and over
each fixed complete discrete valuation ring.

## Section skeleton

**Field manuscript** [S3], 9 sections under `build/sections/`:
00_introduction [S4], 01_preliminaries, 02_geometry, 03_families,
04_labels, 05_runners, 06_endpoint, 07_extensions, 08_periodicity. Its
root is `build/main.tex`, with a `references.tex` bibliography [S7].

**Integral manuscript** [S5:9–16], 7 sections under `build/sections/`:
01_introduction [S6], 02_inputs, 03_rigidity, 04_comparison, 05_sylow,
06_kernel, 07_assembly. Its root is `build/main.tex`, with a
`references.bib` bibliography [S8].

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems are machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX manuscripts —
13 `.tex` files in the field `build/` and 9 in the integral `build/` —
and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | The release's blurb for family 203 at line 4632. |
| S2 | [`overview.tex`](../../overview.tex) | 859 | The catalog abstract at line 487. |
| S3 | [`preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/main.tex`](../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/main.tex) | 29 | Field manuscript main file: title and structure. |
| S4 | [`preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/sections/00_introduction.tex`](../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/sections/00_introduction.tex) | 242 | Field manuscript introduction: abstract, main theorem, prior work, the two uniformity problems, and the proof's new ingredients. |
| S5 | [`preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/main.tex`](../../preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/main.tex) | 31 | Integral manuscript main file: title and abstract. |
| S6 | [`preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/sections/01_introduction.tex`](../../preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/sections/01_introduction.tex) | 190 | Integral manuscript introduction: main theorem, the fixed-coefficient-ring corollary, the companion relationship, and what must be retained over the Witt ring. |
| S7 | [`preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/references.tex`](../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/references.tex) | 418 | Field manuscript bibliography. |
| S8 | [`preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/references.bib`](../../preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/references.bib) | 158 | Integral manuscript bibliography. |

## Bibliography

- J. L. Alperin, _Local representation theory_, in _The Santa Cruz Conference on Finite Groups_ (Santa Cruz, California, 1979), Proc. Sympos. Pure Math. **37**, American Mathematical Society, Providence, RI, 1980, 369–375.
- Alperin, J. L., Local representation theory (1980)
- An, Jianbei, Eaton, Charles W., Morita equivalence classes of blocks with extraspecial defect groups $p_+^{1+2}$ (2025)
- Teruaki Asai, _Unipotent characters of $\mathrm{SO}_{2n}^{\pm}$, $\mathrm{Sp}_{2n}$ and $\mathrm{SO}_{2n+1}$ over $\mathbb F_q$ with small $q$_, Osaka J. Math. **20** (1983), 631–643. doi:10.18910/7124.
- Teruaki Asai, _Unipotent class functions of split special orthogonal groups $\mathrm{SO}_{2n}^{+}$ over finite fields_, Comm. Algebra **12** (1984), 517–615; _The unipotent class functions on the symplectic groups and the odd orthogonal groups over finite fields_, Comm. Algebra **12** (1984), 617–645; _The unipotent class functions of non-split finite special orthogonal groups_, Comm. Algebra **13** (1985), 845–924.
- Michael Aschbacher, _Finite Group Theory_, second edition, Cambridge Studies in Advanced Mathematics **10**, Cambridge University Press, Cambridge, 2000. doi:10.1017/CBO9781139175319.
- The Stacks Project Authors, The Stacks Project (2026)
- The Stacks Project Authors, The Cohen structure theorem (2026)
- A. A. Beilinson, J. Bernstein, and P. Deligne, _Faisceaux pervers_, in _Analyse et topologie sur les espaces singuliers, I_ (Luminy, 1981), Astérisque **100** (1982), 5–171. NUMDAM.
- Cédric Bonnafé, _Quasi-isolated elements in reductive groups_, preprint, 2004. arXiv:math/0402276v1.
- Cédric Bonnafé, Jean-François Dat, and Raphaël Rouquier, _Derived categories and Deligne–Lusztig varieties II_, Ann. of Math. (2) **185** (2017), no. 2, 609–670. doi:10.4007/annals.2017.185.2.5.
- Patrick Brosnan, Jaehyun Hong, and Donggun Lee, _Geometry of regular semisimple Lusztig varieties_, preprint, 2025, revised July 15, 2026; to appear in J. Eur. Math. Soc. arXiv:2504.15868v3.
- Carles Broto, Jesper M. Mø ller, and Bob Oliver, _Automorphisms of fusion systems of finite simple groups of Lie type_, Mem. Amer. Math. Soc. **262** (2019), no. 1267. doi:10.1090/memo/1267.
- Michel Broué, Gunter Malle, and Jean Michel, _Generic blocks of finite reductive groups_, Astérisque **212** (1993), 7–92. NUMDAM.
- Jonathan Brundan, Richard Dipper, and Alexander Kleshchev, _Quantum linear groups and representations of $\GL_n(\F_q)$_, Mem. Amer. Math. Soc. **149** (2001), no. 706. Author manuscript.
- Richard Dipper and Jie Du, _Harish-Chandra vertices_, J. Reine Angew. Math. **437** (1993), 101–130. doi:10.1515/crll.1993.437.101.
- Jianbei An and Charles W. Eaton, _Morita equivalence classes of blocks with extraspecial defect groups $p_+^{1+2}$_, Math. Z. **311** (2025), article no. 12. doi:10.1007/s00209-025-03791-x.
- Charles W. Eaton, _Blocks whose defect groups are Suzuki $2$-groups_, J. Algebra **664** (2025), 498–513. doi:10.1016/j.jalgebra.2024.10.011.
- Charles Eaton, Florian Eisele, Radha Kessar, Markus Linckelmann, and A. A. Schaeffer Fry, _On $2$-blocks with quaternion defect groups_, preprint, 2026. arXiv:2608.12052v1.
- Charles W. Eaton, Florian Eisele, and Michael Livesey, _Donovan's conjecture, blocks with abelian defect groups and discrete valuation rings_, Math. Z. **295** (2020), 249–264. doi:10.1007/s00209-019-02354-1.
- Eaton, Charles W., Eisele, Florian, Kessar, Radha and Linckelmann, Markus, Schaeffer Fry, A. A., On $2$-blocks with quaternion defect groups (2026)
- Eaton, Charles W., Eisele, Florian, Livesey, Michael, Donovan's conjecture, blocks with abelian defect groups and discrete valuation rings (2020)
- Florian Eisele, _The Picard group of an order and Külshammer reduction_, Algebr. Represent. Theory **24** (2021), 505–518. doi:10.1007/s10468-020-09957-x.
- Florian Eisele, _On the geometry of lattices and finiteness of Picard groups_, J. Reine Angew. Math. **782** (2022), 219–233. doi:10.1515/crelle-2021-0064.
- Eisele, Florian, The Picard group of an order and {Külshammer} reduction (2021)
- Eisele, Florian, On the geometry of lattices and finiteness of Picard groups (2022)
- Eisele, Florian, Livesey, Michael, Arbitrarily large Morita Frobenius numbers (2022)
- Marc Cabanes and Michel Enguehard, _On blocks of finite reductive groups and twisted induction_, Adv. Math. **145** (1999), no. 2, 189–229. doi:10.1006/aima.1998.1814.
- Marc Cabanes and Michel Enguehard, _Representation Theory of Finite Reductive Groups_, New Mathematical Monographs **1**, Cambridge University Press, Cambridge, 2004. doi:10.1017/CBO9780511542763.
- Michel Enguehard, _Towards a Jordan decomposition of blocks of finite reductive groups_, preprint, 2013. arXiv:1312.0106v1.
- Arnaud Eteve, _Tilting representations of finite groups of Lie type_, preprint, 2024, revised 2025. arXiv:2412.13326v2.
- Farrell, Niamh, Kessar, Radha, Rationality of blocks of quasi-simple finite groups (2019)
- Richard Brauer and Walter Feit, _On the number of irreducible characters of finite groups in a given block_, Proc. Natl. Acad. Sci. USA **45** (1959), no. 3, 361–365. doi:10.1073/pnas.45.3.361.
- Richard Dipper and Peter Fleischmann, _Modular Harish-Chandra theory I_, Math. Z. **211** (1992), 49–71. doi:10.1007/BF02571417.
- A. A. Schaeffer Fry, Jay Taylor, and C. Ryan Vinroot, _Galois automorphisms and a unique Jordan decomposition in the case of connected centralizer_, J. Algebra **664** (2025), part B, 123–149. doi:10.1016/j.jalgebra.2024.10.017.
- James A. Green, _The characters of the finite general linear groups_, Trans. Amer. Math. Soc. **80** (1955), no. 2, 402–447. doi:10.1090/S0002-9947-1955-0072878-2.
- Thomas J. Haines, _Cellular pavings of fibers of convolution morphisms_, Épijournal Géom. Algébrique **9** (2025), article no. 9. doi:10.46298/epiga.2024.12352.
- Meinolf Geck and Gerhard Hiss, _Basic sets of Brauer characters of finite groups of Lie type_, J. Reine Angew. Math. **418** (1991), 173–188. doi:10.1515/crll.1991.418.173.
- Gerhard Hiss, _On a question of Brauer in modular representation theory of finite groups_, RIMS K\^oky\^uroku **1149** (2000), 21–29. Author article.
- Hiss, Gerhard, On a question of Brauer in modular representation theory of finite groups (2000)
- James E. Humphreys, _Defect groups for finite groups of Lie type_, Math. Z. **119** (1971), 149–152. doi:10.1007/BF01109967.
- Richard Dipper and Gordon James, _Representations of Hecke algebras of general linear groups_, Proc. London Math. Soc. (3) **52** (1986), no. 1, 20–52. doi:10.1112/plms/s3-52.1.20.
- Thomas Jost, _Morita equivalence for blocks of finite general linear groups_, Manuscripta Math. **91** (1996), 121–144. doi:10.1007/BF02567944.
- Niamh Farrell and Radha Kessar, _Rationality of blocks of quasi-simple finite groups_, Represent. Theory **23** (2019), 325–349. doi:10.1090/ert/530.
- Gerhard Hiss and Radha Kessar, _Scopes reduction and Morita equivalence classes of blocks in finite classical groups_, J. Algebra **230** (2000), 378–423. doi:10.1006/jabr.2000.8319.
- Gerhard Hiss and Radha Kessar, _Scopes reduction and Morita equivalence classes of blocks in finite classical groups II_, J. Algebra **283** (2005), 522–563. doi:10.1016/j.jalgebra.2004.08.030.
- Radha Kessar, _Blocks and source algebras for the double covers of the symmetric and alternating groups_, J. Algebra **186** (1996), no. 3, 872–933. doi:10.1006/jabr.1996.0400.
- Radha Kessar, _A remark on Donovan's conjecture_, Arch. Math. **82** (2004), 391–394. doi:10.1007/s00013-004-4880-8.
- Kessar, Radha, A remark on Donovan's conjecture (2004)
- Burkhard Külshammer, _Donovan's conjecture, crossed products and algebraic group actions_, Israel J. Math. **92** (1995), 295–306.
- Serge Lang, _Algebraic groups over finite fields_, Amer. J. Math. **78** (1956), 555–563.
- Michael Larsen, Gunter Malle, and Pham Huu Tiep, _The largest irreducible representations of simple groups_, Proc. London Math. Soc. (3) **106** (2013), 65–96. doi:10.1112/plms/pds030. Revised author manuscript.
- Robert B. Howlett and Gustav I. Lehrer, _Induced cuspidal representations and generalised Hecke rings_, Invent. Math. **58** (1980), 37–64. doi:10.1007/BF01402273.
- Markus Linckelmann, _The Block Theory of Finite Group Algebras_, Vols. I and II, London Mathematical Society Student Texts **91** and **92**, Cambridge University Press, Cambridge, 2018. Vol. I: doi:10.1017/9781108349321; Vol. II: doi:10.1017/9781108349307.
- Charles W. Eaton and Michael Livesey, _Donovan's conjecture and blocks with abelian defect groups_, Proc. Amer. Math. Soc. **147** (2019), 963–970. doi:10.1090/proc/14316.
- Külshammer, Burkhard, Morita equivalent blocks in Clifford theory of finite groups (1990)
- Külshammer, Burkhard, Donovan's conjecture, crossed products and algebraic group actions (1995)
- Pierre Deligne and George Lusztig, _Representations of reductive groups over finite fields_, Ann. of Math. (2) **103** (1976), no. 1, 103–161. doi:10.2307/1971021.
- George Lusztig, _Characters of Reductive Groups over a Finite Field_, Annals of Mathematics Studies **107**, Princeton University Press, Princeton, NJ, 1984.
- Radha Kessar and Gunter Malle, _Lusztig induction and $\ell$-blocks of finite reductive groups_, Pacific J. Math. **279** (2015), nos. 1–2, 269–298. doi:10.2140/pjm.2015.279.269.
- Frank Lübeck and Gunter Malle, _A Murnaghan–Nakayama rule for values of unipotent characters in classical groups_, Represent. Theory **20** (2016), 139–161. arXiv:1508.01627v4.
- Marcus, Andrei, On equivalences between blocks of group algebras: reduction to the simple components (1996)
- Richard Dipper and Andrew Mathas, _Morita equivalences of Ariki–Koike algebras_, Math. Z. **240** (2002), no. 3, 579–610. doi:10.1007/s002090100371.
- Cédric Bonnafé and Jean Michel, _Computational proof of the Mackey formula for $q>2$_, J. Algebra **327** (2011), 506–526. doi:10.1016/j.jalgebra.2010.10.030.
- Michel Broué and Jean Michel, _Blocs et séries de Lusztig dans un groupe réductif fini_, J. Reine Angew. Math. **395** (1989), 56–67.
- François Digne and Jean Michel, _On Lusztig's parametrization of characters of finite groups of Lie type_, Astérisque **181–182** (1990), 113–156. NUMDAM.
- Yves Laszlo and Martin Olsson, _The six operations for sheaves on Artin stacks I: Finite coefficients_, Publ. Math. Inst. Hautes Études Sci. **107** (2008), 109–168. doi:10.1007/s10240-008-0011-6.
- Yves Laszlo and Martin Olsson, _The six operations for sheaves on Artin stacks II: Adic coefficients_, Publ. Math. Inst. Hautes Études Sci. **107** (2008), 169–210. doi:10.1007/s10240-008-0012-5.
- OpenAI, _Integral Donovan Finiteness over Witt Vectors_, OpenAI Math Release preprint OAI:Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026, 2026.
- OpenAI, _The Blockwise Alperin Weight Conjecture_, OpenAI Math Release preprint OAI:The-Blockwise-Alperin-Weight-Conjecture-September-23-2026, 2026.
- OpenAI, Donovan's Conjecture over Algebraically Closed Fields (2026)
- OpenAI, The Blockwise Alperin Weight Conjecture (2026)
- Jeremy Rickard, _Finite group actions and étale cohomology_, Publ. Math. Inst. Hautes Études Sci. **80** (1994), 81–94. doi:10.1007/BF02698896.
- Cédric Bonnafé and Raphaël Rouquier, _Catégories dérivées et variétés de Deligne–Lusztig_, Publ. Math. Inst. Hautes Études Sci. **97** (2003), 1–59. doi:10.1007/s10240-003-0013-3.
- Rouquier, Raphaël, The derived category of blocks with cyclic defect groups (1998)
- Jie Du and Hebing Rui, _Ariki–Koike algebras with semisimple bottoms_, Math. Z. **234** (2000), 807–830. doi:10.1007/s002090050009.
- Joanna Scopes, _Cartan matrices and Morita equivalence for blocks of the symmetric groups_, J. Algebra **142** (1991), no. 2, 441–455. doi:10.1016/0021-8693(91)90319-4.
- Britta Späth, _Extensions of characters in type D and the inductive McKay condition, II_, Invent. Math. **242** (2025), 45–122. doi:10.1007/s00222-025-01354-9.
- Paul Fong and Bhama Srinivasan, _The blocks of finite general linear and unitary groups_, Invent. Math. **69** (1982), 109–153. doi:10.1007/BF01389188.
- Robert Steinberg, _Automorphisms of finite linear groups_, Canad. J. Math. **12** (1960), 606–615. doi:10.4153/CJM-1960-054-6.
- Gunter Malle and Donna Testerman, _Linear Algebraic Groups and Finite Groups of Lie Type_, Cambridge Studies in Advanced Mathematics **133**, Cambridge University Press, Cambridge, 2011. doi:10.1017/CBO9780511994777.
- Robert A. Wilson, _The Finite Simple Groups_, Graduate Texts in Mathematics **251**, Springer, London, 2009. doi:10.1007/978-1-84800-988-2.
- Xinwen Zhu, _Tame categorical local Langlands correspondence_, preprint, 2025. arXiv:2504.07482v1.
- Bonnafé, Cédric, Rouquier, Raphaël, Catégories dérivées et variétés de Deligne–Lusztig (2003)
- Bonnafé, Cédric, Dat, Jean-François, Rouquier, Raphaël, Derived categories and Deligne–Lusztig varieties II (2017)
