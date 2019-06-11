import pygame
import sys
import time

def main():
    pygame.init()

    # TODO: Create a Game object here. Once you've completed all of the other TODOs in this file come back and call
    #  the run_game() method on the Game object you previously created.


class Game:
    def __init__(self):
        self.width = 300
        self.height = 300
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bouncing Ball')
        self.screen.fill(pygame.Color('gray'))

        # TODO: Create an instance variable of the Game class called self.ball and initialize it to a new Ball object by passing in
        #  self.screen to the Ball's constructor

    def run_game(self):
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
        # TODO: Delete pass and draw the Ball by using pygame.draw.ellipse. pygame.draw.ellipse works slightly different than pygame.draw.circle.
        #  Take a look at the pygame documentation link below to find the difference between these two methods.
        #  pygame.draw.ellipse - https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse
        pass


    def move_ball(self):
        # TODO: Delete pass. There are a few things you will need to do to complete this method:
        #  1) Before moving the Ball you will need to figure out if moving the Ball will result in a collision with the
        #  side of the frame. We don't just want to have our Ball flying off the screen! Complete the Ball's collision
        #  method and then call the collision method inside move_ball.
        #  2) Move the Ball's rect instance variable. Remember, Ball's rect instance is an object and it has method's too.
        #  Maybe you could find a method in the pygame documentation for the Rect class that would help you find the method
        #  that you're looking for - https://www.pygame.org/docs/ref/rect.html
        #  3) Now that we've moved the Ball's rect object, we need to call the Ball's draw method to update the Ball on the screen.
        pass

    def collision(self):
        # TODO: Delete pass and then use the Ball's rect instance variable to detect collisions with the sides of the frame.
        #  You can find method's you can call on the Ball's screen instance variable to find its width and height in the link below:
        #  https://www.pygame.org/docs/ref/surface.html#pygame.Surface
        #  The Ball's rect instance variable has its own instance variables as well. Learn more about them in the link below:
        #  https://www.pygame.org/docs/ref/rect.html
        pass
main()