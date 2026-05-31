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

## Known Map (Practice Round)

The `map.json` file contains the known practice map.

| Parameter | Value |
|-----------|-------|
| Grid Size | 10×10 |
| Timer | 350 seconds |
| Start Position | A1 (row 0, col 0) |
| Treasure | J10 (row 9, col 9) |

## Finale Maps

The 3 finale maps were revealed during the live event. Agents used the same Lambda code and system prompt across all rounds — only the navigation prompt changed.

### Finale 1

| Parameter | Value |
|-----------|-------|
| Grid Size | 10×10 |
| Timer | 65 seconds |
| Start Position | A10 (row 9, col 0) |
| Treasure | J1 (row 0, col 9) |
| Treasure Bonus | 5000 |
| Challenge Overrides | c17: 50 points |

A speed-focused map with a tight 65-second timer. The agent starts bottom-left and must reach the treasure at top-right. Features a horizontal wall of spike traps (c8) across row 4, vertical coins (c7) along the right edge, and concise-answer distractors (c17) at the corners.

### Finale 2

| Parameter | Value |
|-----------|-------|
| Grid Size | 6×6 |
| Timer | 95 seconds |
| Start Position | F1 (row 0, col 5) |
| Treasure | F6 (row 5, col 5) |
| Challenge Overrides | c17: 50 points, c7: 750 points |

A compact 6×6 map with door/key mechanics. The agent starts top-right and must reach the treasure at bottom-right. Features a red door (c30) and red key (c40), walls blocking the top-left corner, and high-value coins (c7 worth 750 points).

### Finale 3

| Parameter | Value |
|-----------|-------|
| Grid Size | 9×9 |
| Timer | 120 seconds |
| Start Position | E9 (row 8, col 4) |
| Treasure | E1 (row 0, col 4) |
| Challenge Overrides | c17: 50 points |

A fortress-style 9×9 map with heavy wall borders forming a concentric maze. The agent starts at the bottom center and must navigate inward/upward to reach the treasure at the top center. The outer ring is mostly walls, with coins (c7) guarding the corridors. The inner rings contain spike traps (c8), guardrails (c1), and point challenges (c4, c5). A red door/key pair and c6 challenge add complexity.

## Files

- `map.json` — The known practice map as a 10×10 grid array
- `map.png` — Visual rendering of the known practice map
- `finale-1-map.json` — Finale round 1 map (10×10)
- `finale-1-map.png` — Visual rendering of finale 1
- `finale-2-map.json` — Finale round 2 map (6×6)
- `finale-2-map.png` — Visual rendering of finale 2
- `finale-3-map.json` — Finale round 3 map (9×9)
- `finale-3-map.png` — Visual rendering of finale 3
- `challenges.yaml` — Full challenge definition file (includes door/key tiles)
- `generate_finale_maps.py` — Script used to generate the finale map JSON files
