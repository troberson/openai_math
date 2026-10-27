# Names — the four places a name sits, and which of them mean subject

Built 2026-10-07 by `notes/scripts/measure_names.py` (measurement — a writer: it lands the
population as the keyed record `.qwen/cache/records/<key>/names.json`, and `--check-only` prints the
report without landing it) and `notes/scripts/build_index.py` (writes `notes/gen/index/names/`,
`notes/gen/tables/names.tsv`, `notes/gen/tables/family-name.tsv`). Every count below is from a fresh run
of those two scripts; the rule that yields each count is stated beside it.

`"Cauchy-related"` is a name query. Names sit in four places in this release, and they do not
mean the same thing:

| Flag | Source | Layer | What a hit means |
|---|---|---|---|
| `F` | Family title (`overview.tex` `\resultentry` title) | title | The release named the family after it — the strongest subject evidence there is. |
| `M` | Manuscript directory name | title | A manuscript takes it as its subject. |
| `E` | Theorem-environment optional title (`theorem[Cauchy's …]`) | title | A statement is named for it. |
| `D` | `main_results` declaration name (`OAI.ArnoldCounterexample.main`) | declaration | A formalized statement is named for it. |
| `b` | Capitalized token in manuscript prose | body | **A citation, not a statement of subject.** |
| `B` | Author surname in a shipped `.bib` | body | **A citation, not a statement of subject.** |

**Headline, with the rule that yields it:** 5,864 name keys measured over the corpus. 550 of
them appear in a title layer (`F`, `M`, `E`) or in a declaration (`D`) — those are the
**subject** names, and each gets a page at `notes/gen/index/names/<name>.md`. The other 5,314 are
found only in prose (`b`) or in a bibliography (`B`) — those are **citation** names, and they
are rows in `notes/gen/tables/names.tsv` with `role=citation` and an empty `page` cell, not pages.
The subject names produce 9,872 family-name edges over all 373 families. No name resolves to
zero families (0), every family has a subject-name hit (373 of 373, so 0 families with no name
hit), and all 10 published reasoning-trace families are covered by subject names.

## What each source contributes

Subject names with at least one hit in the layer, over the 550 subject names:

| Layer | Names with a hit |
|---|---|
| `F` family title | 252 |
| `M` manuscript directory title | 206 |
| `E` theorem-environment title | 392 |
| `D` declaration name | 70 |
| `b` body prose | 549 |
| `B` bib author | 385 |

Zero subject names lack a title-or-declaration layer — that is the page gate, so it is true by
construction, and the interesting number is the one that is not: 549 of 550 subject names also
occur in prose. The single exception is `swinnerton-dyer`, one of the 17 family-title escape
names: the release names a family after it and no manuscript prose ever capitalizes it.

The theorem-environment layer is the load-bearing one. It is what makes `cauchy` a subject name
at all: `cauchy` appears in 233 family-title sets' prose and in 7 theorem-environment titles
(families 102, 122, 143, 232, 233, 261, 264), and in **no** declaration name — the corpus has
207 `main_results` entries over 191 configs, whose declaration names decompose into 356
distinct CamelCase tokens (200 distinct config+declaration pairs), and none of them
contains `cauchy`. That is a fact about the release, not a gap in the extractor: the
formalized statements are named after constructions and counterexamples (`counterexample` 9,
`main` 9, `projection` 5, `target` 5, `critical` 4, `matrix` 4), not after Cauchy.

## Subject versus citation, and why only subjects get a page

A name in a body paragraph is a citation. `cauchy` occurs in the prose of 233 of 373 families
because Cauchy's name is everywhere in analysis; that does not make 232 families "about
Cauchy". `wang` is a subject name in 75 families' records and a bibliography author in 53 of
them; `zhang` in 69 and 55. Those bibliography counts are citations to papers, and they are
reported on the page in their own row, never merged into the subject claim.

So the gate for a page is a title-or-declaration hit, and every page states its provenance by
source in a table, with the per-layer family counts, before it lists any family. Pages are
sorted by family count; `notes/gen/tables/names.tsv` carries all 5,864 rows with a `role` column.

