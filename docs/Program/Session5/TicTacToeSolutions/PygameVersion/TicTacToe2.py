# TicTacToe Version 2 - draw X and O in specific locations.

# import pygame so we can use it
import pygame

# initialize constants
BOARDSIZE  = 3                   # number of rows and columns
BOARDRANGE = range(BOARDSIZE)    # range of rows and columns
PPS        = 150                 # pixels per square
WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
INSET      = 15                  # num pixels around X's and O's in squares
BLACK      = (0, 0, 0)           # color black
WHITE      = (255, 255, 255)     # color white

# Initialize global variables
screen     = None                # Everything is displayed in this screen, initialized in main()

def drawGrid():
  # Draw the horizontal and vertical lines
  for i in range (1, BOARDSIZE):
    pygame.draw.line(screen, BLACK, (0, i*PPS), (WINDOWSIZE, i*PPS))
    pygame.draw.line(screen, BLACK, (i*PPS, 0), (i*PPS, WINDOWSIZE))

# ----- Functions to get various locations within the squares

def rectCenter(row, col):
    'coordinates of center of square'
    return (int(PPS*col + PPS/2), int(PPS*row + PPS/2))

def rectUpperLeft(row, col):
    'coordinates of top left of inset X or O'
    return (PPS*col + INSET, PPS*row + INSET)

def rectLowerRight(row, col):
    'coordinates of bottom right of inset X or O'
    return (PPS*(col+1) - INSET, PPS*(row+1) - INSET)

def rectUpperRight(row, col):
    'coordinates of top right of inset X or O'
    return (PPS*(col+1) - INSET, PPS*row + INSET)

def rectLowerLeft(row, col):
    'coordinates of bottom left of inset X or O'
    return (PPS*col + INSET, PPS*(row+1) - INSET)

# ----- Functions to draw an X and an O in a particular square.

def drawX(row, col):
    'Draw an X in the given square'
    pygame.draw.line(screen, BLACK, rectUpperLeft(row, col), rectLowerRight(row, col), 1)
    pygame.draw.line(screen, BLACK, rectLowerLeft(row, col), rectUpperRight(row, col), 1)

def drawO(row, col):
    'Draw an O in the given square'
    pygame.draw.circle(screen, BLACK, rectCenter(row, col), int(PPS/2-INSET), 1);

# ----- Main Function

def main():
  global screen, BOARDSIZE, BOARDRANGE, WINDOWSIZE

  # First ask for boardsize and set the global parameters
  userSize = input('\nEnter board size (Press Enter for 3): ')
  if userSize != '':
    BOARDSIZE = int(userSize)
    BOARDRANGE = range(BOARDSIZE)
    WINDOWSIZE = PPS * BOARDSIZE  # width and height of window

  # Initialize Pygame
  pygame.init()
  screen = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))
  pygame.display.set_caption("Tic Tac Toe version 1")

  # define a variable to control the main loop
  running = True
  # main loop
  while running:
    for event in pygame.event.get():  # event handling, gets all event from the event queue
      if event.type == pygame.QUIT:  # only do something if the event is of type QUIT
        running = False  # change the value to False, to exit the main loop

    screen.fill(WHITE)  # Clear the screen and set the screen background

    drawGrid()
    drawX(1,2)
    drawO(0,0)

    pygame.display.update()  # Update the screen

  # quit the game when exit out the while loop
  pygame.quit()

# calling main function here
main()