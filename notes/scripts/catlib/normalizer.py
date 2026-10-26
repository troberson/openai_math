"""Math-mode-aware LaTeX -> markdown normalizer.

`strip_markup` in `catlib/text.py` is lossy by design: it exists to compare a page quotation
against the line it cites, so it throws away everything that is not a word. This module takes
the opposite direction. It is the renderer for a summary page's quote windows: it preserves the
math, so a `$x + y$` in the source becomes a rendered `$x + y$` in the page, not a stripped-out
gap. The two rules are complements, not duplicates, so they stay in separate modules.

The pipeline, in `normalize_window`'s order:

1. Read the manuscript's preamble and build a per-manuscript macro table from `\\newcommand`,
   including parameterized bodies. Macro bodies diverge per manuscript (`\\F` has 10 distinct
   bodies over 86 dirs), so a global table is wrong and the table is built per window.
2. Split the window into math and prose regions.
3. In math: expand manuscript macros with argument substitution, remap the one ban-listed command
   that has a safe MathJax form (`\\operatorname{X}` -> `\\mathrm{X}`), keep every standard command
   raw, and wrap the span in `$...$`.
4. In prose: accent escapes to unicode, `\\emph{x}` to `_x_`, `\\textbf{x}` to `**x**`,
   `\\text{...}` to its content, and drop `\\cite`/`\\ref`/`\\Cref`/`\\eqref` and friends.
5. A statement `\\begin{X}` on the window's first line becomes a markdown bold lead-in before the
   quote; the quote starts at the next line.
6. A span that carries a ban-listed command with no safe form is emitted in a fenced code block,
   so a macro MathJax cannot render can never reach the page as a live command.
"""

from __future__ import annotations

import re

from catlib.text import fold_accents, fold_dashes

# Commands the GitHub parser rejects. `\operatorname` is the one ban with a safe MathJax form, so
# it is remapped in place (stage 3); the rest fence the whole span (stage 6). The match is on the
# command boundary: `\operatorname{X}` fires, a hypothetical `\operatornamed` does not.
OPERATOR_REMAP = {"operatorname": "mathrm"}
HARD_BANNED = ("colorbox", "fcolorbox", "style", "class", "cssId", "bbox", "mmlToken",
               "usepackage", "input", "include", "catcode")
_BAN_PATTERNS = {n: re.compile(r"\\%s(?![A-Za-z])" % re.escape(n)) for n in HARD_BANNED}
_OP_PATTERN = re.compile(r"\\operatorname(?![A-Za-z])")

# A `\\newcommand` / `\\renewcommand` with an optional argument-count group and a body. The body
# is a single balanced brace group taken by `read_brace`, not a `[^{}]*`, so a body that contains
# nested braces (the common case: `\\newcommand{\\kk}[2]{\\text{#1 + #2}}`) is read whole.
_NEWCOMMAND = re.compile(r"\\(?:re)?newcommand\s*")

# A `\\DeclareMathOperator` / `\\DeclareMathOperator*` defines a math-mode operator. Its body
# is the display text; the rendered form is `\\mathrm{body}`, which MathJax handles natively.
_DECMATHOP = re.compile(r"\\DeclareMathOperator\*?\s*")


def read_brace(text: str, pos: int) -> tuple[str, int] | None:
    """The balanced brace group whose `{` is at `pos`, as (inner, index-after-`}`).

    Returns `None` when `pos` is not a `{`. Nested braces are counted, so the group is the outermost
    balanced one, which is what a macro body and a macro argument both are.
    """
    if pos >= len(text) or text[pos] != "{":
        return None
    depth = 0
    i = pos
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[pos + 1:i], i + 1
        i += 1
    return None


