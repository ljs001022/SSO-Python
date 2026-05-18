# import turtle as t

# t.shape("turtle")
# for i in range(5):
#     t.forward(300)
#     t.right(144)
# t.done()
# import turtle as t

# t.shape("turtle")
# for i in range(8):
#     t.forward(300)
#     t.right(135)
# t.done()

import turtle as t
import math

t.shape("turtle")

r=150

def _shape(i,j,k,c):
    t.color(c)
    center_angle = (360 / i) * j
    radian_angle = math.radians(center_angle)
    line_length = 2 * r * math.sin(radian_angle / 2)
    length = round(line_length, 3)
    for a in range(i):
        t.forward(length)
        t.right(k)

_shape(9,2,80,'red')
t.right(20)
_shape(9,3,120,'orange')
t.right(20)
_shape(9,4,160,'green')
t.left(60)
_shape(9,1,40,'blue')

t.done()