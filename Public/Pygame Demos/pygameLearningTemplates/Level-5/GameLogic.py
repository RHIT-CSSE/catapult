import pygame
import GraphicsUtil as Graph
import random
from Util import *

# the minimum class for an object that can be displayed on the screen
class ImageObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

# a great example of an object that can move on the screen
class Hero:
    def __init__(self):
        # -- ----------------------
        # [REQUIRED PART] for any class that will be drawn on the screen
        # Grab the surface that Graphics people worked very hard on
        self.img = Graph.heroSprite
        # Set the initial coordinate of this object
        self.x = 0
        self.y = 0
        # ------------------------
        self.vx = 0
        self.vy = 0

    # update the position of hero based on its speed
    def update(self):
        self.x += self.vx
        self.y += self.vy
        bounceIn(self, 0, 0, 500, 500)

# a greate example for an object that does animation
class Star:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.birthTime = time

    def update(self, time):
        self.x += 1
        self.y += 1
        showAnimationOn(self, Graph.shiningAnimation, (time - self.birthTime) / 2)
        wrapAroundIn(self, 20, 20, 480, 480)


class Game:
    def __init__(self):
        # initialize the time and state time to zero.
        ## self.time is a clock that record how many ticks has elapsed
        ## self.stateTime is a clock that record how many ticks has elapsed since switched to this state      
        self.time = self.stateTime = 0
        # set the initial background of the game
        self.background = Graph.background
        # set the initial state of game to be "Normal"
        self.state = "Normal"
        
        # put hero as an attribute of the game
        self.hero = Hero()
        self.ball = ImageObject(250, 250, Graph.someLoadedImage)
        self.stars = []
        # put all objects that will be drawn on the screen in a list
        self.objectsOnScreen = [self.hero, self.ball]

    def switchState(self, newState):
        # configure the game when state swiched
        if newState == "Normal":
            self.background = Graph.background
            self.objectsOnScreen = [self.hero, self.ball]
        elif newState == "Pause":
            self.background = Graph.BLACK
            self.objectsOnScreen = [self.hero, self.stars]
        
        # reset the stateTime when switching to a new state
        self.stateTime = 0
        self.state = newState
        
    # updateGame() is called before each frame is displayed
    def updateGame(self):
        # update both the time and state time
        self.time += 1
        self.stateTime += 1
        # check what state the game is at
        if self.state == "Normal":
            # update the game before each frame of the state
            self.hero.update()
            # dectect collision of stars and hero using rectangle
            for s in self.stars:
                if hasCollideRect(self.hero, s):
                    self.stars.remove(s)
            # showAnimationOn() takes three argument, the object, the animation, and the frameNumber
            # the animation should be a list of surface representing each frame
            # it returns whether a complete animation is shown
            if showAnimationOn(self.ball, Graph.shiningAnimation, self.stateTime / 5):
                self.switchState("Pause")
        elif self.state == "Pause":
            for s in self.stars:
                s.update(self.time)
            if self.stateTime > 200:
                self.switchState("Normal")
        else:
            raise Exception("Undefined game state " + str(state))

    # an example of adding an object to the screen
    def addAnRandomBall(self):
        addedStar = Star(random.randint(0, 500),random.randint(0, 500), self.time)
        self.stars.append(addedStar)

    # A method that does all the drawing for you.
    def draw(self, screen):
        # set the background of the game
        if type(self.background) is tuple:
            screen.fill(self.background)
        else:
            screen.blit(self.background, (0, 0))

        # the magic that draw all the objects in objectsOnScreen onto the screen
        def drawOnScreen(objls):
            for obj in objls:
                if type(obj) is list:
                    drawOnScreen(obj)
                else:
                    screen.blit(obj.img, (obj.x, obj.y))
        drawOnScreen(self.objectsOnScreen)     


