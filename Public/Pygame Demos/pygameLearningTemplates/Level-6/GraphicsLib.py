import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 153, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 51, 153)

# ------------------------------
heroSprite = pygame.Surface((100, 70))
pygame.draw.rect(heroSprite, RED, (0, 0, 100, 60))
pygame.draw.circle(heroSprite, WHITE, (15, 60), 10)
pygame.draw.circle(heroSprite, WHITE, (85, 60), 10)
# set_colorkey(<COLOR>) configure <COLOR> to be transparent
heroSprite.set_colorkey(BLACK)


# This loads an image as a surface. It takes name of the image file
someLoadedImage = pygame.image.load("ball.png")
someLoadedImage = pygame.transform.scale(someLoadedImage, (20, 20))
someLoadedImage.set_colorkey(WHITE)
# <<ADVANCED>> This can some how make screen.blit(someLoadedImage, (x, y)) much faster
# ============ because it convert someLoadedImage into a format based on the current resolution
someLoadedImage = someLoadedImage.convert()

# ------------------------------
ballSpriteOrange = pygame.Surface((20,20))
pygame.draw.circle(ballSpriteOrange, ORANGE, (10, 10), 10)
ballSpriteOrange.set_colorkey(BLACK)

# ------------------------------
ballSpriteBLUE = pygame.Surface((20,20))
pygame.draw.circle(ballSpriteBLUE, BLUE, (10, 10), 10)
ballSpriteBLUE.set_colorkey(BLACK)

# a simple animation of only three frame
animation = [someLoadedImage, ballSpriteBLUE, ballSpriteOrange]


# This loads an image as a surface. It takes name of the image file
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (500, 500))
background = background.convert()


# ------------------------------
# on example of creating an animiation (a list of surface)
# initialize the animiation as an empty list
shiningAnimation = []
# create an function that will append an customized frame to the shiningAnimation
# you can pass anything into this function, even another surface
def addFrameToAnimation(color, radius):
    frame = pygame.Surface((40, 40))
    frame.set_colorkey(BLACK)
    pygame.draw.circle(frame, color, (20, 20), radius)
    # append the created frame to the shiningAnimation
    shiningAnimation.append(frame)
# call this function each time for one frame of the shiningAnimation
for i in range(1, 10):
	addFrameToAnimation(BLUE, i)
for i in range(10, 15):
	addFrameToAnimation(PURPLE, i)
for i in range(15, 20):
	addFrameToAnimation(RED, i)
for i in range(20, 14, -1):
	addFrameToAnimation(RED, i)
for i in range(14, 9, -1):
	addFrameToAnimation(PURPLE, i)
for i in range(9, 0, -1):
	addFrameToAnimation(BLUE, i)

