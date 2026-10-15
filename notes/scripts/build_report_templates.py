#!/usr/bin/env python3
r"""Build a report template from a committed page and the slot dict its writer supplies.

Writer: notes/templates/report/<page>.j2. It rewrites `git show HEAD:<page>` by replacing every
phrase the writer can produce with a `{{ p['<label>'] }}` slot, so the template's literal text -
quotations, anchors, fenced blocks, numbers the writer does not compute - is byte-exact by
construction, and the slot labels and phrase strings come from the writer's own code, not from a
transcription.

The slot set is the writer's, because the writer's slot dict *is* the template's slot set:
render_reports.py builds one dict per page (`phrases`, `abstracts_phrases`, `named_results_phrases`,
`index_phrases`) and passes it to the template as `p`, and its split tables (`NR_SPLIT`,
`INDEX_SPLIT`) are what give the " a"/" b" labels. A template built from any other list - e.g. the
checker's needle list, which is wider - renders slots the writer never supplies, and Jinja renders an
unknown key as the empty string: the page silently loses text. The page's checker needles are read
too, and reported as coverage (slotted / left literal), never as the slot source.

The registry (page -> checker), the writer's per-page slot dicts, the needle derivation and the
number-flexible matcher `flex` are in `catlib/templates.py`, so the builder, the writer's split
tables, `measure_checker_needles.py` and `measure_templates.py` read one rule. What stays here is
the writer path: the locate, the split at the page's own line breaks, the raw-block wrapping, and
the `git show HEAD:<page>` read - a revision, which the package does not own.

Each phrase is located with a whitespace-flexible regex over the WHOLE page (the page wraps phrases
across lines), all matches collected, sorted, and rejected on overlap, then replaced from the end so
offsets stay valid. A phrase the page wraps is split at the page's OWN line breaks, keeping each
break's exact whitespace run as the separator so the rendered page wraps identically; split labels
get " a", " b", ... suffixes. render_reports.py keeps the matching prefix table and raises if a
prefix stops matching the measured phrase, so a drifted number fails the render instead of reflowing
the page.

Literal runs are wrapped in `{% raw %}` / `{% endraw %}` when they carry LaTeX. The pages quote
`\newtheorem` and `\char` blocks verbatim; unescaped, a `{` in such a line is a Jinja expression
start and the template fails to compile (`unexpected char '\\'`). Wrapping is safe: with
`trim_blocks` a tag on its own line emits nothing, so the wrapped lines render byte-identically.

Run it from a clean checkout of the page it rebuilds: it reads HEAD, not the working tree. Proof
after any rebuild is the render - `python3 notes/scripts/render_reports.py` twice, pages
byte-identical to HEAD. Prints the label -> phrase-part dict the writer supplies. Touches no page.

The 18 pages are built in a fork pool, because the wall is the per-page measurement, not the page
loop: measured 2026-10-11, `build_report_templates.py --check-only` runs 190.45 s with user 182.585 s
(one core), of which 173.02 s is the writer measurement, 15.08 s the needle derivation, 0.10 s the
`git show` calls and the regex locate. `build()` is pure and returns its report lines, so the PARENT
prints in sorted page order and stages in sorted page order - the slot numbering `Staging` gives
(`len(self._targets)`) is the serial numbering, and the report is the bytes a serial run prints. A
worker writes nothing: staging is one writer's approval, and 18 workers writing the same slot `0000`
is not it. The pages share caches per process (`measure_names.measure()` is `@cache`d), so a pool
multiplies the corpus walk it needs - the floor is the slowest page, `notes/development/templates.md`,
whose population runs the needle derivation for all 18 checkers.
"""
from __future__ import annotations

import multiprocessing as mp
import pathlib
import re
import subprocess
import sys

from catlib import templates as T
from catlib import text as TX
from catlib.atomic import Staging
from catlib.promote import key_for

