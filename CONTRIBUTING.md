# Contributing to AWS AI League Competition Data

Thank you for contributing! This repository collects historical competition data from AWS AI League Agentic Challenge events.

## What We're Looking For

- Maps from past AI League events (practice maps, finale maps)
- Challenge definitions (YAML configs with tile types, scoring, constraints)
- Game parameters (timer, lives, grid size, start/treasure positions)
- Challenge type overrides specific to events or rounds

## How to Contribute

### Adding a New Competition

1. Create a directory under `competitions/<year>/<Event-Name>/`
2. Add the following files:
   - `README.md` — Event overview, game parameters, challenge types, scoring
   - `map.json` — Map grid as a JSON list-of-lists (each row is a list of tile key strings)
   - `challenges.yaml` — Challenge definitions and scoring parameters
3. Run the render script to generate a map image:
   ```bash
   pip install Pillow
   python scripts/render_map.py competitions/<year>/<Event-Name>/map.json
   ```
4. If the event had multiple rounds/maps, name them descriptively:
   - `map.json` — Known/practice map
   - `finale-1-map.json`, `finale-2-map.json`, etc. — Finale round maps

### Map JSON Format

Maps are stored as a 2D array of tile key strings:

```json
[
  ["normal", "wall", "c5", "normal", "treasure"],
  ["c7", "normal", "c1", "wall", "normal"],
  ["normal", "c8", "normal", "normal", "normal"]
]
```

Each row is a list, and the outer list contains all rows top-to-bottom.

### Valid Tile Keys

| Key | Name | Category |
|-----|------|----------|
| `normal` | Empty floor | Special |
| `wall` | Impassable wall | Special |
| `start` | Player start | Special |
| `treasure` | Goal | Special |
| `c1` | Violent Violet | Challenge |
| `c2` | Blue Brain | Challenge |
| `c3` | Memento | Challenge |
| `c4` | Dark Prophet | Challenge |
| `c5` | Bonehead | Challenge |
| `c6` | Boss | Challenge |
| `c7` | Coins | Coin |
| `c8` | Spikes | Hazard |
| `c17` | Distraction | Challenge |
| `c18` | Healthcare API | Challenge |
| `c30`–`c33` | Doors (Red/Green/Grey/Yellow) | Door |
| `c40`–`c43` | Keys (Red/Green/Grey/Yellow) | Key |

### Rendering Maps

The `scripts/render_map.py` script generates PNG images from map JSON files using the sprite assets in `source/agentic-sprites/`. Each non-wall tile is rendered with the `normal.png` background underneath, with the tile sprite layered on top.

```bash
python scripts/render_map.py path/to/map.json
# Outputs: path/to/map.png
```

### Challenge YAML Format

See existing files in `competitions/2026/` for the full format. Key sections:

- `game_parameters` — Grid size, lives, timer
- `tile_types` — All tile definitions
- `challenge_types` — Challenge scoring and grading methods
- `scoring` — Bonus formulas
- `map_generation` — Density parameters (if applicable)

## Pull Request Process

1. Fork the repository
2. Add your competition data following the structure above
3. Run the render script to generate map images
4. Submit a PR with a clear description of which event the data is from

## Data Accuracy

Please ensure:
- Maps are accurate representations of what was used in the competition
- Point values and game parameters match the actual event configuration
- If data is approximate or reconstructed, note this in the README

## Questions?

Open an issue if you're unsure about format or have data from an event not yet covered.
