# TODO: Copy all of your   05-Animation.py   program and put it below this comment.

# TODO: In this module we'll make the nose reset when the up arrow is pressed.

# Additional challenges (time permitting):
#   Make the eyes move left and right with the left and right arrow button.
#   Make the nose color change when the spacebar is pressed.
#   Make the face grow and shrink with the g and s buttons.
#   Draw a proportionally incorrect stick figure body under the face using lines.
#   Make everything drawn move down off the screen if a the mouse down event occurs.


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Smile")

nose_y = 240
eye_x = 0
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        nose_y = 50
    if pressed_keys[pygame.K_LEFT]:
        eye_x = eye_x - 5
    if pressed_keys[pygame.K_RIGHT]:
        eye_x = eye_x + 5

    screen.fill((120, 80, 0))  # Brown

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)

    pygame.draw.circle(screen, (225, 225, 225), (240 + eye_x, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (240 + eye_x, 160), 25, 3)
    pygame.draw.circle(screen, (0, 0, 0), (242 + eye_x, 162), 7)

    pygame.draw.circle(screen, (225, 225, 225), (400 + eye_x, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (400 + eye_x, 160), 25, 3)
    pygame.draw.circle(screen, (0, 0, 0), (398 + eye_x, 162), 7)

    nose_y = nose_y + 1
    if nose_y > 260:
        nose_y = 240
    pygame.draw.circle(screen, (80, 0, 0), (320, nose_y), 15, 6)

    # pygame.draw.rect(screen, color, (x, y, width, height), thickness)
    pygame.draw.rect(screen, (100, 0, 0), (240, 350, 160, 30))
    pygame.draw.rect(screen, (100, 0, 0), (210, 330, 50, 30))
    pygame.draw.rect(screen, (100, 0, 0), (390, 330, 50, 30))

    pygame.display.update()
