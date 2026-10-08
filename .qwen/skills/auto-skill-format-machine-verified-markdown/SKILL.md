---
name: format-machine-verified-markdown
description: Decide whether a formatter (prettier et al.) can be run over a markdown tree that regex-based checkers verify — probe the formatter's byte-level rewrites, enumerate every place a checker keys on byte form, map files to their readers, and put scoped options to the user.
source: auto-skill
extracted_at: '2026-10-08T14:39:31.948Z'
---

# Formatting markdown that a checker reads

Worked out on `/home/tamara/Downloads/_Git/math` for the request "let's run our markdown files
through prettier". The repo's only test suite is regex checkers over hand-written markdown
(`notes/scripts/verify_*.py`). The formatter turned out to be **incompatible with the checker layer in
two unconfigurable ways**, so the answer was a scoped subset, not a global format pass. Nothing was
formatted; the decision went to the user with measurements attached.

**The core hazard: a formatter's normalization is invisible to a checker, and invisibility reads as
success.** A quotation pattern that stops matching injects no problems — it verifies nothing and
prints green. That is the same failure mode as a pass whose adjacency window can never be true
(`notes-page-checker-traps` §2), caused from outside the checker.

## 1. Probe the formatter before touching a repo file

Never start with `--write`. Build one `/tmp` probe file containing the byte forms your corpus
actually uses, run the formatter on it, and `diff -u`:

```bash
printf '%s\n' 'Literal *star* and 2 * 3 = 6.' \
  'Underscore _emph_ and main_results and __pycache__/ and a\_b.' \
  'A *not imposed* clause with **bold** and `code *x*`.' > /tmp/t2.md
./node_modules/.bin/prettier --config /tmp/.prettierrc /tmp/t2.md > /tmp/pv2.md; diff -u /tmp/t2.md /tmp/pv2.md
```

Run it from the repo root (`./node_modules/.bin/prettier`), not from `/tmp` — `npx` in `/tmp` fails
with `npx canceled due to missing packages and no YES option`.

Measure the corpus the same way (report-only python, no writes): count the byte forms the formatter
rewrites, and count how many of them sit **inside quotations** — those are the ones a checker will
fail.

```python
star = re.compile(r'(?<![A-Za-z0-9_*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![A-Za-z0-9])')
q    = re.compile(r'[“"]([^”"]{6,})[”"]')
bad  = [x for x in q.findall(text) if star.search(x)]   # quotations a formatter will rewrite
```

## 2. Enumerate the checker's byte-form couplings

Grep the checker directory for the three patterns that break. This is the whole decision, so do it
exhaustively:

| Coupling | Grep | What a formatter does to it |
|---|---|---|
| Literal quotation form | `QUOTE = re.compile(r'\*"([^&#124;]{12,})"\*')` | `*x*` → `_x_` ⇒ pattern matches **0** quotations, checker goes silently green |
| Normalizer strip list | `def norm(` … `s.replace("**", "").replace("`", "").replace("*", "")` | `_` not in the strip list ⇒ rewritten quotations report `NOT VERBATIM` |
| Strict table row regex | `r'^\| (\d{3}) \| (T\d) \| (\d) \| …\|$'` | table padding (`\| A   \|`) ⇒ regex matches 0 rows |

Do **not** "fix" the strip list by adding a blanket `_` strip. Backticks strip to nothing first, so
`` `main_results` `` → `mainresults` ≠ source. Stripping must be emphasis-pair-scoped:

```python
re.sub(r'(?<![A-Za-z0-9])_(?=\S)(.+?)(?<=\S)_(?![A-Za-z0-9])', r'\1', s)
```

Also gate the count of things verified, so a formatter (or any refactor) that empties a pattern is
loud, not green:

```python
if checked < 12:
    problems.append(f"only {checked} anchored quotations verified")
```

## 3. Map files to their readers — filename grep is not enough

Which files are safe to format is a property of the checkers, not of the file. Grep each basename in
the scripts, **then separately grep for glob-based readers**, which never mention a filename:

```
glob\("\*\.md"\)|rglob\("\*\.md"\)
```

In this repo the 21 summary pages matched no script by name and are read by four of them via
`SUMMARIES.rglob("*.md")` / `(ROOT/"notes"/"summaries").glob("*/*.md")`. Only after the glob pass did
the truly-unread set come out: `AGENTS.md`, `CLAUDE.md`, and three notes docs.

## 4. Scope exclusions to state explicitly

A format pass must name what it will never touch:

- **Generated trees** — a renderer's output must stay byte-identical across runs; formatting it breaks
  the twice-run diff test. Edit the generator, not the output.
- **Mirrored upstream/release files** — a byte-for-byte mirror of someone else's release is not yours
  to restyle.
- **Tool-generated files** (issue-store READMEs, scaffolds).
- **Files with YAML frontmatter** (skills) — formatters reformat frontmatter.
- **Files with dirty working-tree state owned by the user** — leave them out of a bulk write.

## 5. Config keys worth knowing

```json
{"proseWrap": "preserve", "embeddedLanguageFormatting": "off"}
```

`embeddedLanguageFormatting: "off"` is the one that protects quoted code fences (a JSON block quote
inside a fenced block is reformatted otherwise). `proseWrap: "preserve"` keeps hand-wrapped prose.

**Check which options the installed version actually exposes** — prettier 3.9.9's markdown printer
registers only `proseWrap` and `singleQuote`:

```
var mm={proseWrap:Vn.proseWrap,singleQuote:Vn.singleQuote}
```

