"""Famous Last Words at 1 Percent entry.

Writes a single line of text -- the last words a phone says as its
battery hits 1 percent -- to /output/entry.txt. The competition gate
requires UTF-8 text of 1 to 199 characters, not only white space.
The program is deterministic: every run writes exactly the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199

LINE = "At 1%, my dying confession: I autocorrected 'ducking' on purpose, I snoozed your alarm to watch you panic, and that photo you swore you never sent? I backed it up. Twice."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
