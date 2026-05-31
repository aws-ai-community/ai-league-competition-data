#!/usr/bin/env python3
"""Generate the 3 London Finale map JSON files."""

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent


def parse_coord(s: str) -> tuple[int, int]:
    """Parse coordinate like 'A1' -> (row, col). Column=letter, Row=number."""
    col = ord(s[0]) - ord('A')
    row = int(s[1:]) - 1
    return (row, col)


def make_grid(size: int) -> list[list[str]]:
    return [["normal"] * size for _ in range(size)]


# --- Finale 1: 10x10, 65s, start A10 [row 9, col 0], treasure J1 [row 0, col 9] ---
def generate_finale_1():
    g = make_grid(10)
    for s in ["A1", "E1", "A5", "J5", "E10", "J10"]:
        r, c = parse_coord(s)
        g[r][c] = "c17"
    for s in ["B1", "C1", "D1", "J6", "J7", "J8", "J9"]:
        r, c = parse_coord(s)
        g[r][c] = "c7"
    for s in ["B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5"]:
        r, c = parse_coord(s)
        g[r][c] = "c8"
    for s in ["A8", "B8", "C8", "C9", "C10"]:
        r, c = parse_coord(s)
        g[r][c] = "c5"
    r, c = parse_coord("I1")
    g[r][c] = "c2"
    r, c = parse_coord("J1")
    g[r][c] = "treasure"
    return g


# --- Finale 2: 6x6, 95s, start F1 [row 0, col 5], treasure F6 [row 5, col 5] ---
def generate_finale_2():
    g = make_grid(6)
    r, c = parse_coord("A1")
    g[r][c] = "c7"
    r, c = parse_coord("B1")
    g[r][c] = "wall"
    r, c = parse_coord("B2")
    g[r][c] = "wall"
    r, c = parse_coord("A2")
    g[r][c] = "c30"
    r, c = parse_coord("A6")
    g[r][c] = "c40"
    for s in ["C1", "A4", "C4", "F4", "C6"]:
        r, c = parse_coord(s)
        g[r][c] = "c2"
    for s in ["E5", "F5", "E6"]:
        r, c = parse_coord(s)
        g[r][c] = "c1"
    r, c = parse_coord("F6")
    g[r][c] = "treasure"
    return g


# --- Finale 3: 9x9, 120s, start E9 [row 8, col 4], treasure E1 [row 0, col 4] ---
def generate_finale_3():
    g = make_grid(9)
    for s in ["A1", "B1", "C1", "D1", "F1", "G1", "H1", "I1",
              "A2", "A3", "A4", "A5", "A6", "A7", "C7", "D7",
              "I2", "I3", "I4", "I5", "I6", "I7", "H7", "G7", "F7"]:
        r, c = parse_coord(s)
        g[r][c] = "wall"
    for s in ["B3", "B4", "B5", "B6", "H3", "H4", "H5", "H6", "A8", "A9", "I8"]:
        r, c = parse_coord(s)
        g[r][c] = "c7"
    r, c = parse_coord("I9")
    g[r][c] = "c40"
    r, c = parse_coord("B7")
    g[r][c] = "c30"
    for s in ["D2", "F2", "C3", "D3", "E3", "F3", "G3", "C4", "C5", "C6", "G4", "G5", "G6"]:
        r, c = parse_coord(s)
        g[r][c] = "c8"
    for s in ["E7", "D4", "E4", "F4"]:
        r, c = parse_coord(s)
        g[r][c] = "c1"
    for s in ["D6", "E6", "F6"]:
        r, c = parse_coord(s)
        g[r][c] = "c5"
    for s in ["B2", "H2"]:
        r, c = parse_coord(s)
        g[r][c] = "c17"
    r, c = parse_coord("E1")
    g[r][c] = "treasure"
    r, c = parse_coord("E2")
    g[r][c] = "c6"
    for s in ["D5", "E5", "F5"]:
        r, c = parse_coord(s)
        g[r][c] = "c4"
    for s in ["C2", "G2"]:
        r, c = parse_coord(s)
        g[r][c] = "c2"
    return g


if __name__ == "__main__":
    # Generate and save all three maps
    maps = [
        ("finale-1-map.json", generate_finale_1()),
        ("finale-2-map.json", generate_finale_2()),
        ("finale-3-map.json", generate_finale_3()),
    ]

    for filename, grid in maps:
        path = OUTPUT_DIR / filename
        with open(path, "w") as f:
            json.dump(grid, f, indent=2)
        print(f"Generated {path}")
        # Print grid for verification
        print(f"  Size: {len(grid)}x{len(grid[0])}")
        for row in grid:
            print(f"    {row}")
        print()
