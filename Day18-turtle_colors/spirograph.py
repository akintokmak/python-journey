import turtle as t
import random


t.colormode(255)
t.pensize(2)
t.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r,g,b)
    return r_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.pencolor(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()