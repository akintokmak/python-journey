# from turtle import Turtle,Screen
# from turtle import * # import everything in module

#alias name
#from turtle as t

# tim  =  Turtle()
#
# def turtle_moving(t_right,t_forward):
#     tim.right(t_right)
#     tim.forward(t_forward)
#
# for _ in range(4):
#     turtle_moving(90,100)
"""---------------------------------------------"""
from turtle import Screen
import turtle as t
import random
tim = t.Turtle()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.right(angle)
        tim.forward(100)

t.colormode(255)
for num_sides in range(3,11):

    draw_shapes(num_sides)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.pencolor(r,g,b)


screen = Screen()
screen.exitonclick()