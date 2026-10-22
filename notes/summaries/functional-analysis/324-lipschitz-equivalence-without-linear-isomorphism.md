Notes / Summaries / Functional analysis / [Family 324](../../index/functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md)

# 324 — Lipschitz equivalence without linear isomorphism

[Index page](../../index/functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md)

## Original CONTENTS.md summary

[S1:744] carries the family entry:

> Constructs separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic, resolving the separable Lipschitz-isomorphism problem negatively. Thus even the complete metric structure up to bi-Lipschitz equivalence does not determine a separable Banach space's linear isomorphism class.

The entry links the two manuscripts as "Lipschitz equivalence without linear isomorphism" and "Bi-Lipschitz $c_0$ absorption" [S1:744].

The first manuscript's title is `Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic` [S2:1].

The README dates it September 24, 2026 [S2:5].

The second manuscript's title is `Bi-Lipschitz Absorption of c_0 Without a Linear Copy of c_0` [S12:1].

The README dates it September 26, 2026 [S12:5].

## Undergraduate summary

Two Banach spaces are **bi-Lipschitz equivalent** when a bijection between them distorts distances by a bounded factor in both directions, and **linearly isomorphic** when a bounded linear bijection with a bounded inverse identifies them. The question is whether the metric structure determines the linear structure.

The first manuscript's abstract states the result. [S3:46–48] says: "There are separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic. This gives a negative answer to the separable Banach-space Lipschitz-isomorphism problem."

The second manuscript's abstract states the absorption result. [S13:37–40] says: "We construct a separable real Banach space \(Z\) that contains no linear copy of \(c_0\), yet is bi-Lipschitz equivalent to \(Z\oplus_\infty c_0\). The same space contains a bi-Lipschitz image of every separable metric space."

The first manuscript states its theorem. [S6:23–24] gives it: "There are separable real Banach spaces \(X,Y\) and a bijection \(\Psi:X\to Y\) such that, for every \(s,t\in X\)," and [S6:31–34] states the obstruction: "The space \(X\) contains a linearly isometric copy of \(c_0(\ell_2)\), while \(Y\) contains no closed subspace linearly isomorphic to \(c_0(\ell_2)\). In particular, \(X\) and \(Y\) are not linearly isomorphic."

The second manuscript states its theorem. [S16:52–56] gives it: "There is a separable real Banach space \(Z\) containing no closed linear subspace isomorphic to \(c_0\), and an onto bi-Lipschitz map \[ F:Z\oplus_\infty c_0\longrightarrow Z. \]"

The consequence for the Lipschitz-isomorphism problem is stated in the second manuscript. [S16:59–66] gives it: "The map is automatically a bijection by its lower Lipschitz bound. The two spaces in Theorem~  cannot be linearly isomorphic: the direct sum contains a linear copy of \(c_0\), whereas \(Z\) does not. Restricting \(F\) to that summand gives a bi-Lipschitz embedding of \(c_0\) into this same \(Z\). Aharoni proved that every separable metric space embeds bi-Lipschitzly into \(c_0\)  ; composition therefore makes this one space \(Z\) a bi-Lipschitz universal target for separable metric spaces."

## Graduate summary

The first manuscript opens with the nonlinear geometry question. [S6:4–10] states it: "A Banach-space norm defines both a linear topology and a metric. A bounded linear isomorphism preserves the metric up to multiplicative constants, but a map with that metric property need not preserve addition or scalar multiplication. The Lipschitz-isomorphism problem asks whether a _bijection_ with two-sided Lipschitz bounds nevertheless forces two Banach spaces to be linearly isomorphic. We consider the separable real case and obtain a negative answer."

The first manuscript's obstruction is block-valued. [S6:37–39] states it: "The obstruction in this theorem is deliberately block-valued: each coordinate of \(c_0(\ell_2)\) is an entire Hilbert space. It does not say that \(Y\) contains no ordinary \(c_0\)."

The scope of the first theorem is bounded. [S6:40–41] bounds it: "The Hilbert block in each coordinate is essential to the obstruction proved below."

