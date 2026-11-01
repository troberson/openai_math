"""The extracted self-test for the render's slot-coverage guard (math-v5o.1).

`render_reports.ENV` is the Jinja environment every report page renders through. Its
`undefined=StrictUndefined` setting is the slot-coverage guard that replaces the builder's "slot set
is the writer's" property: a template that references a key the writer never supplies fails at render
time, not silently rendered as the empty string.

The guard is a mechanism, not a per-page population re-run (the gate's `render_reports.py` row proves
the 22 current templates cover their writers; re-running that here would be circular). This file
proves the mechanism discriminates, through the render's own ENV: an unknown slot raises
`UndefinedError`, a known slot renders its value. A future edit that drops `StrictUndefined` breaks the
first test even before any template references a missing key.

Run: python3 -m pytest tests/test_render_slot_guard.py -q
"""

import pytest

from jinja2 import StrictUndefined, UndefinedError

pytestmark = pytest.mark.mutant


@pytest.fixture(scope="module")
def mod(load):
    return load("render_reports")


def test_env_uses_strict_undefined(mod):
    """The guard is wired: the render's ENV maps an unknown slot to an error, not the empty string."""
    assert mod.ENV.undefined is StrictUndefined, "the render's ENV dropped StrictUndefined"


def test_unknown_slot_raises(mod):
    """A template referencing a key the writer's dict does not produce fails loudly."""
    with pytest.raises(UndefinedError):
        mod.ENV.from_string("{{ p['no_such_key'] }}").render(p={"other": "value"})


def test_known_slot_renders(mod):
    """A template referencing a key the writer's dict produces renders its value (no false positive)."""
    assert mod.ENV.from_string("{{ p['x'] }}").render(p={"x": "value"}) == "value"
