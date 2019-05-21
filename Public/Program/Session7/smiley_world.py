'''  
description:
    This module exercises the Smiley class by creating several graphical and animated scenes.
    
    The user is asked to select from among 4 scenes to illustrated the behavior of the Smiley objects.

@author: Claude Anderson, created on Nov 5, 2009. Delvin Defoe and David Mutchler, October, 2010
'''

from smileySolution import Smiley
import time
from zellegraphics import GraphWin, Text, Point


def runCollisionScene(smileys, steps):
    '''move the smileys in the list until time runs out or until
       all have collided (and therefore stopped).
       Notice the frowns after collisions!'''
    win=GraphWin("", 400, 400)
    
    # This text message gets displayed if all of the smileys crash.
    t=Text(Point(200, 40), "PileUp!!")
    t.setSize(30)
    t.setFace('arial')
    t.setStyle('bold')
    t.setFill('blue3')
    
    # Number of smileys that have not crashed
    moverCount = 0; 

    # Draw them all and count how many are moving.
    for s in smileys:
        s.draw(win)
        if s.isMoving():
            moverCount +=1

    for i in range(steps):  
        # Move all smileys and check for collisions
        if moverCount==0:
            break
        for s in smileys:  # Move them
            s.move()
        for i in range(len(smileys)): # Check for collisions
            for j in range(i+1, len(smileys)): # Avoid comparing to self (and duplicate checks).
                if smileys[i].collidedWith(smileys[j]):
                    for k in [i, j]:  # Stop both of them.
                        if smileys[k].isMoving():
                            smileys[k].frown()
                            smileys[k].stop()
                            moverCount -= 1
                            
        time.sleep(1.0/24.0) # Pause before next iteration.
   
    if moverCount == 0: # All smileys have crashed!.
        t.draw(win)
    win.getMouse()
    win.close()

def scene1():  
    ''' Show the basic setup and movement of smiley faces without complex logic. '''
    s1 = Smiley(50, 50, 2, 2)
    s2 = Smiley(5, 130, 5, 2, 60, 'green', False)
    win=GraphWin("", 400, 400)
    smileys = [s1]
    s1.draw(win)
    s2.draw(win)    
    smileys.append(s2)   
    for i in range(70): #@UnusedVariable
        for s in smileys:
            s.move()
        time.sleep(0.05)
    s1.frown()
    s2.smile()
    win.getMouse()
    win.close()

def scene2():
    ''' tests the runCollisionScene with 4 smiley faces and 150 steps '''
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -1, 4, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     150)


def scene3():
    ''' tests the runCollisionScene with 4 smiley faces and 200 steps '''
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -2, 4, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     200 )

def scene4():
    ''' tests the runCollisionScene with 4 smiley faces and 200 steps '''
    runCollisionScene([Smiley(130, 200, 4, 3, 60, 'pink'),
                       Smiley(300, 70, -1, 5, 25, 'blue'),
                       Smiley(70, 350, 3, 0, 40, 'red')], 
                     250 )
    


def main():
    '''
        Tests the implementation of the Smiley class functions.
    '''  
    scenes = [scene1, scene2, scene3, scene4]
    print("There are several Smiley Face scenes that you can explore.")
    scene = int(input('Which scene do you want? (1, 2, 3, or 4): '))
    if 1 <= scene <= len(scenes):
        scenes[scene-1]()    
    
if __name__ == '__main__':
    main()

    