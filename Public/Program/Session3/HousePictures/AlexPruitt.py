import zellegraphics as zg
from zellegraphics import *
import time









win = zg.GraphWin("House", 900,500)

for offset in range (20):
    smoke=Circle(Point(500+6*offset,80-8*offset),30)
    smoke.setFill('grey')
    smoke.draw(win)

rect= Rectangle(Point(300,500), Point(600,120))
rect.setOutline('brown')
rect.setFill('orange')
rect.draw(win)
poly=Polygon(Point(600,120),Point(450,50),Point(300,120))
poly.setOutline('brown')
poly.setFill('brown')
poly.draw(win)
door = Rectangle(Point(450,450),Point(500,500))
door.setOutline('black')
door.setFill('black')
door.draw(win)
line=Line(Point(50,30),Point(70,30))
line.draw(win)

win.getMouse()
for i in range(900):
    line.move(1,0)
    time.sleep(.01)