The first manuscript's local orthogonality is stated. [S6:102–105] gives it: "Here \(U=(\bigoplus_{n\ge1}U_n)_2\) is a Hilbert sum of finite-dimensional coordinate blocks. The map \(h\) is an onto bi-Lipschitz change of variables fixing zero, close to an isometry. Its relevant nonlinear part is" and [S6:109–113] states the local property: "The construction arranges that, near any finite family of distinct points of \(M\), the sufficiently high output coordinates of \(D\) lie in mutually orthogonal coordinate subspaces. The cutoff index and the neighborhoods may depend on that finite family. We call this property _local orthogonality_."

The first manuscript's free space is stated. [S6:115–117] gives it: "To turn this geometry into a linear obstruction, use the Lipschitz-free space \(E=\mathcal F(M)\), the closed linear span of evaluation functionals on real zero-preserving Lipschitz functions."

The first manuscript's complete continuity is stated. [S6:124–127] gives it: "Section~  proves that local orthogonality makes \(q\) _completely continuous_: a weakly null sequence in \(E\) has norm-null image. This is the one place where the local coordinate geometry enters the Banach-space obstruction."

The first manuscript's triangular norm is stated. [S6:129–130] gives it: "The linearization is also what makes the metric change of variables possible. Give \(E\oplus V\) its sum norm and put" and [S6:135–137] states the triangular identity: "The identity \(qB=hQ_1\) is triangular: applying \(q\) to the new variable records \(h\) of the old output. Given \(z\in E\), one first recovers \(x=h^{-1}(qz)\) and then subtracts \(\delta(x)\); this yields"

The first manuscript's graph space is defined. [S6:141–143] defines it: "For a bounded linear \(Q:A\to H\), the graph space used in the final step consists of sequences \(s=(s_i)\) for which \(\sum_i2^{-i}\|s_i\|<\infty\) and \((Qs_i)\in c_0(H)\), with norm"

The first manuscript's bijection is stated. [S6:148–151] states it: "Set \(X=Z_{Q_1}\) and \(Y=Z_q\). Applying \(B\) in each coordinate gives the desired bijection: \(qB=hQ_1\) controls the second part of the graph norm, and the Lipschitz bounds for \(B\) control the weighted sum. The \(V\) coordinates embed \(c_0(V)\) isometrically in \(X\)."

The first manuscript's exclusion is argued. [S6:152–158] argues it: "By contrast, complete continuity of \(q\) makes each fixed output coordinate tend to zero along an orthonormal sequence in any Hilbert block of a proposed \(c_0(\ell_2)\) copy in \(Y\). A disjoint-support argument then finds a unit vector in each block with arbitrarily small full \(c_0(U)\) output. A surviving copy would embed ordinary \(c_0\) into \(\ell_1(E)\). Section~  excludes this because \(E=\mathcal F(M)\) is weakly sequentially complete."

The first manuscript's slots are stated. [S6:171–176] states them: "For the Hilbert map, a unit vector in each block is designated as a slot. With the slots frozen, perpendicular components stay in their blocks, old slot coordinates move to even blocks, and the additional \(\ell_2\) coordinates fill odd blocks. This is an onto linear isometry. The slots are then allowed to depend on the input so that near different points they eventually use disjoint coordinates."

The second manuscript opens with the same question. [S16:15–17] states it: "The nonlinear geometry of Banach spaces asks how much linear structure is retained by maps that control distances but need not respect addition."

The space $c_0$ and the Godefroy–Kalton–Lancien theorem are stated together. [S16:32–35] gives them: "The space \(c_0=c_0(\mathbb N)\) consists of real scalar sequences tending to zero, with the supremum norm. Godefroy, Kalton and Lancien proved that a Banach space bi-Lipschitz equivalent to a linear subspace of \(c_0\) is linearly isomorphic to a subspace of \(c_0\)"

Kalton's Schur space is the related construction with weaker control. [S16:68–71] gives it: "There are related separable constructions with weaker control of small distances. Kalton constructed a separable Schur space, in which weakly convergent sequences converge in norm, uniformly homeomorphic to a space containing complemented \(c_0\)"

