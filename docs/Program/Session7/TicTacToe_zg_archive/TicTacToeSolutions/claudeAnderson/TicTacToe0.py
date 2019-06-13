# TicTacToe Version 0 - draw a bsic 3x3 grid.

from zellegraphics import *
import time

BOARD_SIZE  = 3                   # number of rows and columns
BOARD_RANGE = range(BOARD_SIZE)    # range of rows and columns
PPS        = 150                 # pixels per square
WINDOW_SIZE = PPS * BOARD_SIZE     # width and height of window
INSET      = 15                  # num pixels around X's and O's in squares
win        = None                # Everything is displayed in this window, initialized in main()



def drawGrid():
    'Draw the horizontal and vertical lines'
    for i in range (1, BOARD_SIZE):
        Line(Point(0, i*PPS), Point(WINDOW_SIZE, i * PPS)).draw(win)
        Line(Point(i*PPS, 0), Point(i * PPS, WINDOW_SIZE)).draw(win)

def main():
    global win
    win = GraphWin("TicTacToe version 0", WINDOW_SIZE, WINDOW_SIZE)
    drawGrid()
    time.sleep(3)
    win.close()

main()


