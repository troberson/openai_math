[Notes](../../README.md) / [Summaries](../README.md) / [Algebra](../../index/disciplines/algebra.md) / [Family 195](../../index/algebra/195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md)

# 195 — A counterexample to the small Cohen–Macaulay module conjecture

[Index page](../../index/algebra/195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md)

## Original CONTENTS.md summary

 carries the family entry:

> Constructs a three-dimensional complete Noetherian normal local domain over $\mathbb C$ with no nonzero finitely generated maximal Cohen–Macaulay module. A three-dimensional local domain essentially of finite type over $\mathbb C$ has the same property, disproving the domain form of the small Cohen–Macaulay module conjecture. [S1:471]

The entry names the manuscript "A Complete Local Domain without a Small Cohen–Macaulay Module [S1:471]" .

The README title is `A Complete Local Domain without a Small Cohen-Macaulay Module` [S2:1].

The README dates it 2026-09-23 [S2:5].

## Undergraduate summary

A small Cohen--Macaulay module over a Noetherian local ring is a nonzero finitely generated module whose depth equals the ring's dimension. The domain form of the conjecture asks whether every complete Noetherian local domain has one.

The manuscript's abstract states the counterexample. says: "We construct a three-dimensional complete Noetherian normal local domain containing $\mathbb C$, with residue field $\mathbb C$, that has no nonzero finitely generated maximal Cohen–Macaulay module. This disproves the domain form of the small Cohen–Macaulay module conjecture. [S3:38–41]"

The main theorem names the ring. gives it: "There exists a three-dimensional complete Noetherian normal local domain $R$ containing $\mathbb C$, with residue field $\mathbb C$, such that no nonzero finitely generated $R$-module has depth three. [S3:55–57]"

The proof starts from a smooth projective surface and its section ring, completes the cone at the vertex, and shows that any finite module of full depth would force a Chern-character inequality that the chosen surface violates.

## Graduate summary

The conjecture is stated. states it: "A _small Cohen–Macaulay module_ over a Noetherian local ring $(R,\mathfrak m)$ is a nonzero finitely generated $R$-module $M$ such that $\depth_R M=\dim R$. Such a module is also called a maximal Cohen–Macaulay module. The domain form of the small Cohen–Macaulay module conjecture asks whether every complete Noetherian local domain has one. [S3:47–51]"

The module-versus-algebra distinction is stated. states it: "The distinction between modules and algebras matters here. A module-finite extension domain $R\subseteq B$ that is Cohen–Macaulay supplies such a module, but the converse need not hold. Our obstruction applies to every finite module; it requires neither a grading nor an algebra structure. [S3:60–62]"

Hochster's problem is recorded. records it: "Hochster formulated the finite-module existence problem in his early work on Cohen–Macaulay modules and homological conjectures [S3:63–64]"

The low-dimensional cases are recorded. records them: "In dimensions at most two, a complete local domain has a small Cohen–Macaulay module: its finite normalization is Cohen–Macaulay [S3:65–67]"

The big-module results are recorded. records them: "Dropping finite generation changes the problem. In the balanced convention, a _big Cohen–Macaulay module_ is a possibly infinitely generated module on which every system of parameters is a regular sequence and whose quotient by the maximal ideal is nonzero. [S3:78–81]"

Hochster's existence theorem is recorded. records it: "quotient by the maximal ideal is nonzero. Hochster proved existence in equal characteristic [S3:81–82]"

The positive-characteristic algebra is recorded. records it: "Hochster–Huneke showed that the absolute integral closure of an excellent local domain of positive characteristic is such an algebra [S3:82–84]"

The mixed-characteristic result is recorded. records it: "Perfectoid methods later yielded big Cohen–Macaulay algebras in mixed characteristic, completing the existence theorem for Noetherian local rings [S3:84–86]"

The scope of those results is stated. states it: "These results impose no finite-generation conclusion. [S3:87–88]"

The trace argument is stated. states it: "For a normal local domain containing the rational numbers, trace makes the ring a direct summand of every module-finite extension domain. A Cohen–Macaulay extension would therefore force the original ring to be Cohen–Macaulay. [S3:90–93]"

Bhatt's obstruction is recorded. records it: "Bhatt constructed positive-characteristic complete normal local domains with no finite Cohen–Macaulay extension, using a Witt-vector cohomological obstruction [S3:93–95]"

