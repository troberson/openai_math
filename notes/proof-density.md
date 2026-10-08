# Proof density — tested as a ledger signal, and rejected

`notes/sources.tsv` counts `\begin{proof}` per manuscript. The question beads `math-hqd.3` asks is
whether proofs-per-family carries information the ledger does not already carry. It does not: **no
column was added.** Every number below comes from
`python3 notes/scripts/measure_proof_density.py --mutant`, run 2026-10-08; the report is deterministic
(two runs, byte-identical) and writes nothing.

## The rule, fixed before the statistics

AUC is P(group A > group B) (Mann–Whitney U; ties 0.5), with the tie-corrected normal-approximation z
and two-sided p. AUC 0.5 is no separation. The decision thresholds were written into the script header
before the data was read, following the `notes/conditional.md` discipline (a tag is quotable only after
it discriminates):

- **SEPARATES** — AUC ≥ 0.65 **and** p < 0.01.
- **SIZE-EXPLAINED** — the signal passes the bar but its AUC is within 0.03 of the tex-KB control on
  the same pair, i.e. file size explains the separation and the signal adds nothing.
- **NULL** — everything else.

Population: 722 source rows, 372 families, **20,449** `\begin{proof}` and **21,402** theorem-like
environments (the declared-`\newtheorem` rule minus the non-statement names; the six-name list gives
21,317). Tiers T3 127 / T2 108 / T1 0 / T0 137. Gates: row count, distinct dirs, family-set equality
with the ledger, per-family row count == ledger `paps`, the two corpus totals, tier counts, positive
`tex_bytes`, non-negative counts, every source dir present under `preprints/`, ledger `paps` sum == 722.
All 0 problems; statistic self-test 5/5; injected mutants caught 8/8.

## Medians by tier

| Signal | T0 | T2 | T3 |
|---|---|---|---|
| proofs per family | 44.0 | 25.5 | 26.0 |
| statements per family | 48.0 | 27.0 | 27.0 |
| proofs per manuscript | 30.0 | 21.4 | 17.0 |
| proofs per statement | 0.966 | 0.962 | 0.974 |
| proofs per tex KB | 0.175 | 0.171 | 0.183 |
| tex KB per manuscript (control) | 168.9 | 120.6 | 86.0 |

The direction is the opposite of the naive reading: the **least-formalized** tier (T0, no scope note)
carries the most proofs per manuscript, because T0 manuscripts are the physically largest.

## Tier separations

| Signal | T0 > T2 | T0 > T3 | T2 > T3 |
|---|---|---|---|
| proofs per family | 0.647 / 8.3e-05 → NULL | 0.676 / 7.9e-07 → SIZE-EXPLAINED | 0.530 / 0.44 → NULL |
| statements per family | 0.650 / 5.6e-05 → NULL | 0.678 / 5.8e-07 → SIZE-EXPLAINED | 0.529 / 0.44 → NULL |
| proofs per manuscript | 0.697 / 1.1e-07 → SIZE-EXPLAINED | 0.782 / 2.2e-15 → SIZE-EXPLAINED | 0.594 / 0.013 → NULL |
| proofs per statement | 0.491 / 0.81 → NULL | 0.456 / 0.21 → NULL | 0.466 / 0.37 → NULL |
| proofs per tex KB | 0.503 / 0.93 → NULL | 0.453 / 0.19 → NULL | 0.457 / 0.26 → NULL |
| tex KB per manuscript (control) | 0.691 / 2.9e-07 | 0.784 / 1.4e-15 | 0.615 / 0.0023 |

Two facts decide it. Raw proof count and raw statement count track the size control to within 0.03
wherever they clear the bar — a proof count is a **document-length proxy**, not a density. And the two
genuine density measures (proofs per statement, proofs per KB) separate nothing at all: the
proof-to-statement ratio is ≈0.97 across the whole corpus, tier-independent. T2 vs T3 — the two
formalized tiers — is NULL for every signal.

## Claim shapes and ledger flags

No shape clears the bar. The largest effects are the two smallest groups, and both are under-powered:
`conditional` (n=5) at 0.736 / 0.070 and `undecidability` (n=4) at 0.697 / 0.18 on proofs per family.
`partial` per KB is the one shape with a significant p in the right tail — 0.375 / 0.0082 — and it is
**inverse**: partial-progress families have *fewer* proofs per KB, which is a statement about terse
writeups, not about proof density.

| Flag | proofs/man | proofs/statement | proofs/KB |
|---|---|---|---|
| `conditional` (n=5) | 0.726 / 0.083 | 0.426 / 0.57 | 0.436 / 0.62 |
| `resolves_named` (n=233) | 0.465 / 0.27 | 0.513 / 0.66 | 0.565 / 0.037 |
| `counterex_broad` (n=74) | **0.356 / 1.3e-04** | 0.489 / 0.77 | 0.571 / 0.059 |

`counterex_broad` is the strongest result in the whole measurement and it is inverse: families that use
counterexample language have markedly **fewer** proofs per manuscript (P(a T0-style family has more
proofs than a counterexample family) = 0.356). The pre-registered bar is one-sided (it asks for the
first group to be higher), so under the rule as written this is not a separation. Recording it as an
inverse association is fair; adding it as a ledger column is not — the ledger already carries
`counterex_broad`, and a column that says "these manuscripts are shorter" restates `tex_bytes`.

## Decision

No ledger column. Proof density is (a) a length proxy at the tier level, (b) flat at 0.97 proofs per
statement, and (c) silent on every claim shape. The script stays in `notes/scripts/` as a report-only
measurement so the null result is re-checkable against a command, which is the same reason the
counterexample and multi-claim nulls are recorded.

## What has not been checked

- Proof **length** (words per proof) and nested/inline proofs: `\begin{proof}` counts environments, not
  work. A 2-line "by the cited theorem" proof counts the same as a 40-line construction.
- Proofs outside `proof` environments — `proofsketch`, `proofidea`, and hand-written "Proof." prose are
  not counted by the rule, and no survey of those environment names was done.
- Statements counted in files the source index does not read: `notes/sources.tsv` counts the LaTeX tree
  per manuscript directory, so a proof in a file outside that tree is invisible.
- The tier pairs are Lean-exposure groups, not difficulty groups. Nothing here separates a hard
  manuscript from an easy one, and no difficulty measure was attempted.
- The shape contrasts key to the `overview.tex` paraphrase, not to the manuscripts
  (`notes/abstracts.md`), so a shape-level null is a null about the summary labels.
- No multiple-comparison correction: 6 signals × 3 tier pairs + 36 shape contrasts + 9 flag contrasts
  are reported unadjusted, so a single p < 0.01 among them is not by itself evidence.