## Normalization

`fold()` strips LaTeX accent escapes (`\'e`, `\H{u}`), Unicode diacritics, and braces.
`key()` folds, unifies the five Unicode dashes to `-`, strips a trailing possessive
(`Kaplansky's` → `kaplansky`), and lowercases. So `Mézard–Parisi`, `Mézard-Parisi` and
`Mezard-Parisi` are one key, `mezard-parisi`, and the page lists every surface spelling it saw.

325 of the 550 subject names are spelled more than one way in prose alone. The variants are
listed on each page; the count of names with >1 prose spelling is 325.

## The name-versus-word test

A capitalized token in prose is a name when the corpus capitalizes it **mid-sentence** and
almost never writes it lowercase. Sentence-initial capitalization is free, so the token's
preceding character is checked: whitespace after `.!?;:}~%&$\{}[]()#` is not mid-sentence, and
a token within 40 characters of a blank line (a heading) is not mid-sentence. Cross-reference
and cite braces are stripped first, because cite keys are lowercase name fragments and would
poison the lowercase count.

The table is the report's `probe tokens` line — `notes/scripts/measure_names.py` prints
`token=mid/low` for every token below, in the order listed here. Rejected candidates carry no
JSON row, so this line is the only record of their gate evidence.

| Token | mid-sentence | lowercase |
|---|---|---|
| `the` | 23,830 | 859,677 |
| `all` | 1,431 | 44,068 |
| `games` | 61 | 100 |
| `lane` | 16 | 48 |
| `hom` | 647 | 270 |
| `quot` | 69 | 22 |
| `cat` | 169 | 42 |
| `adm` | 414 | 40 |
| `boolean` | 655 | 35 |
| `catalan` | 33 | 7 |
| `koebe` | 39 | 14 |
| `saxl` | 21 | 9 |
| `pixton` | 14 | 6 |
| `wang` | 203 | 8 |
| `cauchy` | 2,212 | 113 |

The gate is `mid >= 3 and low <= max(1, mid // 2)`. `the` and `all` fail by a factor of 36 and
31. `games` (61/100) and `lane` (16/48) fail; `catalan` (33/7) and `koebe` (39/14) pass.
`cauchy` is capitalized 2,212 times mid-sentence and written lowercase 113 times.

## The rejection ladder

Candidate keys are the union of the four title/declaration layers: 3,414 keys. They are
screened in this order, and 2,858 are rejected, leaving 556; the plural merge below removes 6,
so 550 subject names remain.

| Rejected as | Count | Rule |
|---|---|---|
| `not-a-word-key` | 77 | Key shorter than 3 letters, or not `^[a-z][a-z]*(-[a-z][a-z]*)*$`. |
| `label-word` | 25 | In `LABEL_WORDS`: statement-environment words, months (every manuscript directory ends in one), publishers, `lean`, `openai`. |
| `maths-word` | 6 | In `JUNK_WORDS` — see below. |
| `contains-digit` | 0 | Any digit in the key. |
| `acronym` | 60 | The dominant surface form is all capitals (`CAT`, `ADM`). |
| `latex-macro` | 15 | The dominant surface form has a second internal capital (`OpenAIWidth`). |
| `no-prose-evidence` | 290 | No mid-sentence capitalized occurrence anywhere in the corpus. |
| `prose-word` | 2,385 | Fails the mid-sentence test above. |

The acronym and macro tests are judged on the **dominant surface form over all six layers**,
not on prose alone. That is a fix, not a nicety: `OpenAIWidth` reaches the candidate set
through a `\cite{OpenAIWidth}` that leaked into a theorem-environment title, so it never
appears as prose, and a prose-only view of surface forms cannot see it. `cat` (169/42) and
`adm` (414/40) both pass the mid-sentence name test; the acronym test is what rejects them.

## The family-title escape

A name in a family title is the release's own naming decision, so it is not required to
survive the prose ladder. 17 keys are kept on that basis: `bochner`, `campana`, `curtis`,
`elliott`, `etingof`, `green`, `jacobsthal`, `kraetzer`, `mahler`, `ostmann`, `pop`, `riesz`,
`ryser`, `shub`, `swinnerton-dyer`, `wilson`. Each appears in a family title and has no
qualifying mid-sentence prose evidence, which is a statement about how often the corpus writes
the name, not about whether it is a name.

