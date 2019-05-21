'''
Displays various messages depending on whether or not we click in a circle.

'''

import zellegraphics as zg
import math

# Defines the mathematical distance formula between the points "p1" and "p2"
def distance(p1, p2):
    ''' The distance formula '''
    return 0

# print the distance between the point (10,10) and the point (13, 7)
d = distance(zg.Point(10, 10), zg.Point(13, 7))
print(d)

# draw a window with a title "Click in circle" with dimensions 400x400


# Create a text object, set its properties, and display it on the window
instructions = zg.Text(zg.Point(200, 75), "Click in the circle")
instructions.setStyle("bold italic")
instructions.setSize(30)
instructions.setTextColor("purple")

# Create a circle at (200, 200) with radius 80 and draw it on the window


# Create a text object at (200, 350) and draw it on the window
message = zg.Text(zg.Point(200, 350), "")


# Main loop of the program: wait for a mouse click and store its click 
# coordinates in a "click" variable. Check to see if the distance from 
# the click to the center of the circle is larger than the radius. If it is, 
# then the user missed and the message is changed accordingly. If not, then
# the user hit, the message is updated to say "Bullseye", and the loop is 
# broken out of.


# Wait for a mouse click and close the window
