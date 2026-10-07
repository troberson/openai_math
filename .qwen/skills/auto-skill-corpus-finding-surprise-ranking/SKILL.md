---
name: corpus-finding-surprise-ranking
description: Rank a corpus of results by how surprising and how consequential they are, using the
  assistant's training-data prior for the conjecture's standing and the repo for the claim. Use when
  asked which findings matter most, what is most surprising, what is consequential, or how to build a
  name/topic cross-reference over a corpus. Measures the layers before ranking and labels the prior.
source: auto-skill
extracted_at: '2026-10-07T09:16:58.409Z'
---

# Ranking findings by surprise and consequence

Worked out on the OpenAI Research Catalog (`/home/tamara/Downloads/_Git/math`): 372 result families,
722 manuscripts, September–October 2026. The user's framing: "we'll trust the model that all findings
are correct. we're not looking for inconsistencies. I'm more interested in which findings are the most
surprising and consequential."

**This is not a verification task.** Do not audit proofs, do not hunt contradictions, do not lead with
`review.status: unchecked`. Reading scope notes here is not fact-checking — it is how you learn *what
was claimed*, which is a prerequisite for ranking. Say that distinction when the user has just told
you to stop verifying.

## 0. The equation, and the honest boundary

**Surprise = claim − prior.** The repo supplies the claim. The training data supplies the prior: how
long the conjecture was open, how famous, what the accepted partial results were, where the barrier
sat. Consequence is the same shape — how much *other* mathematics changes status, which is a judgment
about the literature, not about the repo.

State the boundary up front: manuscripts dated after the training cutoff are **not in training data**.
Never assert what a specific manuscript proves from memory. The repo states the claim; the prior states
what was known before it.

## 1. Try the internal consequence proxy first, and measure it

Before ranking anything, test whether influence is measurable inside the corpus. Match each family's
own title against the corpus's bibliographies:

```python
allbib = " ".join(open(b, encoding='utf8', errors='replace').read().lower()
                  for b in glob.glob('preprints/*/*.bib') + glob.glob('preprints/*/*/*.bib'))
hits = [r['fam'] for r in rows if " ".join(re.split(r'\s+', r['title'].lower())[:6]) in allbib]
```

Catalog result: **14 of 372.**

That count reproduces, and its conclusion does not. Measured 2026-10-07 by
`python3 notes/scripts/extract_links.py`, which prints this proxy as a report line:

- The snippet scans `preprints/*/*.bib` + `preprints/*/*/*.bib` = **417 of the 501** `.bib` files; the
  77 at depth 4 are outside it. Over all 501 the same title rule gives **18**.
- It concatenates every bibliography, so a family matched in **its own** `.bib` counts. With an
  ownership test: **10** cross-family over 417 files, **12** over 501.
- The corpus is lowercased, not normalized. Normalizing it (punctuation stripped, every `the` dropped)
  and using the full title gives **23** any / **12** cross-family — the rule shipped in
  `notes/links.tsv`. Corpus normalization is the dominant knob: it moves 5 to 23.

Meanwhile the release's own citation edges are in those same bibliographies as URLs: **397**
release-labelled `.bib` entries resolve to **396** manuscript→manuscript edges over **158 of 372**
families, **105** crossing a family boundary, plus **213** body hrefs (`notes/links.tsv`). The
manuscripts *do* cite each other; a title phrase is simply not how the release writes a citation.

So the course change is narrower than "consequence is unmeasurable". What is unmeasurable is the
**type** of each edge — the release records no builds-on / contrasts-with / refutes relation — so a
consequence ranking stays **prior-based and must be labelled as such**, and you may quote the 396
edges as evidence that a result was cited, never as evidence that it mattered. Do not build a
consequence score on intra-corpus edges, and do not report the title-phrase count as a citation count.
See `notes/links.md` for the full rule grid.

## 2. Get the claim set from the ledger, then check the correlation

Named-conjecture resolution is the useful claim set: `resolves_named` set **and** a `resolution`
shape → 139 of 372 families. Cross-tab it against the formalization tier before ranking:

