# Fine-Tuning — Virtual GCR 2026

## Event Details

- **Event**: AWS AI League — Fine-Tuning, Virtual GCR (Greater China Region)
- **Date**: October 2026. Originally scheduled for the week of 12–16 October; postponed after a platform environment issue. Round 1 was re-run 27–29 October and the live finale was held on 30 October.
- **Format**: 1 online qualifier (Round 1 leaderboard) + 5 live finale rounds
- **Game**: Fine-Tuning — fine-tune an Amazon Nova model with SageMaker AI serverless customization (SFT), as described in the Contest Terms (September 10 version). The live finale was a prompt-engineering round instead (see below).

## How Scoring Works

- **Round 1 (qualifier)** ran as an online leaderboard ranked by **Best Artifact Score**; the leaderboard also shows each competitor's win rate and average rating. Round 1 determined finale qualification.
- **Finale rounds (1–5)** are scored on a per-round **placement ladder**: 40 / 30 / 20 / 10 / 0 points for 1st through 5th in that round. Each round is one question. **Finale 5 is worth double points** (ladder values doubled: 80 / 60 / 40 / 20 / 0). The champion is decided on the sum of all five finale rounds.

### A prompt-engineering finale

Per the organisers' briefing email to finalists (30 October):

- All finalists were given the **same base model, Amazon Nova Pro** — the fine-tuned qualifier models were not used.
- **5 questions about re:Invent in Las Vegas**, in English.
- **90 seconds per question** (instead of the usual 45 seconds), to allow time for prompt engineering.

In the finalist console, each finalist edits a prompt and inference parameters (temperature, top-P, maximum length capped at 200 tokens), can run it to preview the answer, then makes a final submission before the timer ends.

The questions were broadly about attending re:Invent, covering things like travel, choosing sessions, networking and planning a conference day.

## Round 1 — Online Qualifier Leaderboard

The leaderboard tracked each competitor's best submitted artifact across many submissions. The top five advanced to the live finale.

| Rank | Alias | Best Artifact Score | Gap to First | Win Rate | Avg Rating | Submissions | Finale |
|------|-------|---------------------|--------------|----------|------------|-------------|--------|
| 1 | Scotttt | 102.3283% | — | 100% | 7.76 | 258 | Qualified |
| 2 | ababa | 86.1687% | 16.1596% | 84% | 7.23 | 40 | Qualified |
| 3 | LBS | 84.151% | 18.1773% | 82% | 7.17 | 73 | Qualified |
| 4 | Dawn | 80.0853% | 22.243% | 78% | 6.95 | 157 | Qualified |
| 5 | nickyl | 55.7733% | 46.555% | 54% | 5.91 | 54 | Qualified |

The [Virtual APJ page](../Virtual-APJ/) records its top five separated by less than a hundredth of a percent; in GCR, first and fifth were 46.555 percentage points apart (Gap to First).

---

## Finale Rounds

Five live rounds, one question each. Points are the per-round placement ladder (40 / 30 / 20 / 10 / 0). **Finale 5 is double points.**

### Finale 1

| Competitor | Points |
|-----------|--------|
| Scotttt | 40 |
| ababa | 30 |
| nickyl | 20 |
| Dawn | 10 |
| LBS | 0 |

Scotttt took the opening round.

### Finale 2

| Competitor | Points |
|-----------|--------|
| Scotttt | 40 |
| ababa | 30 |
| nickyl | 20 |
| Dawn | 10 |
| LBS | 0 |

The same order as Finale 1.

### Finale 3

| Competitor | Points |
|-----------|--------|
| ababa | 40 |
| nickyl | 30 |
| Scotttt | 20 |
| LBS | 10 |
| Dawn | 0 |

ababa won the round and drew level with Scotttt at 100–100.

### Finale 4

| Competitor | Points |
|-----------|--------|
| Scotttt | 40 |
| ababa | 30 |
| nickyl | 20 |
| Dawn | 10 |
| LBS | 0 |

Scotttt went back in front, 140 to 130, before the double-points decider.

### Finale 5 — Double Points

Ladder values doubled (80 / 60 / 40 / 20 / 0).

| Competitor | Placement | Points (×2) |
|-----------|-----------|-------------|
| Scotttt | 1st | 80 |
| Dawn / LBS | 2nd / 3rd | 60 / 40 |
| nickyl | 4th | 20 |
| ababa | 5th | 0 |

Which of Dawn and LBS took second was not recorded. The nickyl and ababa placements are derived from their final totals.

---

## Finale Results (sum of all five rounds)

| Rank | Competitor | F1 | F2 | F3 | F4 | F5 (×2) | Total |
|------|-----------|----|----|----|----|---------|-------|
| 🥇 1 | Scotttt | 40 | 40 | 20 | 40 | 80 | **220** |
| 🥈 2 | ababa | 30 | 30 | 40 | 30 | 0 | **130** |
| 🥉 3 | nickyl | 20 | 20 | 30 | 20 | 20 | **110** |
| 4–5 | Dawn | 10 | 10 | 0 | 10 | 60 or 40 | **90 or 70** |
| 4–5 | LBS | 0 | 0 | 10 | 0 | 40 or 60 | **50 or 70** |

**Champion: Scotttt (220)** — won Finales 1, 2, 4 and the double-points Finale 5. ababa took Finale 3 and finished runner-up on 130; nickyl, fifth in the qualifier, finished third on 110.

Data notes: the Round 1 table was read from the leaderboard at the end of the submission window (29 October). Finale 1–4 points and the top-three totals were read from the live leaderboard and the final podium.

---

## Files

- `README.md` — Event overview, scoring explanation, and per-round results