ROOT = pathlib.Path(__file__).resolve().parents[2]
TPL_DIR = ROOT / "notes" / "templates" / "report"
# The builder reads each page from HEAD, so its L1 is the page set, and `key_for` hashes that L1 from
# HEAD for this writer: the key is a function of the bytes it reads, not of the working tree. Its own
# output feeds one L1 entry — notes/development/templates.md tabulates the template bytes — so a
# render after the builder moves that page and a working-tree key would stop matching the key this run
# used.
KEY = key_for("build_report_templates.py", tuple(sys.argv[1:]))
ST = Staging("build_report_templates", KEY)
WS_RUN = re.compile(r"[ \t]*\n[ \t]*")
# Measured 2026-10-11: the pool wall equals the slowest page (notes/development/templates.md, 71 s
# cold), so 6 workers reach the floor (69.34 s) and 12 and 18 do not beat it (66.56 s / 68.71 s); 6
# keeps the concurrent peak at ~600 MB of the 847 MB the 18 isolated pages measure.
POOL = 6

# The registry, the writer's slot dicts and the needle derivation are in catlib/templates.py;
# this module is the writer path that turns them into a template.

def committed_page(page_rel: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{page_rel}"],
                          capture_output=True, text=True, check=True).stdout


def split_parts(matched: str, phrase: str) -> tuple[list[str], list[str]]:
    """Split the matched span at the page's line breaks, keeping each break's exact whitespace."""
    runs = list(WS_RUN.finditer(matched))
    if not runs:
        return [matched], [" "]
    parts: list[str] = []
    seps: list[str] = []
    pos = 0
    for r in runs:
        parts.append(matched[pos:r.start()].rstrip(" \t"))
        seps.append(r.group(0))
        pos = r.end()
    parts.append(matched[pos:].lstrip(" \t"))
    if not TX.flex(phrase).fullmatch(" ".join(parts)):
        print(f"SPLIT MISMATCH for {phrase!r}\n  parts: {parts}")
        sys.exit(1)
    return parts, seps


def raw_wrap(text: str) -> str:
    """Wrap literal runs that carry LaTeX in a raw block so the template compiles.

    The opening tag is glued to the run's FIRST line — `{% raw %}<line>` — not put on its own line.
    Jinja captures a raw block's body verbatim, `trim_blocks` included, so a tag on its own line emits
    the newline that follows it (a plain `{% raw %}` gains a blank line), and the whitespace-control
    form `{%- raw %}` strips ALL preceding whitespace, which deletes the blank line of a
    "heading, blank, LaTeX paragraph" sequence. Glued, the tag consumes nothing: the newline before it
    is literal text, no newline follows the tag, and `trim_blocks` consumes only the newline after
    `{% endraw %}`. The run then renders byte-identically.
    """
    out: list[str] = []
    run: list[str] = []

    def flush() -> None:
        if run:
            out.append("{% raw %}" + run[0])
            out.extend(run[1:])
            out.append("{% endraw %}")
            run.clear()

    for line in text.split("\n"):
        # Only the markers THIS builder emits are Jinja constructs. A literal page line can carry `{{`
        # or `{%` as LaTeX — sources.md quotes `\item{{{\ttfamily\char`\\documentclass}` and
        # `\def\extractclass#1#2@{%`, and flushing on those leaves the line unescaped, so the template
        # fails to compile with "unexpected char '\\'".
        if ("{{ p['" in line or line.startswith(("{% raw %}", "{% endraw %}", "{#"))):
            flush()
            out.append(line)
        elif "\\" in line or "{" in line or "}" in line:
            run.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return "\n".join(out)


