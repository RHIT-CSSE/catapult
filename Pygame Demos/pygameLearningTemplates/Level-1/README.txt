Get something moving on the screen

=================================================================================
Lesson
=================================================================================
1. Create sprite surface
	According to wikipedia, spirte is any two-dimensional bitmap used as part of a graphics display.
	It is a common design pattern to
		First, create sprites for all components you want to displayed on the screen before the game start
		Then, just copy them onto the screen whenever you need them

	pygame.Surface((40, 40))
		creates a surface that you can draw figures on
		you can copy this surface onto another surface or screen 

    conpiedTo.blit(conpiedFrom, (leftUpCorner_x, leftUpCorner_y))
    	copy surface <conpiedFrom> to <copiedTo> with its left up corner cordinate specified

2. Create moving objects
	To make objects moving on the screen, there has to be multiple frames, so you would need a loop.
	Inside each loop you need to repeat these steps:
		1. clear the screen or set up the background		screen.fill(BACKGROUND_COLOR)
		2. copy prepared sprites onto the screen 			screen.blit(surface, (x, y))
		3. ask pygame to display the screen 				pygame.display.flip()
		4. wait for a interval to reach a framerate 		clock.tick(FRAME_RATE)


=================================================================================
Challenge
=================================================================================
1. Make two cycles (like eyes) move instead
2. Change the directionto move up to down.
