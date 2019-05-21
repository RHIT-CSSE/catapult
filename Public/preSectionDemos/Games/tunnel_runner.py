#Andrew Shiemke

#Tunnel Runner game

import pygame
import random



#colors
WHITE= [255, 255, 255]
BLACK= [0, 0, 0]
GREY= [128, 128, 128]

class Game:
    progress= 0
    hangTime=0
    speed=400

    def __init__(self):
        #create screen
        self.screenSize=[1000, 150]
        self.screen= pygame.display.set_mode(self.screenSize)
        self.backgroundColor= GREY
        #position of player and obstacles
        self.player= Sprite([0, 50], self.screen)
        self.obstacle = Obstacle(self.screen)
        
        self.clock= pygame.time.Clock()
        self.playing= True
        
        
    def Input(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                self.playing= False#quits game
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_DOWN:
                    self.player.duck()
                if event.key== pygame.K_UP:
                    self.player.jump()
                if event.key== pygame.K_p:
                    print ("Pause does not work")
                    
                    
                    
    def newScreen(self):
        Game.progress= 0
        self.obstacle = Obstacle(self.screen)
        Game.speed= Game.speed + 5
        print (Game.speed)
        
    def die(self): 
        print ("You Lost, but you managed to make it through "+ str (self.player.screens)+ " screens")
        self.playing = False   
                       
    def main(self):
        while self.playing:
            if self.hangTime <= 0:
                self.Input()
            self.screen.fill(self.backgroundColor)
            Game.progress= Game.progress+ 1
            self.player.position[0]= Game.progress
            if Game.hangTime== 1:
                self.player.run()
            Game.hangTime= Game.hangTime- 1
            self.player.rect.x = self.player.position[0]
            self.player.rect.y = self.player.position[1]
            self.player.draw()
            self.obstacle.draw()
            self.player.coll([self.obstacle])
            if self.player.lives== 0:
                self.die()
            pygame.display.update()
            if self.progress== 1000:
                self.newScreen()
                self.player.screens= self.player.screens+ 1
                
                
                
            self.clock.tick(self.speed)
            
        
class Sprite:
    def __init__(self, position, screen):
        self.position= position
        self.width=50
        self.hieght=100
        self.surface= pygame.Surface( (self.width, self.hieght) )
        #self.rect= self.surface.get_rect()
        self.person()
        self.rect= self.surface.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.screen= screen
        self.lives= 5
        self.screens=0
        
    def person(self):
        self.surface.fill(GREY)
        pygame.draw.circle(self.surface, BLACK, ( 25, 15), 15)
        
        pygame.draw.rect(self.surface, BLACK, (0, 29, 50, 80))
# x y width height
    def draw(self):
        self.screen.blit(self.surface, self.position)
        
    def jump(self):
        self.position=[Game.progress, -30]
        self.screen.fill(GREY)
        self.draw()
        pygame.display.update()
        Game.hangTime= 150
        
        
    def duck(self):
        self.position=[Game.progress, 100]
        self.screen.fill(GREY)
        self.draw()
        pygame.display.update()
        Game.hangTime= 150
        
        
    def run(self):
        self.position=[Game.progress, 50]
        self.screen.fill(GREY)
        #self.rect.x = self.position[0]
        #self.rect.y = self.position[1]
        #print(self.position)
        self.draw()
        pygame.display.update()
        
    def update(self):
        pass
    
    def coll(self, listStuff):
        for thing in listStuff:
            if self.rect.colliderect(thing.rect):
                self.lives= self.lives-1
                Game.progress= 0
                Game.hangTime
                print ("You have "+ str (self.lives)+ " lives remaining")
        
        
class Obstacle:
    def __init__(self, screen):
        
        self.vert= random.randrange(0, 2)
        self.vert=self.vert* 75
        self.position= [random.randrange(300, 800), self.vert]
        self.hieght= 75
        self.width= 50
        self.surface= pygame.Surface( (self.width, self.hieght) )
        self.rect= self.surface.get_rect()
        
        self.surface.fill(WHITE)
        self.screen= screen
        #self.rect= self.screen.get_rect()
        self.rect.x= self.position[0]
        self.rect.y= self.position[1]
        
    def draw(self):
        self.screen.blit(self.surface, self.position)
    
        

game = Game()
game.main()
