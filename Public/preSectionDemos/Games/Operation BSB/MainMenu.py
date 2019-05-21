#######                                                   
#     # #####  ###### #####    ##   ##### #  ####  #    # 
#     # #    # #      #    #  #  #    #   # #    # ##   # 
#     # #    # #####  #    # #    #   #   # #    # # #  # 
#     # #####  #      #####  ######   #   # #    # #  # # 
#     # #      #      #   #  #    #   #   # #    # #   ## 
####### #      ###### #    # #    #   #   #  ####  #    # 

######   #####  ######  
#     # #     # #     # 
#     # #       #     # 
######   #####  ######  
#     #       # #     # 
#     #       # #     #
#     # #     # #     # 
######   #####  ######  

#    Group 1: Hot Air Balloons
#    Zach Babyak
#    David Dvorak
#    Nate Adams

import pygame
from pygame.locals import *
from MainMenu import *
from Levels import *
from Credits import *
from Over import *
from Congrats import *
from Instructions import *

def init():
    pygame.init()
    screen_width = 1000
    screen_height = 600
    fps = 30
    pygame.mixer.music.load('UR2.mp3')
    screen = pygame.display.set_mode([screen_width,screen_height],0,32)
    pygame.mixer.music.play(-1)
    return screen

def startgame():
    s = init()
    startpage(s)

class Menu:
    '''    The main menu for the game    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pass
    def handle(self, event):
        pass

class Title(Menu):
    def __init__(self, screen, x, y):
        Menu.__init__(self, screen, x, y)
        self.image = pygame.image.load("Title.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
class Instructions(Menu):
    def __init__(self, screen, x, y):
        Menu.__init__(self, screen, x, y)
        self.image = pygame.image.load("Instructions.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
class Play(Menu):
    def __init__(self, screen, x, y):
        Menu.__init__(self, screen, x, y)
        self.image = pygame.image.load("Play.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
class Credits(Menu):
    def __init__(self, screen, x, y):
        Menu.__init__(self, screen, x, y)
        self.image = pygame.image.load("Credits.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

def MouseClick(click):
    global playx, playy, instructionsx, instructionsy, creditsx, creditsy, choice
    if click[0] > playx and click[0] < playx+129 and click[1] > playy and click[1] < playy+111:
        choice = 'PLAY'
    if click[0] > instructionsx and click[0] < instructionsx+269 and click[1] > instructionsy and click[1] < instructionsy+50:
        choice = 'INSTRUCTIONS'
    if click[0] > creditsx and click[0] < creditsx+168 and click[1] > creditsy and click[1] < creditsy+85:
        choice = 'CREDITS'

def handle(events, objects):
    for event in events:
        if event.type == QUIT:
            exit()

def draw(screen, objects):
    screen.fill(pygame.Color('black'))
    for object in objects:
        object.draw()
    pygame.display.flip()

def startpage(screen):
    global playx, playy, instructionsx, instructionsy, creditsx, creditsy,choice
    title = Title(screen, 150, 50)
    playx = 400
    playy = 230
    play = Play(screen, playx, playy)
    instructionsx = 350
    instructionsy = playy + 140
    instructions = Instructions(screen, instructionsx, instructionsy)
    creditsx = 400
    creditsy = instructionsy + 100
    credits = Credits(screen, creditsx,creditsy)
    menuobjects = [title,play,instructions,credits]
    clock = pygame.time.Clock()
    events = pygame.event.get()
    choice = 0
    while choice == 0:
        draw(screen, menuobjects)
        handle(events, menuobjects)
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mousepos = event.pos
                MouseClick(mousepos)
            if event.type == QUIT:
                exit()
        events = pygame.event.get()

    if choice == 'PLAY':
        pygame.mixer.music.load('Hidden Village.mp3')
        pygame.mixer.music.play(-1)
        alive = level(1)
        if alive:
            alive = level(2)
        if alive:
            alive = level(3)
        if alive:
            alive = level(4)
        if alive:
            pygame.mixer.music.stop()
            youwin()
        pygame.mixer.music.stop()
        endgame()
    if choice == 'INSTRUCTIONS':
        instruct()
        startpage(screen)
    if choice == 'CREDITS':
        showcredits()
        startpage(screen)

if __name__ == "__main__":
    startgame()