# Proof-level faithfulness audits

Per-family pages in this directory (`<NNN>.md`) compare a preprint's proof with its Lean
formalization. The statement-level comparison (hypotheses, conclusion, quantifier order) is
family-specific. The *proof-level* comparison — does the 20,000-line Lean DAG mirror the
preprint's argument, or is it a valid but different proof of the same theorem? — follows the
shared protocol below.

## The problem

The "lost in translation" paper (arXiv 2610.08144) demonstrates that a compiling Lean proof
does not guarantee a semantically faithful translation of the natural-language proof. Three
concrete failure modes, drawn from OpenAI's own Navier-Stokes formalization:

- **§3.1 — Extra hypothesis.** The NL paper declares a stronger statement (fewer assumptions)
  than the Lean proves. The Lean's proof compiles because the extra hypothesis makes the
  theorem easier, but the formalized claim is strictly weaker.
- **§3.2 — Both statement and proof mistranslated.** The Lean proves the same statement but
  by a *different* argument. A step the preprint uses (a specific inequality, a specific
  decomposition) is replaced by a structurally different one that happens to close the gap.
- **§3.4 — The iterative loop.** The autoformalization pipeline is `while no proof compiles:
  revise`. The 20,000 intermediate lines were likely generated to make the proof compile, not
  to mirror the preprint's structure. They are *a* valid path to the theorem, not *the*
  preprint's path.

The Lean kernel guarantees every inference edge in the dependency DAG is valid. It does **not**
guarantee that the DAG is isomorphic to the preprint's argument.

## Audit protocol

For each family, identify the points where the preprint makes **specific quantitative claims**
about its proof — the exact form of a remainder, the number of applications of a named
inequality, the precise hypothesis set, the limit order. These are the locations where a
§3.1 or §3.2 divergence would be most likely to hide, because the Lean could silently weaken
or substitute without the final theorem failing to compile.

### Step 1: Extract the preprint's quantitative claims

