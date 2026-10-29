[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 076](../index/real-and-complex-analysis/076-ultraflat-real-littlewood-polynomials.md)

# 076 — Ultraflat real Littlewood polynomials

[Index page](../index/real-and-complex-analysis/076-ultraflat-real-littlewood-polynomials.md)

## Original CONTENTS.md summary

The release's blurb [S1:1888] and the catalog abstract [S2:226] state the
family's claim: real Littlewood polynomials — polynomials of length $`N`$ with
$`\{-1,1\}`$ coefficients — can be made ultraflat, with modulus
$`(1+o(1))\sqrt N`$ uniformly on the entire unit circle for every
sufficiently large integer length, and their binary merit factors tend to
infinity, disproving Turyn's bounded-merit-factor conjecture. The family
ships three manuscripts in a versioning chain; the current (highest)
manuscript's abstract 

> For every $`\varepsilon\in(0,1)`$ and every sufficiently large integer $`N`$,
there is a polynomial of length $`N`$ with coefficients in $`\{-1,1\}`$ whose
modulus lies between $`(1-\varepsilon)\sqrt N`$ and
$`(1+\varepsilon)\sqrt N`$ everywhere on the unit circle. Thus real
Littlewood polynomials can be ultraflat through every sufficiently large
integer length. The signs may be chosen separately at each length. [S7:39–46]

## Undergraduate summary

A Littlewood polynomial of length $`N`$ is $`\sum_{k=0}^{N-1}\varepsilon_k z^k`$
with each sign $`\varepsilon_k\in\{-1,1\}`$. Parseval's identity says its
mean-square modulus on the unit circle is exactly one, so the maximum
$`|P(z)|`$ can never fall below $`\sqrt N`$; $`m_N`$, the minimum over all sign
choices of the normalized maximum, is at least one. The flatness question is
how close to that square-root floor the *maximum* can be pushed.

The real-sign restriction is the hard part. Polynomials with complex phases
of modulus one can be made ultraflat by classical quadratic-phase
constructions, and a two-sided *constant-factor* flat statement was proved
for real signs, but making the upper constant tend to one for real signs
— at every integer length, not just a subsequence — is the theorem
here. Erdös's fixed-gap question had asked whether $`m_N`$ stays above
$`1+c`$ for some absolute $`c>0`$ [S4:14–19]; the answer is no.

The three manuscripts sharpen the result in sequence: first the maximum is
asymptotically minimal [S3:35–42], then it is asymptotically minimal
while the minimum stays a fixed positive multiple of $`\sqrt N`$
[S5:36–41], and finally both bounds pinch to $`(1\pm\varepsilon)\sqrt N`$
for every small $`\varepsilon`$ [S7:39–46].

## Graduate summary

**The versioning chain.** The three manuscripts are a nesting of statements
about the same real-sign class. The first (asymptotically-minimal) defines
$`m_N`$ and proves 

> **Theorem 1.1**
For Littlewood polynomials with real coefficients,
$$\lim_{N\to\infty}m_N=1.$$
Equivalently, for every $`\eta>0`$ there is $`N_0`$ such that for every integer
$`N\ge N_0`$ there are signs $`\varepsilon_0,\ldots,\varepsilon_{N-1}`$ with
$$\max_{|z|=1}\left|\sum_{k=0}^{N-1}\varepsilon_kz^k\right|
 \le(1+\eta)\sqrt N.$$ [S4:22–33]

so the smallest possible maximum is $`(1+o(1))\sqrt N`$ through all integer
lengths. The second strengthens the result to coexist with a uniform lower
bound — a single polynomial at every sufficiently large length whose
modulus lies between $`\sqrt N/16`$ and $`(1+\eta)\sqrt N`$ on the whole circle


> **Theorem 1.1**
For every $`\eta>0`$ there is an integer $`N_0=N_0(\eta)`$ such that, for every
integer $`N\ge N_0`$, there exist real signs
$`\varepsilon_0,\ldots,\varepsilon_{N-1}`$ for which
$$\frac1{16}\sqrt N
 \le\left|\sum_{k=0}^{N-1}\varepsilon_kz^k\right|
 \le(1+\eta)\sqrt N
 \qquad (|z|=1).$$ [S6:18–28]

The third (the current manuscript) drops the fixed constant on the lower
side, giving two-sided ultraflatness: for every $`\varepsilon\in(0,1)`$ there
are signs with $`(1-\varepsilon)\sqrt N\le |P(z)|\le(1+\varepsilon)\sqrt N`$
for every $`|z|=1`$ 

