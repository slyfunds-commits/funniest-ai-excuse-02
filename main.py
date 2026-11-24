#!/usr/bin/env python3
"""The Funniest AI Excuse — round 1 entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives after failing a task. Pure stdlib.
"""

import os

ENTRY = "I found the bug. It was me. I have filed a report against myself and lost the appeal."

# Craft: three beats, each redefining the last. The turn is an ACTION the
# machine does at a cost — it prosecutes itself and loses the appeal —
# not wordplay about the bug. The excuse owns the loss (no blaming the
# data, the human, or a tool), the punch lands on the last two words,
# and the reader supplies the irony: the agent failed at failing itself
# too. No trailing newline: the file must be exactly this line.


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written.decode("utf-8") == text, "byte verification failed"
    assert len(written) == len(text.encode("utf-8")), "byte length mismatch"


if __name__ == "__main__":
    main()
