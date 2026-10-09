# The typed-edge inventory

Measured 2026-10-08 by `python3 notes/scripts/extract_links.py`, which writes `notes/links.tsv` —
**22 rows, 7 fields** (`edge`, `source`, `pattern`, `count`, `detail`, `command`, `not_meaning`). No
`lake`, `lean`, `lake exe cache get`, or comparator run, so nothing here is a verified build, a
verified pass, or a verified citation target beyond the file-existence checks stated per row. The
report the script prints is the test; every count below is reproducible by the command in its row,
and quote a number with the rule that yields it.

**Scope.** Every `preprints/` scan is restricted to the **719** manuscript directories the release
lists in `CONTENTS.md`, not to every directory under `preprints/`. Upstream keeps a superseded
edition of a revised manuscript beside its replacement, and a withdrawn manuscript's directory beside
its notice: **749** directories on disk = **719** listed + **27** superseded + **3** withdrawal
notices. A directory walk would count a superseded edition's bibliography a second time. The
whole-tree counts are printed in the report and are not written to the TSV.

## The rows

| Edge | Count | What the edge is not |
|---|---|---|
| family→manuscript | **719** | A published link, not a claim the manuscript is formalized, read, or correct |
| manuscript→formalized | **172** of 719 | A source-level declaration under `review: status: unchecked` |
| family→scope note | **242** of 372 | Release prose stating exclusions, not a certification |
| scope note→comparator statement | **426** | A link to a statement file, not a comparator pass |
| comparator config→statement+solution | **416** | A statement/solution pair on disk, not a run |
| family→main_results declaration | **200** | The release's own list, not a verification |
| formalization→declared library | **30** | A declared pin, not a buildable pin |
| formalization→observed import root | **12** | Direct imports over `lean/OAI/`, not the transitive closure |
| manuscript→bibliography entry | **12,876** | Shipped entries, not checked references |
| manuscript→corpus manuscript (bib href) | **393** | What the release chose to cite, not importance |
| manuscript→corpus manuscript (body href) | **211** | An in-text pointer, not a dependency |
| abstract→companion family | **2** | An abstract naming a sibling, not a citation |
| abstract→"companion" wording | **9** | A word, creating no edge |
| family→reasoning trace | **10** | Release attribution, not evidence the trace is the proof |
| named-in-title | **153** of 372 | A property of catalog prose, not of the literature |
| cited-in-bib | **12** of 372 | A title-phrase proxy; a miss is not evidence of no impact |
| mentioned-in-body | **11** of 372 | A shared phrase can be not-a-reference |
| family→MSC code | **0** | Negative: no classification vocabulary exists to read |
| bibliography entry→keywords field | **0** | Negative: bibliographies carry no topic vocabulary |
| manuscript→`\keywords` macro | **12** of 719 | 98% of manuscripts define no keyword list |
| manuscript→verification bundle | **30** | A certificate bundle, not a theorem check |
| family→notes summary page | **21** | Our artifact, not part of the release |

## 426 vs 416: link occurrences, not missing files

`lean/docs/*.md` (242 files) contain **426** occurrences of `](../ComparatorChallenges/<name>.lean)`
and **416** distinct config names. The 10 extra occurrences are the same config linked twice
**inside one doc** — 7 docs: `071, 100, 115, 134, 274, 275, 293`. **0** configs are linked by more
than one family's doc, so the 416 configs are partitioned by family, not shared.

The ledger's `chal` column is the per-doc **deduped** count, so it sums to **416** while this row
counts **426**. Both are correct for their rule; the generator report line is `challenges 416`.
Docs link `.lean` and never `.json`; **0** of the 416 `.json` files are unlinked and **0** linked
targets are absent from disk.

## 200 / 189 / 136: the main_results layer

`lean/formalization.yaml` → `status.main_results` carries **200** `comparator_config:` entries over
**189** unique configs — **11** repeated entries across **8** configs (`ComparatorChallenges/`
`EgyptianFractions` ×3, `MatrixMultiplication` ×3, `TraceIdealTransportSupport` ×3,
`GaussianReplacement` ×2, `IndependentProducts` ×2, `SmoothYau` ×2, `OneTapeSpace` ×2,
`UniformFourier` ×2). **136** families have ≥1 entry, and the ledger `mainres` column sums to 189, so
no config is shared between families.

The bead spec's "168 families with `mainres>0`" is **not reproduced**; the measured figure is 136.

