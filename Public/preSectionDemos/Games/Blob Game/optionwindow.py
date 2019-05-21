from zellegraphics import *
from time import sleep

class Button:
    def __init__(self,text,startpoint,sizex,sizey):
        "text,startpoint,sizex,sizey"
        self.text = text
        self.sizex = sizex
        self.sizey = sizey
        self.p1 = startpoint
        self.p2 = Point(startpoint.getX()+sizex , startpoint.getY()+sizey)
        self.center = Point(self.p1.getX()+sizex/2 , self.p1.getY()+sizey/2)
        self.box = Rectangle(self.p1, self.p2)
        self.box.setFill('white')
        self.text = Text(self.center, text)
    def button_draw(self,window):
        self.box.draw(window)
        self.text.draw(window)
    def button_undraw(self):
        self.box.undraw()
        self.text.undraw()
    def button_check_click(self,point):
        box_left_bound = self.p1.getX()
        box_right_bound = self.p2.getX()
        box_upper_bound = self.p2.getY()
        box_lower_bound = self.p1.getY()
        point_x = point.getX()
        point_y = point.getY()
        collision_number = 0
        if box_left_bound < point_x:
            collision_number = collision_number + 1
        if box_right_bound > point_x:
            collision_number = collision_number + 1
        if box_upper_bound > point_y:
            collision_number = collision_number + 1
        if box_lower_bound < point_y:
            collision_number = collision_number + 1
        if collision_number == 4:
            return True
        else:
            return False        

if __name__ == '__main__':
    mouseclick = False
    win = GraphWin("w",400,400)
    walk = catabutton("Hello,World!",Point(100,100),100,50)
    walk.button_draw(win)
    while mouseclick == False:
        if walk.button_check_click(win.getMouse()):
            mouseclick = True
            print('success')
            sleep(4)
        else:
            pass
    win.close()