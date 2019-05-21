#-------------------------
# test if whether point (x, y) is inside the surface of obj
#-------------------------
def pointInside(obj, x, y):
    obj_rect = obj.img.get_rect()
    return obj_rect.collidepoint(x, y)


#-------------------------
# test if whether two objects has collided based on their distance and a threshold
#-------------------------
def hasCollideCirc(a, b, threshold):
    a_rect = a.img.get_rect()
    a_center_x, a_center_y = a.x + a_rect.w, a.y + a_rect.h
    b_rect = b.img.get_rect()
    b_center_x, b_center_y = b.x + b_rect.w, b.y + b_rect.h
    return (a_center_x - b_center_x) ** 2 + (a_center_y - b_center_y) < threshold ** 2

#-------------------------
# test if whether two objects has collided based on their .img surface
#-------------------------
def hasCollideRect(a, b):
    a_rect = a.img.get_rect()
    a_rect = a_rect.move(a.x, a.y)
    b_rect = b.img.get_rect()
    b_rect = b_rect.move(b.x, b.y)
    return a_rect.colliderect(b_rect)


#-------------------------
# let obj bounce in size rectangle (x1, y1) <-> (x2, y2)
    # if (x1, y1) is the left up corner and (x2, y2) is the right botton corner, then bounce inside this rectangle
    # if (x1, y1) is the right bottom corner and (x2, y2) is the left up corner, then bounce outside this rectangle    
#-------------------------
def bounceIn(obj, x1, y1, x2, y2):
    obj_rect = obj.img.get_rect()
    x_left, y_top, x_right, y_bottom = obj.x, obj.y, obj.x + obj_rect.w, obj.y + obj_rect.h
    if x_left < x1:
        obj.vx = abs(obj.vx)
        obj.x = 2*x1 - x_left
    elif x_right > x2:
        obj.vx = - abs(obj.vx)
        obj.x = 2*x2 - x_right - obj_rect.w

    if y_top < y1:
        obj.vy = abs(obj.vy)
        obj.y = 2*y1 - y_top
    elif y_bottom > y2:
        obj.vy = - abs(obj.vy)
        obj.y = 2*y2 - y_bottom - obj_rect.h

#-------------------------
# test if whether two objects has collided based on their .img surface
#-------------------------
def wrapAroundIn(obj, x1, y1, x2, y2):
    obj_rect = obj.img.get_rect()
    x_left, y_top, x_right, y_bottom = obj.x, obj.y, obj.x + obj_rect.w, obj.y + obj_rect.h
    x_offset, y_offset = x2 - x1 + obj_rect.w, y2 - y1 + obj_rect.h
    if x_right < x1:
        obj.x += x_offset
    elif x_left > x2:
        obj.x -= x_offset

    if y_bottom < y1:
        obj.y += y_offset
    elif y_top > y2:
        obj.y -= y_offset
        

#-------------------------
# show the animation on obj.
# animation should just be a list of surface, each represent one frame
# frameNum specifies which frame to show and should be a multiplier of time
# return true if frameNum extends number of frame in the animation
    # in this case, it would just repeat the animation
# return false if frameNum is within number of frame in the animation
#-------------------------
def showAnimationOn(obj, animation, frameNum):
    num_of_frame = len(animation)
    index = int(frameNum) % num_of_frame
    obj.img = animation[index]
    return num_of_frame <= frameNum
