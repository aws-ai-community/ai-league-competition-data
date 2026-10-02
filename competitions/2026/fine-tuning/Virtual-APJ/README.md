# Fine-Tuning — Virtual APJ 2026

## Event Details

- **Event**: AWS AI League — Fine-Tuning, Virtual APJ (Asia Pacific & Japan)
- **Date**: September 2026
- **Format**: 1 online qualifier (Round 1 leaderboard) + 5 live finale rounds
- **Game**: Fine-Tuning — customise a small base model (via Bedrock RFT / RLVR with a training dataset, evaluation dataset, and reward function) so it beats a larger baseline model in head-to-head, LLM-as-a-judge evaluation. Unlike the Agentic Maze (scored map runs) and Agentic Football (head-to-head knockouts), this is a dataset-and-reward engineering challenge.

## How Scoring Works

Competitors submit a fine-tuned model. Each submission is evaluated against a held-out evaluation set and judged head-to-head against the larger baseline model by an LLM judge.

- **Round 1 (qualifier)** is scored as a **win-rate percentage** — the share of head-to-head judgements the fine-tuned model wins against the baseline, expressed as a percentage. A score above 100% means the fine-tuned small model is beating the larger baseline on balance. Round 1 ran as an online leaderboard and determined finale qualification; the margins are razor-thin (hundredths of a percent).
- **Finale rounds (1–5)** are scored on a per-round **placement ladder**: 40 / 30 / 20 / 10 / 0 points for 1st through 5th in that round. Each round presents a new, unseen evaluation theme. **Finale 5 is worth double points** (ladder values doubled: 80 / 60 / 40 / 20 / 0). The champion is decided on the sum of all five finale rounds.

## Round 1 — Online Qualifier Leaderboard

The top five on the online leaderboard advanced to the live finale. Scores are the head-to-head win-rate percentage against the baseline model.

| Rank | Competitor | Win Rate | Finale |
|------|-----------|----------|--------|
| 1 | an-ander | 102.4351% | Qualified |
| 2 | jwlee | 102.4255% | Qualified |
| 3 | Mimimaomao | 102.4123% | Qualified |
| 4 | Eunji Lee | 102.4117% | Qualified |
| 5 | chanche3 | 102.4108% | Qualified |

All five finalists cleared 102.41%, separated by less than a hundredth of a percent from top to bottom — an-ander led the qualifier, while chanche3 scraped into the finale in fifth.

---

## Finale Rounds

Five live rounds, each a fresh unseen evaluation theme. Points are the per-round placement ladder (40 / 30 / 20 / 10 / 0). **Finale 5 is double points.**

### Finale 1

| Competitor | Points |
|-----------|--------|
| an-ander | 40 |
| chanche3 | 20 |
| Mimimaomao | 30 |
| Eunji Lee | 10 |
| jwlee | 0 |

an-ander carried qualifier form straight into a round win.

### Finale 2

| Competitor | Points |
|-----------|--------|
| Mimimaomao | 40 |
| chanche3 | 30 |
| an-ander | 20 |
| Eunji Lee | 10 |
| jwlee | 0 |

Mimimaomao topped the round; chanche3 began the climb that would define the finale.

### Finale 3

| Competitor | Points |
|-----------|--------|
| chanche3 | 40 |
| jwlee | 30 |
| an-ander | 20 |
| Eunji Lee | 10 |
| Mimimaomao | 0 |

chanche3 took first and Mimimaomao's early lead evaporated with a last-place finish.

### Finale 4

| Competitor | Points |
|-----------|--------|
| chanche3 | 40 |
| jwlee | 30 |
| an-ander | 20 |
| Eunji Lee | 10 |
| Mimimaomao | 0 |

A repeat of Finale 3's order — chanche3 won again, building a lead going into the double-points decider.

### Finale 5 — Double Points

Ladder values doubled (80 / 60 / 40 / 20 / 0).

| Competitor | Placement | Points (×2) |
|-----------|-----------|-------------|
| chanche3 | 1st | 80 |
| an-ander | 2nd | 60 |
| jwlee | 3rd | 40 |
| Eunji Lee | 4th | 20 |
| Mimimaomao | 5th | 0 |

chanche3 closed out the title with a round win on double points, while an-ander's second place secured the runner-up spot.

---

## Finale Results (sum of all five rounds)

| Rank | Competitor | F1 | F2 | F3 | F4 | F5 (×2) | Total |
|------|-----------|----|----|----|----|---------|-------|
| 🥇 1 | chanche3 | 20 | 30 | 40 | 40 | 80 | **210** |
| 🥈 2 | an-ander | 40 | 20 | 20 | 20 | 60 | **160** |
| 🥉 3 | jwlee | 0 | 0 | 30 | 30 | 40 | **100** |
| 4 | Mimimaomao | 30 | 40 | 0 | 0 | 0 | **70** |
| 5 | Eunji Lee | 10 | 10 | 10 | 10 | 20 | **60** |

**Champion: chanche3 (210)** — the lowest qualifier seed turned the finale around, winning Finales 3, 4, and the double-points Finale 5 to run away with the title. an-ander, who led the online qualifier and won Finale 1, finished runner-up on 160. jwlee took third on the strength of a strong back half (two seconds and a double-points third).

---

## Files

- `README.md` — Event overview, scoring explanation, and per-round results