def build_macro_table(preamble: str) -> dict[str, tuple[int, str]]:
    """Per-manuscript macro table: name -> (parameter count, body), from `\\newcommand`.

    The parameter count is 0 for the plain `\\newcommand{\\X}{body}` form and n for
    `\\newcommand{\\X}[n]{body}`. `\\DeclareMathOperator` definitions are also collected:
    their body is rendered as `\\mathrm{body}`. Only the preamble is read, so a macro is
    never taken from the body of a quoted statement where it is used, not defined.
    """
    table: dict[str, tuple[int, str]] = {}
    for m in _NEWCOMMAND.finditer(preamble):
        i = m.end()
        # The control-sequence argument: `{\\X}` (rarely a bare `\\X`).
        if i < len(preamble) and preamble[i] == "{":
            group = read_brace(preamble, i)
            if group is None:
                continue
            name, i = group
            name = name.lstrip("\\")
        else:
            nm = re.match(r"\\([A-Za-z]+)", preamble[i:])
            if nm is None:
                continue
            name = nm.group(1)
            i += nm.end()
        # Optional parameter count: `[n]`.
        params = 0
        j = i
        while j < len(preamble) and preamble[j] in " \t":
            j += 1
        if j < len(preamble) and preamble[j] == "[":
            cm = re.match(r"\[(\d)\]", preamble[j:])
            if cm is not None:
                params = int(cm.group(1))
                j += cm.end()
        # The body: one balanced brace group.
        while j < len(preamble) and preamble[j] in " \t":
            j += 1
        body = read_brace(preamble, j)
        if body is None:
            continue
        inner = body[0]
        # The 2-brace form: `\newcommand{\X}{{body}}` gives a body whose inner is one wrapper
        # group around the real body; unwrap that single group so `{{\mathcal{O}}}` renders as
        # `\mathcal{O}`, not `{\mathcal{O}}`.
        if inner.startswith("{") and inner.endswith("}"):
            candidate = read_brace(inner, 0)
            if candidate is not None and inner[candidate[1]:].strip() == "":
                inner = candidate[0]
        table[name] = (params, inner)
    # `\\DeclareMathOperator{\\X}{body}` / `\\DeclareMathOperator*{\\X}{body}`: the operator's
    # rendered form is `\\mathrm{body}`, which MathJax handles natively in math mode. No
    # parameter count — `\DeclareMathOperator` defines a fixed operator, not a parameterized
    # macro.
    for m in _DECMATHOP.finditer(preamble):
        i = m.end()
        if i < len(preamble) and preamble[i] == "{":
            group = read_brace(preamble, i)
            if group is None:
                continue
            name, i = group
            name = name.lstrip("\\")
            body = read_brace(preamble, i)
            if body is None:
                continue
            table[name] = (0, "\\mathrm{" + body[0] + "}")
    return table


def _macro_invocation(name: str) -> re.Pattern[str]:
    return re.compile(r"\\%s(?![A-Za-z])" % re.escape(name))


def expand_macros(text: str, table: dict[str, tuple[int, str]], depth: int = 0) -> str:
    """Expand manuscript macros with `#1`-style argument substitution, to a bounded depth.

    A macro not in the table is left raw, so a standard command (`\\frac`, `\\mathbb`) — which is
    never in a manuscript's `\\newcommand` table — passes through untouched. The depth bound stops
    a self- or mutually-recursive body from looping; at the bound the remaining macros stay raw,
    which is the honest result for a body the table cannot make safe.
    """
    if depth > 8 or not table:
        return text
    out = text
    for name in table:
        params, body = table[name]
        pat = _macro_invocation(name)
        if not pat.search(out):
            continue
        rebuilt: list[str] = []
        pos = 0
        for m in pat.finditer(out):
            args: list[str] = []
            cursor = m.end()
            ok = True
            for _ in range(params):
                k = cursor
                while k < len(out) and out[k] in " \t":
                    k += 1
                grp = read_brace(out, k)
                if grp is None:
                    ok = False
                    break
                args.append(grp[0])
                cursor = grp[1]
            if not ok:
                continue
            sub = body
            # Substitute highest argument number first so `#1` does not match inside `#10` when
            # params > 9; the corpus's parameter counts are single-digit, but the rule is cheap.
            for a in range(len(args), 0, -1):
                sub = sub.replace(f"#{a}", args[a - 1])
            rebuilt.append(out[pos:m.start()])
            rebuilt.append(expand_macros(sub, table, depth + 1))
            pos = cursor
        rebuilt.append(out[pos:])
        out = "".join(rebuilt)
    return out


