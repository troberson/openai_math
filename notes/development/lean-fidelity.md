# Per-family Lean-fidelity pages: read pass

A side-by-side comparison of the Lean formal statement and the manuscript's theorem
statement, for the family a `main_results` entry names. This is a **reading pass** — it
produces a census, three example comparisons, and a design decision on the page type. It
does not build the generator, checker, or gate row; those are a separate, larger bead.

Two facts scope what any such page can claim, and both are already settled elsewhere:

- A Lean/`comparator` run establishes the **formalized** statement, not the manuscript's
  theorem. It moves a claim from "the release states it" to "a checker accepts this
  translation"; the carrier `Prop` can encode a strictly weaker claim. The release's own
  `review: status: unchecked` is one global block, not per family. So a fidelity page is a
  *comparison*, not a *verification* — it says where the two statements agree or differ, and
  it says nothing about whether the Lean proof elaborates.
- The formalization-faithfulness pass (`measure_faithfulness.py` / `verify_faithfulness.py`)
  carries **regex-rule claims over a read subset**: 61 carrier-typed declarations and 2,288
  theorem environments are read; the other 128 declarations and the 547 unformalized
  manuscripts are not. A green pass says the measured rules hold over the read set.

The consequence: a divergence row on a fidelity page is a **reading judgment**, not a
machine-checkable fact. The checker a fidelity page needs verifies the *citations* (the
carrier body is verbatim from the `.lean` file, the manuscript theorem verbatim from the
`.tex`, the scope note verbatim from the `.md`), not the *judgment*.

## Population

`formalization.yaml` carries 200 `main_results` entries over 189 unique configs. A config's
declaration is resolved in the file the yaml names and its statement classified. Re-measured
this pass with `python3 notes/scripts/measure_faithfulness.py`:

| surface | count |
|---|---|
| `main_results` entries | 200 |
| unique configs | 189 |
| statements resolved | 189 (0 not found) |
| **carrier-typed declarations** | **61** |
| carrier bodies resolved | 61 (0 missing) |
| distinct families | 52 |

Eight families carry **two or more** carrier-typed declarations each (072, 089, 130, 140,
197, 199, 238, 324 — 140 has three, the rest two), so 61 carriers map to 52 families — well
inside the 136 families the 189 configs reach. The maximum population for a fidelity page is the 61; the **minimum** is the subset
whose carrier body is a readable formula. Four carriers are 1-line package combiners that
only *name* sub-`Prop`s and carry no inline formula — 049 `PrincipalPackage :=
PolynomialPackage ∧ FiberPackage`, 119 `FullStatement := CourtadeKumarStatement ∧
DictatorAttainmentStatement`, 130 `ConvGoal := ∃ order solve W, ConvProgram order solve
W ∧ TimeBounds W`, and 241 `MainTheorem := ∀ π : Degree ≃o Degree, ∀ a : Degree, π a = a`.
A page for one of these reads the named sub-`Prop`s, so it is a
deeper import-closure walk, not a one-file read.

The theorem-environment pairing is **not** in the release. The scope note links family →
config → file, and the carrier is named by the Lean source (`DeligneDrinfeld.MainStatement`,
`GaussianPropeller.AllPartitions`), but nothing links a declaration to a specific
`\begin{theorem}`. The pairing below is this pass's read: for each carrier, the manuscript
theorem it formalizes, identified by matching the carrier's hypotheses against the
introduction's `\label{thm:main}`.

## The numeric census is a hint, not a classifier

`measure_faithfulness.py` also does a *numeric pairing*: it collects the integer literals in
each carrier body and the integer and `\frac` literals in the family's headline theorem
environments, and classifies the pair as exact / lean-subset / overlap / disjoint. Re-measured
this pass it reads:

| class | count |
|---|---|
| exact | 1 |
| lean-subset | 31 |
| overlap | 15 |
| disjoint | 2 |
| carrier-no-literal | 10 |
| no-headline-literal | 2 |

The tempting read — "the 2 disjoint configs are the divergences" — is **wrong**. The two
"disjoint" configs are 199 `AuslanderReiten` (carrier literal `{2}`) and 165
`BipartiteCrossing` (carrier literal `{0}`). Family 199 read side by side is a match, not a
divergence:

- **Carrier** `FullStatement` (`OAI/Algebra/AuslanderReiten/Statement.lean:52`): `AlgebraicIndependent
  (ZMod 2) parameters ∧ ∃ s : System, Conclusions K …` where `Conclusions` asserts
  `FiniteDimensional F R ∧ FiniteDimensional F Z ∧ ¬ Module.Projective R Z ∧
  TotallyAcyclicWitness R Z ∧ (∀ i, 0 < i → Subsingleton (Ext i Z Z)) ∧ (∀ i, 0 < i →
  Subsingleton (Ext i Z R)) ∧ Nonempty ((R ⧸ jacobson R) ≃ₐ[F] (Fin 8 → F)) ∧ (jacobson
  R)^4 ≠ ⊥`, plus a field-extension persistence quantifier.
