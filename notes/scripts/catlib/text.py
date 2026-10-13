"""Text normalizers, named by what they are for.

`norm` is not one join in this corpus: the same name covers six different rules, so the package
ships them under distinct names and a caller says which one it means.

  collapse_ws     verbatim comparison: quotations checked "verbatim modulo whitespace"
  strip_markup    a page quotation against the source line it cites: emphasis markers, code spans,
                  HTML entities and tags, LaTeX commands, and the number a page substituted for a
                  `\\ref` are markup, not words, so they are removed before the substring test
  fold_apostrophe U+2019/U+2018 -> ASCII, because overview.tex is inconsistent (76 titles use
                  ASCII ' and 8 use U+2019), so an ASCII pattern misses a title silently
  title_key       lowercase alphanumerics, leading 'the' and possessives dropped (title joins)
  library_key     lowercase alphanumerics with the lean4/lean and trailing-digit suffixes stripped
                  (lakefile <-> deps <-> yaml joins)
  url_key         repo URL join key: the lakefile writes '.git', formalization.yaml does not

The LaTeX-prose normalizer in compare_abstracts.py and the accent-stripping bib-title normalizer
(`catlib.bib.norm_title`) are deliberately **not** merged here: they are lossy in ways their own pages
document, and a checker's sensitivity variant (verify_citations.norm_noguard) is defined as a
difference from one of them.
"""

from __future__ import annotations

import re
from collections.abc import Mapping


def collapse_ws(s: str) -> str:
    """Whitespace collapsed to single spaces and trimmed — the verbatim-comparison form."""
    return re.sub(r"\s+", " ", s).strip()


def strip_markup(s: str) -> str:
    """A page quotation compared against the source line it cites, markup aside.

    Moved verbatim from verify_summaries.py, where it is the checker's quotation rule;
    locate_summary_quotes.py and verify_findings.py call the same rule, so it lives here.
    """
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("**", "").replace("`", "").replace("*", "")
    s = s.replace("&emsp;", " ").replace("&thinsp;", " ").replace("&mdash;", "-")
    # Markup, not words: the release writes <i>p</i> in its blurbs and the page renders *p*. Strip
    # tags to nothing, not to a space - `prime-to-<i>p</i>` must normalize to `prime-to-p`, and a
    # space here would break the substring test against the page.
    s = re.sub(r"</?[a-zA-Z][^>]*>", "", s)
    # The page links its sources relatively (../../../ from notes/summaries/<discipline>/), while
    # the release text spells the same target as a repo-relative path.
    s = re.sub(r"(?:\.\./)+", "", s)
    # LaTeX-aware: a rendered cross-reference is not a misquote. `\ref{thm:main}` in the source is
    # "Theorem 1" in the page, so strip the command *and* the number the page substituted for it.
    s = re.sub(r"\\(?:ref|eqref|label|autoref|Cref|cref|cite[tp]*|citeauthor|citeyear)\{[^}]*\}",
               "", s)
    s = re.sub(r"\\[a-zA-Z@]+", " ", s).replace("~", " ").replace("{}", " ")
    s = re.sub(r"\b(Theorem|Lemma|Corollary|Proposition|Definition|Remark|Item|Axiom|Step)"
               r"\s+\d+(?:\.\d+)*\b", r"\1", s)
    s = re.sub(r"[{}]", " ", s)
    s = re.sub(r"\s+([.,;:!?])", r"\1", s)
    return collapse_ws(s)


def fold_apostrophe(s: str) -> str:
    """Typographic apostrophes folded to ASCII."""
    return s.replace("\u2019", "'").replace("\u2018", "'")


def title_key(s: str) -> str:
    """Lowercase alphanumerics, single-spaced, leading 'the' dropped, possessives stripped."""
    s = fold_apostrophe(s.lower())
    s = re.sub(r"'s\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\bthe\b", " ", s)
    return " ".join(s.split())


def library_key(name: str) -> str:
    """Canonical library join key: lowercase alphanumerics, then drop the trailing
    'lean4' / 'lean' / digit suffixes the three layers add and drop unevenly."""
    s = re.sub(r"[^a-z0-9]", "", name.lower())
    for suffix in ("lean4", "lean"):
        if s.endswith(suffix) and len(s) > len(suffix):
            s = s[: -len(suffix)]
            break
    return re.sub(r"[0-9]+$", "", s)


def url_key(url: str) -> str:
    """Join key for a repo URL: the lakefile writes '.git' and formalization.yaml does not."""
    last = url.rstrip("/").split("/")[-1]
    last = last.removesuffix(".git")
    return library_key(last)


