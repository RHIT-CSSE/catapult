'''
Created on Jun 6, 2016

@author: castonkr

''' 
import pygame, math, random
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE, K_q, \
    K_RETURN, MOUSEBUTTONDOWN
from pygame.draw import circle
from shutil import which
from pygame import sprite
from math import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 51, 204)
ORANGE = (255, 153, 51)

# Distance Formula
def distance(point1, point2):
    return math.sqrt((point1[1] - point2[1]) ** 2 + (point1[0] - point2[0]) ** 2)
     
pygame.init()

# Add Sounds
pygame.mixer.init()
song = pygame.mixer.Sound("bounce.wav")
weapon_sound = pygame.mixer.Sound("explosion.wav")

# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ball Game")

# Start Menu
ball = pygame.image.load("ball.png")
title_font = pygame.font.SysFont('Calibri', 75)
title_text = title_font.render('Play Ball Game', True, WHITE)
other_font = pygame.font.SysFont('Calibri', 25, bold=True)
start_text = other_font.render("Start Game", True, WHITE)
screen.blit(ball, [315, 300])
screen.blit(title_text, [125, 125])
screen.blit(start_text, [300, 325])
pygame.display.flip()
start_game = True
my_clock = pygame.time.Clock()
while start_game:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()  
            if distance((355, 340), a) < 40:
                start_game = False
            if start_game is True:
                my_clock = 0       
             
# Loop until the user clicks the close button.
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
all_items = pygame.sprite.Group()
circLs = pygame.sprite.Group()


# Constructs the balls
class Circle(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.radius = random.randrange(3, 15)
        self.dx = random.randrange(1, 5)
        self.dy = random.randrange(1, 5)
        self.x = random.randrange(0, WIDTH - 2 * self.radius)
        self.y = random.randrange(0, HEIGHT - 2 * self.radius)
        
        self.image = pygame.Surface((self.radius * 2, self.radius * 2));
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.circle(self.image, color, [self.radius , self.radius], self.radius);
        
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        
    # Updates the ball's position    
    def update(self):
        if self.x >= WIDTH - 2 * self.radius or self.x <= 0:
            self.dx *= -1
         
        if self.y >= HEIGHT - 2 * self.radius or self.y <= 0:
            self.dy *= -1
        
        self.x += self.dx
        self.y += self.dy
        
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

class Weapon(Circle):
    def __init__(self):
        super().__init__(ORANGE)
        self.dx = random.randrange(0, 2)
        self.dy = random.randrange(0, 2)
        
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
    
# Bounces circles off each other           
def circleCollide(a, b):
    relx, rely = (b.x + b.radius - b.dx) - (a.x + a.radius - a.dx) , (b.y + a.radius - b.dy) - (a.y + b.radius - b.dy)
    relLen = math.sqrt(relx ** 2 + rely ** 2)
    if relLen == 0:
        return
    relx, rely = relx / relLen , rely / relLen;
    ah , av = a.dy * relx - a.dx * rely , a.dx * relx + a.dy * rely
    bh , bv = b.dy * relx - b.dx * rely , b.dx * relx + b.dy * rely
    ratio = a.radius / b.radius
    av2 = (2 * bv + av * (ratio - 1)) / (ratio + 1)
    bv2 = (2 * ratio * av + bv * (1 - ratio)) / (ratio + 1)
    a.dx, a.dy = av2 * relx - ah * rely , av2 * rely + ah * relx
    b.dx, b.dy = bv2 * relx - bh * rely , bv2 * rely + bh * relx

# Constructs the object the Hero is to collect
class Objs(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, GREEN, [0, 0, 5, 5])
        self.rect = self.image.get_rect()
        x = random.randrange(100, WIDTH - 5)
        y = random.randrange(40, HEIGHT - 5)
        self.rect = self.rect.move(x, y)
    
    # Draws the object 
    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.rect.x, self.rect.y, 5, 5])
    
    # Moves the object after the Hero "eats" it
    def eaten(self):
        self.rect.x = random.randrange(0, WIDTH - 5)
        self.rect.y = random.randrange(0, HEIGHT - 5)
        
