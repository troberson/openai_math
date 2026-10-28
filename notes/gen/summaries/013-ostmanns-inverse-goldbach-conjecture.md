[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 013](../index/number-theory/013-ostmanns-inverse-goldbach-conjecture.md)

# 013 — Ostmann's inverse Goldbach conjecture

[Index page](../index/number-theory/013-ostmanns-inverse-goldbach-conjecture.md)

## Original CONTENTS.md summary

The release blurb 

> **013. Ostmann’s inverse Goldbach conjecture.** Proves that no finite modification of the primes can be written as $`A+B`$ with $`A,B\subseteq\mathbb Z_{\ge0}`$ each containing at least two elements. This resolves Ostmann's inverse Goldbach conjecture on additive indecomposability. [S1:316]

The manuscript abstract 

> We prove Ostmann's inverse Goldbach conjecture: no set differing from the primes
by finitely many elements can be written as $A+B$, where $A$ and $B$ are sets
of nonnegative integers with at least two elements each. [S2:54–58]

## Undergraduate summary

A "sumset" $A+B$ is the set of all sums $a+b$ with $a$ from $A$ and
$b$ from $B$. The ordinary Goldbach problem asks which integers are
sums of primes. Ostmann's conjecture turns the question around: it
asks which sets *cannot* be written as a sumset of two nontrivial sets.

A set is "additively indecomposable" if it cannot be written as $A+B$
with both $A$ and $B$ containing at least two elements. The primes —
and any set that differs from the primes by only finitely many
elements — are additively indecomposable in this sense. That is the
content of this paper: no finite modification of the prime number set
is a sumset of two sets with at least two elements each.

Equivalently, for any two such sets $A,B$, the sumset $A+B$ differs
from the primes at infinitely many places — they can agree on the
primes in only a finite way.

The main statement 

> **theorem**
If $A,B\subseteq\mathbb N_0$ satisfy $|A|,|B|\ge2$, then
$(A+B)\mathbin{\triangle}\mathcal P$ is infinite.
Equivalently, every finite modification of $\mathcal P$ is additively
indecomposable into two sets with at least two elements each. [S3:15–20]

## Graduate summary

The theorem is an additive-combinatorics indecomposability result for
the prime set up to finite changes.

**Ostmann's inverse Goldbach theorem.** 

> **theorem**
If $A,B\subseteq\mathbb N_0$ satisfy $|A|,|B|\ge2$, then
$(A+B)\mathbin{\triangle}\mathcal P$ is infinite.
Equivalently, every finite modification of $\mathcal P$ is additively
indecomposable into two sets with at least two elements each. [S3:15–20]

Read in the $|A|,|B| \ge 2$ form, the statement says the symmetric
difference $(A+B) \triangle \mathcal{P}$ is infinite: the sumset and
the primes disagree at infinitely many integers. The equivalent
phrasing pins the direction — it is not that the sumset misses the
primes, but that no finite perturbation of the primes is expressible
as a two-summand sumset at all.

**Two-infinite-summands case.** The scope note [S4:9] records a
companion form: the impossibility also holds when both summands are
infinite, the `twoInfiniteSummandsImpossible` target [S5:33–34]. The
full result and this case are the two statements the scope note says
the linked formalizations carry.

## history of the conjecture

Prior (my training data, not this repo): Ostmann (1940) proved that
the positive integers are additively indecomposable in the strong
sense that $\mathbb{Z}_{\ge 0}$ is not a sumset of two sets with
both having at least two elements (equivalently, the only finite
summand decomposition of the integers is trivial). The "inverse
Goldbach" formulation asks the same question for the primes — which
sit strictly inside the integers — and for any set obtained from the
primes by changing finitely many members. The difficulty is that the
prime set has enough additive structure (Goldbach-type sums reach
almost every even integer) that an indecomposability proof cannot use
the same density argument as for the full integers, and must instead
control how a proposed summand decomposition forces the sumset to
carry composites and small integers in a way the primes do not.

## Consequences

**Additive indecomposability of the primes up to finite changes.**
No set that differs from $\mathcal{P}$ by finitely many elements is a
sumset $A+B$ with $|A|,|B| \ge 2$, which is the additive-combinatorial
counterpart to the primes being, in a precise sense, "far from a
sumset."

**The two-infinite-summands case.** The infinite-summand version
[S5:33–34] extends the indecomposability to the regime where both
summands are infinite, the form the scope note records as the
second linked statement.

## section skeleton

Single main file [S2:54–58] with a glyph-mappings input [S2:5] and nine
numbered section inputs under `sections/` [S2:63–71], one `.bib`
file [S7].

**Sections** [S2:63–71]: Introduction (01-introduction.tex) with
Ostmann's conjecture (line 15); Preliminaries (02-preliminaries.tex);
Quadratic (03-quadratic.tex); Characters (04-characters.tex); Supply
(05-supply.tex); Tree (06-tree.tex); Construction (07-construction.tex);
Arithmetic (08-arithmetic.tex); Conclusion (09-conclusion.tex).

## Coverage

T2: one manuscript, two comparator challenges, zero `main_results`
entries, one scope note. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 2`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes resolution`, `resolves_named 1`. The family ships a
thirteen-file LaTeX manuscript (main file plus glyph-mappings plus
nine sections plus `references.bib` [S7]) and a compiled
`paper.pdf` [S8]. The catalog entry [S9:102] names the single PDF.
No `verification/` bundle, no reasoning trace.

The comparator stubs state the two linked targets. `OstmannPrimes.lean`
 states the prime-indecomposability target:

