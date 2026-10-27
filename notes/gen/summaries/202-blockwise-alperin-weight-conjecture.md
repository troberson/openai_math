[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 202](../index/algebra/202-blockwise-alperin-weight-conjecture.md)

# 202 — The blockwise Alperin weight conjecture

[Index page](../index/algebra/202-blockwise-alperin-weight-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4616] and the catalog abstract [S2:485] state
the family's claim: the numerical blockwise Alperin weight conjecture
for every prime and every finite group — the number of irreducible Brauer
characters in a block equals the number of conjugacy classes of its
weights. The manuscript's abstract "We prove the numerical blockwise Alperin weight conjecture for every
finite group and every prime $p$. For each $p$-block $B$, the number of
irreducible Brauer characters in $B$ equals the number of conjugacy
classes of $B$-weights. [S3:82–85]"

## Undergraduate summary

The local–global principle in modular representation theory recovers
information about representations of a finite group from normalizers of
its $p$-subgroups. Alperin's weight conjecture gives this principle an
exact numerical form, block by block: the number of simple modules in a
$p$-block $B$ equals the number of conjugacy classes of $B$-weights,
where a weight is a pair $(Q,\phi)$ of a $p$-subgroup and a defect-zero
ordinary character of its normalizer quotient [S4:4–39]. The manuscript
proves the conjecture 

> **theorem**
For every prime $p$, every finite group $G$, and every $p$-block $B$ of $G$,
\[
                  l(B)=|W_p(B)|.
\] [S4:42–47]

The equality is a count of cardinalities; no canonical correspondence
between the two sets is required. The case $Q=1$ is part of the assertion.

## Graduate summary

**From block algebra to a tuple-divisibility problem.** The proof
proceeds in two stages. The algebraic stage reduces the weight equality
to a uniform divisibility statement: chain inversion converts the
local–global identity into an alternating sum of simple-module counts,
powers modulo commutators replace those counts by ordinary-character
counts, and a central group-algebra element supported on $p$-singular
elements isolates the defect-zero contribution. The remaining counting
problem is to show that, for a finite group $J$ with $O_p(J)=1$ and
$n=p^s$, the number of generating tuples $(x,y,u_1,\ldots,u_n)$ with each
$u_i$ $p$-singular is divisible by $p^h$ for every fixed $h\ge1$ and
sufficiently large $s$ — uniformly in the prescribed multiset of
conjugacy classes [S4:171–292].

**The geometric divisibility input.** The divisibility is proved using a
marked genus-one curve over a finite field of characteristic $p$ with
two key properties: every divisor degree on the curve is divisible by
$p^s$, and after a cyclic splitting extension it becomes a constant
elliptic curve with independently varying marked points. A purely
inseparable cover then yields a genus bound that is made *exact* by the
index property — after multiplication by the cover degree, the difference
between the genus term and the ramification expression is a multiple of
$p^{s-h}$, and a differential calculation bounds that difference below by
a constant independent of $s$. The uniform $p^h$-divisibility of orbit
sizes for the Galois action on the finite cover set completes the argument
[S4:171–292].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Alperin formulated the weight conjecture at the 1986 Arcata conference,
extending the notion of weights from groups of Lie type in defining
characteristic to arbitrary finite groups. Early large-family cases
include Alperin–Fong (symmetric groups, general linear groups in odd
characteristic), Knörr–Robinson (alternating-sum reformulation),
Navarro–Tiep and Späth (blockwise reductions to conditions on simple
groups), and Feng–Li–Zhang (special linear and unitary groups, groups
with abelian Sylow 3-subgroups) [S4:102–167]. Recent progress includes
the inductive blockwise condition for $F_4(q)$ (An–Hiss–Lübeck),
inertial blocks (Hu–Zhou), and chain/Galois/functorial reformulations
(Huang–Yilmaz). The present proof does not use a classification of finite
simple groups or an inductive weight condition; it passes directly from
block-algebra calculation to covers of curves [S4:102–167].

## Consequences

