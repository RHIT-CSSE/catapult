# connect the dots program.
# responds to clicks by connecting the dots.
# when same point is clicked again, make and fill a polygon.

import math, time
from zellegraphics import *

TOLERANCE = 5

def nearEnough(point1, point2):
    'Is point1 within TOLERANCE distance from point2?'
    return distance(point1, point2) <= TOLERANCE

def distance(point1, point2):
    return math.sqrt((point1.getX() - point2.getX())**2 +
                     (point1.getY() - point2.getY())**2)

def drawPoint (p):
    c = Circle(p, TOLERANCE)
    c.setFill('magenta')
    c.draw(win)
    

def tests():
    p1 = Point(1,7)
    p2 = Point(4, 11)
    p3 = Point(-1, 23)
    print ('Distances (should be 5 and 13): ', distance(p1, p2), distance (p2, p3))
    print ('Nearness (should be True, False): ', nearEnough(p1, p2), nearEnough(p2, p3))





#tests()

win = GraphWin()
pointList = [];
while len(pointList) < 3 or not nearEnough(pointList[0], pointList[-1]):
    newPoint = win.getMouse()
    drawPoint(newPoint);
    pointList.append(newPoint)
    if len(pointList) >= 2:
        Line(pointList[-2], pointList[-1]).draw(win)
poly = Polygon(*pointList)
poly.setFill('red')
poly.draw(win)
    
    


time.sleep(2)
win.close()

    
