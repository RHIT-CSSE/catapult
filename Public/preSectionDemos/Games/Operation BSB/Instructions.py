import pygame
from pygame.locals import *

screen_width = 1000
screen_height = 600
fps = 30

class Instructions:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pass

class Background(Instructions):
    def __init__(self, screen, x, y):
        Instructions.__init__(self, screen, x, y)
        self.image = pygame.image.load("int.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class Background2(Instructions):
    def __init__(self, screen, x, y):
        Instructions.__init__(self, screen, x, y)
        self.image = pygame.image.load("int 2.png")
        self.x_speed = 0
        self.y_speed = 0     
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class Background3(Instructions):
    def __init__(self, screen, x, y):
        Instructions.__init__(self, screen, x, y)
        self.image = pygame.image.load("int3.png")
        self.x_speed = 0
        self.y_speed = 0     
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class MainMenuLink(Instructions):
    def __init__(self, screen, x, y):
        Instructions.__init__(self, screen, x, y)
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

def instruct():
    screen = init()
    click = (0,0)
    running = 0
    credits = Background(screen, 0, 0)
    credits2 = Background2(screen, 0, 0)
    credits3 = Background3(screen, 0, 0)
    link = MainMenuLink(screen, 750, 490)
    guys = [credits]
    rect = pygame.Rect(750,475,214,99)
    clock = pygame.time.Clock()
    events = pygame.event.get()
    while running < 3:
        draw(screen, guys)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    click = (755,480)
            if event.type == QUIT:
                exit()
        if rect.collidepoint((click[0],click[1])):
            running += 1
            click = (0,0)
            if running == 1:
                guys = [credits2]
            if running == 2:
                guys = [credits3, link]
        clock.tick(fps)
        events = pygame.event.get()
if __name__ == "__main__":
    instruct()
