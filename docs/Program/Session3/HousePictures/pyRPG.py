from unicurses import *
import time
from random import randrange
from sys import stdout

def charadd(ch, ad) :
    """Adds a specified value to a character using ASCII addition. Uses only last byte of addition.
charadd(ch, ad)

Arguments:
ch: The given character
ad: The value to add
"""
    return chr((ord(ch)+ad) % 256)

WHITE = 0
RED = 1
BLUE = 2
CYAN = 3
GREEN = 4
MAGENTA = 5
YELLOW = 6

def printc(x, y, ch, color = WHITE):
    "Prints a character at the given location with the given color.\n\nArguments:\nx: The x location to print the character\ny: The y location to print the character\nch: The character to print\ncolor: The color to print the character, default white\n\nBounds: String must end before reaching 79 along x-axis, must be before 24 on y-axis."
    if (x > 79 - len(ch)) | (y > 23) | (x < 1) | (y < 1):
        raise Exception("String out of bounds, shorten string or move left. Bounds are <= 79 on right, <= 23 on bottom, and >= 1 on top and left")
    if ('\n' in ch) | ('\r' in ch):
        raise Exception("No newlines in strings")
    mvaddstr(y, x, ch, COLOR_PAIR(color))


stdscr = initscr()
noecho()
nodelay(stdscr, True)

if (has_colors() == False):
    endwin()
    print("Your terminal does not support color!")
    exit(1)

start_color()
init_pair(0, COLOR_WHITE, COLOR_BLACK)
init_pair(1, COLOR_RED, COLOR_BLACK)
init_pair(2, COLOR_BLUE, COLOR_BLACK)
init_pair(3, COLOR_CYAN, COLOR_BLACK)
init_pair(4, COLOR_GREEN, COLOR_BLACK)
init_pair(5, COLOR_MAGENTA, COLOR_BLACK)
init_pair(6, COLOR_YELLOW, COLOR_BLACK)

border()
curs_set(0)


printc(30, 12, "Here we go!")
getch()

playerX = 10
playerY = 10
addChars = True
playerTrailColor = 0
while True: # Main game loop
    str = chr(randrange(ord('a'), ord('z')))
    if addChars:
        printc(randrange(1, 79), randrange(1, 24), str, randrange(0, 7))
    key = getch()
    printc(playerX, playerY, '%', playerTrailColor + 1)
    if key == ord('w'):
        playerY -= 1
        if playerY < 1:
            playerY = 1
    if key == ord('s'):
        playerY += 1
        if playerY > 23:
            playerY = 23
    if key == ord('a'):
        playerX -= 1
        if playerX < 1:
            playerX = 1
    if key == ord('d'):
        playerX += 1
        if playerX > 78:
            playerX = 78
    printc(playerX, playerY, '%')
    if key == ord(' '):
        flash()
    if key == ord('q'):
        addChars = not addChars
    if key == ord('e'):
        playerTrailColor = (playerTrailColor + 1) % 6
    if key == ord('p'):
        clear()
        border()
    if key == 27 :
        break

    
nodelay(stdscr, False)
endwin()
exit(0)