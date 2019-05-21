# TicTacToe Version 0 - draw a bsic 3x3 grid.

import zellegraphics as zg
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
        zg.Line(zg.Point(0, i*PPS), zg.Point(WINDOWSIZE, i*PPS)).draw(win)
        zg.Line(zg.Point(i*PPS, 0), zg.Point(i*PPS, WINDOWSIZE)).draw(win)

def main():
    global win
    win = zg.GraphWin("TicTacToe version 0", WINDOWSIZE, WINDOWSIZE)
    drawGrid()
    win.getMouse()
    win.close()

main()


