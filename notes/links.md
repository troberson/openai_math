# The typed-edge inventory

Measured 2026-10-07 by `python3 notes/scripts/extract_links.py`, which writes `notes/links.tsv` —
**22 rows, 7 fields** (`edge`, `source`, `pattern`, `count`, `detail`, `command`, `not_meaning`). No
`lake`, `lean`, `lake exe cache get`, or comparator run, so nothing here is a verified build, a
verified pass, or a verified citation target beyond the file-existence checks stated per row. The
report the script prints is the test; every count below is reproducible by the command in its row,
and quote a number with the rule that yields it.

## The rows

| Edge | Count | What the edge is not |
|---|---|---|
| family→manuscript | **722** | A published link, not a claim the manuscript is formalized, read, or correct |
| manuscript→formalized | **162** of 722 | A source-level declaration under `review: status: unchecked` |
| family→scope note | **235** of 372 | Release prose stating exclusions, not a certification |
| scope note→comparator statement | **415** | A link to a statement file, not a comparator pass |
| comparator config→statement+solution | **405** | A statement/solution pair on disk, not a run |
| family→main_results declaration | **185** | The release's own list, not a verification |
| formalization→declared library | **30** | A declared pin, not a buildable pin |
| formalization→observed import root | **12** | Direct imports over `lean/OAI/`, not the transitive closure |
| manuscript→bibliography entry | **12,928** | Shipped entries, not checked references |
| manuscript→corpus manuscript (bib href) | **397** | What the release chose to cite, not importance |
| manuscript→corpus manuscript (body href) | **213** | An in-text pointer, not a dependency |
| abstract→companion family | **2** | An abstract naming a sibling, not a citation |
| abstract→"companion" wording | **10** | A word, creating no edge |
| family→reasoning trace | **10** | Release attribution, not evidence the trace is the proof |
| named-in-title | **153** of 372 | A property of catalog prose, not of the literature |
| cited-in-bib | **12** of 372 | A title-phrase proxy; a miss is not evidence of no impact |
| mentioned-in-body | **10** of 372 | A shared phrase can be not-a-reference |
| family→MSC code | **0** | Negative: no classification vocabulary exists to read |
| bibliography entry→keywords field | **0** | Negative: bibliographies carry no topic vocabulary |
| manuscript→`\keywords` macro | **12** of 722 | 98% of manuscripts define no keyword list |
| manuscript→verification bundle | **30** | A certificate bundle, not a theorem check |
| family→notes summary page | **12** | Our artifact, not part of the release |

## 415 vs 405: link occurrences, not missing files

`lean/docs/*.md` (235 files) contain **415** occurrences of `](../ComparatorChallenges/<name>.lean)`
and **405** distinct config names. The 10 extra occurrences are the same config linked twice
**inside one doc** — 7 docs: `071, 100, 115, 134, 274, 275, 293`. **0** configs are linked by more
than one family's doc, so the 405 configs are partitioned by family, not shared.

The ledger's `chal` column is the per-doc **deduped** count, so it sums to **405** while this row
counts **415**. Both are correct for their rule; the generator report line is `challenges 405`.
Docs link `.lean` and never `.json`; **0** of the 405 `.json` files are unlinked and **0** linked
targets are absent from disk.

## 185 / 178 / 127: the main_results layer

`lean/formalization.yaml` → `status.main_results` carries **185** `comparator_config:` entries over
**178** unique configs — **7** repeated entries across 5 configs (`EgyptianFractions`,
`GaussianReplacement`, `IndependentProducts`, `MatrixMultiplication`, `SmoothYau`). **127** families
have ≥1 entry, and the ledger `mainres` column sums to 178, so no config is shared between families.

The bead spec's "168 families with `mainres>0`" is **not reproduced**; the measured figure is 127.

**The main_results set equals the formalized set.** 127 families have a `main_results` entry and 127
families have a formalized manuscript (162 manuscripts), with **0** families in either difference.
So the release declares main results only for families it formalized, and formalizes every family it
declares main results for. The two layers are not independent signals, and a coverage answer that
quotes both is quoting one.