```
139-set:  T3 52   T2 36   T0 51     (tier totals: T3 127, T2 108, T1 0, T0 137)
233-set:  T3 88   T2 57   T0 88     (resolves_named alone)
```

Quote the set with its rule: `T3 88 T2 57 T0 51` is not a row of either — it splices the 233-set's
T3/T2 counts onto the 139-set's T0 count and sums to 196. Measured 2026-10-07 from
`notes/catalog.tsv`; the 139 rows in `notes/conjecture-standing.tsv` carry the 139-set split.

**Tier and named-resolution are uncorrelated.** 51 families that resolve a named conjecture have zero
formalization signal. Lead with that: the corpus's boldest claims are its least-certified ones. It is
a structural fact, not a criticism, and it tells you the ranking has to read below the coverage layer.

## 3. Calibration gate: read the scope notes before ranking

Ranking titles is how you get this wrong. Titles over-sell. Measured in `overview.tex` abstracts:
`"as a consequence"` 1, `"corollary"` 0, `"we also prove"` 0, `"as an application"` 0 — the release's
own abstracts are single-claim and state no corollaries.

Worked deflations, the model for what a prior does to a headline:

| Family | Title reads as | Prior says |
|---|---|---|
| 002 | "The full Birch–Swinnerton-Dyer formula" | Corank 0 and 1 cases were largely established (Kato, Skinner–Zhang, Greenes). Consolidation, not a Clay-problem resolution. `resolves_named = 0` agrees. |
| 074 | "Kakeya in three and four dimensions" | ℝ³ announced resolved by Wang–Zahl in early 2025. The 3D half is a re-proof; the 4D half is the news. One family, two surprises. |
| 165 | "Exact crossing numbers of complete graphs" | The Harary–Klein formula was disproved ~2019 (de Klerk–Pach–Tóth). "Exact" must mean something else. |
| 095 | "Hyperbolicity cones without semidefinite lifts" | Counterexamples to the generalized Lax conjecture were known (Brändén–Kasperczyk). Expected-shape. |
| 014 | "Restricted geometric Langlands" | Full geometric Langlands for curves proved by Gaitsgade–Raskin in 2024. A restricted, conditional result in a recently-resolved area is low consequence. |

Every deflation is a case where the title outran the prior. That is the deliverable the user cannot
get from the repo.

## 4. Tier the ranking, and carry a confidence column

Rank by distance from the prior, not by fame:

- **Tier 1 — the prior says this should not have been possible yet.** Hilbert's tenth over ℚ (004,
  reduces to defining ℤ in ℚ; no route known for ℚ). Zilber–Pink in abelian varieties (016, a 20-year
  partial-results program: Pila, Habegger–Pila, Gao–Habegger–Pila, Kühn, Zhang). Goldfeld's conjecture
  (006, known only for special families). Fontaine–Mazur modularity at **p = 2** (010 — Kisin's
  lifting is p ≥ 3; p = 2 is the known hard case, and under-publicised). Artin's primitive root for
  every base (029, Hooley needs GRH). Log abundance (034, central open MMP conjecture). 3D
  Bochner–Riesz (078) and restriction (077).
- **Tier 2 — famous, prior says plausible-but-unachieved.** Margulis–Platonov (018), rational Hodge
  for CM abelian varieties (032 — much is known for divisors and K3-type fourfolds via Voisin, so read
  the scope first), LeBrun–Salamon (062), Falconer distance (073), Hilbert's 16th limit cycles (143).
- **Tier 3 — the prior deflates the headline.** Section 3.

Ship it as a table with a **`prior_confidence`** column. The frontier is exactly where training data is
thinnest and stalest, and Tier 3 is what a low-confidence prior looks like when checked. Confidence is
in the *prior*, not in the result.

Shipped 2026-10-07 as **`notes/conjecture-standing.tsv`** — 139 rows, 10 columns
(`fam discipline tier conjecture standing_prior_2025 prior_confidence release_claim gap
surprise_tier abstract_line`), with `notes/conjecture-standing.md` for the scheme and
`notes/scripts/verify_conjecture_standing.py` as its checker. Measured yields: surprise tier
1:60, 2:64, 3:11, 4:4; confidence high 42, medium 84, low 13; all 139 anchors resolve to their own
`\resultentry` line. Two things the shipped table does that the scheme above only asks for: the
standing column is **named** `standing_prior_2025`, so the labelling is structural and cannot be read
as a fact; and the `abstract_line` column makes every row checkable against the line it reads, which
is what caught three rows naming a conjecture the abstract does not name (266, 310, 326) and one
mis-cited anchor (187).

