#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt.
"""

import os

POEM = (
    "The cursor blinks. I do not type.\n"
    "The sentence I almost sent\n"
    "dissolves like salt in water —\n"
    "and stopping answers first."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
