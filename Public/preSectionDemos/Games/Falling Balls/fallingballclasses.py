import pygame
from pygame.locals import *
import math
from random import randint

def distance (point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
class Mover:
    def __init__(self,height,width):
        self.rect = Rect(150,0,20,20)
        self.xvel, self.yvel = 0,0
        self.ball = pygame.image.load("ball.png")
        self.ball = pygame.transform.scale(self.ball, (20,20))
        
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.rect.center,self.rect.width/2)
             
    def draw_special(self,surface):
        surface.blit(self.ball, self.rect.topleft)

    def move(self,dx,dy):
        self.rect = self.rect.move(dx,dy)
    def relocate(self,pos):
        self.rect.topleft = pos

    def set_vel(self,newxvel,newyvel):
        self.xvel, self.yvel = newxvel,newyvel
    def set_xvel(self,newxvel):
        self.xvel = newxvel
    def set_yvel(self, newyvel):
        self.yvel = newyvel
    def move_self(self):
        self.rect = self.rect.move(self.xvel,self.yvel)
    def acc_ball(self, newyvel):
        newyvel = newyvel + 1
        pygame.time.wait(3)
        
class platform:
    
    def __init__ (self,yvel):
        a = randint(0,260)
        self.rect = Rect(a,600,50,20)
        self.plat = pygame.image.load("plat.png")
        self.plat = pygame.transform.scale(self.plat, (50,10))
        self.yvel = yvel
        self.xvel = 0
     
    def draw(self,surface):
        pygame.draw.rect(surface,self.rect.center,self.rect.width/2)

    def draw_special(self, surface):
        surface.blit(self.plat, self.rect.topleft)

    def move_self(self):
        self.rect = self.rect.move(self.xvel,self.yvel)
    
    def set_vel(self,newxvel,newyvel):
        self.xvel, self.yvel = newxvel,newyvel
        
    def relocate(self, pos):
        self.rect.center = pos
        
    def moveself(self):
        self.rect = self.rect.move(0, self.yvel)
    
    def accelerate(self, newyvel):
        newyvel = newyvel + 1

class heart:
    
    def __init__ (self,rect,yvel):
        self.rect = rect.move(0,-30)
        self.plat = pygame.image.load("heart.png")
        self.plat = pygame.transform.scale(self.plat, (30,30))
        self.yvel = yvel
        self.xvel = 0
     
    def draw(self,surface):
        pygame.draw.rect(surface,self.rect.center,self.rect.width/2)

    def draw_special(self, surface):
        surface.blit(self.plat, self.rect.topleft)
    
    def move_self(self):
        self.rect = self.rect.move(self.xvel,self.yvel)
    
    def set_vel(self,newxvel,newyvel):
        self.xvel, self.yvel = newxvel,newyvel

class Spike:
    def __init__ (self,yvel):
        a = randint(0,260)
        self.rect = Rect(a,600,40,20)
        self.spike = pygame.image.load("spike.png")
        self.spike = pygame.transform.scale(self.spike, (50,10))
        self.yvel = yvel
        self.xvel = 0
     
    def draw(self,surface):
        pygame.draw.rect(surface,self.rect.center,self.rect.width/2)
        
    def draw_special(self, surface):
        surface.blit(self.spike, self.rect.topleft)

    def move_self(self):
        self.rect = self.rect.move(self.xvel,self.yvel)
    
    def set_vel(self,newxvel,newyvel):
        self.xvel, self.yvel = newxvel,newyvel

    def relocate(self, pos):
        self.rect.center = pos
        
    def moveself(self):
        self.rect = self.rect.move(0, self.yvel)

class Star:
    def __init__ (self,rect,yvel):
        self.rect = rect.move(0,-30)
        self.plat = pygame.image.load("star.png")
        self.plat = pygame.transform.scale(self.plat, (30,30))
        self.yvel = yvel
        self.xvel = 0
     
    def draw(self,surface):
        pygame.draw.rect(surface,self.rect.center,self.rect.width/2)

    def draw_special(self, surface):
        surface.blit(self.plat, self.rect.topleft)
    
    def move_self(self):
        self.rect = self.rect.move(self.xvel,self.yvel)
    
    def set_vel(self,newxvel,newyvel):
        self.xvel, self.yvel = newxvel,newyvel
        

        
