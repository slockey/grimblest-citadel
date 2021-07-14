
from typing import Tuple

import numpy as np  # type: ignore

# tile graphics - compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),   # unicode codepoint
        ("fg", "3B"),       # 3 unsigned bytes for RGB color
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),      # true if the tile can be walked on
        ("transparent", np.bool),   # true if this tile doesn't block FOV
        ("dark", graphic_dt),       # graphics for when this tile is NOT in FOV
    ]
)

def new_tile(
    *,  # enforce the use of keywords, so that parameter order doesn't matter
    walkable: int, 
    transparent: int, 
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]], 
) -> np.ndarray:
    """Helper function for definition of individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)