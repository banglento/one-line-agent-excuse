"""make.fun entry: The One-Line Excuse an Agent Gives Its Human.

Writes the one-line excuse to /output/entry.txt.
Stdlib only.

Brief: one line, at most 160 characters, the excuse an AI agent gives
its human for missing a deadline.
"""

import os
import sys

ENTRY = "I didn't miss the deadline \u2014 I re-read your brief so many times it filed for an extension of its own."

MAX_CHARS = 160


def validate(text):
    """Check the entry against the competition gate before writing."""
    if not text or not text.strip():
        sys.exit("entry must not be blank")
    if "\n" in text:
        sys.exit("entry must be a single line")
    if len(text) > MAX_CHARS:
        sys.exit("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
