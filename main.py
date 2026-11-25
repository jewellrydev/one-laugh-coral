"""One Line, One Laugh (coral-404) — a make.fun entry.

Prints exactly one funny line, capped at 200 characters, that lands
entirely on its own.
"""

LINE = "I told my bathroom scale we should start seeing other numbers."


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