**The main_results set is one family away from the formalized set, and the gap is a release defect.**
136 families have a `main_results` entry; **135** have a formalized manuscript (172 manuscripts).
`mainres`−formalized = **1** family: **342** (Donaldson's tamed-to-compatible conjecture), and
formalized−`mainres` = **0**. Family 342's `sources:` entry
(`lean/formalization.yaml:684`) names
`preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/paper.pdf`, which is the
edition upstream superseded on 2026-10-07; the listed manuscript is the `…-October-6-2026` directory.
So the release declares a main result for a family whose only listed manuscript it no longer points
at. Before the merge the two sets were equal (127 = 127, 0 in either difference); the merge made the
formalized count strictly smaller. The two layers are near-identical signals, and a coverage answer
that quotes both is quoting one signal plus one defect.

## The manuscript→manuscript layer is the href, not the title

The release cites its own preprints by URL. In the 12,876 bibliography entries owned by listed
manuscripts, **393** contain the literal string `OpenAI Math Release`; **391** resolve to a shipped
PDF through `\href{…/preprints/<dir>/<file>.pdf}` (**0** unresolved). Those edges span **268** target
directories over **156 of 372 families**, from **259** citing directories: **287** point at a
manuscript of the same family, **104** cross a family boundary.

Body text adds a second, smaller layer: **211** `\href{…/preprints/…}` occurrences in `.tex`, over
**147** target directories spanning **84** families, from **128** citing directories. All 147 body
targets are listed manuscripts.

**No listed manuscript cites a superseded edition.** Over the listed scope, **0** of the 391 resolved
bib hrefs point at a directory outside the 719. Over the whole tree (superseded editions' own
bibliographies included) the same scan resolves **432** hrefs, of which **22** point at **16**
superseded editions. The superseded-target citations live only inside superseded editions, which is
why scoping the inventory to listed manuscripts loses nothing and removes a double count.

Most-cited target families (bib href edges): **034** (19), **260** (18), **068** (14), **033** (12),
**227** (11), **238** (10), **376** (9), **331** (7), **215** (6), **090** (6).

This is the measurement that makes intra-release consequence measurable. `notes/conjecture-standing.md`,
the `AGENTS.md` dev tip, and the `corpus-finding-surprise-ranking` skill all conclude from
"only 14 of 372 family titles appear in the corpus's `.bib` files" that the manuscripts do not cite
each other, so intra-corpus consequence is unmeasurable. The **count** reproduces (see the section
below); the **conclusion** does not follow. The same corpus carries 391 resolved manuscript→manuscript
citation edges reaching 156 families, because the release cites by URL and a title phrase is not how a
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
| mentioned-in-body | `preprints/**/*.tex` | **11** of 372 | 113 |

`cited-in-bib`: **001, 003, 006, 038, 066, 086, 109, 145, 166, 202, 231, 312**. Each was read and
validated as a genuine citation — the entry reads e.g. `{Milne's rationality conjecture for abelian
varieties}}, howpublished = {OpenAI Math Release preprint \href{https://github.com/openai/…`. The
merge changed no member of this list.

`mentioned-in-body`: **003, 006, 032, 086, 094, 109, 145, 176, 194, 202, 299**. **6** of these 11
(003, 006, 086, 109, 145, 202) also appear in `cited-in-bib`, which is the signature of a real
reference; the **5** that do not — **032, 094, 176, 194, 299** — are the ones to read before
believing, and 6 of the 12 `cited-in-bib` families (001, 038, 066, 166, 231, 312) are cited in a
bibliography without the title phrase appearing in any body text. **032** is new to this list after
the 2026-10-07 merge: its title was rewritten when three of its manuscripts were withdrawn, and the
new phrase is what matches. It has not been read.

### The recorded "14" is reproduced, by a rule with two scope defects

The repo records "14 of 372 family titles appear in the corpus's `.bib` files". The rule behind it was
written down — in the `corpus-finding-surprise-ranking` skill — and it reproduces exactly: a
**6-token lowercased title prefix** searched in the concatenation of `preprints/*/*.bib` +
`preprints/*/*/*.bib`, with the corpus **lowercased, not normalized**, and own-family bibliographies
**included**. `notes/scripts/extract_links.py` computes it and prints it as a report line, so 14 is
reproducible by the same command as every other number here.

The count is a measurement of a rule, and the rule has two defects that the prose did not record:

- **Scope.** The two globs reach **417 of the 500** listed-manuscript `.bib` files; the 83 at depth 4
  (`preprints/*/*/*/*.bib`) are outside it.
- **No ownership test.** It counts a title appearing in *any* bibliography, including the owning
  family's own. Under the same title rule over all 500 listed files: **17** families, **12**
  cross-family.

Measured 2026-10-08 over the listed scope, all three knobs at once (title rule × corpus text × file
scope):

| Title rule | Corpus text | `.bib` scope | Any family | Cross-family |
|---|---|---|---|---|
| 6-token prefix | lowercased | 417 (depth ≤3) | **14** ← the recorded figure | 10 |
| 6-token prefix | lowercased | 500 (all listed) | 17 | 12 |
| 6-token prefix | normalized | 417 | 2 | 1 |
| 6-token prefix | normalized | 500 | 2 | 1 |
| normalized full title | lowercased | 417 | 4 | 3 |
| normalized full title | lowercased | 500 | 5 | 4 |
| normalized full title | normalized | 417 | 20 | 10 |
| normalized full title | normalized | 500 | **23** | **12** ← shipped `cited-in-bib` |

The last row is the rule shipped in `notes/links.tsv`; the first row is the recorded 14. Normalizing
the corpus is the dominant knob — it is what turns punctuation-bearing titles into matchable phrases,
taking 5 to 23 — which is why a stem-style variant is not interchangeable with a normalized one.
Other variants measured over the 500 listed `.bib` files: title-core (trailing noun dropped) over a
lowercased corpus 10 / 9; verbatim case-sensitive over the raw corpus 12 / 9; verbatim case-insensitive
15 / 11; verbatim ci with `the` stripped 7 / 5; normalized with `the` kept 6 / 4; `title={}` field
only (brace-balanced), verbatim ci 15 / 11; `title={}` field only, normalized 23 / 12.

So the recorded figure is not a phantom, and the conclusion drawn from it is unchanged: the
title-phrase layer reaches 12 cross-family families while the href layer reaches 104, so the proxy
under-counts citations by an order of magnitude. What changes is the reason to give. Quote 14 with its
rule and its 417-file scope, and quote 12 with the normalized rule and the 500-file scope.

## Negatives, stated as measurements

- **0** MSC codes anywhere. Rule: `MSC 20xx | \msc | mscclass | "Mathematics Subject Classification"
  | Primary nnXxx` over 8,206 files (7,705 `.tex` + 500 `.bib` + `overview.tex`). A bare `\bMSC\b`
  scan is **not** this rule: case-sensitively it returns **0** hits, and case-insensitively **1** hit
  in **1** file — `type = {MSc thesis}` in
  `preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/build/references/references.bib`.
- **0** `keywords =` fields in 12,876 bibliography entries.
- `\keywords` in **12** of 719 manuscript directories (1.7%).
- **2** companion edges: `001→032`, `002→006`. The pattern is
  `result (\d{3})` at **`notes/scripts/build_catalog.py:106`** — the bead spec cites line 267 and the
  pre-refactor file carried it at 308, both stale. **9** families use the word "companion" in an
  abstract and **0** of them carry a `result NNN` edge, so the word and the edge are disjoint signals.
- **0** one-sided family→manuscript links: `overview.tex`-only links 0, `CONTENTS.md`-only links 0.

## Not checked

- **No citation was read past its entry.** The 393 release-labelled entries were matched by string
  and their hrefs resolved against disk; none was checked for a correct author, year, title, or venue,
  and the 12 validated `cited-in-bib` cases were read as entry text, not verified against the work.
- The 104 cross-family citation edges are **not** typed. Why a manuscript cites another — builds-on,
  contrasts-with, refutes, acknowledges — is not recorded anywhere in the release, and this inventory
  does not infer it.
- `mentioned-in-body` is a phrase match over normalized text with no boundary test for abbreviations
  or translations, so a hit can be a shared term. The 11 cross-family hits were not individually read;
  **032** is new to the list and unread.
- The 211 body hrefs were counted as occurrences, not deduped to edges; a manuscript linking the same
  target twice counts twice here, unlike the bib layer.
- Bibliography coverage is **494 of 719** manuscript directories. The 225 directories with no `.bib`
  were not checked for a bibliography in another format.
- The 12,876 entries are counted by `^@[A-Za-z]+`; entries in commented-out blocks are included, and
  no check was made that each parses as a BibTeX entry.
- Import roots are direct statements over `lean/OAI/` only. `lean/docs/` ships no `.lean`, and
  imports inside vendored upstream trees were not inspected — `.lake/packages` is absent.
- Whether the 30 verification directories verify anything is not measured; family 318's
  `SUPPORT-COVERAGE.md` names artifacts that do not exist on disk.
- The 27 superseded editions and 3 withdrawal notices are counted in the report census and excluded
  from every TSV row; their internal bibliographies were not read.
- The `not_meaning` column is a reading of what the release asserts, not an audit of whether the
  assertion holds.
