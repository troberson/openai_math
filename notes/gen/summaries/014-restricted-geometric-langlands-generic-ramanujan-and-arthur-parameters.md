[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 014](../index/number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md)

# 014 — Restricted geometric Langlands, generic Ramanujan and Arthur parameters

[Index page](../index/number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md)

## Original CONTENTS.md summary

The release names the family "Restricted geometric Langlands, global Arthur enhancements, and generic Ramanujan [S1:332]" ; the ledger title is the shorter "Restricted geometric Langlands, generic Ramanujan and Arthur parameters [S43:15]" . The entry opens 

> Proves the restricted geometric Langlands equivalence for connected reductive groups on smooth projective connected curves over $`\overline{\mathbb F}_q`$ under the four stated Lie-theoretic characteristic hypotheses. [S1:332]

Over an arbitrary algebraically closed field the entry adds "the same conclusion holds assuming additionally that *p* is very good for the group and $`p\nmid |W_G|`$ [S1:332]" , and it closes 

> Assuming the finite-level Ramanujan–Arthur decomposition, constructs global Arthur enhancements of occurring cuspidal excursion parameters for split connected semisimple groups at full finite level, recovering the given parameters by diagonal specialization on the entire Weil group, including inertia. [S1:332]

The triage record files the family as eight papers, notes that "Ramanujan is unconditional [S42:129]" for the exceptional groups, and records the Arthur half as constructed "assuming the finite-level Ramanujan–Arthur decomposition [S42:131–132]" — "The `conditional` tag is genuine here. [S42:132]" [S42:127–132]

The Arthur-enhancement manuscript's blurb 

> Under the finite-level Ramanujan–Arthur decomposition stated in Theorem 1.1, we construct a global Arthur enhancement for every occurring cuspidal excursion parameter at a specified full finite level for a split connected semisimple group over a global function field. A single algebraic SL*2* and a commuting Weil centralizer map recover the given parameter by diagonal specialization on the entire Weil group, including inertia. The result does not assert ellipticity, Arthur-packet classification, or a multiplicity formula. [S1:341]

The decomposition manuscript's blurb 

> We prove rational and $`\overline{\mathbb Q}_\ell`$ decompositions of cuspidal automorphic functions for split semisimple groups over global function fields into subspaces indexed by nilpotent orbits of the dual group. The decompositions hold at every full finite level, with arbitrary divisor multiplicities. Each summand is governed by the same orbit at every unramified place and every complex embedding. At trivial level this proves Conjectures 3.4.5 and 3.4.6 of Gaitsgory–Lafforgue–Raskin. For split connected adjoint absolutely simple groups, we also prove that a cuspidal automorphic representation with one generic unramified local component is tempered at every unramified place. Thus globally generic cuspidal representations in this scope satisfy the unramified part of the generalized Ramanujan conjecture. [S1:359]

The equivalence manuscript's blurb begins 

> We prove the $`\overline{\mathbb Q}_\ell`$-linear restricted geometric Langlands equivalence for smooth projective connected curves and connected reductive groups in characteristic [S1:377]

and ends 

> Over arbitrary algebraically closed fields, we assume these conditions and additionally that *p* is very good and does not divide the Weyl-group order. This proves Gaitsgory–Raskin's full-support conjecture [S1:377]

The Weil-eigensheaf manuscript's blurb begins 

> We construct nonzero perverse Weil Hecke eigensheaves for SL*n* with Borel level at one marked point, after a finite extension of the field of constants. [S1:404]

and ends 

> The full multi-leg eigenstructure is Frobenius compatible with the prescribed arithmetic eigenvalue, and the geometric sheaf has parabolic nilpotent singular support. [S1:404]

The four blurbs quoted above are the two headline claims of each cluster. The remaining four are the rationality of the canonical unramified Arthur filtration [S1:350], temperedness at ramified places for globally generic exceptional groups [S1:368], constructible tame Hecke eigensheaves [S1:386], and tame Hecke eigensheaves with several marked points [S1:395]. The release overview carries the same entry with the eight manuscript links at 104 [S2:104].

## Undergraduate summary

Eight manuscripts, two clusters, one correspondence. Geometric Langlands over a function field asks for a dictionary between automorphic objects on the group side and *local systems* — representations of the fundamental group — on the spectral side. The family attacks that dictionary from both ends, and the two halves are visibly different in style. The first half is arithmetic: it talks about cuspidal automorphic representations, Arthur parameters, and the Ramanujan property, over a global function field. The second half is geometric: it constructs the automorphic-side objects — Hecke eigensheaves — directly on the moduli stack of $G$-bundles, over a curve in positive characteristic.

The arithmetic cluster is built around a decomposition. An Arthur parameter is a homomorphism from the Weil group times a copy of $\mathrm{SL}_2$ into the $L$-group, and the nilpotent orbit of the image of that $\mathrm{SL}_2$ is a coarse label for how far the parameter is from being tempered. The decomposition manuscript splits the space of cuspidal automorphic functions into pieces indexed by those nilpotent orbits, at every finite level, and shows the same orbit governs each piece at every unramified place. From that, Ramanujan follows for the representations whose unramified component is *generic*: genericity forces the orbit label to be the trivial one. The enhancement manuscript then goes the other way, producing global Arthur parameters of the kind Arthur's conjecture predicts, and the temperedness manuscript removes the unramified-only restriction for exceptional groups.

The geometric cluster is built around existence. The automorphic side of the correspondence is a category of Hecke eigensheaves, and the spectral side one wants is not the whole category of local systems but a restricted one: local systems whose singular support is the parabolic nilpotent cone. The equivalence manuscript proves the resulting *restricted* equivalence in two characteristic regimes, and the other three manuscripts construct nonzero eigensheaves in that class — at Borel level with one marked point, then with several marked points, and finally with the Frobenius structure that makes the eigensheaf arithmetic rather than merely geometric.

**The proofs run in two directions at once.** On the arithmetic side, the decomposition is established at full finite level by controlling the summands at every place simultaneously, and the enhancement is then assembled from a single algebraic $\mathrm{SL}_2$ together with a commuting map from the Weil centralizer, so that specializing diagonally recovers the prescribed parameter on the whole Weil group — inertia included, which is what makes the parameter an Arthur parameter and not merely a Langlands parameter. On the geometric side, the construction degenerates the curve to a separating node, uses a $T$-torsor of enhanced flags to slice the relevant strata, detects the eigensheaf by coherence of the Hecke system, truncates perverse cohomology to keep the singular support inside the nilpotent cone, and descends the result back to the original curve; the several-leg case adds a cyclic-stabilizer argument and a Witt-vector lifting step, and the arithmetic case adds a finite extension of the field of constants so that the eigenstructure is Frobenius-compatible.

## Graduate summary

**The decomposition, and the Ramanujan corollary.** Manuscript 3 fixes a curve over a finite field, a split semisimple group, a level $D$ and a coefficient field, and writes $C_D$ for the space of cuspidal automorphic functions at that level. Its main theorem is the direct-sum statement [S13:108–118]: "For every $X,G,D,\ell$ as above, the natural addition maps [S13:109]" the orbit-indexed sums into $C_D$, and those maps "are isomorphisms. The sums range over the nilpotent orbits of $\widehat G$. [S13:117]" Taking the trivial level settles the conjectures it was written for: "Taking $D=0$ resolves Conjecture 3.4.6 of Gaitsgory–Lafforgue–Raskin positively, as well as its equivalent rational form, Conjecture 3.4.5. [S13:120–122]" The Ramanujan statement is a corollary, not the theorem [S13:141–152]: "In particular, every globally generic cuspidal automorphic representation of $G(\mathbb A_F)$ is tempered at every unramified place. [S13:149–151]" Its scope is stated with the same care: "Here unramified means spherical for a hyperspecial maximal compact subgroup. The conclusion is only about these local components. [S13:154–155]" 

**The enhancement, and what it assumes.** Manuscript 1 states its main theorem under a hypothesis imported from manuscript 3, quoted in its own environment title as "Finite-level Ramanujan–Arthur decomposition [S4:155]" . The hypothesis says "For every occurring excursion character $\nu$, there is a unique nilpotent $L$-orbit [S4:157–158]" governing the local Arthur form of the parameter, with "The same orbit occurs at every $x$. [S4:170–171]" Manuscript 1 is explicit about the gap between that hypothesis and its conclusion: "The theorem is a statement about good-place semisimple classes. [S4:174]" and "Our result supplies the global homomorphism and retains the specified character $\nu$. [S4:177–178]" Its theorem opens "Assume Theorem . [S4:181]" and produces an algebraic homomorphism from $\mathrm{SL}_{2,k}$ into the $L$-group together with a continuous homomorphism from the Weil group into the centralizer of its image, both defined over a finite extension of $\mathbb Q_\ell$, subject to "The Zariski closure of $\tau_\nu(\Gamma)$ is reductive. [S4:198]" , an absolute-value-one condition on the eigenvalues at closed points, and a diagonal specialization identity recovering $\sigma_\nu$ for every element of $\Gamma$. The environment closes "The centralizer is the full algebraic centralizer; it may be disconnected. [S4:211–212]" 

**Rationality of the filtration.** Manuscript 2 works under four Lie-theoretic hypotheses, "The following four conditions hold. [S8:42]" — an invariant nondegenerate form on the Lie algebra, an isomorphism of invariant rings for each Levi and maximal torus, "The scheme-theoretic centralizer in $H$ of every semisimple element of $\mathfrak h$ is a Levi subgroup. [S8:55–56]" , and a parabolic containment condition for nilpotents over every extension. Its theorem [S8:118–127] begins "Under Assumption , for every prime $\ell\ne\mathrm{char}(\mathbb F_q)$ and every closed invariant $Y\subset\widehat{\mathcal N}$, the natural map [S8:119–121]" and ends "is an isomorphism. The intersection is taken inside $\mathcal A_E$. [S8:126]" What it does not assume is listed: "No Hecke-finiteness or cuspidality condition is imposed. [S8:129]" and "The theorem does not require $X(\mathbb F_q)$ to be nonempty. [S8:129–130]" Where the two clusters meet is the cuspidal subspace: the filtration "identifies this filtration with the sums of the rational cuspidal Arthur summands of [S8:134–135]" manuscript 3, indexed by the orbit labels in $Y$ [S8:134–136].

