# TicTacToe Version 1 - allow different board sizes.

from zellegraphics import *
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
        Line(Point(0, i*PPS), Point(WINDOWSIZE, i*PPS)).draw(win)
        Line(Point(i*PPS, 0), Point(i*PPS, WINDOWSIZE)).draw(win)

    
def main():
    global win, BOARDSIZE, BOARDRANGE, WINDOWSIZE
    
    # First ask for boardsize and set the global parameters
    userSize = raw_input('Enter board size (Press Enter for 3): ')
    if userSize != '':
        BOARDSIZE  = eval(userSize)    
        BOARDRANGE = range(BOARDSIZE)
        WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
    win = GraphWin("TicTacToe version 1", WINDOWSIZE, WINDOWSIZE)
    
    drawGrid()
    time.sleep(3)
    win.close()

main()


