# TicTacToe Version 1 - allow different board sizes.

import zellegraphics as zg
import time

# Default values for global constants
BOARD_SIZE  = 3                   # number of rows and columns
BOARD_RANGE = range(BOARD_SIZE)    # range of rows and columns
PPS        = 150                 # pixels per square
WINDOW_SIZE = PPS * BOARD_SIZE     # width and height of window
INSET      = 15                  # num white pixels around X's and O's in squares
win        = None                # Everything is displayed in this window, initialized in main()

def drawGrid():
    'Draw the horizontal and vertical lines'
    for i in range (1, BOARD_SIZE):
        zg.Line(zg.Point(0, i*PPS), zg.Point(WINDOW_SIZE, i * PPS)).draw(win)
        zg.Line(zg.Point(i*PPS, 0), zg.Point(i * PPS, WINDOW_SIZE)).draw(win)

    
def main():
    global win, BOARD_SIZE, BOARD_RANGE, WINDOW_SIZE
    
    # First ask for boardsize and set the global parameters
    userSize = input('Enter board size (Press Enter for 3): ')
    if userSize != '':
        BOARDSIZE  = int(userSize)    
        BOARDRANGE = range(BOARDSIZE)
        WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
    win = zg.GraphWin("TicTacToe version 1", WINDOWSIZE, WINDOWSIZE)
    
    drawGrid()
    win.getMouse()
    win.close()

main()


