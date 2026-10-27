[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 041](../index/algebraic-and-complex-geometry/041-hyperkahler-syz-and-projective-space-bases.md)

# 041 — Hyperkähler SYZ and projective-space bases

[Index page](../index/algebraic-and-complex-geometry/041-hyperkahler-syz-and-projective-space-bases.md)

## Original CONTENTS.md summary

The release's blurb "**041. Hyperkähler SYZ and projective-space bases.** Proves the strong hyperkähler SYZ conjecture: every holomorphic line bundle with nonzero nef isotropic first Chern class on a compact irreducible holomorphic symplectic Kähler manifold is semiample. It also proves that every projective Lagrangian fibration with normal projective base has projective space as its base, in every dimension and deformation type. [S1:1160]" The two manuscripts
are "The strong hyperkähler SYZ conjecture [S3:1]" and the projective-space bases companion [S11:1].
The SYZ abstract reads: "We prove the strong hyperkähler SYZ conjecture: every holomorphic line
bundle with nonzero nef isotropic first Chern class on a compact
irreducible holomorphic symplectic Kähler manifold is semiample. [S4:7–11]"

## Undergraduate summary

A compact irreducible holomorphic symplectic (IHS) Kähler manifold
has a symplectic form $\sigma$ with $H^0(X,\Omega_X^2)=\mathbb C\sigma$
and even complex dimension $2n$. A line bundle $L$ is nef isotropic
when $c_1(L)$ lies on the boundary of the Kähler cone and satisfies
$q(c_1(L))=0$ for the Beauville–Bogomolov–Fujiki form. Such a class
has numerical dimension exactly $n$, by Fujiki's relation [S5:15–23].
"A nonzero nef isotropic class has numerical dimension $n$, by
Fujiki's relation: its powers have positive intersection with a
Kähler class through degree $n$, and zero intersection in higher
degrees. The strong hyperkähler SYZ conjecture asks whether every
line bundle with such a class is semiample
\cite[Conjecture 1.7]VerbitskySYZ. This would turn a class on the
boundary of the Kähler cone into a holomorphic map with
half-dimensional fibers. The numerical condition by itself supplies
neither sections nor control of their base locus. [S5:15–23]" The strong SYZ conjecture (Verbitsky) asks whether every
such line bundle is semiample. The theorem 

> **theorem**
Let $X$ be a compact irreducible holomorphic symplectic Kähler
manifold of complex dimension $2n$, where $n\ge1$. If a holomorphic
line bundle $L$ satisfies
\[
 c_1(L)\ne0,\qquad c_1(L)\in\overline{\mathcal K_X},
                  \qquad q_X(c_1(L))=0,
\]
then $L$ is semiample.

More precisely, there exist a positive integer $m$, a normal
projective variety $B$, an ample line bundle $A$ on $B$, and a
surjective holomorphic map with connected fibers
\[
                 f:X\longrightarrow B,\qquad L^m\simeq f^*A,
\]
such that $\dim_{\mathbb C}B=n$. Every irreducible component of every
fiber has complex dimension $n$, and $\sigma$ vanishes on its
smooth locus. [S5:25–44]

The conclusion is that a positive power of $L$ defines a Lagrangian
fibration $f:X\to B$ with $\dim B=n$ and every component of every
fiber Lagrangian — the holomorphic version of the SYZ
fibration picture.

## Graduate summary

**The finiteness corollary.** Combining the semiampleness theorem
with the boundedness of Lagrangian-fibered symplectic varieties
(Engel–Filipazzi–Greer–Mauri–Svaldi) gives finiteness of smooth
deformation types in dimension $2n$ with $b_2\ge5$ 

> **corollary**
For each integer $n\ge1$, there are only finitely many smooth
deformation types of compact irreducible holomorphic symplectic
Kähler manifolds of complex dimension $2n$ with $b_2\ge5$.
\endcorollary

