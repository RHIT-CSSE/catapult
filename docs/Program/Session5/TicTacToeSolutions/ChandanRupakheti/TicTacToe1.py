# TicTacToe Version 1 - allow different board sizes.

import zellegraphics as zg
import time

# Default values for global constants
BOARDSIZE  = 3                   # number of rows and columns
BOARDRANGE = range(BOARDSIZE)    # range of rows and columns
PPS        = 150                 # pixels per square
WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
INSET      = 15                  # num white pixels around X's and O's in squares
win        = None                # Everything is displayed in this window, initialized in main()

def drawGrid():
    'Draw the horizontal and vertical lines'
    for i in range (1, BOARDSIZE):
        zg.Line(zg.Point(0, i*PPS), zg.Point(WINDOWSIZE, i*PPS)).draw(win)
        zg.Line(zg.Point(i*PPS, 0), zg.Point(i*PPS, WINDOWSIZE)).draw(win)

    
def main():
    global win, BOARDSIZE, BOARDRANGE, WINDOWSIZE
    
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


