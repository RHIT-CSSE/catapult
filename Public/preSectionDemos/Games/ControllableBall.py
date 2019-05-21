'''
Created on Jun 21, 2014

@author: burchtm
'''
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("Welcome to pygame!")
# background = pygame.image.load("Catapult-TV-Slide.gif")

def eventLoop():
    center = [200,200]
    radius = 50
    drawCircle = True
    while True:
        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEMOTION:
                center = event.pos
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_UP:
                    radius += 10
                if event.key == pygame.K_DOWN:
                    radius -= 10
                    if radius < 0:
                        radius = 0
                if event.key == pygame.K_1:
                    drawCircle = False
                if event.key == pygame.K_2:
                    drawCircle = True
            screen.fill([0,0,0])
#             screen.blit(background, [0,0])
            if drawCircle:
                pygame.draw.circle(screen, [150, 210, 235], center, radius)
            pygame.display.update()
            
eventLoop()