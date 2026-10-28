[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 164](../index/combinatorics/164-hindmans-finite-sums-and-products-conjecture.md)

# 164 — Hindman's finite sums and products conjecture

[Index page](../index/combinatorics/164-hindmans-finite-sums-and-products-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:3861] and the catalog abstract [S2:407] state
the family's claim: it proves Hindman's finite sums and products
conjecture, that every finite coloring of the positive integers
contains, for any prescribed finite size, a set whose nonempty subset
sums and nonempty subset products all share one color. The
manuscript's abstract "We prove Hindman's finite sums and products conjecture: for every finite
coloring of the positive integers and every positive integer $k$, there is a
$k$-element set whose nonempty subset sums and nonempty subset products all
have the same color. [S3:67–70]"

## Undergraduate summary

For a finite set $A\subset\mathbb N$, write $\mathrm{FS}(A)$ for the set of
all nonempty subset sums of $A$ and $\mathrm{FP}(A)$ for the set of all
nonempty subset products [S4:3–11]. The conjecture asks for a set whose
combined family $\mathrm{FS}(A)\cup\mathrm{FP}(A)$ is monochromatic. The manuscript
proves this with a separation: the elements can be chosen so that no
prefix sum is divisible by a later element, which eliminates collisions
between expressions except the shared singletons 

> **Theorem 1.1**
Let $r,m\ge1$ be integers, and fix real numbers $R\ge2$ and $D\ge1$.
For every coloring $\chi:\mathbb N\to[r]$,
there are distinct positive integers $a_1<\cdots<a_m$ and a color
$c\in[r]$ such that
$$\chi\left(\sum_{j\in J}a_j\right)
 =\chi\left(\prod_{j\in J}a_j\right)=c
 \quad\text{for every }\varnothing\ne J\subseteq[m].$$
Equivalently, $\mathrm{FS}(A)\cup\mathrm{FP}(A)$ is monochromatic for a set
$A\subset\mathbb N$ of cardinality $m$.
The elements can additionally be chosen to satisfy
$$a_1>R,\qquad
 a_d>R\left(\sum_{k<d}a_k+\prod_{k<d}a_k\right)^D
 \quad(2\le d\le m).$$ [S4:13–31]

The corollary adds that the $2^m-1$ sums and the $2^m-1$ products are
all distinct apart from the $m$ elements, so the union has
$2(2^m-1)-m$ distinct values 

> **Theorem 1.2**
For every finite coloring of $\mathbb N$ and every $m\ge1$, there is an
$m$-element set $A\subset\mathbb N$ for which $\mathrm{FS}(A)\cup\mathrm{FP}(A)$ is
monochromatic and
$$|\mathrm{FS}(A)|=|\mathrm{FP}(A)|=2^m-1,\qquad \mathrm{FS}(A)\cap\mathrm{FP}(A)=A.$$
In particular, the union has $2(2^m-1)-m$ distinct elements. [S4:39–47]

## Graduate summary

**Two principles: Prediction and Alignment.** The finite combinatorial
part works on ordered blocks of widely separated variables: a Ramsey
argument and the finite sums theorem select block products whose
nonempty products are already one color, and the remaining task is to
make their sums carry that same color [S4:116–122]. The proof
separates this into a Prediction Principle and an Alignment
Principle [S4:124–138]. Prediction replaces the color functions by
piecewise nilsequences — Lipschitz functions along nilpotent orbits,
separately on intervals and residue classes — while retaining the
multiplicative color masks. Alignment selects from a finite list of
rational scale vectors so that a positive prediction at every center
stays positive after all the required additive shifts, with success
probability bounded below independently of the nilsequence complexity.

**Three constructions.** Weights encode divisibility by the earlier
variables and let weighted Cauchy–Schwarz strip the product-color
conditions; nilsequence models on nested intervals supply a common
model at two additive scales; and a nilpotent recurrence argument
realizes the required shifts as transformations of the nilsequence
states, with a step independent of model complexity [S4:139–175]. The
inputs are the Green–Tao–Ziegler inverse theorem, the Tao–Ziegler
concatenation theorem, quantitative polynomial equidistribution, and
nilpotent polynomial recurrence.

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The separate additive and multiplicative problems have classical
answers: Schur's theorem, the Folkman–Rado–Sanders finite sums
theorem, and the multiplicative half by coloring $n\mapsto\chi(2^n)$
[S4:56–73]. The simultaneous question is different: Hindman
constructed a finite coloring with no infinite set whose terms,
pairwise sums and products all have one color, and his finite
conjecture asks for arbitrarily large finite sets instead
[S4:74–93]. For two variables, computer-assisted arguments of Graham
and Hindman established a monochromatic quartet $\{x,y,x+y,xy\}$ in
every two-coloring; Bowen and Moreira gave proofs for stronger
configurations [S4:94–112].

