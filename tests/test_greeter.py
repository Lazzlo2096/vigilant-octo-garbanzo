from pathlib import Path
import sys

import pytest

# Ensure the project root is on sys.path so we can import ``greeter`` as a module.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from greeter import make_greeting


@pytest.mark.parametrize(
    ("raw_name", "expected"),
    [
        ("World", "Hello, World!"),
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_make_greeting_accepts_various_names(raw_name: str, expected: str) -> None:
    assert make_greeting(raw_name) == expected


def test_make_greeting_trims_surrounding_whitespace() -> None:
    assert make_greeting("  TDD  ") == "Hello, TDD!"


def test_make_greeting_rejects_blank_names() -> None:
    with pytest.raises(ValueError):
        make_greeting("   ")


def test_make_greeting_requires_string_input() -> None:
    with pytest.raises(TypeError):
        make_greeting(123)  # type: ignore[arg-type]
