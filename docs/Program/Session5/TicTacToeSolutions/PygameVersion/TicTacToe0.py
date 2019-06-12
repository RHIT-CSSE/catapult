# TicTacToe Version 0 - draw a bsic 3x3 grid.

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

# ----- Main Function

def main():
  global screen

  pygame.init() # Initialize Pygame
  screen = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))
  pygame.display.set_caption("Tic Tac Toe version 0")

  # define a variable to control the main loop
  running = True
  # main loop
  while running:
    for event in pygame.event.get():  # event handling, gets all event from the event queue
      if event.type == pygame.QUIT:  # only do something if the event is of type QUIT
        running = False  # change the value to False, to exit the main loop

    screen.fill(WHITE)  # Clear the screen and set the screen background

    drawGrid()

    pygame.display.update()  # Update the screen
# calling main function here
main()