Sarı's coarse-Lipschitz embedding is the other related construction. [S16:76–77] gives it: "Sar{\i} constructed a coarse-Lipschitz embedding of \(c_0\) into a separable dual Banach space, which contains no linear copy of \(c_0\)"

The proof begins with an algebraic absorption criterion. [S16:93–96] gives the setup: "The first step is algebraic. Suppose \(E,U\) are Banach spaces and \(P:E\oplus_\infty U\to U\) is the projection. We seek an onto bi-Lipschitz map \(g:E\oplus_\infty U\to U\), a bounded linear map \(Q:Z\to U\), and a Lipschitz map \(K:E\oplus_\infty U\to Z\) such that"

The criterion and the two tasks are stated. [S16:100–104] gives them: "Section~  proves that these data make \(F(b,t)=b+K(t,Qb)\) an onto bi-Lipschitz map \(Z\oplus_\infty E\to Z\). Thus the construction has two concrete tasks: realize   with \(E=c_0\), and arrange that \(Z\) contains no linear \(c_0\)."

The weights are introduced. [S16:110–111] begins: "We first construct \(g\). Let \(E\) and \(U\) be countable-coordinate copies of \(c_0\)."

The tests are stated. [S16:127–135] gives them: "We next construct \(Z\) and lift the correction. Record each coordinate of \((S_s-P)s\) as a scalar function of \(s\) in the unit ball of \(E\oplus_\infty U\). These functions depend on finitely many coordinates and have localized supports. Section~  enlarges them by two local operations, one making a function constant on a small cylinder and one retaining only the change. A strict scale budget keeps their supports localized, and a nonincreasing order of scales controls what happens after a small local change. Tail factors give a second way to separate supports."

The norm is built from selected tests. [S16:141–149] describes it: "from lists of selected tests whose signed sums have a common Lipschitz bound. It combines their evaluation norms, with exponents approaching one, in an outer square sum. The square sum prevents a hypothetical \(c_0\) basis from escaping through different test classes; the varying exponents then select one scalar test detecting each basis vector. We prove directly the completion and duality properties needed for this norm. The coordinate tests define \(Q\), and radial extension of the point molecules defines \(K\) with  ."

The detector argument is stated. [S16:151–161] gives it: "Finally, a hypothetical linear \(c_0\) basis in \(Z\) has uniformly bounded signed sums. Section~  extracts one detecting test for each vector from a single class with a common operation budget. A test's label records its original correction coordinate. Distinct labels can be separated either by tails or by nested coordinate cylinders. For a repeated label, an expansion leaves either disjoint tails or a first small local change. In the latter case, its support shrinks and its value becomes small enough that nested tests still have uniformly Lipschitz signed sums. The norm then forces the signed sums of the vectors to grow, a contradiction."

## History of the conjecture

The rigidity results are named. [S16:26–28] gives them: "Johnson, Lindenstrauss and Schechtman developed both rigidity results and separable examples with different linear structures under the weaker relation of uniform homeomorphism"

The embedding question was described as open. [S16:42–44] records it: "Hájek, Johanis and Schlumprecht still described the embedding question as apparently open in their January 2024 preprint (arXiv:2401.00831v1), later published in 2025"

The second manuscript names an earlier counterexample with a different obstruction. [S16:82–84] describes it: "An earlier real-separable counterexample to the Lipschitz-isomorphism question uses a different linear obstruction: one space contains \(c_0(\ell_2)\), the space of \(\ell_2\)-valued null sequences,"

The relation between the two constructions is stated. [S16:86–89] states it: "Its Hilbert-block and localized Lipschitz-free argument is independent of the construction here. The present construction excludes ordinary \(c_0\) and yields absorption by the same space."

## Section skeleton

Manuscript A:

