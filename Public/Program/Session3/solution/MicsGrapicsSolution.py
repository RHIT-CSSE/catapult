import zellegraphics as zg
# In each of the functions below, replace "pass" with some graphics code.
# The miscgraphicsTarget.jpg gives an idea of what each function should draw when you have completed it.

import time
import math


win = zg.GraphWin(width=800, height=650)

# TODO on each: replace the "pass" with the definition of the function

# Draw "numLines" amount of parallel lines of color "color" and length "length" and seperated by "distanceBetween" pixels
def parallelVerticalLines(numLines, length, distanceBetween, color):
    startX = 10
    startY = 10
    endX = startX
    endY = startY + length

    for n in range(numLines):
        line = zg.Line(zg.Point(startX,startY), zg.Point(endX, endY))
        line.setFill(color)
        line.draw(win)
        
        startX = startX + distanceBetween
        endX = endX + distanceBetween
        

# Draw an equilateral triangle with a lower left point at the point "lowerLeftPoint" and a side length of "width"
def equilateralTriangle(lowerLeftPoint, width):
    x = lowerLeftPoint.x
    y = lowerLeftPoint.y
    
    base = zg.Line(zg.Point(x, y), zg.Point(x + width, y))
    base.draw(win)
    
    height = math.sqrt(width**2 - (width/2)**2)
    left = zg.Line(zg.Point(x, y), zg.Point(x + width / 2, y - height))
    left.draw(win)
    
    right = zg.Line(zg.Point(x + width, y), zg.Point(x + width / 2, y - height))
    right.draw(win)

# Draw "num" number of concentric circles with a center at the point "center" and 
# spaced apart by "spacing" number of pixels (which is the base radius of the smallest circle)
def concentricCircles(num, center, spacing):
    for n in range(num):
        circle = zg.Circle(center, spacing * n)
        circle.setOutline('red')
        circle.draw(win)

# Draws three equilateral triangles arranged in a pyramid, with the most lower left point at the point
# "lowerLeftPoint" and a total width of "width"
def tri2(lowerLeftPoint, width):
    x = lowerLeftPoint.x
    y = lowerLeftPoint.y
    height = math.sqrt(width**2 - (width/2)**2)

    equilateralTriangle(lowerLeftPoint, width/2)
    equilateralTriangle(zg.Point(x + width/2, y), width/2)
    equilateralTriangle(zg.Point(x + width/4, y - height/2), width/2)
    

# Draws three equilateral triangles arranged in a pyramid, with the most lower left point at the point
# "lowerLeftPoint" and a total width of "width". Then, within each of these three triangles, three more 
# equilateral triangles are drawn.
def tri3(lowerLeftPoint, width):
    x = lowerLeftPoint.x
    y = lowerLeftPoint.y
    height = math.sqrt((width/2)**2 - (width/4)**2)

    tri2(lowerLeftPoint, width/2)
    tri2(zg.Point(x + width/2, y), width/2)
    tri2(zg.Point(x + width/4, y - height), width/2)
    
    

# Draws a pattern of triangles in a pyramid shape. The lower left point of the pattern is at the point
# "lowerLeftPoint" and the largest, all-containing triangle has a width of "width". The pattern is similar to
# "tri2" and "tri3" except there are n layers of triangles within triangles. 
def triN(n, lowerLeftPoint, width):
    if n<=1:
        equilateralTriangle(lowerLeftPoint, width)
    else:
        x = lowerLeftPoint.x
        y = lowerLeftPoint.y
        height = math.sqrt(width**2 - (width/2)**2)

        triN(n-1, lowerLeftPoint, width/2)
        triN(n-1, zg.Point(x + width/2, y), width/2)
        triN(n-1, zg.Point(x + width/4, y - height/2), width/2)
        


# This is the part that calls the various functions:
parallelVerticalLines(10, 100, 20, 'blue')
parallelVerticalLines(5, 50, 17, 'red')
equilateralTriangle(zg.Point(20, 300), 100)
equilateralTriangle(zg.Point(520, 150), 50)
concentricCircles(12, zg.Point(200, 200), 10)
concentricCircles(5, zg.Point(350, 80), 8)

tri2(zg.Point(650, 350), 100)
tri3(zg.Point(600, 200), 150)

# wait for a mouse click
win.getMouse()

for i in range(8):
    triN(i+1,zg.Point(150, 575), 600)
    time.sleep(1.5)

win.getMouse()

win.close()
