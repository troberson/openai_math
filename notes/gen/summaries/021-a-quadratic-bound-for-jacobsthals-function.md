[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 021](../index/number-theory/021-a-quadratic-bound-for-jacobsthals-function.md)

# 021 — A quadratic bound for Jacobsthal's function

[Index page](../index/number-theory/021-a-quadratic-bound-for-jacobsthals-function.md)

## Original CONTENTS.md summary

The release blurb 

> **021. A quadratic bound for Jacobsthal’s function.** Answers Jacobsthal's quadratic-bound question: every interval of $`Ck^2`$ consecutive integers contains an integer coprime to any prescribed positive integer with at most k distinct prime divisors, for an absolute constant C. The bound is uniform over prime sets and interval positions and removes the classical logarithmic loss. [S1:570]

The manuscript abstract 

> Let $h(k)$ be the least integer such that every interval of $h(k)$
consecutive integers contains an integer coprime to any prescribed
positive integer having at most $k$ distinct prime divisors. We prove
$h(k)\ll k^2/(\log\log(3k))^2$, giving an affirmative answer to
Jacobsthal's quadratic-bound question. [S2:40–46]

## Undergraduate summary

Jacobsthal's function $h(k)$ asks the worst-case gap: what is the
shortest interval of consecutive integers you must look in to be
guaranteed to find a number coprime to a given modulus with at most
$k$ distinct prime divisors? For example, if the modulus is squarefree
with $k$ odd prime factors, then in any stretch of integers there is
always some integer none of those primes divides — the question is how
long the stretch must be.

Jacobsthal conjectured the answer should grow at most quadratically in
$k$. This paper proves a slightly stronger statement: $h(k)$ is at
most a constant times $k^2 / (\log\log(3k))^2$, which is a quadratic
bound with an iterated-logarithmic saving. The constant is absolute and
the bound is uniform — it does not depend on which particular primes
are used, and the interval may start at any (signed) integer. This
removes a classical logarithmic factor that earlier proofs carried.

The main statement 

> **Theorem 1.1**
There is an absolute constant $C>0$ such that
$$h(k)\le C\frac{k^2}{(\log\log(3k))^2}
 \qquad\text{for every integer }k\ge1.$$ [S3:24–30]

## Graduate summary

The theorem is a uniform upper bound on Jacobsthal's function with an
iterated-logarithmic saving over the classical quadratic order.

**Main theorem.** 

> **Theorem 1.1**
There is an absolute constant $C>0$ such that
$$h(k)\le C\frac{k^2}{(\log\log(3k))^2}
 \qquad\text{for every integer }k\ge1.$$ [S3:24–30]

There is an absolute $C > 0$ with
$h(k) \le C k^2 / (\log\log(3k))^2$ for every $k \ge 1$. The content is
threefold: the order is $k^2$ (quadratic, confirming the conjectured
order), the iterated-log factor $(\log\log(3k))^{-2}$ is a genuine
saving over bare $k^2$, and the constant is absolute and the bound
uniform over the underlying prime set. The scope note [S4:9] records
that the interval start is unrestricted — "intervals may begin at any
signed integer" — and that the optimal order of growth is not
determined (the bound is an upper bound, not a matching lower one).

**The quadratic baseline.** The scope note [S4:9] notes the *earlier*
quadratic bound (bare $Ck^2$, no iterated-log saving) is retained as a
separate statement alongside the strengthened one — the two comparator
targets formalize the two orders.

## history of the conjecture

Prior (my training data, not this repo): Jacobsthal (1938) defined the
function and proved a bound of the form $h(k) \ll k^2 \log^2 k$,
carrying a logarithmic loss over the quadratic order he conjectured to
be sharp. Iwaniec and Sutherland, and later Pintz, refined the argument
and removed part of the loss. The iterated-logarithmic saving
$(\log\log k)^{-2}$ is the content here: it is a genuine improvement
over the classical logarithmic factor, and the uniformity in the prime
set (no dependence on which $k$ primes are involved) is what makes the
bound usable in the applications to consecutive-smooth-number and
covering-system arguments that Jacobsthal's function feeds. The
matching lower bound remains out of reach, which is why the scope note
flags the optimal order as undetermined.

## Consequences

**An affirmative answer to Jacobsthal's quadratic-bound question,
with a saving.** $h(k) \ll k^2 / (\log\log(3k))^2$ for an absolute
$C$, uniformly over prime sets and interval positions, removing the
classical logarithmic loss [S3:24–30].

**A uniform, start-position-free bound.** The interval may begin at
any signed integer, so the estimate is usable for arbitrary windows,
not just those anchored at $0$ [S4:9].

## section skeleton

Single main file [S2:40–46] with twelve section inputs under `sections/`
[S2:48–61], one `.bib` file [S8].

**Sections** [S2:48–61]: Introduction (introduction.tex) with the main
theorem (line 24); inputs (inputs.tex); tree (tree.tex); functions
(functions.tex); prime paths (prime-paths.tex); reference
(reference.tex); boxes (boxes.tex); inverse (inverse.tex); variance
(variance.tex); stops (stops.tex); assembly (assembly.tex); hyperbola
(hyperbola.tex); elementary inputs (elementary-inputs.tex).

## Comparison with the formalized statement

The scope note states the formalization's reach: "Let $h(k)$ be the least interval length that guarantees an integer coprime to any prescribed positive modulus with at most $k$ distinct prime factors. The formalization proves the paper's strengthened Jacobsthal bound $h(k)\le Ck^2/(\log\log(3k))^2$ for one absolute $C>0$ and every $k\ge1$. Intervals may begin at any signed integer. The earlier quadratic bound is also retained as a separate statement; the optimal order of growth is not determined. [S4:9]" — the
strengthened iterated-log Jacobsthal bound $h(k) \le Ck^2 /
(\log\log(3k))^2$ for an absolute $C$, plus the retained quadratic
bound, with unrestricted interval start.