def build(page_rel: str, checker_name: str) -> tuple[int, list[str], pathlib.Path, str]:
    """One page's template, built without writing: (rc, report lines, template path, template text).

    The per-page work is pure — `git show HEAD:<page>`, the writer's slot dict, the regex locate, the
    needle derivation, the string replacement — so it runs in a pool worker. Staging is NOT here: the
    parent stages, in sorted page order, which is what makes the slot numbering the serial numbering.
    Every line this function would have printed is returned in `lines` so the parent prints the report
    in page order.
    """
    lines: list[str] = []
    label_fn = T.LABELS.get(page_rel)
    if label_fn is None:
        lines.append(f"no writer slot dict recorded for {page_rel}")
        return 1, lines, pathlib.Path(""), ""
    labels = label_fn()
    groups = T.group_labels(labels)

    text = committed_page(page_rel)
    hits: list[tuple[int, int, str, list[tuple[str, str]]]] = []
    ambiguous: list[str] = []
    for base, parts in groups.items():
        needle = " ".join(v for _, v in parts)
        found = list(TX.flex(needle).finditer(text))
        if not found:
            lines.append(f"NOT FOUND ({base}): {needle!r}")
            return 1, lines, pathlib.Path(""), ""
        spans = {" ".join(text[m.start():m.end()].split()) for m in found}
        if len(spans) > 1:
            # A slot is one place in the page. A needle that fires on more than one *different* span is
            # ambiguous, so it is left literal and reported: the "631M" needle for the preprints size
            # also matched "**1740M**" and "**14M**", which rendered all three du surfaces as 631M.
            # Repeated identical spans are fine — the README states the family-342 coverage gap twice,
            # once wrapped — so the test is span identity, not match count. A weak needle is the
            # writer's work list: widen the label value until it names its own words.
            ambiguous.append(base)
            continue
        hits.extend((m.start(), m.end(), base, parts) for m in found)
    # Sort widest-first at each start: a label whose phrase nests inside a wider phrase is
    # slotted by the wider span, and the "covered by" branch only fires for a span that ends
    # inside the kept one. A number-flexible needle makes nesting common — "**12** scripts"
    # and "**12** scripts and **18** catlib modules" are the same region on HEAD's stale bytes.
    hits.sort(key=lambda h: (h[0], -h[1]))
    kept: list[tuple[int, int, str, list[tuple[str, str]]]] = []
    for h in hits:
        if kept and h[0] < kept[-1][1]:
            # A label whose phrase is a substring of another label's phrase is already slotted by the
            # wider span; only a partial overlap is a real conflict.
            if h[1] <= kept[-1][1]:
                lines.append(f"covered by {kept[-1][2]!r}: {h[2]!r} [{h[0]}:{h[1]}]")
                continue
            lines.append(f"OVERLAP: {kept[-1][2]!r} [{kept[-1][0]}:{kept[-1][1]}] vs "
                         f"{h[2]!r} [{h[0]}:{h[1]}]")
            return 1, lines, pathlib.Path(""), ""
        kept.append(h)
    hits = kept

    slots: dict[str, str] = {}
    nslots = 0
    wrapped: list[str] = []
    # `ambiguous` is initialized before the needle loop; re-initializing here would discard
    # the weak needles collected there, and the report line would print 0 for a page that has
    # weak needles.
    for start, end, base, parts in reversed(hits):
        matched = text[start:end]
        if len(parts) == 1:
            if "\n" in matched:
                # The writer supplies this phrase as ONE single-line string. Slotting it would drop the
                # page's own line break and reflow the paragraph, so the span stays literal — the
                # template's literal text is byte-exact from the committed page. A phrase the page wraps
                # is slotted only when the writer supplies it as split labels (" a"/" b"), which carry
                # the break as the separator.
                wrapped.append(base)
                continue
            lab, val = parts[0]
            slots[lab] = val
            rendered = "{{ p['" + lab + "'] }}"
            nslots += 1
        else:
            split, seps = split_parts(matched, " ".join(v for _, v in parts))
            if len(split) != len(parts):
                lines.append(f"WRAP MISMATCH ({base}): page splits into {len(split)}, "
                             f"writer has {len(parts)}")
                return 1, lines, pathlib.Path(""), ""
            exprs = []
            for (lab, _), part in zip(parts, split, strict=True):
                slots[lab] = part
                exprs.append("{{ p['" + lab + "'] }}")
            rendered = exprs[0]
            for i in range(1, len(exprs)):
                rendered += seps[i - 1] + exprs[i]
            nslots += len(split)
        text = text[:start] + rendered + text[end:]

    text = raw_wrap(text)
    # The builder names a template by the page's basename; the two README.md pages collide, so the
    # registry's TEMPLATE_NAME map gives the scripts census its own file name. The target stays the
    # locally built constant the ownership rule reads (`out = TPL_DIR / (name)`), so the builder stays
    # visible in the derived writer set.
    name = T.TEMPLATE_NAME.get(page_rel, pathlib.Path(page_rel).name + ".j2")
    out = TPL_DIR / (name)
    header = (f"{{# {pathlib.Path(page_rel).name} - generated by notes/scripts/build_report_templates.py\n"
              f"   from git show HEAD:{page_rel} and the slot dict in notes/scripts/render_reports.py.\n"
              f"   Literal text is byte-exact from the committed page; every {{{{ }}}} slot is a label the\n"
              f"   writer supplies. Proof after a rebuild: render_reports.py twice, page byte-identical. #}}\n")
    full = header + text
    total = text.count("{{ ")
    needles = T.checker_needles(ROOT / "notes" / "scripts" / checker_name)
    lines.append(f"template written: {out.relative_to(ROOT)}")
    lines.append(f"labels {len(labels)} groups {len(groups)} hits {len(hits)} slots {nslots} exprs {total}")
    lines.append(f"template lines {len(full.splitlines())} bytes {len(full.encode())}")
    if ambiguous:
        # A needle that matches more than one distinct span on HEAD's bytes is not landed: the page
        # keeps HEAD's literal and the writer's measured value is not written. This is the work list
        # for widening the label value, the same shape as the split work list below.
        lines.append(f"weak needles {len(ambiguous)} (needle matches >1 distinct span, left literal): "
                     + " ".join(sorted(ambiguous)))
    if wrapped:
        # A phrase the page breaks across lines stays literal unless the writer supplies it as split
        # labels. This list is the work list for the writer's split table (INDEX_SPLIT / NR_SPLIT).
        lines.append(f"left literal {len(wrapped)} (page wraps, writer supplies one string): "
                     + " ".join(sorted(wrapped)))
    if needles:
        lines.append(f"checker needles {len(needles)} slotted "
                     f"{sum(1 for ph, _ in needles if ph in labels.values())} literal "
                     f"{sum(1 for ph, _ in needles if ph not in labels.values())}")
    else:
        # A checker whose needle list cannot be derived from a call with no population gives no
        # coverage signal at all; printing "0 needles" would read as a clean report that checked nothing.
        lines.append(f"checker needles NOT DERIVED ({checker_name}) - coverage unverified")
    lines.append("\n# writer slots (label -> phrase part)")
    for k, v in sorted(slots.items()):
        lines.append(f"    {k!r}: {v!r},")
    return 0, lines, out, full


