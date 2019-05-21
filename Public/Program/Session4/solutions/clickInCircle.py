'''
Displays various messages depending on whether or not we click in a circle.

Created on Jul 11, 2013

@author: boutell
'''

import zellegraphics as zg
import math

# Defines the mathematical distance formula between the points "p1" and "p2"
def distance(p1, p2):
    ''' The distance formula '''
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx ** 2 + dy ** 2)

# print the distance between the point (10,10) and the point (13, 7)
d = distance(zg.Point(10, 10), zg.Point(13, 7))
print(d)

# draw a window with a title "Click in circle" with dimensions 400x400
win = zg.GraphWin("Click in circle", 400, 400)

# Create a text object, set its properties, and display it on the window
instructions = zg.Text(zg.Point(200, 75), "Click in the circle")
instructions.setStyle("bold italic")
instructions.setSize(30)
instructions.setTextColor("purple")
instructions.draw(win)

# Create a circle and draw it on the window
center = zg.Point(200, 200)
radius = 80
circle = zg.Circle(center, radius)
circle.setWidth(3)
circle.draw(win)

message = zg.Text(zg.Point(200, 350), "")
message.draw(win)

# Main loop of the program: wait for a mouse click and store its click coordinates in "click".
# Then, check to see if the distance from the click to the center of the circle is larger than the radius.
# If it is, then the user missed and the message is changed accordingly. If not, then the user hit, and 
# the loop is broken out of.
while True:
    click = win.getMouse()
    if distance(center, click) > radius:
        message.setText("You missed")
    else: 
        message.setText("Bullseye")
        break

# Wait for a mouse click and close the window
win.getMouse()
win.close()
