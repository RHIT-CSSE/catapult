import pygame
from pygame.locals import *
from random import randint
from time import sleep


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CHARACTER_OFFSET = 50
CHARACTER_SPEED = 7
BLAST_SPEED = 10


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Rainfall")
clock = pygame.time.Clock()
killGame = False


def overlap(r1,r2):
    '''Overlapping rectangles overlap both horizontally & vertically
    '''
    hoverlaps = False
    voverlaps = False
    if (r1.left <= r2.left and r1.left + r1.width > r2.left):
        hoverlaps = True
    elif(r2.left <= r1.left and r2.left + r2.width > r1.left):
        hoverlaps = True
    if (r1.top <= r2.top and r1.top + r1.height > r2.top):
        voverlaps = True
    elif(r2.top <= r1.top and r2.top + r2.height > r1.top):
        voverlaps = True
    if hoverlaps == True and voverlaps == True:
        return True
    else:
        return False
    



def eventLoop():
    character = Character(SCREEN_WIDTH/2 - Character.WIDTH/2, SCREEN_HEIGHT - CHARACTER_OFFSET)
    enemies = []
    blasts = []
    for k in range (20):
        x = Enemy(Enemy.WIDTH*k, 22)
        enemies.append(x) 
    vx = 0
    vy = 0
    lives = 3
    score = 0
    selected = False
    pygame.draw.rect(screen, BLACK, [0,0, SCREEN_WIDTH, SCREEN_HEIGHT], 0)
    message = '       Select a difficulty! (1-5)'.format(str(score), str(lives)) 
    font = pygame.font.SysFont("Impact", 50, bold=False, italic=False)
    scoreText = font.render(message, True, WHITE)
    screen.blit(scoreText, [0, SCREEN_HEIGHT/2 - 20])
    pygame.display.update()    
    while(selected == False):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN and event.key == K_1:
                selected = True
                DIFFICULTY_MODIFIER = 1
            if event.type == KEYDOWN and event.key == K_2:
                selected = True
                DIFFICULTY_MODIFIER = 2
            if event.type == KEYDOWN and event.key == K_3:
                selected = True
                DIFFICULTY_MODIFIER = 3
            if event.type == KEYDOWN and event.key == K_4:
                selected = True
                DIFFICULTY_MODIFIER = 4
            if event.type == KEYDOWN and event.key == K_5:
                selected = True
                DIFFICULTY_MODIFIER = 5
    pygame.draw.rect(screen, BLACK, [0,0, SCREEN_WIDTH, SCREEN_HEIGHT], 0)
    paused = False
    resetLevel = False
    while True:
        clock.tick(10)
        events = pygame.event.get()
        for event in events:
            if event.type == KEYDOWN and event.key == K_SPACE:
                paused = not paused 
        if not paused:       
            character.derender(screen)
            for enemy in enemies:
                enemy.derender
            for k in range(DIFFICULTY_MODIFIER):
                shooter = randint(0,50)
                if shooter < 20:
                    blasts.append(enemies[shooter].shoot())
            for event in events:
                if event.type == pygame.QUIT:
                    return True
                if event.type == KEYUP and event.key == K_w:
                    vy = 0
                if event.type == KEYUP and event.key == K_s:
                    vy = 0
                if event.type == KEYUP and event.key == K_a:
                    vx = 0
                if event.type == KEYUP and event.key == K_d:
                    vx = 0                
                if event.type == KEYDOWN and event.key == K_w:
                    vy = -CHARACTER_SPEED
                if event.type == KEYDOWN and event.key == K_s:
                    vy = CHARACTER_SPEED
                if event.type == KEYDOWN and event.key == K_a:
                    vx = -CHARACTER_SPEED
                if event.type == KEYDOWN and event.key == K_d:
                    vx = CHARACTER_SPEED
            for blast in blasts:
                blast.derender(screen)
                blast.move()
                killer = overlap(blast.getHitbox(), character.getHitbox())
                if killer == True:
                    resetLevel = True
                    character.derender(screen)
                    lives -= 1
                if blast.delete == True:
                    score += 1
                    blasts.remove(blast)
                else:
                    blast.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            pygame.draw.rect(screen, BLACK, [0,0, SCREEN_WIDTH, 22], 0)
            message = 'Score: {0}, Lives Remaining: {1}'.format(str(score), str(lives)) 
            font = pygame.font.SysFont("Impact", 22, bold=False, italic=False)
            scoreText = font.render(message, True, WHITE)
            screen.blit(scoreText, [SCREEN_WIDTH / 2 - 150, 0])
            if lives < 1:
                message = 'Game Over: {0}'.format(str(score)) 
                font = pygame.font.SysFont("Impact", 36, bold=False, italic=False)
                scoreText = font.render(message, True, WHITE)
                screen.blit(scoreText, [SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2])
                pygame.display.update()        
                sleep(3)
                return
            if resetLevel == True:
                for blast in blasts:
                    blast.derender(screen)
                blasts.clear()
                character.derender(screen)
                character.resetPos()
                resetLevel = False
            moveCharacter(vx, vy, character)
            character.move()
            character.draw(screen)
            pygame.display.update()


