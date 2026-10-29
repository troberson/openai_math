[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 310](../index/topology/310-quillens-conjecture-in-rational-homology.md)

# 310 — Quillen's conjecture in rational homology

[Index page](../index/topology/310-quillens-conjecture-in-rational-homology.md)

## Original CONTENTS.md summary

The release's blurb [S1:7651] and the catalog abstract [S2:714] state
the family's claim: Quillen's conjecture is proved for every finite
group and every prime in its stronger rational-homology form. If the
largest normal $`p`$-subgroup $`O_p(G)`$ is trivial, the poset of
nontrivial elementary abelian $`p`$-subgroups has nonzero augmented
reduced rational homology, and is therefore not contractible. The
manuscript's abstract "We prove Quillen's conjecture for all finite groups and all primes.
More precisely, if a finite group $`G`$ has trivial largest normal
$`p`$-subgroup $`O_p(G)`$, then the poset of nontrivial elementary abelian
$`p`$-subgroups of $`G`$ has nonzero augmented reduced rational homology.
This establishes the stronger rational-homology form of the conjecture. [S3:69–75]"

## Undergraduate summary

The order complex of a poset turns its chains of elements into the
faces of a simplicial complex, and contractibility of that complex is
a topological statement about how the elements sit inside one
another. Quillen's conjecture concerns the poset $`\mathcal A_p(G)`$ of
the nonidentity elementary abelian $`p`$-subgroups of a finite group
$`G`$, ordered by inclusion. It predicts that this order complex is
contractible exactly when $`G`$ has a nontrivial normal $`p`$-subgroup:
the elementary abelian subgroups "detect" a normal $`p`$-part if and
only if one exists. The manuscript proves a stronger, rational version
of the same dichotomy [S4:3–8]:

> **theorem**
For every finite group $`G`$ and every prime $`p`$, if $`O_p(G)=1`$, then
$$\widetilde H_*(\mathcal A_p(G);\mathbb Q)\ne0.$$
Here reduced homology is augmented, so that the empty poset has
$`\widetilde H_{-1}(\varnothing;\mathbb Q)=\mathbb Q`$. [S4:15–22]

The contrapositive is the content: a trivial $`p`$-core forces nonzero
reduced rational homology somewhere in the order complex, so the
complex cannot be contractible. Because a contractible nonempty
complex has zero reduced homology and the empty complex is not
contractible, the rational statement outright settles the original
contractibility conjecture, with no restriction on the prime or on the
composition factors of $`G`$.

## Graduate summary

**Why rational.** The nonvanishing is over $`\mathbb Q`$, which is the form
that propagates. The order complex is finite, so a nonzero rational
homology group arises from an integral homology group of positive free
rank; the universal coefficient theorem then lifts it to nonzero
reduced homology over every field in the same degree. Conversely, a
nontrivial $`p`$-core makes $`\mathcal A_p(G)`$ contractible, so acyclicity
over any fixed field characterizes the existence of a normal $`p`$-
subgroup. The rational reduction to the component cases is what lets
the earlier reduction theorems, developed over $`\mathbb Q`$, feed the present
proof [S4:40–99].

**The cycle construction.** The proof builds nonzero cycles on full
subgroup flags. A "frame" is a decomposition of a vector space into
lines (nondegenerate and mutually orthogonal when a form is present);
independent scalar signs on the lines give an elementary abelian
projective subgroup, and its flags support apartment chains. Relations
between frames differing only inside a plane force the boundaries of
their chains to cancel. The load-bound is a dimension lower bound on
the resulting coefficient space, uniform as the ambient dimension grows
over a fixed field, proved by encoding merger trees of frame lines in
multilinear Lie superbrackets with a Poincaré--Birkhoff--Witt argument
[S4:102–138].

**From a coefficient to homology.** The constructed cycle can live in
a larger automorphism group than the chosen extension $`H`$ of a simple
component. A restriction procedure selects a supported elementary
group with largest intersection index and takes a residue at a fixed
complement, where the operation is injective, so one nonzero full-flag
coefficient survives. At the prime two a minimal-counterexample
argument with proper-subgroup induction supplies a nonbounding cycle in
the relevant centralizer; for odd primes the cited reduction asks for
nonzero homology in the largest possible degree for certain unitary
extensions, which the rank formula establishes before the cycles are
built [S4:141–171].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Quillen formulated the contractibility conjecture in 1978, building on
the homotopy equivalence between $`\mathcal A_p(G)`$ and Brown's poset
of all nonidentity $`p`$-subgroups, and proved it for solvable groups,
groups of elementary abelian $`p`$-rank at most two, and groups of Lie
type in defining characteristic. The almost-simple case was settled by
Aschbacher and Kleidman, and Aschbacher--Smith developed the
component-extension control for $`p>5`$, reducing the problem to a
dimension property for specified elementary extensions of unitary
groups. Piterman and Smith extended the reduction to all odd primes;
Díaz-Ramos proved the required unitary result, and at the prime two a
sequence of component eliminations by Piterman and collaborators
narrowed the remaining Lie-type families. The present proof retains a
direct frame proof of the unitary dimension property and closes the
last cases by its cycle and propagation constructions [S4:40–99].