The asymptotic substitutes are recorded. records them: "Neither obstruction excludes arbitrary finite modules. Bhatt, Hochster, and Ma instead study asymptotic substitutes for small Cohen–Macaulay modules. Their August 25, 2026 version [S3:95–97]"

The open-problem statement is recorded. records it: "describes the existence problem as open even for local rings at maximal ideals of affine three-dimensional domains over algebraically closed fields [S3:98–100]"

The geometric input is defined. defines it: "The geometric input is a smooth integral projective surface $X$ over $\mathbb C$ with an ample globally generated line bundle $\mathcal O_X(H)$. Write [S3:102–104]"

The completed ring and the affine-local corollary are stated. states them: "Here the hat denotes completion at the maximal ideal. We write $K_X$ for the canonical divisor and $c_2(X)$ for the second Chern number. For the specific pair $(X,H)$ used for Theorem  , the uncompleted vertex localization $T(X,H)_{T(X,H)_{>0}}$ also has no small Cohen–Macaulay module (Corollary  ). It is a three-dimensional local domain essentially of finite type over $\mathbb C$, so this supplies a counterexample in the affine-local class just described. The deduction uses faithful flatness of completion. [S3:109–116]"

The obstruction theorem is the load-bearing statement. gives it: "Let $X$ be a smooth integral projective surface over $\mathbb C$, and let $H$ be an ample globally generated divisor. If $R(X,H)$ admits a small Cohen–Macaulay module, then $$\label{eq:obstruction} K_X^2-2c_2(X)\leq 6H^2.$$ [S3:120–125]"

The Ulrich route is recorded. records it: "A numerical obstruction for Ulrich sheaves on surfaces follows from Bogomolov's inequality and the Hodge index theorem. Beauville presented this route for surfaces of Néron–Severi rank one [S3:128–130]"

The rank restriction is removed. states it: "Anghel gives the surface inequality without that Néron–Severi rank restriction [S3:131–132]"

The Ulrich triviality is recorded. records it: "For a projective surface, an Ulrich sheaf has trivial vector-bundle pushforward under a finite linear projection to $\mathbb P^2$ [S3:134–135]"

The replacement is stated. states it: "The argument here replaces that triviality condition by a comparison of coherent extensions across the exceptional divisor of a completed cone. A module over the completed local ring need not carry a grading. We therefore retain its actual vector bundle on the punctured spectrum, rather than assume it descends to an Ulrich sheaf on $X$. It is this comparison that permits arbitrary nongraded modules. [S3:136–142]"

The antecedent is recorded. records it: "The explicit surface used below is the complete-quadrangle Hirzebruch–Kummer construction appearing in [S3:143–144]"

The direct verification is stated. states it: "We give its construction and all the required numerical and positivity checks directly. [S3:145–146]"

The overlapping work is recorded. records it: "Anghel's September 14, 2026 preprint excludes arithmetically Cohen–Macaulay bundles under the sharper inequality $K_X^2-2c_2(X)>3H^2$, and excludes graded maximal Cohen–Macaulay modules over the same complete-quadrangle section rings used here [S3:148–152]"

The scope of that statement is stated. states it: "That statement does not assert nonexistence of arbitrary modules over the vertex completion. Chen's September 21, 2026 preprint proposes a [S3:153–154]"

Chen's bound is recorded. [S3:155–159] records it: "quantitative local-cohomology bound for every nonzero finite reflexive module over a completed cone when $K_X\equiv4H$ and $15H^2/8-\chi(\mathcal O_X)>0$, and obtains a proposed completed-local counterexample from the exponent-six cover [S3:155–158]"

The overlap and the difference are stated. states them: "Thus the existential completed-module claim overlaps with that work. Our obstruction applies without the proportionality hypothesis on $K_X$ and $H$; the exponent-seven polarization used below has $K_X\equiv5H$. [S3:160–163]"

The first proof step is stated. states it: "Choose a finite morphism $f:X\to\mathbb P^2$ with $f^*\mathcal O_{\mathbb P^2}(1)=\mathcal O_X(H)$, and put $h=H^2=\deg f$. The completed cone is finite over the regular local ring $A=\mathbb C[[x_0,x_1,x_2]]$. A small Cohen–Macaulay module is free over $A$. Its restriction to the punctured cone is a vector bundle, which extends to a coherent sheaf $\mathcal E$ on a regular model $W\to\Spec R(X,H)$ that is an isomorphism away from the exceptional surface $X$. [S3:169–175]"

