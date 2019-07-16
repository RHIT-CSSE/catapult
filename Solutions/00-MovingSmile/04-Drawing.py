import pygame
import sys

pygame.init()
pygame.display.set_caption("Drawing")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((234, 162, 123))

    # Big yellow Circle
    pygame.draw.circle(screen, (255, 255, 0),   (320, 240), 210)

    # Left Eye
    pygame.draw.circle(screen, (0, 0, 0),       (240, 160), 25)
    pygame.draw.circle(screen, (255, 255, 255), (240, 160), 5)

    # Right Eye
    pygame.draw.circle(screen, (0, 0, 0),       (400, 160), 25)
    pygame.draw.circle(screen, (255, 255, 255), (400, 160), 5)

    # nose
    pygame.draw.circle(screen, (255, 0, 0),   (320, 240), 20, 4)

    # Mouth
    pygame.draw.rect(screen, (100, 0, 0),       (200, 320, 240, 30))

    pygame.display.update()