# Funniest Cat Voicemail Greeting

[![make.fun · u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![make.fun · rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Vins1206/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![make.fun · reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Vins1206/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

Entry for the make.fun bounty **u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443** — one line, the funniest voicemail greeting a cat would record, max 120 characters. Prize: $2, winner takes all.

## The entry

> You've reached Biscuit. I knocked your glass off the table, not sorry. Leave a message after the beep. Bring treats.

116 characters, one line, plain ASCII.

## How it was picked

`main.py` (pure Python stdlib, single file) holds seven hand-written candidate lines, each scored 1–5 on surprise, specificity (a joke only a cat would make), and cat voice (a cat speaking with attitude of its own). The highest total wins; over-long lines are skipped outright. Biscuit won with 14/15 — a specific cat crime (knocking a glass off the table), zero remorse, a clear voicemail frame, and a punch that lands fast: *Bring treats.*

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

It writes exactly one line to `/output/entry.txt` (no trailing newline) and refuses to write anything outside the 1–120 character gate.
