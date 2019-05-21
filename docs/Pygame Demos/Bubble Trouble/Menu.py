'''
Created on Jun 10, 2014

@author: burchtm
'''
import pygame
import sys
import Level

class Menu():
    '''
    classdocs
    '''

    #Sets up the menu and the music and click boxes assosiated with it.
    def __init__(self):
        '''
        Constructor
        '''
        self.controller = None
        self.size = self.width, self.heigh = 800,800
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.image.load('images/main_menu.gif')
        self.playRect = pygame.Rect((452,143),(232,232))
        self.quitRect = pygame.Rect((124,427),(232,232))
        self.clock = pygame.time.Clock()
        self.sonicFile = 'sounds/sonic theme.wav'
        self.setup()
        
        
    def playGame(self):
        pygame.joystick.init()
        if(pygame.joystick.get_count()!=0):
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
        while 1:
            self.selection = None
            if(pygame.joystick.get_count()!=0):   
                self.checkControllerMouseMovement()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                #Uses different events to get the selection of what level to play or to quit
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.checkClick() 
                if(pygame.joystick.get_count()!=0):
                    if event.type == pygame.JOYBUTTONDOWN and (self.controller.get_button(4)==True or self.controller.get_button(5)==True):
                        self.checkClick()
                    if(event.type==pygame.JOYBUTTONDOWN):
                        self.getControllerSelection()
                if (event.type == pygame.KEYDOWN):
                    self.getKeySelection(event)
                    
                #Uses the selection to tell the program to quit or play the game
                if(self.selection != None):
                    if(self.selection ==-1):
                        sys.exit()
                    else:
                        self.sonicTheme.stop()
                        self.play(self.selection)
                        
                #Controls the frame rate to 65 fps
                self.clock.tick(65)
    
    #Starts play at the given level and then returns the the main menu and resets the menu once play is over            
    def play(self, startingLevel):
        i = None
        for i in range(startingLevel, 6):
            level = Level.Level(i, self.screen)
            level.start()
            if(level.died==True):
                pygame.event.clear()
                break
        pygame.mixer.init()
        self.setup()

    #Sets up the menu screen
    def setup(self):
        self.sonicTheme = pygame.mixer.Sound(self.sonicFile)
        self.sonicTheme.play(-1)
        self.screen.blit(self.background,self.background.get_rect())
        pygame.display.flip()
        pygame.mouse.set_visible(True)
        
    #Checks if a click was on a spot that triggers play or quit
    def checkClick(self):
        self.pos = pygame.mouse.get_pos()
        if self.playRect.collidepoint(self.pos):
            self.selection =  1
        if self.quitRect.collidepoint(self.pos):
            self.selection =  -1   
            
    #Checks if the mouse is moved by the controller
    def checkControllerMouseMovement(self):
        x,y = pygame.mouse.get_pos()
        if(self.controller.get_axis(3) > .25 or self.controller.get_axis(3)<-.25 or self.controller.get_axis(4)>.25 or self.controller.get_axis(4)<-.25):
            pygame.mouse.set_pos(x+(self.controller.get_axis(4)*10),y+(self.controller.get_axis(3)*10))
            
    #Gets the selection based on controller buttons
    def getControllerSelection(self):
        if(self.controller.get_button(6)==True):
            self.selection =  -1
        if(self.controller.get_button(7)==True):
            self.selection =  1
        if(self.controller.get_button(0)==True):
            self.selection =  2
        if(self.controller.get_button(1)==True):
            self.selection =  3
        if(self.controller.get_button(2)==True):
            self.selection =  4
        if(self.controller.get_button(3)==True):
            self.selection =  5
            
    #Gets the selection based on keys pressed
    def getKeySelection(self,event):
        if (event.key == pygame.K_1):
            self.selection =  1
        if(event.key == pygame.K_2):
            self.selection =  2
        if (event.key == pygame.K_3):
            self.selection =  3
        if (event.key == pygame.K_4):
            self.selection =  4
        if (event.key == pygame.K_5):
            self.selection = 5