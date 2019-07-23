import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]
    return math.sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2)


def main():
    # pygame screen setup
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Fruit Ninja Stripped")
    font = pygame.font.Font(None, 25)
    clock = pygame.time.Clock()

    # instruction font setup
    instruction_text = 'Click on the circles to "kill" them'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    # circles setup
    number_of_circles = 3
    circle_colors = [(154, 58, 212), (135, 206, 235), (0, 255, 0)]
    radius_list = [50, 60, 40]
    center_points = [(25, 400), (-20, 300), (0, 100)]
    velocity_list = [(10, -15), (8, -15), (10, -10)]
    gravity = -1
    dead_velocity = (0, 40)

    pause_balls = False

    while True:
        clock.tick(60)
        screen.fill(pygame.Color("Black"))

        # go through the list to draw all circles
        for i in range(number_of_circles):
            # draw the new circle
            pygame.draw.circle(screen, circle_colors[i], center_points[i], radius_list[i])

        # detect clicks in any circle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                pause_balls = not pause_balls
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                print("@click:", click_position)
                # detect click in any of the circles
                for j in range(number_of_circles):
                    print(center_points[j])
                    distance_from_circle = distance(click_position, center_points[j])
                    print("distance:", distance_from_circle)
                    print("radius:", radius_list[j])
                    if distance_from_circle < radius_list[j]:
                        print("+++Clicked in circle", j)
                        circle_colors[j] = pygame.Color("Yellow")
                        velocity_list[j] = dead_velocity

        if not pause_balls:
            for i in range(number_of_circles):
                # update the position of circles for next loop's drawing
                x = center_points[i][0]
                y = center_points[i][1]
                x_velocity = velocity_list[i][0]
                y_velocity = velocity_list[i][1]
                new_center_point = (x + x_velocity, y + y_velocity)
                center_points[i] = new_center_point

                # update the y velocity to factor in gravity
                if velocity_list[i] != dead_velocity:
                    new_velocity = (x_velocity, y_velocity - gravity)
                    velocity_list[i] = new_velocity



        # blit the instruction font onto the screen
        screen.blit(instructions_image, (10, 10))

        pygame.display.update()


main()
