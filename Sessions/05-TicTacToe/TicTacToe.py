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
EMPTY_MARK = '.' # mark for an empty cell

# Initialize global variables
screen     = None                 # Everything is displayed in this screen, initialized in main()


def draw_grid():
    'Draw the horizontal and vertical lines'

    # TODO 1: implement this function
    # Hint: you'll want 1 or 2 for loops
    #
    # Here's an example of what the code to draw a horzontal line looks like
    # pygame.draw.line(screen, BLACK, (0, i * PPS), (WINDOW_SIZE, i * PPS))

    pass

def draw_board():
    'Draw the board based on the marked store in the board configuration array'
    global board
    for row in BOARD_RANGE:
        for col in BOARD_RANGE:
            mark = board[row][col]
            # do the right thing here in step 3

# ----- Main Function

def main():
    global screen, board, BOARD_SIZE, BOARD_RANGE, WINDOW_SIZE

    # First ask for boardsize and set the global parameters
    user_size = input('\nEnter board size (Press Enter for 3): ')
    if user_size != '':
        BOARD_SIZE = int(user_size)
        BOARD_RANGE = range(BOARD_SIZE)
        WINDOW_SIZE = PPS * BOARD_SIZE  # width and height of window

    board = [[EMPTY_MARK for _ in BOARD_RANGE] for _ in BOARD_RANGE]
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
            # TODO 4: Make clicking the mouse edit the board array
            # TODO 5 (advanced): figure out if the click won the game and if so allow no more moves

        screen.fill(WHITE)  # Clear the screen and set the screen background

        draw_grid()

        # TODO 2: write functions that draw an x or o at a particular
        # board row and column (e.g. 1 2 is middle row rightmost column on a 3x3)

        # There are images includes in this directory for you to use
        # draw_o(1, 2)
        # draw_x(0, 0)

        # TODO 3:
        # Rather than expicitly calling draw_x and draw_o, we want to have a board that we draw from
        # remove the draw_x and draw_o calls from TODO2 above and instead implement draw_board
        board[0][1] = 'X'
        board[2][2] = 'O'
        draw_board()

        pygame.display.update()  # Update the screen

    # quit the game when exit out the while loop
    pygame.quit()


# calling main function here
main()
