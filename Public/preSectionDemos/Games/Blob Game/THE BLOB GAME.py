from theBlobClass import *
from optionwindow import *
from levelpack import *
import sys
from copy import copy

blob=[]
x,y = 700,700
stillplaying = True

def victory(haswon):
    if haswon == True:
        win3 = GraphWin("Victory", 400, 200)
        wintext = Text(Point(200, 100), "You Have Won")
        wintext.setStyle("bold")
        wintext.setSize(36)
        wintext.draw(win3)
        time.sleep(5)
        win3.close()
def lost():
    if not haswon:
        game.win.close()
        win3 = GraphWin("YOU LOSE! GAME OVER, MAN! GAME OVER!",400,200)
        again = Button("play again",Point(50,50),100,50)
        again.button_draw(win3)
        quit = Button("quit",Point(250,50),100,50)
        quit.button_draw(win3)
        credits = Button("Credits", Point(150, 150), 100, 50)
        credits.button_draw(win3)
        click = win3.getMouse()
        if credits.button_check_click(click) == True:
            win4 = GraphWin("Credits", 400, 200)
            credtext = Text(Point(200, 50), "Date Started: 6/19/2007 \n Date Completed: 6/27/2007 \n Coded By: \n Andrew Miller \n Richard Neal")
            credtext.draw(win4)
            time.sleep(5)
            win.close()
        if again.button_check_click(click) == True:
            again = True
            win3.close()
            return again
        else:
            stillplaying = False
            sys.exit(0)
              
while stillplaying:
    win2 = GraphWin("Make your choice puny mortal",400,200)
    puzzlemode = Button("puzzle mode",Point(50,50),100,50)
    puzzlemode.button_draw(win2)
    arcademode = Button("arcade mode",Point(250,50),100,50)
    arcademode.button_draw(win2)
    
    while True:
        click = win2.getMouse()
        if puzzlemode.button_check_click(click) == True or arcademode.button_check_click(click) == True:
            win2.close()
            break
    if puzzlemode.button_check_click(click) == True:
        again = False   
        for i in range(len(levels)):
            copyarray = [[0 for j in range(len(levels[i]))] for k in range(len(levels[i][0]))]
            for q in range(len(copyarray)):
                for r in range(len(copyarray[0])):
                    copyarray[q][r] = levels[i][q][r]
            game = Game(copyarray,widthlist[i],4,0,turnlist[i])
            haswon = game.run()
            again = lost()
            if again == True:
                break
        victory(haswon)
    if arcademode.button_check_click(click) == True:
        game = Game(None)
        haswon = game.run()
        stillplaying = lost()
        victory(haswon)
            


