[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 301](../index/operator-algebras/301-classification-by-trace-cones-after-razak-jacelon-stabilization.md)

# 301 — Classification by trace cones after Razak–Jacelon stabilization

[Index page](../index/operator-algebras/301-classification-by-trace-cones-after-razak-jacelon-stabilization.md)

## Original CONTENTS.md summary

[S1:7464] (family entry):

> **301. Trace cones and Razak–Jacelon stabilization.** Classifies separable nuclear complex *C*∗-algebras after tensoring with the Razak–Jacelon algebra and the compact operators, using their full topological cones of extended lower-semicontinuous tracial weights. This answers Robert's trace-cone question, including algebras with arbitrary ideal structure and both finite and infinite subquotients. ([Lean](../../../lean/docs/301.md))

[S2:696] carries the `\resultentry` with the single manuscript [S3:3, S3:5]. The abstract 

> We prove that the canonical topological cone of all extended
lower-semicontinuous tracial weights determines a separable nuclear
$`C^*`$-algebra after tensoring with the Razak–Jacelon algebra and the
compact operators, answering Robert's trace-cone classification question
positively. The isomorphism realizes the prescribed cone map, with
arbitrary ideal structure and without a density assumption on the finite
domains of the weights. [S3:9–17]

## Undergraduate summary

A **trace** on a $`C^*`$-algebra is a positive linear functional that is
"central" in the sense that $`\tau(ab) = \tau(ba)`$. The collection of all
such traces (allowing infinite values — the **extended** tracial weights)
forms a cone, and that **trace cone** is one of the main invariants used
to classify $`C^*`$-algebras.

The **Razak–Jacelon algebra** $`\mathcal{W}`$ is a special, nonseparable
$`C^*`$-algebra that acts as a "separability absorber": tensoring a
separable algebra $`A`$ with $`\mathcal{W}`$ (and the compact operators
$`\mathcal{K}`$) produces an algebra that is easier to classify than $`A`$
itself.

**Robert's trace-cone question** asked: after this stabilization, does the
trace cone *determine* the algebra? In other words, if two separable
nuclear algebras $`A`$ and $`B`$ have isomorphic trace cones, are
$`A \otimes \mathcal{W} \otimes \mathcal{K}`$ and
$`B \otimes \mathcal{W} \otimes \mathcal{K}`$ isomorphic? The answer is
**yes** [S3:9–17], and the isomorphism exists even for algebras with
arbitrary ideal structure — no density assumption on the finite domains
of the weights is needed.

## Graduate summary

**Main theorem** [S3:9–17, S2:696].
Let $`A`$ and $`B`$ be separable nuclear complex $`C^*`$-algebras. A
topological isomorphism between their canonical cones of extended
lower-semicontinuous tracial weights induces an isomorphism
$`A \otimes \mathcal{W} \otimes \mathcal{K} \cong B \otimes \mathcal{W}
\otimes \mathcal{K}`$ that realizes the prescribed cone map. The result
holds for algebras with arbitrary ideal structure and without a density
assumption on the finite domains of the weights [S3:9–17]. This answers
Robert's trace-cone classification question positively.

**The ideal-transport ingredient.** The classification rests on a
supporting result in Section 2: a trace-cone equivalence induces an
*order isomorphism of closed two-sided ideals*, carrying the ideals
determined by finiteness and vanishing of each trace to those of its
image. Each closed ideal $`I`$ determines a trace — zero on positive
elements of $`I`$ and infinite elsewhere — and these traces are exactly the
**additive idempotents** ($`\tau + \tau = \tau`$), whose addition recovers
ideal inclusion [S4:9, S4:11].

**Scope boundary.** The formalization proves this ideal-transport result
and its supporting closure and lower-semicontinuity properties
[S4:9, S4:13], but it does **not** establish the paper's main
isomorphism conclusion — the existence of the stabilization models, norm
uniqueness, and the final intertwining are all outside the formalized
statement [S4:15].

## History of the conjecture

Robert's trace-cone question sits in the classification program for
nuclear $`C^*`$-algebras. The trace cone (with its natural order and
topology) has long been one of the central invariants, and the Razak–
Jacelon algebra $`\mathcal{W}`$ was introduced precisely to produce a
well-behaved stabilized object from a separable algebra. The question
asked whether, after stabilization by $`\mathcal{W} \otimes \mathcal{K}`$,
the trace cone becomes a complete invariant.

The answer here [S3:9–17] is affirmative, with two features that extend
the classical picture: (i) arbitrary ideal structure is allowed — the
algebra need not be simple or have a prescribed lattice of ideals; and
(ii) no density assumption is needed on the finite domains of the
traces. The ideal-transport lemma [S4:9] is the piece that lets the cone
map be promoted to an actual algebra isomorphism, by controlling how the
ideal lattice behaves under the trace-cone equivalence.

