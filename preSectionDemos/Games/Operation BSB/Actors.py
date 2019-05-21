import pygame
from pygame.locals import *

class Actor:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    
    def act(self):
        pass
    
    def draw(self):
        pass
    
    def handle(self, event):
        pass

class Player(Actor):
    def __init__(self, screen, x, y):
        Actor.__init__(self, screen, x, y)
        self.image1 = pygame.image.load("Player01.png").convert_alpha()
        self.image2 = pygame.image.load("player02.png").convert_alpha()
        self.image3 = pygame.image.load("player03.png").convert_alpha()
        self.image4 = pygame.image.load("player04.png").convert_alpha()
        self.image2b = pygame.image.load("player02b.png").convert_alpha()
        self.image3b = pygame.image.load("player03b.png").convert_alpha()
        self.image4b = pygame.image.load("player04b.png").convert_alpha()
        self.image = self.image1
        self.x_speed = 0
        self.y_speed = 0
        self.i = 0
        self.moving = False
    
    def act(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.playerrect = pygame.Rect(self.x,self.y,73,196)
        if self.moving and self.x_speed > 0:
            if self.i < 5:
                self.image = self.image2
            elif self.i < 10:
                self.image = self.image3    
            elif self.i < 15:
                self.image = self.image4
            self.i += 1
            if self.i == 16:
                self.i = 0
        elif self.moving and self.x_speed < 0:
            if self.i < 5:
                self.image = self.image2b
            elif self.i < 10:
                self.image = self.image3b   
            elif self.i < 15:
                self.image = self.image4b
            self.i += 1
            if self.i == 16:
                self.i = 0
  
        else:
            self.image = self.image1

    def handle(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.x_speed = -10
            elif event.key == K_RIGHT:
                self.x_speed = 10
            self.moving = True
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.x_speed = 0
            self.moving = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
#        self.screen.blit(self.images[self.cur_image_index], (self.x, self.y))

class Counselor(Actor):
    def __init__(self, screen, x, y):
        Actor.__init__(self, screen, x, y)
        self.image = pygame.image.load("counselorsight.png").convert_alpha()
        self.x_speed = 0
        self.y_speed = 0   
        self.m = 0
        self.counselorrect = None

    def act(self):
        if self.m == 400:
            self.m = 0
            self.image = pygame.image.load("counselorsight.png").convert_alpha()
        if self.m > 0:
            self.x_speed = 2
            self.counselorrect = pygame.Rect(self.x+self.x_speed+54,self.y,137,200)
        if self.m > 150:
            self.image = pygame.image.load("counselor.png").convert_alpha()
            self.x_speed = 0
            self.counselorrect = None
        if self.m > 175:
            self.image = pygame.image.load("counselorreverse.png").convert_alpha()
        if self.m == 200:
            self.x -= 137
            self.image = pygame.image.load("counselorsightreverse.png").convert_alpha()
            self.counselorrect = pygame.Rect(self.x,self.y,137,200)
        if self.m > 200:
            self.image = pygame.image.load("counselorsightreverse.png").convert_alpha()
            self.x_speed = -2
            self.counselorrect = pygame.Rect(self.x-10*self.x_speed,self.y,137,200)
        if self.m == 351:
            self.x += 137
        if self.m > 350:
            self.image = pygame.image.load("counselorreverse.png").convert_alpha()
            self.x_speed = 0
            self.counselorrect = None
        if self.m > 375:
            self.image = pygame.image.load("counselor.png").convert_alpha()
        self.m +=1
        self.x += self.x_speed
        self.y += self.y_speed
    
    def sees(self, player):
        if self.counselorrect != None:
            if player.playerrect.colliderect(self.counselorrect):
                return True
        return False
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))