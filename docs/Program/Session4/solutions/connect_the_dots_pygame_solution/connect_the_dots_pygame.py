import pygame
import math
import time

pygame.init()

frame_width = 400
frame_height = 400

frame = pygame.display.set_mode((frame_width, frame_height))

pygame.display.set_caption('Connect the dots!')

click_distance_threshold = 10

white = (255, 255, 255)
black = (0, 0, 0)
orange = (203, 105, 11)

def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)

def draw_point(point_position):
    pygame.draw.circle(frame, black, point_position, click_distance_threshold, click_distance_threshold)

def draw_line(point1, point2):
    pygame.draw.line(frame, black, point1, point2, click_distance_threshold)

list_of_points_clicked_by_user = []

user_is_clicking_points = True

while user_is_clicking_points:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            user_is_clicking_points = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            click_position = event.pos

            enough_points_to_make_a_polygon = len(list_of_points_clicked_by_user) >= 2

            if enough_points_to_make_a_polygon:
                first_point = list_of_points_clicked_by_user[0]

                distance_from_first_click = distance(click_position, first_point)

                if distance_from_first_click < click_distance_threshold:
                    user_is_clicking_points = False

            list_of_points_clicked_by_user.append(click_position)

    frame.fill(white)

    for point in list_of_points_clicked_by_user:
        draw_point(point)

    number_of_points_clicked_by_user = len(list_of_points_clicked_by_user)

    if number_of_points_clicked_by_user >= 2:

        for i in range(1, number_of_points_clicked_by_user):
            last_point_clicked_index = -i
            second_to_last_point_clicked = -(i+1)

            last_point_clicked = list_of_points_clicked_by_user[last_point_clicked_index]
            second_to_last_point_clicked = list_of_points_clicked_by_user[second_to_last_point_clicked]

            draw_line(second_to_last_point_clicked, last_point_clicked)

    pygame.display.update()

polygon_rect = pygame.draw.polygon(frame, orange, list_of_points_clicked_by_user, click_distance_threshold)

pygame.display.update()

time.sleep(10)
