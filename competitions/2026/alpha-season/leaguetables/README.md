# League tables

Snapshots of the public leaderboard for all six leagues (A–F) of the league phase,
one per week from week 4, plus the final table after the organisers removed some sides.
Each snapshot comes as Markdown (to read on GitHub) and JSON (to analyse), and both
hold the full table for every league.

| Snapshot | Date (UTC) | What it shows | Played |
|---|---|---|---|
| [`week-4`](week-4.md) ([json](week-4.json)) | 5 Oct | End of week 4 | up to 40 |
| [`week-5`](week-5.md) ([json](week-5.json)) | 13 Oct | End of week 5 | up to 50 |
| [`week-6`](week-6.md) ([json](week-6.json)) | 22 Oct | End of week 6 | up to 60 |
| [`week-7`](week-7.md) ([json](week-7.json)) | 26 Oct | End of week 7: the league closed at 15:59 UTC on 25 Oct | up to 70 |
| [`final`](final.md) ([json](final.json)) | 23 Nov | Final, after sides were removed | up to 70 |

There are no snapshots for weeks 1–3.

Each week snapshot was taken after that week's matches and before the next week
opened, so no side in it has played more than 10 × the week number.

## Columns

| Markdown | JSON | Meaning |
|---|---|---|
| # | `rank` | Position, as the leaderboard gives it |
| Team | `teamName` | Team name at the time of the snapshot (sides can rename) |
| P, W, D, L | `played`, `wins`, `draws`, `losses` | |
| GF, GA, GD | `goalsFor`, `goalsAgainst`, `goalDifference` | |
| Clean | `cleanSheets` | Matches without conceding |
| Sweeps | `sweeps` | Bonus count reported by the leaderboard |
| Pts | `points` | |

Every row in every file satisfies

    points = 30·W + 10·D + 2·L + GF + 5·clean sheets + 15·sweeps

Each league in the JSON also carries `sides` (the number of rows), `matches` (the
leaderboard's own match count) and `tableComputedAt` (when the leaderboard last
recomputed that table). The final snapshot adds `closedAt`.

## Week 7 and the final table

Both are included because the organisers removed sides from every league after the
league closed. Their matches were also taken out of everyone else's records, so some
sides that stayed have fewer matches played in the final table than at the close.

| League | Sides at close | Sides in final | Removed | Remaining sides whose W–D–L changed |
|---|--:|--:|--:|--:|
| A | 581 | 556 | 25 | 22 |
| B | 611 | 574 | 37 | 17 |
| C | 581 | 569 | 12 | 18 |
| D | 551 | 530 | 21 | 1 |
| E | 593 | 574 | 19 | 5 |
| F | 584 | 561 | 23 | 12 |

No new sides appear in the final table. The `matches` figure the leaderboard reports
went up after the close (League A: 3,644 → 4,454) even though sides were removed. It
is given here as reported, without explanation.
