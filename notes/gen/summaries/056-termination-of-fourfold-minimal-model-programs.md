[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 056](../index/algebraic-and-complex-geometry/056-termination-of-fourfold-minimal-model-programs.md)

# 056 — Termination of fourfold minimal model programs

[Index page](../index/algebraic-and-complex-geometry/056-termination-of-fourfold-minimal-model-programs.md)

## Original CONTENTS.md summary

The release blurb 

> **056. Termination of projective and Kähler fourfold minimal model programs.** Proves termination of every existing generalized log canonical flip sequence on globally Weil ℚ-factorial compact Kähler fourfolds, with rational boundary, fixed rational analytically nef b-data, and projective small flip diagrams with the prescribed ample signs. Also proves termination of arbitrary permitted minimal model programs for projective log canonical fourfolds with rational boundary in characteristic zero. [S1:1429]

This family ships **five** termination manuscripts, in two pairs and a
generalized-flip pair. The two generalized-flip termination statements:

Manuscript 1, generalized log canonical flips 

> Every sequence of generalized log canonical flips on a normal irreducible globally Weil \(\mathbbQ\)-factorial compact Kähler fourfold terminates, provided the flips are projective small diagrams with the stated opposite ample signs. The boundary is rational, and the nef b-divisor is fixed and represented by an analytically nef \(\mathbbQ\)-Cartier divisor on a projective modification. No scaling rule or pseudo-effectivity assumption is required. The theorem concerns existing flip sequences; it does not assert the existence of all contractions or flips. [S3:1]

Manuscript 2, generalized-canonical flips 

> Every sequence of generalized-canonical flips on compact Kähler
fourfolds with rational boundary and fixed rational analytically nef
b-divisor terminates when the small morphisms are projective. We prove
this for normal globally Weil $\mathbb Q$-factorial models with boundary
coefficients less than one, allowing exceptional log discrepancies equal
to one. No scaling rule or pseudo-effectivity assumption is required.
The theorem applies to existing projective small diagrams with the
specified opposite ample signs. [S6:1–10]

The two ordinary-program terminations (Kähler, klt, rational boundary):

Manuscript 4, maximal ordinary programs 

> We prove that every maximal ordinary negative-ray program starting from a compact Kähler klt fourfold pair with effective rational boundary in the global Weil-divisor $\mathbb Q$-factorial category terminates. It ends at a nef model when the adjoint is pseudo-effective and at a projective Mori fibre space otherwise. [S9:71–73]

Manuscript 5, finite ordinary programs 

> We prove that a globally Weil-$\mathbb Q$-factorial compact Kähler klt fourfold pair with effective rational boundary and canonical rational line bundle admits a finite ordinary minimal model program starting on the given pair. It ends at a nef model when the adjoint class is pseudo-effective and at a Mori fibre space otherwise. [S11:86–88]

The projective log canonical termination:

Manuscript 3, projective lc fourfolds 

> We prove that every permitted minimal model program for a projective log canonical fourfold with rational boundary over an algebraically closed field of characteristic zero terminates. The result allows arbitrary negative extremal rays and mixed birational steps on the given models, without pseudo-effectivity or initial $\mathbb Q$-factoriality. [S7:63–65]

## Undergraduate summary

The **minimal model program** (MMP) is an algorithm that simplifies a
projective variety by a sequence of standard moves — *divisorial
contractions* and *flips* — until it reaches a canonical "minimal" form
(a model whose canonical divisor is *nef*: nonnegative on every curve),
or a **Mori fibre space** (a fibration onto a lower-dimensional base).
The central obstruction to the algorithm is **termination**: the moves
must stop after finitely many steps, not run forever.

**Flips** are the hard move: they trade one contraction for another in
a way that improves the canonical class, but each flip changes the
geometry, so a priori the chain of flips could be infinite. Termination
of flip sequences is the core hard direction of the birational
classification program.

This family proves that on **fourfolds** (four complex dimensions), in a
collection of related categories — generalized log canonical Kähler
models, ordinary klt Kähler models, and projective log canonical
models — every such flip sequence and every permitted minimal model
program is **finite**. The theorems cover "existing" sequences (manuscripts
1 and 2) and the general existence-plus-finite-steps form (manuscript
3), and give the clean klt fourfold statement in two equivalent
"maximal program" and "finite program" formulations (manuscripts 4
and 5).

