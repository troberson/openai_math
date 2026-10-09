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
    if last.endswith(".git"):
        last = last[: -len(".git")]
    return library_key(last)


def fmt_counter(counter: Mapping[str, int]) -> str:
    """Counter -> 'name n, name n, ...' sorted by count desc, then name — the report form."""
    return ", ".join(f"{n} {c}" for n, c in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])))
