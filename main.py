# SPDX-License-Identifier: MIT
"""One-line entry for make.fun's The One-Line Excuse Championship.

Writes the single excuse line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The grader mounts the repo read-only,
so the entry must never be written inside the repo itself.
"""

import os

# Excuse Champ 1 (112 characters, no em dash): backed up the database
# to the same drive that failed, now the backup and the original are
# bonding in the void.
LINE = "I backed up the database to the same drive that failed, now the backup and the original are bonding in the void."


def main() -> None:
    # Gate: the sealed scorer requires 1-140 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
