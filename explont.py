import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Explon\'t')

screen = pygame.display.set_mode((500, 500), 0, 32)

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)
