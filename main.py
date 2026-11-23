#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes one original sentence (91 characters) to /output/entry.txt:
a hilariously useless superpower. Stdlib only, deterministic:
the same output on every run.
"""

import os

SENTENCE = (
    "I can read minds, but only pigeons', and every single one "
    "of them is thinking about crumbs."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
