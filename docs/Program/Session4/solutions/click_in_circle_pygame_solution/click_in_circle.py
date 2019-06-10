import pygame
import math

pygame.init()

def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)

frame_width = 400
frame_height = 400

frame_color = (0,0,0)

frame = pygame.display.set_mode((frame_width, frame_height))

pygame.display.set_caption("Click in circle")

text_type = 'Comic Sans'
text_size = 25
bold = False
italic = False

font = pygame.font.SysFont(text_type, text_size, bold, italic)

instruction_text = 'Click in the circle'
antialias = True
text_color = (122, 237, 201)
text_background_color = frame_color

instruction_displayable_text = font.render(instruction_text, antialias, text_color, text_background_color)

circle_color = (182,210,110)
circle_center = (frame.get_width() // 2, frame.get_height() // 2)
circle_radius = 50
circle_border_width = 5

pygame.draw.circle(frame, circle_color, circle_center, circle_radius, circle_border_width)

success_message = ''

player_clicking_in_circles = True

while player_clicking_in_circles:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_clicking_in_circles = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = event.pos

            distance_from_circle = distance(click_position, circle_center)

            if distance_from_circle < circle_radius:
                success_message = 'Bullseye!'
            else:
                success_message = 'You missed!'

    frame.fill(frame_color)

    pygame.draw.circle(frame, circle_color, circle_center, circle_radius, circle_border_width)

    successful_click_text = font.render(success_message, True, (122, 237, 201), (0, 0, 0))

    frame.blit(instruction_displayable_text, (25, 25))
    frame.blit(successful_click_text, (25, 375))

    pygame.display.update()



