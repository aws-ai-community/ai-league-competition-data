# AWS AI League — Competition Data

Historical competition data from the AWS AI League Agentic Challenge events.

This repository contains maps, challenge definitions, and scoring parameters from past competitions. Use this data to practice strategies, build tools, or study map layouts with the [Community Edition Map Builder](https://github.com/aws-ai-community/ai-league-community-edition).

## Competitions

| Event | Date | Maps | Details |
|-------|------|------|---------|
| [Hero Community Builder](competitions/2026/Hero-Community-Builder/) | May 2026 | 1 map (10×10, 230s) | Online leaderboard competition |
| [London Summit](competitions/2026/London-Summit/) | May 2026 | 1 practice + 3 finale maps | In-person summit with door/key mechanics |
| [Bengaluru Summit](competitions/2026/Bengaluru-Summit/) | May 2026 | Same as London | In-person summit (same day as London) |
| [New York City Summit](competitions/2026/New-York-City-Summit/) | June 2026 | 1 practice + finale maps | In-person summit with dual door/key pairs |

## Directory Structure

```
competitions/
└── 2026/
    ├── Hero-Community-Builder/   # Online competition
    ├── London-Summit/            # Example structure (all events follow this pattern)
    │   ├── README.md             # Event overview with all maps embedded
    │   ├── map.json              # Known practice map
    │   ├── map.png               # Practice map rendering
    │   ├── finale-1-map.json     # Finale round 1
    │   ├── finale-1-map.png
    │   ├── finale-2-map.json     # Finale round 2
    │   ├── finale-2-map.png
    │   ├── finale-3-map.json     # Finale round 3
    │   └── finale-3-map.png
    ├── Bengaluru-Summit/
    ├── New-York-City-Summit/
    └── ...                       # Additional events follow the same structure
source/
└── agentic-sprites/              # 100×100 PNG sprite assets for all tile types
scripts/
└── render_map.py                 # Generate map PNGs from map.json using sprites
```

## How to Use

### View maps

Each competition README embeds the rendered map images inline. Click through to the competition links above.

### Render a map image

```bash
pip install Pillow
python scripts/render_map.py competitions/2026/London-Summit/finale-3-map.json
```

Outputs a PNG in the same directory as the input file. Non-wall tiles are rendered with the normal floor background underneath.

### Load in the Community Edition Map Builder

The `map.json` files are compatible with the Map Builder's import format. Copy the JSON content and use it to visualize and test pathfinding strategies.

## Sprite Assets

The `source/agentic-sprites/` directory contains the 100×100 PNG sprites used in the game:

- `normal.png`, `wall.png`, `treasure.png` — terrain tiles
- `c1.png` through `c43.png` — challenge, coin, hazard, door, and key tiles
- `avatar.png` — player character
- `lives.png`, `time.png` — UI elements

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding competition data.

## License

See [LICENSE](LICENSE) for details.
