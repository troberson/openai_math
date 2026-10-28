[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 204](../index/algebra/204-tensor-saturation-for-even-spin-groups.md)

# 204 — Tensor saturation for even spin groups

[Index page](../index/algebra/204-tensor-saturation-for-even-spin-groups.md)

## Original CONTENTS.md summary

The release's blurb [S1:4657] and the catalog abstract [S2:489] state
the family's claim: saturation factor one for $\mathrm{Spin}(2n)$,
$n\ge2$ — for three dominant integral weights whose sum lies in the root
lattice, an invariant at any common positive integral dilation already
gives an invariant at the original weights, resolving the type-$D$ part
of the simply-laced saturation conjecture. The manuscript's abstract
 "We prove the saturation conjecture for $\mathrm{Spin}(2n)$, $n\ge2$.
If three dominant integral weights sum to an element of the root lattice,
then the existence of a nonzero tensor invariant after a positive integral
dilation implies the existence of one at the original weights. [S3:48–53]"

## Undergraduate summary

In the representation theory of a semisimple group $G$, a tensor
invariant in $V(\lambda)\otimes V(\mu)\otimes V(\nu)$ is a $G$-equivariant
map from the tensor product to the trivial representation — equivalently,
an invariant vector. A natural scaling question asks whether such an
invariant at dilated weights $N\lambda, N\mu, N\nu$ forces one at the
original weights. For simply connected groups a necessary condition is
that $\lambda+\mu+\nu$ lie in the root lattice (otherwise the center acts
nontrivially on the product). The saturation conjecture asserts that this
congruence, together with the existence of a dilated invariant, is also
sufficient [S4:3–14]. Kapovich and Millson formulated the root-lattice
assertion for all simply-laced groups [S4:29–31]; the manuscript proves
its type-$D$ case 

> **Theorem 1.1**
Let $G=\mathrm{Spin}(2n)$, $n\ge2$, and let $\lambda,\mu,\nu$ be dominant
integral weights such that $\lambda+\mu+\nu\in Q(D_n)$. Then, for every
positive integer $N$,
$$\bigl(V(\lambda)\otimes V(\mu)\otimes V(\nu)\bigr)^G\ne0
 \quad\Longleftrightarrow\quad
 \bigl(V(N\lambda)\otimes V(N\mu)\otimes V(N\nu)\bigr)^G\ne0.$$ [S4:33–42]

The theorem covers all three classical even-spin ranks $n\ge2$ and
includes the half-integral spin weights.

## Graduate summary

**The path-model and lattice-obstruction structure.** The proof separates
the geometric and arithmetic roles of Littelmann's path model. Real paths
through the building give a real moment-polytope feasibility condition;
integrality of the schedule (all switch coefficients integral) is the
arithmetic obstacle. In type $D$ a rank reduction leaves exactly one
obstruction: the signed root graph has two unbalanced components, each
with an odd coordinate sum in its assigned label difference. Joining the
components introduces one relation among the roots, and motion along half
its primitive integer generator reaches integral coefficients without
changing the endpoint [S4:74–94].

**The three constructions.** The first produces an integral schedule
whose switch roots form a real basis. The second converts integral
schedules for a sequence of fundamental columns (straight path segments
with fundamental-weight increments) into tensor intertwiners, using a
common-wall invariant covector and a flag-composition argument. The third
removes a common terminal zero block via a preprojective-module
construction whose key ingredient is a filtered intersection estimate
for the socle of a nilpotent operator [S4:74–142].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The saturation problem was answered in type $A$ by Knutson and Tao's
honeycomb theorem, with a quiver proof by Derksen–Weyman and a geometric
proof by Belkale. General saturation-factor results give partial
conclusions: Kapovich–Millson give factor four in type $D$, Belkale–Kumar
give factor two for symplectic and odd orthogonal groups, Sam gives
factor two uniformly for classical groups, and Hong–Shen obtain factor
two for odd spin groups under the root-lattice congruence [S4:49–72].
Kapovich–Kumar–Millson proved saturation for $\mathrm{Spin}(8)$,
and Kiers for $\mathrm{Spin}(10)$ and $\mathrm{Spin}(12)$;
the present result extends these to all $n\ge2$ [S4:49–72].

## Consequences

**The type-$D$ part of the simply-laced saturation conjecture is
resolved.** The theorem gives factor-one saturation for all even spin
groups, closing the last remaining simply-laced case after type $A$
(honeycomb), type $C$ (Belkale), and type $B$ (odd orthogonal, via
descent). Combined with the type-$A$ honeycomb theorem and the
Belkale–Kumar factor-two results for the remaining classical families,
the simply-laced saturation conjecture is now settled for all
simply-connected classical groups [S4:3–31].

**The path-model machinery is reusable.** The real-schedule construction
with its lattice obstruction analysis, and the column-intertwiner
construction, are stated as general tools. The zero-tail reduction via
the preprojective-module construction applies to any even spin rank
[S4:74–142].

