from pygame.math import Vector2

class GameSprite:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite 
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)
    
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)
    
    def move(self):
        self.position = self.position + self.velocity
    
    def check_collision(self, other_sprite):
        distance = self.position.distance_to(other_sprite.position)
        return distance < self.radius + other_sprite.radius
        
        