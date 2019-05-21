import pygame
import GraphicsUtil as Graph
import random
from Util import showAnimationOn, hasCollideRect

# the minimum class for an object that can be displayed on the screen
class ImageObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

# a great example of an object that can move on the screen
class Hero:
    def __init__(self):
        # ------------------------
        # [REQUIRED PART] for any class that will be drawn on the screen
        # Grab the surface that Graphics people worked very hard on
        self.img = Graph.heroSprite
        # Set the initial coordinate of this object
        self.x = 0
        self.y = 0
        # ------------------------
        # TODO: add more properties to Hero based on your game
        self.vx = 0
        self.vy = 0

    # update the position of hero based on its speed
    def update(self):
        self.x += self.vx
        self.y += self.vy


class Game:
    def __init__(self):
        # initialize the time to zero.
        # self.time is a clock that record how many ticks has elapsed
        self.time = 0
        # set the initial background of the game
        self.background = Graph.BLACK
        # set the initial state of game to be "Normal"
        self.state = "Normal"

        # put hero as an attribute of the game
        self.hero = Hero()
        self.ball = ImageObject(250, 250, Graph.someLoadedImage)
        self.stars = []
        # put all objects that will be drawn on the screen in a list
        self.objectsOnScreen = [self.hero, self.ball]


    # updateGame() is called before each frame is displayed
    def updateGame(self):
        # update the time
        self.time += 1
        # check what state the game is at
        if self.state == "Normal":
            # update the game before each frame of the state
            self.hero.update()
            # dectect collision of stars and hero using rectangle
            for s in self.stars:
                if hasCollideRect(self.hero, s):
                    self.stars.remove(s)
                    self.objectsOnScreen.remove(s)
            # showAnimationOn() takes three argument, the object, the animation, and the frameNumber
            # the animation should be a list of surface representing each frame
            showAnimationOn(self.ball, Graph.animation, self.time / 20)
        elif self.state == "Pause":
            pass
        else:
            raise Exception("Undefined game state " + str(self.state))
        return self.state

    # an example of adding an object to the screen
    def addAnRandomBall(self):
        addedStar = ImageObject(random.randint(0, 500),random.randint(0, 500), Graph.someLoadedImage)
        self.stars.append(addedStar)
        self.objectsOnScreen.append(addedStar)


    # A method that does all the drawing for you.
    def draw(self, screen):
        # clear the screen, or set up the background, 
        screen.fill(self.background)

        for obj in self.objectsOnScreen:
            screen.blit(obj.img, (obj.x, obj.y))