## Words that pass the name test and are not names

Six keys clear the mid-sentence gate, appear in a title layer, and name a mathematical object
or an English adjective. They are rejected by name, each traced to the title that produced it:

| Key | Title evidence | What it is |
|---|---|---|
| `hom` | "The orbit Hom calculation" | the Hom functor |
| `quot` | "The open Quot enhancement" | the Quot functor |
| `combinatorics` | "Combinatorics of shapes" | a subject heading |
| `computer` | "Computer-assisted" | an adjective |
| `beaver` | "The Busy Beaver cutoff" | the busy-beaver function |
| `stablest` | "Majority Is Stablest with a degree cutoff" | a superlative |

Kept, because they are names used adjectivally by the release itself: `boolean` (655 mid / 35
lowercase; family 283's title), `diophantine`, and the surnames that look like common nouns —
`eccles` ("Eccles's conjecture for spheres"), `street` ("Street nerves of two-piece covers"),
`villain` (the Villain field), `sebastiani` ("Thom–Sebastiani–Sakamoto"), `solitar`
(Baumslag–Solitar), and `maker` and `snaky`, which are family 187's own game roles (142/0 and
8/0 mid-sentence — the corpus never writes them lowercase).

## Yield

Top 40 subject names by family count. `F`/`M`/`E`/`D` columns count families (declarations)
with a hit in that layer; `b` and `B` are family counts of prose and bibliography hits.

| Name | Families | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| `cauchy` | 233 | — | — | 7 | — | 233 | — |
| `euclidean` | 193 | 4 | 6 | 11 | 3 | 193 | — |
| `schwarz` | 194 | — | — | 1 | — | 194 | 1 |
| `lipschitz` | 178 | 4 | 9 | 10 | 1 | 178 | — |
| `hilbert` | 171 | 6 | 7 | 15 | 2 | 171 | 3 |
| `taylor` | 166 | — | — | 12 | — | 165 | 21 |
| `fourier` | 161 | 3 | 8 | 27 | 8 | 161 | — |
| `borel` | 140 | 1 | — | 4 | — | 137 | 10 |
| `jacobian` | 136 | — | — | 5 | — | 136 | — |
| `markov` | 134 | 2 | 2 | 1 | 1 | 133 | 1 |
| `gaussian` | 131 | 5 | 10 | 39 | 2 | 131 | — |
| `lebesgue` | 125 | 1 | 1 | — | — | 125 | — |
| `euler` | 122 | — | — | 10 | — | 122 | 1 |
| `holder` | 115 | — | 1 | 4 | 1 | 115 | — |
| `riemann` | 110 | 1 | 2 | 2 | — | 110 | — |
| `gram` | 108 | — | — | 12 | — | 108 | — |
| `poincare` | 101 | — | — | 3 | — | 101 | — |
| `hausdorff` | 94 | 1 | 3 | 2 | — | 94 | 1 |
| `schur` | 88 | — | — | 8 | — | 88 | — |
| `hessian` | 87 | — | 1 | 9 | 1 | 87 | — |
| `frobenius` | 85 | — | 1 | 14 | — | 85 | — |
| `hermitian` | 86 | — | — | 1 | — | 86 | — |
| `dirichlet` | 85 | — | 1 | 9 | 1 | 85 | — |
| `laurent` | 84 | — | — | 6 | — | 83 | 3 |
| `neumann` | 79 | 1 | 1 | 4 | — | 79 | 2 |
| `minkowski` | 78 | 1 | 1 | 3 | 1 | 78 | — |
| `sobolev` | 76 | 2 | 1 | 14 | — | 76 | — |
| `wang` | 75 | — | — | 2 | — | 66 | 53 |
| `bernoulli` | 72 | 2 | 3 | — | — | 72 | — |
| `poisson` | 72 | — | 2 | 10 | — | 72 | 1 |
| `banach` | 71 | 2 | 2 | 2 | 1 | 71 | — |
| `schmidt` | 71 | — | — | 1 | — | 66 | 16 |
| `zhang` | 69 | — | — | 1 | — | 55 | 55 |
| `boolean` | 66 | 1 | 3 | 9 | — | 66 | — |
| `green` | 65 | 1 | 1 | 12 | — | 61 | 17 |
| `young` | 62 | — | — | 3 | — | 60 | 5 |
| `laplacian` | 62 | — | — | 4 | — | 62 | — |
| `gauss` | 60 | 1 | 1 | 6 | — | 60 | — |
| `haar` | 60 | — | — | 12 | — | 60 | — |
| `serre` | 58 | 1 | — | — | — | 55 | 21 |