## Section skeleton

**Manuscript** [S3:48–53], 6 sections under `build/sections/`:
01-introduction [S4:33–42], 02-real-schedules, 03-lattice-continuation,
04-moment-knots, 05-columns, 06-zero-tail-completion. Plus two figure
files under `build/figures/`.

The manuscript's root is `build/main.tex`, with a `references.bib`
bibliography [S5]. It ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 8 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 204 at line 4657. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 489. |
| S3 | [`preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/main.tex`](../../../preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/main.tex) | 62 | Main file: title and abstract. |
| S4 | [`preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/sections/01-introduction.tex) | 142 | The main theorem, the saturation setup, prior work, and the proof's constructions. |
| S5 | [`preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/references.bib`](../../../preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/references.bib) | 414 | The manuscript's bibliography. |

## Bibliography

- Atiyah, M. F., Convexity and commuting Hamiltonians (1982)
- Atiyah, Michael F., On the Krull–Schmidt theorem with application to sheaves (1956)
- The Stacks Project Authors, The Stacks Project (2026)
- Belkale, Prakash, Kumar, Shrawan, Eigencone, saturation and Horn problems for symplectic and odd orthogonal groups (2010)
- Belkale, Prakash, Geometric proofs of Horn and saturation conjectures (2005)
- Berenstein, Arkady, Sjamaar, Reyer, Coadjoint orbits, moment polytopes, and the Hilbert–Mumford criterion (2000)
- Brouwer, L. E. J., Über Abbildung von Mannigfaltigkeiten (1911)
- Derksen, Harm, Weyman, Jerzy, Semi-invariants of quivers and saturation for Littlewood–Richardson coefficients (2000)
- Gel'fand, I. M., Serganova, V. V., Combinatorial geometries and torus strata on homogeneous compact manifolds (1987)
- Fang, Jiepeng, Lan, Yixin, Xiao, Jie, The correspondence between the canonical and semicanonical bases (2023)
- Fresse, Lucas, Betti numbers of Springer fibers in type A (2009)
- Fulton, William, Harris, Joe, Representation Theory: A First Course (1991)
- Gao, Shiliang, Orelowitz, Gidon, Ressayre, Nicolas, Yong, Alexander, Newell–Littlewood numbers III: Eigencones and GIT-semigroups (2025)
- Geiss, Christof, Leclerc, Bernard, Schröer, Jan, Semicanonical bases and preprojective algebras (2005)
- Hall, P., On Representatives of Subsets (1935)
- Hong, Jiuzu, Shen, Linhui, Tensor invariants, saturation problems, and Dynkin automorphisms (2015)
- Kac, Victor G., Infinite root systems, representations of graphs and invariant theory, II (1982)
- Kapovich, Michael, Kumar, Shrawan, Millson, John J., The eigencone and saturation for $\mathrm{Spin(8)$} (2009)
- Kapovich, Misha, Millson, John J., Structure of the tensor product semigroup (2006)
- Kapovich, Michael, Millson, John J., A path model for geodesics in Euclidean buildings and its applications to representation theory (2008)
- Kapovich, Michael, Leeb, Bernhard, Millson, John, Convex functions on symmetric spaces, side lengths of polygons and the stability inequalities for weighted configurations at infinity (2009)
- Kempf, George, Ness, Linda, The length of vectors in representation spaces (1979)
- Kiers, Joshua, On the saturation conjecture for $\mathrm{Spin(2n)$} (2021)
- Klyachko, A. A., Stable bundles, representation theory and Hermitian operators (1998)
- Knutson, Allen, Tao, Terence, The honeycomb model of $GL_n(\mathbb{C)$ tensor products I: Proof of the saturation conjecture} (1999)
- Kumar, Shrawan, Tensor Product Decomposition (2010)
- Littelmann, Peter, A Littlewood–Richardson rule for symmetrizable Kac–Moody algebras (1994)
- Littelmann, Peter, Paths and root operators in representation theory (1995)
- Littelmann, Peter, Contracting modules and standard monomial theory for symmetrizable Kac–Moody algebras (1998)
- Lusztig, George, Semicanonical bases arising from enveloping algebras (2000)
- Min, Jaewon, Proof of the Newell–Littlewood saturation conjecture (2024)
- Panyushev, D. I., Yakimova, O. S., The PRV-formula for tensor product decompositions and its applications (2008)
- Parthasarathy, K. R., Ranga Rao, R., Varadarajan, V. S., Representations of complex semi-simple Lie groups and Lie algebras (1967)
- Sam, Steven V., Symmetric quivers, invariant theory, and saturation theorems for the classical groups (2012)
- Schofield, Aidan, General Representations of Quivers (1992)
- Zaslavsky, Thomas, Signed graphs (1982)
- Zaslavsky, Thomas, Signed graphs and geometry (2012)
