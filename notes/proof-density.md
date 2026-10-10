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

Population: 719 source rows, 372 families, **20,341** `\begin{proof}` and **21,288** theorem-like
environments (the declared-`\newtheorem` rule minus the non-statement names; the six-name list gives
21,203). Tiers T3 136 / T2 106 / T1 0 / T0 130. Gates: row count, distinct dirs, family-set equality
with the ledger, per-family row count == ledger `paps`, the two corpus totals, tier counts, positive
`tex_bytes`, non-negative counts, every source dir present under `preprints/`, ledger `paps` sum == 719.
All 0 problems; statistic self-test 5/5; injected mutants caught 9/9.

## Medians by tier

| Signal | T0 | T2 | T3 |
|---|---|---|---|
| proofs per family | 44.0 | 25.0 | 27.0 |
| statements per family | 48.5 | 26.5 | 27.0 |
| proofs per manuscript | 30.0 | 21.2 | 18.0 |
| proofs per statement | 0.965 | 0.962 | 0.973 |
| proofs per tex KB | 0.176 | 0.171 | 0.182 |
| tex KB per manuscript (control) | 168.2 | 118.7 | 89.0 |

The direction is the opposite of the naive reading: the **least-formalized** tier (T0, no scope note)
carries the most proofs per manuscript, because T0 manuscripts are the physically largest.

## Tier separations

The size control is measured at **two scales**: tex KB per family gates the two per-family signals, tex
KB per manuscript gates proofs per manuscript. The report prints both control rows.

| Signal | T0 > T2 | T0 > T3 | T2 > T3 |
|---|---|---|---|
| proofs per family | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.674 / 9.89e-07 → SIZE-EXPLAINED | 0.513 / 7.32e-01 → NULL |
| statements per family | 0.671 / 6.19e-06 → SIZE-EXPLAINED | 0.676 / 6.55e-07 → SIZE-EXPLAINED | 0.513 / 7.29e-01 → NULL |
| proofs per manuscript | 0.709 / 3.41e-08 → SIZE-EXPLAINED | 0.770 / 2.46e-14 → SIZE-EXPLAINED | 0.572 / 5.61e-02 → NULL |
| proofs per statement | 0.485 / 6.94e-01 → NULL | 0.458 / 2.28e-01 → NULL | 0.474 / 4.72e-01 → NULL |
| proofs per tex KB | 0.502 / 9.62e-01 → NULL | 0.467 / 3.59e-01 → NULL | 0.472 / 4.57e-01 → NULL |
| tex KB per manuscript (control) | 0.705 / 5.80e-08 | 0.769 / 3.68e-14 | 0.589 / 1.77e-02 |
| tex KB per family (control) | 0.658 | 0.677 | 0.534 |

Two facts decide it. Raw proof count and raw statement count now clear the bar on **both** T0 pairs
(0.667 / 0.674 and 0.671 / 0.676) and sit within 0.03 of the per-family control (0.658 / 0.677) on each
— a proof count is a **document-length proxy**, not a density. Proofs per manuscript clears the same two
pairs (0.709 / 0.770) and is within 0.03 of the per-manuscript control (0.705 / 0.769). And the two
genuine density measures (proofs per statement, proofs per KB) separate nothing at all: the
proof-to-statement ratio is ≈0.97 across the whole corpus, tier-independent. T2 vs T3 — the two
formalized tiers — is NULL for every signal.

## Claim shapes and ledger flags

No shape clears the bar. The largest effects are the two smallest groups, and both are under-powered:
`conditional` (n=5) at 0.737 / 6.91e-02 and `undecidability` (n=4) at 0.697 / 1.74e-01 on proofs per
family. `partial` per KB is the one shape with a significant p in the right tail — 0.376 / 8.59e-03 —
and it is **inverse**: partial-progress families have *fewer* proofs per KB, which is a statement about
terse writeups, not about proof density.

| Flag | proofs/man | proofs/statement | proofs/KB |
|---|---|---|---|
| `conditional` (n=5) | 0.725 / 8.37e-02 | 0.426 / 5.67e-01 | 0.436 / 6.23e-01 |
| `resolves_named` (n=248) | 0.442 / 6.78e-02 | 0.511 / 7.27e-01 | **0.586 / 6.84e-03** |
| `counterex_broad` (n=74) | **0.356 / 1.22e-04** | 0.489 / 7.68e-01 | 0.572 / 5.60e-02 |

`counterex_broad` is the strongest result in the whole measurement and it is inverse: families that use
counterexample language have markedly **fewer** proofs per manuscript (P(a T0-style family has more
proofs than a counterexample family) = 0.356). The pre-registered bar is one-sided (it asks for the
first group to be higher), so under the rule as written this is not a separation. Recording it as an
inverse association is fair; adding it as a ledger column is not — the ledger already carries
`counterex_broad`, and a column that says "these manuscripts are shorter" restates `tex_bytes`.

`resolves_named` per KB carries the smallest p in the measurement — 0.586 / 6.84e-03 — and it is the one
flag number that moved when the column's scope changed: under the abstract-only scope (n=233) the same
contrast read 0.565 / 0.037. It is an association, not a separation. 0.586 sits 0.064 below the AUC bar,
the flag contrast is not size-controlled, and the bar was written before the data was read, so a p that
clears 0.01 while the AUC does not clear 0.65 is recorded as a null with a direction: flagged families
carry somewhat more proofs per KB than the rest, by less than the measurement asked to call an effect.

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
