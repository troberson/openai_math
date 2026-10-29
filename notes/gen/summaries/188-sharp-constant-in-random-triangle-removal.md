[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 188](../index/combinatorics/188-sharp-constant-in-random-triangle-removal.md)

# 188 — The sharp constant in random triangle removal

[Index page](../index/combinatorics/188-sharp-constant-in-random-triangle-removal.md)

## Original CONTENTS.md summary

The release's blurb [S1:4352] and the catalog abstract [S2:457]
state the family's claim: starting from the complete graph on
$`n`$ vertices, repeatedly delete a uniformly chosen remaining
triangle; the terminal edge count is asymptotic to
$`n^{3/2} / (2\sqrt{2})`$, with mean-square convergence after
normalization by $`n^{3/2}`$. This proves the triangle case of
the Joos–Kühn sharp-constant conjecture. The
manuscript is *The sharp terminal leave in random triangle
removal* [S3:3, S3:5]; its abstract 

> Starting from the complete graph on $`n`$ vertices, repeatedly remove the three
edges of a uniformly chosen remaining triangle. We prove that the number of
edges left at termination, divided by $`n^{3/2}`$, converges in $`L^2`$ to
$`1/(2\sqrt2)`$. This proves the triangle case of the sharp-constant conjecture
of Joos and Kühn. In particular, the same limit holds in probability and
for the normalized expectation. [S3:9–14]

## Undergraduate summary

Start with a **complete graph**: a drawing where every pair
of $`n`$ dots is joined by an edge, so there are
$`\binom{n}{2}`$ of them. Repeatedly pick one of the
remaining **triangles** — three dots all mutually
joined — at random and **erase its three edges**.
Eventually no triangle is left, and some edges survive. The
**terminal leave** is the number of edges left over. The
question is: as $`n`$ grows, how many edges remain? The answer
is a precise constant: about $`1/(2\sqrt{2}) \approx 0.354`$
times $`n^{3/2}`$ — a formula that the proof
**establishes** rather than merely estimates, and whose
convergence is in the strong $`L^2`$ (mean-square) sense
[S3:9–14, S2:457].

## Graduate summary

**The main theorem** [S3:9–14, S4:9]. Let the process
run on $`K_n`$ and let $`G_n`$ be the terminal graph. Then the
normalized leave $`|V(G_n)| / n^{3/2}`$ (the surviving-edge
count divided by $`n^{3/2}`$) converges in $`L^2`$ to
$`1/(2\sqrt{2})`$ [S4:9]. In particular it converges in
probability to the same constant, and the normalized
expectation $`\mathbb{E}(|E(G_n)|)/ n^{3/2}`$ converges to
$`1/(2\sqrt{2})`$ [S4:9]. This is the triangle case of the
sharp terminal-leave conjecture of Joos and Kühn
[S3:9–14].

**The scope of the formalization.** The scope note states
the formalization proves the $`L^2`$ convergence
of the normalized leave to $`1/(2\sqrt{2})`$, and also states
the convergence in probability and the convergence of the
normalized expectation to the same constant
[S4:9]. The scope note names one comparator [S4:15]:
`TriangleRemoval.lean`.

## History of the conjecture

The **random triangle removal** process is a natural
generalization of triangle-free random processes: at each
step a random triangle is deleted. The **terminal-leave
conjecture** of Joos and Kühn asks for the exact sharp
constant governing the number of edges remaining when the
process halts. Prior work gave asymptotic estimates and
upper bounds on the terminal leave, but the precise
$`L^2`$-convergent constant $`1/(2\sqrt{2})`$ — with a
concentration argument strong enough to establish mean-square
convergence — was the missing piece. This manuscript
supplies it, and the proof is a careful tracking of the
process's **suffix** behavior (the tail of the removal
sequence) via a prefix-failure envelope and a
probability-prefix-failure bound
[S3:9–14, S2:457].

**Prior (my training data, not this repo).** I know the
random triangle-removal process and that the
Joos–Kühn terminal-leave conjecture is a named
open problem in probabilistic combinatorics. The specific
**$`L^2`$ convergence to $`1/(2\sqrt{2})`$** — with the
suffix-tracking, prefix-failure-envelope, and
`main_l2_prefix_failure_bound` machinery — is a result I
cannot independently verify from training alone; the 287-file
OAI tree in [S6:79–87] is not something I can recall.

## Consequences

**The triangle case of the Joos–Kühn sharp-constant
conjecture is resolved.** The terminal edge count,
normalized by $`n^{3/2}`$, converges in $`L^2`$ to
$`1/(2\sqrt{2})`$ [S3:9–14, S4:9, S2:457].

**Convergence in probability and in expectation follow.**
The normalized leave converges in probability, and the
normalized expected leave converges, to the same constant
[S4:9].

## Section skeleton

