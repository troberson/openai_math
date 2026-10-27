[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 304](../index/topology/304-hilbert-smith-conjecture-in-every-dimension.md)

# 304 — The Hilbert–Smith conjecture in every dimension

[Index page](../index/topology/304-hilbert-smith-conjecture-in-every-dimension.md)

## Original CONTENTS.md summary

The release's blurb [S1:7512] and the catalog abstract [S2:702] state
the family's claim: the Hilbert--Smith conjecture holds in every finite
dimension — a locally compact second-countable Hausdorff group acting
faithfully and jointly continuously on a connected finite-dimensional
topological manifold is a Lie group. The manuscript's abstract
 "We prove the Hilbert–Smith conjecture in every finite dimension: every
locally compact second-countable Hausdorff group acting faithfully and
jointly continuously on a connected Hausdorff second-countable
finite-dimensional topological manifold without boundary is a Lie group. [S3:89–94]"

## Undergraduate summary

The Hilbert--Smith conjecture asks how much a "mere" continuous group
action can distort a manifold. A group of homeomorphisms acts on a
manifold $M$; the action is *faithful* when no non-identity element
fixes every point. The conjecture predicts that if $M$ is connected and
finite-dimensional, then a locally compact group that acts faithfully
and continuously on it must be a Lie group — a smooth $n$-dimensional
manifold that is also a group, with smooth multiplication. Locally
compact groups include familiar Lie groups (compact matrix groups,
$\mathbb R^n$), but also the profinite groups such as the $p$-adic integers
$\mathbb Z_p$, which are uncountable, totally disconnected, and far from
being manifolds [S4:3–7]. Positive dimension is the only hypothesis:
the manifold may be noncompact, nonorientable, or nontriangulable, and
actions may have arbitrary stabilizers 

> **Theorem 1.1**
Let \(n\geq1\). A locally compact second-countable Hausdorff group
acting faithfully and jointly continuously on a connected Hausdorff
second-countable topological \(n\)-manifold without boundary is a Lie
group. [S4:9–14]

In dimension zero a connected manifold is a point, so a faithful
acting group is trivial and the conclusion holds as well [S4:16–20].

## Graduate summary

**The reduction to $p$-adic exclusion.** The full group theorem follows
from the classical structure theory of Gleason, Montgomery--Zippin, and
Yamabe once faithful actions of the additive group of $p$-adic
integers $\mathbb Z_p$ are excluded. The precise statement is that every
jointly continuous action of $\mathbb Z_p$ on a connected Hausdorff
second-countable $n$-manifold without boundary has nonzero kernel, so
the action factors through a finite quotient [S4:22–35].

**The signature-lattice obstruction.** The proof by contradiction
produces an integral cohomological obstruction. For an odd integer
$d>n$ it constructs an abelian group $E_d(S^d)$, an orientation class
$u_d$, and a positive integer $L_d$ such that rationaly the group is
one-dimensional over the orientation class, with integral elements
constrained to a lattice of index $L_d$. A faithful $\mathbb Z_p$-action
would supply, for every $k\ge1$, $p^k$ integral classes with equal
rational images summing to $4u_d$; each image is then $(4/p^k)u_d$,
which lies outside the fixed lattice once $p^k>4L_d$ — the
contradiction [S4:165–231].

**How the action supplies the equal parts.** Newman's rigidity
theorem for periodic transformations is the local input: a
finite-order homeomorphism fixing a nonempty open set pointwise is the
identity. The action is localized to a coordinate chart, thickened to
a product $W=O\times\mathbb R^{d-n}$, one-point compactified and passed
through the orbit space of a small open $\mathbb Z_p$-subgroup, so the
characters of $\mathbb Z_p$ — the roots of unity of $p$-power order — decompose
the sheaf complex into orthogonal character parts whose signature data
carry the $p^k$ equal rational parts the lattice forbids
[S4:235–314].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Hilbert's fifth problem asked how far differentiability could be
removed from the theory of continuous transformation groups. Gleason
and Montgomery--Zippin resolved the locally Euclidean formulation in
1952, and Yamabe extended the structure theory to general locally
compact groups. One- and two-manifold cases were classical; Pardon
proved the three-dimensional case using incompressible surfaces in an
invariant open set and the resulting action on a surface mapping class
group. A separate line controls the action by its regularity:
Bochner--Montgomery for the differentiable case, Repovš--Ščepin for
Lipschitz actions, Maleshich for Hölder actions, and Martin for
quasiconformal actions. Their dimension-raising obstructions connect
to the integral cohomological dimension theory of Yang and
Bredon--Raymond--Williams, and Shelukhin used Floer-theoretic methods
to exclude nontrivial continuous $\mathbb Z_p$-actions on a class of closed
symplectic manifolds [S4:59–127].

## Consequences

**The Hilbert--Smith conjecture is true in every finite dimension.**
Every locally compact second-countable Hausdorff group acting
faithfully and jointly continuously on a connected Hausdorff
second-countable $n$-manifold without boundary is a Lie group
[S4:9–14].

