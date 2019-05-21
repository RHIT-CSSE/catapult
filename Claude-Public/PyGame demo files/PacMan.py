import pygame
from pygame.locals import *
from random import randint

width = 800
height = 800
fps = 60
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3


pygame.init()
icon = pygame.Surface((16,16))
icon.fill((255,0,0))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width,height),0,32)

pac_width = 100
pac_height = 100

closed = pygame.Surface((pac_width,pac_height))
closed.fill((255,255,255))
closed.set_colorkey((255,255,255))
pygame.draw.circle(closed,pygame.Color('yellow'),(int(pac_width/2),int(pac_height/2)),int(pac_width/2))

open = pygame.Surface((pac_width,pac_height))
open.fill((255,255,255))
open.set_colorkey((255,255,255))
pygame.draw.circle(open,pygame.Color('yellow'),(int(pac_width/2),int(pac_height/2)),int(pac_width/2))
pygame.draw.polygon(open,(255,255,255),[(pac_width/2,pac_height/2),(pac_width,0),(pac_width,pac_height)])

graphics = [[None, None] for i in range(4)]

for i in range(4):
    graphics[i][0] = pygame.transform.rotate(closed, i*90)
    graphics[i][1] = pygame.transform.rotate(open, i*90)

cur_frame = 0

x = 50
y = 50
speed = 5
dir = LEFT

def draw():
    screen.fill((255,255,255))
    if cur_frame % 30 <= 15:
        screen.blit(graphics[dir][0], (x,y))
    else:
        screen.blit(graphics[dir][1], (x,y))
    pygame.display.update()


event = pygame.event.poll()
while event.type is not QUIT:
    draw()
    if event.type == KEYDOWN:
        if event.key == K_UP:
            dir = UP
        elif event.key == K_DOWN:
            dir = DOWN
        elif event.key == K_LEFT:
            dir = LEFT
        elif event.key == K_RIGHT:
            dir = RIGHT
    if dir == UP:
        y -= speed
    elif dir == DOWN:
        y += speed
    elif dir == LEFT:
        x -= speed
    elif dir == RIGHT:
        x += speed
        
    if x < 0:
        x = 0
        dir = randint(0,3)
    if y < 0:
        y = 0
        dir = randint(0,3)
    if x+pac_width > width:
        x = width-pac_width
        dir = randint(0,3)
    if y+pac_height > height:
        y = height-pac_height
        dir = randint(0,3)
        
    cur_frame += 1
    pygame.time.delay(int(1000/fps))
    event = pygame.event.poll()