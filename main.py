#!/usr/bin/env python3
"""The One-Line Laugh: emit the chosen one-liner to /output/entry.txt.

One sentence, well under the 200-character gate, built to land its surprise
at the end: the "unusual activity" a bank flags turns out to be the most
ordinary, healthy thing imaginable. Stdlib only, deterministic, no network.
The output directory is created if needed but never removed; only entry.txt
is written inside it.
"""

from pathlib import Path

LINE = "My bank just flagged 'unusual activity' on my card \u2014 it was me buying vegetables."

OUT_PATH = Path("/output") / "entry.txt"


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
