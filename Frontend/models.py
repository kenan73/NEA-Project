from pygame.math import Vector2
from pygame.transform import rotozoom

from game_utils import load_sprite

up = Vector2(0, -1)

class GameEntity:
    def __init__(self, position, sprite, screen_dimensions):
        self.position = Vector2(position)
        self.sprite = load_sprite(sprite) 
        self.screen_width, self.screen_height = screen_dimensions
        self.velocity = Vector2(0, 0)
        
    def move(self):
        self.position += self.velocity
        self.wrap_screen()
    
    def wrap_screen(self):
        '''Wraps sprites across opposite ends of the screen.'''
        if self.position.x < 0:
            self.position.x = self.screen_width
        elif self.position.x > self.screen_width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = self.screen_height
        elif self.position.y > self.screen_height:
            self.position.y = 0
    
    def draw(self, surface):
        blit_position = self.position - Vector2(self.sprite.get_width() / 2, self.sprite.get_height() / 2)
        surface.blit(self.sprite, blit_position)
    
    def update(self):
        self.move()
        
class Spaceship(GameEntity):
    '''Initialises the position of the spaceship and calculates its movements'''
    def __init__(self, position, screen_dimensions):
        super().__init__(position, 'spaceship', screen_dimensions)
        self.direction = Vector2(0, -1)
        self.rotation_speed = 5
        self.acceleration = 0.5
        self.friction = 0.98
        self.max_speed = 7.0
        self.is_thrusting = False
    
    def rotate(self, clockwise=True):
        '''The angle of rotation for the ship is calculated.'''
        sign = 1 if clockwise else -1
        angle = self.rotation_speed * sign
        self.direction.rotate_ip(angle)
    
    def apply_acceleration(self):
        '''The acceleration of the ship is applied to its velocity based on its current direction.'''
        if self.is_thrusting:
            self.velocity += self.direction * self.acceleration
        else:
            self.velocity *= self.friction
        
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
    
    def update(self, surface):
        '''Updates spaceship's state, applies rotation and acceleration, then updates its position.'''
        self.apply_acceleration()
        super().move()
    
    def draw(self, surface):
        '''Draws the rotated ship at its current position.'''
        angle = self.direction.angle_to(Vector2(0, -1))
        rotated_sprite = rotozoom(self.sprite, angle, 1.0)
        blit_position = self.position - Vector2(rotated_sprite.get_size()) / 2
        surface.blit(rotated_sprite, blit_position)

class Asteroid(GameEntity)
                