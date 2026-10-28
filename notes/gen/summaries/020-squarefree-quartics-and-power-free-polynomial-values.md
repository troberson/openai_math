[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 020](../index/number-theory/020-squarefree-quartics-and-power-free-polynomial-values.md)

# 020 — Squarefree quartics and power-free polynomial values

[Index page](../index/number-theory/020-squarefree-quartics-and-power-free-polynomial-values.md)

## Original CONTENTS.md summary

The release blurb 

> **020. Squarefree quartics and power-free polynomial values.** Proves the squarefree-values conjecture for irreducible integer quartics with no fixed prime-square divisor: squarefree values on positive integers have the predicted positive Euler-product density. More generally, establishes the $`(d-2)`$-power-free density for irreducible integer polynomials of degrees four through eight under the necessary local condition; together with Browning's higher-degree theorem, this covers every d ≥ 4. [S1:554]

The manuscript abstract 

> We prove that every irreducible integer quartic with no fixed prime-square
divisor takes squarefree values with the predicted positive Euler-product
density. More generally, we obtain the corresponding $(d-2)$-power-free
density in degrees $4\le d\le8$. The proof combines number-field factorization,
determinant estimates with adaptive auxiliary primes, and explicit
low-degree geometry. Together with Browning's theorem for higher degrees,
this gives the $(d-2)$-power-free density for every $d\ge4$. [S2:37–45]

## Undergraduate summary

Take an irreducible integer polynomial $f$ and look at the values
$f(n)$ as $n$ runs through the positive integers. A value is
"squarefree" if no square of a prime divides it. The squarefree-values
conjecture predicts that, for a "generic" polynomial $f$ — one with no
fixed prime-square dividing every value — the squarefree values occur
with a positive, explicitly computable density, namely a convergent
Euler product over primes.

This paper proves that prediction for quartics (degree 4) and, more
generally, gives the $(d-2)$-power-free density for irreducible
integer polynomials of every degree $4 \le d \le 8$. The $(d-2)$-power
condition generalizes squarefree (which is the $d=4$, $k=2$ case).
Together with Browning's theorem for higher degrees, the result
covers every $d \ge 4$.

The main statement 

> **Theorem 1.1**
Let $f\in\mathbb Z[x]$ be irreducible over $\mathbb Q$, of degree $d$ with
$4\le d\le8$, and put $k=d-2$. If holds,
then
$$S_{f,k}(X)=c_{f,k}X+o_f(X),\qquad
 c_{f,k}=\prod_p\left(1-\frac{\rho_f(p^k)}{p^k}\right)>0.$$
No primitivity or sign condition on the leading coefficient is required. [S3:20–29]

## Graduate summary

The theorem is a positive-density statement for power-free values of
irreducible integer polynomials.

**Power-free density.** 

> **Theorem 1.1**
Let $f\in\mathbb Z[x]$ be irreducible over $\mathbb Q$, of degree $d$ with
$4\le d\le8$, and put $k=d-2$. If holds,
then
$$S_{f,k}(X)=c_{f,k}X+o_f(X),\qquad
 c_{f,k}=\prod_p\left(1-\frac{\rho_f(p^k)}{p^k}\right)>0.$$
No primitivity or sign condition on the leading coefficient is required. [S3:20–29]

For an irreducible integer polynomial $f$ of degree $d \in [4,8]$, set
$k = d - 2$. Under the local-admissibility condition (roughly: no
prime $k$th power divides every value of $f$), the counting function
$S_{f,k}(X)$ of $n \le X$ with $f(n)$ $k$-free satisfies
$S_{f,k}(X) = c_{f,k} X + o_f(X)$ with
$c_{f,k} = \prod_p (1 - \rho_f(p^k)/p^k) > 0$. The content is that the
Euler product converges to a strictly positive constant and the
error is $o_f(X)$. No monicity, primitivity, or coefficient-height
assumption is imposed.

**Proof ingredients.** The abstract [S2:37–45] names the three
machines: number-field factorization (to control which primes can
divide $f(n)$), determinant estimates with adaptive auxiliary primes
(to cut down the lattice of solutions), and explicit low-degree
geometry (the quartic and curve cases handled by hand). The degree
range $4 \le d \le 8$ is the range the elementary-geometry input
covers; Browning's theorem handles $d \ge 9$.

## history of the conjecture

Prior (my training data, not this repo): the squarefree-values
conjecture, in the style of Schinzel and the polynomial squarefree
heuristic, predicts a positive Euler-product density of squarefree
values for irreducible integer polynomials under a standard local
obstruction condition. The classical results cover low-degree cases
and, via sieve methods, a range of degrees; the power-free
generalization $(d-2)$-free is the form suggested by the arithmetic of
the polynomial's factorization over its splitting field. Browning has
a higher-degree theorem, which this paper extends down to degree 4,
closing the full range $d \ge 4$ between the two.

## Consequences

**The squarefree-values conjecture for irreducible integer quartics
with no fixed prime-square divisor.** The squarefree values carry the
predicted positive Euler-product density [S3:20–29].

**The $(d-2)$-power-free density for degrees $4 \le d \le 8$.** The
generalized power-free statement covers the full elementary-geometry
range; combined with Browning's higher-degree theorem it gives the
density for every $d \ge 4$.

## section skeleton

Single main file [S2:37–45] with thirteen section inputs under `sections/`
[S2:47–60], one `.bib` file [S7].

