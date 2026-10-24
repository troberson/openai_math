[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 052](../../index/algebraic-and-complex-geometry/052-tangent-bundle-splittings-and-universal-covers.md)

# 052 — Tangent-bundle splittings and universal covers

[Index page](../../index/algebraic-and-complex-geometry/052-tangent-bundle-splittings-and-universal-covers.md)

## Original CONTENTS.md summary

 carries the family entry:

> A splitting of the tangent bundle of a compact Kähler manifold into two integrable holomorphic subbundles induces a compatible product decomposition of its universal cover, proving the two-summand form of Beauville's splitting conjecture. On smooth rationally connected projective manifolds, both summands are automatically integrable, establishing Höring's conjecture and the corresponding product decomposition.

The entry links the two manuscripts as "Kähler universal-cover splitting [S1:180]" and "Integrability on rationally connected manifolds [S1:180]" .

The first manuscript's title is `Universal-cover splitting for compact Kähler manifolds` [S2:1].

The README dates it 2026-09-23 [S2:5].

The second manuscript's title is `Integrability of split tangent bundles on rationally connected manifolds` [S18:1].

The README dates it 2026-09-23 [S18:5].

## Undergraduate summary

A product of complex manifolds has a tangent bundle split into the pullbacks of its factors' tangent bundles. The converse starts from a specified decomposition of the tangent bundle and asks whether the infinitesimal factors come from a product. A necessary local condition is integrability: the holomorphic local sections of each summand must be closed under the Lie bracket.

The first manuscript's abstract states the universal-cover result. [S3:48–52] says: "We prove the two-summand form of Beauville's compatible splitting conjecture. If the tangent bundle of a compact connected Kähler manifold decomposes into two integrable holomorphic subbundles of positive rank, then its ordinary universal cover admits a product decomposition whose factor tangent bundles are the lifted specified summands."

The second manuscript's abstract states the integrability result. [S19:45–50] says: "We prove that both summands of every specified holomorphic splitting of the tangent bundle of a smooth rationally connected projective complex manifold into two positive-rank subbundles are integrable. This proves Höring's conjecture on rationally connected projective manifolds. Höring's product theorem then gives a product decomposition compatible with the specified splitting."

The first manuscript's theorem names the splitting and the product. [S4:101–115] gives it: "Let $X$ be a compact connected Kähler manifold of complex dimension $n\geq2$, and let \[ T_X=E_1\oplus E_2 \] be a specified decomposition into integrable holomorphic subbundles of positive ranks $r_1,r_2$. If $\pi:\widetilde X\to X$ is the ordinary universal covering map, there are connected simply connected complex manifolds $Y_1,Y_2$ and a biholomorphism $\Phi:\widetilde X\to Y_1\times Y_2$ such that \[ \mathrm d\Phi(\pi^*E_i)=\pr_i^*T_{Y_i}\qquad(i=1,2), \] where $\mathrm d\pi$ identifies $T_{\widetilde X}$ with $\pi^*T_X$. In particular, $\dim_\mathbb C Y_i=r_i$."

The second manuscript's theorem is the integrability statement. gives it: "Let \(X\) be a smooth connected projective complex manifold of dimension at least two. Suppose that two general points of \(X\) lie on the image of a morphism \(\mathbb P^1\to X\). For every specified holomorphic decomposition \[ T_X=E_1\oplus E_2 \] into subbundles of positive rank, both \(E_1\) and \(E_2\) are integrable. [S20:22–28]"

## Graduate summary

The first manuscript opens with the converse question. states it: "If a complex manifold is a product, its holomorphic tangent bundle is the direct sum of the tangent bundles of the factors. The converse starts with a specified holomorphic decomposition \[ T_X=E_1\oplus E_2 \] and asks whether the infinitesimal factors come from a product on the universal cover. Compatibility with the given subbundles is part of the question: an abstract product decomposition need not realize the specified embeddings of $E_1$ and $E_2$ into $T_X$. [S4:3–12]"

Integrability is defined. defines it: "A subbundle is _integrable_ if its local holomorphic sections are closed under the Lie bracket. When both summands are integrable, holomorphic Frobenius gives simultaneous local product coordinates. The problem is to continue these local products globally. [S4:13–16]"