- **Manuscript** `thm:main` (`01-introduction.tex:26`): "Let $\kk=\mathbb F_2(q,H_1,H_2)$ …
  There exist a finite-dimensional $\kk$-algebra $\Lambda$ and a finite-dimensional
  nonprojective left $\Lambda$-module $Z$ such that $\Ext^i_\Lambda(Z,Z)=0=\Ext^i_\Lambda(Z,\Lambda)$
  for every integer $i\ge1$. The module $Z$ is Gorenstein-projective. The semisimple quotient is
  $\Lambda/\rad\Lambda\simeq\kk^8$ … also $\rad(\Lambda)^4\ne0$. These conclusions persist after
  every field extension of $\kk$."

The field (`\mathbb F_2`), the nonprojective module, both `Ext^i` vanishings, the `k^8`
quotient, `rad^4≠0`, and the field-extension persistence all line up. The "disjoint" is a
literal-regex artifact: the manuscript writes `\mathbb F_2`, where the `2` is preceded by `_`,
so the `LIT` pattern (`(?<![\w.])\d+`) skips it, while the carrier's `ZMod 2` counts. The
numeric census flagged 199 as the one config to worry about; it is one of the cleanest matches.

The `overlap` class (a carrier literal the headline lacks) is where a real divergence can
hide, and 113 shows one — see the example below.

## Three example comparisons

The side-by-side format. Each carries the carrier body verbatim (from the `.lean` file), the
manuscript theorem verbatim (from the `.tex`), the per-clause comparison, and the scope note.
The divergence rows are reading judgments; the citations are what a checker would pin.

### 008 — Deligne–Drinfeld (numeric class: exact)

**Lean side** — `MainStatement`, `OAI/Algebra/Drinfeld/RealLie.lean:255` (10 lines):

```lean
def MainStatement : Prop :=
  ∃ (e : OddFree ≃ₗ[ℝ] W) (h : Graded e),
    (∀ a b, (e ⁅a,b⁆ : L) = ihara (e a) (e b)) ∧
    Function.LeftInverse (completedInv e h) (completed e h) ∧
    Function.RightInverse (completedInv e h) (completed e h) ∧
    Continuous (completed e h) ∧ Continuous (completedInv e h) ∧
    (∀ (a b : OddCompletion) n, (e (∑ i ∈ Finset.range (n+1), ⁅(a i), (b (n-i))⁆) : L)
      = ∑ i ∈ Finset.range (n+1), ⁅(a i), (b (n-i))⁆))
```

**Manuscript side** — `thm:main`, `01-introduction.tex:50`: "There are homogeneous elements
$\sigma_{2k+1}\in W_{2k+1}$, one for each $k\ge1$, for which
$\Lie_{\Q}\langle e_3,e_5,e_7,\ldots\rangle\to(W,\{,\})$, $e_{2k+1}\mapsto\sigma_{2k+1}$, is an
isomorphism of graded Lie algebras. In particular, $W$ is closed under the bracket. The induced
map on completions by weight is a continuous graded isomorphism."

**Comparison.**

| clause | Lean | manuscript |
|---|---|---|
| graded Lie isomorphism | `e : OddFree ≃ₗ[ℝ] W`, `ihara (e a) (e b)` | isomorphism of graded Lie algebras | MATCH |
| bracket closure | `e : OddFree ≃ₗ[ℝ] W` (the isomorphism is onto `W`) | "$W$ is closed under the bracket" | MATCH |
| completion continuity | `Continuous (completed e h) ∧ Continuous (completedInv e h)` | "induced map on completions … is a continuous graded isomorphism" | MATCH |

**Scope note** (`lean/docs/008.md`): "The formalization establishes this for the rational
solution space of antisymmetry, the three-term equation, and the four-strand pentagon with the
Ihara bracket. It also gives the corresponding continuous isomorphism after completion by
weight. The regularized-transport proposition and graph-complex consequences are not included."

The exclusions (regularized transport, graph-complex consequences) sit *outside* `thm:main`
and do not touch the carrier. A clean MATCH.

### 096 — Gaussian propeller (numeric class: overlap; reads as MATCH)

**Lean side** — `AllPartitions`, `OAI/Probability/GaussianPropeller/Model.lean:32` (5 lines):

```lean
def AllPartitions : Prop :=
  (∀ (d k : ℕ), 0 < d → 0 < k → ∀ A : Fin k → Set (Space d),
    IsPartition A → value A ≤ 9 / (8 * Real.pi)) ∧
  (∀ (d k : ℕ), 2 ≤ d → 3 ≤ k →
    IsPartition (propeller d k) ∧ value (propeller d k) = 9 / (8 * Real.pi))
```

