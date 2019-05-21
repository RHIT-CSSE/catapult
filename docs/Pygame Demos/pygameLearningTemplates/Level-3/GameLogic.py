import pygame
import GraphicsUtil as Graph
import random
from Util import hasCollideRect

# the minimum class for an object that can be displayed on the screen
class ImageObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img


class Game:
    def __init__(self):
        # set the initial background of the game
        self.background = Graph.BLACK
        # put hero as an attribute of the game
        self.hero = ImageObject(0, 0, Graph.heroSprite)
        self.stars = []
        # put all objects that will be drawn on the screen in a list
        self.objectsOnScreen = [self.hero]


    # updateGame() is called before each frame is displayed
    def updateGame(self):
        # dectect collision of stars and hero using rectangle
        for s in self.stars:
            # imported from util.py
            # hasCollideRect(a, b) checks whether a and b collides based on their rectangles
            if hasCollideRect(self.hero, s):
                self.stars.remove(s)
                self.objectsOnScreen.remove(s)
                

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


