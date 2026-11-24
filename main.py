#!/usr/bin/env python3
"""Fortune in a Pot — a kind, funny fortune for a houseplant.

Writes one single-line fortune (120 characters or fewer) to
/output/entry.txt, where the make.fun judge reads it.
"""

import os

FORTUNE = "You will read your keeper's fortune next: more sun, less worry, and a second plant by spring."

OUTPUT_PATH = "/output/entry.txt"


def validate(fortune: str) -> None:
    """Guard the kit's gate: UTF-8 text, 1-120 chars, one line, not blank."""
    if not fortune or not fortune.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if len(fortune) > 120:
        raise ValueError(f"fortune is {len(fortune)} characters, over the 120 limit")
    if "\n" in fortune or "\r" in fortune:
        raise ValueError("fortune must be a single line")


def main() -> None:
    validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    if written != FORTUNE:
        raise RuntimeError("output does not match the fortune verbatim")


if __name__ == "__main__":
    main()