**Temperedness at ramified places.** Manuscript 4 removes the unramified-only restriction for the exceptional types [S18:23–30]: "Let $G/F$ be split connected adjoint absolutely simple of type $G_2$, $F_4$, $E_6$, $E_7$, or $E_8$. [S18:24–25]" and "If $\pi=\bigotimes'_v\pi_v$ is a complex globally generic cuspidal automorphic representation of $G(\mathbb A_F)$, then $\pi_v$ is tempered for every place $v$. [S18:25–28]" [S18:26–28] The scope sentence is unusually strong: "There is no restriction on the characteristic of $F$, the ramification depth, or the local representation type. [S18:28–29]" It extends the unramified result of manuscript 3 — "Ramanujan theorem of the companion paper \cite[Corollary 1.2]UnramifiedRamanujan. [S18:21]" — and names the obstruction it has to clear: "The distinction between spherical and ramified components is substantial. [S18:32–33]" because "at a ramified place a Weil–Deligne parameter also contains a nilpotent monodromy operator. [S18:34–35]" 

**The equivalence, and its two regimes.** Manuscript 5 imposes four Lie-theoretic conditions under the heading "Common characteristic assumptions [S23:117]" , stating "The following conditions hold for $G/k$. [S23:118]" a nondegenerate $G$-invariant form whose restriction to every Levi center is nondegenerate, Chevalley restriction as an isomorphism for every Levi, "The scheme-theoretic centralizer in $G$ of every semisimple element of $\mathfrak g$ is a Levi subgroup. [S28:37–38]" , and a parabolic containment condition for nilpotents over every extension. It locates them precisely: "The first three conditions are those of \cite[\S14.4.1]AGKRRV; the last is the additional condition of \cite[\S D.1.1]AGKRRV. These are the assumptions referenced by \cite[\S0.1.9]GR. [S23:137–139]" The theorem is then proved in two regimes with different hypotheses. Regime A, titled "Regime A: finite-field descent [S23:143]" , requires a model over $\mathbb F_q$ and says "No additional restriction on the order of the Weyl group is imposed in this regime. [S23:152–153]" Regime B, titled "Regime B: arbitrary algebraically closed base [S23:156]" , drops the descent and adds the characteristic restrictions: "The field $k$ is any algebraically closed field of characteristic $p>0$. Hypothesis holds, $p$ is very good for $G$, and $p\nmid |W_G|$. No finite-field descent of $X$ is assumed. [S23:158–160]" The manuscript spells out very good — "for type $A_n$, $p\nmid n+1$; for $B_n,C_n,D_n$, $p\ne2$; for $G_2,F_4,E_6,E_7$, $p\ne2,3$; and for $E_8$, $p\ne2,3,5$, on every irreducible factor. A torus has no such exclusions. [S23:163–166]" — and refuses to merge the regimes: "The two regimes have distinct proofs of the needed Lie-theoretic statement; neither is used as a substitute for the other. [S23:168–170]" 

The theorem itself is the full-support statement, titled "Full support [S23:186]" "Under either Hypothesis or Hypothesis , the inclusion [S23:187–188]" $Y'\subset Y$ "is equality as spectral prestacks. Consequently the given functor is a $\mathrm{QCoh}(Y)$-linear equivalence [S23:189–190]" [S23:188–190] between the sheaves on $\mathrm{Bun}_G$ with nilpotent singular support and $\mathrm{IndCoh}_{\mathrm{Nilp}}(Y)$. Its relation to the conjecture it resolves is bounded in the next paragraph: "This proves Conjecture 1.3.10 of in the two displayed regimes. [S23:198–199]" and "The present theorem concerns the restricted theory with its stated characteristic hypotheses. [S23:202–203]" 

A second theorem moves the statement to rational coefficients, titled "Rational spectral support [S23:240]" "For the rational datum just specified, every nonempty open-and-closed substack $U\subset Y_0$ has [S23:241–242]" nonvanishing tensor product , so "Consequently, if $Y'_0\subset Y_0$ is an open-and-closed support union whose complementary structure idempotent acts by zero on $\mathcal C_0$, then $Y'_0=Y_0$ [S23:246–248]" as spectral prestacks. Its scope sentence is the sharpest boundary in the cluster: "The conclusion concerns the entire rational spectral prestack, without identifying its components with rational points. [S23:253–254]" and "No rational extension of regime B is asserted here. [S23:258–259]" 

**The eigensheaf existence theorem.** Manuscript 6 is the root of the constructive half and reuses the same four Lie-theoretic conditions, including "The scheme-theoretic centralizer in $G$ of every semisimple element of $\mathfrak g$ is a Levi subgroup. [S23:129–130]" It defines the two terms it quantifies over — "Here semisimple means geometrically conjugate into a toral Lie algebra, and nilpotent means that the geometric adjoint-orbit closure contains zero. [S28:44–45]" — and states what it does not require: "We impose no additional condition that $p$ be prime to the order of a Weyl group. [S28:46–47]" Its main theorem [S28:105–123] asserts existence under those hypotheses: "Assume – . For every Zariski-dense parameter satisfying , there is a nonzero locally constructible perverse geometric $E$-adic sheaf $M$ on $\mathcal A$ such that [S28:106–109]" its singular support lies in the parabolic nilpotent cone, and "For every finite set $I$ and every family $(V_i)_{i\in I}$, it carries isomorphisms [S28:113–114]" identifying the Hecke transform with the external tensor product built from the parameter, "natural in the representations and coherently compatible with the tensor unit, convolution, permutations of legs, and fusion along every collision diagonal. [S28:120–122]" The eigenstructure is required for every collision diagonal at once, which is the content of the coherence clause and the reason the construction is not a one-leg statement.

**Several marked points, and how the hypotheses loosen.** Manuscript 7 specializes to $G=\mathrm{SL}_n$ and tightens the characteristic inequality: "Let $n\ge2$, let $k=\overline{\mathbb F}_q$ have characteristic $p>n$, and fix a prime $\ell\ne p$. [S33:6]" It fixes $s$ marked points, "Set $G=\mathrm{SL}_n$ and $\check G=\mathrm{PGL}_{n,E}$, and let $B\subset G$ be the upper-triangular Borel subgroup. [S33:10]" takes a Zariski-dense parameter into $\mathrm{PGL}_n(L)$ that kills wild inertia at each marked point and is unipotent on inertia via a chosen tame quotient, and is explicit that the nilpotent monodromy data need not be nonzero: "No regularity is assumed for $N_i$; it may be zero. [S33:21]" Its theorem [S33:40–52] gives "For every parameter satisfying the preceding hypotheses, there is a nonzero locally constructible perverse geometric $E$-adic sheaf $M$ on $\mathcal A$ with [S33:41]" singular support in the parabolic nilpotent cone $\Lambda_D$, plus "For every finite set $I$ and every family $(V_i)_{i\in I}$, it has isomorphisms [S33:45]" of the Hecke transform with the external product, "natural in the representations and coherent for the tensor unit, convolution, permutations, and fusion on every collision diagonal. [S33:51]" The scope note is the reason manuscript 8 exists: "The parameter and eigensheaf are geometric: the statement does not require a Frobenius structure. [S33:54]" 

**Adding the Frobenius structure.** Manuscript 8 is the arithmetic upgrade, and it says what that costs. "A Weil structure over $\mathbb F_{q^m}$ means an isomorphism between the $q^m$-Frobenius pullback of the geometric sheaf and the sheaf itself. [S39:31–32]" and "We require the eigenisomorphisms to respect this structure and the Frobenius structure on the parameter. [S39:33–34]" Its theorem [S39:36–52] keeps $p>n$ — "Let $n\geq2$, let $\mathbb F_q$ have characteristic $p>n$, let $\ell\ne p$, [S39:37]" — adds a genus floor, "Let $X_0/\mathbb F_q$ be a smooth projective geometrically connected curve of genus at least two, with $x_0\in X_0(\mathbb F_q)$, and put $U_0=X_0\setminus\{x_0\}$. [S39:38–40]" [S39:38–39], and strengthens the monodromy condition from arbitrary nilpotent to "for a regular nilpotent $N$. [S39:50]" The conclusion is existence after a base change: "There are an integer $m\geq1$ and a nonzero $E$-adic Weil sheaf $M_0$ on [S39:54]" the Borel-level bundle stack over $\mathbb F_{q^m}$, "whose geometric pullback $M$ is locally constructible perverse and has singular support in $\Lambda_{\mathrm{par}}$. [S39:58–59]" with "for every finite set $I$ and every family $V_i\in\mathrm{Rep}_E(\mathrm{PGL}_n)$ there are isomorphisms of Weil sheaves [S39:61–62]" that are "natural in the representations and coherent for the unit, convolution, permutations, and all fusion diagonals. [S39:67–68]" Two scope sentences explain the price of the arithmetic statement: "The Frobenius structure is required on the entire eigenstructure, rather than only on the underlying perverse sheaf. [S39:73–74]" and "The finite extension in the theorem arises when a point on an auxiliary bundle stack is made invariant under a power of Frobenius. [S39:74–76]" 

**The moves.**

