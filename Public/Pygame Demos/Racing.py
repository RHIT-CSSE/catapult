import pygame
from pygame.locals import *
import random 
import time

# Created by Derek Grayless - Operation Catapult 2018 Session 1

pygame.init()

gameWidth = 1200
gameHeight = 675

carSpeed = 5

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption('Racing')
clock = pygame.time.Clock()

# http://www.orangefreesounds.com/wilhelm-scream/ - Source for Wilhelm Scream

wilhelmScream = pygame.mixer.Sound("WilhelmScream.wav")

x = gameWidth * 0.5
y = gameHeight * 0.5

class Background(pygame.sprite.Sprite):
    def __init__(self, image, pos, gameDisplay):
        try:
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
            self.x = pos[0]
            self.y = pos[1]
            self.gameDisplay = gameDisplay
        except:
            "Problem loading car image and setting instance variables!"

    def draw(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))

class Car(pygame.sprite.Sprite):
    def __init__(self, image, pos, gameDisplay):
        try:
            self.image = pygame.image.load(image)
            self.x = pos[0]
            self.y = pos[1]
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            self.vx = carSpeed
            self.vy = carSpeed
            self.gameDisplay = gameDisplay
            self.score = 0 
            self.numLives = 3
        except:
            "Problem loading background image and setting instance variables!"

    def draw(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))
        return 

    def move(self, changeX, changeY): 
        if changeX > 0 and self.withinDisplay(changeX, changeY):
            self.x += self.vx
            self.rect.x = self.x
        if changeX < 0 and self.withinDisplay(changeX, changeY):
            self.x -= self.vx
            self.rect.x = self.x
        if changeY > 0 and self.withinDisplay(changeX, changeY):
            self.y -= self.vy
            self.rect.y = self.y
        if changeY < 0 and self.withinDisplay(changeX, changeY): 
            self.y += self.vy
            self.rect.y = self.y
        
        return 
        
    def withinDisplay(self, changeX, changeY):
        width = self.gameDisplay.get_width()
        height = self.gameDisplay.get_height()
        if changeX > 0:
            temp = self.x
            if temp + self.vx > width - self.image.get_width():
                return False
        if changeX < 0:
            temp = self.x
            if self.x - self.vx < 0:
                return False
        if changeY < 0:
            temp = self.y
            if self.y + self.vx > height - self.image.get_height():
                return False
        if changeY > 0:
            temp = self.y
            if temp - self.vy < 0:
                return False
    
        return True

    def incrementScore(self):
        self.score += 1

    def decrementLives(self):
        self.numLives -= 1
    
class Pedestrian(pygame.sprite.Sprite):
    def __init__(self, image, pos, dir, gameDisplay):
        try:
            self.image = pygame.image.load(image)
            self.x = pos[0]
            self.y = pos[1]
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            if dir == 1:
                self.vx = 1
            else:
                self.vx = -1
            self.gameDisplay = gameDisplay
        except:
            print("Unable to load pedestrian image")

    def move(self):
        self.x += self.vx
        self.rect.x = self.x
        return 

    def draw(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))
        return

    def increaseScore(self):
        if self.x <= 0:
            return True
        return False

class ObstacleCar(pygame.sprite.Sprite):

    def __init__(self, image, x, gameDisplay):
        try:
            self.image = pygame.image.load(image)
            self.x = x
            self.y = -self.image.get_height()
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            self.vy = carSpeed
            self.gameDisplay = gameDisplay
        except:
            print("Unable to load obstacle car image")

    def move(self):
        self.y += self.vy
        self.rect.y = self.y
        return 

    def draw(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))
        return

    def increaseScore(self):
        if self.y >= self.gameDisplay.get_height():
            return True
        return False

def numPartitions(gameObject, checkWidth, checkHeight):
    if checkWidth:
        width = gameObject.image.get_width()
        numPartitions = (gameWidth - gameObject.image.get_width()) // gameObject.image.get_width()
        return numPartitions, width
    if checkHeight:
        height = gameObject.image.get_height()
        numPartitions = (gameHeight - gameObject.image.get_height()) // gameObject.image.get_height()
        return numPartitions, height