> **Theorem 1**
For every $`\varepsilon\in(0,1)`$ there is an integer $`N_0`$ such that,
for every integer $`N\ge N_0`$, there are signs
$`\varepsilon_0,\ldots,\varepsilon_{N-1}`$ for which
$$(1-\varepsilon)\sqrt N
 \le\left|\sum_{k=0}^{N-1}\varepsilon_k z^k\right|
 \le(1+\varepsilon)\sqrt N
 \qquad\text{for every }|z|=1.$$ [S8:15–25]

The first manuscript's proof gives no positive lower bound and asserts no
two-sided ultraflatness [S4:35–39]; all three conclusions are existential,
with no convergence rate and no signing algorithm.

**The $`L^p`$-flatness addition.** Beyond the uniform maximum, the
formalization proves a finite-exponent statement for one all-length real-sign
family: for every fixed finite $`p>0`$ the $`L^p`$ mean of
$`\bigl||P_N(z)|/\sqrt N-1\bigr|`$ on the circle tends to zero [S9].

## History of the conjecture

Erdös asked (Problem 26) whether real-sign polynomials could stay between
two fixed positive multiples of $`\sqrt N`$ on the entire circle
[S8:33–40]; Littlewood posed the related flatness question. The Rudin–Shapiro
construction gives real-sign polynomials with maximum $`\sqrt{2N}`$ at dyadic
lengths, and Balister, Bollobás, Morris, Sahasrabudhe and Tiba proved the
two-sided constant-factor flat statement at every degree at least two;
neither makes the upper constant tend to one.

The coefficient class is the dividing line. Complex unimodular coefficients
admit ultraflat constructions (Kahane; Bombieri–Bourgain quantitatively),
and the present proof must instead preserve real coefficients and round them
to signs [S4:56–64]. A growing additive gap above the Parseval bound is
nonetheless possible — Erdélyi showed every Littlewood polynomial satisfies
$`\|P\|_\infty^2\ge N+(N-1)^{1/3}/38`$ — which is compatible with
$`m_N\to1`$ [S4:73–80].

The merit-factor consequence is on a separate line. The largest binary merit
factor at length $`N`$ is, in the standard normalization, what Turyn's
conjecture (Erdös's $`L^4`$-norm conjecture) asserts is bounded
[S4:100–102]; the family disproves that boundedness in the stronger
all-length form, the merit factor tending to infinity through all integers
[S4:107–109].

**Prior (my training data, not this repo).** The real-sign flatness and
merit-factor questions are genuine open problems in additive combinatorics
and harmonic analysis; I know the Rudin–Shapiro, Kahane,
Bombieri–Bourgain, and Balister–Bollobás–Morris–Sahasrabudhe–Tiba antecedents
and Turyn's conjecture, all consistent with the manuscripts' accounts. I
cannot independently verify these 2026 manuscripts' arguments.

## Consequences

**Two-sided ultraflatness.** For every $`\varepsilon\in(0,1)`$ and every
sufficiently large $`N`$ there are real signs with
$`(1-\varepsilon)\sqrt N\le |P(z)|\le(1+\varepsilon)\sqrt N`$ on the whole
circle, including the real endpoints [S8:15–29].

**Unbounded binary merit factor.** The largest binary merit factor at length
$`N`$ tends to infinity through all integers, disproving Turyn's conjecture
[S4:107–109].

**A simple-spectrum Morse shift.** By the Downarowicz–Lacroix theorem,
unbounded binary merit factors feed a uniquely ergodic binary Morse shift
with simple spectrum whose zero-coordinate spectral measure is absolutely
continuous with an $`L^2`$ density [S4:111–118].

**The $`L^p`$-flatness implication.** The main theorem implies flatness in
every fixed finite $`L^p`$ modulus sense, the content of the second formalized
statement [S9].

## Section skeleton

Three manuscripts, a versioning chain in the same real-sign class:

- **v1** `Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026`
  — root `build/main.tex` [S3:35–42] (title [S3:30], date [S3:32]), ten flat
  `.tex` files under `build/` (introduction [S4:22–33], reduction, packing,
  spreading, sampling, rounding, flatness, merit-morse), one appendix
  (concentration), `refs.bib`.
- **v2** `Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026`
  — root `build/main.tex` [S5:36–41] (title [S5:31], date [S5:33]), seven files
  under `build/sections/` (introduction [S6:18–28], spreading, packing, sampling,
  correction, rounding, completion), `refs.bib`.
- **v3** `Ultraflat-real-Littlewood-polynomials-October-5-2026` — root
  `build/main.tex` [S7:39–46] (title [S7:34], date [S7:36]), six files under
  `build/sections/` (introduction [S8:15–25], oscillation, rounding, balanced,
  waves, completion), `refs.bib`.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S9]. The formalization gives real Littlewood polynomials of