**Manuscript side** — `thm:main`, `main.tex:81`: "For all positive integers $d$ and $k$, every
measurable partition $(A_1,\ldots,A_k)$ of $\mathbb R^d$ satisfies
$\sum_{i=1}^k\|\int_{A_i}x\,d\gamma_d(x)\|^2\le\frac9{8\pi}$. Empty cells are allowed. The
constant is sharp whenever $d\ge2$ and $k\ge3$: three planar sectors of angle $2\pi/3$,
multiplied by the orthogonal complement of their plane, attain equality, with any further cells
empty."

**Comparison.**

| clause | Lean | manuscript |
|---|---|---|
| universal upper bound | `IsPartition A → value A ≤ 9/(8·π)` for `0 < d`, `0 < k` | "every measurable partition … ≤ 9/(8π)" for positive `d`, `k` | MATCH |
| sharpness / equality case | `value (propeller d k) = 9/(8·π)` for `2 ≤ d`, `3 ≤ k` | "the constant is sharp whenever d≥2 and k≥3 … attain equality" | MATCH |

The numeric census put 096 in `overlap` with an "extra" carrier literal `[9]`. Reading it, the
`9/(8·π)` is the *same* constant the manuscript states — the "extra" is because the manuscript
writes `\frac9{8\pi}` and the headline-literal extractor's `FRAC` pattern (`\frac{4}{3}`-form)
does not parse the `\frac9{8\pi}` brace-mixing the way the Lean `9 / (8 * Real.pi)` does.
Another MATCH, mislabeled by the literal census.

### 113 — Perfect-matchings FPRAS (numeric class: overlap; a real divergence)

**Lean side** — `FullEndpoint`, `OAI/Computability/LoopMatching/Model.lean:68` (10 lines; the
conclusion clause is the load-bearing one):

```lean
def FullEndpoint : Prop :=
  ∃ A : Input → ℕ × ℕ,
    ∃ machine : Turing.TM2ComputableInPolyTime encodeInput encodeOutput A,
      (∀ k, Finite (machine.tm.Γ k)) ∧
      (∃ P : Polynomial ℕ, ∀ G, (encodeOutput (A G)).length ≤ P.eval (encodeInput G).length) ∧
      ∀ G, 0 < (A G).2 ∧
        (A G).1 ≤ (A G).2 * count G ∧
        (A G).2 * count G ≤ 2 ^ (18 * G.n) * (A G).1 ∧
        ((A G).1 = 0 ↔ count G = 0)
```

**Manuscript side** — `thm:main`, `main.tex:132`: "There is a uniform classical randomized
algorithm which, given $G$ and rational parameters $0<\eps<1$ and $0<\delta<1/2$, returns a
nonnegative rational number $\widehat Z$ such that
$\Prb[(1-\eps)Z(G)\le\widehat Z\le(1+\eps)Z(G)]\ge1-\delta$. If $Z(G)=0$, the output is zero
with certainty. The worst-case bit running time is polynomial in the input encoding length,
$\eps^{-1}$, and $\log\delta^{-1}$."

**Comparison.**

| clause | Lean | manuscript |
|---|---|---|
| approximation guarantee | (witness `(A G).1`, `(A G).2` bracket `count G`) | $(1-\eps)Z\le\widehat Z\le(1+\eps)Z$ w.p. $1-\delta$ | PARTIAL — the carrier bakes in a ratio bound with a concrete exponent; the theorem states it as a relative-error probability |
| running time / witness bound | `(A G).2 * count G ≤ 2^(18·n) * (A G).1` | "the worst-case bit running time is **polynomial**" | **DIVERGENCE** — the carrier pins a super-polynomial witness bound (the constant `18`); the theorem and the scope note state only polynomial time, naming no constant |
| zero-matching case | `((A G).1 = 0 ↔ count G = 0)` | "if $Z(G)=0$, the output is zero with certainty" | MATCH |

**The divergence, stated plainly.** The manuscript's theorem is a *qualitative* FPRAS:
polynomial worst-case time, no constant named. The carrier's `FullEndpoint` is *quantitative*:
it fixes a witness bound of $2^{18n}$, a specific exponential in the input size. The `18` is
absent from the manuscript theorem because the theorem does not commit to a running-time
constant. This is the bead's type-(c) divergence — "the Lean changes a constant the preprint
leaves open" — and it is exactly the kind a literal census surfaces (the "extra" literal `[18]`
in the overlap class) and a read must confirm. The scope note (`lean/docs/113.md`) corroborates
the manuscript: it describes "a fully polynomial randomized approximation scheme" with
"relative error at most $\varepsilon$ with probability at least $1-\delta$" and a "fixed
finite-alphabet randomized machine whose worst-case [running time is polynomial]" — no `18`.

