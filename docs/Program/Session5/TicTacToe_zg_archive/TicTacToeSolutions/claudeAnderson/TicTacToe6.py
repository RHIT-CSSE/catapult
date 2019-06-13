# TicTacToe Version 6
# Checks for a winner and draws the line.

from zellegraphics import *
import time

# Default values for global constants
BOARD_SIZE  = 3                   # number of rows and columns
BOARD_RANGE = range(BOARD_SIZE)    # range of rows and columns
PPS        = 150                 # pixels per square
WINDOW_SIZE = PPS * BOARD_SIZE     # width and height of window
INSET      = 15                  # num white pixels around X's and O's in squares
win        = None                # Everything is displayed in this window, initialized in main()

# Constants for who is occupying a board position
EMPTY   = -1
# XFILLED = 0  (but these never need to be explicitly used)
# OFILLED = 1

def drawGrid():
    for i in range (1, BOARD_SIZE):
        Line(Point(0, i*PPS), Point(WINDOW_SIZE, i * PPS)).draw(win)
        Line(Point(i*PPS, 0), Point(i * PPS, WINDOW_SIZE)).draw(win)

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


# ----- Functions to test for a Winning move.  If so, returns the endpoints of the line to be drawn.

def checkWinner(row, col):
    'Check to see if the latest move resulted in a win'
    xo = squareState[row][col]
    if checkRow(row, xo):
        return [rectUpperLeft(row, 0), rectLowerRight(row, BOARD_SIZE - 1)]
    if checkCol(col, xo):
        return [rectUpperLeft(0, col), rectLowerRight(BOARD_SIZE - 1, col)]
    if row == col and checkMainDiagonal(xo):
        return [rectUpperLeft(0, 0), rectLowerRight(BOARD_SIZE - 1, BOARD_SIZE - 1)]
    if row + col == BOARD_SIZE-1 and checkOtherDiagonal(xo):
        return [rectUpperRight(0, BOARD_SIZE - 1), rectLowerLeft(BOARD_SIZE - 1, 0)]
    return False


def checkRow(row, xo):
    return checkGeneral(row, 0, 0, 1, xo)
def checkCol(col, xo):
    return checkGeneral(0, col, 1, 0, xo)
def checkMainDiagonal(xo):
    return checkGeneral(0, 0, 1, 1, xo);
def checkOtherDiagonal(xo):
    return checkGeneral(0, BOARD_SIZE - 1, 1, -1, xo)

def checkGeneral(row, col, rowIncrement, colIncrement, xo):
    for i in BOARD_RANGE:
        if squareState[row][col] != xo:
            return False
        row += rowIncrement
        col += colIncrement
    return True

    
def main():
    global win, BOARD_SIZE, BOARD_RANGE, WINDOW_SIZE, squareState
    
    # First ask for boardsize and set the global parameters
    userSize = input('Enter board size (Press Enter for 3): ')
    if userSize != '':
        BOARDSIZE  = int(userSize)    
        BOARDRANGE = range(BOARDSIZE)
        WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
    win = GraphWin("TicTacToe version 6", WINDOWSIZE, WINDOWSIZE)

    # initialize the board state with all empty spaces
    squareState = [[EMPTY for j in BOARDRANGE] for i in BOARDRANGE]

    drawGrid()
    turnCount = 0
   

    while turnCount < BOARDSIZE * BOARDSIZE:
        clickPoint = win.getMouse()
        row, col = boardCoord(clickPoint.getY()), boardCoord(clickPoint.getX())
        if squareState[row][col] == EMPTY: # if already filled, do nothing.
            drawList[turnCount%2](row, col) # this line calls the function stored in drawList at turnCount%2 with the parameters (row, col)
            # ^^^ This is equivalent to:
			# if (turnCount % 2 == 0):
			# 	drawX(row, col)
			# else:
			# 	drawO(row, col)
			
            squareState[row][col] = turnCount%2
            turnCount = turnCount + 1
            winner = checkWinner(row, col)
            if winner:
                winLine = Line(winner[0], winner[1])
                winLine.setOutline('red')
                winLine.setWidth(4)
                winLine.move(6,0)
                winLine.draw(win)
                break
 
    time.sleep(3)
    win.close()

main()
