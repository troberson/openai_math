"""overview.tex and CONTENTS.md: the release's own claims, parsed.

Moved verbatim from build_catalog.py, which stays the writer of notes/catalog.tsv and
re-exports these names for the scripts that import it.

overview.tex declares both \\cataloguesection and \\resultentry with \\newcommand at lines 28
and 35, so a substring count of either command name reads 18 and 373; the counts are 17 and
372, counted by the command at line start.
"""

from __future__ import annotations

import re
from collections import defaultdict
from typing import Any

from catlib.paths import CONTENTS_MD, OVERVIEW_TEX, read_text

# Paren-aware: preprints/Sharp-integral-fillings-in-CAT(0)-spaces-.../paper.pdf
# Braces and backslashes must stay out of the class, or a greedy match in overview.tex
# swallows the "}\\enspace\\textperiodcentered\\enspace\\href{" separator between links.
PAP = r"preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf"
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE_SUFFIX = re.compile(rf"-(?:{MONTHS})-\d{{1,2}}-\d{{4}}$")


def read_args(text: str, i: int) -> tuple[list[str], int]:
    """text[i] == '{' -> (list of brace-group bodies, index after the last group)."""
    args: list[str] = []
    while i < len(text) and text[i] == "{":
        depth, j, buf = 0, i + 1, []
        while j < len(text):
            c = text[j]
            back = 0
            k = j - 1
            while k >= 0 and text[k] == "\\":
                back += 1
                k -= 1
            escaped = back % 2 == 1
            if c == "{" and not escaped:
                depth += 1
                buf.append(c)
            elif c == "}" and not escaped:
                if depth == 0:
                    break
                depth -= 1
                buf.append(c)
            else:
                buf.append(c)
            j += 1
        args.append("".join(buf))
        i = j + 1
    return args, i


def parse_overview_text(text: str) -> tuple[list[str], dict[str, dict[str, Any]]]:
    """-> (families ordered, {fam: {discipline,title,abstract,links}}) for a **string**.

    The text-level core `parse_overview()` delegates to; `links` is the raw 4th brace group.
    A checker that compares two revisions of the release parses both from a
    `git show <rev>:overview.tex` string, so the traversal must not be disk-bound; the disk
    read lives in the wrapper.

    Read this, never a `[^{}]*` regex over the entries: the abstracts contain braces, so a
    brace-free group silently drops the math-heavy families.
    """
    start = text.index("\\begin{document}")
    discipline = None
    fams: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    i = start
    while True:
        ns = text.find("\\cataloguesection{", i)
        nr = text.find("\\resultentry{", i)
        if nr == -1:
            break
        if ns != -1 and ns < nr:
            args, i = read_args(text, ns + len("\\cataloguesection"))
            discipline = args[0]
            continue
        args, i = read_args(text, nr + len("\\resultentry"))
        fam, title, abstract, links = args[0], args[1], args[2], args[3]
        fams[fam] = {
            "discipline": discipline,
            "title": title.strip(),
            "abstract": abstract.strip(),
            "links": links,
        }
        order.append(fam)
    return order, fams


def parse_overview() -> tuple[list[str], dict[str, dict[str, Any]]]:
    """-> (families ordered, {fam: {discipline,title,abstract,tex_paps}}) from disk."""
    order, fams = parse_overview_text(read_text(OVERVIEW_TEX))
    for entry in fams.values():
        entry["tex_paps"] = re.findall(PAP, entry.pop("links"))
    return order, fams


def parse_contents() -> dict[str, list[str]]:
    """-> {fam: [manuscript paths]} in document order."""
    text = read_text(CONTENTS_MD)
    fam = None
    paps: dict[str, list[str]] = defaultdict(list)
    header = re.compile(r"^\*\*(\d{3})\.\s", re.M)
    link = re.compile(r"\]\((" + PAP + r")\)")
    events = [(m.start(), "fam", m.group(1)) for m in header.finditer(text)]
    events += [(m.start(), "pap", m.group(1)) for m in link.finditer(text)]
    events.sort()
    for _, kind, val in events:
        if kind == "fam":
            fam = val
        elif fam is not None and val not in paps[fam]:
            paps[fam].append(val)
    return paps


def resultentry_lines() -> dict[str, tuple[int, str]]:
    """{fam: (1-based line, that line's text)} — the anchor plus the text it cites.

    The form a checker needs when it checks a quotation against the cited line, not just the
    line number. Same rule as overview_lines(): first line containing `\\resultentry{NNN}`,
    which skips the `\\newcommand` definitions at lines 28 and 35.
    """
    out: dict[str, tuple[int, str]] = {}
    entry = re.compile(r"\\resultentry\{(\d{3})\}")
    for n, line in enumerate(read_text(OVERVIEW_TEX).splitlines(), 1):
        m = entry.search(line)
        if m and m.group(1) not in out:
            out[m.group(1)] = (n, line)
    return out


def overview_lines() -> dict[str, int]:
    """{fam: 1-based line of its \\resultentry}, the anchor every citation to the release uses.

    A family's abstract ships as one logical line re-wrapped across the file, so an anchor is
    the line the entry starts on; a quotation that wraps is matched against the contiguous
    lines below it, not against the line it ends on. Rule: first line containing
    `\\resultentry{NNN}`, which skips the `\\newcommand` definitions at lines 28 and 35.
    """
    return {fam: n for fam, (n, _) in resultentry_lines().items()}


def resultentry_link_fields() -> dict[str, str]:
    """{fam: raw body of the 4th `\\resultentry` brace group}, by slice-based brace reading.

    Slice reading, not a regex: the field is a run of `\\href{…}{…}` and a group split
    mis-slices as soon as a display title carries a brace.
    """
    text = read_text(OVERVIEW_TEX)
    i = text.index("\\begin{document}")
    links: dict[str, str] = {}
    while True:
        ns = text.find("\\cataloguesection{", i)
        nr = text.find("\\resultentry{", i)
        if nr == -1:
            return links
        if ns != -1 and ns < nr:
            _, i = read_args(text, ns + len("\\cataloguesection"))
            continue
        args, i = read_args(text, nr + len("\\resultentry"))
        links[args[0]] = args[3]


def href_pairs(body: str) -> list[tuple[str, str]]:
    """[(target, display title)] for every `\\href{…}{…}` in a 4th-field body, in order.

    The display text is link text, not the manuscript's own title — that is the `preprints/`
    directory name — and the release is inconsistent about capitalization and dashes, so a
    normalized title is not verbatim.
    """
    out: list[tuple[str, str]] = []
    k = 0
    while True:
        h = body.find("\\href", k)
        if h == -1:
            return out
        j = h + len("\\href")
        while j < len(body) and body[j] in " \t\n":
            j += 1
        if j >= len(body) or body[j] != "{":
            k = h + len("\\href")
            continue
        groups, after = read_args(body, j)
        if len(groups) == 2:
            out.append((groups[0].strip(), groups[1].strip()))
        k = after
