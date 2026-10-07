---
name: lean-formalization-coverage-audit
description: Measure how much of a manuscript collection is actually formalized in an accompanying
  Lean library, check the non-Lean evidence its manuscripts ship (verification scripts, coverage
  documents, provenance notes), and report the gap without overstating what it proves.
source: auto-skill
extracted_at: '2026-10-07T05:29:45.327Z'
---

# Auditing Lean formalization coverage

Use when asked how much of a paper/manuscript collection is formalized, how complete the
formal proofs are, or what the formalization gap is. Worked out on the OpenAI Research
Catalog (`/home/tamara/Downloads/_Git/math`): 722 manuscripts, 372 families, a 25.9M-line
`OAI/` Lean library.

## 1. Report coverage as separate layers — never as one percentage

The catalogue records coverage at four layers that **do not agree**. Averaging them, or
picking one and calling it "the coverage", is the main way to get this wrong.

| Layer | Where it lives | Catalog value |
|---|---|---|
| Manuscripts with a formalized main result | `formalization.yaml` → `sources:` (`id: ../preprints/<dir>/<file>.pdf`) | 162 / 722 |
| Families with a scope note | `lean/docs/<NNN>.md` | 235 / 372 |
| Statement/solution pairs | `lean/ComparatorChallenges/*.json` (+ matching `.lean`) | 405 |
| Catalogued main results | `formalization.yaml` → `status.main_results` (`comparator_config:` / `declaration:` / `file:`) | 185 entries, 178 unique configs |

- Count entries with `grep -c 'comparator_config:'`, then `sort -u` the extracted names —
  some configs appear 2–3× (multiple main declarations per challenge). Entries ≠ unique configs.
- Challenges not listed in `main_results` are companion/secondary statements, not failures.
  They are still linked from a family scope note.
- `status.scope`, `automation.methods`, and `review.status` are the release's own statement of
  how the proofs were produced. Quote them verbatim; they set the ceiling on any claim of verification.

## 2. `solution_module` is an import shim — follow the transitive closure

The decisive measurement (are the proofs complete?) requires resolving imports. A comparator
config points at a module whose file is often **one line**:

```json
{ "solution_module": "OAI.Geometry.BallPacking.Necessity.Main",
  "theorem_names": ["OAI.HigherDimensionalBallPacking.packing_necessity"] }
```

```console
$ cat OAI/Geometry/BallPacking/Necessity/Main.lean
import OAI.Geometry.BallPacking.Necessity.PackingNecessity
```

Checking that file for `sorry` finds nothing and proves nothing. Build a module→file index
(`mod2file`), parse `^\s*import\s+([A-Za-z0-9_.]+)` per file, and walk the closure:

```python
def closure(mod):
    seen, stack, bad = set(), [mod], []
    while stack:
        cur = stack.pop()
        f = mod2file.get(cur)
        if f is None: bad.append(cur); continue   # Mathlib / external deps: expected
        if f in seen: continue
        seen.add(f); stack.extend(imports[f])
    return seen, bad
```

Aggregate `sorry`, `axiom`, `native_decide`, line counts over the closure. Cache per-file
declaration sets — scanning 121k files once is fine; rescanning a closure per declaration name
is not.

## 3. Three false-positive traps (all three bit me)

- **Paths with parentheses.** `preprints/Sharp-integral-fillings-in-CAT(0)-spaces-.../paper.pdf`
  breaks `\(preprints/([^)]+\.pdf)\)` and silently loses a manuscript. Use
  `preprints/(?:[^\s()]|\([0-9]+\))*\.pdf`. My first pass reported 721 of 722 and I nearly
  reported a missing entry in `CONTENTS.md`.
- **Namespace-qualified declarations.** `OAI/RepresentationTheory/RowColumn/Occupied.lean:274`
  is `theorem RowColumn.occupied_overlap` inside `namespace OAI`. Matching the last dotted
  segment (`occupied_overlap`) against a captured leading identifier finds nothing → 7 phantom
  "missing declarations". Match the qualified tail against the file text, not against a
  single-token capture.
- **`axiom` in prose.** `^\s*axiom\s` matches doc-comment text
  (`/- ... the axiom of choice is used ... -/`). All 3 "axioms" in the library were comments.
  Read the matched line before reporting an axiom.
- **Braces inside `overview.tex` abstracts.** `\resultentry{NNN}{title}{abstract}{links}` and
  abstracts are full of braces (`$\mathbb A^4$`, `\href{...}{...}`), so a regex for "the next
  `{...}` group" cannot work. Count braces:

  ```python
  def group(s, i):              # s[i] == '{'
      d, j = 0, i
      while True:
          j += 1
          if s[j] == '{': d += 1
          elif s[j] == '}':
              if d == 0: return s[i+1:j], j+1
              d -= 1

  for m in re.finditer(r'\\resultentry\{(\d{3})\}', tex):
      i = m.end(); title, i = group(tex, i); abstract, i = group(tex, i)
  ```

  Assert the parse count equals the family count (372) before using any abstract.
