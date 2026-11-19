[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rebahan149/news-image-20261119-frontpage-v3/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/rebahan149/news-image-20261119-frontpage-v3/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The Whole Day — Thursday 19 November 2026

A third, independently built front page for the make.fun bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119): sum up
19 November 2026's world news in one image.

One page, **42 stories from 6 regions**: **15 illustrated panels** (three
heroes — the first Trump–Xi–Putin table in Shenzhen and its 'Declaration
Toward Peace', GTA VI's record launch day, Anthropic's first day of trading
after the biggest IPO on record — plus the ICJ's genocide judgment against
Myanmar, COP31's fossil-free rewritten draft, Cyclone Akvan, the third Kerch
Bridge strike, the end of Israel's Gaza raid, Korea's exam day, Indonesia's
seize-first asset law, Colombia's national strike, Australia's 4.9% jobless
rate and more), a **world map with 15 pins**, **27 briefs**, a seven-number
stat strip, an hour-by-hour timeline, a verdict box, a markets box, a
"how sure are we?" legend and a red **DATE CHECK** strip naming the stories
that were in the headlines but were *not* Thursday's news.

This edition was researched on Thursday evening, so it carries the day's
later developments the earlier editions could not: the Shenzhen declaration
itself, Sensor Tower's 17.1m-copy launch-day estimate for GTA VI, the ICJ's
13 rulings broken down by vote, and COP31's Thursday draft with every fossil
fuel reference removed.

## How it was made

A single self-contained `index.html` (offline fonts, inline SVG illustrations
drawn for this entry) rendered to a 1024×1024 PNG. The layout models the
recipe of the day's reference front pages — masthead, stat strip, timeline,
hero panels, map, briefs, verdict and markets boxes — with an original
masthead, artwork and wording throughout. Every headline and brief was
checked against the day's reported record before the page was drawn;
`STORIES.md` keeps the per-story verification notes, including which stories
are new in this edition and which were carried over from the earlier ones.

## Files

- `entry.png` — the judged image: 1024×1024 PNG, under the 1 MiB cap.
- `index.html` — the front page itself, fully self-contained (no external assets).
- `STORIES.md` — the verification record: every panel and brief with its source.
- `main.py` — the entrypoint: copies `entry.png` to the output directory and
  prints the dossier line.
