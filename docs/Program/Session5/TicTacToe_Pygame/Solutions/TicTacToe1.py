# TicTacToe Version 1 - allow different board sizes.

# import pygame so we can use it
import pygame

# initialize constants
BOARD_SIZE  = 3                   # number of rows and columns
BOARD_RANGE = range(BOARD_SIZE)   # range of rows and columns
PPS         = 150                 # pixels per square
WINDOW_SIZE = PPS * BOARD_SIZE    # width and height of window
INSET       = 15                  # num pixels around X's and O's in squares
BLACK       = (0, 0, 0)           # color black
WHITE       = (255, 255, 255)     # color white

# Initialize global variables
screen     = None                 # Everything is displayed in this screen, initialized in main()


def draw_grid():
    'Draw the horizontal and vertical lines'
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (0, i * PPS), (WINDOW_SIZE, i * PPS))
        pygame.draw.line(screen, BLACK, (i * PPS, 0), (i * PPS, WINDOW_SIZE))


# ----- Main Function

def main():
    global screen, BOARD_SIZE, BOARD_RANGE, WINDOW_SIZE

    # First ask for boardsize and set the global parameters
    user_size = input('\nEnter board size (Press Enter for 3): ')
    if user_size != '':
        BOARD_SIZE = int(user_size)
        BOARD_RANGE = range(BOARD_SIZE)
        WINDOW_SIZE = PPS * BOARD_SIZE  # width and height of window

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Tic Tac Toe version 1")

    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        for event in pygame.event.get():    # event handling, gets all event from the event queue
            if event.type == pygame.QUIT:   # only do something if the event is of type QUIT
                running = False             # change the value to False, to exit the main loop

        screen.fill(WHITE)  # Clear the screen and set the screen background

        draw_grid()

        pygame.display.update()  # Update the screen

    # quit the game when exit out the while loop
    pygame.quit()


# calling main function here
main()
