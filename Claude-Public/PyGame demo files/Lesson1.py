import pygame #import pygame libraimport pygame #import pygame library
from pygame.locals import * #import pygame local variables into our namespace for quicker accesss

# store the desired screen width and height into variables so they can be changed or reused easily
screen_width = 800
screen_height = 800

pygame.init() #initialize pygame (this must be done before you do anything else with pygame functions)
screen = pygame.display.set_mode([screen_width,screen_height],0,32) #set up the screen with the desired width and height, no special mode, and 32 bits of colour depth

screen.fill((255,255,255)) #fill the screen with white
pygame.draw.circle(screen,(40,240,100),(500,500),100) #draw a circle on the screen we created, with the color (40,240,100), with its center at (500,500), and a radius of 100 pixels 
pygame.draw.rect(screen,(100,100,0),Rect((40,40),(50,50))) #draw a rectangle on the screen we created with the color (100,100,0), in the area described by a rectangle with its top left corner at (40,40), a width of 50, and a height of 50

pygame.display.flip() #this actually moves all of the things we just did onto the screen

events = pygame.event.get() #get the list of all events that have occured since the last time we checked for events
while True: #loop infinitely (it's okay, we'll exit when we want to)
    for event in events: #go through each item in events, calling the current one "event"
        if event.type == QUIT: #quit if the event is a QUIT event
            exit()
    #wait 100 milliseconds (so we don't use 100% of the processor)
    pygame.time.delay(100)
    events = pygame.event.get() #get all the events since the last time we checked for events