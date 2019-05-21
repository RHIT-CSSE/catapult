'''
Created on Jun 10, 2014

@author: fahslaj
'''
import pygame
from Cool_Guy import *
from Bubble import *
from The_Spear import *
import Bubble_Trouble
import sys

class Level():
        
    
    '''
    classdocs
    '''
    
    #Initializes the level class
    def __init__(self, num, screen):
        '''
        Constructor
        '''
        self.screen = screen
        self.levelNum = num
        self.initialize()
        
    #Initializes gameplay. Creates a clock to uses and turns off the visability of the cursor
    def initialize(self):
        pygame.mixer.init()
        self.loadMusic()
        self.clock = pygame.time.Clock()
        self.easy = False
        self.died = False
        pygame.time.delay(1000)
        self.controller = None
        self.width, self.height = 800,800
        pygame.mouse.set_visible(False)

    #Loads all sounds that will be used during gameplay and starts the main music for gameplay
    def loadMusic(self):
        self.theme = pygame.mixer.Sound('sounds/mario theme.wav')
        self.gong = pygame.mixer.Sound('sounds/gong.wav')
        self.pew = pygame.mixer.Sound('sounds/pew.wav')
        self.deathSound = pygame.mixer.Sound('sounds/mario death.wav')
        self.stageClear = pygame.mixer.Sound('sounds/mario stage clear.wav')
        self.worldClear = pygame.mixer.Sound('sounds/mario world clear.wav')
        self.theme.play(-1)
    
    #Starts the correct level based on the pased in level num    
    def start(self):
        if (self.levelNum == 1):
            self.level1()
        elif (self.levelNum == 2):
            self.level2()
        elif (self.levelNum == 3):
            self.level3()
        elif (self.levelNum == 4):
            self.level4()
        elif (self.levelNum == 5):
            self.level5()
        self.checkState()
    
    #Checks to see if the level was exited due to death or due to winning and triggers the correct response.
    def checkState(self):
        self.theme.stop()
        if(self.died==False):
            if(self.levelNum!=5):
                self.levelWin()
            else:
                self.gameWin()
    
    #Shows the level clear screen and plays the winning music.
    def levelWin(self):
        winningScreen = pygame.image.load('images/level_up.gif')
        self.screen.blit(winningScreen,(0,0))
        pygame.display.flip()
        self.stageClear.play(0)
        pygame.time.delay(6000)
    
    #Shows the game clear screen, plays the winning music, and then triggers the overall win movie.            
    def gameWin(self):
        overallWinningScreen = pygame.image.load('images/winning_screen.gif')
        self.screen.blit(overallWinningScreen, (0,0))
        pygame.display.flip()
        self.worldClear.play(0)
        pygame.time.delay(6000)
        self.playMovie()            
    
    #The main event loop for every level that controls all movement and events that happen
    def mainLoop(self):
        self.movement = 0
        self.spear = None
        pygame.joystick.init()
        if(pygame.joystick.get_count()!=0):
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
        pygame.event.clear()
        self.died = False
        while self.died ==False:
            self.checkKeyMovement()      
            for event in pygame.event.get():
                self.checkPauseAndQuit(event)          
                self.checkKeyHax(event)
                self.checkPop(event)         
                if(self.controller!=None):
                    self.controllerMouseMovement(self.controller)
                    self.checkcontrollerMovement()
                    self.checkControllerSpear()
                    self.checkControllerPauseAndQuit(event)
                    self.checkControllerPop(event)
                    self.checkcontrollerHax(event, self.controller)
            self.spearMovement()       
            
            #Redraws the background for the level    
            self.screen.fill((204,204,204))
            self.screen.blit(self.scaledbgi, (0,0))
            
            self.guyMovement()
            
            #Draws the spear if there is one   
            if(self.spear!=None):
                self.spear.draw()
            
            #Draws the guy on the screen    
            self.screen.blit(self.guy.coolGuy, (self.guy.x,self.guy.y))
            
            #Loops through the bubbles and updates the bubble's coordinates and the guy's coordinates
            for bubble in self.bubbles:
                self.updateBubble(bubble, self.height, self.width)
                bubbleRect = pygame.Rect((bubble.x,bubble.y),(bubble.radius*2,bubble.radius*2))
                guyRect = pygame.Rect((self.guy.x,self.guy.y),(50,100))
                
                #Checks for death of player
                if(guyRect.colliderect(bubbleRect)):
                    self.death()
                    break
                
                #Checks to see if the spear hit any bubbles and pops them if it did
                if(self.spear != None):
                    spearRect = pygame.Rect((self.spear.x, self.spear.y), (40, 800))
                    if (spearRect.colliderect(bubbleRect)):
                        self.pop(self.bubbles, bubble)
                        if (not self.easy):
                            self.spear = None
            
            #Checks if all the bubble have been popped and if they have ends the level
            if not self.bubbles:
                break
            
            #Updates the screen and sets the frames per second to 65
            pygame.display.update()
            self.clock.tick(65)
            
    #Triggers the death music and game over screen
    def death(self):
        self.died = True
        self.theme.stop()
        soundChannel = self.deathSound.play(0)
        soundChannel.queue(self.gong)
        self.gameOver(self.screen)
    
    #Moves the player
    def guyMovement(self):
        self.guy.x = self.guy.x + self.movement
        if(self.guy.x+50<0):
            self.guy.x = self.width
        elif(self.guy.x>self.width):
            self.guy.x = -50
                        
    #Moves the spear if there is one
    def spearMovement(self):
        if(self.spear!=None):
            self.spear.y += self.spear.vy
        if(self.spear !=None and self.spear.y<=0):
            self.spear = None
    
    #Checks to see if a bubble is being popped using the controller
    def checkControllerPop(self,event):
        if (event.type == pygame.JOYBUTTONDOWN and (self.controller.get_button(4)==True or self.controller.get_button(5)==True)):
            for b in self.bubbles:
                rect = pygame.Rect((b.x,b.y),(b.radius*2,b.radius*2))
                if (rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                    self.pop(self.bubbles, b)
                                
            
    #Checks if the controller is pausing or quiting the game
    def checkControllerPauseAndQuit(self,event):
        if (event.type == pygame.JOYBUTTONDOWN) and (self.controller.get_button(6)==True):
            sys.exit()
        if (event.type == pygame.JOYBUTTONDOWN) and (self.controller.get_button(7)==True):
            pygame.mixer.pause()
            paused = True
            while (paused):
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()
                    if (e.type == pygame.JOYBUTTONDOWN) and (self.controller.get_button(7)==True):
                        paused = False
            pygame.mixer.unpause()
            
    #Checks if a spear is to be send and sends one if so using the controller
    def checkControllerSpear(self):
        if((self.controller.get_axis(2)>.5)|(self.controller.get_axis(2)<-.5)):
            if(self.spear==None):
                self.pew.play(1)
                self.spear = The_Spear(self.screen, self.guy)
            
    #Moves the player using the self.controller
    def checkcontrollerMovement(self,event):
        if((event.type == pygame.JOYAXISMOTION) & (self.controller.get_axis(0)<-.5)):
            self.movement = self.controller.get_axis(0)*5
        if((event.type == pygame.JOYAXISMOTION) & (self.controller.get_axis(0)>.5)):
            self.movement = self.controller.get_axis(0)*5
        if((event.type == pygame.JOYAXISMOTION) & (self.controller.get_axis(0)>-.5) & (self.controller.get_axis(0)<.5)):
            self.movement = 0  
    
    #Moves the mouse using the self.controller
    def controllerMouseMovement(self):
        x,y = pygame.mouse.get_pos()
        if(self.controller.get_axis(3) > .25 or self.controller.get_axis(3)<-.25 or self.controller.get_axis(4)>.25 or self.controller.get_axis(4)<-.25):
            pygame.mouse.set_pos(x+(self.controller.get_axis(4)*5),y+(self.controller.get_axis(3)*5))       
            
    #Checks whether or not the hax are turned on or off using a self.controller
    def checkControllerHax(self,event):
        if (event.type == pygame.JOYHATMOTION and self.controller.get_hat(0) == (-1,0)):
            pygame.mouse.set_visible(True)
        if (event.type == pygame.JOYHATMOTION and self.controller.get_hat(0) == (1,0)):
            pygame.mouse.set_visible(False)
        if (event.type == pygame.JOYHATMOTION and self.controller.get_hat(0) == (0,-1)):
            self.bubbles = []
        if (event.type == pygame.JOYHATMOTION and self.controller.get_hat(0) == (0,1)):
            self.easy = True
    #Checks to see if a Bubble is being popped or not
    def checkPop(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("detected: "+str(pygame.mouse.get_pos()))
            for b in self.bubbles:
                rect = pygame.Rect((b.x,b.y),(b.radius*2,b.radius*2))
                if (rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                    self.pop(self.bubbles, b)
    
    #Checks whether or not the hax are turned on or off using keys
    def checkKeyHax(self,event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_c):
            pygame.mouse.set_visible(True)
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_v):
            pygame.mouse.set_visible(False)
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS):
            self.bubbles = []
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
            self.easy = True
    
    #Checks Movement Based on Key Presses 
    def checkKeyMovement(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            self.movement = 5
        if (keys[pygame.K_LEFT]):
            self.movement = - 5
        if(not keys[pygame.K_RIGHT]and not keys[pygame.K_LEFT] and pygame.joystick.get_count()==0):
            self.movement = 0        
        if (keys[pygame.K_SPACE]):
            if(self.spear==None):
                self.pew.play(1)
                self.spear = The_Spear(self.screen, self.guy)
        if(not keys[pygame.K_RIGHT]and not keys[pygame.K_LEFT] and pygame.joystick.get_count()==1 and self.controller.get_axis(0)>-.5 and self.controller.get_axis(0)<.5):
            self.movement = 0    
    
    #Checks if the game is being paused using the p key or being quit using the q key or the x
    def checkPauseAndQuit(self, event):
        if event.type == pygame.QUIT:
                    exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit()
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_p):
            pygame.mixer.pause()
            paused = True
            while (paused):
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()
                    if (e.type == pygame.KEYDOWN and event.key == pygame.K_p):
                        paused = False
            pygame.mixer.unpause()
     
    #Plays the overall winning movie.                
    def playMovie(self):
        pygame.mixer.quit()
        movie = pygame.movie.Movie("images/winning_final.mpg")
        movie.set_display(self.screen, self.screen.get_rect())
        movie.play()
        while(movie.get_busy()==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
   
    #Sets up the bubbles and background for Level 1 then triggers the mainLoop   
    def level1(self):
        self.guy = CoolGuy(self.screen, 0, 725)
        self.bubbles = [(Bubble(self.screen, (300, 250), 2)), 
                        (Bubble(self.screen, (400, 250), 1))]
        backgroundImage = pygame.image.load("images/bubblebackground01.jpg").convert()
        backgroundImage.set_alpha(140)
        self.scaledbgi = pygame.transform.scale(backgroundImage, (800, 800))
        self.mainLoop()
    
    #Sets up the bubbles and background for Level 2 then triggers the mainLoop
    def level2(self):
        self.guy = CoolGuy(self.screen, 0, 725)
        self.bubbles = [(Bubble(self.screen, (500, 450), 3))]
        backgroundImage = pygame.image.load("images/bubblebackground02.jpg").convert()
        backgroundImage.set_alpha(140)
        self.scaledbgi = pygame.transform.scale(backgroundImage, (800, 800))
        self.mainLoop()

    #Sets up the bubbles and background for Level 3 then triggers the mainLoop
    def level3(self):
        self.guy = CoolGuy(self.screen, 0, 725)
        self.bubbles = [(Bubble(self.screen, (100, 650), 1)),
                        (Bubble(self.screen, (300, 650), 1)),
                        (Bubble(self.screen, (500, 650), 1)),
                        (Bubble(self.screen, (700, 650), 1)),
                        (Bubble(self.screen, (200, 450), 2)),
                        (Bubble(self.screen, (400, 450), 2)),
                        (Bubble(self.screen, (600, 450), 2)),]
        backgroundImage = pygame.image.load("images/bubblebackground03.jpg").convert()
        backgroundImage.set_alpha(140)
        self.scaledbgi = pygame.transform.scale(backgroundImage, (800, 800))
        self.mainLoop()
        
    #Sets up the bubbles and background for Level 4 then triggers the mainLoop   
    def level4(self):
        self.guy = CoolGuy(self.screen, 0, 725)
        self.bubbles = [(Bubble(self.screen, (600, 600), 4)),
                        (Bubble(self.screen, (400, 400), 2)),
                        (Bubble(self.screen, (200, 200), 3))]
        backgroundImage = pygame.image.load("images/bubblebackground04.jpg").convert()
        backgroundImage.set_alpha(140)
        self.scaledbgi = pygame.transform.scale(backgroundImage, (800, 800))
        self.mainLoop()
        
    #Sets up the bubbles and background for Level 5 then triggers the mainLoop
    def level5(self):
        self.guy = CoolGuy(self.screen, 0, 725)
        self.bubbles = [(Bubble(self.screen, (500, 150), 6))]
        backgroundImage = pygame.image.load("images/bubblebackground05.jpg").convert()
        backgroundImage.set_alpha(140)
        self.scaledbgi = pygame.transform.scale(backgroundImage, (800, 800))
        self.mainLoop()
    
    #Updates the given bubble, checks if it is going off the screen, and then draws the bubble at its current position
    def updateBubble(self, bubble, height, width):
        bubble.increment()
        if (bubble.x+(bubble.radius*2) >= width or bubble.x <= 0):
            bubble.vx = -bubble.vx
        if (bubble.y+(bubble.radius*2) >= height or bubble.y <= 0):
            bubble.vy = -bubble.vy
        bubble.draw()
    
    #Pops the current Bubble and then calls Bubble's split method to make to more and appends them to the list of Bubbles        
    def pop(self, bubbles, bubble):
        bubbles.remove(bubble)
        if (bubble.size > 1):
            splits = bubble.split()
            bubbles.append(splits[0])
            bubbles.append(splits[1])
    
    #Shows the Game Over Screen        
    def gameOver(self, screen):
        gameOverScreen = pygame.image.load("images/game_over.png")
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            screen.blit(gameOverScreen,(0,0))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        
        
    

        