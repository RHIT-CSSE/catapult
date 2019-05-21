import pygame
from pygame.locals import *
from MainMenu import *
from Over import *

screen_width = 750
screen_height = 425
fps = 30

class Loser:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pass
    
class Background(Loser):
    def __init__(self, screen, x, y):
        Loser.__init__(self, screen, x, y)
        self.image = pygame.image.load("gameover.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

def init():
    pygame.init()
    pygame.mixer.music.load('Parker.wav')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode([screen_width,screen_height],0,32)
    return screen

def draw(screen, objects):
    screen.fill(pygame.Color('black'))
    for object in objects:
        object.draw()
    pygame.display.flip()

def endgame():
    screen = init()
    click = (0,0)
    running = True
    youlose = Background(screen, 0, 0)
    linkbox = pygame.Rect(521,283,116,32)
    exitbox = pygame.Rect(519,318,69,34)
    guys = [youlose]
    rect = pygame.Rect(750,475,214,99)
    clock = pygame.time.Clock()
    events = pygame.event.get()
    while running:
        draw(screen, guys)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
            if event.type == QUIT:
                exit()
        if linkbox.collidepoint((click[0],click[1])) or exitbox.collidepoint((click[0],click[1])):
            running = False
#        clock.tick(fps)
        events = pygame.event.get()
    if linkbox.collidepoint((click[0],click[1])):
        import MainMenu
        MainMenu.startgame()
    if exitbox.collidepoint((click[0],click[1])):
        exit()
    
if __name__ == "__main__":
    endgame()
