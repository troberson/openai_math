[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 340](../index/differential-geometry/340-a-counterexample-to-the-nearby-lagrangian-conjecture.md)

# 340 — A counterexample to the nearby Lagrangian conjecture

[Index page](../index/differential-geometry/340-a-counterexample-to-the-nearby-lagrangian-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:8272] and the catalog abstract [S2:778] state
the family's claim: a disproof of the unrestricted nearby Lagrangian
conjecture, by constructing for some sufficiently large even $N$ a
closed exact embedded Lagrangian in $T^*(S^9\times S^{N-1})$ that is
diffeomorphic to the base but not Hamiltonian isotopic to its zero
section. The manuscript's abstract "We disprove the unrestricted nearby Lagrangian conjecture. For some
sufficiently large even integer $N$, we construct a closed exact smoothly
embedded Lagrangian in $T^*(S^9\times S^{N-1})$ that is diffeomorphic to
the base but is not Hamiltonian isotopic to the zero section. [S3:8–13]"

## Undergraduate summary

Arnold's nearby Lagrangian conjecture asks whether every closed exact
embedded Lagrangian in the cotangent bundle $T^*Q$ is Hamiltonian
isotopic to the zero section. For $Q=S^2$ the answer is yes, from
positive isotopy results and the classification of closed surfaces.
In general, the cotangent projection $\pi:L\to Q$ of a nearby
Lagrangian is a homotopy equivalence (Abouzaid, Kragh) and even a
simple homotopy equivalence (Abouzaid–Kragh), so the abstract smooth
manifold $L$ agrees with $Q$. The conjecture asks the stronger question
of ambient Hamiltonian isotopy class. The manuscript answers
negatively: the projection can be a diffeomorphism while the
Lagrangian sits in a nontrivial Hamiltonian isotopy class


> **theorem**
For some sufficiently large even integer $N$, the manifold
$Q=S^9\times S^{N-1}$ admits a closed exact smoothly embedded Lagrangian
$L\subset T^*Q$ such that $L$ is diffeomorphic to $Q$ and no compactly
supported Hamiltonian isotopy carries the zero section to $L$. [S4:25–30]

Both the base and the Lagrangian are connected and simply connected.
The obstruction is to how $L$ lies in the cotangent bundle, not to
its intrinsic smooth structure.

## Graduate summary

**Stable tube spaces and a kernel class.** The construction uses
Waldhausen's algebraic $K$-theory of spaces. The generating families
agree outside a fixed ball with degree-two homogeneous functions;
their negative domains form a stable smooth tube space $\mathbf{T}$.
A map $\gamma:\mathbf{T}\to BG$ associates to each tube family its
stable spherical fibration. Using Rognes's low-degree smooth Whitehead
group calculation, the manuscript exhibits a nonzero class
$a\in\pi_9\mathbf{T}$ with $\gamma_*a=0$: the tube family is nontrivial
while its fibration is trivial [S5:1–8].

**The one-critical-point obstruction.** The key obstruction proposition
states that a smooth family $f_b:\mathbb R^{2p}\to\mathbb R$, $b\in S^9$, homogeneous
at infinity with smooth data in $T_{p,p}$, with exactly one nondegenerate
critical point per fiber and zero stable spherical class, has zero
stable tube class. The proof proceeds in two stages: Morse theory gives
a fiber homotopy equivalence between the negative eigendirections at
the critical point and the negative domain at infinity; the local
quadratic model, after normalization, produces a family of
$h$-cobordisms between an inner and outer sphere in the regular zero
level. Thickening and extending into a cylinder gives a cobordism with
a product complement, and stability yields a product for the whole
family, contradicting the nontriviality of $a$ [S4:142–156].

**Embedding via the sphere factor.** The extra sphere factor in
$Q=S^9\times S^{N-1}$ realizes the class: a scale function $R(b)$
and a linear coupling to $v\in S^{N-1}$ arrange that the critical
locus satisfies $\nabla g_b(w)=R(b)v$. Homogeneity parametrizes this
locus by $S^9\times S^{N-1}=Q$. The sphere and base momenta are the
two components of the generated covector; equality of sphere momenta
confines the difference between two putative coincident branches to
one line, and varying $R$ over $S^9$ separates the remaining pairs
[S4:157–173].

