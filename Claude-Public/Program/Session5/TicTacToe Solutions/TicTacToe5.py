# TicTacToe Version 5
# ignores clicks in filled squares
# uses a list of lists - squareState, to keep track of what is in which square.


from zellegraphics import *
import time

# Default values for global constants
BOARDSIZE  = 3                   # number of rows and columns
BOARDRANGE = range(BOARDSIZE)    # range of rows and columns
PPS        = 50                 # pixels per square
WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
INSET      = 15                  # num white pixels around X's and O's in squares
win        = None                # Everything is displayed in this window, initialized in main()

# Constants for who is occupying a board position
EMPTY   = -1
# XFILLED = 0  (but these names never need to be explicitly used)
# OFILLED = 1

def drawGrid():
    for i in range (1, BOARDSIZE):
        Line(Point(0, i*PPS), Point(WINDOWSIZE, i*PPS)).draw(win)
        Line(Point(i*PPS, 0), Point(i*PPS, WINDOWSIZE)).draw(win)

# ---- Functions to get various locations within the squares

def rectCenter(row, col):
    'coordinates of center of square'
    return Point(PPS*col +PPS/2, PPS*row + PPS/2)

def rectUpperLeft(row, col):
    'coordinates of top left of inset X or O'
    return Point(PPS*col + INSET, PPS*row + INSET)

def rectLowerRight(row, col):
    'coordinates of bottom right of inset X or O'
    return Point(PPS*(col+1) - INSET, PPS*(row+1) - INSET)

def rectUpperRight(row, col):
    'coordinates of top right of inset X or O'
    return Point(PPS*(col+1) - INSET, PPS*row + INSET)

def rectLowerLeft(row, col):
    'coordinates of bottom left of inset X or O'
    return Point(PPS*col + INSET, PPS*(row+1) - INSET)

# ----- Functions to draw an X and an O in a particular square.

def drawX(row, col):
    'Draw an X in the given square'
    Line(rectUpperLeft(row, col), rectLowerRight(row, col)).draw(win)
    Line(rectLowerLeft(row, col), rectUpperRight(row, col)).draw(win)

def drawO(row, col):
    'Draw an O in the given square'
    Circle(rectCenter(row, col), PPS/2-INSET).draw(win);

drawList = [drawX, drawO] # makes it possible to use '% 2' in main() instead of if.

# ----- Coordinate conversion.                 
def boardCoord(pixelCoord):
    'Find out row or colum number that corresponds to this pixel coordinate'
    return pixelCoord // PPS;

def main():
    global win, BOARDSIZE, BOARDRANGE, WINDOWSIZE, squareState
    
    # First ask for boardsize and set the global parameters
    userSize = input('Enter board size (Press Enter for 3): ')
    if userSize != '':
        BOARDSIZE  = int(userSize)    
        BOARDRANGE = range(BOARDSIZE)
        WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
    win = GraphWin("TicTacToe version 5", WINDOWSIZE, WINDOWSIZE)

    # initialize the board state with all empty spaces
    squareState = [[EMPTY for j in BOARDRANGE] for i in BOARDRANGE]

    drawGrid()
    turnCount = 0
    
    while turnCount < BOARDSIZE * BOARDSIZE:
        clickPoint = win.getMouse()
        row, col = boardCoord(clickPoint.getY()), boardCoord(clickPoint.getX())
        if squareState[row][col] == EMPTY:    # if this square already filled, do nothing.
            drawList[turnCount%2](row, col)
            squareState[row][col] = turnCount%2
            turnCount = turnCount + 1

    time.sleep(3)
    win.close()

main()
