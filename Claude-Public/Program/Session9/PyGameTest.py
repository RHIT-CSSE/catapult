import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([300,300],0,32)
pygame.display.set_caption('This is a pygame window.')

event = pygame.event.poll()

pygame.mouse.set_visible(0)

while event.type != QUIT:
    if event.type == KEYDOWN:
        print event.key
        if event.key == K_UP:
            print 'Up?'
    screen.fill((0,0,0))
    point = pygame.mouse.get_pos()
    pygame.draw.circle(screen,(255,255,255),point,50)
    pygame.display.update()
    event = pygame.event.poll()
