#-------------------------
# initialize pygame
#-------------------------
import pygame

# initialize pygame
pygame.init()

# create a screen of 500 * 500
# pygame.display.set_mode((screenWidth, screenHeight))
screen = pygame.display.set_mode((500, 500))

#-------------------------
# draw an circle onto the screen
#-------------------------
# define color, an tuple of 3 number representing (Red, Green, Blue)
WHITE = (255, 255, 255)
# pygame.draw.method(...) has many functions to draw on a screen
# pygame.draw.circle(surfaceToBeDrawnOn, color, centerCoordinate, radius)
pygame.draw.circle(screen, WHITE, (20, 20), 20)

# ask pygame to display screen on the GUI
pygame.display.flip()