def _contains_hard_banned(text: str) -> bool:
    return any(p.search(text) for p in _BAN_PATTERNS.values())


def normalize_math(span: str, table: dict[str, tuple[int, str]], display: bool = False) -> str:
    """One math span, expanded and wrapped, or fenced when it carries an un-mappable banned macro."""
    s = expand_macros(span.strip(), table)
    s = _OP_PATTERN.sub(r"\\mathrm", s)
    if _contains_hard_banned(s):
        fence = "```"
        return f"{fence}latex\n$${s.strip()}$${fence}"
    open_d = "$$" if display else "$"
    close_d = "$$" if display else "$"
    return f"{open_d}{s.strip()}{close_d}"


_CITE_REF = re.compile(
    r"\\(?:cite[pt]*|citeauthor|citeyear|ref|eqref|autoref|Cref|cref|label)\{[^{}]*\}")


_HREF = re.compile(r"\\href\s*\{([^}]*)\}\s*\{([^}]*)\}")
_URL = re.compile(r"\\url\s*\{([^}]*)\}")


def _strip_plain_braces(s: str) -> str:
    """Standalone `{GROUP}` braces to their content, leaving command arguments raw.

    A plain letter/digit/space group that is not the argument of an accent command
    (`\\H{o}`, `\\'{E}`) is a LaTeX grouping for display (`{GL}`, `{CM}`), so its braces
    drop. An accent-argument group is kept for `fold_accents` to resolve. Math-grouping
    braces (`{$p$}`) carry a `$` and are not matched, so they pass through untouched.
    """
    def rep(m: re.Match[str]) -> str:
        i = m.start() - 1
        if i >= 1 and s[i - 1] == "\\" and s[i] in "Hvckudr'\"`":
            return m.group(0)  # accent-command argument: keep for fold_accents
        return m.group(1)
    return re.sub(r"\{([A-Za-z0-9 \u2013\u2014]+)\}", rep, s)


def _prose_markup(s: str) -> str:
    """The fixed prose transforms: emphasis to markdown, `\\text` to content, cross-refs dropped."""
    s = _CITE_REF.sub(" ", s)
    # A `\href{url}{text}` and a bare `\url{url}` are external cross-references: keep the
    # text label, drop the URL. Rendering them as markdown links would add upstream links,
    # which the summaries checker rejects (pass_b) — same reason `\cite`/`\ref` are dropped.
    s = _HREF.sub(r"\2", s)
    s = _URL.sub(" ", s)
    # The release's catalog (CONTENTS.md) uses HTML emphasis and subscript tags in its
    # abstracts (`<i>`, `<sub>`). Strip the tags, keep the content.
    s = re.sub(r"</?(?:i|b|sub|sup|em|strong)>", "", s)
    s = re.sub(r"\\emph\s*\{([^{}]*)\}", r"_\1_", s)
    s = re.sub(r"\\textbf\s*\{([^{}]*)\}", r"**\1**", s)
    s = re.sub(r"\\text\s*\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\%", "%").replace("\\&", "&").replace("\\#", "#")
    s = s.replace("~", " ")
    s = fold_dashes(s)
    s = _strip_plain_braces(s)
    # Fold ASCII quotes to typographic so no bare `"` survives in prose; a bare ASCII double quote
    # reads as markup in the page. Pairs are opened/closed in order of appearance.
    out: list[str] = []
    open_q = True
    prev = ""
    for ch in s:
        if ch == '"' and prev != "\\":
            out.append("\u201c" if open_q else "\u201d")
            open_q = not open_q
        else:
            out.append(ch)
        prev = ch
    return "".join(out)


def normalize_prose(span: str, table: dict[str, tuple[int, str]], depth: int = 0) -> str:
    """One prose span: manuscript macros expanded, then the fixed markup transforms, accents folded."""
    s = expand_macros(span, table, depth)
    s = _prose_markup(s)
    s = fold_accents(s)
    # Post-fold: grouping braces that wrap now-plaintext ({{\L}ojasiewicz} → {Łojasiewicz}).
    # The pre-fold _strip_plain_braces sees the backslash and leaves the group; after the
    # fold the content is plain Unicode and the braces are inert.
    return re.sub(r"\{([^\{}\\$]+)\}", r"\1", s)


