Use object-oriented programming to manage objects on screen

=================================================================================
Lesson
=================================================================================
1. Use self.objectsOnScreen to control objects on screen
	We always use blit to copy an image sprite to the screen.
		screen.blit(img, (x, y))
	Notice that blit needs three data: img, x and y
	We can store them as attributes of the objects:
		self.img  				its surface				how it looks like
		self.x & self.y			its coordinate			where it locates

	With this structure, we can make a list of everything on the screen 			self.objectsOnScreen = [ obj1 , obj2 ]
	Then use a simple and elegant loop to blit all of them to the screen 			for obj in self.objectsOnScreen:
																			            screen.blit(obj.img, (obj.x, obj.y))

    If you want to add an object to the screen, just append it to the list 			self.objectsOnScreen.append(added_obj)
    If you want to remove an object to the screen, just remove it to the list 		self.objectsOnScreen.remove(added_obj)

2. Create class for object on the screen
	As discussed before, any objects with three required attributes (x, y, img) are qualified to appear on the screen
	You can create your own class to represent any customized objects on the screen, as long as it has required attributes -- x, y, img
	For simple static objects, you can just take advantage of ImageObject, the simplest class that satisfied this requirement.
		To create an instance of ImageObject				obj = ImageObject(x, y, img)

	In fact, pygame has an Sprite library built on this idea. Feel free to read their documentation and use it.


3. Write Utility function to save time
	There are many similar features in the game, such as collisions, bouncing.
	To make main logic shorter and cleaner, we often write utitility function to perform those common operation.

	As you put more features into your game, Gamelogic.py can grow really large, you can also catergorize similar classes into anothre file.


4. load images
	Images can be loaded directly into pygame as surfaces.
	Check out the examples in GraphicsUtil.py


=================================================================================
Challenge
=================================================================================
1. make the randomly added balls move at some speed
2. make those balls bounce at the border
	Hint: there is a nice function in Util.py --- bounceIn(obj, x1, y1, x2, y2)
