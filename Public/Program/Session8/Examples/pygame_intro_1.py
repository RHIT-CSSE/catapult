import pygame
import sys

"""
Code will pop up a black screen
"""

def main():
    pygame.init()
    game = Game()
    game.runGame()



"""
Game class
"""
class Game:
    def __init__(self):
        self.width = 1000 # Values can be changed as needed. Example values
        self.height = 700 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Need to set background so shapes are drawn with full color
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill((220,220,220)) # Values can be changed as needed. Example values

    def runGame(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()


main()