import pygame, sys
import math

# TODO 1: Add multiple circles and make them individually detect clicks
# TODO 2: Make the circles move slowly in a straight line
# TODO 3: Make the circles move in arcs, add drop behavior
# TODO 4: Bombs, sound and anything else



def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]
    return math.sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")

    circle_color = (154, 58, 212)
    # for reasons, we've written this to allow your
    # centers to be floating point numbers
    circle_center = (100.2, 100)
    circle_radius = 50

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                distance_from_circle = distance(click_position, circle_center)
                if distance_from_circle < circle_radius:
                    circle_color = (40, 40, 40)

        screen.fill(pygame.Color("Black"))

        # force x and y to integer values here so we can store them as floating point numbers
        center_x, center_y = circle_center
        pygame.draw.circle(screen, circle_color, (int(center_x), int(center_y)), circle_radius)

        pygame.display.update()


main()
