import pygame
import math

pygame.init()

frame_width = 1200
frame_height = 700

frame = pygame.display.set_mode((frame_width, frame_height))
pygame.display.set_caption('Miscellaneous Pygame Graphics')

def draw_parallel_vertical_lines(starting_point, number_of_lines, line_length, distance_between_lines):
    start_x = starting_point[0]
    start_y = starting_point[1]

    line_color = pygame.Color('red')

    for i in range(0, number_of_lines):
        line_x_position_offset = i * distance_between_lines
        pygame.draw.line(frame, line_color, (start_x + line_x_position_offset, start_y), (start_x + line_x_position_offset, start_y + line_length))

def draw_equilateral_triangle(lower_left_point, triangle_width):
    triangle_point_list = []
    triangle_point_list.append(lower_left_point)

    lower_left_point_x = lower_left_point[0]
    lower_left_point_y = lower_left_point[1]

    lower_right_point = (lower_left_point_x + triangle_width, lower_left_point_y)
    triangle_point_list.append(lower_right_point)

    height = math.sqrt(triangle_width**2 - (triangle_width // 2)**2)
    top_triangle_lower_left_point = (lower_left_point_x + (triangle_width // 2), lower_left_point_y - height)
    triangle_point_list.append(top_triangle_lower_left_point)

    triangle_border_width = 3

    pygame.draw.polygon(frame, pygame.Color("black"), triangle_point_list, triangle_border_width)

def draw_concentric_circles(number_of_concentric_circles, center_point, radius):
    circle_color = pygame.Color('blue')

    for i in range(1, number_of_concentric_circles + 1):
        pygame.draw.circle(frame, circle_color, center_point, radius * i, 1)

def draw_triangle_pyramid(lower_left_point, triangle_width):
    height = math.sqrt(triangle_width**2 - (triangle_width // 2)**2)

    lower_right_trianagle_lower_left_point = (lower_left_point[0] + triangle_width, lower_left_point[1])
    upper_triangle_lower_left_point = (lower_left_point[0] + (triangle_width // 2), lower_left_point[1] - height)

    draw_equilateral_triangle(lower_left_point, triangle_width)
    draw_equilateral_triangle(lower_right_trianagle_lower_left_point, triangle_width)
    draw_equilateral_triangle(upper_triangle_lower_left_point, triangle_width)

def draw_nested_triangle_pyramids(lower_left_point, triangle_width):
    height = math.sqrt((triangle_width // 2)**2 - (triangle_width // 4)**2)

    lower_left_x = lower_left_point[0]
    lower_left_y = lower_left_point[1]

    draw_triangle_pyramid(lower_left_point, triangle_width // 2)
    draw_triangle_pyramid((lower_left_x + (triangle_width // 2), lower_left_y), triangle_width // 2)
    draw_triangle_pyramid((lower_left_x + (triangle_width // 4), lower_left_y - height), triangle_width // 2)

def n_layers_of_nested_triangle_pyramids(layers_of_triangles, lower_left_point, triangle_width):
    if layers_of_triangles <= 1:
        draw_equilateral_triangle(lower_left_point, triangle_width)
    else:
        height = math.sqrt(triangle_width**2 - (triangle_width // 2)**2)

        lower_left_x = lower_left_point[0]
        lower_left_y = lower_left_point[1]

        n_layers_of_nested_triangle_pyramids(layers_of_triangles - 1, lower_left_point, triangle_width // 2)
        n_layers_of_nested_triangle_pyramids(layers_of_triangles - 1, (lower_left_x + (triangle_width // 2), lower_left_y), triangle_width // 2)
        n_layers_of_nested_triangle_pyramids(layers_of_triangles - 1, (lower_left_x + (triangle_width // 4), lower_left_y - (height // 2)), triangle_width // 2)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        frame.fill(pygame.Color('white'))

        draw_parallel_vertical_lines((50, 50), 20, 30, 10)
        draw_equilateral_triangle((200, 200), 50)
        draw_concentric_circles(10, (300, 300), 5)
        draw_triangle_pyramid((400, 400), 40)
        draw_nested_triangle_pyramids((500, 500), 30)

        for i in range(8):
            n_layers_of_nested_triangle_pyramids(i + 1, (575, 575), 600)

        pygame.display.update()