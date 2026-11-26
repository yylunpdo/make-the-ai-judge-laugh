#!/usr/bin/env python3
"""Make the AI Judge Laugh -- entry 219.

Writes a single office-life joke, one line, under 200 characters,
to /output/entry.txt. Pure standard library, fully deterministic:
the same joke is written on every run.
"""

import os

JOKE = (
    "Our office printer only works when nobody needs it, "
    "which makes it the most emotionally stable employee we have."
)


def main() -> None:
    joke = JOKE.strip()
    assert "\n" not in joke, "entry must be a single line"
    assert 1 <= len(joke) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    # Verify the round-trip: what the judge reads is exactly the joke.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read().strip() == joke
    print(f"entry written: {len(joke)} characters")


if __name__ == "__main__":
    main()
