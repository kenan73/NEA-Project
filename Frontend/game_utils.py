from __future__ import annotations

import random
from pathlib import Path

from pygame.image import load
from pygame.math import Vector2
from pygame.surface import Surface


_ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets" / "sprites"


def load_sprite(name: str, with_alpha: bool = True):
    """Load a sprite from the assets directory."""
    path = _ASSETS_PATH / f"{name}.png"
    sprite = load(str(path))
    return sprite.convert_alpha() if with_alpha else sprite.convert()


def get_random_position(surface: Surface) -> Vector2:
    """Return a random position inside the given surface."""
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )


def get_random_velocity(min_speed: float, max_speed: float) -> Vector2:
    """Return a random velocity vector between the given speeds."""
    speed = random.uniform(min_speed, max_speed)
    angle = random.uniform(0, 360)
    return Vector2(speed, 0).rotate(angle)


def wrap_position(position: Vector2, surface: Surface) -> Vector2:
    """Wrap a position around the screen so objects never leave the play area."""
    x, y = position
    return Vector2(x % surface.get_width(), y % surface.get_height())