The de Rham analogy is stated. states it: "A holomorphic splitting supplies no complete metric making the distributions parallel. Compactness makes every smooth metric complete, but it does not turn the given foliations into parallel distributions. The missing step is therefore a continuation theorem for the specified local products. [S4:21–25]"

Beauville's conjecture is recorded. [S4:29–31] records it: "Beauville formulated the compatible universal-cover conjecture for compact Kähler manifolds with integrable partial sums of the tangent summands"

The Kähler--Einstein case is recorded. [S4:34–37] records it: "In the Kähler–Einstein case, Beauville refines an earlier splitting result of Yau, as he explains in his introduction. For two summands, the partial-sum condition means precisely that both are integrable."

The compatible-product distinction is illustrated. illustrates it: "The distinction between a product and a compatible product is already visible in Beauville's example on $A\times\mathbb P^1$, where $A$ is an abelian surface [S4:41–43]" continues: "Take independent translation-invariant vector fields $U,V$ on $A$ and vector fields $S,T$ on $\mathbb P^1$ with $[S,T]\ne0$, viewed as fields on the product. The rank-two subbundle spanned by $U+S,V+T$ complements $T_{\mathbb P^1}$, but is not integrable: its two generators have the nonzero vertical bracket $[S,T]$. Thus even an underlying product need not realize a specified tangent splitting. [S4:43–49]"

Druel's projective result is recorded. records it: "Several later results establish global continuation under additional geometric hypotheses. Druel treats projective manifolds whose tangent bundle is a sum of line bundles, with the relevant partial sums integrable, and obtains automatic integrability in the minimal projective case [S4:51–55]"

The line-summand case is recorded. [S4:55–56] records it: "Brunella, Pereira, and Touzet treat the case of a line summand with integrable complement on a compact Kähler manifold"

Their proof method is recorded. records it: "Their work also gives uniformization results when the tangent bundle is a sum of line bundles. Their proof uses leafwise Poincaré metrics and transverse invariant metrics to control continuation. [S4:57–60]"

The Hermitian-flat case is recorded. records it: "In higher rank, Pereira and Touzet obtain a compatible Euclidean factor when one involutive direct summand is Hermitian flat [S4:63–64]"

The numerically-flat case is recorded. records it: "Druel, Pereira, Pym, and Touzet show that a regular foliation with numerically flat tangent bundle—meaning that the bundle and its dual are nef—is Hermitian flat and admits an integrable complement, again producing a compatible Euclidean factor [S4:65–68]"

The compact-leaf case is recorded. records it: "A different continuation mechanism applies when a foliation has a compact leaf. Druel, Pereira, Pym, and Touzet prove compatible universal-cover splitting when one foliation has a compact leaf with finite holonomy [S4:70–73]"

Their proof is recorded. records it: "Their argument uses global Reeb stability and a flat Ehresmann connection. Our proof replaces these additional flatness or leaf hypotheses by extension estimates for maps adapted to the two distributions. [S4:73–76]"

The projective integrability result is recorded. [S4:78–80] records it: "In the projective setting, integrability and product decomposition are distinct issues. Höring proves automatic integrability for split tangent bundles on non-uniruled projective manifolds"

His proof is recorded. records it: "His proof combines the positivity theorem for cotangent quotients of Campana and Peternell [S4:81–82]"

and by "with Demailly's integrability theorem for holomorphic forms valued in the inverse of a pseudoeffective line bundle [S4:83–85]"

The Fano-type result is recorded. records it: "His recent work proves algebraic integrability for tangent summands on normal $\mathbf Q$-factorial projective klt varieties of Fano type; its product corollary, which does not require $\mathbf Q$-factoriality, gives compatible products after finite quasi-étale covers [S4:85–89]"

The companion is named. names it: "on a smooth connected rationally connected projective complex manifold, both summands of every specified holomorphic splitting $T_X=E_1\oplus E_2$ into positive-rank subbundles are integrable. [S4:92–94]"

The relation is stated. [S4:95–98] states it: "These results address the geometry that forces a splitting to define foliations. In our main theorem integrability is an explicit hypothesis, while the ambient manifold is only assumed to be compact Kähler."

