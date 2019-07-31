# Painting House Assignment Starting Code
# Created by Shijun Yu, 6/11/2019

# TODO: replace [YOUR_NAME] with your name in the next line to claim credit
author = '[YOUR_NAME]'

# import the pygame module
import pygame

# pre-define RGB colors for Pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (172, 172, 172)
BROWN = (165, 42, 42)
SKY_BLUE = (135, 206, 235)
LAWN_GREEN = (96, 128, 56)

# TODO: Add you favourite colors below for your picture


# initialize the pygame module
pygame.init()

# create a surface on screen that has the size of 800 x 700 with a caption
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Painting House by " + author)

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
    screen.fill(LAWN_GREEN)
    # Draw the blue sky
    pygame.draw.rect(screen, SKY_BLUE, [0,0,800,400])

    # TODO: Add shapes below to create your own house painting!


    # Update the screen
    pygame.display.update()

# Exit pygame when hit here
pygame.quit()
