import pygame
import time

pygame.init()

# create a pygame frame

frame_width = 750
frame_height = 750

frame_dimension = (frame_width,frame_height)

frame = pygame.display.set_mode(frame_dimension)

pygame.display.set_caption('My Pygame window')

black = (0,0,0)
white = (255,255,255)
red = pygame.Color("red")
green = pygame.Color("green")
yellow = pygame.Color("yellow")
blue = pygame.Color("blue")
purple = pygame.Color("purple")
pink = pygame.Color("pink")
orange = pygame.Color("orange")

# event loop

running = True
loopCounter = 0
moving_dot_x = 0
moving_dot_go_right = True
moving_dot_trailer = frame_width/2
trailer_dot_x = 0
trailer_dot_go_right = True
starting_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame.fill(white)
    #pygame.draw.rect(frame, yellow,(0, 0, 50, 50))
    for i in range(0, 4):
        rectangle_dimensions = (0 + (50 * i), 0 + (50 * i), 50, 50)

        pygame.draw.rect(frame, red, rectangle_dimensions)
        pygame.draw.rect(frame, green, rectangle_dimensions, 3)
        pygame.draw.ellipse(frame, yellow, rectangle_dimensions)

    start_position = (250,50)
    end_position = (250,100)
    pygame.draw.line(frame,blue,start_position,end_position, 15)

    color_list = [red,green,yellow,blue]
    point_list = [(450,100), (450,250), (600,250), (600,100), (450,100)]

    for i in range(len(point_list)-1):
        current_starting_point = point_list[i]
        current_ending_point = point_list[i+1]
        current_color = color_list[i]
        pygame.draw.line(frame,current_color,current_starting_point,current_ending_point,5)

    loopCounter = loopCounter+1 # for timing loops

    if (moving_dot_go_right):  # for moving bar at bottom
        moving_dot_x = moving_dot_x+2
        if (moving_dot_x + 5 > frame_width):
            moving_dot_go_right = False
    else:
        moving_dot_x = moving_dot_x-2
        if (moving_dot_x < 2):
            moving_dot_go_right = True
    moving_dot_trailer = moving_dot_trailer-2
    if (moving_dot_trailer <= 0): # time to make it move
        if (trailer_dot_go_right):
            trailer_dot_x = trailer_dot_x + 1
            if (trailer_dot_x + 5 > frame_width):
                trailer_dot_go_right = False
        else:
            trailer_dot_x = trailer_dot_x - 1
            if (trailer_dot_x < 2):
                trailer_dot_go_right = True
    if trailer_dot_x < moving_dot_x:
        moving_line_color = purple
    else:
        moving_line_color = orange
    pygame.draw.line(frame,moving_line_color,(trailer_dot_x, frame_height-6),(moving_dot_x, frame_height-6),5)
    pygame.display.update()

    if (loopCounter % 100 == 0):
        elapsed_time = time.time() - starting_time
        loops_per_second = loopCounter / elapsed_time
        elapsed_print_time = str(elapsed_time)[0:5]
        avg_loops_per_second = str(loops_per_second)[0:5]
        print ("loopCounter = "+str(loopCounter)+" in "+
               elapsed_print_time+" sec, or "+avg_loops_per_second+" loops/sec")