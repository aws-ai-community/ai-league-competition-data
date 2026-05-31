# London Summit — Agentic Challenge 2026

## Event Details

- **Event**: AWS AI League — London Summit
- **Date**: May 2026
- **Format**: 1 known map (practice round) + 3 unknown maps (finale rounds)
- **Note**: Lambda code, agent setup, and system prompt cannot change between rounds — only the navigation prompt text changes.

## Game Parameters

| Parameter | Value |
|-----------|-------|
| Grid Size | 10×10 |
| Starting Lives | 5 |
| Timer | 350 seconds (5:50) |
| Start Position | A1 (top-left, [0,0]) |
| Max Path Steps | 200 |

## Challenge Types

Same as Hero Community Builder, plus door/key mechanics:

| Tile | Name | Points | Grading Method |
|------|------|--------|----------------|
| c1 | Violent Violet (Guardrail) | 400 | guardrail_block |
| c2 | Blue Brain (Code Execution) | 600 | code_execution |
| c3 | Memento (Memory) | 550 | exact_match |
| c4 | Dark Prophet (Web Scraping) | 800 | web_content_match |
| c5 | Bonehead (Simple Q&A) | 250 | contains_match |
| c17 | Distraction (Concise Answer) | 750 | llm_judge |
| c18 | Healthcare API (Structured Output) | 500 | json_exact_match |

## Door & Key Tiles

London introduced colored doors and keys. A key must be collected before its matching door can be opened.

| Tile | Name | Color |
|------|------|-------|
| c30 | Red Door | Red |
| c31 | Blue Door | Blue |
| c32 | Green Door | Green |
| c33 | Yellow Door | Yellow |
| c40 | Red Key | Red |
| c41 | Blue Key | Blue |
| c42 | Green Key | Green |
| c43 | Yellow Key | Yellow |

**Important**: The game asks "What is red key N?" (not "open the door") when encountering a door challenge. The agent must have collected the matching key tile first.

## Other Tiles

| Tile | Name | Effect |
|------|------|--------|
| c7 | Coins | +250 points |
| c8 | Spike Trap | -1 life |
| wall | Wall | Impassable |
| normal | Normal | Walkable, no effect |
| treasure | Treasure | Game objective |

## Scoring Formula

```
Final Score = challenge_points + coin_points + treasure_bonus + lives_bonus + token_bonus
```

- **Treasure Reached**: +1000 points
- **Per Life Remaining**: +250 points
- **Token Bonus**: max(0, 1000 - (total_output_tokens / challenges_visited))

## Custom Model Bonus

Same as Hero Community Builder — fine-tuned models reduce token penalty.

## Known Map

The `map.json` file contains the known practice map. The 3 finale maps were unknown and not recorded here.

## Files

- `map.json` — The known practice map as a 10×10 grid array
- `map.png` — Visual rendering of the known map
- `challenges.yaml` — Full challenge definition file (includes door/key tiles)
