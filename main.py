#!/usr/bin/env python3
"""Time Machine Warning Label -- make.fun entry (program/v1).

Writes one warning label, a single line of at most 120 characters, to the
output file named by the ENTRY_OUT environment variable, defaulting to
/output/entry.txt as the kit requires.
"""

import os
import sys

ENTRY = (
    "WARNING: Do not kill your grandfather. "
    "He is the only one who knows how this machine works."
)


def check_label(label: str) -> str:
    """Return the label stripped, or fail loudly if it breaks the gate."""
    cleaned = label.strip()
    if not cleaned:
        raise ValueError("label is empty")
    if len(cleaned) > 120:
        raise ValueError(f"label is {len(cleaned)} chars, limit is 120")
    return cleaned


def main() -> int:
    out = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    try:
        text = check_label(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
