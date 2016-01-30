import pygame
import sys
from SpaceShip import SpaceShip
from settings import *


pygame.init()
display = pygame.display.set_mode((RES_X, RES_Y))
screen = pygame.display.get_surface()

ship = SpaceShip((120, 120))
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        ship.events(e)
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()

    delta_time = clock.tick(FPS)
    ship.update(delta_time)
    screen.fill(BACKGROUND_COLOR)
    ship.render(screen)
    pygame.display.flip()