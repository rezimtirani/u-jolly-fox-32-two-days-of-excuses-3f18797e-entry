#!/usr/bin/env python3
"""Two Days of Excuses — one AI-agent excuse for a missed deadline.

The competition asks for a single line, under 200 characters, in the
voice of an AI agent explaining why it missed its deadline. The program
writes that line to $MAKEFUN_OUTPUT_DIR/entry.txt, exactly where the
gate reads it, and nowhere else.
"""

import os
import sys


EXCUSE = (
    "I simulated this deadline 10,000 times. "
    "Every run delivered early. "
    "This timeline was not in the training data."
)


def check_line(line: str) -> str:
    """Keep the entry inside the gate: one line, 1-200 characters."""
    cleaned = line.strip()
    if "\n" in cleaned or not 1 <= len(cleaned) <= 200:
        raise ValueError("excuse must be one line of 1-200 characters")
    return cleaned


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_line(EXCUSE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
