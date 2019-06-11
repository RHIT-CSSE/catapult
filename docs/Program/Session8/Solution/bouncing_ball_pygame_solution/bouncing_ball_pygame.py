import pygame
import sys
import time

def main():
    pygame.init()
    game = Game()
    game.runGame()

class Game:
    def __init__(self):
        self.width = 300
        self.height = 300
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bouncing Ball')
        self.screen.fill(pygame.Color('gray'))
        self.ball = Ball(self.screen)

    def runGame(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(pygame.Color('gray'))

            self.ball.move_ball()

            time.sleep(.01)

            pygame.display.update()


class Ball():
    def __init__(self, screen):
        self.screen = screen
        self.ball_color = pygame.Color("green")
        self.x = 70
        self.y = 70
        self.x_direction = 2
        self.y_direction = 4
        self.radius = 10
        self.ball_width = 0
        self.rect = pygame.draw.circle(screen, self.ball_color, (self.x, self.y), self.radius, self.ball_width)

    def draw(self):
        pygame.draw.ellipse(self.screen, self.ball_color, self.rect)

    def move_ball(self):
        collision_result = self.collision()
        self.rect = self.rect.move(self.x_direction, self.y_direction)
        self.draw()
        return collision_result

    def collision(self):
        if (self.rect.centerx + self.radius >= self.screen.get_width()):
            self.x_direction = -self.x_direction
            return True
        if (self.rect.centery + self.radius >= self.screen.get_height()):
            self.y_direction = -self.y_direction
            return True
        if (self.rect.centerx - self.radius <= 0):
            self.x_direction = -self.x_direction
            return True
        if (self.rect.centery - self.radius <= 0):
            self.y_direction = -self.y_direction
            return True

        return False

main()