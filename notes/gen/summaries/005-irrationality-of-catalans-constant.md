[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 005](../index/number-theory/005-irrationality-of-catalans-constant.md)

# 005 — Irrationality of Catalan's constant

[Index page](../index/number-theory/005-irrationality-of-catalans-constant.md)

## Original CONTENTS.md summary

The release blurb 

> **005. Irrationality of Catalan's constant.** Proves that Catalan's constant $`G=\sum_{j\ge0}(-1)^j/(2j+1)^2`$ is irrational. [S1:125]

The manuscript abstract 

> We prove that Catalan's constant
$G=\sum_{j\geq0}(-1)^j/(2j+1)^2$ is irrational. [S2:25–28]

## Undergraduate summary

Catalan's constant $G$ is the alternating sum of the reciprocals of
odd squares: $G = 1 - 1/9 + 1/25 - 1/49 + \cdots$. It appears in
number theory, combinatorics, and hyperbolic geometry. Whether $G$ is
rational or irrational had been an open problem for over two hundred
years.

This paper settles the question: $G$ is irrational. The proof
constructs a family of determinants $\Delta_N$ whose entries are
polynomial expressions in $G$. If $G$ were rational, all the
determinants would be rational. The proof then shows that, for large
prime $p$, the determinants are nonzero (a congruence argument
modulo $p$) and that their size is pinched between two explicit
bounds that are incompatible. The contradiction proves $G$ is
irrational.

The main statement 

> **Theorem 1.1**
Catalan's constant is irrational. [S3:16–18]

## Graduate summary

The proof is a single theorem with a multi-stage argument spread
across seven section files.

**Main theorem.** 

> **Theorem 1.1**
Catalan's constant is irrational. [S3:16–18]

**Determinant construction.** The determinant strategy


> \subsectionThe determinant strategy

We construct determinants $\Delta_N$ of size $n=48N$ whose entries
combine moments of two elementary kernels. Each moment is a rational
linear combination of $1$, $G$ and $\zeta(2)$. The polynomial rows are
chosen to have high Taylor contact: two prescribed expressions in the
rows have identical initial Taylor coefficients. This agreement cancels the $\zeta(2)$ term
in every entry. Consequently, the single hypothesis $G\in\mathbb Q$
makes all the determinants rational. [S3:106–114]

The determinants have size $n = 48N$; their entries are mixed
moments of two elementary kernels. The key is that each entry is a
rational linear combination of $1$, $G$, and $\zeta(2)$, and the
polynomial rows are chosen so the $\zeta(2)$ term cancels by Taylor
contact. Under the hypothesis $G \in \mathbb{Q}$, all entries are
rational, so $\Delta_N \in \mathbb{Q}$.

**Nonvanishing.** For large primes $p$, reduction modulo $p$ of the
polynomial rows shows $\Delta_p \neq 0$ (a Frobenius argument on
palindromic bases).

**Finite-place bound.** The product formula for nonzero rationals
gives a lower bound on $\log|\Delta_p|$ in terms of the prime
valuations.

**Real-place bound.** An integral representation of $\Delta_p$
gives an upper bound via two interpolation estimates (Hadamard-type).

**The contradiction.** The conclusion 

> Suppose that $G$ is rational. Proposition then
makes $\Delta_N$ rational for every $N$.
By Proposition , $\Delta_p\ne0$ for every
sufficiently large prime $p$. Apply the product-formula lower bound of
Proposition along this sequence:
$$\liminf_{\substack{p\to\infty\\p\ {\rm prime}}}
\left(\frac{\log|\Delta_p|}{(48p)^2}-\frac12\log 2\right)>-2.29084.$$
Proposition gives, along the same sequence, an
upper limit strictly smaller than $-2.2909$. Since
$-2.29084>-2.2909$, this is a contradiction. Therefore $G$ is irrational. [S4:3–16]

The lower bound from the product formula (liminf $> -2.29084$)
contradicts the upper bound from the integral ($< -2.2909$). The gap
is $0.00006$, which is the quantitative content of the two barrier
propositions in the certificate section.

The manuscript notes a geometric application: Agol's theorem
identifies $4G$ as the minimum volume of an orientable complete
finite-volume hyperbolic 3-manifold [S4:18–20].

## history of the conjecture

Prior (my training data, not this repo): the irrationality of $G$
was open since Euler's time. Rivoal and Zudilin (2001) proved that
infinitely many even values of the beta function $\beta(2k)$ are
irrational, and that at least one of $\beta(2), \ldots, \beta(14)$
is irrational; Zudilin (2019) narrowed this to the first six values.
Catalan's constant $\beta(2)$ was the simplest remaining case. The
determinant strategy here is in the same family as Apéry's proof of
the irrationality of $\zeta(3)$ (1978): construct a sequence of
rationals that, under the rationality hypothesis, is both a
$0$-sequence mod $p$ (nonvanishing) and too large (product formula)
while being too small (integral bound).

## Consequences

**Catalan's constant is irrational.** This settles a two-hundred-year
open problem and removes $\beta(2)$ from the finite set of open even
beta values identified by Rivoal–Zudilin and Zudilin.

**A quantitative barrier for hyperbolic geometry.** The certificate
section pins the two barriers to explicit constants ($-2.29084$ vs
$-2.2909$), which are the limits of the finite-place and real-place
estimates along the prime sequence. The gap is the proof's margin.

## section skeleton

Single main file [S2:25–28] with eight `\input` sections [S3], no
`build/sections/` subdirectory in the usual sense (the sections are
flat files under `build/sections/`), one `.bib` file [S8].