def gameLoop():

    # Background was made in Paint
    # https://zebdiel.com/2017/09/16/bugatti-chiron-goes-0-249mph-back-to-0-in-42-seconds/ - Source for Player Car

    background = Background("road.png", (0,0), gameDisplay)
    car = Car("cartopview.png", (x,y), gameDisplay)

    testObstacleCar = ObstacleCar("ObstacleCar.png", 200, gameDisplay)
    testPedestrian = Pedestrian("Pedestrian.png", gameWidth + 100, -10, gameDisplay)

    numObstacleCarPartitions, width = numPartitions(testObstacleCar, True, False)
    numPedestrianPartitions, height = numPartitions(testPedestrian, False, True)
    
    playingGame = True

    xMove = 0
    yMove = 0

    obstacles = []

    livesFormatted = "Lives: {0}".format(str(car.numLives))
    livesText = pygame.font.SysFont("Elephant", 40, 0, 0)
    livesDisplayText = livesText.render(livesFormatted, True, (34, 177, 76), (255, 255, 255)) 
    livesDisplayTextRect = livesDisplayText.get_rect()

    scoreFormatted = "Score: {0}".format(str(car.score))
    scoreText = pygame.font.SysFont("Elephant", 40, 0, 0)
    scoreDisplayText = scoreText.render(scoreFormatted, True, (255, 255, 255), (34, 177, 76))
    scoreDisplayTextRect = scoreDisplayText.get_rect()

    # https://purepng.com/photo/5568/transportation-cars-car-top-view - Source for Obstacle Car
    # https://emojipedia.org/apple/ios-9.1/pedestrian/ - Source for Pedestrian 

    while playingGame:

        for i in range(5):
        # Pedestrian - self, image, pos, dir, gameDisplay
            randomDouble = random.uniform(0, 100)
            if randomDouble < 0.5:
                    obstacles.append(Pedestrian("Pedestrian.png", (gameWidth + 100, random.randint(0, numPedestrianPartitions) * height), -10, gameDisplay))
    
        for i in range(5):
            # ObstacleCar - self, image, gameDisplay
            randomDouble = random.uniform(0, 100)
            if randomDouble < 0.5:
                obstacles.append(ObstacleCar("ObstacleCar.png", random.randint(0, numObstacleCarPartitions) * width, gameDisplay))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playingGame = False

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    xMove = -1
                    yMove = 0
                if event.key == K_RIGHT:
                    xMove = 1
                    yMove = 0
                if event.key == K_UP:
                    xMove = 0
                    yMove = 1
                if event.key == K_DOWN:
                    xMove = 0
                    yMove = -1 
            
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    xMove = 0
                if event.key == K_UP or event.key == K_DOWN:
                    yMove = 0 

        car.move(xMove, yMove)
        for obstacle in obstacles:
            obstacle.move()
        gameDisplay.fill(white)
        background.draw()
        car.draw()

        for obstacle in obstacles:
            obstacle.draw()

        # need to check car's y and pedestrian x for score to increase

        for obstacle in obstacles:
            if obstacle.increaseScore():
                car.incrementScore()
                obstacles.remove(obstacle)

        for obstacle in obstacles:
            if car.rect.colliderect(obstacle.rect):
                time.sleep(1)
                pygame.mixer.Sound.play(wilhelmScream)
                car.decrementLives()
                car.x = gameWidth * 0.5 
                car.y = gameHeight * 0.5
                if car.numLives == 0:
                    playingGame = False
                obstacles.clear()
                time.sleep(1)

        
        scoreFormatted = "Score: {0}".format(str(car.score))
        scoreDisplayText = scoreText.render(scoreFormatted, True, (255, 255, 255), (34, 177, 76))
        gameDisplay.blit(scoreDisplayText, (25, 25))

        livesFormatted = "Lives: {0}".format(str(car.numLives))
        livesDisplayText = livesText.render(livesFormatted, True, (255, 255, 255), (34, 177, 76)) 
        gameDisplay.blit(livesDisplayText, (gameWidth - livesDisplayText.get_width() - 25, 25))

        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
