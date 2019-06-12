# Examples of using graphics with pygame

# import the pygame module, so you can use it
import pygame
import time

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# initialize the pygame module
pygame.init()
# initial position
x = 550
y = 50
width = 700
height = 500
# initial direction
dx = 0
dy = 5


# create a surface on screen that has the size of 700 x 500 with a caption
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Our First Graphics Demo")

# define a variable to control the main loop
running = True

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # update square's y position with direction
    y += dy
    # check bounds
    if y < 0 or y + 100 > height:
        dy = -dy

    # Draw a line with color black and width 1 on the screen
    pygame.draw.line(screen, BLACK, (50, 50), (500, 50), 1)

    # Draw a Rectangle(Square) with color green on the screen
    # and move it up and down
    pygame.draw.rect(screen, GREEN, [x, y, 100, 100])

    # Draw a circle with red fill
    pygame.draw.circle(screen, RED, (150, 350), 50)

    # Draw an ellipse with blue outline
    pygame.draw.ellipse(screen, BLUE, [300, 300, 150, 100], 1)

    # draw several lines on the screen in a loop
    for i in range(10):
        offset = 20
        y1 = 50 + offset * (i + 1)
        y2 = 50 + offset * (i + 1)
        pygame.draw.line(screen, BLACK, (50, y1), (500, y2), 1)

    # Update the screen
    pygame.display.update()
    time.sleep(0.01)


# Exit pygame when hit here
pygame.quit()