# Examples of using graphics

import zellegraphics as zg
import time
 
# Create a graphics window
win = zg.GraphWin('Our First Graphics Demo' , 700, 500)

# Create a line and draw it on the window
line = zg.Line(zg.Point(20, 30), zg.Point(300, 490))
line.draw(win)

# Create a new line, set its width, set its color, and draw it on the window
thickLine = zg.Line(zg.Point(30, 490), zg.Point(200, 30))
thickLine.setWidth(5)
thickLine.setOutline('red')
thickLine.draw(win)

# Create a new line and draw it in one statement
(zg.Line(zg.Point(200, 230), zg.Point(500, 230))).draw(win)

# Create a circle and draw it on the window
zg.Circle(zg.Point(500, 100), 70).draw(win)

# Create a rectangle, set its fill to green, and draw it on the screen
rectangle = zg.Rectangle(zg.Point(350, 450), zg.Point(400, 500))
rectangle.setFill('green')
rectangle.draw(win)

# draw several lines on the screen in a loop
for offset in range(20):
    orangeLine = zg.Line(zg.Point(200 - 6* offset, 100 + 8* offset),
                      zg.Point(50 - 6* offset, 50 + 8* offset))
    orangeLine.setOutline(zg.color_rgb(255, 150, 0))
    orangeLine.setWidth(3)
    orangeLine.draw(win)

# move the rectangle across the screen and sleep a set amount of time
for i in range(300):
    rectangle.move(1, -1)
    time.sleep(0.01)

# wait to close the window
time.sleep(5)
win.close()

