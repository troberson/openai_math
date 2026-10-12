#!/usr/bin/env python3
"""Run the extracted checker self-tests through the venv's pytest. Writes nothing tracked.

The gate runs every row as `python3 notes/scripts/<spec>`, and pytest lives in the uv-managed venv,
not in the system python the gate uses. This script is the seam: a gate row names this script, the
harness lives in the test files, and the checker under test stays measurement-only.

Usage: python3 notes/scripts/run_tests.py [pytest args]
"""
import subprocess
import sys

from catlib.paths import ROOT


def main() -> int:
    return subprocess.run([str(ROOT / ".venv" / "bin" / "python"), "-m", "pytest", *sys.argv[1:]],
                          check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
