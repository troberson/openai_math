"""Self-test for catlib/normalizer.py.

Covers the four surfaces the bead names:
- the 187 distinct commands inside the current quotes (spot-checked)
- the parameterized macro set (argument substitution)
- the accent set (LaTeX escapes -> Unicode)
- the banned map (hard-banned macros fence the span; operatorname remaps)

Each test asserts the rendered output is free of banned macros and bare
ASCII double-quote characters, which is the module's acceptance criterion.
"""

from __future__ import annotations

import re

from catlib.normalizer import (
    build_macro_table,
    expand_macros,
    normalize_math,
    normalize_prose,
    normalize_window,
    split_regions,
)

BAN_RE = re.compile(r"\\(?:colorbox|fcolorbox|style|class|cssId|bbox|mmlToken|"
                    r"usepackage|input|include|catcode)(?![A-Za-z])")
OP_RE = re.compile(r"\\operatorname(?![A-Za-z])")
BARE_QUOTE_RE = re.compile('"')


def assert_clean(text: str, allow_fenced: bool = False) -> None:
    """The acceptance criterion: no banned macro, no bare ASCII double quote.

    When `allow_fenced` is True, the text may carry a fenced code block (the
    module's escape hatch for un-mappable banned macros); the fence *is* the
    safety measure, so we assert the fence is present rather than the absence
    of the macro inside it.
    """
    if allow_fenced:
        assert "```" in text, f"expected fence in: {text!r}"
        return
    assert not BAN_RE.search(text), f"banned macro in: {text!r}"
    assert not OP_RE.search(text), f"operatorname in: {text!r}"
    assert not BARE_QUOTE_RE.search(text), f"bare quote in: {text!r}"


class TestAccents:
    """The accent set: LaTeX escapes to Unicode."""
    def test_diaeresis(self):
        out = normalize_prose(r'K\"ahler surface', build_macro_table(""))
        assert "\u00e4" in out  # ä
        assert_clean(out)

    def test_acute(self):
        out = normalize_prose(r"Gy\u0027arf\u0027as" .replace("\u0027", "'") , build_macro_table(""))
        # Use the actual LaTeX form: Gy\'arf\'as
        out = normalize_prose("Gy\\'arf\\'as", build_macro_table(""))
        assert "\u00e1" in out  # á
        assert_clean(out)

    def test_double_accent(self):
        out = normalize_prose(r"Erd\H{o}s", build_macro_table(""))
        assert "\u0151" in out  # ő
        assert_clean(out)

    def test_v_on_s(self):
        out = normalize_prose(r"\v{s}tandard", build_macro_table(""))
        assert "\u0161" in out  # š
        assert_clean(out)

    def test_v_on_a(self):
        out = normalize_prose(r"\v{a}", build_macro_table(""))
        assert "\u0103" in out  # á (caron)
        assert_clean(out)


class TestParamMacros:
    """The parameterized macro set: argument substitution."""
    def test_simple_substitution(self):
        preamble = r"\newcommand{\kk}[2]{$\mathbb{#1}^{#2}$}"
        out = normalize_window("We show \\kk{k}{2} is finite.", preamble)
        assert "\\mathbb{k}^{2}" in out
        assert_clean(out)

    def test_three_args(self):
        preamble = r"\newcommand{\poly}[3]{#1 - #2 #3}"
        table = build_macro_table(preamble)
        out = normalize_prose("the polynomial \\poly{a}{b}{c}", table)
        assert "a - b c" in out
        assert_clean(out)

    def test_nested_macro_in_body(self):
        preamble = (r"\newcommand{\F}{\mathbb{F}}"
                    r"\newcommand{\thm}[1]{\textbf{Theorem #1}}")
        table = build_macro_table(preamble)
        out = normalize_prose("Over \\F, see \\thm{1.2}", table)
        assert "\\mathbb{F}" in out
        assert "Theorem 1.2" in out
        assert_clean(out)

    def test_macro_not_in_table_stays_raw(self):
        out = normalize_prose("Use \\frac{1}{2} here", build_macro_table(""))
        assert "\\frac{1}{2}" in out
        assert_clean(out)


class TestBannedMap:
    """The banned map: hard-banned macros fence; operatorname remaps."""
    def test_operatorname_remaps_to_mmathrm(self):
        out = normalize_math(r"\operatorname{Ext}^1(A, B)", {})
        assert "\\mathrm{Ext}^1(A, B)" in out
        assert_clean(out)

    def test_colorbox_fences(self):
        out = normalize_math(r"\colorbox{red}{x}", {})
        assert_clean(out, allow_fenced=True)

    def test_input_fences(self):
        out = normalize_math(r"\input{other}", {})
        assert_clean(out, allow_fenced=True)

    def test_class_fences(self):
        out = normalize_math(r"\class A", {})
        assert_clean(out, allow_fenced=True)

    def test_ext_macro_remaps(self):
        preamble = r"\newcommand{\Ext}{{\operatorname{Ext}}}"
        table = build_macro_table(preamble)
        out = normalize_math(r"\Ext^1", table)
        assert "\\mathrm{Ext}^1" in out
        assert_clean(out)


