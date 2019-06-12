import pygame

pygame.init()

frame_width = 1200
frame_height = 700

frame = pygame.display.set_mode((frame_width, frame_height))
pygame.display.set_caption('Miscellaneous Pygame Graphics')

def draw_parallel_vertical_lines(starting_point, number_of_lines, line_length, distance_between_lines):
    # TODO: Delete pass and draw parallel vertical lines.
    #  PyGame documentation for drawing lines - https://www.pygame.org/docs/ref/draw.html#pygame.draw.line
    pass

def draw_equilateral_triangle(lower_left_point, triangle_width):
    # TODO: Delete pass and draw an equilateral triangle.
    #  PyGame documentation for drawing a triangle - https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
    pass

def draw_concentric_circles(number_of_concentric_circles, center_point, radius):
    # TODO: Delete pass and draw concentric circles.
    #  PyGame documentation for drawing a circle - https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    pass

def draw_triangle_pyramid(lower_left_point, triangle_width):
    # TODO: Delete pass and draw a pyramid composed of three equilateral triangles with a total width of 'triangle_width'.
    pass

def draw_nested_triangle_pyramids(lower_left_point, triangle_width):
    # TODO: Delete pass and draw a nested pyramid composed of three equilateral triangles.
    #  Each of these equilateral triangles should be composed of three inner equilateral triangles.
    #  The pyramid should have an overall width of 'triangle_width'
    pass

def n_layers_of_nested_triangle_pyramids(layers_of_triangles, lower_left_point, triangle_width):
    # TODO: Delete pass and draw a pyramid with n layers of nested equilateral triangles.
    #  The pyramid should have an overall width of 'triangle_width'
    pass

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        frame.fill(pygame.Color('white'))

        # TODO: As you complete the above TODO's, uncomment the corresponding function call to the function you just
        #  completed to see your work appear on the window.
        #  If you are unsure whether or not things look the way they are supposed to, refer to the image titled
        #  'WhatThingsShouldLookLikeWhenYouAreFinished.png' to compare your screen with the way things should look.

        # draw_parallel_vertical_lines((50, 50), 20, 30, 10)
        # draw_equilateral_triangle((200, 200), 50)
        # draw_concentric_circles(10, (300, 300), 5)
        # draw_triangle_pyramid((400, 400), 40)
        # draw_nested_triangle_pyramids((500, 500), 30)

        # for i in range(8):
        #     n_layers_of_nested_triangle_pyramids(i + 1, (575, 575), 600)

        pygame.display.update()