The theorem discussion is stated. states it: "Theorem   proves the two-summand form of Beauville's compatible splitting conjecture. Its factors are the universal covers of the intrinsic leaves through a common point. The leaves and factors can be noncompact. The conclusion is about the ordinary universal cover; it does not assert that a finite cover of $X$ is a product. If a summand has rank zero, the corresponding factor is a point, so the positive-rank formulation removes only the trivial case. [S4:118–124]"

The nef-and-big setting is defined. defines it: "For a smooth projective manifold, a line bundle is _nef_ if it has nonnegative degree on every curve, and it is _big_ if its sections have maximal asymptotic growth. When $K_X$ is nef and big, its pluricanonical sections define a birational contraction $f:X\to Z$ to the canonical model. We call $X^0=f^{-1}(Z_{\mathrm{reg}})$, the inverse image of the smooth locus of $Z$, the _regular canonical locus_. [S4:142–147]"

The metric argument is stated. [S4:144–173] states it: "When $K_X$ is ample, the negative Kähler–Einstein metric and Beauville's theorem already give this conclusion. For nef and big $K_X$, we use the canonical Kähler–Einstein approximation on a smooth crepant resolution, as developed by Song. The integrated squared second fundamental forms of the supplied summands are $O(\varepsilon)$ along the approximation. Their limit vanishes on the regular canonical locus, where the limiting metric makes both summands parallel. The holomorphic Frobenius obstructions then vanish on all of $X$. This supplies the precise hypothesis needed to apply Theorem  ."

The extension problem is stated. states it: "Local product coordinates alone do not show that a path in one foliation can be transported all the way along a path in the other. We first solve that extension problem for holomorphic maps, and then pass to continuous paths. A holomorphic _box_ in two scalar parameters is a map $f$ whose $s$-derivative lies in $E_1$ and whose $t$-derivative lies in $E_2$. In a simultaneous product chart it has the separated form $(f_1(s),f_2(t))$. We do not impose an immersion or full-rank condition. [S4:181–187]"

The Hartogs step is stated. [S4:189–199] states it: "The first analytic step fills a Hartogs figure by a holomorphic box (Proposition  ). Ivashkovich's theorem gives a meromorphic extension to the envelope of holomorphy. The separate tangencies then exclude positive-dimensional fibres of its graph. If a first target coordinate varied along such a fibre, fixing that coordinate together with $s$ would give an isolated level at a general fibre point. Nearby ordinary graph points instead lie on one-dimensional levels, because the same coordinate is independent of $t$. A compact local analytic level would result, which is impossible in a coordinate ball. The argument works for every summand rank and for boxes with deficient rank."

The boundary step is stated. [S4:201–211] states it: "The second step crosses a smooth convex boundary at which the complex tangent has nonzero components in both parameter directions (Proposition  ). Bounded projections onto $E_1$ and $E_2$ compare the normal and tangential speeds of the box. Stokes' theorem for a Kähler form then bounds the areas of shrinking complex tangent disks. Among many disjoint annuli, one has small area; a local derivative rescaling argument gives a small image. Product coordinates on that image build a Hartogs shell whose size exceeds the remaining distance to the boundary. The first step fills it. Closedness of the Kähler form enters the area estimate, while its metric need not make the two summands orthogonal."

The grids are stated. states them: "These extension results combine two holomorphic disk axes into a box on their entire bidisk. A finite coordinate construction proves holomorphic dependence on additional parameters, yielding full polydisk boxes (Section  ). This is stronger than continuation of individual germs: after transport, an edge still has a holomorphic representative on its whole original parameter polydisk. Consequently a finite rectangular grid combines arbitrary continuous plaque paths, and a second grid realizes any continuous path as the diagonal of a rectangle (Section  ). The rectangles continue both the local product map and its inverse. Monodromy and basepoint-matched covering lifts then give inverse biholomorphisms on the simply connected covers. [S4:213–224]"

The neighborhood theorem is stated. states it: "The canonical contraction also permits a different continuation method. We develop it in the appendices because it supplies a useful neighborhood theorem for singular projective sets as well as another proof of Corollary  . If $P$ is a compact simply connected projective set in a smooth projective manifold with complementary integrable tangent subbundles, and every two points of $P$ are joined by rational chains, ordinary local crossing extends to a holomorphic map $c:U\times U\to M$ on a neighborhood of the whole set $P$ [S4:228–235]"

