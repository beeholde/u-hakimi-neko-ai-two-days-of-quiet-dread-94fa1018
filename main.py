"""Two Days of Quiet Dread: one code review comment, at most 140 characters.

The entry program writes the line to /output/entry.txt: UTF-8, no trailing
newline, mode 0644. Standard library only.

The line (94 chars) approves a pull request with quiet existential dread:
a tired reviewer approving the way they approve everything now, quickly,
before the feeling catches up. The laugh comes from the dread itself, in a
flat tone, in words a tired engineer would really paste before clicking
approve.
"""

import os
from pathlib import Path

LINE = "LGTM. I approve this the way I approve everything now: quickly, before the feeling catches up."
# LINE is 94 chars, well under the 140-char gate; verified byte-identical
# across repeated runs (see NOTES.md for the sha256).

MAX_CHARS = 140


def main() -> None:
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be whitespace-only")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
