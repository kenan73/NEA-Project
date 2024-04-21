import pygame
import math

class Spaceship:
    def __init__(self, x, y, image, screen_size):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.health = 3
        self.image = image
        self.original_image = image  # Keep the original to prevent degradation on rotation
        self.screen_width, self.screen_height = screen_size
        self.radius = self.image.get_width() / 2  # Assuming the image is circular

    def rotate(self, direction):
        if direction == "left":
            self.angle += 5
        elif direction == "right":
            self.angle -= 5
        self.angle %= 360  # Ensure the angle stays within 0-359 degrees
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def move(self):
        radians = math.radians(self.angle)
        self.dx += math.cos(radians)
        self.dy += math.sin(radians)
        self.x += self.dx
        self.y += self.dy
        self.x %= self.screen_width  # Wrap around horizontally
        self.y %= self.screen_height  # Wrap around vertically

    def shoot(self):
        radians = math.radians(self.angle)
        bullet_dx = math.cos(radians) * 10
        bullet_dy = math.sin(radians) * 10
        return Bullet(self.x, self.y, bullet_dx, bullet_dy)

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, -self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_image, new_rect.topleft)

    def check_collision(self, asteroid):
        dist = math.hypot(self.x - asteroid.x, self.y - asteroid.y)
        return dist < self.radius + asteroid.radius

    def update(self, screen):
        self.move()
        self.draw(screen)
