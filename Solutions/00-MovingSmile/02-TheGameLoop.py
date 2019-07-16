# My first Pygame program.
# Authors: Many people and David Fisher

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()


# DONE: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
