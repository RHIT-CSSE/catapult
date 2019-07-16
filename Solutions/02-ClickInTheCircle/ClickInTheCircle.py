import pygame, sys
import math


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
    font = pygame.font.Font(None, 25)

    pygame.mixer.music.load('drums.wav')

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                distance_from_circle = distance(click_position, circle_center)
                if distance_from_circle < circle_radius:
                    message_text = 'Bullseye!'
                    pygame.mixer.music.play(-1)
                else:
                    message_text = 'You missed!'
                    pygame.mixer.music.stop()

        screen.fill(pygame.Color("Black"))

        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        onscreen_message = font.render(message_text, True, (122, 237, 201))

        screen.blit(instructions_image, (25, 25))
        screen.blit(onscreen_message, (25, 375))

        pygame.display.update()


main()
