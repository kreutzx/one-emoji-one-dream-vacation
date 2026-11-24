"""One Emoji, One Dream Vacation — entry for @kreutzx.

Writes exactly one emoji to /output/entry.txt: the Milky Way night sky,
standing in for the dream trip of chasing the northern lights under a
star-filled Arctic sky.
"""

import os

# The entry: one emoji, nothing else.
# U+1F30C MILKY WAY — the night sky over the Arctic on an aurora-chasing
# trip: one cold, clear night in Tromsø, green light rippling overhead,
# the one journey on the bucket list that no beach can replace.
ENTRY_TEXT = "🌌"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
