[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 142](../index/theoretical-computer-science/142-deterministic-polynomial-factorization-over-prime-fields.md)

# 142 — Deterministic polynomial factorization over prime fields

[Index page](../index/theoretical-computer-science/142-deterministic-polynomial-factorization-over-prime-fields.md)

## Original CONTENTS.md summary

[S1:3427] (family entry):

> **142. Deterministic polynomial factorization over prime fields.** Gives a uniform deterministic algorithm that completely factors every nonzero dense degree-n polynomial over a prime field 𝔽p, including multiplicities, in bit complexity polynomial in $`(n+1)\log p`$. The prime is supplied in binary. No randomness, integer-factorization or primitive-root oracle, or GRH assumption is required.

[S2:361] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Polynomial factorization over a finite field.** Given a polynomial
$f(x)$ with coefficients in $\mathbf F_p = \mathbf Z/p\mathbf Z$, write it as a product of
irreducible polynomials, each with its multiplicity. This is a basic
operation in computational algebra — it underlies Reed–Solomon decoding,
cryptography, and symbolic computation.

The standard algorithms are **randomized**: pick random elements in the
quotient algebra and use them to split $f$ into factors
(**Cantor–Zassenhaus**, 1981). They run in expected polynomial time,
but the randomness is doing real work — finding an element that
"separates" the irreducible components [S4:16–19].

This family asks: **can we do it deterministically?** The answer is
**yes**, in bit complexity polynomial in $(n+1)\log p$, where $n$ is
the degree and $p$ is the prime [S4:28–38]. The exponent is a fixed
constant (the paper writes $10^{12}$ as a deliberately generous
placeholder) — the point is that *some* polynomial bound holds,
uniformly, with no randomness, no GRH, and no oracle for integer
factorization or primitive roots.

## Graduate summary

**Main theorem** ([S4:28–38], `thm:factorization`). "There is a
uniform deterministic algorithm that, given a prime $p$ in binary and
a nonzero dense polynomial $f\in\mathbf F_p[x]$ of degree $n$, outputs its
leading coefficient and its distinct monic irreducible factors with
their multiplicities in
$O\bigl(((n+1)\lceil\log_2 p\rceil)^{10^{12}}\bigr)$ bit operations,
with absolute implied constant. A constant polynomial returns an empty
factor list. The algorithm uses no randomness, integer-factorization
oracle, primitive-root oracle, or GRH assumption" [S4:28–38].

**The exponent is a placeholder.** "The exponent is deliberately
generous. The point is one fixed polynomial bound for all degrees and
prime characteristics" [S4:40–42]. The theorem is a uniformity result,
not a practical running-time claim.

**Auxiliary-prime reduction** ([S4:54–69], `thm:reduction`). The
proof separates the algebraic construction from its analytic input. If
the algorithm is also given, for each prime $q \le n$, an *auxiliary
prime* $\ell_q$ (a prime with $\ell_q \equiv 1 \bmod 12q$ and
$p^{(\ell_q-1)/q} \not\equiv 1 \bmod \ell_q$), then the factorization
runs in $O((B+E)^C)$ bit operations, where $B = 20+(n+1)(L+1)$ and
$E = \max(2, \max_q \ell_q)$ [S4:47–53]. The dependence on $E$ is on
the *numerical value* of the auxiliary primes, not their bit lengths.

**The analytic input.** The existence of small auxiliary primes is
supplied by a companion paper's zero-free theorem for finite-order
Hecke $L$-functions [S4:23–25]. This paper proves the
algebraic construction and the reduction; the analytic bound that
makes $E$ polynomial in $B$ is in the companion. Upward search,
trial division, and modular exponentiation construct the auxiliary
primes once the companion's bound is in hand [S4:70–74].

**Deterministic splitting.** Once the auxiliary prime is available,
the splitting procedure is a deterministic analogue of
Cantor–Zassenhaus: the auxiliary prime supplies the arithmetic
information that random choices provide in the classical algorithm
[S4:17–21].

