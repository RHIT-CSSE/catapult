# Moving smiley program to illustrate objects and how they can interact.
# Claude Anderson.  June 16, 2007
# Modified Nov 5, 2009
'''  
description:
    This module illustrates how to define a class (the Smiley class) to generate custom objects.
    The Smiley class has a constructor, several instance variables and  methods. 
    
    The smiley_world module imports and uses this module to illustrate how objects are 
    generated and interact with each other.
    

@author: Claude Anderson, created on June 16, 2007. Modified by many others.
'''
from zellegraphics import Point, Circle, Line
import math

#----------------------------------------------------------------------
# Auxiliary functions which are not part of the Smiley class
#----------------------------------------------------------------------
def translate(point, dx, dy):
    'return a Point that is a translation of point by deltas dx and dy'
    return Point(point.getX()+dx, point.getY()+dy)

def distance (point1, point2):
    'return the distance between point1 and point2'
    return math.sqrt((point1.getX() - point2.getX())**2 +
                     (point1.getY() - point2.getY())**2)

#----------------------------------------------------------------------
# We add a Smiley Class definition here.
#----------------------------------------------------------------------
class Smiley:

    ''' A Smiley is a smiley-face object that is capable of moving. '''
    
    # Constructor
    def __init__ (self, initX, initY, dx, dy, size=40, color='red', isSmiling=True):
        ''' The constructor of this class (and every Python class) is the __init__ function.
            The first parameter of the constructor (and any method) is self.  self refers to 
            the object in question, in this case the object being constructed. 
            An object of type Smiley is instantiated by calling the Smiley() function, without 
            the self parameter.  This is an implicit parameter.  Although there is no Smiley() 
            function or method defined in this class, calling the Smiley() invokes the real 
            constructor __init__() for this class.  __init__ is never invoked directly.
            
            INSTANCE VARIABLES:
              - centerPoint: center of this smiley
              - dx, dy, amount the smiley moves each step
              - size: radius of this smiley
              - isSmiling, isMoving: booleans indicating current dynamic state.
              - parts: a list of all of the drawable parts.
                  -- leftEye, etc.: the individual drawable parts
          
          '''
        self.centerPoint = Point(initX, initY)
        self.dx = dx
        self.dy = dy
        self.size = size
        self.isSmiling = isSmiling
        self.moving = True
        self.color = color
        
        # now initialize drawable components:
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
        self.parts = [self.head, self.leftEye, self.rightEye,
                      self.smileBase, self.smileLeft, self.smileRight, self.centerPoint]


    #----------------------------------------------------------------------
    # TODO: 2. add several methods to the Smiley class definition here.
    #    1. draw()
    #    2. move()
    #    3. smile()
    #    4. frown()
    #  NOTE: each method must take a self parameter, even though you do not
    #  explicitly supply one when you invoke the method.  The way self gets 
    #  interpreted is follows. The self parameter applies to the object that 
    #  invokes its method.  Say for example, we construct an object called
    #  smiley1 and smiley1 invokes its draw method like this: 
    #  smiley1.draw(win).  Notice that self is not passed as a parameter to 
    #  the draw method.  Instead,  self applies to smiley1.  That assignment
    #  takes place implicitly. It's like saying I am smiley1 and you asked me 
    #  to invoke my draw method, using the given window.
    #----------------------------------------------------------------------
    
    def draw(self, win):
        for part in self.parts:
            part.draw(win)
    
    def move(self):
        for part in self.parts:
            part.move(self.dx, self.dy)
    
    def smile(self):
        self.isSmiling = True
        self.smileLeft.move(0, -self.size/4)
        self.smileRight.move(0, -self.size/4)
    
    def frown(self):
        self.isSmiling = False
        self.smileLeft.move(0, self.size/4)
        self.smileRight.move(0, self.size/4)

    #----------------------------------------------------------------------
    # In order to run the rest of the scenarios (scenes 2, 3, and 4 in
    # smiley_world), we need to implement and use the 
    # following methods.
    #----------------------------------------------------------------------
    def stop(self):
        'Stop moving.'
        self.moving = False

    def isMoving(self):
        'Is this object moving?'
        return self.moving

    def collidedWith (self, otherSmiley):
        'Has this smiley collided with that other one?'
        return distance(self.centerPoint, otherSmiley.centerPoint) < self.size + otherSmiley.size