The slope normalization is defined. defines it: "For a nonzero torsion-free sheaf $B$ on $X$, its normalized slope is \[ \mu(B)=\frac{c_1(B)\cdot H}{\rk(B)H^2}. \] It is slope-semistable if no nonzero subsheaf of smaller rank has larger slope. Its Harder–Narasimhan filtration has torsion-free semistable factors with decreasing slopes. We choose $\mathcal E$ with torsion-free restriction $P=\mathcal E|_X$. [S3:177–184]"

The two analytic steps are stated. states them: "First, elementary modifications of $\mathcal E$ along $X$ arrange that the slopes of the Harder–Narasimhan factors of $P$ lie in an interval of length at most one. These modifications preserve the bundle away from $X$. Second, that bundle comes from an $A$-free module. Comparing the pushforward of $\mathcal E$ with a trivial sheaf on the blowup of $\Spec A$ gives, for $F=f_*P$ of rank $N$, the inequality $2N\ch_2(F)\geq c_1(F)^2$, with Chern characters evaluated on $\mathbb P^2$. [S3:185–191]"

The surface-theory comparison is stated. states it: "Bogomolov's inequality for the semistable factors bounds the same normalized Chern expression above. More precisely, if $r=\rk P$, then $N=rh$ and the two comparisons give \[ 0\leq \frac{2\ch_2(f_*P)}N -\left(\fracc_1(f_*P)N\right)^2 \leq\frac12-\fracK_X^2-2c_2(X)12H^2. \] This yields  . Neither $P$ nor $f_*P$ is assumed semistable or Ulrich. [S3:192–201]"

The organization is recorded. records it: "Section   constructs the resolution and extends an arbitrary module. Section   proves the slope modification lemma. Section   establishes the Chern-character inequality, and Section   combines it with surface theory. Finally, Section   constructs a surface with $K_X^2-2c_2(X)>6H^2$. [S3:203–208]"

The cone section opens with the model. opens it: "Throughout this section, $X$ and $H$ satisfy the hypotheses of Theorem  . We construct a regular model of the completed cone and explain how a small Cohen–Macaulay module produces a sheaf on it. We also prove that the completed ring is normal. [S3:211–214]"

The finite map is constructed. constructs it: "Global generation supplies sections $s_0,s_1,s_2$ of $\mathcal O_X(H)$ with no common zero. Indeed, choose $s_0\ne0$, then $s_1$ avoiding the components of its zero divisor, and then $s_2$ nonvanishing at their finitely many common zeros. The resulting morphism \[ f:X\longrightarrow D:=\mathbb P^2,\qquad f^*\mathcal O_D(1)=\mathcal O_X(H), \] is finite and surjective. A positive-dimensional fiber would contain a curve on which $H$ is both ample and trivial, which is impossible. Properness then gives finiteness, and the intersection formula gives $\deg f=h:=H^2$. [S3:217–227]"

The regular model is defined. defines it: "Let $V_0=\Tot(\mathcal O_D(-1))$, the blowup of $\Spec S$ at the origin, and let \[ W_0=X\times_D V_0=\Tot(\mathcal O_X(-H)). \] The map $W_0\to V_0$ is finite. Evaluation of homogeneous sections gives $W_0\to\Spec T$. It is an isomorphism off the zero section. [S3:267–273]"

The module is made free. states it: "Suppose that $M$ is a small Cohen–Macaulay $R$-module. The parameters $x_0,x_1,x_2$ form an $M$-regular sequence, so $M$ has depth three over $A$. [S3:332–334]"

The Auslander--Buchsbaum conclusion is stated. states it: "shows that $$\label{eq:A-free} M\simeq A^N\quad\text{as an $A$-module},\qquad N>0.$$ [S3:336–339]"

The support is stated. states it: "The localization $R\otimes_A\Frac(A)$ is a finite-dimensional domain over a field, hence a field. Thus $M$ has positive generic rank over $R$ and full support. [S3:340–342]"

The balancing step is stated. states it: "We now modify the extension along $X$ so that its restriction has Harder–Narasimhan slopes in an interval of length at most one. Recall the normalization $\mu(B)=c_1(B)\cdot H/(\rk(B)h)$, where $h=H^2$. Tensoring with $\mathcal O_X(H)$ increases slope by one. [S3:378–381]"

The antecedent is recorded. records it: "Elementary modification to constrain the slopes of exceptional-divisor restrictions has an antecedent in Chen–Sun's optimal extensions of [S3:383–384]"