def fmt_counter(counter: Mapping[str, int]) -> str:
    """Counter -> 'name n, name n, ...' sorted by count desc, then name — the report form."""
    return ", ".join(f"{n} {c}" for n, c in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])))


def first_group(pattern: str | re.Pattern[str], text: str) -> str:
    """The first capture group of `pattern` in `text`, or `""` when the pattern does not fire.

    A checker that reads a report line with `re.search(...).group(1)` crashes with AttributeError on
    the exact defect it is looking for — a report that no longer prints the line. Returning `""` lets
    the caller report the absence; a count read from `""` is 0, which the page's count comparison
    flags, so the missing line becomes a finding instead of a traceback. `pattern` may be a compiled
    pattern, which is what a checker that already carries one passes.
    """
    m = re.search(pattern, text)
    return m.group(1) if m else ""


NUM_RUN = re.compile(r"\d[\d,]*(?:\.\d+)?")


def flex(phrase: str) -> re.Pattern[str]:
    """Regex for a phrase whose spaces may be any whitespace run, and whose numbers may differ.

    A template is built from HEAD's committed page, so the number a slot carries in HEAD is the
    *previous* measurement, and a split prefix transcribed from HEAD is the previous number too.
    Matching numbers flexibly keeps the slot in the template, and keeps the prefix check in the split
    valid, when a count moves: the render writes the measured value into the slot, so a page whose
    count changed needs no hand sweep and no second commit. A phrase matched on its exact number is
    NOT FOUND on HEAD's stale bytes, the template keeps the literal, and the render writes HEAD's
    literal back into the page.
    """
    if NUM_RUN.fullmatch(phrase):
        # A needle that is nothing but a number carries no literal anchor, so relaxing its digits
        # makes it match the first number anywhere in HEAD's page — the bare "719" needle for the
        # sources-row count matched "A 2-line ... 40-line construction" and slotted the row count into
        # a sentence that never names rows. A number-only needle must match exactly, so a writer that
        # wants a drifting count to stay slotted supplies the count with its words.
        return re.compile(re.escape(phrase))
    if len(NUM_RUN.sub("", phrase)) < 2:
        # A needle relaxes its digits only when it carries literal context. "719" has none, so relaxing
        # it matched "A 2-line ... 40-line construction" and slotted the sources-row count into a
        # sentence that never names rows; "631M" has one character, so relaxing it turned the needle
        # into "any number followed by M" and the preprints size also matched "1740M" and "14M",
        # rendering all three surfaces as 631M. A needle with two literal characters — "**342**",
        # "147.8 B/row", a template row's `README.md.j2` — is anchored by its words, so its numbers
        # can move with HEAD's stale measurement.
        return re.compile(re.escape(phrase))
    toks = []
    for tok in phrase.split(" "):
        out, pos = "", 0
        for m in NUM_RUN.finditer(tok):
            out += re.escape(tok[pos:m.start()])
            # A digit run relaxes only when neither neighbour inside the token is a letter. "631M" has
            # a letter after, so relaxing it reads "any number followed by M"; "README.md.j2" has a
            # letter before the 2, so the template's filename would match a sibling suffix.
            prev = tok[m.start() - 1] if m.start() else " "
            nxt = tok[m.end()] if m.end() < len(tok) else " "
            out += re.escape(m.group(0)) if prev.isalpha() or nxt.isalpha() else NUM_RUN.pattern
            pos = m.end()
        toks.append(out + re.escape(tok[pos:]))
    return re.compile(r"\s+".join(toks))


def apply_split(label: str, phrase: str, prefixes: list[str]) -> dict[str, str]:
    """Split a measured phrase at the page's recorded line-break prefixes.

    Each prefix is matched number-flexibly against the start of the remainder, and the part emitted
    is the measured span, not the prefix. A prefix transcribed from HEAD carries HEAD's number, so an
    exact `startswith` raises the moment a count moves; matching flexibly and emitting the measured
    text keeps the split table valid across a drift, and the page keeps its own line breaks.
    """
    out: dict[str, str] = {}
    rest = phrase
    for i, pre in enumerate(prefixes):
        rest = rest.lstrip()
        m = flex(pre).match(rest)
        if m is None:
            raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {rest!r}")
        out[f"{label} {'abcdefghij'[i]}"] = rest[:m.end()]
        rest = rest[m.end():]
    out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def first_match(pattern: str | re.Pattern[str], text: str) -> str:
    """The whole match of `pattern` in `text`, or `""` when the pattern does not fire.

    The `group(0)` companion of `first_group`, for a pattern with no capture group — the manuscript
    path pattern in `build_catalog`, which a page's path set is compared against.
    """
    m = re.search(pattern, text)
    return m.group(0) if m else ""