def moveCharacter(vx, vy, character):
    character.setMoving(vx,vy)
    return


class Character:
    """ A character that is controllable by the user """
    WIDTH = 30
    HEIGHT = 30
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.bbox = []
        
    def draw(self, surface):
        self.bbox = pygame.draw.rect(surface, WHITE, [self.x,self.y, self.WIDTH, self.HEIGHT])
        pygame.draw.rect(surface, WHITE, [self.x,self.y, self.WIDTH, self.HEIGHT], 3)
        
    def setMoving(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def resetPos(self):
        self.x = SCREEN_WIDTH/2 - Character.WIDTH/2
        self.y = SCREEN_HEIGHT - CHARACTER_OFFSET
        return
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - Character.WIDTH:
            self.x = SCREEN_WIDTH - Character.WIDTH
        if self.y < 22 + Enemy.HEIGHT:
            self.y = 22 + Enemy.HEIGHT
        elif self.y > SCREEN_HEIGHT - Character.HEIGHT:
            self.y = SCREEN_HEIGHT - Character.HEIGHT
        return

    def derender(self, surface):
        self.bbox = pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT])
        pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT], 3)
        return

    def getHitbox(self):
        rectangle = Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        return rectangle

class Enemy:
    """ A character that is controllable by the user """
    WIDTH = 30
    HEIGHT = 30
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.bbox = []
        
    def draw(self, surface):
        self.bbox = pygame.draw.rect(surface, GREEN, [self.x,self.y, self.WIDTH, self.HEIGHT])
        pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT], 3)
        return
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - Character.WIDTH:
            self.x = SCREEN_WIDTH - Character.WIDTH
        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - Character.HEIGHT:
            self.y = SCREEN_HEIGHT - Character.HEIGHT
        return

    def shoot(self):
        z = Blast(self.x + self.WIDTH/2, self.y + self.HEIGHT / 2)
        return z

    def derender(self, surface):
        self.bbox = pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT])
        pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT], 3)

class Blast:
    """ A character that is controllable by the user """
    WIDTH = 3
    HEIGHT = 15
    delete = False

    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = BLAST_SPEED
        self.bbox = []
        self.delete = False
        
    def draw(self, surface):
        self.bbox = pygame.draw.rect(surface, RED, [self.x,self.y, self.WIDTH, self.HEIGHT])
        pygame.draw.rect(surface, RED, [self.x,self.y, self.WIDTH, self.HEIGHT], 3)
        
    def move(self):
        self.y += self.vy
        if self.y > SCREEN_HEIGHT - Character.HEIGHT:
            self.delete = True


    def derender(self, surface):
        self.bbox = pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT])
        pygame.draw.rect(surface, BLACK, [self.x,self.y, self.WIDTH, self.HEIGHT], 3)

    def getHitbox(self):
        rectangle = Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        return rectangle

while killGame == False:
    killGame = eventLoop()
