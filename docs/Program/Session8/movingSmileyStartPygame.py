'''
Created on Jun 19, 2011

@author: chenowet
'''
# Moving smiley program to illustrate objects and how they can interact.
# Original by Claude Anderson.  June 16, 2007
# Modified by Michael Boland

import math, pygame
from pygame.locals import *

def translate(point, dx, dy):
    'return a point that is a translation of point by deltas dx and dy'
    return (point[0]+dx, point[1]+dy)

def distance (point1, point2):
    'return the distance between point1 and point2'
    return math.sqrt((point1[0] - point2[0])**2 +
                     (point1[1] - point2[1])**2)

class Smiley:
    """ A Smiley is a smiley-face object that is capable of moving.
        FIELDS:
          centerPoint: center of this smiley
          dx, dy, amount the smiley moves each step
          size: radius of this smiley
          isSmiling, isMoving: booleans indicating current dynamic state.
          
    """ 
    def __init__ (self, initX, initY, dx, dy, size=40, color='red', isSmiling='true'):
        self.dx = dx
        self.dy = dy
        self.size = size
        #three ways to get colors - pygame.Color(name), pygame.Color(hex value), or just straight RGB values
        #example: pygame.Color('blue'), pygame.Color(0x0000FF), and (0,0,255) all give the exact same shade of blue
        #a list of available color names is at http://www.mcfedries.com/books/cightml/x11color.htm
        self.color = pygame.Color(color)
        self.isSmiling = isSmiling
        self.moving = True
        self.centerPoint = (initX,initY)

    # TODO: Add draw method
    def draw(self, surface):
        pass
                
    # TODO: Add move method
    def move(self):
        pass
    
    # TODO: Add smile method
    def smile(self):
        pass
    
    # TODO: Add frown method
    def frown(self):
        pass
    
    # TODO: Add stop method
    def stop(self):
        pass
    
    # TODO: Add isMoving method
    def isMoving(self):
        pass
    
    # TODO: Add colldeWith method
    def collideWith(self, otherSmiley):
        pass
    

def scene1():  # to show the basic setup and movement, without complex logic.
    s1 = Smiley(50, 50, 2, 2)
    s2 = Smiley(130, 130, 5, 2, 60, 'green', False)
    #pygame.init() lets pygame set up all of the stuff it needs to before it can run properly
    pygame.init()
    #this is analogous to creating a GraphWin in Zelle's library
    #the first argument is a tuple or list for the size of the window in pixels
    #the second argument is special flags for setting whether the window is full screen, resizable, etc. - 0 gives a normal default window
    #the last argument is the bit depth for the colours - it doesn't matter if you understand what that means or not, just know that 32 means you can use transparency
    #this returns a pygame Surface object, which we can then use to paint on
    screen = pygame.display.set_mode((400,400),0,32)
    #set_caption sets the title of the window
    pygame.display.set_caption('Smilies!')
    smileys = [s1, s2]
    #screen.fill fills in the whole picture with the given colour
    screen.fill(pygame.Color('white'))
    #we draw these two smileys by passing the screen to their draw functions
    s1.draw(screen)
    s2.draw(screen)
    #after drawing, we need to call update so all the changes will take effect on the screen
    pygame.display.update()
    for i in range(70):
        #If we don't clear out the screen every frame, we just draw on top of the last one! Comment out this line to see what I mean.
        screen.fill(pygame.Color('white'))
        for s in smileys:
            s.move()
            #a big difference between pygame and Zelle is that we have to redraw our smiles after we move them for the change to happen
            s.draw(screen)
        #once again, we need to use update so our changes are reflected on the screen
        pygame.display.update()
        #this does the same thing as time.sleep, but we'll use the pygame version so it plays nicely with pygame
        pygame.time.delay(50)
        
    #this is somewhat similar to using getMouse, but it doesn't pause waiting for input and it also applies to every possible kind of input
    event = pygame.event.poll()
    #every event has a type - in this case, we only care about QUIT type events
    #as long as our event type isn't QUIT, we pause and then check the event again
    while event.type != QUIT:
        #delay does the same thing as sleep, but it takes an integer amount of milliseconds as its argument
        pygame.time.delay(100)
        event = pygame.event.poll()

def runCollisionScene(smileys, steps):
    '''move the smileys in the list until time runs out or until
       all have collided (and therefore stopped).
       Notice the frowns after collisions!'''
    #for an explanation of this bit of code, please see the above function
    pygame.init()
    screen = pygame.display.set_mode((400,400),0,32)
    pygame.display.set_caption("Smilies!")
    
    # This text message gets displayed if all of thesmileys crash.
    #Doing fonts in pygame is weird.
    #If you want a certain font, you have to use pygame.font.match_font(font name, bold (true or false), italics (true or false).
    #You then create a font object using the path to the font that you find with match_font with the additional argument of size
    #You aren't limited to a max size of 36 in pygame!
    #Note that the text isn't actually drawn here - we do that later. This Font object merely lets us draw text.
    my_font = pygame.font.Font(pygame.font.match_font('Arial',True,False),30)
    
    moverCount = 0; # how many smileys have not crashed?

    # Draw 'em all and count how many are moving.
    #The explanation for painting is covered in the above function.
    screen.fill(pygame.Color('white'))
    for s in smileys:
        s.draw(screen)
        if s.moving:
            moverCount +=1
    pygame.display.update()
    for i in range(steps):  # move all smileys and check for collisions
        screen.fill(pygame.Color('white'))
        if moverCount==0:
            break
        for s in smileys:  # move them
            s.move()
            s.draw(screen)
        for i in range(len(smileys)): # check for collisions
            for j in range(i+1, len(smileys)): # avoid comparing to self (and duplicate checks).
                if smileys[i].collidedWith(smileys[j]):
                    for k in [i, j]:  #stop both of them.
                        if smileys[k].isMoving():
                            smileys[k].frown()
                            smileys[k].stop()
                            moverCount -= 1
        pygame.display.update()
        pygame.time.delay(1000//24) # pause before next iteration.
        
    if moverCount == 0: #all smileys have crashed!.
        #Drawing text is a little weird. You use the a Font object (in this case my_font) to render your text. The arguments are as follows:
        #text - the text to render
        #anti-alias - True if you want pygame to smooth your fonts so the edges don't look as sharp
        #colour - the colour to use
        #background colour - optional - set a background to your rendered text
        #using render actually returns a new Surface (just like Screen is a surface).
        drawn_text = my_font.render('PileUp!!', True, pygame.Color('blue')) 
                #you use a Surface's "blit" function to draw another surface on it.
        #So, since we want this text to appear on screen, we blit the Surface we got from rendering the text onto a location that seems suitable.
        screen.blit(drawn_text,(100,20))
        for s in smileys:
            s.draw(screen)
        pygame.display.update()
    
    #this code is explained in the above function
    event = pygame.event.poll()
    while event.type != QUIT:
        pygame.time.delay(100)
        event = pygame.event.poll()
    

def scene2():
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -1, 4, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     150)


def scene3():
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -2, 4, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     200 )

def scene4():
    runCollisionScene([Smiley(50, 50, 2, 2),
                       Smiley(130, 200, 4, 3, 60, 'green'),
                       Smiley(300, 70, -1, 5, 25, 'orange'),
                       Smiley(70, 350, 3, 0, 40, 'blue1')], 
                     200 )
    
scenes = [scene1, scene2, scene3, scene4]

if __name__ == '__main__':
    scene = int(input("Which scene? (1, 2, 3, 4)"))
    scenes[scene-1]()
    
