"""The `.bib` primitives the shared-bibliography extractor and its checker share.

Moved out of `extract_citations.py`, where `verify_citations.py` reached every one of them by
importing that script -- the corpus's largest `duplicate-code` cluster. The pair window and the
connected-component scan are here too: the extractor inlines them, the checker re-implemented them,
and the two must agree because the page's tables are the extractor's rows.

The bib-title normalizer is the accent-stripping rule `extract_citations.py` documents in its
method section. It is deliberately **not** in `catlib.text` -- that module's docstring records why
the lossy normalizers stay with the pages that document them -- and
`verify_citations.norm_noguard` is defined as a difference from this one: the same rule with the
`(?![a-zA-Z])` accent guard removed, which is the page's sensitivity variant.

Static reading only: never run lake, lean, or comparator.
"""

from __future__ import annotations

import collections
import os
import re
import unicodedata
from collections.abc import Iterable, Mapping

from catlib.paths import PREPRINTS, SUBFINDINGS_TSV, rel
from catlib.tsv import read_rows

ENTRY = re.compile(r"^\s*@\s*(\w+)\s*\{\s*([^,]*)\s*,", re.M)
ATLINE = re.compile(r"^\s*@", re.M)
ACCENT = re.compile(r"\\(?:['`^~=\".](?![a-zA-Z])|c|v|u|H|k|r|d|b|t|o)\{?([a-zA-Z])\}?")
CITE = re.compile(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])?\{([^}]*)\}")
RELEASE_HREF = re.compile(r"\\href\{[^}]*/preprints/([^/]+)/[^}]*\.pdf\}")
THRESHOLDS = (1, 2, 3, 5, 10)
CLUSTER_K = (1, 5, 10)
TOP_N = 20


def ranked(counter: Mapping[str, int], n: int | None = None) -> list[tuple[str, int]]:
    """most_common with ties broken by key, so the report is byte-stable."""
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    return items if n is None else items[:n]


def read(path: str | os.PathLike[str]) -> str:
    """A `.bib`/`.tex` read with undecodable bytes replaced -- the extractor's rule, not
    `catlib.paths.read_text`, which is strict and would raise on the corpus's own bytes."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def bib_files() -> list[str]:
    """Every `preprints/**/*.bib`, in repo-relative path order."""
    out = []
    for dirpath, dirs, files in os.walk(PREPRINTS):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".bib"):
                out.append(os.path.join(dirpath, f))
    return sorted(out, key=rel)


def field(body: str, name: str) -> str | None:
    """Raw value of `name = {...}` (or `name = "..."`) in an entry body, or None."""
    m = re.search(r"\b%s\s*=\s*([{\"\"])" % name, body, re.I)
    if not m:
        return None
    j = m.end()
    depth = 1
    k = j
    while k < len(body) and depth:
        c = body[k]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                break
        k += 1
    return body[j:k]


def norm_title(s: str) -> str:
    """Work identity: accent macros folded to the base letter, escapes unescaped, commands
    removed, braces and math delimiters dropped, U+2019/U+2018 folded, NFKD with combining marks
    dropped, lowercased, non-alphanumeric runs collapsed to one space."""
    s = ACCENT.sub(r"\1", s)
    s = s.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_").replace("\\-", "")
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)


def entries(text: str) -> list[tuple[str, str, str, int]]:
    """(type, key, body, start_line) for every @-entry, body cut at the next line-start @."""
    heads = list(ENTRY.finditer(text))
    bounds = [m.start() for m in ATLINE.finditer(text)]
    out = []
    for _i, m in enumerate(heads):
        nxt = len(text)
        for b in bounds:
            if b > m.end():
                nxt = b
                break
        out.append((m.group(1).lower(), m.group(2).strip(), text[m.end():nxt],
                    text.count("\n", 0, m.start()) + 1 + m.group(0).count("\n")))
    return out


def manuscript_map() -> dict[str, str]:
    """{manuscript dir: family} from the manuscript rows of notes/subfindings.tsv."""
    man2fam = {}
    for r in read_rows(SUBFINDINGS_TSV):
        if r.get("kind") == "manuscript":
            man2fam[r["path"].split("/")[1]] = r["fam"]
    return man2fam


def tex_tree(man: str) -> Iterable[str]:
    """Every `.tex` file in a manuscript directory, in walk order."""
    base = os.path.join(PREPRINTS, man)
    for dirpath, dirs, files in os.walk(base):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".tex"):
                yield os.path.join(dirpath, f)


def cite_keys(man: str) -> set[str]:
    """Keys that appear in a `\\cite...{...}` locator anywhere in the manuscript's own tree."""
    out = set()
    for p in tex_tree(man):
        for m in CITE.finditer(read(p)):
            for k in m.group(1).split(","):
                if k.strip():
                    out.add(k.strip())
    return out


def pair_counts(groups: Iterable[Iterable[str]]) -> collections.Counter:
    """Counter of manuscript pairs weighted by shared items.

    Each group is the set of manuscripts carrying one item; the window is the pair layer the page's
    threshold table reports, so it is one rule here and not two loops.
    """
    pairs: collections.Counter[tuple[str, str]] = collections.Counter()
    for s in groups:
        ms = sorted(s)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                pairs[(ms[i], ms[j])] += 1
    return pairs


def clusters(pairs: Mapping[tuple[str, str], int], k: int) -> list[set[str]]:
    """Connected components of the pair graph at threshold `k`, largest first, ties by smallest member.

    Returns every component, singletons included; a caller that wants only the non-trivial ones
    filters on `len(c) > 1`.
    """
    adj = collections.defaultdict(set)
    for (a, b), v in pairs.items():
        if v >= k:
            adj[a].add(b)
            adj[b].add(a)
    seen, comps = set(), []
    for n0 in sorted(adj):
        if n0 in seen:
            continue
        stack, comp = [n0], set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            seen.add(x)
            stack.extend(adj[x] - comp)
        comps.append(comp)
    comps.sort(key=lambda c: (-len(c), min(c)))
    return comps