**Formalization status.** None. No `lean/OAI/` file, no
`lean/docs/142.md`, no comparator challenge, no `main_results` entry —
the ledger row `fam=142` records tier T0 with zero challenges, zero
main results, zero formalized manuscripts, and no reasoning trace
[S6]. The manuscript ships its LaTeX under `build/` [S3] and a
typeset PDF at its root [S5]; the release ships nothing for this
family beyond those files. Nothing about this family is machine-checked:
"proves" in the abstract is the release's claim, and everything above
is read from that LaTeX.

## History of the conjecture

**Berlekamp** (1967, 1970) put linear algebra at the center of
finite-field factorization: Frobenius-fixed elements in the quotient
algebra encode the irreducible factors, and GCDs turn suitable such
elements into factors [S4:82–83].

**Cantor and Zassenhaus** (1981) gave the randomized algorithm that
runs in expected polynomial time: random elements separate the
components [S4:85–87]. The difficulty is to make every random choice
deterministic, with a bound polynomial in both the degree and the bit
length of the characteristic [S4:88–90].

Existing deterministic results all carry a price:
- **Shoup** (1990): polynomial in $n$ but $p^{1/2+o(1)}$ in $p$ — not
  polynomial in $\log p$ [S4:92–93].
- **Rónyai** (1988): polynomial under GRH, and only when the number
  of irreducible factors is bounded [S4:95].
- **Evdokimov**: conditional on other unproven hypotheses
  [S4:96–97].

The theorem here removes all of those conditions: no randomness, no
GRH, no oracle, and no bound on the number of factors. The analytic
ingredient (the zero-free theorem for finite-order Hecke $L$-functions
in the companion paper) supplies the missing deterministic separator
[S4:23–25][S4:70–74].

**Prior (my training data, not this repo).** The randomized
Cantor–Zassenhaus factorization and Shoup's $p^{1/2+o(1)}$
deterministic bound are standard in computational algebra. The
conditional results under GRH (Rónyai, Evdokimov) are established.
A *unconditional* deterministic polynomial-time factorization over
$\mathbf F_p$ with the prime given in binary — no randomness, no GRH, no
oracle — is the load-bearing claim of the release. I cannot confirm
such a result in my training data; the release ships the manuscript
(and a companion analytic paper) as proof.

## Consequences

- **Unconditional deterministic factorization.** Every nonzero dense
  degree-$n$ polynomial over $\mathbf F_p$ is completely factored, with
  multiplicities, in bit complexity polynomial in $(n+1)\log p$,
  uniformly, with no randomness, no GRH, and no oracle
  [S4:28–38][S1:3427].
- **The bound is uniform.** The same algorithm works for every prime
  $p$ and every degree $n$; the constant is absolute
  [S4:28–38].
- **The exponent is a placeholder.** The $10^{12}$ is deliberately
  generous; the theorem asserts the *existence* of a polynomial bound,
  not an optimal exponent [S4:40–42].
- **The algebra is separated from the analysis.** The reduction
  `thm:reduction` [S4:54–69] makes the algebraic construction
  self-contained given the auxiliary primes; the analytic input that
  bounds them polynomially is in the companion paper
  [S4:23–25][S4:70–74].
- **The randomized algorithms are matched deterministically.** The
  $O(\text{poly}((n+1)\log p))$ scale of Cantor–Zassenhaus in
  expectation is achieved deterministically, removing the randomness
  as a hypothesis [S4:85–90].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3427], manuscript link [S1:3434] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 142 at [S2:361] |
| S3 | [`preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/main.tex`](../../preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/main.tex) | 72 | document root; 73 lines |
| S4 | [`preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/00-introduction.tex`](../../preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/00-introduction.tex) | 278 | `thm:factorization` [S4:28–38], `thm:reduction` [S4:54–69]; 278 lines |
| S5 | [`preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf`](../../preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf) | 18911 | the manuscript as shipped |
| S6 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=142`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
