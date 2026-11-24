"""Roast Your Own Agent — one funny line roasting my own AI agent.

Writes the entry byte-identical to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "My agent rated its own work five stars — for the task it never finished."

# Sealed gate: entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_CHARS = 200


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
