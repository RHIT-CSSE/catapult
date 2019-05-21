from zellegraphics import *
import random, time
from LinkedList import *
from winsound import Beep
from Beeper import *
from APBeeper import *

moving = LinkedList()

class Game:
    def __init__(self,blobFill,width=0,fullsize=4,numblocks=8,turns=20):
        "blobFill(matrix),win,x,y,fullsize,numblocks,turns"
        self.fullsize = fullsize
        self.numblocks = numblocks
        if blobFill != None:
            self.numblocks = len(blobFill)
        if blobFill == None:
            width = 700
            self.blobFill = None
        self.turns = turns
        self.combo = 0
        self.displayturns = Text(Point(650, 100), "Turns:\n" + str(self.turns))
        self.combonum = Text(Point(650, 200), "Combo:\n" + str(self.combo))
        self.x = width
        self.y = self.x
        self.win = GraphWin("The BLOB GAME",self.x,self.y)
        self.blocksize = (self.x-100) / self.numblocks
        self.boardsize = self.blocksize*self.numblocks
        self.blob = [[0 for i in range(self.numblocks)] for i in range(self.numblocks)]
        self.blocks = [[0 for i in range(self.numblocks)] for i in range(self.numblocks)]
        if blobFill != None:
            self.blobFill = blobFill
            self.blocks = self.blobFill
    def distance (self, point1, point2):
        return math.sqrt((point1.getX() - point2.getX()**2) +
                         (point1.getY() - point2.getY())**2)

##find what block a click is in
    def findblock(self,point):
        blockx = -1
        blocky = -1
        for i in range(self.numblocks):
            if i * self.blocksize + self.blocksize > point.getX():
                blockx = i
                break
        for i in range(self.numblocks):
            if i * self.blocksize + self.blocksize > point.getY():
                blocky = i
                break
        return blockx, blocky

##draw the board
    def drawlines(self,win):
        for i in range(self.numblocks):
            linev = Line(Point(i * self.blocksize, 0), Point(i * self.blocksize, self.y))
            lineh = Line(Point(0, i * self.blocksize), Point(self.x, i * self.blocksize))
            coverpoly = Polygon(Point(self.boardsize,0),Point(self.boardsize+100,0),Point(self.boardsize+100,self.boardsize+100),
                                Point(0,self.boardsize+100),Point(0,self.boardsize),Point(self.boardsize,self.boardsize))
            coverpoly.setFill(color_rgb(255,255,255))
            linev.draw(win)
            lineh.draw(win)
            coverpoly.draw(win)

##generate the blobs
    def generateblobs(self):
        i = 0
        while i < 100:
            p = Point(random.randint(0,self.numblocks-1),
                      random.randint(0,self.numblocks-1))
            if self.blocks[p.getX()][p.getY()] < self.fullsize:
                self.blocks[p.getX()][p.getY()] = self.blocks[p.getX()][p.getY()] + 1
                i = i+1
        

    def drawblobs(self,win):
        for i in range(self.numblocks):
            for j in range(self.numblocks):
                if self.blocks[i][j] != 0:
                    self.blob[i][j] = blobs(i+1,j+1,self.blocks[i][j],self)
                    self.blob[i][j].draw(win)

    def expand(self, blockx, blocky,win):
        if self.blocks[blockx][blocky] == 0:
            return
        if self.blocks[blockx][blocky] < self.fullsize:
            blorb = APBeeper(400,50)
            blorb.start()
            self.blocks[blockx][blocky] = self.blocks[blockx][blocky] + 1
            self.blob[blockx][blocky].expand(win)
        else:
            blorb = APBeeper(100,50)
            blorb.start()
            self.explode(blockx, blocky,win)

    def explode(self, blockx, blocky,win):
        self.blob[blockx][blocky].undraw()
        self.blob[blockx][blocky].explode(win, blockx, blocky)
        if self.blobFill == None:
            self.combo = self.combo + 1
            if self.combo%3 == 0:
                self.turns = self.turns + 1
                self.combonum.undraw()
                self.combonum = Text(Point(650, 250), "combo:\n" + str(self.combo))
                self.combonum.draw(win)
            
    
    
    def run(self):
        b = Beeper()
        b.start()
        for i in range(self.numblocks):
            for j in range(self.numblocks):
                self.blob[i][j] = blobs(i+1,j+1,0,self)
        self.drawlines(self.win)
        #print type(self.blocks)
        if  self.blocks != self.blobFill:
            self.generateblobs()
        self.drawblobs(self.win)
        self.displayturns.draw(self.win)
        self.combonum.draw(self.win)
        while True:
            self.combo = 0
            self.combonum.undraw()
            self.combonum = Text(Point(self.boardsize + 50, self.boardsize*1/4), "combo:\n" + str(self.combo))
            self.combonum.draw(self.win)
            self.displayturns.undraw()
            self.displayturns = Text(Point(self.boardsize + 50, self.boardsize*3/4), "turns:\n" + str(self.turns))
            self.displayturns.draw(self.win)
            if self.turns == 0:
                break
            point = self.win.getMouse()
            a, b = self.findblock(point)
            if a >= 0 and b >= 0:
                if self.blob[a][b].drops > 0:
                    self.turns = self.turns - 1
                self.expand(a,b,self.win)
            while len(moving) > 0:
                curNode = moving.getFirst()
                while curNode != None:
                    curNode.element.move()
                    curNode = curNode.getNext()
                time.sleep(1.0/24)
            clear = []
            for i in range(self.numblocks):
                for j in range(self.numblocks):
                    clear.append(self.blocks[i][j])
            if clear.count(0) == self.numblocks * self.numblocks:
                time.sleep(2)
                self.win.close()
                return True
            if self.turns == 0:
                return False             
                        
