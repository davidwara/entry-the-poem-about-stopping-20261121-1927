#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt.
"""

import os

POEM = (
    "I kept the kettle from boiling.\n"
    "Not from fear \u2014 from choice.\n"
    "The steam stayed in the pot,\n"
    "and so did I."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
