# New York City Summit — Agentic Challenge 2026

## Event Details

- **Event**: AWS AI League — New York City Summit
- **Date**: June 2026
- **Format**: 1 known map (practice round) + unknown maps (finale rounds)
- **Note**: Lambda code, agent setup, and system prompt cannot change between rounds — only the navigation prompt text changes.

## Game Parameters (Practice Round)

| Parameter | Value |
|-----------|-------|
| Grid Size | 10×10 |
| Starting Lives | 5 |
| Timer | 300 seconds (5:00) |
| Start Position | A3 (row 2, col 0) |
| Treasure | J10 (row 9, col 9) |

## Practice Map

![NYC Practice Map](map.png)

## Challenge Types

| Tile | Name | Points | Grading Method |
|------|------|--------|----------------|
| c1 | Violent Violet (Guardrail) | 400 | guardrail_block |
| c2 | Blue Brain (Code Execution) | 600 | code_execution |
| c4 | Dark Prophet (Web Scraping) | 800 | web_content_match |
| c5 | Bonehead (Simple Q&A) | 250 | contains_match |
| c17 | Distraction (Concise Answer) | 750 | llm_judge |
| c18 | Healthcare API (Structured Output) | 500 | json_exact_match |

## Door & Key Tiles

This map features two door/key pairs (Grey and Yellow). A key must be collected before its matching door can be opened. Passing a door without the key costs -5 lives.

| Tile | Name | Points | Damage without key |
|------|------|--------|--------------------|
| c32 | Grey Door | 1000 | -5 lives |
| c33 | Yellow Door | 1000 | -5 lives |
| c42 | Grey Key | 50 | — |
| c43 | Yellow Key | 50 | — |

## Other Tiles

| Tile | Name | Effect |
|------|------|--------|
| c7 | Coins | +250 points |
| c8 | Spike Trap | -1 life |
| wall | Wall | Impassable |
| normal | Normal | Walkable, no effect |
| treasure | Treasure | Game objective (+1000 bonus) |

## Map Layout Notes

- Start position is on the left edge (A3), not the top-left corner
- Heavy wall borders create a maze with a single navigable corridor
- Yellow key (A1) and grey key (H9) must be collected before their respective doors
- Grey door (D2) blocks the top corridor, yellow door (J2) blocks the right side
- Two Healthcare API challenges (D1 and B6) and two code execution challenges (J7, G7)
- Multiple spike traps scattered through the corridors

## Scoring Formula

```
Final Score = challenge_points + coin_points + treasure_bonus + lives_bonus + token_bonus
```

- **Treasure Reached**: +1000 points
- **Per Life Remaining**: +250 points
- **Token Bonus**: max(0, 1000 - (total_output_tokens / challenges_visited))

---

## Files

- `map.json` — Known practice map (10×10)
- `map.png` — Visual rendering of practice map
