import pygame
from pygame.locals import *
from MainMenu import *
from Over import *
from Actors import *

screen_width = 750
screen_height = 425
fps = 30
background = None
world = None 

def init(backgroundpicture):
    global background, world
    pygame.init()
    screen = pygame.display.set_mode([screen_width,screen_height],0,32)
    background = pygame.image.load(backgroundpicture).convert_alpha()
    world = pygame.Surface((background.get_width(), background.get_height()))
    return screen

def update(counselors, player):
    global gameover
    player.act()
    for counselor in counselors:
        counselor.act()
        if counselor.sees(player):
            gameover = True

def draw(screen, actors, center_x, center_y):
    x = min(max(0, center_x - screen_width/2), world.get_width() - screen_width)
    y = min(max(0, center_y - screen_height/2), world.get_height() - screen_height)
    screen_rect = Rect(x, y, screen_width, screen_height)
    world.blit(background, screen_rect, screen_rect)
    for actor in actors:
        actor.draw()
    screen.blit(world, (0,0), screen_rect)
    pygame.display.flip()

def handle(events, actors):
    for event in events:
        if event.type == QUIT:
            exit()
        else:
            for actor in actors:
                actor.handle(event)

def level(number):
    if number == 1:
        backgroundpicture = 'basement.png'
    if number == 2:
        backgroundpicture = 'Floor1.png'
    if number == 3:
        backgroundpicture = 'Floor2.png'
    if number == 4:
        backgroundpicture = 'Floor3.png' 
    screen = init(backgroundpicture)
    global gameover
    gameover = False
    spacing = (2125-100)/(number+1)
    player = Player(world, 100, 210)
    counselors = []
    for i in range(1, number+1):
        counselors.append(Counselor(world, spacing*i-6,210))

    clock = pygame.time.Clock()
    events = pygame.event.get()
    running = True
    while running:
        handle(events, [player] + counselors)
        update(counselors, player)
        center_x = player.x + player.image.get_width()
        center_y = player.y + player.image.get_height()
        draw(screen, [player] + counselors, center_x, center_y)
        clock.tick(fps)
#        print clock.get_fps()
        if number < 4:
            if center_x >= 2100 or gameover == True:
                running = False
        elif number == 4:
            if center_x >= 2050 or gameover == True:
                running = False
        events = pygame.event.get()
    if gameover == True:
        return False
    return True


if __name__ == "__main__":
    level(number)
