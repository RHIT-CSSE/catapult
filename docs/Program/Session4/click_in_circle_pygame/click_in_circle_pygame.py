import pygame
import math

pygame.init()

def distance(point1, point2):
    # TODO: Delete pass and fill in this function with the distance formula - point1 and point2 are tuples in the form (x, y)
    pass

frame_width = 400
frame_height = 400

frame_caption = "Click in circle"
frame_color = (0,0,0)

# TODO: Create a PyGame frame using the frame_width and frame_height as parameters - use the variable name frame

# TODO: Set the caption of the frame you just created using frame_caption


# A pygame Font object is created below
text_type = 'Comic Sans'
text_size = 25
bold = False
italic = False

font = pygame.font.SysFont(text_type, text_size, bold, italic)

# Text that can actually be rendered to the screen is created below by calling render on the Font object created above
instruction_text = 'Click in the circle'
antialias = True
text_color = (122, 237, 201)
text_background_color = frame_color

instruction_displayable_text = font.render(instruction_text, antialias, text_color, text_background_color)

# Here we draw a circle. This will be the circle that you click in later. Note the a pygame Rect object is returned and not the circle itself
circle_color = (182,210,110)
circle_center = (frame.get_width() // 2, frame.get_height() // 2)
circle_radius = 50
circle_border_width = 5

pygame.draw.circle(frame, circle_color, circle_center, circle_radius, circle_border_width)

''' This is the message that is displayed on the screen indicating whether you
    successfully clicked inside the circle or not. It's an empty string now because 
    we haven't clicked anything yet. You'll change this in your next TODO'''
success_message = ''

player_clicking_in_circles = True

while player_clicking_in_circles:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_clicking_in_circles = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = event.pos

            # TODO: Check the distance from click_position to circle_center
            #  if the distance is less than circle_radius set success_message to something indicating success
            #  otherwise set it to something indicating failure

    frame.fill(frame_color)

    pygame.draw.circle(frame, circle_color, circle_center, circle_radius, circle_border_width)

    successful_click_text = font.render(success_message, True, (122, 237, 201), (0, 0, 0))

    frame.blit(instruction_displayable_text, (25, 25))
    frame.blit(successful_click_text, (25, 375))

    pygame.display.update()



