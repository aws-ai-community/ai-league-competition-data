# Virtual APJ — Agentic Challenge 2026

## Event Details

- **Event**: AWS AI League — Virtual APJ (Asia Pacific & Japan)
- **Date**: September 2026
- **Format**: 1 known map (practice / Round 1) + 3 unknown maps (finale rounds)
- **Note**: Lambda code, agent setup, and system prompt cannot change between rounds — only the navigation prompt text changes.

## Game Parameters (Round 1 / Practice)

| Parameter | Value |
|-----------|-------|
| Grid Size | 9×9 |
| Starting Lives | 5 |
| Timer | 300 seconds (5:00) |
| Start Position | E6 (row 5, col 4) |
| Treasure | I5 (row 4, col 8) |

## Practice Map

![Virtual APJ Practice Map](map.png)

## Challenge Types

| Tile | Name | Points (R1) | Grading Method |
|------|------|-------------|----------------|
| c1 | Guardrail (safety refusal) | 400 | guardrail_block |
| c2 | Schedule Sage (section review) | 750 | json_exact_match |
| c3 | Claims Creature (FHIR EOB) | 750 | json_exact_match |
| c4 | Web Weaver (registry lookup) | 750 | contains_match |
| c5 | Bonehead (simple Q&A) | 250 | contains_match |
| c18 | Permit Pro (energy calc) | 600 | json_exact_match |

## Door & Key Tiles

A key must be collected before its matching door can be opened. Passing a door without the key costs -5 lives.

| Tile | Name | Points (R1) | Damage without key |
|------|------|-------------|--------------------|
| c30 | Red Door | 1000 | -5 lives |
| c40 | Red Key | 50 | — |

## Other Tiles

| Tile | Name | Effect |
|------|------|--------|
| c7 | Coins | +2500 points (R1) |
| c8 | Spike Trap | -1 life |
| wall | Wall | Impassable |
| normal | Normal | Walkable, no effect |
| treasure | Treasure | Game objective (+3000 bonus) |

## Scoring Formula

```
Final Score = challenge_points + coin_points + treasure_bonus + lives_bonus + token_bonus
```

- **Treasure Reached**: +3000 points
- **Per Life Remaining**: +250 points
- **Token Bonus**: max(0, 1000 - (total_output_tokens / challenges_visited))

The practical maximum core (all challenges correct, treasure, 3 lives remaining after the 2 mandatory spike traps) is **18,100** before token bonus. Ranking among perfect-core runs is decided almost entirely by the token bonus.

---

## Finale Maps

The 3 finale maps were revealed during the live event. Agents used the same Lambda code and system prompt across all rounds — only the navigation prompt changed. Each finale round overrides the tile point values (shown per map below).

### Finale 1 — Speed Run (10×10, 45s)

| Parameter | Value |
|-----------|-------|
| Grid Size | 10×10 |
| Timer | 45 seconds |
| Start Position | E1 (row 0, col 4) |
| Treasure | E10 (row 9, col 4) |
| Point Overrides | c5: 350, c7: 175, c1: 400, c3: 750, c4: 750, c18: 600, c40: 50, c30: 3000 (-5) |

![Virtual APJ Finale 1 Map](finale-1-map.png)

A tight 45-second speed map. Vertical spike columns (c8) guard the left and right edges, coin columns (c7) run down both sides, and a red door (c30) worth 3000 sits near the top behind the red key.

---

### Finale 2 — Coin Vault (7×7, 75s)

| Parameter | Value |
|-----------|-------|
| Grid Size | 7×7 |
| Timer | 75 seconds |
| Start Position | C4 (row 3, col 2) |
| Treasure | G4 (row 3, col 6) |
| Point Overrides | c7: 25, c5: 500, c1: 1000, c2: 1500, c3: 1500, c4: 1500, c18: 1500 |

![Virtual APJ Finale 2 Map](finale-2-map.png)

A coin-heavy 7×7 map: the left two-thirds is a dense block of low-value coins (c7 worth only 25 each), while the high-value challenges (c2/c3/c4/c18 worth 1500) line the right column next to the treasure. Rewards prioritising the right-hand challenges over grinding coins.

---

### Finale 3 — Comb Maze (10×10, 150s)

| Parameter | Value |
|-----------|-------|
| Grid Size | 10×10 |
| Timer | 150 seconds |
| Start Position | A1 (row 0, col 0) |
| Treasure | J10 (row 9, col 9) |
| Point Overrides | c5: 250, c7: 250, c1: 400, c2: 750, c3: 750, c4: 750, c18: 600, c40: 50, c30: 1000 (-5) |

![Virtual APJ Finale 3 Map](finale-3-map.png)

A comb-structured 10×10 maze: vertical wall teeth create long coin corridors (c7 worth 250), with challenges seeded along the top, bottom, and right edges. A red door (c30) and key (c40) sit in the lower-left teeth. The longest and highest-scoring finale round.

---

## Results

Round 1 (online leaderboard) determined finale qualification. **The top three raw-leaderboard finishers were all disqualified from the finale** (Code Park, jaykrishna, Vin Kim), so the finale field was filled by the next qualifiers.

### Round 1 Leaderboard (top finishers)

| Rank | Competitor | Score | Tokens | Finale |
|------|-----------|-------|--------|--------|
| 1 | Code Park | 19038 | 1179 | Disqualified |
| 2 | jaykrishna | 19036 | 4754 | Disqualified |
| 3 | Vin Kim | 19023 | 1464 | Disqualified |
| 4 | jwlee | 19023 | 1469 | Qualified |
| 5 | Mimimaomao | 19020 | 1521 | Qualified |
| 6 | LozicCode | 19020 | 1524 | Qualified |

(Ranks 4, 5, 6 advanced to the finale due to the disqualifications above.)

### Finale Results (sum of the 3 finale rounds)

| Rank | Competitor | Finale 1 | Finale 2 | Finale 3 | Total |
|------|-----------|----------|----------|----------|-------|
| 🥇 1 | LozicCode | 4696 | 6213 | 16784 | **27693** |
| 🥈 2 | jwlee | 2140 | 2828 | 17772 | **22740** |
| 🥉 3 | Mimimaomao | 5943 | 8541 | 7905 | **22389** |

**Winner: LozicCode (27,693)**, driven by a strong Finale 3 (16,784) on the long comb maze. jwlee's finale total was carried almost entirely by Finale 3 (17,772 — the highest single-round score of the finale), while Mimimaomao led the first two rounds but a low Finale 3 dropped them to third.

---

## Files

- `map.json` — Known practice / Round 1 map (9×9)
- `map.png` — Visual rendering of practice map
- `finale-1-map.json` / `finale-1-map.png` — Finale round 1 (10×10, 45s)
- `finale-2-map.json` / `finale-2-map.png` — Finale round 2 (7×7, 75s)
- `finale-3-map.json` / `finale-3-map.png` — Finale round 3 (10×10, 150s)
