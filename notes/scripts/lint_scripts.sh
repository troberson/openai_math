#!/usr/bin/env bash
# Proof chain for the lint trio over notes/scripts/, capturing each tool's OWN exit code.
# The extracted checker self-tests live inside that tree (notes/scripts/tests/), so the trio checks
# them with the scripts; no second scope is needed.
# pylint needs PYTHONPATH so it can import the module-level render_reports import.
# Root from git, not from the script's depth: "$(dirname "$0")/../.." is correct only at exactly
# two levels below the root.
cd "$(git rev-parse --show-toplevel)" || exit 1
set -u

echo "== ruff"
.venv/bin/ruff check notes/scripts/
echo "ruff exit $?"

echo "== mypy"
.venv/bin/mypy notes/scripts/
echo "mypy exit $?"

echo "== pylint"
PYTHONPATH=notes/scripts .venv/bin/pylint notes/scripts/
echo "pylint exit $?"

echo "LINT_PROOF_DONE"
TZ=UTC date -u +%H:%M:%S
