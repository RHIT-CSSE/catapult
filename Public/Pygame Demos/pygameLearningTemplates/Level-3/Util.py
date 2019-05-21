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