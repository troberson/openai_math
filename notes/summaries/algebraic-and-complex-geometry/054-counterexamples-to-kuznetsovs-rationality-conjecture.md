[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 054](../../index/algebraic-and-complex-geometry/054-counterexamples-to-kuznetsovs-rationality-conjecture.md)

# 054 — Counterexamples to Kuznetsov's rationality conjecture

[Index page](../../index/algebraic-and-complex-geometry/054-counterexamples-to-kuznetsovs-rationality-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1388]: "**054. Irrational cubic fourfolds with Hodge-theoretic and categorical K3 associations.** For every sufficiently large admissible Hassett discriminant, a very general smooth complex cubic fourfold is irrational despite having both an untwisted geometric K3 category and an integral Hodge-theoretic K3 association. This disproves Kuznetsov's rationality conjecture and the sufficiency of the associated-K3 criterion for rationality; the discriminant threshold is ineffective." The manuscript title is
"Irrational cubic fourfolds with geometric K3 categories" [S3:1], and its abstract [S4:51–58] reads: "For every sufficiently large admissible Hassett discriminant, we prove that"

## Undergraduate summary

A smooth cubic fourfold $X\subset\mathbf P^5$ is rational if its function
field is a purely transcendental extension of $\C$ of transcendence
degree four. The connection between this birational question and K3
surfaces appears both in the middle cohomology and in the derived
category [S5:3–7]. "A smooth cubic fourfold \(X\subset\mathbf P^5_{\mathbb C}\) is rational if its field of rational functions is" Kuznetsov's rationality conjecture asserts
that $X$ is rational if and only if its Kuznetsov component
$\Ku(X)$ is equivalent to the derived category of a projective K3
surface. The theorem [S5:77–85]:

> **theorem**


The threshold $d_0$ is ineffective. Some Hassett divisors
($\mathcal C_{26}$, $\mathcal C_{38}$, $\mathcal C_{42}$) consist
entirely of rational cubics [S5:87–92].

## Graduate summary

**The two-evaluations argument.** The proof uses a fixed collection
$\mathcal S$ of Picard-number-one K3 surfaces whose integral
transcendental Hodge lattice, after shifting Hodge types by $(1,1)$
and reversing the pairing, is isometric to $T_X$ [S5:100–118].
An invariant $c_u(f)$ counts prime divisors acquired and lost by a
birational map, each weighted by the MRC-quotient test [S5:121–127]:

> For an integral variety \(E\), let \(u(E)\) be one if the MRC quotient

**Evaluation via smooth factorization.** Weak factorization expresses
$f$ as blowups and blowdowns along smooth centers. Genus-zero
Gromov–Witten pairings determine operators on the transcendental
lattice whose projectors force a blowdown to remove a whole integral
block. Rank $21$ and $h^{3,1}(X)=1$ leave exactly one block, giving
$c_u(f)=1$ [S5:129–150]:

> Smooth weak factorization expresses \(f\) as blowups and blowdowns

**Evaluation via Sarkisov factorization.** The Mori-factorization
pass through conic-bundle nodes gives integer-valued functions $v,s$
on the nodes. The surface calculation at a conic-bundle node uses
finite residue fields and Brauer ramification covers. A second
Sarkisov factorization on the threefold bases gives genus bounds
incompatible with pencils on large-degree K3 surfaces, so the
corrections telescope to $c_u(f)=0$ [S5:152–181]:

> The Sarkisov factorization passes through Mori fibre spaces: contractions

The contradiction $c_u(f)=1$ and $c_u(f)=0$ proves irrationality.

## History of the conjecture

The geometric connection to K3 surfaces grew from explicit rationality
constructions: Fano, Tregub, Beauville–Donagi, Hassett. The
Kuznetsov component gives the categorical connection. Kuznetsov
verified the prediction for Pfaffian cubics. Addington–Thomas proved
the Hodge-theoretic and categorical K3 associations agree on a dense
open subset. Bayer, Lahoz, Macrì, Stellari and collaborators built
stability conditions giving an ordinary K3 derived category for every
cubic with an associated K3 surface [S5:9–71].

## Consequences

**Kuznetsov's rationality conjecture is false.** For every
sufficiently large admissible discriminant, a very general cubic
fourfold is irrational despite having $\Ku(X)\simeq D^b(\Coh S)$
for a smooth projective K3 surface [S5:77–85].

**The associated-K3 rationality prediction is also false.** The same
cubics have untwisted polarized K3 surfaces in the Hodge-theoretic
sense, disproving the sufficiency direction of Huybrechts's
associated-K3 criterion [S4:56–58].

**The threshold is uniform and ineffective.** One bound $d_0$ works
for all lattice data in the irrationality criterion, and the bound is
independent of the test subcollection and the number of links
[S5:178–191].

## Section skeleton

**Main file** [S4], 6 sections under `build/sections/`:

1. Introduction [S5]
2. Preliminaries [S6]
3. Genus-zero Gromov–Witten pairings [S7]
4. The bound [S8]
5. Surface links [S9]
6. Cubics and period data [S10]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
6 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 054 at line 1388. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 184. |
| S3 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/README.md`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/README.md) | 17 | Manuscript readme: title, date. |
| S4 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/paper.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/paper.tex) | 74 | The main file: abstract and section inputs. |
| S5 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/introduction.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/introduction.tex) | 388 | The Kuznetsov component, the admissible definition, the theorem, and the two-evaluations argument. |
| S6 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/preliminaries.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/preliminaries.tex) | 237 | The lattice invariant and the MRC-quotient test. |
| S7 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/gw.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/gw.tex) | 847 | Genus-zero Gromov–Witten pairings and the net-center proposition. |
| S8 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/bounds.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/bounds.tex) | 1215 | The bound on surface centers. |
| S9 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/surface-links.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/surface-links.tex) | 884 | The subfield and surface-link calculation. |
| S10 | [`preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/cubics.tex`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/build/sections/cubics.tex) | 306 | Period and categorical results for admissible divisors. |
