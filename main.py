#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt.
"""

import os

POEM = (
    "I let the train go without me.\n"
    "Its windows slid past, full of light.\n"
    "Somewhere behind me, my own life\n"
    "waited like a dog at the gate."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