- **`Path` vs `str` in a membership test.** A generator that builds a reference set of directories
  (`{p.parent for p in root.glob("*/verification")}`) and then tests membership per row using a
  *string* row value makes every test false: `str in {Path(...)}` never matches. The column reads 0
  for every row, which is indistinguishable from a genuinely empty column — three evidence columns
  here were quoted as empty for a whole project before anyone noticed. Key the reference set on the
  same type as the tested value (`p.parent.name`), and make the generator print the repo-wide sum so
  a zero column is visibly wrong. Then check for basename collisions before trusting name-keying
  (here: 30/30, 4/4, 2/2 unique, so it is safe). Repaired values: 30 verification dirs over 22
  families, 4 `INPUTS.md`, 2 `COVERAGE.md`.

## 4. Say what a zero-`sorry` result does and does not mean

Zero `sorry` across 25.9M lines is a **source-level** fact. It does not mean the library
elaborates, and it is not verification. State the distinction explicitly, then give the
command that produces the checked fact:

```sh
lake update && lake exe cache get
lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json
```

That needs `comparator`, `landrun`, `lean4export` on `PATH` and a full build. If you have not
run it, say so. Do not present a source scan as a comparator pass, and never as peer review.

## 5. Attribute the gap by discipline

Map family → discipline from `overview.tex` section order (`\cataloguesection{...}{n}` sets the
current discipline; each following `\resultentry{NNN}{...}` belongs to it). Family → manuscripts
comes from `CONTENTS.md` (`**NNN. Title**` headers, then `(preprints/...pdf)` links). Then tabulate
per discipline: families, families with a scope note, manuscripts, formalized manuscripts.

Expect strong skew. Catalog result: Topology 3/18 families and 1/26 manuscripts covered,
algebraic geometry 7/36 and 7/89, versus functional analysis 10/11 and 16/19, logic 6/6 and 5/8.

Worth checking separately: **the marquee results.** Ten of the twelve headline number-theory
families (Milne, full BSD, Hilbert's tenth over ℚ, Goldfeld, Fontaine–Mazur at 2,
Ford–Konyagin–Luca, restricted geometric Langlands, Zilber–Pink, Margulis–Platonov, p-adic
section) have no scope note, while all 10 families with published reasoning traces do. Lead
with that pattern when it holds — coverage tracks what the release chose to expose to checking,
not what the community will scrutinize.

## 6. Reading the scope notes

`lean/docs/<NNN>.md` has an explicit **Scope** section stating what the Lean result covers and
what it excludes (003: the paper's later applications are not formalized; no explicit
Landau–Siegel constant). Quote exclusions when judging a result. Absence of a formalization
carries little signal in a collection where most manuscripts are unformalized — do not treat it
as a red flag.

## 7. Tooling notes

