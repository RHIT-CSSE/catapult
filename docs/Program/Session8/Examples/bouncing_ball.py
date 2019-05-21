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
        self.width = 300 # Values can be changed as needed. Example values
        self.height = 300 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Need to set background so shapes are drawn with full color
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill((220,220,220)) # Values can be changed as needed. Example values
        self.ball = Ball(self.screen)

    def runGame(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values

        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((220,220,220)) # Values can be changed as needed. Example values
            # self.ball.draw()
            self.ball.move_ball()
            time.sleep(.1)
            pygame.display.update()


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.ball_color = pygame.Color("green")
        self.x_direction = 2
        self.y_direction = 4
        self.radius = 10 # Can be used in other functions
        self.rect = pygame.draw.circle(screen, self.ball_color,  (70, 70), self.radius, 0) # Values can be changed as needed. Example values

    def draw(self):
        pygame.draw.ellipse(self.screen, self.ball_color, self.rect)
    
    def move_ball(self):
        if (self.rect.centerx + self.radius >= self.screen.get_width()):
            self.x_direction = -self.x_direction
        if (self.rect.centery + self.radius>= self.screen.get_height()):
            self.y_direction = -self.y_direction
        if (self.rect.centerx - self.radius <= 0):
            self.x_direction = -self.x_direction
        if (self.rect.centery - self.radius <= 0):
            self.y_direction = -self.y_direction
        self.rect.move_ip(self.x_direction, self.y_direction)
        self.draw()


main()