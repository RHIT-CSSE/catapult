'''
Created on Jun 9, 2014

@author: burchtm
'''

import pygame
from Bubble import *

class CoolGuy():
    '''
    classdocs
    '''

    #Initializes the CoolGuy player. Uses the Bubble's load_image function to load the image and the scales the picture and draws him to the scren
    def __init__(self, screen, x, y):
        '''
        Constructor
        '''
        self.coolGuy = Bubble.load_image(self, "images/bubbleGuy.png", -1)
        self.coolGuy = pygame.transform.scale(self.coolGuy, (40, 75))
        self.screen = screen
        self.x = x
        self.y = y
        self.screen.blit(self.coolGuy,(self.x,self.y))
    
        