This follows by combining Theorem   with the boundedness
of Lagrangian-fibered symplectic varieties proved by
Engel–Filipazzi–Greer–Mauri–Svaldi  . [S5:57–65]

**The projective corollary.** When $X$ is projective, the base must
be projective space, with no codimension-one multiple
fibers 

> **corollary**
In Theorem  , assume additionally that $X$ is projective,
and let $f:X\to B$ be the associated connected-fiber map furnished there.
Then $B\simeq\mathbb P^n_{\mathbb C}$. Moreover, there do not exist a prime
divisor $D\subset B$, an effective divisor $E$ on $X$, and an integer
$r>1$ such that $f^*D=rE$. [S5:69–74]

This is a consequence of the companion's projective-space base
theorem 

> **theorem**
Let \(n\geq1\), and let \(X\) be a compact irreducible holomorphic symplectic
Kähler manifold of dimension \(2n\), with symplectic form \(\sigma\).
Suppose that
\[
                       f:X\longrightarrow B
\]
is a projective surjective holomorphic morphism with connected fibers,
where \(B\) is a normal projective variety of dimension \(n\).
Assume that every irreducible component of every fiber has dimension
\(n\) and that the restriction of \(\sigma\) to its smooth locus is zero.
Then \(B\) is isomorphic to \(\mathbb P^n_{\mathbb C}\). [S13:59–70]

The companion's proof first establishes smoothness of the base and
then applies Hwang's smooth-base theorem . "For projective IHS total spaces, the cohomological constraint is already
that of projective space: Shen–Yin compute the rational intersection
cohomology of \(B\) as one-dimensional in degrees \(0,2,\ldots,2n\) and
zero in odd degrees \cite[Theorem 0.4(a)]ShenYin2022. This does not itself establish
smoothness. Our proof first establishes smoothness and then applies Hwang's
theorem. [S13:52–57]"
Its inputs include the SYZ semiampleness theorem, a polarized
family for a prescribed class, and a torsion-free finite-index
isometry group [S13:81–90].

## History of the conjecture

The SYZ conjecture connects to the Strominger–Yau–Zaslow
mirror-symmetry picture: in the hyperkähler setting, rotation of
complex structure relates special Lagrangian and holomorphic
Lagrangian geometry [S5:85–103]. Matsushita established the
half-dimensional and Lagrangian character of fibrations;
Greb–Lehn extended to compact Kähler IHS total spaces [S5:96–103].

Analytic positivity results: Verbitsky proved semiampleness
with a smooth semipositive metric; Höring–Lazić–Lehn obtained
nonvanishing or coisotropic-locus alternatives [S5:105–115].
"Analytic positivity gives another source of progress. Verbitsky proves
that a nontrivial nef isotropic bundle with a smooth semipositive
Hermitian metric has a nonzero section in some positive power
\cite[Theorem 1.9]VerbitskySYZ.
Höring–Lazić–Lehn obtain nonvanishing or coisotropic-locus
alternatives for nef isotropic classes. In complex dimension four,
they prove semiampleness if the class contains a closed positive
current whose Lelong numbers all vanish
\cite[Theorem D and Corollary E]HoringLazicLehn.
These results show how additional analytic positivity or geometric
information can turn the numerical condition into sections. [S5:105–115]"

The deformation approach (Soldatenkov–Verbitsky, Bayer–Macrì,
Markman, Yoshioka, Mongardi–Rapagnetta, Mongardi–Onorati)
established the conjecture for each known deformation type
[S5:117–130].

The projective-space base problem: Hwang proved it for smooth
bases, Greb–Lehn for compact Kähler total spaces, leaving the
singular-base case . "Hwang proved the projective-space conclusion when \(X\) is projective and
\(B\) is smooth \cite[Theorem 1.2]Hwang2008. Greb and Lehn extended the
smooth-base theorem to compact Kähler IHS total spaces
\cite[Theorem 1.1]GrebLehn2014. These results reduce the base problem to
the possible singularities of \(B\). [S13:16–20]" Ou reduced the
dimension-four surface base to $\mathbb P^2$ or a specific Fano
surface; Huybrechts–Xu excluded the second case; Müller–Zheng Xu
proved a local smoothness theorem [S13:37–50].

