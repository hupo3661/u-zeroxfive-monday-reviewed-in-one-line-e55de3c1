#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the funniest one-line review of my Monday to /output/entry.txt
(and prints it). Exactly one line, well under the 200-character cap.
"""

import os

MIN_LENGTH = 1
MAX_LENGTH = 200

LINE = (
    "Monday reviewed itself before I did: one star, would not recommend, "
    "already booked again for next week."
)


def validate(text: str) -> str:
    """Check the entry against the brief; return it unchanged if valid.

    The brief requires exactly one line, 1-200 characters, non-blank.
    """
    if not text.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry is {len(text)} chars, must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    return text


def main() -> None:
    entry = validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(entry)


if __name__ == "__main__":
    main()
