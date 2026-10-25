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

Each phrase is located with a whitespace-flexible, number-exact regex over the WHOLE page (the page
wraps phrases across lines, but a digit must match the measured value). All matches are collected,
sorted, and rejected on overlap, then replaced from the end so offsets stay valid. A stale number is
NOT FOUND and fails the build - it cannot silently stay literal or be relaxed onto a neighbouring
span. A phrase the page wraps is split at the page's OWN line breaks, keeping each
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

The 21 pages are built in a fork pool, because the wall is the per-page measurement, not the page
loop: measured 2026-10-11, `build_report_templates.py --check-only` runs 190.45 s with user 182.585 s
(one core), of which 173.02 s is the writer measurement, 15.08 s the needle derivation, 0.10 s the
`git show` calls and the regex locate. `build()` is pure and returns its report lines, so the PARENT
prints in sorted page order and stages in sorted page order - the slot numbering `Staging` gives
(`len(self._targets)`) is the serial numbering, and the report is the bytes a serial run prints. A
worker writes nothing: staging is one writer's approval, and 21 workers writing the same slot `0000`
is not it. The pages share caches per process (`measure_names.measure()` is `@cache`d), so a pool
multiplies the corpus walk it needs - the floor is the slowest page, `notes/development/templates.md`,
whose population runs the needle derivation for all 19 distinct checkers.
"""
from __future__ import annotations

import multiprocessing as mp
import pathlib
import re
import subprocess
import sys

import render_reports as R  # prewarm() before the fork; see main()
from catlib import splits as SP
from catlib import templates as T
from catlib import text as TX
from catlib import tsv as TSV
from catlib.atomic import Staging
from catlib.paths import SPLIT_TSV
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


def split_parts(matched: str, label: str, phrase: str) -> tuple[list[str], list[str]]:
    """Split the matched span at the page's line breaks, keeping each break's exact whitespace.

    The parts are validated with `catlib.text.apply_split` - the render's own rule - not with a second
    matcher here. `flex` refuses to relax a number-only needle because a needle searched anywhere in a
    page has no literal anchor, but a recorded part is matched only at the start of the remainder, so its
    digits can move freely; 201 of the 1,069 recorded parts are number-only and would raise on a drift
    under the exact rule.
    """
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
    try:
        TX.apply_split(label, phrase, parts)
    except ValueError as exc:
        print(f"SPLIT MISMATCH for {phrase!r}\n  parts: {parts}\n  {exc}")
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


def exact_phrase(phrase: str) -> re.Pattern[str]:
    """Whitespace-flexible, number-exact matcher: the page may wrap a phrase across lines, but
    every digit must match the measured value.

    A stale number is NOT FOUND, never relaxed and re-slotted: the flex rule that let a HEAD
    literal disagree with the measurement is gone. A page whose literal disagrees with the
    writer's value is a build failure, so the figure cannot silently stay literal.
    """
    return re.compile(r"\s+".join(re.escape(tok) for tok in phrase.split()))


def build(page_rel: str, checker_name: str) -> tuple[int, list[str], pathlib.Path, str, list[dict[str, str]]]:
    """One page's template, built without writing: (rc, report lines, template path, template text, rows).

    The per-page work is pure — `git show HEAD:<page>`, the writer's slot dict, the regex locate, the
    needle derivation, the string replacement — so it runs in a pool worker. Staging is NOT here: the
    parent stages, in sorted page order, which is what makes the slot numbering the serial numbering.
    Every line this function would have printed is returned in `lines` so the parent prints the report
    in page order.

    `rows` is this page's part of `notes/tables/splits.tsv`: one row per recorded part, in the page's
    own order, for a label the page breaks. A label the page does not break is one slot and has no row.
    """
    lines: list[str] = []
    label_fn = T.LABELS.get(page_rel)
    if label_fn is None:
        lines.append(f"no writer slot dict recorded for {page_rel}")
        return 1, lines, pathlib.Path(""), "", []
    labels = label_fn()
    groups = T.group_labels(labels)

    text = committed_page(page_rel)
    hits: list[tuple[int, int, str, list[tuple[str, str]]]] = []
    for base, parts in groups.items():
        needle = " ".join(v for _, v in parts)
        found = list(exact_phrase(needle).finditer(text))
        if not found:
            # Fail hard: the page's literal disagrees with the measured value. A stale figure must
            # not stay literal, and a number must not be relaxed onto a neighbouring span.
            lines.append(f"NOT FOUND ({base}): {needle!r} - stale figure; "
                         f"the page's literal disagrees with the measurement")
            return 1, lines, pathlib.Path(""), "", []
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
            return 1, lines, pathlib.Path(""), "", []
        kept.append(h)
    hits = kept

    slots: dict[str, str] = {}
    nslots = 0
    wrapped: list[str] = []
    # (start, base, part): the replacement loop runs `reversed(hits)` to keep offsets valid, which would
    # otherwise record a page's parts backwards, so the start is kept and the rows sorted at the end.
    rows: list[tuple[int, str, str]] = []
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
            split, seps = split_parts(matched, base, " ".join(v for _, v in parts))
            if len(split) != len(parts):
                lines.append(f"WRAP MISMATCH ({base}): page splits into {len(split)}, "
                             f"writer has {len(parts)}")
                return 1, lines, pathlib.Path(""), "", []
            rows.extend((start, base, p) for p in split[:-1])
            exprs = []
            for i in range(len(split)):
                slots[TX.part_label(base, i)] = split[i]
                exprs.append("{{ p['" + TX.part_label(base, i) + "'] }}")
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
    return 0, lines, out, full, [{"page": page_rel, "label": b, "part": p} for _, b, p in sorted(rows)]


def worker(page_checker: tuple[str, str]) -> tuple[int, list[str], pathlib.Path, str, list[dict[str, str]]]:
    """`build` as a pool task: a `sys.exit(1)` from `split_parts` becomes rc 1, not a traceback.

    `split_parts` exits the process on a SPLIT MISMATCH; in a worker that would raise SystemExit
    through `pool.map` and print a traceback in the parent. The serial builder exits 1 with its line
    printed, so the conversion keeps the report and the exit code the same.
    """
    page, checker = page_checker
    try:
        return build(page, checker)
    except SystemExit:
        return 1, [], pathlib.Path(""), "", []


def main(argv: list[str]) -> int:
    check_only = "--check-only" in argv
    argv = [a for a in argv if a != "--check-only"]
    if not argv:
        pages = sorted(T.ALL_PAGES.items())
        R.prewarm()
        # fork, not the Python 3.14 default (forkserver): the workers must inherit the parent's
        # _PREWARMED dict so child_out returns cached bytes without spawning a second child.
        # math-gyd.
        with mp.get_context("fork").Pool(POOL) as pool:
            results = pool.map(worker, pages)
        rows: list[dict[str, str]] = []
        for rc, lines, out, text, page_rows in results:
            for line in lines:
                print(line)
            if rc:
                return rc
            rows.extend(page_rows)
            if not check_only:
                ST.stage(out, text)
        if not check_only:
            # Staged after the pages, so the slot numbering stays the serial numbering. `pool.map`
            # preserves the order of `sorted(T.ALL_PAGES.items())`, so the table's row order is the page
            # order the render reads.
            ST.stage(SPLIT_TSV, TSV.csv_text(SP.COLS, rows))
            ST.promote()
        print(f"split table rows {len(rows)}")
        return 0
    if len(argv) != 2:
        print("usage: build_report_templates.py [<notes/page.md> <verify_page.py>]")
        return 2
    rc, lines, out, text, _ = build(argv[0], argv[1])
    for line in lines:
        print(line)
    if rc == 0 and not check_only:
        # A single-page run does not write the table: the table is the whole registry's, and one page's
        # rows would replace it.
        ST.stage(out, text)
        ST.promote()
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
