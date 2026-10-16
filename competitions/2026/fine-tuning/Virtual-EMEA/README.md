# Fine-Tuning — Virtual EMEA 2026

## Event Details

- **Event**: AWS AI League — Fine-Tuning, Virtual EMEA (Europe, Middle East & Africa)
- **Date**: October 2026
- **Format**: 1 online qualifier (Round 1 leaderboard) + 5 live finale rounds
- **Game**: Fine-Tuning — customise a small base model (via Bedrock RFT / RLVR with a training dataset, evaluation dataset, and reward function) so it beats a larger baseline model in head-to-head, LLM-as-a-judge evaluation. Unlike the Agentic Maze (scored map runs) and Agentic Football (head-to-head knockouts), this is a dataset-and-reward engineering challenge.

## How Scoring Works

Competitors submit a fine-tuned model. Each submission is evaluated against a held-out evaluation set and judged head-to-head against the larger baseline model by an LLM judge.

- **Round 1 (qualifier)** is scored as a **win-rate percentage** — the share of head-to-head judgements the fine-tuned model wins against the baseline. Round 1 ran as an online leaderboard and determined finale qualification.
- **Finale rounds (1–5)** are scored on a per-round **placement ladder**: 40 / 30 / 20 / 10 / 0 points for 1st through 5th in that round. Each round presents a new, unseen evaluation theme. **Finale 5 is worth double points** (ladder values doubled: 80 / 60 / 40 / 20 / 0). The champion is decided on the sum of all five finale rounds.

### A much harder challenge than APJ

AWS made the EMEA evaluation **significantly harder than the APJ event**. Where APJ finalists cleared win rates above 102%, EMEA's top qualifier topped out at **1.8438%** — and **no competitor managed a single correct answer in Round 1**. The leaderboard was decided on partial-credit margins (win rate, average rating) rather than outright correct answers.

## Round 1 — Online Qualifier Leaderboard

The leaderboard tracked each competitor's best submitted artifact across many submissions. The top finishers advanced to the live finale.

| Rank | Alias | Win Rate | Gap to First | Avg Rating | Best Artifact Score | Submissions | Finale |
|------|-------|----------|--------------|------------|---------------------|-------------|--------|
| 1 | pp | 0% | — | 6.15 | 1.8438% | 72 | Qualified |
| 2 | Yuki Tsunoda | 0% | 0.0357% | 6.03 | 1.8081% | 82 | Qualified |
| 3 | FL | 0% | 0.3432% | 5.00 | 1.5006% | 8 | Qualified |
| 4 | MarkRoss | 0% | 0.4065% | 4.79 | 1.4373% | 69 | Qualified — withdrew (see below) |
| 5 | alexli | 0% | 0.4308% | 4.71 | 1.4130% | 58 | Qualified |
| 6 | Jochem | 0% | 0.4845% | 4.53 | 1.3593% | 44 | Qualified |

**Win Rate** is the head-to-head correct-answer win rate against the baseline — **0% for every competitor**, reflecting how hard the evaluation was. Ranking was therefore decided on **Best Artifact Score** (and average rating), where pp's 1.8438% edged out Yuki Tsunoda by less than four hundredths of a percent. FL reached third on just 8 submissions.

### MarkRoss withdrew from the finale

MarkRoss qualified in fourth but **gave up his finale spot so another competitor could have a chance at the re:Invent prize** — he had already qualified via the Agentic Maze challenge earlier in the AI League. His withdrawal promoted the next qualifiers, and the live finale was contested by **pp, Yuki Tsunoda, FL, alexli, and Jochem**.

---

## Finale Rounds

Five live rounds, each a fresh unseen evaluation theme. Points are the per-round placement ladder (40 / 30 / 20 / 10 / 0). **Finale 5 is double points.**

### Finale 1

| Competitor | Points |
|-----------|--------|
| Jochem | 40 |
| alexli | 30 |
| pp | 20 |
| Yuki Tsunoda | 10 |
| FL | 0 |

Jochem took the opening round; alexli started strong in second.

### Finale 2

| Competitor | Points |
|-----------|--------|
| alexli | 40 |
| pp | 30 |
| FL | 20 |
| Jochem | 10 |
| Yuki Tsunoda | 0 |

alexli won the first of four straight round wins.

### Finale 3

| Competitor | Points |
|-----------|--------|
| alexli | 40 |
| Jochem | 30 |
| FL | 20 |
| pp | 10 |
| Yuki Tsunoda | 0 |

alexli again, pulling clear at the top of the standings.

### Finale 4

| Competitor | Points |
|-----------|--------|
| alexli | 40 |
| FL | 30 |
| Yuki Tsunoda | 20 |
| Jochem | 10 |
| pp | 0 |

A third consecutive win for alexli, all but sealing the title before the double-points decider.

### Finale 5 — Double Points

Ladder values doubled (80 / 60 / 40 / 20 / 0).

| Competitor | Placement | Points (×2) |
|-----------|-----------|-------------|
| alexli | 1st | 80 |
| Yuki Tsunoda | 2nd | 60 |
| FL | 3rd | 40 |
| pp | 4th | 20 |
| Jochem | 5th | 0 |

alexli capped an unbeaten finale run (Finales 2–5) with a double-points win. Yuki Tsunoda's second place in the decider lifted them past Jochem on the tiebreak.

---

## Finale Results (sum of all five rounds)

| Rank | Competitor | F1 | F2 | F3 | F4 | F5 (×2) | Total |
|------|-----------|----|----|----|----|---------|-------|
| 🥇 1 | alexli | 30 | 40 | 40 | 40 | 80 | **230** |
| 🥈 2 | FL | 0 | 20 | 20 | 30 | 40 | **110** |
| 🥉 3 | Yuki Tsunoda | 10 | 0 | 0 | 20 | 60 | **90** |
| 4 | Jochem | 40 | 10 | 30 | 10 | 0 | **90** |
| 5 | pp | 20 | 30 | 10 | 0 | 20 | **80** |

**Champion: alexli (230)** — after a second-place opener, alexli won Finales 2, 3, 4, and the double-points Finale 5 for a commanding, unbeaten-from-round-two title run. FL took runner-up on 110 with a strong back half. Yuki Tsunoda and Jochem tied on 90; the tie is broken in Yuki Tsunoda's favour on the double-points Finale 5 (60 vs 0), where the head-to-head decider counted for most.

---

## Files

- `README.md` — Event overview, scoring explanation, and per-round results