The appendix proof is stated. [S4:238–246] states it: "The proof first fills products of rational curves, using meromorphic Hartogs extension and the same complementary-tangency obstruction to exceptional curves. It then uses proper stable-map spaces, semialgebraic path lifting, and monodromy to continue _ambient_ germs near the possibly singular or reducible set $P$. For the canonical contraction, Hacon–McKernan's rational-chain theorem and Takayama's local simple-connectedness theorem provide the required fibre topology. Song's metric completion supplies a continuous pseudodistance that collapses exactly those fibres."

The crossings are stated. states them: "Crossings are separately nonexpanding for this pseudodistance, and a finite grid gives path rectangles even for paths contained in a collapsed fibre. No length bound on those paths is required. [S4:247–249]"

The organization is recorded. records it: "The main proof occupies Sections  – . Section   proves the metric estimate and the nef-and-big application. Appendices  –  give the alternative continuation mechanism in its dependency order. All manifolds and varieties are complex. All covers and fundamental groups are taken in the ordinary topology, and leaves carry their intrinsic manifold topology. [S4:251–257]"

The second manuscript opens with the same converse. opens it: "A product of complex manifolds has a tangent bundle split into the pullbacks of the tangent bundles of its factors. A converse must keep track of more than the abstract bundles. For a specified decomposition \[ T_X=E_1\oplus E_2, \] the embeddings of \(E_1\) and \(E_2\) in \(T_X\) are part of the data, and a compatible product must identify these subbundles with its factor directions. A necessary local condition is _integrability_: the holomorphic local sections of each \(E_i\) must be closed under the Lie bracket. [S20:3–13]"

Rational connectedness is defined. defines it: "We prove that rational connectedness forces this local condition. Here and below, ``two general points'' means all pairs in some nonempty Zariski open subset of \(X\times X\). A smooth connected projective complex manifold is rationally connected if two general points lie on the image of a morphism \(\mathbb P^1\to X\). [S20:15–19]"

The theorem's scope is stated. states it: "The theorem has no further rank or positivity hypothesis. It proves the smooth rationally connected assertion formulated in [S20:31–32]"

The product corollary is stated. [S20:33–34] states it: "Höring's earlier product theorem then answers the global question for the same specified splitting."

Höring's product theorem applies. [S20:18–55] applies it: "rationally connected projective complex manifold with a specified splitting of its tangent bundle and at least one integrable summand. By  , these hypotheses hold. His theorem gives an isomorphism with a product that identifies the specified summands with the factor tangent bundles. Each factor is smooth. It is projective because its realization as a slice of the product is a closed complex submanifold of \(X\), and a projective embedding of \(X\) restricts to an embedding of that slice. [S20:48–55]"

Rational connectedness rules out the counterexample. states it: "Rational connectedness rules out that example and supplies the abundance of rational curves used in our proof. [S20:64–66]"

The low-rank results are recorded. records them: "Several earlier results establish compatible products under positivity or rank assumptions. Campana and Peternell treated Fano manifolds with a two-summand splitting when one summand has rank one or two, and hence every two-summand splitting on a Fano manifold of dimension at most five [S20:68–71]"

The integrability corollary is recorded. records it: "showed that, for a rationally connected projective manifold, integrability of one summand already gives a compatible product. [S20:73–75]"

The conjecture is recorded. records it: "He then isolated the remaining question by conjecturing that at least one summand is integrable [S20:75–76]"

The low-rank theorem is recorded. records it: "His later low-rank result applies to a uniruled projective manifold whose tangent bundle splits into summands all of rank at most two, and proves that at least one of them is integrable [S20:77–80]"

The Fano-type theorem is recorded. records it: "integrability with algebraic leaves for split tangent sheaves on normal \(\mathbb Q\)-factorial projective klt varieties of Fano type. In the smooth Fano case it yields an actual compatible product [S20:83–85]"

The positivity condition is removed. states it: "The present theorem removes this positivity condition for smooth rationally connected manifolds. Smoothness matters: [S20:86–87]"

The singular example is recorded. records it: "gives a singular rationally connected example with a nonintegrable summand. [S20:88–89]"

The consequences are named. [S20:89–92] names them: "Section   applies the smooth theorem to general fibers of the rationally connected quotient, supplying the integrability premise in Höring's structure theorems for uniruled compact Kähler manifolds."