**A dynamical corollary (Pardon's Conjecture 1.4).** For such a
manifold, an almost periodic homeomorphism — one whose cyclic subgroup
has compact closure in $\mathrm{Homeo}(M)$ — has a positive iterate that is the
time-one map of a continuous real flow: the compact closure is a
compact abelian Lie group whose identity component is a torus of finite
index [S4:42–55].

## Section skeleton

**Manuscript** [S3:89–94], 6 sections under `build/sections/`:
01-introduction [S4:9–14], 02-categories, 03-localization, 04-lattice,
05-local-tests, 06-character-classes. Plus one figure
(`build/figures/local-test`) and one appendix
(`build/appendices/duality-signs`). Its root is `build/main.tex`, with
a `references.bib` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— 6 `.tex` files in `build/sections/`, one in the root, one in
`build/figures/`, and one in `build/appendices/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 304 at line 7512. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 702. |
| S3 | [`preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/main.tex`](../../../preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/main.tex) | 111 | Manuscript main file: title and abstract. |
| S4 | [`preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/sections/01-introduction.tex) | 314 | Introduction: the statement, the predecessors, the duality mechanism, the lattice obstruction, and how the action supplies the equal parts. |
| S5 | [`preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/references.bib`](../../../preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/references.bib) | 452 | Manuscript bibliography. |

## Bibliography

- The Stacks Project Authors, The Stacks Project: Proper Base Change in Topology (2026)
- The Stacks Project Authors, The Stacks Project: Derived Colimits (2026)
- The Stacks Project Authors, The Stacks Project: Derived Categories (2026)
- The Stacks Project Authors, The Stacks Project: Čech and Sheaf Cohomology (2026)
- Balmer, Paul, Triangular Witt Groups. Part I: The 12-Term Localization Exact Sequence (2000)
- Balmer, Paul, Walter, Charles, A Gersten–Witt Spectral Sequence for Regular Schemes (2002)
- Bergfalk, Jeffrey, Lupini, Martino, Panagiotopoulos, Aristotelis, The Definable Content of Homological Invariants II: Čech Cohomology and Homotopy Classification (2024)
- Bochner, Salomon, Montgomery, Deane, Locally Compact Groups of Differentiable Transformations (1946)
- Bredon, G. E., Raymond, Frank, Williams, R. F., $p$-Adic Groups of Transformations (1961)
- Coste, Michel, An Introduction to Semialgebraic Geometry (2000)
- Dranishnikov, Alexander N., Ferry, Steven C., Weinberger, Shmuel, Large Riemannian Manifolds Which Are Flexible (2003)
- Eilenberg, Samuel, Steenrod, Norman, Foundations of Algebraic Topology (1952)
- Gleason, Andrew M., Groups without small subgroups (1952)
- Hardt, Robert M., Semi-Algebraic Local-Triviality in Semi-Algebraic Mappings (1980)
- Hardt, Robert, Lambrechts, Pascal, Turchin, Victor, Volić, Ismar, Real Homotopy Theory of Semi-Algebraic Sets (2011)
- Hatcher, Allen, Algebraic Topology (2002)
- Hilbert, David, Mathematical problems (1902)
- Hornbostel, Jens, Schlichting, Marco, Localization in Hermitian K-Theory of Rings (2004)
- Kashiwara, Masaki, Schapira, Pierre, Sheaves on Manifolds (1990)
- Lee, Joo Sung, Totally disconnected groups, $p$-adic groups and the Hilbert–Smith conjecture (1997)
- Maleshich, Iozhe, The Hilbert–Smith Conjecture for Hölder Actions (1997)
- Martin, Gaven J., The Hilbert–Smith Conjecture for Quasiconformal Actions (1999)
- Mj, Mahan, Pattern Rigidity and the Hilbert–Smith Conjecture (2012)
- Montgomery, Deane, Zippin, Leo, Small subgroups of finite-dimensional groups (1952)
- Montgomery, Deane, Zippin, Leo, Topological Transformation Groups (1955)
- Newman, M. H. A., A Theorem on Periodic Transformations of Spaces (1931)
- Pardon, John, The Hilbert–Smith Conjecture for Three-Manifolds (2013)
- Pardon, John, Totally disconnected groups (not) acting on two-manifolds (2019)
- Ranicki, Andrew, Weiss, Michael, On the Construction and Topological Invariance of the Pontryagin Classes (2010)
- Raymond, Frank, The Orbit Spaces of Totally Disconnected Groups of Transformations on Manifolds (1961)
- Schapira, Pierre, An Introduction to Categories and Sheaves (2023)
- Serre, Jean-Pierre, Homologie singuli{\`e}re des espaces fibrés. Applications (1951)
- Serre, Jean-Pierre, Groupes d'homotopie et classes de groupes abéliens (1953)
- Shelukhin, Egor, A Symplectic Hilbert–Smith Conjecture (2024)
- Verdier, Jean-Louis, Dualité dans la cohomologie des espaces localement compacts (1966)
- Woolf, Jon, Witt Groups of Sheaves on Topological Spaces (2008)
- Yamabe, Hidehiko, On the conjecture of Iwasawa and Gleason (1953)
- Yamabe, Hidehiko, A generalization of a theorem of Gleason (1953)
- Yang, Chung-Tao, $p$-Adic Transformation Groups (1960)
- Repovš, Dušan, Ščepin, Evgenij V., A Proof of the Hilbert–Smith Conjecture for Actions by Lipschitz Maps (1997)