**The local–global bounds, now unconditional.** The theorem supplies
the weight-conjecture hypotheses for the established consequences: the
local block bounds $l(B)\ge l(b)$ with equality when the defect group is
abelian (Alperin's Consequences 1–2), the block-free inequality
$|\mathrm{IBr}_p(G)|\ge|\mathrm{IBr}_p(N_G(P))|$, and the principal-block bounds of
Hung–Sambale–Tiep 

> **corollary**
Let $p$ be a prime, $G$ a finite group, $B$ a $p$-block with defect group
$D$, and $b$ its Brauer correspondent in $N_G(D)$. Then
\[
 l(B)\geq l(b),\qquad
 D abelian\Longrightarrow l(B)=l(b).
\]
For $P\in\mathrm{Syl}_p(G)$, one also has
\[
 |\mathrmIBr_p(G)|\geq|\mathrmIBr_p(N_G(P))|.
\]
Let $B_0$ be the principal $p$-block of $G$, and let $k_p(G)$ count the
conjugacy classes of $p$-power-order elements, including the identity.
Then
\[
 \beginaligned
 k_p(G)=3&\Longrightarrow l(B_0)\geq (p-1)/2,\\
 p\mid |G|&\Longrightarrow l(B_0)\geq 2\sqrtp-1+1-k_p(G).
 \endaligned
\] [S4:61–81]

The block-free inequality for $p=2$ was previously proved by
Malle–Navarro–Tiep, and the local inequality for maximal-defect
2-blocks by Feng–Martinez–Rossi; the current result extends both to all
primes and all defect groups [S4:49–51, S4:83–98].

**A classification and functorial identity.** The sharper
classification of character-count and defect data, and the functorial
formulation of the theorem, are developed in the consequences section
[S4:95–97]. The theorem gives an equality of cardinalities without
requiring a canonical correspondence, which is the numerical form of the
conjecture.

## Section skeleton

**Manuscript** [S3:82–85], 8 sections under `build/sections/`:
intro [S4], foundations, group, twist, differentials, valuations,
specialization, consequences.

The manuscript's root is `build/paper.tex`, with a `references.bib`
bibliography [S5]. It ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 11 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 202 at line 4616. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 485. |
| S3 | [`preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/paper.tex`](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/paper.tex) | 103 | Main file: title and abstract. |
| S4 | [`preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/sections/intro.tex`](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/sections/intro.tex) | 310 | The main theorem, the weight and block-assignment conventions, the local-global consequences corollary, the prior work, the proof mechanism, and the conventions. |
| S5 | [`preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/references.bib`](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/references.bib) | 448 | The manuscript's bibliography. |

## Bibliography

- Alperin, J. L., Weights for finite groups (1987)
- Alperin, J. L., Fong, Paul, Weights for symmetric and general linear groups (1990)
- An, Jianbei, Hiss, Gerhard, Lübeck, Frank, The inductive blockwise {Alperin weight condition for the Chevalley groups $F_4(q)$} (2024)
- The Stacks Project Authors, The Stacks Project (2026)
- D{\`e}bes, Pierre, Douai, Jean-Claude, Algebraic covers: field of moduli versus field of definition (1997)
- Boltje, Robert, Bouc, Serge, Yılmaz, Deniz, On Alperin's conjecture and functorial equivalence of blocks (2026)
- Brauer, Richard, Zur Darstellungstheorie der Gruppen endlicher Ordnung. II (1959)
- Carlson, Jon F., Block idempotents and the Brauer correspondence (1971)
- Carlson, Jon F., Corrigendum: Block idempotents and the Brauer correspondence (1973)
- Chen, William Y., Nonabelian level structures, Nielsen equivalence, and Markoff triples (2024)
- Clark, Pete L., Lacy, Allan, There are genus one curves of every index over every infinite, finitely generated field (2019)
- Deligne, P., Rapoport, M., Les schémas de modules de courbes elliptiques (1973)
- Ekedahl, Torsten, Canonical models of surfaces of general type in positive characteristic (1988)
- Schröer, Stefan, On genus change in algebraic curves over imperfect fields (2009)
- Feng, Zhicheng, Li, Conghui, Zhang, Jiping, On the inductive blockwise Alperin weight condition for type A (2023)
- Feng, Zhicheng, Malle, Gunter, Zhang, Jiping, Generic weights for finite reductive groups (2026)
- Feng, Zhicheng, Martínez, J. Miquel, Rossi, Damiano, Alperin's bound and normal Sylow subgroups (2026)
- Grothendieck, Alexandre, Dieudonné, Jean, {Éléments de géométrie algébrique III. Étude cohomologique des faisceaux cohérents, Premi{\`e}re partie} (1961)
- Grothendieck, Alexandre, Dieudonné, Jean, {Éléments de géométrie algébrique IV. Étude locale des schémas et des morphismes de schémas, Troisi{\`e}me partie} (1966)
- Higman, Donald G., On orders in separable algebras (1955)
- Hu, Xueqin, Zhou, Yuanyang, The blockwise Alperin weight conjecture and inertial blocks (2025)
- Huang, Xin, Yılmaz, Deniz, Alperin's weight conjecture, Galois automorphisms, alternating sums, and functorial equivalences (2026)
- Hung, Nguyen Ngoc, Sambale, Benjamin, Tiep, Pham Huu, Bounding {$p$-Brauer characters in finite groups with two conjugacy classes of $p$-elements} (2024)
- Kaplansky, Irving, Maximal fields with valuations (1942)
- Klug, Michael R., Counting homomorphisms from surface groups to finite groups (2025)
- Krull, Wolfgang, Allgemeine Bewertungstheorie (1932)
- Lorenz, Martin, Tokoly, Loretta Fitzgerald, Projective modules over Frobenius algebras and Hopf comodule algebras (2011)
- Malle, Gunter, Navarro, Gabriel, Tiep, Pham Huu, On Alperin's lower bound for the number of Brauer characters (2023)
- Milne, James S., Abelian Varieties (2022)
- Milne, James S., Lectures on Étale Cohomology (2008)
- Navarro, Gabriel, Tiep, Pham Huu, A reduction theorem for the Alperin weight conjecture (2011)
- Poonen, Bjorn, Maximally complete fields (1993)
- Knörr, Reinhard, Robinson, Geoffrey R., Some remarks on a conjecture of Alperin (1989)
- Silverman, Joseph H., The arithmetic of elliptic curves (2009)
- Tate, John, Genus change in inseparable extensions of function fields (1952)
- Späth, Britta, A reduction theorem for the blockwise Alperin weight conjecture (2013)
- Héthelyi, László, Horváth, Erzsébet, Külshammer, Burkhard, Murray, John, Central ideals and Cartan invariants of symmetric algebras (2005)
- Tsushima, Yukio, On the Block of Defect Zero (1971)
- Zhang, Baoyu, On the inductive blockwise Alperin weight condition for type $\mathsf B$ and type $\mathsf C$ (2026)
