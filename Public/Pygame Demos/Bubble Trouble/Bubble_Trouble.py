'''
Created on Jun 9, 2014

@author: burchtm
'''

import pygame
from Cool_Guy import *
from Bubble import *
from The_Spear import *
from Level import *
from Menu import *
import sys

#Sets up the window icon and caption and changes the mouse cursor. Also, initializes the mixer module then starts the game by starting the main menu.
def main():
    pygame.display.set_icon(pygame.transform.scale(pygame.image.load("./images/bubble.gif"), (32,32)))
    pygame.display.set_caption("Bubble Trouble!")
    pygame.mixer.init()
    initializeCursor()
    Menu().playGame()

#Changes the look of the cursor to be used. Uses strings that are a multiple of 8X8. Can set the white, black, and inverted parts of the new cursor    
def initializeCursor():
    cursorString = [
        "X               ",
        "XX              ",
        "XoX             ",
        "XooX            ",
        "XoooX           ",
        "XooooX          ",
        "XoooooX         ",
        "XooooooX        ",
        "XoooooooX       ",
        "XooooooooX      ",
        "XooooooooXX     ",
        "XooooooXXX      ",
        "XooooXXX        ",
        "XooXXX          ",
        "XXXX            ",
        "XX              "]
    #Compiles the new cursor. The xor is the parts of the cursor that will be inverted. 
    datatuple, masktuple = pygame.cursors.compile(cursorString, black='X', white='.', xor='o')
    #Sets the new cursor using (width,height),clickPoint,datatuple,masktuple the later two are returned when the cursor is compiled
    pygame.mouse.set_cursor((len(cursorString), len(cursorString[0])),(1,1),datatuple, masktuple)
    
if __name__ == '__main__':
    main()