The setting difference is stated. states it: "Their analytic setting and reflexivity hypotheses differ from the Noetherian Cartier-divisor setting below; we give the needed algebraic modification and termination argument. [S3:386–388]"

The filtration is constructed. constructs it: "We recall briefly why the filtration exists in this setting. A torsion-free sheaf embeds in a sum of sufficiently positive line bundles, so its subsheaf slopes are bounded above by taking determinants. Their denominators are bounded because their ranks are bounded. Choose a subsheaf of maximum slope and, among these, of maximum rank; saturate it. Saturation does not decrease degree, since a torsion sheaf has effective divisorial first Chern class. The chosen subsheaf is semistable, and every subsheaf of its torsion-free quotient has strictly smaller slope. Induction on rank gives the filtration. [S3:390–398]"

The lattice section is stated. states it: "The pushforward of our extension agrees with a trivial bundle away from $D$. We show that this agreement forces a nonnegative expression in the Chern characters of its restriction to $D$. [S3:454–456]"

The variance expression is stated. states it: "For $F=\bigoplus_{i=1}^N\mathcal O_D(a_i)$, this is the ordinary variance of the integers $a_i$. It need not be nonnegative for arbitrary sheaves. The expression is unchanged by twisting $F$ by $\mathcal O_D(b)$. [S3:463–465]"

The numerical section opens. opens it: "We first compute the contribution of one semistable factor. [S3:543]"

The Riemann--Roch extension is stated. states it: "On each smooth projective surface, finite locally free resolutions extend Riemann–Roch additively to coherent sheaves [S3:547–548]"

and by "This covers the possibly non-locally-free sheaves $G$ and $f_*G$ below; we compare their Euler characteristics, without requiring the finite morphism $f$ to be smooth. [S3:549–551]"

The surface construction is stated. states it: "We construct a family of smooth projective surfaces from which we will choose one violating the inequality established above. The construction uses the six lines joining four points of the plane, followed by a cover obtained by taking roots of their ratios. The same line arrangement provides the sections needed for an ample globally generated divisor on the cover. This choice of arrangement and polarization is the complete-quadrangle construction [S4:4–9]"

The proposition is the numerical target. gives it: "For each prime $n\geq3$, there is a smooth integral projective complex surface $X$ with an ample globally generated divisor $H$ such that \[ H^2=5n^3,\qquad K_X^2-2c_2(X)=n^3(n^2-10). \] [S4:13–17]"

The method is stated. states it: "We prove the proposition by constructing the cover, checking its local coordinates, and then finding sections of the required polarization. [S4:20–21]" adds: "The covering construction goes back to Hirzebruch's work on line [S4:22]"

The counterexample is instantiated. instantiates it: "Take the surface and polarization of Proposition   with $n=7$. Their invariants are \[ H^2=5\cdot7^3=1715,\qquad K_X^2-2c_2(X)=39\cdot7^3=13377>10290=6H^2. \] [S3:633–638]"

The deduction is stated. states it: "The ring $R(X,H)$ is a complete Noetherian normal local domain of dimension three, with residue field $\mathbb C$, by Section  . If it had a nonzero finite module of depth three, Theorem   would give the opposite numerical inequality. Thus it has no such module. [S3:639–643]"

The affine-local corollary is given. gives it: "Let $X$ and $H$ be the surface and polarization constructed in Proposition   for $n=7$, and put \[ T=T(X,H),\qquad \mathfrak n=T_>0. \] Then $T$ is a finitely generated graded three-dimensional $\mathbb C$-domain, $\mathfrak n$ is maximal with $T/\mathfrak n=\mathbb C$, and the three-dimensional local domain $T_{\mathfrak n}$ has no nonzero finitely generated maximal Cohen–Macaulay module. [S3:647–655]"

The corollary proof is stated. [S3:670–674] states it: "Suppose that $M$ is a nonzero finite $R_0$-module of depth three, and choose an $M$-regular sequence $z_1,z_2,z_3$ in the maximal ideal of $R_0$. The completion map $R_0\to R$ is faithfully flat, and, since $M$ is finite, its completion satisfies $\widehat M\cong M\otimes_{R_0}R$ [S3:670–673]"

and by "This is a finite nonzero $R$-module. Put $M_0=M$ and $M_i=M/(z_1,\ldots,z_i)M$ for $1\leq i\leq3$. Nakayama's lemma gives $M_i\ne0$ successively. [S3:674–676]"

