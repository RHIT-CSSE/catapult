import zellegraphics as zg
# In each of the functions below, replace "pass" with  graphics code that draws what the function's comments specify.
# The miscgraphicsTarget.jpg gives an idea of what each function should draw when you have completed it.

import time
import math

win = zg.GraphWin(width=800, height=650)

# TODO on each: replace the "pass" with the definition of the function

# Create and draw "numLines" parallel vertical lines of color "color" and length "length" and seperated by "distanceBetween" pixels
# The top point of the  leftmost line should be at coordinates (10, 10). 
def parallelVerticalLines(numLines, length, distanceBetween, color):
    pass
	
# Create and draw "num" number of concentric circles with a center at the point "center" and 
# spaced apart by "spacing" number of pixels (which is the  radius of the smallest circle)
def concentricCircles(num, center, spacing):
    pass

# Draw an "upward-pointing" equilateral triangle whose lower-left  vertex is 
# the Point "lowerLeftPoint" and whose side length is "width"
# The triangle should not be filled.  This can be done by calculating the coordinates of the three vertices
# and drawing the lines between them.  The calculation is harder than it may look at first.  
# It may take several tries to get the coordinates right.
def equilateralTriangle(lowerLeftPoint, width):
    pass        


# Draws three equilateral triangles arranged in a pyramid, with the loweer-leftmost vertex at the point
# "lowerLeftPoint" and a total width of "width".  I.e., the width of each of the small triangles is width/2.
# You should use a call to equilateralTriangle to draw each of the small triangle.
def tri2(lowerLeftPoint, width):
    pass

# Draws three tri2's  arranged in a pyramid, with the most lower left point at the point
# "lowerLeftPoint" and a total width of "width". Do this by calling your tri2 function three times.
def tri3(lowerLeftPoint, width):
    pass

# CHALLENGE PROBLEM:
# Draws a pattern of triangles in a pyramid shape. The lower left point of the pattern is at the point
# "lowerLeftPoint" and the largest, all-containing triangle has a width of "width". The pattern is similar to
# "tri2" and "tri3" except there are n layers of triangles within triangles.    When n is 1, it draws an equilateral
# triangle.  When n is 2, it draws a tri2 figure, etc.  
# EXTRA CHALLENGES: Can you avoid writing functions like "tri4", "tri5", etc?
#                   Can you avoid calling tri2 and tri3?
def triN(n, lowerLeftPoint, width):
    pass

# This is the part that tests the various functions
# You should not change any of the code that comes after this comment.

parallelVerticalLines(10, 100, 20, 'blue')
parallelVerticalLines(5, 50, 17, 'red')

concentricCircles(12, zg.Point(200, 200), 10)
concentricCircles(5, zg.Point(350, 80), 8)

equilateralTriangle(zg.Point(20, 300), 100)
equilateralTriangle(zg.Point(520, 150), 50)

tri2(zg.Point(650, 350), 100)
tri3(zg.Point(600, 200), 150)

# wait for a mouse click
win.getMouse()


for i in range(1,9):
    triN(i, zg.Point(150, 575), 600)
    time.sleep(1.5)

win.getMouse()

win.close()
