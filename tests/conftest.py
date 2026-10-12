"""The shared loader for the extracted checker self-tests.

The checkers import their siblings by bare name (`import extract_scope_notes as ex`) and import the
`catlib` package, so the script tree has to be on `sys.path` before any checker is imported. Each
checker is loaded as a module from its file, which is what makes `ROOT = Path(__file__).resolve().parents[2]`
resolve to the repo root inside it.
"""

import importlib.util
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "notes" / "scripts"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


@pytest.fixture(scope="session")
def load():
    """Return the loader: name -> the checker as a module."""

    def _load(name: str):
        spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    return _load