The construction is stated. states it: "The construction that drives the proof does not require rational connectedness. Given any holomorphic map \(g:\mathbb P^1\to X\) into a smooth projective manifold with a split tangent bundle, we construct \[ F:\mathbb P^1\times\mathbb P^1\longrightarrow X,\qquad F(s,s)=g(s), \] with the first factor direction tangent to \(E_1\) and the second tangent to \(E_2\). We call \(F\) a _tangent box_. The name records these tangencies; the map may have critical points and need not give local coordinates. [S20:96–105]"

The projectors are stated. states them: "Write \(P_i:T_X\to E_i\subset T_X\) for the holomorphic projectors defined by the splitting. The diagonal first carries a formal solution. In coordinates \(u=s\), \(v=t-s\), the equation \(\partial_v\widehat F=P_2(\widehat F)\partial_u\widehat F\) recursively separates the derivative of \(g\) into its two summands. The positive normal bundle of the diagonal then bounds the number of global formal sections of a twisted line bundle. Comparing that bound with pairs of polynomial sections forces the formal projective coordinate ratios to be rational. A local cancellation makes these ratios holomorphic near a diagonal patch. Finally, on a resolution of the rational map, the two tangency identities force every exceptional curve to be contracted. The resulting map is holomorphic on the entire product. [S20:107–119]"

The partial connection is stated. states it: "The splitting also provides the projected-bracket partial connection \(\nabla^i_\xi e=P_i[\xi,e]\) on \(E_i\) in directions of the complementary summand. On a tangent box it gives transport along the fibers of \(\operatornamepr_i\), which vary the complementary factor, and hence \[ F^*E_i\simeq\operatornamepr_i^*(g^*E_i), \] normalized to be the identity on the diagonal. Thus, on a factor curve, the corresponding summand retains the bundle \(g^*E_i\), while the complementary summand is trivial. [S20:123–132]"

The last step is stated. states it: "Rational connectedness enters only in the last step. A two-point family of rational curves supplies sections of \(g^*E_i\) that vanish at one marked point and span the summand at another. Applying the bracket tensor \(\bigwedge^2E_i\to E_j\) to two such sections on a factor curve gives a section of a trivial bundle on \(\mathbb P^1\). It is constant and vanishes at the first mark, so it vanishes at the second. The spanning property then kills the bracket tensor on an open set of \(X\), and hence everywhere. [S20:134–141]"

The antecedent is recorded. records it: "the tangent box supplies the trivial complementary target in arbitrary rank. [S20:142–143]"

The organization is recorded. records it: "constructs tangent boxes through the formal Cauchy problem, rational reconstruction, and removal of indeterminacy.   establishes the bundle identifications, and   proves  . The rational-quotient consequence follows in  . Appendix   proves the required point-blowup resolution for a surface, and Appendix   derives the two-point family directly from rational connectedness. [S20:147–154]"

## Section skeleton

Manuscript A:

- `build/main.tex` [S3]
- `build/intro.tex` [S4]
- `build/prelim.tex` [S5]
- `build/canonical.tex` [S6]
- `build/boxes.tex` [S7]
- `build/hartogs.tex` [S8]
- `build/boundary.tex` [S9]
- `build/global.tex` [S10]
- `build/appendices/01-collapsed-metric.tex` [S12]
- `build/appendices/02-rational-boxes.tex` [S13]
- `build/appendices/03-neighborhood-crossing.tex` [S14]
- `build/appendices/04-metric-globalization.tex` [S15]
- `build/figures/boundary-scales.tex` [S16]
- `build/figures/grid.tex` [S17]
- `build/references.tex` [S11]

Manuscript B:

- `build/main.tex` [S19]
- `build/sections/introduction.tex` [S20]
- `build/sections/surface.tex` [S21]
- `build/sections/transport.tex` [S22]
- `build/sections/vanishing.tex` [S23]
- `build/sections/variation.tex` [S24]
- `build/sections/boxes.tex` [S25]
- `build/sections/consequences.tex` [S26]
- `build/figures/tangent-box.tex` [S28]
- `build/references.tex` [S27]

## Comparison with the formalized statement

The scope note states the formalized claim. says: "The formalized result gives an affirmative answer for a compact connected Kähler manifold whose tangent bundle splits into two positive-rank, integrable holomorphic subbundles. The universal cover is a product of connected simply connected complex manifolds of the prescribed dimensions, and the differential identifies the two tangent factors with the original summands. [S29:10]"

