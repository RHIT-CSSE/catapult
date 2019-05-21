import math, time
from zellegraphics import *

def nearEnough(point1, point2, tolerance):
    'Is point1 within TOLERANCE distance from point2?'
    return distance(point1, point2) <= tolerance

def distance(point1, point2):
    return math.sqrt((point1.getX() - point2.getX())**2 +
                     (point1.getY() - point2.getY())**2)

win = GraphWin("Click Inside the Circle", 400, 400)
CENTERPOINT = Point(200, 200)
radius = 75
c = Circle(CENTERPOINT, radius)
c.setWidth(4)
c.draw(win)
t = Text(Point(200, 50), "Click inside the circle")
t.setFace('arial')
t.setSize(30)
t.setStyle('bold italic')
t.setFill('yellow1')
t.draw(win)


miss = Text(Point(200, 350), "You missed!")
miss.setFace('arial')
miss.setSize(20)
miss.setFill('red3')
missDrawn=False


p = win.getMouse()
while not nearEnough(p, CENTERPOINT, radius):
    if not missDrawn:
        miss.draw(win)
        missDrawn = True
    p =win.getMouse()
if missDrawn:
    miss.undraw()
hit = Text(Point(200, 350), "Bull's eye!")
hit.setSize(36)
hit.setFace('arial')
hit.setFill('green')
hit.draw(win)

time.sleep(2.5)
win.close()
    
          