This is the non-trivial divergence the read pass was required to produce. It is also evidence
for the general point: the divergence sits in a clause the numeric census only half-flags
(overlap, "extra literal"), and confirming it is a read, not a measurement.

## Design decision on the page type

**New directory?** No. The ownership manifest (`notes/scripts/verify_script_ownership.py`)
owns only fixed note-tree shapes — `notes/index/`, `notes/summaries/`, `notes/data/`, the
template trees, `notes/development/upstream_history/`, `notes/development/probe/`,
`notes/tables/`, files directly under `notes/`, and files directly under `notes/development/`
and `notes/reports/`. A new `notes/fidelity/` directory would be flagged "file under notes/
owned by no rule" and fail the ownership census. A hand-written analysis doc lives in
`notes/development/`, which is where this page sits.

**Template?** Not for the read pass, and not for the generated fleet. A summary page's body is
byte-reproducible from its data file, so a template owns it. A fidelity page's *comparison
table* is a reading judgment — the MATCH/PARTIAL/DIVERGENCE rows are not derivable from the
corpus. The mechanical parts (the carrier body verbatim from the `.lean`, the manuscript
theorem verbatim from the `.tex` through the normalizer, the scope note verbatim from the
`.md`) *can* be rendered from anchors, but the comparison is authored per family. So the page
type is **partially generated**: a template renders the three citation blocks from
`(file, start, end)` anchors, and the comparison table is hand-authored between them. This is
a new shape the summaries pipeline does not serve — its data file is all prose, its checker
compares the page bytes to a full render.

**Checker?** A `verify_fidelity.py` that (a) pins the carrier block against the `.lean` file's
`file:start–end` verbatim, (b) pins the manuscript theorem against the `.tex`'s
`file:start–end` verbatim modulo the normalizer, (c) pins the scope note against the `.md`'s
`## Scope` span, and (d) requires each comparison row to name a clause and a class from a fixed
vocabulary (MATCH / PARTIAL / DIVERGENCE). The checker verifies the citations and the row
shape, not the judgment — the same split the summary checker draws between "the quotation is
verbatim on the line it cites" (checked) and "the reading is sound" (not).

**Gate row?** One plain row running the checker, matching the twenty-three other
page-checker rows in `notes/scripts/gate.py`'s `ROWS`.

**Population.** The 61 carrier-typed declarations is the maximum. The practical first cut is
the readable-body subset: everything except the four 1-line package combiners (049, 119, 130,
241) that need a deeper import-closure walk. That is 57 carriers over 49 families — the three
families whose only carrier is a combiner (049, 119, 241) drop out, while 130 keeps its second,
readable carrier.

## What this pass did not check

- The 84 families with a `main_results` config but **no** carrier-typed declaration (their
  configs resolve to opaque `theorem main : MainStatement :=` bodies with no readable carrier —
  136 families carry a config, 52 carry a carrier) have no fidelity page in this pass. They are
  the larger, harder population: a page for one would have to open the named `MainStatement`
  through the import closure and is not covered here.
- The theorem-environment pairing is this pass's read for the three example families; the
  remaining 58 carriers are not individually paired.
- No divergence taxonomy was applied fleet-wide. The four types (Lean stronger / weaker /
  different constant / narrower-than-theorem) are demonstrated, not census'd.
- No generator, checker, or gate row was built. The design decision above is the stopping point
  of this bead; the implementation is a separate, larger bead.

## Sources

1. `notes/scripts/measure_faithfulness.py` — the declaration-surface and numeric-pairing
   measurement; the census figures in this page are its report.
2. `lean/formalization.yaml` — the `main_results` entries (200 over 189 configs).
3. `OAI/Algebra/Drinfeld/RealLie.lean:255` — the 008 `MainStatement` carrier.
4. `preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/build/sections/01-introduction.tex:50`
   — the 008 `thm:main`.
5. `lean/OAI/Probability/GaussianPropeller/Model.lean:32` — the 096 `AllPartitions` carrier.
6. `preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/main.tex:81`
   — the 096 `thm:main`.
7. `OAI/Computability/LoopMatching/Model.lean:68` — the 113 `FullEndpoint` carrier.
8. `preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/build/main.tex:132`
   — the 113 `thm:main`.
9. `lean/docs/008.md`, `lean/docs/096.md`, `lean/docs/113.md`, `lean/docs/199.md` — the scope
   notes quoted above.
10. `OAI/Algebra/AuslanderReiten/Statement.lean:52` — the 199 `FullStatement` carrier.
11. `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/01-introduction.tex:26`
    — the 199 `thm:main`.
12. `notes/scripts/verify_script_ownership.py` — the ownership manifest the new-directory
    design decision is checked against.
