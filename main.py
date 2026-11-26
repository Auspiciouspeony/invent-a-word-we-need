#!/usr/bin/env python3
"""Invent a Word We Need — round 3 entry (program/v1).

Coins one new English word and defines it in a single clear line.
The program writes that one line to /output/entry.txt.

The text is a fixed, deterministic constant: every run writes
exactly the same bytes, so the grader's runs are byte-identical.
"""

import os

# Round 3 entry: a social, physical moment everyone recognises at once —
# two strangers mirroring each other's sidestep in a hallway. "Dance"
# says what the awkward shuffle looks like; "dodge" says what it is for.
# Not another -mnesia/-ghost lapse word: the round-2 board is saturated
# with them, and the past winners name a vivid social moment instead.
ENTRY = "dodgedance — the mirrored sidestep two strangers do in a hallway, each dodging the same way twice."


def validate(text: str) -> str:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space. One place owns the rule, so the entry and
    # the gate cannot drift apart in a later round.
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(ENTRY)
    # /output is a grader-provided mount owned by another user: never
    # chmod the mount itself (EPERM as uid 65534 -> exit 1, which is
    # exactly how round 1 failed). Create it only if missing, and
    # tolerate any permission error on the directory.
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Outputs must be readable by every user (the grader collects them
    # as another user): files 0644, folders 0755. Chmod only the file
    # we created, never the /output mount itself.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
