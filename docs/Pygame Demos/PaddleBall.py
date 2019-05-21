'''
Starting point for the PaddleBall game.

Created on Jun 21, 2010

@author: Matt Boutell
'''

import pygame
from pygame.locals import *
from time import time, sleep
from random import random, randrange, triangular
import math


SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
PADDLE_OFFSET = 100
PADDLE_SPEED = 2
BALL_OFFSET = 100
BALL_MOVEMENT_INTERVAL = 0.03
BALL_CREATION_INTERVAL = 4
BALL_MOVEMENTS_PER_CREATION = BALL_CREATION_INTERVAL / BALL_MOVEMENT_INTERVAL
NUM_STARS = 50

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Helper functions
def distance(p1, p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    return math.sqrt(dx*dx + dy*dy)

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def scalarMultiply(v, k):
    return [v[0] * k, v[1] * k]

def vectorAdd(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]


class Paddle:
    """ A paddle that is controllable by the user """
    WIDTH = 60
    HEIGHT = 20
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.bbox = []
        
    def draw(self, surface):
        self.bbox = pygame.draw.rect(surface, [128, 128, 0], [self.x,self.y,Paddle.WIDTH, Paddle.HEIGHT])
        pygame.draw.rect(surface, [255, 255, 128], [self.x,self.y,Paddle.WIDTH, Paddle.HEIGHT], 3)
        
    def setMoving(self, vx):
        self.vx = vx
        
    def move(self):
        self.x += self.vx
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - Paddle.WIDTH:
            self.x = SCREEN_WIDTH - Paddle.WIDTH
 
class Star:
    def __init__(self):
        self.x = random() * SCREEN_WIDTH
        self.y = triangular(0, SCREEN_HEIGHT, 0.1 * SCREEN_HEIGHT) 
        self.radius = 1.5 + random() * 1.5
        
    def draw(self, surface):
        pygame.draw.circle(surface, [255, 255, 255], [int(self.x), int(self.y)], int(self.radius))
 
class Ball:
    """ A single moving ball """
    RADIUS = 15
    INIT_X, INIT_Y = SCREEN_WIDTH/2, BALL_OFFSET

    def __init__(self):
        self.x = Ball.INIT_X
        self.y = Ball.INIT_Y
        self.vx = random() * 4 - 2
        self.vy = random() * 2 + 2 
        self.bbox = []
        self.radius = randrange(10,20)
        self.mass = math.pi * self.radius**2 # constant density
        self.color = [randrange(32, 256), randrange(32, 256), randrange(32, 256)]
    def draw(self, surface):
        self.bbox = pygame.draw.circle(surface, self.color, [int(self.x), int(self.y)], self.radius)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounces off side walls
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.vx = -self.vx
        
        # Bounces off top
        if self.y - self.radius < 50:
            self.vy = -self.vy

        # Acceleration due to gravity
        self.vy += 0.02

    def moveBackwards(self):
        self.x -= self.vx
        self.y -= self.vy

        # Bounces off side walls
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.vx = -self.vx
        
        # Bounces off top
        if self.y - self.radius < 50:
            self.vy = -self.vy

        # CONSIDER: delete?
        # Acceleration due to gravity
        self.vy -= 0.02

    def stop(self):
        self.vx, self.vy = 0, 0

    def isCollide(self, other):
        return distance([self.x, self.y], [other.x, other.y]) < self.radius + other.radius

    def elasticCollide(self,other):
        """2D elastic collision, using only normal and tangent vectors.
        Much simpler than alternatives I've seen, since no trig. From 
        http://www.vobarian.com/collisions/2dcollisions2.pdf """  
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        v1 = [self.vx, self.vy]
        v2 = [other.vx, other.vy]
        m1 = self.mass
        m2 = other.mass
        
        # 1. Find normal and tangent unit vectors
        n = [x2-x1, y2-y1]
        nMag = math.sqrt(n[0]**2 + n[1]**2)
        n = [n[0]/nMag, n[1]/nMag]
        t = [-n[1], n[0]]
        
        # 2. Project velocities onto normal and tangent vectors
        v1n = dot(v1, n)
        v1t = dot(v1, t)
        v2n = dot(v2, n)
        v2t = dot(v2, t)
        
        # 3. Find new normal velocity scalars
        v1nNew = (v1n * (m1 - m2) + 2 * m2 * v2n)/(m1 + m2)
        v2nNew = (v2n * (m2 - m1) + 2 * m1 * v1n)/(m1 + m2)
        
        # 4. Find new velocity vector (normal component)
        v1n = scalarMultiply(n, v1nNew)
        v2n = scalarMultiply(n, v2nNew)
         
        # 5. Repeat for tangent velocities 
        # No force is applied in tangent direction, so scalars remain the same
        v1t = scalarMultiply(t, v1t)
        v2t = scalarMultiply(t, v2t)
        
        # 6. Combine normal and tangent vectors
        v1 = vectorAdd(v1n, v1t)
        v2 = vectorAdd(v2n, v2t)
        
        # 7. Copy back to the balls as their new velocities
        self.vx = v1[0]
        self.vy = v1[1]
        other.vx = v2[0]
        other.vy = v2[1]

class Planet(Ball):
    def __init__(self):
        self.hasRing = False
        if random() < 0.2:
            self.hasRing = True
        Ball.__init__(self)

    def draw(self, surface):
        Ball.draw(self, surface)
        if self.hasRing:
            start = [int(self.x - 1.5 * self.radius), int(self.y + 0.5 * self.radius)]
            end = [int(self.x + 1.5 * self.radius), int(self.y - 0.5 * self.radius)]
            pygame.draw.line(surface, [255, 255, 255], start, end, 2)

def checkPaddleCollisions(paddle, balls):
    ballLocations = [b.bbox for b in balls]
    whichCollided = paddle.bbox.collidelist(ballLocations)
    score = 0
    if whichCollided > -1:
# Attempted hack
#        while balls[whichCollided].y >= paddle.y:
#            balls[whichCollided].moveBackwards()
#        balls[whichCollided].vy *= -1 # bounce
#        balls[whichCollided].vy += 0.1 # friction
# original
        balls[whichCollided].vy *= -1 # bounce
        balls[whichCollided].y -= 2 # move up past paddle if overlap slightly
        balls[whichCollided].vy += 0.1 # friction
        score = len(balls)
    return score

def checkBallCollisions(balls):
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            collide = balls[i].isCollide(balls[j])
            if collide:
                balls[i].moveBackwards()
                balls[j].moveBackwards()
                balls[i].elasticCollide(balls[j])
    
def createStars():
    stars = []
    for i in range(NUM_STARS):
        stars.append(Star())
    return stars
    
def eventLoop():
    message = "PaddleBall!"
    startTime = time()
    ballCreationCounter = 0
    paddle = Paddle(SCREEN_WIDTH/2 - Paddle.WIDTH/2, SCREEN_HEIGHT - PADDLE_OFFSET)
    balls = [Planet()]
    stars = createStars()
    score = 0
    paused = False
    keyCount = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_LEFT:
                paddle.setMoving(-PADDLE_SPEED)
                keyCount += 1
            if event.type == KEYDOWN and event.key == K_RIGHT:
                paddle.setMoving(PADDLE_SPEED)
                keyCount += 1
            if event.type == KEYDOWN and event.key == K_SPACE:
                paused = not paused
            if event.type == KEYUP: 
                keyCount -= 1
            if keyCount == 0:
                paddle.setMoving(0)

       
        if not paused:    
            screen.fill([0,0,0])
            for star in stars:
                star.draw(screen)
            paddle.move()
            paddle.draw(screen)
            elapsedTime = time() - startTime
            # Move the balls at regular intervals
            if elapsedTime > BALL_MOVEMENT_INTERVAL:
                ballCreationCounter += 1
                if ballCreationCounter > BALL_MOVEMENTS_PER_CREATION:
                    balls.append(Planet())
                    ballCreationCounter = 0
                #print("moving")
                for ball in balls:
                    ball.move()
                startTime = time()
            for ball in balls:
                ball.draw(screen)
            
            # Check for collisions and increment the score by the number of balls out there.
            score += checkPaddleCollisions(paddle, balls)
            checkBallCollisions(balls)
    
    
            # Remove balls that go off the screen
            #for i in range(len(balls):
            for ball in balls:
                if ball.y > SCREEN_HEIGHT:
                    balls.remove(ball)
            
            message = 'Score: {0}'.format(str(score)) 
            # Draw the score
            font = pygame.font.SysFont("Century Gothic", 24, bold=True, italic=False)
            scoreText = font.render(message, True, [255, 255, 0])
            screen.blit(scoreText, [20, 20])
            
            pygame.display.update()        
    
            # end game if no more balls
            if len(balls) < 1:
                message = 'Game Over: {0}'.format(str(score)) 
                font = pygame.font.SysFont("Century Gothic", 36, bold=True, italic=False)
                scoreText = font.render(message, True, [255, 255, 0])
                screen.blit(scoreText, [0, SCREEN_WIDTH/2])
                pygame.display.update()        
                sleep(3)
                return
        

        
eventLoop()


        
