from zellegraphics import *
import time

win = GraphWin("House Drawing", 1280, 720)

sky = Rectangle(Point(0, 0), Point(1280, 400))
sky.draw(win)
sky.setFill(color_rgb(12,121, 245))
sky.setOutline(color_rgb(12,121, 245))

cloud = Oval(Point(40, 40), Point(200, 100))
cloud.draw(win)
cloud.setFill("white")
cloud.setOutline("white")

cloud2 = cloud.clone()
cloud2.draw(win)
cloud2.move(40, 30)

cloud3 = cloud.clone()
cloud3.draw(win)
cloud3.move(60, -20)

cloud4 = cloud.clone()
cloud4.draw(win)
cloud4.move(110, 10)

lawn = Rectangle(Point(0, 400), Point(1280, 720))
lawn.draw(win)
lawn.setFill(color_rgb(12, 179, 34))
lawn.setOutline(color_rgb(12, 179, 34))

base = Rectangle(Point(460, 320), Point(820, 680))
base.draw(win)
base.setFill(color_rgb(198, 13, 13))

brick_horizontal = Line(Point(460, 320), Point(820, 320))
brick_horizontal.draw(win)

y = 20
while(y < 360):
    temp = brick_horizontal.clone()
    temp.draw(win)
    temp.move(0, y)
    y += 20

brick_vertical = Line(Point(460, 320), Point(460, 340))
brick_vertical.draw(win)

temp = brick_vertical.clone()
row = 0
x = 0
while(row <= 17):
    if(row % 2 == 0):
        x = 40
        for i in range(9):
            temp = brick_vertical.clone()
            temp.draw(win)
            temp.move(x, row * 20)
            x += 40
    if(row % 2 != 0):
        x = 20
        temp = brick_vertical.clone()
        temp.draw(win)
        temp.move(x, row * 20)
        x = 40
        for j in range(8):
            temp2 = temp.clone()
            temp2.draw(win)
            temp2.move(x, 0)
            x += 40
    row += 1


chimney = Rectangle(Point(760, 320), Point(800, 180))
chimney.draw(win)
chimney.setFill("gray")

roof = Polygon(Point(460, 320), Point(640, 100), Point(820,320))
roof.draw(win)
roof.setFill(color_rgb(48, 46, 43))

door = Rectangle(Point(610, 680), Point(670, 560))
door.draw(win)
door.setFill(color_rgb(111, 61, 5))

path = Rectangle(Point(610, 720), Point(670, 681))
path.draw(win)
path.setFill("gray")
path.setOutline("gray")

knob = Circle(Point(655, 620), 3)
knob.draw(win)
knob.setFill("gold")

window1 = Rectangle(Point(510, 400), Point (570, 480))
window1.draw(win)
window1.setFill(color_rgb(12,121, 245))

window_vertical = Line(Point(540, 400), Point(540, 480))
window_vertical.draw(win)
window_vertical.setWidth(2)
window_horizontal = Line(Point(510, 440), Point(570, 440))
window_horizontal.draw(win)
window_horizontal.setWidth(2)

window2 = window1.clone()
window2.draw(win)
window2.move(200, 0)

window_vertical2 = window_vertical.clone()
window_vertical2.draw(win)
window_vertical2.move(200, 0)
window_horizontal2 = window_horizontal.clone()
window_horizontal2.draw(win)
window_horizontal2.move(200, 0)
