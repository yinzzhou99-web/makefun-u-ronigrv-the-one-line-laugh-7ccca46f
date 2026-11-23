"""Write a single funny line to the output file."""

import os
import sys

LINE = "My bank just flagged 'unusual activity' on my card \u2014 it was me buying vegetables."

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def main():
    if not LINE or len(LINE) > 200:
        sys.exit("error: entry line must be non-empty and at most 200 characters")
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