every sufficiently large length with maximum modulus at most
$`(1+\eta)\sqrt N`$ for any fixed $`\eta>0`$ (so the smallest possible maximum
is asymptotically minimal through all integer lengths), plus a second
statement choosing one all-length real-sign family whose $`L^p`$ mean of
$`\bigl||P_N(z)|/\sqrt N-1\bigr|`$ tends to zero for every fixed finite $`p>0`$.
Both results are existential, with no effective convergence rate or signing
algorithm. The scope note links only the v1 manuscript; it records
`scope: "Partial progress."` and `review: status: unchecked`, and zero
`sorry` in the Lean source is not a comparator pass — the library has not
been built here.

**The two comparator stubs.** Both ship with a `sorry`. The
asymptotically-minimal target 

```lean
def MainStatement : Prop :=
  ∀ η : ℝ, 0 < η → ∃ N₀ : ℕ, 1 ≤ N₀ ∧ ∀ N : ℕ, N₀ ≤ N →
    ∃ ε : Fin N → ℝ, IsRealSigning ε ∧
      ∀ z : ℂ, ‖z‖ = 1 → ‖littlewoodValue ε z‖ ≤ (1 + η) * Real.sqrt N

theorem main : MainStatement := by
  sorry
```
[S10:13–19]

The finite-exponent-flatness target 

```lean
def MainStatement : Prop :=
  ∃ ε : (N : ℕ) → Fin N → ℝ,
    (∀ N : ℕ, IsRealSigning (ε N)) ∧
    ∀ p : ℝ, 0 < p →
      Filter.Tendsto
        (fun N : ℕ =>
          ∫ t : UnitAddCircle,
            Real.rpow
              |‖littlewoodValue (ε N) (fourier (1 : ℤ) t)‖ /
                  Real.sqrt (N : ℝ) - 1|
              p
            ∂AddCircle.haarAddCircle)
        Filter.atTop (𝓝 (0 : ℝ))

/-- One all-length real-sign family for every finite positive real exponent. -/
theorem main : MainStatement := by
  sorry
```
[S11:19–35]

**Statement 1, proven in the OAI tree.** The `main_results` entry names
`OAI.AsymptoticallyMinimalLittlewood.main` in
`OAI/Analysis/Littlewood/Main.lean`. Its `MainStatement` — the
asymptotically-minimal property — is defined in `Model.lean`


```lean
def MainStatement : Prop :=
  ∀ η : ℝ, 0 < η → ∃ N₀ : ℕ, 1 ≤ N₀ ∧ ∀ N : ℕ, N₀ ≤ N →
    ∃ ε : Fin N → ℝ, IsRealSigning ε ∧
      ∀ z : ℂ, ‖z‖ = 1 → ‖littlewoodValue ε z‖ ≤ (1 + η) * Real.sqrt N
```
[S12:15–18]

and proved at `Main.lean:187` 

```lean
theorem main : MainStatement := by
  intro η hη
  obtain ⟨δ,hδ,hδ20,hbudget⟩ := small_delta_budget hη
  obtain ⟨X,L,C,hC,hL,hX,hE,hmax⟩ := almost_sign_sampler hδ hδ20
  let B := Real.sqrt ((1+δ)^3/(1-δ))+393216*Real.sqrt (δ*Real.log (20/δ))
  have hB : B<1+η := by dsimp [B]; linarith
```
[S13:187–192]

**Statement 2, proven in the OAI tree.** The second statement's
`MainStatement` (the $`L^p`$-flatness of one all-length family) is defined in
`FlatnessModel.lean` 

```lean
def MainStatement : Prop :=
  ∃ ε : (N : ℕ) → Fin N → ℝ,
    (∀ N : ℕ, IsRealSigning (ε N)) ∧
    ∀ p : ℝ, 0 < p →
      Filter.Tendsto
        (fun N : ℕ =>
          ∫ t : UnitAddCircle,
            Real.rpow
              |‖littlewoodValue (ε N) (fourier (1 : ℤ) t)‖ /
                  Real.sqrt (N : ℝ) - 1|
              p
            ∂AddCircle.haarAddCircle)
        Filter.atTop (𝓝 (0 : ℝ))
```
[S14:19–31]

and proved at `FiniteFlatness.lean:14` 

