"""The citation-anchor grammar and the fenced-block scan the page checkers share.

Every notes page cites its evidence as `path:line`; some pages add ranges, markdown-link
anchors, or a bare `:N` that resolves against the nearest preceding explicit path. The
extension set is a per-page rule that the page documents, so it is a parameter here and
never a default: a checker that silently widens the page's anchor grammar stops flagging
the anchors its own mutants inject.
"""

from __future__ import annotations

import re

# Extension sets, named by the pages that ship them.
EXT_DOC = ("py", "md", "tex", "json", "tsv", "yaml")  # sources.md, index-design.md
EXT_MAN = ("py", "md", "tex", "json", "txt", "lean", "yaml", "bib")  # named-results.md, t0-chains.md
EXT_LEAN = ("lean", "md", "yaml")  # conditional.md
EXT_YAML = ("py", "md", "tex", "json", "txt", "lean", "yaml")  # counterexample-crosscheck.md
EXT_MD = ("py", "md", "tex", "json", "txt")  # verification-dirs.md


def anchor_pattern(extensions, ranges=False):
    """The `path:line` (optionally `path:a-b`) anchor grammar for one extension set.

    `extensions=None` is the no-extension rule (`dependency-drift.md` anchors any path).
    """
    body = r"[\w./+-]+" if extensions is None else r"[\w./+-]+?\.(?:%s)" % "|".join(extensions)
    tail = r":(\d+)(?:-(\d+))?" if ranges else r":(\d+)"
    return re.compile(rf"`({body}){tail}`")


def fenced_blocks(lines, dedent=False):
    """Yield (index of the opening fence, body lines) for each ``` block, in order.

    `dedent=True` is the form the pages that indent a block under its anchor ship: the fence
    test strips leading whitespace and the fence's own indent is removed from each body line,
    so a block nested in a list item compares against the source at its own indentation.
    """
    i = 0
    while i < len(lines):
        fence = lines[i].lstrip() if dedent else lines[i]
        if fence.startswith("```"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())] if dedent else ""
            j = i + 1
            body = []
            while j < len(lines):
                inner = lines[j].lstrip() if dedent else lines[j]
                if inner.startswith("```"):
                    break
                ln = lines[j]
                body.append(ln[len(indent):]
                            if dedent and ln.startswith(indent) and ln.strip() else ln)
                j += 1
            yield i, body
            i = j + 1
        else:
            i += 1


def nearest_anchor(lines, before, pattern, window=8):
    """The last anchor on the nearest preceding line, scanning at most `window` lines up.

    Returns the regex's match tuple, so a ranges pattern yields a 3-tuple.
    """
    for k in range(before - 1, max(before - 1 - window, -1), -1):
        found = pattern.findall(lines[k])
        if found:
            return found[-1]
    return None