**Sections** [S2:47–60]: Introduction (01-introduction.tex) with the
main theorem (line 20); sieve (02-sieve.tex); affine counting
(03-affine-counting.tex); arithmetic boxes (04-arithmetic-boxes.tex);
determinant cuts (05-determinant-cuts.tex); lattice boxes
(06-lattice-boxes.tex); Hilbert bounds (07-hilbert-bounds.tex);
quartic geometry (08-quartic-geometry.tex); curves (09-curves.tex);
parameters (10-parameters.tex); tail proof (11-tail-proof.tex);
certificate (12-certificate.tex); cyclotomic (13-cyclotomic.tex).

## Comparison with the formalized statement

The scope note states what the formalization proves: "The formalized result proves positive-density power-free values for every integer polynomial $f$ irreducible over $\mathbb Q$ of degree $d\ge4$. Put $k=d-2$ and assume no prime $k$th power divides every value of $f$. Then the number of positive integers $n\le X$ for which $f(n)$ is $k$-free is $c_fX+o_f(X)$, where $c_f>0$ is the convergent product of local factors. Negative values are allowed and zero is excluded. No monicity, primitivity, or coefficient-height restriction is imposed. [S4:9]" —
the positive-density power-free statement for every irreducible
integer polynomial of degree at least 4 under the local-admissibility
condition, with no monicity, primitivity, or coefficient-height
restriction.

The comparator stub [S5:37–42] states the same target and ends in
`sorry`:

```lean
theorem allDegrees (f : Polynomial ℤ)
 (hirr : Irreducible (f.map (Int.castRingHom ℚ)))
 (hdeglo : 4 ≤ f.natDegree)
 (hlocal : LocallyAdmissible f (f.natDegree - 2)) :
 DensityStatement f (f.natDegree - 2) := by
 sorry
```
[S5:37–42]

The proved version lives in `OAI/NumberTheory/PowerFree/Main.lean`
[S6], where `theorem allDegrees` (line 144) is discharged — the file
carries **zero** `sorry` occurrences — so the `main_results` entry
`OAI.QuarticPowerFree.allDegrees` is landed (ledger `paps_form 1`,
`mainres 1`), in contrast to a stub-only family.

## Coverage

T3: one manuscript, one comparator challenge, one `main_results`
entry, one scope note. The ledger reads `paps 1`, `paps_form 1`,
`mainres 1`, `chal 1`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes resolution|density`, `resolves_named 1`. The family
ships a fifteen-file LaTeX manuscript (main file plus thirteen
sections plus `references.bib` [S7]) and a compiled
`manuscript.pdf` [S8]. The catalog entry [S9:116] names the single
PDF. No `verification/` bundle, no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 020 at line 554) |
| S2 | [`preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/main.tex`](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/main.tex) | 63 | Main file: abstract, section inputs |
| S3 | [`preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/sections/01-introduction.tex) | 302 | Main theorem (power-free density) |
| S4 | [`lean/docs/020.md`](../../../lean/docs/020.md) | 15 | Scope note |
| S5 | [`lean/ComparatorChallenges/PowerFreeValues.lean`](../../../lean/ComparatorChallenges/PowerFreeValues.lean) | 46 | Challenge stub (allDegrees + sorry) |
| S6 | [`lean/OAI/NumberTheory/PowerFree/Main.lean`](../../../lean/OAI/NumberTheory/PowerFree/Main.lean) | 153 | Proved version in the Lean tree (allDegrees, 0 sorry) |
| S7 | [`preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/references.bib`](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/references.bib) | 345 | Bibliography |
| S8 | [`preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf`](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf) | 19116 | Compiled manuscript |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 020 at line 116) |

## Bibliography

- The Stacks project authors, The Stacks project (2026)
- Bombieri, Enrico, Pila, Jonathan, The number of integral points on arcs and ovals (1989)
- Browning, T. D., Power-free values of polynomials (2011)
- Browning, Tim D., Shparlinski, Igor E., Square-free values of random polynomials (2024)
- Carella, N. A., Squarefree Values Of Polynomials (2023)
- Zapata Ceballos, Sergio Ricardo, Jalalvand, Fatemeh, On the Squarefree Values of Degree-$2q$ Polynomials (2026)
- Eisenbud, David, Green, Mark, Hulek, Klaus, Popescu, Sorin, Small schemes and varieties of minimal degree (2006)
- Erdős, Paul, Arithmetical properties of polynomials (1953)
- Erdős, Paul, Some recent advances and current problems in number theory (1965)
- Granville, Andrew, ABC allows us to count squarefrees (1998)
- Greaves, George, Power-free values of binary forms (1992)
- Heath-Brown, D. R., Square-free values of $n^2+1$ (2012)
- Heath-Brown, D. R., Power-free values of polynomials (2013)
- Heath-Brown, D. R., The density of rational points on curves and surfaces (2002)
- Heath-Brown, D. R., Sums and differences of three $k$th powers (2009)
- Heath-Brown, D. R., Counting rational points on algebraic varieties (2006)
- Helfgott, H. A., On the square-free sieve (2004)
- Hooley, Christopher, On the power free values of polynomials (1967)
- Huxley, M. N., Nair, M., Power free values of polynomials III (1980)
- Milne, James S., Algebraic Number Theory (2020)
- Nair, M., Power free values of polynomials (1976)
- Nair, M., Power free values of polynomials II (1979)
- Reuss, Thomas, Power-free values of polynomials (2015)
- Ricci, Giovanni, Ricerche aritmetiche sui polinomi (1933)
- Salberger, Per, On the density of rational and integral points on algebraic varieties (2007)
- Salberger, Per, Counting rational points on projective varieties (2023)
- Sofos, Efthymios, Counting square-free values of random polynomials (2026)
- Xiao, Stanley Yao, Power-free values of binary forms and the global determinant method (2017)
