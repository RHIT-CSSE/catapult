import pygame
from pygame.locals import *
import MainMenu

screen_width = 750
screen_height = 425
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
        self.image = pygame.image.load("Congrats.png")
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

def init():
    pygame.init()
    pygame.mixer.music.load('FF7.wav')
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode([screen_width,screen_height],0,32)
    return screen

def draw(screen, objects):
    for object in objects:
        object.draw()
    pygame.display.flip()

def youwin():
    screen = init()
    running = True
    congratulations = Background(screen, 0, 0)
    guys = [congratulations]
    clock = pygame.time.Clock()
    events = pygame.event.get()
    draw(screen, guys)
    running = True
    while running:
        for event in events:
            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                running = False
            if event.type == QUIT:
                exit()
        clock.tick(fps)
#        pygame.time.delay(2500)
        events = pygame.event.get()
    pygame.mixer.music.stop()
    MainMenu.startgame()

if __name__ == "__main__":
    youwin()
