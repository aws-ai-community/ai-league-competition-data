#!/usr/bin/env python3
"""
Render a map.json file into a visual PNG image using sprite assets.

Usage:
    python scripts/render_map.py competitions/2026/Hero-Community-Builder/map.json
    python scripts/render_map.py competitions/2026/London-Summit/map.json

Output:
    Creates map.png in the same directory as the input map.json.
"""

import json
import sys
from pathlib import Path

from PIL import Image


# Resolve paths relative to the repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
SPRITES_DIR = REPO_ROOT / "source" / "agentic-sprites"


def get_sprite_path(tile_code: str) -> Path:
    """Map a tile code to its sprite PNG file."""
    if tile_code == "start":
        return SPRITES_DIR / "avatar.png"
    sprite_file = SPRITES_DIR / f"{tile_code}.png"
    if sprite_file.exists():
        return sprite_file
    # Fallback to normal tile for unknown codes
    return SPRITES_DIR / "normal.png"


def render_map(map_path: Path) -> Path:
    """Render a map.json file to a PNG image."""
    with open(map_path) as f:
        grid = json.load(f)

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        print("Error: empty map", file=sys.stderr)
        sys.exit(1)

    # Determine sprite size from the first available sprite
    sample_sprite = Image.open(get_sprite_path("normal"))
    tile_size = sample_sprite.width  # Sprites are square

    # Load the normal background tile (used as base for all cells)
    normal_sprite = Image.open(SPRITES_DIR / "normal.png").convert("RGBA")
    if normal_sprite.width != tile_size or normal_sprite.height != tile_size:
        normal_sprite = normal_sprite.resize((tile_size, tile_size), Image.LANCZOS)

    # Tiles that replace the background entirely (no normal underneath)
    OPAQUE_TILES = {"wall"}

    # Create output image
    output = Image.new("RGBA", (cols * tile_size, rows * tile_size))

    for row_idx, row in enumerate(grid):
        for col_idx, tile_code in enumerate(row):
            x = col_idx * tile_size
            y = row_idx * tile_size

            if tile_code in OPAQUE_TILES:
                # Wall tiles replace the background entirely
                sprite_path = get_sprite_path(tile_code)
                sprite = Image.open(sprite_path).convert("RGBA")
                if sprite.width != tile_size or sprite.height != tile_size:
                    sprite = sprite.resize((tile_size, tile_size), Image.LANCZOS)
                output.paste(sprite, (x, y), sprite)
            else:
                # All other tiles: draw normal background first, then overlay the tile sprite
                output.paste(normal_sprite, (x, y), normal_sprite)
                if tile_code != "normal":
                    sprite_path = get_sprite_path(tile_code)
                    sprite = Image.open(sprite_path).convert("RGBA")
                    if sprite.width != tile_size or sprite.height != tile_size:
                        sprite = sprite.resize((tile_size, tile_size), Image.LANCZOS)
                    output.paste(sprite, (x, y), sprite)

    # Place avatar on start position (top-left, [0,0])
    avatar_path = SPRITES_DIR / "avatar.png"
    if avatar_path.exists():
        avatar = Image.open(avatar_path).convert("RGBA")
        if avatar.width != tile_size or avatar.height != tile_size:
            avatar = avatar.resize((tile_size, tile_size), Image.LANCZOS)
        # Only overlay avatar if the start cell isn't already the avatar
        start_tile = grid[0][0]
        if start_tile != "start":
            output.paste(avatar, (0, 0), avatar)

    # Save output — use same base name as input with .png extension
    output_path = map_path.with_suffix('.png')
    output.save(output_path, "PNG")
    print(f"Rendered {rows}x{cols} map ({tile_size}px tiles) -> {output_path}")
    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python render_map.py <path/to/map.json>", file=sys.stderr)
        sys.exit(1)

    map_path = Path(sys.argv[1])
    if not map_path.is_absolute():
        map_path = Path.cwd() / map_path

    if not map_path.exists():
        print(f"Error: {map_path} not found", file=sys.stderr)
        sys.exit(1)

    render_map(map_path)


if __name__ == "__main__":
    main()
