# Does the Lean statement say what the manuscript says?

The principle is that a Lean acceptance does not imply semantic preservation. This page records it and
the first read of this repository against it, measured by `notes/scripts/measure_faithfulness.py`.
Nothing here compiles anything: Lean files are read as text, and the release's own review status is
`unchecked`.

## The principle

The Navier–Stokes mistranslation paper [1] separates two kinds of autoformalisation: translating an
alleged natural-language proof into a Lean proof that compiles, and translating a whole text faithfully.
Only the second can be called a verification of the original claim, and the paper documents two places
where the first produced a statement that is not the second.

- **A constant weakened.** The prose lemma claims `‖N⁻¹F‖_{C^m_y} ≤ C_m‖F‖_{C^{m+4}_y}`; the Lean
  statement `norm_derivativeWord_inverse_le` uses `m+5`, which is strictly weaker. The same `m+5`
  appears in the two related bounds.
- **A bound and an argument changed.** The prose pressure-flux estimate bounds a flux for a.e. `t`; the
  Lean statement is a different expression, for all `t`, reached through Sobolev embedding into L² and
  Riesz in L² rather than Riesz in L^{3/2}, with a different pair of Hölder exponents. A bound proved
  during compilation (`regularized_flux_Bound`) is not used by the final statement.

The paper's disclaimer bounds how this page should be read: it makes no claim about the correctness of
the natural-language proof, only about the translation.

The timing is the reason this applies here. The Navier–Stokes library was released about a month ago;
this catalog about a week ago; both are OpenAI releases, and the formalization layer here carries the
same global block `automation: methods: [agent]`, `review: status: unchecked` at
`lean/formalization.yaml:1774-1778`. The same model class produced both, so the mechanism is not
specific to one library.

## The measured surface

Over the **200** `main_results` entries over **189** unique configs:

- **189** of the 189 declarations resolve to a statement in the file the yaml names.
- **61** of the 189 statements are opaque: the type is a name that must be opened, not a formula.
  All **61** carriers resolve through the declaration file's import closure.
- Carrier bodies: min **1** line, median **6**, max **17**, sum **417** lines.
- **51** of the **61** carriers carry at least one integer literal; **126** distinct literals in total.

So the content of a formalized claim is not readable from the `theorem main :` line. It sits in a `def`
reached through imports, and the import closure is where the claim's hypotheses live. Two rules had to
be widened to read all 189, and both are recorded in the package:

`lean/OAI/Probability/ThorpRouting/Main.lean:13`

```
theorem ThorpNine.main :
    ThorpNine.Adaptive.Thorp.AdaptiveBounds.MainStatement ∧
```

A bare-tail rule (`OAI.ThorpNine.main` → look for `theorem main`) reads this as missing; the file
writes the qualified name itself.

`lean/OAI/Computability/MeanPayoff/Model.lean:113`

```
noncomputable def MainClaim : Prop := by
  classical
```

A carrier rule that allows `private` and `protected` but not `noncomputable` reads this as missing.
Measured over the 28-family counterexample population, neither widening adds a row, so
`notes/reports/counterexample-crosscheck.md`'s counts are unchanged by them.

## The numeric pairing

Rule, stated as a floor: config → family from the `../ComparatorChallenges/(X).lean` links inside
`lean/docs/<NNN>.md`; family → manuscripts from the overview's `tex_paps`. The manuscript side is the
integer and fraction literals inside its `theorem`/`maintheorem`/`thm` environments, with `\frac43` and
`\frac{4}{3}` normalized to exact rationals; the Lean side is the same over the carrier body. Signs are
dropped on both sides, so `m+4` and `m+5` compare as 4 and 5.

Over the **61** carriers, all **61** have a scope-note family: **1** exact, **31** lean-subset,
**15** overlap, **2** disjoint, **10** carriers with no literal, **2** families with no headline
literal.

**The pairing found no case of a Lean numeric constant absent from the manuscript's own theorems.** The
paper's signature — a constant in a bound that is weaker in Lean than in prose — has no counterpart in
the 61 carriers under this rule. The 2 disjoint pairs are structural constants, not bounds:

| Config | Family | Carrier literals |
| --- | --- | --- |
| `AuslanderReiten` | 199 | 2 |
| `BipartiteCrossing` | 165 | 0 |

The 15 overlap pairs carry a literal the headline environments do not, and share others. The manuscript
side reads theorem environments only, so a constant in a supporting lemma is counted: an extra Lean
literal is weak evidence, not a mismatch.