## The manuscript→manuscript layer is the href, not the title

The release cites its own preprints by URL. In the 12,928 bibliography entries, **397** contain the
literal string `OpenAI Math Release`; **396** resolve to a shipped PDF through
`\href{…/preprints/<dir>/<file>.pdf}` (**0** unresolved). Those edges span **273** target
directories over **158 of 372 families**, from **261** citing directories: **291** point at a
manuscript of the same family, **105** cross a family boundary.

Body text adds a second, smaller layer: **213** `\href{…/preprints/…}` occurrences in `.tex`, over
**149** target directories spanning **84** families, from **129** citing directories.

Most-cited target families (bib href edges): **034** (19), **260** (18), **068** (14), **033** (12),
**227** (11), **238** (10), **376** (9), **331** (7), **215** (6), **090** (6).

This is the measurement that makes intra-release consequence measurable. `notes/conjecture-standing.md`,
the `AGENTS.md` dev tip, and the `auto-skill-corpus-finding-surprise-ranking` skill all conclude from
"only 14 of 372 family titles appear in the corpus's `.bib` files" that the manuscripts do not cite
each other, so intra-corpus consequence is unmeasurable. The **count** reproduces (see the section
below); the **conclusion** does not follow. The same corpus carries 396 resolved manuscript→manuscript
citation edges reaching 158 families, because the release cites by URL and a title phrase is not how a
citation is written. What is unmeasurable is the *type* of each edge, not its existence. All three
documents are corrected in the same pass as this record.

## The three name relations are three rows

They measure three different things, and the repo has previously quoted one number for all three.
All three normalize the family title the same way — lowercase alphanumerics, single-spaced, leading
`the` dropped, possessives stripped — and differ only in the text searched.

| Relation | Text searched | Cross-family | Including own-family |
|---|---|---|---|
| named-in-title | `overview.tex` `\resultentry` arg 2 | **153** of 372 | — |
| cited-in-bib | `preprints/**/*.bib` | **12** of 372 | 23 |
| mentioned-in-body | `preprints/**/*.tex` | **10** of 372 | 112 |

`cited-in-bib`: **001, 003, 006, 038, 066, 086, 109, 145, 166, 202, 231, 312**. Each was read and
validated as a genuine citation — the entry reads e.g. `{Milne's rationality conjecture for abelian
varieties}}, howpublished = {OpenAI Math Release preprint \href{https://github.com/openai/…`.

`mentioned-in-body`: **003, 006, 086, 094, 109, 145, 176, 194, 202, 299**. **6** of these 10
(003, 006, 086, 109, 145, 202) also appear in `cited-in-bib`, which is the signature of a real
reference; the **4** that do not — **094, 176, 194, 299** — are the ones to read before believing,
and 6 of the 12 `cited-in-bib` families (001, 038, 066, 166, 231, 312) are cited in a bibliography
without the title phrase appearing in any body text.

### The recorded "14" is reproduced, by a rule with two scope defects

The repo records "14 of 372 family titles appear in the corpus's `.bib` files". The rule behind it was
written down — in the `auto-skill-corpus-finding-surprise-ranking` skill — and it reproduces exactly:
a **6-token lowercased title prefix** searched in the concatenation of `preprints/*/*.bib` +
`preprints/*/*/*.bib`, with the corpus **lowercased, not normalized**, and own-family bibliographies
**included**. `notes/scripts/extract_links.py` now computes it and prints it as a report line, so 14 is
reproducible by the same command as every other number here.

The count is a measurement of a rule, and the rule has two defects that the prose did not record:

- **Scope.** The two globs reach **417 of the 501** `.bib` files; the 77 at depth 4
  (`preprints/*/*/*/*.bib`) are outside it.
- **No ownership test.** It counts a title appearing in *any* bibliography, including the owning
  family's own. Under the same title rule over all 501 files: **18** families, **12** cross-family.

Measured 2026-10-07, all three knobs at once (title rule × corpus text × file scope):

