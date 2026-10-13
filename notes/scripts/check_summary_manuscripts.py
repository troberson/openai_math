#!/usr/bin/env python3
"""Report which manuscripts each summary page reads, and whether the release still names them.

`verify_summaries.py` proves a cited file exists and that a quotation is verbatim on the line it
cites. Neither test can see the failure a release update actually produces: the update supersedes a
manuscript by shipping a new dated directory, and it leaves the superseded directory on disk. Every
anchor in the page then stays green while the page describes a manuscript the catalog no longer
lists for that family.

The rule here is the one the checker cannot infer from the filesystem, because both directories are
real. `overview.tex` names 719 distinct manuscript directories; 749 exist under `preprints/`, so 30
are on disk and unnamed. A page is *current* when every manuscript directory it names is named by
the family the page belongs to, and *stale* when its declared manuscript root is not.

The page read — family number, manuscript directories, declared root — is `catlib/summaries.py`'s,
shared with `verify_summaries.py`. The root rule is the first backticked `preprints/` path in the page:
the root-declaring prose ships in **13** forms across the 21 pages and **5** pages declare their root
inside a table row, so a rule keyed on the `Manuscript root — ` phrase sees 2 pages and reports "no
declared root" on 19.

Report-only; writes nothing.

Usage: python3 notes/scripts/check_summary_manuscripts.py          # every page
       python3 notes/scripts/check_summary_manuscripts.py <page.md> ...
"""
import sys
from pathlib import Path

from catlib.paths import PREPRINTS, ROOT, SUMMARIES_DIR
from catlib.summaries import named_dirs, page_dirs, page_fam

SUMMARIES = SUMMARIES_DIR


def main():
    args = sys.argv[1:]
    pages = [Path(a).resolve() for a in args] if args else sorted(SUMMARIES.glob("**/*.md"))
    named = named_dirs()
    disk = {p.name for p in PREPRINTS.iterdir() if p.is_dir()}

    stale_pages = 0
    total_dirs = 0
    unnamed = 0
    foreign = 0
    for path in pages:
        fam = page_fam(path.name)
        dirs, root = page_dirs(path)
        if fam is None:
            stale_pages += 1
            print(f"===== {path.relative_to(ROOT)}  [no family id in the page name]")
            continue
        total_dirs += len(dirs)
        bad = []
        for d in dirs:
            owners = named.get(d)
            if owners is None:
                unnamed += 1
                bad.append(f"{d} — named by NO family (superseded; {len(disk)} dirs on disk, "
                           f"{len(named)} named)")
            elif fam not in owners:
                foreign += 1
                bad.append(f"{d} — named by family {', '.join(sorted(owners))}, not {fam}")
        root_state = "no declared root"
        if root:
            owners = named.get(root)
            root_state = ("root " + (f"{root} named by {fam}" if owners and fam in owners
                                      else "NOT named by " + fam))
        if bad:
            stale_pages += 1
            print(f"===== {path.relative_to(ROOT)}  [{root_state}]")
            for b in bad:
                print(f"    {b}")
    print(f"\npages {len(pages)}  pages with an off-family manuscript {stale_pages}  "
          f"manuscript dirs named {total_dirs}  unnamed-on-catalog {unnamed}  "
          f"named-by-another-family {foreign}")
    named_set = set(named)
    print(f"preprint dirs on disk {len(disk)}  distinct dirs named by overview.tex {len(named_set)}  "
          f"on disk and unnamed {len(disk - named_set)}  named and absent {len(named_set - disk)}")
    raise SystemExit(0)


main()