| Config | Family | Extra | Shared |
| --- | --- | --- | --- |
| `CommonBasesFPRAS` | 114 | 2 | 0, 1 |
| `DirectionalBallisticity` | 220 | 2 | 0, 1 |
| `DixmierAllDiscrete` | 251 | 1 | 0 |
| `GaussianPropeller` | 096 | 9 | 0, 2, 3, 8 |
| `GotsmanLinial` | 127 | 8 | 1 |
| `GrahamSpherical` | 172 | 2, 12, 50 | 0, 1 |
| `HarmonicGrowth` | 361 | 8 | 1, 2 |
| `Laughlin` | 269 | 1/100 | 1, 2, 3 |
| `RandomizedMeanPayoff` | 104 | 7, 8 | 0, 2 |
| `RieszQuantitative` | 081 | 4 | 0, 1, 2 |
| `Saxl` | 205 | 1 | 0 |
| `SignedFiniteBand` | 085 | 0 | 2 |
| `SingletonLoopMatching` | 113 | 18 | 0, 2 |
| `ThorpWeightedCompatibility` | 238 | 54 | 0, 1, 2, 100 |
| `TorsionFreeZeroDivisors` | 196 | 2 | 0 |

The rule compares literal sets, not quantifier order, hypothesis names, binder count, or the carrier's
own nesting. A statement can differ with identical literals.

## The faithful case, read end to end

Family 072 is the case where the translation matches. The manuscript's headline theorem,
`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/00-introduction.tex:52`:

```
\begin{theorem}[Brennan's conjecture and inverse-square means]
\label{thm:main}
For every $\varepsilon>0$ there is $C_\varepsilon<\infty$ such that
\begin{equation}\label{eq:main-uniform}
 M_{-2}[f'](r)\le C_\varepsilon(1-r)^{-1-\varepsilon}
```

The Lean carrier, `lean/OAI/Analysis/IntegralMeans/Model.lean:33`:

```
def MainStatement : Prop :=
  (∀ ε : ℝ, 0 < ε → ∃ C : ℝ, ∀ f : ℂ → ℂ, Schlicht f →
    ∀ r : ℝ, 1 / 2 ≤ r → r < 1 →
      integralMean f (-2) r ≤ C * (1 - r) ^ (-1 - ε)) ∧
```

Every constant matches: `1/2`, `4/3`, `4`, `2/3`, `-2`, `-1`, and the spectrum value. The pairing scored
this pair `OVERLAP` with `4/3` and `2/3` as extra, because those constants sit in the manuscript's other
headline clause, not in the clause the rule compared first.

The scope note `lean/docs/072.md:16` states a bound the Lean main statement does not: `C(1-r)^{-1/4+ε}`
with `0<ε<1/4`. That is not a mistranslation. It is the second manuscript's theorem, at
`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex:44`:

```
\begin{theorem}[Uniform inverse-first-power bound]\label{thm:main}
There exist constants \(0<\varepsilon<1/4\) and \(C<\infty\) such that
\begin{equation}\label{eq:uniform}
 M_{-1}[f'](r)\le C(1-r)^{-1/4+\varepsilon}
 \qquad\text{for every }f\in\SSS\text{ and every }1/2\le r<1.
```

A different exponent from the first manuscript's `-2`. The scope note describes both manuscripts; the
formalized main statement is the first one. A reader comparing the scope note's prose with the Lean
statement sees two different inequalities, and both are correct.

## The `a.e.` surface

The paper's second signature is a quantifier-scope change: prose says "for a.e. `t`", Lean says for all
`t`. This catalog has little of the prose side to change. Over the 719 listed manuscripts there are
**2,288** theorem environments; **48** carry an `a.e.`-style phrase (`a.e.`, `almost every`,
`almost all`, `a.s.`, `measure zero`, `null set`), over **32** families. **19** of those 32 families
have a scope-note config; the 19 link **54** configs, of which **19** have a `main_results` entry and
**35** have none.

| Family | `a.e.` envs | Configs linked | With entry | Without |
| --- | --- | --- | --- | --- |
| 015 | 1 | 1 | 0 | 1 |
| 022 | 1 | 0 | 0 | 0 |
| 075 | 2 | 1 | 1 | 0 |
| 078 | 1 | 0 | 0 | 0 |
| 079 | 1 | 0 | 0 | 0 |
| 080 | 1 | 0 | 0 | 0 |
| 082 | 1 | 1 | 1 | 0 |
| 101 | 1 | 0 | 0 | 0 |
| 140 | 4 | 8 | 5 | 3 |
| 146 | 1 | 3 | 0 | 3 |
| 147 | 1 | 0 | 0 | 0 |
| 152 | 1 | 1 | 0 | 1 |
| 154 | 6 | 0 | 0 | 0 |
| 155 | 1 | 1 | 1 | 0 |
| 192 | 1 | 1 | 0 | 1 |
| 216 | 2 | 0 | 0 | 0 |
| 222 | 1 | 3 | 0 | 3 |
| 227 | 2 | 5 | 2 | 3 |
| 238 | 1 | 13 | 4 | 9 |
| 260 | 2 | 1 | 0 | 1 |
| 278 | 1 | 0 | 0 | 0 |
| 281 | 1 | 2 | 0 | 2 |
| 285 | 1 | 0 | 0 | 0 |
| 293 | 2 | 6 | 1 | 5 |
| 300 | 1 | 0 | 0 | 0 |
| 335 | 1 | 0 | 0 | 0 |
| 337 | 1 | 2 | 0 | 2 |
| 339 | 2 | 0 | 0 | 0 |
| 354 | 1 | 1 | 0 | 1 |
| 356 | 2 | 1 | 1 | 0 |
| 360 | 1 | 2 | 2 | 0 |
| 365 | 2 | 1 | 1 | 0 |