**Sections:** Introduction (introduction.tex) with the main theorem
(line 16) and the determinant strategy (line 106); Foundations
(foundations.tex) with polynomial rows and mixed moments; Odd primes
and the finite-place lower bound (odd-primes.tex); Nonvanishing
along the prime sequence (nonvanishing.tex); Real place
(real-place.tex) with interpolation and Hadamard estimates; Energy
bound (energy.tex); Certificate (certificate.tex) with exact trial
sequences and root brackets; Conclusion (conclusion.tex) with the
proof of Theorem `thm:main`.

## Coverage

T2: one manuscript, one comparator challenge, zero `main_results`
entries, one scope note. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 1`, `scope_note 1`, `verification 0`, `trace`
empty. The family ships a nine-file LaTeX manuscript (main file plus
eight sections plus one `.bib`), a compiled `paper.pdf` [S7], and a
`README.md`. No `verification/` bundle, no reasoning trace. The catalog entry [S9:86]
lists the single PDF. The comparator stub states the target:

```lean
theorem catalan_irrational :
    Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2) := by
  sorry
```
[S6:7–9]

The scope note confirms the formalization's reach: "The formalization proves that Catalan's constant $G=\sum_{j=0}^{\infty}(-1)^j/(2j+1)^2$ is irrational. This is the mathematical assertion in the paper's title. [S5:9]"
Note the ledger reads `paps_form 0` (no `main_results` entry), so
the scope note describes an intended target, not a landed
formalization.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 005 at line 125) |
| S2 | [`preprints/Catalans-constant-is-irrational-September-24-2026/build/main.tex`](../../../preprints/Catalans-constant-is-irrational-September-24-2026/build/main.tex) | 44 | Main file: preamble, abstract, section inputs |
| S3 | [`preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/introduction.tex`](../../../preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/introduction.tex) | 208 | Introduction, main theorem, determinant strategy |
| S4 | [`preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/conclusion.tex`](../../../preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/conclusion.tex) | 51 | Proof of Theorem thm:main, hyperbolic volume remark |
| S5 | [`lean/docs/005.md`](../../../lean/docs/005.md) | 15 | Scope note |
| S6 | [`lean/ComparatorChallenges/Catalan.lean`](../../../lean/ComparatorChallenges/Catalan.lean) | 13 | Challenge stub (sorry) |
| S7 | [`preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf`](../../../preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf) | 16409 | Compiled manuscript |
| S8 | [`preprints/Catalans-constant-is-irrational-September-24-2026/build/references.bib`](../../../preprints/Catalans-constant-is-irrational-September-24-2026/build/references.bib) | 319 | Bibliography |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 005 at line 86) |

## Bibliography

- Agol, Ian, The minimal volume orientable hyperbolic 2-cusped 3-manifolds (2010)
- Beukers, Frits, A note on the irrationality of $\zeta(2)$ and $\zeta(3)$ (1979)
- Calegari, Frank, Dimitrov, Vesselin, Tang, Yunqing, The linear independence of {$1$, $\zeta(2)$, and $L(2,\chi_{-3})$} (2024)
- Calegari, Frank, Irrationality of certain $p$-adic periods for small $p$ (2005)
- Calegari, Frank, Dimitrov, Vesselin, Tang, Yunqing, Arithmetic holonomy bounds and effective Diophantine approximation (2025)
- Descartes, René, La Géométrie (1637)
- Eskandari, Payman, Improved rational approximations to Catalan's constant (2026)
- Fischler, Stéphane, Irrationality of values of $L$-functions of Dirichlet characters (2020)
- Forrester, Peter J., Meet Andréief, Bordeaux 1886, and Andreev, Kharkov 1882–83 (2018)
- Garoufalidis, Stavros, Popescu, Ionel, Analyticity of the Planar Limit of a Matrix Model (2013)
- Krattenthaler, Christian, Zudilin, Wadim, Hypergeometry inspired by irrationality questions (2019)
- Krattenthaler, Christian, Rivoal, Tanguy, On a linear form for Catalan's constant (2008)
- Krattenthaler, Christian, Advanced determinant calculus (1999)
- Lai, Li, Zhou, Li, At least two of $\zeta(5),\zeta(7), ,\zeta(35)$ are irrational (2022)
- Nesterenko, Yu. V., On Catalan's constant (2016)
- Rivoal, Tanguy, Zudilin, Wadim, Diophantine properties of numbers related to Catalan's constant (2003)
- Rivoal, Tanguy, Nombres d'Euler, approximants de Padé et constante de Catalan (2006)
- Apéry, Roger, Irrationalité de $\zeta 2$ et $\zeta 3$ (1979)
- Saff, Edward B., Logarithmic Potential Theory with Applications to Approximation Theory (2010)
- Sarason, Donald, Generalized interpolation in $H^\infty$ (1967)
- National Institute of Standards, Technology, Digital Library of Mathematical Functions, Section 18.5 (n.d.)
- Sun, Zhi-Wei, Catalan's constant is irrational (2026)
- Viola, Carlo, Rational approximations to Catalan's constant (2022)
- Voight, John, Quaternion Algebras (2021)
- Zagier, Don, Newman's short proof of the prime number theorem (1997)
- Zudilin, Wadim, An Apéry-like difference equation for Catalan's constant (2003)
- Zudilin, Wadim, Arithmetic of Catalan's constant and its relatives (2019)
- Zudilin, Wadim, A determinantal approach to irrationality (2017)