## Graduate summary

The five theorems share the fourfold-termination shape but live in
different categories and with different boundary/nef-b-data hypotheses.

**Generalized log canonical flips (Kähler).** 

> **Theorem 1.1**
Let \(X_0\) be a normal irreducible globally Weil \(\mathbbQ\)-factorial compact Kähler fourfold. Let \(B_0\) be an effective rational Weil divisor of finite support with coefficients in \([0,1]\). Let \(\mathbfM\) be represented by an analytically nef \(\mathbbQ\)-Cartier divisor on a projective bimeromorphic normal compact Kähler model of \(X_0\). Fix compatible actual canonical divisor representatives on all birational models under consideration. Suppose that \(D_0=K_X_0+B_0+M_X_0\) is \(\mathbbQ\)-Cartier and that \((X_0,B_0+\mathbfM)\) is generalized log canonical.

Consider a sequence of normal irreducible globally Weil \(\mathbbQ\)-factorial compact Kähler fourfolds
$$X_0\dashrightarrow X_1\dashrightarrow X_2\dashrightarrow\cdots.$$
On \(X_i\), let \(B_i\) be the strict transform of \(B_0\), let \(M_i=M_X_i\) be the trace of the same b-divisor, and assume that \(D_i=K_X_i+B_i+M_i\) is \(\mathbbQ\)-Cartier. Transport the canonical representatives under the induced identifications of prime divisors. Suppose that every step is given by a diagram
$$\label{eq:flip-diagram}
\begin{tikzcd}[column sep=large]
 X_i \arrow[r,"f_i"] & Z_i & X_{i+1}\arrow[l,"f_i^+"']
\end{tikzcd}$$
where \(Z_i\) is normal compact Kähler, both maps are projective small bimeromorphic morphisms with connected fibers, neither is an isomorphism, and
$$-D_i\text{ is }f_i\text{-ample},\qquad
 D_{i+1}\text{ is }f_i^+\text{-ample}.$$
Here _small_ means that the exceptional locus contains no prime divisor. Then the sequence is finite. [S4:25–44]

On a normal irreducible globally Weil $\mathbb Q$-factorial compact Kähler
fourfold with rational boundary and a fixed analytically nef b-divisor,
any sequence of projective *small* flip diagrams with the prescribed
opposite ample signs is finite. The theorem concerns existing flip
sequences; it does not assert the existence of every contraction or
flip.

**Generalized-canonical flips (Kähler).** 

> **theorem**
Let $X_0$ be a normal irreducible globally Weil $\mathbb Q$-factorial compact
Kähler fourfold, and let $B_0\geq0$ be a rational divisor with
coefficients in $[0,1)$. Fix compatible actual canonical divisors on
the birational models. Let $\mathbf M$ be the rational b-divisor represented
by an analytically nef $\mathbb Q$-Cartier divisor $M'$ on a projective
birational morphism $X'\to X_0$ of normal compact Kähler spaces.
Assume
$$\begin{aligned}
 a(E;X_0,B_0+\mathbf M)&>0&&\text{for every prime over $X_0$},\\
 a(E;X_0,B_0+\mathbf M)&\geq1&&\text{for every exceptional prime}.
 \end{aligned}$$
Consider a sequence of normal globally Weil $\mathbb Q$-factorial compact
Kähler fourfolds
$$X_0\dashrightarrow X_1\dashrightarrow X_2\dashrightarrow\cdots .$$
On $X_i$, let $B_i$ be the strict transform of $B_0$, let $M_i$ be
the trace of this same $\mathbf M$, and suppose
$D_i=K_{X_i}+B_i+M_i$ is $\mathbb Q$-Cartier. Suppose that every step is
given by a diagram
$$\label{eq:step-diagram}
 X_i\xrightarrow{\ f_i\ }Z_i
       \xleftarrow{\ f_i^+\ }X_{i+1}$$
of projective small bimeromorphic morphisms with connected fibres,
where $Z_i$ is normal compact Kähler, both morphisms are
nonisomorphisms, $-D_i$ is $f_i$-ample, and $D_{i+1}$ is
$f_i^+$-ample. Then the sequence is finite. [S6:99–130]

The parallel statement for *generalized-canonical* fourfolds (coefficients
in $[0,1)$, exceptional log discrepancies allowed to equal one): every
projective small flip sequence with the fixed analytically nef
b-divisor terminates.

**Projective log canonical fourfolds.** 

> **theorem**
Let $k$ be an algebraically closed field of characteristic zero, and let $(X,B)$ be a projective lc pair of dimension four with rational boundary. No $\mathbb Q$-factoriality or pseudo-effectivity is assumed.
\beginenumerate[label=\textup{(\roman*)}]
\item Every negative extremal ray at every stage has the contraction and, when birational, a positive model required by Definition .
\item Every program of Definition starting from $(X,B)$ has finitely many birational steps, for every sequence of permitted choices.
\item Every maximal program ends either at a projective lc pair with nef adjoint, or at a Mori fibre space: a projective contraction with connected fibres, relative Picard number one, lower-dimensional normal base, and relatively ample negative adjoint.
\endenumerate
An already nef input has a zero-step completed program. [S8:97–105]

Over an algebraically closed field of characteristic zero, a projective
lc pair of dimension four with rational boundary (no $\mathbb Q$-factoriality
or pseudo-effectivity assumed) has: every negative extremal ray
contractable with a required positive birational model, every permitted
program with finitely many birational steps, and every maximal program
ending at a nef adjoint or a Mori fibre space.

**Ordinary programs, maximal form.** 

> **Theorem 1.2**
Let $X$ be a normal globally Weil $\mathbb Q$-factorial compact Kähler
fourfold, with a canonical Weil divisor $K_X$, and let $\Delta\geq0$
be a rational divisor such that $(X,\Delta)$ is klt. Then every maximal
ordinary negative-ray program starting on $(X,\Delta)$ terminates.
Its birational steps form a finite sequence
$$(X,\Delta)=(X_0,\Delta_0)\dashrightarrow\cdots
 \dashrightarrow(X_n,\Delta_n).$$
Every $X_i$ is normal, compact Kähler and globally Weil
$\mathbb Q$-factorial; every $(X_i,\Delta_i)$ is klt, and
$D_i=K_{X_i}+\Delta_i$ is $\mathbb Q$-Cartier. The canonical divisors are
the transforms of the specified datum. The following alternatives hold.
\beginenumerate[label=\textup{(\roman*)}]
\item If $D=K_X+\Delta$ is pseudo-effective, then $D_n$ is nef.
The composite $\phi:X\dashrightarrow X_n$ extracts no prime divisor,
and
$$a(E;X,\Delta)\leq a(E;X_n,\Delta_n)$$
for every prime divisor over the two models, with strict inequality
for every prime on $X$ contracted by $\phi$.
\item If $D$ is not pseudo-effective, there is a projective surjective
morphism $g:X_n\to S$ with connected fibres, where $S$ is normal
compact Kähler, $\dim S<4$, $\rho(X_n/S)=1$, and $-D_n$ is
$g$-ample.
\endenumerate
For each negative contraction, including $g$, the relative
Bott–Chern dimension is one. If $X$ is globally strongly
$\mathbb Q$-factorial, so is every $X_i$.

The same conclusions hold in the intrinsic formulation with the
canonical rational line bundle in place of a chosen canonical Weil
divisor. In either formulation the first model is exactly $X$. [S10:84–119]

On a normal globally Weil $\mathbb Q$-factorial compact Kähler klt fourfold
pair with rational boundary, every *maximal* ordinary negative-ray
program terminates: the birational steps are finite, and the endpoint is
a nef model (adjoint pseudo-effective) or a projective Mori fibre space
(adjoint not pseudo-effective), with discrepancies nondecreasing and
strictly increasing on contracted primes.

**Ordinary programs, finite form.** 

> **Theorem 1.2**
Let $X$ be a normal globally Weil $\mathbb Q$-factorial compact Kähler
fourfold, with a canonical Weil divisor $K_X$, and let $\Delta\geq0$
be a rational divisor such that $(X,\Delta)$ is klt. Then there is a
finite sequence of ordinary negative steps
$$(X,\Delta)=(X_0,\Delta_0)\dashrightarrow\cdots
 \dashrightarrow(X_n,\Delta_n).$$
Every $X_i$ is normal, compact Kähler and globally Weil
$\mathbb Q$-factorial; every $(X_i,\Delta_i)$ is klt, and
$D_i=K_{X_i}+\Delta_i$ is $\mathbb Q$-Cartier. The canonical divisors are
the transforms of the specified datum. The following alternatives hold.
\beginenumerate[label=\textup{(\roman*)}]
\item If $D=K_X+\Delta$ is pseudo-effective, then $D_n$ is nef.
The composite $\phi:X\dashrightarrow X_n$ extracts no prime divisor,
and
$$a(E;X,\Delta)\leq a(E;X_n,\Delta_n)$$
for every prime divisor over the two models, with strict inequality
for every prime on $X$ contracted by $\phi$.
\item If $D$ is not pseudo-effective, there is a projective surjective
morphism $g:X_n\to S$ with connected fibres, where $S$ is normal
compact Kähler, $\dim S<4$, $\rho(X_n/S)=1$, and $-D_n$ is
$g$-ample.
\endenumerate
For each negative contraction, including $g$, the relative
Bott–Chern dimension is one. If $X$ is globally strongly
$\mathbb Q$-factorial, so is every $X_i$.

The same conclusions hold in the intrinsic formulation with the
canonical rational line bundle in place of a chosen canonical Weil
divisor. In either formulation the first model is exactly $X$. [S12:97–131]

The same statement phrased as *existence* of a finite sequence of
ordinary negative steps with the identical nef-model / Mori-fibre-space
dichotomy and discrepancy control; the two formulations (manuscripts 4
and 5) are the "maximal program terminates" and "a finite program
exists" faces of the same result.

## history of the conjecture

Prior (my training data, not this repo): the **Minimal Model
Conjecture** (Mori, 1980s) asserts that a smooth projective variety with
pseudo-effective canonical divisor has a terminal minimal model, reached
by a finite sequence of divisorial contractions and flips. Termination
is the hard direction: divisorial termination in dimension four is a
theorem of Birkar (via the boundedness of weak Fano type
triples), and flip termination for fourfolds follows from the
classification of Fano type fibre spaces and the absence of infinite
flip chains in the relevant extremal-ray structure. The
Birkar–Cascini–Hacon–McKernan theorem (BCHM) gave global termination
for varieties of general type, and the boundedness machinery reduced
the fourfold case. This family supplies the Kähler (compact complex
analytic) and generalized-pair versions of the same fourfold
termination, in the projective small-diagram setting with nef
b-data.

## Consequences

**Termination of generalized log canonical flip sequences** on
globally Weil $\mathbb Q$-factorial compact Kähler fourfolds with rational
boundary and a fixed analytically nef b-divisor [S4:25–44].

**Termination of generalized-canonical flip sequences** in the
parallel Kähler category with a fixed nef b-divisor [S6:99–130].

**Termination of permitted minimal model programs** for projective
log canonical fourfolds with rational boundary, characteristic zero
[S8:97–105].

**Termination of ordinary negative-ray programs** for klt compact
Kähler fourfold pairs, in both the maximal-program and the
finite-program formulation, with the nef-model / Mori-fibre-space
dichotomy and discrepancy control [S10:84–119, S12:97–131].

## section skeleton

Five manuscripts, each a single main file with a flat section list.

Manuscript 1 [S2] `build/main.tex`, nine inputs [S2:54, 59–66]
(00-abstract, 01-introduction with the theorem at [S4:25],
02-preliminaries, 03-comparisons, 04-terminal-junctions,
05-branch-topology, 06-curve-places, 07-difficulty, 08-completion).
The abstract text lives in `sections/00-abstract.tex` [S3:1], which
`main.tex` inputs.

Manuscript 2 [S5] `build/build/paper.tex`, seven inputs [S5:43–49]
(01-introduction with the abstract at [S6:1] and the theorem at
[S6:99], 02-foundations, 03-comparison, 04-low-places, 05-witnesses,
06-cycles, 07-termination).

Manuscript 3 [S7:63–65] `build/paper.tex`, ten inputs [S7:67–76]
(00-introduction with the theorem at [S8:97], 01-comparisons,
02-terminal-models, 02a-difficulty-setup, 03-branch-topology,
04-local-valuations, 05-difficulty, 06-lc-and-existence,
07-field-transfer, 08-consequences). The abstract is in `paper.tex`
itself at [S7:63–65].

Manuscript 4 [S9:71–73] `build/main.tex`, fourteen inputs [S9:76–88, 90]
(01-introduction with the theorem at [S10:84], 02-analytic, 03-steps,
04-terminal, 05-scaling, 06-perturbation, 07-endpoints, 08-resolutions,
08-relative, 09-threefold, 10-special, 11-threshold, 12-supply,
13-local-convention). The abstract is in `main.tex` itself at
[S9:71–73].

Manuscript 5 [S11:86–88] `build/main.tex`, nine inputs [S11:91–97, 99]
(01-introduction with the theorem at [S12:97], 02-analytic, 03-steps,
04-terminal, 05-scaling, 06-perturbation, 07-endpoints,
13-local-convention). The abstract is in `main.tex` itself at
[S11:86–88].

## Coverage

T0: five manuscripts, zero comparator challenges, zero `main_results`
entries, zero scope notes. The ledger reads `paps 5`, `paps_form 0`,
`mainres 0`, `chal 0`, `scope_note 0`, `verification 0`, `trace`
empty, `shapes bound|classification|uniform`, `resolves_named 0`.
Each manuscript ships a PDF at its directory top level (manuscript 1's
is `termination-generalized-lc-kahler-fourfolds.pdf`, manuscript 2's
is `termination-generalized-terminal-flips-compact-kahler-fourfolds.pdf`,
and manuscripts 3, 4, and 5 each ship `paper.pdf`) and a `build/`
LaTeX tree. The catalog entry [S13:188] names all five PDFs. No
`verification/` bundle, no reasoning trace, no scope note, and no
comparator challenge: the family is a pure unformalized
five-manuscript set, the simplest tier in the release.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 056 at line 1429) |
| S2 | [`preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/build/main.tex`](../../../preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/build/main.tex) | 68 | Manuscript 1: section inputs |
| S3 | [`preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/build/sections/00-abstract.tex`](../../../preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/build/sections/00-abstract.tex) | 1 | Manuscript 1: abstract (input into main.tex) |
| S4 | [`preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/build/sections/01-introduction.tex`](../../../preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/build/sections/01-introduction.tex) | 62 | Manuscript 1: main theorem (generalized lc flip termination) |
| S5 | [`preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026/build/build/paper.tex`](../../../preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026/build/build/paper.tex) | 51 | Manuscript 2: section inputs |
| S6 | [`preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026/build/build/sections/01-introduction.tex`](../../../preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026/build/build/sections/01-introduction.tex) | 273 | Manuscript 2: abstract, main theorem (generalized-canonical flip termination) |
| S7 | [`preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/build/paper.tex`](../../../preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/build/paper.tex) | 82 | Manuscript 3: abstract, section inputs |
| S8 | [`preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/build/sections/00-introduction.tex) | 197 | Manuscript 3: main theorem (projective lc program termination) |
| S9 | [`preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026/build/main.tex`](../../../preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026/build/main.tex) | 93 | Manuscript 4: abstract, section inputs |
| S10 | [`preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026/build/sections/01-introduction.tex) | 191 | Manuscript 4: main theorem (ordinary program termination, maximal) |
| S11 | [`preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/build/main.tex`](../../../preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/build/main.tex) | 106 | Manuscript 5: abstract, section inputs |
| S12 | [`preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/build/sections/01-introduction.tex) | 245 | Manuscript 5: main theorem (ordinary program termination, finite) |
| S13 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 056 at line 188) |