## Consequences

**Quillen's conjecture is resolved for every finite group and every
prime.** If $`O_p(G)=1`$ then $`\widetilde H_*(\mathcal A_p(G);\mathbb Q)\ne0`$;
in particular the order complex is not contractible. The statement
imposes no restriction on the prime or on the composition factors of
$`G`$ [S4:15–22].

**The rational-homology form characterizes the $`p`$-core.** Acyclicity
of $`\mathcal A_p(G)`$ over any fixed field is equivalent to the
existence of a nontrivial normal $`p`$-subgroup: a nonzero rational
homology group lifts to every field by the universal coefficient
theorem, while a nontrivial $`p`$-core makes the complex contractible
[S3:69–75].

## Section skeleton

**Manuscript** [S3:69–75], 10 sections under `build/sections/`:
introduction [S4:15–22], reductions, propagation, frames, chain-procedures,
linear, symplectic, orthogonal, exceptional, conclusion. Plus one
figure (`build/figures/fixed-complement.tex`). Its root is
`build/paper.tex`, with a `glyph-mappings.tex` and a `references.bib`
bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— 10 `.tex` files under `build/sections/`, a root `build/paper.tex`,
one `glyph-mappings.tex`, one figure under `build/figures/`, and a
`references.bib` bibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 310 at line 7651. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 714. |
| S3 | [`preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/paper.tex`](../../../preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/paper.tex) | 94 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/sections/01-introduction.tex) | 182 | Introduction: the setup, the main theorem, the background and reductions, the cycle construction, the passage from a coefficient to homology, and the organization. |
| S5 | [`preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/references.bib`](../../../preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/references.bib) | 243 | Manuscript bibliography. |

## Bibliography

- Aschbacher, Michael, Smith, Stephen D., On Quillen's conjecture for the $`p`$-groups complex (1993)
- Aschbacher, Michael, Kleidman, Peter B., On a conjecture of Quillen and a lemma of Robinson (1990)
- Brown, Kenneth S., Euler characteristics of groups: the $`p`$-fractional part (1975)
- Chernousov, Vladimir, Elduque, Alberto, Knus, Max-Albert, Tignol, Jean-Pierre, Algebraic groups of type $`D_4`$, triality, and composition algebras (2013)
- Golod, Evgenii S., Shafarevich, Igor R., On the class field tower (1964)
- Gorenstein, Daniel, Lyons, Richard, Solomon, Ronald, The Classification of the Finite Simple Groups, Number 3. Part I, Chapter A: Almost Simple $`K`$-Groups (1998)
- Milne, James S., Fields and Galois Theory (2022)
- Milne, James S., Descent for algebraic schemes (2024)
- Milnor, John W., Moore, John C., On the structure of Hopf algebras (1965)
- Piterman, Kevin Iván, Smith, Stephen D., Some results on Quillen's conjecture via equivalent-poset techniques (2025)
- Piterman, Kevin Iván, Smith, Stephen D., Eliminating components in Quillen's conjecture (2022)
- Piterman, Kevin Iván, Maximal subgroups of exceptional groups and Quillen's dimension (2024)
- Piterman, Kevin Iván, Components in characteristic $`p`$ and Quillen's conjecture (2026)
- Piterman, Kevin Iván, An approach to Quillen's conjecture via centralisers of simple groups (2021)
- Piterman, Kevin Iván, Welker, Volkmar, Homotopy properties of the complex of frames of a unitary space (2024)
- Quillen, Daniel, Homotopy properties of the poset of nontrivial $`p`$-subgroups of a group (1978)
- Díaz Ramos, Antonio, Quillen's conjecture and unitary groups (2026)
- Díaz Ramos, Antonio, On Quillen's conjecture for $`p`$-solvable groups (2018)
- Díaz Ramos, Antonio, Mazza, Nadia, A geometric approach to Quillen's conjecture (2022)
- Björner, Anders, Some combinatorial and algebraic properties of Coxeter complexes and Tits buildings (1984)
- Robinson, Alan, Partition complexes, duality and integral tree representations (2004)
- Scheunert, Manfred, The Theory of Lie Superalgebras: An Introduction (1979)
- Segev, Yoav, Webb, Peter, Extensions of $`G`$-posets and Quillen's complex (1994)
- Solomon, Louis, The Steinberg character of a finite group with BN-pair (1969)
- Stanley, Richard P., Some aspects of groups acting on finite posets (1982)
- Steinberg, Robert, Automorphisms of finite linear groups (1960)
- Taylor, Donald E., The Geometry of the Classical Groups (1992)
