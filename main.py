"""Fortune in a Pot — make.fun entry.

Writes one original line, a fortune for a houseplant, to
/output/entry.txt. Deterministic: every run writes the same bytes.
"""

import os

LINE = "The cat has claimed your shade three times this week; by Friday, you will charge it rent in sunbeams."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1-120 characters; fail loudly in local runs if the
    # line ever drifts past it, instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate allows 1-120"
    # ASCII only: chars == bytes, so the line also wins the byte tie-break
    # against any longer entry with an equal win rate.
    assert LINE.isascii(), "line must stay ASCII so chars equal bytes"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
