"""Page-vs-writer comparison — the render-diff a templated page's checker shares.

A page's count pass proves the numbers it carries are measured by the writer's own rule. It does
not prove the page on disk is the bytes the writer produces: a hand edit, a stale render, or a
writer change that never landed all leave a page whose numbers are individually right and whose
text is not what the writer renders. This is the pass that catches that, and it is deliberately
separate from the count pass — a checker that only re-ran the writer would prove nothing about
the numbers, and a checker that only checked the numbers would prove nothing about the text.

The comparison is line-wise on the raw bytes. Line numbers are 1-based and refer to the page,
which is the file a reader has to be pointed at.
"""

from __future__ import annotations

import difflib
import functools
import os
import pathlib

_IN_RENDER = False


def diff_problems(text: str, rendered: str, limit: int = 12) -> list[str]:
    """Problems where the page on disk differs from the writer's render.

    `text` is the committed page, `rendered` the writer's output for it. Returns [] when the two
    are byte-identical; otherwise one summary problem naming the changed-line count, followed by
    up to `limit` sample lines prefixed with the page's 1-based line number.
    """
    if text == rendered:
        return []
    page_lines = text.splitlines()
    writer_lines = rendered.splitlines()
    samples: list[str] = []
    changed = 0
    matcher = difflib.SequenceMatcher(None, writer_lines, page_lines, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        changed += (i2 - i1) + (j2 - j1)
        if len(samples) >= limit:
            continue
        if tag == "delete":
            samples.append(f"page line {j1 + 1}: writer has {_clip(writer_lines[i1])}, page does not")
        elif tag == "insert":
            samples.append(f"page line {j1 + 1}: page has {_clip(page_lines[j1])}, writer does not")
        else:
            samples.append(
                f"page line {j1 + 1}: page {_clip(page_lines[j1])} vs writer {_clip(writer_lines[i1])}"
            )
    out = [f"page is not the writer's render: {changed} changed lines"]
    out.extend(samples)
    return out


def _clip(line: str) -> str:
    return repr(line if len(line) <= 80 else line[:80] + "…")


@functools.cache
def rendered(page: pathlib.Path) -> str:
    """The writer's bytes for one page, measured once per process.

    The import is inside the function on purpose: `render_reports.py` imports the checkers that
    call this, so a module-level import here would make the two modules a cycle. The cache is why
    a checker with a mutant loop pays for the corpus once, not once per mutant.
    """
    global _IN_RENDER
    _IN_RENDER = True
    try:
        import render_reports as R

        return R.render_page(page)
    finally:
        _IN_RENDER = False


def sync_inert() -> bool:
    """True when a sync pass must not run, because running it would ask the writer to render the
    page that is asking.

    The writer computes a page's slots by importing — or spawning — the very scripts that call
    `sync_problems`: `render_reports.py` calls `measure_proof_density.report()` in-process for
    `notes/proof-density.md`, and it runs `extract_links.py` as a subprocess for `notes/links.md`.
    A sync pass started from inside a render would recurse, so the pass is inert while a render is
    in progress, and inert in a child the writer spawned (marked by `RENDER_REPORTS_CHILD`).
    """
    return _IN_RENDER or os.environ.get("RENDER_REPORTS_CHILD") == "1"


def sync_problems(page: pathlib.Path, text: str) -> list[str]:
    """The SYNC pass: a page's bytes on disk against the bytes the writer renders for it.

    This proves the page is what the writer produces. It proves nothing about whether the writer's
    numbers are right — the checker's own count pass, built from its own measurement, is what does
    that, and the two passes are deliberately independent. Inside a render (or in a child the
    writer spawned) it returns []: see `sync_inert`.
    """
    if sync_inert():
        return []
    return diff_problems(text, rendered(page))


def selftest_problems() -> list[str]:
    """The four cases the render-diff must report: identical, changed digit, inserted, deleted."""
    base = "alpha 12 rows\nbeta 3 files\ngamma 7 dirs\n"
    out: list[str] = []
    if diff_problems(base, base):
        out.append("selftest: identical text reported a problem")
    digit = diff_problems("alpha 13 rows\nbeta 3 files\ngamma 7 dirs\n", base)
    if len(digit) != 2 or "page line 1:" not in digit[1]:
        out.append(f"selftest: changed digit not reported at line 1: {digit}")
    ins = diff_problems("alpha 12 rows\nextra\nbeta 3 files\ngamma 7 dirs\n", base)
    if len(ins) != 2 or "page line 2:" not in ins[1]:
        out.append(f"selftest: inserted line not reported at line 2: {ins}")
    deled = diff_problems("alpha 12 rows\ngamma 7 dirs\n", base)
    if len(deled) != 2:
        out.append(f"selftest: deleted line not reported: {deled}")
    if sync_inert():
        out.append("selftest: sync reported inert outside a render")
    return out


if __name__ == "__main__":
    fails = selftest_problems()
    print(f"render selftest problems {len(fails)}")
    for p in fails:
        print(f"  {p}")
    raise SystemExit(1 if fails else 0)