## Consequences

**The finite conjecture, with separation.** The theorem resolves
Hindman's finite sums and products conjecture positively, and the
separation eliminates every collision except the shared singleton
values [S4:33–37].

**A distinct-values corollary.** The elementary corollary gives an
$m$-element set whose $2(2^m-1)-m$ sum-and-product values are all
distinct apart from the $m$ elements, an explicit count the main
statement does not supply [S4:39–47].

**A finite statement, not an infinite one.** Both conclusions concern
prescribed finite sets; the separation does not assert the existence
of an infinite simultaneous sequence, and Hindman's earlier counterexample
remains compatible with both [S4:49–52].

## Section skeleton

**Manuscript** [S3:67–70], 8 sections under `build/sections/`:
introduction [S4], framework, arithmetic, correlation, prediction,
rough progressions, cube limits, and alignment.

The manuscript's root is `build/main.tex`, and its reference list is a
`thebibliography` block [S5], not a `.bib` file. It ships no
`verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 10 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 164 at line 3861. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 407. |
| S3 | [`preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/main.tex`](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/main.tex) | 82 | Main file: title and abstract. |
| S4 | [`preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/sections/01_introduction.tex`](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/sections/01_introduction.tex) | 220 | The main theorem, the distinct-expressions corollary, the history, and the proof strategy. |
| S5 | [`preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/references.tex`](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/references.tex) | 237 | The manuscript's bibliography (a thebibliography block). |

## Bibliography

- R. Alweiss, _Monochromatic sums and products over $\mathbb{Q}$_, arXiv:2307.08901v6, 12 July 2026; accepted for publication in Duke Mathematical Journal. .
- R. Alweiss, _Monochromatic sums and products of polynomials_, Discrete Anal. **2024**, Paper No. 5, 7 pp. .
- R. Alweiss, M. Bowen and M. Sabok, _Sums, products, and exponents in two-colorings of the naturals_, arXiv:2512.09598v1, 10 December 2025. .
- M. Bowen, _Monochromatic products and sums in $2$-colorings of $\mathbb{N}$_, Adv. Math. **462** (2025), 110095. .
- W. T. Gowers, _Decompositions, approximate structure, transference, and the Hahn–Banach theorem_, Bull. Lond. Math. Soc. **42** (2010), no. 4, 573–606. .
- B. Green, T. Tao and T. Ziegler, _An inverse theorem for the Gowers $U^{s+1}[N]$-norm_, Ann. of Math. (2) **176** (2012), no. 2, 1231–1372. . Further revision: arXiv:1009.3998v5, 23 April 2026, .
- B. Green, T. Tao and T. Ziegler, _Erratum for ``An inverse theorem for the Gowers $U^{s+1}[N]$-norm''_, author-hosted erratum, April 2024, 6 pp. .
- N. Hindman, _Finite sums from sequences within cells of a partition of $N$_, J. Combin. Theory Ser. A **17** (1974), no. 1, 1–11. .
- N. Hindman, _Partitions and sums and products of integers_, Trans. Amer. Math. Soc. **247** (1979), 227–245. .
- N. Hindman, _Partitions and sums and products—Two counterexamples_, J. Combin. Theory Ser. A **29** (1980), no. 1, 113–120. .
- B. Host and B. Kra, _Nonconventional ergodic averages and nilmanifolds_, Ann. of Math. (2) **161** (2005), no. 1, 397–488. .
- V. Bergelson and A. Leibman, _Set-polynomials and polynomial extension of the Hales–Jewett theorem_, Ann. of Math. (2) **150** (1999), no. 1, 33–75. .
- V. Bergelson and A. Leibman, _Topological multiple recurrence for polynomial configurations in nilpotent groups_, Adv. Math. **175** (2003), no. 2, 271–296. .
- A. Leibman, _Multiple recurrence theorem for nilpotent group actions_, Geom. Funct. Anal. **4** (1994), no. 6, 648–659. .
- A. Leibman, _Pointwise convergence of ergodic averages for polynomial sequences of translations on a nilmanifold_, Ergodic Theory Dynam. Systems **25** (2005), no. 1, 201–213. .
- V. Bergelson and J. Moreira, _Measure preserving actions of affine semigroups and $\{x+y,xy\}$ patterns_, Ergodic Theory Dynam. Systems **38** (2018), no. 2, 473–498. .
- V. Bergelson and J. Moreira, _Ergodic theorem involving additive and multiplicative groups of a field and $\{x+y,xy\}$ patterns_, Ergodic Theory Dynam. Systems **37** (2017), no. 3, 673–692. .
- J. Moreira, _Monochromatic sums and products in $\mathbb{N}$_, Ann. of Math. (2) **185** (2017), no. 3, 1069–1090. .
- N. Hindman and D. Phulara, _Some new additive and multiplicative Ramsey numbers_, J. Combin. **4** (2013), no. 1, 81–93.
- O. Reingold, L. Trevisan, M. Tulsiani and S. Vadhan, _New proofs of the Green–Tao–Ziegler dense model theorem: An exposition_, arXiv:0806.0381v1, 2 June 2008. .
- F. K. Richter, _Sums and products in sets of positive density_, arXiv:2507.00515v2, 7 February 2026. .
- M. Bowen and M. Sabok, _Monochromatic products and sums in the rationals_, Forum Math. Pi **12** (2024), e17. .
- B. Green and T. Sanders, _Monochromatic sums and products_, Discrete Anal. **2016**, Paper No. 5, 48 pp. .
- J. H. Sanders, _A Generalization of Schur's Theorem_, author-posted excerpt from the author's Ph.D. dissertation, Yale University, 1968; arXiv:1712.03620v1 (2017). .
- I. Schur, _Über die Kongruenz $x^m+y^m\equiv z^m\pmod p$_, Jahresber. Dtsch. Math.-Ver. **25** (1916), 114–117.
- A. Selberg, _An elementary proof of the prime-number theorem for arithmetic progressions_, Canad. J. Math. **2** (1950), 66–78. .
- N. Hindman and D. Strauss, _Algebra in the Stone–Čech compactification: Theory and applications_, 2nd revised and extended ed., De Gruyter Textbook, Walter de Gruyter, Berlin–Boston, 2012. .
- E. Szemerédi, _On sets of integers containing no $k$ elements in arithmetic progression_, Acta Arith. **27** (1975), 199–245. .
- B. Green and T. Tao, _The quantitative behaviour of polynomial orbits on nilmanifolds_, Ann. of Math. (2) **175** (2012), no. 2, 465–540. .
- B. Green and T. Tao, _On the quantitative distribution of polynomial nilsequences—erratum_, Ann. of Math. (2) **179** (2014), no. 3, 1175–1183. . Further revision: arXiv:1311.6170v3, 14 August 2015, .
- B. Green and T. Tao, _Linear equations in primes_, Ann. of Math. (2) **171** (2010), no. 3, 1753–1850. .
- B. Green and T. Tao, _The primes contain arbitrarily long arithmetic progressions_, Ann. of Math. (2) **167** (2008), no. 2, 481–547. .
- B. Green and T. Tao, _An arithmetic regularity lemma, an associated counting lemma, and applications_, in _An Irregular Mind: Szemerédi is 70_, Bolyai Society Mathematical Studies, Springer, 2010, pp. 261–334. Corrected version: arXiv:1002.2028v3, 24 November 2020, .
- B. L. van der Waerden, _Beweis einer Baudetschen Vermutung_, Nieuw Arch. Wiskd. (2) **15** (1927), 212–216.
- T. Yamada, _Explicit improvements of the Brun–Titchmarsh theorem for arbitrary intervals_, arXiv:2312.16090v1, 26 December 2023. .
- T. Tao and T. Ziegler, _Concatenation theorems for anti-Gowers-uniform functions and Host-Kra characteristic factors_, Discrete Anal. **2016**, Paper No. 13, 61 pp. . Revised version: arXiv:1603.07815v4, 17 January 2017, .
- P. Zorin-Kranich, _A nilpotent IP polynomial multiple recurrence theorem_, J. Anal. Math. **123** (2014), 183–225. . Revised version: arXiv:1206.0287v4, 4 June 2018, .