One manuscript [S3:9–14] (title [S3:3], date [S3:5]) —
`paper.tex` (27 lines) under `build/`. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves that the
number of edges at termination, divided by $`n^{3/2}`$,
converges in $`L^2`$ to $`1/(2\sqrt{2})`$. It also states
convergence in probability and convergence of the normalized
expectation to the same constant. This is the triangle case
of the sharp terminal-leave conjecture of Joos and
Kühn [S4:9]. The scope note names one comparator
[S4:15]: `TriangleRemoval.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry for
this family and the manuscript is **not** in its `sources:`
listing. The comparator `TriangleRemoval.lean` restates the
target `theorem sharp_terminal_leave` — a **three-term
conjunction**: the $`L^2`$ convergence, the convergence in
probability for every $`\varepsilon > 0`$, and the
normalized-expectation convergence — with a bare
`sorry` body 

```lean
theorem sharp_terminal_leave :
    Tendsto (fun n => expectation n (fun G =>
      (normalizedLeave n G - sharpConstant) ^ 2)) atTop (𝓝 0) ∧
    (∀ ε : ℝ, 0 < ε →
      Tendsto (fun n => probability n (fun G =>
        ε < |normalizedLeave n G - sharpConstant|)) atTop (𝓝 0)) ∧
    Tendsto (fun n => expectation n (fun G => (G.card : ℝ)) / normalization n)
      atTop (𝓝 sharpConstant) := by
  sorry
```
[S5:55–63]

**What the OAI tree does carry.** The
`OAI/Combinatorics/TriangleRemoval` package (**287 files over
33,800 lines, zero `sorry`**) carries a **real, non-`sorry`**
proof of the comparator's target. The OAI `Main.lean`
splits the three conjuncts into separate theorems:
`sharp_terminal_leave_l2` [S6:36–50] discharges the
$`L^2`$ bound by `uniform_prefix_obligation` and
`main_l2_prefix_failure_bound`;
`sharp_terminal_leave_probability` [S6:52–62]
discharges convergence in probability by
`squeeze_zero` and the Markov square bound
`pmfMean_markov_sq`; `sharp_terminal_leave_expectation`
[S6:64–77] discharges the normalized-expectation
convergence by a `Metric.tendsto_nhds` argument from the
$`L^2`$ bound; and `sharp_terminal_leave` [S6:79–87]
reassembles the three:

```lean
theorem sharp_terminal_leave :
    Tendsto (fun n => expectation n (fun G =>
      (normalizedLeave n G - sharpConstant) ^ 2)) atTop (𝓝 0) ∧
    (∀ ε : ℝ, 0 < ε →
      Tendsto (fun n => probability n (fun G =>
        ε < |normalizedLeave n G - sharpConstant|)) atTop (𝓝 0)) ∧
    Tendsto (fun n => expectation n (fun G => (G.card : ℝ)) / normalization n)
      atTop (𝓝 sharpConstant) :=
  ⟨sharp_terminal_leave_l2,sharp_terminal_leave_probability,sharp_terminal_leave_expectation⟩
```
[S6:79–87]

The proof closes with
`⟨sharp_terminal_leave_l2,
sharp_terminal_leave_probability,
sharp_terminal_leave_expectation⟩` — the
conjunction assembled from the three separately-proved
conjuncts, no `sorry` [S6:79–87].

**Registration, not proof.** The OAI tree proves the
comparator's `sharp_terminal_leave` in full, but the release
registered neither a `main_results` entry nor a `sources:`
listing for it — the gap between the tree and the ledger
is one of **registration**, not of proof. The comparator json
names `OAI.Combinatorics.TriangleRemoval.Main` as the
solution module and `OAI.SharpTerminalLeave.sharp_terminal_leave`
as the theorem, so the release set the target and the tree
answered it; the ledger simply does not carry that answer.
The release records `scope: "Partial progress."` and
`review: status: unchecked`; the comparator's `sorry` is the
target the release set, and the proved `sharp_terminal_leave`
in the OAI tree is the result the tree carries without a
ledger entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 188 at [S1:4352] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{188} at [S2:457] |
| S3 | [`preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/build/paper.tex`](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/build/paper.tex) | 27 | the single manuscript root; title [S3:3], date [S3:5], abstract [S3:9–14] |
| S4 | [`lean/docs/188.md`](../../../lean/docs/188.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:15] |
| S5 | [`lean/ComparatorChallenges/TriangleRemoval.lean`](../../../lean/ComparatorChallenges/TriangleRemoval.lean) | 67 | the comparator: the `sharp_terminal_leave` theorem [S5:55–62] and the `sorry` [S5:63] |
| S6 | [`lean/OAI/Combinatorics/TriangleRemoval/Main.lean`](../../../lean/OAI/Combinatorics/TriangleRemoval/Main.lean) | 93 | the OAI tree (287 files, 33800 lines, 0 sorry): the real proof, split into `sharp_terminal_leave_l2` [S6:36–50], `sharp_terminal_leave_probability` [S6:52–62], and `sharp_terminal_leave_expectation` [S6:64–77], reassembled at `sharp_terminal_leave` [S6:79–87] |