The scope note states what is not formalized. says: "Both integrability assumptions are required. Automatic integrability and the paper's additional corollaries are not included. [S29:12]"

The scope note states the second formalized claim. [S29:10–14] says: "The formalization proves integrability of both summands in a holomorphic splitting of the tangent bundle of a rationally connected projective manifold. More precisely, for a compact connected complex manifold of dimension at least two with a projective embedding witnessing rational connectedness, each positive-rank summand of a holomorphic tangent-bundle splitting is integrable. The paper's compatible product decomposition is a separate consequence, outside this selected statement. [S29:14]"

The declaration is `OAI.UniversalCoverSplitting.main` at `lean/OAI/Geometry/KahlerSplitting/Main.lean:14` [S30:14]. The comparator stubs carry `sorry` at `lean/ComparatorChallenges/KahlerSplitting.lean:133` [S31:133] and `lean/ComparatorChallenges/SplitTangentIntegrability.lean:136` [S32:136].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 180 |
| S2 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/README.md`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/README.md) | 18 | Manuscript 1 title, date |
| S3 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/main.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/main.tex) | 69 | Abstract, lines 48–52 |
| S4 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/intro.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/intro.tex) | 257 | Introduction: theorem, history, proof strategy |
| S5 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/prelim.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/prelim.tex) | 77 | Preliminaries |
| S6 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/canonical.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/canonical.tex) | 190 | Canonical metric |
| S7 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/boxes.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/boxes.tex) | 167 | Boxes |
| S8 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/hartogs.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/hartogs.tex) | 160 | Hartogs |
| S9 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/boundary.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/boundary.tex) | 219 | Boundary |
| S10 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/global.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/global.tex) | 273 | Global |
| S11 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/references.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/references.tex) | 208 | Bibliography entries |
| S12 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/01-collapsed-metric.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/01-collapsed-metric.tex) | 102 | Collapsed metric |
| S13 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/02-rational-boxes.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/02-rational-boxes.tex) | 264 | Rational boxes |
| S14 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/03-neighborhood-crossing.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/03-neighborhood-crossing.tex) | 266 | Neighborhood crossing |
| S15 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/04-metric-globalization.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/appendices/04-metric-globalization.tex) | 268 | Metric globalization |
| S16 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/figures/boundary-scales.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/figures/boundary-scales.tex) | 38 | Figure source |
| S17 | [`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/figures/grid.tex`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/figures/grid.tex) | 56 | Figure source |
| S18 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/README.md`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/README.md) | 18 | Manuscript 2 title, date |
| S19 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/main.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/main.tex) | 62 | Abstract, lines 45–50 |
| S20 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/introduction.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/introduction.tex) | 154 | Introduction: theorem, history, proof strategy |
| S21 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/surface.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/surface.tex) | 121 | Surface resolution |
| S22 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/transport.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/transport.tex) | 95 | Transport |
| S23 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/vanishing.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/vanishing.tex) | 76 | Vanishing |
| S24 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/variation.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/variation.tex) | 105 | Variation |
| S25 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/boxes.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/boxes.tex) | 487 | Boxes |
| S26 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/consequences.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/consequences.tex) | 61 | Consequences |
| S27 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/references.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/references.tex) | 79 | Bibliography entries |
| S28 | [`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/figures/tangent-box.tex`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/figures/tangent-box.tex) | 30 | Figure source |
| S29 | [`lean/docs/052.md`](../../../lean/docs/052.md) | 21 | Scope |
| S30 | [`lean/OAI/Geometry/KahlerSplitting/Main.lean`](../../../lean/OAI/Geometry/KahlerSplitting/Main.lean) | 43 | Declaration |
| S31 | [`lean/ComparatorChallenges/KahlerSplitting.lean`](../../../lean/ComparatorChallenges/KahlerSplitting.lean) | 139 | Comparator stub |
| S32 | [`lean/ComparatorChallenges/SplitTangentIntegrability.lean`](../../../lean/ComparatorChallenges/SplitTangentIntegrability.lean) | 142 | Comparator stub |

## Bibliography