| Title rule | Corpus text | `.bib` scope | Any family | Cross-family |
|---|---|---|---|---|
| 6-token prefix | lowercased | 417 (depth ≤3) | **14** ← the recorded figure | 10 |
| 6-token prefix | lowercased | 501 (all) | 18 | 12 |
| 6-token prefix | normalized | 417 | 2 | 1 |
| 6-token prefix | normalized | 501 | 2 | 1 |
| normalized full title | lowercased | 417 | 4 | 3 |
| normalized full title | lowercased | 501 | 5 | 4 |
| normalized full title | normalized | 417 | 20 | 10 |
| normalized full title | normalized | 501 | **23** | **12** ← shipped `cited-in-bib` |

The last row is the rule shipped in `notes/links.tsv`; the first row is the recorded 14. Normalizing
the corpus is the dominant knob — it is what turns punctuation-bearing titles into matchable phrases,
taking 5 to 23 — which is why a stem-style variant is not interchangeable with a normalized one.
Other variants measured over all 501 files with a lowercased corpus: title-core (trailing noun
dropped) 29 / 16; verbatim case-sensitive 12 / 9; verbatim case-insensitive 15 / 11; verbatim ci with
`the` stripped 16 / 11; normalized with `the` kept 21 / 11; `title={}` field only, verbatim ci 16;
`title={}` field only, normalized 5.

So the recorded figure is not a phantom, and the conclusion drawn from it is unchanged: the
title-phrase layer reaches 12 cross-family families while the href layer reaches 105, so the proxy
under-counts citations by an order of magnitude. What changes is the reason to give. Quote 14 with its
rule and its 417-file scope, and quote 12 with the normalized rule and the 501-file scope.

## Negatives, stated as measurements

- **0** MSC codes anywhere. Rule: `MSC 20xx | \msc | mscclass | "Mathematics Subject Classification"
  | Primary nnXxx` over 8,231 files (7,729 `.tex` + 501 `.bib` + `overview.tex`). A bare `\bMSC\b`
  scan is **not** this rule — it returns 14 hits over 13 files, all prose: `type = {MSc thesis}`,
  "2-primary class groups", "primary classical construction".
- **0** `keywords =` fields in 12,928 bibliography entries.
- `\keywords` in **12** of 722 manuscript directories (1.7%).
- **2** companion edges: `001→032`, `002→006`. The pattern is
  `result (\d{3})` at **`notes/scripts/build_catalog.py:308`** — the bead spec cites line 267, which
  is stale. **10** families use the word "companion" in an abstract and **0** of them carry a
  `result NNN` edge, so the word and the edge are disjoint signals.
- **0** one-sided family→manuscript links: `overview.tex`-only links 0, `CONTENTS.md`-only links 0.

## Not checked

- **No citation was read past its entry.** The 397 release-labelled entries were matched by string
  and their hrefs resolved against disk; none was checked for a correct author, year, title, or venue,
  and the 12 validated `cited-in-bib` cases were read as entry text, not verified against the work.
- The 105 cross-family citation edges are **not** typed. Why a manuscript cites another — builds-on,
  contrasts-with, refutes, acknowledges — is not recorded anywhere in the release, and this inventory
  does not infer it.
- `mentioned-in-body` is a phrase match over normalized text with no boundary test for abbreviations
  or translations, so a hit can be a shared term. The 10 cross-family hits were not individually read.
- The 213 body hrefs were counted as occurrences, not deduped to edges; a manuscript linking the same
  target twice counts twice here, unlike the bib layer.
- Bibliography coverage is **495 of 722** manuscript directories. The 227 directories with no `.bib`
  were not checked for a bibliography in another format.
- The 12,928 entries are counted by `^@[A-Za-z]+`; entries in commented-out blocks are included, and
  no check was made that each parses as a BibTeX entry.
- Import roots are direct statements over `lean/OAI/` only. `lean/docs/` ships no `.lean`, and
  imports inside vendored upstream trees were not inspected — `.lake/packages` is absent.
- Whether the 30 verification directories verify anything is not measured; family 318's
  `SUPPORT-COVERAGE.md` names artifacts that do not exist on disk.
- The `not_meaning` column is a reading of what the release asserts, not an audit of whether the
  assertion holds.
