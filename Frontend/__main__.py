import pygame
import random
from asteroid import Asteroid
from bullet import Bullet 
from spaceship import Spaceship

pygame.init()
my_asteroid = Asteroid(x=100, y=100, dx=5, dy=5, size=20, image=asteroid_image)
pygame.display.set_caption('Kinda Blue')
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    screen.fill((135, 206, 235))
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    r = random.randint(2, 10)
    pygame.draw.circle(screen, (0, 0, 150), (x, y), r)
    pygame.display.flip()