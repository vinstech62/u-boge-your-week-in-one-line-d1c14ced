#!/usr/bin/env python3
"""Your Week in One Line -- entry program.

Writes exactly one line summing up the week to /output/entry.txt
(or $ENTRY_OUTPUT when set, for local testing).

Deterministic, standard library only, no network, no randomness.
"""

import os

LINE = "My week: wrote 200 lines, deleted 190 of them, and the one line that survived is this one."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