**Prior (my training data, not this repo).** The Razak–Jacelon algebra
and the question of whether the trace cone classifies after
stabilization are both within the scope of the literature (Robert,
Rørdam, and related classification work). The positive answer with
arbitrary ideal structure and no density assumption, and the
ideal-transport mechanism, are the novel contributions claimed here;
I cannot verify the classification-theoretic arguments independently
from training alone.

## Consequences

- **Robert's trace-cone question is answered positively** [S3:9–17,
  S2:696]: a separable nuclear $`C^*`$-algebra is determined, after
  tensoring with the Razak–Jacelon algebra and the compact operators, by
  its cone of extended lower-semicontinuous tracial weights. This is the
  named resolution the ledger's `resolves_named` flag records.
- **Arbitrary ideal structure is allowed** [S3:14–15, S2:696]: the
  classification holds with both finite and infinite subquotients,
  without assuming a prescribed ideal lattice.
- **No density assumption on the finite domains** [S3:15–17]: the
  isomorphism exists even when the finite domains of the traces are not
  dense, removing a technical hypothesis present in prior formulations.
- **Trace-cone equivalence controls the ideal lattice** [S4:9, S4:11]:
  a trace-cone equivalence induces an order isomorphism of closed
  two-sided ideals, and the ideal-determined traces are exactly the
  additive idempotents.

## Section skeleton

One manuscript [S3:9–17]. Root `build/paper.tex` (36 lines), abstract in the
root [S3:9–17]. Sections under `build/sections/`: `01-introduction`,
`02-structure`, `03-sequence-models`, `04-small-stabilizers`,
`05-uniqueness`, `06-tracial-cone`, `07-cone-correction`,
`08-point-intertwining`, plus a `preamble.tex` and a `figures/`
directory. No verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note [S4],
one comparator stub [S5], one `main_results` config
(`ComparatorChallenges/TraceIdealTransportSupport.json`) carrying
**three** declarations, and a proved OAI tree. The ledger's `mainres=1`
counts the single config; the three declarations under it are
`OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_finIdeal` and
`OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_zeroIdeal`
(both in `OAI/Analysis/TraceCone/IdealTransport.lean`) and
`OAI.TraceConeClassification.closed_ideal_weight_exists` (in
`OAI/Analysis/TraceCone/FiniteIdeal.lean`).

The scope note describes the formalized content in three positive
paragraphs — the ideal-transport result [S4:9], the ideal-determined
traces as additive idempotents [S4:11], and the ideal/closure and
lower-semicontinuity properties [S4:13] — and then states the exclusion
explicitly: the main isomorphism conclusion [S4:15] is **not**
established by the formalization.

The single comparator stub carries 17 `sorry`:
`TraceIdealTransportSupport.lean` (237 lines) with
`theorem closed_ideal_weight_exists` at [S5:61]. The proved copies of
the three `main_results` declarations live under
`lean/OAI/Analysis/TraceCone/` — an 11-file tree with 0 `sorry` — where
`FiniteIdeal.lean` carries `closed_ideal_weight_exists` [S6] and
`IdealTransport.lean` carries `idealOrderIso_finIdeal` and
`idealOrderIso_zeroIdeal` [S6]. The gap is the paper's main
classification conclusion, which the scope note [S4:15] places outside
the formalized statement. The reading is of source text only.

**Tree measurement (source-level).**

The `main_results` entry OAI.TraceConeClassification.closed_ideal_weight_exists resolves to `OAI/Analysis/TraceCone/FiniteIdeal.lean` (388 lines); the top-level theorem is `theorem closed_ideal_hereditary`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 11 files with 26 theorems and 70 defs.

The preprint states 45 theorem environments while the tree carries only 26 (0.58×), indicating a focused sub-formalization (source-level).

## Coverage

The ledger row `fam=301` [S6] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=1517`, `verification=0`, `trace=`. The T3
shape is "scope note, comparators, `main_results`, and a proved OAI tree
exist." The `main_results` config carries three declarations, all proved
in the 11-file OAI tree under `lean/OAI/Analysis/TraceCone/` (0
`sorry`); the single comparator stub carries 17 `sorry`. The formalized
content is the ideal-transport supporting result, not the paper's main
isomorphism [S4:15]. The shape flags are `shapes=resolution|uniform`,
`resolves_named=1` — a resolution family recording Robert's trace-cone
question, with the formalization covering its supporting lemma.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7464] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 301 at [S2:696] |
| S3 | [`preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/build/paper.tex`](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/build/paper.tex) | 36 | manuscript (root); title [S3:3], date [S3:5], abstract [S3:9–17] |
| S4 | [`lean/docs/301.md`](../../../lean/docs/301.md) | 21 | scope note — Scope at [S4:9, S4:11, S4:13, S4:15] and the comparator link `TraceIdealTransportSupport.lean` |
| S5 | [`lean/ComparatorChallenges/TraceIdealTransportSupport.lean`](../../../lean/ComparatorChallenges/TraceIdealTransportSupport.lean) | 237 | comparator stub (formalized target) — 237 lines, 17 `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=301`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
