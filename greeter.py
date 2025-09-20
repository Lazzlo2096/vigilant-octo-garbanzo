"""Utilities for generating friendly greetings."""


def make_greeting(name: str) -> str:
    """Return a greeting for ``name``.

    The function accepts any non-empty string, trims surrounding whitespace,
    and raises a :class:`ValueError` if nothing remains afterwards. Passing a
    non-string value results in a :class:`TypeError` so that callers are
    alerted early to invalid usage.
    """

    if not isinstance(name, str):
        raise TypeError("name must be a string")

    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must be a non-empty string")

    return f"Hello, {cleaned_name}!"
