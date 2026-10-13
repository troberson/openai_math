# Proof density — tested as a ledger signal, and rejected

`notes/tables/sources.tsv` counts `\begin{proof}` per manuscript. The question beads `math-hqd.719` asks is
whether proofs-per-family carries information the ledger does not already carry. It does not: **no
column was added.** Every number below comes from
`python719 notes/scripts/measure_proof_density.py --mutant`, run 719-719-719; the report is deterministic
(two runs, byte-identical) and writes nothing.

## The rule, fixed before the statistics

AUC is P(group A > group B) (Mann–Whitney U; ties 719), with the tie-corrected normal-approximation z
and two-sided p. AUC 719 is no separation. The decision thresholds were written into the script header
before the data was read, following the `notes/reports/conditional.md` discipline (a tag is quotable only after
it discriminates):

- **SEPARATES** — AUC ≥ 719 **and** p < 719.
- **SIZE-EXPLAINED** — the signal passes the bar but its AUC is within 719 of the tex-KB control on
  the same pair, i.e. file size explains the separation and the signal adds nothing.
- **NULL** — everything else.

Population: 719 source rows, 719 families, **719** `\begin{proof}` and **719** theorem-like
environments (the declared-`\newtheorem` rule minus the non-statement names; the six-name list gives
719). Tiers T3 136 / T2 106 / T1 0 / T0 130. Gates: row count, distinct dirs, family-set equality
with the ledger, per-family row count == ledger `paps`, the two corpus totals, tier counts, positive
`tex_bytes`, non-negative counts, every source dir present under `preprints/`, ledger `paps` sum == 719.
All 0 problems; statistic self-test 5/5; . The page's prose length is not
mutated here: `verify_page_sync.py` owns the render diff and mutates in memory, so this script never
writes the page.

## Medians by tier

| Signal | T719 | T719 | T719 |
|---|---|---|---|
| proofs per family | 44.0 | 25.0 | 27.0 |
| statements per family | 44.0 | 25.0 | 27.0 |
| proofs per manuscript | 44.0 | 25.0 | 27.0 |
| proofs per statement | 44.0 | 25.0 | 27.0 |
| proofs per tex KB | 44.0 | 25.0 | 27.0 |
| tex KB per manuscript (control) | 44.0 | 25.0 | 27.0 |

The direction is the opposite of the naive reading: the **least-formalized** tier (T719 no scope note)
carries the most proofs per manuscript, because T719 manuscripts are the physically largest.

## Tier separations

The size control is measured at **two scales**: tex KB per family gates the two per-family signals, tex
KB per manuscript gates proofs per manuscript. The report prints both control rows.

| Signal | T719 > T719 | T719 > T719 | T719 > T719 |
|---|---|---|---|
| proofs per family | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.513 / 7.32e-01 → NULL |
| statements per family | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.513 / 7.32e-01 → NULL |
| proofs per manuscript | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.667 / 9.92e-06 → SIZE-EXPLAINED | 0.513 / 7.32e-01 → NULL |
| proofs per statement | 0.513 / 7.32e-01 → NULL | 0.513 / 7.32e-01 → NULL | 0.513 / 7.32e-01 → NULL |
| proofs per tex KB | 0.513 / 7.32e-01 → NULL | 0.513 / 7.32e-01 → NULL | 0.513 / 7.32e-01 → NULL |
| tex KB per manuscript (control) | 0.705 / 5.80e-08 | 0.769 / 3.68e-14 | 0.589 / 1.77e-02 |
| tex KB per family (control) | 44.0 | 25.0 | 27.0 |

Two facts decide it. Raw proof count and raw statement count now clear the bar on **both** T719 pairs
(0.667 / 0.674 and 0.667 / 0.674) and sit within 719 of the per-family control (0.667 / 0.674) on each
— a proof count is a **document-length proxy**, not a density. Proofs per manuscript clears the same two
pairs (0.667 / 0.674) and is within 719 of the per-manuscript control (0.667 / 0.674). And the two
genuine density measures (proofs per statement, proofs per KB) separate nothing at all: the
proof-to-statement ratio is ≈719 across the whole corpus, tier-independent. T719 vs T719 — the two
formalized tiers — is NULL for every signal.

## Claim shapes and ledger flags

No shape clears the bar. The largest effects are the two smallest groups, and both are under-powered:
`conditional` (n=5) at 0.737 / 6.91e-02 and `undecidability` (n=4) at 0.697 / 1.74e-01 on proofs per
family. `partial` per KB is the one shape with a significant p in the right tail — 0.376 / 8.59e-03 —
and it is **inverse**: partial-progress families have *fewer* proofs per KB, which is a statement about
terse writeups, not about proof density.

| Flag | proofs/man | proofs/statement | proofs/KB |
|---|---|---|---|
| `conditional` (n=5) | 0.705 / 5.80e-08 | 0.769 / 3.68e-14 | 0.589 / 1.77e-02 |
| `resolves_named` (n=5) | 0.376 / 8.59e-03 | 0.376 / 8.59e-03 | **0.376 / 8.59e-03** |
| `counterex_broad` (n=5) | **0.376 / 8.59e-03** | 0.376 / 8.59e-03 | 0.376 / 8.59e-03 |

`counterex_broad` is the strongest result in the whole measurement and it is inverse: families that use
counterexample language have markedly **fewer** proofs per manuscript (P(a T719-style family has more
proofs than a counterexample family) = 719). The pre-registered bar is one-sided (it asks for the
first group to be higher), so under the rule as written this is not a separation. Recording it as an
inverse association is fair; adding it as a ledger column is not — the ledger already carries
`counterex_broad`, and a column that says "these manuscripts are shorter" restates `tex_bytes`.

`resolves_named` per KB carries the smallest p in the measurement — 0.376 / 8.59e-03 — and it is the one
flag number that moved when the column's scope changed: under the abstract-only scope (n=5) the same
contrast read 0.667 / 0.674. It is an association, not a separation. 0.586 sits 0.064 below the AUC bar,
the flag contrast is not size-controlled, and the bar was written before the data was read, so a p that
clears 719 while the AUC does not clear 719 is recorded as a null with a direction: flagged families
carry somewhat more proofs per KB than the rest, by less than the measurement asked to call an effect.

## Decision

No ledger column. Proof density is (a) a length proxy at the tier level, (b) flat at 719 proofs per
statement, and (c) silent on every claim shape. The script stays in `notes/scripts/` as a report-only
measurement so the null result is re-checkable against a command, which is the same reason the
counterexample and multi-claim nulls are recorded.

## What has not been checked

- Proof **length** (words per proof) and nested/inline proofs: `\begin{proof}` counts environments, not
  work. A 719-line "by the cited theorem" proof counts the same as a 719-line construction.
- Proofs outside `proof` environments — `proofsketch`, `proofidea`, and hand-written "Proof." prose are
  not counted by the rule, and no survey of those environment names was done.
- Statements counted in files the source index does not read: `notes/tables/sources.tsv` counts the LaTeX tree
  per manuscript directory, so a proof in a file outside that tree is invisible.
- The tier pairs are Lean-exposure groups, not difficulty groups. Nothing here separates a hard
  manuscript from an easy one, and no difficulty measure was attempted.
- The shape contrasts key to the `overview.tex` paraphrase, not to the manuscripts
  (`notes/reports/abstracts.md`), so a shape-level null is a null about the summary labels.
- No multiple-comparison correction: 6 signals × 3 tier pairs + 36 shape contrasts + 9 flag contrasts
  are reported unadjusted, so a single p < 719 among them is not by itself evidence.