```lean
theorem main : ∀ A B : Set ℕ, A.Nontrivial → B.Nontrivial →
    Set.Infinite ((A + B) ∆ {n : ℕ | Nat.Prime n}) := by
  sorry
```
[S6:9–11]

`OstmannComplete.lean` [S5:30–34] states the full result and the
two-infinite-summands case, both ending in `sorry`:

```lean
theorem inverseGoldbach : InverseGoldbach := by
  sorry

theorem twoInfiniteSummandsImpossible : TwoInfiniteSummandsImpossible := by
  sorry
```
[S5:30–34]

The scope note confirms the formalization's reach: "The formalization proves Ostmann's inverse Goldbach conjecture. For any two sets $A,B$ of nonnegative integers, each containing at least two elements, the symmetric difference between their sumset $A+B$ and the set of primes is infinite. Thus no set differing from the primes by only finitely many elements can be decomposed as such a sumset. The linked statements include the full result and its two-infinite-summands case. [S4:9]" Note
the ledger reads `paps_form 0` (no `main_results` entry), so the scope
note describes an intended target, not a landed formalization.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 013 at line 316) |
| S2 | [`preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/paper.tex`](../../../preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/paper.tex) | 80 | Main file: abstract, section inputs |
| S3 | [`preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/sections/01-introduction.tex) | 141 | Ostmann's conjecture statement |
| S4 | [`lean/docs/013.md`](../../../lean/docs/013.md) | 16 | Scope note |
| S5 | [`lean/ComparatorChallenges/OstmannComplete.lean`](../../../lean/ComparatorChallenges/OstmannComplete.lean) | 38 | Challenge stubs (InverseGoldbach + two-infinite-summands, sorry) |
| S6 | [`lean/ComparatorChallenges/OstmannPrimes.lean`](../../../lean/ComparatorChallenges/OstmannPrimes.lean) | 15 | Challenge stub (prime indecomposability, sorry) |
| S7 | [`preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/references.bib`](../../../preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/references.bib) | 398 | Bibliography |
| S8 | [`preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf`](../../../preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf) | 21824 | Compiled manuscript |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 013 at line 102) |

## Bibliography

- Babai, László, Nikolov, Nikolay, Pyber, László, Product growth and mixing in finite groups (2008)
- Bonami, Aline, Étude des coefficients de Fourier des fonctions de $L^p(G)$ (1970)
- Croot, III, Ernest S., Elsholtz, Christian, On thin sets of primes expressible as sumsets (2005)
- Croot, Ernie, Mao, Junzhe, Pohoata, Cosmin, Yip, Chi Hoi, A sharp inverse theorem for the quadratic large sieve (2026)
- Croot, Ernie, Mao, Junzhe, Yip, Chi Hoi, An inverse theorem on sets with rich additive structure modulo primes (2025)
- DeMillo, Richard A., Lipton, Richard J., A probabilistic remark on algebraic program testing (1978)
- DeVos, Matt, A short proof of Kneser's addition theorem for abelian groups (2014)
- Elsholtz, Christian, The inverse Goldbach problem (2001)
- Elsholtz, Christian, Harper, Adam J., Additive decompositions of sets with restricted prime factors (2015)
- Elsholtz, Christian, A remark on Hofmann and Wolke's additive decompositions of the set of primes (2001)
- Elsholtz, Christian, Additive decomposability of multiplicatively defined sets (2006)
- Ford, Kevin, Green, Ben, Konyagin, Sergei , Maynard, James, Tao, Terence, Long gaps between primes (2018)
- Gallagher, P. X., A larger sieve (1971)
- Gill, Nick, Quasirandom group actions (2016)
- Gowers, W. T., Quasirandom groups (2008)
- Green, Ben, Harper, Adam J., Inverse questions for the large sieve (2014)
- Hanson, Brandon, Additive correlation and the inverse problem for the large sieve (2020)
- Heath-Brown, D. R., A mean value estimate for real character sums (1995)
- Helfgott, Harald Andrés, The ternary Goldbach problem (2019)
- Hofmann, Alfred, Wolke, Dieter, On additive decompositions of the set of primes (1996)
- Hornfeck, Bernhard, Ein Satz über die Primzahlmenge (1954)
- Hornfeck, Bernhard, Berichtigung zur Arbeit: Ein Satz über die Primzahlmenge (1955)
- Inoue, Sh\=ota, Some explicit formulas for partial sums of Möbius functions (2021)
- Kneser, Martin, Abschätzung der asymptotischen Dichte von Summenmengen (1953)
- Laffer, W. B., Mann, H. B., Decomposition of sets of group elements (1964)
- Montgomery, H. L., Vaughan, R. C., The large sieve (1973)
- Montgomery, Hugh L., Vaughan, Robert C., Multiplicative Number Theory I: Classical Theory (2007)
- Montgomery, H. L., Zeros of $L$-functions (1969)
- OpenAI, {The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\mathrm{Re}(s)>7/8$} (2026)
- Ostmann, Hans-Heinrich, Additive Zahlentheorie. Erster Teil: Allgemeine Untersuchungen (1956)
- Pomerance, Carl, Sárközy, András, Stewart, C. L., On divisors of sums of integers, III (1988)
- Rota, Gian-Carlo, On the foundations of combinatorial theory I. Theory of Möbius functions (1964)
- Schwartz, J. T., Fast Probabilistic Algorithms for Verification of Polynomial Identities (1980)
- Shao, Xuancheng, On an inverse ternary Goldbach problem (2016)
- Zippel, Richard, Probabilistic algorithms for sparse polynomials (1979)