- `build/main.tex` [S3]
- `build/sections/01-introduction.tex` [S6]
- `build/sections/02-free-graph.tex` [S7]
- `build/sections/03-triangular.tex` [S8]
- `build/sections/04-localization.tex` [S9]
- `build/sections/05-hilbert.tex` [S10]
- `build/sections/06-assembly.tex` [S11]
- `build/figures/slot-rearrangement.tex` [S5]
- `build/references.bib` [S4]

Manuscript B:

- `build/main.tex` [S13]
- `build/sections/01-introduction.tex` [S16]
- `build/sections/02-absorption.tex` [S17]
- `build/sections/03-weights.tex` [S18]
- `build/sections/04-shift.tex` [S19]
- `build/sections/05-tests.tex` [S20]
- `build/sections/06-molecules.tex` [S21]
- `build/sections/07-no-c0.tex` [S22]
- `build/sections/08-assembly.tex` [S23]
- `build/figures/terminal-scalar.tex` [S15]
- `build/references.bib` [S14]

## Comparison with the formalized statement

The scope note states the formalized counterexample. [S24:10] says: "The formalized counterexample gives separable real Banach spaces $X,Y$ that are bi-Lipschitz equivalent but not linearly isomorphic. The bijection has lower Lipschitz bound $4/21$ and upper bound $76/25$. The linear obstruction is explicit: $X$ contains a linear isometric copy of $c_0(\ell_2)$, whereas $Y$ contains no bounded linear copy of that space."

The scope note states the absorption result. [S24:12] says: "The formalized result constructs one separable real Banach space $X$ that is bi-Lipschitz equivalent to $X\times c_0$ but contains no closed linear subspace isomorphic to $c_0$. The same space contains a bi-Lipschitz copy of $c_0$, is bi-Lipschitz universal for separable metric spaces, and is not linearly isomorphic to $X\times c_0$. Thus nonlinear absorption of $c_0$ does not force a linear copy of it."

The first declaration is `OAI.LipschitzCounterexample.main` [S25:8]. The second is `OAI.C0Absorption.main_result` [S26:33].

The comparator stubs carry `sorry`. `OAI.LipschitzEquivalence.main` is at `LipschitzEquivalence.lean:39` [S27:39] and `OAI.C0Absorption.main` at `C0Absorption.lean:29` [S28:29].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 744 |
| S2 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/README.md`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/README.md) | 18 | Manuscript 1 title, date |
| S3 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/main.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/main.tex) | 60 | Abstract, lines 46–48 |
| S4 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/references.bib`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/references.bib) | 168 | Bibliography entries |
| S5 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/figures/slot-rearrangement.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/figures/slot-rearrangement.tex) | 17 | Figure source |
| S6 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/01-introduction.tex) | 183 | Introduction: theorem, history, proof overview |
| S7 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/02-free-graph.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/02-free-graph.tex) | 357 | Free graph space |
| S8 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/03-triangular.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/03-triangular.tex) | 178 | Triangular norm |
| S9 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/04-localization.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/04-localization.tex) | 395 | Localization |
| S10 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/05-hilbert.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/05-hilbert.tex) | 578 | Hilbert block argument |
| S11 | [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/06-assembly.tex`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/06-assembly.tex) | 52 | Assembly |
| S12 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/README.md`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/README.md) | 18 | Manuscript 2 title, date |
| S13 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/main.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/main.tex) | 52 | Abstract, lines 37–40 |
| S14 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/references.bib`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/references.bib) | 146 | Bibliography entries |
| S15 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/figures/terminal-scalar.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/figures/terminal-scalar.tex) | 32 | Figure source |
| S16 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/01-introduction.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/01-introduction.tex) | 163 | Introduction: theorem, history, proof overview |
| S17 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/02-absorption.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/02-absorption.tex) | 77 | Absorption criterion |
| S18 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/03-weights.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/03-weights.tex) | 308 | Weights |
| S19 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/04-shift.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/04-shift.tex) | 243 | Shift |
| S20 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/05-tests.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/05-tests.tex) | 247 | Tests |
| S21 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/06-molecules.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/06-molecules.tex) | 274 | Molecules |
| S22 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/07-no-c0.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/07-no-c0.tex) | 599 | No copy of c_0 |
| S23 | [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/08-assembly.tex`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/08-assembly.tex) | 50 | Assembly |
| S24 | [`lean/docs/324.md`](../../../lean/docs/324.md) | 19 | Scope |
| S25 | [`lean/OAI/Analysis/LipschitzEquivalence/Main.lean`](../../../lean/OAI/Analysis/LipschitzEquivalence/Main.lean) | 15 | Declaration |
| S26 | [`lean/OAI/Analysis/C0Absorption/Main.lean`](../../../lean/OAI/Analysis/C0Absorption/Main.lean) | 42 | Declaration |
| S27 | [`lean/ComparatorChallenges/LipschitzEquivalence.lean`](../../../lean/ComparatorChallenges/LipschitzEquivalence.lean) | 44 | Comparator stub |
| S28 | [`lean/ComparatorChallenges/C0Absorption.lean`](../../../lean/ComparatorChallenges/C0Absorption.lean) | 33 | Comparator stub |

