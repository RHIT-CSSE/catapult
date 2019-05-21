from zellegraphics import *
import time
from math import sqrt

win = GraphWin('Loopy Pics', 1000, 700)

def parallelLines(startX, startY, height, nLines, spacing):
    for i in range(nLines):
        line = Line(Point(startX+i*spacing, startY), Point(startX+i*spacing, startY + height))
        line.setWidth(3)
        line.draw(win)

def concentricCircles(startX, startY, nCircles, spacing):
    for i in range(nCircles):
        circle = Circle(Point(startX, startY), i*spacing)
        circle.setWidth(2)
        circle.setOutline('red')
        circle.draw(win)

def equilateralTriangle(botLeft, width):
    x1 = botLeft.getX()
    y1 = botLeft.getY()
    x2 = x1 + width
    y2 = y1
    x3 = x1 + width/2
    y3 = y1 - int(width * sqrt(3) / 2)
    pointList = [Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x1, y1)]
    Polygon(pointList).draw(win)

def tri2(botLeft, width):
    x1 = botLeft.getX()
    y1 = botLeft.getY()
    height = int(width * sqrt(3) / 2)
    equilateralTriangle(botLeft, width/2)
    equilateralTriangle(Point(x1 + width/2, y1), width/2)
    equilateralTriangle(Point(x1 + width/4, y1-height/2), width/2)

def tri3(botLeft, width):
    x1 = botLeft.getX()
    y1 = botLeft.getY()
    height = int(width * sqrt(3) / 2)
    tri2(botLeft, width/2)
    tri2(Point(x1 + width/2, y1), width/2)
    tri2(Point(x1 + width/4, y1-height/2), width/2)

def triN(n, botLeft, width):
    if (n <= 1):
        equilateralTriangle(botLeft, width)
    else:
        x1 = botLeft.getX()
        y1 = botLeft.getY()
        height = int(width * sqrt(3) / 2)
        triN(n-1, botLeft, width/2)
        triN(n-1, Point(x1 + width/2, y1), width/2)
        triN(n-1, Point(x1 + width/4, y1-height/2), width/2)
 

parallelLines(10, 10, 100, 10, 10)
#parallelLines(20, 20, 50, 20, 6)
concentricCircles(200, 100, 15, 6)
equilateralTriangle(Point(100, 300), 100)
tri2(Point(700, 300), 100)
tri3(Point(800, 500), 150)
#triN(8, Point(100, 650), 700)

for i in range(1,9):
    triN(i, Point(100, 650), 700)
    time.sleep(1)

win.close()