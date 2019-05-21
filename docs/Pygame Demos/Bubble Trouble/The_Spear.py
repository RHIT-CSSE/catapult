'''
Created on Jun 9, 2014

@author: burchtm
'''

from Cool_Guy import *

class The_Spear():
    '''
    classdocs
    '''

    #Sets up the spear with its initial coordinates
    def __init__(self, screen, Cool_Guy):
        '''
        Constructor
        '''
        
        self.screen = screen
        self.guy = Cool_Guy
        self.spear = pygame.image.load("images/The Spear.gif")
        self.vy = -8
        self.x = self.guy.x + 5
        self.y = self.guy.y
        self.draw()
    
    #Draws the spear onto the screen at its current coordinates    
    def draw(self):
        self.screen.blit(self.spear, (self.x,self.y))