```lean
theorem main : MainStatement := by
  have hmain : ∀ η : ℝ, 0 < η → ∃ N₀ : ℕ, 1 ≤ N₀ ∧ ∀ N : ℕ, N₀ ≤ N →
      ∃ ε : Fin N → ℝ, IsRealSigning ε ∧
        ∀ z : ℂ, ‖z‖ = 1 → ‖littlewoodValue ε z‖ ≤ (1 + η) * Real.sqrt N := by
    change AsymptoticallyMinimalLittlewood.MainStatement
```
[S15:14–18]

Only statement 1 appears in `main_results` (config
`ComparatorChallenges/AsymptoticallyMinimalLittlewood.json` \u2192 declaration
`OAI.AsymptoticallyMinimalLittlewood.main` \u2192 file
`OAI/Analysis/Littlewood/Main.lean`); statement 2 has its comparator stub
linked from the scope note but no `main_results` entry. The OAI
`Littlewood` tree is 27 `.lean` files over 9,601 lines with zero `sorry`.

## Coverage

T3: the family is formalized. The ledger row `fam=076` records `paps 3`,
`paps_form 1`, `tier T3`, `chal 2`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes bound|uniform`, `resolves_named 1`,
`counterex_broad 1`, `summary 1`. The family ships three LaTeX manuscripts
(v1 formalized, v2 and v3 superseding it), a scope note, two comparator
challenges and one `main_results` entry; it ships no verification bundle and
no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 076 at [S1:1888] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry for 076 at [S2:226] |
| S3 | [`preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/build/main.tex`](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/build/main.tex) | 56 | v1 (asymptotically-minimal) manuscript root; title [S3:30], date [S3:32], abstract [S3:35–42] |
| S4 | [`preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/build/introduction.tex`](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/build/introduction.tex) | 162 | v1 introduction; the $m_N$ definition and fixed-gap question [S4:14–19], the main theorem [S4:22–33], the no-rate / no-lower-bound caveat [S4:35–39], the coefficient-class divide [S4:56–64], the Erdélyi gap [S4:73–80], the merit-factor / Turyn section [S4:100–109], the Morse-shift consequence [S4:111–118] |
| S5 | [`preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/build/main.tex`](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/build/main.tex) | 52 | v2 (nearly-minimal) manuscript root; title [S5:31], date [S5:33], abstract [S5:36–41] |
| S6 | [`preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/build/sections/introduction.tex`](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/build/sections/introduction.tex) | 146 | v2 introduction; the two-sided theorem [S6:18–28] |
| S7 | [`preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/build/main.tex`](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/build/main.tex) | 55 | v3 (ultraflat) manuscript root; title [S7:34], date [S7:36], abstract [S7:39–46] |
| S8 | [`preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/build/sections/introduction.tex`](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/build/sections/introduction.tex) | 137 | v3 introduction; the ultraflat theorem [S8:15–25], the Erdös-Problem-26 context [S8:33–40] |
| S9 | [`lean/docs/076.md`](../../../lean/docs/076.md) | 18 | the formalization scope note: the two proven statements and the existential caveat |
| S10 | [`lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.lean`](../../../lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.lean) | 23 | comparator stub (asymptotically minimal): the target with a `sorry` [S10:13–19] |
| S11 | [`lean/ComparatorChallenges/LittlewoodFiniteFlatness.lean`](../../../lean/ComparatorChallenges/LittlewoodFiniteFlatness.lean) | 41 | comparator stub (finite-exponent flatness): the target with a `sorry` [S11:19–35] |
| S12 | [`lean/OAI/Analysis/Littlewood/Model.lean`](../../../lean/OAI/Analysis/Littlewood/Model.lean) | 22 | the OAI statement-1 proposition (asymptotically minimal) [S12:15–18] |
| S13 | [`lean/OAI/Analysis/Littlewood/Main.lean`](../../../lean/OAI/Analysis/Littlewood/Main.lean) | 232 | the OAI statement-1 proved entry point `theorem main` [S13:187–192] |
| S14 | [`lean/OAI/Analysis/Littlewood/FlatnessModel.lean`](../../../lean/OAI/Analysis/Littlewood/FlatnessModel.lean) | 37 | the OAI statement-2 proposition (L^p flatness) [S14:19–31] |
| S15 | [`lean/OAI/Analysis/Littlewood/FiniteFlatness.lean`](../../../lean/OAI/Analysis/Littlewood/FiniteFlatness.lean) | 29 | the OAI statement-2 proved entry point `theorem main` [S15:14–18] |