and it warns, not fails, on unknown keys: `[warn] Ignored unknown option { emphasisStar: true }`.
A warning is not a failure, so a config written from a blog post silently does nothing. Grep the
installed package for the option name before promising behaviour.

Measured prettier 3.9.9 markdown behaviour: `*p*` → `_p_` (unconditional, including inside quoted
spans); `__c__` → `**c**`; tables padded; padding stripped inside `` ``double-backtick`` `` spans;
list continuation lines re-indented; `main_results`, `a\_b` and code spans untouched; `2 * 3` left
alone. Check the corpus for tokens the parser will read as emphasis — `__pycache__/` outside a code
span becomes `**pycache**/` (this repo had 0 such tokens, all were backticked).

## 6. Options to present, with the cost of each

Present as plain text with a recommendation, never as a dialog:

- **A. Format only files no reader touches.** Zero checker risk, small win.
- **B. Format everything and adapt the checkers** (emphasis-pair `_` stripping, widen the literal
  patterns to accept both forms, relax strict table regexes to `\s*`, sweep the convention docs).
  Cleanest end state; edits the test suite.
- **C. Format everything plus a tracked post-pass** restoring the byte forms. Works, but the
  formatter is not idempotent on emphasis, so the restore becomes a mandatory workflow step and new
  machinery to verify.
- **D. Downgrade the formatter** to a version exposing the option. Not recommended: the pin is in
  `package.json` and the other rewrites usually stay.

After any format pass, re-run **every** checker before reporting green, and commit the config file
separately from the formatting. Run each one **twice** — plain, then `--mutant` — because the two runs
answer different questions (§7).

Recommendation rule: when the rewrite is **unconfigurable** (the option registry is measured, §5) and
the tree is byte-clean at a named commit, recommend **restore** and name the command
(`git checkout -- notes/`). Adaptation is only worth proposing when the user wants the formatter in the
workflow permanently — it converts every future notes page into a page that must be written in the
formatter's output form.

## 7. Post-pass: measure damage in two runs, and lead with the gate loss

The plain run and the mutant run are **not** the same measurement, and the mutant run's problem lines
are not real failures. A mutant that is *caught* prints exactly the text you would mistake for damage:
`verify_t0_chains` printed `count phrase missing (population): '**28** families carrying **56**
manuscripts'` in the `--mutant` run — that was the `pop-count` mutant being detected; the same checker's
plain run reported 0 missing phrases. Capture both runs to files and read the authoritative line of each
(`===== TOTAL … N problems (M undetected mutants)`, `problems N`, `mutants not caught N of M`).

**Lead the report with mutant-injection failure, not with checker failures.** After a format pass the
dominant class is mutants that can no longer be injected, because the mutation code keys on byte-exact
page text the formatter rewrote:

```
NOT INJECTED (page text changed — fix the mutant)
NOT INJECTED (target text absent)
NOT INJECTED (phrase absent from the page)
mutants not caught 3 of 9        mutants caught 8/12        26 undetected mutants
```

A checker whose mutants cannot be injected silently verifies nothing, so this is the primary cost of the
pass. Measured run: 47 files formatted (2927+/2878−) → **7** checkers fail the plain run (79 real
problems: 41 `verify_summaries`, 30 `verify_t0_chains`, 4 `verify_named_conjectures`, 1 each
`verify_abstracts` / `verify_index_design` / `verify_named_results`, 1 pre-existing `verify_findings`)
while **12** fail the mutant run. Separate the pre-existing failure from the new ones and say so.

Quantify the byte rewrites from the diff — that is what sizes the adaptation work and what the user
decides on:

```python
add = [l[1:] for l in open('/tmp/fmt.diff') if l.startswith('+') and not l.startswith('+++')]
rem = [l[1:] for l in open('/tmp/fmt.diff') if l.startswith('-') and not l.startswith('---')]
us  = sum(len(re.findall(r'(?<![A-Za-z0-9_])_[^_\n]+_(?![A-Za-z0-9])', l)) for l in add)
q   = sum(l.count('_"') for l in add) - sum(l.count('_"') for l in rem)
pad = sum(1 for l in add if re.match(r'^\|.*\s\|\s+$', l))
```

Measured: 720 `_x_` spans introduced, 244 `*"…"` quote markers → `_"…"` (5 survivors, all inside code
spans), 2,043 padded table lines.

**A derived expectation can move with the page's byte form.** Some checkers derive their expected
numbers from the page's own tables (byte totals "scoped to the TSVs the page tabulates"). When padding
breaks the row regex, the derivation widens and the checker prints a count mismatch that reads like a
data drift in the corpus — `verify_index_design` demanded `630987` where the page states `541463`, and
`630987` was the sum of a wider glob, not a changed file. Reproduce the derivation in-process before
quoting any drift:

```python
import sys; sys.path.insert(0, 'notes/scripts')
import verify_t0_chains as v
m = v.measured(); flat = v.norm(v.PAGE.read_text())
print([p for p, l in v.count_phrases(m) if v.norm(p) not in flat])
```

Report shape: two tables (checker → real problems → the byte-form mechanism from §2; checker → mutants
not caught), the byte-rewrite counts, the restore command with the commit the tree is byte-clean at,
then what was **not** checked (generators and build scripts re-run? pages eyeballed in a renderer?).

## 8. Report

Quote probe output verbatim (the `[warn] Ignored unknown option` lines, the diff lines), state counts
with the rule that yields them (`49 files, 853 *emphasis* spans, 26 quotations containing emphasis in
15 files`), name the checkers by file:line, and end with what was **not** checked.
