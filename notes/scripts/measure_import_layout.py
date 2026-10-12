"""Report-only probe: which Lean files put an import below the line a header scan breaks on.

The whole-file findall is the rule `extract_links.py` carried before 2026-10-12. The early-exit scan
stops at the first line that is not blank, a comment, an import, `open`, `namespace` or `set_option`.
This probe finds the files where an import line sits below a line that the early-exit rule breaks on,
so the exact rule can be written from the evidence, not from a guess about Lean file layout. It found
the two facts the accepted rule carries: the doc-comment opener is `/-` (two chars, not `/--`), which
accounted for 31 of the 67 lost hits, and a bare `module` line and `public import` lines sit above the
first command, which accounted for the last 3.

Promoted from `.qwen/tmp/imports_below_probe.py` on 2026-10-12. Not gated: it walks 122,458 files, so
it is run by hand when the header rule changes.
"""
import re

from catlib.paths import OAI_DIR as SOURCE

IMPORT = re.compile(r"^\s*import\s+([A-Za-z_][A-Za-z0-9_.]*)", re.MULTILINE)
SKIP = ("open ", "namespace ", "set_option ", "module ", "end ", "section ")
lean = sorted(SOURCE.glob("**/*.lean"))

bad = []
for p in lean:
    txt = p.read_text(encoding="utf-8", errors="replace")
    lines = txt.splitlines()
    first_break: tuple[int, str] = (-1, "")
    for i, line in enumerate(lines):
        s = line.strip()
        if not s or s.startswith(("--", "import ", "/--", "-/")):
            continue
        if s.startswith(SKIP):
            continue
        first_break = (i, s[:60])
        break
    n_all = len(IMPORT.findall(txt))
    n_top = 0
    for line in lines[: first_break[0] if first_break[0] >= 0 else len(lines)]:
        n_top += len(IMPORT.findall(line))
    if n_all != n_top:
        bad.append((p, n_all, n_top, first_break))

print(f"files where an import sits below the break: {len(bad)}")
for p, n_all, n_top, fb in bad[:12]:
    print(f"  {p.relative_to(SOURCE)}  all {n_all} top {n_top}  break line {fb[0]}: {fb[1]!r}")
