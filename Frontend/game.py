import pygame
import sys  # Import sys for handling exit

from models import GameSprite
from game_utils import load_sprite

class Asteroids:
    def __init__(self):
        '''Initializes pygame and sets up the game window.'''
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite('space', False)
        self.clock = pygame.time.Clock()
        self.spaceship = GameSprite(
            (400, 300), load_sprite('spaceship'), (0, 0)
        )
        self.asteroid = GameSprite(
            (400, 300), load_sprite('Asteroid Huge'), (1,0)
            
        )

    def main_loop(self):
        '''Runs the main game loop.'''
        running = True
        while running:
            for event in pygame.event.get():
                self._handle_input(event)
            self._process_logic()
            self._draw()

    def _init_pygame(self):
        '''Initializes the pygame modules and sets the caption of the window.'''
        pygame.init()
        pygame.display.set_caption('Asteroids: Remastered')

    def _handle_input(self, event):
        '''Handles user input.'''
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def _process_logic(self):
        '''Processes the game logic.'''
        self.spaceship.move()
        self.asteroid.move()

    def _draw(self):
        '''Draws all game elements on the screen and updates the display.'''
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
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
