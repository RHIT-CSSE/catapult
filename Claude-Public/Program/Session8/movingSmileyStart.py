# Moving smiley program to illustrate objects and how they can interact.
# Claude Anderson.  June 16, 2007

import math
from time import sleep
from graphics import *

def translate(point, dx, dy):
    'return a Point that is a translation of point by deltas dx and dy'
    return Point(point.getX()+dx, point.getY()+dy)

def distance (point1, point2):
    'return the distance between point1 and point2'
    return math.sqrt((point1.getX() - point2.getX())**2 +
                     (point1.getY() - point2.getY())**2)

class Smiley:
    """ A Smiley is a smiley-face object that is capable of moving.
        FIELDS:
          centerPoint: center of this smiley
          dx, dy, amount the smiley moves each step
          size: radius of this smiley
          isSmiling, isMOving: booleans indicating current dynamic state.
          parts: a list of all of the drawable parts.
          others: the individual drawable parts
          
    """ 
    def __init__ (self, initX, initY, dx, dy, size=40, color='red', isSmiling='true'):
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color
        self.isSmiling = isSmiling
        self.moving = True
        # now initialize drawable components:
        self.centerPoint = Point(initX, initY)
        self.head = Circle(Point(initX, initY), size);
        self.head.setFill(color)
        self.head.setWidth(3)
        self.leftEye = Circle(translate(self.centerPoint, -size/4, -size/3), size/8)
        self.rightEye = Circle(translate(self.centerPoint, size/4, -size/3), size/8)
        self.smileBase = Line(translate(self.centerPoint, -size/4, size/2),
                              translate(self.centerPoint, size/4, size/2))
        # initialize the "corners of the mouth" in smile position
        self.smileLeft  = Line(translate(self.centerPoint, -size/4, size/4),
                               translate(self.centerPoint, -size/4,  size/2))
        self.smileRight = Line(translate(self.centerPoint, size/4, size/4),
                               translate(self.centerPoint, size/4,  size/2))
        if not isSmiling:  # move them to frown position.
            self.smileLeft.move(0, size/4)
            self.smileRight.move(0, size/4)
        # Collect all drawable parts into a list.


    # ADD ALL NEEDED METHODS HERE




def scene1():  # to show the basic setup and movement, without complex logic.
    s1 = Smiley(50, 50, 2, 2)
    s2 = Smiley(130, 130, 5, 2, 60, 'green', False)
    win=GraphWin("", 400, 400)
    smileys = [s1, s2]
    s1.draw(win)
    s2.draw(win)
    for i in range(70):
        for s in smileys:
            s.move()
        sleep(0.05)
    win.getMouse()
    win.close()

def runCollisionScene(smileys, steps):
    '''move the smileys in the list until time runs out or until
       all have collided (and therefore stopped).
       Notice the frowns after collisions!'''
    win=GraphWin("", 400, 400)
    
    # This text message gets displayed if all of thesmileys crash.
    t=Text(Point(200, 40), "PileUp!!")
    t.setSize(30)
    t.setFace('arial')
    t.setStyle('bold')
    t.setFill('blue3')
    
    moverCount = 0; # how many smileys have not crashed?

    # Draw 'em all and count how many are moving.
    for s in smileys:
        s.draw(win)
        if s.moving:
            moverCount +=1

# Fill in code here to check for collisions


   
    if moverCount == 0: #all smileys have crashed!.
        t.draw(win)
    win.getMouse()
    win.close()


def scene2():
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -1, 4, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     150)


def scene3():
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -2, 4, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     200 )

def scene4():
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -1, 5, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     200 )
    
scenes = [scene1, scene2, scene3, scene4]

if __name__ == '__main__':
    # ADD CODE TO TEST SMILEYS HERE
    pass



#    scene = int(raw_input('Which scene do you want? (1, 2, 3, or 4): ').replace('\r', ''))
#    scenes[scene-1]()
    
