# Created by Derek Grayless, 06/14/2019
# 2019 Operation Catapult Session 1 Introduction to PyGame Live Coding

import pygame
import math

pygame.init()

# TODO: 1. Create a PyGame window and give it a name

frame_width = 750
frame_height = 750

frame = pygame.display.set_mode((frame_width, frame_height))

pygame.display.set_caption('Pygame Frame')

# TODO: 2. Define colors that we can use throughout our program

black = (0, 0, 0)
white = (255, 255, 255)

red = pygame.Color('red')
green = pygame.Color('green')
yellow = pygame.Color('yellow')
blue = pygame.Color('blue')
purple = pygame.Color('purple')
pink = pygame.Color('pink')
orange = pygame.Color('orange')

# TODO: 3. Make event loop, introduce events, and get program to quit

program_is_running = True

while program_is_running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            program_is_running = False

    frame.fill(white)

    # TODO: 4. Draw a rectangle using pygame.draw.rect(Surface, color, Rect, width=0), draw multiple rectangles with a for loop
    # TODO: 6. Add border to rectangles
    # TODO: 7. Draw ellipse using pygame.draw.ellipse(Surface, color, Rect, width=0) inside of rectangles

    for i in range(0, 4):
        rectangle_dimensions = (0 + (50 * i), 0 + (50 * i), 50, 50)

        pygame.draw.rect(frame, red, rectangle_dimensions)
        pygame.draw.rect(frame, green, rectangle_dimensions, 3)

        pygame.draw.ellipse(frame, yellow, rectangle_dimensions)

    # TODO: 8. Draw a line using pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
    start_point = (250, 50)
    end_point = (250, 100)

    pygame.draw.line(frame, blue, start_point, end_point, 10)

    # TODO: 9. Draw lines - 1. Using point_list and for loop, 2. Using pygame.draw.lines(Surface, color, closed, pointlist, width=1)

    color_list = [red, green, yellow, blue]
    point_list = [(450, 100), (450, 250), (600, 250), (600, 100), (450, 100)]

    for i in range(len(point_list) - 1):
        current_start_point = point_list[i]
        current_end_point = point_list[i + 1]

        pygame.draw.line(frame, color_list[i], current_start_point, current_end_point, 5)

    pygame.draw.lines(frame, green, True, point_list, 5)

    # TODO: 10. Draw a circle using pygame.draw.circle(Surface, color, pos, radius, width=0)
    circle_center = (300, 300)
    circle_radius = 25

    pygame.draw.circle(frame, purple, circle_center, circle_radius)

    # TODO: 11. Draw a circle using pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1)
    circle_center_x = circle_center[0]
    circle_center_y = circle_center[1]

    rect_x = circle_center_x - circle_radius
    rect_y = circle_center_y - circle_radius
    rect_width = 2 * circle_radius
    rect_height = 2 * circle_radius

    pygame.draw.arc(frame, pink, (rect_x, rect_y, rect_width, rect_height), 0, 2 * math.pi, 5)

    # TODO: 12. Draw a polygon using pygame.draw.polygon(Surface, color, pointlist, width=0)
    pygame.draw.polygon(frame, red, [(500, 500), (535, 500), (520, 520)])

    # TODO: 13. Draw two rectangles, and call rect.colliderect(rect)

    rect_1 = pygame.draw.rect(frame, blue, [100, 400, 100, 100], 5)
    rect_2 = pygame.draw.rect(frame, orange, [150, 400, 100, 100], 5)

    print("Rectangle 1 collides with rectangle 2 - " + str(rect_1.colliderect(rect_2)))
    print("Rectangle 2 collides with rectangle 1 - " + str(rect_2.colliderect(rect_1)))

    # TODO: 14. Create a point and call rect.collidepoint(point)

    point = (125, 450)

    print("Point collides with rectangle 1 - " + str(rect_1.collidepoint(point)))
    print("Point collides with rectangle 2 - " + str(rect_2.collidepoint(point)))

    # TODO: 5. Call pygame.display.update()
    pygame.display.update()
