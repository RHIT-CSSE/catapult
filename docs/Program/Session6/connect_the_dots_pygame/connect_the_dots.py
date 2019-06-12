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
    # TODO: Delete pass and draw a circle using pygame.draw.circle, the link below may be helpful to you
    #  https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    #  Make your circle black, and use click_distance_threshold for your radius and width
    pass

def draw_line(point1, point2):
    # TODO: Delete pass and draw a line using pygame.draw.line, the link below may be helpful to you
    #  https://www.pygame.org/docs/ref/draw.html#pygame.draw.line
    #  The line should start at point1 and end at point2
    #  Make your line black, and use click_distance_threshold for the line's width
    pass

list_of_points_clicked_by_user = []

user_is_clicking_points = True

while user_is_clicking_points:

    for event in pygame.event.get():
        # TODO: Remove pass.
        #  Fill in this for loop by checking the type's of events you receive from pygame.event.get()
        #  1) If the event is of type pygame.QUIT, then your program should set some variable to false causing your
        #   program to break out of the while loop (HINT: What variable is currently causing your while loop to run infinitely)
        #  2) If the event is of type pygame.MOUSEBUTTONDOWN, we have received a click from the user!
        #   There are two things we need to watch out for when we receive a click from the user:
        #       a) if there are more than one clicks already in the list 'list_of_points_clicked_by_user', this means
        #       that the click we are currently working with could be the click to finish connecting the dots.
        #       If we have enough clicks (more than 1) then we also need to check if the clicks distance is less than
        #       click_distance_threshold away from the first click we received. If this condition is also true we should
        #       set the same variable we set in part 1) to False once again
        #       b) if part 2a) was not true we should simply add the click we are currently working with to list_of_points_clicked_by_user
        pass

    ''' each time we get new events from pygame, there is a chance that we have changed the state of our frame meaning
    some object may have been added, removed, moved, or any other number of things - before updating our frame with 
    these new changes we wipe our canvas clean in a sense by filling our frame with some color before painting our new
    picture of the new changed frame with all of its objects in the right place'''
    frame.fill(white)

    for point in list_of_points_clicked_by_user:
        # TODO: Remove pass. This is where we will draw the points that the user has clicked.
        #  Is there a function that you completed earlier that you could call to help you with this?
        pass

    number_of_points_clicked_by_user = len(list_of_points_clicked_by_user)

    if number_of_points_clicked_by_user >= 2:
        # TODO: Remove pass. This is where the connecting of the dots will actually happen. What you will need to do here is draw
        #  lines (perhaps by calling some function you completed earlier?) from one point in the next. Create a for loop
        #  that will loop over list_of_points_clicked_by_user to do just that.
        pass

    pygame.display.update()

# here we draw a polygon outlined in orange with the now connected shape made up of the points clicked by the user
polygon_rect = pygame.draw.polygon(frame, orange, list_of_points_clicked_by_user, click_distance_threshold)

pygame.display.update()

# this will pause your program for ten seconds to allow you to pause and reflect on the beautiful shape you've connected
time.sleep(10)
