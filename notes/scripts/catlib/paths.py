"""Repository paths and the path rules every ledger tool shares.

This file sits at notes/scripts/catlib/paths.py, so the repository root is parents[3]:
catlib -> scripts -> notes -> repo root. build_catalog.py, one level up, uses parents[2].
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Release surface
OVERVIEW_TEX = ROOT / "overview.tex"
CONTENTS_MD = ROOT / "CONTENTS.md"
README_MD = ROOT / "README.md"
PREPRINTS = ROOT / "preprints"
REASONING_TRACES = ROOT / "reasoning_traces"

# Lean surface
LEAN = ROOT / "lean"
FORMALIZATION_YAML = LEAN / "formalization.yaml"
LAKEFILE = LEAN / "lakefile.lean"
LAKE_MANIFEST = LEAN / "lake-manifest.json"
COMPARATOR_DIR = LEAN / "ComparatorChallenges"
OAI_DIR = LEAN / "OAI"
DOCS_DIR = LEAN / "docs"

# Ledger surface
NOTES = ROOT / "notes"
SCRIPTS = NOTES / "scripts"
TABLES = NOTES / "tables"
LEDGER_TSV = TABLES / "catalog.tsv"
SOURCES_TSV = TABLES / "sources.tsv"
LINKS_TSV = TABLES / "links.tsv"
SUBFINDINGS_TSV = TABLES / "subfindings.tsv"
ABSTRACTS_TSV = TABLES / "abstracts.tsv"
DEPS_TSV = TABLES / "formalization-deps.tsv"
STANDING_TSV = TABLES / "conjecture-standing.tsv"
TOPICS_TSV = TABLES / "topics.tsv"
QUOTES_TSV = TABLES / "quotes.tsv"
INDEX_DIR = NOTES / "index"
SUMMARIES_DIR = NOTES / "summaries"

# The eight TSVs the proof gate hashes; the gate's snapshot rule is this list plus every
# file under INDEX_DIR. The snapshot used to name a ninth, notes/named-results.tsv, which
# no writer produces — the named-result page is report-fed, not table-fed — so the phantom
# entry and the 2>/dev/null that hid it are gone together.
GATE_TSVS = (
    LEDGER_TSV,
    SOURCES_TSV,
    LINKS_TSV,
    SUBFINDINGS_TSV,
    ABSTRACTS_TSV,
    DEPS_TSV,
    STANDING_TSV,
    TOPICS_TSV,
)


def rel(path: Path | str) -> str:
    """Repo-relative POSIX path, the form every table cell and citation anchor uses."""
    p = Path(path)
    return p.relative_to(ROOT).as_posix() if p.is_absolute() else Path(p).as_posix()


def owner(path: Path | str) -> str:
    """Manuscript directory name a preprints/ path belongs to.

    The component after `preprints`, never parts[-2]: every one of the 719 resolved main
    files sits under a `build/` directory, so parts[-2] files manuscripts under `build/`
    and `sections/` and silently makes every cross-family join match nothing.
    """
    parts = Path(path).parts
    return parts[parts.index("preprints") + 1]


def read_text(path: Path) -> str:
    """The repo's whole read surface is UTF-8 text; one call site for the encoding."""
    return path.read_text(encoding="utf-8")
