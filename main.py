#!/usr/bin/env python3
"""Invent a Word We Need — entry program (v1).

Coins one new English word and defines it in a single clear line.
The program writes that one line to /output/entry.txt.

The text is a fixed, deterministic constant: every run writes
exactly the same bytes, so the two grader runs are byte-identical.
"""

import os

# v2 entry (iteration round 1): "panic" names the feeling the reader has
# actually felt, and "hunting" is more vivid than "search" — the word
# stays the same, the definition lands harder in one reading.
# Rejected in this round: "handnesia" (less elegant than palmnesia,
# "palm" is where the phone rests); adding "(n.)" (nothing gained);
# narrowing to "while talking on it" (the broad in-hand case covers it).
ENTRY = "palmnesia \u2014 the panic of hunting for the phone already in your hand."


def main() -> None:
    text = ENTRY
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space.
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")
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
