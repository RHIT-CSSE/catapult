'''
Created on Jun 9, 2014

@author: burchtm
'''
import pygame
import math

class Bubble():
    '''
    classdocs
    '''

    #Initializes a new Bubble object with the given screen, location, and size
    def __init__(self, screen, location, size):
        '''
        Constructor
        '''
        #Sets the basic information for the new Bubble
        self.size = size
        self.radius = 15*size
        self.screen = screen
        self.x = location[0]
        self.y = location[1]
        self.vx = 5
        
        #Uses the Bubble's size to set its velocity. Also has a velocity cap based on it size or a size 4 bubble if it is bigger than that
        self.vy = 2.5*size
        self.ay = .25
        self.cap = 2.5*max(9-size, 4)
        if (self.vy > self.cap):
            self.vy = self.cap
            
        #Loads the image, sets the transparency of the immage, and scales the bubble to the correct size    
        self.bubble = self.load_image("images/bubble.gif", -1)
        self.bubble.set_alpha(140)
        self.bubble = pygame.transform.scale(self.bubble, (self.radius*2,self.radius*2))
        self.draw()
        
    #Draws the Bubble on the screen at its current x and y coordinates
    def draw(self):
        self.screen.blit(self.bubble, (self.x,self.y))
        
    #Updates the current position of the Bubble on the screen
    def increment(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.ay
        if (math.fabs(self.vy) > self.cap):
            self.vy = self.vy/self.vy * self.cap
        
    #Splits the buble into two new Bubble's that are one size smaller. One moves to the right and one moves to the left.   
    def split(self):
        bubble1 = Bubble(self.screen, (self.x, self.y), int(self.size-1))
        bubble2 = Bubble(self.screen, (self.x, self.y), int(self.size-1))
        bubble2.vx = -bubble2.vx
        bubble2.vy = -math.fabs(bubble2.vy)
        bubble1.vy = -math.fabs(bubble1.vy)
        return (bubble1, bubble2)
    
    #Loads the image for the Bubble and makes any changes necessary for transparency to work.
    def load_image(self, name, colorkey=None):
        try:
            image = pygame.image.load(name)
        except pygame.error:
            print ('Cannot load image:', name)
            raise SystemExit
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCELOK)
        return image
