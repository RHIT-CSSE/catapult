# TicTacToe Version 0 - draw a bsic 3x3 grid.

from zellegraphics import *
import time

BOARDSIZE  = 3                   # number of rows and columns
BOARDRANGE = range(BOARDSIZE)    # range of rows and columns
PPS        = 150                 # pixels per square
WINDOWSIZE = PPS * BOARDSIZE     # width and height of window
INSET      = 15                  # num pixels around X's and O's in squares
win        = None                # Everything is displayed in this window, initialized in main()



def drawGrid():
    'Draw the horizontal and vertical lines'
    for i in range (1, BOARDSIZE):
        Line(Point(0, i*PPS), Point(WINDOWSIZE, i*PPS)).draw(win)
        Line(Point(i*PPS, 0), Point(i*PPS, WINDOWSIZE)).draw(win)

def main():
    global win
    win = GraphWin("TicTacToe version 0", WINDOWSIZE, WINDOWSIZE)
    drawGrid()
    time.sleep(3)
    win.close()

main()


