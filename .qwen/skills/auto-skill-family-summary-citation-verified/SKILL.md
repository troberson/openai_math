---
name: family-summary-citation-verified
description: Write a per-result extended summary page (undergraduate + graduate + history + consequences
  + sources) from a manuscript's own LaTeX, then prove every numbered source marker in it by script. Use
  when asked to expand a terse catalog blurb into a real summary, to build a summaries directory, or to
  guarantee a notes page contains no invented citation.
source: auto-skill
extracted_at: '2026-10-07T09:41:32.231Z'
---

# Writing a citation-verified family summary

Worked out on the OpenAI Research Catalog (`/home/tamara/Downloads/_Git/math`), family 001 (Milne's
rationality conjecture), tier T0. The user's ask: "The summaries in contents are very terse and
high-level. Using the preprint and lean and other information about a proof, are we able to generate a
more extensive summary."

The writing is the easy half. **The verification loop is the skill** — a first draft of this page
contained 12 citation errors, all found by script, none found by reading. Budget most of the effort for
step 5.

## 0. Pick the source layer from the ledger row first

Read the row before writing a sentence: `paps`, `paps_form`, `tier`, `chal`, `mainres`, `scope_note`,
`verification`, `trace`, `shapes`, `resolves_named`, `companions`.

- **T0 (`paps_form=0`)**: no Lean, no scope note, no challenge, no trace. The manuscript LaTeX under
  `build/` is the *only* source. State it where the reader meets it — in the graduate section's
  formalization-status paragraph: "Nothing about this family is machine-checked." Not in a preamble.
- **Formalized**: read `lean/docs/<NNN>.md` first — its `## Scope` section states the exclusions,
  which are load-bearing — then the manuscript.
- Manuscripts ship LaTeX, so **PDF extraction is never needed**. Read `build/main.tex`,
  `build/sections/*.tex`, `build/references.tex`.

Label the epistemic status of every sentence: source-level (manuscript text), release-level (what
`CONTENTS.md` / `overview.tex` claims), or **prior** (the assistant's training data). "Proves" in an
abstract is a claim, not a verified result.

## 1. Capture the release's own text verbatim

Quote `CONTENTS.md` (family entry *and* manuscript entry) and the `overview.tex` `\resultentry` as
block quotes attributed with source markers (`[S1:25]`). Do not paraphrase them — the point of the
first section is that the reader can diff the new summary against the old one. **Paste, do not
retype:** these lines are long, one-per-entry, and retyping is how a paraphrase ends up inside
quotation marks. Pass C is what proves you pasted. Note that the manuscript's own abstract is usually
identical to the release's manuscript blurb (`[S3:58–64]` is word-for-word `[S1:25]`), which is worth
saying in the page. Paste the release's **words** and render its inline HTML as markdown — `<i>p</i>`
becomes `*p*`, a leading `&emsp;` goes, and a relative link it carries is rewritten with
`os.path.relpath` so it resolves from the page's own directory, link text unchanged (see the markup
trap).