1. Decompose at full level. Manuscript 3 controls the cuspidal space at every level $D$ at once, indexing summands by nilpotent orbits of $\check G$ and tracking the same orbit label at every unramified place, so that genericity can be read off locally and the trivial orbit forced [S13:108–118].
2. Read Ramanujan off the decomposition. The temperedness statement is derived from the orbit labelling rather than from a global argument, and its scope is left at the unramified places [S13:141–155].
3. Build the enhancement under the decomposition. Manuscript 1 takes the orbit unicity as a hypothesis, then constructs one algebraic $\mathrm{SL}_{2,k}$ and one commuting Weil-centralizer map whose diagonal specialization recovers the parameter on all of $\Gamma$, inertia included [S4:180–213].
4. Make the filtration rational. Manuscript 2 proves the rational isomorphism under the four Lie-theoretic conditions and identifies the cuspidal part with manuscript 3's rational Arthur summands, which is what makes the orbit labelling available over $\mathbb Q$ and not only over $\overline{\mathbb Q}_\ell$ [S8:118–136].
5. Remove the unramified restriction. Manuscript 4 treats the ramified case for the exceptional types, where the Weil--Deligne parameter carries nilpotent monodromy that the spherical Satake picture does not see [S18:23–35].
6. Degenerate the curve to create level. Manuscript 6 "first constructs an eigensheaf with Borel level in characteristic zero, and then specializes it to the curve of Theorem . [S28:185–186]" and inside that construction "a degeneration to a separating node creates the level structure. [S28:188]" Two copies of a pointed curve are joined at their marked points, a parameter with inverse boundary monodromy is placed on the second component, and the compatible finite quotients glue on twisted nodal models and lift to the smooth generic curve; "Their inverse limit is an unramified dense parameter there, to which we apply the characteristic-zero unramified correspondence. [S28:196–197]" 
7. Slice with enhanced flags. "The special fiber introduces enhanced flags. [S28:201]" The stack $\mathcal A^+$ of bundles with an $R_u(B)$-reduction maps to $\mathcal A$ as "a $T$-torsor [S28:203]" , and "Nearby cycles, pullback to the product, and restriction to one enhanced factor give a nonzero eigencomplex on $\mathcal A_1^+$. [S28:208–209]" Pushing forward and truncating gives the eigensheaf: "Taking a nonzero perverse cohomology, applying $q_!$, and taking perverse cohomology once more produce the ordinary-flag perverse eigensheaf. [S28:209–211]" 
8. Detect, and keep nonzero. Manuscript 7 states the two arguments that the several-point case needs: "A local calculation with two Hecke modifications detects covectors outside the nilpotent cone. [S33:72]" and, because "nearby cycles of a nonzero complex can vanish [S33:60]" , the same calculation over a trait proves nonvanishing when the closure of the nonzero generic stalks meets the special fiber. Exactness of the fixed-point Hecke functors near a dense parameter is what lets perverse cohomology preserve the tensor and collision comparisons .
9. Descend, then make Frobenius-equivariant. The curve with its marked points is lifted over the Witt ring $W(k)$ so the finite quotients of the parameter extend over root stacks [S33:74]. Manuscript 8 then names what equivariance costs: "There are two extra difficulties in making the geometric construction equivariant. First, an invariant parameter need not make an arbitrarily chosen geometric eigenobject visibly invariant. Second, the two boundary parameters at a separating node must be glued by a conjugation that preserves both Frobenius and compact image. [S39:136–140]" 

**What the family does not say.** Manuscript 1 states its own boundary: "The result does not assert ellipticity, Arthur-packet classification, or a multiplicity formula. [S1:341]" It also situates itself against a stronger announced result — "A global enhancement in the everywhere unramified setting has already been announced by Raskin as part of joint work with Gaitsgory and Lafforgue [S4:271–273]" — so its contribution is the full finite level with the excursion character retained, not the unramified case. Manuscript 5 proves the restricted equivalence, not the full one: the full characteristic-zero equivalence and the general linear groups are inputs, "established inputs from Main Theorem 1.3.9 of that paper. [S23:201]" Manuscripts 6, 7 and 8 construct eigensheaves; they do not prove the correspondence, and manuscript 7 is explicit that its object carries no Frobenius structure . Manuscript 4 is restricted to split adjoint absolutely simple exceptional groups, and manuscript 3's Ramanujan corollary reaches only the unramified components .

**The conditional tag, and the absence of a named resolution.** The ledger records this family with `conditional=1` and `resolves_named=0` , and the triage record explains the first from the manuscript text: the enhancements are constructed "assuming the finite-level Ramanujan–Arthur decomposition [S42:131–132]" — "The `conditional` tag is genuine here. [S42:132]" [S42:127–132] Manuscript 1's own theorem opens "Assume Theorem . [S4:181]" , and the theorem it assumes is manuscript 3's: the statement is `\cite[Theorem~1.1]{Parent}` inside manuscript 1's finite-level Ramanujan--Arthur decomposition theorem [S4:155–156], and the `Parent` bibliography entry is a release link to manuscript 3's directory [S4:5420–5424]. So the family contains an unconditional Ramanujan statement for the exceptional groups and an enhancement result that is conditional on a theorem proved elsewhere in the same family. Nothing in the family is presented as resolving a named conjecture of the literature: the conjectures it settles are Gaitsgory–Lafforgue–Raskin 3.4.5 and 3.4.6 and Gaitsgory–Raskin's full-support conjecture , and the release blurb for the enhancement paper names no conjecture at all . Nothing about this family is machine-checked: the ledger records 0 of 8 manuscripts formalized, no scope note, no comparator challenge, and no `main_results` entry .

## History of the conjecture

Arthur's conjectures are the origin of the arithmetic half of the family. "Arthur's conjectures explain the non-tempered part of the discrete spectrum by supplementing a tempered parameter with an algebraic $\mathrm{SL}_2$ whose image commutes with it. [S4:226–228]" "This structure appeared in his Maryland lectures, published in 1984, and was developed in his subsequent formulation of unipotent automorphic representations [S4:228–230]" "The corresponding global conjectures also concern packets and their multiplicities; the existence of a commuting pair is one part of that larger structure. [S4:235–237]" The commuting pair is therefore an old object, and manuscript 1's contribution is to produce it at full finite level with the excursion data attached, not to propose it.

Function fields supplied the inputs. "Over function fields, Drinfeld's work for $\mathrm{GL}_2$ and Laurent Lafforgue's work for $\mathrm{GL}_n$ realized the Langlands correspondence in the cohomology of shtukas [S4:239–241]" "Laurent Lafforgue's purity theorem for irreducible lisse sheaves with finite-order determinant supplies the weight input used here [S4:243–244]" "Vincent Lafforgue subsequently constructed excursion operators and attached semisimple global parameters to cuspidal automorphic functions for reductive groups at arbitrary finite level [S4:246–248]" "These operators retain invariants of tuples of Galois elements, so the resulting parameter contains more information than its individual unramified Frobenius classes. [S4:250–252]" Vincent Lafforgue's own Arthur conjecture "asks that each occurring parameter arise from an elliptic global Arthur parameter. [S4:254–255]" Manuscript 1 does not prove that conjecture; it proves the existence half of a related statement and says so.

The conjecture the family settles is the one in Gaitsgory–Lafforgue–Raskin. "In the everywhere unramified setting, Gaitsgory–Lafforgue–Raskin formulate the Ramanujan–Arthur decomposition by requiring the same nilpotent-orbit spectral type at every unramified place [S4:257–260]" "They distinguish this condition from support on global Arthur parameters, which is formulated separately in \cite[Section 3.6]history:GLR. [S4:262–264]" "The finite-level theorem of \cite[Theorem 1.1]Parent, recalled in Theorem , supplies the former condition for arbitrary full level. [S4:265–267]" "Passing from that condition to one commuting pair requires compatibility with the complete excursion parameter, [S4:267–268]" The decomposition theorem is manuscript 3's, and manuscript 1's enhancement theorem is stated under it, which is the whole content of the family's `conditional` tag.

Prior (my training data, not this repo). Before this release, the Ramanujan conjecture for function-field cuspidal automorphic forms was open outside the general linear groups: Lafforgue's purity theorem gave weights for $\mathrm{GL}_n$, and the spectral-type formulation in Gaitsgory–Lafforgue–Raskin's 2025 preprint was a set of conjectures, not a theorem. The Beilinson–Drinfeld quantization of the Hitchin system gave eigensheaves for semisimple groups over $\mathbb C$ at unramified level, and the five-paper Geometric Langlands collaboration had established the categorical unramified correspondence in characteristic zero. A positive-characteristic eigensheaf with prescribed ramification at marked points, at finite level, with nilpotent monodromy, was not something I can name a precedent for.

The announced comparison sits at the end of manuscript 1's history section. "That announcement recovers the specified cuspidal excursion parameter from a commuting $W_X\times\mathrm{SL}_2$ parameter and asserts irreducibility of the latter, under the standing characteristic hypotheses of its Section 1.1.1. [S4:275–278]" "Theorem treats arbitrary full finite level under the finite-level decomposition hypothesis. [S4:279–280]" The comparison is stated as a difference of scope, not as a competition.

The eigensheaf half has its own genealogy, recorded in manuscript 7's history section. "The eigensheaf problem originates in Drinfeld's rank-two construction and Laumon's geometric formulation for general linear groups [S34:1–2]" "Frenkel, Gaitsgory, and Vilonen reduced unramified $\mathrm{GL}_n$ eigensheaf existence to a vanishing conjecture [S34:3–4]" "Geometric Satake identifies the local Hecke kernels with representations of the dual group and supplies their tensor and fusion structure [S34:5–7]" "For semisimple groups over $\mathbb C$, Beilinson and Drinfeld constructed eigensheaves from opers by quantizing the Hitchin system [S34:19–20]" "Arinkin, Gaitsgory, Kazhdan, Raskin, Rozenblyum, and Varshavsky introduced the stack of local systems with restricted variation and its action on sheaves with nilpotent singular support [S34:23–25]" "Gaitsgory and Raskin use this framework to formulate the geometric adic correspondence and compare characteristic zero with positive characteristic [S34:26–27]" "The input needed here is the characteristic-zero restricted equivalence \cite[Main Theorem 1.3.9(ii)]GR, through the unramified eigencomplex construction of \cite[Lemma 8.1]CT. [S34:28–30]" "Thus the categorical theory enters on a smooth projective curve before level structures are introduced. [S34:30–32]" [S34:28–32]

