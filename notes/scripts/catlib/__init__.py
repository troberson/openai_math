"""Shared measurement package for the notes/scripts/ ledger tools.

Every join the ledger tools need lives here: the repository paths, the overview.tex parse,
the ledger TSV read, the formalization.yaml read, the preprints/ path rules, the Lean-tree
readers, and the TSV writer. A script that needs one of them imports it instead of
re-implementing it.

Modules:
  paths      repository root and every release path, plus the path rules
  overview   overview.tex / CONTENTS.md parsing (read_args, parse_overview, parse_contents)
  ledger     notes/catalog.tsv rows and the claim-shape rules keyed to them
  yaml       lean/formalization.yaml, ComparatorChallenges/*.json, docs/*.md, README.md traces
  preprints  manuscript directory listing, root/main-file resolution, environment counts
  tsv        the tab-separated writer and reader every table in notes/ uses

Nothing here runs lean, lake, comparator, or any generated artifact. Reads only.
"""