**Transport to the zero section.** The final section follows the
generating family through a hypothetical Hamiltonian isotopy to the
zero section. The direct small-step construction preserves the stable
class of the homogeneous data. At the zero section, the critical-locus
projection would be a diffeomorphism, giving a unique nondegenerate
critical point over each base point. Restricting to a fixed $S^9$ slice
gives precisely the family excluded by the one-critical-point
proposition, completing the contradiction [S4:170–173].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The nearby Lagrangian conjecture is a modern formulation of a question
in Arnold's discussion of Lagrangian knots. Classical intersection
theorems of Hofer and Laudenbach–Sikorav constrain Hamiltonian
deformations of the zero section; generating functions provide one
route to such results. Positive isotopy results in low dimension
include Hind's theorem for Lagrangian spheres in $T^*S^2$ and the
cotangent-torus theorem of Dimitroglou Rizell–Goodman–Ivrii, which
together give the closed exact case over $S^2$. On the topological
side, Fukaya–Seidel–Smith and Nadler established cohomological and
categorical constraints under additional assumptions; Abouzaid proved
the projection is a homotopy equivalence when the Maslov class vanishes;
Kragh removed that hypothesis; Abouzaid–Kragh proved it is a simple
homotopy equivalence. More recent work by Abouzaid–Courte–Guillermou–
Kragh and by Abouzaid–Álvarez-Gavela–Courte–Kragh constrains the
normal invariant of the projection; Porcelli–Smith place it in the
image of the stable Hopf action. Álvarez-Gavela–Igusa–Sullivan
constructed Legendrians with nontrivial tube torsion in the jet space
$J^1Q$; the present construction works in $T^*Q$ proper and proves
branch separation. Courte–Porcelli constrain the parametrized Whitehead
torsion of families of nearby Lagrangians [S4:42–120].

## Consequences

**The unrestricted nearby Lagrangian conjecture is false.** For some
sufficiently large even $N$, there exists a closed exact smoothly
embedded Lagrangian in $T^*(S^9\times S^{N-1})$ diffeomorphic to the
base but not Hamiltonian isotopic to the zero section
[S4:25–30].

**The cotangent projection can be a diffeomorphism without the
Lagrangian being Hamiltonian isotopic to the zero section.** The
obstruction is to the ambient isotopy class, not to the abstract
smooth structure or the projection's homotopy class [S4:33–38].

**A nonzero stable tube class with trivial associated fibration is
realized as an embedded Lagrangian in $T^*Q$.** The construction
exhibits a family in $\pi_9\mathbf{T}$ that maps to zero under
$\gamma:\mathbf{T}\to BG$ and proves every possible pair of coincident
cotangent branches is separated [S5:1–8].

## Section skeleton

**Manuscript** [S3:8–13], 7 sections under `build/sections/`: introduction
[S4:25–30], tubes [S5], morse, obstruction, embedding, transport. Its root
is `build/main.tex`, with a `preamble.tex` and a `references.bib`
bibliography. Two figure files under `build/figures/`
(`momentum-separation.tex`, `regular-band.tex`).

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — a root `build/main.tex`, a `preamble.tex`, 6 `.tex` files
under `build/sections/`, 2 figure `.tex` files, and a `references.bib`
bibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 340 at line 8272. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 778. |
| S3 | [`preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/main.tex`](../../../preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/main.tex) | 26 | Manuscript main file: title and abstract. |
| S4 | [`preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/sections/introduction.tex`](../../../preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/sections/introduction.tex) | 173 | Introduction: the main theorem, context, and the proof strategy in generating-family language. |
| S5 | [`preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/sections/tubes.tex`](../../../preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/sections/tubes.tex) | 258 | Stable tube spaces: the nonzero kernel class whose fibration is trivial. |
