[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 015](../index/number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md)

# 015 — Torus-packet equidistribution in prime, quartic, and sextic degrees

[Index page](../index/number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md)

## Original CONTENTS.md summary

The release blurb 

> **015. Torus-packet equidistribution in prime, quartic, and sextic degrees.** Proves Haar equidistribution without escape of mass for complete volume-weighted torus packets from totally real fields: arbitrary lattices and prescribed local types in fixed prime degree at least five, arbitrary-order Picard packets in primitive quartic fields, and maximal-order ideal-class packets in primitive sextic fields. Here primitive means having no proper intermediate field; the relevant order or field discriminant tends to infinity. [S1:411]

The three manuscripts attack the same equidistribution question in
three degrees. The September 24 headline covers every fixed prime
degree at least five 

> We prove the packet form of the higher-dimensional Duke equidistribution
problem for totally real fields of any fixed prime degree at least five,
allowing arbitrary local homothety types of full lattices. As the
multiplier-order discriminant tends to infinity, the volume-weighted packet
measures converge to Haar probability measure, with no escape of mass. [S2:41–47]

The two October 5 companions are the special even degrees: the
primitive quartic paper, arbitrary orders [S3:15–17], and the
primitive sextic paper, maximal orders:

> We prove that the complete ideal-class packets of maximal orders in
totally real sextic fields with no proper intermediate fields become
equidistributed, with no escape of mass, in the space of unimodular
lattices as their field discriminants tend to infinity. The limit is
Haar probability measure. Each packet includes all coordinate-sign
translates and is weighted by diagonal-orbit volume. [S4:64–71]

## Undergraduate summary

A "torus packet" is a structured family of lattices built from a
number field: take all the periodic orbits of a torus action, group
them by their ideal class, and weight each by its orbit volume. As the
field gets larger (its discriminant goes to infinity), the question is
where this weighted mass ends up.

"Equidistribution" means the mass spreads out uniformly — it
converges to the uniform (Haar) probability measure — and "no escape
of mass" means none of it leaks off to infinity (the cusp). This
family proves exactly that, in three settings: every fixed prime
degree at least five, the primitive quartic degree, and the primitive
sextic degree. "Primitive" simply means the field has no proper
intermediate field between it and $\mathbb{Q}$.

The headline statement 

> **theorem**
For every fixed prime $n\ge5$ and every sequence
$(K_i,M_i,\sigma_i)$ as above with \mbox$D(M_i)\to\infty$,
$$\mu_{K_i,M_i,\sigma_i}\longrightarrow m_n.$$
The convergence is weak convergence of probability measures. In
particular, it holds against every continuous compactly supported
function, and no mass escapes into the cusp. [S2:103–112]

## Graduate summary

The family delivers Haar equidistribution without escape of mass for
complete volume-weighted torus packets in three degree regimes, all
for totally real fields.

**Prime degree (headline).** 

> We prove the packet form of the higher-dimensional Duke equidistribution
problem for totally real fields of any fixed prime degree at least five,
allowing arbitrary local homothety types of full lattices. As the
multiplier-order discriminant tends to infinity, the volume-weighted packet
measures converge to Haar probability measure, with no escape of mass. [S2:41–47]

The main theorem 

> **theorem**
For every fixed prime $n\ge5$ and every sequence
$(K_i,M_i,\sigma_i)$ as above with \mbox$D(M_i)\to\infty$,
$$\mu_{K_i,M_i,\sigma_i}\longrightarrow m_n.$$
The convergence is weak convergence of probability measures. In
particular, it holds against every continuous compactly supported
function, and no mass escapes into the cusp. [S2:103–112]

For each fixed prime $n \ge 5$, the volume-weighted packet measures
$\mu_{K_i, M_i, \sigma_i}$ converge weakly to the Haar probability
measure $m_n$ as the multiplier-order discriminant $D(M_i) \to
\infty$. The content beyond the limit is the *no-escape* clause: the
measures form a tight family, so convergence is against every
continuous compactly supported function, with no mass lost to the
cusp.

**Quartic.** 

