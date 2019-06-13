# TicTacToe Version 5 - checks for a winner and draws the line.

# import pygame so we can use it
import pygame

# Initialize constants
BOARD_SIZE  = 3                   # number of rows and columns
BOARD_RANGE = range(BOARD_SIZE)   # range of rows and columns
PPS         = 150                 # pixels per square
WINDOW_SIZE = PPS * BOARD_SIZE    # width and height of window
INSET       = 15                  # num pixels around X's and O's in squares
BLACK       = (0, 0, 0)           # color black
WHITE       = (255, 255, 255)     # color white
RED         = (255, 0, 0)         # color red
EMPTY_MARK  = '.'                 # mark for an empty cell

# Initialize global variables
screen      = None                # Everything is displayed in this screen, initialized in main()
turn_count  = 0                   # The count for total turns have taken so far
board       = []                  # Board configuration to keep track of throughout the game
marks       = ['X', 'O']          # Possible marks for each cell
win_line    = []                  # The line that crosses the winner


def draw_grid():
    'Draw the horizontal and vertical lines'
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (0, i*PPS), (WINDOW_SIZE, i*PPS))
        pygame.draw.line(screen, BLACK, (i*PPS, 0), (i*PPS, WINDOW_SIZE))


# ----- Functions to get various locations within the squares

def rect_center(row, col):
    'coordinates of center of square'
    return int(PPS*col + PPS/2), int(PPS*row + PPS/2)


def rect_upper_left(row, col):
    'coordinates of top left of inset X or O'
    return (PPS*col + INSET), (PPS*row + INSET)


def rect_lower_right(row, col):
    'coordinates of bottom right of inset X or O'
    return (PPS*(col+1) - INSET), (PPS*(row+1) - INSET)


def rect_upper_right(row, col):
    'coordinates of top right of inset X or O'
    return (PPS*(col+1) - INSET), (PPS*row + INSET)


def rect_lower_left(row, col):
    'coordinates of bottom left of inset X or O'
    return (PPS*col + INSET), (PPS*(row+1) - INSET)


def rect_upper_center(row, col):
    'coordinates of upper center of inset X or O'
    return (PPS*col + PPS//2), (PPS*row + INSET)


def rect_lower_center(row, col):
    'coordinates of lower center of inset X or O'
    return (PPS*col + PPS//2), (PPS*(row+1) - INSET)


def rect_left_center(row, col):
    'coordinates of left center of inset X or O'
    return (PPS*col + INSET), (PPS*row + PPS//2)


def rect_right_center(row, col):
    'coordinates of right center of inset X or O'
    return (PPS*(col+1) - INSET), ((PPS*row + PPS//2))


# ----- Functions to draw an X and an O in a particular square.

def draw_x(row, col):
    'Draw an X in the given square'
    pygame.draw.line(screen, BLACK, rect_upper_left(row, col), rect_lower_right(row, col), 1)
    pygame.draw.line(screen, BLACK, rect_lower_left(row, col), rect_upper_right(row, col), 1)


def draw_o(row, col):
    'Draw an O in the given square'
    pygame.draw.circle(screen, BLACK, rect_center(row, col), int(PPS / 2 - INSET), 1);


def draw_board():
    'Draw the board based on the marked store in the board configuration array'
    global board
    for row in BOARD_RANGE:
        for col in BOARD_RANGE:
            mark = board[row][col]
            if mark == 'X':
                draw_x(row, col)
            elif mark == 'O':
                draw_o(row, col)


# ----- Handle game turns

def get_board_coord(pixel_x, pixel_y):
    'Find out row or colum number that corresponds to this pixel coordinate'
    return (pixel_x // PPS), (pixel_y // PPS)


def take_turn():
    'Handle the current turn of the player and update board array'
    global screen, turn_count, board, win_line
    click_x, click_y = pygame.mouse.get_pos()     # get the current mouse position
    col, row = get_board_coord(click_x, click_y)  # Y coordinate is the row, X coordinate is the column

    # Only update the board if the clicked position is empty
    if board[row][col] == EMPTY_MARK:
        board[row][col] = marks[turn_count % 2]       # save the mark to its position based on turn_count
        turn_count = turn_count + 1                   # next turn for the game
        # Check if the game is at a winning stage
        winner = check_winner(row, col)
        if winner:
            win_line = winner


# ----- Functions to test for a Winning move.  If so, returns the endpoints of the line to be drawn.

def check_winner(row, col):
    'Check to see if the latest move resulted in a win'
    mark = board[row][col]
    if check_row(row, mark):
        return [rect_left_center(row, 0), rect_right_center(row, BOARD_SIZE - 1)]
    if check_col(col, mark):
        return [rect_upper_center(0, col), rect_lower_center(BOARD_SIZE - 1, col)]
    if row == col and check_main_diagonal(mark):
        return [rect_upper_left(0, 0), rect_lower_right(BOARD_SIZE - 1, BOARD_SIZE - 1)]
    if row + col == BOARD_SIZE - 1 and check_other_diagonal(mark):
        return [rect_upper_right(0, BOARD_SIZE - 1), rect_lower_left(BOARD_SIZE - 1, 0)]
    return False


def check_row(row, mark):
    return check_general(row, 0, 0, 1, mark)


def check_col(col, mark):
    return check_general(0, col, 1, 0, mark)


def check_main_diagonal(mark):
    return check_general(0, 0, 1, 1, mark)


def check_other_diagonal(mark):
    return check_general(0, BOARD_SIZE - 1, 1, -1, mark)


def check_general(row, col, row_increment, col_increment, mark):
    for _ in BOARD_RANGE:
        if board[row][col] != mark:
            return False
        row += row_increment
        col += col_increment
    return True


# ----- Main Function

def main():
    global screen, board, BOARD_SIZE, BOARD_RANGE, WINDOW_SIZE

    # First ask for boardsize and set the global parameters
    user_size = input('\nEnter board size (Press Enter for 3): ')
    if user_size != '':
        BOARD_SIZE = int(user_size)
        BOARD_RANGE = range(BOARD_SIZE)
        WINDOW_SIZE = PPS * BOARD_SIZE  # width and height of window

    # Create a BOARD_SIZE * BOARD_SIZE 2D array filled with empty_mark
    board = [[EMPTY_MARK for _ in BOARD_RANGE] for _ in BOARD_RANGE]

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Tic Tac Toe version 5")

    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # Exit the game if the board is filled with enough clicks
        if turn_count >= BOARD_SIZE * BOARD_SIZE:
            break

        for event in pygame.event.get():    # event handling, gets all event from the event queue
            if event.type == pygame.QUIT:   # only do something if the event is of type QUIT
                running = False             # change the value to False, to exit the main loop
            # check for mouse clicks to handle next turn
            # only do something if the game is not won and the mouse click is released
            if not win_line and event.type == pygame.MOUSEBUTTONUP:
                take_turn()                 # handle the current turn and update the board

        screen.fill(WHITE)  # Clear the screen and set the screen background

        draw_grid()
        draw_board()

        if win_line:  # if the game is won, draw the red line across the winning marks
            pygame.draw.line(screen, RED, win_line[0], win_line[1], 4)

        pygame.display.update()  # Update the screen

    # quit the game when exit out the while loop
    pygame.quit()


# calling main function here
main()
