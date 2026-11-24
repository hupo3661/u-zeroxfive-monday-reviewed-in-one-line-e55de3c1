#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the funniest one-line review of my Monday to /output/entry.txt
(and prints it). Exactly one line, well under the 200-character cap.
"""

import os

LINE = (
    "Monday reviewed itself before I did: one star, would not recommend, "
    "already booked again for next week."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be exactly one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
