# Examples of using graphics

from zellegraphics import *
import time
 
win = GraphWin('Our First Graphics Demo' , 700, 500)
line = Line(Point(20, 30), Point(300, 490))
line.draw(win)

thickLine = Line(Point(30, 490), Point(200, 30))
thickLine.setWidth(5)
thickLine.setOutline('red')
thickLine.draw(win)

(Line(Point(200, 230), Point(500, 230))).draw(win)

Circle(Point(500, 100), 70).draw(win)

rectangle = Rectangle(Point(350, 450), Point(400, 500))
rectangle.setFill('green')
rectangle.draw(win)

for i in range(300):
    rectangle.move(1, -1)
    time.sleep(0.01)


time.sleep(5)
win.close()











##
##
##win = GraphWin('First Graphics Demo', 700, 500)
##
##myLine = Line(Point(20, 30), Point(300, 500))
##myLine.draw(win)
##
##line2 = Line(Point(200, 30), Point(30, 500))
##line2.setOutline('red')
##line2.setWidth(3)
##line2.draw(win)
##
##Line(Point(200, 200), Point(500,200)).draw(win)
##rect = Rectangle(Point(450, 450), Point(500,500))
##rect.setFill('green')
##rect.draw(win);
##
##Circle(Point(500, 100),80).draw(win)
##
##for x in range(120):
##    time.sleep(0.05);
##    rect.move(2, -2)
##
##
##time.sleep(3)
##win.close()






              
