from __future__ import annotations

import sys
import pygame
from pygame.math import Vector2

from .models import Spaceship, Asteroid, Bullet
from .game_utils import load_sprite, get_random_position, get_random_velocity


class AsteroidsGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Asteroids: Remastered")

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.background = load_sprite("space", with_alpha=False)
        self.font = pygame.font.Font(None, 36)

        self.spaceship = Spaceship(Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2))
        self.bullets: list[Bullet] = []
        self.asteroids: list[Asteroid] = []
        self.score = 0

        for _ in range(6):
            asteroid = Asteroid(
                get_random_position(self.screen),
                size="Large",
                velocity=get_random_velocity(1, 3),
            )
            self.asteroids.append(asteroid)

    def create_bullet(self) -> None:
        velocity = self.spaceship.direction * 10 + self.spaceship.velocity
        bullet = Bullet(self.spaceship.position, velocity)
        self.bullets.append(bullet)

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    self.create_bullet()

        keys = pygame.key.get_pressed()
        self.spaceship.is_thrusting = keys[pygame.K_w]
        if keys[pygame.K_d]:
            self.spaceship.rotate(clockwise=True)
        if keys[pygame.K_a]:
            self.spaceship.rotate(clockwise=False)
        return True

    def process_logic(self) -> None:
        self.spaceship.update(self.screen)
        for bullet in list(self.bullets):
            bullet.update(self.screen)
            if bullet.expired:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            asteroid.update(self.screen)

        for bullet in list(self.bullets):
            for asteroid in list(self.asteroids):
                if bullet.collides_with(asteroid):
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    self.score += 10
                    self.asteroids.extend(asteroid.split())
                    break

        for asteroid in self.asteroids:
            if asteroid.collides_with(self.spaceship):
                self.reset_game()
                break

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))

        for asteroid in self.asteroids:
            asteroid.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        self.spaceship.draw(self.screen)

        score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        self.clock.tick(60)

    def reset_game(self) -> None:
        self.__init__()

    def main_loop(self) -> None:
        running = True
        while running:
            running = self.handle_events()
            self.process_logic()
            self.draw()

    def quit_game(self) -> None:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = AsteroidsGame()
    try:
        game.main_loop()
    finally:
        game.quit_game()