Read the proof-strategy section (and any "two Cauchy–Schwarz close the argument" or "the
remainder is a sum of explicit squares" sentences) and record:

1. **Hypothesis set** — which assumptions does the proof require? (e.g., "global upper Hessian
   bound, no global lower bound")
2. **Key decomposition** — what is the structure of the critical identity? (e.g., "remainder
   is a sum of squares")
3. **Named inequalities** — how many, which ones? (e.g., "two Cauchy–Schwarz")
4. **Parameter constraints** — what are the restrictions on free parameters? (e.g., "q ≥ 2
   even, ε > 0")
5. **Limit structure** — what is the order of limits taken? (e.g., "q→∞ first, then ε→0")
6. **Coordinate transform** — what is the change of variables, and what are the source/target
   measures?
7. **Exponents and constants** — what are the specific numerical exponents, derivative orders,
   Hölder conjugates, and multiplicative constants in the bounds? (e.g., "the weight has power
   q", "the Sobolev embedding loses one derivative", "the Riesz transform acts on L^{3/2}")

### Step 2: Locate each claim in the Lean

For each claim, find the Lean definition/lemma/hypothesis that carries it. Check:

- Does the Lean carry **exactly** the stated hypothesis, or a stronger one (extra assumption)?
- Is the decomposition literally of the stated form, or a different valid decomposition?
- Are there exactly the stated number of named-inequality applications, or more/fewer?
- Do the parameter constraints match, or is the Lean more/less restrictive?
- Is the limit order the same, or joint?
- Is the transport map the same?
- Do the **exponents, derivative orders, and constants** match? The "lost in
  translation" paper's smallest divergences are here: a derivative order shifted by a
  fixed amount (NL uses `m`, Lean uses `m+5`), a Hölder conjugate changed, an operator
  substituted (Riesz transform on L^{3/2} replaced by Sobolev embedding to L²), an extra
  quantity carried in the bound that the NL paper bounds away. Check the *numerical* value,
  not the shape.
- Is a shifted/exponent-offset parameter a **reparameterization** or a **divergence**? A
  shift is a reparameterization iff (a) the *range* of the value is identical, (b) the *limit*
  is identical, and (c) no other lemma in the proof reads the pre-shift symbol. Verify all
  three: an offset that changes the set of admissible values, or that is applied
  inconsistently (one lemma uses `q`, another uses `q+2`), is a divergence, not a cosmetic
  shift. (Example: a weight power written `q` in the NL and `q+2` in Lean, where `q+2`
  ranges over exactly the same set and no lemma mixes the two, is a reparameterization.)

### Step 3: Classify each target

| Classification | Meaning |
|---|---|
| **Match** | Lean carries the same structure *and* the same numerical values the preprint names |
| **Reparameterization** | A shifted parameter (exponent, derivative order) that ranges over the same set with the same limit; the mathematics is unchanged |
| **§3.1 divergence** | Lean carries an extra hypothesis the preprint does not |
| **§3.2 divergence** | Lean uses a different argument at this point |
| **Not formalized** | The preprint's claim has no Lean counterpart (coverage gap) |
| **Weaker** | Lean proves a specialization the preprint does not claim |

The **sign audit** is a separate pass, run only on families whose intermediate quantities are
convention-dependent (orientation, winding, signed trace, intersection number, Euler
characteristic). The distinguishing feature is whether the quantity is *structurally
non-negative* — a variance, a norm, a PSD trace, a quadratic form in a PSD matrix. For those,
a sign flip makes the quantity negative, violating a `nonneg`/`PosSemidef` hypothesis, and the
proof **fails to compile**: the Lean kernel is the sign checker, and the family is safe-class.
For convention-dependent quantities a sign flip is invisible to the type system (the proof
compiles, the statement is correct, one constant is flipped) — the audit that caught a
withdrawing sign error in a released family — and the sign must be checked against the
preprint's convention line by line. Grep the closure for the safe markers (`PosDef`,
`PosSemidef`, `nonneg`, `sq_nonneg`, `norm`) and the vulnerable ones (`orientation`, `winding`,
`signed`, `Euler`, `intersection`, `degree`); a family can carry both classes.

### Step 4: Record in the family page

The family page carries a `## proof-level faithfulness` section with one subsection per audit
target, each carrying:
- The preprint quote (with `[S#:line]` anchor)
- The Lean quote (with `[S#:line]` anchor)
- The classification (Match / §3.1 / §3.2 / Not formalized / Weaker)

A summary table at the end of the section lists all targets with their verdicts.

## What the audit does and does not prove

**Proves:** The structural skeleton of the Lean proof matches the preprint's argument at the
identified decision points. No extra hypotheses, no substituted inequalities, no different
remainder form.

**Does not prove:** That every individual algebraic identity in the intermediate infrastructure
(lines between the audit targets) is *the* identity the preprint would have written. The
intermediate lemmas formalize cited black boxes (e.g., Berman–Berndtsson, Klartag) that the
preprint invokes by reference; their internal structure is a valid formal development of those
references, and line-by-line isomorphism with a hypothetical "the preprint's internal proof of
Berman–Berndtsson" is neither required nor checkable (the preprint does not contain it).

**Residual risk:** A §3.4 divergence that changes only the *order* of intermediate lemmas
(without changing hypotheses, decomposition form, or inequality count) is undetectable by this
protocol. This is the weakest form of "different valid argument" and has no mathematical
consequence — the theorem is the same, the proof is valid, only the presentation order
differs.

## Partial verdicts

Ten of the 114 proof pages carry a **Partial** verdict — the Lean carrier
proves a genuine sub-statement (zero sorry), but the manuscript's headline
claim is strictly stronger, or the comparison is incomplete for a structural
reason. These are the cases the protocol exists to surface: the formalization
is correct and complete for what it states, and the stated statement is a
proper subclaim of the preprint's headline theorem, or the comparator stub
has not been resolved into a proved entry.

The two most instructive cases, where the Lean proves a real sub-theorem
that is *not* what the title advertises:

- **Family 195** — The Lean carrier `candidate_ring_properties` proves the
  candidate ring's structure (Noetherian, a domain, finite-dimensional over the
  base field) but does **not** prove the "no small Cohen–Macaulay module" claim
  that is the manuscript's headline. The Lean builds the object; it does not
  prove the property the title advertises.
- **Family 210** — The Lean carrier `canonical_foulkes_howe_surjective` proves
  the averaged Foulkes–Howe surjectivity in the range $a \ge 2$,
  $b \ge a(a{-}1)$. For the sixth-power case ($a = 6$) this gives
  $b \ge 30$, not the manuscript's full $b \ge 6$. The scope note records the
  gap verbatim: "the companion's full range $b \ge 6$ is not included."

The remaining eight Partials (087, 140, 157, 174, 179, 185, 290, 301) are
comparator-coverage gaps: the comparator stub is present but the `main_results`
entry has not been resolved into a proved declaration under `lean/OAI/`, so the
proof-level comparison cannot be completed.

The full distribution over the 114 proof pages: **65 Match**, **10 Partial**,
**11 Not formalized** (the Lean covers no part of the preprint's proof), and
**28 statement-only** files that carry a sign audit or a statement-level
comparison without a top-level verdict line.

## Scope

This protocol applies to T3 families (those with a `main_results` entry resolving to a file
under `lean/OAI/`). For T2 families (scope note + comparator stub, no proved entry), the
comparison is statement-only. For T0/T1 families, there is no Lean to compare.