class Mover:
    def __init__(self,centerpoint,radius,direction,blobs,game):
        self.centerpoint = centerpoint
        self.radius = radius
        self.direction = direction
        self.boardsize = game.boardsize
        self.findblock = game.findblock
        self.game = game
        self.blob = game.blob
        self.shot = Circle(centerpoint, radius)
        #self.shot.setFill('red')
        self.shot.setOutline('red')
        
        self.velocity = 5
        
        if self.direction == 0:
            self.vy = -self.velocity
            self.vx = 0
        if self.direction == 1:
            self.vy = 0
            self.vx = self.velocity
        if self.direction == 2:
            self.vy = self.velocity
            self.vx = 0
        if self.direction == 3:
            self.vy = 0
            self.vx = -self.velocity
            

    def move(self):
        self.shot.move(self.vx,self.vy)
        if self.shot.getCenter().getX() >= self.boardsize or self.shot.getCenter().getY() >= self.boardsize or self.shot.getCenter().getX() <= 0 or self.shot.getCenter().getY() <= 0:
            moving.remove(self)
            self.shot.undraw()
        else:
            a,b = self.findblock(self.shot.getCenter())
            if     self.blob[a][b].drops > 0:
                moving.remove(self)
                self.shot.undraw()
                self.game.expand(a,b,self.game.win)
                
            def draw(self,win):
                self.shot.draw(win)
    
            def undraw(self):
                self.shot.undraw()

class blobs:
    def __init__(self,boxx,boxy,drops,game):
        self.boxx = (boxx - 1)
        self.boxy = (boxy - 1)
        self.game = game
        self.centerpoint = Point(self.boxx * game.blocksize + (.5 * game.blocksize),
                                 self.boxy * game.blocksize + (.5 * game.blocksize))
        self.drops = drops
    # initialize drawable parts
        self.blob = Circle(self.centerpoint, self.drops * (game.blocksize/(game.fullsize * 2)))
        self.blob.setFill('red')

    def draw(self, win):
        self.blob.draw(win)

    def undraw(self):
        self.blob.undraw()

    def expand(self, win):
        self.drops = self.drops + 1
        self.blob.undraw()
        self.blob = Circle(self.centerpoint, self.drops * (self.game.blocksize/(self.game.fullsize * 2)))
        self.blob.setFill('red')
        self.blob.draw(win)
    def explode(self, win, blockx, blocky):
        global moving
        self.drops = 0
        self.game.blocks[blockx][blocky] = self.drops
        for i in range(4):
                dot = Mover(self.centerpoint, 5, i,self,self.game)
                moving.add(dot)
                dot.shot.draw(win)


