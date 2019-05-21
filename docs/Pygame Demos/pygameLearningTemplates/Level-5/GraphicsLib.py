import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 153, 0)
BLUE = (0, 0, 255)

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