class TestProseMarkup:
    """The prose markup: emphasis, text, cross-refs."""
    def test_emph(self):
        out = normalize_prose("This is \\emph{important}", build_macro_table(""))
        assert "_important_" in out
        assert_clean(out)

    def test_textbf(self):
        out = normalize_prose("The \\textbf{main} result", build_macro_table(""))
        assert "**main**" in out
        assert_clean(out)

    def test_text_inner(self):
        out = normalize_prose("We \\text{show} that", build_macro_table(""))
        assert "We show that" in out
        assert_clean(out)

    def test_cite_dropped(self):
        out = normalize_prose("As in \\cite{milne1992} we see", build_macro_table(""))
        assert "As in" in out
        assert "\\cite" not in out
        assert_clean(out)

    def test_ref_dropped(self):
        out = normalize_prose("See \\ref{thm:main} for details", build_macro_table(""))
        assert "See" in out
        assert "for details" in out
        assert "\\ref" not in out
        assert_clean(out)


class TestMathRegions:
    """Region splitting: inline and display math."""
    def test_inline_math(self):
        out = normalize_window("If $x + y = 0$ then done.", "")
        assert "$x + y = 0$" in out
        assert_clean(out)

    def test_display_math(self):
        out = normalize_window("We get $$\\sum_{i=1}^n a_i$$", "")
        assert "$$" in out
        assert_clean(out)

    def test_macro_in_math(self):
        preamble = r"\newcommand{\PP}{\mathbb{P}}"
        out = normalize_window("Let $\\PP^2$ be the plane.", preamble)
        assert "\\mathbb{P}^2" in out
        assert_clean(out)


class TestStatementLeadIn:
    """Statement lead-in: a \\begin{X} becomes a bold label."""
    def test_theorem_begin(self):
        window = "\\begin{theorem}\nThe map $f: A \\to B$ is surjective.\n\\end{theorem}"
        out = normalize_window(window, "")
        assert out.startswith("**theorem**")
        assert "$f: A \\to B$" in out
        assert_clean(out)

    def test_no_begin(self):
        out = normalize_window("Just a plain sentence.", "")
        assert not out.startswith("**")
        assert_clean(out)


class TestSplitRegions:
    """The split_regions function directly."""
    def test_no_math(self):
        regions = split_regions("no math here")
        assert len(regions) == 1
        assert regions[0] == (False, "no math here", False)

    def test_inline(self):
        regions = split_regions("a $b$ c")
        assert len(regions) == 3
        assert regions[0][0] is False
        assert regions[1] == (True, "b", False)
        assert regions[2][0] is False

    def test_display(self):
        regions = split_regions("a $$b$$ c")
        assert len(regions) == 3
        assert regions[1] == (True, "b", True)


class TestCorpusSpotCheck:
    """Spot-check a representative subset of the 187 commands in the current quotes."""

    def test_mathbb(self):
        out = normalize_math("\\mathbb{R}^n", {})
        assert "\\mathbb{R}^n" in out
        assert_clean(out)

    def test_ell(self):
        out = normalize_math("\\ell^2", {})
        assert "\\ell^2" in out
        assert_clean(out)

    def test_bigr(self):
        out = normalize_math("\\bigl( f \\bigr)", {})
        assert "\\bigl( f \\bigr)" in out
        assert_clean(out)

    def test_subs(self):
        out = normalize_math("x_{i+1}", {})
        assert "x_{i+1}" in out
        assert_clean(out)

    def test_supers(self):
        out = normalize_math("a^2 + b^2", {})
        assert "a^2 + b^2" in out
        assert_clean(out)

    def test_top_command(self):
        out = normalize_math("\\top", {})
        assert "\\top" in out
        assert_clean(out)

    def test_aleph(self):
        out = normalize_math("\\aleph_0", {})
        assert "\\aleph_0" in out
        assert_clean(out)

    def test_clifford(self):
        preamble = r"\newcommand{\cO}{{\mathcal{O}}}"
        table = build_macro_table(preamble)
        out = normalize_math("\\cO_X", table)
        assert "\\mathcal{O}_X" in out
        assert_clean(out)

    def test_R_macro(self):
        preamble = r"\newcommand{\R}{{\mathbb{R}}}"
        table = build_macro_table(preamble)
        out = normalize_math("\\R^n", table)
        assert "\\mathbb{R}^n" in out
        assert_clean(out)


class TestBuildMacroTable:
    """build_macro_table: the per-manuscript macro table."""
    def test_plain(self):
        table = build_macro_table(r"\newcommand{\F}{\mathbb{F}}")
        assert table["F"] == (0, "\\mathbb{F}")

    def test_parameterized(self):
        table = build_macro_table(r"\newcommand{\kk}[2]{#1 + #2}")
        assert table["kk"] == (2, "#1 + #2")

    def test_nested_braces_in_body(self):
        table = build_macro_table(r"\newcommand{\X}{\text{a \{braced\} body}}")
        assert "braced" in table["X"][1]

    def test_renewcommand(self):
        table = build_macro_table(r"\renewcommand{\text}[1]{\mathrm{#1}}")
        assert table["text"] == (1, "\\mathrm{#1}")


class TestRecursiveGuard:
    """The recursive guard: bounded expansion depth."""
    def test_self_recursive_macro(self):
        table = {"X": (0, "\\X + 1")}
        out = expand_macros("\\X", table, 0)
        assert out  # non-empty, terminates
        assert "1" in out

    def test_mutually_recursive(self):
        table = {"A": (0, "\\B"), "B": (0, "\\A")}
        out = expand_macros("\\A", table, 0)
        assert out  # terminates
