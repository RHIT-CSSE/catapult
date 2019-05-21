#-------------------------
# initialize pygame
#-------------------------
import pygame
# initialize pygame
pygame.init()

# initialize a clock for the game, so you can control the framerate
clock = pygame.time.Clock()

# create a screen of 500 * 500
screen = pygame.display.set_mode((500, 500))

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
pygame.key.set_repeat(50, 50)

#-------------------------
# initialize the game
#-------------------------
# import the game class from GameLogic
from GameLogic import Game, Graph

# acquire a game object
game = Game()

#-------------------------
# Our Main Loop
#-------------------------
## Your must have one and only one big while loop for your game
## Each time the loop is executed, one framed
while True:
    #-------------------------
    # Our event hanlding loop
    #-------------------------
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
        # check for some key presses
        if event.type == pygame.KEYDOWN:
            # move the hero
            if event.key == pygame.K_UP:
                game.hero.y -= 10
            elif event.key == pygame.K_DOWN:
                game.hero.y += 10
            elif event.key == pygame.K_LEFT:
                game.hero.x -= 10
            elif event.key == pygame.K_RIGHT:
                game.hero.x += 10
            # change the background color
            elif event.key == pygame.K_o:
                game.background = Graph.ORANGE
            elif event.key == pygame.K_b:
                game.background = Graph.BLACK
            # add an random ball to the screen
            elif event.key == pygame.K_a:
                game.addAnRandomBall()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # move the hero to where mouse clicked
            game.hero.x, game.hero.y = event.pos

    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen in updateGame()
    game.updateGame()

    #-------------------------
    # The graphics block
    #-------------------------
    ## all the drawing happen in updateGame()
    game.draw(screen)

    #-------------------------
    # display this frame and wait
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
        
    clock.tick(60)
    # set the framerate of the game to 60fps, i.e. 60 updates in one second
