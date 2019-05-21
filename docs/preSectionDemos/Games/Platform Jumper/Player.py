import pygame
from pygame.locals import *
from BlockGeneration import *

class Player(object):
    '''
    This is the character that the player controls
    '''


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 25
        self.width = 50
        self.height = 80
        self.velocity = 0
        self.isFalling = True
        self.onGround = False
        self.starting = True
        self.player = pygame.image.load('player.png')
        self.movingRight = True
        self.movingLeft = True
        self.winCondition = False
        
    def update(self, gravity, blockList, player):
        if(self.starting):
            self.starting = False
        elif self.velocity == 0:
            self.isFalling = False
            
        self.collision = False
        
        blockX = 0
        blockY = 0
        
        for block in blockList:
            self.collided = player.colliderect(block.block)
            if(self.collided):
                self.collisionDown = self.detectCollisionsDown(player, block)
                self.collisionSideways=self.detectCollisionsSideways(player, block)
                if self.collisionDown == 1 or self.collisionDown == 2 or self.collisionSideways == 3 or self.collisionSideways == 4 or self.collisionDown==5:
                    blockX = block.x
                    blockY = block.y
                    break
        
        
        if(self.collided):
            if self.collisionDown == 1:
                
                if self.isFalling:
                    self.isFalling = False
                    self.onGround = True
                    self.y = blockY - self.height+1
                    self.velocity = 0                   
            
            elif self.collisionDown == 2:
                if self.isFalling:
                    self.isFalling = True
                    self.onGround = False
                    #self.y = blockY - self.height+1
                    self.velocity = -3
                    
            elif self.collisionDown == 5:
                if self.isFalling:
                    self.isFalling = False
                    self.onGround = True
                    self.y = blockY - self.height+1
                    self.velocity = 0
                    self.winCondition = True  
                    
            if self.collisionSideways == 3:
                self.movingRight=False
                self.x=block.x-self.width-1
            else:
                self.movingRight=True
            if self.collisionSideways == 4:
                self.movingLeft=False
                self.x=(block.x+block.width+1)
            else:
                self.movingLeft=True
    
        else: 
            self.onGround=False
            self.isFalling=True
                
                
                
        if self.onGround == False:
            self.velocity += gravity
        self.y -= self.velocity
        
    def render(self, window):  
        window.blit(self.player, (self.x, self.y))
   
    def detectCollisionsDown(self, player, block):
        
        for i in range(block.x, (block.x + block.width)):
            collideBottom = player.collidepoint(i, block.y)
            collideTop = player.collidepoint(i, (block.y + block.height))
            if(block.win==True):
                return 5
            if(block.top==True):
                if collideBottom == True:
                    return 1
            if(block.bottom==True):
                if collideTop == True:
                    return 2
        return 3
     
    def detectCollisionsSideways(self,player,block):     
        for j in range(block.y+5, (block.y + block.height-5)):
            collideRight = player.collidepoint(block.x, j)
            collideLeft = player.collidepoint((block.x+block.width), j)
            if(block.left):
                if collideRight == True:
                    return 3
            else:
                self.movingRight=True
            
            if(block.right):        
                if collideLeft == True:
                    return 4
            else:
                self.movingLeft=True
        return 5
        '''
        if (player.colliderect(block.block)):
            return True
        else: 
            return False
        '''
       
    def moveRight(self):
        if self.movingRight:
            self.x += 10
        else:
            self.x +=0
    
    def moveLeft(self):
        
        if self.movingLeft:
            self.x -= 10
        else:
            self.x -= 0
           
    def jump(self):
        if self.onGround == False:
            return
        self.velocity = 15
        self.onGround = False       
       

        
        
            
    
        
        

    