Manuscript 7 states precisely what it inherits and what it adds. "Our immediate antecedent is \cite[Theorem 1.1]CT, whose main theorem has one marked point and regular-unipotent monodromy for a broader class of groups. [S34:11–13]" "Here the group is $\mathrm{SL}_n$ with $p>n$, there are several marked points, and every nilpotent boundary logarithm is allowed. [S34:13–14]" The chain inside the family runs the same way: manuscript 5 proves the restricted equivalence, manuscript 6 constructs the eigensheaf under it, manuscripts 7 and 8 extend that construction to several points and to a Frobenius structure, and each of them cites manuscript 6 as its antecedent.

## Consequences

Manuscript 5 lists its own consequences, and they are the load-bearing ones for the geometric half of the family. "Section records three consequences. [S23:205]" "Localizing the given functor at any spectral component gives the corresponding nonzero ind-coherent category. [S23:205–207]" "In regime A, the known primed trace formula becomes the full arithmetic formula using derived geometric Frobenius fixed points. [S23:207–209]" "For an arbitrary parameter, spectral linearity produces a nonzero Hecke eigenobject with coherent tensor and fusion compatibilities. [S23:209–211]" "Its asserted category is ind-constructible and nilpotent; no bounded constructibility or perversity assertion is needed. [S23:211–212]" 

The first is structural: no component of the spectral side is empty. "every connected component $Z\subset Y$ has a nonzero localized automorphic category. [S44:32–34]" "The restriction of the given spectral-linear Langlands functor induces an equivalence [S44:34–35]" Between them these say that the automorphic side has a summand for every spectral component, and the equivalence restricts to it, so the correspondence is not vacuous on any part of the stack.

The second identifies a function space with a geometric one. "The finite-field models $X_0$ and $G_0$ determine geometric $q$-Frobenius. [S44:69–70]" "Define its derived fixed-point stack by [S44:72]" "In particular, an $E$-point includes a Weil structure on the geometric local system. [S44:78–79]" "The left side is the vector space of compactly supported functions on isomorphism classes of rational bundles, regarded as a complex concentrated in degree zero. [S44:91–93]" "The right side uses the ind-coherent dualizing object and ind-coherent global sections on the derived fixed-point stack. [S44:93–94]" The arithmetic trace formula is thereby recovered as ind-coherent sections on a derived fixed-point stack, which is the shape the characteristic-zero theory predicts and which the primed formula only approximated.

The third is the existence of eigenobjects without any finiteness proviso. "every parameter $\sigma:\mathrm{Spec}(E)\to Y$ admits a nonzero object $M_\sigma\in\mathrm{Shv}_{\mathrm{Nilp}}(\mathrm{Bun}_G)$ with a coherent Hecke eigenstructure of eigenvalue $\sigma$. [S44:216–219]" "The assertion concerns the ind-constructible dg category and includes no boundedness, perversity or Weil structure. [S44:221–222]" The last sentence is the honest reading of the result: the eigenobject exists, and its category is the large ind-constructible one.

The arithmetic half pays out differently. Manuscript 3's corollary is the Ramanujan statement for the exceptional groups at unramified places, with the Arthur spectral type fixed across all of them [S13:141–155]; manuscript 4 moves that statement to ramified places, where the parameter has nilpotent monodromy [S18:23–35]; manuscript 2 makes the filtration that carries the decomposition rational, so the labelling exists over $\mathbb Q$ [S8:118–136]; and manuscript 1 attaches the enhancement, under manuscript 3's decomposition as a hypothesis [S4:180–213]. Read together, the four give a Ramanujan-and-Arthur picture for split adjoint exceptional groups over function fields whose enhancement layer is conditional on a theorem inside the same family.

The eigensheaf half pays out as method. Manuscript 6 says plainly where its arguments come from: "The two-Hecke and projective slicing methods follow \cite[Sections 3–7]OpenAIFullSupport2026; we prove their versions for ordinary and enhanced Borel level and the simultaneous torus quotient, [S28:263–266]" and the hard part is keeping the Hecke system intact through the specialization: "Preserving the Hecke system requires more than commuting nearby cycles with a fixed-point operator. [S28:269–270]" "The comparison must retain all moving legs, including collisions, and the maps expressing convolution and fusion. [S28:270–271]" Manuscripts 7 and 8 inherit that machinery and extend it, manuscript 7 to several marked points and arbitrary nilpotent boundary logarithms , manuscript 8 to a Frobenius structure [S39:36–52].

