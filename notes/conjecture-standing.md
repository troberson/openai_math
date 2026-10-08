# Conjecture standing for the 139 named-conjecture resolution families

Written 2026-10-07 as the record for `notes/conjecture-standing.tsv`. The table's `standing_prior_2025`
column is **the assistant's training-data prior, not a literature survey**: what a working
mathematician's memory, frozen at the release's pre-announcement cutoff, says about each conjecture's
standing. Nothing in that column was read from this repo, and nothing in it has been checked against
the literature. The repo supplies only the claim (`release_claim`) and the citation
(`abstract_line`). No `lake`, `lean`, or comparator run.

## The selection: 139, not 248

`resolves_named = 1` marks **248** families (T0 91, T2 62, T3 95); the abstract-only scope it
replaced marked 233 (T0 88, T2 57, T3 88). Intersecting it with the
`resolution` shape tag leaves **139** (T0 51, T2 36, T3 52), and the table carries exactly those 139 —
none of the 15 title-scope additions carries the `resolution` shape, so the intersection did not move.

Recorded ambiguity, with the provisional choice and its revisit condition: `math-el4.6`'s spec quotes
the 233-family tier split (88/57/88) while naming 139 rows. Provisional choice: build the
intersection, because the intersection is the set whose abstracts both name a target and claim a
resolution — a "standing" row for a family whose headline is a bound, not a resolution, would compare
the prior against a claim the abstract does not make. Revisit condition: if the 109
`resolves_named`-only families are wanted, the table extends by adding rows whose `release_claim`
comes from a bound/classification headline; that is a second table with a different `gap` semantics,
not a widening of this one.

## Columns

```
fam  discipline  tier  conjecture  standing_prior_2025  prior_confidence
release_claim  gap  surprise_tier  abstract_line
```

Pure TSV, header line, no comments — parse with `csv.DictReader(..., delimiter='\t')`. `discipline`
and `tier` are copied from `notes/catalog.tsv`, not judged. Naming the standing column
`standing_prior_2025` is the structural labelling: the number is never presented as the conjecture's
status, only as the prior's account of it.

`abstract_line` is `overview.tex:<n>`, the line of the family's own `\resultentry`. Each family is one
source line and each abstract is single-line, so the anchor is exact, not approximate: the checker
resolves all 139 anchors to the family's own entry.

## Surprise tiers

Surprise is `claim − prior`, so the tier records the *relation*, not a difficulty ranking:

| tier | meaning | count |
|---|---|---|
| 1 | the prior says not-yet-possible | 60 |
| 2 | famous, plausible-unachieved | 64 |
| 3 | the prior deflates the headline — largely known already | 11 |
| 4 | niche — the prior cannot judge | 4 |

Tier 3 is the deflation set: **032, 074, 075, 113, 118, 147, 174, 175, 184, 188, 204**. Five of them
name a result the prior already holds as a theorem — 174 (Cymerman–Ram 2021, strong thin trees), 175
(Park 2022, Talagrand's expectation-threshold conjecture), 184 (the AEKS independence half is a 1982
theorem), 188 (Isaak 2016–17, triangle-removal terminal density), 204 (Belkale–Kumar 2011, saturation
constant 1 for types B, C, D). Tier 4 is **027, 136, 187, 301** — problems the prior cannot place, so
no surprise value is recorded for them at all.

`prior_confidence` is a three-value vocabulary: **high 42, medium 84, low 13**. It is the load-bearing
column: a tier-1 row with `low` confidence is a weak claim of surprise. Only 1 of the 60 tier-1 rows
is `low`; 34 are `high`.

## The one row where the prior contradicts the claim

