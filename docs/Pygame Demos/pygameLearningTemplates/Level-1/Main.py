#-------------------------
# initialize pygame
#-------------------------
import pygame
# initialize pygame
pygame.init()

# initialize a clock for the game, so you can control the framerate
clock = pygame.time.Clock()

# create a screen of 500 * 500
screen = pygame.display.set_mode((500, 500))

#-------------------------
# CREATE GRAPHICS COMPONENTS (Surface) of the game
#-------------------------
# define color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
img = pygame.Surface((40, 40))
pygame.draw.circle(img, WHITE, (20, 20), 20)


#-------------------------
# Our Main Loop
#-------------------------
## Each time the loop is executed, one framed
# 100 frames will be displayed with an interval of 100ms
for i in range(100):
    #-------------------------
    # The graphics block
    #-------------------------
    ## all the drawing happen here
    screen.fill(BLACK)

    # copies surface img onto surface screen
    # conpiedTo.blit(conpiedFrom, (leftUpCorner_x, leftUpCorner_y))
    screen.blit(img, (20+i, 20+i))

    #-------------------------
    # display this frame and wait
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everything on the GUI
    
    clock.tick(60)
    # set the framerate of the game to 60fps, i.e. 60 updates in one second
    