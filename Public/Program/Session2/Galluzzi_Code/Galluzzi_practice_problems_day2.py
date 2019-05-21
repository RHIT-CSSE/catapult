import zellegraphics as zg
import time

'''********************
Description: Moves a circle from the upper
left corner of the window to the lower
right corner.
Inputs: zellegraphics window
Outputs: None
Side effects: Makes a circle on a window and
moves it diagonally
********************'''
def diagonalCircle(win):
    #Get the width and height of the window
    width=win.getWidth()
    height=win.getHeight()
    #Make a circle at the upper left hand corner of the window
    circle=zg.Circle(zg.Point(0,0),30)
    circle.setFill('blue')
    circle.draw(win)
    #Repeatedly move the circle until it hits the lower right corner
    while (circle.getCenter().x<width and circle.getCenter().y<height):
        #Note the use of integer division to get whole numbers.
        #The +1 is added because it is possible for both to be 0!
        #Is there a more elegant way to do this (hint: yes)--see
        #if you can think of one!
        circle.move(width//50+1,height//50+1)

        time.sleep(.1)
#Testing diagonalCircle
print("Testing the diagonalCircle function")
win1=zg.GraphWin("First Test",200,200)
diagonalCircle(win1)
win2=zg.GraphWin("Second Test",200,400)
diagonalCircle(win2)
win3=zg.GraphWin("Third Test",49,49) #49//50 will result in 0
diagonalCircle(win3)

'''********************
Description: Changes the colors of the circles
in the list
Inputs: a list of circles
Outputs: None
Side effects: Changes the colors of the circles
********************'''
def changeColors(circles):
    for c in circles:
        c.setFill('red')
#Testing changeColors
print("Testing the changeColors function")
win4=zg.GraphWin("Testing changeColors")
circleList1=[zg.Circle(zg.Point(10,10),5),zg.Circle(zg.Point(30,30),10),zg.Circle(zg.Point(50,50),15)]
for c in circleList1:
    c.draw(win4)
time.sleep(.5)
changeColors(circleList1)

'''********************
Description: This class represents a car as a graphical object.
********************'''
class Car:
    '''********************
    Description: This is the constructor which makes an instance of a Car
    Inputs: the center of the car
    Outputs: None
    Side effects: Sets the correct values in the given car
    ********************'''
    def __init__(self,center):
        self.body=zg.Rectangle(zg.Point(center.x-20,center.y-10),zg.Point(center.x+20,center.y+10))
        self.body.setFill('Red')
        self.tire1=zg.Circle(zg.Point(center.x-20,center.y+10),5) #Make a tire at one point of the body
        self.tire2=zg.Circle(zg.Point(center.x+20,center.y+10),5) #Make a tire on the other side of the bottom
        self.tire1.setFill('Black')
        self.tire2.setFill('Black')
        self.carShapes=[self.body,self.tire1,self.tire2]
    '''********************
    Description: Draws the car
    Inputs: A zellegraphics window
    Outputs: None
    Side effects: The car appears on the given window
    ********************'''
    def draw(self, win):
        for s in self.carShapes:
            s.draw(win)
    '''********************
    Description: Changes the car's color
    Inputs: The new color as a string
    Outputs: None
    Side effects: The car changes color
    ********************'''
    def color(self,color):
        self.body.setFill(color)
    '''********************
    Description: Moves the car
    Inputs: The distance to move in the x and y direction
    Outputs: None
    Side effects: The car moves
    ********************'''
    def move(self,x,y):
        for s in self.carShapes:
            s.move(x,y)
    
#Test the car class
print("Testing the car class")
w=zg.GraphWin("Cars!",400,200)
car1=Car(zg.Point(100,50))
car2=Car(zg.Point(200,100))
car3=Car(zg.Point(300,50))
car1.draw(w)
car2.draw(w)
car3.draw(w)
time.sleep(.5)
car1.color('Blue')
car2.color('Silver')
car3.color('Yellow')
time.sleep(.5)
car1.move(10,0)
car2.move(10,0)
car3.move(10,0)
time.sleep(.5)
car1.move(0,10)
car2.move(10,0)
car3.move(0,-10)