and by "The images of the $z_i$ lie in the maximal ideal of $R$, so they form an $\widehat M$-regular sequence of length three. Hence $\depth_R\widehat M\geq3$. For a nonzero finite module over a Noetherian local ring, depth is at most the dimension of its support [S3:688–691]"

and by "which here is at most $\dim R=3$. Thus $\widehat M$ has depth three, contradicting the completed-ring conclusion just proved for $R=R(X,H)$. [S3:691–693]"

## Section skeleton

- `build/paper.tex` [S3]
- `build/surface.tex` [S4]
- `build/references.bib` [S5]

## Comparison with the formalized statement

The scope note states the formalized claim. says: "The small Cohen–Macaulay module conjecture asks whether every complete local domain has a nonzero finitely generated maximal Cohen–Macaulay module. The linked formalization verifies only the ring-theoretic candidate: there exists a three-dimensional complete Noetherian integrally closed local domain over $\mathbb C$ whose residue field is $\mathbb C$. [S6:9]"

The scope note states what is not formalized. says: "It does not prove that this ring lacks a nonzero finitely generated maximal Cohen–Macaulay module, or the paper's counterexample essentially of finite type. [S6:11]"

The declaration is `OAI.SmallCM.candidate_ring_properties` at `lean/OAI/AlgebraicGeometry/SurfaceCones/CandidateRing.lean:16` [S7:16]. The comparator stub carries `sorry` at `lean/ComparatorChallenges/SurfaceConeCandidateSupport.lean:14` [S8:14].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 471 |
| S2 | [`preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/README.md`](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/README.md) | 18 | Title, date |
| S3 | [`preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/paper.tex`](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/paper.tex) | 698 | Abstract, theorems, proof overview, sections |
| S4 | [`preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/surface.tex`](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/surface.tex) | 337 | Surface construction |
| S5 | [`preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/references.bib`](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/references.bib) | 213 | Bibliography entries |
| S6 | [`lean/docs/195.md`](../../../lean/docs/195.md) | 17 | Scope |
| S7 | [`lean/OAI/AlgebraicGeometry/SurfaceCones/CandidateRing.lean`](../../../lean/OAI/AlgebraicGeometry/SurfaceCones/CandidateRing.lean) | 29 | Declaration |
| S8 | [`lean/ComparatorChallenges/SurfaceConeCandidateSupport.lean`](../../../lean/ComparatorChallenges/SurfaceConeCandidateSupport.lean) | 18 | Comparator stub |

## Bibliography

- André, Yves, La conjecture du facteur direct (2018)
- Anghel, Cristian, Smooth Counterexamples to the Eisenbud–Schreyer–Weyman Ulrich Existence Problem (2026)
- Anghel, Cristian, Polarized varieties without arithmetically Cohen–Macaulay bundles and section rings without graded maximal Cohen–Macaulay modules in characteristic zero (2026)
- The Stacks Project Authors, The Stacks Project (2026)
- Beauville, Arnaud, Ulrich bundles: to be or not to be (2017)
- Behrend, Kai, Donaldson–Thomas type invariants via microlocal geometry (2009)
- Bhatt, Bhargav, Hochster, Mel, Ma, Linquan, Lim Cohen–Macaulay sequences of modules (2026)
- Bhatt, Bhargav, On the non-existence of small Cohen–Macaulay algebras (2014)
- Chen, Liang, A local cohomology obstruction to small Cohen–Macaulay modules (2026)
- Chen, Xuemiao, Sun, Song, Algebraic tangent cones of reflexive sheaves (2020)
- Eisenbud, David, Schreyer, Frank-Olaf, Resultants and Chow forms via exterior syzygies (2003)
- Hartshorne, Robin, Algebraic Geometry (1977)
- Hirzebruch, Friedrich, Arrangements of lines and algebraic surfaces (1983)
- Hochster, Melvin, Homological conjectures and lim Cohen–Macaulay sequences (2017)
- Hochster, Melvin, Huneke, Craig, Infinite integral extensions and big Cohen–Macaulay algebras (1992)
- Hochster, Melvin, Yao, Yongwei, Frobenius splitting, strong $F$-regularity, and small Cohen–Macaulay modules (2023)
- Hochster, Melvin, Topics in the Homological Theory of Modules over Commutative Rings (1975)
- Hochster, Melvin, Cohen–Macaulay modules (1973)
- Huybrechts, Daniel, Lehn, Manfred, The Geometry of Moduli Spaces of Sheaves (1997)
