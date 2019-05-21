import pygame #import pygame library
from pygame.locals import * #import pygame local variables into our namespace for quicker accesss

#create some global variables
#store the desired screen width and height into variables so they can be changed or reused easily
screen_width = 800
screen_height = 800
fps = 30 #this variable indicates how many frames per second we want the program to run

def init(): #a function to set up the screen
    pygame.init() #initialize pygame (this must be done before you do anything else with pygame functions)
    screen = pygame.display.set_mode([screen_width,screen_height],0,32) #set up the screen with the desired width and height, no special mode, and 32 bits of colour depth
    return screen #return the screen object

def draw(screen): #a function to draw our stuff on the screen
    #do something interesting to the screen here! check out pygame.draw
    pygame.display.flip() #applies our changes to the screen

def handle(events): #a function to handle input events
    for event in events: #go through each item in events, calling the current one "event"
        if event.type == QUIT: #quit if the event is a QUIT event
            exit()
        #other possible event types can be found in the documentation
        #certain events, such as keyboard and mouse events, contain information like which key was pressed or where the mouse is now.

def main(): #the main program
    screen = init() #call our initialization function

    clock = pygame.time.Clock() #create a PyGame Clock object that we'll use to get a constant framerate
    events = pygame.event.get() #get the list of all events that have occured since the last time we checked for events
    while True: #loop infinitely (it's okay, we'll exit when we want to)
        handle(events) #handle our current events
        draw(screen) #call our draw function
        clock.tick(fps) #tell the clock that we want it to try to use the framerate specified above
        events = pygame.event.get() #get all the events since the last time we checked for events, so they can be used next time the loop runs


if __name__ == "__main__": #a fun Python incantation that calls the main function only if it's being run directly as opposed to being imported
    main()