What is left open is stated by the manuscripts themselves. Manuscript 1 does not prove ellipticity, packet classification, or a multiplicity formula [S1:341], so Vincent Lafforgue's Conjecture 12.7 is untouched here [S4:254–255]. Manuscript 5 proves the restricted equivalence under two hypotheses, and the full equivalence is an input rather than a conclusion [S23:201]. Manuscripts 6, 7 and 8 construct eigenobjects and do not prove the correspondence, and manuscript 7's object has no Frobenius structure [S33:54]. None of these consequences is machine-checked: the ledger records 0 of 8 manuscripts formalized for this family, no scope note, no comparator challenge, and no `main_results` entry [S43:15].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Family entry at 332; manuscript blurbs at 341, 350, 359, 368, 377, 386, 395, 404 |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family `\resultentry` at 104 |
| S3 | [`preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/README.md`](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S4 | [`preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/build/manuscript.tex`](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/build/manuscript.tex) | 5465 | Title at 63, abstract at 69–76, `thm:parent` at 155–156, history section at 224–283, `Parent` bibitem at 5420–5424 |
| S5 | [`preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf`](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf) | 23046 | Typeset manuscript, 793,468 bytes |
| S6 | [`preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/README.md`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S7 | [`preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/build/paper.tex`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/build/paper.tex) | 39 | Title at 14, abstract at 20–25, section inputs at 31–37 |
| S8 | [`preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/build/sections/01-introduction.tex) | 280 | Main theorem at 118–136, cuspidal comparison at 129–130 |
| S9 | [`preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/build/references.tex`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/build/references.tex) | 212 | Release links at 158 and 166 |
| S10 | [`preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf) | 18682 | Typeset manuscript, 654,080 bytes |
| S11 | [`preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/README.md`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S12 | [`preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/main.tex`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/main.tex) | 32 | Title at 3–4, abstract at 10–21, bibliography at 30–31 |
| S13 | [`preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/sections/01-introduction.tex) | 334 | Main theorem at 108–118, arithmetic corollary at 141–155 |
| S14 | [`preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/references.bib`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/references.bib) | 646 | Release link to manuscript 2 at 16 |
| S15 | [`preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf) | 21306 | Typeset manuscript, 750,187 bytes |
| S16 | [`preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/README.md`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S17 | [`preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/build/paper.tex`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/build/paper.tex) | 59 | Title at 39, abstract at 45–50, section inputs at 52–57 |
| S18 | [`preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/build/sections/introduction.tex`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/build/sections/introduction.tex) | 172 | Hypotheses at 21, main theorem at 23–35 |
| S19 | [`preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/build/references/bibliography.tex`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/build/references/bibliography.tex) | 179 | Release link to manuscript 3 at 134 |
| S20 | [`preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf) | 11380 | Typeset manuscript, 401,075 bytes |
| S21 | [`preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/README.md`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S22 | [`preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/main.tex`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/main.tex) | 84 | Title at 54, abstract at 60–68, section inputs at 71–79 |
| S23 | [`preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/sections/01-introduction.tex) | 331 | Main theorem at 129–166, scope discussion at 186–212 |
| S24 | [`preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/refs.bib`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/refs.bib) | 270 | Bibliography carrying no release URL |
| S25 | [`preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf) | 16447 | Typeset manuscript, 574,527 bytes |
| S26 | [`preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/README.md`](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S27 | [`preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/build/manuscript/main.tex`](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/build/manuscript/main.tex) | 31 | Title at 3, abstract at 10–17, section inputs at 21–28 |
| S28 | [`preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/build/manuscript/introduction.tex`](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/build/manuscript/introduction.tex) | 318 | Hypotheses at 37–47, main theorem at 105–123, method provenance at 263–271 |
| S29 | [`preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/build/manuscript/references.bib`](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/build/manuscript/references.bib) | 365 | Release link to manuscript 5 at 363 |
| S30 | [`preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/constructible-tame-hecke-eigensheaves-positive-characteristic.pdf`](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/constructible-tame-hecke-eigensheaves-positive-characteristic.pdf) | 19042 | Typeset manuscript, 669,524 bytes |
| S31 | [`preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/README.md`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S32 | [`preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/main.tex`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/main.tex) | 94 | Title at 67, abstract at 73–80, section inputs at 85–93 |
| S33 | [`preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/sections/introduction.tex`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/sections/introduction.tex) | 78 | Hypotheses at 6–21, main theorem at 40–52, scope sentence at 54 |
| S34 | [`preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/sections/history.tex`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/sections/history.tex) | 78 | History subsections at 1–32 |
| S35 | [`preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/references.tex`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/build/references.tex) | 171 | Release link to manuscript 6 at 147 |
| S36 | [`preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf) | 17575 | Typeset manuscript, 614,643 bytes |
| S37 | [`preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/README.md`](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S38 | [`preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/build/main.tex`](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/build/main.tex) | 87 | Title at 61, abstract at 67–73, section inputs at 80–86 |
| S39 | [`preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/build/sections/introduction.tex`](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/build/sections/introduction.tex) | 177 | Weil-structure definition at 31–34, main theorem at 36–52, scope sentences at 73–76 |
| S40 | [`preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/build/references.tex`](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/build/references.tex) | 112 | Release link to manuscript 6 at 105 |
| S41 | [`preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/tame-hecke-frobenius.pdf`](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/tame-hecke-frobenius.pdf) | 14342 | Typeset manuscript, 503,521 bytes |
| S42 | [`notes/gen/reports/t0-triage.md`](../../../notes/gen/reports/t0-triage.md) | 897 | Family 014 entry at 127–132 |
| S43 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Family row at 15 |
| S44 | [`preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/sections/08-consequences.tex`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/build/sections/08-consequences.tex) | 267 | Component categories at 20–39, arithmetic formula at 67–95, coherent eigenobjects at 124–223 |

## Bibliography

- Vladimir G. Drinfeld. Langlands' conjecture for $\mathrm{GL}(2)$ over functional fields. In  Proceedings of the International Congress of Mathematicians (Helsinki, 1978), volume 2, pages 565–574. Academia Scientiarum Fennica, Helsinki, 1980.
- Cong Xue. Smoothness of cohomology sheaves of stacks of shtukas. arXiv: 2012.12833v1, 2020.
- Abramovich, Dan, Vistoli, Angelo, Compactifying the space of stable maps (2002)
- Adams, Jeffrey, Taibi, Olivier, Galois and Cartan cohomology of real groups (2016)
- Cong Xue. Finiteness of cohomology groups of stacks of shtukas as modules over Hecke algebras, and applications. { Épijournal de Géométrie Algébrique}, 4, 2020. Article 6, 42 pp.
- Domingo Luna. Slices étales. In  Sur les groupes algébriques, number 33 in Bulletin de la Société Mathématique de France. Mémoire, pages 81–105. Société Mathématique de France, 1973.
- Sam Raskin. Conjectures of Arthur and Ramanujan for unramified automorphic forms: announcement, 2026. Contribution to the 2026 ICM Proceedings; manuscript dated October 12, 2025, updated March 10, 2026.
- Dima Arinkin, Dennis Gaitsgory, David Kazhdan, Sam Raskin, Nick Rozenblyum, and Yakov Varshavsky, _The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support_, arXiv:2010.01906v2, 6 April 2022. .
- Dima Arinkin, Dennis Gaitsgory, David Kazhdan, Sam Raskin, Nick Rozenblyum, and Yakov Varshavsky, _Duality for automorphic sheaves with nilpotent singular support_, arXiv:2012.07665v2, 17 May 2022. .
- Dima Arinkin, Dennis Gaitsgory, David Kazhdan, Sam Raskin, Nick Rozenblyum, and Yakov Varshavsky, _Automorphic functions as the trace of Frobenius_, arXiv:2102.07906v2, 3 June 2022. .
- Arinkin, Dima, Gaitsgory, Dennis, Kazhdan, David and Raskin, Sam, Rozenblyum, Nick, Varshavsky, Yakov, The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support (2022)
- Arinkin, Dima, Gaitsgory, Dennis, Kazhdan, David and Raskin, Sam, Rozenblyum, Nick, Varshavsky, Yakov, Automorphic functions as the trace of Frobenius (2022)
- Arinkin, Dima, Gaitsgory, Dennis, Singular support of coherent sheaves, and the geometric Langlands conjecture (2015)
- Arinkin, Dima, Gaitsgory, Dennis, Kazhdan, David, Raskin, Sam, Rozenblyum, Nick, Varshavsky, Yakov, The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support (2020)
- D. Arinkin, D. Gaitsgory, D. Kazhdan, S. Raskin, N. Rozenblyum, and Y. Varshavsky, _The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support_, preprint, 2020, revised 2022, arXiv:2010.01906v2.
- D. Arinkin, D. Gaitsgory, D. Kazhdan, S. Raskin, N. Rozenblyum, and Y. Varshavsky, _The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support_, arXiv:2010.01906v2, April 6, 2022.
- Arkhipov, Sergey, Bezrukavnikov, Roman, Perverse sheaves on affine flags and Langlands dual group (2009)
- Arkhipov, Sergey, Bezrukavnikov, Roman, Ginzburg, Victor, Quantum groups, the loop Grassmannian, and the Springer resolution (2004)
- Arkhipov, Sergey, Bezrukavnikov, Roman, Perverse sheaves on affine flags and Langlands dual group (2009)
- James Arthur, _Unipotent automorphic representations: conjectures_, Astérisque **171–172** (1989), 13–71. .
- Arthur, James, Unipotent automorphic representations: conjectures (1989)
- J. Arthur, _Unipotent automorphic representations: conjectures_, Astérisque **171–172** (1989), 13–71.
- Tasho Kaletha. Supercuspidal $L$-packets. arXiv:1912.03274v2, 2021.
- Arnaud Eteve and Cong Xue. Nearby cycles commute with proper direct image on stacks of shtukas. arXiv:2409.16474v1, 2024.
- Michael F. Atiyah, _Riemann surfaces and spin structures_, Annales scientifiques de l'École Normale Supérieure (4) **4** (1971), no. 1, 47–62. .
- The Stacks Project Authors, _The Stacks Project_, 2026, Tags 00MA, 00IP, 0A06, and 0BKH, accessed 18 September 2026.
- The Stacks Project Authors, The Stacks Project (2026)
- The Stacks Project Authors, Stacks Project (2026)
- The Stacks Project Authors, _Stacks Project_, 2026. .
- Barrett, Owen, The singular support of an $\ell$-adic sheaf (2024)
- O. Barrett, _The singular support of an $\ell$-adic sheaf_, Tunisian J. Math. **6** (2024), no. 4, 703–734. doi:10.2140/tunis.2024.6.703.
- O. Barrett, _The singular support of an $\ell$-adic sheaf_, Tunisian J. Math. **6** (2024), no. 4, 703–734.
- Michael Bate, Benjamin Martin, and Gerhard Röhrle. A geometric approach to complete reducibility.  Inventiones Mathematicae, 161(1):177–218, 2005.
- Michael Bate, Benjamin Martin, and Gerhard Röhrle. Semisimplification for subgroups of reductive algebraic groups.  Forum of Mathematics, Sigma, 8, 2020. e43, 10 pp.
- Michael Bate, Benjamin Martin, Gerhard Röhrle, and Rudolf Tange. Closed orbits and uniform $S$-instability in geometric invariant theory.  Transactions of the American Mathematical Society, 365(7):3643–3673, 2013.
- Beauville, Arnaud, Laszlo, Yves, Un lemme de descente (1995)
- Beauville, Arnaud, Laszlo, Yves, Un lemme de descente (1995)
- Alexander A. Beilinson, Joseph Bernstein, and Pierre Deligne.  Faisceaux pervers, volume 100 of { Astérisque}. Société Mathématique de France, Paris, 1982.
- Beilinson, A. A., On the derived category of perverse sheaves (1987)
- Beilinson, Alexander, Constructible sheaves are holonomic (2017)
- Beilinson, Alexander, Drinfeld, Vladimir, Quantization of Hitchin's integrable system and Hecke eigensheaves
- Beilinson, Alexander, Constructible sheaves are holonomic (2016)
- A. Beilinson, _Constructible sheaves are holonomic_, Selecta Math. (N.S.) **22** (2016), no. 4, 1797–1819. doi:10.1007/s00029-016-0260-z.
- A. Beilinson, _Constructible sheaves are holonomic_, Selecta Math. (N.S.) **22** (2016), no. 4, 1797–1819.
- A. A. Beilinson, J. Bernstein, and P. Deligne, _Faisceaux pervers_, in _Analyse et topologie sur les espaces singuliers I_, Astérisque **100** (1982), 5–171.
- Belkale, Prakash, Fakhruddin, Najmuddin, Triviality properties of principal bundles on singular curves (2019)
- David Ben-Zvi, Harrison Chen, David Helm, and David Nadler. Coherent Springer theory and the categorical Deligne–Langlands correspondence.  Inventiones Mathematicae, 235:255–344, 2024.
- David Ben-Zvi, Yiannis Sakellaridis, and Akshay Venkatesh, _Relative Langlands duality_, arXiv:2409.04677v1, 7 September 2024. .
- Ben-Zvi, David, Francis, John, Nadler, David, Integral transforms and Drinfeld centers in derived algebraic geometry (2010)
- Ben-Zvi, David, Sakellaridis, Yiannis, Venkatesh, Akshay, Relative Langlands duality (2024)
- Beraldo, Dario, Lin, Kevin, Reeves, Wyatt, Coherent sheaves, sheared D-modules, and Hochschild cochains (2024)
- Bernstein, Joseph, Lapid, Erez, On the meromorphic continuation of Eisenstein series (2024)
- Bezrukavnikov, Roman, Finkelberg, Michael, Equivariant Satake category and Kostant–Whittaker reduction (2008)
- S. Arkhipov and R. Bezrukavnikov, _Perverse sheaves on affine flags and Langlands dual group_, with an appendix by R. Bezrukavnikov and I. Mirković, Israel J. Math. **170** (2009), 135–183. doi:10.1007/s11856-009-0024-y.
- N. uit de Bos, _An explicit geometric Langlands correspondence for the projective line minus four points_, Int. Math. Res. Not. IMRN **2022**, no. 24, 19690–19746. doi:10.1093/imrn/rnab218.
- Michel Brion, _Invariant Hilbert schemes_, arXiv:1102.0198v2, 21 April 2011. .
- Broer, Bram, Line bundles on the cotangent bundle of the flag variety (1993)
- Caprace, Pierre-Emmanuel, Ciobotaru, Corina, Gelfand pairs and strong transitivity for Euclidean buildings (2015)
- Cass, Robert, van den Hove, Thibaud, Scholbach, Jakob, Central motives on parahoric flag varieties (2025)
- H. del Castillo, G. Henniart, and L. Lomelí, _On generic representations of quasi-split reductive groups over local fields of positive characteristic_, preprint, 2024, arXiv:2412.00229.
- Mark Andrea de Cataldo, Thomas J. Haines, and Li Li. Frobenius semisimplicity for convolution morphisms.  Mathematische Zeitschrift, 289(1–2):119–169, 2018. Theorem locators refer to arXiv version 3.
- de Cataldo, Mark Andrea, Haines, Thomas J., Li, Li, Frobenius semisimplicity for convolution morphisms (2018)
- Ciubotaru, Dan, Harris, Michael, On the generalized Ramanujan and Arthur conjectures over function fields (2023)
- Conrad, Brian, Reductive group schemes (2014)
- Conrad, Brian, Reductive group schemes (2014)
- C. Cunningham, S. Dijols, A. Fiori, and Q. Zhang, _Whittaker normalization of $p$-adic ABV-packets and Vogan's conjecture for tempered representations_, Int. Math. Res. Not. IMRN **2025** (2025), no. 20, rnaf316. doi:10.1093/imrn/rnaf316.
- Mirković, Ivan, Vilonen, Kari, Geometric Langlands duality and representations of algebraic groups over commutative rings (2007)
- Mirković, I., Vilonen, K., Geometric Langlands duality and representations of algebraic groups over commutative rings (2018)
- Mirković, Ivan, Vilonen, Kari, Geometric Langlands duality and representations of algebraic groups over commutative rings (2007)
- J.-F. Dat, D. Helm, R. Kurinczuk, and G. Moss, _Finiteness for Hecke algebras of $p$-adic groups_, J. Amer. Math. Soc. **37** (2024), 929–949. doi:10.1090/jams/1034.
- J.-F. Dat, D. Helm, R. Kurinczuk, and G. Moss, _Local Langlands in families: The banal case_, J. Reine Angew. Math., published online 2026. doi:10.1515/crelle-2026-0034.
- Pierre Deligne, _La conjecture de Weil: II_, Publications Mathématiques de l'IHÉS **52** (1980), 137–252. .
- Deligne, Pierre, La conjecture de Weil. II (1980)
- P. Deligne, _Les constantes des équations fonctionnelles des fonctions $L$_, in _Modular Functions of One Variable II_, Lecture Notes in Mathematics **349**, Springer, Berlin, 1973, 501–597. doi:10.1007/978-3-540-37855-6\_7.
- P. Deligne, _La conjecture de Weil. II_, Publ. Math. Inst. Hautes Études Sci. **52** (1980), 137–252. doi:10.1007/BF02684780.
- Dhillon, Gurbir, Taylor, Jeremy, The universal monodromic Arkhipov–Bezrukavnikov equivalence (2025)
- Dhillon, Gurbir, Taylor, Jeremy, Tame local Betti geometric Langlands (2025)
- V. G. Drinfeld, _Proof of the Petersson conjecture for $\mathrm{GL}(2)$ over a global field of characteristic $p$_, Funct. Anal. Appl. **22** (1988), no. 1, 28–43. doi:10.1007/BF01077720.
- Drinfeld, V. G., Simpson, Carlos, $B$-structures on $G$-bundles and local triviality (1995)
- Drinfeld, Vladimir G., Two-dimensional $\ell$-adic representations of the fundamental group of a curve over a finite field and automorphic forms on $\mathrm{GL}(2)$ (1983)
- Drinfeld, Vladimir G., Simpson, Carlos, $B$-structures on $G$-bundles and local triviality (1995)
- A. Beilinson and V. Drinfeld, _Quantization of Hitchin's integrable system and Hecke eigensheaves_, preprint. Authors' manuscript.
- V. G. Drinfeld, _Two-dimensional $\ell$-adic representations of the fundamental group of a curve over a finite field and automorphic forms on $\GL(2)$_, Amer. J. Math. **105** (1983), no. 1, 85–114. doi:10.2307/2374382.
- V. G. Drinfeld, _Two-dimensional $\ell$-adic representations of the fundamental group of a curve over a finite field and automorphic forms on $\mathrm{GL}(2)$_, Amer. J. Math. **105** (1983), no. 1, 85–114.
- Eberhardt, Jens Niklas, Scholbach, Jakob, Integral motivic sheaves and geometric representation theory (2023)
- P. Belkale and N. Fakhruddin, _Triviality properties of principal bundles on singular curves_, Algebraic Geometry **6** (2019), no. 2, 234–259.
- Faltings, Gerd, Stable $G$-bundles and projective connections (1993)
- G. Faltings, _Stable $G$-bundles and projective connections_, J. Algebraic Geom. **2** (1993), no. 3, 507–568.
- Flath, Daniel, Decomposition of representations into tensor products (1979)
- Frenkel, E., Gaitsgory, D., Vilonen, K., On the geometric Langlands conjecture (2001)
- Frenkel, Edward, Gaitsgory, Dennis, Vilonen, Kari, On the geometric Langlands conjecture (2002)
- E. Frenkel, D. Gaitsgory, and K. Vilonen, _On the geometric Langlands conjecture_, J. Amer. Math. Soc. **15** (2002), no. 2, 367–417. doi:10.1090/S0894-0347-01-00388-5.
- E. Frenkel, D. Gaitsgory, and K. Vilonen, _On the geometric Langlands conjecture_, J. Amer. Math. Soc. **15** (2002), no. 2, 367–417.
- Færgeman, Joakim, Motivic realization of rigid $G$-local systems on curves and tamely ramified geometric Langlands (2024)
- J. Færgeman, _Motivic realization of rigid $G$-local systems on curves and tamely ramified geometric Langlands_, preprint, 2024, arXiv:2405.18268v2.
- Dennis Gaitsgory, Vincent Lafforgue, and Sam Raskin. Tempered vs generic automorphic functions and the canonical filtration on automorphic functions, 2026. Version 2, April 14, 2026.
- Dima Arinkin and Dennis Gaitsgory, _Singular support of coherent sheaves and the geometric Langlands conjecture_, Selecta Mathematica, New Series **21** (2015), no. 1, 1–199. . Introduction locators refer to arXiv:1201.6343v4. .
- Vladimir Drinfeld and Dennis Gaitsgory, _On some finiteness questions for algebraic stacks_, Geometric and Functional Analysis **23** (2013), 149–294; arXiv:1108.5351v3, 26 October 2012. .
- Dennis Gaitsgory, _Ind-coherent sheaves_, arXiv:1105.4857v7, 22 September 2012. .
- Dennis Gaitsgory, Vincent Lafforgue, and Sam Raskin, _Tempered vs generic automorphic functions and the canonical filtration on automorphic functions_, arXiv:2603.26925v2, 2026. .
- Gaitsgory, Dennis, Lafforgue, Vincent, Raskin, Sam, Tempered vs generic automorphic functions and the canonical filtration on automorphic functions (2026)
- Gaitsgory, Dennis, Construction of central elements in the affine Hecke algebra via nearby cycles (2001)
- Gaitsgory, Dennis, Raskin, Sam, Geometric Langlands in positive characteristic from characteristic zero (2025)
- Gaitsgory, D., Kazhdan, D., Rozenblyum, N., Varshavsky, Y., A toy model for the Drinfeld–Lafforgue shtuka construction (2022)
- Gaitsgory, Dennis, Raskin, Sam, Proof of the geometric Langlands conjecture I: construction of the functor (2025)
- Gaitsgory, Dennis, Raskin, Sam, Proof of the geometric Langlands conjecture V: the multiplicity one theorem (2026)
- Gaitsgory, Dennis, On a vanishing conjecture appearing in the geometric Langlands correspondence (2004)
- Gaitsgory, Dennis, On a vanishing conjecture appearing in the geometric Langlands correspondence (2004)
- Gaitsgory, Dennis, Raskin, Sam, Geometric Langlands in positive characteristic from characteristic zero (2025)
- Gaitsgory, Dennis, Raskin, Sam, Proof of the geometric Langlands conjecture I: construction of the functor (2024)
- Gaitsgory, Dennis, Construction of central elements in the affine Hecke algebra via nearby cycles (2001)
- D. Gaitsgory, _Construction of central elements in the affine Hecke algebra via nearby cycles_, Invent. Math. **144** (2001), no. 2, 253–280. doi:10.1007/s002220100122.
- D. Gaitsgory, _On a vanishing conjecture appearing in the geometric Langlands correspondence_, Ann. of Math. (2) **160** (2004), no. 2, 617–682. doi:10.4007/annals.2004.160.617.
- D. Gaitsgory, _Construction of central elements in the affine Hecke algebra via nearby cycles_, Invent. Math. **144** (2001), no. 2, 253–280.
- D. Gaitsgory, _On a vanishing conjecture appearing in the geometric Langlands correspondence_, Ann. of Math. (2) **160** (2004), no. 2, 617–682.
- D. Gaitsgory, D. Kazhdan, N. Rozenblyum, and Y. Varshavsky, _A toy model for the Drinfeld–Lafforgue shtuka construction_, arXiv:1908.05420v5, February 7, 2022.
- W. T. Gan, M. Harris, and W. Sawin, with an appendix by R. Beuzart-Plessis, _Local parameters of supercuspidal representations_, Forum Math. Pi **12** (2024), e13, 1–41. doi:10.1017/fmp.2024.10.
- Ginzburg, Victor, Perverse sheaves on a loop group and Langlands' duality (2000)
- Ginzburg, Victor, The global nilpotent variety is Lagrangian (2001)
- V. Ginzburg, _The global nilpotent variety is Lagrangian_, Duke Math. J. **109** (2001), no. 3, 511–519. doi:10.1215/S0012-7094-01-10933-2.
- Haines, Thomas J., Cellular pavings of fibers of convolution morphisms (2025)
- Haines, Thomas J., Kottwitz, Robert E., Prasad, Amritanshu, Iwahori–Hecke algebras (2009)
- Hall, Jack, Rydh, David, Coherent Tannaka duality and algebraicity of Hom-stacks (2019)
- Hall, Jack, Rydh, David, Coherent Tannaka duality and algebraicity of Hom-stacks (2019)
- Hansen, David, Scholze, Peter, Relative perversity (2023)
- Hansen, David, Scholze, Peter, Relative perversity (2023)
- D. Ciubotaru and M. Harris, _On the generalized Ramanujan and Arthur conjectures over function fields_, Ann. of Math. (2) **204** (2026), no. 2, 545–601. doi:10.4007/annals.2026.204.2.3.
- Hemo, Tamir, Richarz, Timo, Scholbach, Jakob, Constructible sheaves on schemes (2023)
- James Arthur. On some problems suggested by the trace formula. In Rebecca Herb, Stephen Kudla, Ronald Lipsman, and Jonathan Rosenberg, editors,  Lie Group Representations II, volume 1041 of  Lecture Notes in Mathematics, pages 1–49. Springer, Berlin, 1984.
- Hoffmann, Norbert, On moduli stacks of $G$-bundles over a curve (2010)
- Marc Hoyois, Sarah Scherotzke, and Nicol\`o Sibilla, _Higher traces, noncommutative motives, and the categorified Chern character_, arXiv:1511.03589v3. .
- The Stacks project authors. The stacks project. , 2026. Tag 0A6A, Lemma 15.101.2(3). Accessed October 3, 2026.
- W. T. Gan and A. Ichino, _The Gross–Prasad conjecture and local theta correspondence_, Invent. Math. **206** (2016), 705–799. doi:10.1007/s00222-016-0662-8.
- Javanpeykar, Ariyan, Krämer, Thomas, Lehn, Christian, Maculan, Marco, The monodromy of families of subvarieties on abelian varieties (2025)
- Jordan, Bruce W., Ribet, Kenneth A., Scholl, Anthony J., Modular curves and {Néron} models of generalized Jacobians (2024)
- Roman Bezrukavnikov and Michael Finkelberg. Equivariant Satake category and Kostant–Whittaker reduction.  Moscow Mathematical Journal, 8(1):39–72, 2008.
- Bernhard Keller, _A-infinity algebras, modules and functor categories_, arXiv:math/0510508v3, 12 February 2006. .
- Lafforgue, Vincent, Introduction to chtoucas for reductive groups and to the global Langlands parameterization (2017)
- Lafforgue, Laurent, Chtoucas de Drinfeld et correspondance de Langlands (2002)
- Lafforgue, Laurent, Noyaux du transfert automorphe de Langlands et formules de Poisson non linéaires (2013)
- A. Genestier and V. Lafforgue, _Chtoucas restreints pour les groupes réductifs et paramétrisation de Langlands locale_, preprint, 2017, revised July 30, 2026, arXiv:1709.00978v3.
- L. Lafforgue, _Chtoucas de Drinfeld et correspondance de Langlands_, Invent. Math. **147** (2002), no. 1, 1–241. doi:10.1007/s002220100174.
- V. Lafforgue, _Chtoucas pour les groupes réductifs et paramétrisation de Langlands globale_, J. Amer. Math. Soc. **31** (2018), no. 3, 719–891. doi:10.1090/jams/897.
- Lang, Serge, Algebraic groups over finite fields (1956)
- Laszlo, Yves, Olsson, Martin, Perverse $t$-structure on Artin stacks (2009)
- Laszlo, Yves, Olsson, Martin, The six operations for sheaves on Artin stacks. II: Adic coefficients (2008)
- Laumon, Gérard, Correspondance de Langlands géométrique pour les corps de fonctions (1987)
- Laumon, Gérard, Un analogue global du c{\^o}ne nilpotent (1988)
- G. Laumon, _Correspondance de Langlands géométrique pour les corps de fonctions_, Duke Math. J. **54** (1987), no. 2, 309–359. doi:10.1215/S0012-7094-87-05418-4.
- G. Laumon, _Un analogue global du c\^one nilpotent_, Duke Math. J. **57** (1988), no. 2, 647–671. doi:10.1215/S0012-7094-88-05729-8.
- G. Laumon, _Correspondance de Langlands géométrique pour les corps de fonctions_, Duke Math. J. **54** (1987), no. 2, 309–359.
- Lee, Ting-Yu, Adjoint quotients of reductive groups (2015)
- Lieblich, Max, Olsson, Martin, Generators and relations for the étale fundamental group (2010)
- Liu, Yifeng, Zheng, Weizhe, Enhanced six operations and base change theorem for higher Artin stacks (2024)
- W. T. Gan and L. Lomelí, _Globalization of supercuspidal representations over function fields and applications_, J. Eur. Math. Soc. **20** (2018), no. 11, 2813–2858. doi:10.4171/JEMS/825.
- L. A. Lomelí, _Functoriality for the classical groups over function fields_, Int. Math. Res. Not. IMRN **2009** (2009), no. 22, 4271–4335. doi:10.1093/imrn/rnp089.
- L. A. Lomelí, _The Langlands–Shahidi method over function fields: Ramanujan Conjecture and Riemann Hypothesis for the unitary groups_, preprint, 2015, arXiv:1507.03625.
- L. A. Lomelí, _Rationality and holomorphy of Langlands–Shahidi $L$-functions over function fields_, Math. Z. **291** (2019), 711–739. doi:10.1007/s00209-018-2100-7.
- Lu, Qing, Zheng, Weizhe, Categorical traces and a relative Lefschetz–Verdier formula (2022)
- Andrew Salmon. Unipotent nearby cycles and the cohomology of shtukas.  Compositio Mathematica, 159(3):590–615, 2023. . Preprint version consulted: arXiv:2106.04768v3.
- R. W. Thomason. The classification of triangulated subcategories.  Compositio Mathematica, 105(1):1–27, 1997.
- Dennis Gaitsgory. Construction of central elements in the affine Hecke algebra via nearby cycles.  Inventiones Mathematicae, 144(2):253–280, 2001.
- Laurent Lafforgue. Chtoucas de Drinfeld et correspondance de Langlands.  Inventiones Mathematicae, 147(1):1–241, 2002.
- Sergey Arkhipov and Roman Bezrukavnikov. Perverse sheaves on affine flags and Langlands dual group.  Israel Journal of Mathematics, 170:135–183, 2009. Section and equation locators refer to arXiv version 6.
- Ivan Mirković and Kari Vilonen. Geometric Langlands duality and representations of algebraic groups over commutative rings.  Annals of Mathematics, 166(1):95–143, 2007.
- Alexander Bertoloni Meli, Naoki Imai, and Alex Youcis. The Jacobson–Morozov morphism for Langlands parameters in the relative setting.  International Mathematics Research Notices, 2024(6):5100–5165, 2024. Statement numbering as in arXiv:2203.01768v3.
- Bertoloni Meli, Alexander, Imai, Naoki, Youcis, Alex, The Jacobson–Morozov morphism for Langlands parameters in the relative setting (2024)
- William M. Goldman and John J. Millson, _The deformation theory of representations of fundamental groups of compact Kähler manifolds_, Publications Mathématiques de l'IHÉS **67** (1988), 43–96. .
- J. S. Milne, _Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field_, Cambridge University Press, 2017. .
- Milne, James S., Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field (2017)
- Milne, J. S., Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field (2022)
- Milne, J. S., Lectures on Étale Cohomology (2013)
- Morris, L. E., Eisenstein series for reductive groups over global function fields. I: The cusp form case (1982)
- Morris, L. E., Eisenstein series for reductive groups over global function fields. II: The general case (1982)
- David Mumford, _Theta characteristics of an algebraic curve_, Annales scientifiques de l'École Normale Supérieure (4) **4** (1971), no. 2, 181–192. .
- Mœglin, Colette, Waldspurger, Jean-Loup, Spectral Decomposition and Eisenstein Series: A Paraphrase of the Scriptures (1995)
- Nadler, David, Yun, Zhiwei, Spectral action in Betti geometric Langlands (2019)
- Nadler, David, Yun, Zhiwei, Automorphic gluing functor in Betti geometric Langlands (2021)
- Yoshinori Namikawa, _Birational geometry for nilpotent orbits_, arXiv:1002.2821v2, 10 March 2010; Handbook of Moduli, vol. III, Advanced Lectures in Mathematics **26** (2013), 1–38. .
- OpenAI. Ramanujan–Arthur Decompositions of Cuspidal Functions at Full Finite Level. OpenAI Math Release preprint OAI:Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026, 2026.
- David Kazhdan and Andrei Okounkov, _On the unramified Eisenstein spectrum_, arXiv:2203.03486v3. . Section and equation locators refer to this version.
- Olsson, Martin C., (Log) twisted curves (2007)
- M. Lieblich and M. Olsson, _Generators and relations for the étale fundamental group_, Pure Appl. Math. Q. **6** (2010), no. 1, 209–243. doi:10.4310/PAMQ.2010.v6.n1.a6.
- M. C. Olsson, _(Log) twisted curves_, Compos. Math. **143** (2007), no. 2, 476–494. doi:10.1112/S0010437X06002442.
- M. Lieblich and M. Olsson, _Generators and relations for the étale fundamental group_, Pure Appl. Math. Q. **6** (2010), no. 1, 209–243.
- M. C. Olsson, _(Log) twisted curves_, Compos. Math. **143** (2007), no. 2, 476–494.
- OpenAI, _Ramanujan–Arthur Decompositions of Cuspidal Functions at Full Finite Level_, OpenAI Math Release preprint OAI:Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026, 2026.
- OpenAI, _The Restricted Geometric Langlands Equivalence in Positive Characteristic_, OpenAI Math Release preprint OAI:The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026, 2026.
- OpenAI, Rationality of the Canonical Unramified Arthur Filtration (2026)
- OpenAI, _Ramanujan–Arthur Decompositions of Cuspidal Functions at Full Finite Level_, OpenAI Math Release preprint OAI:Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026, 2026.
- OpenAI, The Restricted Geometric Langlands Equivalence in Positive Characteristic (2026)
- OpenAI, _Constructible tame Hecke eigensheaves in positive characteristic_, OpenAI Math Release preprint OAI:Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026, 2026.
- OpenAI, _Constructible tame Hecke eigensheaves in positive characteristic_, OpenAI Math Release preprint OAI:Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026, 2026.
- Pappas, George, Zhu, Xinwen, Local models of Shimura varieties and a conjecture of Kottwitz (2013)
- Prasad, Amritanshu, On Bernstein's presentation of Iwahori–Hecke algebras and representations of split reductive groups over non-Archimedean local fields (2005)
- B. H. Gross and D. Prasad, _On the decomposition of a representation of $\mathrm{SO}_n$ when restricted to $\mathrm{SO}_{n-1}$_, Canad. J. Math. **44** (1992), no. 5, 974–1002. doi:10.4153/CJM-1992-060-8.
- J. P. Pridham, _The deformation theory of representations of the fundamental group of a smooth variety_, arXiv:math/0401344v2, revised 3 July 2019. .
- Ram, Arun, Affine Hecke algebras and generalized standard Young tableaux (2003)
- Dennis Gaitsgory and Sam Raskin, _Geometric Langlands in positive characteristic from characteristic zero_, arXiv:2508.02237v1, 4 August 2025. .
- Sam Raskin, _Conjectures of Arthur and Ramanujan for unramified automorphic forms: announcement_, ICM 2026 contribution, 12 October 2025, updated 10 March 2026. .
- D. Gaitsgory and S. Raskin, _Proof of the geometric Langlands conjecture I: construction of the functor_, preprint, 2024, revised 2025, arXiv:2405.03599v3.
- D. Gaitsgory and S. Raskin, _Proof of the geometric Langlands conjecture V: the multiplicity one theorem_, preprint, 2024, revised 2026, arXiv:2409.09856v3.
- D. Gaitsgory and S. Raskin, _Geometric Langlands in positive characteristic from characteristic zero_, preprint, 2025, arXiv:2508.02237v1.
- D. Gaitsgory and S. Raskin, _Geometric Langlands in positive characteristic from characteristic zero_, arXiv:2508.02237v1, August 4, 2025.
- D. Renard, _Représentations des groupes réductifs $p$-adiques_, Cours spécialisés **17**, Société Mathématique de France, Paris, 2010.
- J. Fæ rgeman, _Motivic realization of rigid $G$-local systems on curves and tamely ramified geometric Langlands_, arXiv:2405.18268v2, July 28, 2024; to appear in Selecta Mathematica.
- Richarz, Timo, Scholbach, Jakob, The motivic Satake equivalence (2021)
- Richarz, Timo, Scholbach, Jakob, The motivic Satake equivalence (2021)
- Richarz, Timo, A new approach to the geometric Satake equivalence (2014)
- F. Rodier, _Mod\`eles de Whittaker des représentations admissibles des groupes réductifs $p$-adiques quasi-déployés_, author manuscript, revised 1975. Author's archival manuscript. The published summary appears in _Harmonic Analysis on Homogeneous Spaces_, Proc. Sympos. Pure Math. **26**, American Mathematical Society, Providence, RI, 1973, 425–430.
- Dennis Gaitsgory and Nick Rozenblyum, _DG indschemes_, arXiv:1108.1738v8, 19 March 2023. .
- Rydh, David, Compactification of stacks and extending stackiness across the boundary (2014)
- J. Hall and D. Rydh, _Coherent Tannaka duality and algebraicity of Hom-stacks_, Algebra Number Theory **13** (2019), no. 7, 1633–1675. doi:10.2140/ant.2019.13.1633.
- D. Rydh, _Compactification of stacks and extending stackiness across the boundary_, preprint, September 16, 2014. Author's manuscript.
- J. Hall and D. Rydh, _Coherent Tannaka duality and algebraicity of Hom-stacks_, Algebra Number Theory **13** (2019), no. 7, 1633–1675.
- D. Rydh, _Compactification of stacks and extending stackiness across the boundary_, preprint, September 16, 2014.
- James Arthur. Unipotent automorphic representations: conjectures. In { Orbites unipotentes et représentations – II. Groupes $p$-adiques et réels}, number 171–172 in Astérisque, pages 13–71. Société mathématique de France, 1989.
- Roman Bezrukavnikov. On two geometric realizations of an affine Hecke algebra. { Publications Mathématiques de l'IHÉS}, 123:1–67, 2016.
- Sawin, Will, Templier, Nicolas, On the Ramanujan conjecture for automorphic forms over function fields I. Geometry (2021)
- Schieder, Simon, The Harder–Narasimhan stratification of the moduli stack of $G$-bundles via Drinfeld's compactifications (2015)
- Timo Richarz and Jakob Scholbach, _The motivic Satake equivalence_, Mathematische Annalen **380** (2021), 1595–1653, published 15 May 2021. .
- D. Hansen and P. Scholze, _Relative perversity_, Commun. Amer. Math. Soc. **3** (2023), 631–668. doi:10.1090/cams/21.
- D. Hansen and P. Scholze, _Relative perversity_, Commun. Amer. Math. Soc. **3** (2023), 631–668.
- F. Shahidi, _Arthur packets and the Ramanujan conjecture_, Kyoto J. Math. **51** (2011), no. 1, 1–23. doi:10.1215/0023608X-2010-018.
- S. Shen, _Tamely ramified geometric Langlands correspondence in positive characteristic_, Int. Math. Res. Not. IMRN **2024**, no. 7, 6176–6208. doi:10.1093/imrn/rnae005.
- V. G. Drinfeld and C. Simpson, _$B$-structures on $G$-bundles and local triviality_, Math. Res. Lett. **2** (1995), no. 6, 823–829.
- François Digne and Jean Michel. Quasi-semisimple elements.  Proceedings of the London Mathematical Society, 116:1301–1328, 2018.
- Vincent Lafforgue. Chtoucas pour les groupes réductifs et paramétrisation de Langlands globale.  Journal of the American Mathematical Society, 31(3):719–891, 2018.
- Springer, T. A., Linear Algebraic Groups (1998)
- Sun, Shenghao, $L$-series of Artin stacks over finite fields (2012)
- Sun, Shenghao, Generic base change, Artin's comparison theorem, and the decomposition theorem for complex Artin stacks (2017)
- G. Dhillon and J. Taylor, _The universal monodromic Arkhipov–Bezrukavnikov equivalence_, preprint, 2025, arXiv:2501.14156v1.
- G. Dhillon and J. Taylor, _Tame local Betti geometric Langlands_, preprint, 2025, arXiv:2501.14157v1.
- Jeffrey Adams and Olivier Taïbi, _Galois and Cartan cohomology of real groups_, arXiv:1611.05956v2, 21 November 2016. .
- W. Sawin and N. Templier, _On the Ramanujan conjecture for automorphic forms over function fields I. Geometry_, J. Amer. Math. Soc. **34** (2021), no. 3, 653–746. doi:10.1090/jams/968.
- Tits, Jacques, Reductive groups over local fields (1979)
- Tudor Pădurariu and Yukinobu Toda, _The categorical DT/PT correspondence and quasi-BPS categories for local surfaces_, Moduli **3** (2026), e1, 1–44. .
- Yukinobu Toda, _Categorical Donaldson–Thomas theory for local surfaces_, arXiv:1907.09076v4, 10 June 2021. .
- Varshavsky, Yakov, Lefschetz–Verdier trace formula and a generalization of a theorem of Fujiwara (2007)
- I. Mirković and K. Vilonen, _Geometric Langlands duality and representations of algebraic groups over commutative rings_, Ann. of Math. (2) **166** (2007), no. 1, 95–143. doi:10.4007/annals.2007.166.95.
- I. Mirković and K. Vilonen, _Geometric Langlands duality and representations of algebraic groups over commutative rings_, Ann. of Math. (2) **166** (2007), no. 1, 95–143; corrected version arXiv:math/0401222v5, February 13, 2018.
- D. Abramovich and A. Vistoli, _Compactifying the space of stable maps_, J. Amer. Math. Soc. **15** (2002), no. 1, 27–75.
- J.-L. Waldspurger, _La formule de Plancherel pour les groupes $p$-adiques, d'apr\`es Harish-Chandra_, J. Inst. Math. Jussieu **2** (2003), no. 2, 235–333. doi:10.1017/S1474748003000082.
- R. Taylor and T. Yoshida, _Compatibility of local and global Langlands correspondences_, J. Amer. Math. Soc. **20** (2007), no. 2, 467–493. doi:10.1090/S0894-0347-06-00542-X.
- Yun, Zhiwei, Rigidity in automorphic representations and local systems (2014)
- D. Nadler and Z. Yun, _Spectral action in Betti geometric Langlands_, Israel J. Math. **232** (2019), 299–349. doi:10.1007/s11856-019-1871-9.
- D. Nadler and Z. Yun, _Automorphic gluing functor in Betti geometric Langlands_, preprint, 2021, revised 2023, arXiv:2105.12318v3.
- D. Nadler and Z. Yun, _Automorphic gluing functor in Betti geometric Langlands_, arXiv:2105.12318v3, June 6, 2023.
- I. N. Bernstein and A. V. Zelevinsky, _Induced representations of reductive $p$-adic groups. I_, Ann. Sci. École Norm. Sup. (4) **10** (1977), no. 4, 441–472. doi:10.24033/asens.1333.