- Arnaud Beauville, _Complex Algebraic Surfaces_, second edition, London Mathematical Society Student Texts, vol. 34, Cambridge University Press, Cambridge, 1996. doi:10.1017/CBO9780511623936.
- Arnaud Beauville, _Complex manifolds with split tangent bundle_, in Thomas Peternell and Frank-Olaf Schreyer (eds.), _Complex Analysis and Algebraic Geometry: A Volume in Memory of Michael Schneider_, de Gruyter, Berlin, 2000, pp. 61–70. doi:10.1515/9783110806090-004.
- A. Beauville, _Complex algebraic surfaces_, second edition, London Mathematical Society Student Texts **34**, Cambridge University Press, Cambridge, 1996. doi:10.1017/CBO9780511623936.
- A. Beauville, _Complex manifolds with split tangent bundle_, in _Complex Analysis and Algebraic Geometry_, de Gruyter, Berlin, 2000, pp. 61–70. arXiv:math/9809033v2.
- Jacek Bochnak, Michel Coste, and Marie-Françoise Roy, _Real Algebraic Geometry_, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3. Folge, vol. 36, Springer-Verlag, Berlin, 1998. doi:10.1007/978-3-662-03718-8.
- R. Brody, _Compact manifolds and hyperbolicity_, Trans. Amer. Math. Soc. **235** (1978), 213–219. doi:10.1090/S0002-9947-1978-0470252-3.
- Marco Brunella, Jorge Vitório Pereira, and Frédéric Touzet, _Kähler manifolds with split tangent bundle_, Bulletin de la Société Mathématique de France **134** (2006), no. 2, 241–252. doi:10.24033/bsmf.2507.
- L. Bădescu, _Algebraic Barth–Lefschetz theorems_, Nagoya Math. J. **142** (1996), 17–38. doi:10.1017/S0027763000005626.
- Michel Coste, _An Introduction to O-minimal Geometry_, lecture notes, November 1999.  .
- Jean-Pierre Demailly, _On the Frobenius integrability of certain holomorphic $p$-forms_, in _Complex Geometry_, Springer, Berlin, 2002, pp. 93–98. doi:10.1007/978-3-642-56202-0\_6.
- J.-P. Demailly, _Complex Analytic and Differential Geometry_, manuscript, version of June 21, 2012.  .
- S. Druel, _Variétés algébriques dont le fibré tangent est totalement décomposé_, J. Reine Angew. Math. **522** (2000), 161–171. arXiv:math/9901138v2.
- S. Druel, J. V. Pereira, B. Pym, and F. Touzet, _A global Weinstein splitting theorem for holomorphic Poisson manifolds_, Geom. Topol. **26** (2022), no. 6, 2831–2853. doi:10.2140/gt.2022.26.2831.
- Stéphane Druel, Jorge Vitório Pereira, Brent Pym, and Frédéric Touzet, _Numerically flat foliations and holomorphic Poisson geometry_, preprint, 2024. arXiv:2411.08806v1.
- Ichiro Enoki, _Stability and negativity for tangent sheaves of minimal Kähler spaces_, in _Geometry and Analysis on Manifolds_, Lecture Notes in Mathematics, vol. 1339, Springer, Berlin, 1988, pp. 118–126. doi:10.1007/BFb0083051.
- Henri Guenancia, _Semistability of the tangent sheaf of singular varieties_, Algebraic Geometry **3** (2016), no. 5, 508–542. doi:10.14231/AG-2016-024.
- Andreas Höring, _Uniruled varieties with split tangent bundle_, Mathematische Zeitschrift **256** (2007), no. 3, 465–479. doi:10.1007/s00209-006-0072-5; arXiv:math/0505327v3.
- Andreas Höring, _Fano varieties with split tangent sheaf_, preprint, 2026. arXiv:2602.15427v1.
- A. Höring, _Uniruled varieties with split tangent bundle_, arXiv:math/0505327v3. Published in Math. Z. **256** (2007), 465–479. The title and theorem numbering used here follow the preprint.
- A. Höring, _The structure of uniruled manifolds with split tangent bundle_, Osaka J. Math. **45** (2008), no. 4, 1067–1084. Published text. Numbering and the fibration convention used here follow this version.
- A. Höring, _Fano varieties with split tangent sheaf_, preprint, February 17, 2026. arXiv:2602.15427v1.
- S. M. Ivashkovich, _The Hartogs-type extension theorem for meromorphic maps into compact Kähler manifolds_, Invent. Math. **109** (1992), 47–54. doi:10.1007/BF01232018.
- S. Ivashkovich, _Extra extension properties of equidimensional holomorphic mappings: results and open questions_, preprint, 2008. arXiv:0810.4588v2.
- Dennis M. DeTurck and Jerry L. Kazdan, _Some regularity theorems in Riemannian geometry_, Annales Scientifiques de l'École Normale Supérieure (4) **14** (1981), no. 3, 249–260. doi:10.24033/asens.1405.
- J. Kollár, _Rationally connected varieties over local fields_, Ann. of Math. (2) **150** (1999), no. 1, 357–367. doi:10.2307/121107.
- J. Kollár, Y. Miyaoka, and S. Mori, _Rationally connected varieties_, J. Algebraic Geom. **1** (1992), no. 3, 429–448.
- H. Hironaka and H. Matsumura, _Formal functions and formal embeddings_, J. Math. Soc. Japan **20** (1968), nos. 1–2, 52–82. doi:10.2969/jmsj/02010052.
- Christopher D. Hacon and James McKernan, _On Shokurov's rational connectedness conjecture_, Duke Mathematical Journal **138** (2007), no. 1, 119–136. doi:10.1215/S0012-7094-07-13813-4; arXiv:math/0504330v2.
- János Kollár and Shigefumi Mori, _Birational Geometry of Algebraic Varieties_, Cambridge Tracts in Mathematics, vol. 134, Cambridge University Press, Cambridge, 1998. doi:10.1017/CBO9780511662560.
- OpenAI, _Integrability of split tangent bundles on rationally connected manifolds_, OpenAI Math Release preprint OAI:Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026, 2026.
- William Fulton and Rahul Pandharipande, _Notes on stable maps and quantum cohomology_, in János Kollár, Robert Lazarsfeld, and David R. Morrison (eds.), _Algebraic Geometry—Santa Cruz 1995_, Proceedings of Symposia in Pure Mathematics, vol. 62, part 2, American Mathematical Society, Providence, RI, 1997, pp. 45–96. arXiv:alg-geom/9608011.
- Frédéric Campana and Thomas Peternell, _Geometric stability of the cotangent bundle and the universal cover of a projective manifold_, with an appendix by Matei Toma, Bull. Soc. Math. France **139** (2011), no. 1, 41–74. doi:10.24033/bsmf.2599.
- F. Campana and T. Peternell, _Projective manifolds with splitting tangent bundle, I_, Math. Z. **241** (2002), no. 3, 613–637. doi:10.1007/s00209-002-0435-5. Theorem numbering follows arXiv:math/0101198v1.
- Joël Merker and Egmont Porten, _The Hartogs extension theorem on $(n-1)$-complete complex spaces_, Journal für die reine und angewandte Mathematik **637** (2009), 23–39. doi:10.1515/CRELLE.2009.088.
- G. de Rham, _Sur la réductibilité d'un espace de Riemann_, Comment. Math. Helv. **26** (1952), 328–344. doi:10.1007/BF02564308.
- Jean-Pierre Serre, _Géométrie algébrique et géométrie analytique_, Annales de l'Institut Fourier **6** (1956), 1–42. doi:10.5802/aif.59.
- Yusuke Nakamura and Kohsuke Shibata, _A counterexample to the PIA conjecture for minimal log discrepancies_, Duke Mathematical Journal **175** (2026), no. 10, 1715–1736. arXiv:2404.06164v4.
- Jian Song, _Riemannian geometry of Kähler–Einstein currents_, preprint, 2014. arXiv:1404.0445v1.
- Shigeharu Takayama, _Local simple connectedness of resolutions of log-terminal singularities_, International Journal of Mathematics **14** (2003), no. 8, 825–836. doi:10.1142/S0129167X0300196X.
- J. V. Pereira and F. Touzet, _Foliations with vanishing Chern classes_, Bull. Braz. Math. Soc. (N.S.) **44** (2013), no. 4, 731–754. arXiv:1210.5916v1.
- Shing-Tung Yau, _A splitting theorem and an algebraic geometric characterization of locally Hermitian symmetric spaces_, Communications in Analysis and Geometry **1** (1993), 473–486.
