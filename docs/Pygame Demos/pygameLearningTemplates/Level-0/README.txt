Get something show up on the screen

=================================================================================
Lesson
=================================================================================
pygame.init()
	initialize pygame, so it's ready for work

pygame.display.set_mode((screenWidth, screenHeight))
	creates an surface representing the screen

Color = (Red, Green, Blue)
	creates an tuple of three element to represent color

pygame.draw.circle(surfaceToBeDrawnOn, color, centerCordinate, radius)
	pygame.draw.SomeMethod(surface, ...) can be used to draw premitive figures on screen
		Look up other methods you can use at http://www.pygame.org/docs/ref/draw.html
	centerCordinate is a tuple of x-coordinate and y-coordinate  (x, y)
	Different from math coordinate, computer scientists love to make leftUpper corner the origin (0,0), and x-axis goes right, while y-axis goes down.

pygame.display.flip()
	This is the only command that pygame would actually change the GUI screen
	After ploting the surface, let's print it to the screen



=================================================================================
Challenge
=================================================================================
1. Try to draw an BLUE rectangle at coordinate (100, 200)