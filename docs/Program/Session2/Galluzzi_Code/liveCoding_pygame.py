import pygame

WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
# get pygame library ready

screen = pygame.display.set_mode((500, 500))
# create a 500X500 Screen. Note screen is an instance of surface 

car = pygame.Surface((100, 90))
# create a surface that we will draw a car on

pygame.draw.rect(car, WHITE, (0, 0, 100, 80))
# draw the car body

pygame.draw.circle(car, ORANGE, (15, 80), 10)
pygame.draw.circle(car, ORANGE, (85, 80), 10)
car.set_colorkey(BLACK)
# In surface car, wherever there is black, it means it is transparent.

x = 10
y = 10
# initial position of the car
vx = 10
vy = 2
# initial velocity of the car

while True:
    eventLs = pygame.event.get()
    # grab all events pygame recieved
    for event in eventLs:
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()

    screen.fill(RED)
    # clear the whole screen with RED background

    x += vx
    y += vy
    # update the position depending on the velocity
    screen.blit(car, (x, y))
    # copy the car onto the screen surface

    pygame.display.flip()
    # ask pygame to display everythong on the GUI

    pygame.time.wait(100)
    # delay the time, so can see the Windows

pygame.quit()
# quit the game and close window