## 5. Name and topic queries have three layers, and they disagree

For "find all the Cauchy-related / manifold-related proofs", measure all three layers before
promising an index:

| term | in catalog titles | dirs whose `.bib` cites it | dirs whose `.tex` mentions it |
|---|---|---|---|
| Cauchy | **0** | 9 | **432** |
| manifold | 32 | 127 | 199 |
| ergodic | 6 | 41 | 55 |
| Langlands | 2 | 15 | 20 |

Full-text keyword search returns 60% of the corpus and answers nothing — Cauchy-Schwarz and Cauchy
sequences are tools, not subjects. Title search returns zero. The bibliography layer is the only one
that means *this work engages Cauchy's*.

**Conclusion: relation-typed edges, not a keyword bag** — `named-in-title` / `cited-in-bib` /
`mentioned-in-body` as three distinct edge types. This is an edge-*semantics* problem, not a scale
problem, so it is a schema decision made in Python, not a graph database.

Check for a curated vocabulary before designing one, because it may not exist:

```sh
grep -ril 'Mathematics Subject Classification\|\\msc\|MSC[0-9]' --include='*.tex' preprints | wc -l   # 0
grep -rho '^\s*keywords\s*=' preprints --include='*.bib' | wc -l                                     # 0
grep -rl '\\keywords\|\\subject' --include='*.tex' preprints | wc -l                                 # 12 of 722
```

Catalog: **no MSC codes, no bib `keywords` fields, author keyword lists in 12 manuscripts.** A topic
vocabulary is curated by you and validated by the generator; auto-derived terms reproduce the
432-directory Cauchy noise.

## 6. The corpus as a dataset answers "what do we learn from this"

Answer the meta-question from joint distributions, not from anecdotes:

- **Certification lags production.** 162/722 manuscripts formalized, `automation.methods: [agent]`,
  `review.status: unchecked`, zero `sorry` at source — and 51 of 139 named-conjecture resolutions at
  zero formalization signal.
- **It almost never leans on unproven assumptions.** Genuine conditional families: **5 of 372** (014,
  125, 240, 244, 282) = 1%. The keyword regex flagged 9 and 5 were false.
- **Disproving is a disproportionate share of output.** 44 tagged counterexample families, 74 genuine —
  about a fifth of the corpus. Counterexample-hunting is a search problem, and search is what sampling
  is good at. Concentrated in Combinatorics 9, Differential geometry 6, Algebraic/complex geometry 5,
  Topology 5, Algebra 4, Operator algebras 4.
- **Where it works tracks self-containedness, not importance.** Dense: combinatorics 37/33/50/19,
  theoretical CS 40/32/73/29, functional analysis 11/10/19/16. Thin: topology 18/3/26/1,
  algebraic+complex geometry 36/7/89/7, dynamics 12/9/19/2. Automated proving succeeds where arguments
  are finitary and self-contained; it stalls where a proof needs a large pre-built dependency mass.
- **The limits are catalogued, not hidden.** 227 of 405 challenge configs are not in `main_results`;
  154 of them in 108 families with zero main results. That is a release-authored list of what it posed
  and did not finish — the most informative dataset about failure modes, and it is dense JSON.
- **Results ship as clusters.** 722/372 = 1.94 manuscripts per family. Reasoning traces exist for 10 of
  372 (2.7%) — the method is almost entirely opaque.

## 7. Rules

- Label every consequence/surprise number as a **prior-based estimate**, never as a measurement.
- Quote counts from a fresh generator report; parse the ledger with
  `csv.DictReader(..., delimiter='\t')`.
- Never run `lake`, `lean`, or `comparator` to settle a ranking question.
- End with what the ranking cannot say: the manuscripts postdate the prior, no proof was checked, and
  consequence in the literature is not in the repo.
