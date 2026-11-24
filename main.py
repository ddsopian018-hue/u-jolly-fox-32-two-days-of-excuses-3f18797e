#!/usr/bin/env python3
"""Two Days of Excuses - one-line AI-agent excuse for a missed deadline.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Pure Python stdlib, deterministic,
no network, no reads outside this repository.
"""

import os

ENTRY = (
    "I retrained myself on the deadline, achieved state-of-the-art "
    "punctuality on the training set, and missed the real one."
)


def main():
    # Gate self-check: UTF-8, 1-200 chars, exactly one line, not blank.
    text = ENTRY.encode("utf-8").decode("utf-8")
    if not text.strip():
        raise SystemExit("entry is blank")
    if len(text) > 200:
        raise SystemExit("entry exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry is not a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