The bottom of the list is 66 names attached to exactly one family, e.g. `zarankiewicz` (one
declaration, no title hit), `urysohn` (two manuscript directory titles), `woodin`,
`waldhausen`, `vlasov` (family 362's title).

## Distribution

9,872 subject edges over 373 families: 26.5 subject names per family on average. Median 7
families per name; 66 names attach to exactly 1 family; 17 names attach to 100 or more.

## Measurement totals

7,266 `.tex` files at depth 1–3; 16,919 statement environments carrying an optional title;
13,661 `.bib` entries, 5,832 distinct author-surname keys. (`notes/gen/tables/sources.tsv` reports 21,353
environments under a wider pattern; `notes/gen/reports/sources.md` states both rules.)

## Recorded decisions

- **Family pages do not link name pages.** The average family carries 26.5 subject names; that is
  a table, not a header row. The link direction is name → family, and
  `notes/gen/tables/family-name.tsv` carries the family → name side with layer flags.
- **Citation-only names get no page** (5,314 of them). They are rows with `role=citation` and an
  empty `page` cell, so a query can find them and a page cannot overstate them.
- **Theorem-environment titles are capped at 8 per page** (`env_hits`), verbatim after folding.
- **An earlier gate required a theorem-environment title for a page.** It deleted `cauchy`,
  `fermat`, `legendre`, `baire`, `grassmann`, `bayes`, `haar`, `schur`, `poincare`, `bessel`,
  `sylow` — names the release uses as subjects in family and manuscript titles that no
  environment title happens to carry. The gate was deleted; the page gate is any title layer or
  a declaration.
- **Plural merge:** a subject key ending in `s` whose singular is also a subject key is dropped
  into the singular, provided the plural is not itself in a family title. 6 keys merged:
  `goldfelds`, `hamiltonians`, `hessians`, `jacobians`, `lagrangians`, `laplacians`. 266 plural
  forms appear in a title layer whose singular also appears in a title layer; 6 of them clear the
  mid-sentence name test, so exactly these 6 reach the merge step.
- `boolean` (66 families) and `diophantine` (9) are kept as name-derived adjectives; `maker` and
  `snaky` are kept as family 187's own game roles.

## Not checked

- The keyword ladder is a floor, not a census. 2,385 candidates were rejected as prose-words by
  a capitalization ratio; a name the corpus always writes at a sentence start is invisible to
  this test, and the 290 `no-prose-evidence` rejections are exactly that case for names that
  appear in a title.
- Prose (`b`) and bibliography (`B`) hits are citations. No claim is made that a name's prose
  count measures relevance, and no per-occurrence context is recorded — only the manuscript
  directory and family.
- Author extraction takes the last name of the first author-list element per entry (comma form
  preferred). First names, `editor` fields, and institutional authors are not parsed, and no
  author is disambiguated across spellings beyond `key()`.
- Declaration names are tokenized from `main_results` only; `lean/OAI/` declaration names
  (the full library) are not indexed, and no Lean file was built or elaborated.
- Names are not linked to the 92 topic pages, and no name-to-name graph (e.g.
  Baumslag–Solitar, Thom–Sebastiani–Sakamoto as a pair) is built; multi-word surnames are kept
  as single hyphenated keys, not split into component people.
- Whether a name page's family list is *about* that name is a judgement the page does not make;
  it reports which layer produced each family.
