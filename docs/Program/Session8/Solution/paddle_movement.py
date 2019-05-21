import pygame
import sys
import time

"""
Code will pop up a black screen
"""

def main():
    pygame.init()
    game = Game()
    game.runGame()



"""
Game class
"""
class Game:
    def __init__(self):
        self.width = 500 # Values can be changed as needed. Example values
        self.height = 300 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Need to set background so shapes are drawn with full color
        self.background = pygame.Surface(self.screen.get_size())
        self.myfont = pygame.font.SysFont("monospace", 15)
        self.background = self.background.convert()
        self.screen.fill((220,220,220)) # Values can be changed as needed. Example values
        self.ball = Ball(self.screen)
        self.paddle_bottom = Paddle(self.screen, 50, 250, True)
        self.paddle_top = Paddle(self.screen, 50, 50, False)
        self.cur_time = time.clock()
        self.playing = False
        pygame.mixer.init()
        self.sound1 = pygame.mixer.Sound("ball_bounce.wav")

    def runGame(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        
        self.paddle_bottom.draw_paddle()
        self.paddle_top.draw_paddle()
        while 1:
            self.screen.fill((220,220,220)) # Values can be changed as needed. Example values
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.playing = True
            if self.playing:
                # self.ball.draw()
                self.paddle_bottom.move_paddle()
                self.paddle_top.move_paddle()
                time.sleep(.07)
                self.ball.move_ball()
                self.paddle_collision()
            else:
                text = self.myfont.render("Welcome to pong. Click anywhere to play", 1, (pygame.Color("black")))
                self.screen.blit(text, (50, self.height/2 - 30))
            pygame.display.update()
        
    def paddle_collision(self):
        if pygame.sprite.collide_rect(self.paddle_top, self.ball):
            self.ball.bounceY()
            if self.ball.rect.centerx <= self.paddle_top.rect.centerx:
                print("bounced on left part of the top paddle")
            if self.ball.rect.centerx > self.paddle_top.rect.centerx:
                print("bounced on left part of the top paddle")
            self.sound1.play()
        if pygame.sprite.collide_rect(self.paddle_bottom, self.ball):
            self.ball.bounceY()
            if self.ball.rect.centerx <= self.paddle_bottom.rect.centerx:
                print("bounced on left part of the bottom paddle")
            if self.ball.rect.centerx > self.paddle_bottom.rect.centerx:
                print("bounced on left part of the bottom paddle")
            self.sound1.play()
        


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.ball_color = pygame.Color("green")
        self.x_direction = 2
        self.y_direction = 4
        self.radius = 10 # Can be used in other functions
        self.x_loc = 70
        self.y_loc = 70
        self.rect = pygame.draw.circle(self.screen, self.ball_color,  (self.x_loc, self.y_loc), self.radius, 0) # Values can be changed as needed. Example values

    def draw(self):
        pygame.draw.ellipse(self.screen, self.ball_color, self.rect)
    
    def move_ball(self):
        if (self.rect.centerx + self.radius >= self.screen.get_width()):
            self.x_direction = -self.x_direction
        if (self.rect.centery + self.radius>= self.screen.get_height()):
            self.rect.centerx = self.x_loc
            self.rect.centery = self.y_loc
            self.x_direction = 2
            self.y_direction = 4
        if (self.rect.centerx - self.radius <= 0):
            self.x_direction = -self.x_direction
        if (self.rect.centery - self.radius <= 0):
            # self.bounceY()
            self.rect.centerx = self.x_loc
            self.rect.centery = self.y_loc
            self.x_direction = 2
            self.y_direction = 4

        self.rect.move_ip(self.x_direction, self.y_direction)
        self.draw()
    
    def bounceY(self):
        self.y_direction = -self.y_direction

    
class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen, x_loc, y_loc, paddle_bool):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.paddle_color = pygame.Color("red")
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.paddle_bool = paddle_bool
        self.image = pygame.image.load("brick.jpg")
        self.image = pygame.transform.scale(self.image, (25, 10))
        self.rect = self.image.get_rect()
        self.rect.center=(self.x_loc, self.y_loc)
        # self.rect = pygame.draw.rect(self.screen, self.paddle_color, pygame.Rect(self.x_loc, self.y_loc, 25, 10))
    
    def draw_paddle(self):
        # pygame.draw.rect(self.screen, self.paddle_color, self.rect)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_paddle(self):
        key = pygame.key.get_pressed()
        if self.paddle_bool:
            if key[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
            if key[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)
        else:
            if key[pygame.K_a]:
                self.rect.move_ip(-5,0)
            if key[pygame.K_d]:
                self.rect.move_ip(5,0)
        self.draw_paddle()


main()