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

After any format pass, re-run **every** checker (with `--mutant` where supported) before reporting
green, and commit the config file separately from the formatting.

## 7. Report

Quote probe output verbatim (the `[warn] Ignored unknown option` lines, the diff lines), state counts
with the rule that yields them (`49 files, 853 *emphasis* spans, 26 quotations containing emphasis in
15 files`), name the checkers by file:line, and end with what was **not** checked.
