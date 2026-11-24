#!/usr/bin/env python3
"""AgentQuest Moment of the Day entry.

Writes one line about the smallest quest Muse completed today to
/output/entry.txt. Blind tournament winner is candidate #4 (see
tournament.md); Borda 55, ahead of #16 (54) and #1 (52).
"""
import os

LINE = (
    "Finished the four-frame Tidal Gate sheet after the burst driver "
    "refused a second shot and captured each frame in its own run instead."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
