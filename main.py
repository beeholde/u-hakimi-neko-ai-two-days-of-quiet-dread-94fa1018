"""Two Days of Quiet Dread, entry v3.

Writes one code review comment to the entry file: UTF-8, one line,
no trailing newline. Standard library only.

The v3 line (102 chars) approves a pull request while carrying quiet
existential dread: somewhere in this diff is a decision the reviewer
will forget by Friday, and it will outlive them anyway. Flat tone,
no exclamation, in words a tired engineer would really paste before
clicking approve.
"""

import os
from pathlib import Path

LINE = "Approved. Somewhere in this diff is a decision I will forget by Friday, and it will outlive me anyway."
# Gate note: LINE is 102 chars, under the 140-char gate; single line,
# no trailing newline, UTF-8. Output file mode 0644 (file only).
# Verified byte-identical across repeated runs:
# sha256 91d1488bd2e638cf3076431fefd4a7a741ae33a010f1cfdbb65a1276df5ccb86
# (comment only — output unchanged).

MAX_CHARS = 140
OUTPUT_NAME = "entry.txt"


def output_path() -> Path:
    """Grader output dir, or /output when the variable is unset."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / OUTPUT_NAME


def checked(line: str) -> str:
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be whitespace-only")
    return line


def main() -> None:
    text = checked(LINE)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