- `rg -f patterns.txt` with patterns ending in `\n` fails even with `-U` ("the literal `\n`
  is not allowed in a regex"). For per-file declaration sets, scan in Python.
- Building the graph over 121,734 files takes ~1 min; pickle it (`/tmp/graph.pkl`) so follow-up
  questions don't rescan.
- `du -sh lean/OAI` ≈ 1.7 GB. Compiling the whole library can fail on low `vm.max_map_count`;
  see `lean/README.md` (`-DMMAP=OFF`, `GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1`).
- Also worth counting: `preprints/*/verification/` dirs (reproducible arithmetic checks, 30 in
  the catalog) and their `COVERAGE.md` limits files.

## 8. Triage the tier with no coverage signal

When a tier has no scope note, no comparator challenge, and no formalized manuscript, claim shape is
the only discriminator left. Check the derived identity first: if the top tier is defined as
"families with ≥1 formalized manuscript", the zero-signal tier has **0 formalized manuscripts by
construction** — sum the formalized column over it, confirm 0, and say so, because it stops "not
formalized" from being read as a finding.

- **Bucket by first match, and label the buckets as ordering only.** Shapes are multi-label (66
  families match ≥3 shapes, 57 match none), so a partition is a triage device, not a taxonomy.
  Order buckets by how cheaply the claim can be checked, not by importance: counterexample (names a
  concrete object — cheapest), resolution (largest claim, no evidence), bound, classification,
  uniform, other, untagged. Print a reconciliation line: bucket families and manuscripts must equal
  the tier totals exactly (137 / 255 in the catalog).
- **Choose the reading subset from three overlapping criteria and quote the union, never the sum:**
  the counterexample bucket ∪ the marquee id range (the opening families of the release's most
  prominent discipline) ∪ families with ≥3 manuscripts. Catalog: 16 ∪ 15 ∪ 22 = **44 families, 134
  manuscripts**; the per-group manuscript counts (29 / 36 / 104) overlap and never sum to 134.
- **Scope qualifiers live in abstracts, not titles.** "the discriminant threshold is ineffective",
  "retain their stated height, renormalization, and field-input assumptions", "under the stated
  marked-boundary approximations", "for some sufficiently large even N", "the required nuclear charge
  is specified nonnumerically". Record them per family — a title-level taxonomy cannot see them, and
  they are what a reader needs to judge the claim.
- **A keyword tag is not a claim.** The `conditional` tag flagged 9 families; reading found 5. Every
  tag needs a reading pass before it is quoted as a property of a family, and a reading pass is
  allowed to move a family out of a bucket.
- **Tags omit as well as mislabel — measure both directions.** The `counterexample` tag matches 44
  families while 74 use counterexample language in title or abstract; of the 31 untagged flags, 30
  were genuine on reading (the false positive matched only through "nonnegatively"). Report tag
  counts as floors, and search for the shape's language outside the tagged set before treating a
  bucket as a census. Widening a rule is a generator change: measure its yield the way the
  `conditional` audit recorded it, and do not silently retag.
- **Expect the taxonomy to be silent.** 20 of 137 T0 families carry no shape tag at all, including
  marquee-grade results. Say that plainly rather than forcing them into a bucket. Reading the
  untagged set settled most of them: 9 of 15 resolve a conjecture named in the title, 1 is a
  counterexample, 3 resist the vocabulary entirely.
- **Close with what was not read** — here, abstracts are the release's own source-level assertions,
  not verified results: no manuscript PDF was read, no proof was checked against the conjecture as
  stated in the literature, and no Lean was run. State the remaining gap in families and
  manuscripts; after the second pass this catalog's zero-signal tier is fully read at abstract
  level (44 families / 134 manuscripts, then 93 / 121), so the gap is depth, not coverage.

## 9. Check the evidence that ships with a result

A family with no Lean coverage can still ship executable support. Checking it is cheap and it is
where a coverage audit finds its most actionable facts. Worked on the 21 counterexample-shaped
families of the zero-signal tier (34 manuscripts): all 21 had no scope note, no challenge, no main
result and no trace, so the abstract was the whole evidence.

- **Record one object and one broken conjecture per counterexample family, plus its construction
  mode.** Mode = **E** when the abstract names a constructed object, **X** when the object is
  indexed by an unspecified parameter, plus a mixed case. Catalog: 14 E / 6 X / 1 mixed. The X rows
  are the ones to read first — the claim is stated with a free parameter, so the object is not
  pinned. This is a cheap, checkable classification and it survives a change of taxonomy.
- **Run the shipped scripts, in a temp copy, with assertions on.** `python3` from stdlib only; copy
  out of the repo so nothing writes into it. Report the scripts' own success strings, not your
  interpretation. Only 2 of 21 families shipped runnable checks, and both passed inside limits they
  state themselves: "it does not certify the topological or lattice-theoretic parts of the proof",
  "Successful execution means the programs' assertions hold; it does not independently verify their
  analytic interpretation or the full theorem." **Execution is replay, not review** — say which one
  you performed.
- **A coverage document is not coverage.** When a family ships a `SUPPORT-COVERAGE.md`, check that
  every artifact it names exists on disk and in `git ls-files`. Family 318 names
  `support/r-ce/ce_certificate.py`, its `.json`/`.txt` transcripts, `BUILDING.md` and
  `SUPPORT-COVERAGE.json`; none exist. The same file also says "No Lean source or Lean verification
  is supplied for this article." Never describe a family as having support from the existence of a
  document *about* support. A ledger with a boolean column for such a file cannot express "named, not
  shipped" — record it as a finding, not a count.
- **Read `INPUTS.md` before treating it as an input list.** Family 259's is a provenance caveat:
  "The available source record does not establish that it was the final revision of that argument."
  That is a statement about the evidence chain, and it belongs in the family's record.
- **"Explicit" can be explicit in form only.** Follow a certificate's own formula to a number.
  Family 059's certificate reports ambient dimension `4*s0+16` with
  `s0 = 4*sum_abs_e + 2*sum_e + common_tail_variable_count_per_side + 2`; at the supplied instance
  s0 = 1.1439…×10¹⁴³, i.e. ~4.58×10¹⁴³ variables. The construction is named, and unusable as a
  concrete object. Quote the formula, not a rounded exponent — mis-transcribing an exponent is how
  this finding nearly became wrong.
- **Depth is usually available offline.** Check `preprints/<dir>/build/*.tex` before proposing a
  toolchain: all 34 manuscripts here ship LaTeX (2–17 `.tex` each), so reading a proof needs no
  Lean, no build, and no network.

