# import the pygame module
import pygame

# pre-define RGB colors for Pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize the pygame module
pygame.init()
pygame.font.init()

# create a surface on screen that has the size of 800 x 700 with a caption
screen = pygame.display.set_mode((470, 500))
pygame.display.set_caption("Text and Image Example")

# define a variable to control the main loop
running = True

# Load the music and the image
pygame.mixer.music.load("bark.mp3")
image1 = pygame.image.load("2dogs.JPG")

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        # play the music if there's a mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.play()

    # Setup displays to draw on the screen
    font1 = pygame.font.Font(None, 30)
    caption1 = font1.render("Two Doggos", True, BLACK)

    image1 = pygame.transform.scale(image1, (470, 470))

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw the surfaces on the screen
    screen.blit(image1, (0, 0))
    screen.blit(caption1, ((image1.get_width() // 2 - caption1.get_width() // 2), (image1.get_height() + 5)))

    # Update the screen
    pygame.display.update()

# Exit pygame when hit here
pygame.font.quit()
pygame.quit()
