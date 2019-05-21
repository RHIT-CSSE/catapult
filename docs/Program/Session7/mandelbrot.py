'''
Created on Jul 11, 2015
Mandelbrot set visualizer. Too inefficient to zoom.

@author: Matt Boutell 
'''

import time
import math
import pygame
import pygame.locals as pl


WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
rectangle = pl.Rect(100, 100, 50, 50) # x,y,w,h
BLACK = [0,0,0]
WHITE = [255, 255, 255]

# Create a pixel array so I can write conveniently to a surface
surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
pixels = pygame.PixelArray(surface)

# Mandelbrot equation.   
def f(z, c):
    return z*z + c

# How to color each pixel
def getColor(x, y):
# Map x,y pixels to complex numbers z=a+bi in the range x = [-2,1], y = [-1, 1]    
    a = 3*x/WINDOW_WIDTH - 2
    b = 1- 2*y/WINDOW_HEIGHT
    c = complex(a,b)
    
    # Iterate the function
    MAX_ITERATIONS = 500 # Lower = faster, higher = better resolution. 40 is a good tradeoff.
    z = 0
    for i in range(MAX_ITERATIONS):
        z = f(z,c)
        mag = abs(z)
        if mag > 10000:
            break  

    # False color        
    if mag > 2:
        offset = int(math.log(mag)*10)
        return [255- offset % 255, offset % 255, offset % 255]  
    return BLACK

# Operate on each pixel
def fill(pixels):
    for row in range(WINDOW_HEIGHT):
        for col in range(WINDOW_WIDTH):
            pixels[col][row] = getColor(col, row)


start = time.time()
fill(pixels)
elapsed = time.time() - start
print(elapsed)
# Need to release the PixelArray to draw the surface
pixels = None

# Display until they exit.
while True:
    for event in pygame.event.get():
        if event.type == pl.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