def _emphasis_pass(text: str) -> str:
    """Brace-balanced `\\emph{X}` → `_X_` and `\\textbf{X}` → `**X**`, applied
    before the region split.

    A `\\emph{A $p$-adic}` straddles a math boundary, so the per-region
    `_prose_markup` regex (which matches `[^{}]*`) cannot see its closing
    brace. This pass runs on the raw text, where it sees the whole group.
    """
    for cmd, open_md, close_md in (("\\emph", "_", "_"), ("\\textbf", "**", "**")):
        out: list[str] = []
        i = 0
        while i < len(text):
            if text[i:i + len(cmd)] == cmd:
                j = i + len(cmd)
                while j < len(text) and text[j] in " \t":
                    j += 1
                if j < len(text) and text[j] == "{":
                    depth = 0
                    k = j
                    while k < len(text):
                        if text[k] == "{":
                            depth += 1
                        elif text[k] == "}":
                            depth -= 1
                            if depth == 0:
                                break
                        k += 1
                    if depth == 0:
                        out.append(open_md + text[j + 1:k] + close_md)
                        i = k + 1
                        continue
            out.append(text[i])
            i += 1
        text = "".join(out)
    return text


def split_regions(text: str) -> list[tuple[bool, str, bool]]:
    """Split a window into (is_math, chunk, display) regions on `$$...$$` and `$...$`.

    A run of three or more `$` (as in `$$...$$`) is a display span; a run of two is an inline span.
    An unmatched `$` is taken as prose, so a lone dollar sign can never eat the rest of the window.
    """
    regions: list[tuple[bool, str, bool]] = []
    i, n = 0, len(text)
    buf: list[str] = []

    def flush() -> None:
        if buf:
            regions.append((False, "".join(buf), False))
            buf.clear()

    while i < n:
        if text[i] == "$":
            j = i
            while j < n and text[j] == "$":
                j += 1
            run = j - i
            display = run >= 2
            close = text.find("$" * (2 if display else 1), j)
            # For an inline run of exactly two followed by more, keep it inline; the simple rule is
            # "the delimiter is the run's length rounded to the nearest 2". Use 2 for a >=2 run.
            delim = "$$" if display else "$"
            close = text.find(delim, j)
            if close == -1:
                buf.append(text[i:])
                i = n
            else:
                flush()
                regions.append((True, text[j:close], display))
                i = close + len(delim)
            continue
        buf.append(text[i])
        i += 1
    flush()
    return regions


def normalize_body_math(body: str, preamble: str) -> str:
    """A summary page's hand-written body: manuscript macros expanded in its math regions.

    The body is authored markdown, and a ``$...$`` region in it carries the same
    manuscript macros a quote span does (``\\eps``, ``\\F``, ...). The quote path
    expands them through ``normalize_window``; the body path had no equivalent, so
    a macro the manuscript defines and the author reached for rendered raw. This
    pass reuses the quote path's ``split_regions`` and ``normalize_math``: each
    math region gets the full quote-path treatment (macro expansion, the
    ``\\operatorname`` remap, the hard-banned fence), and every non-math byte —
    markdown, citations, code spans, ``[S#]`` markers — is left untouched.
    Display regions (``$$...$$``) expand the same way.

    A macro the manuscript did not define (``\\varepsilon``, ``\\log``) is never
    in the table, so ``expand_macros`` passes it through, which is why the table
    is built from this manuscript's preamble only.
    """
    table = build_macro_table(preamble)
    return "".join(
        normalize_math(chunk, table, display)
        if is_math else chunk
        for is_math, chunk, display in split_regions(body)
    )


_BEGIN = re.compile(r"\\begin\{([A-Za-z]+)\}")
_END = re.compile(r"\\end\{([A-Za-z]+)\}")


def statement_lead_in(window: str) -> str | None:
    """The environment name when the window opens with a `\\begin{X}` on its first content line."""
    for ln in window.split("\n"):
        s = ln.strip()
        if not s:
            continue
        m = _BEGIN.match(s)
        return m.group(1) if m else None
    return None