## Bibliography

**15 entries** from `references.bib`:
- Aharoni, Israel, Lindenstrauss, Joram. *Uniform equivalence between {Banach} spaces*. (1978) [AL78]
- Ribe, Martin. *On uniformly homeomorphic normed spaces*. (1976) [Ribe76]
- Ribe, Martin. *Existence of separable uniformly homeomorphic nonisomorphic {Banach} spaces*. (1984) [Ribe84]
- Aharoni, Israel, Lindenstrauss, Joram. *An extension of a result of {Ribe}*. (1985) [AL85]
- Johnson, William B., Lindenstrauss, Joram, Schechtman, Gideon. *{Banach} spaces determined by their uniform structures*. (1996) [JLS96]
- Arens, Richard F., Eells, Jr., James. *On embedding uniform and topological spaces*. (1956) [AE56]
- Kalton, Nigel J.. *Spaces of {Lipschitz} and {H\"older} functions and their applications*. (2004) [Kalton04]
- Kalton, Nigel J.. *The nonlinear geometry of {Banach} spaces*. (2008) [Kalton08]
- Albiac, Fernando, Kalton, Nigel J.. *{Lipschitz} structure of quasi-{Banach} spaces*. (2009) [AK09]
- Albiac, Fernando, Ansorena, Jos{\'e} L., B{\'i}ma, Jan, C{\'u}th, Marek. *{Lipschitz} free {$p$}-spaces for {$0<p<1$} in the light of the {Schur} {$p$}-property and the compact reduction*. (2026) [AABC26]
- … and 5 more

**14 entries** from `references.bib`:
- Ribe, Martin. *On uniformly homeomorphic normed spaces*. (1976) [Ribe76]
- Aharoni, Israel. *Every separable metric space is {Lipschitz} equivalent to a subset of {$c_0^+$}*. (1974) [Aharoni74]
- Aharoni, Israel, Lindenstrauss, Joram. *Uniform equivalence between {Banach} spaces*. (1978) [AL78]
- Ribe, Martin. *Existence of separable uniformly homeomorphic nonisomorphic {Banach} spaces*. (1984) [Ribe84]
- Aharoni, Israel, Lindenstrauss, Joram. *An extension of a result of {Ribe}*. (1985) [AL85]
- Johnson, William B., Lindenstrauss, Joram, Schechtman, Gideon. *{Banach} spaces determined by their uniform structures*. (1996) [JLS96]
- Godefroy, Gilles, Kalton, Nigel J., Lancien, Gilles. *Subspaces of {$c_0(\mathbb{N})$} and {Lipschitz} isomorphisms*. (2000) [GKL00]
- Arens, Richard F., Eells, Jr., James. *On embedding uniform and topological spaces*. (1956) [AE56]
- Godefroy, Gilles, Kalton, Nigel J.. *{Lipschitz}-free {Banach} spaces*. (2003) [GK03]
- Kalton, Nigel J.. *Spaces of {Lipschitz} and {H{\"o}lder} functions and their applications*. (2004) [Kalton04]
- … and 4 more