**Know the shape of the entry you are quoting.** In `CONTENTS.md` a family entry is a heading line
carrying the title plus a one-paragraph summary (family 032: line 755), and each manuscript is a table
row — a `<tbody><tr>` block whose first line is the indented PDF link and whose second line is the
blurb (032's eight rows: 762/764, 771/773, 780/782, 789/791, 798/800, 807/809, 816/818, 825/827).
Quote the blurb line, never the link line: those lines start with `&emsp;` and carry markdown links, so
a "quote" of one is markup, not prose. When you quote one blurb out of many, say the row order in the
page ("The rows run products, all-surfaces, CM, locus, …, so the CM blurb is the third [S1:782]") —
that sentence is checkable and it tells the reader which of the eight you pasted.

## 2. Fixed section order

```
# <NNN> — <title> (<discipline>, <n> manuscript(s), tier <T>)
## Original CONTENTS.md summary
## Undergraduate summary        (1-3 paragraphs of prose, then the proof sketch as a distinct block)
## Graduate summary             (1-3 paragraphs: state the theorem, then the moves, then what it does not say)
## History of the conjecture    (if known)
## Consequences now that the proof has been found   (if known)
## Sources
```

### The numbered-source convention (the body names no files)

The body cites `[S4:29]` (one line), `[S4:29–56]` (a range), `[S4]` (the file itself). File names and
links appear **once**, in the `## Sources` table at the bottom. The user asked for this after seeing the
first draft: "we're using bare links with backticks and that's awkward … we could number our sources
and put the link at the bottom." ~150 long paths out of the body, 16 links total.

```
Manuscript root — `preprints/<dir>/` (author, date, N lines of LaTeX under `build/`).
S3–S12 are paths inside it; S1–S2 are at the repository root.

| # | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,169 | release family list |
| S13 | [`notes/t0-triage.md`](../../t0-triage.md) | 879 | ours, not in the release |
```

- **One row per file**, `S1…Sn` in the order the page uses them, plus a line-count column and a role
  column. State the marker grammar and that line numbers are 1-based, as in the shipped files.
- **The manuscript-root line is load-bearing, not decorative.** Both checkers parse it to resolve the
  table's relative paths. Never glob `preprints/*`: `build/main.tex`, `05_reduction.tex`,
  `references.tex` and `README.md` exist in many preprint trees, so a glob resolves to an arbitrary
  paper.
- **Write every File cell as a repo-relative path, in backticks.** The checker reads the *first
  backticked* text in the cell as the path, so a plain link cell resolves nothing and every marker in
  that file becomes `UNKNOWN SOURCE`. This matters most in a multi-manuscript family: family 032 ships
  eight manuscripts, and `build/paper.tex` exists in five of the eight trees while
  `build/sections/01-introduction.tex` exists in two (repo-wide the counts are 207 and 194). With one
  manuscript root as the first search root, a cell written
  `build/sections/01-introduction.tex` silently resolved into the CM tree and
  reported `LINE COUNT … says 156, file has 227`, while paths present in neither root resolved to
  `None` — and a `None` path is dropped from the citation set, so one bad row cascades into
  `NO CITATION in unit` for every prose unit that cites it. Spell the manuscript root out in the cell
  (`preprints/<dir>/build/paper.tex`); keep the href relative to the page directory.
- **Links are relative, not upstream.** The user's ruling: "okay, use relative links then, we don't
  need to link upstream." Every row gets a link, built with `os.path.relpath(target, page_dir)` — from
  `notes/summaries/<discipline>/` that is `../../../` for the repo root and `../../` for `notes/`,
  which is exactly what a renderer computes. Release files and our own `notes/**` rows then link the
  same way, and a local checkout resolves with no network. Once the URL can no longer say who owns a
  file, the role cell must: label ours "Ours, not in the release". A dead link is worse than no link —
  pass B resolves every href from the page directory.
- **Line anchors:** a relative link carries none; the line numbers live in the markers. GitHub's
  documented anchor is `#L29` appended to a file URL (`.../blob/main/CONTENTS.md?plain=1#L29`), and a
  markdown file needs `?plain=1` before the anchor (`CONTENTS.md?plain=1#L16`) because GitHub renders
  markdown as prose with no line numbers. Range anchors are not documented for markdown files, so a
  range marker resolves to its first line. Say these rules in the page; do not write an anchor form you
  have not seen documented, and write a worked example as `.../blob/main/…`, not as a `<owner>`-style
  template — angle-bracket placeholders trip the page's own HTML scan.
- **Apply the numbering by script, never by hand.** Rewrite the draft's `file:line` citations as
  markers (skip fenced code and verbatim block quotes; copy verbatim any name that is not in the
  numbering map — the "Absent by construction" list deliberately names files that do not exist), then
  grep for leftovers: `` `(?:[^\s`]*?/)?[A-Za-z0-9_.-]+\.(tex|md|tsv):\d+` `` and `` `:\d+` `` must
  both return zero.
- **The Sources table is the resolver.** Once the file name leaves the body, passes B and C can only
  resolve `S5` by parsing that table — so the table is checked data, not prose, and pass B checks its
  declared line counts against the files on disk.

No preamble between the title and the first heading, and no provenance lead-in under a heading either —
the user called both metacommentary unnecessary. "Source-level, from the manuscript's own …" and
"Every attribution below is the manuscript's own `\cite`" are the pattern to avoid. Provenance is
carried by the citation on each claim, not announced per section; the ledger row is read, not quoted.
The one label that stays is inline: **Prior (my training data, not this repo).** at the start of a
paragraph that is not repo text.

The undergraduate and graduate sections are the **same argument at two depths**, so the sketch in the
undergraduate section must map one-to-one onto the moves in the graduate section. The 1–3 paragraphs
are prose; the proof sketch is a **distinct block after them with a bold lead-in and no heading of its
own** — the graduate section does exactly this with its numbered moves, so the undergraduate section
gets the same four moves in plain language. Rules that keep the undergraduate register honest: no word
appears that the section has not defined in the same sentence — no quasi-isogeny, no filtration, no
Rosati, no "Lefschetz"; and the sketch is sourced, not invented. Many manuscripts ship a survey-level
proof overview (001: `00_intro.tex:186`–`:265`, four labelled stages, plus a figure whose caption
separates the two transports) — translate that. When a manuscript has no such overview, assemble the
shape from the section headings and say in the page that the ordering is the page's reading of the
section order, not the manuscript's own framing.

## 3. History and consequences come from the manuscript's own `\cite`s

Do not write history from memory. Extract the intro's origins/antecedents subsection and rebuild each
attribution from the `\cite[locator]{key}` the manuscript itself uses, then resolve `key` in
`references.tex` (these bibliographies are `\begin{thebibliography}` with `\bibitem` — **not** BibTeX,
so `grep '^\s*@'` and `grep 'title\s*='` return nothing).

This is where drafts go wrong. In this session the first draft claimed, from prior, that Milne 2025
"proves the CM case" (it gives a *conditional* criterion), that Markman's theorem concerns CM by an
imaginary quadratic field (it concerns abelian fourfolds of Weil type and sixfolds of split Weil type
in characteristic 0), and placed a lifting question in the wrong subsection. All three were fixed by
reading the manuscript's `\cite` locators.

Quarantine the training-data background in one clearly marked **prior** paragraph per section, and end
it with the honest limit ("I have not seen this result and cannot confirm it independently").

## 4. Grep the release's adjectives before repeating them

Release blurbs add qualifiers the theorem does not contain. Here `CONTENTS.md:25` says "every rational
Hodge class **whose specialization is defined over the prime field**"; `grep -rn "prime field"
build/` returns **nothing**, and `thm:main` has no such hypothesis and no polarization hypothesis.

So: before any phrase from a blurb appears in your own prose, grep it in the manuscript. If absent,
record it as a release gloss in the page — and make sure no other section quietly asserts it.

Cross-family dependencies: check the ledger's `companions` column and the manuscript's `\cite` of a
sibling release entry. State the manuscript's own disclaimer about the dependency (001 cites family
032's CM Hodge theorem for the algebraicity corollary and states twice that the main theorem's proof
is independent of it).

## 5. Verify every citation by script — three passes, in this order

**Pass A — needle check.** Hand-list `(file, line, needle)` for every load-bearing citation and assert
the needle is on that line. Print the real line on a miss, and search ±8 lines for it so the fix is
immediate.

**Pass B — extract from the finished document.** Do not trust pass A to cover the document. Parse the
markdown you just wrote, resolve every marker through the Sources table, and print the real line:

```python
ROW    = re.compile(r"^\|\s*(S\d+)\s*\|\s*(.+?)\s*\|\s*([\d,]+|—)\s*\|\s*(.*?)\s*\|\s*$")
CELL   = re.compile(r"`([^`]+)`")                                  # the path inside the row's cell
MARKER = re.compile(r"\[S(\d+)(?::(\d+)(?:[–-](\d+))?)?\]")        # [S4] [S4:29] [S4:29–56]
# The Sources table IS the resolver: {S#: (rel, path)}. Resolve rel against the manuscript root named
# in the Sources prose FIRST, then the repo root, and print a loud note for any name that exists
# under both — a bare `README.md` is 18 lines in the preprint and 50 at the repo root.
PRE = None
for line in doc_lines:
    m = re.search(r"`(preprints/[^`]+)`", line)
    if m: PRE = ROOT / m.group(1); break
