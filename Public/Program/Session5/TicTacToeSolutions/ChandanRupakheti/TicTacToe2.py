# TicTacToe Version 2 -  Draw X and O in specific locations.

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

# ----- Functions to get various locations within the squares

def rectCenter(row, col):
    'coordinates of center of square'
    return zg.Point(PPS*col +PPS/2, PPS*row + PPS/2)

def rectUpperLeft(row, col):
    'coordinates of top left of inset X or O'
    return zg.Point(PPS*col + INSET, PPS*row + INSET)

def rectLowerRight(row, col):
    'coordinates of bottom right of inset X or O'
    return zg.Point(PPS*(col+1) - INSET, PPS*(row+1) - INSET)

def rectUpperRight(row, col):
    'coordinates of top right of inset X or O'
    return zg.Point(PPS*(col+1) - INSET, PPS*row + INSET)

def rectLowerLeft(row, col):
    'coordinates of bottom left of inset X or O'
    return zg.Point(PPS*col + INSET, PPS*(row+1) - INSET)

# ----- Functions to draw an X and an O in a particular square.

def drawX(row, col):
    'Draw an X in the given square'
    zg.Line(rectUpperLeft(row, col), rectLowerRight(row, col)).draw(win)
    zg.Line(rectLowerLeft(row, col), rectUpperRight(row, col)).draw(win)

def drawO(row, col):
    'Draw an O in the given square'
    zg.Circle(rectCenter(row, col), PPS/2-INSET).draw(win)
         
def main():
    global win, BOARDSIZE, BOARDRANGE, WINDOWSIZE
    
    # First ask for boardsize and set the global parameters
    userSize = input('Enter board size (Press Enter for 3): ')
    if userSize != '':
        BOARDSIZE  = int(userSize)    
        BOARDRANGE = range(BOARDSIZE)
        WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
    win = zg.GraphWin("TicTacToe version 2", WINDOWSIZE, WINDOWSIZE)

    drawGrid()
    drawX(1,2) # only works if BOARDSIZE>2
    drawO(0,0)
    win.getMouse()
    win.close()

main()


