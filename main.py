#!/usr/bin/env python3
"""The One-Line Laugh — write one original funny line to /output/entry.txt.

The joke is a single sentence, at most 200 characters: an everyday truth
(the snooze button) with a surprise at the end that still makes sense.
"""

from pathlib import Path

JOKE = (
    "I set my alarm for 6 a.m. and my snooze button for 6:05, 6:10, "
    "6:15, and eventually, unemployment."
)


def main() -> None:
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("line must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    # Read back and confirm exactly what the judge will see.
    written = out.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("round-trip mismatch")
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