roots = ([PRE] if PRE and PRE.is_dir() else []) + [ROOT]
# Flag: unknown source, file not on disk, out of range, blank line, reversed range.
# Then check the table's own claims: declared "Lines" vs len(path.read_text().splitlines()).
# Report declared-but-never-cited sources as information, not as a problem.
# Scan raw HTML: ENTITY = re.compile(r"&(#[0-9]+|[a-zA-Z][a-zA-Z0-9]*);"), TAG = re.compile(r"<[a-zA-Z/][^>]*>").
# Require **zero hits anywhere in the page, block quotes included** — the release's inline HTML is
# rendered as markdown when the quote is pasted (see the markup trap below), so a surviving tag or
# entity is a paste artifact, not source text.
# Resolve every markdown link from the page's own directory: LINK = re.compile(r"\]\(([^)\s]+)\)");
# flag an http(s)/mailto href (this page links relatively), a bare `#` anchor, an href whose
# (page_dir / href).resolve() is not a file, and a target that leaves the repo. Count the links and
# print the count in the summary line, so a row that lost its link shows up as a smaller tally.
```

Pass B is what makes the page trustworthy: it catches markers you wrote and never listed, and it
catches a table that lies about a file's length. Expect ~170 positions on a 290-line page. Iterate
until **0 problems**, then re-run after the last edit — the tally you report is from that final run,
not from an earlier one.

**Pass C — quote fidelity. Pass B proves a cited line *exists*; it proves nothing about the text you
attribute to it.** A paraphrase dressed as a block quote sails through pass B, and one did ship: a
`CONTENTS.md:25` block quote that said "including every rational Hodge class whose specialization is
defined over the prime field" — a sentence that appears nowhere in the release for this family — plus
an invented `([manuscripts](#fam-001))` anchor. Pass C pairs every quoted span with the citations in
its unit and asserts the span is a substring of the cited text:

```python
QUOTE = re.compile(r"“([^”]{6,})”|\"([^\"]{6,})\"")
# Join wrapped prose/bullet lines into logical units; a block quote is its own unit, attributed by
# the markers on the line above it. For each unit, collect every marker as a candidate position
# ([S4:29–56] is one candidate; a bare [S4] is the whole file). A span passes if it matches ANY
# candidate — do not try to parse which marker "owns" the quote; that parser is fragile and the
# property that matters is "this text exists at a cited position nearby".
# Skip: units containing the inline **Prior** label (not repo text), and spans under 12 characters
# (those are terms under discussion, e.g. "proves", not quotations).
# Keep the haystack STRICT: lines a–b only, no forward slack. A quotation that spans two source lines
# must cite both ([S9:361] failed for a sentence occupying 361–362; the fix is the citation, never a
# wider haystack).
```

Normalize both sides before comparing, and make the normalization markup-aware as well as
LaTeX-aware: the source writes `Theorem~\ref{thm:main}` and the page renders "Theorem 1", so strip
`\ref{}`-family commands, strip LaTeX macros and `~`, strip the number the page substituted after a
theorem-type word, and collapse space-before-punctuation (stripping the ref leaves `Theorem .`, which
otherwise fails the substring test against the page's `Theorem.`). Strip inline HTML tags **to
nothing** — the release's `<i>p</i>` must match the page's `*p*`, and replacing a tag with a space
leaves `prime-to- p`, which fails against `prime-to-p`. Strip leading `../` sequences too: the page
links relatively (`../../../CONTENTS.md`) while the release spells the same target as a repo-relative
path, so a quoted link must compare equal to the line it cites.

**Prove the pass discriminates before trusting it.** Mutate the finished page twice — paraphrase one
block quote and invent one inline quote at a real citation — run pass C on the mutants, and confirm
both are flagged while the real page is clean. A green pass you have never seen go red is not a check.

## 6. Traps (each one fired in this session)

- **Never glob `preprints/*` to resolve a manuscript path.** `build/main.tex`, `05_reduction.tex`,
  `references.tex`, `README.md` exist in many preprint trees, so `next(dir for dir in glob)` picks an
  arbitrary paper and every range check goes red at once (`S10:222 -> references.tex (file has 216
  lines)` when the real file has 274). Resolve through the manuscript root the Sources section names.
- **A bare relative name is ambiguous between the two roots.** `README.md` is 18 lines in the preprint
  and 50 at the repo root. Resolve manuscript-first, and print a loud note when a name exists under
  both roots — a silent pick here reads as a line-count error in the table.
- **A hand-written range can split into three markers.** `` `05_reduction.tex:361`, `:443`–`:448` ``
  numbered as `[S9:361], [S9:443]–[S9:448]` because the comma closed the marker and the tail
  self-closed. One range per marker (`[S9:443–448]`), then grep the finished body for a `–` outside a
  marker.
- **A transform branch that can never fire looks like success.** `key = m.group(1) if m.re is not TAIL
  else None` followed by `if key not in NUM:` sends every tail down the verbatim-skip branch (`None
  not in NUM` is true), so the stats read `tail: 0` while the output mangles every range into
  `[S4:29]–`:56``. Print per-category counts, expect them non-zero, and grep for leftovers.
- **Invented range ends are off by one.** A range ends at the last *content* line; the line after it is
  blank. `:90`–`:91` when the text ends at `:90`. Check both ends of every range.
- **Path routing.** `references.tex` sits in `build/`, the sections in `build/sections/`. A checker
  that assumes one layout crashes mid-run and silently skips its trailing diagnostics.
- **Accents.** The source writes `Andr\'e`, so a needle `Andre's` never matches. Use accent-safe
  substrings.
- **Environment names.** `\begin{corollary}[The divisor filtration condition]` — do not assume the
  block is a lemma because your prose calls it one.
- **Labels live where they are declared.** `lem:lift-hom` is `01_preliminaries.tex:158`; the line
  number copied from a neighbouring file pointed at an unrelated lemma. `grep -rn "label{lem:x}"`.
- **Line counts.** Use `len(text.splitlines())` / `wc -l`, not a viewer's count (trailing newline adds
  one). Verify every number in the Sources table, plus any aggregate ("3,065 lines of LaTeX under
  `build/`", "35 `\bibitem`s"). Pass B checks the table's declared counts against the files, so a
  stale number fails the run instead of sitting in the page.
- **A claim belongs to the corollary that states it.** "including `p = 2`" appeared twice, in two
  different corollaries; the draft cited the algebraicity line for the good-theory corollary.
- **Quote counts only from a fresh run** — ledger row, companions-edge count, totals. Never from an
  earlier run's output.
- **A paraphrase inside quotation marks is a fabrication.** It is the failure pass B cannot see, and
  it is the failure that shipped here: two "verbatim" `CONTENTS.md` block quotes that were my own
  paraphrase, one carrying a "defined over the prime field" gloss that appears nowhere in the release
  for this family, and a graduate-section paragraph built to argue about that invented gloss. If you
  cannot paste the source text, do not put it in quotes — write it as your own prose.
- **Verbatim covers the words, not the markup.** The release writes inline HTML in its blurbs — this
  page quotes text that ships as a leading `&emsp;` and as `prime-to-<i>p</i>`. Render that markup as
  markdown when you paste (`<i>p</i>` → `*p*`, drop the leading `&emsp;`) and keep the words
  byte-identical; the user's ruling: "I think formatting is outside the scope of 'verbatim'." Record the
  conversion in the Sources row's role cell so the reader knows the quote is not byte-for-byte, and
  require **zero HTML anywhere in the finished page** — a surviving tag is a paste artifact, not source
  text. A relative link pasted from `CONTENTS.md` is dead from `notes/summaries/<discipline>/`, so
  rewrite it with `os.path.relpath(target, page_dir)` and keep the link text unchanged. Pass C must
  then normalize tags to *nothing*, not to a space — `prime-to-<i>p</i>` has to match `prime-to-p` —
  and strip leading `../` so the rewritten link still matches the release's repo-relative path.
- **Never write an anchor you have not seen.** `grep` the target file for the anchor before linking to
  it. The page linked `(#fam-001)`; `CONTENTS.md` contains no anchors at all, and repo-wide `](#`
  matches only TikZ source. An anchor you invented resolves to nothing and looks fine in a preview.
  Same rule for URL forms: markdown files need `?plain=1` before `#L16`, range anchors are not
  documented for markdown files, and permalink snippets do not work in markdown files — all verified
  against the GitHub docs before writing the Sources section.

## 7. Report

State the verification tally (positions checked, misses), the corrections the loop forced, and then
**what has not been checked**: the mathematics itself (no Lean run — repo rule), prior sections
(uncorroborated in repo), the release glosses, the PDF (LaTeX read instead). Do not commit without the
user's word.

Keep the verifier. The pass B and pass C checkers are promoted: `notes/scripts/verify_summaries.py`
is the standing checker for `notes/summaries/`, so every page is one command away from green —
no arguments checks every page, named pages check just those, and `--mutant` proves the quote check
discriminates. Pass A stays per-page: its needles are that page's own recorded findings.

## Related skills

`proof-triage` is the router for the ledger and the tier/shape vocabulary this page starts from; it
also carries the never-run-Lean rule. `corpus-finding-surprise-ranking` supplies the
surprise = claim − prior framing and the prior-labelling discipline used in the history and
consequences sections.
