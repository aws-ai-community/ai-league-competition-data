# AWS AI League — Competition Data

Historical competition data from the AWS AI League Agentic Challenge events, across two game formats: **Agentic Maze** (scored dungeon-map runs) and **Agentic Football** (head-to-head team knockouts).

This repository contains maps, challenge definitions, scoring parameters, and results from past competitions. Use this data to practice strategies, build tools, or study map layouts with the [Community Edition Map Builder](https://github.com/aws-ai-community/ai-league-community-edition).

## Agentic Maze

Scored dungeon-map competitions: navigate a grid, solve challenges, reach the treasure, and optimise your token bonus.

| Event                                                                           | Date           | Maps                       | Details                                                       | Winner    |
| ------------------------------------------------------------------------------- | -------------- | -------------------------- | ------------------------------------------------------------- | --------- |
| [Hero Community Builder](competitions/2026/agentic-maze/Hero-Community-Builder/) | May 2026       | 1 map (10×10, 230s)        | Online leaderboard competition                                | rosscomp1   |
| [London Summit](competitions/2026/agentic-maze/London-Summit/)                   | May 2026       | 1 practice + 3 finale maps | In-person summit with door/key mechanics                      | Josh Bayne   |
| [Bengaluru Summit](competitions/2026/agentic-maze/Bengaluru-Summit/)             | May 2026       | Same as London             | In-person summit (same day as London)                         | TBC   |
| [New York City Summit](competitions/2026/agentic-maze/New-York-City-Summit/)     | June 2026      | 1 practice + finale maps   | In-person summit with dual door/key pairs                     | rosscomp1    |
| [Hong Kong Summit](competitions/2026/agentic-maze/Hong-Kong-Summit/)             | 17 June 2026   | 1 practice + 3 finale maps | First HK summit; same maps as London, +2000 practice treasure | Max Chui   |
| [Washington DC Summit](competitions/2026/agentic-maze/Washington-DC-Summit/)     | June/July 2026 | 1 practice + finale maps   | In-person summit                                              | Rogue   |
| [Virtual APJ](competitions/2026/agentic-maze/Virtual-APJ/)                       | September 2026 | 1 practice + 3 finale maps | Online APJ competition; per-round point overrides             | LozicCode |
| [EMEA Virtual](competitions/2026/agentic-maze/EMEA-Virtual/)                     | September 2026 | 1 practice + 3 finale maps | Online EMEA competition; APJ-style maps, reduced lives        | MarkRoss  |
| [GCR Virtual](competitions/2026/agentic-maze/GCR-Virtual/)                       | September 2026 | 1 practice + 3 finale maps | Online GCR competition; same maps as APJ, no disqualifications | Wood      |
| [LATAM Virtual](competitions/2026/agentic-maze/LATAM-Virtual/)                   | September 2026 | 1 practice + 3 finale maps | Online LATAM competition; same maps as APJ                     | wen       |

## Agentic Football

Head-to-head competitions: build a team of AI agents that compete in live matches, played as a single-elimination knockout bracket.

| Event                                                              | Date           | Format                     | Details                              | Champion         |
| ------------------------------------------------------------------ | -------------- | -------------------------- | ------------------------------------ | ---------------- |
| [Virtual APJ](competitions/2026/agentic-football/Virtual-APJ/)     | September 2026 | 16-team knockout           | Round of 16 → QF → SF → Final        | Snow Halation FC |

## Directory Structure

```
competitions/
└── 2026/
    ├── agentic-maze/                 # Scored dungeon-map competitions
    │   ├── Hero-Community-Builder/
    │   ├── London-Summit/            # Example structure (all maze events follow this pattern)
    │   │   ├── README.md             # Event overview with all maps embedded
    │   │   ├── map.json              # Known practice map
    │   │   ├── map.png               # Practice map rendering
    │   │   ├── finale-1-map.json     # Finale round 1
    │   │   ├── finale-1-map.png
    │   │   ├── finale-2-map.json     # Finale round 2
    │   │   ├── finale-2-map.png
    │   │   ├── finale-3-map.json     # Finale round 3
    │   │   └── finale-3-map.png
    │   ├── Bengaluru-Summit/
    │   ├── New-York-City-Summit/
    │   ├── Hong-Kong-Summit/         # Same maps as London; +2000 practice treasure
    │   ├── Virtual-APJ/              # Online APJ competition (per-round point overrides)
    │   ├── EMEA-Virtual/             # Online EMEA competition (APJ-style maps, reduced lives)
    │   ├── GCR-Virtual/              # Online GCR competition (same maps as APJ, no DQs)
    │   ├── LATAM-Virtual/            # Online LATAM competition (same maps as APJ)
    │   └── ...                       # Additional maze events follow the same structure
    └── agentic-football/             # Head-to-head team knockout competitions
        └── Virtual-APJ/              # 16-team knockout bracket
            └── README.md             # Bracket diagram + per-round results
source/
└── agentic-sprites/              # 100×100 PNG sprite assets for all maze tile types
scripts/
└── render_map.py                 # Generate maze map PNGs from map.json using sprites
```

## How to Use

### View maps

Each competition README embeds the rendered map images inline. Click through to the competition links above.

### Render a map image

```bash
pip install Pillow
python scripts/render_map.py competitions/2026/agentic-maze/London-Summit/finale-3-map.json
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