> Let $K$ range over totally real quartic fields with no proper intermediate field, and let $\mathcal O$ be any order in $K$. We prove that the packets of periodic diagonal orbits attached to invertible $\mathcal O$-ideal classes, weighted by orbit volume, equidistribute with no escape of mass as $|\mathrm{Disc}(\mathcal O)|$ tends to infinity. The proof combines measure rigidity with a cubic-resolvent estimate that remains uniform at primes dividing the order index. [S3:15–17]

The quartic paper allows *arbitrary* orders (not just maximal), which
is the harder local point: the cubic-resolvent estimate must stay
uniform at primes dividing the order index.

**Sextic.** 

> We prove that the complete ideal-class packets of maximal orders in
totally real sextic fields with no proper intermediate fields become
equidistributed, with no escape of mass, in the space of unimodular
lattices as their field discriminants tend to infinity. The limit is
Haar probability measure. Each packet includes all coordinate-sign
translates and is weighted by diagonal-orbit volume. [S4:64–71]

The sextic paper restricts to maximal orders and to the *complete*
ideal-class packet (all coordinate-sign translates included), with
the limit again Haar probability measure.

## history of the conjecture

Prior (my training data, not this repo): Duke's equidistribution
results and their higher-dimensional generalizations describe how
periodic orbits of diagonal flows on symmetric spaces distribute as
the discriminant grows. The "packet" formulation packages the full
orbit family for a given ideal class, weighted by volume, and asks
for weak convergence to Haar measure with a tightness clause. The
prime-degree regime generalizes the classical results to every fixed
prime degree $\ge 5$ and to *arbitrary* local homothety types of full
lattices; the quartic and sextic papers isolate the first two even
degrees where a proper-intermediate-field condition ("primitive") is
the right hypothesis. The no-escape clause is the technically
essential part — a weak limit alone does not rule out mass escaping
into the cusp.

## Consequences

**No-escape Haar equidistribution in three regimes.** Prime degree
$\ge 5$ (arbitrary lattices, arbitrary local types), primitive quartic
(arbitrary orders), and primitive sextic (maximal orders) all give
weak convergence of the volume-weighted packet measures to Haar
probability measure with a tightness clause.

**Arbitrary local types and arbitrary orders.** The prime-degree
result allows the local homothety types to vary freely, and the
quartic result works for arbitrary (not just maximal) orders, which
is uniform at index-dividing primes.

## section skeleton

Three manuscripts with distinct trees.

**Prime-degree** [S2], `build/paper.tex`: abstract (line 41), main
theorem (line 103), then six section inputs [S2:234–241] (packets,
local, analytic, geometry, entropy, adelic), one `.bib` file [S7].

**Quartic** [S3:15–17], `build/manuscript/main.tex`: abstract (line 15),
then a macros input [S3:9] and nine section inputs [S3:19–27]
(introduction, packets, ordinary, rigidity, exterior, local-fourier,
additive, sieve, conclusion).

**Sextic** [S4:64–71], `build/main.tex`: abstract (line 64), then nine
section inputs [S4:73–81] (introduction, arithmetic, homogeneous,
conditioning, product, activity, entropy, combination, assembly),
one `.bib` file.

## Coverage

T2: three manuscripts, zero formalized, one comparator challenge,
zero `main_results` entries, one scope note. The ledger reads `paps
3`, `paps_form 0`, `mainres 0`, `chal 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes uniform`. The catalog entry
[S11:106] names all three PDFs [S8] [S9] [S10]. No `verification/`
bundle, no reasoning trace.

The scope note [S5:9] covers the prime-degree manuscript and states the
equidistribution target: "The formalization proves equidistribution of volume-weighted torus packets for totally real number fields of every fixed prime degree at least five. For any sequence of full lattices whose multiplier-order discriminants tend to infinity, the packet measures converge weakly to Haar probability measure and form a tight family, so no mass escapes. Arbitrary local homothety types are allowed, and the fields may vary along the sequence. [S5:9]"

The comparator stub [S6:200–211] states that target — weak convergence
of the complete packet measures to a Haar probability measure with a
tightness clause — and ends in `sorry`:

