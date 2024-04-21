import pygame
import random
import math

class Asteroid:
    def __init__(self, x, y, dx, dy, size, image):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.image = image
        self.radius = self.image.get_width() / 2  # Assuming the image is a circle

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Screen wrapping logic
        self.x %= 800  # Assuming screen width is 800 pixels
        self.y %= 600  # Assuming screen height is 600 pixels

    def split(self):
        # This method will be called when the asteroid is hit by a bullet
        fragments = []
        if self.size > 1:
            for _ in range(2):  # Split into two smaller pieces
                new_size = self.size - 1
                new_dx = random.choice([-1, 1]) * (self.dx * 1.5)
                new_dy = random.choice([-1, 1]) * (self.dy * 1.5)
                new_image = pygame.transform.scale(self.image, (int(self.radius * 0.5), int(self.radius * 0.5)))
                fragments.append(Asteroid(self.x, self.y, new_dx, new_dy, new_size, new_image))
        return fragments

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def update(self):
        self.move()

# The image loading and resizing should be handled outside the class to avoid repetition and enhance performance
