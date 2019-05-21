import zellegraphics as zg
import time

class Box:
    '''********************
    Description: The __init__ function will set the variables
    of a given class instance.
    Inputs: upper-left and lower-right corners of box
    Outputs: None
    Side effects: Sets variables in this Box instance
    ********************'''
    def __init__(self, p1, p2):
        #Creates a square that will represent this box.
        self.representation = zg.Rectangle(p1,p2)
        self.representation.setFill('brown')
        #Gives us a variable "center" that is the center of the box
        self.center = self.representation.getCenter()
        #Sets up a list of our contents (right now there is nothing)
        self.contents=[]
    '''********************
    Description: Draws this box
    Inputs: zellegraphics window
    Outputs: None
    Side effects: shows box on screen
    ********************'''    
    def draw(self, win):
        self.representation.draw(win)
    '''********************
    Description: Adds shape to the box
    Inputs: shape to be added
    Outputs: None
    Side effects: Changes location of the shape to be inside the box
    ********************'''
    def add(self, shape):
        #Move the shape to (0,0)
        shape.move(-shape.getCenter().x, -shape.getCenter().y)
        #Move the shape to the center of the box
        shape.move(self.center.x, self.center.y)
        #Add the shape to the contents list
        self.contents = self.contents + [shape]
    '''********************
    Description: Changes the color of all shapes to given color
    Inputs: color to be changed to (as string)
    Outputs: None
    Side effects: Changes the colors of shapes in the box
    ********************'''
    def colorContents(self, color):
        #Going through each shape in the box
        for shape in self.contents:
            shape.setFill(color)

def run():
    #Make the first box
    b=Box(zg.Point(100,100),zg.Point(200,150))
    #Make a new window
    w=zg.GraphWin(title="Box!",height=300,width=300)
    #Draw the first box on the window
    b.draw(w)
    #Make a second box
    b2=Box(zg.Point(250,250),zg.Point(300,300))
    #Draw the second box on the window
    b2.draw(w)
    #Make a green circle on the upper-left hand corner of the window
    c=zg.Circle(zg.Point(10,10),40)
    c.setFill('green')
    c.draw(w)
    time.sleep(1)
    #Add the circle to the box
    b.add(c)
    #Make a yellow circle on the lower-left hand corner of the window
    c2=zg.Circle(zg.Point(10,300),20)
    c2.setFill('yellow')
    c2.draw(w)
    time.sleep(1)
    #Add that circle to the box
    b.add(c2)
    time.sleep(1)
    #Make shapes contained in the box turn blue
    b.colorContents('blue')