```lean
theorem prime_degree_packet_measure_equidistribution_unconditional
 (d : ℕ) (hprime : Nat.Prime (d+1)) (hfive : 5 ≤ d+1)
 (K : ℕ → Type u) [∀ i, Field (K i)] [∀ i, NumberField (K i)]
 [∀ i, NumberField.IsTotallyReal (K i)]
 (M : ∀ i, PrimeDegreePackets.FullLattice (d+1) (K i))
 (σ : ∀ i, OrderedEmbeddings (d+1) (K i))
 (hn : ∀ i, Module.finrank ℚ (K i)=d+1)
 (hD : Tendsto (fun i => PrimeDegreePackets.multiplierDiscriminant (M i)) atTop atTop) :
 ∃ ν : Measure (X (d+1)), IsHaarProbability ν ∧
 WeakProbabilityConvergence (fun i => packetMeasure (M i) (σ i)) ν ∧
 IsTightMeasureSet (Set.range (fun i => packetMeasure (M i) (σ i))) := by
 sorry
```
[S6:200–211]

Note the ledger reads `paps_form 0` (no `main_results` entry), so the
scope note describes an intended target, not a landed
formalization. The quartic and sextic companions carry no comparator
at all.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 015 at line 411) |
| S2 | [`preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/build/paper.tex`](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/build/paper.tex) | 247 | Prime-degree manuscript: abstract, main theorem |
| S3 | [`preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/build/manuscript/main.tex`](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/build/manuscript/main.tex) | 30 | Quartic manuscript: abstract |
| S4 | [`preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/build/main.tex`](../../../preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/build/main.tex) | 88 | Sextic manuscript: abstract |
| S5 | [`lean/docs/015.md`](../../../lean/docs/015.md) | 15 | Scope note |
| S6 | [`lean/ComparatorChallenges/DukePrimeDegree.lean`](../../../lean/ComparatorChallenges/DukePrimeDegree.lean) | 231 | Challenge stub (prime-degree target, sorry) |
| S7 | [`preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/build/references.bib`](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/build/references.bib) | 123 | Prime-degree bibliography |
| S8 | [`preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf`](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf) | 11360 | Compiled prime-degree manuscript |
| S9 | [`preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf`](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf) | 21589 | Compiled quartic manuscript |
| S10 | [`preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf`](../../../preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf) | 20218 | Compiled sextic manuscript |
| S11 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 015 at line 106) |

## Bibliography

- Duke, William, Hyperbolic distribution problems and half-integral weight Maass forms (1988)
- Einsiedler, Manfred, Lindenstrauss, Elon, Michel, Philippe, Venkatesh, Akshay, Distribution of periodic torus orbits and Duke's theorem for cubic fields (2011)
- Einsiedler, Manfred, Lindenstrauss, Elon, Michel, Philippe, Venkatesh, Akshay, Distribution of periodic torus orbits on homogeneous spaces (2009)
- Einsiedler, Manfred, Katok, Anatole, Lindenstrauss, Elon, Invariant measures and the set of exceptions to Littlewood's conjecture (2006)
- Greschonig, Gernot, Schmidt, Klaus, Ergodic decomposition of quasi-invariant probability measures (2000)
- Khayutin, Ilya, Arithmetic of double torus quotients and the distribution of periodic torus orbits (2019)
- Linnik, Yurij V., Ergodic Properties of Algebraic Fields (1968)
- Mahler, Kurt, On lattice points in $n$-dimensional star bodies. I. Existence theorems (1946)
- Milne, James S., Algebraic Number Theory (2020)
- Lemke Oliver, Robert J., Thorner, Jesse, Zaman, Asif, An approximate form of Artin's holomorphy conjecture and non-vanishing of Artin $L$-functions (2024)
- Pollack, Paul, Nonnegative multiplicative functions on sifted sets, and the square roots of $-1$ modulo shifted primes (2020)
- Rokhlin, V. A., Lectures on the entropy theory of measure-preserving transformations (1967)
- Shiu, Peter, A Brun–Titchmarsh theorem for multiplicative functions (1980)
- Stark, H. M., Some effective cases of the Brauer–Siegel theorem (1974)
- Sutherland, Andrew V., The Analytic Class Number Formula (2021)
