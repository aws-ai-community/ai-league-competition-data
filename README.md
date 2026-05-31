# AWS AI League — Competition Data

Historical competition data from the AWS AI League Agentic Challenge events.

This repository contains maps, challenge definitions, and scoring parameters from past competitions. Use this data to practice strategies, build tools, or study map layouts with the [Community Edition](https://github.com/aws-ai-community/ai-league-community-edition) Map Builder.

## Directory Structure

```
competitions/
└── 2026/
    ├── Hero-Community-Builder/   # Online competition (May 2026)
    │   ├── README.md             # Event overview and rules
    │   ├── map.json              # Map grid (10×10 array)
    │   ├── map.png               # Visual map rendering
    │   └── challenges.yaml       # Challenge definitions and scoring
    ├── London-Summit/            # In-person summit event (May 2026)
    │   ├── README.md
    │   ├── map.json              # Known practice map
    │   ├── map.png
    │   └── challenges.yaml       # Includes door/key mechanics
    └── .../                      # Future events
source/
└── agentic-sprites/              # 64×64 PNG sprite assets for all tile types
scripts/
└── render_map.py                 # Generate map.png from map.json using sprites
```

## Competitions

| Event | Date | Timer | Notable Features |
|-------|------|-------|------------------|
| Hero Community Builder | May 2026 | 3:50 | Base challenge set, online leaderboard |
| London Summit | May 2026 | 5:50 | Door/key mechanics, 1 known + 3 unknown maps |

## How to Use

### Load a map in the Community Edition Map Builder

The `map.json` files are compatible with the Map Builder in the AI League Community Edition app. Import them directly to visualize and test pathfinding strategies.

### Render a map image

```bash
pip install Pillow
python scripts/render_map.py competitions/2026/Hero-Community-Builder/map.json
```

This generates a `map.png` in the same directory as the input file.

### Study challenge definitions

Each `challenges.yaml` contains the full game parameters: challenge types, point values, grading methods, scoring formulas, and tool constraints.

## Sprite Assets

The `source/agentic-sprites/` directory contains the 64×64 PNG sprites used in the game UI:

- `normal.png`, `wall.png`, `treasure.png` — terrain tiles
- `c1.png` through `c43.png` — challenge, coin, hazard, door, and key tiles
- `avatar.png` — player character (used for start position)
- `lives.png`, `time.png` — UI elements

## Contributing

If you have data from other AI League events (maps, challenge configs, scoring results), feel free to open a PR.
