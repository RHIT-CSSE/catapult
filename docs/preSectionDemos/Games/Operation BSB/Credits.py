import pygame
from pygame.locals import *

screen_width = 1000
screen_height = 600
fps = 30

class Credits:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pass

class Background(Credits):
    def __init__(self, screen, x, y):
        Credits.__init__(self, screen, x, y)
        self.image = pygame.image.load("creditspic.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class MainMenuLink(Credits):
    def __init__(self, screen, x, y):
        Credits.__init__(self, screen, x, y)
        self.image = pygame.image.load("mainmenulink.png")
        self.x_speed = 0
        self.y_speed = 0     
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

def init():
    pygame.init()
    screen = pygame.display.set_mode([screen_width,screen_height],0,32)
    return screen

def draw(screen, objects):
    screen.fill(pygame.Color('black'))
    for object in objects:
        object.draw()
    pygame.display.flip()

def showcredits():
    screen = init()
    click = (0,0)
    running = True
    credits = Background(screen, 0, 0)
    link = MainMenuLink(screen, 750, 475)
    guys = [credits, link]
    rect = pygame.Rect(750,475,214,99)
    clock = pygame.time.Clock()
    events = pygame.event.get()
    while running:
        draw(screen, guys)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    running = False
            if event.type == QUIT:
                exit()
        if rect.collidepoint((click[0],click[1])):
            running = False
#        clock.tick(fps)
        events = pygame.event.get()
if __name__ == "__main__":
    showcredits()
