Manage game state and build animation

=================================================================================
Lesson
=================================================================================
1. Manage game state
	It is very common to have multiple states in the game.
	Therefore, we can store this information as an attribute of the game.
	Then in updateGame(), do different operations based on the state.

2. Animation
	Animiaton is essentially showing different frames at each time.
	We represent an image with a surface.
	We can represent an animiation with a list of surface.

	Animation is time sensitive because it needs to know which frame to show based on the time.
	Therefore, we need to track time (or frame number) in our game.
		In the example, self.timer increments for each frame.

	A very helpful function is defined in Util.py ------- showAnimationOn(obj, animation, frameNum)
		obj 		the obj you want to show animiation on
		animiation  a list of surfaces showing each frames
		frameNum	frame number is related to the time. If you pass in self.time, the animiatin is going to update every frame.
						You can easily adjust how fast the animiatin is playing by dividing a number (slowing time down).

=================================================================================
Challenge
=================================================================================