def worker(page_checker: tuple[str, str]) -> tuple[int, list[str], pathlib.Path, str]:
    """`build` as a pool task: a `sys.exit(1)` from `split_parts` becomes rc 1, not a traceback.

    `split_parts` exits the process on a SPLIT MISMATCH; in a worker that would raise SystemExit
    through `pool.map` and print a traceback in the parent. The serial builder exits 1 with its line
    printed, so the conversion keeps the report and the exit code the same.
    """
    page, checker = page_checker
    try:
        return build(page, checker)
    except SystemExit:
        return 1, [], pathlib.Path(""), ""


def main(argv: list[str]) -> int:
    check_only = "--check-only" in argv
    argv = [a for a in argv if a != "--check-only"]
    if not argv:
        pages = sorted(T.ALL_PAGES.items())
        with mp.Pool(POOL) as pool:
            results = pool.map(worker, pages)
        for rc, lines, out, text in results:
            for line in lines:
                print(line)
            if rc:
                return rc
            if not check_only:
                ST.stage(out, text)
        if not check_only:
            ST.promote()
        return 0
    if len(argv) != 2:
        print("usage: build_report_templates.py [<notes/page.md> <verify_page.py>]")
        return 2
    rc, lines, out, text = build(argv[0], argv[1])
    for line in lines:
        print(line)
    if rc == 0 and not check_only:
        ST.stage(out, text)
        ST.promote()
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
