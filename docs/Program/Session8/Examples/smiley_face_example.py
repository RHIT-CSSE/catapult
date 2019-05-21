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
            
            """
            Draw shapes here
            """
            pygame.draw.circle(self.screen, pygame.Color("yellow"),(200, 200), 150)
            pygame.draw.circle(self.screen, pygame.Color("green"), (150, 150), 25)
            pygame.draw.circle(self.screen, pygame.Color("green"), (250, 150), 25)
            pygame.draw.polygon(self.screen, pygame.Color("orange"), [(200, 175), (175, 200), (225, 200)])
            pygame.draw.arc(self.screen, pygame.Color("blue"), [100, 125, 200, 200], 3.14, 2*3.14, 5)



            pygame.display.update()


main()