# Constructs the hero 
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x;
        self.y = y;
        self.rect = pygame.Rect(x, y, 20, 30)
        
        pos = [(0, 30), (20, 30), (10, 0)];
        self.imageUpNormal = pygame.Surface((20, 30))
        self.imageUpNormal.fill(WHITE)
        self.imageUpNormal.set_colorkey(WHITE)
        pygame.draw.polygon(self.imageUpNormal, BLUE, pos)

        self.imageUpHitten = pygame.Surface((20, 30))
        self.imageUpHitten.fill(WHITE)
        self.imageUpHitten.set_colorkey(WHITE)
        pygame.draw.polygon(self.imageUpHitten, PURPLE, pos)
        
        self.imageUp = self.imageUpNormal
        self.image = self.imageUp
        
        self.key = 0b0000
        self.hitTime = 0
    
    # Changes Hero color if hit by ball
    def hitten(self):
        self.hitTime = 10
        self.imageUp = self.imageUpHitten

    # Updates the Hero's position 
    def update(self):
        if self.hitTime > 0:
            self.hitTime -= 1
            if self.hitTime == 0:
                self.imageUp = self.imageUpNormal
        
        if self.key == 0b1000:
            self.y -= 2
            self.rect = pygame.Rect(self.x, self.y, 20, 30);
            self.image = self.imageUp.copy()
        elif self.key == 0b0100:
            self.x += 2
            self.rect = pygame.Rect(self.x, self.y, 30, 30);
            self.image = pygame.transform.rotate(self.imageUp, -90)
        elif self.key == 0b0010:
            self.y += 2
            self.rect = pygame.Rect(self.x, self.y, 20, 30);
            self.image = pygame.transform.rotate(self.imageUp, 180)
        elif self.key == 0b0001:
            self.x -= 2
            self.rect = pygame.Rect(self.x, self.y, 20, 30);
            self.image = pygame.transform.rotate(self.imageUp, 90)
        elif self.key == 0b1100:
            self.x += 1.414
            self.y -= 1.414
            self.rect = pygame.Rect(self.x, self.y, 30, 30);
            self.image = pygame.transform.rotate(self.imageUp, -45)
        elif self.key == 0b0110:
            self.x += 1.414
            self.y += 1.414
            self.rect = pygame.Rect(self.x, self.y, 30, 30);
            self.image = pygame.transform.rotate(self.imageUp, -135)
        elif self.key == 0b0011:
            self.x -= 1.414
            self.y += 1.414
            self.rect = pygame.Rect(self.x, self.y, 30, 30);
            self.image = pygame.transform.rotate(self.imageUp, 135)
        elif self.key == 0b1001:
            self.x -= 1.414
            self.y -= 1.414
            self.rect = pygame.Rect(self.x, self.y, 30, 30);
            self.image = pygame.transform.rotate(self.imageUp, 45)

        if self.y + self.rect.h > HEIGHT:
            self.y = HEIGHT - self.rect.h
        elif self.y < 0:
            self.y = 0
        if self.x + 30 > WIDTH:
            self.x = WIDTH - 30
        elif self.x < 0:
            self.x = 0

    # Setting a bit-key to the arrow keys when a key is pressed
    def keyDown(self, key):
        if key == K_UP:
            self.key |= 0b1000
        elif key == K_RIGHT:
            self.key |= 0b0100
        elif key == K_DOWN:
            self.key |= 0b0010
        elif key == K_LEFT:
            self.key |= 0b0001
    
    # Setting a bit-key to the arrow keys when a key is released 
    def keyUp(self, key):
        if key == K_UP:
            self.key &= 0b0111
        elif key == K_RIGHT:
            self.key &= 0b1011
        elif key == K_DOWN:
            self.key &= 0b1101
        elif key == K_LEFT:
            self.key &= 0b1110
            
# Displays the score and health a player has    
class Score:
    def __init__(self):
        self.init()
        
    def init(self):
        self.points = 0
        self.lives = 100
    
    # Draws the score and health
    def draw(self, surface):        
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text1 = font.render("Score: " + str(self.points), True, WHITE)
        # health_bar 
        pygame.draw.rect(surface, (150, 0, 0), (0, 20, 100, 20))
        pygame.draw.rect(surface, (0, 150, 0), (0, 20, self.lives, 20))
        if self.lives > 0:
            text2 = font.render("Health: " + str(self.lives), True, WHITE)
        else:
            text2 = font.render("Game Over!", True, RED)            
        surface.blit(text1, [0, 0])
        surface.blit(text2, [0, 20])
     
# Initializes hero, obj, score     
hero = Hero(WIDTH / 2, HEIGHT / 2)
obj = Objs()
score = Score()
weapon = Weapon()


# Restarts the game
def restart():
    score.init()
    circ1 = Circle(RED)
    circ2 = Circle(RED)
    circLs.add(circ1 , circ2)
    print("restart")
    global all_items
    global weapon
    weapon = Weapon()
    all_items.empty()
    all_items.add(circ1, circ2, hero, obj)
    all_items.add(weapon)
    
def main():
# -------- Main Program Loop -----------
    while True:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT:
                    hero.keyDown(event.key)
                elif event.key == K_q:
                    exit()
                elif event.key == K_RETURN:
                    if score.lives == 0:
                        restart()
            elif event.type == pygame.KEYUP:
                hero.keyUp(event.key)
                
        screen.fill(BLACK)
     
        if pygame.sprite.spritecollide(hero, circLs, False):
            print("Hero was hit!")
            score.lives -= 1
            hero.hitten()
        
        if hero.rect.colliderect(obj.rect):
            obj.eaten()
            score.points += 1
            newCircle = Circle(RED)
            circLs.add(newCircle)
            all_items.add(newCircle)
            song.play(1, 200)
            
        if hero.rect.colliderect(weapon.rect):
            weapon_range = 10 * weapon.radius
            for c in circLs:
                if distance((c.x + c.radius, c.y + c.radius), (weapon.x + weapon.radius, weapon.y + weapon.radius)) < weapon_range:
                    all_items.remove(c)
                    circLs.remove(c)
                    print("removing")
            pygame.draw.circle(screen, ORANGE, (weapon.x, weapon.y), weapon_range)        
            weapon.kill()
            global weapon
            weapon = Weapon()
            all_items.add(weapon)
            weapon_sound.play(1, 500)
            
            
        hero.update()
        # Draw objects on screen
        
        ls = circLs.sprites()
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                if distance(ls[i].rect, ls[j].rect) < ls[i].radius + ls[j].radius:
                    circleCollide(ls[i], ls[j])
        
        circLs.update()
        weapon.update()
        hero.update()
        score.draw(screen)
        all_items.draw(screen)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        if score.lives <= 0:
            score.lives = 0
            all_items.empty() 
            circLs.empty()
            game_over = pygame.sprite.Sprite()
            message = pygame.Surface((400, 200))
            
            font = pygame.font.SysFont('Calibri', 20, True, False)
            text1 = font.render("Game Over, Press Enter to start new game", True, WHITE)
            text2 = font.render("Q to quit", True, WHITE)          
            message.blit(text1, [0, 0])
            message.blit(text2, [0, 20])
            
            game_over.image = message
      
            game_over.rect = message.get_rect()
            game_over.rect.move_ip(200, 200)
            all_items.add(game_over)
           
        clock.tick(60)
     
# Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    restart()
    main()
