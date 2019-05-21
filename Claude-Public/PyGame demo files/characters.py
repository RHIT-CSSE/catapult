import pygame #import pygame library
from pygame.locals import * #import pygame local variables into our namespace for quicker accesss
from random import randint

#create some global variables
#store the desired screen width and height into variables so they can be changed or reused easily
screen_width = 640
screen_height = 480
fps = 30 #this variable indicates how many frames per second we want the program to run

class Actor:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    
    def act(self):
        pass
    
    def draw(self):
        pass
    
    def handle(self, event):
        pass

class Blob(Actor):
    def __init__(self, screen, x, y):
        Actor.__init__(self, screen, x, y)
        self.image = pygame.image.load("blob4.png").convert_alpha()
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class FancyPants(Actor):
    def __init__(self, screen, x, y):
        Actor.__init__(self, screen, x, y)
        self.image = pygame.image.load("mario.png").convert_alpha()
        self.x_speed = 0
        self.y_speed = 0
    
    def act(self):
        self.x += self.x_speed
        self.y += self.y_speed
    
    def handle(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.x_speed = -5
            elif event.key == K_RIGHT:
                self.x_speed = 5
            elif event.key == K_UP:
                self.y_speed = -5
            elif event.key == K_DOWN:
                self.y_speed = 5
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.x_speed = 0
            elif event.key == K_DOWN or event.key == K_UP:
                self.y_speed = 0
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

global font
def init(): #a function to set up the screen
    global font
    pygame.init() #initialize pygame (this must be done before you do anything else with pygame functions)
    screen = pygame.display.set_mode([screen_width,screen_height],0,32) #set up the screen with the desired width and height, no special mode, and 32 bits of colour depth
    font = pygame.font.SysFont("Futura", 72)
    return screen #return the screen object

def update(actors):
    for actor in actors:
        actor.act()

def draw(screen, actors): #a function to draw our stuff on the screen
    #do something interesting to the screen here! check out pygame.draw
    screen.fill(pygame.Color('white'))
    for actor in actors:
        actor.draw()
    text = font.render("Hello!", True, (0,0,0))
    screen.blit(text, (100,100))
    pygame.display.flip() #applies our changes to the screen

def handle(events, actors): #a function to handle input events
    for event in events: #go through each item in events, calling the current one "event"
        if event.type == QUIT: #quit if the event is a QUIT event
            exit()
        else:
            for actor in actors:
                actor.handle(event)
        #other possible event types can be found in the documentation
        #certain events, such as keyboard and mouse events, contain information like which key was pressed or where the mouse is now.

def main(): #the main program
    screen = init() #call our initialization function
    
    guy = FancyPants(screen, 100, 100)
    some_blob = Blob(screen, 30, 50)
    guys = [some_blob,guy]
    for i in range(10):
        guys.append(Blob(screen, randint(0, screen_width), randint(0, screen_height)))

    clock = pygame.time.Clock() #create a PyGame Clock object that we'll use to get a constant framerate
    events = pygame.event.get() #get the list of all events that have occured since the last time we checked for events
    while True: #loop infinitely (it's okay, we'll exit when we want to)
        handle(events, guys) #handle our current events
        update(guys) #have our actors act
        draw(screen, guys) #call our draw function
        clock.tick(fps) #tell the clock that we want it to try to use the framerate specified above
        events = pygame.event.get() #get all the events since the last time we checked for events, so they can be used next time the loop runs


if __name__ == "__main__": #a fun Python incantation that calls the main function only if it's being run directly as opposed to being imported
    main()
