#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — make.fun entry.

Writes one short family scene to /output/entry.txt.
"""

import os

ENTRY = (
    "Dad fixed the wobbly table leg with three books, two coasters, "
    "and my maths homework. Mom pretended not to notice. We ate dinner "
    "on it anyway, like it was the finest table in the world."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