**145** (Rokhlin multiple mixing) is the only row whose `gap` field records a direct conflict: the
prior's record has published counterexamples to the Rokhlin multiple mixing property (Krengel 1978,
Friedman–Ornstein 1982, Jones 1980), and the abstract claims the property for a class of actions. The
table records the conflict and stops; reconciling it needs the manuscript, and no manuscript was read.
**340** (nearby Lagrangian) and **199** (Auslander–Reiten / Tachikawa / Nakayama) are reversals of
open conjectures, which is tier 1 in the other direction — the prior has them open, the release refutes
them.

## Checker

`python3 notes/scripts/verify_conjecture_standing.py` — reads the ledger, `overview.tex`, and the
table; writes nothing. It checks 10 fields per row, that the fam set is exactly the
`resolves_named ∩ resolution` intersection, that `discipline`/`tier` match the ledger, that
`prior_confidence` is filled and in vocabulary, that every `abstract_line` resolves to that family's
own `\resultentry` line, that the `conjecture` field is named from the abstract it cites (surname
tokens, dash-normalized), that `surprise_tier` is 1–4, and that no `gap`/`standing` field asserts
consequence.

Current run: `rows: 139 selected: 139 fields: 10`, `surprise_tier: 1:60 2:64 3:11 4:4`,
`prior_confidence: high:42 low:13 medium:84`, `anchors resolved to \resultentry lines: 139`,
`problems: 0`.

Six mutants, all detected: anchor shifted by two lines; a blanked `prior_confidence`; a family added
outside the selection; a consequence assertion written into a `gap` field; a conjecture renamed to a
name absent from its abstract; a row widened to 11 fields.

Three rows were corrected by the checker on its first run: **187** cited line 451, its entry is line
453; **266**, **310**, **326** carried conjecture names the abstracts do not use, and now read
"Zauner dimension-six mutually unbiased bases conjecture", "Quillen conjecture in rational homology",
"cotype-cotype conjecture under the approximation property".

## Not checked

- **No row asserts consequence.** The table records standing and claim only. The reason is not that
  the corpus lacks citation structure: `notes/links.tsv` measures **397** release-labelled
  bibliography entries resolving to **396** manuscript→manuscript edges over **158 of 372** families,
  **105** of them crossing a family boundary. The reason is that those edges are **untyped** — the
  release records no builds-on / contrasts-with / refutes relation, so an edge says the release chose
  to cite, not that the cited result mattered. The "**14 of 372** family titles appear in the `.bib`
  files" figure this bullet used to carry is reproduced (a 6-token lowercased title prefix over the 417
  `.bib` files at glob depth ≤3, own-family bibliographies included), but it measures a proxy whose
  scope is 417 of 501 files and which has no ownership test; the shipped title rule yields 12
  cross-family / 23 including own-family. See `notes/links.md`. Consequence claims stay
  external to this table, now because the edges carry no direction of dependence, not because they
  are absent.
- The prior is not a literature survey. It is one model's memory at a cutoff: it can be wrong about a
  conjecture's status, stale on a 2024–2025 preprint, and it is systematically better on famous
  conjectures than on the niche ones, which is why tier 4 exists.
- No manuscript was read for any of the 139 rows. `release_claim` is the abstract's claim, restated —
  not the theorem the manuscript proves, and not verified against the formalization (no Lean run).
- The `conjecture` field is checked for *name fidelity to the abstract*, not for identity with the
  conjecture as the literature names it. Where the abstract names a target by person (Zauner, Quillen,
  Kirk), the row follows the abstract.
- `prior_confidence` is self-reported by the same prior it qualifies; it is not calibrated against
  anything. Its only use is ordering: a `low` row should not be quoted as evidence of surprise.
- The tier assignments were validated against each abstract, not copied from `math-el4`'s draft
  tiers; the draft's examples (002 BSD, 014 Langlands) are not in the 139 at all.
- **Not measured:** how often the prior is wrong. The negative control — reading the literature
  record for a sample of rows, starting with the 42 `high`-confidence tier-1 rows — has not been run,
  so the tier counts are a prior-based ranking, not a finding about the release.
