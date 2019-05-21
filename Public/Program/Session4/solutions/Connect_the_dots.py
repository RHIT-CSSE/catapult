# connect the dots program.
# responds to clicks by connecting the dots.
# when same point is clicked again, make and fill a polygon.

import math, time
import zellegraphics as zg

TOLERANCE = 5
# Defines the mathematical distance formula between the points "point1" and "point2"
def distance(point1, point2):
    dx = point1.getX() - point2.getX()
    dy = point1.getY() - point2.getY()
    return math.sqrt(dx **2 + dy **2)

# Draws a "Point" as seen by the user on the screen. The points that appear are magenta-filled
# circles with a radius of "TOLERANCE"
def drawPoint (p):
    c = zg.Circle(p, TOLERANCE)
    c.setFill('magenta')
    c.draw(win)
    
# Test the distance formula
def tests():
    p1 = zg.Point(1,7)
    p2 = zg.Point(4, 11)
    p3 = zg.Point(-1, 23)
    print('Distances (should be 5 and 13): ', distance(p1, p2), distance (p2, p3))

# Run the main loop of the program. Create a window and wait for clicks from the user. Then, 
# draw points on the screen (using the drawPoint function) at the locations that the user clicks.
# If the point clicked is within the TOLERANCE of the first point (would overlap the first point when drawn)
# Then the shape is finished. A polygon is created using the points that were clicked (and stored in a list)
# and that polygon is filled in green.
win = zg.GraphWin()
pointList = []
while True:
    newPoint = win.getMouse()
    if len(pointList) > 1 and distance(newPoint, pointList[0]) <= TOLERANCE:
        break
    drawPoint(newPoint)
    pointList.append(newPoint)
    if len(pointList) > 1:
        zg.Line(pointList[-2], pointList[-1]).draw(win)
poly = zg.Polygon(pointList)
poly.setFill('green')
poly.draw(win)
    
win.getMouse()
win.close()