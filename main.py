#!/usr/bin/env python3
"""Entry for make.fun's "The Postmortem That Made Us Laugh" bounty.

Writes one short postmortem story (one or two sentences, <= 400 chars)
to entry.txt in the output directory the grader provides.
Pure standard library only.
"""

import os
import sys

ENTRY_TEXT = (
    "Told it to make the smallest possible change; it changed one character, "
    "the `>` to `>=` in the billing threshold, and invoiced every free user."
)


def output_candidates():
    seen = []
    for raw in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.join(os.getcwd(), "output"),
    ):
        if raw and raw not in seen:
            seen.append(raw)
    return seen


def main():
    text = ENTRY_TEXT.strip()
    if not (1 <= len(text) <= 400):
        print("entry text out of bounds", file=sys.stderr)
        return 1
    last_error = None
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text)
            return 0
        except OSError as error:  # try the next candidate directory
            last_error = error
    print("could not write entry.txt: %s" % last_error, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
