import pygame
class BlockGeneration(object):
    '''
    Generates and reads a tilemap
    '''
   

    def __init__(self, x, y,style):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.win = None
        self.style = style
        if(self.style==1):
            self.top=True
            self.left=False
            self.right=False
            self.bottom = False
        elif(self.style==2):
            self.top = False
            self.left = True
            self.right = True
            self.bottom = False
        elif(self.style==3):
            self.left = True
            self.right = False
            self.top=True
            self.bottom = True
        elif(self.style==4):
            self.left = False
            self.right = True
            self.top=True
            self.bottom = True
        elif(self.style==5):
            self.left=True
            self.right = True
            self.top = True
            self.bottom = False
        elif(self.style==6):
            self.top=False
            self.left=False
            self.right=False
            self.bottom = True
        elif(self.style==7):
            self.top=True
            self.left=False
            self.right=False
            self.bottom = True
        elif(self.style==8):
            self.win=True
        
    def render(self, window):
        if self.style == 8:
            self.block = pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.width, self.height))  
        else:
            self.block = pygame.draw.rect(window, (71,94,245), (self.x, self.y, self.width, self.height))
    
        
        