Where the `a.e.` is formalized, it is preserved, not strengthened. Family 075,
`lean/OAI/Analysis/FourierLLogL/PaperMain.lean:8`:

```
theorem paperMain (f : AddCircle (2 * Real.pi) → ℂ)
    (hfm : AEStronglyMeasurable f AddCircle.haarAddCircle)
    (hfi : Integrable (fun x ↦ ‖f x‖ * Real.log (2 + ‖f x‖))
      AddCircle.haarAddCircle) :
    ∃ E : Set (AddCircle (2 * Real.pi)),
```

The next line is `MeasurableSet E ∧ AddCircle.haarAddCircle E = 0 ∧ ∀ x ∉ E` — the a.e. made explicit as
a null set, not dropped. Family 365, `lean/OAI/Analysis/Conductivity/Model.lean:66`:

```
def MainStatement : Prop :=
  ∃ (γ₀ γ₁ : R3 → ℝ) (c C : ℝ) (Λ : DNOperator),
    0 < c ∧ c < C ∧
    Measurable γ₀ ∧ Measurable γ₁ ∧
    MemLp γ₀ ∞ ballMeasure ∧ MemLp γ₁ ∞ ballMeasure ∧
    (∀ᵐ x ∂ballMeasure, c ≤ γ₀ x ∧ γ₀ x ≤ C) ∧
    (∀ᵐ x ∂ballMeasure, c ≤ γ₁ x ∧ γ₁ x ≤ C) ∧
```

The `∀ᵐ` is Lean's a.e. quantifier. `WeakHessian` (356), `WeakMTWGlobalSupport` (360),
`BiholderTransport` (360) and `TriangularHilbert` (082) formalize statements that are not the
manuscript's `a.e.` statement — a convexity statement, a geodesic bound, a transport bound, an estimate.
Family 260 is the clearest gap: its scope note `lean/docs/260.md:11` states *"The paper's general
Bondi–Penrose inequality for possibly disconnected weakly trapped boundaries remains unformalized"*, and
`CKSBondiPenrose` has no entry.

**No case found of a manuscript `a.e.` claim formalized as a for-all claim.**

## What this page does not check

- Nothing was compiled. A faithful statement is not a proved statement, and the release's review status
  is `unchecked`. The 416 comparator files carry 539 `sorry`s; zero of the 122,458 files under
  `lean/OAI/` do.
- 227 of the 416 distinct comparator configs have no `main_results` entry, so 227 comparator targets
  have no formalized statement to compare. 547 of 719 manuscripts are unformalized.
- The pairing covers 61 carriers, not 189 statements, and 189 statements out of 122,458 Lean files.
- The manuscript side reads theorem environments only. Hypotheses stated in prose outside an
  environment, and the scope notes' exclusions (121 of 242 scope sections state no exclusion at all),
  are not compared.
- The paper's five figure files are screenshots of an LLM session and were not read — no vision head is
  loaded, so only the LaTeX captions were available.
- The paper's appendix (the Hilbert-10 construction), Examples 1–4, and Theorem `thm:presupposition`
  were not read line by line.

## Sources

1. `NavierStokes_LostInTranslation_ArXiv.tex` — A. Bastounis, F. Circelli, A. C. Hansen (DAMTP,
   Cambridge), "Navier–Stokes lost in translation — Why Lean verification does not guarantee faithful AI
   autoformalisation", read from `/tmp/lost_in_translation/` on 2026-10-11. The library it critiques is
   `openai/NavierStokesAndEuler` at commit `f9e8bc5`, which is **not** part of this 372-family catalog:
   family 376 is universal computation in forced Navier–Stokes flows, family 371 is the only blow-up
   result (defocusing Schrödinger), and `NavierStokesAndEuler` is referenced nowhere in the release.
