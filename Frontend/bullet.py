import pygame

class Bullet:
    def __init__(self, x, y, dx, dy, screen_size, image=None):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.screen_width, self.screen_height = screen_size
        self.image = image
        self.radius = 5  # Small radius for simple collision detection

    def move(self):
        """Update the bullet's position."""
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        """Draw the bullet on the screen."""
        if self.image:
            screen.blit(self.image, (self.x - self.radius, self.y - self.radius))
        else:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    def off_screen(self):
        """Check if the bullet is off the screen."""
        return not (0 <= self.x <= self.screen_width and 0 <= self.y <= self.screen_height)

# Collision detection with asteroids handled in GameManager
