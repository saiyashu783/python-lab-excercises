# Write a function ball collides that takes two balls as parameters and
# computes if they are colliding. Your function should return a Boolean
# representing whether the balls are colliding.
# Hint:  Represent a ball on a plane as a tuple of (x, y, r), r being the radius If
# (distance between two balls centers) <= (sum of their radii) then (they are
# colliding)

def is_ball_collides(b1, b2):
    dis = ((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)**0.5
    if dis <= (b1[2] + b2[2]):
        return True
    else:
        return False


ball_1 = (0, 0, 1)
ball_2 = (2, 2, 1)
if is_ball_collides(ball_1, ball_2):
    print("balls collide.")
else:
    print("balls don't collide.")