## Consequences

**The strong SYZ conjecture in full.** Every nonzero nef
isotropic line bundle on a compact IHS Kähler manifold is
semiample, in every dimension and deformation type, with no
$B_2$ restriction [S5:25–44].

**Finiteness of deformation types.** For $b_2\ge5$, there are
finitely many smooth deformation types in each even complex
dimension [S5:57–65].

**Projective-space bases.** Every projective Lagrangian
fibration with normal projective base has $\mathbb P^n$ as its base,
and no codimension-one multiple fibers exist [S13:59–70].

## Section skeleton

**Main manuscript** (6 sections under `build/sections/`):

1. Introduction [S5]
2. Metric estimates [S6]
3. Completion [S7]
4. The complex-structure rotation [S8]
5. The polarized family [S9]
6. The finiteness deduction [S10]

Main file: `main.tex` [S4:7–11].

**Companion manuscript** (12 sections under `build/source/sections/`):

1. Introduction [S13]
2. Setup [S14]
3. Local tensor [S15]
4. Stratum analysis [S16]
5. Base change [S17]
6. The Euler characteristic [S18]
7. Deformation [S19]
8. The isotrivial case [S20]
9. The second system [S21]
10. The variation [S22]
11. The quotient [S23]
12. The conclusion [S24]

Main file: `source/main.tex` [S12].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The main manuscript
ships 7 `.tex` files under `build/`; the companion ships 12 under
`build/source`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 041 at line 1160. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 160. |
| S3 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/README.md`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/README.md) | 17 | Main manuscript readme: title, author, date. |
| S4 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/main.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/main.tex) | 23 | Main manuscript main file: abstract and section inputs. |
| S5 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/introduction.tex) | 259 | The strong SYZ theorem, the finiteness corollary, the projective corollary, and the context. |
| S6 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/metric_estimates.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/metric_estimates.tex) | 605 | Metric estimates. |
| S7 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/completion.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/completion.tex) | 478 | Completion. |
| S8 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/rotation.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/rotation.tex) | 466 | The complex-structure rotation. |
| S9 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/polarized_family.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/polarized_family.tex) | 687 | The polarized family. |
| S10 | [`preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/finiteness.tex`](../../../preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/build/sections/finiteness.tex) | 65 | The finiteness deduction. |
| S11 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/README.md`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/README.md) | 17 | Companion manuscript readme: title, author, date. |
| S12 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/main.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/main.tex) | 83 | Companion main file. |
| S13 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/01-introduction.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/01-introduction.tex) | 253 | The projective-space base theorem, the historical context, and the proof inputs. |
| S14 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/02-setup.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/02-setup.tex) | 171 | Setup. |
| S15 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/03-local-tensor.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/03-local-tensor.tex) | 1067 | Local tensor. |
| S16 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/04-stratum.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/04-stratum.tex) | 789 | Stratum analysis. |
| S17 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/05-base-change.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/05-base-change.tex) | 1086 | Base change. |
| S18 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/06-euler.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/06-euler.tex) | 1045 | The Euler characteristic. |
| S19 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/07-deformation.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/07-deformation.tex) | 493 | Deformation. |
| S20 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/08-isotrivial.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/08-isotrivial.tex) | 902 | The isotrivial case. |
| S21 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/09-second-system.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/09-second-system.tex) | 612 | The second system. |
| S22 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/10-variation.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/10-variation.tex) | 571 | The variation. |
| S23 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/11-quotient.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/11-quotient.tex) | 871 | The quotient. |
| S24 | [`preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/12-conclusion.tex`](../../../preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/build/source/sections/12-conclusion.tex) | 39 | The conclusion. |
