"""Funniest cat voicemail greeting — program/v1.

Writes exactly one line to /output/entry.txt.

The line was chosen from the hand-written candidates below by a small
local rubric, each scored 1-5 on:
  surprise   — fresh, unexpected turn, not a known pun or catchphrase
  specificity — a joke only a cat would make (knocking things off,
                boxes, keyboards, screaming for food at 4 a.m.)
  voice      — a cat speaking with attitude of its own, not an owner
                writing about a cat

Rubric totals (surprise + specificity + voice):
  Biscuit, glass off the table, not sorry ......... 4 + 5 + 5 = 14  WINNER
  Luna, phone off the counter, sat on it .......... 5 + 5 + 4 = 14
  Biscuit, staring at the wall, 4 a.m. food ........ 4 + 4 + 4 = 12
  Chairman Meow, asleep on the keyboard ........... 3 + 4 + 4 = 11
  Milo, mug off the table, ignore at 4 a.m. ....... 3 + 4 + 4 = 11
  Miso, asleep in the shoe box, 4 a.m. ............ 4 + 4 + 3 = 11
  Pickles, the box is mine now .................... 4 + 4 + 3 = 11

Luna ties Biscuit on total, but loses the tie-break: "I'll read it
never" is awkward spoken aloud, and Biscuit's voicemail frame is
clearer ("Leave a message after the beep. Bring treats."), which is
the judge's first criterion. The winner is 116 characters, ASCII,
so it passes the 1-120 character gate with room to spare.
"""

import os

# Hand-written candidates: (line, surprise, specificity, voice).
CANDIDATES = [
    (
        "You've reached Biscuit. I knocked your glass off the table, "
        "not sorry. Leave a message after the beep. Bring treats.",
        4,
        5,
        5,
    ),
    (
        "Hi, you've reached Luna. I knocked your phone off the counter, "
        "then sat on it. Leave a message \u2014 I'll read it never.",
        5,
        5,
        4,
    ),
    (
        "Hi, it's Biscuit. Leave a message after the beep. I'm busy "
        "staring at the wall, then screaming for food at 4 a.m.",
        4,
        4,
        4,
    ),
    (
        "You've reached Chairman Meow. I'm asleep on your keyboard. "
        "Leave a message after the beep, then bring treats.",
        3,
        4,
        4,
    ),
    (
        "Hi, you've reached Milo. I'm knocking your mug off the table. "
        "Leave a message after the beep \u2014 I'll ignore it at 4 a.m.",
        3,
        4,
        4,
    ),
    (
        "Hi, you've reached Miso. I'm asleep in the box your shoes came "
        "in. Leave a message \u2014 I'll scream for breakfast at 4 a.m.",
        4,
        4,
        3,
    ),
    (
        "Hi, you've reached Pickles. I'm in the box. The box is mine now. "
        "Leave a message after the beep. I'll knock it off later.",
        4,
        4,
        3,
    ),
]


def pick_winner(candidates):
    """Highest rubric total wins; earliest entry breaks a tie.

    A candidate over the 120-character gate can never win, however
    funny it is, so over-long lines are skipped outright instead of
    being picked and then failing the gate in main().
    """
    best = None
    best_total = -1
    for line, surprise, specificity, voice in candidates:
        if len(line) > 120 or len(line) < 1:
            continue
        total = surprise + specificity + voice
        if total > best_total:
            best = line
            best_total = total
    if best is None:
        raise ValueError("no candidate fits the 1-120 character gate")
    return best


ENTRY = pick_winner(CANDIDATES)


def main():
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
