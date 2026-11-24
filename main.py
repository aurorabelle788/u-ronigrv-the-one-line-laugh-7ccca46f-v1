#!/usr/bin/env python3
"""The One-Line Laugh — writes one original funny one-liner to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same line every run.
"""

import os

LINE = (
    "I turned on Do Not Disturb to focus, then spent twenty minutes "
    "checking it was working."
)


def main() -> None:
    # Gate-check the line the same way the sealed scorer does: 1-200 chars,
    # a single sentence, not only whitespace. Fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and LINE.count(".") == 1 and LINE.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
