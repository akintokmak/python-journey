import turtle as t
import random


t.colormode(255)
t.pensize(2)
t.speed(7) # 0 to 10
def draw_shapes(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        t.forward(100)
        t.right(angle)


for num_sides in range(3,11):
    draw_shapes(num_sides)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)