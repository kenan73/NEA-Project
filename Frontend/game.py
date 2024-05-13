import pygame
import sys  # Import sys for handling exit

from models import Spaceship
from game_utils import load_sprite

class Asteroids:
    def __init__(self):
        '''Initializes pygame and sets up the game window.'''
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite('space', False)
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship((400, 300,), (self.screen.get_width(), self.screen.get_height()))

    def main_loop(self):
        '''Runs the main game loop.'''
        running = True
        while running:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            self.handle_input(event)
            self.process_logic()
            self.draw()

    def _init_pygame(self):
        '''Initializes the pygame modules and sets the caption of the window.'''
        pygame.init()
        pygame.display.set_caption('Asteroids: Remastered')

    def handle_input(self, event):
        '''Handles user inputs.'''
        is_key_pressed = pygame.key.get_pressed()
        
        self.spaceship.is_thrusting = False
        if is_key_pressed[pygame.K_d]:
            self.spaceship.rotate(clockwise=True)
        if is_key_pressed[pygame.K_a]:
                self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_w]:
            self.spaceship.is_thrusting = True

    def process_logic(self):
        '''Processes the game logic.'''
        self.spaceship.update(self.screen)

    def draw(self):
        '''Draws all game elements on the screen and updates the display.'''
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        '''self.asteroid.draw(self.screen)'''
        pygame.display.flip()
        self.clock.tick(60)

    def quit_game(self):
        '''Handles tasks to quit the game properly.'''
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Asteroids()
    try:
        game.main_loop()
    finally:
        game.quit_game()
