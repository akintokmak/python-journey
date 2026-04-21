import turtle as t
import random

t.colormode(255)
directions = [0,90,180,270]
t.pensize(5)
t.speed("fastest")
for _ in range(200):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.pencolor(r,g,b)

    t.forward(30)
    t.setheading(random.choice(directions)) #setheading turns right or left