def _drop_first_begin_line(window: str) -> str:
    """The window with its leading `\\begin{X}` line removed, so the quote starts on the next line."""
    lines = window.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip():
            if _BEGIN.match(ln.strip()):
                return "\n".join(lines[i + 1:])
            break
    return window


def _strip_trailing_end_line(window: str, env: str) -> str:
    """The window with its trailing `\\end{env}` line removed, if present."""
    lines = window.split("\n")
    for i in range(len(lines) - 1, -1, -1):
        s = lines[i].strip()
        if not s:
            continue
        m = _END.match(s)
        if m and m.group(1) == env:
            del lines[i]
            return "\n".join(lines)
        break
    return window


_DISPLAY_ENV = re.compile(
    r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?)\}"
    r"(.*?)"
    r"\\end\{\1\}",
    re.DOTALL,
)


def _convert_display_envs(text: str) -> str:
    """`\\begin{equation}X\\end{equation}` → `$$X$$` so the region splitter sees it as math.

    Runs before env detection so a window that *is* an equation doesn't trigger a lead-in.
    """
    return _DISPLAY_ENV.sub(r"$$\2$$", text)


def is_counter_env(preamble: str, env: str) -> bool:
    """True when the preamble defines `env` as a theorem-like counter environment.

    `\\newtheorem{theorem}{Theorem}[section]` and `\\newtheorem{lemma}[theorem]` both
    make their env a counter env. `abstract`, `equation` etc. are not.
    """
    pat = re.compile(
        r"\\newtheorem\s*(?:\[([^\]]*)\])?\{\s*" + re.escape(env) + r"\s*\}"
        r"(?:\{([^}]*)\})?(?:\[([^\]]*)\])?"
    )
    return bool(pat.search(preamble))


def normalize_window(window: str, preamble: str = "", number: str = "") -> str:
    """A quote window to MathJax-safe markdown with no banned macro and no bare quote mark.

    The preamble is the manuscript's own, so the macro table is per-manuscript. The result carries
    a bold statement lead-in when the window opened with a theorem-like `\\begin{X}`, math spans
    wrapped and expanded, prose markup folded, and any un-mappable banned span fenced. `number`
    is the rendered LaTeX label (e.g. "Theorem 1.1"); when present it replaces the bare
    environment name in the lead-in.

    Display-math environments (`\\begin{equation}` etc.) are converted to `$$...$$` before env
    detection, so a window that *is* an equation is treated as math, not as a statement.
    Non-counter envs (`abstract`, `definition`, `assumption`) get their `\\begin/\\end` delimiters
    stripped without a lead-in.
    """
    table = build_macro_table(preamble)
    # Convert display-math envs to $$...$$ so the region splitter sees them as math.
    window = _convert_display_envs(window)
    lead = statement_lead_in(window)
    if lead and not is_counter_env(preamble, lead):
        # Non-counter env (abstract, definition, assumption): strip delimiters, no lead-in.
        body = _drop_first_begin_line(window)
        body = _strip_trailing_end_line(body, lead)
        lead = None
    else:
        body = _drop_first_begin_line(window) if lead else window
        if lead:
            body = _strip_trailing_end_line(body, lead)
    # Brace-balanced emphasis before the region split: an `\emph{A $p$-adic}`
    # straddles a math boundary, so the per-region regex cannot see its closing
    # brace. This pass converts it to `_A $p$-adic_` where the `$...$` survives
    # as a math span inside the emphasis.
    body = _emphasis_pass(body)
    # A math-grouping brace `{$...$}` is a LaTeX display hack (prevent a space
    # after the math span). It has no role in markdown, so the outer braces
    # drop. This must run before the region split: the braces and the `$...$`
    # must be in the same text for the pattern to match.
    body = re.sub(r"\{(\$[^$]+\$)\}", r"\1", body)
    parts = [normalize_math(chunk, table, display) if is_math
             else normalize_prose(chunk, table)
             for is_math, chunk, display in split_regions(body)]
    text = "".join(parts).strip()
    if lead:
        label = number if number else lead
        text = f"**{label}**\n{text}"
    return text