The two comparator stubs state the two targets. `Jacobsthal.lean`
 is the quadratic bound:

```lean
theorem erdos_970_quadratic : NumberTheoryLean.Targets.JacobsthalQuadratic := by
  sorry
```
[S5:24–25]

`JacobsthalImproved.lean` is the iterated-log bound:

```lean
theorem erdos_970_iterated_log : NumberTheoryLean.Targets.JacobsthalIteratedLog := by
  sorry
```
[S6:22–23]

Both end in `sorry`. The quadratic bound is the one *landed* in the
Lean tree: `OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean`
[S7] carries **zero** `sorry` occurrences, so the `main_results` entry
`OAI.Erdos970.Erdos970Final.erdos_970_quadratic` is proved (ledger
`mainres 1`). The iterated-log bound is **not** in `main_results` —
its target remains stub-only, so the ledger reads `paps_form 1` for
the quadratic statement while the strengthened bound the manuscript
headline is only a comparator challenge.

## Coverage

T3: one manuscript, two comparator challenges, one `main_results`
entry, one scope note. The ledger reads `paps 1`, `paps_form 1`,
`mainres 1`, `chal 2`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes resolution|bound|partial|uniform`, `resolves_named 1`.
The family ships a fourteen-file LaTeX manuscript (main file plus
twelve sections plus `references.bib` [S8]) and a compiled
`paper.pdf` [S9]. The catalog entry [S10:118] names the single PDF.
No `verification/` bundle, no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 021 at line 570) |
| S2 | [`preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/main.tex`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/main.tex) | 68 | Main file: abstract, section inputs |
| S3 | [`preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/sections/introduction.tex`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/sections/introduction.tex) | 269 | Main theorem (iterated-log Jacobsthal bound) |
| S4 | [`lean/docs/021.md`](../../../lean/docs/021.md) | 16 | Scope note |
| S5 | [`lean/ComparatorChallenges/Jacobsthal.lean`](../../../lean/ComparatorChallenges/Jacobsthal.lean) | 31 | Challenge stub (quadratic bound + sorry) |
| S6 | [`lean/ComparatorChallenges/JacobsthalImproved.lean`](../../../lean/ComparatorChallenges/JacobsthalImproved.lean) | 29 | Challenge stub (iterated-log bound + sorry) |
| S7 | [`lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean`](../../../lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean) | 23 | Proved quadratic bound in the Lean tree (0 sorry) |
| S8 | [`preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/references.bib`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/references.bib) | 378 | Bibliography |
| S9 | [`preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) | 23449 | Compiled manuscript |
| S10 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 021 at line 118) |

## Bibliography

- Banks, William, Ford, Kevin, Tao, Terence, Large prime gaps and probabilistic models (2023)
- Costello, Fintan, Watts, Paul, An upper bound on Jacobsthal's function (2015)
- Estermann, T., On Kloosterman's sum (1961)
- Fiori, Andrew, Kadiri, Habiba, Swidinsky, Joshua, Sharper bounds for the error term in the prime number theorem (2023)
- Ford, Kevin, Green, Ben, Konyagin, Sergei and Maynard, James, Tao, Terence, Long gaps between primes (2018)
- Friedlander, John, Iwaniec, Henryk, Opera de Cribro (2010)
- Gallagher, P. X., On the distribution of primes in short intervals (1976)
- Gallagher, P. X., A larger sieve (1971)
- Granville, Andrew, Soundararajan, K., The distribution of prime numbers
- Granville, Andrew, Soundararajan, K., Multiplicative number theory: The pretentious approach (2014)
- Hajdu, L., Saradha, N., Disproof of a conjecture of Jacobsthal (2012)
- Heath-Brown, D. R., Prime numbers in short intervals and a generalized Vaughan identity (1982)
- Helfgott, H. A., Venkatesh, A., How small must ill-distributed sets be? (2009)
- Huxley, M. N., On the difference between consecutive primes (1972)
- Iwaniec, Henryk, On the problem of Jacobsthal (1978)
- Iwaniec, Henryk, Kowalski, Emmanuel, Analytic Number Theory (2004)
- Iwaniec, Henryk, On the error term in the linear sieve (1971)
- Jacobsthal, Ernst, Über Sequenzen ganzer Zahlen, von denen keine zu $n$ teilerfremd ist. I–III (1960)
- Jarník, Vojtěch, Über die Gitterpunkte auf konvexen Kurven (1926)
- Lichtman, Jared Duker, Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors (2022)
- Montgomery, H. L., Vaughan, R. C., The large sieve (1973)
- Montgomery, Hugh L., Vaughan, Robert C., Multiplicative Number Theory III
- Montgomery, Hugh L., Vaughan, Robert C., Multiplicative Number Theory II: Primes and Sieves
- Erdős, P., On the integers relatively prime to $n$ and on a number-theoretic function considered by Jacobsthal (1962)
- Serfozo, Richard, Basics of Applied Stochastic Processes (2009)
- Sofos, Efthymios, Gaps between prime divisors and analogues in Diophantine geometry (2023)
- Tao, Terence, 254A, Notes 4: Some sieve theory (2015)
- Vaughan, Robert C., Math 571, Chapter 5: The large sieve (2025)
- Vaughan, R. C., On the order of magnitude of Jacobsthal's function (1977)
- Walsh, Miguel N., The inverse sieve problem in high dimensions (2012)
- Walsh, Miguel N., The algebraicity of ill-distributed sets (2014)
- Ziller, Mario, New computational results on a conjecture of Jacobsthal (2019)
