from __future__ import annotations

from pygame.math import Vector2
from pygame.transform import rotozoom
from pygame.surface import Surface

from .game_utils import load_sprite, wrap_position, get_random_velocity


class GameEntity:
    """Base class for all moving objects in the game."""

    def __init__(self, position: Vector2, sprite_name: str):
        self.position = Vector2(position)
        self.sprite = load_sprite(sprite_name)
        self.radius = max(self.sprite.get_size()) / 2
        self.velocity = Vector2(0, 0)

    def move(self, surface: Surface) -> None:
        self.position += self.velocity
        self.position = wrap_position(self.position, surface)

    def draw(self, surface: Surface) -> None:
        rect = self.sprite.get_rect(center=self.position)
        surface.blit(self.sprite, rect)

    def update(self, surface: Surface) -> None:
        self.move(surface)

    def collides_with(self, other: "GameEntity") -> bool:
        return self.position.distance_to(other.position) < self.radius + other.radius


class Spaceship(GameEntity):
    """Player controlled spaceship."""

    def __init__(self, position: Vector2):
        super().__init__(position, "spaceship")
        self.direction = Vector2(0, -1)
        self.rotation_speed = 5
        self.acceleration = 0.25
        self.friction = 0.99
        self.max_speed = 8.0
        self.is_thrusting = False

    def rotate(self, clockwise: bool = True) -> None:
        angle = self.rotation_speed if clockwise else -self.rotation_speed
        self.direction.rotate_ip(angle)

    def apply_acceleration(self) -> None:
        if self.is_thrusting:
            self.velocity += self.direction * self.acceleration
        self.velocity *= self.friction
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

    def update(self, surface: Surface) -> None:
        self.apply_acceleration()
        super().update(surface)

    def draw(self, surface: Surface) -> None:
        angle = self.direction.angle_to(Vector2(0, -1))
        rotated_sprite = rotozoom(self.sprite, angle, 1.0)
        rect = rotated_sprite.get_rect(center=self.position)
        surface.blit(rotated_sprite, rect)


class Bullet(GameEntity):
    """Projectile fired by the spaceship."""

    def __init__(self, position: Vector2, velocity: Vector2):
        super().__init__(position, "bullet ")
        self.velocity = Vector2(velocity)
        self.lifetime = 60

    def update(self, surface: Surface) -> None:
        super().update(surface)
        self.lifetime -= 1

    @property
    def expired(self) -> bool:
        return self.lifetime <= 0


_NEXT_SIZE = {"Huge": "Large", "Large": "Medium", "Medium": "Small"}


class Asteroid(GameEntity):
    """Asteroid object that can split into smaller asteroids."""

    def __init__(self, position: Vector2, size: str = "Large", velocity: Vector2 | None = None):
        super().__init__(position, f"Asteroid {size}")
        self.size = size
        self.velocity = Vector2(velocity) if velocity is not None else get_random_velocity(1, 3)

    def split(self) -> list["Asteroid"]:
        if self.size not in _NEXT_SIZE:
            return []
        new_size = _NEXT_SIZE[self.size]
        return [
            Asteroid(self.position, new_size, get_random_velocity(1, 3)),
            Asteroid(self.position, new_size, get_random_velocity(1, 3)),
        ]
