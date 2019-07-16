import pygame
import sys
import random

class Ball:
    def __init__(self, screen, x, y, color, radius):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.randint(-5, 5)  # Note, it might pick 0, oh well
        self.speed_y = random.randint(-5, 5)  # Note, it might pick 0, oh well

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.x + self.radius >= self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.y + self.radius >= self.screen.get_height():
            self.speed_y = -self.speed_y
        if self.x - self.radius <= 0:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))

    clock = pygame.time.Clock()

    demo_with_1_ball_only = True

    if demo_with_1_ball_only:
        ball = Ball(screen, 70, 70, pygame.Color("green"), 10)
    else:
        balls = []
        for k in range(100):
            new_ball = Ball(screen, random.randint(10, 290), random.randint(10, 290),
                            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                            random.randint(8, 12))
            balls.append(new_ball)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        if demo_with_1_ball_only:
            ball.move()
            ball.draw()
        else:
            for ball in balls:
                ball.move()
                ball.draw()

        pygame.display.update()


main()
