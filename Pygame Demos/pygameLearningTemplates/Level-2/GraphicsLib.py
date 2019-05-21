import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# ------------------------------
heroSprite = pygame.Surface((100, 70))
pygame.draw.rect(heroSprite, RED, (0, 0, 100, 60))
pygame.draw.circle(heroSprite, WHITE, (15, 60), 10)
pygame.draw.circle(heroSprite, WHITE, (85, 60), 10)
